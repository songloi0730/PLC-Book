# Máy mẫu xuyên suốt — DP-01 · Trạm tra keo & sấy UV trên chuyền board mạch

*Dispensing & UV-cure station on a PCB conveyor line*

> **Bất biến B8:** mọi ví dụ từ Ch.8 trở đi dùng chung hồ sơ này. Đổi số liệu ở đây **trước**, rồi mới
> rà lại các chương đã dùng số cũ. Ch.57 ráp toàn bộ thành một chương trình hoàn chỉnh; Phụ lục J là
> bản hồ sơ đầy đủ để người đọc dùng lại làm khung cho dự án thật.
>
> ⚠ DP-01 là máy **phiếm chỉ** (generic), dựng riêng cho mục đích dạy học. Không dựa trên máy, dự án
> hay khách hàng cụ thể nào. Số liệu là minh hoạ hợp lý, **không phải thông số kiểm định**.

Trạng thái: ✅ **đã chốt số liệu (session 11)** — xem §7. Còn 2 hạng mục nhỏ ở §8.
Lý do chọn máy này: ADR 0002 §2.

---

## 1. Máy làm gì

Board mạch (PCB) đi từ máy phía trước sang, được tra một đường keo bảo vệ lên vùng linh kiện, rồi
sấy cứng bằng đèn UV, rồi chuyển sang máy phía sau. Mỗi board có mã 2D riêng — máy đọc mã, hỏi hệ
thống quản lý sản xuất (MES) xem board này có được phép làm không và làm theo công thức nào, rồi báo
kết quả về sau khi xong.

```text
 [Máy trước] ──SMEMA──► ┌──────────────── DP-01 ────────────────┐ ──SMEMA──► [Máy sau]
                        │                                        │
                        │  chuyền vào    TRẠM 1        TRẠM 2    │
                        │      ●────────► TRA KEO ────► SẤY UV ──►│
                        │   đọc mã 2D   gantry XY+Z   đèn UV      │
                        │   hỏi MES     van tra keo   cửa chắn    │
                        └────────────────────────────────────────┘
```

### Vì sao chọn máy này làm máy mẫu

| Yêu cầu dạy học | DP-01 đáp ứng bằng |
|---|---|
| Logic rời rạc *(discrete logic)*, tuần tự | Chặn → nâng kẹp → xử lý → hạ → nhả — lặp ở cả hai trạm |
| ⭐ **Song song & pipeline** | Hai trạm xử lý **hai board khác nhau cùng lúc** — bài toán thật, không phải ví dụ giả định |
| ⭐ **Phục hồi sau lỗi khó** | Dừng khi board A đang ở trạm keo *và* board B đang ở trạm UV — phải xử lý cả hai |
| Analog & PID | Áp suất khí, áp keo, nhiệt độ gia nhiệt keo *(PID)*, cường độ UV |
| Chuyển động *(motion)* | Gantry XY + trục Z — nhiều trục phối hợp, chạy theo đường |
| ⭐ **Truy xuất nguồn gốc** *(traceability)* | Đọc mã 2D → hỏi MES → ghi kết quả; xử lý khi mất kết nối MES |
| ⭐ **Ghép nối dây chuyền** | Bắt tay *(handshake)* kiểu SMEMA với máy trước và máy sau |
| An toàn máy | Bức xạ UV là **mối nguy vật lý thật** — chương an toàn không phải nói lý thuyết suông |
| Đặc thù điện tử | ESD *(tĩnh điện)*, ion hoá, công thức theo mã hàng, xử lý board NG |

Máy đủ nhỏ để dựng lại được trên phần mềm mô phỏng, đủ lớn để chạm hết kỹ năng cần dạy.

### Bóc lớp dần — chương nào dùng phần nào

| Giai đoạn | Chỉ dùng | Chương |
|---|---|---|
| **Lát cắt 1 — thuần rời rạc** | Chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp | Ch.8–22 |
| **Lát cắt 2 — thêm thiết kế** | + máy trạng thái 2 trạm, trình tự song song, công thức sản phẩm | Ch.23–30 |
| **Lát cắt 3 — thêm analog & trục** | + áp keo, nhiệt độ, cường độ UV, gantry XY/Z | Ch.31–37 |
| **Lát cắt 4 — thêm mạng** | + mã 2D, MES, SMEMA, HMI | Ch.38–46 |
| **Lát cắt 5 — đầy đủ** | + mạch an toàn, chạy thử, chẩn đoán | Ch.47–58 |

