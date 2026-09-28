# -*- coding: utf-8 -*-
"""Bộ chạy thử ST tối giản — đủ cho các ví dụ hoàn chỉnh của sách (đợt 62).

Đọc: TYPE (STRUCT, liệt kê), VAR_GLOBAL, FUNCTION, FUNCTION_BLOCK, PROGRAM; câu lệnh gán, IF, CASE,
FOR, WHILE, REPEAT, gọi khối/hàm có tên chân; biểu thức theo thứ tự ưu tiên IEC 61131-3.
Khối chuẩn: TON, TOF, TP (tính ET = bây giờ − lúc bắt đầu — KHÔNG gọi thì không tạm dừng, theo tài
liệu S7-1200 và Logix 5000, Phụ lục B mục B.9b), R_TRIG (bộ nhớ khởi tạo FALSE), F_TRIG (bộ nhớ
khởi tạo TRUE), CTU, CTD, CTUD, SR, RS. Tên không phân biệt hoa thường (như chuẩn).

SFC dạng văn bản (đợt 63): INITIAL_STEP/STEP … END_STEP, TRANSITION FROM … TO … := điều kiện;
END_TRANSITION — kể cả nhiều bước ở hai đầu (nhánh song song). Hành động là biến BOOL với bổ ngữ N.
Một vòng quét theo "cách thực thi điển hình" của PLCopen (Structuring with SFC, mục 3.6.1): xét
chuyển tiếp theo trạng thái ĐẦU vòng → đổi bước → đặt biến hành động theo trạng thái MỚI. `.T` về 0
khi vào bước, GIỮ giá trị lúc rời (chuẩn, mục 2.1); đặt May.t_khi_roi = "ve0" để thử hệ đặt lại khi
rời bước. Hai chuyển tiếp cùng đúng từ một bước → ghi vào the.nhap_nhang (luật loại trừ nhau, 4.3).

⚠ Giới hạn biết trước: không kiểm kiểu dữ liệu, không mô phỏng tràn số nguyên, không có LD, FBD,
phương thức hay giao diện; SFC chưa có ACTION … END_ACTION và các bổ ngữ khác N. Nó là MÔ HÌNH để thử
logic qua nhiều vòng quét — không phải PLC.
Kịch bản thử nằm ở kich_ban.py cùng thư mục.

Dùng:
    m = May(ma_st)                  # nạp mọi POU/kiểu/biến toàn cục
    m.dat("DI_BoardStn1", True)     # ghi biến toàn cục (hoặc "Prg.Bien")
    m.quet("Prg_X", ms=10)          # tăng đồng hồ rồi chạy một vòng quét của chương trình
    m.doc("Stn1.Ready")
"""
import re

TU_KHOA = {
    "IF", "THEN", "ELSIF", "ELSE", "END_IF", "CASE", "OF", "END_CASE", "FOR", "TO", "BY", "DO",
    "END_FOR", "WHILE", "END_WHILE", "REPEAT", "UNTIL", "END_REPEAT", "EXIT", "RETURN", "CONTINUE",
    "AND", "OR", "XOR", "NOT", "MOD", "TRUE", "FALSE", "END_VAR", "VAR", "VAR_INPUT", "VAR_OUTPUT",
    "VAR_IN_OUT", "VAR_GLOBAL", "VAR_EXTERNAL", "VAR_TEMP", "CONSTANT", "RETAIN", "PERSISTENT",
    "FUNCTION", "FUNCTION_BLOCK", "PROGRAM", "END_FUNCTION", "END_FUNCTION_BLOCK", "END_PROGRAM",
    "TYPE", "END_TYPE", "STRUCT", "END_STRUCT", "ARRAY", "AT",
}


class LoiST(Exception):
    pass


# ───────────────────────────── Tách từ ─────────────────────────────
TOK = re.compile(r"""
  (?P<chuoi>'[^']*')
 |(?P<thoigian>(?:T|TIME|LT|LTIME)\#[-\w.]+)
 |(?P<cokieu>(?:2|8|16)\#[0-9A-Fa-f_]+|(?:[A-Za-z]+INT|BOOL|REAL|LREAL|BYTE|WORD|DWORD)\#[-\w.]+)
 |(?P<so>\d[\d_]*\.\d[\d_]*(?:[eE][-+]?\d+)?|\d[\d_]*[eE][-+]?\d+|\d[\d_]*)
 |(?P<ten>[A-Za-z_]\w*(?:\#[A-Za-z_]\w*)?)
 |(?P<toan>:=|=>|<=|>=|<>|\*\*|\.\.|[-+*/()\[\],;:.=<>&])
 |(?P<cach>\s+)
""", re.X)


def bo_chu_thich(s):
    s = re.sub(r"\(\*.*?\*\)", " ", s, flags=re.S)
    return re.sub(r"//[^\n]*", "", s)


def doc_thoi_gian(t):
    """T#1H2M3S4MS → mili-giây (số nguyên)."""
    v = t.split("#", 1)[1].replace("_", "").upper()
    am = v.startswith("-")
    v = v.lstrip("-")
    tong = 0.0
    for so, dv in re.findall(r"(\d+(?:\.\d+)?)(MS|D|H|M|S)", v):
        tong += float(so) * {"D": 86400000, "H": 3600000, "M": 60000, "S": 1000, "MS": 1}[dv]
    return int(round(-tong if am else tong))


