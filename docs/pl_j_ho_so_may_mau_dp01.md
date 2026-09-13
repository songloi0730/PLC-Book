
# Phụ lục J — Hồ sơ máy mẫu DP-01 đầy đủ

> **Đây là tài liệu tra cứu, không phải chương để đọc tuần tự.**
>
> Mọi ví dụ trong sách từ Chương 8 trở đi dùng chung hồ sơ này. Khi một chương nhắc tới một tag, một
> con số, hay một bước trình tự của DP-01, ⭐ **định nghĩa chính thức nằm ở đây**.

---

> ⚠⚠ **ĐỌC TRƯỚC — bản chất của hồ sơ này**
>
> DP-01 là một cỗ máy **phiếm chỉ**, dựng riêng để dạy học. Nó **không** dựa trên máy, dự án hay
> khách hàng cụ thể nào.
>
> - Số liệu ở đây là **minh hoạ hợp lý**, ⚠ **không phải thông số kiểm định**.
> - Bảng chức năng an toàn ở §6 là **ví dụ dạy học**, ⚠⚠ **không phải kết quả đánh giá rủi ro**.
> - Hồ sơ này **không thay thế** thiết kế của một máy thật. Máy thật cần đánh giá rủi ro riêng do
>   **người có thẩm quyền** thực hiện, và mức an toàn phải xác định từ đánh giá đó — không chép từ
>   sách (Chương 6, 47, 48).
>
> ⭐ **Dùng nó làm khung cho dự án của bạn — không dùng nó làm bản thiết kế.**

---

## J.1 Máy làm gì

Board mạch đi từ máy phía trước sang, được tra một đường keo bảo vệ lên vùng linh kiện, rồi sấy cứng
bằng đèn UV, rồi chuyển sang máy phía sau. Mỗi board có mã 2D riêng — máy đọc mã, hỏi hệ thống quản
lý sản xuất xem board này có được phép làm không và làm theo công thức nào, rồi báo kết quả về sau
khi xong.

```text
 [Máy trước] ──SMEMA──► ┌──────────────── DP-01 ────────────────┐ ──SMEMA──► [Máy sau]
                        │                                        │
                        │  chuyền vào    TRẠM 1        TRẠM 2    │
                        │      ●────────► TRA KEO ────► SẤY UV ──►│
                        │   đọc mã 2D   gantry XY+Z   đèn UV      │
                        │   hỏi MES     van tra keo   cửa chắn    │
                        └────────────────────────────────────────┘
```

### ⭐ Số liệu chốt

| Hạng mục | Giá trị | Dùng ở chương |
|---|---|---|
| ⭐ **Sản lượng mục tiêu** | **300 board/giờ** | 55, 57 |
| ⭐ **Chu kỳ mục tiêu** | **12,0 s/board** | 55, 57 |
| ⭐ **Trạm quyết định nhịp** | ⭐⭐ **Trạm 2 — sấy UV, 6–12 s tuỳ mã hàng** | 55 |
| Kích thước board | **100 × 80 mm** | 32, 37, 55 |
| Vùng làm việc gantry | **X 0–150 · Y 0–120 · Z 0–50 mm** | 37 |
| Trục Z | ⭐ **Servo** (cả X và Y cũng servo) | 29, 37 |
| Đầu đọc mã 2D | **Ethernet** | 42 |
| Bộ điều khiển nhiệt keo | ⭐ **Rời, RS-485 / Modbus RTU** | 33, 35, 38, 39 |
| Thị giác máy | ⚠ **Không có trong DP-01** — nếu cần chỉ **nhận kết quả** (X, Y, góc) | 43 |

> ⚠⚠ **Con số đáng chú ý nhất trong bảng: với mã hàng cần sấy 12 giây, trạm 2 chiếm TRỌN chu kỳ mục
> tiêu** — không còn dư cho chặn, kẹp, nhả. Nghĩa là ở mã hàng đó, DP-01 **không đạt 300 board/giờ**.
>
> ⭐ Đây là **nút cổ chai có thật và tính ra được** — xem Chương 55. Nó được giữ nguyên có chủ ý, không
> "làm đẹp" cho tròn số, vì bài học nằm ở chính chỗ đó.