> 💡 Cách dùng khi viết: chương thuộc lát cắt nào thì **chỉ được nhắc tới thiết bị của lát cắt đó và
> các lát cắt trước**. Ch.15 (Ladder) không được lấy ví dụ về servo.

---

## 2. Bảng vào/ra — I/O list (bản nháp)

Quy ước đặt tên: `DI_/DO_/AI_/AO_` + vị trí + chức năng. Trạm 1 = tra keo, trạm 2 = sấy UV.

### 2.1 Ngõ vào số — Digital Input (DI)

| Tag | Mô tả | Loại thiết bị | Trạng thái nghỉ | Lát cắt | Chương |
|---|---|---|---|---|---|
| `DI_StartPB` | Nút Start | Nút nhấn *(push button)* NO | 0 | 1 | 15, 25 |
| `DI_StopPB` | Nút Stop | Nút nhấn **NC** | 1 | 1 | 15, 48 |
| `DI_ResetPB` | Nút Reset | Nút nhấn NO | 0 | 1 | 25, 28 |
| `DI_ModeAuto` | Chọn chế độ Auto / Manual | Công tắc xoay 2 vị trí | — | 1 | 28 |
| `DI_EStopOK` | Mạch dừng khẩn cấp lành | Tiếp điểm **NC** từ rơ-le an toàn | 1 | 5 | 47, 48 |
| `DI_Door1Closed` | Cửa bảo vệ trạm keo đóng & khoá | Công tắc an toàn **NC** | 1 | 5 | 47 |
| `DI_Door2Closed` | Cửa bảo vệ trạm UV đóng & khoá | Công tắc an toàn **NC** | 1 | 5 | 47 |
| `DI_CurtainOK` | Rèm quang *(light curtain)* tại cửa chuyền không bị cắt | Từ rơ-le an toàn, **NC** | 1 | 5 | 47 |
| `DI_AirOK` | Áp suất khí đạt ngưỡng tối thiểu | Công tắc áp suất NO | 1 khi đủ khí | 1 | 48 |
| `DI_BoardInfeed` | Có board ở đầu chuyền vào | Quang thu-phát *(through-beam)*, PNP | 0 | 1 | 4, 15 |
| `DI_BoardStn1` | Board đã tới vị trí trạm keo | Quang thu-phát, PNP | 0 | 1 | 4, 18 |
| `DI_BoardStn2` | Board đã tới vị trí trạm UV | Quang thu-phát, PNP | 0 | 1 | 4, 18 |
| `DI_BoardOutfeed` | Board ở đầu chuyền ra | Quang thu-phát, PNP | 0 | 1 | 15 |
| `DI_Stop1Up` / `DI_Stop1Dn` | Chặn trạm 1 đã nâng / đã hạ | Reed xy-lanh, PNP | 0 / 1 | 1 | 5, 26 |
| `DI_Clamp1Up` / `DI_Clamp1Dn` | Bàn nâng kẹp trạm 1 đã lên / đã xuống | Reed xy-lanh, PNP | 0 / 1 | 1 | 5, 48 |
| `DI_Stop2Up` / `DI_Stop2Dn` | Chặn trạm 2 đã nâng / đã hạ | Reed xy-lanh, PNP | 0 / 1 | 1 | 5, 26 |
| `DI_Clamp2Up` / `DI_Clamp2Dn` | Bàn nâng kẹp trạm 2 đã lên / đã xuống | Reed xy-lanh, PNP | 0 / 1 | 1 | 5, 48 |
| `DI_ShutterOpen` / `DI_ShutterClosed` | Cửa chắn đèn UV mở / đóng | Reed xy-lanh, PNP | 0 / 1 | 5 | 47 |
| `DI_VfdReady` | Biến tần chuyền sẵn sàng, không lỗi | Tiếp điểm khô NO | 1 | 3 | 36, 51 |
| `DI_IonizerOK` | Bộ khử tĩnh điện *(ionizer)* hoạt động bình thường | Tiếp điểm khô NO | 1 | 1 | 7, 51 |
| `DI_SmemaInAvail` | Máy trước báo: **có board sẵn sàng chuyển sang** | Tín hiệu SMEMA, cách ly quang | 0 | 4 | 41 |
| `DI_SmemaOutRdy` | Máy sau báo: **sẵn sàng nhận board** | Tín hiệu SMEMA, cách ly quang | 0 | 4 | 41 |

