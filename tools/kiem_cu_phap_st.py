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
 11. (đợt 62) ⭐ Kiểu cấu trúc / liệt kê cùng tên phải là CÙNG MỘT kiểu — sách từng có
     ba `ST_Station` khác nhau. Bản trong khối có dấu lược được phép là TẬP CON.
 12. (đợt 62) `biến.trường` — trường phải có thật trong kiểu cấu trúc của biến.
 13. (đợt 62) ⭐⭐ Khối mở đầu bằng `// ✔ VÍ DỤ HOÀN CHỈNH` phải TỰ ĐỦ khai báo: mọi
     biến dùng đến đều khai trong chính khối (kể cả I/O, qua VAR_GLOBAL/VAR_EXTERNAL);
     mọi kiểu phải có thật (chuẩn, hoặc định nghĩa ở đâu đó trong sách, hoặc MC_*/AXIS_REF
     của thư viện chuyển động); không dấu lược; biến cục bộ khai mà không dùng là lỗi
     (PLCopen CP24). Khối khai báo có thêm chữ "sơ đồ ở khối kế tiếp" thì mọi tên có
     dấu gạch dưới trong sơ đồ (LD/FBD/SFC) ở khối ngay sau cũng phải được khai.
 14. (đợt 62) ⭐⭐ Thể hiện khối gọi BÊN TRONG nhánh IF/CASE — Phụ lục B mục B.9b: khối
     không được gọi thì không thấy sườn xuống, nên lần thứ hai đi qua nhánh đó nó không
     chạy (đợt 61–62 tìm ra 7 chỗ như vậy, cả 7 chỉ lộ ra ở chu trình thứ hai). Được
     phép khi dòng gọi hoặc dòng ngay trên có chữ "CỐ Ý" kèm lý do (PID gọi theo nhịp).
 15. (đợt 62) Đầu vào sườn là HẰNG: `CLK := TRUE/FALSE`, `Execute := TRUE` — không bao
     giờ tạo được sườn thứ hai.
 16. (đợt 62) `CASE XStep OF` mà trong nhánh lại gán số cho một biến bước KHÁC
     (`Step := 20` trong `CASE LoadStep`) — trình tự không bao giờ tiến.

Không kiểm (giới hạn biết trước): kiểu dữ liệu của biểu thức; biến chưa khai báo trong
ĐOẠN TRÍCH (khối không có dấu hiệu hoàn chỉnh); khối chuyển động MC_* (đặc tả PLCopen
Part 1 không có trong bộ tài liệu cục bộ).

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
      "INTERFACE": "END_INTERFACE", "ACTION": "END_ACTION", "VAR": "END_VAR",
      "PROPERTY_GET": "END_PROPERTY", "PROPERTY_SET": "END_PROPERTY",   # bản 4 (2025)
      "INITIAL_STEP": "END_STEP", "STEP": "END_STEP", "TRANSITION": "END_TRANSITION"}  # SFC văn bản
DONG = {v: k for k, v in MO.items()}
DONG["END_PROPERTY"] = "PROPERTY"
DONG["END_STEP"] = "STEP"
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
    for k, (T, goc_tk, dong, sau_cham) in enumerate(tk):
        if sau_cham:
            continue
        if T in SFC_VB and not la_sfc_van_ban(tk, k):
            continue                                     # `Step` là tên biến, không phải từ khoá SFC
        if T in MO or VAR_MO.match(T):
            ngan.append(("VAR" if VAR_MO.match(T) else T, dong))
        elif T in DONG:
            mo = DONG[T]
            if ngan and MO.get(ngan[-1][0]) == T:        # PROPERTY / PROPERTY_GET / _SET cùng đóng
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


SFC_VB = {"INITIAL_STEP", "STEP", "END_STEP", "TRANSITION", "END_TRANSITION"}


