# -*- coding: utf-8 -*-
"""
kiem_nhat_quan.py — kiểm TRÔI DẠT (drift) giữa các tài liệu của bộ sách.

kiem_tra_chuong.py kiểm TỪNG chương có đúng khung không.
File này kiểm các chương có KHỚP NHAU không — thứ mà kiểm từng file không thấy.

Bắt khái niệm "documentation drift": khi một tài liệu đổi, các tài liệu trỏ tới nó
vẫn giữ nội dung cũ và không ai biết.

(Ghi chú nguồn: bản đầu của file này ghi ý tưởng lấy từ prodigy. Đã tra tài liệu
prodigy 2026-09-02 — nó KHÔNG có tính năng phát hiện drift, chỉ có orchestration
chung. Sửa lại cho đúng: công cụ này viết riêng cho bộ sách, không phỏng theo
công cụ nào.)

Sáu nhóm kiểm:
  XREF  dẫn chiếu tới mục / chương / phụ lục KHÔNG tồn tại  → LỖI
  XRTX  dẫn chiếu tới mục có tồn tại nhưng SAI CHỦ ĐỀ       → CẢNH BÁO
  TAG   tên tag không có trong bảng I/O chính thức (J.2)    → LỖI
  SO    số liệu chốt bị viết khác nhau giữa các chương      → LỖI
  TC    mã tiêu chuẩn sai chính tả / không có trong danh mục→ CẢNH BÁO
  TN    thuật ngữ Việt–Anh dùng không nhất quán             → TIN
  GLOS  Phụ lục F dẫn số chương mà chương đó KHÔNG dạy      → CẢNH BÁO

Dùng:
    python tools/kiem_nhat_quan.py                # kiểm toàn bộ
    python tools/kiem_nhat_quan.py --chi XREF,TAG # chỉ vài nhóm
    python tools/kiem_nhat_quan.py --json         # xuất JSON cho hook/CI

Mã thoát: 0 nếu không có LỖI; 1 nếu có LỖI.
"""
import json
import os
import re
import sys
from collections import defaultdict

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(GOC, "docs")
CAUHINH = os.path.join(GOC, "tools", "cau_hinh_nhat_quan.json")

LOI, CANHBAO, TIN = "LỖI", "CẢNH BÁO", "TIN"


class KetQua:
    def __init__(self):
        self.muc = []

    def them(self, muc, ma, tep, dong, tdiep):
        self.muc.append((muc, ma, tep, dong, tdiep))

    def loi(self, *a):      self.them(LOI, *a)
    def canh_bao(self, *a): self.them(CANHBAO, *a)
    def tin(self, *a):      self.them(TIN, *a)

    def dem(self, muc):
        return sum(1 for m in self.muc if m[0] == muc)


# ---------------------------------------------------------------- nạp tài liệu

def khoa_tai_lieu(ten_tep):
    """ch49_... -> '49'   |   pl_a1_... -> 'A1'   |   pl_j_... -> 'J'"""
    m = re.match(r"ch(\d{2})_", ten_tep)
    if m:
        return str(int(m.group(1)))
    m = re.match(r"pl_([a-z]\d?)_", ten_tep)
    if m:
        return m.group(1).upper()
    return None


def bo_code_block(noi_dung):
    """Thay code block bằng số dòng trống tương ứng để SỐ DÒNG khớp file thật."""
    return re.sub(r"```.*?```",
                  lambda m: "\n" * m.group(0).count("\n"),
                  noi_dung, flags=re.S)


