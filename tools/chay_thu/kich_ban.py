# -*- coding: utf-8 -*-
"""Chạy thử HÀNH VI các ví dụ hoàn chỉnh của sách — đọc thẳng khối mã in trong docs/.

Bộ kiểm cú pháp (tools/kiem_cu_phap_st.py) chỉ đọc mã. Tệp này CHẠY mã: mỗi ví dụ hoàn chỉnh về
logic được nạp vào bộ chạy thử st_mini.py, cho chạy qua các kịch bản — ⭐ đặc biệt là những kịch bản
mà lỗi của mã trình tự hay trốn: chu trình THỨ HAI, giữ máy lâu rồi chạy tiếp, cơ cấu kẹt, Reset khi
nguyên nhân còn, huỷ chu trình giữa chừng.

Đợt 62 dùng nó tìm ra lỗi "Done của lệnh cũ" ở Chương 26 (Bẫy 7) — lỗi mà sáu bộ kiểm tĩnh không thấy.

⚠ Đây là MÔ HÌNH, không phải PLC: hành vi khối chuẩn lấy theo tài liệu đã đối chiếu (Phụ lục B mục
B.9b); mô hình vật lý (xy-lanh, board) là đơn giản hoá. Đạt ở đây KHÔNG thay việc chạy trên hệ thật.

Chạy:  python tools/chay_thu/kich_ban.py      (mã thoát 1 nếu có kịch bản hỏng)
"""
import glob
import io
import os
import re
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
DAY = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DAY)
from st_mini import May  # noqa: E402

DOCS = (sys.argv[1] if len(sys.argv) > 1          # tham số tuỳ chọn: thư mục khác, để thử lỗi cài sẵn
        else os.path.join(DAY, "..", "..", "docs"))
SO_DAT, SO_HONG = [0], []


def khoi(mau_tep, chua):
    """Khối iecst đầu tiên trong tệp khớp mẫu có chứa chuỗi `chua`."""
    p = glob.glob(os.path.join(DOCS, mau_tep))[0]
    s = io.open(p, encoding="utf-8").read()
    for m in re.finditer(r"^```iecst\n(.*?)^```", s, flags=re.S | re.M):
        if chua in m.group(1):
            return m.group(1)
    raise KeyError("%s: không thấy khối chứa %r" % (mau_tep, chua))


def cat(ma, dau, cuoi):
    """Cắt từ `dau` tới hết `cuoi` — lấy riêng một kiểu hay một khối trong khối lớn."""
    a = ma.index(dau)
    return ma[a:ma.index(cuoi, a) + len(cuoi)]


def kiem(dk, mo_ta):
    if dk:
        SO_DAT[0] += 1
        print("  ✔ " + mo_ta)
    else:
        SO_HONG.append(mo_ta)
        print("  ✘ " + mo_ta)


def quet(m, prg, n=1, ms=10):
    for _ in range(n):
        m.quet(prg, ms)


ST_STATION = cat(khoi("ch11_*.md", "TYPE ST_Station"), "TYPE ST_Station", "END_TYPE")
ST_RECIPE = khoi("pl_j_*.md", "TYPE ST_Recipe")
FB_CYL = khoi("ch27_*.md", "FUNCTION_BLOCK FB_Cylinder2Pos")
FB_DEB = cat(khoi("ch17_*.md", "FUNCTION_BLOCK FB_Debounce"), "FUNCTION_BLOCK", "END_FUNCTION_BLOCK")


def ch27_xylanh():
    print("Ch.27 — FB_Cylinder2Pos")
    m = May(FB_CYL + """
VAR_GLOBAL
    Req, Permit, Rst, SW, SH : BOOL;
END_VAR
PROGRAM T
VAR
    C : FB_Cylinder2Pos;
END_VAR
C(Req := Req, Permit := Permit, Reset := Rst, SensWork := SW, SensHome := SH, Limit := T#3S);
END_PROGRAM
""")
    m.dat("Permit", True)
    m.dat("SH", True)
    quet(m, "T")
    kiem(m.doc("T.C.Done") and not m.doc("T.C.Valve"), "ở gốc, Req FALSE → Done, van tắt")
    m.dat("Req", True)
    quet(m, "T")
    kiem(m.doc("T.C.Valve") and not m.doc("T.C.Done"), "Req TRUE → van bật, chưa Done")
    m.dat("SH", False)
    quet(m, "T", 30)
    m.dat("SW", True)
    quet(m, "T")
    kiem(m.doc("T.C.Done") and not m.doc("T.C.Fault"), "tới đích → Done, không lỗi")
    m.dat("Req", False)
    m.dat("SW", False)
    quet(m, "T", 310)
    kiem(m.doc("T.C.Fault") and m.doc("T.C.FaultCode") == 1, "kẹt 3,1 s → Fault, mã 1")
    m.dat("SH", True)
    m.dat("Rst", True)
    quet(m, "T")
    m.dat("Rst", False)
    quet(m, "T")
    kiem(not m.doc("T.C.Fault") and m.doc("T.C.Done"), "Reset khi đã về gốc → hết lỗi")
    m.dat("SW", True)
    quet(m, "T")
    kiem(m.doc("T.C.Fault") and m.doc("T.C.FaultCode") == 2, "hai cảm biến cùng bật → mã 2")
    m.dat("SW", False)
    m.dat("Permit", False)
    m.dat("Req", True)
    quet(m, "T")
    kiem(not m.doc("T.C.Valve"), "mất Permit → van đứng yên, không bật theo Req")


