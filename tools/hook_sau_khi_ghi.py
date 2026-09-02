# -*- coding: utf-8 -*-
"""
hook_sau_khi_ghi.py — hook PostToolUse: tự kiểm tra chương ngay sau khi ghi file.

Đọc JSON của hook trên stdin, lấy đường dẫn file. Nếu là docs/chNN_*.md thì
chạy kiem_tra_chuong.py cho đúng chương đó và in kết quả để Claude thấy ngay,
thay vì phát hiện thiếu mục sau khi đã viết xong cả loạt chương.

Chỉ báo LỖI và CẢNH BÁO; TIN (gợi ý xem lại code) để dành cho lần rà thủ công
— nếu không hook sẽ ồn sau mỗi lần sửa nhỏ.
"""
import json
import os
import re
import subprocess
import sys

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    try:
        du_lieu = json.load(sys.stdin)
    except (json.JSONDecodeError, ValueError):
        return 0

    duong_dan = (du_lieu.get("tool_input") or {}).get("file_path") or ""
    m = re.search(r"ch(\d{2})_[^/\\]*\.md$", duong_dan.replace("\\", "/"))
    if not m:
        return 0
    so = int(m.group(1))

    kq = subprocess.run(
        [sys.executable, os.path.join(GOC, "tools", "kiem_tra_chuong.py"),
         str(so), "--json"],
        capture_output=True, text=True, encoding="utf-8", cwd=GOC)

    try:
        muc = json.loads(kq.stdout or "[]")
    except (json.JSONDecodeError, ValueError):
        return 0

    dang_ke = [x for x in muc if x["muc"] in ("LỖI", "CẢNH BÁO")]
    if not dang_ke:
        return 0

    dong = ["Kiểm tra bất biến — Chương %d:" % so]
    for x in dang_ke:
        dong.append("  [%s] %s — %s" % (x["muc"], x["ma"], x["thong_diep"]))
    dong.append("Chạy `python tools/kiem_tra_chuong.py %d` để xem đầy đủ." % so)
    dong.append("Nhớ chạy thêm `python tools/kiem_nhat_quan.py` — kiểm trôi dạt GIỮA các tài liệu")
    dong.append("(dẫn chiếu gãy, tên tag lệch bảng I/O, số liệu chốt viết khác nhau).")

    sys.stdout.buffer.write(("\n".join(dong) + "\n").encode("utf-8", "replace"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
