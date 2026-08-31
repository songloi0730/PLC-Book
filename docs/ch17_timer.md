# Chương 17 — Timer: TON / TOF / TP

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 17.1 Bài toán: cỗ máy chạy tốt suốt tám tháng rồi phá một lô hàng

Một trạm kẹp board. Người viết chương trình dùng cách đơn giản nhất:

```
// Ra lệnh kẹp, chờ 2 giây, coi như đã kẹp xong
M_ClampReq := TRUE;
T_Wait(IN := TRUE, PT := T#2S);
IF T_Wait.Q THEN
    Step := Step + 1;          // đi tiếp
END_IF;
```

Xy-lanh kẹp thật ra chỉ mất 0,6 giây. Hai giây là dư dả. Máy chạy tám tháng không sự cố.

Rồi bộ lọc khí đầy nước, áp suất tụt nhẹ. Xy-lanh kẹp bây giờ mất **2,4 giây**.

Chương trình vẫn đi tiếp sau đúng 2 giây — **trong khi kẹp mới đi được ba phần tư hành trình**. Bước
tiếp theo cho cơ cấu gia công chạy. Board chưa được giữ chắc, xê dịch. Cả lô hỏng.

Không có báo động nào. Với chương trình, mọi bước đều "thành công".

Nếu người viết dùng cảm biến phản hồi thay vì timer, máy đã dừng ngay từ board đầu tiên với thông báo
*"S1.20 quá thời gian — chờ DI_Clamp1Up"*, và có người đi xả nước bộ lọc.

Đây là **sai lầm phổ biến nhất trong lập trình PLC**, và cả chương này xoay quanh nó.

---

## 17.2 Ba loại timer chuẩn

Chuẩn IEC 61131-3 định nghĩa **ba** khối timer. Mọi hãng đều có cả ba, tên gọi giống nhau.

![Ba loại timer — sơ đồ thời gian](../assets/ch17/hinh_17_1_timer.svg)

*Hình 17.1 — Cùng một tín hiệu vào, ba loại timer cho ba kết quả khác nhau.*

### TON — trễ sườn lên *(on-delay)*

Ngõ ra lên **sau khi** ngõ vào đã giữ mức 1 đủ thời gian đặt. Ngõ vào tụt xuống 0 thì ngõ ra tắt
**ngay lập tức** và bộ đếm về 0.

**Dùng khi:** cần một điều kiện tồn tại **liên tục** một khoảng thời gian mới coi là thật.

```
// Chỉ báo mất khí khi tín hiệu mất LIÊN TỤC quá 0,5 giây
// → chống báo động giả do nhiễu hoặc dao động ngắn
T_AirFault(IN := NOT DI_AirOK, PT := T#500MS);
M_AirFault := T_AirFault.Q;
```

Đây là công dụng chính đáng và phổ biến nhất của TON: **lọc tín hiệu nhiễu**.

### TOF — trễ sườn xuống *(off-delay)*

Ngõ ra lên **ngay** khi ngõ vào lên. Khi ngõ vào tụt, ngõ ra **còn giữ thêm** đủ thời gian đặt rồi mới tắt.

**Dùng khi:** cần kéo dài một trạng thái sau khi điều kiện đã mất.

```
// Quạt hút chạy thêm 30 giây sau khi tắt nguồn nhiệt
T_FanRun(IN := M_HeaterOn, PT := T#30S);
DO_ExhaustFan := T_FanRun.Q;
```

### TP — tạo xung *(pulse)*

Ngõ ra lên khi ngõ vào có **sườn lên**, và giữ **đúng** thời gian đặt rồi tắt — **không phụ thuộc**
ngõ vào sau đó. Nhấn giữ hay nhả ra đều không đổi kết quả.

**Dùng khi:** cần một xung có độ dài xác định.

```
// Còi kêu đúng 1 giây mỗi lần có báo động mới, dù báo động kéo dài bao lâu
T_Buzz(IN := M_NewAlarm, PT := T#1S);
DO_Buzzer := T_Buzz.Q;
```

### Timer giữ giá trị — phần mở rộng của hãng

Ngoài ba loại chuẩn, nhiều hãng có thêm loại **cộng dồn, giữ giá trị** khi ngõ vào mất, và cần lệnh
**đặt lại** riêng.