def la_sfc_van_ban(tk, k):
    """Từ khoá SFC dạng văn bản chỉ khi VIẾT HOA và đúng hình: `STEP Ten :` · `TRANSITION FROM`."""
    T, goc_tk = tk[k][0], tk[k][1]
    if goc_tk != T:
        return False
    if T in ("END_STEP", "END_TRANSITION"):
        return True
    sau = [x[0] for x in tk[k + 1:k + 3]]
    if T == "TRANSITION":
        return bool(sau) and (sau[0] == "FROM" or (len(sau) > 1 and sau[1] == "FROM"))
    return len(sau) == 2 and re.match(r"[A-Z_]", sau[0]) is not None and sau[1] == ":"


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
        # Phương thức và thuộc tính cũng là thành viên đọc/gọi được qua dấu chấm: `Stn2.IsEmpty()`
        for t in re.finditer(r"\b(?:METHOD|PROPERTY(?:_GET|_SET)?)\s+(?:(?:PUBLIC|PRIVATE|PROTECTED|INTERNAL"
                             r"|ABSTRACT|FINAL|OVERRIDE)\s+)*(\w+)", m.group(2)):
            ra_.add(t.group(1))
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


# ─────────────────────────────────────────────────────────────────────────────
# Đợt 62 — kiểu người dùng, trường cấu trúc, ví dụ hoàn chỉnh
# ─────────────────────────────────────────────────────────────────────────────

DAU_HOAN_CHINH = re.compile(r"^\s*//\s*✔\s*VÍ DỤ HOÀN CHỈNH")
SO_DO_KE_TIEP = re.compile(r"sơ đồ ở khối kế tiếp")

TU_KHOA = {
    "IF", "THEN", "ELSIF", "ELSE", "END_IF", "CASE", "OF", "END_CASE", "FOR", "TO", "BY", "DO",
    "END_FOR", "WHILE", "END_WHILE", "REPEAT", "UNTIL", "END_REPEAT", "EXIT", "RETURN",
    "CONTINUE", "AND", "OR", "XOR", "NOT", "MOD", "TRUE", "FALSE", "VAR", "VAR_INPUT",
    "VAR_OUTPUT", "VAR_IN_OUT", "VAR_GLOBAL", "VAR_EXTERNAL", "VAR_TEMP", "VAR_STAT", "VAR_INST",
    "END_VAR", "CONSTANT", "RETAIN", "PERSISTENT", "NON_RETAIN", "AT", "FUNCTION",
    "FUNCTION_BLOCK", "PROGRAM", "END_FUNCTION", "END_FUNCTION_BLOCK", "END_PROGRAM", "TYPE",
    "END_TYPE", "STRUCT", "END_STRUCT", "ARRAY", "POINTER", "REFERENCE", "REF", "REF_TO", "THIS",
    "SUPER", "METHOD", "END_METHOD", "PROPERTY", "END_PROPERTY", "PROPERTY_GET", "PROPERTY_SET",
    "INTERFACE", "END_INTERFACE", "EXTENDS", "IMPLEMENTS", "PUBLIC", "PRIVATE", "PROTECTED",
    "INTERNAL", "ABSTRACT", "FINAL", "OVERRIDE", "ACTION", "END_ACTION", "NULL",
    "INITIAL_STEP", "STEP", "END_STEP", "TRANSITION", "END_TRANSITION", "FROM",
}
BO_NGU = re.compile(r"\(\s*(?:N|R|S|P|P0|P1|L|D|SD|DS|SL)\s*(?:,[^)]*)?\)")  # bổ ngữ hành động SFC
KIEU_CHUAN = {
    "BOOL", "BYTE", "WORD", "DWORD", "LWORD", "SINT", "INT", "DINT", "LINT", "USINT", "UINT",
    "UDINT", "ULINT", "REAL", "LREAL", "TIME", "LTIME", "DATE", "LDATE", "TIME_OF_DAY", "TOD",
    "LTOD", "DATE_AND_TIME", "DT", "LDT", "STRING", "WSTRING", "CHAR", "WCHAR", "USTRING", "UCHAR",
}
LITERAL_CO_KIEU = re.compile(
    r"\b(?:T|TIME|LT|LTIME|D|DATE|LD|LDATE|TOD|TIME_OF_DAY|LTOD|DT|DATE_AND_TIME|LDT|BOOL|SINT|"
    r"INT|DINT|LINT|USINT|UINT|UDINT|ULINT|REAL|LREAL|BYTE|WORD|DWORD|LWORD|2|8|16)"
    r"#[\w.:+\-]+", re.I)
