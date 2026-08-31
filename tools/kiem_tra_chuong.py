# -*- coding: utf-8 -*-
"""
kiem_tra_chuong.py — kiểm tra bản thảo sách PLC theo các bất biến B1–B14.

Thiết kế theo phân loại quy tắc của Vale (existence / occurrence / consistency),
nhưng viết riêng vì sách bằng tiếng Việt — bộ quy tắc văn phong tiếng Anh của
Vale, proselint, alex không áp dụng được.

Dùng:
    python tools/kiem_tra_chuong.py              # kiểm mọi chương
    python tools/kiem_tra_chuong.py 47 48        # kiểm chương chỉ định
    python tools/kiem_tra_chuong.py --json       # xuất JSON cho hook/CI

Mã thoát: 0 nếu không có LỖI; 1 nếu có LỖI (CẢNH BÁO không làm hỏng mã thoát).
"""
import json
import os
import re
import sys
import xml.etree.ElementTree as ET

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(GOC, "docs")
ASSETS = os.path.join(GOC, "assets")
CAUHINH = os.path.join(GOC, "tools", "cau_hinh_kiem_tra.json")

LOI, CANHBAO, TIN = "LỖI", "CẢNH BÁO", "TIN"


class KetQua:
    def __init__(self):
        self.muc = []          # (mức, chương, mã, thông điệp)

    def them(self, muc, chuong, ma, tdiep):
        self.muc.append((muc, chuong, ma, tdiep))

    def loi(self, *a):     self.them(LOI, *a)
    def canh_bao(self, *a): self.them(CANHBAO, *a)
    def tin(self, *a):     self.them(TIN, *a)

    def dem(self, muc):
        return sum(1 for m in self.muc if m[0] == muc)


def doc_cau_hinh():
    with open(CAUHINH, encoding="utf-8") as f:
        return json.load(f)


def tim_chuong():
    """Trả về {số chương: đường dẫn}."""
    ra = {}
    for ten in sorted(os.listdir(DOCS)):
        m = re.match(r"ch(\d{2})_.*\.md$", ten)
        if m:
            ra[int(m.group(1))] = os.path.join(DOCS, ten)
    return ra


def lat_cat_cua(so, cfg):
    for p in cfg["lat_cat"]["pham_vi"]:
        if p["tu"] <= so <= p["den"]:
            return p["lat_cat"], p["ten"]
    return None, None


def bo_code_block(noi_dung):
    """Trả về (văn xuôi, danh sách code block).

    Code block bị thay bằng đúng số dòng trống tương ứng để SỐ DÒNG trong
    văn xuôi luôn khớp số dòng thật của file — nếu xoá hẳn thì mọi vị trí
    báo lỗi đều lệch.
    """
    blocks = re.findall(r"```.*?\n(.*?)```", noi_dung, re.S)
    vanxuoi = re.sub(r"```.*?```",
                     lambda m: "\n" * m.group(0).count("\n"),
                     noi_dung, flags=re.S)
    return vanxuoi, blocks


def dong_cua(van, vi_tri):
    """Số dòng (1-based) chứa vị trí ký tự."""
    return van.count("\n", 0, vi_tri) + 1


def mau_thuat_ngu(t):
    """Biên dịch thuật ngữ thành regex có ranh giới từ.

    Từ viết tắt toàn hoa (STO, PID, MES) phải khớp PHÂN BIỆT HOA-THƯỜNG và
    trọn từ — nếu không, 'STO' sẽ khớp bên trong 'DI_StopPB', tên tín hiệu
    của xy-lanh chặn, vốn hoàn toàn hợp lệ ở lát cắt 1.
    """
    viet_tat = re.fullmatch(r"[A-Z0-9\-]+", t) is not None
    return re.compile(r"(?<![0-9A-Za-z_])%s(?![0-9A-Za-z_])" % re.escape(t),
                      0 if viet_tat else re.I)


# ─────────────────────────────────────────────── các phép kiểm

def kiem_muc_bat_buoc(so, nd, cfg, kq):
    """B12 — chương thiếu mục bắt buộc coi như chưa viết xong."""
    for muc in cfg["muc_bat_buoc"]["chung"]:
        if muc.lower() not in nd.lower():
            kq.loi(so, "B12", "thiếu mục bắt buộc: %s" % muc)
    if so not in cfg["chuong_khong_can_bay"]:
        for muc in cfg["muc_bat_buoc"]["chuong_khai_niem"]:
            if muc.lower() not in nd.lower():
                kq.loi(so, "B12", "thiếu mục bắt buộc: %s" % muc)


