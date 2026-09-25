# Chương 20 — Structured Text: cho người biết lập trình

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 20.1 Chương này dành cho ai — và một cảnh báo trước

Nếu bạn đã viết C, Pascal, Python hay bất kỳ ngôn ngữ nào có `if` và `for`, **Structured Text** *(ST,
văn bản có cấu trúc)* sẽ quen tay ngay. Cú pháp gần Pascal, và bạn có thể viết được đoạn ST đầu tiên
trong mười lăm phút.

Đó vừa là ưu điểm vừa là cái bẫy.

Ưu điểm: ST gọn hơn ladder rất nhiều với những việc mà ladder làm dở — tính toán, xử lý mảng, máy
trạng thái nhiều nhánh. Sách này dùng ST cho phần lớn ví dụ chính vì lý do đó.

Cái bẫy: **quen tay không có nghĩa là môi trường giống nhau.** Code ST chạy trong vòng quét, trên
một CPU điều khiển máy móc vật lý, và sẽ được đọc bởi người thợ điện lúc hai giờ sáng. Ba ràng buộc
đó không có trong bất kỳ ngôn ngữ nào bạn từng dùng, và chúng đổi hẳn cái gì là "code tốt".

Mục 20.5 (vòng lặp) là mục có thể làm **treo CPU**. Mục 20.6 (khi nào ST là lựa chọn tệ) là mục quan
trọng nhất của chương, và nó không nói về kỹ thuật.

---

## 20.2 Cú pháp đủ dùng

### Câu lệnh và phép gán

```iecst
M_Running    := TRUE;              // gán, dùng :=  (không phải =)
BoardCount   := BoardCount + 1;    // mọi câu lệnh kết thúc bằng dấu ;
DO_ConvRun   := M_Enable AND NOT M_AnyFault;
```

Ba khác biệt so với ngôn ngữ quen thuộc:

| Trong ST | Trong C / Python |
|---|---|
| Gán là `:=` | `=` |
| So sánh bằng là `=` | `==` |
| Kết thúc câu lệnh bằng `;` **bắt buộc** | Tuỳ ngôn ngữ |

Nhầm `=` với `:=` là lỗi biên dịch, nên nó tự lộ ra. Điều đó tốt.

### Chú thích

```iecst
// Chú thích một dòng — kiểu này phổ biến nhất

(* Chú thích nhiều dòng,
   kiểu gốc của chuẩn *)
```

Kiểu `(* … *)` có ở mọi hệ; kiểu `//` là bổ sung sau và cũng gần như phổ biến, nhưng nếu làm việc
với hệ cũ thì kiểm trước.

### Khai báo biến

```iecst
VAR
    BoardCount   : INT := 0;              // có thể đặt giá trị đầu
    AvgCycleMs   : DINT;
    M_Running    : BOOL;
    T_StepGuard  : TON;                   // thể hiện của khối chức năng
    BoardNG      : ARRAY[0..3] OF BOOL;
END_VAR

VAR CONSTANT
    MAX_BOARD_IN_MACHINE : INT := 2;      // hằng số — đặt tên, đừng viết số trần
END_VAR
```

> 💡 **MẸO** — mọi con số có ý nghĩa nên là hằng số có tên. `IF Count > 2` không nói được gì;
> `IF Count > MAX_BOARD_IN_MACHINE` tự giải thích, và khi con số đổi thì chỉ sửa một chỗ (Chương 30).

### Rẽ nhánh

```iecst
IF DI_BoardStn1 AND NOT M_Stn1Busy THEN
    M_Stn1Busy := TRUE;
ELSIF M_Stn1Done THEN
    M_Stn1Busy := FALSE;
ELSE
    ;                                     // không làm gì — vẫn cần dấu ;
END_IF;
```

Lưu ý `ELSIF` viết liền, không phải `ELSE IF`. Và mọi khối đều có từ khoá đóng riêng: `END_IF`,
`END_CASE`, `END_FOR`, `END_WHILE`, `END_REPEAT`. Không dùng dấu ngoặc nhọn, không dùng thụt lề để phân khối —
thụt lề chỉ để người đọc, trình biên dịch không quan tâm.

### CASE — nơi ST vượt hẳn ladder

```iecst
CASE Stn1_Step OF
    0:                                    // chờ lệnh chạy
        IF M_Running THEN  Stn1_Step := 10;  END_IF;

    10:                                   // chờ board tới
        IF DI_BoardStn1 THEN  Stn1_Step := 20;  END_IF;

    20:                                   // nâng kẹp
        M_Stn1_ClampReq := TRUE;
        IF DI_Clamp1Up THEN  Stn1_Step := 30;  END_IF;

    30, 31, 32:                           // nhiều giá trị dùng chung một nhánh
        ;

    100..199:                             // cả một dải giá trị
        M_Stn1InFault := TRUE;

ELSE                                      // giá trị không nằm trong danh sách nào
    Stn1_Step := 0;                       // đưa về trạng thái đã biết chắc
END_CASE;
```

Nhánh `ELSE` ở đây **không phải tuỳ chọn**. Nếu biến bước nhận một giá trị ngoài danh sách — do lỗi
tính toán, do người nào đó ghi tay khi gỡ lỗi, do nhiễu bộ nhớ — thì không có nhánh nào chạy và
**trình tự đứng im vĩnh viễn mà không báo gì**. Đúng cỗ máy ở Chương 26, mục 26.1.