DIA_CHI = re.compile(r"%[IQM][XBWDL]?[\d.]+", re.I)


def dinh_nghia_kieu(s):
    """{tên: ("STRUCT", {trường: kiểu}) | ("ENUM", [giá trị])} của mọi TYPE trong khối."""
    ra = {}
    for m in re.finditer(r"\bTYPE\s+(\w+)\s*:\s*(.*?)\bEND_TYPE\b", s, re.S):
        ten, than = m.group(1), m.group(2)
        cs = re.match(r"\s*STRUCT\b(.*?)\bEND_STRUCT\b", than, re.S)
        if cs:
            truong = {}
            for d in re.finditer(r"^\s*([A-Za-z_][\w\s,]*?)\s*:\s*(ARRAY\b.*?\bOF\s+)?([A-Za-z_]\w*)",
                                 cs.group(1), re.M):
                for t in d.group(1).split(","):
                    truong[t.strip()] = ("[]" if d.group(2) else "") + d.group(3)
            ra[ten] = ("STRUCT", truong)
            continue
        ce = re.match(r"\s*\(([^)]*)\)", than, re.S)
        if ce:
            ra[ten] = ("ENUM", [re.sub(r":=.*", "", v).strip() for v in ce.group(1).split(",")])
    return ra


def kiem_kieu_trung(khoi):
    """Mục 11 — cùng tên kiểu thì cùng định nghĩa; bản có dấu lược được là tập con."""
    noi = {}
    for ten, d0, ma in khoi:
        s = bo_chu_thich(ma)
        luoc = bool(LUOC.search(ma))
        for k, v in dinh_nghia_kieu(s).items():
            noi.setdefault(k, []).append((v, luoc, ten, d0))
    loi, dang_ky = [], {}
    for k, ds in noi.items():
        day_du = [x for x in ds if not x[1]]
        chuan = day_du[0][0] if day_du else ds[0][0]
        dang_ky[k] = chuan
        cho = " · ".join("%s:%d" % (t, d) for _, _, t, d in ds)
        if len({repr(sorted(x[0][1].items()) if x[0][0] == "STRUCT" else x[0])
                for x in day_du}) > 1:
            loi.append(("*", 0, "kiểu %s định nghĩa %d lần KHÁC NHAU: %s" % (k, len(ds), cho)))
            continue
        for v, luoc, t, d in ds:
            if luoc and v[0] == "STRUCT" and chuan[0] == "STRUCT":
                thua = {f: ft for f, ft in v[1].items() if chuan[1].get(f) != ft}
                if thua:
                    loi.append((t, d, "kiểu %s (bản trích) có trường không khớp bản đầy đủ: %s"
                                % (k, ", ".join(sorted(thua)))))
    return loi, dang_ky


def mang_the_hien(s):
    """{tên_mảng: kiểu_phần_tử} từ `x : ARRAY[..] OF KIỂU;`."""
    ra = {}
    for v in re.finditer(r"\bVAR\w*\b(.*?)\bEND_VAR\b", s, re.S):
        for d in re.finditer(r"^\s*([A-Za-z_][\w\s,]*?)\s*:\s*ARRAY\s*\[[^\]]*\]\s*OF\s+(\w+)",
                             v.group(1), re.M):
            for t in d.group(1).split(","):
                ra[t.strip()] = d.group(2)
    return ra


