# Chương 32 — Từ giá trị thô tới đại lượng kỹ thuật

> **Lát cắt máy mẫu:** 3 — thêm analog (áp suất, nhiệt độ, cường độ UV) và trục gantry XY+Z servo.

---

## 32.1 Bài toán: con số đúng, đơn vị sai

Kỹ sư viết đoạn quy đổi áp keo, chạy thử, thấy màn hình hiện **4,2** — đúng bằng đồng hồ cơ khí trên
đường ống. Xong việc.

Ba tuần sau, đổi sang mã hàng cần áp keo cao hơn. Người vận hành nhập **5,5** vào công thức. Máy chạy,
nhưng đường keo mỏng bất thường và tỉ lệ lỗi tăng.

Nguyên nhân: chương trình quy đổi giá trị thô sang **đơn vị 0,1 bar** — con số `42` trong bộ nhớ nghĩa
là 4,2 bar. Nhưng ô nhập công thức nhận thẳng con số người vận hành gõ. Nhập `5,5` vào một trường số
nguyên đơn vị 0,1 bar cho ra **5**, tức là **0,5 bar**.

Không có lỗi nào. Không có cảnh báo nào. Con số vẫn "trông hợp lý".

Chương này về việc biến giá trị thô thành đại lượng kỹ thuật — và về những chỗ phép biến đổi đó âm
thầm sai.

---

## 32.2 Module analog trả về cái gì

Module analog không trả về "4,2 bar". Nó trả về một **số nguyên** — kết quả của **bộ chuyển đổi
tương tự–số** *(analogue-to-digital converter, ADC)*.

```text
   Cảm biến ──► 4–20 mA ──► [ ADC ] ──► số nguyên thô ──► [ CHƯƠNG TRÌNH ] ──► 4,2 bar
                              ↑                              ↑
                         phần cứng                    việc của chương này
```

Ánh xạ giữa dòng và số thô do **module** quy định. Ví dụ điển hình cho module 16 bit:

| Dòng | Giá trị thô |
|---|---|
| 4 mA | 0 |
| 20 mA | 27 648 |
| ⚠ Dưới 4 mA | Số **âm** |
| ⚠ Trên 20 mA | Vượt 27 648 |

> ⚠ **Con số 27 648 là ví dụ, không phải hằng số phổ quát.**
> Mỗi hãng — thậm chí mỗi dòng module — dùng một cách ánh xạ khác nhau. Có module cho 0–32 767, có
> module cho 0–4095, có module trả thẳng giá trị theo đơn vị đã đặt.
>
> ⭐ **Đây là con số đầu tiên phải tra trong datasheet module**, trước khi viết dòng quy đổi nào. Lấy
> nhầm con số này thì mọi phép đo sai theo tỉ lệ, và sai một cách **trông hợp lý**.

Hai hàng cuối bảng là quà tặng của chuẩn 4–20 mA (Chương 31): vùng ngoài dải **biểu diễn được**, nên
chương trình phân biệt được lỗi mạch với giá trị thật.

---

## 32.3 ⭐ Độ phân giải — phép đo của bạn có ý nghĩa tới đâu

### Từ số bit ra bước nhỏ nhất

**Độ phân giải** *(resolution)* là **bước nhỏ nhất** mà phép đo phân biệt được. Nó suy ra từ số bit
của ADC và dải đo:

```text
Bước nhỏ nhất  =  (dải kỹ thuật)  /  (số bước của ADC)
```

Với `AI_GluePress` của DP-01 — dải **0–6 bar**, module cho 0–27 648 bước:

```text
6 bar / 27 648 = 0,000217 bar/bước  ≈  0,0002 bar
```

Rất mịn. Nhưng đừng vội mừng — xem mục sau.

### ⚠ Độ phân giải không phải độ chính xác

Đây là nhầm lẫn phổ biến nhất về analog.

| | **Độ phân giải** *(resolution)* | **Độ chính xác** *(accuracy)* |
|---|---|---|
| Trả lời | Phân biệt được bước nhỏ tới đâu | Giá trị đọc **gần sự thật** tới đâu |
| Quyết định bởi | Số bit ADC và dải đo | **Cảm biến**, nhiễu, hiệu chuẩn, nhiệt độ môi trường |
| Cải thiện bằng | Module nhiều bit hơn | Cảm biến tốt hơn, hiệu chuẩn, chống nhiễu |

> ⚠⚠ **Một cảm biến áp suất sai số ±1 % dải, đọc qua ADC 16 bit, KHÔNG cho bạn phép đo chính xác tới
> 0,0002 bar.**
>
> Với dải 0–6 bar, sai số ±1 % là **±0,06 bar**. Mọi chữ số sau đó là **rác** — chúng ổn định và
> trông thuyết phục, nhưng không mang thông tin về thực tế.
>
> Hiển thị `4,2038 bar` khi cảm biến chỉ đảm bảo ±0,06 bar là **nói dối người vận hành**. Hiển thị
> `4,2 bar` là trung thực.

> 💡 **Quy tắc thực dụng:** số chữ số hiển thị phải khớp với **sai số của cảm biến**, không khớp với
> số bit của ADC. Tra sai số trong datasheet cảm biến, rồi làm tròn hiển thị cho tương xứng.

### Chọn dải đo cho đủ phân giải