def nap_tai_lieu(cfg):
    """Trả về {khoa: {'tep','duong_dan','tho','van','tieu_de','muc'}}."""
    ra = {}
    for ten in sorted(os.listdir(DOCS)):
        if not ten.endswith(".md") or ten in cfg["bo_qua_file"]:
            continue
        khoa = khoa_tai_lieu(ten)
        if khoa is None:
            continue
        duong_dan = os.path.join(DOCS, ten)
        with open(duong_dan, encoding="utf-8") as f:
            tho = f.read()
        van = bo_code_block(tho)
        # mục: '## 49.3 Tiêu đề'  |  '### J.2.1 Tiêu đề'
        muc = {}
        for m in re.finditer(r"^#{2,4}\s+([A-Z]{0,2}\d*(?:\.\d+)+)\s+(.*)$", van, re.M):
            muc[m.group(1)] = m.group(2).strip()
        tieu_de = ""
        m = re.search(r"^#\s+(.*)$", van, re.M)
        if m:
            tieu_de = m.group(1).strip()
        ra[khoa] = {"tep": ten, "duong_dan": duong_dan, "tho": tho,
                    "van": van, "tieu_de": tieu_de, "muc": muc}
    return ra


def so_dong(van, vi_tri):
    return van.count("\n", 0, vi_tri) + 1


# ------------------------------------------------------------------ XREF drift

def chuan_hoa_muc(khoa_dich, so_muc):
    """'7.1' trong ngữ cảnh phụ lục J -> thử cả '7.1' và 'J.7.1'."""
    ung_vien = [so_muc]
    if not re.match(r"^[A-Z]", so_muc) and re.match(r"^[A-Z]", khoa_dich):
        ung_vien.append("%s.%s" % (khoa_dich, so_muc))
    return ung_vien


def kiem_xref(tl, cfg, kq):
    """Mọi dẫn chiếu phải trỏ tới mục/chương/phụ lục có thật."""
    nhom = cfg.get("bi_danh_nhom", {})
    # 'Phụ lục J §J.4'  |  'Phụ lục J §7.1'  |  'Phụ lục A2 §A2.8'
    mau_pl_muc = re.compile(r"Phụ lục ([A-Z]\d?)\s*§\s*([A-Z]{0,2}\d*(?:\.\d+)*)")
    # 'Phụ lục J' đứng một mình
    mau_pl = re.compile(r"Phụ lục ([A-Z]\d?)(?![\w.])")
    # 'Chương 49 mục 49.7'  |  'Ch.49 mục 49.7'
    mau_ch_muc = re.compile(r"(?:Chương|Ch\.)\s*(\d{1,2}),?\s*mục\s+(\d{1,2}\.\d+)")
    # 'mục 49.7' đứng một mình (chương suy từ phần trước dấu chấm)
    mau_muc = re.compile(r"(?<!Ch\.)(?<!Chương )mục\s+(\d{1,2}\.\d+)")
    # 'Chương 49' | 'Ch.49'
    mau_ch = re.compile(r"(?:Chương|Ch\.)\s*(\d{1,3})(?![\d.])")

    for khoa, d in sorted(tl.items(), key=lambda x: sap_xep_khoa(x[0])):
        van = d["van"]

        for m in mau_pl_muc.finditer(van):
            dich, so_muc = m.group(1), m.group(2)
            ln = so_dong(van, m.start())
            if dich in nhom:
                continue                     # bí danh nhóm: mục nằm ở A1 hoặc A2
            if dich not in tl:
                kq.loi("XREF", d["tep"], ln,
                       "dẫn tới Phụ lục %s — phụ lục này KHÔNG tồn tại" % dich)
                continue
            ung_vien = chuan_hoa_muc(dich, so_muc)
            if not any(u in tl[dich]["muc"] for u in ung_vien):
                co = ", ".join(sorted(tl[dich]["muc"], key=sap_xep_muc)[:6])
                kq.loi("XREF", d["tep"], ln,
                       "dẫn tới 'Phụ lục %s §%s' — mục KHÔNG tồn tại (phụ lục %s có: %s …)"
                       % (dich, so_muc, dich, co))

        for m in mau_pl.finditer(van):
            dich = m.group(1)
            if dich in tl or dich in nhom:
                continue
            kq.loi("XREF", d["tep"], so_dong(van, m.start()),
                   "dẫn tới Phụ lục %s — KHÔNG tồn tại" % dich)

        for m in mau_ch_muc.finditer(van):
            ch, so_muc = m.group(1), m.group(2)
            ln = so_dong(van, m.start())
            if str(int(ch)) not in tl:
                kq.loi("XREF", d["tep"], ln, "dẫn tới Chương %s — KHÔNG tồn tại" % ch)
            elif so_muc not in tl[str(int(ch))]["muc"]:
                kq.loi("XREF", d["tep"], ln,
                       "dẫn tới 'Chương %s mục %s' — mục KHÔNG tồn tại" % (ch, so_muc))
            elif so_muc.split(".")[0] != str(int(ch)):
                kq.canh_bao("XREF", d["tep"], ln,
                            "'Chương %s mục %s' — số mục không thuộc chương đó" % (ch, so_muc))

        for m in mau_muc.finditer(van):
            so_muc = m.group(1)
            ch = so_muc.split(".")[0]
            ln = so_dong(van, m.start())
            if ch not in tl:
                continue                      # có thể là mục của phụ lục, bỏ qua
            if so_muc not in tl[ch]["muc"]:
                kq.loi("XREF", d["tep"], ln,
                       "dẫn tới 'mục %s' — mục KHÔNG tồn tại trong Chương %s" % (so_muc, ch))

        for m in mau_ch.finditer(van):
            ch = m.group(1)
            if int(ch) > 58 or int(ch) < 1:
                kq.loi("XREF", d["tep"], so_dong(van, m.start()),
                       "dẫn tới Chương %s — ngoài phạm vi 1–58" % ch)