**Dùng khi:** cần đếm **tổng thời gian tích luỹ**, không phải thời gian liên tục — ví dụ tổng giờ chạy
của một cơ cấu, để lên lịch bảo trì (Chương 51, mục 51.11).

> ⚡ **LƯU Ý**
> Loại này **không nằm trong ba khối chuẩn**. Tên gọi và hành vi khác nhau đáng kể giữa các hãng, đặc
> biệt ở chỗ **có giữ giá trị qua mất điện hay không**. Nếu dùng, hãy tra tài liệu của đúng hệ bạn
> đang làm — xem mục 17.7.

### Bảng so sánh

| | **TON** | **TOF** | **TP** |
|---|---|---|---|
| Ngõ ra lên khi | Ngõ vào giữ 1 đủ thời gian | Ngõ vào lên — **ngay** | Sườn lên của ngõ vào — **ngay** |
| Ngõ ra tắt khi | Ngõ vào về 0 — **ngay** | Sau khi ngõ vào về 0 đủ thời gian | Hết thời gian đặt |
| Ngõ vào rung có ảnh hưởng? | ✅ Có — đếm lại từ đầu | ✅ Có | ❌ **Không** — xung đã bắt đầu là chạy hết |
| Công dụng điển hình | Lọc nhiễu, xác nhận điều kiện bền | Kéo dài trạng thái | Xung độ dài cố định |

---

## 17.3 Độ phân giải và sai số

Timer trong PLC **không phải đồng hồ độc lập**. Nó được cập nhật **mỗi lần khối timer được gọi** — tức
là **một lần mỗi vòng quét** (Chương 10).

Hệ quả trực tiếp:

> **Sai số của timer ít nhất bằng một chu kỳ quét.**
>
> Với thời gian quét 10 ms, một timer đặt 50 ms có thể kết thúc ở đâu đó trong khoảng 50–60 ms. Sai số
> tương đối là **20 %**.
>
> Cùng timer đó đặt 5 giây thì sai số tương đối là **0,2 %** — không đáng kể.

Quy tắc thực dụng:

| Thời gian đặt so với chu kỳ quét | Độ tin cậy | Kết luận |
|---|---|---|
| Nhỏ hơn 1 chu kỳ quét | ❌ Không dùng được | Cần bộ đếm phần cứng hoặc ngắt |
| 1–10 lần chu kỳ quét | ⚠ Sai số lớn | Chỉ dùng khi không cần chính xác |
| Lớn hơn 100 lần chu kỳ quét | ✅ Tốt | Dùng thoải mái |

> 🔍 **BẪY — timer trong nhánh chương trình không phải lúc nào cũng chạy**
> Nếu khối timer nằm trong một nhánh `IF` **không được thực thi ở vòng quét này**, thì timer đó
> **không được cập nhật** — nó đứng yên chứ không chạy tiếp.
>
> Nhiều người tưởng timer chạy nền như đồng hồ. Không phải: nó chỉ tiến khi được gọi.
>
> Nếu cần timer chạy liên tục bất kể logic, hãy **gọi khối đó ở ngoài nhánh điều kiện**, và đưa điều
> kiện vào chân `IN` thay vì bọc cả khối trong `IF`.

---

## 17.4 Trên máy mẫu DP-01

Ba cách dùng timer chính đáng trong lát cắt này.

### Lọc tín hiệu — chống báo động giả

```
// Công tắc áp suất khí dao động quanh ngưỡng khi máy nén đang nạp.
// Chỉ báo lỗi nếu mất khí LIÊN TỤC quá 500 ms.
T_AirLow(IN := NOT DI_AirOK, PT := T#500MS);
M_AirFault := T_AirLow.Q;
```

Không có TON này, máy sẽ báo lỗi mỗi lần máy nén nạp — báo động giả, và người vận hành sẽ học cách bỏ
qua báo động (Chương 44).

### Chống rung tiếp điểm nút bấm

```
// Nút bấm cơ khí nảy vài lần trong vài mili-giây khi nhấn
T_StartDeb(IN := DI_StartPB, PT := T#20MS);
M_StartClean := T_StartDeb.Q;
```

### Timeout của bước — ⭐ dùng để **báo lỗi**, không để chuyển bước

Đây là cách dùng timer đúng đắn nhất trong toàn bộ chương trình trình tự:

```
// ── Bước 20: nâng kẹp ──
M_Stn1_ClampReq := TRUE;

// CHUYỂN BƯỚC: bằng phản hồi thật
IF DI_Clamp1Up THEN
    Stn1_Step := 30;
END_IF;

// BÁO LỖI: bằng timer, chạy song song
T_Step20(IN := (Stn1_Step = 20), PT := T#3S);
IF T_Step20.Q THEN
    Stn1_FaultStep := 20;
    M_AnyFault     := TRUE;      // "S1.20 quá thời gian — chờ DI_Clamp1Up"
END_IF;
```

Hai khối này **làm hai việc khác nhau và không thay thế nhau**:

| | Điều kiện chuyển bước | Timer |
|---|---|---|
| Trả lời câu hỏi | *Cơ cấu đã tới đích chưa?* | *Đã trôi qua bao lâu?* |
| Nguồn thông tin | **Thế giới thật** (cảm biến) | Đồng hồ trong PLC |
| Khi mọi thứ bình thường | Đúng | Đúng |
| ⭐ Khi có sự cố | **Vẫn đúng** — không tới đích thì không chuyển | **Sai** — vẫn hết giờ như thường |

Dòng cuối là toàn bộ lý do. Hai câu hỏi trùng nhau khi mọi thứ ổn, và **tách nhau đúng lúc bạn cần
câu trả lời đúng nhất**.

---

## 17.5 Nối tầng timer

Một số hệ giới hạn thời gian đặt tối đa của một timer. Cần thời gian dài hơn thì nối tầng:

```
// Ví dụ: cần 30 phút từ hai timer 15 phút
T_A(IN := M_Enable AND NOT T_B.Q, PT := T#15M);
T_B(IN := T_A.Q,                  PT := T#15M);
M_30MinDone := T_B.Q;
```

Cách khác thường gọn hơn: dùng **một timer ngắn kích một bộ đếm**:

```
// Timer 1 giây tự kích lại, đếm số giây
T_Sec(IN := M_Enable AND NOT T_Sec.Q, PT := T#1S);
C_Sec(CU := T_Sec.Q, R := NOT M_Enable, PV := 1800);   // 1800 giây = 30 phút
M_30MinDone := C_Sec.Q;
```

Cách thứ hai có lợi thế: bạn **đọc được đã trôi qua bao nhiêu giây** — hữu ích khi gỡ lỗi. Bộ đếm ở
Chương 18.

> ⚡ **LƯU Ý**
> Với thời gian rất dài (hàng giờ, hàng ngày), timer không phải công cụ đúng — sai số tích luỹ và giá
> trị mất khi mất điện. Dùng **đồng hồ thời gian thực** của PLC và so sánh mốc thời gian.

---

## 17.6 Bẫy thường gặp

### 🔍 BẪY 1 — Dùng timer thay cho tín hiệu phản hồi ⭐

Bẫy trung tâm của chương và của cả cuốn sách. Đã mổ xẻ ở mục 17.1 và 17.4.

Cách nhận ra trong code của người khác: tìm mọi chỗ điều kiện chuyển bước là `T_xxx.Q`. Mỗi chỗ như
vậy là một câu hỏi cần trả lời: *"vì sao ở đây không có cảm biến xác nhận?"*

Có **một** câu trả lời chính đáng: **thật sự không có cách nào đo được**. Ví dụ: chờ keo chảy đủ, chờ
nhiệt lan toả. Khi đó timer là đúng — nhưng phải ghi comment nói rõ, và phải hiểu rằng bạn đang chấp
nhận rủi ro *"nếu quá trình chậm hơn dự kiến, máy không biết"*.

Nếu câu trả lời là *"lắp cảm biến thì tốn thêm"* — hãy so sánh với chi phí một lô hàng hỏng.

### 🔍 BẪY 2 — Timer bị đặt lại ngoài ý muốn

TON đặt lại bộ đếm **ngay** khi ngõ vào tụt xuống 0, dù chỉ một vòng quét.

Nếu điều kiện vào dao động — cảm biến rung, tín hiệu nhiễu, hoặc một điều kiện logic nhấp nháy — thì
timer **không bao giờ đếm đủ**, và triệu chứng là *"timer không bao giờ hết giờ"*.