Chiều ngược lại cũng quan trọng: **dải đo quá rộng làm mất độ phân giải ở vùng bạn thật sự quan tâm**.

Ví dụ: bạn cần đo áp keo trong khoảng 3–5 bar với bước 0,01 bar.

| Chọn cảm biến dải | Bước ADC (16 bit) | Đủ không |
|---|---|---|
| 0–6 bar | 0,0002 bar | ✅ Thừa sức |
| 0–100 bar | 0,0036 bar | ✅ Vẫn đủ về ADC — nhưng ⚠ **sai số cảm biến** ±1 % của 100 bar là **±1 bar** |
| 0–250 bar | 0,009 bar | ❌ Sai số ±2,5 bar — vô dụng cho bài toán này |

> ⭐ **Bài học: chọn cảm biến có dải VỪA ĐỦ bao phủ vùng làm việc.**
> Sai số thường tính theo **phần trăm của dải đo**, nên dải càng rộng thì sai số tuyệt đối càng lớn.
> Một cảm biến 0–250 bar dùng để đo 4 bar là phép đo gần như vô nghĩa — dù nó "đo được".
>
> Đây là quyết định **lúc mua cảm biến**, không sửa được bằng phần mềm.

---

## 32.4 Công thức quy đổi thang

### Công thức tuyến tính

Quy đổi từ giá trị thô sang đại lượng kỹ thuật là một phép nội suy tuyến tính:

```text
              (thô − thô_min)
GT_kỹ_thuật = ─────────────── × (KT_max − KT_min)  +  KT_min
              (thô_max − thô_min)
```

Với `AI_GluePress`: thô 0–27 648 ↔ kỹ thuật 0–6 bar.

### ⚠ Viết bằng số nguyên — thứ tự phép tính quyết định

Theo quy tắc ở Chương 19 mục 19.5, dùng **số nguyên đơn vị nhỏ** thay cho số thực. Đơn vị chọn:
**0,01 bar** — đủ mịn so với sai số cảm biến, và cho số tròn.

```iecst
VAR CONSTANT
    RAW_MIN      : DINT := 0;        // ứng 4 mA
    RAW_MAX      : DINT := 27648;    // ứng 20 mA — ⚠ TRA DATASHEET MODULE
    PRESS_MIN_X100 : DINT := 0;      //   0,00 bar
    PRESS_MAX_X100 : DINT := 600;    //   6,00 bar
END_VAR

// ⭐ NHÂN TRƯỚC, CHIA SAU — và dùng DINT để kết quả trung gian không tràn
GluePressX100 := (DINT_raw - RAW_MIN) * (PRESS_MAX_X100 - PRESS_MIN_X100)
                 / (RAW_MAX - RAW_MIN)
                 + PRESS_MIN_X100;
```

Ba điều bắt buộc, cả ba đã gặp ở Chương 19:

- ⭐ **Nhân trước, chia sau.** Chia trước thì phép chia số nguyên cắt hết phần lẻ và kết quả chỉ còn
  0 hoặc giá trị đầu dải (Chương 19, mục 19.4).
- ⭐ **Dùng `DINT`.** Kết quả trung gian `27648 × 600 ≈ 16,6 triệu` vượt xa dải `INT` (Chương 19,
  mục 19.5). Đây là chỗ tràn số kinh điển của quy đổi thang.
- ⭐ **Đơn vị nằm trong tên biến** — `GluePressX100`, không phải `GluePress` (Chương 11, mục 11.3).

> ⚠⚠ **Cỗ máy ở mục 32.1 chính là hậu quả của việc quên gạch đầu dòng thứ ba.**
> Biến trong bộ nhớ mang đơn vị 0,1 bar; ô nhập công thức nhận đơn vị bar. Không ai nhận ra vì tên
> biến không nói gì.
>
> Quy tắc: **mọi biến mang đơn vị phải có đơn vị trong tên**, và **mọi chỗ nhập liệu phải ghi rõ đơn
> vị trên màn hình** (Chương 44). Hai việc, không phải một.

### Quy đổi ngược cho ngõ ra

Ngõ ra analog đi theo chiều ngược lại — từ đại lượng kỹ thuật sang giá trị thô:

```iecst
// AO_ConvSpeed: 0–100 % ↔ thô 0–27 648
RawConvSpeed := (ConvSpeedPct * RAW_MAX) / 100;
```

> ⚠ **Luôn kẹp giá trị trước khi ghi ra ngõ ra analog.**
> Một giá trị vượt dải — do tính toán sai, do công thức chưa nạp, do người vận hành nhập nhầm — có
> thể làm module báo lỗi, hoặc tệ hơn, làm thiết bị nhận hiểu thành một lệnh vô lý.
>
> ```iecst
> IF ConvSpeedPct < 0   THEN ConvSpeedPct := 0;   END_IF;
> IF ConvSpeedPct > 100 THEN ConvSpeedPct := 100; END_IF;
> ```

---

## 32.5 ⭐ Phát hiện ngoài dải

Chương 31 mục 31.3 đã nêu nguyên tắc. Ở đây là cách hiện thực đầy đủ, **trước** phép quy đổi.

