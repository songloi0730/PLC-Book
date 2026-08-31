# Chương 26 — Thiết kế theo lưu đồ & bit trình tự

> **Lát cắt máy mẫu:** 2 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp, hai trạm, trình
> tự song song, công thức sản phẩm.

---

## 26.1 Bài toán: máy đứng im, không báo gì

DP-01 đang chạy sản xuất. Đột nhiên nó **dừng lại**. Đèn xanh vẫn sáng — máy vẫn ở trạng thái `Running`.
Không có báo động. Không có gì trên màn hình. Chuyền không chạy, kẹp không động, board nằm im.

Kỹ thuật viên tới. Mở phần mềm, xem trực tuyến. Chương trình đang chạy bình thường, thời gian quét bình
thường, không có lỗi CPU. Máy chỉ đơn giản là **không làm gì cả**.

Mất bốn mươi phút để tìm ra: trình tự đang kẹt ở bước chờ `DI_Clamp1Up`. Cảm biến reed trên xy-lanh kẹp
bị lỏng vít, tụt ra khỏi rãnh. Kẹp đã lên thật, nhưng cảm biến không báo. Trình tự chờ một tín hiệu
sẽ **không bao giờ tới**, và nó sẵn sàng chờ như vậy tới hết ca.

Bốn mươi phút đó là **hoàn toàn tránh được**. Nếu mỗi bước có thời gian tối đa, màn hình đã hiện ngay
từ giây thứ ba: *"Bước S1.40 quá thời gian — chờ DI_Clamp1Up"*. Kỹ thuật viên đi thẳng tới cảm biến,
siết vít, hai phút xong.

Chương này dạy cách xây trình tự — và bài học ở trên là **quy tắc trung tâm của nó**.

---

## 26.2 Từ lưu đồ tới bit bước

Chương 25 cho máy các **chế độ**. Bên trong chế độ `Running` là một **chu trình** gồm hàng chục bước
nối tiếp nhau. Đó là thứ chương này xây.

### Bắt đầu bằng lưu đồ, không bằng code

**Lưu đồ** *(flowchart)* là cách rẻ nhất để phát hiện thiếu sót. Vẽ bằng bút mất năm phút; sửa một sai
lầm trong code đã viết mất nửa ngày.

Lưu đồ cho trạm 1 của DP-01, dạng đơn giản nhất:

```
      ┌─────────────┐
      │  Chờ board  │◄────────────────┐
      └──────┬──────┘                 │
             │ DI_BoardStn1 = 1       │
      ┌──────▼──────┐                 │
      │  Nâng chặn  │                 │
      └──────┬──────┘                 │
             │ DI_Stop1Up = 1         │
      ┌──────▼──────┐                 │
      │   Nâng kẹp  │                 │
      └──────┬──────┘                 │
             │ DI_Clamp1Up = 1        │
      ┌──────▼──────┐                 │
      │  Xử lý board│                 │
      └──────┬──────┘                 │
             │ xong                   │
      ┌──────▼──────┐                 │
      │   Hạ kẹp    │                 │
      └──────┬──────┘                 │
             │ DI_Clamp1Dn = 1        │
      ┌──────▼──────┐                 │
      │ Chờ trạm 2  │                 │
      │   sẵn sàng  │                 │
      └──────┬──────┘                 │
             │ Stn2_Ready = 1         │
      ┌──────▼──────┐                 │
      │  Hạ chặn,   │                 │
      │ chuyển board│─────────────────┘
      └─────────────┘
```

Hai thứ cần chú ý ngay trên lưu đồ này:

- **Mỗi mũi tên có một điều kiện**, và điều kiện đó là **tín hiệu phản hồi thật** — `DI_Stop1Up`,
  `DI_Clamp1Up` — chứ không phải một khoảng thời gian. Đây là nguyên tắc từ Chương 17, và nó quyết
  định trình tự có đáng tin hay không.
- **Bước "Chờ trạm 2 sẵn sàng"** đọc `Stn2_Ready` — giao diện công bố của trạm 2, không phải biến nội
  bộ của nó (Chương 27).

