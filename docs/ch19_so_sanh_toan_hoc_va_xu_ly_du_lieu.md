# Chương 19 — So sánh, toán học & xử lý dữ liệu

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 19.1 Chương này giải quyết cái gì

Tới đây bạn đã làm việc với **bit**: tiếp điểm, cuộn dây, cạnh, cờ nhớ. Bit trả lời câu hỏi có/không.

Nhưng máy thật còn chứa **giá trị**: số board đã làm, thời gian chu trình, số hiệu bước, mã hàng đang
chạy, chiều dài đoạn keo. Với giá trị, câu hỏi không còn là "có hay không" mà là "bằng bao nhiêu",
"lớn hơn hay nhỏ hơn", "quy đổi sang đơn vị nào".

Chương này gồm bốn nhóm việc:

| Nhóm | Câu hỏi | Mục |
|---|---|---|
| **Chuyển dữ liệu** | Đưa giá trị từ chỗ này sang chỗ khác | 19.2 |
| **So sánh** | Giá trị này so với giá trị kia thế nào | 19.3 |
| **Tính toán** | Cộng trừ nhân chia, và những chỗ PLC hành xử khác máy tính thường | 19.4–19.5 |
| **Cấu trúc dữ liệu** | Theo dõi nhiều sản phẩm cùng lúc trên một chuyền | 19.6–19.7 |

Mục 19.5 (chia cho 0 và ép kiểu) và mục 19.6 (thanh ghi dịch) là hai mục quan trọng nhất. Mục đầu vì
nó làm **dừng CPU**; mục sau vì nó giải một bài toán có mặt ở gần như mọi dây chuyền.

---

## 19.2 MOVE — chuyển giá trị

Lệnh cơ bản nhất: sao chép một giá trị từ nguồn sang đích.

```iecst
OkCountHmi := OkCount;              // đưa ra cho màn hình đọc
Stn1_Step  := 10;                   // đặt bước về giá trị cố định
TargetPos  := RecipeDispenseLen;    // nạp từ công thức sản phẩm
```

Trong ladder, lệnh này thường là một hộp `MOVE` với chân nguồn và chân đích, đặt ở cuối một nấc thang
— nghĩa là **chỉ chạy khi đường dẫn của nấc đó đúng**.

Ba điều dễ vấp:

- **MOVE chạy mỗi vòng quét** nếu điều kiện luôn đúng. Muốn nạp một lần thì bắt cạnh (Chương 16).
  Nạp công thức liên tục sẽ ghi đè mọi thay đổi người vận hành vừa nhập.
- **Đích phải đủ chỗ chứa.** Chuyển giá trị 40 000 vào một biến `INT` 16 bit có dấu (tối đa 32 767)
  cho kết quả sai — xem mục 19.5.
- **MOVE không đổi kiểu** ở nhiều hệ; hai bên phải cùng kiểu, hoặc phải ép kiểu tường minh.

> 💡 **MẸO — MOVE là chỗ tốt để đặt điểm quan sát**
> Khi gỡ lỗi một giá trị "không biết từ đâu ra", tìm **mọi** lệnh ghi vào biến đó — MOVE, phép gán,
> khối chức năng có chân ra nối vào nó. Công cụ tham chiếu chéo *(cross-reference)* của phần mềm lập
> trình làm việc này trong vài giây (Chương 22). Đây là kỹ thuật gỡ lỗi năng suất nhất với dữ liệu.

---

## 19.3 So sánh

Sáu phép so sánh chuẩn, cho kết quả là một bit:

| Phép | Ký hiệu ST | Nghĩa |
|---|---|---|
| Bằng | `=` | |
| Khác | `<>` | |
| Lớn hơn | `>` | |
| Lớn hơn hoặc bằng | `>=` | |
| Nhỏ hơn | `<` | |
| Nhỏ hơn hoặc bằng | `<=` | |

Trong ladder, mỗi phép là một hộp đặt **trên đường dẫn**, hoạt động như một tiếp điểm: so sánh đúng
thì cho dòng đi qua.

```iecst
M_TrayFull    := OkCount >= 50;
M_Stn1AtStep20 := Stn1_Step = 20;
M_CycleTooLong := CycleTimeMs > RecipeMaxCycleMs;
```