def ch27_anh_xa():
    print("Ch.27 — tầng ánh xạ vào/ra (Prg_IoRead, Prg_OutputMap)")
    m = May(chr(10).join([FB_DEB, FB_CYL, khoi("ch27_*.md", "PROGRAM Prg_IoRead")]))
    m.dat("DI_StopPB", True)
    m.dat("DI_AirOK", True)
    quet(m, "Prg_IoRead")
    kiem(m.doc("X_StopOK") and m.doc("X_AirOK"), "Stop lành, đủ khí → X_StopOK, X_AirOK")
    m.dat("DI_BoardStn1", True)
    quet(m, "Prg_IoRead", 3)
    m.dat("DI_BoardStn1", False)
    quet(m, "Prg_IoRead")
    m.dat("DI_BoardStn1", True)
    quet(m, "Prg_IoRead", 3)
    kiem(not m.doc("X_BoardStn1"), "board nháy ngắn hơn 50 ms → CHƯA công nhận")
    quet(m, "Prg_IoRead", 3)
    kiem(m.doc("X_BoardStn1"), "board ổn định ≥ 50 ms → X_BoardStn1")
    m.dat("DI_StopPB", False)
    quet(m, "Prg_IoRead")
    kiem(not m.doc("X_StopOK"), "nhấn Stop (hoặc đứt dây NC) → X_StopOK FALSE ngay trong vòng quét đó")
    m.dat("DI_StopPB", True)
    m.dat("M_SimMode", True)
    m.dat("DI_BoardStn1", False)
    m.dat("Sim_BoardStn1", True)
    m.dat("Sim_Clamp1Up", True)
    quet(m, "Prg_IoRead", 8)
    kiem(m.doc("X_BoardStn1") and m.doc("X_Clamp1Up") and not m.doc("DI_Clamp1Up"),
         "mô phỏng → X_ theo giá trị giả, dây thật bị bỏ qua")
    m.dat("DI_StopPB", False)
    quet(m, "Prg_IoRead")
    kiem(not m.doc("X_StopOK"), "đang mô phỏng, nhấn Stop → X_StopOK vẫn FALSE ngay — Stop không qua lớp mô phỏng")
    m.dat("DI_StopPB", True)
    len_canh, truoc = 0, m.doc("X_StartPB")
    for x in (True, False, True, False, True, True, True, True, True):
        m.dat("DI_StartPB", x)
        quet(m, "Prg_IoRead")
        hien = m.doc("X_StartPB")
        len_canh += 1 if (hien and not truoc) else 0
        truoc = hien
    kiem(m.doc("X_StartPB") and len_canh == 1, "nút Start nảy rồi giữ → công nhận đúng MỘT lần")
    m.dat("M_ConvRunCmd", True)
    m.dat("Clamp1.Valve", True)
    quet(m, "Prg_OutputMap")
    kiem(m.doc("DO_ConvRun") and m.doc("DO_Clamp1Vlv") and not m.doc("DO_Stop1Vlv"),
         "tầng ghi ra chép đúng quyết định của tầng trên, mỗi ngõ ra một dòng")
    kiem(m.doc("M_SimMode") and m.doc("DO_Clamp1Vlv"),
         "đang mô phỏng → tầng ghi ra KHÔNG tắt van (tắt van một cuộn là ra lệnh chuyển động)")


def ch30_chuyen_board():
    print("Ch.30 — FB_BoardTransfer (hai lần liên tiếp)")
    m = May(khoi("ch30_*.md", "FUNCTION_BLOCK FB_BoardTransfer") + """
VAR_GLOBAL
    Ex, Arr : BOOL;
END_VAR
PROGRAM T
VAR
    X : FB_BoardTransfer;
END_VAR
X(Execute := Ex, Arrived := Arr, TimeOut := T#1S);
END_PROGRAM
""")
    for lan in (1, 2):
        m.dat("Ex", True)
        quet(m, "T")
        kiem(m.doc("T.X.Busy") and m.doc("T.X.ConvReq"), "lần %d: sườn Execute → Busy, ConvReq" % lan)
        quet(m, "T", 20)
        m.dat("Arr", True)
        quet(m, "T")
        kiem(m.doc("T.X.Done") and not m.doc("T.X.Busy"), "lần %d: tới nơi → Done" % lan)
        m.dat("Arr", False)
        m.dat("Ex", False)
        quet(m, "T")
        kiem(not m.doc("T.X.Done"), "lần %d: Execute hạ → Done xoá" % lan)
    m.dat("Ex", True)
    quet(m, "T", 110)
    kiem(m.doc("T.X.Error") and m.doc("T.X.ErrorID") == 1, "không tới trong 1 s → Error, mã 1")


def ch42_ma():
    print("Ch.42 — KiemTraMaHopLe")
    m = May(khoi("ch42_*.md", "FUNCTION KiemTraMaHopLe") + """
VAR_GLOBAL
    Ma : STRING[40];
    Kq : BOOL;
    Lo : STRING[10];
END_VAR
PROGRAM T
Kq := KiemTraMaHopLe(Ma := Ma);
Lo := MID(Ma, 6, 5);
END_PROGRAM
""")
    for ma, mong in (("DP1-L2409A-000457", True), ("DP1-L2409A-00045", False),
                     ("DP1-L2409A-00045X", False), ("XX1-L2409A-000457", False),
                     ("SHIP-2409-000123-AB", False), ("", False)):
        m.dat("Ma", ma)
        quet(m, "T")
        kiem(m.doc("Kq") == mong, "%-22r → %s" % (ma, mong))
    m.dat("Ma", "DP1-L2409A-000457")
    quet(m, "T")
    kiem(m.doc("Lo") == "L2409A", "tách mã lô → L2409A")


def ch14_pou():
    print("Ch.14 — FUNCTION / FUNCTION_BLOCK / PROGRAM")
    m = May(khoi("ch14_*.md", "FUNCTION PercentOf"))
    for ng in (False, True, False):
        m.dat("M_Board1IsNG", ng)
        m.dat("M_Board1Present", True)
        quet(m, "Prg_Stn1Count", 5)
        m.dat("M_Board1Present", False)
        quet(m, "Prg_Stn1Count", 2)
    kiem(m.doc("Stn1Total") == 3 and m.doc("Stn1NgQty") == 1, "3 board, 1 NG → Total 3, NgQty 1")
    kiem(m.doc("Stn1NgPct") == 33, "tỉ lệ NG = 33 % (nhân trước, chia sau)")
    m.dat("M_ShiftStart", True)
    quet(m, "Prg_Stn1Count")
    kiem(m.doc("Stn1Total") == 0 and m.doc("Stn1NgPct") == 0, "đầu ca → 0; mẫu số 0 không làm hỏng hàm")


def ch16_danh_dau():
    print("Ch.16 — cạnh lên / SET / cạnh xuống")
    m = May(khoi("ch16_*.md", "PROGRAM Prg_Board1Mark"))
    m.dat("M_Board1Present", True)
    quet(m, "Prg_Board1Mark", 3)
    m.dat("M_DispFault", True)
    quet(m, "Prg_Board1Mark")
    m.dat("M_DispFault", False)
    quet(m, "Prg_Board1Mark", 3)
    kiem(m.doc("M_Board1IsNG"), "lỗi thoáng qua → dấu NG DÍNH lại")
    m.dat("M_Board1Present", False)
    quet(m, "Prg_Board1Mark", 3)
    m.dat("M_Board1Present", True)
    quet(m, "Prg_Board1Mark", 3)
    kiem(not m.doc("M_Board1IsNG"), "board mới vào → dấu của board trước bị xoá")
    m.dat("M_Board1Present", False)
    quet(m, "Prg_Board1Mark", 3)
    kiem(m.doc("Stn1NgCount") == 1 and m.doc("Stn1OkCount") == 1, "hai board → 1 NG, 1 OK, mỗi board đếm MỘT lần")


