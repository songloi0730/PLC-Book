# -*- coding: utf-8 -*-
"""Hình chuyên biệt của Chương 33 — RTD đấu 2, 3 và 4 dây.

Hình ASCII cũ trong chương vẽ ba cách như ba bó dây song song giống hệt nhau,
nên nó KHÔNG nói được điều duy nhất đáng nói: sợi nào mang dòng, chỗ nào đo áp,
và vì sao thêm một sợi lại bù được sai số. Đó đúng là "đường đi của dòng điện"
— tiêu chí số một của bất biến B13.

Chạy:  python tools/sinh_hinh_ch33.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sinh_hinh import (  # noqa: E402
    INK, INK2, RULE, CUR, OK, BAD, WARN, PANEL, T, R, L, arw, head, save, log,
)

XR, WR = 200, 80          # hộp RTD
XM, WM = 600, 118         # hộp module
XD = 520                  # cột đặt ký hiệu điện trở của dây
SENSE = "#1F5F8B"         # dây ĐO — không mang dòng


def _day(s, y, mau, sw="2.4"):
    """Một sợi dây nối RTD với module, kèm ký hiệu điện trở của chính nó."""
    s.append(L(XR + WR, y, XM, y, mau, sw))
    s.append(R(XD - 13, y - 7, 26, 14, fill="#FFFFFF", stroke=mau, sw="1.3", rx="1"))
    s.append(T(XD, y + 4, "R", 8, mau, "700", "middle"))


def _hang(s, ry, so_day, tieu_de, ket_luan, mau_kl, trai, phai, duoi, mau_duoi):
    s.append(R(16, ry, 868, 142, fill="#FFFFFF", stroke=RULE, sw="1.1"))
    s.append(T(30, ry + 26, tieu_de, 13, INK, "700"))
    s.append(T(30, ry + 45, ket_luan, 9.5, mau_kl, "700"))
    for k, d in enumerate(trai):
        s.append(T(30, ry + 70 + k * 15, d, 9, INK2))

    gy = ry + 70
    s.append(R(XR, gy - 24, WR, 48, fill=PANEL, stroke=INK, sw="1.5"))
    s.append(T(XR + WR / 2, gy - 3, "RTD", 11.5, INK, "700", "middle"))
    s.append(T(XR + WR / 2, gy + 13, "Pt100", 9, INK2, "400", "middle"))
    s.append(R(XM, gy - 38, WM, 76, fill=PANEL, stroke=INK, sw="1.5"))
    s.append(T(XM + WM / 2, gy - 22, "MODULE", 10.5, INK, "700", "middle"))

    if so_day == 2:
        ys = [gy - 16, gy + 16]
        for y in ys:
            _day(s, y, CUR)
        s += arw(XR + WR + 18, ys[0], XR + WR + 66, ys[0], CUR, "2.2")
        s += arw(XM - 18, ys[1], XM - 66, ys[1], CUR, "2.2")
        s.append(L(XM + 12, ys[0], XM + 12, ys[1], INK, "1.6"))
        s.append(L(XM + 12, gy, XM + 34, gy, INK, "1.6"))
        s.append("<circle cx='%d' cy='%d' r='13' fill='#FFFFFF' stroke='%s' stroke-width='1.6'/>"
                 % (XM + 47, gy, INK))
        s.append(T(XM + 47, gy + 5, "V", 11, INK, "700", "middle"))
    elif so_day == 3:
        ys = [gy - 24, gy, gy + 24]
        _day(s, ys[0], CUR)
        _day(s, ys[1], SENSE)
        _day(s, ys[2], CUR)
        s += arw(XR + WR + 18, ys[0], XR + WR + 66, ys[0], CUR, "2.2")
        s += arw(XM - 18, ys[2], XM - 66, ys[2], CUR, "2.2")
        s.append(T(300, ys[1] - 9, "sợi thứ ba: KHÔNG mang dòng", 8.5, SENSE, "700"))
    else:
        ys = [gy - 30, gy - 10, gy + 10, gy + 30]
        _day(s, ys[0], CUR)
        _day(s, ys[1], SENSE)
        _day(s, ys[2], SENSE)
        _day(s, ys[3], CUR)
        s += arw(XR + WR + 18, ys[0], XR + WR + 66, ys[0], CUR, "2.2")
        s += arw(XM - 18, ys[3], XM - 66, ys[3], CUR, "2.2")
        s.append(T(300, ys[1] - 8, "hai sợi ĐO: dòng ≈ 0", 8.5, SENSE, "700"))

    s.append(T((XR + WR + XM + WM) / 2, ry + 130, duoi, 9, mau_duoi, "700", "middle"))
    for k, d in enumerate(phai):
        s.append(T(XM + WM + 16, gy - 6 + k * 16, d, 9.5, INK if k == 0 else INK2,
                   "700" if k == 0 else "400"))


def fig_33_1():
    """Hai, ba, bốn dây: khác nhau ở chỗ dây nào mang dòng và đo áp ở đâu."""
    W, H = 900, 646
    s = head(W, H, "Hình 33.1 — RTD đấu 2, 3 và 4 dây: dòng đi đường nào",
             "Ba cách trông giống nhau trên bản vẽ. Khác biệt duy nhất, và là khác biệt quyết định: "
             "sợi nào mang dòng kích thích, và điện áp được đo ở đâu.")
    s.append(T(24, 76, "Nét đỏ = sợi mang dòng kích thích   ·   Nét xanh = sợi chỉ để ĐO   ·   "
                       "ô  R  = điện trở của chính sợi dây", 10.5, INK2))

    _hang(s, 88, 2, "2 DÂY", "⚠ Không bù được", BAD,
          ["Điện trở hai sợi dây", "nằm TRONG phép đo"],
          ["Module đo:", "R(RTD) + 2·R(dây)"],
          "⚠ Module chỉ đo được tại chân của chính nó — dây nằm trong kết quả", BAD)

    _hang(s, 238, 3, "3 DÂY", "⭐ Bù được (có giả định)", OK,
          ["Sợi thứ ba cho module", "đo riêng điện trở dây"],
          ["Đo được R một sợi,", "rồi trừ khỏi kết quả"],
          "⚠ Giả định: ba sợi cùng loại, cùng chiều dài, đi cùng một cáp", WARN)

    _hang(s, 388, 4, "4 DÂY", "⭐ Không cần giả định gì", OK,
          ["Tách hẳn mạch cấp dòng", "khỏi mạch đo áp"],
          ["Sợi đo không có dòng", "→ không có sụt áp"],
          "⭐ Đo áp đúng trên hai đầu RTD — dây dài bao nhiêu cũng được", OK)

    s.append(R(16, 546, 868, 88, fill="#FDF6E7", stroke=WARN, sw="1.3"))
    s.append(T(32, 570, "⭐⭐ Vì sao 3 dây là mặc định của ngành: nó bù được gần hết sai số với "
                        "chi phí thêm ĐÚNG MỘT SỢI DÂY.", 11.5, "#7A5B08", "700"))
    s.append(T(32, 592, "⚡ Bước từ 2 lên 3 dây cải thiện rất nhiều; bước từ 3 lên 4 dây cải thiện "
                        "thêm rất ít trong điều kiện máy công nghiệp.", 11, INK))
    s.append(T(32, 612, "⚠ Và nhớ giả định của cách 3 dây: nối thêm một đoạn dây khác loại vào MỘT "
                        "sợi là phá giả định đó — sai số quay lại mà không báo gì.", 11, INK))
    return save(s, "ch33", "hinh_33_1_rtd_2_3_4_day.svg")


if __name__ == "__main__":
    fig_33_1()
    print(log[-1])