### ⚠ So sánh bằng với số thực

```iecst
// ✗ SAI — gần như không bao giờ đúng
IF ActualLength = 12.5 THEN ...
```

Số thực *(REAL)* được lưu ở dạng dấu chấm động, và phần lớn số thập phân **không biểu diễn được chính
xác** ở dạng nhị phân. Giá trị trông là `12.5` có thể thật ra là `12.499999`. Phép so sánh bằng trả
về sai, và nó sai một cách **không tái hiện được** — chạy đúng trong mô phỏng, hỏng trên máy thật.

```iecst
// ✓ ĐÚNG — so sánh trong dải dung sai
IF ABS(ActualLength - 12.5) < 0.01 THEN ...
```

> **Quy tắc: không bao giờ dùng `=` hoặc `<>` với số thực.** Với số nguyên thì `=` hoàn toàn an toàn.

### So sánh trong dải — và vì sao nên có trễ

Kiểm tra một giá trị có nằm trong khoảng cho phép:

```iecst
M_LengthOk := (ActualLength >= RecipeMin) AND (ActualLength <= RecipeMax);
```

Khi giá trị dao động quanh đúng ngưỡng, bit kết quả sẽ **nhấp nháy** — mỗi lần nhấp là một lần báo
lỗi rồi hết lỗi. Cách chữa là **trễ** *(hysteresis)*: ngưỡng bật và ngưỡng tắt khác nhau.

```iecst
// Cảnh báo bật ở 45, chỉ tắt khi đã xuống dưới 40
IF CycleTimeSec > 45.0 THEN
    M_CycleWarn := TRUE;
ELSIF CycleTimeSec < 40.0 THEN
    M_CycleWarn := FALSE;
END_IF;                     // giữa 40 và 45: giữ nguyên trạng thái cũ
```

Nhánh `ELSIF` không có `ELSE` là cố ý: vùng ở giữa **không đổi gì cả**. Đây là kỹ thuật dùng lại
nhiều lần khi sang analog (Chương 32), nhưng nguyên tắc đã đúng từ đây.

---

## 19.4 Bốn phép tính

```iecst
Total     := OkCount + NgCount;
Remaining := TargetQty - Total;
TotalMs   := CycleCount * CycleTimeMs;
AvgMs     := TotalMs / CycleCount;        // ⚠ xem mục 19.5
```

Ba điều cần biết ngay:

- **Thứ tự thực hiện** theo quy tắc toán thông thường: nhân chia trước, cộng trừ sau. Khi nghi ngờ,
  **thêm ngoặc** — ngoặc không tốn gì và giúp người đọc sau này.
- **Phép chia số nguyên cắt phần thập phân**, không làm tròn: `7 / 2` cho `3`, không phải `3.5` và
  cũng không phải `4`.
- **Kết quả trung gian có thể tràn** dù kết quả cuối vẫn nằm trong dải — xem mục 19.5.

### Tỉ lệ phần trăm — bẫy thứ tự phép tính

```iecst
// ✗ SAI — chia trước, số nguyên cắt hết phần lẻ
YieldPct := (OkCount / TotalCount) * 100;      // luôn ra 0 hoặc 100

// ✓ ĐÚNG — nhân trước rồi mới chia
YieldPct := (OkCount * 100) / TotalCount;
```

Với `OkCount = 1187` và `TotalCount = 1240`, cách sai cho `0 * 100 = 0`; cách đúng cho `95`.

Nhưng cách đúng lại tạo ra rủi ro mới: `1187 * 100 = 118 700`, vượt dải `INT` 16 bit. Nếu các biến là
`INT`, phép nhân **tràn** trước khi kịp chia. Đây chính là "kết quả trung gian tràn" nói ở trên, và
cách chữa là dùng kiểu 32 bit cho phép tính, hoặc tính bằng số thực.

---

## 19.5 ⭐ Ba chỗ PLC hành xử khác máy tính thường

### Chia cho 0 — có thể **dừng CPU**

```iecst
AvgCycleMs := TotalMs / CycleCount;    // đầu ca, CycleCount = 0
```

