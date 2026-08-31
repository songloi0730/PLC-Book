# Chương 30 — Chuẩn hoá & tái sử dụng

> **Lát cắt máy mẫu:** 2 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp, hai trạm, trình
> tự song song, công thức sản phẩm.

---

## 30.1 Người đọc thật sự của chương trình bạn viết

Chương trình PLC có hai loại người đọc, và loại thứ hai mới là loại quyết định cách bạn nên viết.

**Loại thứ nhất là CPU.** Nó không quan tâm tên tag, không quan tâm comment, không quan tâm cấu trúc.
Với nó, một chương trình gọn gàng và một chương trình hỗn độn là như nhau.

**Loại thứ hai là người sẽ mở chương trình này ra lúc hai giờ sáng**, khi máy dừng và cả xưởng đang
chờ. Người đó:

- **Không phải bạn.** Hoặc là bạn của sáu tháng sau, đã quên hết.
- **Không có tài liệu** trong tay, hoặc có mà không kịp đọc.
- **Đang chịu áp lực** — mỗi phút máy dừng là tiền.
- **Không dám sửa nhiều**, vì không biết sửa chỗ này sẽ hỏng chỗ nào.

Chương này là cách viết cho người đó. Và đây không phải phép lịch sự — nó là **một yêu cầu kỹ thuật**,
vì thời gian dừng máy là chi phí thật.

> ⚡ **LƯU Ý**
> Mọi quy ước trong chương này đều có một tiêu chí duy nhất để đánh giá: *"nó có làm người kia hiểu
> nhanh hơn không?"* Quy ước nào không trả lời được câu đó thì là trang trí, không phải chuẩn hoá.

---

## 30.2 Đặt tên — nhất quán quan trọng hơn đẹp

Cả chương này nói về **chuẩn hoá** *(standardization)* và **dùng lại** *(reuse)*. Bộ quy tắc đặt tên
thống nhất trong một đơn vị gọi là **quy ước đặt tên** *(naming convention)*; tập các khối đã kiểm
chứng đem dùng lại giữa các dự án gọi là **thư viện** *(library)*.

### Vì sao nhất quán quan trọng hơn

Có nhiều cách đặt tên tag hợp lý. Không cách nào **đúng tuyệt đối**. Nhưng **trộn nhiều cách trong
cùng một chương trình** thì luôn sai — vì người đọc mất khả năng **đoán**.

Khi quy ước nhất quán, nhìn thấy `DI_BoardStn2` là bạn biết ngay: ngõ vào số, thuộc trạm 2, liên quan
board. Bạn không cần tra. Khi quy ước hỗn độn, mỗi tag là một lần phải đi tìm.

> **Giá trị của quy ước đặt tên nằm ở chỗ nó cho phép ĐOÁN ĐÚNG.** Một quy ước "xấu" mà nhất quán còn
> tốt hơn ba quy ước "đẹp" trộn lẫn.

### Quy ước dùng trong sách

```text
<tiền tố>_<vùng><chức năng>

DI_   ngõ vào số          DO_   ngõ ra số
AI_   ngõ vào analog      AO_   ngõ ra analog
M_    biến nội bộ         X_    tín hiệu đã qua lớp chọn nguồn (Chương 50)
T_    thể hiện timer      C_    thể hiện counter
S_    bit trạng thái      FB_   kiểu khối chức năng
```

Ví dụ từ DP-01:

| Tag | Đọc ra là | |
|---|---|---|
| `DI_BoardStn1` | ngõ vào số · board · trạm 1 | |
| `DO_Clamp1Vlv` | ngõ ra số · van kẹp · trạm 1 | |
| `M_Stn1_ClampReq` | biến nội · trạm 1 · yêu cầu kẹp | ⭐ yêu cầu, không phải lệnh ra van (Chương 27) |
| `Stn2_Ready` | giao diện công bố của trạm 2 | không có tiền tố `M_` vì nó là giao diện, không phải biến nội |

