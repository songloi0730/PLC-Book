# -*- coding: utf-8 -*-
"""Hình chuyên biệt của Chương 43 — sơ đồ thời gian một vòng kích ảnh.

Dùng chung bộ token thị giác ở `sinh_hinh.py`.
Chạy:  python tools/sinh_hinh_ch43.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sinh_hinh import (  # noqa: E402
    INK, INK2, RULE, CUR, OK, BAD, WARN, PANEL, T, R, L, arw, head, save, log,
)


def fig_43_1():
    """Một vòng kích–kết quả: ai làm gì, lúc nào, và số thứ tự đi kèm ở đâu."""
    W, H = 900, 452
    s = head(W, H, "Hình 43.1 — Một vòng kích ảnh, từ lệnh tới lúc PLC dám dùng kết quả",
             "Ba việc phải đúng: bit CHO PHÉP đã bật · kích theo CẠNH LÊN · kết quả mang ĐÚNG số thứ tự.")

    xl, xr = 168, 866          # trục thời gian
    lanes = [
        ("PLC — cho phép kích", 104),
        ("PLC — lệnh kích", 152),
        ("Camera — chụp & xử lý", 200),
        ("Mạng — kết quả về", 248),
        ("PLC — dùng kết quả", 296),
    ]
    for nhan, y in lanes:
        s.append(T(24, y + 4, nhan, 11, INK2))
        s.append(L(xl, y, xr, y, RULE, "1.1", "3,3"))

    t_trig, t_done, t_res, t_use = 300, 560, 636, 668

    # Lane 1 — bit cho phép: lên trước và giữ suốt
    s.append(L(xl, 104, 214, 104, RULE, "1.6"))
    s.append(L(214, 104, 214, 92, OK, "2"))
    s.append(L(214, 92, xr, 92, OK, "2.4"))
    s.append(T(220, 86, "bật TRƯỚC — và giữ nguyên", 10, OK, "700"))

    # Lane 2 — xung kích
    s.append(L(xl, 152, t_trig, 152, RULE, "1.6"))
    s.append(L(t_trig, 152, t_trig, 140, CUR, "2.4"))
    s.append(L(t_trig, 140, t_trig + 26, 140, CUR, "2.4"))
    s.append(L(t_trig + 26, 140, t_trig + 26, 152, CUR, "2.4"))
    s.append(L(t_trig + 26, 152, xr, 152, RULE, "1.6"))
    s.append(T(t_trig - 4, 132, "cạnh lên", 10, CUR, "700"))

    # Lane 3 — camera làm việc
    s.append(R(t_trig, 186, t_done - t_trig, 28, fill="#EAF1F6", stroke=INK, sw="1.4"))
    s.append(T((t_trig + t_done) // 2, 204, "phơi sáng  →  xử lý ảnh", 11, INK, "700", "middle"))

    # Lane 4 — kết quả về mạng
    s.append(R(t_done, 234, t_res - t_done, 28, fill="#DFF0E4", stroke=OK, sw="1.4"))
    s.append(T((t_done + t_res) // 2, 252, "gói kết quả", 10, INK, "700", "middle"))
    s.append(T(t_res + 8, 246, "kèm SỐ THỨ TỰ", 10, OK, "700"))

    # Lane 5 — PLC dùng
    s.append(L(xl, 296, t_use, 296, RULE, "1.6"))
    s.append(L(t_use, 296, t_use, 284, OK, "2.4"))
    s.append(L(t_use, 284, xr, 284, OK, "2.4"))
    s.append(T(t_use + 6, 278, "chỉ dùng khi SỐ THỨ TỰ khớp", 10, OK, "700"))

    # Dải đo độ trễ
    yb = 330
    s.append(L(t_trig, 214, t_trig, yb, RULE, "1.1", "3,3"))
    s.append(L(t_use, 296, t_use, yb, RULE, "1.1", "3,3"))
    s += arw(t_trig, yb, t_use, yb, INK2, "1.6")
    s += arw(t_use, yb, t_trig, yb, INK2, "1.6")
    s.append(T((t_trig + t_use) // 2, yb - 8,
               "toàn vòng ~55–59 ms  (số đo trên một hệ thật)", 11, INK, "700", "middle"))

    # Hai hộp cảnh báo
    s.append(R(24, 352, 418, 76, fill="#FBE9E7", stroke=BAD, sw="1.2"))
    s.append(T(38, 372, "⚠⚠  Nếu bit CHO PHÉP chưa bật:", 11.5, BAD, "700"))
    s.append(T(38, 390, "camera bỏ qua mọi lệnh kích — và KHÔNG báo lỗi gì.", 10.5, "#7A2E24"))
    s.append(T(38, 408, "Triệu chứng: dây đúng, địa chỉ đúng, mà không có ảnh nào.", 10.5, "#7A2E24"))

    s.append(R(456, 352, 418, 76, fill="#FDF6E7", stroke=WARN, sw="1.2"))
    s.append(T(470, 372, "⚠  Nếu xử lý chậm hơn nhịp máy:", 11.5, "#7A5B08", "700"))
    s.append(T(470, 390, "gói về có thể là kết quả của SẢN PHẨM TRƯỚC.", 10.5, "#7A5B08"))
    s.append(T(470, 408, "Số thứ tự không khớp → VỨT BỎ, không dùng.", 10.5, "#7A5B08"))

    return save(s, "ch43", "hinh_43_1_vong_kich_anh.svg")


if __name__ == "__main__":
    fig_43_1()
    for line in log:
        print(line)