Đây cũng chính là lý do `CASE` là cách viết máy trạng thái tốt nhất trong ST: mọi trạng thái nằm
trong một khối, đọc từ trên xuống là thấy hết, và **không thể** ở hai trạng thái cùng lúc
(Chương 25, Chương 26).

### Hàm và khối chức năng

```iecst
// Hàm — không có bộ nhớ, cùng đầu vào luôn cho cùng đầu ra
AbsValue := ABS(Deviation);
Bigger   := MAX(ValueA, ValueB);

// Khối chức năng — CÓ bộ nhớ, phải khai báo thể hiện riêng
T_StepGuard(IN := (Stn1_Step = 20), PT := T#3S);
IF T_StepGuard.Q THEN
    M_Stn1Timeout := TRUE;
END_IF;
```

Phân biệt **hàm** *(function)* với **khối chức năng** *(function block, FB)* là điều phải nắm chắc:
FB có bộ nhớ riêng, nên mỗi chỗ dùng cần một thể hiện riêng. Dùng chung một thể hiện cho hai việc là
lỗi đã gặp ở Chương 16 (Bẫy 2) và Chương 18. Chương 27 nói kỹ về cách viết FB dùng lại.

---

## 20.3 ST vẫn chạy trong vòng quét

Đây là mục ngắn nhất chương và là mục phải nhớ kỹ nhất.

> **Toàn bộ đoạn ST của bạn chạy từ đầu tới cuối, mỗi vòng quét, mãi mãi.**

Không có `main()`, không có vòng đời chương trình, không có "chạy một lần rồi thôi". Mọi kết luận từ
Chương 10 vẫn đúng nguyên vẹn:

- `BoardCount := BoardCount + 1;` không bọc trong bắt cạnh sẽ đếm hàng trăm lần (Chương 16, 18).
- Ghi vào `DO_Clamp1Vlv` ở hai chỗ khác nhau trong cùng đoạn ST là **cùng một lỗi** với cuộn dây trùng
  trong ladder — và ở ST nó **khó thấy hơn**, vì hai dòng có thể cách nhau hai trăm dòng chứ không
  nằm trên hai nấc thang cạnh nhau.
- Biến đọc ở đầu đoạn và ghi ở cuối đoạn: giá trị đọc được là **của vòng quét này** nếu ghi nằm phía
  trên, hoặc **của vòng quét trước** nếu ghi nằm phía dưới. Thứ tự dòng lệnh có ý nghĩa.

> ⚠ **ST che giấu lỗi ghi trùng tốt hơn ladder.**
> Trong ladder, hai cuộn dây cùng tên là thứ nhìn thấy được và nhiều phần mềm còn cảnh báo. Trong ST,
> hai phép gán cùng một ngõ ra trong hai nhánh `IF` xa nhau trông hoàn toàn bình thường. Dùng tham
> chiếu chéo để tìm mọi chỗ ghi vào một biến — thói quen này quan trọng hơn hẳn khi viết ST
> (Chương 22).

---

## 20.4 Khi nào ST vượt trội

Bốn nhóm việc mà ST rõ ràng hơn ladder:

### Tính toán

```iecst
// ST — đọc là hiểu
IF DoneCount > 0 THEN
    AvgCycleMs := TotalCycleMs / DoneCount;
ELSE
    AvgCycleMs := 0;
END_IF;
```

Cùng phép tính này trong ladder cần ba, bốn hộp lệnh nối nhau, mỗi hộp một phép, với biến trung gian
giữa các hộp. Chuỗi công thức càng dài thì khoảng cách càng lớn.

### Máy trạng thái và trình tự

Khối `CASE` ở mục 20.2. Cùng trình tự đó viết bằng ladder cần một nấc thang cho mỗi bước cộng logic
so sánh số bước ở đầu mỗi nấc — dài gấp nhiều lần và khó thấy tổng thể.

### Xử lý mảng và lặp trên nhiều đối tượng giống nhau

```iecst
// Kiểm 4 vị trí thanh ghi dịch, đếm số board lỗi đang trong máy
NgInMachine := 0;
FOR i := 0 TO 3 DO
    IF BoardNG[i] THEN
        NgInMachine := NgInMachine + 1;
    END_IF;
END_FOR;
```

Ladder không có vòng lặp; việc này phải viết tay bốn lần, và khi số vị trí đổi thành tám thì phải sửa
tám chỗ.

### Thuật toán có nhiều điều kiện lồng nhau

Logic kiểu "nếu A và (B hoặc C) nhưng không D, trừ khi E" viết bằng nấc thang thành một mê cung nhánh
song song. ST viết thẳng bằng ngoặc.

---

## 20.5 ⚠⚠ Vòng lặp trong môi trường quét

### Vấn đề

Cả ba vòng lặp — `FOR`, `WHILE`, `REPEAT` — chạy **trọn vẹn trong một vòng quét**. Không có chuyện
"lặp qua nhiều vòng quét" —
CPU chưa ra khỏi vòng lặp thì chưa sang giai đoạn tiếp theo của chu kỳ quét (Chương 10).

Hệ quả: **thời gian chạy vòng lặp cộng thẳng vào thời gian quét.**

Mỗi CPU có **bộ giám sát thời gian quét** *(watchdog)*. Quá thời gian cho phép, CPU coi như chương
trình đã treo và **chuyển sang STOP**:

> ⚠⚠ **NGUY HIỂM**
> Watchdog kích hoạt nghĩa là **mọi ngõ ra tắt cùng lúc, giữa chu trình**, không theo trình tự dừng
> nào. Cơ cấu đang giữ có thể nhả; cơ cấu đang chuyển động dừng ở giữa hành trình. Đây là kiểu dừng
> tệ nhất, và một vòng `WHILE` viết sai là một trong số ít cách mà **code thuần logic** gây ra nó.

