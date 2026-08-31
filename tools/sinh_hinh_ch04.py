# -*- coding: utf-8 -*-
import os
A = r"C:/Users/dinhn/OneDrive/Study/Chung/PLC_Programming_Book/assets/ch04"
os.makedirs(A, exist_ok=True)
INK = "#1A1D21"; INK2 = "#565E66"; RULE = "#9AA3AB"
CUR = "#C0392B"; OK = "#2E7D4F"; BAD = "#B03A2E"
PANEL = "#F4F5F7"; BG = "#FFFFFF"
F = "font-family=\"Segoe UI,Roboto,Helvetica,Arial,sans-serif\""


def cell(ox, oy, sensor, common_to, works, note):
    s = []
    W, H = 440, 260
    y24, y0 = oy + 56, oy + 206
    sx1, sx2 = ox + 34, ox + 152
    px1, px2 = ox + 244, ox + 372
    bt, bb = oy + 96, oy + 172
    ym = oy + 134
    cx = px2 + 30
    col = OK if works else BAD
    cxs = (sx1 + sx2) // 2
    cxp = (px1 + px2) // 2
    sp = sx1 + 24

    if common_to == "0 V":
        c_y1, c_y2 = ym, y0
    else:
        c_y1, c_y2 = bt, y24
    c_lbl_y = (c_y1 + c_y2) // 2 + 4

    s.append("<rect x='%d' y='%d' width='%d' height='%d' rx='4' fill='%s' stroke='%s' stroke-width='1.6'/>"
             % (ox + 8, oy + 8, W - 16, H - 16, BG, col))
    mark = "\u2713 CH\u1EA0Y" if works else "\u2717 KH\u00D4NG L\u00CAN"
    s.append("<text x='%d' y='%d' %s font-size='13' font-weight='700' fill='%s'>C\u1EA3m bi\u1EBFn %s + ch\u00E2n chung \u2192 %s</text>"
             % (ox + 22, oy + 32, F, INK, sensor, common_to))
    s.append("<text x='%d' y='%d' %s font-size='13' font-weight='700' fill='%s' text-anchor='end'>%s</text>"
             % (ox + W - 24, oy + 32, F, col, mark))

    s.append("<text x='%d' y='%d' %s font-size='11' fill='%s'>+24 V</text>" % (ox + 22, y24 + 4, F, INK2))
    s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='1.6'/>" % (ox + 66, y24, ox + W - 22, y24, RULE))
    s.append("<text x='%d' y='%d' %s font-size='11' fill='%s'>0 V</text>" % (ox + 22, y0 + 4, F, INK2))
    s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='1.6'/>" % (ox + 66, y0, ox + W - 22, y0, RULE))

    s.append("<rect x='%d' y='%d' width='%d' height='%d' rx='3' fill='%s' stroke='%s' stroke-width='1.4'/>"
             % (sx1, bt, sx2 - sx1, bb - bt, PANEL, INK))
    s.append("<text x='%d' y='%d' %s font-size='11.5' fill='%s' text-anchor='middle'>C\u1EA3m bi\u1EBFn</text>" % (cxs, bt + 22, F, INK2))
    s.append("<text x='%d' y='%d' %s font-size='14' font-weight='700' fill='%s' text-anchor='middle'>%s</text>" % (cxs, bt + 42, F, INK, sensor))
    sub = "\u0111\u00F3ng l\u00EAn +24 V" if sensor == "PNP" else "\u0111\u00F3ng xu\u1ED1ng 0 V"
    s.append("<text x='%d' y='%d' %s font-size='10' fill='%s' text-anchor='middle'>%s</text>" % (cxs, bt + 62, F, INK2, sub))
    s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='1.6'/>" % (sp, bt, sp, y24, INK))
    s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='1.6'/>" % (sp, bb, sp, y0, INK))

    s.append("<rect x='%d' y='%d' width='%d' height='%d' rx='3' fill='%s' stroke='%s' stroke-width='1.4'/>"
             % (px1, bt, px2 - px1, bb - bt, PANEL, INK))
    s.append("<text x='%d' y='%d' %s font-size='11.5' font-weight='600' fill='%s' text-anchor='middle'>Ng\u00F5 v\u00E0o PLC</text>" % (cxp, bt + 20, F, INK))
    s.append("<circle cx='%d' cy='%d' r='12' fill='%s' stroke='%s' stroke-width='1.4'/>" % (cxp, ym, BG, INK))
    s.append("<text x='%d' y='%d' %s font-size='9.5' fill='%s' text-anchor='middle'>opto</text>" % (cxp, ym + 4, F, INK2))

    s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='2'/>" % (sx2, ym, cxp - 12, ym, INK))
    s.append("<text x='%d' y='%d' %s font-size='10' fill='%s' text-anchor='middle'>d\u00E2y \u0111en</text>" % ((sx2 + px1) // 2, ym - 10, F, INK2))

    s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='2'/>" % (cxp + 12, ym, cx, ym, INK))
    s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='1.8'/>" % (cx, c_y1, cx, c_y2, INK))
    s.append("<text x='%d' y='%d' %s font-size='10' fill='%s' text-anchor='end'>ch\u00E2n chung</text>" % (cx - 8, c_lbl_y, F, INK2))

    if works:
        if sensor == "PNP":
            p1 = "M %d %d L %d %d" % (sx2, ym, cxp - 12, ym)
            p2 = "M %d %d L %d %d L %d %d" % (cxp + 12, ym, cx, ym, cx, y0)
        else:
            p1 = "M %d %d L %d %d L %d %d" % (cx, y24, cx, ym, cxp + 12, ym)
            p2 = "M %d %d L %d %d" % (cxp - 12, ym, sx2, ym)
        s.append("<path d='%s' fill='none' stroke='%s' stroke-width='2.8' opacity='0.9'/>" % (p1, CUR))
        s.append("<path d='%s' fill='none' stroke='%s' stroke-width='2.8' opacity='0.9'/>" % (p2, CUR))
        s.append("<rect x='%d' y='%d' width='11' height='11' fill='%s'/>" % (ox + W - 162, oy + H - 32, CUR))
        s.append("<text x='%d' y='%d' %s font-size='10.5' fill='%s'>\u0111\u01B0\u1EDDng d\u00F2ng kh\u00E9p k\u00EDn</text>" % (ox + W - 146, oy + H - 22, F, CUR))
    else:
        mx = (sx2 + px1) // 2
        s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='3'/>" % (mx - 11, ym - 11, mx + 11, ym + 11, BAD))
        s.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='3'/>" % (mx - 11, ym + 11, mx + 11, ym - 11, BAD))
        s.append("<text x='%d' y='%d' %s font-size='10.5' fill='%s' text-anchor='end'>hai \u0111\u1EA7u c\u00F9ng %s \u2192 kh\u00F4ng ch\u00EAnh \u00E1p</text>"
                 % (ox + W - 24, oy + H - 22, F, BAD, common_to))

    s.append("<text x='%d' y='%d' %s font-size='11' font-weight='600' fill='%s'>%s</text>" % (ox + 22, oy + H - 22, F, INK2, note))
    return "\n".join(s)


W, H = 900, 620
o = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 %d %d' width='%d' height='%d'>" % (W, H, W, H),
     "<rect width='%d' height='%d' fill='%s'/>" % (W, H, BG),
     "<text x='24' y='34' %s font-size='16' font-weight='700' fill='%s'>H\u00ECnh 4.2 \u2014 B\u1ED1n t\u1ED5 h\u1EE3p: c\u1EA3m bi\u1EBFn \u00D7 ch\u00E2n chung module</text>" % (F, INK),
     "<text x='24' y='56' %s font-size='12' fill='%s'>Ch\u1EC9 hai t\u1ED5 h\u1EE3p kh\u00E9p k\u00EDn \u0111\u01B0\u1EE3c m\u1EA1ch. Hai t\u1ED5 h\u1EE3p c\u00F2n l\u1EA1i c\u00F3 hai \u0111\u1EA7u c\u00F9ng \u0111i\u1EC7n th\u1EBF n\u00EAn kh\u00F4ng c\u00F3 d\u00F2ng \u2014 bit kh\u00F4ng bao gi\u1EDD l\u00EAn.</text>" % (F, INK2)]
o.append(cell(10, 76, "PNP", "0 V", True, "T\u1ED5 h\u1EE3p 1 \u2014 ph\u1ED5 bi\u1EBFn \u1EDF ch\u00E2u \u00C2u"))
o.append(cell(460, 76, "PNP", "+24 V", False, "T\u1ED5 h\u1EE3p 2"))
o.append(cell(10, 346, "NPN", "+24 V", True, "T\u1ED5 h\u1EE3p 3 \u2014 ph\u1ED5 bi\u1EBFn \u1EDF thi\u1EBFt b\u1ECB Nh\u1EADt"))
o.append(cell(460, 346, "NPN", "0 V", False, "T\u1ED5 h\u1EE3p 4"))
o.append("</svg>")

path = os.path.join(A, "hinh_04_2_bon_to_hop.svg")
open(path, "w", encoding="utf-8").write("\n".join(o))

import xml.etree.ElementTree as ET
import pymupdf
ET.parse(path)
d = pymupdf.open(path)
d[0].get_pixmap(dpi=110).save(r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/preview_04_2.png")
open(r"C:/Users/dinhn/AppData/Local/Temp/claude/C--Users-dinhn-OneDrive-C-VS-AM-AutoFrame/2ec7d332-f9ff-4710-aba9-ee68e44c58f0/scratchpad/svglog.txt", "w").write("OK - svg valid, png rendered")
