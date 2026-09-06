# -*- coding: utf-8 -*-
"""Hình chuyên biệt của Chương 21 — nhánh song song và nhánh lựa chọn trong SFC.

Vạch đôi và vạch đơn trông rất giống nhau nhưng nghĩa ngược nhau; vẽ ra thì
khác biệt đó không thể nhầm được nữa.

Chạy:  python tools/sinh_hinh_ch21.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sinh_hinh import (  # noqa: E402
    INK, INK2, RULE, OK, BAD, WARN, PANEL, T, R, L, arw, head, save, log,
)


def _buoc(x, y, nhan, w=104, h=34, fill=PANEL, edge=INK):
    return [R(x - w / 2, y, w, h, fill=fill, stroke=edge, sw="1.5"),
            T(x, y + 22, nhan, 11.5, INK, "700", "middle")]


def fig_21_1():
    """Hai kiểu nhánh: vạch đôi chờ CẢ HAI, vạch đơn chọn MỘT."""
    W, H = 900, 486
    s = head(W, H, "Hình 21.1 — Vạch đôi và vạch đơn: hai nét vẽ, hai nghĩa ngược nhau",
             "Vẽ nhầm một nét là máy đứng im vĩnh viễn mà không báo gì. Đếm số vạch trước khi kết luận về luồng.")

    # ── Bên trái: nhánh SONG SONG (vạch đôi)
    cx = 236
    s.append(R(24, 84, 412, 330, fill="#FFFFFF", stroke=RULE, sw="1.2"))
    s.append(T(cx, 108, "NHÁNH SONG SONG — vạch ĐÔI", 12.5, INK, "700", "middle"))
    s.append(T(cx, 126, "chạy cùng lúc, đi tiếp khi CẢ HAI xong", 10.5, INK2, "400", "middle"))

    s += _buoc(cx, 136, "Bước trước")
    s += arw(cx, 170, cx, 186, INK, "2")
    # vạch đôi
    s.append(L(96, 190, 376, 190, INK, "2.6"))
    s.append(L(96, 196, 376, 196, INK, "2.6"))
    s.append(L(146, 196, 146, 214, INK, "1.8"))
    s.append(L(326, 196, 326, 214, INK, "1.8"))
    s += _buoc(146, 214, "Trạm 1", 96)
    s += _buoc(326, 214, "Trạm 2", 96)
    s.append(L(146, 248, 146, 272, INK, "1.8"))
    s.append(L(326, 248, 326, 272, INK, "1.8"))
    # vạch đôi hợp nhất
    s.append(L(96, 272, 376, 272, INK, "2.6"))
    s.append(L(96, 278, 376, 278, INK, "2.6"))
    s += arw(cx, 278, cx, 296, INK, "2")
    s += _buoc(cx, 296, "Bước sau")

    s.append(R(44, 344, 372, 56, fill="#DFF0E4", stroke=OK, sw="1.2"))
    s.append(T(58, 364, "⭐  Cả hai nhánh CÙNG chạy.", 11, "#1E5B37", "700"))
    s.append(T(58, 382, "Bước sau chỉ bắt đầu khi nhánh CHẬM NHẤT đã xong.", 10.5, "#1E5B37"))

    # ── Bên phải: nhánh LỰA CHỌN (vạch đơn)
    cx2 = 682
    s.append(R(464, 84, 412, 330, fill="#FFFFFF", stroke=RULE, sw="1.2"))
    s.append(T(cx2, 108, "NHÁNH LỰA CHỌN — vạch ĐƠN", 12.5, INK, "700", "middle"))
    s.append(T(cx2, 126, "chọn MỘT đường, tuỳ điều kiện nào đúng", 10.5, INK2, "400", "middle"))

    s += _buoc(cx2, 136, "Bước trước")
    s += arw(cx2, 170, cx2, 186, INK, "2")
    # vạch đơn
    s.append(L(542, 192, 822, 192, INK, "2.6"))
    s.append(L(592, 192, 592, 214, INK, "1.8"))
    s.append(L(772, 192, 772, 214, INK, "1.8"))
    s.append(T(586, 208, "OK", 10, OK, "700", "end"))
    s.append(T(778, 208, "NG", 10, BAD, "700"))
    s += _buoc(592, 214, "Chuyển tiếp", 96, fill="#DFF0E4", edge=OK)
    s += _buoc(772, 214, "Loại bỏ", 96, fill="#FBE9E7", edge=BAD)
    s.append(L(592, 248, 592, 272, INK, "1.8"))
    s.append(L(772, 248, 772, 272, INK, "1.8"))
    s.append(L(542, 272, 822, 272, INK, "2.6"))
    s += arw(cx2, 272, cx2, 296, INK, "2")
    s += _buoc(cx2, 296, "Bước sau")

    s.append(R(490, 344, 372, 56, fill="#EAF1F6", stroke=INK2, sw="1.2"))
    s.append(T(504, 364, "⭐  Chỉ MỘT nhánh chạy.", 11, INK, "700"))
    s.append(T(504, 382, "Nhánh còn lại không bao giờ được kích hoạt lần này.", 10.5, INK2))

    # Cảnh báo chung
    s.append(R(24, 426, 852, 42, fill="#FBE9E7", stroke=BAD, sw="1.3"))
    s.append(T(38, 452,
               "⚠⚠  Vẽ nhầm vạch ĐƠN thành vạch ĐÔI: trình tự sẽ CHỜ một nhánh không bao giờ chạy "
               "— máy đứng im vĩnh viễn, và không có báo động nào.",
               11.5, "#7A2E24", "700"))
    return save(s, "ch21", "hinh_21_1_hai_kieu_nhanh_sfc.svg")


if __name__ == "__main__":
    fig_21_1()
    for line in log:
        print(line)
