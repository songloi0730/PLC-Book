# Chương 41 — Ghép nối máy–máy trong dây chuyền

> **Lát cắt máy mẫu:** 4 — thêm mạng: mã 2D, MES, SMEMA, màn hình vận hành, và bộ điều khiển nhiệt độ
> keo nối RS-485.

---

## 41.1 Bài toán: hai board trên cùng một chỗ

DP-01 nhận board từ máy phía trước. Bắt tay giữa hai máy được viết đơn giản: máy trước báo "có board
sẵn sàng", DP-01 chạy chuyền vào để nhận.

Một sáng, hai board **chồng lên nhau** ở đầu chuyền vào. Board dưới bị đè, hỏng. Cơ cấu chặn kẹt.

Dựng lại sự việc: máy trước đẩy board sang, DP-01 nhận. Nhưng tín hiệu "đã nhận xong" của DP-01 lên
**muộn hơn** một chút so với lúc board thật sự rời khỏi máy trước. Trong khoảng thời gian đó, máy
trước — thấy vùng ra của mình đã trống — đã đẩy board tiếp theo.

**Cả hai máy đều hoạt động đúng theo chương trình của mình.** Không máy nào có lỗi. Vấn đề nằm ở
khoảng giữa: có một thời điểm mà **cả hai máy đều tưởng mình đang không giữ board nào**.

Chương này về việc ghép hai máy lại — và về câu hỏi phải trả lời trước mọi câu khác: **ai đang giữ
sản phẩm.**

---

## 41.2 Vì sao chuyện này quan trọng hơn nó có vẻ

Máy lắp ráp điện tử gần như **không bao giờ đứng một mình**. Nó nằm trong một chuyền: máy trước đẩy
sang, máy sau nhận đi. Một chuyền điển hình có năm tới hai mươi máy nối tiếp.

Ba hệ quả:

| Hệ quả | Nội dung |
|---|---|
| ⭐ **Máy của bạn phải ghép được với máy hãng khác** | Bạn không chọn được máy hàng xóm |
| **Một máy dừng là cả chuyền dừng** | Máy sau hết hàng, máy trước bị dồn |
| ⭐ **Lỗi bắt tay gây hỏng sản phẩm vật lý** | Đúng cỗ máy ở mục 41.1 — không phải chỉ mất thời gian |

> ⭐ **Gạch đầu dòng đầu tiên định hình mọi thứ trong chương này.**
> Bắt tay phải **đơn giản tới mức hai máy của hai hãng khác nhau, thiết kế cách nhau mười năm, vẫn
> nối được**. Đó là lý do các chuẩn bắt tay trong ngành đều dùng **rất ít tín hiệu**, và dùng **tín
> hiệu số** chứ không dùng mạng.

---

## 41.3 ⭐ Bắt tay kiểu SMEMA — hai tín hiệu mỗi chiều

**SMEMA** là chuẩn bắt tay phổ biến nhất trong lắp ráp điện tử. Nó đơn giản tới mức gây bất ngờ, và
sự đơn giản đó chính là lý do nó thành công.

### Bốn tín hiệu

Giữa hai máy kề nhau, chỉ có **hai tín hiệu mỗi chiều**:

```text
   ┌─────────────┐                            ┌─────────────┐
   │  MÁY TRƯỚC  │                            │  MÁY SAU    │
   │  (upstream) │                            │ (downstream)│
   │             │  ──── Board Available ───► │             │
   │             │      "tôi có board sẵn"    │             │
   │             │                            │             │
   │             │  ◄─── Machine Ready ────── │             │
   │             │      "tôi sẵn sàng nhận"   │             │
   └─────────────┘                            └─────────────┘
```

| Tín hiệu | Ai phát | Nghĩa |
|---|---|---|
| ⭐ **Board Available** | Máy **trước** | "Tôi có board sẵn sàng chuyển sang" |
| ⭐ **Machine Ready** | Máy **sau** | "Tôi sẵn sàng nhận board" |

Với DP-01, cả hai phía:

| Tag | Chiều | Nghĩa |
|---|---|---|
| `DI_SmemaInAvail` | Từ máy trước | Máy trước có board sẵn |
| `DO_SmemaInRdy` | Tới máy trước | DP-01 sẵn sàng nhận |
| `DI_SmemaOutRdy` | Từ máy sau | Máy sau sẵn sàng nhận |
| `DO_SmemaOutAvail` | Tới máy sau | DP-01 có board sẵn để chuyển |

> ⭐ **Chỉ khi CẢ HAI tín hiệu cùng đúng thì việc chuyển board mới bắt đầu.**
> Đây là một phép AND đơn giản — và nó đủ để điều phối hai máy bất kỳ.

### Vì sao thiết kế này hiệu quả