```iecst
VAR CONSTANT
    // ⚠ TRA DATASHEET — ngưỡng thô ứng với các mức dòng cần phân biệt
    RAW_WIRE_BREAK : DINT := -2000;    // dưới ~3,6 mA
    RAW_OVER_RANGE : DINT := 29000;    // trên ~21 mA
END_VAR

IF RawGluePress < RAW_WIRE_BREAK THEN
    M_GluePressFault := TRUE;
    M_GluePressFaultCode := 1;                 // đứt dây / mất nguồn cảm biến
ELSIF RawGluePress > RAW_OVER_RANGE THEN
    M_GluePressFault := TRUE;
    M_GluePressFaultCode := 2;                 // chập, hoặc cảm biến báo lỗi
ELSE
    M_GluePressFault := FALSE;
    M_GluePressFaultCode := 0;
    GluePressX100 := ...;                      // ⭐ CHỈ quy đổi khi hợp lệ
END_IF;
```

Ba điểm thiết kế:

- **Quy đổi nằm trong nhánh hợp lệ.** Khi tín hiệu lỗi, `GluePressX100` **giữ giá trị cũ** — nhưng
  ⚠ giá trị cũ đó **không được dùng cho điều khiển** (Chương 31, mục 31.3). Cờ lỗi là thứ quyết định,
  không phải giá trị.
- **Mã lý do riêng cho từng loại lỗi.** "Đứt dây" và "chập" dẫn tới hai hướng kiểm tra khác nhau —
  nói rõ tiết kiệm thời gian cho người sửa (Chương 29, mục 29.4).
- ⭐ **Nếu module có bit trạng thái kênh, dùng nó thay vì tự so ngưỡng** (Chương 31, mục 31.8). Đoạn
  trên là phương án nền.

---

## 32.6 Lọc — và cái giá của nó

Giá trị analog **luôn dao động**: nhiễu điện, dao động thật của quá trình, sai số lượng tử của ADC.
Dao động đó làm màn hình nhảy số và làm điều kiện so ngưỡng nhấp nháy.

### Hai kiểu lọc

**Lọc trung bình trượt** *(moving average)* — giữ N mẫu gần nhất, lấy trung bình:

```iecst
// Trung bình 8 mẫu — chọn luỹ thừa của 2 để chia bằng phép dịch bit, rẻ hơn
SumBuf := SumBuf - Buf[Idx] + GluePressX100;
Buf[Idx] := GluePressX100;
Idx := (Idx + 1) MOD 8;
GluePressFiltX100 := SumBuf / 8;
```

**Lọc số một bậc** *(IIR / exponential filter)* — gọn hơn, chỉ giữ một giá trị:

```iecst
// K trong 1..100: K nhỏ = lọc mạnh, đáp ứng chậm
GluePressFiltX100 := GluePressFiltX100
                   + (K * (GluePressX100 - GluePressFiltX100)) / 100;
```

| | Trung bình trượt | Lọc IIR một bậc |
|---|---|---|
| Bộ nhớ | N giá trị | ⭐ **Một** giá trị |
| Chỉnh độ mạnh | Đổi N | Đổi hệ số K |
| Đáp ứng với bước nhảy | Tuyến tính, xong sau N mẫu | Tiệm cận, không bao giờ tới hẳn |
| ⚠ Nhược | Tốn bộ nhớ khi N lớn | Khó tính chính xác độ trễ |

### ⚠⚠ Cái giá: độ trễ

> **Lọc càng mạnh thì giá trị đọc được càng CHẬM so với thực tế.**
>
> Đây không phải chi tiết nhỏ. Nếu bạn lọc mạnh một tín hiệu áp suất rồi dùng nó làm điều kiện an
> toàn, thì khi áp tụt thật, chương trình **biết muộn** — muộn đúng bằng độ trễ của bộ lọc.

Ba quy tắc:

- **Lọc để hiển thị thì lọc mạnh được** — người đọc không cần thấy số nhảy.
- ⚠ **Lọc để điều khiển thì lọc nhẹ** — độ trễ vào thẳng vòng điều khiển, gây dao động (Chương 35).
- ⚠⚠ **Điều kiện an toàn và điều kiện phát hiện sự cố: lọc rất nhẹ hoặc không lọc.** Nếu cần chống
  báo giả, dùng **timer xác nhận** thay vì lọc — nó cho bạn kiểm soát rõ ràng về thời gian, và bạn
  biết chính xác mình đang chấp nhận trễ bao lâu (Chương 17, mục 17.4).

> 💡 **Gợi ý thực dụng:** giữ **hai** biến — một thô để điều khiển và phát hiện sự cố, một đã lọc để
> hiển thị và ghi log. Chúng phục vụ hai mục đích khác nhau, không có lý do gì phải dùng chung.

---

## 32.6b ⭐⭐ Giá trị bạn đang đọc luôn CŨ HƠN bạn tưởng — cộng đủ ba khoản

Mục trên nói bộ lọc gây trễ. ⚠ Nhưng bộ lọc chỉ là **một** khoản. Thời gian từ lúc đại lượng thật đổi
tới lúc chương trình **nhìn thấy** giá trị mới là **tổng của ba khoản**:

| # | Khoản | Ghi chú |
|:-:|---|---|
| 1 | ⭐ **Thời gian đáp ứng của cảm biến** | ⚠⚠ Thường là khoản **lớn nhất** — cảm biến nhiệt độ rất chậm (Chương 33) |
| 2 | ⭐ **Thời gian cập nhật của module analog** | Bao gồm **trễ do lọc** của chính module (mục 32.6) |
| 3 | **Chu kỳ quét của chương trình** | Chương 10 |