```
// ✗ Điều kiện vào nhấp nháy → timer đếm lại liên tục
T_X(IN := DI_BoardStn1 AND M_SomeFlickeringCondition, PT := T#5S);

// ✓ Lọc điều kiện trước, rồi mới đưa vào timer chính
T_Stable(IN := M_SomeFlickeringCondition, PT := T#100MS);
T_X(IN := DI_BoardStn1 AND T_Stable.Q, PT := T#5S);
```

**Cách chẩn đoán:** xem trực tuyến giá trị đếm hiện tại của timer. Nếu nó cứ nhảy về 0, bạn đã tìm ra
nguyên nhân — và vấn đề nằm ở **điều kiện vào**, không ở timer.

### 🔍 BẪY 3 — Timer nằm trong nhánh không được thực thi

Đã nêu ở mục 17.3. Timer chỉ tiến khi khối của nó được gọi. Đặt trong một nhánh `IF` không chạy thì nó
đứng yên — và triệu chứng cũng là *"timer không bao giờ hết giờ"*, nhưng nguyên nhân khác hẳn Bẫy 2.

**Cách phân biệt hai bẫy:** xem giá trị đếm hiện tại. Nhảy về 0 liên tục → Bẫy 2. Đứng im một chỗ →
Bẫy 3.

### 🔍 BẪY 4 — Đặt thời gian quá gần chu kỳ quét

Timer 20 ms trong hệ có thời gian quét 15 ms là timer không đáng tin. Xem bảng ở mục 17.3.

Và nhớ rằng thời gian quét **tăng lên** khi chương trình lớn dần — một timer đủ tin cậy hôm nay có thể
không còn đủ sau khi ai đó thêm chức năng (Chương 10).

### 🔍 BẪY 5 — Dùng chung một thể hiện timer ở nhiều chỗ

```
// ✗ SAI — cùng một thể hiện T_Wait dùng cho hai bước
IF Step = 20 THEN  T_Wait(IN := TRUE, PT := T#3S);  END_IF;
IF Step = 40 THEN  T_Wait(IN := TRUE, PT := T#5S);  END_IF;
```

Mỗi khối timer có **bộ nhớ riêng gắn với thể hiện**. Dùng chung một thể hiện ở hai chỗ nghĩa là hai
chỗ đó **giẫm lên bộ nhớ của nhau** — giá trị đếm và thời gian đặt bị ghi đè mỗi vòng quét.

Mỗi chỗ cần một timer riêng phải có **một thể hiện riêng**. Nếu thấy mình cần nhiều timer giống nhau,
đó là dấu hiệu nên gói vào một khối chức năng tái dùng (Chương 27).

### 🔍 BẪY 6 — Đặt timeout theo cảm tính

Timeout quá chặt → báo động giả khi khí hơi yếu hoặc trời lạnh. Quá lỏng → mất tác dụng phát hiện.

**Cách đúng:** đo thời gian thật của cơ cấu trên máy, rồi cộng biên an toàn. Và ghi lại con số gốc để
sau này so sánh — xy-lanh chậm dần là dấu hiệu sắp hỏng (Chương 51).

### 🔍 BẪY 7 — Nhầm TON với TOF khi đọc code người khác

Hai khối chỉ khác nhau một chữ cái và làm hai việc **ngược nhau**. Khi đọc chương trình lạ, kiểm lại
đúng loại trước khi suy luận — đây là lỗi đọc nhầm rất tốn thời gian.

---

## 17.7 Khác biệt giữa các hãng

Ba khối TON, TOF, TP nằm trong chuẩn nên **có ở mọi hệ với cùng tên và cùng hành vi**. Nhưng những chi
tiết sau khác nhau và sẽ làm bạn vấp khi chuyển hệ:

| Khía cạnh | Khác nhau ở đâu |
|---|---|
| **Cách viết thời gian** | Định dạng hằng số thời gian khác nhau giữa các hệ |
| **Độ phân giải nhỏ nhất** | Có hệ tới mili-giây, có hệ thô hơn |
| **Thời gian đặt lớn nhất** | Khác nhau — quyết định có phải nối tầng không (mục 17.5) |
| **Timer giữ giá trị** | ⚠ **Không phải khối chuẩn.** Tên gọi, hành vi khi mất điện, và cách đặt lại khác nhau đáng kể |
| **Timer trong ladder** | Có hệ vẽ timer thành một hộp trên nấc thang, có hệ dùng lệnh riêng |
| **Truy cập giá trị đếm hiện tại** | Tên biến khác nhau — nhưng **mọi hệ đều cho xem**, và đó là công cụ chẩn đoán ở Bẫy 2 và 3 |