### `WHILE` — nguy hiểm nhất

```iecst
// ✗ SAI — ĐỪNG CHÉP. Nếu điều kiện không bao giờ sai, CPU treo và watchdog kích hoạt.
WHILE NOT DI_Clamp1Up DO
    ;                              // "chờ" kẹp lên
END_WHILE;
```

Đoạn này đọc rất hợp lý và **hoàn toàn sai**. Nó chờ một tín hiệu vào — nhưng ảnh ngõ vào **chỉ được
cập nhật ở đầu vòng quét** (Chương 10). Trong lúc vòng lặp chạy, `DI_Clamp1Up` **không bao giờ đổi
giá trị**. Vòng lặp không có lối thoát, và CPU dừng sau vài chục mili-giây.

> **Quy tắc: không bao giờ chờ đợi bên trong một vòng lặp.**
> Trong PLC, "chờ" được thực hiện bằng cách **giữ nguyên bước và để vòng quét chạy tiếp** — đúng như
> máy trạng thái ở mục 20.2. Vòng lặp dùng để **xử lý một tập dữ liệu**, không dùng để chờ thời gian
> hay chờ tín hiệu.

```iecst
// ✓ ĐÚNG — chờ bằng cách giữ nguyên bước, để vòng quét làm việc chờ
20:
    M_Stn1_ClampReq := TRUE;
    IF DI_Clamp1Up THEN
        Stn1_Step := 30;
    END_IF;
```

### `FOR` — an toàn hơn nhưng vẫn phải cẩn thận

`FOR` có số vòng lặp xác định trước, nên không treo vô hạn. Nhưng nó vẫn cộng thời gian:

```iecst
// ⚠ Cân nhắc: 5000 vòng chạy trong MỘT vòng quét
FOR i := 0 TO 4999 DO
    Sum := Sum + Data[i];
END_FOR;
```

Ba quy tắc thực dụng:

- **Số vòng lặp phải là hằng số hoặc có trần rõ ràng.** `FOR i := 0 TO n DO` với `n` đến từ tính toán
  là rủi ro — nếu `n` thành 50 000 thì thời gian quét nổ tung.
- **Đo, đừng đoán.** Sau khi thêm vòng lặp, xem thống kê thời gian quét (Chương 51). Con số lớn nhất
  mới quan trọng, không phải con số trung bình.
- **Tập lớn thì chia nhỏ qua nhiều vòng quét**: mỗi vòng quét xử lý một phần, nhớ vị trí đang tới,
  vòng sau làm tiếp. Dài dòng hơn nhưng giữ thời gian quét ổn định.

⭐ **Và hai quy tắc về chính biến đếm — cả hai là bẫy thật, không phải chuyện phong cách:**

```iecst
// ✗ SAI 1 — sửa biến đếm bên trong vòng
FOR i := 0 TO 9 DO
    IF Skip[i] THEN
        i := i + 1;                  // ⚠ "nhảy cóc" bằng tay
    END_IF;
END_FOR;

// ✗ SAI 2 — dùng biến đếm SAU khi vòng đã kết thúc
FOR i := 0 TO 9 DO
    Total := Total + Data[i];
END_FOR;
LastIndex := i;                      // ⚠ 9 hay 10? Tuỳ hãng
```

| Sai | Chuẩn nói gì | ⭐ Làm thế nào cho đúng |
|---|---|---|
| **1** | Biến đếm, giá trị đầu và giá trị cuối **không được bị thay đổi** bởi các câu lệnh bên trong vòng | Cần bỏ qua phần tử → dùng `IF NOT Skip[i] THEN … END_IF;` bao lấy phần xử lý, **đừng đụng vào `i`** |
| **2** | ⚠ **Giá trị của biến đếm sau khi vòng kết thúc do hãng quyết định** | Cần biết đã tới đâu → **gán vào một biến riêng bên trong vòng**; biến đếm chỉ dùng **bên trong** |

> ⭐ Sai 2 đặc biệt khó chịu vì nó **chạy đúng** trên hệ bạn đang dùng, rồi sai khi chương trình được
> chuyển sang hệ khác. ⚡ Bộ quy tắc viết mã của PLCopen ghi cả hai (L12, L13 — Phụ lục N).

### ⚡ "Thế dùng truy cập trực tiếp thì sao?"

Người đã đọc Chương 10 sẽ nghĩ ngay tới lối thoát này: dùng **truy cập trực tiếp** (mục 10.4) để đọc
thẳng chân vào, bỏ qua ảnh — khi đó `DI_Clamp1Up` **thật sự đổi giá trị** trong lúc vòng lặp chạy, và
vòng lặp **sẽ** thoát.

> ⚠⚠ **Đúng về kỹ thuật, và tệ hơn về hậu quả.**
>
> Vòng lặp bây giờ thoát được — nhưng nó thoát **sau khi kẹp lên xong**, tức là ⭐ **CPU đứng chờ suốt
> vài trăm mili-giây** ngay giữa vòng quét. Trong khoảng đó: không nấc thang nào khác chạy, không ngõ
> ra nào được cập nhật, không báo động nào được xét, ⚠⚠ **và nút dừng không được đọc**.
>
> ⭐ Nếu cơ cấu kẹt và tín hiệu không bao giờ tới, bạn quay lại đúng chỗ cũ: watchdog và CPU sang STOP.
>
> ⭐⭐ **Sửa một vòng lặp chờ bằng cách làm cho nó thoát được là chữa triệu chứng.** Vấn đề gốc là
> ⚠ **việc chờ không được nằm trong vòng lặp**, bất kể vòng lặp có thoát được hay không.

