# -*- coding: utf-8 -*-
"""Kiểm trích dẫn "Chương N" có trỏ đúng chương CHỦ NHÀ của chủ đề không.

`kiem_tro_muc.py` chỉ kiểm con trỏ có trỏ tới mục CÓ THẬT. Một con trỏ hoàn
toàn hợp lệ về hình thức vẫn có thể dẫn người đọc sang chương không nói gì về
chủ đề đó — đợt 51 tìm ra 3 chỗ, đợt 56 tìm thêm 6 chỗ, trong đó có nguyên
một CỤM bốn chỗ dẫn "Chương 24" cho việc ghi chú thích (chủ nhà là Chương 30).
Cụm đó là dấu vết của một lần đánh số lại chương chưa cập nhật hết.

Cách kiểm: với mỗi thuật ngữ lõi có ĐÚNG MỘT chương chủ nhà, nếu một dòng vừa
chứa thuật ngữ đó vừa trích dẫn "Chương N" với N khác chủ nhà, VÀ chương N
không hề nhắc thuật ngữ đó, thì báo để người soát quyết định.

⚠ Đây là bộ kiểm CÓ THỂ BÁO NHẦM: câu có thể trích dẫn cho một vế khác. Vì
vậy nó in ra để người đọc xét, và mọi trường hợp đã xét là đúng thì ghi vào
`bo_qua` trong tools/cau_hinh_chu_nha.json.

Chạy:  python tools/kiem_chu_nha.py
"""
import glob
import io
import json
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

GOC = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(GOC, "..", "docs")
CFG = os.path.join(GOC, "cau_hinh_chu_nha.json")

DUNG = re.compile(r"\((?:xem\s+)?(?:Chương|Ch\.)\s*(\d+)[^)]*\)"
                  r"|(?:Chương|Ch\.)\s*(\d+)\s+mục"
                  r"|\|\s*Chương\s+(\d+)[,\s|]")


def main():
    cfg = json.load(io.open(CFG, encoding="utf-8"))
    nha = {k: int(v) for k, v in cfg["chu_nha"].items()}
    bo_qua = {tuple(x) for x in cfg.get("bo_qua", [])}

    noi = {}
    for p in glob.glob(os.path.join(DOCS, "ch*.md")):
        n = int(re.search(r"ch(\d+)", p.replace("\\", "/")).group(1))
        noi[n] = io.open(p, encoding="utf-8").read().lower()

    ra = []
    for p in sorted(glob.glob(os.path.join(DOCS, "*.md"))):
        ten = os.path.basename(p)
        if ten.startswith("00"):
            continue
        s = re.sub(r"```.*?```", "", io.open(p, encoding="utf-8").read(), flags=re.S)
        for i, dong in enumerate(s.split("\n"), 1):
            thap = dong.lower()
            for tu, chu in nha.items():
                if tu.lower() not in thap:
                    continue
                for m in DUNG.finditer(dong):
                    n = int(next(g for g in m.groups() if g))
                    if n not in noi or n == chu:
                        continue
                    if tu.lower() in noi[n]:
                        continue
                    if (ten, tu, n) in bo_qua:
                        continue
                    ra.append((ten, i, tu, n, chu, dong.strip()[:92]))

    print("=" * 78)
    print("KIỂM CHƯƠNG CHỦ NHÀ — %d thuật ngữ lõi" % len(nha))
    print("=" * 78)
    for ten, i, tu, n, chu, d in ra:
        print("  [XÉT] %-30s :%-4d \"%s\" → Ch.%-2d (chủ nhà Ch.%d, Ch.%d không nhắc từ này)"
              % (ten[:30], i, tu, n, chu, n))
        print("        %s" % d)
    print("-" * 78)
    print("TỔNG:  %d chỗ cần xét" % len(ra))
    if ra:
        print("  → sửa, hoặc thêm vào \"bo_qua\" trong tools/cau_hinh_chu_nha.json")
    print("-" * 78)
    return 1 if ra else 0


if __name__ == "__main__":
    sys.exit(main())