### Chuyển lưu đồ thành bit bước

Mỗi ô trong lưu đồ thành một **bước** *(step)*. Có hai cách lưu bước đang chạy, và chúng có cùng bản
chất với hai cách ở Chương 25:

| | **Biến số bước** | **Bit bước** |
|---|---|---|
| Lưu bằng | Một biến số nguyên `Stn1_Step` | Mỗi bước một bit `S1_10`, `S1_20`… |
| Bất biến "một bước" | Được bảo đảm | Phải tự cưỡng chế |
| Hợp với | Structured Text | Ladder |

Với biến số bước, mã bước nên **cách nhau 10** để về sau chèn thêm bước mà không phải đánh số lại:

```
0   — chờ board
10  — nâng chặn
20  — nâng kẹp
30  — xử lý board
40  — hạ kẹp
50  — chờ trạm 2
60  — hạ chặn, chuyển board
```

Cần chèn một bước giữa 20 và 30? Dùng 25. Không phải sửa gì khác.

### Quy tắc bất biến của trình tự

> **Một bước bật thì mọi bước khác tắt.**
>
> Với biến số bước, điều này tự nhiên đúng. Với bit bước, mỗi chuyển tiếp phải **bật bit mới và tắt
> bit cũ trong cùng một nấc thang** — giống hệt quy tắc ở Chương 25, và cũng cần một nấc giám sát
> đếm số bit đang bật.

---

## 26.3 Trên máy mẫu DP-01

Trình tự trạm 1, viết bằng biến số bước:

```
// ── Trình tự trạm 1 — chỉ chạy khi tầng máy cho phép (Chương 27) ──
IF NOT M_CycleEnable THEN
    RETURN;                                   // giữ nguyên bước, không tiến
END_IF;

CASE Stn1_Step OF

  0:  // Chờ board tới
      Stn1_Ready := TRUE;                     // giao diện công bố
      Stn1_Busy  := FALSE;
      IF DI_BoardStn1 OR M_DryRun THEN
          Stn1_Ready := FALSE;
          Stn1_Busy  := TRUE;
          Stn1_Step  := 10;
      END_IF;

 10:  // Nâng chặn
      M_Stn1_StopReq := TRUE;                 // yêu cầu, khối cơ cấu thực hiện
      IF Stop1.Done THEN
          Stn1_Step := 20;
      END_IF;

 20:  // Nâng kẹp
      M_Stn1_ClampReq := TRUE;
      IF Clamp1.Done THEN
          Stn1_Step := 30;
      END_IF;

 30:  // Xử lý board  (nội dung xử lý ở lát cắt sau)
      IF M_Stn1_ProcessDone THEN
          Stn1_Step := 40;
      END_IF;

 40:  // Hạ kẹp
      M_Stn1_ClampReq := FALSE;
      IF Clamp1.Done THEN
          Stn1_Step := 50;
      END_IF;

 50:  // Chờ trạm 2 sẵn sàng  ← điểm đồng bộ giữa hai trạm
      Stn1_BoardDone := TRUE;
      IF Stn2_Ready THEN
          Stn1_Step := 60;
      END_IF;

 60:  // Hạ chặn, chuyển board sang
      M_Stn1_StopReq  := FALSE;
      M_Stn1_ConvReq  := TRUE;                // yêu cầu chuyền chạy
      IF NOT DI_BoardStn1 THEN
          M_Stn1_ConvReq  := FALSE;
          Stn1_BoardDone  := FALSE;
          Stn1_Step       := 0;               // quay lại chờ board mới
      END_IF;

END_CASE;
```

Ba điểm thiết kế trong đoạn trên, mỗi cái đều nối tới một chương khác:

- **Không có dòng nào ghi `DO_…`** — trạm chỉ nêu yêu cầu, khối cơ cấu thực hiện (Chương 27, quy tắc Q3).
- **Mọi chuyển tiếp dùng phản hồi thật** — `Stop1.Done`, `DI_BoardStn1` — không dùng timer (Chương 17).
- **Cờ `M_DryRun` ở bước 0** cho phép chạy khô không có board (Chương 28).