> ⭐⭐ **Cộng đủ ba khoản trước khi kết luận "hệ đáp ứng chậm".**
>
> Người ta hay đi tối ưu chương trình — khoản **nhỏ nhất** trong ba — trong khi ⚠ vấn đề nằm ở cảm
> biến hoặc ở cấu hình lọc của module.
>
> ⚡ Và nhớ rằng ⭐ **bộ lọc phần mềm bạn tự viết là khoản THỨ TƯ**, cộng thêm vào ba khoản trên.

### ⚠ Hai chỗ dễ hiểu sai về tốc độ module

**Một — thời gian một KÊNH khác thời gian cả MODULE**

| Đại lượng | Nghĩa |
|---|---|
| Thời gian quét **một kênh** | Đọc xong một ngõ vào |
| ⭐ **Thời gian chu kỳ của cả module** | Đọc hết **mọi** kênh rồi quay lại kênh đầu |

> ⚠⚠ **Và đây là chỗ phản trực giác: thời gian chu kỳ của module thường KHÔNG giảm khi bạn dùng ít
> kênh hơn.**
>
> ⭐ Module vẫn quét đủ chu kỳ của nó, kể cả với các kênh **không dùng**. Nên mẹo *"chỉ đấu 2 trong 8
> kênh cho nhanh"* ⚠ **không có tác dụng** — trừ khi tài liệu của đúng module đó nói khác.
>
> ⭐ **Muốn nhanh hơn thì phải đổi module**, không phải bỏ bớt kênh.

**Hai — ⚠ khi PLC vừa đọc analog vừa chạy PID**

Với vòng điều khiển (Chương 35), tổng trễ ở trên **đi thẳng vào chất lượng điều khiển**. ⭐ Nếu module
quá chậm so với quá trình, có **hai** đường:

| Cách | Khi nào chọn |
|---|---|
| ⭐ **Đổi sang module analog nhanh hơn** | Khi phần còn lại của thiết kế vẫn hợp |
| ⭐⭐ **Dùng bộ điều khiển chuyên dụng bên ngoài**, PLC chỉ **đặt điểm đặt** cho nó | Khi quá trình nhanh hơn hẳn khả năng của PLC |

> ⚡ Đường thứ hai chính là kiến trúc của bộ điều khiển nhiệt độ rời trên máy mẫu (Chương 38, mục
> 38.11): ⭐ **PLC không điều khiển vòng — nó chỉ ra lệnh và giám sát.**

---

## 32.7 Vùng chết — chống dao động quanh ngưỡng

Đã gặp ở Chương 19 mục 19.3 dưới tên **trễ** *(hysteresis)*; với analog nó là công cụ bắt buộc.

Giá trị dao động quanh đúng ngưỡng làm bit kết quả nhấp nháy — mỗi lần nhấp là một lần báo động rồi
hết báo động. Với hệ cảnh báo, đây là cách nhanh nhất để người vận hành ngừng tin vào nó
(Chương 48, mục 48.6).

```iecst
// Cảnh báo áp keo thấp: bật ở 3,50 bar, chỉ tắt khi đã lên trên 3,70
IF GluePressX100 < 350 THEN
    M_GluePressLow := TRUE;
ELSIF GluePressX100 > 370 THEN
    M_GluePressLow := FALSE;
END_IF;                          // giữa 350 và 370: GIỮ NGUYÊN
```

> ⭐ **Nhánh `ELSIF` không có `ELSE` là cố ý.** Vùng ở giữa **không đổi gì cả** — đó chính là vùng
> chết. Thêm `ELSE` vào là phá mất cơ chế.

Chọn độ rộng vùng chết:

| Quá hẹp | Quá rộng |
|---|---|
| Vẫn nhấp nháy | Phản ứng muộn; giá trị phải sai khá nhiều mới báo |
| | ⚠ Với cảnh báo an toàn, muộn là vấn đề |

Quy tắc thực dụng: **rộng hơn biên độ dao động bình thường của tín hiệu**. Muốn biết biên độ đó thì
**đo** — ghi lại giá trị trong vài phút khi máy chạy bình thường, xem nó dao động bao nhiêu.

---

## 32.8 Hiệu chuẩn — và nó **không** phải cái gì

### Hai khái niệm bị lẫn

| | **Đặt dải đo** *(ranging)* | **Hiệu chuẩn** *(calibration)* |
|---|---|---|
| Làm gì | Khai báo cho hệ biết 4 mA ứng bao nhiêu, 20 mA ứng bao nhiêu | So sánh phép đo với một **chuẩn đã biết** và chỉnh cho khớp |
| Cần gì | Chỉ cần datasheet | ⭐ **Thiết bị chuẩn** có độ chính xác cao hơn |
| Kết quả | Con số quy đổi đúng theo khai báo | Phép đo **đúng với thực tế** |
| Làm ở đâu | Trong chương trình hoặc cấu hình module | Trên cảm biến hoặc trong chương trình, với thiết bị chuẩn |