| Lý do | Giải thích |
|---|---|
| ⭐ **Không cần biết máy kia là gì** | Không giao thức, không địa chỉ, không cấu hình. Hai sợi dây |
| ⭐ **Không cần đồng bộ thời gian** | Mỗi máy chạy nhịp riêng; bắt tay tự khớp |
| **Không có gì để cấu hình sai** | Không baud, không địa chỉ, không bản đồ thanh ghi (Chương 38, 39) |
| ⭐ **Đo được bằng đồng hồ** | Người thợ điện kiểm được bằng đồng hồ vạn năng lúc 2 giờ sáng |
| **Cách ly quang** | Hai máy có hệ điện riêng — cách ly là bắt buộc |

> ⭐ **So sánh đáng suy nghĩ:** một liên kết Modbus (Chương 39) cần bốn tham số nối tiếp, địa chỉ tớ,
> bản đồ thanh ghi, quy ước địa chỉ, thứ tự word — sáu chỗ có thể sai. SMEMA có **hai sợi dây và một
> phép AND**.
>
> Đó là lý do nó vẫn sống sau nhiều thập kỷ, dù mọi máy đều đã có Ethernet.

### ⚠ Cách ly quang là bắt buộc

Hai máy có hệ điện riêng, nguồn 24 V riêng, đất riêng. Nối thẳng tín hiệu giữa chúng tạo ra **vòng
lặp đất** (Chương 31, mục 31.6) và có thể làm hỏng ngõ vào của cả hai.

| Cách | Ghi chú |
|---|---|
| ⭐ **Rơ-le trung gian** | Cách ly cơ khí thật; dễ thay; đo được (Chương 5, mục 5.5) |
| **Cách ly quang** | Gọn hơn; ⚠ vẫn có dòng rò (Chương 9, mục 9.3) |

> ⚠ Với tín hiệu đi **ra khỏi máy**, sách khuyến nghị **rơ-le** — đúng bảng ở Chương 9 mục 9.7 và
> Chương 5 mục 5.8.

---

## 41.4 ⭐⭐ Ai đang giữ sản phẩm

Đây là mục quan trọng nhất chương, và là cách hiểu đúng về cỗ máy ở mục 41.1.

### Nguyên tắc

> **Tại mọi thời điểm, mỗi sản phẩm phải có ĐÚNG MỘT máy chịu trách nhiệm giữ nó.**
>
> Không được có thời điểm nào **không máy nào** giữ — đó là lúc board thứ hai được đẩy vào.
> Không được có thời điểm nào **hai máy cùng** giữ — đó là lúc hai cơ cấu cùng tác động lên một board.

Việc chuyển giao trách nhiệm phải **rõ ràng và không có khoảng trống**:

```text
   Máy trước GIỮ  ──────┐
                        │  ⚠ vùng chuyển giao — phải KHÔNG có khoảng trống
                        └──────►  Máy sau GIỮ
```

### Ba quy tắc bàn giao

| Quy tắc | Nội dung |
|---|---|
| ⭐ **1. Máy trước giữ trách nhiệm cho tới khi board RỜI HẲN** | Không phải tới khi "đã đẩy xong", mà tới khi **cảm biến ra xác nhận board đã đi hết** |
| ⭐ **2. Máy sau nhận trách nhiệm khi board ĐÃ VÀO HẲN** | Không phải khi bắt đầu nhận |
| ⭐ **3. Trong vùng chuyển giao, CẢ HAI cùng chịu trách nhiệm** | ⚠ Chồng lấn là **an toàn**; khoảng trống là **nguy hiểm** |

> ⭐ **Quy tắc 3 là chỗ mà thiết kế ở mục 41.1 sai.**
> Ở đó, máy trước nhả trách nhiệm **trước khi** máy sau nhận — tạo ra một khoảng trống, và board thứ
> hai lọt vào đúng khoảng đó.
>
> Cách đúng là để hai vùng trách nhiệm **chồng lên nhau**: máy trước chỉ báo "đã trống" khi board đã
> ra hẳn, và trong lúc đó máy sau đã nhận trách nhiệm rồi.

### Hiện thực trên DP-01

```iecst
// ── PHÍA NHẬN (từ máy trước) ──

// Sẵn sàng nhận: chuyền vào trống, không lỗi, đang chạy
DO_SmemaInRdy := M_Running
               AND NOT M_AnyFault
               AND NOT DI_BoardInfeed          // ⭐ vùng nhận phải TRỐNG
               AND NOT M_Stn1Occupied;

// ⭐ Nhận trách nhiệm khi board ĐÃ VÀO HẲN — cạnh lên của cảm biến vào
TrigBoardIn(CLK := DI_BoardInfeed);
IF TrigBoardIn.Q THEN
    M_WeOwnBoardIn := TRUE;                    // ⭐ DP-01 chịu trách nhiệm từ đây
END_IF;

// ── PHÍA GIAO (tới máy sau) ──

// Có board sẵn: board đã xong ở trạm 2 và đang ở vùng ra
DO_SmemaOutAvail := M_Board2Done AND DI_BoardOutfeed;

// ⭐ Chỉ nhả trách nhiệm khi board đã RỜI HẲN — cạnh xuống
TrigBoardOut(CLK := DI_BoardOutfeed);          // F_TRIG
IF TrigBoardOut.Q THEN
    M_WeOwnBoardOut := FALSE;                  // ⭐ giao xong từ đây
    OkCount := OkCount + 1;                    // đếm ở đây (Chương 18, mục 18.3)
END_IF;
```