### 2.2 Ngõ ra số — Digital Output (DO)

| Tag | Mô tả | Tải | Kiểu ngõ ra nên dùng | Lát cắt | Chương |
|---|---|---|---|---|---|
| `DO_ConvRun` | Cho phép chuyền chạy (tới biến tần) | Ngõ vào số biến tần | Transistor | 1 | 9, 36 |
| `DO_Stop1Vlv` | Van chặn trạm 1 *(5/2, lò xo về)* | Van điện từ 24 VDC | Transistor + diode dập | 1 | 6, 9 |
| `DO_Clamp1Vlv` | Van nâng kẹp trạm 1 | Van điện từ 24 VDC | Transistor + diode dập | 1 | 6, 9 |
| `DO_Stop2Vlv` | Van chặn trạm 2 | Van điện từ 24 VDC | Transistor + diode dập | 1 | 6, 9 |
| `DO_Clamp2Vlv` | Van nâng kẹp trạm 2 | Van điện từ 24 VDC | Transistor + diode dập | 1 | 6, 9 |
| `DO_DispVlv` | Van tra keo *(dispensing valve)* | Van điện từ tác động nhanh | Transistor | 3 | 9, 37 |
| `DO_SuckBack` | Van hút ngược chống nhỏ giọt | Van chân không | Transistor | 3 | 6 |
| `DO_UvLamp` | Bật đèn UV | Contactor qua rơ-le trung gian | Relay | 5 | 9, 47 |
| `DO_ShutterVlv` | Van cửa chắn đèn UV | Van điện từ 24 VDC | Transistor + diode dập | 5 | 47 |
| `DO_ExhaustFan` | Quạt hút khí trạm UV | Contactor qua rơ-le trung gian | Relay | 5 | 9 |
| `DO_IonizerEn` | Cho phép bộ khử tĩnh điện | Ngõ vào điều khiển | Transistor | 1 | 7 |
| `DO_LampGreen` / `DO_LampYellow` / `DO_LampRed` | Đèn tháp 3 màu | Đèn 24 VDC | Transistor | 1 | 44 |
| `DO_Buzzer` | Còi báo | Còi 24 VDC | Transistor | 1 | 44 |
| `DO_SmemaOutAvail` | Báo máy sau: **có board sẵn sàng chuyển đi** | Tín hiệu SMEMA, cách ly quang | Transistor | 4 | 41 |
| `DO_SmemaInRdy` | Báo máy trước: **sẵn sàng nhận board** | Tín hiệu SMEMA, cách ly quang | Transistor | 4 | 41 |

### 2.3 Analog

| Tag | Mô tả | Tín hiệu | Dải kỹ thuật | Lát cắt | Chương |
|---|---|---|---|---|---|
| `AI_AirPress` | Áp suất khí nén cấp máy | 4–20 mA, 2 dây *(loop-powered)* | 0–10 bar | 3 | 31, 32 |
| `AI_GluePress` | Áp suất keo thực tế tại đầu tra | 4–20 mA, 2 dây | 0–6 bar | 3 | 31, 32 |
| `AI_UvChamberTemp` | Nhiệt độ buồng sấy UV — giám sát quá nhiệt | RTD Pt100, 3 dây | 0–150 °C | 3 | 33 |
| `AI_UvIntensity` | Cường độ đèn UV đo tại buồng sấy | 0–10 V | 0–200 mW/cm² | 3 | 32, 33 |
| `AO_GluePressSet` | Đặt áp keo *(van điều áp điện tử)* | 0–10 V | 0–6 bar | 3 | 32, 37 |
| `AO_ConvSpeed` | Đặt tốc độ chuyền | 0–10 V | 0–100 % ↔ 0–20 m/phút | 3 | 32, 36 |
| `AO_UvPower` | Đặt công suất đèn UV | 0–10 V | 0–100 % | 3 | 32 |

### 2.4 Trục & mạng