---

## J.2 Bảng vào/ra đầy đủ

Quy ước đặt tên: `DI_/DO_/AI_/AO_` + vị trí + chức năng. Trạm 1 = tra keo, trạm 2 = sấy UV.

⭐ **Cột "Lát cắt"** cho biết thiết bị đó xuất hiện từ giai đoạn nào của sách — chương thuộc lát cắt
nào chỉ dùng thiết bị của lát cắt đó và các lát cắt trước.

### J.2.1 Ngõ vào số — DI

| Tag | Mô tả | Loại thiết bị | Trạng thái nghỉ | Lát cắt | Chương |
|---|---|---|---|---|---|
| `DI_StartPB` | Nút Start | Nút nhấn *(push button)* NO | 0 | 1 | 15, 25 |
| `DI_StopPB` | Nút Stop | Nút nhấn **NC** | 1 | 1 | 15, 48 |
| `DI_ResetPB` | Nút Reset | Nút nhấn NO | 0 | 1 | 25, 28 |
| `DI_ModeAuto` | Chọn chế độ Auto / Manual | Công tắc xoay 2 vị trí | — | 1 | 28 |
| ⚠ `DI_EStopOK` | Mạch dừng khẩn cấp lành | Tiếp điểm **NC** từ rơ-le an toàn | 1 | 5 | 47, 48 |
| ⚠ `DI_Door1Closed` | Cửa bảo vệ trạm keo đóng & khoá | Công tắc an toàn **NC** | 1 | 5 | 47 |
| ⚠ `DI_Door2Closed` | Cửa bảo vệ trạm UV đóng & khoá | Công tắc an toàn **NC** | 1 | 5 | 47 |
| ⚠ `DI_CurtainOK` | Rèm quang *(light curtain)* không bị cắt | Từ rơ-le an toàn, **NC** | 1 | 5 | 47 |
| `DI_AirOK` | Áp suất khí đạt ngưỡng tối thiểu | Công tắc áp suất NO | 1 khi đủ khí | 1 | 48 |
| `DI_BoardInfeed` | Có board ở đầu chuyền vào | Quang thu-phát, PNP | 0 | 1 | 4, 15 |
| `DI_BoardStn1` | Board đã tới vị trí trạm keo | Quang thu-phát, PNP | 0 | 1 | 4, 18 |
| `DI_BoardStn2` | Board đã tới vị trí trạm UV | Quang thu-phát, PNP | 0 | 1 | 4, 18 |
| `DI_BoardOutfeed` | Board ở đầu chuyền ra | Quang thu-phát, PNP | 0 | 1 | 15 |
| `DI_Stop1Up` / `DI_Stop1Dn` | Chặn trạm 1 đã nâng / đã hạ | Reed xy-lanh, PNP | 0 / 1 | 1 | 5, 26 |
| `DI_Clamp1Up` / `DI_Clamp1Dn` | Bàn nâng kẹp trạm 1 đã lên / xuống | Reed xy-lanh, PNP | 0 / 1 | 1 | 5, 48 |
| `DI_Stop2Up` / `DI_Stop2Dn` | Chặn trạm 2 đã nâng / đã hạ | Reed xy-lanh, PNP | 0 / 1 | 1 | 5, 26 |
| `DI_Clamp2Up` / `DI_Clamp2Dn` | Bàn nâng kẹp trạm 2 đã lên / xuống | Reed xy-lanh, PNP | 0 / 1 | 1 | 5, 48 |
| `DI_ShutterOpen` / `DI_ShutterClosed` | Cửa chắn đèn UV mở / đóng | Reed xy-lanh, PNP | 0 / 1 | 5 | 47 |
| `DI_VfdReady` | Biến tần chuyền sẵn sàng, không lỗi | Tiếp điểm khô NO | 1 | 3 | 36, 51 |
| `DI_IonizerOK` | Bộ khử tĩnh điện hoạt động bình thường | Tiếp điểm khô NO | 1 | 1 | 7, 51 |
| `DI_SmemaInAvail` | Máy trước: **có board sẵn sàng chuyển sang** | Tín hiệu SMEMA, cách ly quang | 0 | 4 | 41 |
| `DI_SmemaOutRdy` | Máy sau: **sẵn sàng nhận board** | Tín hiệu SMEMA, cách ly quang | 0 | 4 | 41 |