def tach(s):
    ra = []
    for m in TOK.finditer(bo_chu_thich(s)):
        loai = m.lastgroup
        v = m.group(0)
        if loai == "cach":
            continue
        if loai == "chuoi":
            ra.append(("STR", v[1:-1]))
        elif loai == "thoigian":
            ra.append(("TIME", doc_thoi_gian(v)))
        elif loai == "cokieu":
            a, b = v.split("#", 1)
            if a in ("2", "8", "16"):
                ra.append(("NUM", int(b.replace("_", ""), int(a))))
            elif a.upper() == "BOOL":
                ra.append(("NUM", int(b)))
            else:
                ra.append(("NUM", float(b) if "." in b else int(b.replace("_", ""))))
        elif loai == "so":
            v = v.replace("_", "")
            ra.append(("NUM", float(v) if ("." in v or "e" in v.lower()) else int(v)))
        elif loai == "ten":
            if "#" in v:                                   # E_Kieu#GiaTri → giá trị liệt kê
                ra.append(("ID", v.split("#")[1]))
            elif v.upper() in TU_KHOA:
                ra.append(("KW", v.upper()))
            else:
                ra.append(("ID", v))
        else:
            ra.append(("OP", v))
    ra.append(("EOF", None))
    return ra


# ───────────────────────────── Phân tích ─────────────────────────────
class PhanTich:
    def __init__(self, tk):
        self.tk, self.i = tk, 0

    def xem(self, k=0):
        return self.tk[self.i + k]

    def la(self, loai, gt=None, k=0):
        t = self.xem(k)
        return t[0] == loai and (gt is None or t[1] == gt)

    def an(self, loai, gt=None):
        t = self.xem()
        if not (t[0] == loai and (gt is None or t[1] == gt)):
            raise LoiST("chờ %s %s, gặp %r (vị trí %d)" % (loai, gt or "", t, self.i))
        self.i += 1
        return t[1]

    def co(self, loai, gt=None):
        if self.la(loai, gt):
            self.i += 1
            return True
        return False

    # ── đơn vị cấp cao nhất ──
    def tat_ca(self):
        ra = {"kieu": {}, "global": [], "pou": {}, "than": []}
        while not self.la("EOF"):
            if self.la("KW", "TYPE"):
                self.an("KW", "TYPE")
                while not self.la("KW", "END_TYPE"):
                    ten = self.an("ID")
                    self.an("OP", ":")
                    ra["kieu"][ten.upper()] = self.dinh_nghia_kieu()
                    self.co("OP", ";")
                self.an("KW", "END_TYPE")
            elif self.la("KW", "VAR_GLOBAL"):
                ra["global"] += self.khoi_var()[1]
            elif self.la("KW", "FUNCTION") or self.la("KW", "FUNCTION_BLOCK") or self.la("KW", "PROGRAM"):
                p = self.pou()
                ra["pou"][p["ten"].upper()] = p
            elif self.xem()[0] == "KW" and self.xem()[1].startswith("VAR"):
                ra["than"].append(("VAR", self.khoi_var()))
            else:
                ra["than"].append(("LENH", self.cau_lenh()))
        return ra

    def dinh_nghia_kieu(self):
        if self.co("KW", "STRUCT"):
            truong = []
            while not self.la("KW", "END_STRUCT"):
                truong += self.khai_bao()
            self.an("KW", "END_STRUCT")
            return ("STRUCT", truong)
        if self.la("OP", "("):
            self.an("OP", "(")
            gt = []
            while True:
                ten = self.an("ID")
                if self.co("OP", ":="):
                    self.bieu_thuc()
                gt.append(ten.upper())
                if not self.co("OP", ","):
                    break
            self.an("OP", ")")
            if self.la("ID"):
                self.an("ID")                                      # kiểu nền của liệt kê
            if self.co("OP", ":="):
                self.bieu_thuc()
            return ("ENUM", gt)
        return self.kieu()

    def kieu(self):
        if self.co("KW", "ARRAY"):
            self.an("OP", "[")
            khoang = []
            while True:
                lo = self.bieu_thuc()
                self.an("OP", "..")
                hi = self.bieu_thuc()
                khoang.append((lo, hi))
                if not self.co("OP", ","):
                    break
            self.an("OP", "]")
            self.an("KW", "OF")
            return ("ARRAY", khoang, self.kieu())
        ten = self.an("ID").upper()
        if ten in ("STRING", "WSTRING") and (self.la("OP", "(") or self.la("OP", "[")):
            d = self.an("OP")
            self.bieu_thuc()
            self.an("OP", ")" if d == "(" else "]")
        return ("TEN", ten)

    def khai_bao(self):
        ten = [self.an("ID")]
        while self.co("OP", ","):
            ten.append(self.an("ID"))
        if self.co("KW", "AT"):
            while not self.la("OP", ":"):
                self.i += 1
        self.an("OP", ":")
        k = self.kieu()
        dau = None
        if self.co("OP", ":="):
            dau = self.khoi_tao()
        self.an("OP", ";")
        return [(t, k, dau) for t in ten]

    def khoi_tao(self):
        if self.la("OP", "["):
            self.an("OP", "[")
            ds = [self.bieu_thuc()]
            while self.co("OP", ","):
                ds.append(self.bieu_thuc())
            self.an("OP", "]")
            return ("MANG", ds)
        if self.la("OP", "(") and self.la("ID", k=1) and self.la("OP", ":=", k=2):
            self.an("OP", "(")
            ds = {}
            while True:
                f = self.an("ID")
                self.an("OP", ":=")
                ds[f.upper()] = self.khoi_tao()
                if not self.co("OP", ","):
                    break
            self.an("OP", ")")
            return ("CAUTRUC", ds)
        return self.bieu_thuc()

    def khoi_var(self):
        loai = self.an("KW")
        while self.la("KW", "CONSTANT") or self.la("KW", "RETAIN") or self.la("KW", "PERSISTENT"):
            self.i += 1
        ds = []
        while not self.la("KW", "END_VAR"):
            ds += self.khai_bao()
        self.an("KW", "END_VAR")
        return loai, ds

    def pou(self):
        loai = self.an("KW")
        ten = self.an("ID")
        tra = None
        if loai == "FUNCTION" and self.co("OP", ":"):
            tra = self.kieu()
        bien = []
        while self.xem()[0] == "KW" and self.xem()[1].startswith("VAR"):
            bien.append(self.khoi_var())
        het = "END_" + loai
        than, sfc = [], None
        while not self.la("KW", het):
            if self.la_sfc():
                if loai == "FUNCTION":
                    raise LoiST("%s: SFC chỉ dùng trong khối chức năng và chương trình" % ten)
                sfc = sfc or {"buoc": {}, "dau": None, "chuyen": []}
                self.phan_tu_sfc(sfc)
            else:
                than.append(self.cau_lenh())
        self.an("KW", het)
        if sfc is not None:
            if than:
                raise LoiST("%s: một phần POU là SFC thì cả POU phải là SFC — có câu lệnh ngoài sơ đồ" % ten)
            kiem_sfc(ten, sfc)
        return {"loai": loai, "ten": ten, "tra": tra, "bien": bien, "than": than, "sfc": sfc}

    # ── SFC dạng văn bản ──
    def la_sfc(self):
        t = self.xem()
        if t[0] != "ID":
            return False
        if t[1] in ("INITIAL_STEP", "STEP"):                    # chữ HOA đúng như chuẩn viết
            return self.la("ID", k=1) and self.la("OP", ":", 2)
        return t[1] == "TRANSITION" and self.la("ID", "FROM", 1)

    def ds_buoc(self):
        if self.co("OP", "("):
            ds = [self.an("ID").upper()]
            while self.co("OP", ","):
                ds.append(self.an("ID").upper())
            self.an("OP", ")")
            return ds
        return [self.an("ID").upper()]

    def phan_tu_sfc(self, sfc):
        loai = self.an("ID")
        if loai in ("INITIAL_STEP", "STEP"):
            ten = self.an("ID").upper()
            self.an("OP", ":")
            hd = []
            while not self.la("ID", "END_STEP"):
                ten_hd = self.an("ID").upper()
                self.an("OP", "(")
                bo_ngu = self.an("ID").upper()
                tg = self.bieu_thuc() if self.co("OP", ",") else None
                self.an("OP", ")")
                self.an("OP", ";")
                hd.append((ten_hd, bo_ngu, tg))
            self.an("ID", "END_STEP")
            if ten in sfc["buoc"]:
                raise LoiST("bước %s khai hai lần" % ten)
            sfc["buoc"][ten] = hd
            if loai == "INITIAL_STEP":
                if sfc["dau"]:
                    raise LoiST("sơ đồ có hai bước đầu: %s và %s" % (sfc["dau"], ten))
                sfc["dau"] = ten
            return
        self.an("ID", "FROM")
        tu = self.ds_buoc()
        self.an("KW", "TO")
        den = self.ds_buoc()
        self.an("OP", ":=")
        dk = self.bieu_thuc()
        self.an("OP", ";")
        self.an("ID", "END_TRANSITION")
        sfc["chuyen"].append((tu, den, dk))

    # ── câu lệnh ──
    def khoi_lenh(self, *dung):
        ds = []
        while not any(self.la("KW", d) for d in dung) and not self.la("EOF"):
            if self.nhan_case():
                break
            ds.append(self.cau_lenh())
        return ds

    def nhan_case(self):
        """Đang đứng ở đầu một nhãn CASE (`10:` `10, 20:` `0..5:` `Idle:`)?"""
        if not getattr(self, "trong_case", 0):
            return False
        k = 0
        while True:
            t = self.xem(k)
            if t[0] == "OP" and t[1] == "-":
                k += 1
                t = self.xem(k)
            if t[0] not in ("NUM", "ID"):
                return False
            k += 1
            if self.la("OP", "..", k):
                k += 1
                if self.la("OP", "-", k):
                    k += 1
                if self.xem(k)[0] not in ("NUM", "ID"):
                    return False
                k += 1
            if self.la("OP", ",", k):
                k += 1
                continue
            return self.la("OP", ":", k)

    def cau_lenh(self):
        t = self.xem()
        if t == ("OP", ";"):
            self.i += 1
            return ("RONG",)
        if t[0] == "KW":
            kw = t[1]
            if kw == "IF":
                self.i += 1
                nhanh = []
                dk = self.bieu_thuc()
                self.an("KW", "THEN")
                nhanh.append((dk, self.khoi_lenh("ELSIF", "ELSE", "END_IF")))
                while self.co("KW", "ELSIF"):
                    dk = self.bieu_thuc()
                    self.an("KW", "THEN")
                    nhanh.append((dk, self.khoi_lenh("ELSIF", "ELSE", "END_IF")))
                khac = self.khoi_lenh("END_IF") if self.co("KW", "ELSE") else []
                self.an("KW", "END_IF")
                self.co("OP", ";")
                return ("IF", nhanh, khac)
            if kw == "CASE":
                self.i += 1
                chon = self.bieu_thuc()
                self.an("KW", "OF")
                self.trong_case = getattr(self, "trong_case", 0) + 1
                nhom = []
                while not self.la("KW", "ELSE") and not self.la("KW", "END_CASE"):
                    nhan = []
                    while True:
                        am = self.co("OP", "-")
                        a = self.gia_tri_nhan(am)
                        if self.co("OP", ".."):
                            am2 = self.co("OP", "-")
                            nhan.append(("KHOANG", a, self.gia_tri_nhan(am2)))
                        else:
                            nhan.append(("MOT", a))
                        if not self.co("OP", ","):
                            break
                    self.an("OP", ":")
                    nhom.append((nhan, self.khoi_lenh("ELSE", "END_CASE")))
                self.trong_case -= 1
                khac = self.khoi_lenh("END_CASE") if self.co("KW", "ELSE") else []
                self.an("KW", "END_CASE")
                self.co("OP", ";")
                return ("CASE", chon, nhom, khac)
            if kw == "FOR":
                self.i += 1
                bien = self.an("ID")
                self.an("OP", ":=")
                a = self.bieu_thuc()
                self.an("KW", "TO")
                b = self.bieu_thuc()
                buoc = self.bieu_thuc() if self.co("KW", "BY") else ("SO", 1)
                self.an("KW", "DO")
                than = self.khoi_lenh("END_FOR")
                self.an("KW", "END_FOR")
                self.co("OP", ";")
                return ("FOR", bien, a, b, buoc, than)
            if kw == "WHILE":
                self.i += 1
                dk = self.bieu_thuc()
                self.an("KW", "DO")
                than = self.khoi_lenh("END_WHILE")
                self.an("KW", "END_WHILE")
                self.co("OP", ";")
                return ("WHILE", dk, than)
            if kw == "REPEAT":
                self.i += 1
                than = self.khoi_lenh("UNTIL")
                self.an("KW", "UNTIL")
                dk = self.bieu_thuc()
                self.an("KW", "END_REPEAT")
                self.co("OP", ";")
                return ("REPEAT", than, dk)
            if kw in ("EXIT", "RETURN", "CONTINUE"):
                self.i += 1
                self.co("OP", ";")
                return (kw,)
            raise LoiST("từ khoá không mong đợi %s" % kw)
        # gán hoặc gọi
        dich = self.truy_cap()
        if self.co("OP", ":="):
            gt = self.bieu_thuc()
            self.an("OP", ";")
            return ("GAN", dich, gt)
        if dich[0] == "GOI":
            self.an("OP", ";")
            return ("GOITHU", dich)
        raise LoiST("câu lệnh không hiểu được: %r" % (self.xem(),))

    def gia_tri_nhan(self, am):
        t = self.xem()
        self.i += 1
        if t[0] == "NUM":
            return -t[1] if am else t[1]
        return t[1].upper()                                       # giá trị liệt kê

    # ── biểu thức ──
    def bieu_thuc(self):
        return self.hoac()

    def hoac(self):
        a = self.xor()
        while self.co("KW", "OR"):
            a = ("OR", a, self.xor())
        return a

    def xor(self):
        a = self.va()
        while self.co("KW", "XOR"):
            a = ("XOR", a, self.va())
        return a

    def va(self):
        a = self.bang()
        while self.la("KW", "AND") or self.la("OP", "&"):
            self.i += 1
            a = ("AND", a, self.bang())
        return a

    def bang(self):
        a = self.so_sanh()
        while self.la("OP", "=") or self.la("OP", "<>"):
            op = self.an("OP")
            a = (op, a, self.so_sanh())
        return a

    def so_sanh(self):
        a = self.cong()
        while any(self.la("OP", o) for o in ("<", ">", "<=", ">=")):
            op = self.an("OP")
            a = (op, a, self.cong())
        return a

    def cong(self):
        a = self.nhan()
        while self.la("OP", "+") or self.la("OP", "-"):
            op = self.an("OP")
            a = (op, a, self.nhan())
        return a

    def nhan(self):
        a = self.mu()
        while self.la("OP", "*") or self.la("OP", "/") or self.la("KW", "MOD"):
            op = self.xem()[1]
            self.i += 1
            a = (op, a, self.mu())
        return a

    def mu(self):
        a = self.mot_ngoi()
        while self.co("OP", "**"):
            a = ("**", a, self.mot_ngoi())
        return a

    def mot_ngoi(self):
        if self.co("OP", "-"):
            return ("NEG", self.mot_ngoi())
        if self.co("KW", "NOT"):
            return ("NOT", self.mot_ngoi())
        if self.co("OP", "+"):
            return self.mot_ngoi()
        return self.nguyen_to()

    def nguyen_to(self):
        t = self.xem()
        if t[0] == "NUM":
            self.i += 1
            return ("SO", t[1])
        if t[0] == "TIME":
            self.i += 1
            return ("SO", t[1])
        if t[0] == "STR":
            self.i += 1
            return ("SO", t[1])
        if t == ("KW", "TRUE"):
            self.i += 1
            return ("SO", True)
        if t == ("KW", "FALSE"):
            self.i += 1
            return ("SO", False)
        if self.co("OP", "("):
            a = self.bieu_thuc()
            self.an("OP", ")")
            return a
        return self.truy_cap()

    def truy_cap(self):
        ten = self.an("ID")
        nut = ("TEN", ten.upper())
        while True:
            if self.co("OP", "."):
                nut = ("CHAM", nut, self.an("ID").upper())
            elif self.co("OP", "["):
                cs = [self.bieu_thuc()]
                while self.co("OP", ","):
                    cs.append(self.bieu_thuc())
                self.an("OP", "]")
                nut = ("CHISO", nut, cs)
            elif self.la("OP", "("):
                self.an("OP", "(")
                vao, ra, vitri = {}, {}, []
                while not self.la("OP", ")"):
                    if self.la("ID") and self.la("OP", ":=", 1):
                        c = self.an("ID").upper()
                        self.an("OP", ":=")
                        vao[c] = self.bieu_thuc()
                    elif self.la("ID") and self.la("OP", "=>", 1):
                        c = self.an("ID").upper()
                        self.an("OP", "=>")
                        ra[c] = self.truy_cap()
                    else:
                        vitri.append(self.bieu_thuc())
                    if not self.co("OP", ","):
                        break
                self.an("OP", ")")
                nut = ("GOI", nut, vao, ra, vitri)
            else:
                return nut


