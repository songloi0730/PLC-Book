# -*- coding: utf-8 -*-
"""Hình 25.1 — máy trạng thái. Mũi tên vẽ bằng đa giác tường minh (marker SVG không render ổn định)."""
import os, math, xml.etree.ElementTree as ET

ROOT = r"C:/Users/dinhn/OneDrive/Study/Chung/PLC_Programming_Book/assets"
INK = "#1A1D21"; INK2 = "#565E66"; RULE = "#9AA3AB"
CUR = "#C0392B"; OK = "#2E7D4F"; BAD = "#B03A2E"; WARN = "#B8860B"
PANEL = "#F4F5F7"; BG = "#FFFFFF"
F = "font-family=\"Segoe UI,Roboto,Helvetica,Arial,sans-serif\""


def esc(t):
    return t.replace("&", "&amp;")


def T(x, y, txt, size=12, fill=INK, weight="400", anchor="start"):
    return "<text x='%d' y='%d' %s font-size='%s' font-weight='%s' fill='%s' text-anchor='%s'>%s</text>" % (
        x, y, F, size, weight, fill, anchor, esc(txt))


def R(x, y, w, h, fill=PANEL, stroke=INK, sw="1.4", rx="3"):
    return "<rect x='%d' y='%d' width='%d' height='%d' rx='%s' fill='%s' stroke='%s' stroke-width='%s'/>" % (
        x, y, w, h, rx, fill, stroke, sw)


def L(x1, y1, x2, y2, stroke=INK, sw="1.6", dash=None):
    d = " stroke-dasharray='%s'" % dash if dash else ""
    return "<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='%s'%s/>" % (x1, y1, x2, y2, stroke, sw, d)


def arw(x1, y1, x2, y2, col=INK, sw="2", dash=None):
    """Đường + đầu mũi tên đa giác."""
    ang = math.atan2(y2 - y1, x2 - x1)
    hl, hw = 10.0, 5.0
    bx, by = x2 - hl * math.cos(ang), y2 - hl * math.sin(ang)
    p1 = (bx - hw * math.sin(ang), by + hw * math.cos(ang))
    p2 = (bx + hw * math.sin(ang), by - hw * math.cos(ang))
    out = [L(x1, y1, int(bx), int(by), col, sw, dash)]
    out.append("<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' fill='%s'/>" % (x2, y2, p1[0], p1[1], p2[0], p2[1], col))
    return out


W, H = 940, 560
s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' width='%d' height='%d'>" % (W, H, W, H),
     "<rect width='%d' height='%d' fill='%s'/>" % (W, H, BG),
     T(24, 34, "Hình 25.1 — Máy trạng thái chuẩn cho một cỗ máy", 16, INK, "700"),
     T(24, 56, "Tại mọi thời điểm máy ở ĐÚNG MỘT trạng thái. Đường đỏ: lỗi xảy ra được ở bất cứ đâu, nên mọi trạng thái đều phải có lối vào Alarm.", 12, INK2)]

bw, bh = 152, 54
yA, yB, yC = 112, 232, 384
xU, xH, xI, xR = 30, 250, 470, 690


