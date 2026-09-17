# -*- coding: utf-8 -*-
"""Hình chuyên biệt của Chương 31 — ai cấp nguồn cho vòng dòng 4–20 mA.

Ba cách đấu trông gần giống nhau trên bản vẽ, nhưng một trong ba làm hỏng module.
Khác biệt nằm ở ĐƯỜNG ĐI CỦA DÒNG và ở chỗ nguồn 24 V nằm ở đâu — đúng loại nội dung
mà chữ diễn đạt kém còn hình nói ngay (bất biến B13).

Chạy:  python tools/sinh_hinh_ch31.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from sinh_hinh import (  # noqa: E402
    INK, INK2, RULE, CUR, OK, BAD, PANEL, T, R, L, arw, head, save, log,
)


def _khung(s, x, y, w, h, tieu_de, mo_ta, mau_vien, mau_nen):
    """Một ô minh hoạ có tiêu đề."""
    s.append(R(x, y, w, h, fill="#FFFFFF", stroke=RULE, sw="1.2"))
    s.append(R(x, y, w, 30, fill=mau_nen, stroke=mau_vien, sw="1.3"))
    s.append(T(x + w / 2, y + 20, tieu_de, 12, mau_vien, "700", "middle"))
    s.append(T(x + w / 2, y + h - 12, mo_ta, 10.5, INK2, "400", "middle"))


def _module(s, x, y, nhan_phu):
    """Hộp module analog của PLC."""
    s.append(R(x, y, 96, 52, fill=PANEL, stroke=INK, sw="1.5"))
    s.append(T(x + 48, y + 21, "MODULE", 10.5, INK, "700", "middle"))
    s.append(T(x + 48, y + 34, "ANALOG", 10.5, INK, "700", "middle"))
    s.append(T(x + 48, y + 46, nhan_phu, 9, INK2, "400", "middle"))


def _cam_bien(s, x, y):
    s.append(R(x, y, 90, 40, fill="#FFFFFF", stroke=INK, sw="1.5"))
    s.append(T(x + 45, y + 17, "CẢM BIẾN", 10.5, INK, "700", "middle"))
    s.append(T(x + 45, y + 31, "2 dây", 10, INK2, "400", "middle"))


def _nguon(s, x, y, mau=INK):
    s.append(R(x, y, 74, 34, fill="#FFFFFF", stroke=mau, sw="1.6"))
    s.append(T(x + 37, y + 22, "24 V", 12, mau, "700", "middle"))


def fig_31_1():
    """Ba cách đấu vòng 4–20 mA: hai cách đúng, một cách làm hỏng module."""
    W, H = 900, 560
    s = head(W, H, "Hình 31.1 — Ai cấp nguồn cho vòng 4–20 mA",
             "Ba sơ đồ trông na ná nhau. Khác biệt duy nhất là nguồn 24 V nằm ở đâu — "
             "và nó quyết định module sống hay chết.")

    # ── Ô A — module CÓ cấp nguồn vòng ────────────────────────────────
    ax, ay = 24, 80
    _khung(s, ax, ay, 410, 200, "A · ĐÚNG — module CÓ cấp nguồn vòng",
           "Chỉ hai sợi dây. Không đưa thêm nguồn nào từ ngoài.", OK, "#DFF0E4")
    _cam_bien(s, ax + 36, ay + 74)
    _module(s, ax + 260, ay + 68, "có nguồn phụ")
    # day tren: module -> cam bien
    s.append(L(ax + 260, ay + 84, ax + 126, ay + 84, CUR, "2.4"))
    s += arw(ax + 200, ay + 84, ax + 170, ay + 84, CUR, "2.4")
    # day duoi: cam bien -> module
    s.append(L(ax + 126, ay + 108, ax + 260, ay + 108, CUR, "2.4"))
    s += arw(ax + 190, ay + 108, ax + 220, ay + 108, CUR, "2.4")
    s.append(T(ax + 193, ay + 76, "24 V từ module", 9.5, CUR, "700", "middle"))
    s.append(T(ax + 193, ay + 124, "4–20 mA về", 9.5, CUR, "700", "middle"))
    s.append(T(ax + 308, ay + 140, "⭐ một nguồn duy nhất", 10, OK, "700", "middle"))

    # ── Ô B — module CHỈ ĐO, nguồn từ ngoài ───────────────────────────
    bx, by = 466, 80
    _khung(s, bx, by, 410, 200, "B · ĐÚNG — module CHỈ ĐO, nguồn ngoài",
           "Nguồn 24 V mắc NỐI TIẾP trong vòng, đúng một lần.", OK, "#DFF0E4")
    _cam_bien(s, bx + 26, by + 74)
    _module(s, bx + 272, by + 68, "chỉ đo dòng")
    _nguon(s, bx + 150, by + 44, INK)
    # cam bien -> nguon -> module (day tren)
    s.append(L(bx + 71, by + 74, bx + 71, by + 61, CUR, "2.4"))
    s.append(L(bx + 71, by + 61, bx + 150, by + 61, CUR, "2.4"))
    s.append(L(bx + 224, by + 61, bx + 320, by + 61, CUR, "2.4"))
    s.append(L(bx + 320, by + 61, bx + 320, by + 68, CUR, "2.4"))
    s += arw(bx + 250, by + 61, bx + 285, by + 61, CUR, "2.4")
    # module -> cam bien (day duoi)
    s.append(L(bx + 116, by + 108, bx + 272, by + 108, CUR, "2.4"))
    s += arw(bx + 210, by + 108, bx + 175, by + 108, CUR, "2.4")
    s.append(T(bx + 205, by + 130, "một vòng kín, một nguồn", 9.5, CUR, "700", "middle"))
    s.append(T(bx + 316, by + 150, "⭐ một nguồn duy nhất", 10, OK, "700", "middle"))

    # ── Ô C — SAI: cấp nguồn HAI LẦN ──────────────────────────────────
    cx, cy = 24, 302
    _khung(s, cx, cy, 410, 200, "C · ⚠⚠ SAI — cấp nguồn HAI LẦN",
           "Module tự cấp nguồn, VÀ có thêm nguồn ngoài mắc trong vòng.", BAD, "#FBE9E7")
    _cam_bien(s, cx + 26, cy + 84)
    _nguon(s, cx + 150, cy + 54, BAD)
    # Module ve rieng cho ca C: phai nhin thay NGUON THU HAI nam BEN TRONG no
    s.append(R(cx + 266, cy + 78, 108, 62, fill=PANEL, stroke=INK, sw="1.5"))
    s.append(T(cx + 320, cy + 96, "MODULE ANALOG", 10, INK, "700", "middle"))
    s.append(R(cx + 276, cy + 104, 88, 22, fill="#FBE9E7", stroke=BAD, sw="1.4"))
    s.append(T(cx + 320, cy + 119, "nguồn 2 · 24 V", 9.5, BAD, "700", "middle"))
    s.append(T(cx + 320, cy + 136, "(có nguồn phụ sẵn)", 8.5, INK2, "400", "middle"))
    # duong day
    s.append(L(cx + 71, cy + 84, cx + 71, cy + 71, BAD, "2.6"))
    s.append(L(cx + 71, cy + 71, cx + 150, cy + 71, BAD, "2.6"))
    s.append(L(cx + 224, cy + 71, cx + 320, cy + 71, BAD, "2.6"))
    s.append(L(cx + 320, cy + 71, cx + 320, cy + 78, BAD, "2.6"))
    s += arw(cx + 240, cy + 71, cx + 280, cy + 71, BAD, "2.6")
    s.append(L(cx + 116, cy + 152, cx + 320, cy + 152, BAD, "2.6"))
    s.append(L(cx + 320, cy + 140, cx + 320, cy + 152, BAD, "2.6"))
    s.append(L(cx + 116, cy + 124, cx + 116, cy + 152, BAD, "2.6"))
    s += arw(cx + 240, cy + 152, cx + 200, cy + 152, BAD, "2.6")
    s.append(T(cx + 187, cy + 48, "nguồn 1 — bên ngoài", 9.5, BAD, "700", "middle"))
    s.append(T(cx + 205, cy + 176, "⚠⚠ HAI nguồn nối tiếp trong một vòng → HỎNG ngõ vào module",
               10.5, BAD, "700", "middle"))

    # ── Ô D — cách phòng ──────────────────────────────────────────────
    dx, dy = 466, 302
    s.append(R(dx, dy, 410, 200, fill="#FDF6E7", stroke=RULE, sw="1.2"))
    s.append(T(dx + 205, dy + 26, "Phân biệt bằng cách nào", 12.5, INK, "700", "middle"))
    muc = [
        ("⭐", "Tra SƠ ĐỒ ĐẤU trong datasheet của MODULE"),
        ("", "— trước khi đấu sợi dây đầu tiên."),
        ("⚠", "Đừng suy từ TÊN GỌI của module."),
        ("⚠", "Đừng suy từ module khác của cùng hãng."),
        ("⭐", "Cùng một hãng, hai dòng module có thể"),
        ("", "khác nhau ở đúng điểm này."),
    ]
    for i, (dau, chu) in enumerate(muc):
        y = dy + 56 + i * 21
        if dau:
            s.append(T(dx + 22, y, dau, 11, CUR if dau == "⭐" else BAD, "700"))
        s.append(T(dx + 44, y, chu, 11, INK))

    # ── Dải kết dưới cùng ─────────────────────────────────────────────
    s.append(R(24, 512, 852, 42, fill="#EAF1F6", stroke=INK2, sw="1.2"))
    s.append(T(38, 531,
               "⭐ Hai lỗi cho hai triệu chứng KHÁC NHAU — đọc triệu chứng là biết đấu sai kiểu nào:",
               11, INK, "700"))
    s.append(T(38, 547,
               "Đọc 0 mA suốt → có thể KHÔNG nguồn nào (ít hại, chỉ tốn công tìm).    "
               "Đọc vọt quá 20 mA, hoặc module chết → HAI nguồn.",
               10.5, INK2))
    return save(s, "ch31", "hinh_31_1_ai_cap_nguon_vong.svg")


if __name__ == "__main__":
    fig_31_1()
    for line in log:
        print(line)