def ch17_loc():
    print("Ch.17 — FB_Debounce")
    m = May(khoi("ch17_*.md", "FUNCTION_BLOCK FB_Debounce"))
    m.dat("DI_BoardStn1", True)
    quet(m, "Prg_Inputs", 3)
    m.dat("DI_BoardStn1", False)
    quet(m, "Prg_Inputs")
    m.dat("DI_BoardStn1", True)
    quet(m, "Prg_Inputs", 3)
    kiem(not m.doc("M_Board1Present"), "nháy trong thời gian lọc → CHƯA công nhận")
    quet(m, "Prg_Inputs", 3)
    kiem(m.doc("M_Board1Present"), "ổn định ≥ 50 ms → công nhận có board")
    m.dat("DI_BoardStn1", False)
    quet(m, "Prg_Inputs", 2)
    m.dat("DI_BoardStn1", True)
    quet(m, "Prg_Inputs", 10)
    kiem(m.doc("M_Board1Present"), "mất tín hiệu 20 ms giữa chừng → KHÔNG thành hai board")
    m.dat("DI_BoardStn1", False)
    quet(m, "Prg_Inputs", 6)
    kiem(not m.doc("M_Board1Present"), "hết board ≥ 50 ms → công nhận hết")
    for x in (True, False, True, False, True):
        m.dat("DI_StartPB", x)
        quet(m, "Prg_Inputs")
    quet(m, "Prg_Inputs", 3)
    kiem(m.doc("M_StartPB"), "nút nảy rồi giữ → một lần công nhận")


def ch18_dem():
    print("Ch.18 — CTUD trong máy + sản lượng ở lối ra")
    m = May(FB_DEB + "\n" + khoi("ch18_*.md", "PROGRAM Prg_Counting"))

    def qua(cam, nhay=False):
        m.dat(cam, True)
        quet(m, "Prg_Counting", 5)
        if nhay:
            m.dat(cam, False)
            quet(m, "Prg_Counting")
            m.dat(cam, True)
            quet(m, "Prg_Counting")
        quet(m, "Prg_Counting", 5)
        m.dat(cam, False)
        quet(m, "Prg_Counting", 5)
    qua("DI_BoardInfeed")
    qua("DI_BoardInfeed", nhay=True)
    kiem(m.doc("BoardsInMachine") == 2 and m.doc("M_MachineFull"), "hai board vào (một board nháy) → 2, ĐẦY")
    m.dat("M_Board2IsNG", True)
    qua("DI_BoardOutfeed", nhay=True)
    m.dat("M_Board2IsNG", False)
    qua("DI_BoardOutfeed")
    kiem(m.doc("BoardsInMachine") == 0, "hai board ra → 0 trong máy")
    kiem(m.doc("NgCount") == 1 and m.doc("OkCount") == 1, "1 NG, 1 OK — nháy ở lối ra không đếm đôi")
    m.dat("M_ShiftStart", True)
    quet(m, "Prg_Counting")
    kiem(m.doc("OkCount") == 0 and m.doc("NgCount") == 0, "đầu ca → xoá sản lượng")


def ch19_dich():
    print("Ch.19 — FB_NgShift")
    m = May(khoi("ch19_*.md", "FUNCTION_BLOCK FB_NgShift"))

    def dich():
        m.dat("M_ConveyorIndexDone", True)
        quet(m, "Prg_NgTrack")
        m.dat("M_ConveyorIndexDone", False)
        quet(m, "Prg_NgTrack")
    m.dat("M_Stn1DispenseFault", True)
    quet(m, "Prg_NgTrack")
    m.dat("M_Stn1DispenseFault", False)
    dich()
    dich()
    m.dat("M_BoardAtReject", True)
    quet(m, "Prg_NgTrack")
    kiem(not m.doc("M_RejectNow"), "board OK phía trước tới chỗ loại bỏ → không loại")
    dich()
    kiem(m.doc("M_RejectNow"), "đúng board NG tới chỗ loại bỏ → LOẠI")
    dich()
    kiem(not m.doc("M_RejectNow"), "board OK đi sau → không loại (dịch từ cuối về đầu)")


def ch20_ham():
    print("Ch.20 — CycleClass")
    m = May(khoi("ch20_*.md", "FUNCTION CycleClass") + """
VAR_GLOBAL
    Buf : ARRAY[1..8] OF DINT;
    Chuan : DINT;
    Kq : INT;
END_VAR
PROGRAM T
Kq := CycleClass(CycleMs := Buf, RecipeMs := Chuan);
END_PROGRAM
""")
    m.dat("Chuan", 12000)
    quet(m, "T")
    kiem(m.doc("Kq") == 0, "chưa có số liệu → 0")
    for i, v in enumerate((12000, 12500, 11800), 1):
        m.doc("Buf")[i] = v
    quet(m, "T")
    kiem(m.doc("Kq") == 1, "quanh 12 s → 1 bình thường")
    for i in range(1, 9):
        m.doc("Buf")[i] = 15000
    quet(m, "T")
    kiem(m.doc("Kq") == 2, "125 % → 2 chậm")
    for i in range(1, 9):
        m.doc("Buf")[i] = 19000
    quet(m, "T")
    kiem(m.doc("Kq") == 3, "158 % → 3 rất chậm")
    m.dat("Chuan", 0)
    quet(m, "T")
    kiem(m.doc("Kq") == 0, "chuẩn = 0 → 0, không chia cho 0")


def ch24_bang():
    print("Ch.24 — CylPose")
    m = May(khoi("ch24_*.md", "FUNCTION CylPose") + """
VAR_GLOBAL
    H, W : BOOL;
    P : E_CylPose;
END_VAR
PROGRAM T
P := CylPose(SensHome := H, SensWork := W);
END_PROGRAM
""")
    for h, w, mong in ((True, False, "ATHOME"), (False, True, "ATWORK"), (False, False, "UNKNOWN"),
                       (True, True, "SENSORFAULT")):
        m.dat("H", h)
        m.dat("W", w)
        quet(m, "T")
        kiem(m.doc("P") == mong, "Home=%d Work=%d → %s" % (h, w, mong))


