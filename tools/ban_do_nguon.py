# -*- coding: utf-8 -*-
"""Lập bản đồ NGUỒN <-> CHƯƠNG, và chỉ ra chỗ chưa ai đọc tới.

Bài toán: bộ tài liệu nguồn có hàng chục nghìn trang. Khi viết và đối chiếu,
người viết chỉ tra những gì mình NGHĨ RA để tra — nên tài liệu có thể phủ một
chủ đề mà không ai biết, và chương liên quan vẫn thiếu.

Công cụ này ghép ba nguồn dữ liệu:
  1. `chi_muc_nguon.json`  — có những tài liệu nào, cấu trúc mục lục ra sao
  2. mục "Nguồn tham khảo chương N" trong từng chương — chương dẫn nguồn nào
  3. `docs/00d_Nhat_ky_doi_chieu.md` — nguồn nào đã thực sự được đối chiếu

và trả lời câu hỏi quan trọng nhất:
  tài liệu nào trong bộ CHƯA ĐƯỢC CHƯƠNG NÀO DẪN?

Dùng:
    python tools/ban_do_nguon.py          # ghi docs/00e_Ban_do_nguon.md
    python tools/ban_do_nguon.py --kiem   # chỉ in tóm tắt, không ghi tệp
"""
import io
import json
import os
import re
import sys
import glob
import collections

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHI_MUC = os.path.join(GOC, "tools", "chi_muc_nguon.json")
CAU_HINH = os.path.join(GOC, "tools", "cau_hinh_ban_do.json")
TAI_LIEU = os.path.join(GOC, "docs")
DICH = os.path.join(TAI_LIEU, "00e_Ban_do_nguon.md")
NHAT_KY = os.path.join(TAI_LIEU, "00d_Nhat_ky_doi_chieu.md")

MAU_TIEU_DE = re.compile(r"^### Nguồn tham khảo (?:chương|Phụ lục) ([\w\d]+)\s*$", re.M)
MAU_GACH_DAU = re.compile(r"^- (.+)$", re.M)


def xp(s):
    """In an toàn trên console mã hoá hẹp (gbk)."""
    try:
        print(s)
    except UnicodeEncodeError:
        print(s.encode("ascii", "replace").decode("ascii"))


def nap_json(duong):
    with io.open(duong, encoding="utf-8") as f:
        return json.load(f)


def ten_chuong(duong):
    """'docs/ch18_....md' -> '18';  'docs/pl_a1_....md' -> 'A1'."""
    ten = os.path.basename(duong)
    m = re.match(r"ch(\d+)_", ten)
    if m:
        return str(int(m.group(1)))
    m = re.match(r"pl_([a-z]\d?)_", ten)
    if m:
        return m.group(1).upper()
    return ten


def sap_xep_khoa(k):
    return (0, int(k)) if k.isdigit() else (1, k)


def co_tu_khoa(ten_thap, nhan):
    """Khớp thô: một từ đặc trưng (>=5 ký tự) của nhãn có trong tên nguồn."""
    for tu in re.split(r"[^\wÀ-ỹ]+", nhan.lower()):
        if len(tu) >= 5 and tu in ten_thap:
            return True
    return False


def doc_nguon_cac_chuong():
    """Trả về {khoá chương: [tên nguồn được dẫn]}."""
    kq = {}
    tep = sorted(glob.glob(os.path.join(TAI_LIEU, "ch*.md"))) + sorted(
        glob.glob(os.path.join(TAI_LIEU, "pl_*.md"))
    )
    for p in tep:
        s = io.open(p, encoding="utf-8").read()
        m = MAU_TIEU_DE.search(s)
        if not m:
            continue
        khoi = s[m.end():].split("\n\n---")[0]
        ds = []
        for dong in MAU_GACH_DAU.findall(khoi):
            dong = dong.strip()
            mm = re.match(r"\*\*(.+?)\*\*", dong)
            ten = mm.group(1) if mm else dong.split("—")[0].strip()
            ds.append(re.sub(r"\s+", " ", ten)[:120])
        kq[ten_chuong(p)] = ds
    return kq