def kiem_bay_co_ten(so, nd, cfg, kq):
    """B5 — mỗi bẫy phải là một mục có tên riêng."""
    if so in cfg["chuong_khong_can_bay"]:
        return
    n = len(re.findall(r"###\s*🔍\s*BẪY", nd))
    if n == 0 and "Bẫy thường gặp" in nd:
        kq.canh_bao(so, "B5", "có mục Bẫy thường gặp nhưng không bẫy nào đặt tên theo mẫu '### 🔍 BẪY n — …'")
    elif 0 < n < 3:
        kq.canh_bao(so, "B5", "chỉ có %d bẫy có tên — chương khái niệm thường có 4–8" % n)


def kiem_ten_hang(so, vanxuoi, cfg, kq):
    """B1 — trung lập hãng trong thân sách."""
    for ten in cfg["ten_phan_mem_hang"]["cam"]:
        for m in mau_thuat_ngu(ten).finditer(vanxuoi):
            kq.loi(so, "B1", "tên phần mềm hãng '%s' ở dòng %d"
                   % (ten, dong_cua(vanxuoi, m.start())))


def kiem_lat_cat(so, vanxuoi, cfg, kq):
    """B8 — không dùng thiết bị của lát cắt sau."""
    lc, _ = lat_cat_cua(so, cfg)
    if lc is None or lc == 0:
        return
    for lc_sau, tbi in cfg["lat_cat"]["thiet_bi_theo_lat_cat"].items():
        if int(lc_sau) <= lc:
            continue
        for t in tbi:
            for m in mau_thuat_ngu(t).finditer(vanxuoi):
                dau = vanxuoi.rfind("\n", 0, m.start()) + 1
                cuoi = vanxuoi.find("\n", m.end())
                cau = vanxuoi[dau:cuoi if cuoi > 0 else len(vanxuoi)]
                # dẫn chiếu tiến là hợp lệ: "…sẽ nói ở Chương 37"
                if re.search(r"Chương\s+\d+|Ch\.\s*\d+|Phụ lục", cau):
                    continue
                kq.canh_bao(so, "B8", "lát cắt %d dùng '%s' (lát cắt %s) — dòng %d: %s"
                            % (lc, t, lc_sau, dong_cua(vanxuoi, m.start()),
                               cau.strip()[:70]))


def kiem_song_ngu(so, nd, kq):
    """B11 — thuật ngữ song ngữ."""
    n = len(re.findall(r"\*\([a-zA-Z][^)]{2,60}\)\*", nd))
    if n == 0:
        kq.loi(so, "B11", "không có cặp thuật ngữ song ngữ nào")
    elif n < 4:
        kq.canh_bao(so, "B11", "chỉ %d cặp song ngữ — kiểm xem có khái niệm nào thiếu tiếng Anh không" % n)


def kiem_hinh(so, nd, kq):
    """B13 — hình tồn tại, XML hợp lệ, không dùng marker-end, có chú thích."""
    for m in re.finditer(r"!\[[^\]]*\]\((\.\./assets/[^)]+)\)", nd):
        rel = m.group(1)
        thuc = os.path.normpath(os.path.join(DOCS, rel))
        if not os.path.exists(thuc):
            kq.loi(so, "B13", "hình không tồn tại: %s" % rel)
            continue
        try:
            ET.parse(thuc)
        except Exception as e:
            kq.loi(so, "B13", "hình XML hỏng: %s (%s)" % (rel, e))
            continue
        with open(thuc, encoding="utf-8") as f:
            svg = f.read()
        if "marker-end" in svg:
            kq.canh_bao(so, "B13", "%s dùng marker-end — không render ổn định, vẽ mũi tên bằng đa giác" % rel)
        # chú thích ngay sau hình
        sau = nd[m.end():m.end() + 300]
        if not re.search(r"\*Hình\s+\d+\.\d+\s*—", sau):
            kq.canh_bao(so, "B13", "hình %s thiếu dòng chú thích '*Hình N.k — …*' ngay bên dưới" % rel)


def kiem_tieu_chuan(so, nd, cfg, kq):
    """Tiêu chuẩn nên viện dẫn ở mục Nguồn tham khảo."""
    can = cfg["tieu_chuan_theo_chuong"].get(str(so))
    if not can:
        return
    i = nd.find("Nguồn tham khảo")
    phan = nd[i:] if i >= 0 else ""
    for tc in can:
        if tc.lower() not in phan.lower():
            kq.canh_bao(so, "TC", "chưa viện dẫn tiêu chuẩn nên có: %s" % tc)


def kiem_an_toan(so, nd, cfg, kq):
    """B3b — chương an toàn phải có dòng miễn trừ trách nhiệm."""
    if so not in cfg["chuong_an_toan"]["danh_sach"]:
        return
    for cum in cfg["chuong_an_toan"]["cum_tu_bat_buoc"]:
        if cum.lower() not in nd.lower():
            kq.loi(so, "B3b", "chương an toàn thiếu cụm bắt buộc: '%s'" % cum)
    if not re.search(r"không thay thế|đang chờ chuyên gia", nd, re.I):
        kq.loi(so, "B3b", "chương an toàn thiếu dòng miễn trừ trách nhiệm rõ ràng")