def kiem_truong(ma_goc, s, tu_dien, mang, kieu):
    """Mục 12 — `biến.trường` (và `mảng[i].trường`, lồng nhiều cấp) phải có thật.

    Dòng có dấu ✗/SAI, hoặc ngay dưới một chú thích có dấu đó, là ví dụ sai CÓ CHỦ Ý — bỏ qua.
    """
    loi = []
    goc = ma_goc.split("\n")
    for m in re.finditer(r"(?<![\w.#])([A-Za-z_]\w*)(\[[^\]]*\])?((?:\.[A-Za-z_]\w*)+)", s):
        i = s[:m.start()].count("\n")
        if re.search(r"✗|\bSAI\b", goc[i] + (goc[i - 1] if i else "")):
            continue
        k = mang.get(m.group(1)) if m.group(2) else tu_dien.get(m.group(1))
        for f in m.group(3).split(".")[1:]:
            if k not in kieu or kieu[k][0] != "STRUCT":
                break
            if f not in kieu[k][1]:
                loi.append((s[:m.start()].count("\n") + 1, "%s: kiểu %s không có trường '%s'"
                            % (m.group(0), k, f)))
                break
            k = kieu[k][1][f].lstrip("[]")
    return loi


def ten_khai_bao(s):
    """(biến khai báo: {tên: loại_VAR}, tên kiểu được nhắc trong phần khai báo)."""
    bien, kieu_nhac = {}, set()
    for v in re.finditer(r"\b(VAR\w*)\b(.*?)\bEND_VAR\b", s, re.S):
        than_var = re.sub(r"^\s*(?:CONSTANT|RETAIN|PERSISTENT|NON_RETAIN)\b", "", v.group(2))
        for d in re.finditer(r"^[ \t]*([A-Za-z_][\w \t,]*?)[ \t]*(?:AT\s+\S+\s*)?:\s*([^;]*);",
                             than_var, re.M):
            for t in d.group(1).split(","):
                bien[t.strip()] = v.group(1).upper()
            vong = re.split(r":=", d.group(2), maxsplit=1)[0]
            kieu_nhac |= set(re.findall(r"[A-Za-z_]\w*", vong)) - TU_KHOA
    return bien, kieu_nhac


def kiem_hoan_chinh(ma, s, the_gioi, so_do=None):
    """Mục 13 — ví dụ hoàn chỉnh phải tự đủ khai báo; `the_gioi` là tên đã biết cả sách."""
    loi = []
    if LUOC.search(s):
        loi.append((1, "ví dụ hoàn chỉnh không được có dấu lược — hoặc bỏ dấu hiệu ✔"))
    bien, kieu_nhac = ten_khai_bao(s)
    pou = set(re.findall(r"\b(?:FUNCTION_BLOCK|FUNCTION|PROGRAM|METHOD|PROPERTY(?:_GET|_SET)?"
                         r"|INTERFACE|ACTION|TYPE|INITIAL_STEP|STEP)\s+(?:(?:PUBLIC|PRIVATE|PROTECTED"
                         r"|INTERNAL|ABSTRACT|FINAL|OVERRIDE)\s+)*(\w+)", s))
    s = BO_NGU.sub("", s)
    cac_kieu = the_gioi["kieu"] | pou | set(CHUAN) | KIEU_CHUAN
    for k in sorted(kieu_nhac):
        if k not in cac_kieu and not k.startswith(("MC_", "AXIS_REF")) and not k.isdigit():
            loi.append((1, "kiểu '%s' không có ở đâu trong sách, cũng không phải kiểu chuẩn" % k))
    biet = set(bien) | pou | the_gioi["kieu"] | the_gioi["enum"] | set(CHUAN) | KIEU_CHUAN
    s2 = DIA_CHI.sub("0", LITERAL_CO_KIEU.sub("0", s))
    s2 = re.sub(r"\b\w+#(\w+)", r"\1", s2)                  # E_X#Gia_tri → Gia_tri
    # bỏ phần khai báo (tên biến bên trái dấu ':'), giữ giá trị khởi tạo sau ':='
    s3 = re.sub(r"\b(VAR\w*)\b(.*?)\bEND_VAR\b",
                lambda m: "\n".join((x.split(":=", 1)[1] if ":=" in x else "")
                                    for x in m.group(2).split("\n")), s2, flags=re.S)
    dung = set()
    sau_so = 0
    muc = 0                                                  # độ sâu ngoặc — tính XUYÊN dòng
    for i, dong in enumerate(s3.split("\n"), 1):
        tk = list(re.finditer(r":=|=>|[()]|[A-Za-z_]\w*|\.", dong))
        for j, m in enumerate(tk):
            t = m.group(0)
            if t == "(":
                muc += 1
                continue
            if t == ")":
                muc = max(0, muc - 1)
                continue
            if not re.match(r"[A-Za-z_]", t):
                continue
            if j and tk[j - 1].group(0) == ".":
                continue
            ke = tk[j + 1].group(0) if j + 1 < len(tk) else ""
            if muc > 0 and ke in (":=", "=>"):
                continue                                     # tên chân khi gọi khối
            T = t.upper()
            if T in TU_KHOA or T in HAM_CHUAN or "_TO_" in T or t in the_gioi["ham"]:
                continue
            if t.startswith(("MC_", "AXIS_REF")):
                continue
            dung.add(t)
            if t not in biet:
                loi.append((i, "'%s' dùng mà không khai báo trong ví dụ hoàn chỉnh" % t))
                biet.add(t)                                  # báo mỗi tên một lần
        sau_so = i
    if so_do is not None:
        dung |= set(re.findall(r"\b[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]*\b", so_do))
    for t, loai in sorted(bien.items()):
        if loai in ("VAR", "VAR_TEMP") and t not in dung and t not in pou:
            loi.append((1, "biến cục bộ '%s' khai báo mà không dùng (PLCopen CP24)" % t))
    if so_do is not None:
        khai = set(bien) | pou
        for t in sorted(set(re.findall(r"\b[A-Za-z][A-Za-z0-9]*_[A-Za-z0-9_]*\b", so_do))):
            if t not in khai and not t.startswith(("MC_",)) and t.upper() not in HAM_CHUAN:
                loi.append((sau_so, "sơ đồ ở khối kế tiếp dùng '%s' — chưa khai báo ở khối này" % t))
    return loi


