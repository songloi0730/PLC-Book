# -*- coding: utf-8 -*-
"""Sinh hình SVG cho sách PLC. Bộ token thị giác dùng chung cho cả 58 chương."""
import os, xml.etree.ElementTree as ET

ROOT = r"C:/Users/dinhn/OneDrive/Study/Chung/PLC_Programming_Book/assets"
INK = "#1A1D21"; INK2 = "#565E66"; RULE = "#9AA3AB"
CUR = "#C0392B"; OK = "#2E7D4F"; BAD = "#B03A2E"; WARN = "#B8860B"
PANEL = "#F4F5F7"; BG = "#FFFFFF"
F = "font-family=\"Segoe UI,Roboto,Helvetica,Arial,sans-serif\""
log = []


def esc(t):
    return t.replace("&", "&amp;") if "&amp;" not in t else t


def T(x, y, txt, size=12, fill=INK, weight="400", anchor="start"):
    txt = esc(txt)
    return ("<text x='%d' y='%d' %s font-size='%s' font-weight='%s' fill='%s' text-anchor='%s'>%s</text>"
            % (x, y, F, size, weight, fill, anchor, txt))


def R(x, y, w, h, fill=PANEL, stroke=INK, sw="1.4", rx="3"):
    return "<rect x='%d' y='%d' width='%d' height='%d' rx='%s' fill='%s' stroke='%s' stroke-width='%s'/>" % (x, y, w, h, rx, fill, stroke, sw)


def L(x1, y1, x2, y2, stroke=INK, sw="1.6", dash=None):
    d = " stroke-dasharray='%s'" % dash if dash else ""
    return "<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='%s'%s/>" % (x1, y1, x2, y2, stroke, sw, d)


def head(w, h, title, sub):
    return ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' width='%d' height='%d'>" % (w, h, w, h),
            "<rect width='%d' height='%d' fill='%s'/>" % (w, h, BG),
            "<defs><marker id='ar' markerWidth='9' markerHeight='9' refX='8' refY='3' orient='auto'>"
            "<path d='M0,0 L0,6 L9,3 z' fill='%s'/></marker>"
            "<marker id='arc' markerWidth='9' markerHeight='9' refX='8' refY='3' orient='auto'>"
            "<path d='M0,0 L0,6 L9,3 z' fill='%s'/></marker></defs>" % (INK, CUR),
            T(24, 34, title, 16, INK, "700"), T(24, 56, sub, 12, INK2)]


def save(parts, sub, name):
    d = os.path.join(ROOT, sub); os.makedirs(d, exist_ok=True)
    p = os.path.join(d, name)
    open(p, "w", encoding="utf-8").write("\n".join(parts + ["</svg>"]))
    ET.parse(p)
    log.append("OK  " + sub + "/" + name)
    return p