def kiem_code(so, blocks, cfg, kq):
    """B9 — mẫu code đáng ngờ, cần người xem lại."""
    for b in blocks:
        for q in cfg["mau_code_dang_ngo"]["quy_tac"]:
            if re.search(q["regex"], b, re.S | re.I):
                kq.tin(so, q["ma"], q["canh_bao"])


def kiem_tham_chieu(so, nd, ds_chuong, kq):
    """Tham chiếu 'Chương NN' phải trỏ tới chương có trong khung 1–58.

    Bỏ qua tiêu đề và dòng dẫn nhập đầu chương — ở đó chương nhắc số hiệu
    của chính nó là chuyện đương nhiên, không phải lỗi.
    """
    for dong in nd.split("\n"):
        if dong.lstrip().startswith(("#", ">", "|")) or "Lát cắt máy mẫu" in dong:
            continue
        for m in re.finditer(r"Chương\s+(\d+)", dong):
            n = int(m.group(1))
            if n < 1 or n > 58:
                kq.loi(so, "XREF", "tham chiếu Chương %d nằm ngoài khung 1–58" % n)


def kiem_lat_cat_khai_bao(so, nd, cfg, kq):
    """Chương từ 8 trở đi phải khai báo lát cắt ở đầu chương."""
    if so < 8:
        return
    if "Lát cắt máy mẫu" not in nd:
        kq.canh_bao(so, "B8", "thiếu dòng khai báo 'Lát cắt máy mẫu' ở đầu chương")
        return
    lc, _ = lat_cat_cua(so, cfg)
    m = re.search(r"Lát cắt máy mẫu:\*\*\s*(\d)", nd)
    if m and int(m.group(1)) != lc:
        kq.loi(so, "B8", "khai báo lát cắt %s nhưng theo khung phải là %d" % (m.group(1), lc))


# ─────────────────────────────────────────────── chạy

def kiem_mot_chuong(so, duong_dan, cfg, ds_chuong, kq):
    with open(duong_dan, encoding="utf-8") as f:
        nd = f.read()
    vanxuoi, blocks = bo_code_block(nd)

    kiem_muc_bat_buoc(so, nd, cfg, kq)
    kiem_bay_co_ten(so, nd, cfg, kq)
    kiem_ten_hang(so, vanxuoi, cfg, kq)
    kiem_lat_cat_khai_bao(so, nd, cfg, kq)
    kiem_lat_cat(so, vanxuoi, cfg, kq)
    kiem_song_ngu(so, nd, kq)
    kiem_hinh(so, nd, kq)
    kiem_tieu_chuan(so, nd, cfg, kq)
    kiem_an_toan(so, nd, cfg, kq)
    kiem_code(so, blocks, cfg, kq)
    kiem_tham_chieu(so, nd, ds_chuong, kq)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    xuat_json = "--json" in sys.argv
    cfg = doc_cau_hinh()
    ds = tim_chuong()
    if args:
        chon = {int(a): ds[int(a)] for a in args if int(a) in ds}
    else:
        chon = ds

    kq = KetQua()
    for so in sorted(chon):
        kiem_mot_chuong(so, chon[so], cfg, ds, kq)

    if xuat_json:
        print(json.dumps([{"muc": m, "chuong": c, "ma": k, "thong_diep": t}
                          for m, c, k, t in kq.muc], ensure_ascii=False, indent=1))
    else:
        dong = []
        dong.append("=" * 78)
        dong.append("KIỂM TRA BẢN THẢO — %d chương" % len(chon))
        dong.append("=" * 78)
        hien = None
        for m, c, k, t in sorted(kq.muc, key=lambda x: (x[1], {LOI: 0, CANHBAO: 1, TIN: 2}[x[0]])):
            if c != hien:
                dong.append("")
                dong.append("── Chương %d ──" % c)
                hien = c
            dong.append("  [%-8s] %-5s %s" % (m, k, t))
        dong.append("")
        dong.append("-" * 78)
        dong.append("TỔNG:  %d LỖI  ·  %d CẢNH BÁO  ·  %d TIN"
                    % (kq.dem(LOI), kq.dem(CANHBAO), kq.dem(TIN)))
        dong.append("-" * 78)
        out = "\n".join(dong)
        # tránh lỗi codec console trên Windows
        try:
            print(out)
        except UnicodeEncodeError:
            sys.stdout.buffer.write(out.encode("utf-8", "replace"))

    return 1 if kq.dem(LOI) else 0


if __name__ == "__main__":
    sys.exit(main())