Trên máy tính thường, chia cho 0 ném ra một ngoại lệ mà chương trình bắt được. Trên PLC, hậu quả
**khác nhau tuỳ hệ** và bao gồm cả trường hợp xấu nhất:

| Hệ có thể | Hậu quả |
|---|---|
| Đặt lỗi vào một bit trạng thái, kết quả không xác định, chạy tiếp | Sai số liệu, khó phát hiện |
| Trả về giá trị lớn nhất của kiểu | Số liệu vô lý, dễ thấy hơn |
| **Chuyển CPU sang STOP** | ⚠⚠ **Máy dừng đột ngột giữa chu trình** |

> ⚠⚠ **NGUY HIỂM**
> Trường hợp thứ ba là lý do mục này có cảnh báo. CPU chuyển sang STOP nghĩa là **mọi ngõ ra tắt cùng
> lúc**, giữa chu trình, không theo trình tự dừng nào. Cơ cấu đang giữ có thể nhả; cơ cấu đang di
> chuyển dừng ở giữa hành trình. Hậu quả phụ thuộc thiết kế trạng thái an toàn của từng ngõ ra
> (Chương 48) — nhưng dù có thiết kế tốt, đây vẫn là kiểu dừng tệ nhất.
>
> Và tình huống kích hoạt nó thường **rất tầm thường**: chia cho số đếm ở đầu ca, khi số đếm chưa
> được cộng lần nào.

Cách phòng là một dòng, và phải có ở **mọi** phép chia mà mẫu số là biến:

```iecst
// ✓ ĐÚNG — kiểm mẫu số trước, luôn luôn
IF CycleCount > 0 THEN
    AvgCycleMs := TotalMs / CycleCount;
ELSE
    AvgCycleMs := 0;                   // giá trị an toàn khi chưa có dữ liệu
END_IF;
```

> **Quy tắc: mọi phép chia có mẫu số là biến đều phải được bọc bằng một phép kiểm khác 0.**
> Không có ngoại lệ, kể cả khi bạn "chắc chắn" mẫu số không bao giờ bằng 0 — vì đầu ca, sau khi xoá
> số đếm, và sau khi nạp lại chương trình, nó đều bằng 0.

### Tràn số — âm thầm và dai dẳng

Mỗi kiểu số nguyên có dải xác định:

| Kiểu | Dải | Ghi chú |
|---|---|---|
| `INT` | −32 768 … 32 767 | 16 bit có dấu — **rất dễ chạm** |
| `DINT` | ≈ ±2,1 tỉ | 32 bit có dấu — dùng cho bộ đếm tích luỹ |
| `UINT` | 0 … 65 535 | 16 bit không dấu |
| `REAL` | ≈ ±3,4 × 10³⁸, khoảng 7 chữ số có nghĩa | Dải rộng nhưng **độ chính xác hữu hạn** |

Vượt dải thì phần lớn hệ **quay vòng**: `32767 + 1` cho `−32768`. Không có báo lỗi. Một bộ đếm sản
lượng đang tăng dần bỗng thành số âm, và mọi phép tính dựa trên nó đều sai từ đó.

Ba chỗ hay tràn:

- **Bộ đếm tích luỹ** chạy nhiều ngày — dùng `DINT` (Chương 18, Bẫy 2).
- **Kết quả trung gian** như `OkCount * 100` ở mục 19.4.
- **Tổng thời gian tính bằng mili-giây**: 32 767 ms chỉ là **33 giây**. Tính thời gian chạy máy bằng
  `INT` mili-giây là sai ngay từ ý tưởng.

### Ép kiểu — nơi độ chính xác biến mất

**Ép kiểu** *(type conversion)* là chuyển giá trị từ kiểu này sang kiểu khác. Hai hướng, hai loại rủi
ro khác nhau:

| Hướng | Rủi ro | Ví dụ |
|---|---|---|
| Kiểu nhỏ → kiểu lớn (`INT` → `DINT`, `INT` → `REAL`) | ✅ An toàn | `1187` → `1187.0` |
| Kiểu lớn → kiểu nhỏ (`DINT` → `INT`) | ⚠ **Mất dữ liệu nếu vượt dải** | `70000` → giá trị vô nghĩa |
| Số thực → số nguyên (`REAL` → `INT`) | ⚠ **Mất phần thập phân** | `12.9` → `12` hoặc `13`, tuỳ hệ |