def kiem_sfc(ten, sfc):
    """Luật cấu trúc kiểm được ngay khi nạp: một bước đầu, tên bước có thật, bổ ngữ hỗ trợ, tới được."""
    if not sfc["dau"]:
        raise LoiST("%s: sơ đồ không có INITIAL_STEP" % ten)
    for tu, den, _ in sfc["chuyen"]:
        for b in tu + den:
            if b not in sfc["buoc"]:
                raise LoiST("%s: chuyển tiếp nhắc bước không có: %s" % (ten, b))
    for b, ds in sfc["buoc"].items():
        for ten_hd, bo_ngu, _ in ds:
            if bo_ngu != "N":
                raise LoiST("%s: bước %s — bổ ngữ %s chưa hỗ trợ trong bộ chạy thử" % (ten, b, bo_ngu))
    toi = {sfc["dau"]}
    doi = True
    while doi:
        doi = False
        for tu, den, _ in sfc["chuyen"]:
            if set(tu) <= toi and not set(den) <= toi:
                toi |= set(den)
                doi = True
    thieu = sorted(set(sfc["buoc"]) - toi)
    if thieu:
        raise LoiST("%s: bước không bao giờ tới được: %s" % (ten, ", ".join(thieu)))


# ───────────────────────────── Thực thi ─────────────────────────────
class ThoatVong(Exception):
    pass


