# -*- coding: utf-8 -*-
"""Hình chuyên biệt của Chương 36 — ba tháng trôi dạt mà không ai thấy.

Luận điểm trung tâm của chương: biến tần BIẾT máy đang xuống sức, còn PLC thì
không, vì nối với nhau bằng một sợi dây analog một chiều. Chuyện đó là chuyện
CỦA THỜI GIAN — bảng chữ không kể được, đồ thị thì kể được (bất biến B13).

Chạy:  python tools/sinh_hinh_ch36.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sinh_hinh import (  # noqa: E402
    INK, INK2, RULE, CUR, OK, BAD, WARN, PANEL, T, R, L, arw, head, save, log,
)

X0, X1 = 196, 828            # hai mép trái/phải của vùng vẽ
N = 64                       # số điểm lấy mẫu của mỗi đường


def _poly(pts, mau, sw="2.4", dash=None):
    d = " stroke-dasharray='%s'" % dash if dash else ""
    return ("<polyline points='%s' fill='none' stroke='%s' stroke-width='%s'%s/>"
            % (" ".join("%.1f,%.1f" % p for p in pts), mau, sw, d))


def _hang(s, y, cao, nhan1, nhan2, ham, v0, v1, mau, moc=None, don_vi=""):
    """Một băng đồ thị: nền, nhãn trái, mốc nghiệm thu, đường cong."""
    s.append(R(X0, y, X1 - X0, cao, fill=PANEL, stroke=RULE, sw="1"))
    s.append(T(24, y + 18, nhan1, 11, INK, "700"))
    s.append(T(24, y + 33, nhan2, 9.5, INK2))

    def toa_do(v):               # giá trị → toạ độ y trong băng
        return y + cao - 8 - (v - v0) / (v1 - v0) * (cao - 16)

    if moc is not None:                      # giá trị ghi lại lúc nghiệm thu (Bẫy 8)
        ym = toa_do(moc)
        s.append(L(X0, ym, X1, ym, WARN, "1.4", "6,4"))
        s.append(T(X1 + 6, ym + 4, "mốc %d%s" % (moc, don_vi), 9, WARN, "700"))

    pts = [(X0 + (X1 - X0) * i / (N - 1.0), toa_do(ham(i / (N - 1.0))))
           for i in range(N)]
    s.append(_poly(pts, mau))
    cuoi = ham(1.0)
    s.append(T(X1 - 8, toa_do(cuoi) + (-9 if (moc is None or cuoi >= moc) else 17),
               "%d%s" % (round(cuoi), don_vi), 9.5, mau, "700", "end"))


def fig_36_1():
    """Ba đường trôi dạt, và cái PLC nhìn thấy chỉ là đường trên cùng."""
    W, H = 900, 500
    s = head(W, H, "Hình 36.1 — Ba tháng trôi dạt, và vì sao không ai thấy",
             "Cùng một cỗ máy, cùng một quãng thời gian. Ba đại lượng dưới đây đều CÓ SẴN trong biến "
             "tần; PLC chỉ nhìn được đường trên cùng.")

    _hang(s, 92, 54, "Lệnh đặt tốc độ", "AO_ConvSpeed — PLC ghi ra",
          lambda t: 70.0, 55, 75, OK, don_vi=" %")
    s.append(T((X0 + X1) / 2, 92 + 30, "PLC ghi 70 % và không bao giờ đổi — "
                                       "nhìn từ PLC thì mọi thứ vẫn bình thường",
               10, OK, "700", "middle"))

    _hang(s, 162, 60, "Tốc độ thực của động cơ", "biến tần đo được, PLC không đọc",
          lambda t: 70.0 - 6.2 * t * t, 60, 73, CUR, moc=70, don_vi=" %")

    _hang(s, 238, 60, "Dòng động cơ (% Iđm)", "biến tần đo được, PLC không đọc",
          lambda t: 55.0 + 37.0 * t * t, 45, 102, CUR, moc=55, don_vi=" %")

    # ── băng bit số: đang giới hạn dòng ──────────────────────────────
    yb, hb = 314, 26
    s.append(R(X0, yb, X1 - X0, hb, fill="#FFFFFF", stroke=RULE, sw="1"))
    s.append(T(24, yb + 12, "Bit \"đang giới hạn dòng\"", 11, INK, "700"))
    s.append(T(24, yb + 26, "biến tần bật cờ này, PLC không đọc", 9.5, INK2))
    for a, b in [(0.52, 0.56), (0.62, 0.67), (0.71, 0.78), (0.82, 1.0)]:
        xa, xb = X0 + (X1 - X0) * a, X0 + (X1 - X0) * b
        s.append("<rect x='%.1f' y='%d' width='%.1f' height='%d' fill='%s' opacity='0.85'/>"
                 % (xa, yb + 4, xb - xa, hb - 8, BAD))
    s.append(T(X1 + 6, yb + 17, "bật", 9, BAD, "700"))

    # ── trục thời gian ───────────────────────────────────────────────
    yt = yb + hb + 6
    s.append(L(X0, yt, X1, yt, INK, "1.4"))
    for frac, nhan in [(0.0, "nghiệm thu"), (0.33, "tháng 1"),
                       (0.66, "tháng 2"), (1.0, "tháng 3")]:
        x = X0 + (X1 - X0) * frac
        s.append(L(x, yt, x, yt + 6, INK, "1.4"))
        s.append(T(x, yt + 20, nhan, 10, INK2, "400",
                   "start" if frac == 0 else ("end" if frac == 1 else "middle")))
    s.append(T((X0 + X1) / 2, yt + 38, "⚠ Triệu chứng duy nhất mà nhà máy nhìn thấy: "
                                       "chu kỳ máy dài thêm khoảng 8 %",
               11, BAD, "700", "middle"))

    # ── kết luận ─────────────────────────────────────────────────────
    s.append(R(24, 404, 852, 82, fill="#FDF6E7", stroke=WARN, sw="1.3"))
    s.append(T(38, 428, "⭐⭐ Không có gì hỏng, và không có báo động nào nổ. "
                        "Biến tần đang làm ĐÚNG việc của nó: giảm tốc để khỏi quá dòng.",
               11.5, "#7A5B08", "700"))
    s.append(T(38, 450, "⭐ Ba đường dưới cùng nằm sẵn trong biến tần suốt ba tháng. "
                        "Thứ thiếu không phải phép đo — mà là ĐƯỜNG ĐỌC VỀ.", 11, INK))
    s.append(T(38, 470, "⚡ Và đường \"mốc\" màu vàng là thứ phải ghi lại lúc nghiệm thu: "
                        "không có mốc thì có đọc về cũng không biết đã trôi bao nhiêu.", 11, INK))
    return save(s, "ch36", "hinh_36_1_troi_dat.svg")


if __name__ == "__main__":
    fig_36_1()
    print(log[-1])