Hàng cuối là chỗ hay gây tranh cãi: **cắt hay làm tròn?** Chuẩn có hàm riêng cho từng hành vi, nhưng
lệnh mặc định của mỗi hệ khác nhau. Với một chiều dài đoạn keo, chênh lệch giữa cắt và làm tròn là
`0,9` đơn vị — đủ để hỏng sản phẩm.

> ⚡ **LƯU Ý — quy tắc thực dụng cho tính toán có phần lẻ**
> Nhân lên rồi làm việc với **số nguyên đơn vị nhỏ**, thay vì dùng số thực. Đo chiều dài bằng
> **phần mười mi-li-mét** (`125` thay vì `12.5`) thì mọi phép tính là số nguyên, không có sai số dấu
> chấm động, so sánh bằng dùng được, và chỉ quy đổi khi hiển thị. Cách này phổ biến trong máy công
> nghiệp vì nó loại hẳn cả một nhóm lỗi.
>
> Khi chọn cách này, **ghi đơn vị vào tên biến**: `LengthTenthMm`, không phải `Length`. Đơn vị ngầm
> hiểu là nguồn gốc của lỗi quy đổi.

---

## 19.6 ⭐ Thanh ghi dịch — theo dõi sản phẩm dọc chuyền

### Bài toán

Trên DP-01: board được kiểm ở **trạm 1**. Nếu tra keo lỗi, board đó phải bị loại — nhưng chỗ loại bỏ
nằm ở **cuối chuyền**, sau trạm 2. Giữa hai điểm đó có thể có board khác.

Câu hỏi: khi board tới chỗ loại bỏ, làm sao biết **board này** có phải là board đã bị đánh dấu lỗi
lúc ở trạm 1?

Một bit cờ không giải quyết được: lúc board đầu tới chỗ loại bỏ thì trạm 1 đã kiểm board thứ hai và
ghi đè mất cờ.

### Giải pháp

Cần một cấu trúc mà **thông tin đi cùng sản phẩm**. Đó là **thanh ghi dịch** *(shift register)*: một
dãy ô nhớ, mỗi ô ứng với một vị trí trên chuyền. Mỗi khi chuyền tiến một bước, toàn bộ nội dung
**dịch sang một ô**.

```text
        vị trí:   [0]      [1]      [2]      [3]
                 trạm 1   giữa    trạm 2   loại bỏ
   trước khi dịch:  NG      OK       OK       —
   sau khi dịch:    —       NG       OK       OK   ← board OK tới chỗ loại bỏ
   dịch lần nữa:    —       —        NG       OK   ← board NG đang ở trạm 2
   dịch lần nữa:    —       —        —        NG   ← board NG tới chỗ loại bỏ → loại
```

Thông tin "NG" đi cùng board qua từng vị trí. Tới chỗ loại bỏ, ô cuối cho biết chính xác board đang ở
đó có lỗi hay không.

### Hiện thực

```iecst
VAR
    BoardNG   : ARRAY[0..3] OF BOOL;    // 4 vị trí trên chuyền
    TrigShift : R_TRIG;
    i         : INT;
END_VAR

// Dịch khi chuyền tiến đúng một vị trí — dùng chính tín hiệu tiến của chuyền
TrigShift(CLK := M_ConveyorIndexDone);

IF TrigShift.Q THEN
    // Dịch từ CUỐI về ĐẦU — nếu làm ngược sẽ sao chép một giá trị ra cả mảng
    FOR i := 3 TO 1 BY -1 DO
        BoardNG[i] := BoardNG[i - 1];
    END_FOR;
    BoardNG[0] := FALSE;                // vị trí đầu: board mới, chưa đánh dấu
END_IF;

// Đánh dấu tại trạm 1
IF M_Stn1DispenseFault THEN
    BoardNG[0] := TRUE;
END_IF;

// Quyết định tại chỗ loại bỏ
M_RejectNow := BoardNG[3] AND M_BoardAtReject;
```