def st(x, y, name, desc, fill=PANEL, stroke=INK):
    return [R(x, y, bw, bh, fill=fill, stroke=stroke, sw="1.7", rx="7"),
            T(x + bw // 2, y + 24, name, 12.5, INK, "700", "middle"),
            T(x + bw // 2, y + 41, desc, 9.5, INK2, "400", "middle")]


s += st(xU, yA, "Uninitialized", "vừa cấp nguồn")
s += st(xH, yA, "Homing", "đang về gốc")
s += st(xI, yA, "Idle", "sẵn sàng, chờ lệnh")
s += st(xR, yA, "Running", "đang chạy chu trình", "#E8F2EC", OK)
s += st(xR, yB, "Hold", "dừng, GIỮ nguyên vị trí")
s += st(xH, yC, "Resetting", "đang xoá lỗi")
s += st(xI, yC, "Alarm", "có lỗi, đã dừng", "#F8E7E4", BAD)

ym = yA + bh // 2
for xa, xb, lbl in ((xU, xH, "Reset"), (xH, xI, "về gốc xong"), (xI, xR, "Start")):
    s += arw(xa + bw, ym, xb - 4, ym)
    s.append(T((xa + bw + xb) // 2, ym - 12, lbl, 10, INK2, "600", "middle"))

# Running <-> Hold
s += arw(xR + 44, yA + bh, xR + 44, yB - 4)
s.append(T(xR + 36, (yA + bh + yB) // 2 + 4, "Hold", 10, INK2, "600", "end"))
s += arw(xR + 110, yB, xR + 110, yA + bh + 4)
s.append(T(xR + 118, (yA + bh + yB) // 2 + 4, "Start", 10, INK2, "600"))

# Hold -> Idle  (đi vòng dưới, tránh đè hộp)
yh = yB + bh + 24
xmid = xI + bw // 2
s.append(L(xR + bw // 2, yB + bh, xR + bw // 2, yh, INK, "2"))
s.append(L(xR + bw // 2, yh, xmid, yh, INK, "2"))
s += arw(xmid, yh, xmid, yA + bh + 4)
s.append(T((xR + bw // 2 + xmid) // 2, yh + 16, "giữ Stop 2 giây → huỷ chu trình", 10, INK2, "600", "middle"))

# mọi trạng thái -> Alarm
yband = 340
for x in (xU + bw // 2, xH + bw // 2 + 30, xR + bw // 2 + 40):
    s.append(L(x, yA + bh if x != xR + bw // 2 + 40 else yB + bh, x, yband, CUR, "1.5", "5,4"))
s.append(L(xU + bw // 2, yband, xR + bw // 2 + 40, yband, CUR, "1.8"))
s += arw(xI + bw // 2 + 55, yband, xI + bw // 2 + 55, yC - 4, CUR, "2.4")
s.append(T(xR + bw // 2 + 52, yband + 5, "từ MỌI trạng thái", 10.5, CUR, "700"))

# Alarm -> Resetting
s += arw(xI - 4, yC + bh // 2, xH + bw + 4, yC + bh // 2)
s.append(T((xI + xH + bw) // 2, yC - 10, "Reset (lỗi đã hết)", 10, INK2, "600", "middle"))

# Resetting -> Homing
xres = xH + 40
s.append(L(xres, yC, xres, yA + bh + 34, INK, "2"))
s += arw(xres, yA + bh + 34, xres, yA + bh + 4)
s.append(T(xres - 10, yA + bh + 52, "xoá xong → về gốc lại", 10, INK2, "600", "end"))

s.append(R(24, 486, W - 48, 52, fill="#FDF6E7", stroke=WARN, sw="1.2"))
s.append(T(42, 508, "⚠  E-Stop KHÔNG phải một trạng thái ở đây. Nó là mạch cứng cắt nguồn cơ cấu, hoạt động kể cả khi CPU treo.", 11.5, "#7A5B08", "600"))
s.append(T(42, 526, "Máy trạng thái chỉ PHẢN ỨNG với việc E-Stop đã bị nhấn (chuyển sang Alarm), chứ không THỰC HIỆN việc dừng — xem Chương 47.", 11, "#7A5B08"))
s.append("</svg>")

d = os.path.join(ROOT, "ch25"); os.makedirs(d, exist_ok=True)
p = os.path.join(d, "hinh_25_1_may_trang_thai.svg")
open(p, "w", encoding="utf-8").write("\n".join(s))
ET.parse(p)
import pymupdf
pymupdf.open(p)[0].get_pixmap(dpi=105).save(
    r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/p251.png")
open(r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/figlog.txt", "w").write("OK fig25")