class TraVe(Exception):
    pass


class The:
    """Một thể hiện khối (chuẩn hoặc tự viết) hoặc một chương trình — kho biến của riêng nó."""

    def __init__(self, kieu):
        self.kieu = kieu
        self.bien = {}

    def __repr__(self):
        return "<%s %s>" % (self.kieu, self.bien)


class May:
    def __init__(self, ma):
        pt = PhanTich(tach(ma))
        cay = pt.tat_ca()
        self.kieu = cay["kieu"]
        self.pou = cay["pou"]
        self.enum = {}
        for k, v in self.kieu.items():
            if v[0] == "ENUM":
                for g in v[1]:
                    self.enum[g] = g
        self.gio = 0                                             # đồng hồ nền, mili-giây
        self.t_khi_roi = "giu"                                   # SFC: .T khi rời bước — "giu" | "ve0"
        self.toan_cuc = {}
        for ten, k, dau in cay["global"]:
            self.toan_cuc[ten.upper()] = self.tao(k, dau, {})
        self.chuong_trinh = {}
        for ten, p in self.pou.items():
            if p["loai"] == "PROGRAM":
                self.chuong_trinh[ten] = self.tao_the(p)
        if cay["than"]:                                          # khối không bọc POU → chương trình ẩn
            p = {"loai": "PROGRAM", "ten": "MAIN", "tra": None,
                 "bien": [x[1] for x in cay["than"] if x[0] == "VAR"],
                 "than": [x[1] for x in cay["than"] if x[0] == "LENH"]}
            self.pou["MAIN"] = p
            self.chuong_trinh["MAIN"] = self.tao_the(p)

    # ── tạo giá trị ──
    def tao(self, k, dau, pham_vi):
        if k[0] == "ARRAY":
            (lo, hi) = k[1][0]
            lo, hi = self.tinh(lo, pham_vi), self.tinh(hi, pham_vi)
            mang = {i: self.tao(k[2], None, pham_vi) for i in range(lo, hi + 1)}
            if dau and dau[0] == "MANG":
                for j, e in enumerate(dau[1]):
                    mang[lo + j] = self.tinh(e, pham_vi)
            return mang
        ten = k[1] if k[0] == "TEN" else None
        if ten in ("BOOL",):
            v = False
        elif ten in ("SINT", "INT", "DINT", "LINT", "USINT", "UINT", "UDINT", "ULINT", "BYTE",
                     "WORD", "DWORD", "LWORD", "TIME", "LTIME"):
            v = 0
        elif ten in ("REAL", "LREAL"):
            v = 0.0
        elif ten in ("STRING", "WSTRING"):
            v = ""
        elif ten in self.kieu:
            dn = self.kieu[ten]
            if dn[0] == "STRUCT":
                v = {f.upper(): self.tao(fk, fd, pham_vi) for f, fk, fd in dn[1]}
                if dau and dau[0] == "CAUTRUC":
                    for f, e in dau[1].items():
                        v[f] = self.tinh(e, pham_vi)
                return v
            if dn[0] == "ENUM":
                v = dn[1][0]
            else:
                return self.tao(dn, dau, pham_vi)
        elif ten in CHUAN or ten in self.pou:
            return self.tao_the(self.pou.get(ten) or ten)
        else:
            raise LoiST("kiểu không biết: %s" % ten)
        if dau is not None:
            v = self.tinh(dau, pham_vi)
        return v

    def tao_the(self, p):
        if isinstance(p, str):                                   # khối chuẩn
            the = The(p)
            the.bien.update(CHUAN[p]())
            return the
        the = The(p["ten"].upper())
        the.tam = []
        for loai, ds in p["bien"]:
            for ten, k, dau in ds:
                if loai == "VAR_TEMP":
                    the.tam.append((ten.upper(), k, dau))
                if loai == "VAR_EXTERNAL":
                    the.bien[ten.upper()] = ("NGOAI", ten.upper())
                else:
                    the.bien[ten.upper()] = self.tao(k, dau, the.bien)
        if p.get("sfc"):
            for b in p["sfc"]["buoc"]:
                if b in the.bien:
                    raise LoiST("%s: tên bước %s trùng tên biến" % (p["ten"], b))
                the.bien[b] = {"X": False, "T": 0}              # biến ngầm của bước: .X, .T
            the.sfc_moc, the.nhap_nhang, the.sfc_khoi = {}, [], False
        return the

    # ── đọc/ghi theo tên ──
    def _o(self, pv, ten):
        """Trả (kho, khoá) chứa biến `ten` trong phạm vi pv."""
        if pv is not None and ten in pv:
            if isinstance(pv[ten], tuple) and pv[ten][:1] == ("NGOAI",):
                return self.toan_cuc, pv[ten][1]
            return pv, ten
        if ten in self.toan_cuc:
            return self.toan_cuc, ten
        return None, ten

    def gia_tri_ten(self, pv, ten):
        kho, k = self._o(pv, ten)
        if kho is not None:
            return kho[k]
        if ten in self.enum:
            return ten
        if ten in self.chuong_trinh:
            return self.chuong_trinh[ten]
        raise LoiST("biến chưa khai báo: %s" % ten)

    def lay_o(self, pv, nut):
        """(kho, khoá) để GHI vào một đích."""
        if nut[0] == "TEN":
            kho, k = self._o(pv, nut[1])
            if kho is None:
                raise LoiST("ghi vào biến chưa khai báo: %s" % nut[1])
            return kho, k
        if nut[0] == "CHAM":
            cha = self.tinh(nut[1], pv)
            if isinstance(cha, The):
                return cha.bien, nut[2]
            return cha, nut[2]
        if nut[0] == "CHISO":
            cha = self.tinh(nut[1], pv)
            return cha, self.tinh(nut[2][0], pv)
        raise LoiST("không ghi được vào %r" % (nut,))

    # ── biểu thức ──
    def tinh(self, e, pv):
        loai = e[0]
        if loai == "SO":
            return e[1]
        if loai == "TEN":
            return self.gia_tri_ten(pv, e[1])
        if loai == "CHAM":
            cha = self.tinh(e[1], pv)
            if isinstance(cha, The):
                if e[2] not in cha.bien:
                    raise LoiST("%s không có chân/biến %s" % (cha.kieu, e[2]))
                v = cha.bien[e[2]]
                if isinstance(v, tuple) and v[:1] == ("NGOAI",):
                    return self.toan_cuc[v[1]]
                return v
            if isinstance(cha, dict):
                if e[2] not in cha:
                    raise LoiST("cấu trúc không có trường %s" % e[2])
                return cha[e[2]]
            raise LoiST("dấu chấm trên giá trị không phải cấu trúc: %r" % (e,))
        if loai == "CHISO":
            cha = self.tinh(e[1], pv)
            i = self.tinh(e[2][0], pv)
            if i not in cha:
                raise LoiST("chỉ số %s ngoài dải" % i)
            return cha[i]
        if loai == "GOI":
            return self.goi(e, pv)
        if loai == "NEG":
            return -self.tinh(e[1], pv)
        if loai == "NOT":
            v = self.tinh(e[1], pv)
            return (not v) if isinstance(v, bool) else ~v
        a = self.tinh(e[1], pv)
        b = self.tinh(e[2], pv)
        if loai == "AND":
            return (a and b) if isinstance(a, bool) else a & b
        if loai == "OR":
            return (a or b) if isinstance(a, bool) else a | b
        if loai == "XOR":
            return (a != b) if isinstance(a, bool) else a ^ b
        if loai == "=":
            return a == b
        if loai == "<>":
            return a != b
        if loai == "<":
            return a < b
        if loai == ">":
            return a > b
        if loai == "<=":
            return a <= b
        if loai == ">=":
            return a >= b
        if loai == "+":
            return a + b
        if loai == "-":
            return a - b
        if loai == "*":
            return a * b
        if loai == "/":
            if isinstance(a, int) and isinstance(b, int) and not isinstance(a, bool):
                if b == 0:
                    raise LoiST("chia cho 0")
                q = abs(a) // abs(b)
                return q if (a >= 0) == (b >= 0) else -q
            return a / b
        if loai == "MOD":
            return a - b * int(a / b)
        if loai == "**":
            return a ** b
        raise LoiST("toán tử không biết %s" % loai)

    # ── gọi hàm / khối ──
    def goi(self, e, pv):
        _, dich, vao, ra, vitri = e
        ten = dich[1] if dich[0] == "TEN" else None
        if ten and ten in HAM:
            return HAM[ten](*[self.tinh(x, pv) for x in vitri + list(vao.values())])
        if ten and "_TO_" in ten:
            return doi_kieu(ten, self.tinh((vitri or list(vao.values()))[0], pv))
        if ten and ten in self.pou and self.pou[ten]["loai"] == "FUNCTION":
            return self.goi_ham(self.pou[ten], vao, vitri, pv, ra)
        the = self.tinh(dich, pv)
        if not isinstance(the, The):
            raise LoiST("gọi thứ không phải khối: %r" % (dich,))
        for c, bt in vao.items():
            if c not in the.bien:
                raise LoiST("khối %s không có chân vào %s" % (the.kieu, c))
            the.bien[c] = self.tinh(bt, pv)
        if the.kieu in CHUAN:
            CHAY[the.kieu](the.bien, self.gio)
        else:
            for t, k, dau in getattr(the, "tam", []):       # VAR_TEMP: khởi tạo lại mỗi lần gọi
                the.bien[t] = self.tao(k, dau, the.bien)
            self.chay_than(self.pou[the.kieu]["than"], the.bien)
            if self.pou[the.kieu].get("sfc"):
                self.chay_sfc(self.pou[the.kieu]["sfc"], the)
        for c, dich_ra in ra.items():
            kho, k = self.lay_o(pv, dich_ra)
            kho[k] = the.bien[c]
        return None

    def goi_ham(self, p, vao, vitri, pv, ra=None):
        cuc = {}
        ten_vao = []
        for loai, ds in p["bien"]:
            for ten, k, dau in ds:
                cuc[ten.upper()] = self.tao(k, dau, cuc)
                if loai == "VAR_INPUT":
                    ten_vao.append(ten.upper())
        for j, bt in enumerate(vitri):
            cuc[ten_vao[j]] = self.tinh(bt, pv)
        for c, bt in vao.items():
            cuc[c] = self.tinh(bt, pv)
        cuc[p["ten"].upper()] = self.tao(p["tra"], None, cuc)
        try:
            self.chay_than(p["than"], cuc)
        except TraVe:
            pass
        for c, dich_ra in (ra or {}).items():             # ngõ ra => của hàm (VAR_OUTPUT)
            kho, k = self.lay_o(pv, dich_ra)
            kho[k] = cuc[c]
        return cuc[p["ten"].upper()]

    # ── câu lệnh ──
    def chay_than(self, ds, pv):
        for c in ds:
            self.chay(c, pv)

    def chay(self, c, pv):
        loai = c[0]
        if loai == "RONG":
            return
        if loai == "GAN":
            kho, k = self.lay_o(pv, c[1])
            kho[k] = self.tinh(c[2], pv)
        elif loai == "GOITHU":
            self.goi(c[1], pv)
        elif loai == "IF":
            for dk, than in c[1]:
                if self.tinh(dk, pv):
                    self.chay_than(than, pv)
                    return
            self.chay_than(c[2], pv)
        elif loai == "CASE":
            v = self.tinh(c[1], pv)
            for nhan, than in c[2]:
                for n in nhan:
                    if (n[0] == "MOT" and n[1] == v) or (n[0] == "KHOANG" and n[1] <= v <= n[2]):
                        self.chay_than(than, pv)
                        return
            self.chay_than(c[3], pv)
        elif loai == "FOR":
            _, bien, a, b, buoc, than = c
            kho, k = self.lay_o(pv, ("TEN", bien.upper()))
            kho[k] = self.tinh(a, pv)
            den, b_ = self.tinh(b, pv), self.tinh(buoc, pv)
            try:
                while (kho[k] <= den) if b_ > 0 else (kho[k] >= den):
                    self.chay_than(than, pv)
                    kho[k] += b_
            except ThoatVong:
                pass
        elif loai == "WHILE":
            n = 0
            try:
                while self.tinh(c[1], pv):
                    self.chay_than(c[2], pv)
                    n += 1
                    if n > 100000:
                        raise LoiST("WHILE không dừng")
            except ThoatVong:
                pass
        elif loai == "REPEAT":
            try:
                while True:
                    self.chay_than(c[1], pv)
                    if self.tinh(c[2], pv):
                        break
            except ThoatVong:
                pass
        elif loai == "EXIT":
            raise ThoatVong()
        elif loai == "RETURN":
            raise TraVe()
        else:
            raise LoiST("câu lệnh không hỗ trợ %s" % loai)

    # ── giao diện cho kịch bản thử ──
    def quet(self, ten="MAIN", ms=10):
        self.gio += ms
        the = self.chuong_trinh[ten.upper()]
        for t, k, dau in getattr(the, "tam", []):
            the.bien[t] = self.tao(k, dau, the.bien)
        try:
            self.chay_than(self.pou[the.kieu]["than"], the.bien)
        except TraVe:
            pass
        if self.pou[the.kieu].get("sfc"):
            self.chay_sfc(self.pou[the.kieu]["sfc"], the)

    def chay_sfc(self, sfc, the):
        """Một vòng quét của sơ đồ — thứ tự theo PLCopen, Structuring with SFC, mục 3.6.1."""
        b = the.bien
        if not the.sfc_khoi:                                    # khởi động: chỉ bước đầu hoạt động
            the.sfc_khoi = True
            b[sfc["dau"]]["X"] = True
            the.sfc_moc[sfc["dau"]] = self.gio
        for ten in sfc["buoc"]:                                 # .T của bước đang hoạt động
            if b[ten]["X"]:
                b[ten]["T"] = self.gio - the.sfc_moc[ten]
        dang = {t for t in sfc["buoc"] if b[t]["X"]}
        da_dung, xoa = set(), []
        for tu, den, dk in sfc["chuyen"]:                       # 1 · xét theo trạng thái ĐẦU vòng
            if all(t in dang for t in tu) and self.tinh(dk, b):
                if any(t in da_dung for t in tu):
                    the.nhap_nhang.append((self.gio, tuple(tu), tuple(den)))
                    continue                                    # đi nhánh viết trước — như "trái nhất"
                da_dung.update(tu)
                xoa.append((tu, den))
        for tu, den in xoa:                                     # 2 · đổi bước
            for t in tu:
                b[t]["X"] = False
                if self.t_khi_roi == "ve0":
                    b[t]["T"] = 0
            for t in den:
                b[t]["X"], b[t]["T"] = True, 0
                the.sfc_moc[t] = self.gio
        hd = {}                                                 # 3 · hành động BOOL theo trạng thái MỚI
        for ten, ds in sfc["buoc"].items():
            for ten_hd, _, _ in ds:
                hd[ten_hd] = hd.get(ten_hd, False) or b[ten]["X"]
        for ten_hd, v in hd.items():
            kho, k = self._o(b, ten_hd)
            if kho is None:
                raise LoiST("hành động %s: biến chưa khai báo" % ten_hd)
            kho[k] = v

    def _duong(self, duong):
        phan = duong.upper().split(".")
        if phan[0] in self.chuong_trinh:
            o, phan = self.chuong_trinh[phan[0]].bien, phan[1:]
        else:
            o = self.toan_cuc
        for p in phan[:-1]:
            o = o[p].bien if isinstance(o[p], The) else o[p]
        if isinstance(o.get(phan[-1]), tuple) and o[phan[-1]][:1] == ("NGOAI",):
            return self.toan_cuc, o[phan[-1]][1]
        return o, phan[-1]

    def dat(self, duong, gt):
        o, k = self._duong(duong)
        if k not in o:
            raise LoiST("không có %s" % duong)
        o[k] = gt

    def doc(self, duong):
        o, k = self._duong(duong)
        return o[k]


