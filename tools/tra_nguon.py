# -*- coding: utf-8 -*-
"""
tra_nguon.py — tra một khẳng định trong sách ngược về TÀI LIỆU GỐC.

Bộ tài liệu tham khảo (40+ PDF, ~12.000 trang) nằm ở thư mục reference. Công cụ
này trích text một lần vào bộ đệm rồi tìm nhanh, trả về: tên file · số trang ·
đoạn văn xung quanh — đủ để xác nhận hoặc bác bỏ một câu trong sách.

Mục đích: biến việc "kiểm tra so với tài liệu thực tế" từ việc thủ công tốn công
thành việc chạy một lệnh. Không có nó thì bước xác minh sẽ bị bỏ.

Dùng:
    python tools/tra_nguon.py "asynchronous"              # tìm mọi nguồn
    python tools/tra_nguon.py "retentive" --tep Siemens   # lọc theo tên file
    python tools/tra_nguon.py "light curtain" -n 3        # 3 kết quả mỗi file
    python tools/tra_nguon.py --dung                      # dựng lại bộ đệm
    python tools/tra_nguon.py --liet-ke                   # liệt kê nguồn có sẵn

⚠ Công cụ chỉ TÌM. Việc đọc, hiểu và quyết định vẫn là của người dùng — và với
tiêu chuẩn có bản quyền, ⚠ tuyệt đối không chép nguyên văn vào sách.
"""
import os
import re
import subprocess
import sys

def xp(*a):
    """In an toan tren console gbk cua Windows."""
    txt = " ".join(str(x) for x in a)
    try:
        print(txt)
    except UnicodeEncodeError:
        sys.stdout.buffer.write((txt + os.linesep).encode("utf-8", "replace"))


GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Thư mục tài liệu tham khảo nằm NGOÀI repo sách (tài liệu có bản quyền của hãng)
NGUON = os.path.normpath(os.path.join(GOC, "..", "PLC", "reference"))
DEM = os.path.join(GOC, "tools", ".cache_nguon")


def cac_pdf():
    ra = []
    for thu_muc, _, tep in os.walk(NGUON):
        for t in sorted(tep):
            if t.lower().endswith((".pdf", ".txt")):
                ra.append(os.path.join(thu_muc, t))
    return sorted(ra)


def ten_dem(duong_dan):
    rel = os.path.relpath(duong_dan, NGUON).replace(os.sep, "__")
    return os.path.join(DEM, rel + ".txt")


def dung_bo_dem(bat_buoc=False):
    """Trích text mọi PDF một lần. pdftotext giữ ký tự ngắt trang \\f để đếm trang."""
    if not os.path.isdir(NGUON):
        xp("KHÔNG tìm thấy thư mục nguồn: %s" % NGUON)
        return False
    os.makedirs(DEM, exist_ok=True)
    moi = 0
    for p in cac_pdf():
        d = ten_dem(p)
        if os.path.exists(d) and not bat_buoc:
            continue
        if p.lower().endswith(".txt"):
            with open(p, encoding="utf-8", errors="replace") as f:
                noi_dung = f.read()
            with open(d, "w", encoding="utf-8") as f:
                f.write(noi_dung)
        else:
            r = subprocess.run(["pdftotext", "-q", p, d],
                               capture_output=True, text=True)
            if r.returncode != 0:
                xp("  ⚠ không trích được: %s" % os.path.basename(p))
                continue
        moi += 1
    if moi:
        xp("Đã dựng bộ đệm cho %d tài liệu." % moi)
    return True


def trang_cua(van, vi_tri):
    """pdftotext chèn \\f giữa các trang → đếm để ra số trang."""
    return van.count("\f", 0, vi_tri) + 1


def tim(tu_khoa, loc_tep=None, moi_tep=2, rong=260):
    mau = re.compile(tu_khoa, re.I)
    tong = 0
    for p in cac_pdf():
        ten = os.path.basename(p)
        if loc_tep and loc_tep.lower() not in ten.lower():
            continue
        d = ten_dem(p)
        if not os.path.exists(d):
            continue
        with open(d, encoding="utf-8", errors="replace") as f:
            van = f.read()
        hit = list(mau.finditer(van))
        if not hit:
            continue
        xp("\n=== %s  (%d chỗ khớp)" % (ten, len(hit)))
        for m in hit[:moi_tep]:
            a = max(0, m.start() - rong // 2)
            doan = van[a: m.start() + rong // 2]
            doan = re.sub(r"\s+", " ", doan).strip()
            xp("  [tr.%d] …%s…" % (trang_cua(van, m.start()), doan))
            tong += 1
    if tong == 0:
        xp("Không tìm thấy '%s' trong bộ tài liệu." % tu_khoa)
        xp("⚠ KHÔNG có nghĩa là khẳng định sai — có thể bộ tài liệu không phủ chủ đề này.")
        xp("   Khi đó phải tra nguồn ngoài, và GHI RÕ đã tra ở đâu (Phụ lục H).")
    return tong


def liet_ke():
    xp("Thư mục nguồn: %s\n" % NGUON)
    nhom = {}
    for p in cac_pdf():
        nhom.setdefault(os.path.basename(os.path.dirname(p)), []).append(os.path.basename(p))
    for k in sorted(nhom):
        xp("── %s" % k)
        for t in nhom[k]:
            co = "✓" if os.path.exists(ten_dem(os.path.join(NGUON, k, t))) else " "
            xp("   %s %s" % (co, t))
    xp("\n✓ = đã có trong bộ đệm. Chạy --dung để dựng phần còn thiếu.")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("-")]
    if "--liet-ke" in sys.argv:
        dung_bo_dem()
        liet_ke()
        return 0
    if "--dung" in sys.argv:
        return 0 if dung_bo_dem(bat_buoc="--lai" in sys.argv) else 1
    if not args:
        xp(__doc__)
        return 0

    loc = None
    if "--tep" in sys.argv:
        i = sys.argv.index("--tep")
        if i + 1 < len(sys.argv):
            loc = sys.argv[i + 1]
    moi_tep = 2
    if "-n" in sys.argv:
        i = sys.argv.index("-n")
        if i + 1 < len(sys.argv):
            moi_tep = int(sys.argv[i + 1])

    dung_bo_dem()
    tu_khoa = args[0]
    xp("Tra: %r%s" % (tu_khoa, "  (lọc: %s)" % loc if loc else ""))
    tim(tu_khoa, loc, moi_tep)
    return 0


if __name__ == "__main__":
    sys.exit(main())