Nhưng đoạn code trên vẫn **chưa xong**. Nó thiếu đúng thứ đã gây ra sự cố ở mục 26.1.

---

## 26.4 Timeout từng bước — cơ chế báo lỗi, không phải cơ chế điều khiển

Đây là mục quan trọng nhất của chương.

### Nguyên tắc

> **Mỗi bước phải có thời gian tối đa. Quá thời gian → báo lỗi, nêu rõ kẹt ở bước nào và chờ gì.**
>
> Timeout **không** dùng để chuyển bước. Nó chỉ dùng để **phát hiện rằng chuyển tiếp đã không xảy ra**.

Phân biệt này quyết định trình tự có an toàn hay không:

| | Timeout **báo lỗi** ✓ | Timeout **chuyển bước** ✗ |
|---|---|---|
| Khi cơ cấu chậm bất thường | Báo lỗi, dừng máy, người xử lý | **Đi tiếp như không có gì** |
| Khi cảm biến hỏng | Báo rõ cảm biến nào | Đi tiếp, máy làm việc trên giả định sai |
| Khi cơ cấu kẹt cơ khí | Báo lỗi, tránh làm hỏng thêm | Bước sau tác động lên cơ cấu đang kẹt |

Cột phải chính là sai lầm ở Chương 17: *"chờ 2 giây chắc kẹp xong rồi"*. Nó biến một cơ chế phát hiện
lỗi thành một cơ chế **giấu lỗi**.

### Cách hiện thực — một bộ đếm dùng chung

Không cần một timer cho mỗi bước. Một timer dùng chung, tự đặt lại mỗi khi bước đổi:

```
VAR
    Stn1_StepPrev  : INT;
    T_StepTimeout  : TON;
    Stn1_StepLimit : TIME;
END_VAR

// ── Đặt lại timer mỗi khi bước thay đổi ──
IF Stn1_Step <> Stn1_StepPrev THEN
    T_StepTimeout(IN := FALSE);               // xoá timer
    Stn1_StepPrev := Stn1_Step;
END_IF;

// ── Thời gian cho phép của từng bước ──
CASE Stn1_Step OF
    0:   Stn1_StepLimit := T#0S;              // 0 = không giới hạn (chờ board)
   10:   Stn1_StepLimit := T#3S;              // nâng chặn
   20:   Stn1_StepLimit := T#3S;              // nâng kẹp
   30:   Stn1_StepLimit := T#60S;             // xử lý board
   40:   Stn1_StepLimit := T#3S;              // hạ kẹp
   50:   Stn1_StepLimit := T#0S;              // chờ trạm 2 — không giới hạn
   60:   Stn1_StepLimit := T#10S;             // chuyển board đi
END_CASE;

// ── Chạy timer và báo lỗi ──
T_StepTimeout(IN := (Stn1_StepLimit > T#0S), PT := Stn1_StepLimit);

IF T_StepTimeout.Q THEN
    Stn1_FaultStep := Stn1_Step;              // GHI LẠI bước bị kẹt
    Stn1_Fault     := TRUE;
    M_AnyFault     := TRUE;
END_IF;
```

### Hai bước cố ý **không** đặt giới hạn

Bước 0 (chờ board) và bước 50 (chờ trạm 2) đặt `T#0S` — nghĩa là chờ vô hạn. Đây là **quyết định có
chủ ý**, không phải bỏ sót:

- **Bước 0** chờ board từ máy trước. Không có board là chuyện bình thường — máy trước có thể đang thay
  lô. Báo lỗi ở đây là báo động giả.
- **Bước 50** chờ trạm 2 xong. Trạm 2 chậm hơn là chuyện bình thường trong pipeline (Chương 27).

Nhưng chờ vô hạn có rủi ro riêng, nên cần **giám sát ở tầng khác**: nếu máy không cho ra sản phẩm nào
trong một khoảng thời gian dài, tầng máy báo *"máy đứng chờ"* — một cảnh báo mức thấp, không phải lỗi
dừng máy. Cách này phân biệt được **chờ hợp lệ** với **kẹt thật**.