> ⭐ **Chú ý hai cạnh khác nhau:**
> - **Nhận** trách nhiệm ở **cạnh lên** — board vừa vào.
> - **Nhả** trách nhiệm ở **cạnh xuống** — board vừa ra hẳn.
>
> Đây chính là ứng dụng của Chương 16 mục 16.5, và của bài học ở Chương 18 mục 18.3: **đếm ở cạnh
> xuống đếm sản phẩm đã hoàn tất**.

### ⚠ Và phải có timeout

```iecst
// Board vào vùng chuyển giao nhưng không tới nơi trong thời gian dự kiến
T_TransferIn(IN := M_TransferInActive, PT := T#5S);
IF T_TransferIn.Q THEN
    M_Alm_TransferIn := TRUE;        // cờ chốt — gom vào M_AnyFault (Ch.25 mục 25.5c)
    M_FaultCode := 410;              // "board kẹt ở vùng chuyển giao vào"
    DO_SmemaInRdy := FALSE;        // ⭐ ngừng nhận thêm
END_IF;
```

> ⚠ **Không có timeout thì board kẹt ở vùng chuyển giao sẽ không bao giờ được phát hiện** — và máy
> trước có thể đẩy tiếp board sau. Đây là cùng nguyên tắc với Chương 26 mục 26.1: mọi bước chờ phải
> có giới hạn thời gian.

---

## 41.5 Tín hiệu cứng hay qua mạng

Ngày nay hai máy thường đã nối chung mạng (Chương 40). Vậy sao không bắt tay qua mạng cho gọn?

| | ⭐ **Tín hiệu cứng** | **Qua mạng** |
|---|---|---|
| Độ tin cậy | ⭐ Rất cao — hai sợi dây | Phụ thuộc mạng, cấu hình, giao thức |
| Ghép máy khác hãng | ⭐ **Luôn được** | ⚠ Phải cùng giao thức và cùng quy ước |
| Cấu hình | ⭐ Không có gì để sai | Nhiều chỗ có thể sai |
| Chẩn đoán tại chỗ | ⭐ **Đo bằng đồng hồ** | Cần công cụ mạng |
| Thời gian đáp ứng | Nhanh, xác định | Phụ thuộc mạng |
| ⭐ Dữ liệu kèm theo | ⚠ **Không có** — chỉ hai bit | ⭐ Mã sản phẩm, kết quả, lý do NG |
| Số dây | Vài sợi mỗi giao diện | Một cáp mạng |

> ⭐ **Phương án dùng phổ biến nhất, và thường là đúng nhất: dùng cả hai.**
> - **Bắt tay bằng tín hiệu cứng** — điều phối việc chuyển board. Đơn giản, tin cậy, ghép được với
>   mọi máy, và **không phụ thuộc mạng**.
> - **Dữ liệu qua mạng** — mã sản phẩm, kết quả kiểm, lý do NG. Thứ mà hai bit không mang được.
>
> Đây là cùng mẫu với biến tần ở Chương 36 mục 36.5: **lệnh đi dây, dữ liệu qua mạng.**

> ⚠⚠ **Đừng để việc chuyển board phụ thuộc mạng.**
> Mất mạng thì chuyền dừng — chấp nhận được. Nhưng mất mạng mà **hai máy vẫn tiếp tục đẩy board theo
> giả định cũ** thì thành cỗ máy ở mục 41.1. Tín hiệu cứng không có kiểu hỏng đó: mất dây thì tín
> hiệu về 0, và với thiết kế đúng, 0 nghĩa là "không sẵn sàng".

### ⭐ Chiều an toàn của tín hiệu

> **Cả hai tín hiệu phải được thiết kế sao cho MẤT tín hiệu = KHÔNG chuyển board.**
>
> - `Machine Ready` mất → máy trước hiểu "máy sau chưa sẵn sàng" → **không đẩy**. ✅
> - `Board Available` mất → máy sau hiểu "chưa có board" → **không nhận**. ✅
>
> Đứt dây, mất nguồn, máy kia tắt — mọi trường hợp đều dẫn tới **dừng chuyển**, không dẫn tới va chạm.
>
> Đây chính là nguyên tắc hỏng-về-an-toàn ở Chương 3 mục 3.6 và Chương 15, áp cho giao diện máy–máy.

---

## 41.6 Bắt tay dữ liệu — khi cần nhiều hơn hai bit

Với truy xuất nguồn gốc (Chương 42), hai bit không đủ. Máy sau cần biết **board này là board nào** và
**kết quả ở máy trước ra sao**.

### Mẫu thường dùng

```text
   1. Tín hiệu cứng điều phối việc chuyển   ← không đổi
   2. Trước hoặc trong lúc chuyển, máy trước gửi dữ liệu qua mạng:
        - mã sản phẩm (đọc từ mã 2D)
        - kết quả OK/NG
        - lý do NG nếu có
   3. Máy sau nhận, đối chiếu, và xử lý
```