def ch28_giam_sat():
    print("Ch.28 — FB_StepWatch")
    m = May(khoi("ch28_*.md", "FUNCTION_BLOCK FB_StepWatch"))
    m.dat("M_HomingRun", True)
    m.dat("HomingStep", 1)
    quet(m, "Prg_HomeWatch", 250)
    kiem(not m.doc("M_Alm_HomeTimeout"), "H1 2,5 s → chưa lỗi")
    m.dat("HomingStep", 3)
    quet(m, "Prg_HomeWatch", 900)
    kiem(not m.doc("M_Alm_HomeTimeout"), "sang H3 là đếm lại — 9 s chưa lỗi")
    quet(m, "Prg_HomeWatch", 110)
    kiem(m.doc("M_Alm_HomeTimeout") and m.doc("HomeFaultStep") == 3, "H3 quá 10 s → lỗi CHỐT, bước 3")
    m.dat("M_HomingRun", False)
    quet(m, "Prg_HomeWatch", 5)
    kiem(m.doc("M_Alm_HomeTimeout"), "rời Homing → lỗi VẪN chốt")
    m.dat("M_ClearFaults", True)
    quet(m, "Prg_HomeWatch")
    m.dat("M_ClearFaults", False)
    quet(m, "Prg_HomeWatch")
    kiem(not m.doc("M_Alm_HomeTimeout") and m.doc("HomeFaultStep") == 0, "lệnh xoá → hết lỗi")
    m.dat("M_HomingRun", True)
    m.dat("HomingStep", 2)
    quet(m, "Prg_HomeWatch", 1000)
    kiem(not m.doc("M_Alm_HomeTimeout"), "H2 không giới hạn → không bao giờ lỗi")


def ch29_cong_thuc():
    print("Ch.29 — KiemTraCongThuc (dải theo Phụ lục J mục J.5)")
    m = May(ST_RECIPE + "\n" + khoi("ch29_*.md", "FUNCTION KiemTraCongThuc") + """
VAR_GLOBAL
    R : ST_Recipe;
    Kq : BOOL;
    Ly : INT;
END_VAR
PROGRAM T
Kq := KiemTraCongThuc(r := R, LyDo => Ly);
END_PROGRAM
""")
    r = m.doc("R")
    r.update({"ID": 3, "CURETIMEMS": 8000, "DISPENSELENTENTHMM": 500, "CONVSPEEDPCT": 60})
    quet(m, "T")
    kiem(m.doc("Kq") and m.doc("Ly") == 0, "công thức hợp lệ → TRUE, lý do 0")
    r["CURETIMEMS"] = 150000
    quet(m, "T")
    kiem(not m.doc("Kq") and m.doc("Ly") == 2, "sấy 150 s (> 120 s) → lý do 2")
    r["CURETIMEMS"] = 8000
    r["CONVSPEEDPCT"] = 15
    quet(m, "T")
    kiem(not m.doc("Kq") and m.doc("Ly") == 4, "chuyền 15 % (< 20 %) → lý do 4")


def ch25_may():
    print("Ch.25 — Prg_Machine")
    m = May(khoi("ch25_*.md", "PROGRAM Prg_Machine"))
    nn, chot = [False], [False]

    def q(n=1):
        for _ in range(n):
            if m.doc("M_ClearFaults"):                  # chủ cờ: xoá TRƯỚC…
                chot[0] = False
            if nn[0]:                                   # …phát hiện SAU
                chot[0] = True
            m.dat("M_AnyFault", chot[0])
            m.quet("Prg_Machine", 10)

    def nhan(tag, giu=1, nc=False):
        m.dat(tag, not nc)
        q(giu)
        m.dat(tag, nc)
        q()
    m.dat("DI_StopPB", True)
    m.dat("M_AllPermissive", True)
    m.dat("DI_ResetPB", True)
    q(20)
    kiem(m.doc("MachineState") == "UNINITIALIZED", "Reset kẹt lúc cấp điện → KHÔNG tự về gốc")
    m.dat("DI_ResetPB", False)
    q(2)
    nhan("DI_ResetPB")
    kiem(m.doc("MachineState") == "HOMING" and m.doc("M_HomingRun") and m.doc("M_AbortCycle"),
         "nhấn Reset → Homing, huỷ chu trình")
    nhan("M_HomingDone")
    kiem(m.doc("MachineState") == "IDLE" and m.doc("DO_LampYellow") and not m.doc("DO_LampGreen"), "→ Idle, đèn vàng")
    nhan("DI_StartPB")
    kiem(m.doc("MachineState") == "RUNNING" and m.doc("M_CycleEnable") and m.doc("DO_LampGreen")
         and not m.doc("DO_LampYellow"), "Start → Running, chỉ đèn xanh")
    nhan("DI_StopPB", 3, nc=True)
    kiem(m.doc("MachineState") == "HOLD" and not m.doc("DO_LampGreen") and m.doc("DO_LampYellow")
         and not m.doc("M_CycleEnable") and not m.doc("M_MotionEnable"), "Stop → Hold: đèn xanh TẮT (Bẫy 5)")
    nhan("DI_StartPB")
    kiem(m.doc("MachineState") == "RUNNING", "Start → chạy tiếp")
    nhan("DI_StopPB", 230, nc=True)
    kiem(m.doc("MachineState") == "HOMING", "giữ Stop 2,3 s → huỷ chu trình → HOMING")
    nhan("M_HomingDone")
    nhan("DI_StartPB")
    nn[0] = True
    q(2)
    kiem(m.doc("MachineState") == "ALARM" and m.doc("DO_Buzzer") and not m.doc("M_MotionEnable"),
         "lỗi → Alarm: còi, cắt chuyển động")
    nhan("DI_ResetPB")
    kiem(m.doc("MachineState") == "RESETTING" and not m.doc("DO_Buzzer"), "Reset → Resetting, tắt còi")
    q(25)
    kiem(m.doc("MachineState") == "ALARM" and not m.doc("DO_Buzzer"), "nguyên nhân còn → Alarm, còi KHÔNG kêu lại")
    nn[0] = False
    nhan("DI_ResetPB")
    q(25)
    kiem(m.doc("MachineState") == "HOMING", "hết nguyên nhân → Resetting → HOMING")