> ⚠ **Chiều của vòng lặp dịch là chỗ sai kinh điển.**
> Phải dịch từ **chỉ số lớn về chỉ số nhỏ**. Làm ngược lại, `BoardNG[1] := BoardNG[0]` chạy trước, rồi
> `BoardNG[2] := BoardNG[1]` lấy giá trị **vừa mới ghi** — kết quả là giá trị ở ô 0 bị nhân bản ra
> toàn bộ mảng. Một board lỗi làm loại bỏ mọi board phía sau, và triệu chứng trông giống hệt "cảm
> biến kiểm tra hỏng".

### Ba điều bắt buộc

- **Dịch theo sự kiện thật, không theo thời gian.** Kích dịch bằng tín hiệu xác nhận chuyền đã tiến
  đúng một vị trí. Dịch theo timer thì chỉ cần chuyền trượt hoặc kẹt một lần là **toàn bộ thông tin
  lệch vị trí vĩnh viễn** — và board tốt bị loại trong khi board lỗi đi tiếp. Đây là cùng một nguyên
  tắc với Chương 17: phản hồi thật, không phải đồng hồ.
- **Phải có cách đồng bộ lại.** Khi máy xả hết board, xoá toàn bộ mảng. Không có bước này, một lần
  lệch sẽ ở lại mãi.
- **Xả máy khi mất điện.** Sau khi có điện lại, không thể tin nội dung mảng — vị trí board thật có
  thể đã thay đổi. Yêu cầu xả hết rồi bắt đầu lại (Chương 28).

> 💡 **MẸO — thanh ghi dịch chứa được nhiều hơn một bit**
> Thay `ARRAY OF BOOL` bằng `ARRAY OF` một kiểu cấu trúc, bạn mang theo cả mã sản phẩm, thời điểm vào,
> kết quả đo, số hiệu công thức. Khi có truy xuất nguồn gốc (Chương 42), đây chính là chỗ dữ liệu của
> từng board được giữ trong lúc nó đi qua máy.

---

## 19.7 Mảng và địa chỉ gián tiếp

**Mảng** *(array)* là dãy phần tử cùng kiểu, truy cập bằng chỉ số. Bạn vừa dùng nó ở mục 19.6.

**Địa chỉ gián tiếp** *(indirect addressing)* là dùng một **biến** làm chỉ số:

```iecst
StepTimeMs[Stn1_Step] := ElapsedMs;      // ghi vào ô ứng với bước hiện tại
```

Rất gọn. Và cũng rất dễ thành thứ không ai đọc nổi.

| Nên dùng khi | Không nên dùng khi |
|---|---|
| Nhiều đối tượng **giống hệt nhau**: 8 trạm cùng loại, 20 vị trí trên chuyền | Vài đối tượng **khác nhau** — viết thẳng rõ hơn nhiều |
| Dữ liệu đi kèm sản phẩm (thanh ghi dịch) | Chỉ để tiết kiệm vài dòng |
| Bảng tra: hệ số theo mã hàng | Người bảo trì tại nhà máy chỉ quen đọc ladder (Chương 20, mục 20.6) |

> ⚠⚠ **NGUY HIỂM — chỉ số vượt dải mảng**
> `BoardNG[i]` với `i = 7` trên mảng `[0..3]`: tuỳ hệ, hoặc CPU báo lỗi và **chuyển sang STOP**, hoặc
> tệ hơn, **ghi đè lên vùng nhớ của biến khác** — gây ra hỏng hóc ở một chỗ hoàn toàn không liên quan,
> và gần như không thể lần ra nguyên nhân.
>
> Mọi chỉ số đến từ tính toán hoặc từ bên ngoài đều phải được **kẹp trong dải** trước khi dùng:
>
> ```iecst
> IF i < 0 THEN  i := 0;  END_IF;
> IF i > 3 THEN  i := 3;  END_IF;
> BoardNG[i] := TRUE;
> ```
>
> Một số hệ có kiểm tra dải tự động; **đừng dựa vào đó** — nó không có ở mọi hệ, và có hệ chỉ bật khi
> biên dịch ở chế độ gỡ lỗi.

---

## 19.8 Trên máy mẫu DP-01

### Tính thời gian chu trình và hiệu suất

