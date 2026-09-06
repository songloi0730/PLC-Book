# -*- coding: utf-8 -*-
"""Hình chuyên biệt của Chương 35 — ba đường đáp ứng của bộ điều khiển.

Dùng chung bộ token thị giác ở `sinh_hinh.py`.
Chạy:  python tools/sinh_hinh_ch35.py
"""
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sinh_hinh import (  # noqa: E402
    INK, INK2, RULE, CUR, OK, BAD, WARN, T, R, L, arw, head, save, log,
)


def poly(pts, col, sw="2.4", dash=None):
    d = " stroke-dasharray='%s'" % dash if dash else ""
    s = " ".join("%.1f,%.1f" % (x, y) for x, y in pts)
    return ("<polyline points='%s' fill='none' stroke='%s' stroke-width='%s'%s "
            "stroke-linejoin='round'/>" % (s, col, sw, d))


def fig_35_1():
    """P thuần để lại sai lệch tĩnh; thêm I thì hết; P quá lớn thì dao động."""
    W, H = 900, 424
    s = head(W, H, "Hình 35.1 — Vì sao P thuần luôn để lại sai lệch, và thêm I thì hết",
             "Cùng một quá trình, cùng một điểm đặt. Chỉ khác cách chỉnh — và ba kết quả khác hẳn nhau.")

    # Khung đồ thị
    x0, x1 = 88, 628
    yb, yt = 336, 104          # đáy và đỉnh vùng vẽ
    y_sp = 168                 # điểm đặt
    s.append(L(x0, yb, x1, yb, INK, "1.6"))          # trục thời gian
    s.append(L(x0, yb, x0, yt, INK, "1.6"))          # trục giá trị
    s.append(T(x1 + 6, yb + 4, "thời gian", 10.5, INK2))
    s.append(T(x0 - 6, yt - 8, "giá trị đo", 10.5, INK2, "400", "end"))

    # Điểm đặt
    s.append(L(x0, y_sp, x1, y_sp, RULE, "1.6", "6,4"))
    s.append(T(x0 + 6, y_sp - 8, "điểm đặt", 10.5, INK, "700"))

    n = 120
    def xs(i):
        return x0 + (x1 - x0) * i / n

    # A — P thuần: dừng lại DƯỚI điểm đặt (sai lệch tĩnh)
    y_off = y_sp + 40
    a = [(xs(i), yb - (yb - y_off) * (1 - math.exp(-3.2 * i / n))) for i in range(n + 1)]
    s.append(poly(a, WARN))

    # Đáp ứng bậc hai chuẩn — xuất phát từ 0 như mọi đường khác
    def dap_ung(k, w, T=4.6):
        pts = []
        for i in range(n + 1):
            t = T * i / n
            v = 1 - math.exp(-k * t) * (math.cos(w * t) + (k / w) * math.sin(w * t))
            pts.append((xs(i), yb - (yb - y_sp) * v))
        return pts

    # B — P + I: tới đúng điểm đặt, gần như không vọt lố
    s.append(poly(dap_ung(1.5, 1.5), OK))

    # C — P quá lớn: vọt lố mạnh rồi dao động, lâu tắt
    s.append(poly(dap_ung(1.1, 3.4), BAD, "2.2"))

    # Đánh dấu sai lệch tĩnh
    xm = x0 + (x1 - x0) * 0.955
    s += arw(xm, y_sp, xm, y_off, CUR, "2")
    s += arw(xm, y_off, xm, y_sp, CUR, "2")
    s.append(T(xm - 14, (y_sp + y_off) / 2 + 4, "sai lệch tĩnh — không bao giờ tự hết", 11, CUR, "700", "end"))

    # Chú giải
    xl, yl = 664, 118
    legend = [(WARN, "P thuần", "Dừng DƯỚI điểm đặt và ở lại đó"),
              (OK, "P + I", "Tới đúng điểm đặt — I xoá sai lệch"),
              (BAD, "P quá lớn", "Dao động quanh điểm đặt, lâu tắt")]
    for i, (col, ten, mo) in enumerate(legend):
        y = yl + i * 56
        s.append(L(xl, y, xl + 30, y, col, "3"))
        s.append(T(xl + 38, y + 4, ten, 12, INK, "700"))
        s.append(T(xl, y + 24, mo, 10.5, INK2))

    # Ghi chú
    s.append(R(26, 356, 848, 48, fill="#FDF6E7", stroke=WARN, sw="1.2"))
    s.append(T(40, 376,
               "⚠  Sai lệch tĩnh KHÔNG phải lỗi chỉnh định — nó là bản chất của P thuần: "
               "hết sai lệch thì hết tín hiệu ra, nên nó phải giữ lại một chút sai lệch để còn ngõ ra.",
               11, "#7A5B08"))
    s.append(T(40, 394,
               "⭐  Tăng P để bù sai lệch tĩnh sẽ dẫn tới đường màu đỏ. Cách đúng là thêm I "
               "— và khi đó phải lo chống bão hoà tích phân (mục 35.5).",
               11, "#7A5B08"))
    return save(s, "ch35", "hinh_35_1_ba_duong_dap_ung.svg")


if __name__ == "__main__":
    fig_35_1()
    for line in log:
        print(line)