### `REPEAT ... UNTIL` — vòng lặp thứ ba, và cái bẫy riêng của nó

Chuẩn có **ba** vòng lặp. `REPEAT` ít gặp hơn nhưng có hai đặc điểm dễ vấp:

| | `WHILE ... DO` | `REPEAT ... UNTIL` |
|---|---|---|
| ⚠ Cực tính điều kiện | Chạy **CHỪNG NÀO** điều kiện còn đúng | ⭐ Chạy **CHO TỚI KHI** điều kiện đúng |
| ⚠⚠ Thân vòng lặp | Có thể **không chạy lần nào** | ⭐ **Luôn chạy ít nhất một lần** |
| Kiểm điều kiện | Đầu vòng | ⭐ **Cuối vòng** |

> ⚠⚠ **Hai chỗ sai kinh điển:**
>
> | | |
> |---|---|
> | 1 | ⭐ **Chép điều kiện của `WHILE` sang `REPEAT` mà quên đảo** — vòng lặp chạy đúng ngược lại ý muốn, và thường thành vô hạn |
> | 2 | ⭐ Quên rằng thân vòng **luôn chạy một lần** — với tập rỗng hoặc điều kiện đã thoả sẵn, `WHILE` không làm gì còn `REPEAT` **vẫn làm một lần** |

### ⭐⭐ Nguyên tắc chung — và nó giải thích mọi thứ ở trên

> ⭐⭐ **Điều kiện thoát của vòng lặp phải phụ thuộc vào một biến được cập nhật BÊN TRONG chính vòng
> lặp đó.**
>
> Rủi ro vòng lặp vô hạn — hoặc chạy quá lâu — ⚠ **lớn nhất khi điều kiện thoát phụ thuộc vào thứ bên
> ngoài**: tín hiệu vào, giá trị từ mạng, biến do tác vụ khác ghi.
>
> ⭐ Nguyên tắc này gói gọn cả ba trường hợp: `WHILE NOT DI_Clamp1Up` sai vì điều kiện đến từ **bên
> ngoài**; `FOR i := 0 TO n` rủi ro vì `n` đến từ **bên ngoài**; còn `FOR i := 0 TO 99` an toàn vì
> biến đếm do **chính vòng lặp** cập nhật.

**Và khi buộc phải dùng `WHILE`/`REPEAT`: kèm trần số vòng.** Đây là mẫu chuẩn:

```iecst
k := 1;
REPEAT
    LastArea := Pi * Radius[k] * Radius[k];
    Area[k]  := LastArea;
    k := k + 1;
UNTIL LastArea > 1000 OR k > 199        // ⭐ trần cứng nằm NGAY TRONG điều kiện, độc lập dữ liệu
END_REPEAT;
```

> ⚠⚠ **Mẫu này đã được sửa, và lỗi cũ đáng để nhìn kỹ.** Bản trước viết `Area[k] := …; k := k + 1;`
> rồi `UNTIL Area[k] > 1000` — ⚠ tức là **kiểm phần tử CHƯA được tính** ở lượt này, vì `k` vừa tăng.
> Vòng lặp dừng theo một giá trị cũ còn sót trong mảng. ⭐ Cấu trúc đó lấy theo một ví dụ trong sách
> tham khảo, và **mang theo cả lỗi của nó** — không ai thấy vì nó *trông* đúng.
>
> ⭐ Cách tránh cả lớp lỗi này: **kiểm đúng giá trị VỪA tính**, bằng một biến riêng (`LastArea`), thay
> vì đọc lại mảng bằng một chỉ số đã đổi. Đây chính là quy tắc CP3 của PLCopen: *mọi biến phải được
> gán trước khi đọc* (Phụ lục N).

| Đặt trần số vòng ở đâu | Ưu | Nhược |
|---|---|---|
| `IF k >= 200 THEN EXIT; END_IF;` trong thân | Nhìn thấy riêng từng dòng | ⚠ Vòng lặp có **hai** lối ra; PLCopen khuyên tránh `EXIT` (quy tắc L10) |
| ⭐ `UNTIL … OR k > 199` | ⭐ **Một** lối ra; đọc điều kiện là biết hết lúc nào vòng dừng | Điều kiện dài hơn một chút |

⭐ Dùng cách thứ hai. `EXIT` vẫn là lệnh chuẩn và bạn sẽ gặp nó trong chương trình của người khác —
nên phải biết nó làm gì:

> ⚠ **`EXIT` chỉ thoát MỘT tầng.** Đặt `EXIT` trong vòng lặp trong cùng thì **các vòng lặp bao ngoài
> vẫn chạy tiếp**. Muốn thoát nhiều tầng phải có cơ chế riêng — hoặc, tốt hơn, ⭐ **đừng lồng vòng lặp
> trong môi trường quét**.
>
> ⚡ Chuẩn còn có `CONTINUE` — bỏ qua phần còn lại của lần lặp hiện tại và sang lần kế. Nó **không**
> thoát vòng lặp, nên ⚠ **không phải công cụ phòng vòng lặp vô hạn**.