# ───────────────────────────── Khối và hàm chuẩn ─────────────────────────────
def _ton(b, gio):
    if b["IN"]:
        if not b["_M"]:
            b["_BD"] = gio
        b["ET"] = min(gio - b["_BD"], b["PT"])
        b["Q"] = b["ET"] >= b["PT"]
    else:
        b["Q"], b["ET"] = False, 0
    b["_M"] = b["IN"]


def _tof(b, gio):
    if b["IN"]:
        b["Q"], b["ET"], b["_CHAY"] = True, 0, False
    else:
        if b["_M"]:
            b["_BD"], b["_CHAY"] = gio, True
        if b["_CHAY"]:
            b["ET"] = min(gio - b["_BD"], b["PT"])
            if b["ET"] >= b["PT"]:
                b["Q"], b["_CHAY"] = False, False
    b["_M"] = b["IN"]


def _tp(b, gio):
    if not b["_CHAY"] and b["IN"] and not b["_M"]:
        b["_BD"], b["_CHAY"] = gio, True
    if b["_CHAY"]:
        b["ET"] = min(gio - b["_BD"], b["PT"])
        b["Q"] = b["ET"] < b["PT"]
        if not b["Q"]:
            b["_CHAY"] = False
    if not b["_CHAY"] and not b["IN"]:
        b["ET"] = 0
    b["_M"] = b["IN"]