def tich_hop():
    print("Tích hợp — Ch.25 máy + Ch.26 trạm 1 + Ch.27 xy-lanh + mô hình (thứ tự gọi 27.6)")
    ma = "\n".join([ST_STATION, FB_CYL, khoi("ch25_*.md", "PROGRAM Prg_Machine"),
                    khoi("ch26_*.md", "PROGRAM Prg_Stn1Dispense"), """
VAR_GLOBAL
    DI_Stop1Up, DI_Stop1Dn, DI_Clamp1Up, DI_Clamp1Dn : BOOL;
    DO_Stop1Vlv, DO_Clamp1Vlv : BOOL;
END_VAR
PROGRAM Prg_Mech
Stop1(Req := M_Stn1_StopReq, Permit := M_MotionEnable, Reset := M_ClearFaults,
      SensWork := DI_Stop1Up, SensHome := DI_Stop1Dn, Limit := T#3S);
Clamp1(Req := M_Stn1_ClampReq, Permit := M_MotionEnable, Reset := M_ClearFaults,
       SensWork := DI_Clamp1Up, SensHome := DI_Clamp1Dn, Limit := T#3S);
DO_Stop1Vlv := Stop1.Valve;
DO_Clamp1Vlv := Clamp1.Valve;
END_PROGRAM
"""])
    m = May(ma)
    m.dat("DI_StopPB", True)
    m.dat("M_AllPermissive", True)
    m.doc("Stn2")["READY"] = True
    the = {"stop": 0.0, "clamp": 0.0, "board": False, "roi": 0, "ket": False, "xl": 0}
    nk = []

    def vat_ly(dt):
        for ten, van, t, cu, cd in (("stop", "DO_Stop1Vlv", 200, "DI_Stop1Up", "DI_Stop1Dn"),
                                    ("clamp", "DO_Clamp1Vlv", 300, "DI_Clamp1Up", "DI_Clamp1Dn")):
            if not (ten == "clamp" and the["ket"]):
                the[ten] = min(1.0, max(0.0, the[ten] + (1 if m.doc(van) else -1) * dt / t))
            m.dat(cu, the[ten] >= 1.0)
            m.dat(cd, the[ten] <= 0.0)
        if the["board"] and m.doc("M_Stn1_ConvReq") and the["stop"] <= 0.0:
            the["roi"] += dt
            if the["roi"] >= 500:
                the["board"], the["roi"] = False, 0
        m.dat("DI_BoardStn1", the["board"])
        the["xl"] = the["xl"] + dt if m.doc("Prg_Stn1Dispense.Stn1_Step") == 30 else 0
        m.dat("M_Stn1_ProcessDone", the["xl"] >= 1000)

    def vong():
        vat_ly(10)
        m.quet("Prg_Mech", 10)                                  # 2 · tầng cơ cấu
        loi = m.doc("Stn1")["FAULT"] or m.doc("Stop1.Fault") or m.doc("Clamp1.Fault")
        m.dat("M_AnyFault", bool(loi))                          # 3 · gom lỗi
        m.quet("Prg_Machine", 0)                                # 4 · tầng máy
        m.quet("Prg_Stn1Dispense", 0)                           # 5 · tầng trạm
        nk.append((m.doc("MachineState"), m.doc("Prg_Stn1Dispense.Stn1_Step"),
                   m.doc("DO_Stop1Vlv"), m.doc("DO_Clamp1Vlv")))

    def chay(ms):
        for _ in range(ms // 10):
            vong()

    def nhan(tag, nc=False):
        m.dat(tag, not nc)
        chay(30)
        m.dat(tag, nc)
        chay(20)
    chay(100)
    nhan("DI_ResetPB")
    chay(500)
    nhan("M_HomingDone")
    nhan("DI_StartPB")
    kiem(m.doc("MachineState") == "RUNNING", "về gốc xong, Start → Running")
    for so in (1, 2):
        the["board"] = True
        chay(4000)
        kiem(m.doc("Stn1")["DONECOUNT"] == so and m.doc("Prg_Stn1Dispense.Stn1_Step") == 0,
             "board %d: đủ chu trình 0 → 60 → 0" % so)
    buoc = [x[1] for x in nk]
    lien = all(not (a == 10 and b == 30) for a, b in zip(buoc, buoc[1:]))
    kiem(lien and min(buoc.count(10), buoc.count(20)) > 5, "bước 10, 20 thật sự CHỜ chặn, kẹp (Bẫy 7)")
    the["board"] = True
    for _ in range(300):
        vong()
        if m.doc("Prg_Stn1Dispense.Stn1_Step") == 20:
            break
    nhan("DI_StopPB", nc=True)
    kiem(m.doc("MachineState") == "HOLD", "Stop giữa bước 20 → Hold")
    chay(10000)
    kiem(m.doc("MachineState") == "HOLD", "giữ 10 s ở bước giới hạn 5 s → KHÔNG báo lỗi giả")
    nhan("DI_StartPB")
    chay(200)
    kiem(m.doc("MachineState") == "RUNNING", "chạy tiếp → KHÔNG báo lỗi ngay")
    chay(4000)
    kiem(m.doc("Stn1")["DONECOUNT"] == 3, "board 3 hoàn tất sau khi giữ")
    the["ket"] = True
    the["board"] = True
    chay(5000)
    kiem(m.doc("MachineState") == "ALARM", "kẹp kẹt → Alarm")
    kiem(m.doc("Clamp1.FaultCode") == 1 and m.doc("Stn1")["FAULTSTEP"] == 0,
         "khối Clamp1 báo TRƯỚC (3 s, mã 1); lưới 5 s của trạm không cần tới")
    nhan("DI_ResetPB")
    chay(300)
    kiem(m.doc("MachineState") == "ALARM", "Reset khi còn kẹt → cờ chốt lại → Alarm")
    the["ket"] = False
    chay(600)
    nhan("DI_ResetPB")
    chay(1300)
    kiem(m.doc("MachineState") == "HOMING", "gỡ kẹt, Reset → Homing")
    truoc = [i for i, x in enumerate(nk) if x[0] != "HOMING"]
    bd = truoc[-1] + 1 if truoc else 0
    if m.doc("MachineState") != "HOMING" or bd >= len(nk):
        kiem(False, "huỷ chu trình: van kẹp tắt TRƯỚC, van chặn tắt SAU khi kẹp về gốc (V1) — máy không về Homing")
    else:
        i_kep = next((i for i in range(bd, len(nk)) if not nk[i][3]), None)
        i_chan = next((i for i in range(bd, len(nk)) if not nk[i][2]), None)
        kiem(nk[bd][2] and nk[bd][3] and i_kep is not None and i_chan is not None and i_chan > i_kep,
             "huỷ chu trình: van kẹp tắt TRƯỚC, van chặn tắt SAU khi kẹp về gốc (V1)")
    kiem(m.doc("Prg_Stn1Dispense.Stn1_Step") == 0 and not m.doc("M_Stn1_ClampReq"), "bước về 0, yêu cầu về nghỉ")

def ch21_sfc():
    print("Ch.21 — trạm 1 bằng SFC dạng văn bản; chạy HAI lần: .T giữ khi rời bước (chuẩn) và .T về 0")
    ma = khoi("ch21_*.md", "PROGRAM Prg_Stn1Sfc")

    def mot_lan(kieu):
        m = May(ma)
        m.t_khi_roi = kieu
        # vat: vị trí kẹp 0..1 · board · kẹt (kẹp đứng yên) · board kẹt · thời gian xử lý · xử lý hỏng
        v = {"kep": 0.0, "board": False, "roi": 0, "ket": False, "ket_board": False, "xl": 0,
             "xl_hong": False, "hanh_trinh": 300}
        nk = []                                                 # (bước đang sống, ClampReq, ConvReq, Alm)

        def song():
            return tuple(b for b in ("S10", "S20", "S30", "S40", "S50", "S90")
                         if m.doc("Prg_Stn1Sfc.%s.X" % b))

        def vat_ly(dt):
            if not v["ket"]:
                huong = 1 if m.doc("M_Stn1_ClampReq") else -1
                v["kep"] = min(1.0, max(0.0, v["kep"] + huong * dt / v["hanh_trinh"]))
            m.dat("DI_Clamp1Up", v["kep"] >= 1.0)
            m.dat("DI_Clamp1Dn", v["kep"] <= 0.0)
            if v["board"] and m.doc("M_Stn1_ConvReq") and not v["ket_board"]:
                v["roi"] += dt
                if v["roi"] >= 500:
                    v["board"], v["roi"] = False, 0
            m.dat("DI_BoardStn1", v["board"])
            # "lát cắt sau": bộ xử lý làm 1 s khi trạm ở S30 — bộ thử nhìn được mọi thứ, PLC thì không
            v["xl"] = v["xl"] + dt if m.doc("Prg_Stn1Sfc.S30.X") else 0
            m.dat("M_Stn1_ProcessDone", v["xl"] >= 1000 and not v["xl_hong"])

        def chay(ms):
            for _ in range(ms // 10):
                vat_ly(10)
                m.quet("Prg_Stn1Sfc", 10)
                nk.append((song(), m.doc("M_Stn1_ClampReq"), m.doc("M_Stn1_ConvReq"),
                           m.doc("M_Alm_Stn1Seq")))

        def nhan_reset():
            m.dat("DI_ResetPB", True)
            chay(30)
            m.dat("DI_ResetPB", False)
            chay(20)

        kq = {}
        chay(100)
        kq["dau"] = song() == ("S10",) and not (m.doc("M_Stn1_ClampReq") or m.doc("M_Stn1_ConvReq"))
        for _ in range(3):                                      # ba board bình thường
            v["board"] = True
            chay(4000)
        vong = [x[0] for x in nk]
        kq["ba_chu_trinh"] = sum(1 for a, b in zip(vong, vong[1:]) if a == ("S50",) and b == ("S10",)) == 3
        doi_20_30 = [i for i in range(1, len(nk)) if nk[i - 1][0] == ("S20",) and nk[i][0] == ("S30",)]
        kq["kep_lien_mach"] = bool(doi_20_30) and all(nk[i - 1][1] and nk[i][1] for i in doi_20_30)
        kq["cho_that"] = vong.count(("S20",)) >= 3 * 25 and vong.count(("S40",)) >= 3 * 25
        kq["mot_buoc"] = all(len(x) == 1 for x in vong)
        # kẹp chạy chậm 2,9 s (sát giới hạn 3 s) — vẫn qua; board kế tiếp chạy bình thường
        v["hanh_trinh"], v["board"] = 2900, True
        chay(8000)
        v["hanh_trinh"] = 300
        kq["cham_van_qua"] = not any(x[3] for x in nk[-800:]) and song() == ("S10",)
        # kẹp kẹt GIỮA hành trình → S20 quá 3 s → S90
        v["board"] = True
        chay(200)
        v["ket"] = True
        chay(3500)
        kq["ket_s90"] = song() == ("S90",) and m.doc("M_Alm_Stn1Seq") and not m.doc("M_Stn1_ClampReq")
        nhan_reset()
        kq["reset_khi_kep_chua_ha"] = song() == ("S90",)
        v["ket"] = False
        chay(500)
        nhan_reset()
        chay(1500)
        kq["gỡ_kẹt_xả_board"] = song() == ("S10",) and not v["board"] and not m.doc("M_Alm_Stn1Seq")
        # board kế tiếp vào S20 sau lần quá giờ: .T của S20 phải bắt đầu lại từ 0
        v["board"] = True
        chay(4000)
        kq["sau_qua_gio_khong_bao_ngay"] = not any(x[3] for x in nk[-400:]) and song() == ("S10",)
        # xử lý không bao giờ xong → S30 quá 60 s → S90; Reset → xả board, KHÔNG gia công lại
        v["xl_hong"], v["board"] = True, True
        chay(62000)
        kq["s30_qua_gio"] = song() == ("S90",) and m.doc("DI_Clamp1Dn")
        v["xl_hong"] = False
        truoc = len(nk)
        nhan_reset()
        chay(1500)
        kq["xa_khong_gia_cong_lai"] = song() == ("S10",) and all(x[0] != ("S30",) for x in nk[truoc:])
        # board kẹt trên chuyền → S50 quá 10 s → S90; Reset → S50 lần nữa → gỡ kẹt → S10
        v["ket_board"], v["board"] = True, True
        chay(16000)
        kq["s50_qua_gio"] = song() == ("S90",)
        nhan_reset()
        v["ket_board"] = False
        chay(1500)
        kq["s50_phuc_hoi"] = song() == ("S10",) and not v["board"]
        kq["nhap_nhang"] = list(m.chuong_trinh["PRG_STN1SFC"].nhap_nhang)
        return kq, [x[0] for x in nk]

    a, vet_a = mot_lan("giu")
    b, vet_b = mot_lan("ve0")
    for k, mo_ta in (("dau", "khởi động: chỉ S10 sống, mọi hành động FALSE"),
                     ("ba_chu_trinh", "ba board: đủ ba vòng S10 → S50 → S10"),
                     ("kep_lien_mach", "M_Stn1_ClampReq gắn hai bước: KHÔNG rớt một vòng quét nào ở chỗ S20 → S30"),
                     ("cho_that", "S20, S40 thật sự CHỜ kẹp lên/xuống (Bẫy 7 của Chương 26, phiên bản SFC)"),
                     ("mot_buoc", "trình tự tuyến tính: luôn đúng MỘT bước sống"),
                     ("cham_van_qua", "kẹp chậm 2,9 s — sát giới hạn 3 s — vẫn qua, không báo lỗi"),
                     ("ket_s90", "kẹp kẹt giữa hành trình → S90: báo động bật, yêu cầu kẹp tắt"),
                     ("reset_khi_kep_chua_ha", "Reset khi kẹp chưa về → ĐỨNG YÊN ở S90"),
                     ("gỡ_kẹt_xả_board", "gỡ kẹt, Reset → S50 xả board → S10, báo động tắt"),
                     ("sau_qua_gio_khong_bao_ngay", "board kế tiếp sau lần quá giờ: S20 KHÔNG báo lỗi ngay"),
                     ("s30_qua_gio", "xử lý không xong 60 s → S90, kẹp đã hạ"),
                     ("xa_khong_gia_cong_lai", "Reset → xả board, KHÔNG quay lại S30"),
                     ("s50_qua_gio", "board kẹt trên chuyền 10 s → S90"),
                     ("s50_phuc_hoi", "Reset → S50 lần nữa, gỡ kẹt → board ra, về S10")):
        kiem(a[k] and b[k], mo_ta + " (cả hai kiểu .T)")
    kiem(not a["nhap_nhang"] and not b["nhap_nhang"],
         "không lần nào hai chuyển tiếp từ một bước cùng đúng (dòng 5: loại trừ nhau)")
    kiem(vet_a == vet_b, "hai kiểu .T khi rời bước cho CÙNG một chuỗi bước — ví dụ đúng với cả hai hệ")


def ch39_yeu_cau_pc():
    print("Ch.39 — FB_PcRequest (bắt tay với phần mềm PC theo số thứ tự)")
    vo = """
VAR_GLOBAL
    GEx : BOOL;
    GCmd, GPar, GAck, GRes : INT;
END_VAR
PROGRAM T
VAR
    R : FB_PcRequest;
END_VAR
R(Execute := GEx, Cmd := GCmd, Param := GPar, AckId := GAck, AckResult := GRes, TimeOut := T#1S);
END_PROGRAM
"""
    fb = khoi("ch39_*.md", "FUNCTION_BLOCK FB_PcRequest")
    m = May(fb + vo)

    def tra_loi(ket_qua, so=None):
        # phần mềm: ghi kết quả TRƯỚC, số thứ tự SAU (luật 2 của mục 39.9b)
        m.dat("GRes", ket_qua)
        m.dat("GAck", m.doc("T.R.ReqId") if so is None else so)

    quet(m, "T")
    m.dat("GCmd", 1)
    m.dat("GPar", 7)
    m.dat("GEx", True)
    quet(m, "T")
    kiem(m.doc("T.R.Busy") and m.doc("T.R.ReqId") == 1 and m.doc("T.R.ReqCmd") == 1
         and m.doc("T.R.ReqParam") == 7, "sườn Execute → yêu cầu số 1, chốt lệnh và tham số, Busy")
    quet(m, "T", 3)
    tra_loi(1)
    quet(m, "T")
    kiem(m.doc("T.R.Done") and m.doc("T.R.Ok") and not m.doc("T.R.Busy"), "phần mềm trả OK số 1 → Done, Ok")
    m.dat("GEx", False)
    quet(m, "T")
    kiem(not m.doc("T.R.Done") and not m.doc("T.R.Ok"), "Execute hạ → kết quả xoá")
    m.dat("GEx", True)
    quet(m, "T")
    kiem(m.doc("T.R.Busy") and m.doc("T.R.ReqId") == 2, "yêu cầu thứ hai mang số 2")
    quet(m, "T", 2)
    kiem(m.doc("T.R.Busy") and not m.doc("T.R.Done"),
         "phần mềm còn để nguyên kết quả cũ (OK, số 1) → KHÔNG bị nhận nhầm cho yêu cầu 2")
    tra_loi(1)
    quet(m, "T")
    kiem(m.doc("T.R.Done") and m.doc("T.R.Ok"), "hai kết quả OK liên tiếp → nhận đủ cả hai")
    m.dat("GEx", False)
    quet(m, "T")
    m.dat("GEx", True)
    quet(m, "T")
    tra_loi(2)
    quet(m, "T")
    kiem(m.doc("T.R.Done") and not m.doc("T.R.Ok"), "phần mềm trả NG → Done, Ok FALSE")
    m.dat("GEx", False)
    quet(m, "T")
    m.dat("GEx", True)
    quet(m, "T", 99)
    kiem(m.doc("T.R.Busy") and not m.doc("T.R.Error"), "chờ chưa đủ 1 s → còn chờ, chưa lỗi")
    quet(m, "T", 3)
    kiem(m.doc("T.R.Error") and m.doc("T.R.ErrorID") == 1 and not m.doc("T.R.Ok") and not m.doc("T.R.Done"),
         "quá 1 s không trả lời → Error mã 1 — KHÔNG thành NG")
    so_bo_cuoc = m.doc("T.R.ReqId")
    m.dat("GEx", False)
    quet(m, "T")
    m.dat("GEx", True)
    quet(m, "T")
    tra_loi(1, so_bo_cuoc)
    quet(m, "T", 3)
    kiem(m.doc("T.R.Busy") and not m.doc("T.R.Done"), "trả lời ĐẾN MUỘN cho yêu cầu đã bỏ cuộc → bị bỏ qua")
    tra_loi(2)
    quet(m, "T")
    kiem(m.doc("T.R.Done") and not m.doc("T.R.Ok"), "trả lời đúng số của yêu cầu đang chờ → nhận")
    m.dat("GEx", False)
    quet(m, "T")
    m.dat("GEx", True)
    quet(m, "T")
    tra_loi(7)
    quet(m, "T")
    kiem(m.doc("T.R.Error") and m.doc("T.R.ErrorID") == 2, "phần mềm trả mã lạ → Error mã 2")
    m.dat("GEx", False)
    quet(m, "T")
    m.dat("GEx", True)
    quet(m, "T")
    so = m.doc("T.R.ReqId")
    m.dat("GEx", False)
    quet(m, "T", 2)
    m.dat("GEx", True)
    quet(m, "T")
    kiem(m.doc("T.R.Busy") and m.doc("T.R.ReqId") == so, "kích lại khi đang bận → bỏ qua, số không đổi")
    m.dat("GEx", False)
    quet(m, "T")
    tra_loi(1)
    quet(m, "T")
    kiem(m.doc("T.R.Done") and m.doc("T.R.Ok"), "Execute chỉ là xung → kết quả vẫn hiện ít nhất MỘT vòng")
    quet(m, "T")
    kiem(not m.doc("T.R.Done"), "… và xoá ở vòng sau")
    m.dat("T.R.ReqId", 30000)
    m.dat("GEx", True)
    quet(m, "T")
    kiem(m.doc("T.R.ReqId") == 1, "quay vòng: sau 30000 là 1, không bao giờ là 0")
    m2 = May(fb + vo)
    m2.dat("GAck", 57)
    quet(m2, "T")
    m2.dat("GEx", True)
    quet(m2, "T")
    kiem(m2.doc("T.R.ReqId") == 58 and m2.doc("T.R.Busy"),
         "PLC khởi động lại khi phần mềm đã trả số 57 → yêu cầu đầu mang số 58, không nhận nhầm 57")


def ch37_hai_dau():
    print("Ch.37 — FB_TwoHeadsGap (hai đầu chung một ray)")
    m = May(khoi("ch37_*.md", "FUNCTION_BLOCK FB_TwoHeadsGap") + """
VAR_GLOBAL
    A1, T1, A2, T2, V1, V2 : REAL;
    Dec : REAL := 3000.0;
END_VAR
PROGRAM T
VAR
    G : FB_TwoHeadsGap;
END_VAR
G(X1Act := A1, X1Tgt := T1, X2Act := A2, X2Tgt := T2, V1Act := V1, V2Act := V2,
  GapMin := 40.0, DecStop := Dec, TReact := 0.006);
END_PROGRAM
""")

    def dat(a1, t1, a2, t2, v1=0.0, v2=0.0):
        for k, v in (("A1", a1), ("T1", t1), ("A2", a2), ("T2", t2), ("V1", v1), ("V2", v2)):
            m.dat(k, float(v))
        quet(m, "T")

    dat(100, 100, 500, 500)
    kiem(m.doc("T.G.PathClear") and not m.doc("T.G.StopBoth") and abs(m.doc("T.G.GapNow") - 400) < 1e-6,
         "hai đầu xa nhau, đứng yên → được đi, không dừng, khoảng hở 400 mm")
    dat(100, 480, 500, 500)
    kiem(not m.doc("T.G.PathClear"), "đích đầu 1 lấn vào đầu 2 (480 + 40 > 500) → KHÔNG được phát lệnh")
    dat(100, 280, 500, 300)
    kiem(not m.doc("T.G.PathClear"), "đầu 2 đang đi sang 300: đích 280 của đầu 1 cộng 40 lấn đoạn đó → chặn")
    dat(100, 250, 500, 300)
    kiem(m.doc("T.G.PathClear"), "đích 250 + 40 = 290 ≤ 300 → được đi")
    dat(200, 200, 241, 241)
    kiem(not m.doc("T.G.StopBoth"), "đứng yên sát nhau 41 mm (> 40) → KHÔNG báo — việc làm sát nhau vẫn được phép")
    dat(200, 300, 280, 280, v1=300.0)
    kiem(abs(m.doc("T.G.GapNeed") - 56.8) < 1e-6 and not m.doc("T.G.StopBoth"),
         "đầu 1 tiến lại 300 mm/s: cần 40 + 1,8 + 15 = 56,8 mm; đang hở 80 → chưa dừng")
    dat(230, 300, 280, 280, v1=300.0)
    kiem(m.doc("T.G.StopBoth"), "hở còn 50 < 56,8 → dừng cả hai")
    dat(200, 300, 270, 200, v1=300.0, v2=-300.0)
    kiem(abs(m.doc("T.G.GapNeed") - 73.6) < 1e-6 and m.doc("T.G.StopBoth"),
         "hai đầu cùng tiến lại 300 mm/s: cần 73,6 mm; hở 70 → dừng")
    dat(200, 300, 280, 200, v1=300.0, v2=-300.0)
    kiem(not m.doc("T.G.StopBoth"), "… hở 80 > 73,6 → chưa dừng")
    dat(200, 100, 245, 245, v1=-300.0)
    kiem(not m.doc("T.G.StopBoth"), "đầu 1 đang đi RA XA (tốc độ âm) → không tính quãng phanh, hở 45 → không dừng")
    m.dat("Dec", 0.0)
    dat(100, 100, 500, 500)
    kiem(m.doc("T.G.StopBoth") and not m.doc("T.G.PathClear"),
         "gia tốc hãm bằng 0 (thiếu tham số) → dừng và không cho phát lệnh")


def ch28_chay_kho():
    print("Ch.28 — chạy khô nhiều mức: bản ✗ (sườn) và Prg_DryRunMap (tính từ mức)")
    bang = {0: (False, False, False, False), 1: (True, True, True, True),
            2: (False, True, True, True), 3: (False, False, False, True)}
    co = ("M_BypBoard", "M_BypWork", "M_BypLine", "M_BypHost")
    sai = khoi("ch28_*.md", "Lv1Up(CLK")
    m = May("""
VAR_GLOBAL
    M_DryLevel : INT;
    M_BypBoard, M_BypWork, M_BypLine, M_BypHost : BOOL;
END_VAR
PROGRAM X
VAR
    Lv1Up, Lv2Up : R_TRIG;
    Lv1Dn, Lv2Dn : F_TRIG;
END_VAR
""" + sai + """
END_PROGRAM
""")
    quet(m, "X", 3)
    m.dat("M_DryLevel", 2)
    quet(m, "X")
    kiem(tuple(m.doc(c) for c in co) == bang[2], "✗ bản sườn: 0 → 2 → cờ đúng bảng mức 2")
    m.dat("M_DryLevel", 1)
    quet(m, "X")
    kiem(tuple(m.doc(c) for c in co) == (True, False, False, False),
         "✗ bản sườn: đổi 2 → 1 trong MỘT lần ghi → chỉ còn M_BypBoard — đúng lỗi Bẫy 7 (đầu công tác làm việc thật)")
    m.dat("M_DryLevel", 2)
    quet(m, "X")
    kiem(tuple(m.doc(c) for c in co) == bang[2], "✗ bản sườn: đổi 1 → 2 thì lại đúng — lỗi chỉ theo MỘT chiều")

    m = May(khoi("ch28_*.md", "PROGRAM Prg_DryRunMap"))
    hong = []
    for a in range(4):
        for b in range(4):
            m.dat("M_DryLevel", a)
            quet(m, "Prg_DryRunMap")
            m.dat("M_DryLevel", b)
            quet(m, "Prg_DryRunMap")
            if tuple(m.doc(c) for c in co) != bang[b] or m.doc("M_AnyBypass") != any(bang[b]):
                hong.append((a, b))
    kiem(not hong, "✔ Prg_DryRunMap: đổi qua lại cả 16 cặp mức bằng một lần ghi → bốn cờ luôn đúng bảng")
    m.dat("M_BypHostMan", True)
    m.dat("M_DryLevel", 2)
    quet(m, "Prg_DryRunMap")
    m.dat("M_DryLevel", 0)
    quet(m, "Prg_DryRunMap")
    kiem(m.doc("M_BypHost") and not m.doc("M_BypWork") and m.doc("M_AnyBypass"),
         "✔ cờ bật TAY còn nguyên khi rời chạy khô — mức không xoá được nó")
    m.dat("M_BypHostMan", False)
    m.dat("M_DryLevel", 5)
    quet(m, "Prg_DryRunMap")
    kiem(m.doc("M_DryLevelBad") and not m.doc("M_AnyBypass"), "✔ mức ngoài bảng → báo lỗi cấu hình, không bật cờ nào")


def main():
    for f in (ch27_xylanh, ch27_anh_xa, ch30_chuyen_board, ch42_ma, ch14_pou, ch16_danh_dau, ch17_loc, ch18_dem,
              ch19_dich, ch20_ham, ch24_bang, ch28_giam_sat, ch29_cong_thuc, ch25_may, tich_hop,
              ch21_sfc, ch39_yeu_cau_pc, ch37_hai_dau, ch28_chay_kho):
        f()
    print("-" * 78)
    print("CHẠY THỬ: %d đạt · %d hỏng" % (SO_DAT[0], len(SO_HONG)))
    for h in SO_HONG:
        print("  HỎNG: " + h)
    print("-" * 78)
    return 1 if SO_HONG else 0


if __name__ == "__main__":
    sys.exit(main())
