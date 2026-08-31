# -*- coding: utf-8 -*-
"""Hình 27.1 — ba tầng kiến trúc chương trình."""
import os, math, xml.etree.ElementTree as ET

ROOT = r"C:/Users/dinhn/OneDrive/Study/Chung/PLC_Programming_Book/assets"
INK = "#1A1D21"; INK2 = "#565E66"; RULE = "#9AA3AB"
CUR = "#C0392B"; OK = "#2E7D4F"; BAD = "#B03A2E"; WARN = "#B8860B"
PANEL = "#F4F5F7"; BG = "#FFFFFF"; BLUE = "#2C5F8D"; BLUEBG = "#E7EFF6"
F = "font-family=\"Segoe UI,Roboto,Helvetica,Arial,sans-serif\""


def T(x, y, t, sz=12, fill=INK, w="400", a="start"):
    return "<text x='%d' y='%d' %s font-size='%s' font-weight='%s' fill='%s' text-anchor='%s'>%s</text>" % (
        x, y, F, sz, w, fill, a, t.replace("&", "&amp;"))


def R(x, y, w, h, fill=PANEL, stroke=INK, sw="1.4", rx="3", dash=None):
    d = " stroke-dasharray='%s'" % dash if dash else ""
    return "<rect x='%d' y='%d' width='%d' height='%d' rx='%s' fill='%s' stroke='%s' stroke-width='%s'%s/>" % (
        x, y, w, h, rx, fill, stroke, sw, d)


def L(x1, y1, x2, y2, st=INK, sw="1.6", dash=None):
    d = " stroke-dasharray='%s'" % dash if dash else ""
    return "<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='%s'%s/>" % (x1, y1, x2, y2, st, sw, d)


def arw(x1, y1, x2, y2, col=INK, sw="2.2"):
    ang = math.atan2(y2 - y1, x2 - x1); hl, hw = 10.0, 5.0
    bx, by = x2 - hl * math.cos(ang), y2 - hl * math.sin(ang)
    return [L(x1, y1, int(bx), int(by), col, sw),
            "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' fill='%s'/>" % (
                x2, y2, bx - hw * math.sin(ang), by + hw * math.cos(ang),
                bx + hw * math.sin(ang), by - hw * math.cos(ang), col)]


def cross(cx, cy, r=11, col=BAD):
    return [L(cx - r, cy - r, cx + r, cy + r, col, "3.2"), L(cx - r, cy + r, cx + r, cy - r, col, "3.2")]


W, H = 940, 620
s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' width='%d' height='%d'>" % (W, H, W, H),
     "<rect width='%d' height='%d' fill='%s'/>" % (W, H, BG),
     T(24, 34, "Hình 27.1 — Ba tầng kiến trúc chương trình", 16, INK, "700"),
     T(24, 56, "Mũi tên chỉ đi XUỐNG. Tầng dưới không gọi ngược lên — nó chỉ công bố trạng thái để tầng trên đọc.", 12, INK2)]

# ── dải nền ba tầng
tiers = [(84, 92, "TẦNG MÁY", "chế độ vận hành · lỗi toàn máy · cho phép/cấm"),
         (216, 132, "TẦNG TRẠM", "trình tự xử lý"),
         (388, 118, "TẦNG CƠ CẤU", "một thiết bị")]
for y, h, name, desc in tiers:
    s.append(R(24, y, W - 48, h, fill="#FBFBFC", stroke=RULE, sw="1.3", rx="5"))
    s.append(T(40, y + 22, name, 11.5, INK, "700"))
    s.append(T(40, y + 39, desc, 9.8, INK2))

# ── tầng máy
s.append(R(320, 100, 300, 62, fill="#E8F2EC", stroke=OK, sw="1.7", rx="6"))
s.append(T(470, 124, "Máy trạng thái", 13, INK, "700", "middle"))
s.append(T(470, 143, "Idle / Running / Hold / Alarm …", 10, INK2, "400", "middle"))
s.append(T(470, 156, "+ chủ của tài nguyên dùng chung", 9.5, OK, "600", "middle"))