> ⚠ **Ba vấn đề phải giải quyết:**
>
> **1. Ghép đúng dữ liệu với đúng board.** Nếu dữ liệu tới muộn hoặc lệch một nhịp, board A mang dữ
> liệu của board B. ⭐ Cách chắc chắn nhất: **mỗi board tự mang mã của mình** — đọc mã 2D ở mỗi máy
> thay vì truyền dữ liệu (Chương 42).
>
> **2. Dữ liệu không tới.** Máy sau phải quyết định: dừng chờ, hay nhận board mà không có dữ liệu?
> ⚠ Đây là quyết định thuộc đặc tả (Chương 23), không phải mặc định.
>
> **3. Thứ tự.** Nếu hai board đi liên tiếp, dữ liệu phải khớp thứ tự. ⭐ Đây đúng là bài toán **thanh
> ghi dịch** ở Chương 19 mục 19.6.

> ⭐ **Khuyến nghị thực dụng: nếu có mã 2D trên sản phẩm, hãy để mỗi máy tự đọc mã đó.**
> Nó loại bỏ hoàn toàn vấn đề 1 và 3, và biến vấn đề 2 thành một câu hỏi đơn giản hơn nhiều. Truyền
> dữ liệu giữa máy chỉ nên dùng khi sản phẩm **không mang được nhận dạng của chính nó**.

---

## 41.7 Hành vi ở biên chuyền

Ba tình huống thường gặp mà thiết kế bắt tay phải xử lý.

| Tình huống | Vấn đề | Cách xử lý |
|---|---|---|
| **Máy sau dừng** | Board dồn ở vùng ra của DP-01 | ⭐ `Machine Ready` của máy sau về 0 → DP-01 **giữ board lại**, không đẩy |
| **Máy trước dừng** | DP-01 hết hàng | Chạy hết board trong máy rồi vào trạng thái chờ — ⚠ **không báo lỗi**, đây là bình thường |
| ⚠ **DP-01 dừng giữa chừng** | Board đang ở trong máy | ⭐ **Không nhận thêm**; board đang có phải xử lý theo Chương 28 |

> ⭐ **"Máy trước hết hàng" không phải lỗi.**
> Nó là trạng thái vận hành bình thường của mọi chuyền — máy trước đang đổi vật tư, đang bảo trì, hoặc
> chỉ đơn giản là chậm hơn. Báo lỗi cho tình huống này sẽ tạo ra rất nhiều báo giả, và người vận hành
> sẽ học cách bỏ qua (Chương 48, mục 48.6).
>
> Cách đúng: hiển thị trạng thái **"chờ hàng"** khác với **"lỗi"**, và ⭐ **đếm thời gian chờ** — đó là
> số liệu quý cho việc phân tích nút cổ chai (Chương 55).

### ⚠ Xả máy khi dừng cuối ca

Khi dừng có kế hoạch, máy nên **xả hết board** trước khi dừng hẳn — chứ không dừng đột ngột với board
đang dở dang.

```iecst
// Yêu cầu dừng: ngừng nhận, chạy hết board đang có
IF M_StopRequested THEN
    DO_SmemaInRdy := FALSE;               // ⭐ ngừng nhận thêm
    // trình tự vẫn chạy cho tới khi máy rỗng
    IF M_MachineEmpty THEN
        M_Running := FALSE;                 // dừng hẳn khi đã xả xong
    END_IF;
END_IF;
```

> ⭐ Đây là điều kiện đã dùng ở Chương 29 mục 29.5 cho việc đổi công thức — **máy phải biết khi nào nó
> rỗng**. Một cờ, dùng cho nhiều việc.

---

## 41.7b ⭐ Trạm đệm — nơi sản phẩm nằm lại, và nơi chương trình hay mất dấu

Mục 41.4 hỏi *"ai đang giữ sản phẩm"* với **một** sản phẩm ở **một** chỗ giao. Trạm đệm *(buffer)* làm
câu hỏi đó khó hẳn lên: ⭐ **nhiều sản phẩm nằm cùng lúc, và chương trình phải nhớ từng ô có gì.**

Trạm đệm có hai lý do tồn tại, và chúng đòi hỏi khác nhau:

| Kiểu | Mục đích | Điều kiện lấy ra |
|---|---|---|
| ⭐ **Đệm cân bằng nhịp** | Máy trước và máy sau không cùng nhịp (mục 41.2) | Có hàng là lấy được |
| ⭐⭐ **Đệm theo thời gian** | ⭐ **Thời gian nằm lại LÀ một công đoạn** — keo đông, nguội sau sấy | ⚠ **Đủ thời gian mới được lấy** |

### Ba thứ phải có cho mỗi ô

| | Nội dung |
|---|---|
| ⭐ **Có hàng hay không** | Một bit cho mỗi ô |
| ⭐ **Vào lúc nào** | Một đồng hồ cho mỗi ô — cần cho kiểu đệm theo thời gian, và ⚠ **luôn hữu ích** kể cả kiểu kia |
| **Có dùng được không** | ⭐ Ô hỏng thì **bỏ qua ô đó**, không bỏ cả trạm (Chương 51 mục 51.7b) |

