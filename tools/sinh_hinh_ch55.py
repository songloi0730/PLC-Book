# -*- coding: utf-8 -*-
"""Hình chuyên biệt của Chương 55 — mô hình sáu trạng thái thiết bị.

Dùng chung bộ token thị giác ở `sinh_hinh.py` (màu, cỡ chữ, mũi tên đa giác).
Chạy:  python tools/sinh_hinh_ch55.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sinh_hinh import (  # noqa: E402
    INK, INK2, RULE, OK, BAD, WARN, PANEL, T, R, L, head, save, log,
)


def fig_55_1():
    """Sáu trạng thái thiết bị và cách chúng gộp thành các khối thời gian."""
    W, H = 900, 530
    s = head(W, H, "Hình 55.1 — Sáu trạng thái thiết bị và các khối thời gian",
             "Mọi khoảnh khắc của thiết bị phải rơi vào ĐÚNG MỘT trong sáu trạng thái. "
             "Phân loại theo CHỨC NĂNG, không theo ai làm.")

    # Sáu dải trạng thái, xếp sao cho các nhóm nằm liền nhau
    rows = [
        ("Đang sản xuất", "productive", "#DFF0E4", OK,
         "Chạy đúng chức năng · nạp và dỡ · làm lại hàng"),
        ("Chờ", "standby", "#EAF1F6", INK2,
         "Chạy được nhưng không chạy: hết người, hết hàng, hết đồ gá, chờ lệnh cấp trên"),
        ("Kỹ thuật", "engineering", "#EDE7F6", "#5B4B8A",
         "Chạy được, nhưng đang dùng để thử nghiệm quá trình hoặc thiết bị"),
        ("Dừng CÓ kế hoạch", "scheduled downtime", "#FDF6E7", WARN,
         "Bảo trì phòng ngừa · cài đặt đổi lô · thay vật tư tiêu hao · chờ bảo trì"),
        ("Dừng NGOÀI kế hoạch", "unscheduled downtime", "#FBE9E7", BAD,
         "Sửa chữa · đầu vào ngoài quy cách · sự cố hạ tầng · chờ người hoặc phụ tùng"),
        ("Không xếp lịch", "non-scheduled", "#F0F0F0", RULE,
         "Ca không làm · lắp đặt, nâng cấp · đào tạo ngoài giờ · tắt và khởi động lại"),
    ]

    x0, y0, bw, bh, gap = 26, 92, 430, 50, 8
    for i, (vi, en, fill, edge, desc) in enumerate(rows):
        y = y0 + i * (bh + gap)
        s.append(R(x0, y, bw, bh, fill=fill, stroke=edge, sw="1.5"))
        s.append(T(x0 + 14, y + 21, vi, 12.5, INK, "700"))
        s.append(T(x0 + 14 + 7.2 * len(vi) + 10, y + 21, "(" + en + ")", 10, INK2))
        s.append(T(x0 + 14, y + 39, desc, 10, INK2))

    # Ngoặc nhóm — cột 1: lên máy / xuống máy
    def brace(x, ytop, ybot, nhan, col, dx=12):
        out = [L(x, ytop, x + dx, ytop, col, "1.6"),
               L(x + dx, ytop, x + dx, ybot, col, "1.6"),
               L(x, ybot, x + dx, ybot, col, "1.6")]
        out.append(T(x + dx + 8, (ytop + ybot) / 2 + 4, nhan, 11.5, col, "700"))
        return out

    xb1 = x0 + bw + 6
    top1, bot1 = y0, y0 + 3 * bh + 2 * gap
    s += brace(xb1, top1, bot1, "Thiết bị LÊN MÁY", OK)
    s.append(T(xb1 + 20 + 118, (top1 + bot1) / 2 + 4, "(uptime)", 10, INK2))

    top2 = y0 + 3 * (bh + gap)
    bot2 = top2 + 2 * bh + gap
    s += brace(xb1, top2, bot2, "Thiết bị XUỐNG MÁY", BAD)
    s.append(T(xb1 + 20 + 136, (top2 + bot2) / 2 + 4, "(downtime)", 10, INK2))

    # Ngoặc nhóm — cột 2: khối thời gian
    xb2 = xb1 + 178
    s += brace(xb2, y0, bot2, "Thời gian VẬN HÀNH", INK)
    s.append(T(xb2 + 20, (y0 + bot2) / 2 + 20, "(operations time)", 10, INK2))

    ybot_all = y0 + 5 * (bh + gap) + bh
    xt = 862
    s.append(L(xt, y0 - 6, xt, ybot_all, RULE, "1.2", "4,3"))
    s.append(T(xt - 8, ybot_all - 26, "Tổng thời gian", 11.5, INK, "700", "end"))
    s.append(T(xt - 8, ybot_all - 11, "(total time)", 10, INK2, "400", "end"))

    # Ghi chú dưới — đặt HẲN dưới dải cuối, không đè
    s.append(R(26, ybot_all + 20, 848, 48, fill="#FDF6E7", stroke=WARN, sw="1.2"))
    s.append(T(40, ybot_all + 40,
               "⚠  Thời gian SẢN XUẤT (manufacturing time) = thời gian vận hành TRỪ thời gian kỹ thuật "
               "— đó là mẫu số của phần lớn phép tính khả dụng.",
               11, "#7A5B08"))
    s.append(T(40, ybot_all + 58,
               "⭐  Hai cỗ máy chỉ so sánh được khi cùng xếp một khoảnh khắc vào cùng một dải. "
               "Đó là lý do bộ định nghĩa chung tồn tại.",
               11, "#7A5B08"))
    return save(s, "ch55", "hinh_55_1_sau_trang_thai_thiet_bi.svg")


if __name__ == "__main__":
    fig_55_1()
    for line in log:
        print(line)