```iecst
VAR
    TrigDone : F_TRIG;
END_VAR

TrigDone(CLK := DI_BoardStn2);

IF TrigDone.Q THEN
    // Thời gian chu trình: đơn vị mili-giây, dùng DINT để không tràn
    LastCycleMs := CurrentTimeMs - LastBoardTimeMs;
    LastBoardTimeMs := CurrentTimeMs;

    TotalCycleMs := TotalCycleMs + LastCycleMs;
    DoneCount    := DoneCount + 1;

    // ⚠ Luôn kiểm mẫu số — DoneCount bằng 0 ở board đầu tiên của ca
    IF DoneCount > 0 THEN
        AvgCycleMs := TotalCycleMs / DoneCount;
    ELSE
        AvgCycleMs := 0;
    END_IF;

    // Hiệu suất: nhân trước rồi chia, và làm việc với DINT
    IF TotalOut > 0 THEN
        YieldPctX10 := (OkCount * 1000) / TotalOut;   // đơn vị phần mười %
    ELSE
        YieldPctX10 := 0;
    END_IF;
END_IF;
```

Ba kỹ thuật của chương nằm gọn trong đoạn này: kiểm mẫu số trước khi chia, nhân trước khi chia, và
dùng đơn vị nhỏ (`X10`) thay cho số thực. Tên biến mang đơn vị nên người đọc sau không quy đổi nhầm.

### Cảnh báo chu kỳ chậm dần — có trễ

```iecst
// Chu kỳ chuẩn theo công thức sản phẩm, cảnh báo khi vượt 20 %
WarnLimitMs  := (RecipeCycleMs * 120) / 100;
ClearLimitMs := (RecipeCycleMs * 110) / 100;

IF AvgCycleMs > WarnLimitMs THEN
    M_CycleSlowWarn := TRUE;
ELSIF AvgCycleMs < ClearLimitMs THEN
    M_CycleSlowWarn := FALSE;
END_IF;
```

Chu kỳ chậm dần là dấu hiệu sớm của rất nhiều thứ: bộ lọc khí bẩn, xy-lanh mòn, cảm biến đáp ứng
chậm. Phát hiện nó bằng con số **trước khi** nó thành sự cố là một trong những giá trị lớn nhất mà
việc tính toán trong PLC mang lại (Chương 51, Chương 55).

---

## 19.9 Khác biệt giữa các hãng

| Điểm | Điều cần biết |
|---|---|
| ⚠⚠ **Chia cho 0** | Khác nhau **nhiều nhất** và hậu quả nặng nhất — có hệ chuyển CPU sang STOP. Phải tra tài liệu đúng hệ, và dù kết quả thế nào vẫn luôn kiểm mẫu số |
| ⚠ REAL → INT | Cắt hay làm tròn tuỳ hệ và tuỳ lệnh. Dùng hàm ép kiểu **tường minh** thay vì gán ngầm |
| Hành vi khi tràn | Phần lớn quay vòng im lặng; một số hệ đặt bit trạng thái. Đừng dựa vào bit đó nếu chưa xác nhận |
| Tên kiểu dữ liệu | Chuẩn dùng `INT`/`DINT`/`REAL`; các hãng có tên riêng và dải hơi khác — kiểm dải, không suy từ tên |
| Kiểm tra dải mảng | Có hệ kiểm tự động, có hệ không, có hệ chỉ kiểm khi gỡ lỗi. **Luôn tự kẹp chỉ số** |
| Lệnh thanh ghi dịch sẵn có | Nhiều hệ có lệnh dịch bit chuyên dụng, nhanh và gọn hơn vòng `FOR`. Tra Phụ lục A |

---

## 19.10 Bẫy thường gặp

### 🔍 BẪY 1 — Chia cho biến mà không kiểm mẫu số

**Hiện tượng:** máy chạy ổn nhiều ngày rồi dừng đột ngột ngay đầu ca — đúng lúc số đếm vừa được xoá.
Tuỳ hệ, CPU có thể chuyển sang STOP.
**Cách sửa:** bọc mọi phép chia bằng phép kiểm khác 0 (mục 19.5). Không có ngoại lệ.

### 🔍 BẪY 2 — So sánh bằng với số thực