```iecst
// ── Mỗi ô: đếm thời gian đã nằm, và cho biết đã đủ chưa ──
FOR i := 1 TO SLOT_COUNT DO
    IF Slot[i].HasPart THEN
        Slot[i].DwellMs := Slot[i].DwellMs + TASK_MS;
    ELSE
        Slot[i].DwellMs := 0;
    END_IF;

    // ⭐ Ô sẵn sàng để LẤY RA
    Slot[i].ReadyOut := Slot[i].HasPart
                        AND (Slot[i].DwellMs >= MinDwellMs)
                        AND NOT Slot[i].Disabled;
END_FOR;
```

### ⭐ Vào trước ra trước, hay vào sau ra trước — phải chọn, và phải chọn đúng

| | **Vào trước ra trước** *(FIFO)* | **Vào sau ra trước** *(LIFO)* |
|---|---|---|
| Dùng khi | ⭐ **Hầu hết trường hợp** | Kho xếp chồng, chỉ với tới cái trên cùng |
| Với đệm theo thời gian | ⭐⭐ **Bắt buộc** — cái vào trước đủ thời gian trước | ⚠⚠ **Sai** — cái vừa vào chưa đủ thời gian |
| Truy xuất nguồn gốc | ⭐ Thứ tự ra đoán được | ⚠ Khó đối chiếu (Chương 42) |

> ⚠⚠ **Chọn nhầm ở trạm đệm theo thời gian là lỗi không nhìn thấy được.** Máy vẫn chạy, sản lượng vẫn
> đủ, ⭐ **chỉ có chất lượng là sai** — keo chưa đông đã đi tiếp. Và nó sai **âm thầm** đúng kiểu
> Chương 48 cảnh báo: không có phép kiểm nào báo động.
>
> ⭐ Cách phòng rẻ nhất: **đừng lấy ra theo vị trí, hãy lấy ra theo ĐỒNG HỒ.** Chọn ô có thời gian nằm
> lâu nhất trong số các ô đã đủ điều kiện — khi đó thứ tự đúng **tự nhiên đúng**, không phụ thuộc vào
> việc ai đã chọn đúng chế độ.

### ⚠⚠ Bật máy lên, trong đệm đang có hàng

Đây là phần khó nhất, và là phần hay bị bỏ hẳn:

> ⚠⚠ **Mất điện giữa ca thì sản phẩm vẫn nằm nguyên trong trạm đệm — nhưng bộ nhớ của chương trình
> thì không.**

Ba lối xử lý, và cái thứ ba là cái đúng:

| Cách | Vấn đề |
|---|---|
| Giả định đệm rỗng | ⚠⚠ Máy nạp thêm vào ô đã có hàng, hoặc bỏ sót hàng cũ nằm lại mãi |
| Giữ toàn bộ trạng thái qua mất điện | ⚠ Sai ngay khi có người **lấy tay ra** trong lúc máy tắt — và luôn có người làm thế |
| ⭐⭐ **Đọc lại cảm biến khi khởi tạo, rồi HỎI người vận hành** | ⭐ Chương trình dựng lại *"ô nào có hàng"* từ cảm biến; ⚠ nhưng **thời gian đã nằm thì không cảm biến nào biết** |

⭐ Với đệm theo thời gian, câu hỏi phải hỏi thẳng — bằng kênh nhắc thao tác ở Chương 44 mục 44.3b:

```text
   Trong trạm đệm đang có 4 sản phẩm.
   Không biết chúng đã nằm bao lâu.

   [ Tính lại từ bây giờ ]   [ Coi là đã đủ ]   [ Loại bỏ cả 4 ]
```

> ⭐⭐ **Ba nút đó là một quyết định về CHẤT LƯỢNG, nên nó phải do người quyết, không phải do chương
> trình mặc định.** ⚠ Và dù chọn gì, **phải ghi vào nhật ký và đánh dấu bốn sản phẩm đó** — vì nếu về
> sau có sự cố, đây chính xác là bốn sản phẩm cần tra lại (Chương 42).
>
> ⚡ Cùng một lập luận với việc *"bỏ qua camera thì sản phẩm phải bị đánh dấu"* ở Chương 51 mục 51.7b:
> ⭐ **khi máy không biết chắc, hồ sơ phải nói rằng nó không biết chắc** — không được ghi một điều
> đẹp đẽ mà sai.

---

## 41.8 Trên máy mẫu DP-01

### Giao diện đầy đủ

| Phía | Tín hiệu | Kiểu | Ghi chú |
|---|---|---|---|
| **Vào** | `DI_SmemaInAvail` | Ngõ vào số, cách ly | Từ máy trước |
| **Vào** | `DO_SmemaInRdy` | ⭐ Ngõ ra **rơ-le** | Tới máy trước — cách ly thật (Chương 9, mục 9.7) |
| **Ra** | `DI_SmemaOutRdy` | Ngõ vào số, cách ly | Từ máy sau |
| **Ra** | `DO_SmemaOutAvail` | ⭐ Ngõ ra **rơ-le** | Tới máy sau |
| Dữ liệu | Qua mạng chung (Chương 40) | — | Mã sản phẩm, kết quả — Chương 42 |