def _rtrig(b, gio):
    b["Q"] = b["CLK"] and not b["_M"]
    b["_M"] = b["CLK"]


def _ftrig(b, gio):
    b["Q"] = (not b["CLK"]) and not b["_M"]
    b["_M"] = not b["CLK"]


def _ctu(b, gio):
    canh = b["CU"] and not b["_M"]
    b["_M"] = b["CU"]
    if b["R"]:
        b["CV"] = 0
    elif canh:
        b["CV"] += 1
    b["Q"] = b["CV"] >= b["PV"]


def _ctd(b, gio):
    canh = b["CD"] and not b["_M"]
    b["_M"] = b["CD"]
    if b["LD"]:
        b["CV"] = b["PV"]
    elif canh:
        b["CV"] -= 1
    b["Q"] = b["CV"] <= 0


def _ctud(b, gio):
    cu = b["CU"] and not b["_MU"]
    cd = b["CD"] and not b["_MD"]
    b["_MU"], b["_MD"] = b["CU"], b["CD"]
    if b["R"]:
        b["CV"] = 0
    elif b["LD"]:
        b["CV"] = b["PV"]
    else:
        if cu:
            b["CV"] += 1
        if cd:
            b["CV"] -= 1
    b["QU"] = b["CV"] >= b["PV"]
    b["QD"] = b["CV"] <= 0