### Năm quy tắc đặt tên

| # | Quy tắc | Vì sao |
|---|---|---|
| 1 | **Tên nói lên ý nghĩa, không nói cách hiện thực** | `M_ClampReq` tốt hơn `M_Bit47` |
| 2 | **Không viết tắt tuỳ hứng** | `Clamp` tốt hơn `Clp`. Viết tắt chỉ dùng khi đã thành quy ước chung của cả dự án |
| 3 | **Cùng một khái niệm dùng cùng một từ** | Đừng chỗ thì `Board`, chỗ thì `PCB`, chỗ thì `Part` |
| 4 | **Số thứ tự đặt ở vị trí cố định** | `Stn1`, `Stn2` — không phải `Station1` rồi `Stn_2` |
| 5 | ⭐ **Tên phản ánh trạng thái tích cực** | `DI_DoorClosed` tốt hơn `DI_DoorNotOpen` — phủ định chồng phủ định là nguồn lỗi |

Quy tắc 5 đáng giải thích thêm. So sánh:

```iecst
// ✗ Khó đọc — hai phủ định
IF NOT DI_DoorNotOpen THEN …

// ✓ Rõ ràng
IF DI_DoorClosed THEN …
```

Với tín hiệu an toàn, tên nên phản ánh **trạng thái an toàn là mức 1** — khớp với nguyên tắc tiếp điểm
NC ở Chương 4: `DI_EStopOK`, `DI_AirOK`, `DI_DoorClosed`. Nhìn tên là biết "1 nghĩa là ổn".

---

## 30.3 Cấu trúc chương trình — theo cơ cấu, không theo bước

Đây là quyết định cấu trúc quan trọng nhất, và nó nối thẳng vào Chương 27.

### Hai cách tổ chức

| | **Theo bước** | ⭐ **Theo cơ cấu** |
|---|---|---|
| Chương trình chia thành | Bước 1, bước 2, bước 3… | Xy-lanh, trạm, chuyền |
| Muốn sửa một cơ cấu | Phải tìm ở **mọi bước** dùng nó | Mở **một khối** |
| Thêm một cơ cấu giống hệt | Chép và sửa ở nhiều chỗ | **Tạo thêm một thể hiện** |
| Thêm liên động cho một cơ cấu | Thêm ở mọi chỗ điều khiển nó | Thêm **một chỗ** |
| Khi máy lớn lên | Số chỗ phải sửa tăng theo số bước | Không đổi |

Cách tổ chức theo bước có vẻ tự nhiên vì nó khớp với cách bạn nghĩ về chu trình. Nhưng nó làm **mỗi
cơ cấu bị rải ra khắp chương trình**, và mọi thay đổi về sau đều tốn.

### Ba mức tái sử dụng

| Mức | Đơn vị | Ví dụ ở DP-01 | Số thể hiện |
|---|---|---|---|
| **1 — Cơ cấu** | Một thiết bị vật lý | `FB_Cylinder2Pos` | 4 (chặn ×2, kẹp ×2) |
| **2 — Cụm** | Một nhóm cơ cấu làm một việc | `FB_Station` | 2 |
| **3 — Máy** | Toàn máy | Máy trạng thái | 1 |

Mức 1 cho lợi ích lớn nhất và dễ làm nhất. Bốn xy-lanh của DP-01 khác nhau ở tag, giống nhau ở hành
vi — viết một khối, tạo bốn thể hiện (Chương 27, mục 27.3).

### Gói trạng thái vào một kiểu dữ liệu

Khi một cơ cấu có nhiều biến liên quan, gom chúng vào một **kiểu dữ liệu người dùng** *(user-defined
type, UDT)* thay vì để rời rạc:

```iecst
// ✗ Rời rạc — bốn biến không có gì nối chúng lại
M_Stn1_Step      : INT;
M_Stn1_Fault     : BOOL;
M_Stn1_FaultStep : INT;
M_Stn1_Ready     : BOOL;

// ✓ Gói lại — một kiểu, dùng cho mọi trạm
TYPE ST_Station :
STRUCT
    Step       : INT;
    Fault      : BOOL;
    FaultStep  : INT;
    Ready      : BOOL;
    Busy       : BOOL;
    BoardDone  : BOOL;
END_STRUCT
END_TYPE

VAR
    Stn1 : ST_Station;
    Stn2 : ST_Station;
END_VAR
```

Ba lợi ích, và lợi ích thứ ba là lớn nhất:

1. Thêm trạm thứ ba chỉ cần thêm **một dòng khai báo**.
2. Thêm một trường cho mọi trạm chỉ cần sửa **một chỗ**.
3. ⭐ **Không thể quên** — khi bạn tạo `Stn3`, nó tự động có đủ mọi trường. Với biến rời rạc, bạn sẽ
   quên ít nhất một cái.

---

## 30.4 Comment — viết như nhật ký kỹ thuật

### Comment vô dụng và comment có giá trị

```iecst
// ✗ Vô dụng — lặp lại đúng cái code đã nói
// Đặt M_Stn1_ClampReq bằng TRUE
M_Stn1_ClampReq := TRUE;

// ✓ Có giá trị — nói cái code KHÔNG nói được
// Kẹp phải lên TRƯỚC khi hạ chặn, nếu không board rơi tự do xuống
// chuyền đang chạy (bảng va chạm V1 — xem đặc tả mục 4.2).
M_Stn1_ClampReq := TRUE;
```

Nguyên tắc: **code nói CÁI GÌ, comment nói VÌ SAO.** Nếu comment chỉ dịch code sang tiếng Việt thì nó
là gánh nặng — nó sẽ lỗi thời và gây hiểu nhầm.

### Bốn thứ đáng comment

| Loại | Ví dụ | Vì sao |
|---|---|---|
| **Vì sao làm thế này** | "hạ kẹp trước vì V1" | Không suy ra được từ code |
| **Vì sao KHÔNG làm cách khác** | "không dùng lệnh X vì hệ này không giữ giá trị qua mất điện" | ⭐ Ngăn người sau "sửa lại cho gọn" và phá logic |
| **Con số từ đâu ra** | "3 s = thời gian đo được 0,8 s × biên 3,5 lần" | Người sau biết được có sửa được không |
| **Đã thử gì mà không được** | "đã thử dùng cảm biến chung cho hai trạm — không được vì thời gian đáp ứng" | ⭐ Tiết kiệm cho người sau đúng lượng thời gian bạn đã mất |

Hai dòng ⭐ là hai loại comment quý nhất và ít người viết nhất. Chúng biến chương trình thành **nhật
ký kỹ thuật** — nơi ghi lại không chỉ kết quả mà cả **quá trình đi tới kết quả**.

> 💡 **MẸO**
> Khi bạn vừa mất hai giờ để tìm ra một cách làm, hãy dành hai phút viết comment giải thích. Bạn vừa
> tiết kiệm hai giờ cho người sau — hoặc cho chính bạn sáu tháng nữa.

### Comment ở đâu

| Vị trí | Nội dung |
|---|---|
| **Đầu khối** | Khối này làm gì, ai gọi nó, giao diện gồm gì |
| **Đầu mỗi bước trình tự** | Bước này làm gì, chờ gì, timeout bao nhiêu và vì sao |
| **Tại chỗ khó hiểu** | Vì sao lại viết thế này |
| **Tại chỗ dễ bị sửa nhầm** | ⚠ Cảnh báo rõ: "đừng đổi thứ tự hai dòng này — xem…" |

Dòng cuối quan trọng với những chỗ như mạch tạo xung ở Chương 10, nơi **thứ tự là một phần của logic**
nhưng nhìn code không thấy được điều đó.

---

## 30.5 Thư viện dùng lại — và cái giá của dùng lại sai

Sau vài dự án, bạn có một bộ khối dùng được: xy-lanh, băng tải, trạm, xử lý báo động. Dùng lại chúng
tiết kiệm rất nhiều thời gian.