def kiem_xref_chu_de(tl, cfg, kq):
    """Dẫn chiếu trỏ đúng mục tồn tại, nhưng tiêu đề mục không liên quan nội dung dẫn.

    Chỉ bắt trường hợp rõ ràng: câu dẫn nhắc tới một từ khoá mà tiêu đề mục đích
    không chứa và cũng không chứa từ khoá gần nghĩa nào. Mức CẢNH BÁO vì có thể
    sai dương — người đọc kết quả phải tự xác nhận.
    """
    tu_khoa = {
        "số liệu": ["số liệu", "chốt", "máy làm gì"],
        "bảng I/O": ["vào/ra", "I/O"],
        "trình tự": ["trình tự", "đặc tả"],
        "an toàn": ["an toàn"],
        "công thức": ["công thức"],
    }
    mau = re.compile(r"([^.\n]{0,60}?)\(?(?:Phụ lục ([A-Z]\d?)\s*§\s*([A-Z]{0,2}\d*(?:\.\d+)*))\)?")
    for khoa, d in sorted(tl.items(), key=lambda x: sap_xep_khoa(x[0])):
        for m in mau.finditer(d["van"]):
            truoc, dich, so_muc = m.group(1), m.group(2), m.group(3)
            if dich not in tl:
                continue
            ung_vien = [u for u in chuan_hoa_muc(dich, so_muc) if u in tl[dich]["muc"]]
            if not ung_vien:
                continue
            tieu_de_dich = tl[dich]["muc"][ung_vien[0]].lower()
            for tk, gan_nghia in tu_khoa.items():
                if tk.lower() in truoc.lower():
                    if not any(g.lower() in tieu_de_dich for g in gan_nghia):
                        kq.canh_bao("XRTX", d["tep"], so_dong(d["van"], m.start()),
                                    "dẫn '%s' → Phụ lục %s §%s có tiêu đề '%s' — kiểm xem có đúng mục không"
                                    % (tk, dich, so_muc, tl[dich]["muc"][ung_vien[0]]))
                    break


# ------------------------------------------------------------------- TAG drift

