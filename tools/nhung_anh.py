# -*- coding: utf-8 -*-
# -------------------------------------------------------
# File:    nhung_anh.py
# Project: PLC Programming Book
# Purpose: Nhung anh ![..](../assets/..svg) thanh data-URI base64 ngay trong
#          file .md gop, de ban .md + .html xuat ban TU DUNG MOT MINH (khong
#          phu thuoc thu muc assets/ o kho xuat ban). Goi trong gop_sach.sh
#          NGAY SAU khi tao OUT_MD va TRUOC khi chay marked.
# -------------------------------------------------------
"""Nhung anh SVG (va PNG neu co) thanh data-URI trong 1 file markdown.

  python tools/nhung_anh.py "output/<ten> vX.Y.Z.YYMMDD.md"

Tim moi ![alt](../assets/....svg|png), doc file that (tuong doi voi thu muc
chua file .md), ma hoa base64, thay bang ![alt](data:<mime>;base64,....).
File thieu -> giu nguyen + canh bao.
"""
import sys, io, os, re, base64

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

MIME = {".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg"}
IMG_RE = re.compile(r"!\[([^\]]*)\]\((\.\./assets/[^)]+?)\)")


def main() -> None:
    if len(sys.argv) < 2:
        print("Dung: python tools/nhung_anh.py <file.md>")
        sys.exit(1)
    md_path = sys.argv[1]
    md_dir = os.path.dirname(os.path.abspath(md_path))
    text = open(md_path, encoding="utf-8").read()

    embedded = 0
    missing = []

    def repl(m: "re.Match[str]") -> str:
        nonlocal embedded
        alt, rel = m.group(1), m.group(2)
        fpath = os.path.normpath(os.path.join(md_dir, rel))
        ext = os.path.splitext(fpath)[1].lower()
        if not os.path.isfile(fpath) or ext not in MIME:
            missing.append(rel)
            return m.group(0)
        with open(fpath, "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode("ascii")
        embedded += 1
        return f"![{alt}](data:{MIME[ext]};base64,{b64})"

    out = IMG_RE.sub(repl, text)
    with open(md_path, "w", encoding="utf-8") as fh:
        fh.write(out)

    print(f"Nhung anh data-URI: {embedded} anh")
    if missing:
        print(f"  ⚠ {len(missing)} anh KHONG tim thay (giu nguyen): " + ", ".join(missing[:8]))


if __name__ == "__main__":
    main()