def kiem_goi_trong_nhanh(ma_goc, s, ham_sach):
    """Mục 14–16 — gọi khối trong nhánh · đầu vào sườn là hằng · CASE lệch biến bước."""
    if re.search(r"^\s*//.*(✗|\bSAI\b)", ma_goc, re.M):
        return []
    loi, ngan = [], []
    goc = ma_goc.split("\n")
    MO_K = {"IF", "CASE", "FOR", "WHILE", "REPEAT"}
    DONG_K = {"END_IF", "END_CASE", "END_FOR", "END_WHILE", "END_REPEAT"}
    for i, dong in enumerate(s.split("\n"), 1):
        for t in re.finditer(r"(?<![\w.])(IF|CASE|FOR|WHILE|REPEAT|END_IF|END_CASE|END_FOR|"
                             r"END_WHILE|END_REPEAT)\b|(?<![\w.])([A-Za-z_]\w*)\s*\((?=[^;]*(:=|=>))",
                             dong):
            k = t.group(1)
            if k in MO_K:
                ten_case = re.match(r"\s*(\w+)\s+OF\b", dong[t.end():]) if k == "CASE" else None
                ngan.append((k, ten_case.group(1) if ten_case else None))
                continue
            if k in DONG_K:
                if ngan:
                    ngan.pop()
                continue
            ten = t.group(2)
            if (not ten or ten.upper() in HAM_CHUAN or ten in ham_sach or "_TO_" in ten.upper()
                    or ten.upper() in TU_KHOA):
                continue
            if any(x[0] in ("IF", "CASE") for x in ngan) and not any(x[0] == "FOR" for x in ngan):
                tren = goc[i - 2] if i >= 2 else ""
                if "CỐ Ý" not in goc[i - 1] and "CỐ Ý" not in tren:
                    loi.append((i, "%s được gọi BÊN TRONG nhánh %s — khối không được gọi thì không "
                                "thấy sườn xuống; gọi mỗi vòng, ngoài nhánh, đầu vào lấy từ trạng "
                                "thái (Phụ lục B mục B.9b)" % (ten, "/".join(x[0] for x in ngan))))
        for m in re.finditer(r"\b(CLK)\s*:=\s*(TRUE|FALSE)\b|\b(Execute)\s*:=\s*TRUE\b", dong):
            loi.append((i, "%s là HẰNG — không bao giờ có sườn thứ hai" % m.group(0)))
        for m in re.finditer(r"(?:^|;)\s*(?:\d+\s*:\s*)?([A-Za-z_][\w.]*)\s*:=\s*\d+\s*;", dong):
            chon = next((x[1] for x in reversed(ngan) if x[0] == "CASE"), None)
            dich = m.group(1)
            if (chon and chon.upper().endswith("STEP") and dich.upper().endswith("STEP")
                    and dich != chon and not dich.upper().endswith(("FAULTSTEP", "PREVSTEP"))):
                loi.append((i, "CASE %s nhưng nhánh gán '%s' — trình tự không tiến" % (chon, m.group(0).strip())))
    return loi