def kiem_tag(tl, cfg, kq):
    """Mọi tag dùng trong sách phải có trong bảng I/O chính thức (Phụ lục J)."""
    khoa_nguon = khoa_tai_lieu(cfg["file_nguon_tag"])
    if khoa_nguon not in tl:
        kq.canh_bao("TAG", cfg["file_nguon_tag"], 0, "không tìm thấy file nguồn bảng I/O")
        return
    tien_to = "|".join(cfg["tien_to_tag"])
    mau_tag = re.compile(r"\b((?:%s)_[A-Za-z0-9]+)" % tien_to)

    chinh_thuc = set(mau_tag.findall(tl[khoa_nguon]["tho"]))
    chinh_thuc |= set(cfg.get("tag_vi_du_chung", {}))
    if not chinh_thuc:
        kq.canh_bao("TAG", cfg["file_nguon_tag"], 0, "không trích được tag nào từ file nguồn")
        return

    for khoa, d in sorted(tl.items(), key=lambda x: sap_xep_khoa(x[0])):
        if khoa == khoa_nguon:
            continue
        thay = defaultdict(list)
        for m in mau_tag.finditer(d["tho"]):
            if m.group(1) not in chinh_thuc:
                thay[m.group(1)].append(d["tho"].count("\n", 0, m.start()) + 1)
        for tag, dong in sorted(thay.items()):
            kq.loi("TAG", d["tep"], dong[0],
                   "tag `%s` không có trong bảng I/O chính thức (Phụ lục J mục J.2)%s"
                   % (tag, "" if len(dong) == 1 else " — còn %d chỗ nữa" % (len(dong) - 1)))


# -------------------------------------------------------------------- SO drift

def kiem_so_lieu(tl, cfg, kq):
    """Số liệu chốt của máy mẫu phải viết giống nhau ở mọi chương."""
    for ten, quy in cfg["so_lieu_chot"].items():
        mau = re.compile(quy["mau"])
        dung = set(quy["dung"])
        for khoa, d in sorted(tl.items(), key=lambda x: sap_xep_khoa(x[0])):
            for m in mau.finditer(d["van"]):
                if "chi_khi_co" in quy:
                    canh = d["van"][max(0, m.start() - 80): m.end() + 40]
                    if quy["chi_khi_co"].lower() not in canh.lower():
                        continue
                gia_tri = "×".join(g for g in m.groups() if g) if len(m.groups()) > 1 \
                    else (m.group(1) or "")
                gon = gia_tri.replace(" ", "")
                if gia_tri not in dung and gon not in {x.replace(" ", "") for x in dung}:
                    kq.loi("SO", d["tep"], so_dong(d["van"], m.start()),
                           "%s = '%s' — số liệu chốt là %s (Phụ lục J)"
                           % (quy["mo_ta"], gia_tri, " hoặc ".join(sorted(dung))))


# -------------------------------------------------------------------- TC drift

def kiem_tieu_chuan(tl, cfg, kq):
    """Mã tiêu chuẩn phải nằm trong danh mục đã đăng ký, và không dùng mã bị cấm."""
    hop_le = set(cfg["tieu_chuan_hop_le"])
    cam = cfg["tieu_chuan_cam"]
    mau = re.compile(r"\b((?:IEC|ISO)(?:/[A-Z]+)? \d{4,5}(?:-\d+(?:-\d+)?)?)")
    thu_hoi = cfg.get("tieu_chuan_thu_hoi", {})
    for khoa, d in sorted(tl.items(), key=lambda x: sap_xep_khoa(x[0])):
        thay = defaultdict(list)
        for m in mau.finditer(d["van"]):
            thay[m.group(1)].append(so_dong(d["van"], m.start()))
        for ma, dong in sorted(thay.items()):
            if ma in thu_hoi:
                quy = thu_hoi[ma]
                for ln in dong:
                    canh = " ".join(d["van"].splitlines()[max(0, ln - 3): ln + 4])
                    if not any(g.lower() in canh.lower() for g in quy["phai_co_gan"]):
                        kq.loi("TC", d["tep"], ln,
                               "%s ĐÃ BỊ THU HỒI (thay bằng %s) mà không có cảnh báo kèm — %s"
                               % (ma, quy["thay_bang"], quy["ghi_chu"]))
                continue
            if ma in cam:
                kq.loi("TC", d["tep"], dong[0], "dùng %s — %s" % (ma, cam[ma]))
            elif ma not in hop_le:
                goc = ma.rsplit("-", 1)[0]
                if goc in hop_le:
                    continue          # 'IEC 61131' khi danh mục có 'IEC 61131-3'
                kq.canh_bao("TC", d["tep"], dong[0],
                            "mã tiêu chuẩn '%s' không có trong danh mục — kiểm chính tả, "
                            "hoặc thêm vào cau_hinh_nhat_quan.json nếu đúng" % ma)


