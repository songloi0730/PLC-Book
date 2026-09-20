# -*- coding: utf-8 -*-
"""Kiểm tính liền mạch của MỌI dãy số trong sách: số mục, số hình, số bẫy, số bài tập.

Con trỏ trỏ đúng chỗ (kiem_tro_muc.py) vẫn không loại trừ được chuyện dãy số
tự nó bị thủng hoặc trùng: mục 4.5 rồi nhảy sang 4.7, hai mục cùng mang số
19.6, Hình 33.2 không tồn tại vì hình duy nhất của chương là 33.1.

Chạy:  python tools/kiem_danh_so.py
"""
import glob
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")


def _bo_code(s):
    return re.sub(r"```.*?```", "", s, flags=re.S)


def _tach(so):
    """'15.4b' -> (15, 4, 'b')  để so sánh đúng thứ tự."""
    m = re.match(r"(\d+)\.(\d+)([a-z]?)$", so)
    return (int(m.group(1)), int(m.group(2)), m.group(3)) if m else None


def kiem_muc(loi):
    """Số mục trong mỗi chương phải TĂNG DẦN và không trùng."""
    for p in sorted(glob.glob(os.path.join(DOCS, "ch*.md"))):
        ten = os.path.basename(p)
        ch = int(re.search(r"ch(\d+)", ten).group(1))
        s = io.open(p, encoding="utf-8").read()
        muc = re.findall(r"^##\s+(\d+\.\d+[a-z]?)\s", s, re.M)
        thay = set()
        truoc = None
        for m in muc:
            if m in thay:
                loi.append((ten, "mục %s xuất hiện HAI LẦN" % m))
            thay.add(m)
            t = _tach(m)
            if t is None:
                continue
            if t[0] != ch:
                loi.append((ten, "mục %s không mang số chương %d" % (m, ch)))
            if truoc and t <= truoc:
                loi.append((ten, "mục %s đứng SAU %d.%d%s — sai thứ tự"
                            % (m, truoc[0], truoc[1], truoc[2])))
            truoc = t
        # thung so: 4.5 -> 4.7
        chinh = sorted({t[1] for t in (_tach(m) for m in muc) if t})
        for a, b in zip(chinh, chinh[1:]):
            if b - a > 1:
                loi.append((ten, "nhảy số: sau mục %d.%d là %d.%d — thiếu %s"
                            % (ch, a, ch, b,
                               ", ".join("%d.%d" % (ch, x) for x in range(a + 1, b)))))


def kiem_hinh(loi):
    """Mọi 'Hình N.k' được nhắc phải có một chú thích '*Hình N.k — …*' thật."""
    co, nhac = set(), []
    for p in sorted(glob.glob(os.path.join(DOCS, "*.md"))):
        ten = os.path.basename(p)
        if ten.startswith("00d_"):
            continue
        s = io.open(p, encoding="utf-8").read()
        for m in re.finditer(r"^\*Hình\s+(\d+\.\d+)\s+—", s, re.M):
            co.add(m.group(1))
        for i, dong in enumerate(_bo_code(s).split("\n"), 1):
            for m in re.finditer(r"Hình\s+(\d+\.\d+)", dong):
                nhac.append((ten, i, m.group(1)))
    for ten, i, h in nhac:
        if h not in co:
            loi.append((ten, "dòng %d nhắc **Hình %s** nhưng không có chú thích hình đó" % (i, h)))


def kiem_bay(loi):
    """Số BẪY trong mỗi chương phải là 1,2,3… liên tục."""
    for p in sorted(glob.glob(os.path.join(DOCS, "*.md"))):
        ten = os.path.basename(p)
        s = io.open(p, encoding="utf-8").read()
        so = [int(x) for x in re.findall(r"^###\s+🔍\s+BẪY\s+(\d+)", s, re.M)]
        if not so:
            continue
        if so != list(range(1, len(so) + 1)):
            loi.append((ten, "dãy số BẪY không liền mạch: %s" % so))


def main():
    loi = []
    kiem_muc(loi)
    kiem_hinh(loi)
    kiem_bay(loi)
    print("=" * 78)
    print("KIỂM ĐÁNH SỐ — mục · hình · bẫy")
    print("=" * 78)
    for ten, m in loi:
        print("  [LỖI] %-38s %s" % (ten[:38], m))
    print("-" * 78)
    print("TỔNG:  %d LỖI" % len(loi))
    print("-" * 78)
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