> 💡 **MẸO — thông báo lỗi phải nói ba điều**
> Không đủ: *"Lỗi trạm 1"*. Đủ: **bước nào · đang chờ gì · nên kiểm tra gì**.
>
> ```
> "S1.20 quá thời gian (3 giây) — chờ DI_Clamp1Up.
>  Kiểm tra: cảm biến reed kẹp trạm 1, áp suất khí, xy-lanh có kẹt không."
> ```
>
> Dòng thứ hai biến bốn mươi phút mò mẫm thành hai phút. Việc viết nó tốn ba mươi giây.

---

## 26.5 Nhánh song song và điểm hợp nhất

Đôi khi hai việc chạy được **cùng lúc** — làm song song thì chu kỳ ngắn hơn.

Ví dụ ở DP-01: sau khi xử lý xong, có thể **hạ kẹp** và **thông báo cho trạm 2** cùng lúc, thay vì làm
tuần tự.

### Cách viết nhánh song song

Tách thành hai chuỗi bước độc lập, mỗi chuỗi một biến bước riêng, rồi **hợp nhất** khi cả hai xong:

```
// Nhánh A: hạ kẹp
CASE Stn1_BranchA OF
   0:  IF M_ParallelStart THEN Stn1_BranchA := 10; END_IF;
  10:  M_Stn1_ClampReq := FALSE;
       IF Clamp1.Done THEN Stn1_BranchA := 99; END_IF;    // 99 = nhánh xong
END_CASE;

// Nhánh B: chuẩn bị dữ liệu cho trạm 2
CASE Stn1_BranchB OF
   0:  IF M_ParallelStart THEN Stn1_BranchB := 10; END_IF;
  10:  Stn1_ResultData := …;
       Stn1_BranchB := 99;
END_CASE;

// ── Điểm hợp nhất: chờ CẢ HAI nhánh xong ──
IF Stn1_BranchA = 99 AND Stn1_BranchB = 99 THEN
    Stn1_BranchA := 0;
    Stn1_BranchB := 0;
    Stn1_Step    := 50;
END_IF;
```

> ⚡ **LƯU Ý — đừng song song hoá thứ không cần**
> Nhánh song song làm code khó đọc và khó gỡ lỗi hơn hẳn. Chỉ dùng khi **đo được** rằng nó rút ngắn
> chu kỳ đáng kể (Chương 55). Song song hoá hai bước mỗi bước 200 ms trong một chu kỳ 12 giây là công
> sức bỏ đi.

---

## 26.6 Bế tắc

**Bế tắc** *(deadlock)* là tình huống hai bên cùng chờ nhau, và không bên nào tiến được.

Ở máy nhiều trạm, dạng phổ biến nhất:

```
Trạm 1 ở bước 50:  "chờ trạm 2 sẵn sàng"   →  chờ  Stn2_Ready
Trạm 2 ở bước 0:   "chờ board tới"          →  chờ  DI_BoardStn2
```

Nghe có vẻ ổn — trạm 2 chờ board, trạm 1 sẽ gửi board sang. Nhưng nếu ai đó viết trạm 2 công bố
`Stn2_Ready` **chỉ khi đã có board** (nhầm "sẵn sàng" thành "đang bận"), thì:

- Trạm 1 chờ `Stn2_Ready` — không lên vì trạm 2 chưa có board.
- Trạm 2 chờ board — không tới vì trạm 1 đang chờ.

**Cả hai đứng im vĩnh viễn**, và cả hai đều ở bước "chờ không giới hạn" nên không báo lỗi. Đây chính
là dạng nguy hiểm nhất: máy im lặng.

### Ba biện pháp, dùng cả ba

**Một — định nghĩa giao diện cho đúng.** `Stn2_Ready` phải nghĩa là *"tôi trống và nhận được board
mới"*, và phải **bằng TRUE khi trạm 2 rỗng**. Sai nghĩa ở đây là gốc của bế tắc trên.

**Hai — giám sát "máy đứng chờ" ở tầng máy.** Đã nêu ở mục 26.4: nếu không sản phẩm nào ra trong một
khoảng dài, báo cảnh báo kèm **trạng thái mọi trạm**:

```
"Máy đứng chờ 120 giây.  Trạm 1: bước 50 (chờ trạm 2).  Trạm 2: bước 0 (chờ board)."
```

Một dòng như vậy làm bế tắc **lộ ngay ra**, thay vì phải đi tìm.

**Ba — vẽ đồ thị chờ khi thiết kế.** Với mỗi bước chờ, vẽ mũi tên tới thứ nó đang chờ. **Nếu đồ thị có
vòng kín, bạn có bế tắc tiềm tàng** — kể cả khi nó chưa xảy ra trong thử nghiệm. Cách kiểm này làm
được trên giấy, trước khi viết code.

---

## 26.7 Bẫy thường gặp

### 🔍 BẪY 1 — Bước không có timeout

Bẫy trung tâm của chương, đã mổ xẻ ở mục 26.4. Nhắc lại vì nó là bẫy hay gặp nhất và tốn thời gian
nhất: **mọi bước chờ cơ cấu phải có giới hạn thời gian**, và mọi bước cố ý chờ vô hạn phải được giám
sát ở tầng máy.

### 🔍 BẪY 2 — Dùng timeout để chuyển bước

```
// ✗ SAI — timer thay cho phản hồi
IF T_Wait.Q THEN
    Stn1_Step := 30;         // "chắc kẹp lên rồi"
END_IF;
```

Trình tự này chạy đúng khi mọi thứ bình thường, và **hỏng âm thầm** khi cơ cấu chậm hoặc kẹt. Bước sau
sẽ tác động lên một cơ cấu chưa ở đúng vị trí.

```
// ✓ ĐÚNG — phản hồi để chuyển, timeout để báo lỗi
IF Clamp1.Done THEN
    Stn1_Step := 30;
END_IF;
// timeout xử lý riêng, đặt Stn1_Fault
```

### 🔍 BẪY 3 — Đánh số bước liền nhau

Đánh 1, 2, 3, 4… rồi cần chèn một bước giữa 2 và 3. Bạn phải đánh số lại toàn bộ, và mọi tham chiếu
tới số bước — trong thông báo lỗi, trong màn hình, trong tài liệu — đều sai.

Đánh cách 10 ngay từ đầu. Chi phí bằng không, lợi ích rất lớn.

### 🔍 BẪY 4 — Không ghi lại bước bị kẹt

Trình tự báo lỗi rồi **đặt lại bước về 0**. Thông tin quan trọng nhất — kẹt ở bước nào — mất luôn.

Luôn có một biến `Stn1_FaultStep` giữ lại bước lúc xảy ra lỗi, và biến đó **chỉ được xoá khi Reset**.
Đây là phiên bản thu nhỏ của "chụp ảnh trạng thái lúc sự cố" ở Chương 28.

### 🔍 BẪY 5 — Trình tự tự chạy khi máy không cho phép

Đoạn code ở mục 26.3 mở đầu bằng:

```
IF NOT M_CycleEnable THEN
    RETURN;
END_IF;
```

Thiếu ba dòng đó thì trình tự **vẫn chạy khi máy đang `Alarm` hoặc `Hold`** — vì máy trạng thái ở tầng
trên không tự chặn được tầng dưới. Đây là ứng dụng của quy tắc Q1 ở Chương 27: tầng trên *cho phép*,
tầng dưới *phải kiểm tra sự cho phép đó*.

Chú ý `RETURN` **giữ nguyên bước**, không đặt về 0. Nhờ vậy khi được phép chạy lại, trình tự tiếp tục
đúng chỗ — đó là điều làm `Hold` khác `Stop` (Chương 25).

### 🔍 BẪY 6 — Nhánh song song không hợp nhất đúng

Điểm hợp nhất kiểm `BranchA = 99 OR BranchB = 99` thay vì `AND`. Trình tự đi tiếp khi mới một nhánh
xong. Lỗi này chạy đúng phần lớn thời gian — vì thường một nhánh xong sớm hơn hẳn — và hỏng vào đúng
lần nhánh kia chậm bất thường.