> 🔍 **BẪY trung tâm (Ch.4, Ch.15).** `DI_StopPB`, `DI_EStopOK`, `DI_Door1Closed`, `DI_Door2Closed`,
> `DI_CurtainOK` đều là tiếp điểm **NC** — bình thường tín hiệu **có mặt**, và ⭐ **đứt dây làm máy
> dừng**.
>
> Đây là lý do mạch dừng dùng NC: hỏng theo hướng an toàn.

> ⚡ **`DI_IonizerOK` không phải trang trí (Ch.7).** Nếu bộ khử tĩnh điện hỏng mà máy vẫn chạy, board
> hỏng ⚠ **không có triệu chứng tại chỗ** — lỗi chỉ lộ ra ở kiểm cuối, hoặc ở tay khách hàng.
>
> ⭐ Đây là ví dụ trung tâm cho luận điểm: **có những lỗi máy không tự báo được, phải thiết kế để nó
> báo.**

### J.2.2 Ngõ ra số — DO

| Tag | Mô tả | Tải | Kiểu ngõ ra nên dùng | Lát cắt | Chương |
|---|---|---|---|---|---|
| `DO_ConvRun` | Cho phép chuyền chạy (tới biến tần) | Ngõ vào số biến tần | Transistor | 1 | 9, 36 |
| `DO_Stop1Vlv` | Van chặn trạm 1 *(5/2, lò xo về)* | Van điện từ 24 VDC | Transistor + diode dập | 1 | 6, 9 |
| `DO_Clamp1Vlv` | Van nâng kẹp trạm 1 | Van điện từ 24 VDC | Transistor + diode dập | 1 | 6, 9 |
| `DO_Stop2Vlv` | Van chặn trạm 2 | Van điện từ 24 VDC | Transistor + diode dập | 1 | 6, 9 |
| `DO_Clamp2Vlv` | Van nâng kẹp trạm 2 | Van điện từ 24 VDC | Transistor + diode dập | 1 | 6, 9 |
| `DO_DispVlv` | Van tra keo *(dispensing valve)* | Van điện từ tác động nhanh | Transistor | 3 | 9, 37 |
| `DO_SuckBack` | Van hút ngược chống nhỏ giọt | Van chân không | Transistor | 3 | 6 |
| ⚠ `DO_UvLamp` | Bật đèn UV | Contactor qua rơ-le trung gian | Relay | 5 | 9, 47 |
| ⚠ `DO_ShutterVlv` | Van cửa chắn đèn UV | Van điện từ 24 VDC | Transistor + diode dập | 5 | 47 |
| `DO_ExhaustFan` | Quạt hút khí trạm UV | Contactor qua rơ-le trung gian | Relay | 5 | 9 |
| `DO_IonizerEn` | Cho phép bộ khử tĩnh điện | Ngõ vào điều khiển | Transistor | 1 | 7 |
| `DO_LampGreen` / `DO_LampYellow` / `DO_LampRed` | Đèn tháp 3 màu | Đèn 24 VDC | Transistor | 1 | 44 |
| `DO_Buzzer` | Còi báo | Còi 24 VDC | Transistor | 1 | 44 |
| `DO_SmemaOutAvail` | Báo máy sau: **có board sẵn sàng chuyển đi** | Tín hiệu SMEMA, cách ly quang | Transistor | 4 | 41 |
| `DO_SmemaInRdy` | Báo máy trước: **sẵn sàng nhận board** | Tín hiệu SMEMA, cách ly quang | Transistor | 4 | 41 |