| Tên | Mô tả | Lát cắt | Chương |
|---|---|---|---|
| `AX_X`, `AX_Y` | Gantry 2 trục mang đầu tra keo — **servo**, chạy theo đường trong công thức | 3 | 37 |
| `AX_Z` | Trục nâng/hạ đầu tra keo — **servo**, đặt độ cao theo công thức | 3 | 37 |
| `NET_HMI` | Màn hình vận hành | 4 | 44 |
| `NET_Scanner` | Đầu đọc mã 2D trên board — **Ethernet** | 4 | 42 |
| `NET_TempCtrl` | Bộ điều khiển nhiệt độ keo rời — **RS-485, Modbus RTU** | 3 | 33, 35, 38, 39 |
| `NET_MES` | Hệ thống quản lý sản xuất — hỏi công thức, báo kết quả | 4 | 42, 45 |
| `NET_Drives` | 3 servo drive qua Ethernet công nghiệp | 3 | 40 |
| `NET_IoLink` | IO-Link master cho cảm biến thông minh (khoảng cách, áp suất) | 2 | 12 |

> 🔍 **BẪY (dùng khi viết Ch.4 và Ch.15).** `DI_StopPB`, `DI_EStopOK`, `DI_Door1Closed`,
> `DI_Door2Closed`, `DI_CurtainOK` đều là tiếp điểm **NC** — bình thường tín hiệu **có mặt**, và
> **đứt dây làm máy dừng**. Đây là ví dụ trung tâm cho mục "vì sao mạch dừng phải dùng NC" (Ch.4) và
> cho bảng 4 tổ hợp NO/NC ở Ch.15.

> ⚡ **Ghi chú ESD (Ch.7).** `DI_IonizerOK` không phải trang trí: nếu bộ khử tĩnh điện hỏng mà máy
> vẫn chạy, board sẽ hỏng **không có triệu chứng tại chỗ** — lỗi chỉ lộ ra ở công đoạn kiểm cuối
> hoặc tệ hơn là ở tay khách hàng. Đây là ví dụ trung tâm cho luận điểm "có những lỗi máy không tự
> báo được, phải thiết kế để nó báo".

---

## 3. Đặc tả trình tự — sequence (bản nháp)

Điều kiện vào Auto: đã về gốc *(homed)*, không có lỗi, cả hai cửa đóng, rèm quang không bị cắt,
khí đủ, ionizer OK, chọn chế độ Auto, MES kết nối được (hoặc đã bật chế độ chạy tạm không MES).

### 3.1 Trạm 1 — Tra keo

| Bước | Hành động | Điều kiện chuyển tiếp | Timeout |
|---|---|---|---|
| S1.00 | Chờ board vào | `DI_BoardStn1` = 1 | — |
| S1.10 | Nâng chặn, dừng chuyền tại trạm 1 | `DI_Stop1Up` = 1 | 1 s |
| S1.20 | Đọc mã 2D trên board | Nhận được chuỗi mã hợp lệ | 3 s |
| S1.30 | Hỏi MES: board này có được làm không, công thức nào | Nhận phản hồi | 5 s |
| S1.40 | Nâng kẹp board | `DI_Clamp1Up` = 1 | 2 s |
| S1.50 | Kiểm tra điều kiện keo: áp keo và nhiệt độ trong dải công thức | Cả hai đạt | 30 s |
| S1.60 | Gantry chạy theo đường tra keo trong công thức | Hoàn tất đường | 60 s |
| S1.70 | Hút ngược, nâng trục Z về vị trí an toàn | `AX_Z` tại vị trí chờ | 3 s |
| S1.80 | Hạ kẹp | `DI_Clamp1Dn` = 1 | 2 s |
| S1.90 | Hạ chặn, chuyển board sang trạm 2 | `DI_BoardStn1` = 0 **và** trạm 2 rỗng | 5 s |
| → S1.00 | Ghi log, quay lại chờ board | | |

### 3.2 Trạm 2 — Sấy UV