Điểm hợp nhất **luôn dùng `AND`**, và bản thân nó cũng phải có timeout.

---

## 26.8 Bảng chốt — kiểm tra một trình tự

| # | Câu hỏi | Đạt khi |
|---|---|---|
| 1 | Đã vẽ lưu đồ **trước khi** viết code chưa? | Có, trên giấy |
| 2 | Mọi chuyển tiếp dùng **phản hồi thật**, không dùng timer? | Có |
| 3 | Mọi bước chờ cơ cấu có **timeout**? | Có |
| 4 | Bước chờ vô hạn có được **giám sát ở tầng máy**? | Có |
| 5 | Thông báo lỗi nói được **bước nào · chờ gì · kiểm tra gì**? | Đủ ba |
| 6 | Số bước đánh **cách 10**? | Có |
| 7 | Có biến giữ **bước bị kẹt** lúc lỗi? | Có, chỉ xoá khi Reset |
| 8 | Trình tự có kiểm **tầng máy cho phép** trước khi tiến bước? | Có, và `RETURN` giữ nguyên bước |
| 9 | Điểm hợp nhất nhánh song song dùng **AND**? | Có |
| 10 | Đã vẽ **đồ thị chờ** và kiểm không có vòng kín? | Có |

---

## 26.9 Tự kiểm

1. Kể lại sự cố ở mục 26.1. **Một thay đổi nhỏ nào** đã có thể biến bốn mươi phút thành hai phút?
2. Vì sao timeout là **cơ chế báo lỗi** chứ không phải cơ chế chuyển bước? Nêu hậu quả cụ thể khi dùng
   sai.
3. Vì sao bước 0 và bước 50 của DP-01 cố ý **không** đặt giới hạn thời gian? Rủi ro của quyết định đó
   được bù bằng cách nào?
4. Vì sao đánh số bước cách 10 thay vì liền nhau?
5. Mô tả tình huống **bế tắc** ở mục 26.6 và chỉ ra **định nghĩa giao diện sai** đã gây ra nó.
6. Bạn có một bước chờ vô hạn hợp lệ và một bước bị kẹt thật. **Làm sao phân biệt** hai tình huống này
   từ bên ngoài?
7. Vì sao `RETURN` khi máy không cho phép lại **giữ nguyên bước** thay vì đặt về 0?
8. Điểm hợp nhất nhánh song song dùng `OR` thay vì `AND`. Vì sao lỗi này **khó phát hiện khi thử nghiệm**?

Câu 2 và câu 6 là hai câu phân loại. Câu 2 là nguyên tắc trung tâm của chương; câu 6 kiểm tra bạn hiểu
rằng "chờ" và "kẹt" nhìn từ ngoài **giống hệt nhau**, nên phải thiết kế cách phân biệt.

---

### Chương tiếp theo

**Chương 27 — Kiến trúc chương trình cho máy nhiều trạm.** Trình tự một trạm đã xong. Nhưng DP-01 có
hai trạm chạy song song, dùng chung một chuyền — và chương này đã nhắc tới `Stn2_Ready`, `M_CycleEnable`,
`Clamp1.Done` mà chưa nói chúng từ đâu ra. Chương 27 xây phần đó.

---

### Nguồn tham khảo chương 26

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: ngôn ngữ SFC (bước, chuyển
  tiếp, nhánh song song và nhánh lựa chọn) — mô hình khái niệm cho chương này; lệnh `CASE` và khối
  `TON`. *(tiêu chuẩn có bản quyền; chương này chỉ diễn giải ở mức khái niệm)*
- Đặc tả trình tự hai trạm và bảng thời gian bước của DP-01 — Phụ lục J.

> ⚡ Các con số thời gian trong chương (3 giây cho hành trình xy-lanh, 60 giây cho bước xử lý) là **giá
> trị minh hoạ của máy mẫu**. Thời gian thật phải đo trên máy của bạn rồi cộng biên an toàn — đặt quá
> chặt thì báo động giả, đặt quá lỏng thì mất tác dụng phát hiện.