**Hiện tượng:** điều kiện "không bao giờ đúng", dù giá trị hiển thị trên màn hình đúng bằng con số
mong đợi.
**Cách sửa:** so sánh trong dải dung sai, hoặc chuyển sang số nguyên đơn vị nhỏ.

### 🔍 BẪY 3 — Chia trước khi nhân khi tính phần trăm

**Hiện tượng:** hiệu suất luôn là 0 % hoặc 100 %, không bao giờ có giá trị ở giữa.
**Cách sửa:** nhân trước rồi chia — và kiểm kiểu dữ liệu có chứa nổi kết quả trung gian không.

### 🔍 BẪY 4 — Tràn `INT` khi tính thời gian bằng mili-giây

32 767 ms chỉ là 33 giây.

**Hiện tượng:** thời gian tích luỹ nhảy sang số âm sau chưa tới một phút.
**Cách sửa:** dùng `DINT` cho mọi phép tính thời gian tích luỹ.

### 🔍 BẪY 5 — Dịch thanh ghi sai chiều

**Hiện tượng:** một board lỗi làm **mọi** board phía sau bị loại. Rất dễ chẩn đoán nhầm thành "cảm
biến kiểm tra hỏng" hoặc "trạm 1 có vấn đề".
**Cách sửa:** vòng lặp dịch chạy từ chỉ số lớn về chỉ số nhỏ (mục 19.6).

### 🔍 BẪY 6 — Dịch thanh ghi theo timer

**Hiện tượng:** thỉnh thoảng board tốt bị loại còn board lỗi lọt qua, và sai lệch **không tự khỏi**
mà tích luỹ dần.
**Cách sửa:** dịch theo tín hiệu xác nhận chuyền đã tiến; thêm bước đồng bộ khi máy xả hết.

### 🔍 BẪY 7 — Chỉ số mảng không được kẹp trong dải

**Hiện tượng:** hỏng hóc ở một chỗ **hoàn toàn không liên quan** tới đoạn code có lỗi — vì vùng nhớ
của biến khác bị ghi đè. Hoặc CPU chuyển sang STOP.
**Cách sửa:** kẹp mọi chỉ số đến từ tính toán (mục 19.7).

### 🔍 BẪY 8 — MOVE chạy mỗi vòng quét khi nạp tham số

**Hiện tượng:** người vận hành sửa một tham số trên màn hình, giá trị **nhảy về giá trị cũ ngay lập
tức**, và không ai hiểu vì sao.
**Cách sửa:** bắt cạnh điều kiện nạp, hoặc chỉ nạp khi thật sự đổi mã hàng (Chương 29).

### 🔍 BẪY 9 — Đơn vị ngầm hiểu trong tên biến

`Length` là mi-li-mét hay phần mười mi-li-mét? `CycleTime` là giây hay mili-giây?

**Hiện tượng:** sai số gấp 10, 100 hoặc 1000 lần ở một phép quy đổi, thường phát hiện rất muộn.
**Cách sửa:** đưa đơn vị vào tên: `LengthTenthMm`, `CycleTimeMs`, `YieldPctX10`. Quy ước này tốn vài
ký tự và loại hẳn một nhóm lỗi (Chương 30).

---

## 19.11 Bảng chốt

| Việc | Quy tắc | Vì sao |
|---|---|---|
| Chia | **Luôn kiểm mẫu số khác 0** | Có hệ chuyển CPU sang STOP |
| Tính phần trăm | **Nhân trước, chia sau** | Chia số nguyên cắt hết phần lẻ |
| Kết quả trung gian | Kiểm dải kiểu dữ liệu | Tràn xảy ra trước khi chia kịp thu nhỏ lại |
| Thời gian tích luỹ | **`DINT`**, không dùng `INT` | 32 767 ms = 33 giây |
| So sánh số thực | **Không dùng `=`** — so trong dung sai | Dấu chấm động không biểu diễn chính xác |
| Giá trị có phần lẻ | Số nguyên đơn vị nhỏ + **đơn vị trong tên biến** | Loại hẳn sai số dấu chấm động |
| Ngưỡng cảnh báo | Có **trễ** (bật/tắt hai ngưỡng) | Chống nhấp nháy quanh ngưỡng |
| Theo dõi sản phẩm dọc chuyền | **Thanh ghi dịch**, dịch theo sự kiện thật | Thông tin phải đi cùng sản phẩm |
| Vòng lặp dịch | Từ chỉ số **lớn về nhỏ** | Ngược lại thì nhân bản giá trị ra cả mảng |
| Chỉ số mảng | **Luôn kẹp trong dải** | Vượt dải: STOP hoặc ghi đè vùng nhớ khác |
| Nạp tham số | **Bắt cạnh**, không nạp mỗi vòng quét | Ghi đè thay đổi của người vận hành |