| Bước | Hành động | Điều kiện chuyển tiếp | Timeout |
|---|---|---|---|
| S2.00 | Chờ board vào | `DI_BoardStn2` = 1 | — |
| S2.10 | Nâng chặn | `DI_Stop2Up` = 1 | 1 s |
| S2.20 | Nâng kẹp | `DI_Clamp2Up` = 1 | 2 s |
| S2.30 | Bật quạt hút, mở cửa chắn UV | `DI_ShutterOpen` = 1 | 2 s |
| S2.40 | Sấy — giữ đủ thời gian theo công thức, giám sát cường độ UV | Hết thời gian **và** cường độ luôn trong dải | — |
| S2.50 | Đóng cửa chắn UV | `DI_ShutterClosed` = 1 | 2 s |
| S2.60 | Hạ kẹp, hạ chặn | `DI_Clamp2Dn` = 1, `DI_Stop2Dn` = 1 | 2 s |
| S2.70 | Chuyển board ra, bắt tay SMEMA với máy sau | `DI_BoardOutfeed` = 0 | 10 s |
| S2.80 | Báo kết quả về MES, tăng bộ đếm sản lượng | Đã gửi | 5 s |
| → S2.00 | Quay lại chờ board | | |

> 🔍 **BẪY (Ch.17).** Mọi bước chờ cơ cấu ở trên chuyển tiếp bằng **tín hiệu phản hồi thật** (reed
> xy-lanh, cảm biến board), timeout chỉ để **báo lỗi**. Phiên bản sai — mà người mới hay viết — là
> chuyển tiếp bằng chính timer: *"chờ 2 giây chắc kẹp xong rồi"*. Ch.17 và Ch.48 dùng chính bảng này
> để so sánh hai cách và chỉ ra hậu quả.

> ⭐ **Điểm dạy pipeline (Ch.26–27).** S1.90 chỉ chuyển tiếp khi **trạm 2 rỗng**. Hai trạm chạy song
> song trên hai board khác nhau; ràng buộc duy nhất giữa chúng là chỗ trống. Đây là bài toán đồng bộ
> giữa trạm — và là chỗ để dạy vì sao **không được busy-wait** giữa hai trình tự.

---

## 4. Các trạng thái máy — state model (nguồn cho Ch.25)

```text
Uninitialized ──► Homing ──► Idle ──► Running ──► (hai trạm chạy song song)
                    │          │         │
                    │          │         ├──► Hold  (giữ nguyên vị trí, board ở nguyên chỗ)
                    │          │         │
                    └──────────┴─────────┴──► Alarm ──► Reset ──► Homing
```

Mỗi trạm có máy trạng thái con riêng; máy trạng thái tổng quyết định cả hai được phép chạy hay không.

### Điểm khó cố ý — dùng cho Ch.28

Nếu máy vào **Alarm** đúng lúc:
- board A đang **bị kẹp ở trạm 1**, đầu tra keo đang ở giữa đường tra, trục Z đang hạ thấp, **và**
- board B đang **trong buồng UV** với cửa chắn đang mở, đèn đang bật —

thì trình tự về gốc *(homing)* phải:
1. **Tắt đèn UV và đóng cửa chắn trước tiên** — người vào máy trước khi che được nguồn UV là tai nạn.
2. **Nâng trục Z lên vị trí an toàn trước khi** cho gantry XY chạy về gốc — nếu không, đầu tra keo
   quét ngang qua mặt board đang kẹp và phá cả board lẫn đầu keo.
3. **Chỉ nhả kẹp sau khi** trục Z đã lên — nhả trước làm board dịch trong khi đầu keo còn ở gần.
4. Board dở dang phải được **đánh dấu NG và báo MES**, không được lẫn vào hàng tốt.

Đây là ví dụ trung tâm cho luận điểm **"về gốc là bài toán khó nhất thực tế"** (Ch.28), và cho thấy
thứ tự về gốc là kết quả của **phân tích va chạm và mối nguy**, không phải thứ tự tuỳ ý.

---

## 5. Công thức sản phẩm — recipe (nguồn cho Ch.29)

Mỗi mã hàng có một công thức. Đây là lý do máy điện tử **bắt buộc** phải tách tham số khỏi logic:
cùng một máy chạy nhiều mã hàng trong một ca.

| Tham số | Đơn vị | Dải hợp lệ | Dùng ở bước |
|---|---|---|---|
| Đường tra keo (danh sách điểm X, Y, Z) | mm | trong vùng làm việc | S1.60 |
| Áp keo đặt | bar | 0,5 – 5,0 | S1.50 |
| Nhiệt độ keo đặt | °C | 20 – 60 | S1.50 |
| Dung sai nhiệt độ | °C | 0,5 – 5,0 | S1.50 |
| Tốc độ chạy đường tra | mm/s | 5 – 100 | S1.60 |
| Thời gian sấy UV | s | 5 – 120 | S2.40 |
| Công suất đèn UV | % | 30 – 100 | S2.40 |
| Ngưỡng cường độ UV tối thiểu | mW/cm² | 20 – 180 | S2.40 |
| Tốc độ chuyền | % | 20 – 100 | mọi bước chuyền |