> ⚠ **`EXIT` không cứu được `WHILE` chờ tín hiệu.**
> Chuẩn có lệnh `EXIT` để thoát vòng lặp sớm. Nó hữu ích khi tìm thấy phần tử cần tìm trong mảng.
> Nhưng nó **không** giải quyết được ví dụ sai ở trên, vì vấn đề không phải thiếu lối thoát — vấn đề
> là **điều kiện thoát không bao giờ thay đổi** trong khi vòng lặp đang chạy.

### Bảng quyết định

| Việc | Dùng gì |
|---|---|
| Chờ tín hiệu từ cơ cấu | ❌ Không vòng lặp — **giữ nguyên bước** |
| Chờ hết thời gian | ❌ Không vòng lặp — **timer** (Chương 17) |
| Duyệt mảng cố định, nhỏ | ✅ `FOR` |
| Duyệt tập lớn hoặc kích thước thay đổi | ⚠ Chia nhỏ qua nhiều vòng quét |
| Lặp tới khi thoả điều kiện tính trong cùng vòng lặp | ⚠ `WHILE` **kèm trần số vòng** |
| Cần thân vòng chạy **ít nhất một lần** | ⚠ `REPEAT` — ⭐ nhớ **đảo cực tính điều kiện** |
| ⭐ Kiểm mọi vòng lặp trước khi giao | *"Điều kiện thoát có phụ thuộc biến được cập nhật **bên trong** không?"* |

---

## 20.6 ⭐ Khi nào ST là lựa chọn tệ

Đây là mục quan trọng nhất của chương, và nó **không phải bài toán kỹ thuật**.

### Tình huống

Bạn viết chương trình cho một máy đặt tại nhà máy của khách hàng. Bạn bàn giao, nhận tiền, đi làm dự
án khác.

Tám tháng sau, hai giờ sáng, máy dừng. Người mở phần mềm ra xem không phải bạn — đó là thợ bảo trì
của nhà máy đó. Người này đọc được ladder thành thạo, vì mọi máy khác trong xưởng đều là ladder.
Người này **chưa từng đọc ST**.

Chương trình của bạn gọn, đúng, và có cấu trúc đẹp. Nó cũng hoàn toàn không đọc được với người duy
nhất đang đứng trước cỗ máy lúc đó.

Kết quả: dây chuyền dừng tới sáng, hoặc tới khi có người gọi được cho bạn.

### Vì sao ladder vẫn thống trị ở tầng máy

Không phải vì ladder tốt hơn về mặt kỹ thuật. Vì ba lý do thực tế:

- **Nó nhìn giống sơ đồ mạch.** Người có nền điện đọc được ngay mà không cần học lập trình.
- **Trạng thái trực tuyến hiện ngay trên hình.** Nhìn nấc thang đang chạy, thấy tiếp điểm nào sáng,
  đứt ở đâu — chẩn đoán bằng mắt trong vài giây (Chương 51).
- **Người biết ladder nhiều hơn hẳn.** Đó là thực tế của lực lượng lao động, và nó đổi rất chậm.

### Quy tắc chọn

> **Chọn ngôn ngữ theo người sẽ SỬA chương trình, không theo người viết nó.**

Áp dụng thành quy tắc phân chia, đúng trong hầu hết dự án máy:

| Phần chương trình | Ngôn ngữ | Vì sao |
|---|---|---|
| **Logic liên động và điều kiện cho phép** | **Ladder** | Đây là chỗ người bảo trì nhìn đầu tiên khi máy không chạy. Phải chẩn đoán được bằng mắt |
| **Điều khiển ngõ ra cuối cùng** | **Ladder** | "Vì sao van này không mở" phải trả lời được bằng cách nhìn một nấc thang |
| Trình tự / máy trạng thái | ST (`CASE`) hoặc SFC | Gọn hơn nhiều; và người bảo trì thường chỉ cần biết *đang ở bước nào*, thứ hiển thị được trên màn hình |
| Tính toán, quy đổi thang, thống kê | **ST** | Ladder làm việc này rất tệ |
| Xử lý mảng, thanh ghi dịch | **ST** | Ladder không có vòng lặp |
| Xử lý bản tin truyền thông | **ST** | Thao tác chuỗi và mảng |

> 💡 **MẸO — câu hỏi phải hỏi trước khi viết dòng đầu tiên**
> *"Ai sẽ mở chương trình này ra lúc hai giờ sáng, và họ đọc được gì?"*
>
> Hỏi khách hàng, đừng đoán. Câu trả lời thuộc về **đặc tả** (Chương 23) chứ không phải sở thích của
> người lập trình. Có nhà máy quy định rõ ngôn ngữ được dùng; có nhà máy chưa từng nghĩ tới và sẽ
> biết ơn vì bạn hỏi.

### Khi buộc phải dùng ST cho phần người khác sẽ đọc

Đôi khi không có lựa chọn khác. Khi đó, giảm thiệt hại bằng bốn việc:

- **Hiển thị số hiệu bước và tên bước trên màn hình vận hành** (Chương 44), để chẩn đoán không cần
  mở phần mềm lập trình.
- **Chú thích nói *tại sao*, không nói *cái gì*.** `// tăng bước` là vô dụng; `// chờ phản hồi thật,
  không chờ timer — xem sự cố tháng 3` mới có giá trị.
- **Giữ mỗi khối ST ngắn và làm đúng một việc.** Một khối 800 dòng là không đọc được với bất kỳ ai.
- **Viết một trang giải thích cấu trúc chương trình** và để nó **trong tủ điện**, không phải trong
  email (Chương 30, Chương 52).

---

