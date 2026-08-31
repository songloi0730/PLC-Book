# -*- coding: utf-8 -*-
"""Hình 28.1 — thứ tự về gốc: sai và đúng."""
import os, math, xml.etree.ElementTree as ET

ROOT = r"C:/Users/dinhn/OneDrive/Study/Chung/PLC_Programming_Book/assets"
INK = "#1A1D21"; INK2 = "#565E66"; RULE = "#9AA3AB"
CUR = "#C0392B"; OK = "#2E7D4F"; BAD = "#B03A2E"; WARN = "#B8860B"
PANEL = "#F4F5F7"; BG = "#FFFFFF"
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


def arw(x1, y1, x2, y2, col=INK, sw="2"):
    ang = math.atan2(y2 - y1, x2 - x1); hl, hw = 9.0, 4.5
    bx, by = x2 - hl * math.cos(ang), y2 - hl * math.sin(ang)
    return [L(x1, y1, int(bx), int(by), col, sw),
            "<polygon points='%.1f,%.1f %.1f,%.1f %.1f,%.1f' fill='%s'/>" % (
                x2, y2, bx - hw * math.sin(ang), by + hw * math.cos(ang),
                bx + hw * math.sin(ang), by - hw * math.cos(ang), col)]


def machine(ox, oy, clamp1_up, clamp2_up, board1, board2, conv, w=380):
    """Sơ đồ máy thu nhỏ. clamp*_up: kẹp đang nâng. board*: có board."""
    p = []
    ycon = oy + 62                       # mặt chuyền
    p.append(L(ox + 10, ycon, ox + w - 10, ycon, RULE if not conv else INK, "2.4"))
    p.append(T(ox + 10, ycon + 18, "chuyền " + ("ĐANG CHẠY" if conv else "dừng"), 9.5,
               CUR if conv else INK2, "700" if conv else "400"))
    for i, (cx, cup, hasb, nm) in enumerate([(ox + 110, clamp1_up, board1, "Trạm 1"),
                                             (ox + 260, clamp2_up, board2, "Trạm 2")]):
        p.append(T(cx, oy + 14, nm, 10, INK2, "600", "middle"))
        # chặn
        p.append(L(cx + 44, ycon, cx + 44, ycon - 20, INK, "2.6"))
        p.append(T(cx + 50, ycon - 22, "chặn", 8.5, INK2))
        # kẹp: hai ngàm
        yk = ycon - 26 if cup else ycon - 8
        p.append(L(cx - 26, yk, cx + 26, yk, INK, "2.6"))
        p.append(L(cx - 26, yk, cx - 26, yk + 9, INK, "2.6"))
        p.append(L(cx + 26, yk, cx + 26, yk + 9, INK, "2.6"))
        p.append(T(cx - 34, yk + 4, "kẹp " + ("↑" if cup else "↓"), 9, INK2, "600", "end"))
        # board
        if hasb:
            yb = yk + 10 if cup else ycon - 8
            p.append(R(cx - 22, yb, 44, 9, fill="#DCE9F2", stroke="#2C5F8D", sw="1.2", rx="1"))
            p.append(T(cx, yb - 4, "board " + ("A" if i == 0 else "B"), 8.5, "#1F4E66", "700", "middle"))
    return p


W, H = 940, 700
s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' width='%d' height='%d'>" % (W, H, W, H),
     "<rect width='%d' height='%d' fill='%s'/>" % (W, H, BG),
     T(24, 34, "Hình 28.1 — Thứ tự về gốc: sai và đúng", 16, INK, "700"),
     T(24, 56, "Cùng một tư thế xuất phát. Thứ tự bên trái vi phạm bảng va chạm ngay ở bước đầu tiên.", 12, INK2)]

# ── tư thế xuất phát
s.append(R(24, 76, W - 48, 152, fill="#FBFBFC", stroke=RULE, sw="1.4", rx="5"))
s.append(T(40, 98, "TƯ THẾ XUẤT PHÁT — máy vừa vào Alarm vì mất khí", 12, INK, "700"))
s.append(T(40, 116, "Hai board đang bị kẹp NÂNG ở hai trạm. Chặn cả hai trạm đang nâng. Chuyền đã dừng.", 10.5, INK2))
s += machine(180, 128, True, True, True, True, False, 700)