# -------------------------------------------------------------------- TN drift

def kiem_thuat_ngu(tl, cfg, kq):
    """Cùng một thuật ngữ tiếng Anh không nên gán cho hai cụm tiếng Việt khác nhau."""
    khoa_f = khoa_tai_lieu(cfg["file_nguon_thuat_ngu"])
    if khoa_f not in tl:
        return
    mau = re.compile(r"([A-Za-zÀ-ỹ][A-Za-zÀ-ỹ\s·]{2,40}?)\s*\*\(([a-z][a-z\s\-]{2,40})\)\*")
    anh_to_viet = defaultdict(set)
    for khoa, d in sorted(tl.items(), key=lambda x: sap_xep_khoa(x[0])):
        for m in mau.finditer(d["van"]):
            viet = m.group(1).strip().strip("*_ ").lower()
            anh = m.group(2).strip().lower()
            viet = re.sub(r"^(?:là|và|của|một|các|bằng|theo|với|cho)\s+", "", viet)
            viet = viet.split("—")[-1].strip()
            if 2 < len(viet) < 40:
                anh_to_viet[anh].add(viet)
    for anh, tap in sorted(anh_to_viet.items()):
        if len(tap) > 1:
            kq.tin("TN", cfg["file_nguon_thuat_ngu"], 0,
                   "'%s' được dịch %d cách: %s — thống nhất lại nếu cùng nghĩa"
                   % (anh, len(tap), " | ".join(sorted(tap))))


# ------------------------------------------------------------------- GLOS drift

def kiem_glossary(tl, cfg, kq):
    """Phụ lục F dẫn số chương cho mỗi thuật ngữ — chương đó có thật sự dạy nó không?

    Bắt được lớp lỗi mà XREF bỏ sót: số chương nằm trong Ô BẢNG, không theo mẫu
    "Chương N", nên dẫn sai vẫn hợp lệ về cú pháp.

    Cách kiểm: lấy thuật ngữ tiếng Anh (đặc trưng hơn tiếng Việt), đếm số lần xuất
    hiện ở mọi chương. Nếu chương được dẫn KHÔNG nằm trong nhóm dẫn đầu → CẢNH BÁO.
    ⚠ Có thể sai dương — người đọc kết quả phải tự xác nhận.
    """
    khoa_f = khoa_tai_lieu(cfg.get("file_nguon_thuat_ngu", ""))
    if khoa_f not in tl:
        return
    bo_qua = {"safety", "control", "time", "value", "error", "system", "data",
              "input", "output", "signal", "mode", "step", "state", "test"}
    for line in tl[khoa_f]["van"].splitlines():
        if not line.startswith("| ") or line.startswith("|---"):
            continue
        cot = [x.strip() for x in line.strip("|").split("|")]
        if len(cot) < 4:
            continue
        viet, anh, so = cot[0], cot[1], cot[-1]
        if not re.fullmatch(r"[\d,\s·]+", so) or not so.strip():
            continue
        nums = [n for n in re.split(r"[,\s·]+", so) if n.isdigit()]
        if not nums:
            continue
        keys = [k.strip().lower() for k in re.split(r"[·(),]", anh) if len(k.strip()) > 4]
        keys = [k for k in keys if k not in bo_qua]
        if not keys:
            continue
        diem = {}
        for n, d in tl.items():
            if not n.isdigit():
                continue
            diem[n] = sum(d["van"].lower().count(k) for k in keys)
        if not any(diem.values()):
            continue
        dan_dau = sorted(diem, key=lambda n: (-diem[n], int(n)))[:3]
        dan_dau = [n for n in dan_dau if diem[n] > 0]
        if any(n in dan_dau for n in nums):
            continue
        ten = re.sub(r"[⭐⚠*`]", "", viet).strip()[:34]
        if ten in cfg.get("glossary_da_duyet", []):
            continue                      # đã rà tay, xác nhận đúng
        goi_y = ", ".join("Ch.%s(%d)" % (n, diem[n]) for n in dan_dau)
        kq.canh_bao("GLOS", tl[khoa_f]["tep"], 0,
                    "'%s' dẫn Chương %s nhưng thuật ngữ tập trung ở %s — kiểm lại"
                    % (ten, so, goi_y))