## 20.7 Trên máy mẫu DP-01 — chia việc theo ngôn ngữ

Cùng một chức năng, chia đúng chỗ:

### Ladder — điều kiện cho phép và ngõ ra cuối

```text
   M_Stn1_ClampReq  DI_EStopOK  DI_AirOK  DI_Door1Closed      DO_Clamp1Vlv
─────────┤ ├───────────┤ ├────────┤ ├──────────┤ ├───────────────( )──────
```

Nấc này trả lời câu hỏi mà người bảo trì hỏi nhiều nhất: *"vì sao kẹp không lên?"* Nhìn trực tuyến,
tiếp điểm nào không sáng là biết ngay — dừng khẩn, khí, hay cửa. Không cần đọc dòng code nào.

Chú ý `M_Stn1_ClampReq` là **yêu cầu** từ trình tự, còn `DO_Clamp1Vlv` là **ngõ ra thật**. Trình tự
chỉ nêu ý định; các điều kiện an toàn và liên động nằm ở nấc thang này, nơi ai cũng thấy.

### ST — trình tự

```iecst
CASE Stn1_Step OF
    10:
        M_Stn1_ClampReq := FALSE;
        IF DI_BoardStn1 AND M_Running THEN
            Stn1_Step := 20;
        END_IF;

    20:
        M_Stn1_ClampReq := TRUE;                 // chỉ là YÊU CẦU
        IF DI_Clamp1Up THEN                      // chuyển bước bằng phản hồi thật
            Stn1_Step := 30;
        END_IF;

ELSE
    Stn1_Step := 0;                              // giá trị lạ → về trạng thái đã biết
END_CASE;

// Giám sát thời gian bước — chạy song song, chỉ để BÁO LỖI (Chương 17)
T_Step20(IN := (Stn1_Step = 20), PT := T#3S);
IF T_Step20.Q THEN
    M_Stn1Timeout := TRUE;
END_IF;
```

### ST — tính toán

Phần thống kê chu kỳ và hiệu suất ở Chương 19, mục 19.8. Không ai muốn viết nó bằng ladder, và người
bảo trì cũng không cần đọc nó để sửa máy.

Sự phân chia này là **ranh giới thực dụng**: thứ người bảo trì cần nhìn thì để ở dạng nhìn được; thứ
họ không cần nhìn thì viết ở dạng gọn nhất.

---

## 20.8 Khác biệt giữa các hãng

### ⭐ Trước hết là tên gọi

| Hệ | Gọi ngôn ngữ này là gì |
|---|---|
| Chuẩn IEC 61131-3 · CODESYS · Beckhoff TwinCAT | **ST** — *Structured Text* |
| ⚠ **Siemens** | **SCL** — *Structured Control Language* |
| Mitsubishi (GX Works3) | **ST** |
| Rockwell (Studio 5000) | **ST** — routine kiểu *Structured Text* |

> ⚠ **Tra tài liệu Siemens bằng từ khoá "Structured Text" thì bạn sẽ không tìm ra.**
> Siemens gọi nó là **SCL**. Cùng một ngôn ngữ, cùng một chuẩn, khác tên. Chi tiết nhỏ này làm mất
> hàng giờ của người mới.

### Tính sẵn có và bản quyền

| Hệ | Điều phải kiểm **trước khi thiết kế** |
|---|---|
| **Siemens** | SCL có cho S7-1200 và S7-1500; ⚠ với S7-1500 thường cần ấn bản TIA Portal cao hơn. Kiểm gói bản quyền bạn đang có |
| **Mitsubishi** | GX Works3 hỗ trợ ST; dự án đời cũ trên GX Works2 phải là loại dự án có cấu trúc |
| **Rockwell** | ST có ở dòng Logix; ⚠ một số ấn bản phần mềm cũ **không** cho tạo routine ST — kiểm ấn bản đang có |
| **CODESYS / TwinCAT** | ST là ngôn ngữ chính, hỗ trợ đầy đủ nhất |
| ⚠ **Dòng CPU nhỏ, giá thấp** | **Nhiều dòng chỉ có ladder, không có ST.** Đây là ràng buộc phần cứng chứ không phải ràng buộc phần mềm — Chương 13, tiêu chí 5 |

> ⚠⚠ **Kiểm tính sẵn có của ST là việc làm lúc CHỌN CPU, không phải lúc viết code.**
> Phát hiện CPU không hỗ trợ ST sau khi đã thiết kế xong kiến trúc chương trình nghĩa là viết lại từ
> đầu bằng ladder, hoặc đổi CPU. Cả hai đều đắt.

### Các khác biệt còn lại

| Điểm | Điều cần biết |
|---|---|
| Chú thích `//` | Có ở TIA Portal, GX Works3, Studio 5000 và CODESYS. Kiểu `(* … *)` thì chắc chắn có ở mọi hệ |
| ⚠ Watchdog | Siemens: *cycle monitoring time* trong thuộc tính CPU. Rockwell: watchdog **riêng cho từng tác vụ**. Mitsubishi: đặt trong tham số PLC, kèm lệnh `WDT` để nạp lại giữa vòng quét dài. **Đừng tăng nó để chữa vòng lặp chậm** (Bẫy 5) |
| Trạng thái trực tuyến của ST | Khác nhau nhiều và ảnh hưởng thẳng tới việc chẩn đoán: có hệ hiện giá trị ngay cạnh biến trong code, có hệ phải mở bảng theo dõi riêng. ⭐ Đây là một lý do thực tế nữa cho quy tắc ở mục 20.6 |
| Gỡ lỗi từng bước | Ít hệ hỗ trợ chạy từng dòng như IDE thông thường. Đừng thiết kế dựa trên giả định có nó |
| Trộn ngôn ngữ trong một dự án | Mọi hệ nêu trên đều cho mỗi khối hoặc mỗi routine dùng một ngôn ngữ riêng — đó chính là điều kiện để làm được bảng phân chia ở mục 20.6 |

