# -*- coding: utf-8 -*-
"""Kiểm cú pháp mọi khối mã ST (```iecst) trong sách.

Chương 1 hứa "mọi đoạn code trong sách đều tự kiểm được". Trước đợt 58 lời hứa đó
không có công cụ nào đứng sau: soát theo PLCopen Coding Guidelines tìm ra `RETURN`
trong khung trình tự, khối `IF` không đóng, và HAI khối khác nhau cùng mang tên
`FB_Cylinder2Pos` với hai giao diện khác nhau ở hai chương. Bộ kiểm này bắt các
lớp lỗi đó một cách máy móc.

Kiểm:
  1. Khối lệnh đóng/mở cân: IF, CASE, FOR, WHILE, REPEAT, VAR…, POU, TYPE, STRUCT.
     ⭐ Khối có dấu lược "…" hoặc "..." là ĐOẠN TRÍCH CÓ CHỦ Ý: được thiếu phần đóng,
     nhưng KHÔNG được đóng sai (END_CASE khi đang mở IF là sai ở mọi loại khối).
  2. Ngoặc tròn, ngoặc vuông cân trong từng khối.
  3. IF/ELSIF phải có THEN · WHILE/FOR phải có DO · CASE phải có OF.
  4. Dấu "=" dùng như phép gán ở đầu một câu lệnh (phải là ":=").
  5. Thiếu ";" ở cuối câu gán khi câu kế tiếp đã là câu lệnh mới.
  6. Gọi khối chuẩn IEC (TON, TOF, TP, R_TRIG, F_TRIG, CTU, CTD, CTUD, SR, RS) với
     tên chân không có thật, hoặc đọc chân không có thật (`T_Move.Done`).
  7. ⭐ Khối do SÁCH tự định nghĩa: cùng một tên nhưng hai giao diện khác nhau; gọi
     hoặc đọc chân không có trong giao diện.
  8. RETURN / EXIT / CONTINUE (PLCopen CP14, L10): chỉ được có khi chính dòng đó,
     hoặc khối đó, đánh dấu là ví dụ SAI / cảnh báo (✗, SAI, CP14, L10).
  9. (đợt 59) CP20 — một thể hiện khối được gọi ở HAI chỗ trở lên trong cùng một khối
     mã. Mẫu "gọi T(IN := FALSE) để xoá rồi gọi lại" từng có ở sáu chỗ trong sách.
 10. (đợt 59) Khai báo `tên : KIỂU;` nằm NGOÀI `VAR … END_VAR` — không biên dịch được.

Không kiểm (giới hạn biết trước): kiểu dữ liệu của biểu thức; biến chưa khai báo;
khối chuyển động MC_* (đặc tả PLCopen Part 1 không có trong bộ tài liệu cục bộ).

Chạy:  python tools/kiem_cu_phap_st.py
"""
import glob
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