---

## 19.12 Tự kiểm

1. `7 / 2` trong phép chia số nguyên cho kết quả bằng mấy? Vì sao không phải `3.5` và cũng không phải `4`?
2. ⭐ Nêu ba hậu quả khác nhau mà chia cho 0 có thể gây ra trên PLC. Hậu quả nào nguy hiểm nhất và
   vì sao?
3. Vì sao `IF ActualLength = 12.5 THEN` gần như không bao giờ đúng? Viết lại cho đúng.
4. `OkCount = 1187`, `TotalCount = 1240`, cả hai là `INT`. Tính `(OkCount * 100) / TotalCount` gặp vấn
   đề gì? Nêu hai cách chữa.
5. Một biến `INT` đang chứa 32 767, cộng thêm 1. Kết quả bằng mấy ở phần lớn hệ, và có báo lỗi không?
6. ⭐ Giải thích bài toán "board lỗi phát hiện ở trạm đầu, loại bỏ ở cuối chuyền" và vì sao một bit cờ
   không giải quyết được.
7. Trong vòng lặp dịch thanh ghi, vì sao phải chạy từ chỉ số lớn về nhỏ? Mô tả **triệu chứng trên
   máy** nếu làm ngược.
8. Vì sao thanh ghi dịch phải được kích bằng tín hiệu xác nhận chuyền tiến, không phải bằng timer?
9. Nêu hai lý do nên dùng số nguyên đơn vị phần mười mi-li-mét thay cho số thực mi-li-mét.
10. ⭐ Chỉ số mảng vượt dải có thể gây hỏng hóc ở một chỗ hoàn toàn không liên quan. Cơ chế nào dẫn tới
    chuyện đó, và vì sao lỗi kiểu này đặc biệt khó tìm?

> Câu 2, 6 và 10 là ba câu phân loại. Câu 6 là tinh thần của cả chương: **khi dữ liệu phải đi cùng
> sản phẩm, một biến không đủ — cần một cấu trúc có vị trí.**

---

### Chương tiếp theo

Chương 20 — **Structured Text**. Phần lớn ví dụ trong sách này đã viết bằng ST; chương sau nói kỹ về
nó: cú pháp đầy đủ, vòng lặp và mối nguy treo CPU, khi nào ST vượt trội ladder, và ⭐ khi nào chọn ST
là quyết định **tệ** dù nó gọn hơn.

### Nguồn tham khảo chương 19

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: các kiểu dữ liệu cơ bản,
  phép toán, phép so sánh, hàm ép kiểu và quy tắc về dải giá trị. *(tiêu chuẩn có bản quyền)*
- Tài liệu lập trình của từng hệ trong Phụ lục A — dùng cho hành vi khi **chia cho 0**, khi **tràn
  số**, và cho quy tắc làm tròn khi ép kiểu `REAL` → `INT`. Ba điểm này khác nhau giữa các hãng ở mức
  đủ để đổi kết quả, nên **phải tra theo đúng hệ đang dùng**, không suy từ hệ khác.
- Đặc tả trình tự và bảng công thức sản phẩm của DP-01 — Phụ lục J.

> ⚡ Quy tắc "dùng số nguyên đơn vị nhỏ thay cho số thực" ở mục 19.5 là **thực hành phổ biến trong
> ngành**, không phải yêu cầu tiêu chuẩn. Nó đánh đổi sự tiện lợi lấy tính xác định — hợp lý với máy
> điều khiển rời rạc, nhưng khi sang tính toán analog và điều khiển vòng kín (Chương 32, Chương 35)
> thì số thực lại là lựa chọn đúng.