## 20.9 Bẫy thường gặp

### 🔍 BẪY 1 — `WHILE` chờ tín hiệu vào

**Hiện tượng:** CPU chuyển sang STOP ngay lần đầu chạy tới đoạn đó; mọi ngõ ra tắt giữa chu trình.
**Nguyên nhân:** ảnh ngõ vào không được cập nhật trong lúc vòng lặp chạy (mục 20.5).
**Cách sửa:** chờ bằng cách giữ nguyên bước, không bằng vòng lặp.

### 🔍 BẪY 2 — Ghi vào cùng một ngõ ra ở hai nhánh xa nhau

**Hiện tượng:** ngõ ra hành xử khó hiểu; nhánh phía dưới luôn thắng, kể cả khi nhánh phía trên "rõ
ràng đúng".
**Cách sửa:** mỗi ngõ ra chỉ được ghi ở **đúng một chỗ**. Dùng tham chiếu chéo để kiểm (Chương 22).

### 🔍 BẪY 3 — Quên nhánh `ELSE` trong `CASE` máy trạng thái

**Hiện tượng:** trình tự đứng im vĩnh viễn, không báo gì, đèn vẫn xanh — đúng cỗ máy ở Chương 26.
**Cách sửa:** luôn có `ELSE` đưa về trạng thái đã biết chắc và đặt cờ lỗi.

### 🔍 BẪY 4 — `FOR` với trần đến từ tính toán

**Hiện tượng:** thời gian quét thỉnh thoảng vọt lên; thỉnh thoảng watchdog kích hoạt, không tái hiện
được.
**Cách sửa:** trần vòng lặp phải là hằng số, hoặc phải kẹp trước khi vào vòng.

### 🔍 BẪY 5 — Tăng watchdog để chữa quét chậm

**Hiện tượng:** máy hết STOP, nhưng đáp ứng của toàn bộ máy chậm đi — mọi cơ cấu phản ứng trễ hơn, và
độ chính xác của mọi timer giảm (Chương 17, mục 17.3).
**Cách sửa:** tìm nguyên nhân quét chậm. Watchdog là **công cụ phát hiện**, không phải tham số để
chỉnh cho vừa ý.

### 🔍 BẪY 6 — Viết toàn bộ chương trình bằng ST vì nó gọn hơn

**Hiện tượng:** không có triệu chứng nào — cho tới lần đầu máy hỏng lúc bạn không có mặt.
**Cách sửa:** mục 20.6. Đây là quyết định phải chốt ở giai đoạn đặc tả, không phải lúc viết code.

### 🔍 BẪY 7 — Dùng chung một thể hiện khối chức năng

```iecst
// ✗ SAI — một thể hiện TON cho hai bước
T_Guard(IN := (Stn1_Step = 20), PT := T#3S);
IF T_Guard.Q THEN  M_Fault20 := TRUE;  END_IF;
T_Guard(IN := (Stn1_Step = 40), PT := T#5S);    // ghi đè bộ nhớ lần gọi trên
IF T_Guard.Q THEN  M_Fault40 := TRUE;  END_IF;
```

**Hiện tượng:** timeout báo sai bước, hoặc không báo.
**Cách sửa:** mỗi chỗ dùng một thể hiện riêng — `T_Step20`, `T_Step40`.

### 🔍 BẪY 8 — Chú thích lặp lại code

`// tăng bước` viết cạnh `Stn1_Step := 30;` không thêm thông tin nào.

**Hiện tượng:** không phải lỗi chạy, nhưng làm chương trình khó bảo trì đúng vào lúc cần nhất.
**Cách sửa:** chú thích trả lời *vì sao*, và ghi lại những gì không suy ra được từ code — lý do chọn
ngưỡng, sự cố đã dẫn tới đoạn code này, cạm bẫy đã tránh (Chương 30).

---

## 20.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Gán và so sánh bằng | Gán `:=` · so sánh `=` |
| Viết máy trạng thái | `CASE` — **luôn có nhánh `ELSE`** |
| Chờ tín hiệu | ❌ Không vòng lặp — giữ nguyên bước |
| Chờ thời gian | ❌ Không vòng lặp — timer |
| `WHILE` | Chỉ khi điều kiện thoát tính **trong cùng vòng lặp**, và có trần số vòng |
| `FOR` | Trần phải là hằng số hoặc đã kẹp; đo thời gian quét sau khi thêm |
| Watchdog kích hoạt | Sửa vòng lặp, **không tăng watchdog** |
| Ghi ngõ ra | Đúng **một chỗ** cho mỗi ngõ ra |
| Khối chức năng | Mỗi chỗ dùng **một thể hiện riêng** |
| ST hợp cho | Tính toán · trình tự · mảng · truyền thông |
| ⭐ Ladder hợp cho | **Liên động và ngõ ra cuối** — thứ người bảo trì nhìn đầu tiên |
| ⭐⭐ Điều kiện thoát vòng lặp | **Phải phụ thuộc biến cập nhật BÊN TRONG vòng lặp** |
| ⚠ `REPEAT` khác `WHILE` | Cực tính **ngược**, và thân vòng **luôn chạy ít nhất một lần** |
| ⚠ `EXIT` thoát mấy tầng | ⭐ **Một tầng** — vòng bao ngoài vẫn chạy tiếp |
| Dùng truy cập trực tiếp để cứu vòng lặp chờ | ⚠⚠ **Chữa triệu chứng** — CPU vẫn đứng chờ, nút dừng vẫn không được đọc |
| ⭐ Chọn ngôn ngữ theo | **Người sẽ SỬA**, không theo người viết |