# ── hai cột
colw = 436
for ci, wrong in enumerate([True, False]):
    ox = 24 + ci * (colw + 20)
    oy = 246
    col = BAD if wrong else OK
    s.append(R(ox, oy, colw, 372, fill=BG, stroke=col, sw="1.8", rx="5"))
    ttl = "✗ THỨ TỰ SAI — hạ chặn trước" if wrong else "✓ THỨ TỰ ĐÚNG — hạ kẹp trước"
    s.append(T(ox + 16, oy + 26, ttl, 13, col, "700"))

    if wrong:
        steps = [("1", "Hạ chặn cả hai trạm", "board đang treo trên kẹp — chặn không còn giữ gì", BAD),
                 ("2", "Nhả kẹp cả hai trạm", "board A và B cùng rơi xuống mặt chuyền", BAD),
                 ("3", "Cho chuyền chạy để xả board", "hai board trôi tự do, board A đuổi kịp board B", BAD)]
        outcome = ("VA CHẠM", "Vi phạm V1 (board rơi không kiểm soát) và V3 (hai board đâm nhau).", BAD)
    else:
        steps = [("H0", "Dừng chuyền, cấm chuyển động tự động", "chốt điều kiện an toàn trước mọi thao tác", OK),
                 ("H1", "HẠ KẸP cả hai trạm", "board hạ xuống mặt chuyền, chặn vẫn giữ — chống V1", OK),
                 ("H2", "Đánh dấu NG mọi board trong máy", "không để sản phẩm dở dang lẫn hàng tốt", OK),
                 ("H3", "Xả board TỪ TRẠM 2 TRƯỚC, rồi trạm 1", "trạm sau trống thì trạm trước mới có chỗ đi — chống V3", OK),
                 ("H4", "Nâng lại chặn về tư thế gốc", "mỗi bước có timeout + mã lỗi riêng", OK)]
        outcome = ("VỀ GỐC AN TOÀN", "Không bước nào vi phạm bảng va chạm, với mọi tư thế xuất phát.", OK)

    sy = oy + 46
    for k, (num, title, why, c) in enumerate(steps):
        y = sy + k * 54
        s.append("<circle cx='%d' cy='%d' r='13' fill='%s'/>" % (ox + 34, y + 14, c))
        s.append(T(ox + 34, y + 18, num, 10, "#FFFFFF", "700", "middle"))
        s.append(T(ox + 56, y + 12, title, 11.5, INK, "600"))
        s.append(T(ox + 56, y + 29, why, 9.8, INK2))
        if k < len(steps) - 1:
            s += arw(ox + 34, y + 28, ox + 34, y + 46, RULE, "1.6")

    yo = oy + 372 - 62
    s.append(R(ox + 14, yo, colw - 28, 48, fill=("#F8E7E4" if wrong else "#E8F2EC"), stroke=col, sw="1.2"))
    s.append(T(ox + 28, yo + 20, outcome[0], 12, outcome[2], "700"))
    s.append(T(ox + 28, yo + 37, outcome[1], 10, INK2))

s.append(R(24, 638, W - 48, 46, fill="#FDF6E7", stroke=WARN, sw="1.2"))
s.append(T(42, 660, "Hai quy tắc rút ra được, đúng với gần như mọi máy:", 11.5, "#7A5B08", "700"))
s.append(T(42, 677, "① Giải phóng trước, di chuyển sau — nhả kẹp/giữ trước khi cho bất cứ thứ gì chuyển động.   ② Xả sản phẩm từ cuối dây chuyền về đầu.", 11, "#7A5B08"))
s.append("</svg>")

d = os.path.join(ROOT, "ch28"); os.makedirs(d, exist_ok=True)
p = os.path.join(d, "hinh_28_1_thu_tu_ve_goc.svg")
open(p, "w", encoding="utf-8").write("\n".join(s))
ET.parse(p)
import pymupdf
pymupdf.open(p)[0].get_pixmap(dpi=100).save(
    r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/p281.png")
open(r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/figlog.txt", "w").write("OK fig28")