# ─────────────────────────────────────────── Hình 10.1 — vòng quét
def fig_10_1():
    W, H = 900, 330
    s = head(W, H, "Hình 10.1 — Bốn giai đoạn của vòng quét",
             "PLC lặp bốn giai đoạn này mãi mãi. Van chỉ thật sự mở ở giai đoạn 3, không phải lúc chương trình ghi lệnh.")
    boxes = [("1. ĐỌC ngõ vào", "chụp ảnh toàn bộ ngõ vào\nvào bộ nhớ một lượt"),
             ("2. CHẠY chương trình", "từ trên xuống dưới\nđọc ảnh, ghi ảnh"),
             ("3. GHI ngõ ra", "đẩy ảnh ngõ ra\nra module một lượt"),
             ("4. VIỆC hệ thống", "truyền thông, tự chẩn đoán,\nphục vụ phần mềm")]
    x0, y0, bw, bh, gap = 30, 100, 195, 110, 20
    for i, (t, d) in enumerate(boxes):
        x = x0 + i * (bw + gap)
        fill = "#EAF1F6" if i in (0, 2) else PANEL
        s.append(R(x, y0, bw, bh, fill=fill))
        s.append(T(x + bw // 2, y0 + 26, t, 13, INK, "700", "middle"))
        for j, ln in enumerate(d.split("\n")):
            s.append(T(x + bw // 2, y0 + 52 + j * 17, ln, 10.5, INK2, "400", "middle"))
        if i < 3:
            s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='2' marker-end='url(#ar)'/>"
                     % (x + bw + 3, y0 + bh // 2, x + bw + gap - 5, y0 + bh // 2, INK))
    # vòng lặp về đầu
    yb = y0 + bh + 42
    xr = x0 + 3 * (bw + gap) + bw // 2
    s.append(L(xr, y0 + bh, xr, yb, INK, "2"))
    s.append(L(xr, yb, x0 + bw // 2, yb, INK, "2"))
    s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='2' marker-end='url(#ar)'/>"
             % (x0 + bw // 2, yb, x0 + bw // 2, y0 + bh + 6, INK))
    s.append(T((x0 + xr) // 2, yb + 18, "lặp lại — mỗi vòng vài mili-giây tới vài chục mili-giây", 11, INK2, "400", "middle"))
    s.append(R(30, 268, 840, 40, fill="#FDF6E7", stroke=WARN, sw="1.2"))
    s.append(T(44, 293, "⚠  Giữa giai đoạn 1 và giai đoạn 3, dù cảm biến ngoài kia có đổi trạng thái, PLC cũng không biết — nó chỉ nhìn ảnh đã chụp.", 11.5, "#7A5B08"))
    return save(s, "ch10", "hinh_10_1_vong_quet.svg")


# ─────────────────────────────────────────── Hình 10.2 — xung bị bỏ lỡ
def fig_10_2():
    W, H = 900, 380
    s = head(W, H, "Hình 10.2 — Vì sao xung ngắn hơn vòng quét biến mất hoàn toàn",
             "PLC chỉ nhìn ngõ vào một lần mỗi vòng quét. Xung nằm lọt giữa hai lần nhìn thì PLC không hề biết nó đã xảy ra.")
    xL, xR = 150, 860
    scan = 88            # bề rộng một vòng quét (px)
    ticks = [xL + i * scan for i in range(9)]

    # trục thời gian + mốc đọc ngõ vào
    yT = 110
    s.append(T(24, yT + 4, "Thời điểm PLC", 11, INK2))
    s.append(T(24, yT + 20, "đọc ngõ vào", 11, INK2))
    s.append(L(xL - 20, yT, xR, yT, RULE, "1.4"))
    for t in ticks:
        s.append(L(t, yT - 9, t, yT + 9, INK, "2"))
        s.append("<circle cx='%d' cy='%d' r='3.5' fill='%s'/>" % (t, yT, INK))
    s.append(T((xL + xR) // 2, yT - 22, "← mỗi vạch = một lần chụp ảnh ngõ vào (đầu mỗi vòng quét) →", 11, INK2, "400", "middle"))

    # tín hiệu A — xung dài, bắt được
    yA = 190
    s.append(T(24, yA - 6, "Xung DÀI", 11.5, OK, "700"))
    s.append(T(24, yA + 10, "dài hơn 1 vòng quét", 10.5, INK2))
    a1, a2 = ticks[1] + 30, ticks[4] + 20
    s.append(L(xL - 20, yA + 26, a1, yA + 26, INK, "2"))
    s.append(L(a1, yA + 26, a1, yA - 12, INK, "2"))
    s.append(L(a1, yA - 12, a2, yA - 12, INK, "2"))
    s.append(L(a2, yA - 12, a2, yA + 26, INK, "2"))
    s.append(L(a2, yA + 26, xR, yA + 26, INK, "2"))
    for t in ticks:
        if a1 <= t <= a2:
            s.append("<circle cx='%d' cy='%d' r='5' fill='%s'/>" % (t, yA - 12, OK))
    s.append(T(a2 + 14, yA - 8, "✓ có ít nhất một vạch rơi vào xung → bắt được", 11, OK, "600"))

    # tín hiệu B — xung ngắn, mất
    yB = 285
    s.append(T(24, yB - 6, "Xung NGẮN", 11.5, BAD, "700"))
    s.append(T(24, yB + 10, "ngắn hơn 1 vòng quét", 10.5, INK2))
    b1 = ticks[2] + 26
    b2 = b1 + 34
    s.append(L(xL - 20, yB + 26, b1, yB + 26, INK, "2"))
    s.append(L(b1, yB + 26, b1, yB - 12, INK, "2"))
    s.append(L(b1, yB - 12, b2, yB - 12, INK, "2"))
    s.append(L(b2, yB - 12, b2, yB + 26, INK, "2"))
    s.append(L(b2, yB + 26, xR, yB + 26, INK, "2"))
    # vùng mù
    s.append("<rect x='%d' y='%d' width='%d' height='%d' fill='%s' opacity='0.10'/>" % (b1, yB - 20, b2 - b1, 54, BAD))
    s.append(L(b1, yB - 20, b1, yB + 34, BAD, "1", "3,3"))
    s.append(L(b2, yB - 20, b2, yB + 34, BAD, "1", "3,3"))
    s.append(T(b2 + 14, yB - 8, "✗ không vạch nào rơi vào xung → PLC KHÔNG hề biết nó đã xảy ra", 11, BAD, "600"))

    # đường dóng từ mốc đọc xuống
    for t in ticks:
        s.append(L(t, yT + 10, t, 320, RULE, "0.8", "2,4"))
    s.append(T(24, 352, "Điều kiện chắc chắn bắt được:  xung  >  thời gian quét  +  thời gian lọc ngõ vào   (thực hành lấy hệ số an toàn 2 lần)", 11.5, INK, "600"))
    return save(s, "ch10", "hinh_10_2_bo_lo_xung.svg")


# ─────────────────────────────────────────── Hình 15.2 — mạch tự giữ đúng / sai
def fig_15_2():
    W, H = 900, 440
    s = head(W, H, "Hình 15.2 — Mạch tự giữ: đúng và sai",
             "Nhánh tự giữ phải song song CHỈ với nút Start. Vòng qua cả nút Dừng là nút Dừng mất tác dụng vĩnh viễn.")

    def rung(ox, oy, wrong):
        p = []
        col = BAD if wrong else OK
        p.append(R(ox, oy, 420, 172, fill=BG, stroke=col, sw="1.6", rx="4"))
        title = "✗ SAI — nhánh giữ vòng qua cả nút Dừng" if wrong else "✓ ĐÚNG — nhánh giữ chỉ song song với Start"
        p.append(T(ox + 16, oy + 24, title, 12.5, col, "700"))
        xl, xr = ox + 30, ox + 390          # hai ray
        y1 = oy + 62                        # nhánh chính
        y2 = oy + 106                       # nhánh tự giữ
        p.append(L(xl, oy + 44, xl, oy + 126, RULE, "1.6"))
        p.append(L(xr, oy + 44, xr, oy + 126, RULE, "1.6"))
        cStart, cStop = ox + 120, ox + 240
        # nhánh chính
        p.append(L(xl, y1, cStart - 12, y1))
        p.append(L(cStart - 12, y1 - 11, cStart - 12, y1 + 11, INK, "2"))
        p.append(L(cStart + 12, y1 - 11, cStart + 12, y1 + 11, INK, "2"))
        p.append(T(cStart, y1 - 18, "DI_StartPB", 10, INK2, "400", "middle"))
        p.append(L(cStart + 12, y1, cStop - 12, y1))
        p.append(L(cStop - 12, y1 - 11, cStop - 12, y1 + 11, INK, "2"))
        p.append(L(cStop + 12, y1 - 11, cStop + 12, y1 + 11, INK, "2"))
        p.append(T(cStop, y1 - 18, "DI_StopPB", 10, INK2, "400", "middle"))
        p.append(L(cStop + 12, y1, ox + 330, y1))
        p.append("<circle cx='%d' cy='%d' r='11' fill='none' stroke='%s' stroke-width='2'/>" % (ox + 345, y1, INK))
        p.append(L(ox + 356, y1, xr, y1))
        p.append(T(ox + 345, y1 - 18, "M_ConvRunCmd", 10, INK2, "400", "middle"))
        # nhánh tự giữ
        jx = (cStop + 12 + 8) if wrong else (cStart + 12 + 8)
        p.append(L(xl, y2, jx - 30, y2, col, "2"))
        p.append(L(jx - 30 - 12, y2 - 11, jx - 30 - 12, y2 + 11, col, "2"))
        p.append(L(jx - 30 + 12, y2 - 11, jx - 30 + 12, y2 + 11, col, "2"))
        p.append(T(jx - 30, y2 - 18, "M_ConvRunCmd", 10, col, "600", "middle"))
        p.append(L(jx - 30 + 12, y2, jx, y2, col, "2"))
        p.append(L(jx, y2, jx, y1, col, "2"))
        p.append(L(xl, y1, xl, y2, col, "2"))
        note = "Đã chạy rồi thì nút Dừng bị nối tắt → không dừng được" if wrong else "Nhả Start vẫn giữ; nhấn Dừng thì cắt được"
        p.append(T(ox + 16, oy + 158, note, 11, col, "600"))
        return p

    s += rung(24, 84, False)
    s += rung(24, 258, True)
    return save(s, "ch15", "hinh_15_2_tu_giu.svg")


# ─────────────────────────────────────────── Hình 1.1 — tổng quan DP-01
def fig_01_1():
    W, H = 900, 300
    s = head(W, H, "Hình 1.1 — Máy mẫu DP-01: trạm tra keo &amp; sấy UV trên chuyền board mạch",
             "Hai trạm nối tiếp trong cùng một máy — nhờ vậy dạy được pipeline: hai trạm xử lý hai board khác nhau cùng lúc.")
    y = 110
    s.append(R(24, y, 120, 96, fill=BG, stroke=RULE))
    s.append(T(84, y + 44, "Máy trước", 12, INK2, "600", "middle"))
    s.append(R(180, y - 22, 560, 140, fill=BG, stroke=INK, sw="1.8", rx="5"))
    s.append(T(198, y - 4, "DP-01", 14, INK, "700"))
    s.append(R(756, y, 120, 96, fill=BG, stroke=RULE))
    s.append(T(816, y + 44, "Máy sau", 12, INK2, "600", "middle"))
    # chuyền
    cy = y + 48
    s.append(L(144, cy, 180, cy, INK, "2"))
    s.append(L(740, cy, 756, cy, INK, "2"))
    for lbl, x in (("SMEMA", 162), ("SMEMA", 748)):
        s.append(T(x, cy - 12, lbl, 9.5, WARN, "700", "middle"))
    # 2 trạm
    for i, (t1, t2, t3) in enumerate([("TRẠM 1", "TRA KEO", "gantry XY+Z · van tra keo"),
                                      ("TRẠM 2", "SẤY UV", "đèn UV · cửa chắn")]):
        x = 340 + i * 210
        s.append(R(x, y + 8, 180, 76, fill=PANEL))
        s.append(T(x + 90, y + 30, t1, 10.5, INK2, "600", "middle"))
        s.append(T(x + 90, y + 50, t2, 13.5, INK, "700", "middle"))
        s.append(T(x + 90, y + 70, t3, 9.5, INK2, "400", "middle"))
    s.append("<line x1='200' y1='%d' x2='334' y2='%d' stroke='%s' stroke-width='2.4' marker-end='url(#ar)'/>" % (cy, cy, INK))
    s.append("<line x1='526' y1='%d' x2='544' y2='%d' stroke='%s' stroke-width='2.4' marker-end='url(#ar)'/>" % (cy, cy, INK))
    s.append("<line x1='736' y1='%d' x2='738' y2='%d' stroke='%s' stroke-width='2.4'/>" % (cy, cy, INK))
    s.append("<circle cx='250' cy='%d' r='7' fill='%s'/>" % (cy, CUR))
    s.append(T(250, cy + 26, "đọc mã 2D", 9.5, CUR, "600", "middle"))
    s.append(T(250, cy + 40, "hỏi MES", 9.5, CUR, "600", "middle"))
    s.append(R(24, 246, 852, 40, fill="#EAF1F6", stroke=RULE, sw="1.2"))
    s.append(T(40, 271, "Máy được BÓC LỚP: chương thuộc lát cắt nào chỉ dùng thiết bị của lát cắt đó trở về trước. Ch.15 (Ladder) không được lấy ví dụ về servo.", 11.5, "#1F4E66"))
    return save(s, "ch01", "hinh_01_1_dp01_tong_quan.svg")


for fn in (fig_10_1, fig_10_2, fig_15_2, fig_01_1):
    try:
        fn()
    except Exception as e:
        log.append("FAIL " + fn.__name__ + ": " + repr(e))

open(r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/figlog.txt", "w", encoding="utf-8").write("\n".join(log))