# --------------------------------------------------------------------- tiện ích

def sap_xep_khoa(k):
    return (0, int(k), "") if k.isdigit() else (1, 0, k)


def sap_xep_muc(m):
    try:
        return tuple(int(x) for x in re.sub(r"^[A-Z]+", "", m).split(".") if x)
    except ValueError:
        return (99,)


NHOM = {
    "XREF": kiem_xref,
    "XRTX": None,          # cần cfg, gọi riêng
    "TAG": None,
    "SO": None,
    "TC": None,
    "TN": None,
    "GLOS": None,
}


def main():
    chon = None
    for a in sys.argv[1:]:
        if a.startswith("--chi"):
            chon = set(a.split("=", 1)[1].split(",")) if "=" in a else None
    if chon is None and "--chi" in sys.argv:
        i = sys.argv.index("--chi")
        if i + 1 < len(sys.argv):
            chon = set(sys.argv[i + 1].split(","))

    with open(CAUHINH, encoding="utf-8") as f:
        cfg = json.load(f)
    tl = nap_tai_lieu(cfg)
    kq = KetQua()

    def chay(ma):
        return chon is None or ma in chon

    if chay("XREF"):
        kiem_xref(tl, cfg, kq)
    if chay("XRTX"):
        kiem_xref_chu_de(tl, cfg, kq)
    if chay("TAG"):
        kiem_tag(tl, cfg, kq)
    if chay("SO"):
        kiem_so_lieu(tl, cfg, kq)
    if chay("TC"):
        kiem_tieu_chuan(tl, cfg, kq)
    if chay("TN"):
        kiem_thuat_ngu(tl, cfg, kq)
    if chay("GLOS"):
        kiem_glossary(tl, cfg, kq)

    if "--json" in sys.argv:
        out = json.dumps([{"muc": m, "ma": k, "tep": t, "dong": d, "thong_diep": s}
                          for m, k, t, d, s in kq.muc], ensure_ascii=False, indent=1)
    else:
        dong = ["=" * 78,
                "KIỂM TRÔI DẠT GIỮA TÀI LIỆU — %d file" % len(tl),
                "=" * 78]
        hien = None
        for m, k, t, ln, s in sorted(kq.muc,
                                     key=lambda x: (x[2], {LOI: 0, CANHBAO: 1, TIN: 2}[x[0]], x[3])):
            if t != hien:
                dong += ["", "── %s ──" % t]
                hien = t
            dong.append("  [%-8s] %-5s dòng %-5s %s" % (m, k, ln, s))
        dong += ["", "-" * 78,
                 "TỔNG:  %d LỖI  ·  %d CẢNH BÁO  ·  %d TIN"
                 % (kq.dem(LOI), kq.dem(CANHBAO), kq.dem(TIN)),
                 "-" * 78]
        out = "\n".join(dong)

    try:
        print(out)
    except UnicodeEncodeError:
        sys.stdout.buffer.write(out.encode("utf-8", "replace"))

    return 1 if kq.dem(LOI) else 0


if __name__ == "__main__":
    sys.exit(main())