def main():
    chi_kiem = "--kiem" in sys.argv
    if not os.path.exists(CHI_MUC):
        xp("Chua co chi muc. Chay truoc: python tools/lap_chi_muc_nguon.py")
        return 1

    chi_muc = nap_json(CHI_MUC)
    cfg = nap_json(CAU_HINH)
    bi_danh = cfg["bi_danh_tep"]
    mau_ngoai = [re.compile(x) for x in cfg["nguon_ngoai_bo_tai_lieu"]]

    nhan_to_tep = collections.OrderedDict()
    da_gan = set()
    for nhan, manh in bi_danh.items():
        khop = [k for k in chi_muc if any(m.lower() in k.lower() for m in manh)]
        nhan_to_tep[nhan] = sorted(khop)
        da_gan.update(khop)
    tep_khong_nhan = sorted(k for k in chi_muc if k not in da_gan)

    nguon_chuong = doc_nguon_cac_chuong()
    nhan_duoc_dan = collections.defaultdict(list)
    ngoai_bo = collections.Counter()
    khong_khop = collections.Counter()
    for ch, ds in sorted(nguon_chuong.items(), key=lambda x: sap_xep_khoa(x[0])):
        for ten in ds:
            if any(m.search(ten) for m in mau_ngoai):
                ngoai_bo[ten[:60]] += 1
                continue
            trung = [n for n in bi_danh if co_tu_khoa(ten.lower(), n)]
            if trung:
                for n in trung:
                    if ch not in nhan_duoc_dan[n]:
                        nhan_duoc_dan[n].append(ch)
            else:
                khong_khop[ten[:60]] += 1

    nk = io.open(NHAT_KY, encoding="utf-8").read() if os.path.exists(NHAT_KY) else ""
    nhan_trong_nk = set()
    for n in bi_danh:
        dau = n.split("—")[0].strip().lower()
        if (dau and dau in nk.lower()) or co_tu_khoa(nk.lower(), n):
            nhan_trong_nk.add(n)

    chua_dan = [n for n, t in nhan_to_tep.items() if t and not nhan_duoc_dan.get(n)]
    tong_tr_chua = sum(chi_muc[t]["so_trang"] for n in chua_dan for t in nhan_to_tep[n])

    xp("Bo tai lieu       : %d tep - %d trang"
       % (len(chi_muc), sum(v["so_trang"] for v in chi_muc.values())))
    xp("Nhan da gan       : %d nhan (%d tep)"
       % (sum(1 for v in nhan_to_tep.values() if v), len(da_gan)))
    xp("Tep chua gan nhan : %d" % len(tep_khong_nhan))
    xp("CHUA CHUONG NAO DAN: %d nhan (~%d trang)" % (len(chua_dan), tong_tr_chua))
    for n in chua_dan:
        xp("   ! %s" % n)
    xp("Ten nguon khong khop nhan : %d" % len(khong_khop))

    if chi_kiem:
        return 0

    ghi_bao_cao(chi_muc, nhan_to_tep, nhan_duoc_dan, nhan_trong_nk,
                tep_khong_nhan, ngoai_bo, khong_khop)
    xp("Da ghi: %s" % os.path.relpath(DICH, GOC))
    return 0


