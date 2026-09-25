# -*- coding: utf-8 -*-
"""Kiểm bản HTML ĐÃ RENDER: không được còn dấu nhấn markdown chưa chuyển thành thẻ.

Các bộ kiểm khác đọc markdown nguồn. Nhưng có lỗi chỉ lộ ra SAU khi render: đợt 58
tìm ra mục lục thanh bên in nguyên "khi nào **không** nên dùng", bảy dòng Mục lục
có `**` không đóng, và một mẫu `**… *(UDT)*, …**` mà trình chuyển hiểu sai — cả ba
đều nằm trong bản phát hành, và markdownlint không bắt cái nào.

Bỏ qua nội dung trong <pre>, <code>, <style>, <script> và ảnh nhúng.

Chạy:  python tools/kiem_html.py <tệp.html>
"""
import io
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

SOT = re.compile(r"\*<em>|</em>\*|(?<![\w*])\*\*(?=\S)|(?<=\S)\*\*(?![\w*])")


def main():
    h = io.open(sys.argv[1], encoding="utf-8").read()
    for the in ("pre", "code", "style", "script"):
        h = re.sub(r"<%s\b.*?</%s>" % (the, the), "", h, flags=re.S)
    h = re.sub(r'src="data:[^"]*"', "", h)
    ra = []
    for m in SOT.finditer(h):
        ra.append(re.sub(r"<[^>]+>", "", h[max(0, m.start() - 60):m.end() + 40]).replace("\n", " "))
    print("KIỂM HTML ĐÃ RENDER — %d chỗ còn dấu nhấn markdown" % len(ra))
    for d in ra[:20]:
        print("  [LỖI] …%s…" % d.strip())
    return 1 if ra else 0


if __name__ == "__main__":
    sys.exit(main())
