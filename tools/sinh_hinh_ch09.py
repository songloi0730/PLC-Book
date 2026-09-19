# -*- coding: utf-8 -*-
"""Hình chuyên biệt của Chương 9 — ngõ vào kiểu sink và kiểu source.

Hai kiểu chỉ khác nhau ở CHÂN CHUNG nối vào đâu, và từ đó khác nhau ở CHIỀU DÒNG
chạy qua ngõ vào. Bảng chữ nói được cặp "sink ↔ PNP" nhưng không nói được vì sao;
mũi tên dòng thì nói ngay (bất biến B13: đường đi của dòng điện thì vẽ).

Chạy:  python tools/sinh_hinh_ch09.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sinh_hinh import (  # noqa: E402
    INK, INK2, RULE, CUR, OK, BAD, PANEL, T, R, L, arw, head, save, log,
)

SUP = "#9AA3AB"          # dây cấp nguồn cho cảm biến — nét xám mảnh, đọc như nền


def _hop(s, x, y, w, h, dong1, dong2):
    s.append(R(x, y, w, h, fill=PANEL, stroke=INK, sw="1.5"))
    s.append(T(x + w / 2, y + 20, dong1, 10.5, INK, "700", "middle"))
    s.append(T(x + w / 2, y + 35, dong2, 9.5, INK2, "400", "middle"))


def _khung(s, x, y, w, h, tieu_de, phu, mau, nen):
    s.append(R(x, y, w, h, fill="#FFFFFF", stroke=RULE, sw="1.2"))
    s.append(R(x, y, w, 34, fill=nen, stroke=mau, sw="1.3"))
    s.append(T(x + w / 2, y + 15, tieu_de, 12, mau, "700", "middle"))
    s.append(T(x + w / 2, y + 28, phu, 9.5, INK2, "400", "middle"))


def _mot_khung(s, px, py, sink):
    pw, ph = 410, 336
    _khung(s, px, py, pw, ph,
           "A · Ngõ vào kiểu SINK" if sink else "B · Ngõ vào kiểu SOURCE",
           "chân chung nối 0 V  ·  ghép cảm biến PNP" if sink
           else "chân chung nối +24 V  ·  ghép cảm biến NPN",
           OK if sink else INK2,
           "#DFF0E4" if sink else "#EAF1F6")

    y24, y0 = py + 62, py + 222
    for y, nhan, mau in ((y24, "+24 V", CUR), (y0, "0 V", INK)):
        s.append(L(px + 44, y, px + 330, y, mau, "2"))
        s.append(T(px + 46, y - 8, nhan, 10.5, mau, "700"))

    _hop(s, px + 58, py + 104, 100, 46, "CẢM BIẾN", "PNP" if sink else "NPN")
    _hop(s, px + 206, py + 104, 112, 46, "NGÕ VÀO", "của module")

    # Hai chân nguồn của cảm biến. MỘT trong hai chân nằm trong vòng dòng tín hiệu
    # (PNP lấy dòng từ +24 V, NPN xả dòng xuống 0 V) nên phải vẽ đỏ như phần còn lại
    # của vòng; chân kia chỉ nuôi mạch bên trong cảm biến nên để xám.
    s.append(L(px + 76, y24, px + 76, py + 104, CUR if sink else SUP,
               "2.2" if sink else "1.2"))
    s.append(L(px + 100, py + 150, px + 100, y0, SUP if sink else CUR,
               "1.2" if sink else "2.2"))

    # vòng dòng của tín hiệu
    s.append(L(px + 138, py + 150, px + 138, py + 186, CUR, "2.2"))
    s.append(L(px + 262, py + 150, px + 262, py + 186, CUR, "2.2"))
    if sink:
        s += arw(px + 144, py + 186, px + 258, py + 186, CUR, "2.2")
    else:
        s += arw(px + 256, py + 186, px + 142, py + 186, CUR, "2.2")
    s.append(T(px + 200, py + 206,
               "dòng chạy VÀO module" if sink else "dòng chạy RA khỏi module",
               9.5, CUR, "700", "middle"))

    # chân chung — đúng một sợi dây này quyết định tất cả
    s.append(L(px + 318, py + 127, px + 330, py + 127, CUR, "2.4"))
    if sink:                       # dòng rời module, đi xuống 0 V
        s.append(L(px + 330, py + 127, px + 330, y0 - 34, CUR, "2.4"))
        s += arw(px + 330, y0 - 34, px + 330, y0 - 2, CUR, "2.4")
    else:                          # dòng từ +24 V đi xuống, vào module
        s.append(L(px + 330, y24, px + 330, py + 93, CUR, "2.4"))
        s += arw(px + 330, py + 93, px + 330, py + 125, CUR, "2.4")
    s.append(T(px + 336, py + 123, "chân chung", 9.5, CUR, "700"))
    s.append(T(px + 336, py + 137, "nối 0 V" if sink else "nối +24 V", 9.5, CUR, "700"))

    s.append(T(px + 205, py + 244,
               "Cảm biến ĐẨY +24 V ra dây tín hiệu" if sink
               else "Cảm biến KÉO dây tín hiệu xuống 0 V", 10.5, INK, "700", "middle"))
    s.append(R(px + 22, py + 258, pw - 44, 58, fill="#FDF6E7", stroke=RULE, sw="1"))
    s.append(T(px + 34, py + 278,
               "⭐ Module phải NHẬN dòng về → gọi là ngõ vào sink." if sink
               else "⭐ Module phải CẤP dòng ra → gọi là ngõ vào source.", 10.5, INK, "700"))
    s.append(T(px + 34, py + 298,
               "Nên nó ghép với cảm biến PNP." if sink
               else "Nên nó ghép với cảm biến NPN.", 10.5, INK2))


def fig_09_1():
    """Sink và source: cùng một module, khác nhau đúng một sợi dây chân chung."""
    W, H = 900, 530
    s = head(W, H, "Hình 9.1 — Ngõ vào kiểu sink và kiểu source",
             "Hai kiểu khác nhau đúng một chỗ: chân chung nối 0 V hay nối +24 V. "
             "Từ đó suy ra chiều dòng, rồi suy ra phải ghép cảm biến loại nào.")
    s.append(T(24, 76, "Nét đỏ đậm = vòng dòng tín hiệu, khép kín từ +24 V về 0 V   ·   "
                       "Nét xám mảnh = chân nguồn còn lại của cảm biến", 10.5, INK2))
    _mot_khung(s, 24, 88, True)
    _mot_khung(s, 466, 88, False)

    s.append(R(24, 438, 852, 72, fill="#FBE9E7", stroke=BAD, sw="1.3"))
    s.append(T(38, 462,
               "⚠⚠  Phần lớn module đời mới là loại CHUYỂN ĐƯỢC: cùng một module, đấu chân chung "
               "vào 0 V thì thành sink, vào +24 V thì thành source.", 11.5, "#7A2E24", "700"))
    s.append(T(38, 482,
               "⭐ Nghĩa là KHÔNG nhìn ra kiểu đấu từ hình dáng module — chỉ nhìn ra từ sợi dây chân "
               "chung. Ghi rõ kiểu đã chọn lên bản vẽ và lên nhãn", 11, INK))
    s.append(T(38, 500,
               "trong tủ; người sửa máy hai năm sau không đoán ra được.", 11, INK))
    return save(s, "ch09", "hinh_09_1_sink_source.svg")


if __name__ == "__main__":
    fig_09_1()
    print(log[-1])