def ghi_bao_cao(chi_muc, nhan_to_tep, nhan_duoc_dan, nhan_trong_nk,
                tep_khong_nhan, ngoai_bo, khong_khop):
    d = []
    A = d.append
    tong_tr = sum(v["so_trang"] for v in chi_muc.values())
    tong_muc = sum(len(v["muc_luc"]) for v in chi_muc.values())
    khong_trich = [k for k, v in chi_muc.items() if not v.get("trich_duoc")]

    A("# Bản đồ nguồn và chương")
    A("")
    A("> ⭐⭐ **Mục đích:** bộ tài liệu nguồn quá lớn để đọc hết. Người viết chỉ tra những gì mình")
    A("> **nghĩ ra để tra** — nên tài liệu có thể phủ một chủ đề mà không ai biết, và chương liên")
    A("> quan vẫn thiếu. Bảng này trả lời câu hỏi ⚠ **tài liệu nào chưa được chương nào dẫn.**")
    A(">")
    A("> ⚠ Tệp này **sinh tự động** — đừng sửa tay. Cập nhật bằng:")
    A("> `python tools/lap_chi_muc_nguon.py` rồi `python tools/ban_do_nguon.py`")
    A("")
    A("---")
    A("")
    A("## 1. Quy mô bộ tài liệu")
    A("")
    A("| Chỉ số | Giá trị |")
    A("|---|---|")
    A("| Tài liệu PDF | **%d** |" % len(chi_muc))
    A("| Tổng số trang | **%s** |" % f"{tong_tr:,}".replace(",", " "))
    A("| Mục lục nhúng đọc được | **%s mục** trên %d tài liệu |"
      % (f"{tong_muc:,}".replace(",", " "),
         sum(1 for v in chi_muc.values() if v["co_bookmark"])))
    A("| ⚠ Không trích được text | **%d** |" % len(khong_trich))
    A("")
    if khong_trich:
        A("> ⚠⚠ **Tài liệu không trích được text — coi như KHÔNG CÓ cho tới khi OCR.**")
        A(">")
        for k in khong_trich:
            A("> - `%s` — %d trang" % (k, chi_muc[k]["so_trang"]))
        A("")
    A("---")
    A("")
    A("## 2. ⚠⚠ Nguồn CHƯA được chương nào dẫn")
    A("")
    A("⭐ Đây là phần quan trọng nhất của tệp này. Mỗi dòng là tài liệu **đang có trong tay** mà")
    A("**không chương nào dẫn** — nghĩa là hoặc nó thật sự không liên quan, hoặc ⚠ **có nội dung**")
    A("**bị bỏ sót**. Cột cuối cho biết nhật ký đối chiếu đã từng nhắc tới nó chưa.")
    A("")
    chua = [(n, t) for n, t in nhan_to_tep.items() if t and not nhan_duoc_dan.get(n)]
    if not chua:
        A("✅ Không còn nguồn nào chưa được dẫn.")
    else:
        A("| Nguồn | Trang | Mục lục | Nhật ký đã nhắc? |")
        A("|---|--:|--:|:--:|")
        for n, tep in sorted(chua, key=lambda x: -sum(chi_muc[t]["so_trang"] for t in x[1])):
            tr = sum(chi_muc[t]["so_trang"] for t in tep)
            mc = sum(len(chi_muc[t]["muc_luc"]) for t in tep)
            nk = "✔" if n in nhan_trong_nk else "⚠ **chưa**"
            A("| %s | %d | %d | %s |" % (n, tr, mc, nk))
    A("")
    A("---")
    A("")
    A("## 3. Nguồn đã được dẫn — dẫn ở chương nào")
    A("")
    A("| Nguồn | Trang | Chương dẫn |")
    A("|---|--:|---|")
    for n, tep in nhan_to_tep.items():
        if not tep or not nhan_duoc_dan.get(n):
            continue
        tr = sum(chi_muc[t]["so_trang"] for t in tep)
        chs = sorted(nhan_duoc_dan[n], key=sap_xep_khoa)
        A("| %s | %d | %s |" % (n, tr, ", ".join(chs)))
    A("")
    A("---")
    A("")
    A("## 4. Tệp trong bộ chưa gán nhãn")
    A("")
    A("⭐ Các tệp này chưa có bí danh trong `tools/cau_hinh_ban_do.json`, nên **không được theo dõi**.")
    A("Bổ sung bí danh nếu tài liệu có giá trị; bỏ qua nếu không.")
    A("")
    if not tep_khong_nhan:
        A("✅ Mọi tệp đã được gán nhãn.")
    else:
        A("| Tệp | Trang |")
        A("|---|--:|")
        for k in sorted(tep_khong_nhan, key=lambda x: -chi_muc[x]["so_trang"]):
            A("| `%s` | %d |" % (k.replace("|", "\\|"), chi_muc[k]["so_trang"]))
    A("")
    A("---")
    A("")
    A("## 5. Nguồn nằm NGOÀI bộ tài liệu")
    A("")
    A("⭐ Các tên này được chương dẫn nhưng **không có bản gốc trong tay** — chủ yếu là tiêu chuẩn")
    A("có bản quyền, datasheet, và số liệu của máy mẫu. ⚠ Đây là lý do sách **không dẫn số điều khoản**.")
    A("")
    A("| Tên nguồn | Số chương dẫn |")
    A("|---|--:|")
    for t, c in ngoai_bo.most_common(30):
        A("| %s | %d |" % (t.replace("|", "\\|"), c))
    A("")
    if khong_khop:
        A("---")
        A("")
        A("## 6. ⚠ Tên nguồn chưa khớp được nhãn nào")
        A("")
        A("⭐ Hoặc là nguồn ngoài bộ (thêm mẫu vào `nguon_ngoai_bo_tai_lieu`), hoặc là tệp có thật")
        A("nhưng thiếu bí danh (thêm vào `bi_danh_tep`).")
        A("")
        A("| Tên | Số lần |")
        A("|---|--:|")
        for t, c in khong_khop.most_common(40):
            A("| %s | %d |" % (t.replace("|", "\\|"), c))
        A("")
    A("---")
    A("")
    A("*Sinh tự động bởi `tools/ban_do_nguon.py`.*")

    io.open(DICH, "w", encoding="utf-8", newline="").write("\n".join(d) + "\n")


if __name__ == "__main__":
    sys.exit(main())