### J.2.3 Analog — AI / AO

| Tag | Mô tả | Tín hiệu | Dải kỹ thuật | Lát cắt | Chương |
|---|---|---|---|---|---|
| `AI_AirPress` | Áp suất khí nén cấp máy | 4–20 mA, 2 dây | 0–10 bar | 3 | 31, 32 |
| `AI_GluePress` | Áp suất keo tại đầu tra | 4–20 mA, 2 dây | 0–6 bar | 3 | 31, 32 |
| `AI_UvChamberTemp` | Nhiệt độ buồng sấy — giám sát quá nhiệt | RTD Pt100, 3 dây | 0–150 °C | 3 | 33 |
| ⭐ `AI_UvIntensity` | Cường độ đèn UV đo tại buồng sấy | 0–10 V | 0–200 mW/cm² | 3 | 32, 33, 53 |
| `AO_GluePressSet` | Đặt áp keo *(van điều áp điện tử)* | 0–10 V | 0–6 bar | 3 | 32, 37 |
| `AO_ConvSpeed` | Đặt tốc độ chuyền | 0–10 V | 0–100 % ↔ 0–20 m/phút | 3 | 32, 36 |
| `AO_UvPower` | Đặt công suất đèn UV | 0–10 V | 0–100 % | 3 | 32 |

> ⭐⭐ **`AI_UvIntensity` là tín hiệu đáng chú ý nhất trong bảng, và nó không dùng để điều khiển gì.**
>
> Cường độ đèn UV **giảm dần theo giờ chạy**. Board vẫn "được sấy" nhưng keo **cứng chưa đủ** — và
> không có báo động nào, vì mọi thứ vẫn chạy đúng. Tín hiệu này tồn tại để ⭐ **nhìn thấy sự trôi
> trước khi nó thành hàng lỗi** (Chương 53 mục 53.6).

### J.2.4 Trục & mạng

| Tên | Mô tả | Lát cắt | Chương |
|---|---|---|---|
| `AX_X`, `AX_Y` | Gantry 2 trục mang đầu tra keo — **servo**, chạy theo đường trong công thức | 3 | 37 |
| `AX_Z` | Trục nâng/hạ đầu tra keo — **servo**, độ cao theo công thức | 3 | 37 |
| `NET_HMI` | Màn hình vận hành | 4 | 44 |
| `NET_Scanner` | Đầu đọc mã 2D trên board — **Ethernet** | 4 | 42 |
| `NET_TempCtrl` | Bộ điều khiển nhiệt độ keo rời — **RS-485, Modbus RTU** | 3 | 33, 35, 38, 39 |
| `NET_MES` | Hệ thống quản lý sản xuất — hỏi công thức, báo kết quả | 4 | 42, 45 |
| `NET_Drives` | 3 servo drive qua Ethernet công nghiệp | 3 | 40 |
| `NET_IoLink` | IO-Link master cho cảm biến thông minh | 2 | 12 |

---

## J.3 Đặc tả trình tự

⭐ **Điều kiện vào Auto:** đã về gốc, không có lỗi, cả hai cửa đóng, rèm quang không bị cắt, khí đủ,
bộ khử tĩnh điện OK, chọn chế độ Auto, và MES kết nối được (hoặc đã bật chế độ chạy tạm không MES).

### J.3.1 Trạm 1 — Tra keo