Nhưng dùng lại có cái giá, và cái giá đó thường bị bỏ qua.

### Ba kiểu dùng lại

| Kiểu | Cách làm | Ưu | Nhược |
|---|---|---|---|
| **Chép** | Chép khối từ dự án cũ sang, sửa cho hợp | Đơn giản, độc lập | Sửa lỗi ở bản gốc **không lan** sang các bản đã chép |
| **Thư viện có phiên bản** | Khối nằm trong thư viện chung, dự án tham chiếu tới một phiên bản | Sửa lỗi lan được; biết dự án nào dùng phiên bản nào | Cần kỷ luật quản lý phiên bản |
| **Chép rồi sửa nhiều** | Chép xong sửa tới mức không còn nhận ra | ❌ Mất hết lợi ích | Vẫn mang theo phần thừa của bản gốc |

Kiểu thứ ba là kiểu hay xảy ra nhất trong thực tế, và nó tệ hơn viết mới — vì chương trình mang theo
**những đoạn code không ai hiểu vì sao có ở đó**.

> ⚠ **NGUY HIỂM — dùng lại khối cho máy có mối nguy khác**
> Một khối xy-lanh viết cho máy có tải nhẹ nằm ngang, đem dùng cho **trục đứng có tải treo**, sẽ mang
> theo giả định "mất lệnh thì về vị trí lò xo là an toàn" — giả định đó **sai** với trục đứng
> (Chương 47, 48).
>
> **Mỗi lần dùng lại một khối trong bối cảnh mới, phải rà lại các giả định về an toàn của nó.** Khối
> càng tiện thì càng dễ dùng mà không nghĩ.

### Ba yêu cầu với một khối đáng đưa vào thư viện

| # | Yêu cầu | Vì sao |
|---|---|---|
| 1 | **Giao diện rõ ràng, ít chân, ổn định** | Chân vào/ra là hợp đồng — thêm chân là thay đổi phá vỡ |
| 2 | **Không phụ thuộc biến toàn cục** | Khối đọc lén một biến ngoài thì không tái dùng được ở dự án khác |
| 3 | **Có ghi rõ giả định** | ⭐ "khối này giả định cơ cấu về vị trí lò xo khi mất lệnh" — viết ngay đầu khối |

---

## 30.6 Quản lý phiên bản chương trình PLC

### Cái gì so sánh được, cái gì không

Đây là chỗ chương trình PLC khác phần mềm thông thường, và khác biệt đó quyết định cách làm:

| Thành phần | So sánh được không | Ghi chú |
|---|---|---|
| Logic chương trình | ✅ Có — mọi hãng đều có chức năng **so sánh dự án** | Công cụ mạnh nhất bạn có |
| Cấu hình phần cứng | ⚠ Một phần | Thường phải xem bằng mắt |
| Tham số thiết bị (driver, module thông minh) | ❌ Thường không | Phải xuất ra và lưu riêng |
| Dự án màn hình vận hành (Chương 44) | ⚠ Tuỳ hệ | Nhiều hệ không so sánh được |
| Công thức sản phẩm | ✅ Nếu lưu dạng bảng | Nên tách khỏi chương trình (Chương 29) |

> ⚠ **NGUY HIỂM**
> Vì phần lớn không so sánh được bằng công cụ, **bản sao lưu phải là bản đầy đủ** — không chỉ file
> chương trình. Thiếu tham số driver hoặc cấu hình phần cứng nghĩa là **không khôi phục được máy**,
> dù bạn có file chương trình. Chương 54.

### Quy ước tối thiểu

Không cần hệ thống phức tạp. Bốn thứ này đã giải quyết phần lớn vấn đề:

| # | Quy ước | Cách làm |
|---|---|---|
| 1 | **Đánh số phiên bản** và ghi vào **một biến trong chương trình** | Đọc được khi xem trực tuyến, không cần mở file |
| 2 | **Nhật ký thay đổi** ngay trong chương trình | Ai · ngày · sửa gì · **vì sao** |
| 3 | **Sao lưu trước mọi thay đổi**, đặt tên có ngày và phiên bản | `DP01_v1.4_2026-08-31_truoc-sua-timeout` |
| 4 | Hiển thị **phiên bản trên màn hình vận hành** (Chương 44) | Người ở xa hỏi "máy đang chạy bản nào" là trả lời được ngay |

```text
// ── Nhật ký thay đổi — giữ ngay đầu chương trình ──
// v1.4  2026-08-31  NVA  Tăng timeout bước S1.20 từ 2 s lên 3 s.
//                        Lý do: đo thực tế 0,8 s nhưng lúc áp khí thấp
//                        lên tới 1,9 s → biên cũ quá sát. Đã đo lại 20 chu kỳ.
// v1.3  2026-08-20  NVA  Thêm giám sát tình trạng ionizer làm điều kiện
//                        cho phép chạy (yêu cầu QC sau sự cố lô 2608).
```

Chú ý cột **vì sao** trong cả hai dòng. Không có nó, người sau sẽ thấy timeout 3 s và không biết có
được đổi hay không.

---

## 30.7 Bẫy thường gặp

### 🔍 BẪY 1 — "Sẽ dọn dẹp sau"

Viết nhanh cho kịp chạy thử, định dọn sau. **Không bao giờ có "sau"** — sau khi máy chạy thì không ai
cho dừng máy để dọn code.

Chi phí đặt tên đúng và comment đúng **ngay lúc viết** gần bằng không. Chi phí làm lại sau đó rất lớn.

### 🔍 BẪY 2 — Quy ước chỉ nằm trong đầu người viết

Bạn có quy ước rõ ràng, nhưng không viết ra. Người thứ hai vào dự án đặt tên theo cách của họ. Sau sáu
tháng có hai quy ước trộn lẫn — tệ hơn không có quy ước nào.

**Viết quy ước ra một trang**, để trong thư mục dự án, và đi qua nó với người mới trong ngày đầu.

### 🔍 BẪY 3 — Comment dịch lại code

Đã nêu ở mục 30.4. Loại comment này còn có hại: khi code đổi mà comment không đổi, **comment nói dối**
— và người đọc tin nó.

### 🔍 BẪY 4 — Dùng lại khối mà không rà giả định an toàn

Đã cảnh báo ở mục 30.5. Đây là bẫy **có thể gây tai nạn**, không chỉ gây phiền.

### 🔍 BẪY 5 — Tối ưu hoá làm mất khả năng đọc

```iecst
// ✗ Gọn nhưng không ai đọc nổi
M_Out := (A AND NOT B) OR (C AND (D OR NOT E)) AND NOT (F OR G);

// ✓ Dài hơn, đọc được, gỡ lỗi được
M_PartPresent  := A AND NOT B;
M_ReadyToStart := C AND (D OR NOT E);
M_NoFault      := NOT (F OR G);
M_Out          := M_PartPresent OR (M_ReadyToStart AND M_NoFault);
```

Bản dưới dài hơn bốn dòng và **tốn thêm vài micro-giây** mỗi vòng quét. Đổi lại, khi máy không chạy,
bạn xem ba biến trung gian là biết ngay cái nào sai — thay vì phải tự tính lại cả biểu thức.

Đây là ứng dụng của "thiết kế sẵn điểm đo cho chính mình" ở Chương 15 và 51.

### 🔍 BẪY 6 — Sao lưu chỉ file chương trình

Đã cảnh báo ở mục 30.6. Bản sao lưu thiếu cấu hình phần cứng và tham số thiết bị là bản sao lưu
**không khôi phục được máy**.

### 🔍 BẪY 7 — Nhật ký thay đổi chỉ ghi "cái gì"

*"v1.4 — sửa timeout"* không giúp gì. Người sau vẫn không biết **có được đổi tiếp không**, và **vì sao
lại là 3 giây**.