> ⚠⚠ **Đổi con số trong công thức quy đổi KHÔNG phải hiệu chuẩn.**
> Nếu đồng hồ chuẩn chỉ 4,0 bar mà PLC hiện 4,3 bar, bạn có thể sửa hệ số cho nó hiện 4,0. Nhưng bạn
> **chưa biết cái nào đúng** — có thể cảm biến lệch, có thể đồng hồ chuẩn lệch, có thể cả hai.
>
> Hiệu chuẩn thật đòi hỏi một **chuẩn có độ chính xác cao hơn hẳn** và có **vết truy nguyên**. Việc
> chỉnh cho hai con số khớp nhau mà không có chuẩn chỉ là **làm cho chúng nhất quán**, không phải làm
> cho chúng đúng.

### LRV và URV

Hai thuật ngữ bạn sẽ gặp trong tài liệu cảm biến:

| Ký hiệu | Tên | Nghĩa |
|---|---|---|
| **LRV** | *Lower Range Value* | Giá trị ứng với đầu dải — 4 mA |
| **URV** | *Upper Range Value* | Giá trị ứng với cuối dải — 20 mA |

Nhiều cảm biến cho phép **đặt lại LRV/URV** trong một dải cho phép. Ví dụ cảm biến 0–10 bar có thể
đặt lại thành 0–6 bar để dùng hết 16 mA cho vùng quan tâm.

> 💡 **Đặt lại dải trên cảm biến thường tốt hơn thu hẹp bằng phần mềm**, vì nó dùng hết dải dòng cho
> vùng bạn quan tâm — tức là cải thiện độ phân giải thật, không chỉ đổi cách tính.
>
> ⚠ Nhưng nó **không cải thiện sai số cơ bản của cảm biến**, vốn thường tính theo dải gốc. Và nó tạo
> một cái bẫy bảo trì: cảm biến thay thế lấy từ kho sẽ có **dải mặc định của nhà sản xuất**, không
> phải dải bạn đã đặt. Đây chính là bài toán ở Chương 12 mục 12.1 — và là một lý do nữa cho IO-Link.

### Zero và span

Hai phép chỉnh cơ bản:

- **Zero** — chỉnh điểm đầu dải. Với cảm biến áp suất, thường làm khi **xả hết áp**: giá trị phải đọc 0.
- **Span** — chỉnh độ dốc, dùng một giá trị đã biết ở gần cuối dải.

> ⚠ **Thứ tự quan trọng: zero trước, span sau** — và thường phải lặp lại một, hai vòng, vì hai phép
> chỉnh ảnh hưởng lẫn nhau ở mức nhỏ.

---

## 32.9 Trên máy mẫu DP-01

### Bảng quy đổi đầy đủ

Số liệu từ hồ sơ máy mẫu (Phụ lục J), sau khi chốt session 11:

| Tag | Tín hiệu | Dải kỹ thuật | Đơn vị trong biến | Tên biến |
|---|---|---|---|---|
| `AI_AirPress` | 4–20 mA | 0–10 bar | 0,01 bar | `AirPressX100` |
| `AI_GluePress` | 4–20 mA | 0–6 bar | 0,01 bar | `GluePressX100` |
| `AI_UvIntensity` | 0–10 V | 0–200 mW/cm² | 0,1 mW/cm² | `UvIntensityX10` |
| `AI_UvChamberTemp` | RTD Pt100 | 0–150 °C | 0,1 °C | `UvChamberTempX10` |
| `AO_GluePressSet` | 0–10 V | 0–6 bar | 0,01 bar | `GluePressSetX100` |
| `AO_ConvSpeed` | 0–10 V | 0–100 % | 1 % | `ConvSpeedPct` |
| `AO_UvPower` | 0–10 V | 0–100 % | 1 % | `UvPowerPct` |

Ba nhận xét:

- **Mỗi biến mang đơn vị trong tên.** Đây là biện pháp phòng lỗi ở mục 32.1, và nó tốn đúng vài ký tự.
- **Đơn vị chọn theo sai số cảm biến, không theo số bit ADC.** Áp suất dùng 0,01 bar vì sai số cảm
  biến ở bậc 0,05 bar — mịn hơn nữa là vô nghĩa.
- ⚠ **`AI_UvChamberTemp` là RTD, không phải 4–20 mA.** Module RTD thường trả giá trị theo đơn vị 0,1 °C
  **sẵn**, không cần quy đổi thang. Chương 33 nói kỹ.

### Ví dụ đầy đủ — `AI_GluePress`

```iecst
VAR CONSTANT
    RAW_MAX          : DINT := 27648;   // ⚠ TRA DATASHEET MODULE
    PRESS_MAX_X100   : DINT := 600;     // 6,00 bar
    RAW_WIRE_BREAK   : DINT := -2000;   // ⚠ TRA DATASHEET
    RAW_OVER_RANGE   : DINT := 29000;
    GLUE_LOW_ON_X100 : DINT := 350;     // cảnh báo bật ở 3,50 bar
    GLUE_LOW_OFF_X100: DINT := 370;     // tắt ở 3,70 bar — vùng chết
    FILT_K           : DINT := 20;      // lọc nhẹ cho hiển thị
END_VAR

// ── 1. Phát hiện ngoài dải TRƯỚC ──
IF RawGluePress < RAW_WIRE_BREAK THEN
    M_GluePressFault := TRUE;  M_GluePressFaultCode := 1;
ELSIF RawGluePress > RAW_OVER_RANGE THEN
    M_GluePressFault := TRUE;  M_GluePressFaultCode := 2;
ELSE
    M_GluePressFault := FALSE; M_GluePressFaultCode := 0;

    // ── 2. Quy đổi: nhân trước, chia sau, dùng DINT ──
    GluePressX100 := (RawGluePress * PRESS_MAX_X100) / RAW_MAX;

    // ── 3. Lọc — CHỈ cho hiển thị và ghi log ──
    GluePressFiltX100 := GluePressFiltX100
                       + (FILT_K * (GluePressX100 - GluePressFiltX100)) / 100;
END_IF;

// ── 4. Cảnh báo có vùng chết — dùng giá trị CHƯA lọc ──
IF M_GluePressFault THEN
    M_GluePressLow := FALSE;              // mất phép đo ≠ áp thấp (Ch.31)
ELSIF GluePressX100 < GLUE_LOW_ON_X100 THEN
    M_GluePressLow := TRUE;
ELSIF GluePressX100 > GLUE_LOW_OFF_X100 THEN
    M_GluePressLow := FALSE;
END_IF;

// ── 5. Kiểm công thức so với khả năng đo (Chương 29) ──
M_RecipePressValid := (RecipeGluePressX100 >= 0)
                  AND (RecipeGluePressX100 <= PRESS_MAX_X100);
```