DOCS = (sys.argv[1] if len(sys.argv) > 1       # tham số tuỳ chọn: thư mục khác, để thử lỗi cài sẵn
        else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs"))

MO = {"IF": "END_IF", "CASE": "END_CASE", "FOR": "END_FOR", "WHILE": "END_WHILE",
      "REPEAT": "END_REPEAT", "FUNCTION_BLOCK": "END_FUNCTION_BLOCK",
      "FUNCTION": "END_FUNCTION", "PROGRAM": "END_PROGRAM", "TYPE": "END_TYPE",
      "STRUCT": "END_STRUCT", "METHOD": "END_METHOD", "PROPERTY": "END_PROPERTY",
      "INTERFACE": "END_INTERFACE", "ACTION": "END_ACTION", "VAR": "END_VAR"}
DONG = {v: k for k, v in MO.items()}
VAR_MO = re.compile(r"^VAR(_INPUT|_OUTPUT|_IN_OUT|_GLOBAL|_EXTERNAL|_TEMP|_STAT|_INST)?$")
CAN = {"IF": "THEN", "ELSIF": "THEN", "WHILE": "DO", "FOR": "DO", "CASE": "OF"}

# Khối chuẩn IEC 61131-3: (chân vào, chân ra)
CHUAN = {
    "TON": ({"IN", "PT"}, {"Q", "ET"}),
    "TOF": ({"IN", "PT"}, {"Q", "ET"}),
    "TP": ({"IN", "PT"}, {"Q", "ET"}),
    "R_TRIG": ({"CLK"}, {"Q"}),
    "F_TRIG": ({"CLK"}, {"Q"}),
    "CTU": ({"CU", "R", "PV"}, {"Q", "CV"}),
    "CTD": ({"CD", "LD", "PV"}, {"Q", "CV"}),
    "CTUD": ({"CU", "CD", "R", "LD", "PV"}, {"QU", "QD", "CV"}),
    "SR": ({"S1", "R"}, {"Q1"}),
    "RS": ({"S", "R1"}, {"Q1"}),
}

LUOC = re.compile(r"…|\.\.\.")
DANH_DAU_SAI = re.compile(r"✗|\bSAI\b|CP14|L10|⚠")
TOK = re.compile(r"…|\.\.\.|:=|=>|<=|>=|<>|[A-Za-z_][A-Za-z0-9_]*"
                 r"|[0-9][0-9_]*(?:\.[0-9_]+)?(?:[eE][+-]?[0-9]+)?|[;()\[\].=:,]")


def bo_chu_thich(s):
    """Xoá chú thích và chuỗi nhưng GIỮ nguyên số dòng."""
    s = re.sub(r"\(\*.*?\*\)", lambda m: re.sub(r"[^\n]", " ", m.group(0)), s, flags=re.S)
    s = re.sub(r"//[^\n]*", "", s)
    s = re.sub(r"'[^'\n]*'", "''", s)
    return re.sub(r'"[^"\n]*"', '""', s)


def token(s):
    """Danh sách (TOKEN_HOA, token_gốc, số_dòng, đứng_sau_dấu_chấm)."""
    ra = []
    for i, dong in enumerate(s.split("\n"), 1):
        truoc = ""
        for m in TOK.finditer(dong):
            t = m.group(0)
            ra.append((t.upper(), t, i, truoc == "."))
            truoc = t
    return ra


def kiem_khung(s, co_luoc):
    """Mục 1–3: cân khối lệnh, cân ngoặc, từ khoá đi kèm."""
    loi = []
    tk = token(s)
    ngan = []
    for k, (T, _, dong, sau_cham) in enumerate(tk):
        if sau_cham:
            continue
        if T in MO or VAR_MO.match(T):
            ngan.append(("VAR" if VAR_MO.match(T) else T, dong))
        elif T in DONG:
            mo = DONG[T]
            if ngan and ngan[-1][0] == mo:
                ngan.pop()
            else:
                loi.append((dong, "%s nhưng khối đang mở là %s" % (
                    T, "%s (dòng %d)" % ngan[-1] if ngan else "— không có")))
        if T in CAN:
            can = CAN[T]
            for T2, _, _, sc in tk[k + 1:]:
                if sc:
                    continue
                if T2 == can or T2 in ("…", "..."):
                    break
                if T2 in (";", "END_IF", "END_CASE", "END_FOR", "END_WHILE") or T2 in CAN:
                    loi.append((dong, "%s thiếu %s" % (T, can)))
                    break
    if not co_luoc:
        for mo, dong in ngan:
            loi.append((dong, "%s không đóng (khối không có dấu lược nên không phải đoạn trích)"
                        % mo))
    for a, b in (("(", ")"), ("[", "]")):
        if s.count(a) != s.count(b):
            loi.append((1, "ngoặc %s %d cái, %s %d cái" % (a, s.count(a), b, s.count(b))))
    return loi


BAT_DAU = re.compile(r"(;|\bTHEN|\bELSE|\bDO|\bOF|\bEND_VAR|\bREPEAT|^\s*\d+(\s*,\s*\d+)*\s*:)\s*$",
                     re.I)
GAN_BANG = re.compile(r"^\s*[A-Za-z_]\w*(\.\w+|\[[^\]]*\])*\s*=[^=>]")
CAU_MOI = re.compile(r"^\s*([A-Za-z_]\w*(\.\w+|\[[^\]]*\])*\s*:=|(IF|CASE|FOR|WHILE|REPEAT|"
                     r"END_IF|END_CASE|END_FOR|END_WHILE|ELSIF|ELSE|RETURN|EXIT)\b)", re.I)


def kiem_cau_lenh(s):
    """Mục 4–5: '=' thay ':=' · thiếu ';'."""
    loi = []
    dong = s.split("\n")
    trong_var = False
    truoc = ";"
    for i, d in enumerate(dong):
        g = d.strip()
        if not g:
            continue
        H = g.upper()
        if VAR_MO.match(H.split()[0]):
            trong_var = True
        if trong_var:
            if H.startswith("END_VAR"):
                trong_var = False
            truoc = g
            continue
        bat_dau = bool(BAT_DAU.search(truoc)) or truoc == ";"
        if bat_dau and GAN_BANG.match(g) and g.endswith(";") and not LUOC.search(g):
            loi.append((i + 1, "'=' ở đầu câu lệnh — phép gán phải là ':='"))
        if (bat_dau and ":=" in g and not g.endswith(";") and g.count("(") == g.count(")")
                and not LUOC.search(g) and not re.match(r"^\s*(FOR|IF|ELSIF|WHILE|CASE)\b", g, re.I)):
            sau = next((x for x in dong[i + 1:] if x.strip()), "")
            if CAU_MOI.match(sau):
                loi.append((i + 1, "thiếu ';' — dòng sau đã là câu lệnh mới"))
        truoc = g
    return loi


def giao_dien(ma):
    """Trả về {tên_khối: (vào, ra, vào_ra)} cho mọi FUNCTION_BLOCK trong khối mã."""
    ra = {}
    for m in re.finditer(r"\bFUNCTION_BLOCK\s+(\w+)(.*?)(?=\bEND_FUNCTION_BLOCK\b|\Z)", ma, re.S):
        vao, ra_, vr = set(), set(), set()
        for v in re.finditer(r"\b(VAR_INPUT|VAR_OUTPUT|VAR_IN_OUT)\b(.*?)\bEND_VAR\b", m.group(2), re.S):
            dich = {"VAR_INPUT": vao, "VAR_OUTPUT": ra_, "VAR_IN_OUT": vr}[v.group(1)]
            for d in re.finditer(r"^\s*([A-Za-z_][\w\s,]*?)\s*:", v.group(2), re.M):
                for ten in d.group(1).split(","):
                    dich.add(ten.strip())
        ra[m.group(1)] = (frozenset(vao), frozenset(ra_), frozenset(vr))
    return ra


def than_chuan(ma):
    """Trả về {tên_khối: toàn văn đã bỏ khoảng trắng thừa} — để so hai bản cùng tên."""
    return {m.group(1): re.sub(r"\s+", " ", m.group(0)).strip()
            for m in re.finditer(r"\bFUNCTION_BLOCK\s+(\w+).*?(?:\bEND_FUNCTION_BLOCK\b|\Z)", ma, re.S)}


def the_hien(ma):
    """Trả về {tên_thể_hiện: kiểu} từ các khai báo `a, b : KIỂU;` trong VAR."""
    ra = {}
    for v in re.finditer(r"\bVAR\w*\b(.*?)\bEND_VAR\b", ma, re.S):
        for d in re.finditer(r"^\s*([A-Za-z_][\w\s,]*?)\s*:\s*([A-Za-z_]\w*)\s*[;:(]", v.group(1), re.M):
            for ten in d.group(1).split(","):
                ra[ten.strip()] = d.group(2)
    return ra


def kiem_chan(ma, tu_dien, gd):
    """Mục 6–7: tên chân khi gọi và khi đọc."""
    loi = []
    for ten, kieu in tu_dien.items():
        if kieu in CHUAN:
            vao, ra = CHUAN[kieu]
            vr = set()
        elif kieu in gd and gd[kieu] is not None:
            vao, ra, vr = gd[kieu]
        else:
            continue
        for m in re.finditer(r"\b%s\s*\(" % re.escape(ten), ma):
            sau = m.end()
            sau_ngoac, sau_nd = 1, sau
            while sau_nd < len(ma) and sau_ngoac:
                sau_ngoac += {"(": 1, ")": -1}.get(ma[sau_nd], 0)
                sau_nd += 1
            than = ma[sau:sau_nd - 1]
            for a in re.finditer(r"(?:^|[,(\s])(\w+)\s*(:=|=>)", than):
                chan, kieu_gan = a.group(1), a.group(2)
                hop = (vao | vr) if kieu_gan == ":=" else ra
                if chan not in hop:
                    dong = ma[:m.start()].count("\n") + 1
                    loi.append((dong, "%s(%s %s …): khối %s không có chân %s '%s'" % (
                        ten, chan, kieu_gan, kieu, "vào" if kieu_gan == ":=" else "ra", chan)))
        for m in re.finditer(r"\b%s\.(\w+)" % re.escape(ten), ma):
            if m.group(1) not in (vao | ra | vr):
                dong = ma[:m.start()].count("\n") + 1
                loi.append((dong, "%s.%s: khối %s không có chân '%s'" % (
                    ten, m.group(1), kieu, m.group(1))))
    return loi


HAM_CHUAN = {
    "ABS", "SQRT", "LN", "LOG", "EXP", "EXPT", "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN",
    "ADD", "SUB", "MUL", "DIV", "MOD", "MOVE", "SHL", "SHR", "ROL", "ROR", "SEL", "MAX", "MIN",
    "LIMIT", "MUX", "GT", "GE", "EQ", "LE", "LT", "NE", "LEN", "LEFT", "RIGHT", "MID", "CONCAT",
    "INSERT", "DELETE", "REPLACE", "FIND", "TRUNC", "SIZEOF", "ADR",
}


def kiem_goi_doi(ma_goc, s, tu_dien, gd, ham_sach):
    """Mục 9 — CP20: mỗi thể hiện chỉ một chỗ gọi trong một khối (trừ ví dụ SAI).

    Thể hiện = tên có trong bảng khai báo với kiểu là khối, HOẶC tên được gọi với tham số có tên
    (`X(IN := …)`) mà không phải hàm chuẩn / hàm của sách — để bắt cả đoạn trích không khai báo.
    """
    if re.search(r"^\s*//.*(✗|\bSAI\b)", ma_goc, re.M):
        return []
    loi = []
    ung_vien = {t for t, k in tu_dien.items() if k in CHUAN or (k in gd and gd[k] is not None)}
    for m in re.finditer(r"(?<![\w.])([A-Za-z_]\w*)\s*\(([^()]*(?:\([^()]*\)[^()]*)*)\)", s):
        ten = m.group(1)
        if (re.search(r"\b\w+\s*(:=|=>)", m.group(2)) and ten.upper() not in HAM_CHUAN
                and ten not in ham_sach and "_TO_" not in ten.upper()):
            ung_vien.add(ten)
    for ten in sorted(ung_vien):
        cho = [m.start() for m in re.finditer(r"(?<![\w.])%s\s*\(" % re.escape(ten), s)]
        if len(cho) > 1:
            dong = s[:cho[1]].count("\n") + 1
            loi.append((dong, "%s được gọi ở %d chỗ trong một khối — mỗi thể hiện gọi đúng MỘT "
                        "lần mỗi vòng quét (PLCopen CP20)" % (ten, len(cho))))
    return loi


KHAI_BAO = re.compile(r"^\s*[A-Za-z_]\w*(\s*,\s*[A-Za-z_]\w*)*\s*:\s*"
                      r"(ARRAY\b.*|[A-Za-z_]\w*(\s*\(.*\))?)\s*(:=.*)?;\s*$")


def kiem_khai_bao(s):
    """Mục 10 — khai báo biến phải nằm trong VAR…END_VAR (hoặc STRUCT / TYPE)."""
    loi, sau = [], 0
    for i, d in enumerate(s.split("\n"), 1):
        tu = d.strip().upper().split()
        dau = tu[0].rstrip(";") if tu else ""
        if VAR_MO.match(dau) or dau in ("STRUCT", "TYPE"):
            sau += 1
        elif dau in ("END_VAR", "END_STRUCT", "END_TYPE"):
            sau = max(0, sau - 1)
        elif not sau and KHAI_BAO.match(d):
            loi.append((i, "khai báo '%s' nằm NGOÀI VAR … END_VAR" % d.strip()[:40]))
    return loi


def kiem_thoat(ma_goc, s):
    """Mục 8: RETURN / EXIT / CONTINUE."""
    loi = []
    khoi_sai = bool(re.search(r"^\s*//.*(✗|\bSAI\b)", ma_goc, re.M))
    goc = ma_goc.split("\n")
    for i, d in enumerate(s.split("\n"), 1):
        for m in re.finditer(r"\b(RETURN|EXIT|CONTINUE)\b", d, re.I):
            if khoi_sai or DANH_DAU_SAI.search(goc[i - 1]):
                continue
            loi.append((i, "%s — PLCopen %s: chỉ dùng trong ví dụ SAI có đánh dấu" % (
                m.group(1).upper(), "CP14" if m.group(1).upper() == "RETURN" else "L10")))
    return loi


def main():
    khoi = []   # (tệp, dòng_bắt_đầu, mã)
    for p in sorted(glob.glob(os.path.join(DOCS, "*.md"))):
        ten = os.path.basename(p)
        if ten.startswith("00"):
            continue
        s = io.open(p, encoding="utf-8").read()
        for m in re.finditer(r"^```iecst\n(.*?)^```", s, flags=re.S | re.M):
            khoi.append((ten, s[:m.start()].count("\n") + 2, m.group(1)))

    # Hàm do sách tự định nghĩa — gọi nhiều lần là bình thường, không phải thể hiện khối
    ham_sach = set()
    for _, _, ma in khoi:
        ham_sach |= set(re.findall(r"\bFUNCTION\s+(\w+)", bo_chu_thich(ma)))

    # Mục 7a — cùng tên thì phải là CÙNG một khối: cùng giao diện, và cùng cả phần thân
    noi_dn = {}
    for ten, d0, ma in khoi:
        s = bo_chu_thich(ma)
        than = than_chuan(s)
        for fb, g in giao_dien(s).items():
            noi_dn.setdefault(fb, []).append((g, than[fb], ten, d0))
    gd, loi_tong = {}, []
    for fb, ds in noi_dn.items():
        noi = " · ".join("%s:%d" % (t, d) for _, _, t, d in ds)
        if len({g for g, _, _, _ in ds}) > 1:
            gd[fb] = None
            loi_tong.append(("*", 0, "khối %s định nghĩa %d lần với GIAO DIỆN KHÁC NHAU: %s"
                             % (fb, len(ds), noi)))
            continue
        gd[fb] = ds[0][0]
        if len({t for _, t, _, _ in ds}) > 1:
            loi_tong.append(("*", 0, "khối %s có %d bản cùng giao diện nhưng THÂN KHÁC NHAU — "
                             "sửa một bản là hai bản trôi dạt: %s" % (fb, len(ds), noi)))

    # Thể hiện: khai báo trong CÙNG tệp trước; nếu không có thì dùng khai báo ở tệp khác,
    # miễn là cả sách chỉ khai báo tên đó với ĐÚNG MỘT kiểu (Ch.57 đọc `Stop1.Valve` mà
    # thể hiện được khai báo ở Ch.27).
    the_hien_tep, toan_sach = {}, {}
    for ten, _, ma in khoi:
        th = the_hien(bo_chu_thich(ma))
        the_hien_tep.setdefault(ten, {}).update(th)
        for k, v in th.items():
            toan_sach.setdefault(k, set()).add(v)
    chung = {k: next(iter(v)) for k, v in toan_sach.items() if len(v) == 1}

    for ten, d0, ma in khoi:
        s = bo_chu_thich(ma)
        co_luoc = bool(LUOC.search(s))
        loi = kiem_khung(s, co_luoc) + kiem_cau_lenh(s) + kiem_thoat(ma, s)
        tu_dien = dict(chung)
        tu_dien.update(the_hien_tep[ten])
        loi += kiem_chan(s, tu_dien, gd)
        loi += kiem_goi_doi(ma, s, tu_dien, gd, ham_sach) + kiem_khai_bao(s)
        for dong, noi_dung in loi:
            loi_tong.append((ten, d0 + dong - 1, noi_dung))

    print("=" * 78)
    print("KIỂM CÚ PHÁP ST — %d khối iecst" % len(khoi))
    print("=" * 78)
    for ten, dong, nd in loi_tong:
        if ten == "*":
            print("  [LỖI] %s" % nd)
        else:
            print("  [LỖI] %-40s :%-5d %s" % (ten[:40], dong, nd))
    print("-" * 78)
    print("TỔNG:  %d LỖI" % len(loi_tong))
    print("-" * 78)
    return 1 if loi_tong else 0


if __name__ == "__main__":
    sys.exit(main())