Cột **vì sao** là cột duy nhất không suy ra được từ chương trình.

---

## 30.8 Bảng chốt

| # | Kiểm | Đạt khi |
|---|---|---|
| 1 | Quy ước đặt tên đã **viết ra thành văn** | Có, trong thư mục dự án |
| 2 | Tên tag phản ánh **trạng thái tích cực** | `DoorClosed`, không phải `DoorNotOpen` |
| 3 | Chương trình tổ chức **theo cơ cấu**, không theo bước | Mỗi cơ cấu ở một khối |
| 4 | Cơ cấu cùng loại dùng **chung một khối, nhiều thể hiện** | Có |
| 5 | Trạng thái của một cụm gói vào **một kiểu dữ liệu** | Có |
| 6 | Comment nói **vì sao**, không dịch lại code | Có |
| 7 | Có comment cho **những cách đã thử mà không được** | Có ở những chỗ từng mất thời gian |
| 8 | Khối trong thư viện có **ghi rõ giả định an toàn** | Có |
| 9 | **Nhật ký thay đổi** trong chương trình, có cột *vì sao* | Có |
| 10 | Phiên bản **hiển thị trên màn hình** và đọc được khi xem trực tuyến | Có |

---

## 30.9 Tự kiểm

1. Ai là **người đọc thật sự** của chương trình bạn viết? Bốn đặc điểm của người đó là gì?
2. Vì sao **nhất quán** quan trọng hơn **đẹp** khi đặt tên? Trả lời bằng khái niệm "đoán đúng".
3. Vì sao `DI_DoorClosed` tốt hơn `DI_DoorNotOpen`? Liên hệ với Chương 4.
4. So sánh tổ chức chương trình **theo bước** và **theo cơ cấu**. Điều gì xảy ra với mỗi cách khi máy
   lớn lên?
5. Nêu **ba lợi ích** của việc gói trạng thái một cụm vào một kiểu dữ liệu. Lợi ích nào lớn nhất?
6. Nêu **bốn thứ đáng comment**. Hai thứ nào quý nhất và ít người viết nhất?
7. Bạn dùng lại khối xy-lanh từ một máy cũ cho một **trục đứng có tải treo**. Điều gì phải rà lại?
8. Cái gì trong dự án PLC **so sánh được** bằng công cụ và cái gì không? Hệ quả với việc sao lưu?
9. Vì sao viết `M_Out := (A AND NOT B) OR …` gọn trong một dòng lại là lựa chọn tệ?
10. Nhật ký thay đổi ghi *"v1.4 — sửa timeout"*. Thiếu gì, và vì sao thứ thiếu đó quan trọng nhất?

Câu 2, 6 và 7 là ba câu phân loại. Câu 7 là câu về an toàn — dùng lại code là chỗ giả định cũ đi theo
mà không ai để ý.

---

### Chương tiếp theo

**Chương 31 — Tín hiệu analog & vòng dòng 4–20 mA.** Hết Phần IV. Từ chương sau, máy mẫu được bóc thêm
một lớp: analog và chuyển động.

---

### Nguồn tham khảo chương 30

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: khối chức năng, thể hiện,
  kiểu dữ liệu người dùng. *(tiêu chuẩn có bản quyền)*
- Hướng dẫn lập trình và quy ước phong cách của các hãng PLC — nguồn chính cho mục 30.2 và 30.3; các
  tài liệu này bàn đúng về cấu trúc chương trình, khối tái dùng và tối ưu vùng nhớ. Số hiệu cụ thể
  ghi trong Phụ lục A1.
- Quy ước đặt tên và cấu trúc dùng trong sách — Phụ lục C.

> ⚡ Quy ước đặt tên ở mục 30.2 là **quy ước của cuốn sách này**, không phải chuẩn ngành. Dự án của bạn
> có thể dùng quy ước khác — điều bắt buộc là **có một quy ước, viết ra thành văn, và dùng nhất quán**.