---

## 20.11 Tự kiểm

1. Viết phép gán và phép so sánh bằng trong ST. Nhầm lẫn giữa hai ký hiệu này gây hậu quả gì, và vì
   sao đó là hậu quả tương đối lành?
2. Vì sao nhánh `ELSE` trong `CASE` của máy trạng thái là bắt buộc? Mô tả triệu chứng khi thiếu nó.
3. ⭐ Giải thích vì sao `WHILE NOT DI_Clamp1Up DO ; END_WHILE;` chắc chắn làm treo CPU. Nêu rõ cơ chế
   liên quan tới vòng quét.
4. Watchdog kích hoạt thì máy dừng theo kiểu nào? Vì sao kiểu dừng đó tệ hơn dừng bình thường?
5. Vì sao **không** được tăng thời gian watchdog để chữa một vòng lặp chậm? Nêu hai hậu quả.
6. Nêu ba nhóm việc ST rõ ràng hơn ladder, và giải thích ngắn gọn vì sao.
7. ⭐ Một chương trình viết hoàn toàn bằng ST, chạy đúng, gọn, có cấu trúc tốt. Nêu tình huống cụ thể
   khiến nó vẫn là quyết định sai.
8. Phần nào của chương trình DP-01 nên viết bằng ladder, dù ST gọn hơn? Vì sao?
9. Vì sao lỗi ghi trùng ngõ ra khó phát hiện trong ST hơn trong ladder? Công cụ nào giúp tìm?
10. ⭐ Câu hỏi nào phải hỏi **khách hàng** trước khi chọn ngôn ngữ lập trình, và vì sao nó thuộc về
    đặc tả chứ không thuộc về sở thích kỹ thuật?
11. ⭐⭐ Phát biểu **nguyên tắc chung** về điều kiện thoát vòng lặp. Dùng nó giải thích vì sao
    `WHILE NOT DI_Clamp1Up` sai còn `FOR i := 0 TO 99` an toàn.
12. ⚠ `REPEAT` khác `WHILE` ở **hai** điểm. Nêu cả hai, và cho một tình huống mà chép nhầm từ cái này
    sang cái kia tạo ra vòng lặp vô hạn.
13. ⚡ Có người sửa vòng lặp chờ bằng **truy cập trực tiếp** để tín hiệu đổi được trong lúc lặp. Vòng
    lặp thoát được thật. ⭐ Vì sao đây vẫn là lời giải sai? Nêu bốn thứ ngừng hoạt động trong lúc CPU
    đứng chờ.

> Câu 3, 7 và 10 là ba câu phân loại. Câu 7 và 10 là tinh thần của cả chương: **chương trình tốt
> nhất không phải chương trình gọn nhất — mà là chương trình người khác sửa được lúc bạn vắng mặt.**

---

### Chương tiếp theo

Chương 21 — **FBD, SFC và IL**. Bạn đã có ladder và ST. Chương sau hoàn tất bộ năm ngôn ngữ của chuẩn:
FBD cho luồng tín hiệu, SFC cho tuần tự — ngôn ngữ được thiết kế riêng cho đúng bài toán trình tự mà
bạn vừa viết bằng `CASE` — và IL, đủ để đọc chương trình cũ.

### Nguồn tham khảo chương 20

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: cú pháp Structured Text,
  các cấu trúc điều khiển, phân biệt hàm với khối chức năng. *(tiêu chuẩn có bản quyền)*
- Tài liệu lập trình của từng hệ trong Phụ lục A — dùng cho: dòng CPU nào hỗ trợ ST, giá trị watchdog
  mặc định và cách đặt, và chất lượng hiển thị trạng thái trực tuyến của ST. Ba điểm này ảnh hưởng
  trực tiếp tới quyết định ở mục 20.6.
- Đặc tả trình tự của DP-01 — Phụ lục J.
- **Hanssen, Dag H.** — *Programmable Logic Controllers: A Practical Approach to IEC 61131-3 using
  CoDeSys*, §11.8: ba vòng lặp `WHILE` / `FOR` / `REPEAT`, ⭐ `REPEAT` **chạy thân ít nhất một lần**
  và điều kiện **ngược cực tính** với `WHILE`; ⭐⭐ nguyên tắc *điều kiện thoát nên phụ thuộc biến được
  cập nhật bên trong vòng lặp*; và ⚠ `EXIT` đặt ở vòng trong **không dừng vòng bao ngoài** (mục 20.5).

> ⚡ Bảng phân chia ngôn ngữ ở mục 20.6 là **quy tắc thực dụng**, không phải yêu cầu tiêu chuẩn. Một
> số đơn vị có quy định nội bộ chặt hơn (ví dụ: toàn bộ chương trình phải là ladder); một số ngành có
> yêu cầu riêng về ngôn ngữ được phép dùng cho phần liên quan an toàn. **Quy định của khách hàng và
> của ngành luôn thắng bảng này** — và phải hỏi trước khi viết, không phải sau.