### Trạng thái chuyền vào

```iecst
CASE InfeedStep OF
    0:  // Chờ điều kiện đủ để nhận
        DO_SmemaInRdy := M_Running AND NOT M_AnyFault
                       AND NOT DI_BoardInfeed AND NOT M_Stn1Occupied;
        IF DO_SmemaInRdy AND DI_SmemaInAvail THEN
            InfeedStep := 10;                    // ⭐ CẢ HAI cùng đúng
        END_IF;

    10: // Đang nhận — chạy chuyền vào
        M_ConvInRun := TRUE;
        IF DI_BoardInfeed THEN                   // board đã vào hẳn
            M_WeOwnBoardIn := TRUE;              // ⭐ nhận trách nhiệm
            DO_SmemaInRdy := FALSE;            // ⚠ ngừng báo sẵn sàng NGAY
            InfeedStep := 20;
        END_IF;

    20: // Đưa board tới trạm 1
        IF DI_BoardStn1 THEN
            M_Stn1Occupied := TRUE;
            M_ConvInRun := FALSE;
            InfeedStep := 0;
        END_IF;

ELSE
    InfeedStep := 0;                             // Chương 20
END_CASE;

// ⚠ Timeout cho mọi bước có chờ (Chương 26)
T_Infeed(IN := (InfeedStep > 0), PT := T#10S);
IF T_Infeed.Q THEN
    M_Alm_TransferIn := TRUE;  M_FaultCode := 410;
    DO_SmemaInRdy := FALSE;
END_IF;
```

> ⭐ **Dòng `DO_SmemaInRdy := FALSE` ở bước 10 là dòng chống lại cỗ máy ở mục 41.1.**
> Ngay khi board vào hẳn, DP-01 **lập tức** báo "không còn sẵn sàng" — nên máy trước không đẩy board
> tiếp theo trong lúc DP-01 còn đang đưa board này vào trạm.
>
> ⚠ Chú ý nó nằm **cùng chỗ** với việc nhận trách nhiệm. Hai việc phải xảy ra **cùng lúc**, không
> phải ở hai bước khác nhau.

### Đo thời gian chờ — số liệu cho Chương 55

```iecst
// ⭐ Đếm thời gian máy phải chờ máy trước và chờ máy sau
T_WaitUpstream(IN := (InfeedStep = 0) AND DO_SmemaInRdy AND NOT DI_SmemaInAvail,
               PT := T#1H);
T_WaitDownstream(IN := M_Board2Done AND NOT DI_SmemaOutRdy, PT := T#1H);

// Cộng dồn theo ca — số liệu phân tích nút cổ chai
IF TrigMinute.Q THEN
    IF T_WaitUpstream.Q   THEN WaitUpstreamMin   := WaitUpstreamMin + 1;   END_IF;
    IF T_WaitDownstream.Q THEN WaitDownstreamMin := WaitDownstreamMin + 1; END_IF;
END_IF;
```

> ⭐ **Hai con số này trả lời câu hỏi quan trọng nhất về hiệu suất chuyền: máy của tôi chậm, hay hàng
> xóm chậm?**
>
> Với chu kỳ mục tiêu 12 giây đã chốt (Phụ lục J §J.1) và trạm sấy UV sát trần, DP-01 rất có thể là
> **nút cổ chai của chuyền** ở một số mã hàng. Hai bộ đếm này cho biết điều đó bằng số liệu thay vì
> bằng tranh cãi (Chương 55).

---

## 41.9 Khác biệt giữa các hãng và các chuẩn

Bắt tay máy–máy là chỗ **ít phụ thuộc hãng PLC nhất** trong cả cuốn sách — vì nó chỉ là hai ngõ vào
và hai ngõ ra số.

| Khía cạnh | Điều cần biết |
|---|---|
| ⭐ Chuẩn bắt tay | **SMEMA** phổ biến nhất trong lắp ráp điện tử; các ngành khác có chuẩn riêng hoặc quy ước riêng |
| ⚠ **Mức tín hiệu và cách đấu** | Kiểm tài liệu chuẩn và tài liệu máy hàng xóm. ⚠ Đừng giả định — **hỏi trước khi đấu** |
| ⚠ Chiều tác động | Tín hiệu tích cực mức cao hay thấp — kiểm kỹ, đấu ngược thì hành vi đảo hoàn toàn |
| Đầu nối | Thường có quy ước về loại đầu nối và chân — kiểm |
| Dữ liệu kèm theo | Không có trong chuẩn bắt tay cơ bản — dùng mạng riêng (mục 41.6) |
| Ngành khác | Máy đóng gói, máy thực phẩm, máy dược có chuẩn và quy ước riêng — nguyên tắc giống nhau |