> ⚠ **Kiểm tra hợp lệ là bắt buộc (Ch.29).** Nếu công thức tải từ MES có nhiệt độ đặt 600 °C do lỗi
> nhập liệu, máy phải **từ chối và báo lỗi**, không được nhận. Dải hợp lệ ở cột 3 chính là hàng rào
> đó — và nó thuộc về chương trình PLC, không phải thuộc về MES.

---

## 6. Chức năng an toàn — safety functions (nguồn cho Ch.47–48)

| SF | Mối nguy | Biện pháp | Ghi chú |
|---|---|---|---|
| SF1 | Dừng khẩn cấp mọi chuyển động | E-Stop 2 kênh → rơ-le an toàn → cắt nguồn van + STO cho 3 servo + ngắt contactor đèn UV & quạt | **Không** đi qua logic PLC thường (Ch.47) |
| SF2 | ⭐ **Bức xạ UV chiếu vào mắt/da người** | Cửa chắn cơ khí + khoá cửa buồng UV; đèn chỉ được bật khi **cửa buồng đóng và khoá**; mở cửa → cắt nguồn đèn qua mạch an toàn, không qua lệnh PLC | Mối nguy vật lý thật, không có triệu chứng tức thời — người bị chiếu thường không biết |
| SF3 | Kẹp tay khi bàn nâng kẹp hoạt động | Cửa bảo vệ có khoá tại cả hai trạm | Khoá kiểu giữ tới khi an toàn |
| SF4 | Với tay vào qua cửa chuyền vào/ra | Rèm quang tại hai cửa chuyền | Cần cân nhắc muting để board đi qua mà không dừng máy (Ch.47) |
| SF5 | Máy khởi động bất ngờ sau khi khôi phục nguồn | Yêu cầu Reset có chủ ý; không tự vào Running | Ch.48 |
| SF6 | Mất khí nén khi board đang bị kẹp | Trạng thái an toàn cho van kẹp: **giữ kẹp**, không nhả | Quyết định thiết kế có lý do (Ch.48) |
| SF7 | Đầu tra keo nóng gây bỏng | Che chắn cơ khí + cảnh báo; ngắt gia nhiệt khi mở cửa | Ch.47 |

> ⚠ Bảng này là **ví dụ dạy học**, không phải kết quả đánh giá rủi ro *(risk assessment)*. Ch.47 phải
> nêu rõ: máy thật cần đánh giá rủi ro riêng bởi người có thẩm quyền, và mức PL/SIL phải xác định từ
> đánh giá đó — không phải chép từ sách.

---

## 7. Số liệu đã chốt

Năm hạng mục treo từ session 2 đã được chủ dự án chốt (session 11):

| # | Hạng mục | ✅ Quyết định | Ảnh hưởng |
|---|---|---|---|
| 1 | Mục tiêu sản lượng | ⭐ **300 board/giờ** → **12 giây/board** | Ch.55, 57 |
| 2 | Giao tiếp đầu đọc mã 2D | **Ethernet** — theo thực tế thị trường | Ch.42 |
| 2b | Thiết bị dạy giao tiếp nối tiếp | ⭐ **Bộ điều khiển nhiệt độ keo rời, RS-485 / Modbus RTU** | Ch.38, 39 |
| 3 | Thị giác máy trong máy mẫu | **Không đưa vào.** Ch.43 dùng ví dụ riêng; nếu cần, DP-01 chỉ **nhận kết quả** (toạ độ X, Y, góc) | Ch.43, 57 |
| 4 | Trục Z | ⭐ **Servo** — đặt độ cao đầu keo theo công thức | Ch.29, 37 |
| 5 | Kích thước board | ⭐ **100 × 80 mm** | Ch.32, 37, 55 |

### 7.1 Số liệu dẫn xuất

Các con số sau **suy ra** từ quyết định ở trên, dùng thống nhất cho mọi chương:

| Hạng mục | Giá trị | Suy ra từ |
|---|---|---|
| Chu kỳ mục tiêu | **12,0 s/board** | 300 board/giờ |
| Chu kỳ mỗi trạm (pipeline 2 trạm) | ≤ **12,0 s** | Hai trạm chạy song song, trạm chậm nhất quyết định nhịp |
| ⭐ Trạm quyết định nhịp | **Trạm 2 — sấy UV**, 6–12 s theo mã hàng | Bảng công thức §5 — mã B cần 12 s, sát trần |
| Vùng làm việc gantry | **X 0–150 mm · Y 0–120 mm · Z 0–50 mm** | Board 100 × 80 mm + biên gá và bù đầu tra |

> ⚠ **Hàng "trạm quyết định nhịp" là hàng đáng chú ý khi viết Ch.55.**
> Với mã hàng cần sấy 12 giây, trạm 2 chiếm **trọn** chu kỳ mục tiêu — không còn dư cho việc chặn,
> kẹp, nhả. Nghĩa là ở mã hàng đó, DP-01 **không đạt 300 board/giờ**.
>
> Đây là **nút cổ chai có thật và tính ra được**, đúng thứ Ch.55 cần để dạy: đo chu kỳ từng trạm,
> tìm trạm chậm nhất, rồi bàn các hướng xử lý (thêm buồng sấy thứ hai, tăng công suất đèn để rút thời
> gian, hay chấp nhận sản lượng thấp hơn ở mã hàng đó). Đừng "sửa" con số này cho đẹp — nó là bài học.

### 7.2 Ghi chú về quyết định 2 và 2b

Quyết định tách **đầu đọc mã 2D (Ethernet)** khỏi **thiết bị dạy giao tiếp nối tiếp (RS-485)** xuất
phát từ một quan sát của chủ dự án: đầu đọc mã ngày nay phần lớn dùng Ethernet, nên ép nó thành
RS-232 chỉ để dạy Ch.38 sẽ **sai thực tế**.

Bộ điều khiển nhiệt độ rời được chọn thay thế vì ba lý do:

- Đây là **thiết bị nối tiếp phổ biến nhất** trong chế tạo máy — RS-485 với Modbus RTU.
- Nó có sẵn lý do tồn tại trên DP-01: bộ gia nhiệt keo cần nhiệt độ ổn định, và dùng bộ điều khiển
  chuyên dụng là lựa chọn rất thường gặp.
- ⭐ Nó tạo ra một **quyết định thiết kế đáng dạy** ở Ch.35: *khi nào dùng bộ điều khiển rời, khi nào
  tự viết PID trên PLC* — câu hỏi thật mà người làm máy phải trả lời.

Hệ quả: `AI_GlueTemp` (RTD nối thẳng vào PLC) được **bỏ**; nhiệt độ keo đọc qua RS-485. Để giữ một ví
dụ RTD nối trực tiếp cho Ch.33, thêm `AI_UvChamberTemp` — giám sát quá nhiệt buồng sấy, là phép đo có
lý do thật vì đèn UV sinh nhiệt.

> ⚠ **Việc cần kiểm trước khi phát hành:** chủ dự án yêu cầu **đối chiếu thực tế thị trường** —
> đầu đọc mã 2D hiện nay thực sự dùng giao tiếp gì, và bộ điều khiển nhiệt độ rời có còn phổ biến
> không. Hai nhận định ở trên dựa trên hiểu biết chung về ngành, **chưa được xác minh bằng catalogue
> hiện hành** (B2, B10). Cần tra trước khi in.

---

## 8. Việc còn phải chốt

| # | Hạng mục | Ảnh hưởng tới |
|---|---|---|
| 1 | ⚠ `AI_UvIntensity` đang là **0–10 V**. Cường độ UV suy giảm là lỗi "máy không tự phát hiện được" (Ch.48) — có nên đổi sang **4–20 mA** để phân biệt được đứt dây không? Xem lập luận ở Ch.31 mục 31.7 | Ch.31, 32, 48 |
| 2 | Xác minh thực tế thị trường cho quyết định 2 và 2b — xem §7.2 | Ch.38, 39, 42 |
| 3 | ⚠ Biến tần chuyền hiện **chỉ có `DI_VfdReady`** — không đọc được dòng động cơ, tốc độ thật, hay bit "đang giới hạn dòng". Có thêm kết nối mạng tới biến tần không? Xem lập luận ở Ch.36 mục 36.9 | Ch.36, 40, 55 |