Đoạn này gói cả chương. Bốn điểm đáng chú ý:

- **Thứ tự các bước không đổi được**: phát hiện lỗi → quy đổi → lọc → so ngưỡng.
- ⭐ **Cảnh báo dùng `GluePressX100` (chưa lọc), hiển thị dùng `GluePressFiltX100`.** Đúng gợi ý ở
  mục 32.6 — hai mục đích, hai biến.
- ⭐ **Bước 4 phân biệt "mất phép đo" với "áp thấp"** — hai chuyện khác nhau, hai thông báo khác nhau
  (Chương 31, Bẫy 9).
- **Bước 5 nối sang Chương 29**: dải hợp lệ của công thức phải nằm trong dải đo được. Một công thức
  yêu cầu 8 bar trên cảm biến 0–6 bar là công thức không kiểm chứng được.

---

## 32.10 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| ⚠⚠ **Dải giá trị thô** | **Khác nhau nhiều nhất.** Ví dụ thường gặp: Siemens 0–27 648 cho dải danh định; nhiều hệ khác dùng 0–32 767, 0–4095, hoặc số bit khác. ⭐ **Con số đầu tiên phải tra** |
| Giá trị vượt dải | Cách biểu diễn khác nhau — số âm, giá trị đặc biệt, hoặc bit trạng thái riêng |
| ⭐ Bit trạng thái kênh | Nhiều module báo sẵn đứt dây / vượt dải bằng một bit. **Dùng nó nếu có** — chính xác hơn tự so ngưỡng |
| Quy đổi thang sẵn có | Một số hệ có khối chuẩn hoá / quy đổi thang dựng sẵn; một số hệ để bạn tự viết. Dùng khối sẵn có thì gọn hơn nhưng ⚠ vẫn phải hiểu nó làm gì |
| Lọc tích hợp trong module | Nhiều module có lọc số cấu hình được. ⚠ **Nó cũng gây trễ** — cùng đánh đổi ở mục 32.6, chỉ là làm ở tầng khác |
| Module RTD / can nhiệt | Thường trả giá trị **theo đơn vị nhiệt độ sẵn**, không cần quy đổi thang (Chương 33) |

> ⚠ **Đừng chép hằng số quy đổi từ một dự án cũ sang dự án mới nếu module khác nhau.** Đây là lỗi
> chép–dán kinh điển, và nó cho ra con số **sai theo tỉ lệ nhưng trông hợp lý** — loại sai khó phát
> hiện nhất.

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

---

## 32.11 Bẫy thường gặp

### 🔍 BẪY 1 — Lẫn đơn vị giữa biến và ô nhập liệu

**Hiện tượng:** đúng cỗ máy ở mục 32.1 — nhập 5,5 thành 0,5 bar. Không lỗi, không cảnh báo, con số
vẫn trông hợp lý.
**Cách sửa:** đơn vị **trong tên biến**, và đơn vị **hiện trên màn hình** tại ô nhập. Hai việc.

### 🔍 BẪY 2 — Chia trước khi nhân

**Hiện tượng:** giá trị quy đổi luôn bằng 0 hoặc bằng đầu dải.
**Cách sửa:** nhân trước, chia sau (mục 32.4, Chương 19 mục 19.4).

### 🔍 BẪY 3 — Dùng `INT` cho phép quy đổi

**Hiện tượng:** kết quả trung gian `27648 × 600` tràn — giá trị nhảy sang số âm hoặc vô lý.
**Cách sửa:** `DINT` cho toàn bộ phép quy đổi (mục 32.4, Chương 11).

### 🔍 BẪY 4 — Lấy nhầm dải giá trị thô của module

**Hiện tượng:** mọi phép đo **sai theo tỉ lệ** — ví dụ đọc 5,1 bar khi thực tế 4,2. Sai một cách nhất
quán, nên rất dễ bị coi là "cảm biến cần hiệu chuẩn".
**Cách sửa:** tra datasheet module trước khi viết dòng quy đổi nào; ⚠ đừng chép hằng số từ dự án cũ
(mục 32.10).

### 🔍 BẪY 5 — Hiển thị nhiều chữ số hơn cảm biến đảm bảo