# ── tầng trạm
for i, (x, nm) in enumerate([(150, "Trạm 1 — tra keo"), (560, "Trạm 2 — sấy UV")]):
    s.append(R(x, 234, 250, 96, fill=BLUEBG, stroke=BLUE, sw="1.7", rx="6"))
    s.append(T(x + 125, 256, nm, 12.5, INK, "700", "middle"))
    s.append(R(x + 16, 266, 218, 52, fill=BG, stroke=BLUE, sw="1.1", rx="3", dash="4,3"))
    s.append(T(x + 125, 283, "giao diện công bố", 9.5, BLUE, "700", "middle"))
    s.append(T(x + 125, 299, "Ready · Busy · Fault · BoardDone", 9.5, INK2, "400", "middle"))
    s.append(T(x + 125, 313, "← thứ DUY NHẤT người khác được đọc", 8.8, BLUE, "400", "middle"))

# ── tầng cơ cấu
devs = [(150, "Stop1"), (272, "Clamp1"), (394, "Stop2"), (516, "Clamp2"), (638, "Chuyền")]
for x, nm in devs:
    s.append(R(x, 408, 106, 62, fill=PANEL, stroke=INK, sw="1.5", rx="5"))
    s.append(T(x + 53, 430, nm, 11.5, INK, "700", "middle"))
    s.append(T(x + 53, 447, "FB_Cylinder2Pos" if nm != "Chuyền" else "FB_Conveyor", 8.6, INK2, "400", "middle"))
    s.append(T(x + 53, 461, "timeout · Unknown", 8.4, INK2, "400", "middle"))
s.append(R(776, 408, 130, 62, fill="#FDF6E7", stroke=WARN, sw="1.5", rx="5"))
s.append(T(841, 430, "DO_… ngõ ra", 11.5, "#7A5B08", "700", "middle"))
s.append(T(841, 448, "mỗi ngõ ra: ĐÚNG 1 nơi ghi", 8.8, "#7A5B08", "400", "middle"))
s += arw(744, 439, 772, 439, WARN)

# ── mũi tên gọi xuống
s += arw(300, 162, 250, 230)          # máy -> trạm 1
s += arw(640, 162, 690, 230)          # máy -> trạm 2
s.append(T(258, 200, "cho phép / cấm", 9.5, INK2, "600", "end"))
s.append(T(682, 200, "cho phép / cấm", 9.5, INK2, "600"))
for xs, xd in ((240, 203), (300, 325)):
    s += arw(xs, 330, xd, 404)
for xs, xd in ((650, 447), (710, 569)):
    s += arw(xs, 330, xd, 404)
s.append(T(150, 372, "yêu cầu chuyển động", 9.5, INK2, "600"))
s.append(T(600, 372, "yêu cầu chuyển động", 9.5, INK2, "600"))

# ── cấm: trạm gọi ngang
s.append(L(400, 282, 560, 282, BAD, "2.2", "6,4"))
s += cross(480, 282)
s.append(T(480, 262, "KHÔNG đọc ruột nhau", 10, BAD, "700", "middle"))

# ── cấm: trạm ghi thẳng ngõ ra
s.append(L(810, 234, 850, 234, BG, "1"))
s.append(L(841, 330, 841, 404, BAD, "2.2", "6,4"))
s += cross(841, 368)
s.append(T(820, 356, "trạm KHÔNG ghi thẳng", 9.5, BAD, "700", "end"))

s.append(R(24, 522, W - 48, 78, fill="#FBFBFC", stroke=RULE, sw="1.2", rx="5"))
s.append(T(42, 544, "Ba quy tắc gọi — vi phạm là kiến trúc hỏng", 12, INK, "700"))
s.append(T(42, 564, "Q1  Chỉ gọi xuống, không gọi lên. Tầng dưới chỉ báo cáo trạng thái qua biến ra của nó.", 10.5, INK2))
s.append(T(42, 580, "Q2  Ngang hàng không gọi nhau. Trạm 1 không đọc biến nội bộ của trạm 2 — chỉ đọc giao diện đã công bố.", 10.5, INK2))
s.append(T(42, 596, "Q3  Chỉ tầng cơ cấu được chạm vào ngõ ra vật lý. Nhờ vậy cuộn dây trùng không thể xảy ra.", 10.5, INK2))
s.append("</svg>")

d = os.path.join(ROOT, "ch27"); os.makedirs(d, exist_ok=True)
p = os.path.join(d, "hinh_27_1_ba_tang.svg")
open(p, "w", encoding="utf-8").write("\n".join(s))
ET.parse(p)
import pymupdf
pymupdf.open(p)[0].get_pixmap(dpi=100).save(
    r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/p271.png")
open(r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/figlog.txt", "w").write("OK fig27")