> ⚠⚠ **Trước khi ghép máy vào chuyền có sẵn, hãy hỏi và ghi lại ba thứ:**
> 1. **Chuẩn bắt tay** đang dùng và tài liệu của nó.
> 2. **Mức tín hiệu, chiều tác động, loại đầu nối**.
> 3. ⭐ **Chiều cao mặt băng tải và vị trí board** — cơ khí phải khớp, và đây là thứ **không sửa được
>    bằng phần mềm**.
>
> Gạch đầu dòng 3 nằm ngoài phạm vi lập trình nhưng là thứ làm hỏng nhiều dự án nhất khi ghép chuyền.

---

## 41.10 Bẫy thường gặp

### 🔍 BẪY 1 — Có khoảng trống trong việc giữ sản phẩm

**Hiện tượng:** ⭐ đúng cỗ máy ở mục 41.1 — hai board chồng nhau, và **cả hai máy đều đúng theo chương
trình của mình**.
**Cách sửa:** ba quy tắc bàn giao ở mục 41.4 — hai vùng trách nhiệm phải **chồng lấn**, không được có
khoảng trống.

### 🔍 BẪY 2 — Nhả tín hiệu "sẵn sàng nhận" quá muộn

**Hiện tượng:** máy trước đẩy board tiếp theo trong lúc máy sau còn đang xử lý board vừa nhận.
**Cách sửa:** `DO_SmemaInRdy := FALSE` **ngay khi** board vào hẳn, cùng chỗ với việc nhận trách
nhiệm (mục 41.8).

### 🔍 BẪY 3 — Bắt tay qua mạng cho việc chuyển board

**Hiện tượng:** ⚠⚠ mất mạng mà hai máy vẫn đẩy board theo giả định cũ.
**Cách sửa:** việc chuyển board dùng **tín hiệu cứng**; mạng chỉ mang dữ liệu (mục 41.5).

### 🔍 BẪY 4 — Chiều tín hiệu không hỏng-về-an-toàn

**Hiện tượng:** đứt dây làm máy hiểu "sẵn sàng" và tiếp tục đẩy board.
**Cách sửa:** thiết kế sao cho **mất tín hiệu = không chuyển** (mục 41.5).

### 🔍 BẪY 5 — Không cách ly tín hiệu giữa hai máy

**Hiện tượng:** vòng lặp đất; nhiễu; có thể hỏng ngõ vào của cả hai máy.
**Cách sửa:** rơ-le trung gian hoặc cách ly quang (mục 41.3, Chương 5 mục 5.5).

### 🔍 BẪY 6 — Không có timeout ở vùng chuyển giao

**Hiện tượng:** board kẹt giữa hai máy không được phát hiện; máy trước có thể đẩy tiếp.
**Cách sửa:** timeout cho mọi bước chờ, và **ngừng nhận** khi có lỗi (mục 41.4, Chương 26).

### 🔍 BẪY 7 — Báo lỗi khi máy trước hết hàng

**Hiện tượng:** rất nhiều báo giả; người vận hành học cách bỏ qua cảnh báo chuyền.
**Cách sửa:** "chờ hàng" là **trạng thái bình thường**, hiển thị khác với "lỗi"; ⭐ và **đếm thời gian
chờ** (mục 41.7).

### 🔍 BẪY 8 — Ghép sai dữ liệu với board

**Hiện tượng:** board A mang kết quả của board B; truy xuất nguồn gốc sai — và sai theo cách **không
phát hiện được** cho tới khi có khiếu nại.
**Cách sửa:** ⭐ để **mỗi board tự mang mã của mình** và mỗi máy tự đọc (mục 41.6, Chương 42).

### 🔍 BẪY 9 — Dừng máy đột ngột với board đang dở

**Hiện tượng:** board dở dang mắc lại trong máy; ca sau phải xử lý bằng tay.
**Cách sửa:** dừng có kế hoạch thì **xả hết máy trước** (mục 41.7).

### 🔍 BẪY 10 — Không hỏi thông số cơ khí trước khi ghép chuyền

**Hiện tượng:** ⚠ chiều cao mặt băng tải không khớp máy hàng xóm — và **không sửa được bằng phần
mềm**.
**Cách sửa:** hỏi và ghi ba thứ ở mục 41.9 **trước khi** thiết kế cơ khí.

---

## 41.11 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Bắt tay SMEMA gồm mấy tín hiệu | ⭐ **Hai mỗi chiều** — Board Available và Machine Ready |
| Khi nào bắt đầu chuyển board | ⭐ **Cả hai** tín hiệu cùng đúng |
| Vì sao thiết kế đó hiệu quả | Không cần biết máy kia là gì · không cấu hình · ⭐ **đo được bằng đồng hồ** |
| ⭐⭐ Nguyên tắc trung tâm | **Mỗi sản phẩm, đúng một máy chịu trách nhiệm — không có khoảng trống** |
| Máy trước nhả trách nhiệm khi | Board **rời hẳn** (cạnh xuống), không phải khi "đã đẩy" |
| Máy sau nhận trách nhiệm khi | Board **vào hẳn** (cạnh lên) |
| Chồng lấn hay khoảng trống | ⭐ **Chồng lấn an toàn; khoảng trống nguy hiểm** |
| Bắt tay bằng gì | ⭐ **Tín hiệu cứng** cho việc chuyển; **mạng** cho dữ liệu |
| Chiều tín hiệu phải sao | ⭐ **Mất tín hiệu = không chuyển** |
| Cách ly giữa hai máy | ⭐ **Rơ-le** — hai máy có hệ điện riêng |
| Máy trước hết hàng | ⚠ **Trạng thái bình thường**, không phải lỗi — nhưng **đếm thời gian chờ** |
| Dừng có kế hoạch | **Xả hết máy** trước khi dừng hẳn |
| Ghép dữ liệu với sản phẩm | ⭐ Tốt nhất: **sản phẩm tự mang mã**, mỗi máy tự đọc |
| Trước khi ghép chuyền, hỏi | Chuẩn bắt tay · mức và chiều tín hiệu · ⚠ **chiều cao mặt băng tải** |

