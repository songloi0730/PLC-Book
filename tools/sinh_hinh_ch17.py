# -*- coding: utf-8 -*-
"""Hình 17.1 — sơ đồ thời gian ba loại timer."""
import os, math, xml.etree.ElementTree as ET

ROOT = r"C:/Users/dinhn/OneDrive/Study/Chung/PLC_Programming_Book/assets"
INK = "#1A1D21"; INK2 = "#565E66"; RULE = "#9AA3AB"
CUR = "#C0392B"; OK = "#2E7D4F"; BAD = "#B03A2E"; WARN = "#B8860B"
PANEL = "#F4F5F7"; BG = "#FFFFFF"; BLUE = "#2C5F8D"
F = "font-family=\"Segoe UI,Roboto,Helvetica,Arial,sans-serif\""


def T(x, y, t, sz=12, fill=INK, w="400", a="start"):
    return "<text x='%d' y='%d' %s font-size='%s' font-weight='%s' fill='%s' text-anchor='%s'>%s</text>" % (
        x, y, F, sz, w, fill, a, t.replace("&", "&amp;"))


def R(x, y, w, h, fill=PANEL, stroke=INK, sw="1.4", rx="3"):
    return "<rect x='%d' y='%d' width='%d' height='%d' rx='%s' fill='%s' stroke='%s' stroke-width='%s'/>" % (
        x, y, w, h, rx, fill, stroke, sw)


def L(x1, y1, x2, y2, st=INK, sw="1.6", dash=None):
    d = " stroke-dasharray='%s'" % dash if dash else ""
    return "<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='%s'%s/>" % (x1, y1, x2, y2, st, sw, d)


def trace(y, spans, xL, xR, col=INK):
    """Vẽ một tín hiệu số. spans = [(bắt đầu, kết thúc), …]"""
    lo, hi = y + 20, y - 14
    p = []
    cur = xL
    for a, b in spans:
        p.append(L(cur, lo, a, lo, col, "2.4"))
        p.append(L(a, lo, a, hi, col, "2.4"))
        p.append(L(a, hi, b, hi, col, "2.4"))
        p.append(L(b, hi, b, lo, col, "2.4"))
        cur = b
    p.append(L(cur, lo, xR, lo, col, "2.4"))
    return p


W, H = 940, 520
xL, xR = 190, 900
PT = 90
x1, x2 = 240, 440          # xung DÀI
x3, x4 = 570, 620          # xung NGẮN (ngắn hơn PT)

s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' width='%d' height='%d'>" % (W, H, W, H),
     "<rect width='%d' height='%d' fill='%s'/>" % (W, H, BG),
     T(24, 34, "Hình 17.1 — Ba loại timer: cùng một tín hiệu vào, ba kết quả khác nhau", 16, INK, "700"),
     T(24, 56, "Xung thứ hai NGẮN HƠN thời gian đặt (PT) — đây là chỗ ba loại timer bộc lộ khác biệt rõ nhất.", 12, INK2)]

rows = [(130, "IN", "tín hiệu vào", INK, [(x1, x2), (x3, x4)],
         "hai xung: một dài, một ngắn hơn PT"),
        (230, "TON", "trễ sườn lên", BLUE, [(x1 + PT, x2)],
         "lên SAU khi vào giữ đủ PT · xung ngắn KHÔNG kích được"),
        (330, "TOF", "trễ sườn xuống", OK, [(x1, x2 + PT), (x3, x4 + PT)],
         "lên NGAY · tắt SAU khi vào tụt đủ PT"),
        (430, "TP", "tạo xung", CUR, [(x1, x1 + PT), (x3, x3 + PT)],
         "lên NGAY · giữ ĐÚNG PT, không phụ thuộc vào sau đó")]

# lưới dọc mốc thời gian
for x in (x1, x2, x3, x4):
    s.append(L(x, 112, x, 470, RULE, "0.9", "3,4"))

for y, nm, sub, col, spans, note in rows:
    s.append(T(24, y - 2, nm, 13, col, "700"))
    s.append(T(24, y + 15, sub, 9.8, INK2))
    s += trace(y, spans, xL, xR, col)
    s.append(T(xR + 4, y + 6, "", 9))
    s.append(T(190, y + 40, note, 9.8, INK2))

# thanh PT
ypt = 84
s.append(L(x1, ypt, x1 + PT, ypt, WARN, "2.2"))
s.append(L(x1, ypt - 5, x1, ypt + 5, WARN, "2.2"))
s.append(L(x1 + PT, ypt - 5, x1 + PT, ypt + 5, WARN, "2.2"))
s.append(T(x1 + PT // 2, ypt - 9, "PT (thời gian đặt)", 10, WARN, "700", "middle"))

# nhãn xung
s.append(T((x1 + x2) // 2, 106, "xung DÀI hơn PT", 10, INK2, "600", "middle"))
s.append(T((x3 + x4) // 2, 106, "xung NGẮN hơn PT", 10, BAD, "700", "middle"))

# ghi chú then chốt
s.append(R(24, 476, W - 48, 34, fill="#FDF6E7", stroke=WARN, sw="1.2"))
s.append(T(42, 498, "Chú ý cột xung ngắn: TON không kích được (điều kiện chưa đủ bền) · TOF và TP vẫn cho ra xung đủ PT. Đây là tiêu chí chọn loại timer.", 11, "#7A5B08"))
s.append("</svg>")

d = os.path.join(ROOT, "ch17"); os.makedirs(d, exist_ok=True)
p = os.path.join(d, "hinh_17_1_timer.svg")
open(p, "w", encoding="utf-8").write("\n".join(s))
ET.parse(p)
import pymupdf
pymupdf.open(p)[0].get_pixmap(dpi=105).save(
    r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/p171.png")
open(r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/figlog.txt", "w").write("OK fig17")