| Bước | Hành động | Điều kiện chuyển tiếp | Hết giờ |
|---|---|---|---|
| S1.00 | Chờ board vào | `DI_BoardStn1` = 1 | — |
| S1.10 | Nâng chặn, dừng chuyền tại trạm 1 | `DI_Stop1Up` = 1 | 1 s |
| S1.20 | Đọc mã 2D trên board | Nhận được chuỗi mã hợp lệ | 3 s |
| S1.30 | Hỏi MES: board này có được làm không, công thức nào | Nhận phản hồi | 5 s |
| S1.40 | Nâng kẹp board | `DI_Clamp1Up` = 1 | 2 s |
| S1.50 | Kiểm điều kiện keo: áp keo và nhiệt độ trong dải công thức | Cả hai đạt | 30 s |
| S1.60 | Gantry chạy theo đường tra keo trong công thức | Hoàn tất đường | 60 s |
| S1.70 | Hút ngược, nâng trục Z về vị trí an toàn | `AX_Z` tại vị trí chờ | 3 s |
| S1.80 | Hạ kẹp | `DI_Clamp1Dn` = 1 | 2 s |
| ⭐ S1.90 | Hạ chặn, chuyển board sang trạm 2 | `DI_BoardStn1` = 0 ⭐ **và trạm 2 rỗng** | 5 s |
| → S1.00 | Ghi log, quay lại chờ board | | |

### J.3.2 Trạm 2 — Sấy UV

| Bước | Hành động | Điều kiện chuyển tiếp | Hết giờ |
|---|---|---|---|
| S2.00 | Chờ board vào | `DI_BoardStn2` = 1 | — |
| S2.10 | Nâng chặn | `DI_Stop2Up` = 1 | 1 s |
| S2.20 | Nâng kẹp | `DI_Clamp2Up` = 1 | 2 s |
| S2.30 | Bật quạt hút, mở cửa chắn UV | `DI_ShutterOpen` = 1 | 2 s |
| ⭐ S2.40 | Sấy — giữ đủ thời gian theo công thức | Hết thời gian ⭐ **và cường độ UV luôn trong dải** | — |
| S2.50 | Đóng cửa chắn UV | `DI_ShutterClosed` = 1 | 2 s |
| S2.60 | Hạ kẹp, hạ chặn | `DI_Clamp2Dn` = 1, `DI_Stop2Dn` = 1 | 2 s |
| S2.70 | Chuyển board ra, bắt tay SMEMA với máy sau | `DI_BoardOutfeed` = 0 | 10 s |
| S2.80 | Báo kết quả về MES, tăng bộ đếm sản lượng | Đã gửi | 5 s |
| → S2.00 | Quay lại chờ board | | |

> 🔍 **BẪY trung tâm (Ch.17, Ch.48).** Mọi bước chờ cơ cấu ở trên chuyển tiếp bằng ⭐ **tín hiệu phản
> hồi thật** (reed xy-lanh, cảm biến board); cột "hết giờ" chỉ để **báo lỗi**.
>
> ⚠ Phiên bản sai — mà người mới hay viết — là chuyển tiếp bằng chính bộ định thời: *"chờ 2 giây chắc
> kẹp xong rồi"*. Bộ định thời **không biết khi cơ cấu không tới nơi**.

> ⭐⭐ **Điểm dạy pipeline (Ch.26–27).** S1.90 chỉ chuyển tiếp khi **trạm 2 rỗng**. Hai trạm chạy song
> song trên hai board khác nhau; ràng buộc duy nhất giữa chúng là **chỗ trống**.
>
> Đây là bài toán đồng bộ giữa trạm — và là chỗ dạy vì sao **không được chờ bận** *(busy-wait)* giữa
> hai trình tự.

---

## J.4 Mô hình trạng thái máy

```text
Uninitialized ──► Homing ──► Idle ──► Running ──► (hai trạm chạy song song)
                    │          │         │
                    │          │         ├──► Hold  (giữ nguyên vị trí, board ở nguyên chỗ)
                    │          │         │
                    └──────────┴─────────┴──► Alarm ──► Reset ──► Homing
```

Mỗi trạm có máy trạng thái con riêng; ⭐ **máy trạng thái tổng quyết định cả hai được phép chạy hay
không**.

### ⚠⚠ Điểm khó cố ý — về gốc từ trạng thái xấu nhất

Nếu máy vào **Alarm** đúng lúc:

- board A đang **bị kẹp ở trạm 1**, đầu tra keo đang ở giữa đường tra, trục Z đang hạ thấp, **và**
- board B đang **trong buồng UV** với cửa chắn đang mở, đèn đang bật —

thì trình tự về gốc phải theo **đúng thứ tự này**:

| # | Việc | ⚠ Vì sao thứ tự này |
|---|---|---|
| 1 | ⚠⚠ **Tắt đèn UV và đóng cửa chắn** | ⭐ **Người vào máy trước khi che được nguồn UV là tai nạn** |
| 2 | ⚠ **Nâng trục Z lên vị trí an toàn** trước khi cho gantry XY chạy | Nếu không, đầu tra keo **quét ngang mặt board đang kẹp** — phá cả board lẫn đầu keo |
| 3 | Chỉ **nhả kẹp sau khi** trục Z đã lên | Nhả trước làm board dịch trong khi đầu keo còn ở gần |
| 4 | ⭐ Board dở dang **đánh dấu NG và báo MES** | ⚠ Không được lẫn vào hàng tốt |

> ⭐⭐ **Đây là ví dụ trung tâm cho luận điểm "về gốc là bài toán khó nhất thực tế" (Ch.28).**
>
> Thứ tự trên là **kết quả của phân tích va chạm và mối nguy**, không phải thứ tự tuỳ ý. Đảo hai bước
> bất kỳ đều gây hậu quả — và hậu quả của việc đảo bước 1 là hậu quả cho **người**, không phải cho
> sản phẩm.

---

## J.5 Công thức sản phẩm

Mỗi mã hàng có một công thức. ⭐ **Đây là lý do máy điện tử bắt buộc phải tách tham số khỏi logic:**
cùng một máy chạy nhiều mã hàng trong một ca.

| Tham số | Đơn vị | Dải hợp lệ | Dùng ở bước |
|---|---|---|---|
| Đường tra keo (danh sách điểm X, Y, Z) | mm | trong vùng làm việc | S1.60 |
| Áp keo đặt | bar | 0,5 – 5,0 | S1.50 |
| Nhiệt độ keo đặt | °C | 20 – 60 | S1.50 |
| Dung sai nhiệt độ | °C | 0,5 – 5,0 | S1.50 |
| Tốc độ chạy đường tra | mm/s | 5 – 100 | S1.60 |
| ⭐ **Thời gian sấy UV** | s | **5 – 120** | S2.40 |
| Công suất đèn UV | % | 30 – 100 | S2.40 |
| Ngưỡng cường độ UV tối thiểu | mW/cm² | 20 – 180 | S2.40 |
| Tốc độ chuyền | % | 20 – 100 | mọi bước chuyền |

> ⚠⚠ **Kiểm tra hợp lệ là bắt buộc (Ch.32).** Nếu công thức tải từ MES có nhiệt độ đặt 600 °C do lỗi
> nhập liệu, máy phải **từ chối và báo lỗi**, không được nhận.
>
> ⭐ Cột "dải hợp lệ" chính là hàng rào đó — và nó thuộc về **chương trình PLC**, không phải thuộc về
> MES. Máy phải tự bảo vệ mình khỏi dữ liệu sai từ bên ngoài.

---

## J.6 ⚠ Chức năng an toàn