**Hiện tượng:** `4,2038 bar` trên màn hình trong khi cảm biến chỉ đảm bảo ±0,06 bar. Người vận hành
tin vào những chữ số không mang thông tin, và đi chỉnh quy trình theo nhiễu.
**Cách sửa:** số chữ số hiển thị khớp **sai số cảm biến**, không khớp số bit ADC (mục 32.3).

### 🔍 BẪY 6 — Chọn cảm biến dải quá rộng

**Hiện tượng:** đo 4 bar bằng cảm biến 0–250 bar; sai số ±2,5 bar làm phép đo vô dụng.
**Cách sửa:** chọn dải **vừa đủ** bao phủ vùng làm việc — quyết định lúc mua (mục 32.3).

### 🔍 BẪY 7 — Lọc mạnh tín hiệu dùng cho điều kiện an toàn

**Hiện tượng:** áp tụt thật nhưng chương trình biết muộn — muộn đúng bằng độ trễ bộ lọc.
**Cách sửa:** ⚠⚠ điều kiện an toàn và phát hiện sự cố **lọc rất nhẹ hoặc không lọc**; chống báo giả
bằng **timer xác nhận** (mục 32.6, Chương 17).

### 🔍 BẪY 8 — Quy đổi trước khi kiểm ngoài dải

**Hiện tượng:** giá trị đứt dây (số âm) được quy đổi thành một con số trông như phép đo thật.
**Cách sửa:** kiểm dải **trước**, quy đổi **sau** (mục 32.5, Chương 31).

### 🔍 BẪY 9 — Thêm `ELSE` vào khối vùng chết

**Hiện tượng:** vùng chết biến mất, bit cảnh báo nhấp nháy quanh ngưỡng như trước.
**Cách sửa:** khối vùng chết **không có `ELSE`** — vùng giữa phải giữ nguyên trạng thái (mục 32.7).

### 🔍 BẪY 10 — Gọi việc chỉnh hệ số là "hiệu chuẩn"

**Hiện tượng:** hai con số khớp nhau nhưng **cả hai đều sai**; và không có hồ sơ nào chứng minh phép
đo đúng khi khách hàng hỏi.
**Cách sửa:** hiệu chuẩn cần **chuẩn có độ chính xác cao hơn** và có vết truy nguyên. Chỉnh cho khớp
mà không có chuẩn thì gọi đúng tên nó: **làm cho nhất quán** (mục 32.8).

### 🔍 BẪY 11 — Quên cảm biến thay thế có dải mặc định khác

**Hiện tượng:** thay cảm biến đã được đặt lại LRV/URV bằng cái mới từ kho; mọi phép đo sai theo tỉ lệ
và **không ai nghĩ tới nguyên nhân đó**.
**Cách sửa:** ghi dải đã đặt vào tài liệu máy và dán nhãn tại cảm biến; hoặc dùng IO-Link để tham số
tự nạp (mục 32.8, Chương 12).

---

## 32.12 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Module analog trả về gì | **Số nguyên thô** — dải do module quy định |
| Con số đầu tiên phải tra | ⭐ **Dải giá trị thô** trong datasheet module |
| Độ phân giải là gì | Bước nhỏ nhất phân biệt được = dải ÷ số bước ADC |
| Độ phân giải ≠ | ⭐ **Độ chính xác** — cái sau do cảm biến quyết định |
| Hiển thị bao nhiêu chữ số | Khớp **sai số cảm biến**, không khớp số bit ADC |
| Chọn dải cảm biến | **Vừa đủ** bao phủ vùng làm việc — sai số tính theo % dải |
| Thứ tự phép tính quy đổi | ⭐ **Nhân trước, chia sau**, dùng **`DINT`** |
| Tên biến analog | ⭐ **Đơn vị nằm trong tên** — `GluePressX100` |
| Thứ tự xử lý | Kiểm ngoài dải → quy đổi → lọc → so ngưỡng |
| Lọc để hiển thị | Lọc mạnh được |
| Lọc để điều khiển | Lọc nhẹ — trễ vào thẳng vòng điều khiển |
| Lọc cho điều kiện an toàn | ⚠⚠ **Rất nhẹ hoặc không lọc**; dùng **timer xác nhận** |
| Chống nhấp nháy quanh ngưỡng | **Vùng chết** — khối `IF/ELSIF` **không có `ELSE`** |
| Chọn độ rộng vùng chết | Rộng hơn **biên độ dao động đo được** |
| Trước khi ghi ngõ ra analog | **Kẹp giá trị** trong dải |
| Đặt dải ≠ hiệu chuẩn | Hiệu chuẩn cần **chuẩn chính xác hơn** và có vết truy nguyên |
| ⭐⭐ Trễ của giá trị analog | **Tổng BA khoản**: đáp ứng cảm biến + cập nhật module (có lọc) + chu kỳ quét |
| Khoản nào thường lớn nhất | ⚠ **Cảm biến** — không phải chương trình |
| ⚠⚠ Dùng ít kênh cho nhanh | ⭐ **Không có tác dụng** — chu kỳ module không giảm theo số kênh dùng |
| Quá trình nhanh hơn khả năng PLC | ⭐ Đổi module nhanh hơn, hoặc ⭐⭐ **bộ điều khiển rời, PLC chỉ đặt điểm đặt** |
| Cảm biến thay thế | ⚠ Có **dải mặc định của nhà sản xuất** — không phải dải bạn đã đặt |

---

