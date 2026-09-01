# -*- coding: utf-8 -*-
"""danh_dau_xong.py — đánh dấu một chương là đã viết xong trong docs/00_Muc_luc.md.

Thêm liên kết tới file chương và đổi ô trạng thái ⬜ → ✅.
Dùng:  python tools/danh_dau_xong.py 18 ch18_counter_va_dem_xung_toc_do_cao.md
"""
import io
import os
import re
import sys

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MUCLUC = os.path.join(GOC, "docs", "00_Muc_luc.md")


def main():
    if len(sys.argv) != 3:
        return "Dùng: python tools/danh_dau_xong.py <số chương> <tên file .md>"
    so, ten_file = sys.argv[1], sys.argv[2]
    if not os.path.exists(os.path.join(GOC, "docs", ten_file)):
        return "Không thấy file docs/%s" % ten_file

    t = io.open(MUCLUC, encoding="utf-8").read()
    m = re.search(r"^\| %s \|(.*)$" % re.escape(so), t, re.M)
    if not m:
        return "Không thấy dòng chương %s trong mục lục" % so
    dong = m.group(0)

    if "](%s)" % ten_file not in dong:
        # bọc tên chương thành liên kết — tên nằm giữa hai dấu | đầu tiên
        cot = dong.split("|")
        if len(cot) < 3:
            return "Dòng mục lục không đúng định dạng bảng"
        ten = cot[2].strip().strip("*").strip()
        cot[2] = " [%s](%s) " % (ten, ten_file)
        dong = "|".join(cot)

    # Đổi ⬜ → ✅ nhưng GIỮ NGUYÊN các cờ đi kèm (⚠ chờ chuyên gia an toàn,
    # 🔍 chờ xác minh kỹ thuật). Bộ kiểm không gỡ được các cờ đó, và công cụ
    # này cũng không — chỉ người dùng gỡ.
    dong_moi = re.sub(r"⬜(\s*[^|]*)\|\s*$", lambda x: "✅%s|" % x.group(1), dong)
    if dong_moi == dong and "✅" not in dong:
        return "Ô trạng thái chương %s không phải ⬜ — kiểm tay" % so

    io.open(MUCLUC, "w", encoding="utf-8", newline="").write(
        t[:m.start()] + dong_moi + t[m.end():])
    return "OK — chương %s: đã liên kết + đánh dấu ✅" % so


if __name__ == "__main__":
    kq = main()
    sys.stdout.buffer.write((kq + "\n").encode("utf-8", "replace"))
    sys.exit(0 if kq.startswith("OK") else 1)