| SF | Mối nguy | Biện pháp | Ghi chú |
|---|---|---|---|
| **SF1** | Dừng khẩn cấp mọi chuyển động | E-Stop 2 kênh → rơ-le an toàn → cắt nguồn van + STO cho 3 servo + ngắt contactor đèn UV & quạt | ⚠⚠ **Không đi qua logic PLC thường** (Ch.47) |
| ⭐ **SF2** | ⚠⚠ **Bức xạ UV chiếu vào mắt/da người** | Cửa chắn cơ khí + khoá cửa buồng UV; đèn chỉ bật khi **cửa đóng và khoá**; mở cửa → ⭐ **cắt nguồn đèn qua mạch an toàn**, không qua lệnh PLC | ⚠ Mối nguy vật lý thật, **không có triệu chứng tức thời** — người bị chiếu thường không biết |
| **SF3** | Kẹp tay khi bàn nâng kẹp hoạt động | Cửa bảo vệ có khoá tại cả hai trạm | Khoá kiểu giữ tới khi an toàn |
| **SF4** | Với tay vào qua cửa chuyền vào/ra | Rèm quang tại hai cửa chuyền | ⚠ Cần cân nhắc muting để board đi qua mà không dừng máy (Ch.47) |
| **SF5** | Máy khởi động bất ngờ sau khi khôi phục nguồn | ⭐ **Yêu cầu Reset có chủ ý**; không tự vào Running | Ch.48 |
| ⭐ **SF6** | Mất khí nén khi board đang bị kẹp | Trạng thái an toàn cho van kẹp: ⭐ **GIỮ kẹp**, không nhả — ⚠ **phải giữ bằng van một chiều điều khiển hoặc khoá cần**, không phải bằng van hai cuộn | ⭐ Quyết định thiết kế **có lý do** (Ch.48); cơ chế ở Ch.6 mục 6.3 |
| **SF7** | Đầu tra keo nóng gây bỏng | Che chắn cơ khí + cảnh báo; ngắt gia nhiệt khi mở cửa | Ch.47 |

> ⭐⭐ **SF6 đáng dừng lại suy nghĩ.** "Trạng thái an toàn" thường được hiểu là "về vị trí nghỉ" —
> nhưng ở đây nhả kẹp khi mất khí sẽ **thả board rơi**, và có thể thả nó vào vùng đầu tra keo đang ở
> gần.
>
> ⭐ Trạng thái an toàn là **kết quả của phân tích**, không phải một mặc định. Với mỗi cơ cấu, câu hỏi
> là: *"mất năng lượng lúc này thì điều gì an toàn hơn?"* — và câu trả lời khác nhau giữa các cơ cấu
> trên cùng một máy.

> ⚠⚠ **Bảng này là ví dụ dạy học, KHÔNG phải kết quả đánh giá rủi ro.**
>
> Máy thật cần đánh giá rủi ro riêng bởi **người có thẩm quyền**, và mức hiệu năng / mức toàn vẹn phải
> xác định **từ đánh giá đó** — không chép từ sách. Xem Chương 6, 47, 48.

---

## J.7 Bóc lớp theo lát cắt

⭐ **Quy tắc:** chương thuộc lát cắt nào thì **chỉ dùng thiết bị của lát cắt đó và các lát cắt trước**.

| Lát cắt | Chỉ dùng | Chương |
|---|---|---|
| **1 — thuần rời rạc** | Chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp | 8–22 |
| **2 — thêm thiết kế** | + máy trạng thái 2 trạm, trình tự song song, công thức sản phẩm | 23–30 |
| **3 — thêm analog & trục** | + áp keo, nhiệt độ, cường độ UV, gantry XY/Z, biến tần | 31–37 |
| **4 — thêm mạng** | + mã 2D, MES, SMEMA, HMI | 38–46 |
| **5 — đầy đủ** | + mạch an toàn, chạy thử, chẩn đoán, vận hành | 47–58 |

> ⭐ **Vì sao bóc lớp:** để Chương 15 dạy Ladder mà không cần bạn đã biết servo. Mỗi khái niệm xuất
> hiện đúng lúc bạn đủ nền để hiểu nó — và cùng một cỗ máy lớn dần theo bạn.

---

## J.8 Các phép tính đã thực hiện trên DP-01

Gom lại đây vì chúng rải rác trong sách và ⭐ **đều là loại phép tính phải làm TRƯỚC KHI MUA**.

