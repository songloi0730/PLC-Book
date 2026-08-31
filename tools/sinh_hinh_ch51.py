# -*- coding: utf-8 -*-
"""Hình 51.1 — bốn phép đo tách lỗi trên đường tín hiệu ngõ vào."""
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


def arw(x1, y1, x2, y2, col=INK, sw="2"):
    ang = math.atan2(y2 - y1, x2 - x1); hl, hw = 9.0, 4.5
    bx, by = x2 - hl * math.cos(ang), y2 - hl * math.sin(ang)
    return [L(x1, y1, int(bx), int(by), col, sw),
            "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' fill='%s'/>" % (
                x2, y2, bx - hw * math.sin(ang), by + hw * math.cos(ang),
                bx + hw * math.sin(ang), by - hw * math.cos(ang), col)]


W, H = 940, 560
s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' width='%d' height='%d'>" % (W, H, W, H),
     "<rect width='%d' height='%d' fill='%s'/>" % (W, H, BG),
     T(24, 34, "Hình 51.1 — Bốn phép đo tách lỗi trên đường tín hiệu ngõ vào", 16, INK, "700"),
     T(24, 56, "Đo theo thứ tự Đ1 → Đ4. Mỗi phép đo loại trừ được một đoạn của đường tín hiệu — không cần đoán.", 12, INK2)]

ytop, ybot = 96, 240
ycon = 176                                    # đường tín hiệu chính

# ── các khối trên đường tín hiệu
blocks = [(40, 150, "Cảm biến", "PNP, 3 dây"),
          (250, 110, "Cầu đấu", "đầu cốt"),
          (420, 190, "Module vào", "opto + ảnh ngõ vào"),
          (680, 210, "Chương trình", "bit DI_… trong code")]
for x, w, nm, sub in blocks:
    fill = BLUEBG if nm == "Chương trình" else PANEL
    stroke = BLUE if nm == "Chương trình" else INK
    s.append(R(x, ytop + 30, w, 72, fill=fill, stroke=stroke, sw="1.6", rx="5"))
    s.append(T(x + w // 2, ytop + 56, nm, 12.5, INK, "700", "middle"))
    s.append(T(x + w // 2, ytop + 74, sub, 9.8, INK2, "400", "middle"))

# ── dây nối
s.append(L(190, ycon, 250, ycon, INK, "2.2"))
s.append(L(360, ycon, 420, ycon, INK, "2.2"))
s.append(T(220, ycon - 10, "dây đen", 9.5, INK2, "400", "middle"))
s.append(T(390, ycon - 10, "dây đen", 9.5, INK2, "400", "middle"))
s += arw(610, ycon, 676, ycon, BLUE, "2.2")
s.append(T(643, ycon - 10, "phần mềm", 9.5, BLUE, "600", "middle"))

# ── ranh giới phần cứng / phần mềm
s.append(L(645, 84, 645, 262, RULE, "1.4", "6,5"))
s.append(T(637, 96, "PHẦN CỨNG", 9.5, INK2, "700", "end"))
s.append(T(653, 96, "PHẦN MỀM", 9.5, BLUE, "700"))

# ── điểm đo
pts = [(115, "Đ1", "nguồn cấp cảm biến", "nâu ↔ xanh dương"),
       (250, "Đ2", "tín hiệu tại cảm biến", "đen ↔ CHÂN CHUNG module"),
       (420, "Đ3", "tín hiệu tại module", "ngay tại cầu đấu vào"),
       (760, "Đ4", "bit trong chương trình", "xem trực tuyến")]
for x, nm, what, how in pts:
    col = BLUE if nm == "Đ4" else CUR
    s.append("<circle cx='%d' cy='%d' r='15' fill='%s'/>" % (x, ybot + 18, col))
    s.append(T(x, ybot + 23, nm, 11.5, "#FFFFFF", "700", "middle"))
    s.append(L(x, ycon + (30 if nm != "Đ4" else 34), x, ybot + 2, col, "1.6", "4,3"))

# ── bảng kết luận
yt = 300
s.append(R(24, yt, W - 48, 176, fill="#FBFBFC", stroke=RULE, sw="1.3", rx="5"))
hdr = [(46, "Phép đo"), (150, "Đo gì"), (392, "Nếu KHÔNG có → nguyên nhân nằm ở đây")]
for x, t in hdr:
    s.append(T(x, yt + 24, t, 10.5, INK2, "700"))
s.append(L(38, yt + 32, W - 62, yt + 32, RULE, "1.2"))

rows = [("Đ1", "Nguồn cấp cảm biến (nâu ↔ xanh dương)", "Nguồn 24 V hoặc cầu chì nhánh — dừng ở đây, không đo tiếp", CUR),
        ("Đ2", "Đen ↔ chân chung module, khi cảm biến kích hoạt", "Cảm biến hỏng, HOẶC kiểu đấu sai (PNP/NPN — Chương 4)", CUR),
        ("Đ3", "Ngay tại cầu đấu vào module", "Đứt dây hoặc lỏng đầu cốt — đoạn giữa Đ2 và Đ3", CUR),
        ("Đ4", "Bit trong chương trình (xem trực tuyến)", "Module hỏng, hoặc kênh chưa được cấu hình", BLUE)]
for i, (nm, what, concl, col) in enumerate(rows):
    y = yt + 56 + i * 30
    s.append("<circle cx='%d' cy='%d' r='11' fill='%s'/>" % (56, y - 4, col))
    s.append(T(56, y, nm, 10, "#FFFFFF", "700", "middle"))
    s.append(T(90, y, what, 10.5, INK))
    s.append(T(392, y, concl, 10.5, INK2))

s.append(R(24, 490, W - 48, 52, fill="#FDF6E7", stroke=WARN, sw="1.2"))
s.append(T(42, 512, "⚠  Đ2 đo so với CHÂN CHUNG CỦA MODULE, không phải so với 0 V.", 11.5, "#7A5B08", "700"))
s.append(T(42, 530, "Đo so với 0 V sẽ cho kết quả 'có điện áp' ngay cả khi tổ hợp đấu nối sai — bạn sẽ bỏ sót đúng nguyên nhân (Chương 4).", 11, "#7A5B08"))
s.append("</svg>")

d = os.path.join(ROOT, "ch51"); os.makedirs(d, exist_ok=True)
p = os.path.join(d, "hinh_51_1_chuoi_do.svg")
open(p, "w", encoding="utf-8").write("\n".join(s))
ET.parse(p)
import pymupdf
pymupdf.open(p)[0].get_pixmap(dpi=105).save(
    r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/p511.png")
open(r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/figlog.txt", "w").write("OK fig51")