Chi tiết đối chiếu năm hệ: **Phụ lục A2**.

---

## 17.8 Bảng chốt

| # | Kiểm | Đạt khi |
|---|---|---|
| 1 | Mọi chỗ chuyển bước bằng `T_xxx.Q` đã được rà lại | Mỗi chỗ hoặc đổi sang phản hồi, hoặc có comment giải thích vì sao không đo được |
| 2 | Mọi bước chờ cơ cấu có **timeout báo lỗi** | Có, và thông báo nêu rõ bước + tín hiệu đang chờ |
| 3 | Thời gian đặt **lớn hơn nhiều lần chu kỳ quét** | Có; đã xét cả trường hợp quét tăng về sau |
| 4 | Mỗi timer có **thể hiện riêng** | Không dùng chung |
| 5 | Timer cần chạy liên tục được gọi **ngoài nhánh điều kiện** | Có |
| 6 | Timeout đặt theo **đo thật**, không theo cảm tính | Có, và đã ghi con số gốc |
| 7 | Điều kiện vào timer đã **được lọc** nếu có khả năng dao động | Có |

---

## 17.9 Tự kiểm

1. Kể lại sự cố ở mục 17.1. Vì sao máy **chạy tốt tám tháng** rồi mới hỏng?
2. Phân biệt **TON, TOF, TP** — mỗi loại ngõ ra lên khi nào và tắt khi nào?
3. Loại nào **không bị ảnh hưởng** khi ngõ vào rung sau khi đã kích? Vì sao tính chất đó hữu ích?
4. Vì sao sai số của timer **ít nhất bằng một chu kỳ quét**? Timer 30 ms trong hệ quét 10 ms có đáng
   tin không?
5. Nêu **hai câu hỏi khác nhau** mà "điều kiện chuyển bước" và "timer" trả lời. Chúng trùng nhau khi
   nào và tách nhau khi nào?
6. Có **một** trường hợp dùng timer để chuyển bước là chính đáng. Đó là trường hợp nào, và bạn phải
   làm gì kèm theo?
7. Timer "không bao giờ hết giờ". Nêu **hai nguyên nhân** khả dĩ và **cách phân biệt** chúng bằng một
   phép quan sát.
8. Vì sao dùng chung một thể hiện timer ở hai chỗ là sai?
9. Timeout đặt quá chặt và quá lỏng — mỗi cái gây hậu quả gì? Cách đặt đúng?
10. Bạn đọc code của người khác và thấy `T_Wait.Q` làm điều kiện chuyển bước. **Câu hỏi đầu tiên** bạn
    phải đặt là gì?

Câu 5, 6 và 7 là ba câu phân loại. Câu 5 là nguyên tắc trung tâm; câu 6 kiểm tra bạn không áp dụng
nguyên tắc một cách máy móc; câu 7 là kỹ năng chẩn đoán thật.

---

### Chương tiếp theo

**Chương 18 — Counter & đếm xung tốc độ cao.** Timer đếm thời gian; counter đếm sự kiện. Và có một
ngưỡng mà đếm bằng phần mềm không còn khả thi — chương sau cho bạn công thức để biết ngưỡng đó ở đâu.

---

### Nguồn tham khảo chương 17

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: định nghĩa ba khối timer
  chuẩn TP, TON, TOF và kiểu dữ liệu thời gian. *(tiêu chuẩn có bản quyền; chương này chỉ diễn giải ở
  mức khái niệm)*
- Tài liệu hãng về khối timer và timer giữ giá trị — dùng để đối chiếu khác biệt ở mục 17.7; số hiệu
  cụ thể ghi trong Phụ lục A2.
- Bảng thời gian bước của DP-01 — Phụ lục J.

> ⚡ Mọi con số thời gian trong chương (0,6 s cho hành trình kẹp, 3 s timeout, 500 ms lọc khí) là **giá
> trị minh hoạ của máy mẫu**. Giá trị thật phải đo trên máy của bạn.