def main():
    khoi = []   # (tệp, dòng_bắt_đầu, mã)
    so_do_sau = {}   # (tệp, dòng_bắt_đầu) của khối iecst → nội dung khối mã NGAY SAU nó
    for p in sorted(glob.glob(os.path.join(DOCS, "*.md"))):
        ten = os.path.basename(p)
        if ten.startswith("00"):
            continue
        s = io.open(p, encoding="utf-8").read()
        tat_ca = list(re.finditer(r"^```(\w*)\n(.*?)^```", s, flags=re.S | re.M))
        for j, m in enumerate(tat_ca):
            if m.group(1) != "iecst":
                continue
            d0 = s[:m.start()].count("\n") + 2
            khoi.append((ten, d0, m.group(2)))
            if j + 1 < len(tat_ca):
                so_do_sau[(ten, d0)] = tat_ca[j + 1].group(2)

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

    # Mục 11 — kiểu người dùng; và "thế giới" tên đã biết của cả sách cho mục 13
    loi_kieu, kieu = kiem_kieu_trung(khoi)
    loi_tong += loi_kieu
    the_gioi = {"kieu": set(kieu) | set(gd), "enum": set(), "ham": set(ham_sach)}
    for v in kieu.values():
        if v[0] == "ENUM":
            the_gioi["enum"] |= set(v[1])
    mang_tep, mang_toan = {}, {}
    for ten, _, ma in khoi:
        s = bo_chu_thich(ma)
        the_gioi["kieu"] |= set(re.findall(r"\b(?:INTERFACE|FUNCTION_BLOCK)\s+(\w+)", s))
        the_gioi["ham"] |= set(re.findall(r"\bPROGRAM\s+(\w+)", s))
        mg = mang_the_hien(s)
        mang_tep.setdefault(ten, {}).update(mg)
        for k, v in mg.items():
            mang_toan.setdefault(k, set()).add(v)
    mang_chung = {k: next(iter(v)) for k, v in mang_toan.items() if len(v) == 1}

    so_hoan_chinh = 0
    for ten, d0, ma in khoi:
        s = bo_chu_thich(ma)
        co_luoc = bool(LUOC.search(s))
        loi = kiem_khung(s, co_luoc) + kiem_cau_lenh(s) + kiem_thoat(ma, s)
        tu_dien = dict(chung)
        tu_dien.update(the_hien_tep[ten])
        loi += kiem_chan(s, tu_dien, gd)
        loi += kiem_goi_doi(ma, s, tu_dien, gd, ham_sach) + kiem_khai_bao(s)
        mang = dict(mang_chung)
        mang.update(mang_tep[ten])
        loi += kiem_truong(ma, s, tu_dien, mang, kieu)
        loi += kiem_goi_trong_nhanh(ma, s, ham_sach)
        dau = next((x for x in ma.split("\n") if x.strip()), "")
        if DAU_HOAN_CHINH.match(dau):
            so_hoan_chinh += 1
            so_do = so_do_sau.get((ten, d0)) if SO_DO_KE_TIEP.search(dau) else None
            loi += kiem_hoan_chinh(ma, s, the_gioi, so_do)
        for dong, noi_dung in loi:
            loi_tong.append((ten, d0 + dong - 1, noi_dung))

    print("=" * 78)
    print("KIỂM CÚ PHÁP ST — %d khối iecst · %d ví dụ hoàn chỉnh · %d kiểu người dùng"
          % (len(khoi), so_hoan_chinh, len(kieu)))
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