---

## 41.12 Tự kiểm

1. ⭐ Mô tả sự cố ở mục 41.1. Vì sao nói **cả hai máy đều đúng** mà vẫn xảy ra hỏng hóc?
2. Kể bốn tín hiệu của bắt tay SMEMA giữa hai máy, và cho biết ai phát tín hiệu nào.
3. Nêu năm lý do thiết kế "hai tín hiệu mỗi chiều" lại hiệu quả tới vậy. So sánh số chỗ có thể sai
   với một liên kết Modbus.
4. ⭐⭐ Phát biểu nguyên tắc "ai đang giữ sản phẩm". Vì sao **chồng lấn** trách nhiệm là an toàn còn
   **khoảng trống** là nguy hiểm?
5. ⭐ Máy trước nhả trách nhiệm ở cạnh nào của cảm biến, máy sau nhận ở cạnh nào? Vì sao khác nhau?
6. Trong đoạn mã ở mục 41.8, dòng nào chống lại sự cố ở mục 41.1? Vì sao nó phải nằm **cùng chỗ** với
   việc nhận trách nhiệm?
7. So sánh bắt tay bằng tín hiệu cứng với bắt tay qua mạng. Phương án nào thường đúng nhất và vì sao?
8. ⭐ Vì sao **không** được để việc chuyển board phụ thuộc mạng? Mô tả kiểu hỏng mà tín hiệu cứng
   không có.
9. Giải thích nguyên tắc "mất tín hiệu = không chuyển" cho **cả hai** tín hiệu.
10. Vì sao cần cách ly tín hiệu giữa hai máy? Sách khuyến nghị dùng gì và vì sao?
11. ⭐ "Máy trước hết hàng" có phải lỗi không? Nêu hậu quả của việc báo lỗi cho tình huống này, và
    cách xử lý đúng.
12. ⭐ Khi cần truyền dữ liệu kèm sản phẩm, nêu ba vấn đề phải giải quyết. Cách nào loại bỏ được hai
    trong ba?
13. Hai bộ đếm thời gian chờ ở mục 41.8 trả lời câu hỏi gì? Vì sao chúng quan trọng với DP-01?

> Câu 1, 4, 5, 8 và 11 là năm câu phân loại. Câu 4 là tinh thần của cả chương: **hai máy đều đúng vẫn
> làm hỏng sản phẩm, nếu không ai định nghĩa rõ ai đang giữ nó.**

---

### Chương tiếp theo

Chương 42 — **Mã vạch, mã 2D & truy xuất nguồn gốc**. Bạn đã ghép được máy vào chuyền. Chương sau về
việc biết **board này là board nào** — đọc mã, hỏi hệ thống trên xem nó có được phép làm ở đây không,
và báo kết quả về. Cùng với câu hỏi khó nhất: khi mất kết nối thì làm gì.

### Nguồn tham khảo chương 41

- **Đặc tả giao diện SMEMA** — chuẩn bắt tay điện cho thiết bị lắp ráp điện tử; dùng cho mức tín hiệu,
  chiều tác động và quy ước đầu nối. ⚠ Phải đọc bản gốc trước khi đấu.
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu với tín hiệu liên
  máy và cách ly. *(tiêu chuẩn có bản quyền)*
- ⚠ **Tài liệu của máy hàng xóm** — thứ quan trọng nhất khi ghép chuyền, và là thứ phải xin **trước
  khi** thiết kế cơ khí (mục 41.9).
- Bảng I/O và số liệu đã chốt của DP-01 — Phụ lục J.

> ⚡ Mô tả bắt tay ở mục 41.3 là **mô tả nguyên lý** ở mức đủ để bạn hiểu và thiết kế logic. ⚠ Mức
> điện áp, chiều tác động, loại đầu nối và sơ đồ chân phải lấy từ **bản gốc đặc tả** và từ tài liệu
> máy hàng xóm — đấu sai chiều tác động làm hành vi đảo hoàn toàn, và không có gì trong chương trình
> phát hiện được điều đó.
>
> ⚠ Các ngành khác có chuẩn bắt tay riêng. Nguyên tắc ở mục 41.4 — **ai đang giữ sản phẩm** — thì
> không phụ thuộc chuẩn nào; nó đúng với mọi kiểu ghép nối, kể cả ghép bằng tay.