def _sr(b, gio):
    b["Q1"] = b["S1"] or (not b["R"] and b["Q1"])


def _rs(b, gio):
    b["Q1"] = (not b["R1"]) and (b["S"] or b["Q1"])


CHUAN = {
    "TON": lambda: {"IN": False, "PT": 0, "Q": False, "ET": 0, "_M": False, "_BD": 0},
    "TOF": lambda: {"IN": False, "PT": 0, "Q": False, "ET": 0, "_M": False, "_BD": 0, "_CHAY": False},
    "TP": lambda: {"IN": False, "PT": 0, "Q": False, "ET": 0, "_M": False, "_BD": 0, "_CHAY": False},
    "R_TRIG": lambda: {"CLK": False, "Q": False, "_M": False},
    "F_TRIG": lambda: {"CLK": False, "Q": False, "_M": True},
    "CTU": lambda: {"CU": False, "R": False, "PV": 0, "Q": False, "CV": 0, "_M": False},
    "CTD": lambda: {"CD": False, "LD": False, "PV": 0, "Q": False, "CV": 0, "_M": False},
    "CTUD": lambda: {"CU": False, "CD": False, "R": False, "LD": False, "PV": 0, "QU": False,
                     "QD": False, "CV": 0, "_MU": False, "_MD": False},
    "SR": lambda: {"S1": False, "R": False, "Q1": False},
    "RS": lambda: {"S": False, "R1": False, "Q1": False},
}
CHAY = {"TON": _ton, "TOF": _tof, "TP": _tp, "R_TRIG": _rtrig, "F_TRIG": _ftrig, "CTU": _ctu,
        "CTD": _ctd, "CTUD": _ctud, "SR": _sr, "RS": _rs}


def _mid(s, l, p):
    return s[p - 1:p - 1 + l]


def _find(s1, s2):
    i = s1.find(s2)
    return i + 1 if i >= 0 else 0


HAM = {
    "ABS": abs, "MIN": min, "MAX": max, "SQRT": lambda x: x ** 0.5,
    "LIMIT": lambda mn, x, mx: max(mn, min(x, mx)),
    "SEL": lambda g, a, b: b if g else a,
    "MUX": lambda k, *xs: xs[k],
    "LEN": len, "LEFT": lambda s, l: s[:l], "RIGHT": lambda s, l: s[-l:] if l else "",
    "MID": _mid, "CONCAT": lambda *xs: "".join(xs), "FIND": _find,
    "TRUNC": lambda x: int(x),
}


def doi_kieu(ten, v):
    dich = ten.split("_TO_")[1]
    if dich in ("REAL", "LREAL"):
        return float(v)
    if dich == "BOOL":
        return bool(v)
    if dich in ("STRING", "WSTRING"):
        return str(v)
    if isinstance(v, float):
        return int(round(v))                   # làm tròn, không cắt (xem Chương 19)
    return int(v)