| Phép tính | Kết quả | Chương |
|---|---|---|
| Chu kỳ từ sản lượng | 3600 ÷ 300 = **12,0 s/board** | 55 |
| ⭐ **Nút cổ chai** | Trạm 2 (6–12 s) — ⚠ **12 s thì chỉ vừa đủ** | 55 |
| Số lần đóng cắt van/năm | **2,88 triệu lần** (2 ca × 8 h × 300 ngày) | 9 mục 9.3 |
| ⭐ **Số lần uốn cáp xích gantry/năm** | **1,44 triệu lần** | 49 mục 49.7 |
| Ngưỡng nhắc bảo trì van | 0,7 × tuổi thọ datasheet | 53 mục 53.5 |
| Công suất nguồn 24 V | Bước nhiều tải nhất × 1,3–1,5 | 8 mục 8.7 |
| Vùng làm việc gantry | Board 100 × 80 + biên gá → **X 150 · Y 120 · Z 50 mm** | 37 |

> ⭐⭐ **Bảy phép tính, tất cả cùng một dạng: đếm số lần, rồi so với con số trong datasheet.**
>
> Chúng đều đơn giản, đều mất vài phút, và đều phải làm **trước khi mua** — vì phát hiện sau khi máy
> chạy nghĩa là thay thiết bị và đấu lại dây.

---

## J.9 ⚠ Hạng mục còn treo

Ba mục sau chưa chốt. Chúng được ghi lại ở đây thay vì giấu đi, vì ⭐ **biết cái gì chưa chắc chắn là
một phần của hồ sơ kỹ thuật**.

| # | Hạng mục | Ảnh hưởng |
|---|---|---|
| 1 | ⚠ `AI_UvIntensity` đang là **0–10 V**. Suy giảm cường độ UV là lỗi "máy không tự phát hiện được" — có nên đổi sang **4–20 mA** để phân biệt được đứt dây? | Ch.31, 32, 48 |
| 2 | ⚠ **Xác minh thực tế thị trường**: đầu đọc mã 2D hiện nay dùng giao tiếp gì; bộ điều khiển nhiệt độ rời có còn phổ biến không | Ch.38, 39, 42 |
| 3 | ⚠ Biến tần chuyền hiện **chỉ có `DI_VfdReady`** — không đọc được dòng động cơ, tốc độ thật, hay bit "đang giới hạn dòng". Có nên thêm kết nối mạng tới biến tần? | Ch.36, 40, 55 |

> ⭐ **Mục 1 và 3 là cùng một câu hỏi ở hai chỗ: "máy có tự biết khi một thứ đang xấu đi không?"**
>
> Với 0–10 V, đứt dây cho 0 V — trông y hệt "đèn đã tắt", và máy không phân biệt được. Với 4–20 mA,
> đứt dây cho 0 mA, nằm **ngoài dải hợp lệ** — máy biết ngay đó là lỗi cảm biến, không phải giá trị
> đo. Xem Chương 31.
>
> Đây là loại quyết định rẻ ở giai đoạn thiết kế và đắt sau khi máy chạy — đúng chủ đề của Chương 57
> mục 57.11.

---

## J.10 Dẫn về đâu

| Bạn cần | Đọc |
|---|---|
| Ráp toàn bộ thành một dự án theo thứ tự | ⭐ **Chương 57** |
| Bảng biểu mẫu trống để dùng cho máy của bạn | **Phụ lục C** |
| Công thức tính, kèm điều kiện áp dụng | **Phụ lục K** |
| ⭐ **Mẫu code cho mạch thường dùng** (tự giữ, dừng khẩn cấp, tạm dừng, tuần hoàn, servo…) | **Phụ lục L** |
| Tra theo triệu chứng khi máy lỗi | **Phụ lục E** |
| Thuật ngữ Việt–Anh | **Phụ lục F** |

> ⚠⚠ **Nhắc lại lần cuối.** DP-01 là máy dạy học. Dùng cấu trúc của hồ sơ này làm khung cho dự án
> thật là đúng mục đích. ⚠ **Chép số liệu và bảng an toàn của nó vào một máy thật là sai mục đích** —
> máy thật cần đánh giá rủi ro riêng, do người có thẩm quyền thực hiện.
