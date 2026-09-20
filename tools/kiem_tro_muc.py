# -*- coding: utf-8 -*-
"""Kiểm mọi con trỏ "mục N.M" và "Phụ lục X.N" trong sách có trỏ tới chỗ CÓ THẬT không.

Một con trỏ sai là lỗi im lặng: người đọc lật tới nơi, không thấy gì, và mất
niềm tin vào mọi con trỏ khác. Không bộ kiểm nào trước đây soát chuyện này —
kiem_nhat_quan.py soát TRÔI DẠT THUẬT NGỮ, không soát số mục.

Chạy:  python tools/kiem_tro_muc.py
"""
import glob
import io
import os
import re
import sys

# In tiếng Việt ra console Windows mà không phụ thuộc biến môi trường của người gọi.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOCS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs")


def _nap_tieu_de():
    """Trả về tập mọi số mục có thật, dạng {"9.5", "15.4b", "C.10", ...}."""
    co = set()
    for p in glob.glob(os.path.join(DOCS, "*.md")):
        s = io.open(p, encoding="utf-8").read()
        for m in re.finditer(r"^#{2,3}\s+([0-9]+\.[0-9]+[a-z]?|[A-L][0-9]?\.[0-9]+(?:\.[0-9]+)?)\s",
                             s, re.M):
            co.add(m.group(1))
        # chuong khong co so muc con: ghi so chuong de "Chuong N" van hop le
        m = re.match(r"^#\s+Chương\s+([0-9]+)", s, re.M)
        if m:
            co.add(m.group(1))
    return co


# Con tro dang: "mục 9.5" · "§13.4" · "mục 15.4b" · "Phụ lục C.10" · "Phụ lục J §J.1"
MAU = re.compile(r"(?:mục|Mục|§)\s*([0-9]+\.[0-9]+[a-z]?)"
                 r"|Phụ lục\s+([A-L][12]?)\s*[.§]\s*([A-L]?[0-9]+(?:\.[0-9]+)?)"
                 r"|(?:mục|Mục|§)\s*([A-L][12]?\.[0-9]+(?:\.[0-9]+)?)")


def main():
    co = _nap_tieu_de()
    hong, tong = [], 0
    for p in sorted(glob.glob(os.path.join(DOCS, "*.md"))):
        ten = os.path.basename(p)
        if ten.startswith("00d_"):            # nhat ky: chua trich dan lich su
            continue
        s = io.open(p, encoding="utf-8").read()
        s = re.sub(r"```.*?```", "", s, flags=re.S)
        for i, dong in enumerate(s.split("\n"), 1):
            for m in MAU.finditer(dong):
                if m.group(1):
                    khoa = m.group(1)
                elif m.group(2):
                    g3 = m.group(3)
                    khoa = g3 if g3[0].isalpha() else m.group(2) + "." + g3
                else:
                    khoa = m.group(4)
                tong += 1
                if khoa not in co:
                    hong.append((ten, i, khoa, dong.strip()[:96]))

    print("=" * 78)
    print("KIỂM CON TRỎ TỚI SỐ MỤC — %d con trỏ trong %d tệp"
          % (tong, len(glob.glob(os.path.join(DOCS, "*.md")))))
    print("=" * 78)
    for ten, i, khoa, d in hong:
        print("  [LỖI] %-34s :%-5d → không có mục %s" % (ten[:34], i, khoa))
        print("         %s" % d)
    print("-" * 78)
    print("TỔNG:  %d LỖI  ·  %d con trỏ đã kiểm" % (len(hong), tong))
    print("-" * 78)
    return 1 if hong else 0


if __name__ == "__main__":
    sys.exit(main())