## 32.13 Tự kiểm

1. Module analog 16 bit trả về giá trị thô 13 824 với dải 0–27 648, cảm biến 0–6 bar. Áp suất là bao
   nhiêu?
2. ⭐ Phân biệt **độ phân giải** với **độ chính xác**. Cảm biến 0–6 bar sai số ±1 % đọc qua ADC cho
   bước 0,0002 bar — bạn được phép hiển thị bao nhiêu chữ số thập phân, và vì sao?
3. Vì sao **không** nên dùng cảm biến 0–250 bar để đo áp trong khoảng 3–5 bar, dù ADC vẫn đủ phân giải?
4. Viết công thức quy đổi thang tuyến tính. Nêu **ba** điều bắt buộc khi viết nó bằng số nguyên.
5. ⭐ Vì sao phải kiểm ngoài dải **trước** khi quy đổi, không phải sau?
6. Khi cờ lỗi cảm biến lên, biến giá trị kỹ thuật giữ giá trị cũ. Được phép dùng nó không? Vì sao?
7. So sánh lọc trung bình trượt với lọc IIR một bậc. Cái nào tốn bộ nhớ hơn?
8. ⭐ Vì sao **không** được lọc mạnh tín hiệu dùng cho điều kiện an toàn? Nếu cần chống báo giả thì
   dùng gì thay thế?
9. Vì sao khối vùng chết **không có nhánh `ELSE`**? Thêm `ELSE` vào thì chuyện gì xảy ra?
10. Chọn độ rộng vùng chết dựa vào đâu? Làm sao biết con số đó?
11. ⭐ Đồng hồ chuẩn chỉ 4,0 bar, PLC hiện 4,3 bar. Bạn sửa hệ số cho PLC hiện 4,0. Đó có phải hiệu
    chuẩn không? Vì sao?
12. LRV và URV là gì? Đặt lại dải trên cảm biến có lợi gì, và tạo ra **bẫy bảo trì** nào?
13. ⭐⭐ Từ lúc đại lượng thật đổi tới lúc chương trình thấy giá trị mới gồm **ba** khoản nào? ⚠ Khoản
    nào thường lớn nhất, và người ta hay đi tối ưu khoản nào?
14. ⚠⚠ Có người đề xuất *"chỉ đấu 2 trong 8 kênh cho module đọc nhanh hơn"*. ⭐ Đúng hay sai, vì sao?

> Câu 2, 5, 8 và 11 là bốn câu phân loại. Câu 2 là tinh thần của cả chương: **nhiều chữ số không làm
> phép đo đúng hơn — nó chỉ làm người đọc tin nhầm.**

---

### Chương tiếp theo

Chương 33 — **Cảm biến quá trình thường gặp**. Bạn đã biết biến tín hiệu điện thành con số có nghĩa.
Chương sau về các loại cảm biến sinh ra tín hiệu đó: áp suất, nhiệt độ (RTD và can nhiệt — hai loại
hành xử rất khác nhau), lưu lượng, mức — và những chỗ mỗi loại đánh lừa bạn.

### Nguồn tham khảo chương 32

- IEC 61131-2 — *Programmable controllers, Part 2: Equipment requirements and tests*: đặc tính ngõ
  vào/ra analog, độ phân giải, sai số và cách biểu diễn giá trị ngoài dải. *(tiêu chuẩn có bản quyền)*
- IEC 60381-1 và -2 — *Analogue signals for process control systems*: chuẩn hoá tín hiệu dòng và áp.
- **Datasheet module analog** của hệ đang dùng — dùng cho ⚠ **dải giá trị thô**, ngưỡng phát hiện
  ngoài dải, bit trạng thái kênh, và tuỳ chọn lọc tích hợp. Đây là các con số **bắt buộc phải tra**,
  không suy từ hệ khác.
- **Datasheet cảm biến** — dùng cho **sai số**, dải đặt được của LRV/URV, và quy trình chỉnh zero/span.
- Bảng I/O và bảng công thức của DP-01 — Phụ lục J; bảng ở mục 32.9 lấy từ đó.
- **Hanssen, Dag H.** — *Programmable Logic Controllers: A Practical Approach to IEC 61131-3 using
  CoDeSys*, §3.6.2 *Important Properties and Parameters*: ⭐⭐ **thời gian cập nhật của một giá trị
  analog gồm ba khoản** (đáp ứng cảm biến · cập nhật module kèm trễ lọc · chu kỳ quét); phân biệt
  **thời gian một kênh** với **chu kỳ cả module**, và ⚠ **chu kỳ module không đổi dù có kênh không
  dùng**; hai đường xử lý khi module quá chậm cho vòng PID — nền cho mục 32.6b.

> ⚡ Con số **27 648** dùng xuyên suốt chương là **ví dụ minh hoạ**, lấy theo một cách ánh xạ phổ biến.
> Nó **không phải giá trị áp dụng chung** — module của bạn có thể dùng 32 767, 4095, hoặc cách biểu
> diễn khác hẳn. Mọi ví dụ code trong chương đều đánh dấu `⚠ TRA DATASHEET MODULE` ở đúng chỗ cần
> thay số.
>
> Tương tự, các ngưỡng phát hiện ngoài dải (`-2000`, `29000`) là minh hoạ. Giá trị thật lấy từ
> datasheet module và datasheet cảm biến (Chương 31).
