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

### Bốn quy ước thật sự có người dùng — cùng một tín hiệu, bốn cái tên

Nói *"có nhiều cách đặt tên"* rồi bỏ qua là vô ích. Dưới đây là **bốn quy ước gặp thật trong nghề**,
tất cả đặt tên cho **cùng một tín hiệu**: cảm biến báo **xy-lanh kẹp ở trạm 1 đã lên**.

| | Quy ước | Cái tên |
|---|---|---|
| **A** | **Địa chỉ trần** — không có tên tượng trưng | `X10` · `I0.2` · `%IX0.2` |
| **B** | ⭐ **Tiền tố loại + chức năng** — *sách này dùng* | `DI_Clamp1Up` |
| **C** | **Phân cấp theo cấu trúc** | `Stn1.Clamp.UpSensor` |
| **D** | **Theo mã thiết bị trên bản vẽ điện** | `B12_Clamp1Up` |

Cùng một đoạn logic, viết bằng bốn quy ước:

```iecst
// A — địa chỉ trần
IF X10 AND NOT X11 THEN  M20 := TRUE;  END_IF;

// B — tiền tố loại + chức năng
IF DI_Clamp1Up AND NOT DI_Clamp1Dn THEN  M_Stn1_ClampedOk := TRUE;  END_IF;

// C — phân cấp
IF Stn[1].Clamp.UpSensor AND NOT Stn[1].Clamp.DnSensor THEN
    Stn[1].Clamp.Confirmed := TRUE;
END_IF;

// D — theo mã thiết bị trên bản vẽ
IF B12_Clamp1Up AND NOT B13_Clamp1Dn THEN  M_Stn1_ClampedOk := TRUE;  END_IF;
```

### Ưu và nhược của từng quy ước

| | ⭐ Được gì | ⚠ Mất gì | Hợp với |
|---|---|---|---|
| **A** Địa chỉ trần | Không phải nghĩ; **khớp thẳng bản vẽ đấu dây**; ai cũng tra được | ⚠⚠ Đọc chương trình phải **tra bảng liên tục** · đổi module là mọi ghi chú sai · ⚠ **không dùng được ở hệ chỉ có tag** (Phụ lục A1) | Máy rất nhỏ, làm một lần, một người |
| **B** Tiền tố loại | ⭐ **Đoán được loại tín hiệu ngay khi đọc** · lọc và sắp xếp theo tiền tố · dùng được ở mọi hệ | ⚠ Tiền tố **lặp lại thứ trình biên dịch đã biết** · tên dài · ⚠ khi một tín hiệu chuyển từ dây cứng sang lấy qua mạng thì **tên nói sai** | ⭐ **Mặc định tốt** cho máy vừa, nhóm nhiều người |
| **C** Phân cấp | ⭐⭐ **Khớp với kiểu dữ liệu người dùng và mảng** — thêm trạm thứ ba tốn một dòng (mục 30.3) · trình soạn thảo gợi ý theo cấp | ⚠ Phải **thiết kế cấu trúc trước**, sửa cấu trúc về sau rất đắt · ⚠ **lọc theo tiền tố không còn dùng được** · tên đầy đủ dài khi viết vào hồ sơ | Máy nhiều trạm **giống nhau**; hệ hỗ trợ kiểu người dùng tốt |
| **D** Mã thiết bị | ⭐⭐ **Thợ điện cầm bản vẽ và người đọc chương trình nói cùng một ngôn ngữ** — giá trị lớn nhất lúc 2 giờ sáng | ⚠ Sửa bản vẽ là **phải sửa chương trình** · mã thiết bị **không nói chức năng** nên vẫn phải kèm phần chữ · ⚠ phụ thuộc chất lượng hồ sơ điện | Máy có **hồ sơ điện nghiêm túc**, nhiều người bảo trì luân phiên |

### ⭐ Trong thực tế người ta trộn — và trộn thế nào thì được

⚠ Mục 30.2 mở đầu bằng *"trộn nhiều cách thì luôn sai"*. Nói chính xác hơn: ⭐ **trộn TUỲ HỨNG thì
sai; trộn theo một luật viết ra được thì tốt.**

Hai cách trộn hay gặp và đều dùng được:

```iecst
// B + D — tiền tố loại, rồi mã thiết bị, rồi chức năng
DI_B12Clamp1Up         // ai cũng đọc được, và tra được về bản vẽ

// C + B — phân cấp cho cơ cấu, tiền tố cho tín hiệu vào/ra thô
Stn[1].Clamp.UpSensor  // tầng cơ cấu
DI_Clamp1Up            // tầng gán chân, chỉ xuất hiện ở một chỗ duy nhất
```

> ⭐⭐ **Cách trộn thứ hai đáng học nhất.** Tên theo địa chỉ hoặc theo chân chỉ xuất hiện **ở đúng một
> chỗ** — lớp gán vào/ra ở đầu chương trình. Từ đó trở đi mọi thứ dùng tên phân cấp. ⚡ Khi đổi module
> hay đổi chân, **chỉ một chỗ phải sửa**, và phần còn lại của chương trình không biết gì.
>
> ⭐ Đây không phải sáng kiến riêng của sách: PLCopen nêu nó thành một nguyên tắc — ⭐⭐ *"chỉ làm việc
> bằng tên tượng trưng; địa chỉ tuyệt đối chỉ xuất hiện ở phần khai báo"* — với đúng ba lợi ích:
> **dễ thích nghi khi môi trường đổi · tái dùng được nhiều hơn · ít hiệu ứng phụ** (Chương 27 mục 27.2b).

### Chọn cái nào

| Hoàn cảnh | ⭐ Chọn |
|---|---|
| Máy nhỏ, dưới ~30 tín hiệu, một người làm và bảo trì | **A** hoặc **B** — đừng dựng bộ máy to hơn bài toán |
| Máy vừa, vài người, nhiều cơ cấu **khác nhau** | ⭐ **B** — đây là lý do sách chọn nó |
| Máy nhiều trạm **giống nhau**, sẽ còn nhân bản | ⭐⭐ **C**, cộng **B** ở lớp gán chân |
| Nhà máy có nhiều người bảo trì luân phiên, hồ sơ điện tốt | ⭐ **D**, thường trộn với **B** |
| ⚠ Khách hàng đã có quy ước riêng | ⭐⭐ **Theo họ** — dù bạn thấy nó không đẹp. Xem bên dưới |

> ⭐⭐ **Điều tệ nhất không phải chọn sai quy ước, mà là không chọn.** Ba người viết ba kiểu trong cùng
> một chương trình gây thiệt hại lớn hơn bất kỳ quy ước "xấu" nào được tuân thủ nghiêm túc.
>
> ⚠ Và khi bàn giao cho một nhà máy đã có quy ước riêng, ⭐ **quy ước của họ thắng** — kể cả khi bạn
> thấy nó dở. Người sống với chương trình này mười năm tới là họ, không phải bạn. ⚡ Điều bạn nên đấu
> tranh là **có một quy ước và nó được ghi ra**, không phải quy ước nào.

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

## 30.2b ⭐⭐ Quy ước không chọn MỘT lần cho cả chương trình — chọn cho TỪNG TẦNG

Mục 30.2 bày bốn quy ước cạnh nhau, và cách trình bày đó dễ gây một hiểu nhầm: rằng bạn **chọn một
cái rồi dùng nó cho mọi thứ**.

⚠ Chương trình máy thật **không như vậy**. Đo trên một chương trình máy sản xuất đang chạy, ba tầng
dùng **ba quy ước khác nhau** — và đó là lựa chọn đúng:

| Tầng | Quy ước dùng | Ví dụ có thật | Vì sao chọn cái đó ở tầng này |
|---|---|---|---|
| **1. Gán chân vào/ra** | ⭐ **Địa chỉ trần** (quy ước A) — gói thành mảng theo byte và bit | `InX10[3]` · `OutY24[0]` | ⭐ Đối chiếu **một–một với bản vẽ và với vỏ module**. Ở đúng tầng này, "không có nghĩa" lại là **ưu điểm**: nó không hứa hẹn điều gì |
| **2. Khung dùng lại** | ⭐⭐ **Mảng cấu trúc, đánh chỉ số** (quy ước C) | `Cyl[i].Resp.Done` · `Alarm.Cylinder[12]` | ⭐⭐ **Đây là điều kiện để có thư viện** — xem bên dưới |
| **3. Logic riêng của máy** | ⭐ **Tên mô tả** (quy ước B, thường kèm tiền tố kiểu) | `bLock1` · `x_ChanTram1DaLen` | Chỗ này mỗi máy một khác, nên tên phải **nói được việc** |

### ⭐⭐ Vì sao tầng 2 buộc phải đánh chỉ số

Đây là điểm mấu chốt, và nó giải thích một điều nhìn qua tưởng là cẩu thả.

> ⭐⭐ **Bạn không thể viết `FB_Cylinder` một lần rồi tạo 30 thể hiện, nếu mỗi xy-lanh lại có một cái
> tên viết tay trong logic.**
>
> Muốn một khối chạy được cho **mọi** xy-lanh, nó phải nhận **một chỉ số**. Và khi khối đã nhận chỉ
> số thì báo động, cấu hình, timeout, cờ bỏ qua của nó **cũng phải đánh chỉ số theo**.

⭐ Cái giá trả cho việc đó chính là cái lợi đã đo được ở mục 30.5: **25 trên 27 khối giống hệt nhau ở
bốn cỗ máy khác nhau**. ⚡ Nói cách khác — **thư viện dùng lại và tên riêng cho từng thiết bị là hai
thứ loại trừ nhau ở tầng 2.** Phải chọn.

### ⚠⚠ Nhưng cái giá là có thật, và phải trả nó cho đúng chỗ

| ⚠ Cái giá | Trả bằng cách nào |
|---|---|
| ⚠⚠ **`Alarm.Cylinder[12]` không nói gì với người sửa máy lúc hai giờ sáng** | ⭐ Phải có **bảng tra chỉ số → tên thiết bị**, và bảng đó phải **ở nơi người đó với tới được** |
| ⚠ Tên biến **không còn tự giải thích** | ⭐ Phải đọc kèm **chương trình con cấu hình** (nơi gán chỉ số nào cho cơ cấu nào) — Chương 22 |
| ⚠⚠ Bảng tra thường nằm **ngoài dự án PLC** | ⭐⭐ Nên nó **phải nằm trong danh mục sao lưu** — mất nó thì chương trình còn chạy nhưng **không còn đọc được** (Chương 54 mục 54.3) |

> ⚠⚠ **Hàng cuối là hậu quả nặng nhất, và nó ít ai nghĩ tới.**
>
> Với quy ước B, mất hết tài liệu thì bạn vẫn đọc được chương trình — vì **cái tên chính là tài
> liệu**. ⭐ Với quy ước C đánh chỉ số, mất bảng tra là **mất khả năng đọc**: bạn thấy `[12]` báo lỗi
> và không có cách nào biết `[12]` là cơ cấu nào.
>
> ⚡ Vì vậy: chọn tầng 2 theo chỉ số **thì bảng tra chỉ số trở thành một phần của chương trình**, không
> phải một phụ lục cho đẹp.

### ⭐ Cách KIỂM xem kỷ luật đặt tên có được giữ hay không

Nguyên tắc ở Chương 27 mục 27.2b nói: ⭐ **địa chỉ tuyệt đối chỉ được xuất hiện ở tầng khai báo.** Đó
là một phát biểu **kiểm được** bằng đúng công cụ ở Chương 22 mục 22.3, không phải một lời khuyên chung chung:

> ⭐⭐ **Dùng công cụ tham chiếu chéo *(cross-reference)* trên một tag I/O thô, đếm xem nó xuất hiện ở
> **mấy chương trình con**.**
>
> | Kết quả | Nghĩa là |
> |---|---|
> | ⭐ **Chỉ ở chương trình con gán chân** | Kỷ luật đang được giữ. Đổi module chỉ phải sửa một chỗ |
> | ⚠ Xuất hiện thêm ở vài chỗ khác | **Có rò rỉ** — tìm ra và kéo về tầng gán chân |
> | ⚠⚠ Rải khắp nơi | Tầng gán chân chỉ còn là hình thức |

⭐ Làm thử trên một chương trình máy thật cho con số rất cụ thể: **148 trên 158** lần dùng tag I/O
thô nằm trong đúng chương trình con gán chân — **94 %**. Phần còn lại là **một** chương trình con
trao đổi dữ liệu với hệ trên, đọc thẳng một byte vào/ra.

> ⚡ **Con số 94 % đáng nói ở hai điểm.**
>
> ⭐ Thứ nhất: kỷ luật này **giữ được trong thực tế**, không phải lý tưởng trên giấy.
>
> ⚠ Thứ hai: **rò rỉ luôn có, và nó luôn có lý do nghe hợp lý lúc đó** — ở đây là *"chỗ này chỉ cần
> một byte, gán chân làm gì cho rườm"*. ⭐ Cách xử lý không phải là cấm, mà là **biết nó tồn tại và
> ghi lại ở đâu** — vì đúng chỗ đó sẽ là chỗ **quên sửa** khi đổi module (Chương 53).

> ⭐⭐ **Rút gọn thành một câu để mang đi:** *"chọn quy ước nào"* là câu hỏi sai. Câu đúng là ⭐ **"ở
> tầng này, ai là người đọc, và họ cần cái tên nói gì?"** — ở tầng gán chân người đọc cầm bản vẽ; ở
> tầng khung người đọc là **một khối chạy cho mọi thiết bị cùng loại**; ở tầng logic máy người đọc là
> thợ bảo trì lúc hai giờ sáng.

### ⚠ Và có một kiểu thứ ba: KHÔNG đặt tên biến nào cả

Hai tầng ở trên đều giả định chương trình **có khai báo biến**. ⚠ Nhưng còn một kiểu rất phổ biến —
nhất là ở nền đánh địa chỉ theo thiết bị và ở chương trình đời cũ:

> ⚠⚠ **Không khai báo biến nào. Dùng thẳng `X3`, `Y5`, `M20`, `D13` — và ý nghĩa nằm trong CHÚ THÍCH
> THIẾT BỊ** *(device comment)* gắn với từng địa chỉ.

⭐ Khảo sát **16 chương trình dạy học** trên một nền phổ biến cho kết quả rất nhất quán: ⚠ **gần như
không chương trình nào khai báo biến**, trong khi số **chú thích thiết bị do người viết đặt** chạy
từ 0 tới hơn 200 mỗi chương trình.

| | ⭐ Được gì | ⚠ Mất gì |
|---|---|---|
| **Dùng thẳng địa chỉ + chú thích** | ⭐⭐ **Tham chiếu chéo chạy rất tốt** — địa chỉ là chuỗi có thật trong mã (khác hẳn chỉ số, xem Chương 22 mục 22.3b) · khớp một–một với bản vẽ · không cần thiết kế cấu trúc trước | ⚠⚠ **Chú thích gắn với ĐỊA CHỈ, không gắn với ý nghĩa** — đổi cách đánh địa chỉ thì chú thích ở lại chỗ cũ và **thành sai** · ⚠⚠ **mất tệp chú thích là mất toàn bộ ý nghĩa** · ⚠ không tái dùng khối được (mỗi thiết bị một đoạn mã riêng) |

> ⭐⭐ **Ba kiểu, ba thứ bị mất khi mất tài liệu — và đây là cách phân biệt nhanh nhất:**
>
> | Kiểu | Mất tài liệu thì còn đọc được không |
> |---|---|
> | **Tên mô tả** | ⭐ **Còn** — cái tên **chính là** tài liệu |
> | **Mảng đánh chỉ số** | ⚠ **Mất** bảng tra chỉ số → không biết `[12]` là cơ cấu nào |
> | **Địa chỉ + chú thích** | ⚠⚠ **Mất** tệp chú thích → `M20` không còn nghĩa gì |
>
> ⚡ Hai kiểu sau đều biến **một tệp phụ thành một phần không thể thiếu của chương trình**. ⭐ Hệ quả
> giống nhau: tệp đó **phải nằm trong danh mục sao lưu** (Chương 54 mục 54.3), và ⚠ thiếu nó thì máy
> vẫn chạy — chỉ là không ai sửa được nữa.

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

## 30.3b ⭐ Hai quy ước làm cho cấu trúc ở mục 30.3 **giữ được** khi máy lớn lên

Mục 30.3 nói tổ chức theo cơ cấu và gói trạng thái vào một kiểu dữ liệu. Hai quy ước dưới đây là thứ
quyết định cấu trúc đó còn đứng vững sau ba năm hay tan ra — và cả hai đều gần như không tốn gì.

### Quy ước 1 — chia kiểu dữ liệu làm **ba phần**: Lệnh · Dữ liệu · Phản hồi

Kiểu `ST_Station` ở mục 30.3 trộn lẫn thứ **người khác ghi vào** với thứ **khối tự ghi ra**. Khi chỉ
có sáu trường thì không sao. Khi có sáu mươi trường thì không ai còn trả lời được câu hỏi quan trọng
nhất: ⚠ *"biến này ai được phép ghi?"*

⭐ Cách chữa: tách mỗi cơ cấu thành **ba kiểu**, đặt tên theo cùng một khuôn:

| Phần | Nghĩa | Ai ghi | Ai đọc |
|---|---|---|---|
| `…Cmd` — **Lệnh** | Thứ người ngoài **yêu cầu** cơ cấu làm | ⭐ Trình tự, chế độ tay, nơi ra lệnh | Khối cơ cấu |
| `…Data` — **Dữ liệu** | Tham số và số đo: vị trí, tốc độ, thời gian, ngưỡng | ⭐ Công thức, khối | Cả hai |
| `…Resp` — **Phản hồi** | Thứ cơ cấu **công bố** về chính nó | ⭐ **Chỉ khối cơ cấu** | Mọi người |

```iecst
TYPE ST_CylinderCmd :          // ai cũng ghi được
STRUCT
    Req          : BOOL;       // yêu cầu tới vị trí làm việc
    ManualTrig   : BOOL;       // nút trên màn hình
    InitialReset : BOOL;       // đưa về gốc khi khởi tạo
    InterLock    : BOOL;       // chặn từ tầng chống va chạm (Chương 27 mục 27.3b)
    AlarmShield  : BOOL;       // bỏ qua báo động cơ cấu này (Chương 51 mục 51.7b)
    SensShield   : BOOL;       // bỏ qua cảm biến — có điều kiện, xem Ch.51
END_STRUCT
END_TYPE

TYPE ST_CylinderResp :         // ⚠ CHỈ khối cơ cấu được ghi
STRUCT
    Done         : BOOL;
    AtHome       : BOOL;
    AtWork       : BOOL;
    Fault        : BOOL;
    FaultCode    : INT;
    InitialDone  : BOOL;
    ManualActive : BOOL;       // đang bị điều khiển bằng tay
    Admit        : BOOL;       // ⭐ xem bên dưới
END_STRUCT
END_TYPE
```

> ⭐⭐ **Lợi ích thật không nằm ở chỗ gọn, mà ở chỗ quy tắc trở nên KIỂM TRA ĐƯỢC.**
>
> Với ba phần có tên, câu hỏi *"chỗ nào trong chương trình ghi vào phản hồi của xy-lanh 3?"* trả lời
> được bằng **một lần dùng công cụ tham chiếu chéo** *(cross-reference)*. ⚠ Ra nhiều hơn một chỗ là có lỗi — và bạn tìm
> ra nó **trước** khi máy chạy, thay vì sau (Chương 22, Chương 51 mục 51.7).

### ⭐ Trường `Admit` — cơ cấu tự nói nó có nhận lệnh hay không

Trong `…Resp` nên có một trường mà người mới hay bỏ: **cơ cấu tự công bố nó có sẵn sàng nhận lệnh
không**, và nói riêng cho từng chế độ.

```iecst
// Trong khối cơ cấu — KHÔNG phải trong trình tự
Cyl1.Resp.AutoAdmit   := Cyl1.Resp.InitialDone AND NOT Cyl1.Resp.Fault
                         AND NOT Cyl1.Cmd.InterLock AND M_AutoMode;
Cyl1.Resp.ManualAdmit := Cyl1.Resp.InitialDone AND NOT Cyl1.Cmd.InterLock
                         AND M_ManualMode;
```

Vì sao đáng có:

| | |
|---|---|
| 1 | ⭐ Trình tự chỉ cần hỏi **một bit** thay vì lặp lại đủ điều kiện ở mọi chỗ gọi |
| 2 | ⭐⭐ Nơi ra lệnh **biết trước lệnh sẽ bị từ chối**, nên không gửi đi một lệnh chắc chắn rơi vào hư không — và nói được vì sao (Chương 44) |
| 3 | ⚠ Điều kiện nằm **trong** khối nên **không thể quên** khi thêm một cơ cấu mới |

### Quy ước 2 — chia thư mục chương trình theo **vai trò**, không theo thứ tự viết

Chương trình máy thật có vài chục chương trình con. ⚠ Để chúng phẳng trong một danh sách thì sau sáu
tháng không ai tìm được gì. ⭐ Một bố cục theo vai trò đã được dùng nhiều và đủ tốt để bắt chước:

| Nhóm | Chứa gì | Chương |
|---|---|---|
| **A — Cấu hình hệ thống** | Gán I/O, máy trạng thái toàn máy, cờ bỏ qua, tham số hệ thống | 25, 51 |
| **B — Khởi tạo** | Trình tự về gốc: toàn máy, rồi từng trạm | 28 |
| **C — Thao tác tay** | Điều khiển từng cơ cấu bằng tay, điều khiển chuyền | 28 |
| **D — Báo động** | ⭐ **Mỗi nhóm nguyên nhân một chương trình con**: cơ cấu · trục · hệ thống · chống va chạm · trạm · cảnh báo, và một chỗ gom tất cả | 27, 44 |
| **E — Trình tự trạm** | Mỗi trạm một chương trình con, cộng trình tự chạy khô | 26, 27 |
| **F — Cấu hình trục** | Tham số trục, dữ liệu trục, phần hiện lên màn hình | 37 |

> ⭐⭐ **Nhóm D là nhóm chứng minh giá trị của cách chia này.** Tách báo động theo **nguyên nhân** —
> chứ không rải chúng vào chỗ phát hiện ra lỗi — cho ngay ba thứ:
>
> | | |
> |---|---|
> | 1 | ⭐ Đếm được tổng số báo động của máy, và ⚠ **thấy ngay cái nào chưa có** |
> | 2 | ⭐ Mỗi nhóm gom được thành **một bit tổng** để đèn tháp và màn hình dùng (Phụ lục L.11, L.13) |
> | 3 | ⭐⭐ Lỗi **chống va chạm** tách khỏi lỗi **cơ cấu** — hai nhóm gọi hai người khác nhau tới máy (Chương 27 mục 27.3b) |
>
> ⚡ Và nhóm E tách **trình tự chạy khô** *(dry run)* thành một chương trình con riêng thay vì rải
> `IF M_DryRun` khắp trình tự thật — nhờ vậy trình tự thật đọc được, còn chế độ chạy khô không âm thầm
> phân nhánh ở mười chỗ (Chương 28, Chương 50).

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

### ⭐⭐ Hãng cho bạn cơ chế gì để làm được kiểu thứ hai

Bảng trên nói *nên* dùng "thư viện có phiên bản". ⚠ Nhưng bạn **không tự dựng cơ chế đó được** — nó
phải do phần mềm lập trình hỗ trợ. Và ⭐ **hai hãng lớn giải bài toán này theo hai hướng ngược nhau**,
nên câu *"dùng thư viện có phiên bản"* có nghĩa rất khác nhau tuỳ hệ bạn đang dùng.

| | Hướng **CHÉP có kiểm soát** | Hướng **THAM CHIẾU tới kiểu** |
|---|---|---|
| Ví dụ thật | ⭐ **Rockwell — Add-On Instruction (AOI)** | ⭐ **Siemens TIA Portal — "type" trong thư viện** |
| Khối sống ở đâu | ⭐ **Trong chính dự án**; đưa sang dự án khác bằng chép/dán hoặc nhập từ tệp | Trong **thư viện**; dự án chỉ dùng, không sở hữu |
| Cập nhật khi sửa khối gốc | ⚠ **Từng dự án một** — nhập bản sửa đổi mới vào từng dự án | ⭐⭐ **Cập nhật tập trung mọi chỗ dùng** trong dự án, một lệnh |
| Nhiều phiên bản cùng lúc | ⭐ Được — mỗi dự án giữ bản của nó | ⚠⚠ **Chỉ MỘT phiên bản của một kiểu trong cùng một bộ điều khiển** |
| Chống sửa lén | ⭐ **Chữ ký khối** — ký xong thì khối **bị niêm**, không sửa được nữa | ⭐ Hệ **không cho sửa tại chỗ dùng**; hệ tự giữ nhất quán |
| ⚠⚠ Cái giá | Niêm rồi thì **kể cả chú thích cũng không sửa được** cho tới khi gỡ chữ ký | ⚠⚠ **Xoá một kiểu là xoá luôn MỌI chỗ đang dùng nó** trong chương trình |

> ⭐⭐ **Đọc bảng này xong thì bảng "ba kiểu dùng lại" ở trên có nghĩa cụ thể hơn hẳn.** ⚡ Cơ chế của
> Rockwell **là kiểu "chép"** — nhưng là chép **có kiểm soát**: có bản sửa đổi, có chữ ký, có lịch sử.
> Cơ chế của Siemens **là kiểu "thư viện có phiên bản"** theo đúng nghĩa đen.
>
> ⭐ Nghĩa là ⚠ **"chép" không tự động xấu** — cái xấu là chép mà **không biết mình đã chép bản nào**.

**Hai chi tiết đáng nhớ, vì cả hai đều bất ngờ với người quen hệ kia:**

> ⚠⚠ **Chữ ký khối của Rockwell NIÊM cả tài liệu.** ⭐ Sau khi sinh chữ ký, khối không sửa được —
> và "không sửa được" gồm cả **chú thích nấc thang và mô tả biến**. Muốn sửa một dấu phẩy trong chú
> thích cũng phải **gỡ chữ ký ra rồi ký lại**.
>
> ⭐ Đổi lại, chữ ký cho bạn một thứ rất giá trị: ⚡ **bằng chứng rằng khối này chưa bị ai đụng vào**.
> Đó là lý do nó **bắt buộc** khi khối tham gia chức năng an toàn mức SIL 3, và hay bị yêu cầu ở các
> ngành có quản lý chặt (Chương 47).
>
> ⚠ Nhưng có một lỗ hổng phải biết: ⭐ **chữ ký KHÔNG khoá các khối và kiểu dữ liệu mà nó tham
> chiếu**. Khối của bạn niêm rồi, mà cái nó gọi bên trong thì vẫn sửa được.

> ⚠⚠ **Xoá một "type" của Siemens là xoá mọi chỗ dùng nó.** ⭐ Đây là mặt trái trực tiếp của ưu điểm
> "hệ tự giữ nhất quán": hệ **không cho phép tồn tại chỗ dùng mồ côi**, nên nó xoá luôn.
>
> ⚡ Và ràng buộc **một bộ điều khiển chỉ chứa một phiên bản của mỗi kiểu** nghĩa là: ⚠ nâng cấp khối
> xy-lanh lên V2 thì **cả máy dùng V2**, không có chuyện "trạm này V1, trạm kia V2". ⭐ Nghe như hạn
> chế, nhưng nó chính là thứ **chặn đứng** kiểu thứ ba trong bảng trên.

### ⭐ Hệ của bạn thuộc hướng nào — bốn câu hỏi để tự tra

⚠ Đừng suy từ hai cột trên. Mỗi hệ một khác, và ⭐ **cùng một hãng cũng đổi giữa các đời phần mềm**.
Mở tài liệu hệ bạn dùng rồi trả lời bốn câu này — trả lời xong là biết mình đang ở hướng nào:

| # | Câu hỏi | ⭐ Vì sao nó quyết định |
|---|:--|:--|
| 1 | Sửa khối trong thư viện thì các dự án đang dùng **tự đổi theo**, hay phải **nhập lại từng cái**? | Phân biệt tham chiếu với chép |
| 2 | Hệ có ghi **số phiên bản** của khối, và có cho **xem dự án nào dùng bản nào** không? | ⚠ Không có cái này thì "thư viện có phiên bản" chỉ là tên gọi |
| 3 | Có cách **khoá khối** để người khác không sửa lén không? Khoá rồi thì **còn sửa được gì**? | Quyết định khối có dùng được cho phần an toàn không |
| 4 | ⚠⚠ **Xoá hoặc đổi tên khối trong thư viện thì chuyện gì xảy ra** với chỗ đang dùng? | ⭐ Đây là câu nguy hiểm nhất, và là câu ít người thử nhất |

> ⭐⭐ **Câu 4 phải thử thật, trên một dự án bỏ đi.** ⚡ Không tài liệu nào mô tả đủ rõ chuyện này, và
> ⚠ đây là loại chuyện mà **biết vào lúc đang sửa máy chạy sản xuất là quá muộn**.

### Ba yêu cầu với một khối đáng đưa vào thư viện

| # | Yêu cầu | Vì sao |
|---|---|---|
| 1 | **Giao diện rõ ràng, ít chân, ổn định** | Chân vào/ra là hợp đồng — thêm chân là thay đổi phá vỡ |
| 2 | **Không phụ thuộc biến toàn cục** | Khối đọc lén một biến ngoài thì không tái dùng được ở dự án khác |
| 3 | **Có ghi rõ giả định** | ⭐ "khối này giả định cơ cấu về vị trí lò xo khi mất lệnh" — viết ngay đầu khối |

### ⭐⭐ Mức 3 trông như thế nào trong thực tế

Mức 3 ở bảng mục 30.3 — *tái sử dụng ở quy mô cả máy* — nghe trừu tượng. Đây là hình dạng thật của
nó, đo trên **hai cỗ máy khác nhau do cùng một nhóm kỹ thuật viết**:

| Hạng mục | Hai máy đó |
|---|---|
| Bố cục thư mục | ⭐ **Giống hệt** — sáu nhóm ở mục 30.3b |
| Thư viện khối cơ cấu | ⭐ **Giống hệt** — cùng một bộ khối cho xy-lanh, trục, chân không, đầu ép, khay, kho đệm, đếm chu kỳ, đếm tuổi thọ vật tư, thống kê năng suất |
| Bộ kiểu dữ liệu | ⭐ Giống hệt |
| Khối giao diện với màn hình | ⭐⭐ **Khoảng hai phần ba trùng nhau từng tên biến** |
| ⚠ **Phần khác nhau** | Gần như **chỉ có thư mục trình tự trạm**, cộng vài tín hiệu bắt tay riêng giữa các trạm của máy đó |

> ⭐⭐ **Đó là câu trả lời cụ thể cho câu hỏi "tái sử dụng ở mức máy nghĩa là gì".** Không phải chép cả
> chương trình rồi sửa. Mà là: ⭐ **mọi thứ KHÔNG đặc thù cho cỗ máy này đều nằm ngoài phần đặc thù**
> — và phần đặc thù thu lại thành **một thư mục**.
>
> ⚡ Khi đạt tới hình dạng này, câu *"làm máy mới mất bao lâu"* đổi nghĩa: nó không còn là *"viết lại
> chương trình"* mà là *"viết trình tự cho mấy trạm"*. ⚠ Nhưng nó cũng đặt ra một kỷ luật mới —
> **sửa một khối dùng chung là chạm vào mọi cỗ máy đang dùng nó**, nên bắt buộc phải có phiên bản
> (mục 30.6) và phải biết máy nào đang dùng phiên bản nào.

> ⭐ **Bắt đầu từ đâu.** Phụ lục L gom sẵn những mẫu lặp lại ở gần như mọi máy — tự giữ, chuỗi
> cho phép, ba lệnh dừng, khung trình tự có timeout, khối cơ cấu hai vị trí dùng lại được.
> ⚠ Mỗi mẫu ở đó **ghi kèm giả định của nó** đúng theo yêu cầu số 3 trong bảng trên — đọc phần
> giả định trước khi chép, vì đó mới là chỗ dùng lại sai.

---

### ⚠⚠ Thời điểm viết tài liệu — thứ quyết định chất lượng của nó

Comment tốt viết lúc nào? Cùng lúc viết code. ⭐ **Nguyên tắc đó đúng cho cả hồ sơ dự án**, và đây là
lý do:

> ⚠⚠ **Tài liệu để dồn tới cuối dự án thì KHÔNG BAO GIỜ tốt được — không phải vì lười, mà vì đến lúc
> đó chi tiết đã quên mất rồi.**
>
> Người viết phải **nhớ lại**, nên vừa mất nhiều thời gian hơn, vừa ra một bản luôn thiếu. ⚠ Và thứ
> bị quên trước nhất luôn là ⭐ **lý do** — *vì sao chọn cách này thay vì cách kia* — đúng thứ người
> đọc sau cần nhất (mục 30.4).

| Thời điểm | Ghi cái gì |
|---|---|
| Trước khi viết | Bảng I/O · đặc tả trình tự (Chương 23) |
| ⭐ **Trong khi viết** | ⭐ **Lý do của mọi quyết định lạ** · con số lấy từ đâu · cái đã thử mà không được |
| Khi chạy thử | Giá trị đo thật thay cho giá trị giả định (Chương 52) |
| ⚠ Sau khi xong | ⭐ **Chỉ còn dọn dẹp và đóng gói** — không phải lúc bắt đầu viết |

> ⭐ **Hệ quả tổ chức:** hồ sơ nên ở dạng **biểu mẫu để sẵn** (Phụ lục C) chứ không phải một bản báo
> cáo viết một lần. Biểu mẫu đặt tại chỗ mọi người lấy được và **cập nhật được khi máy thay đổi** —
> tài liệu chỉ sống nếu người bảo trì sửa được nó (Chương 53).

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

### ⭐⭐ Làm cho nó so sánh được — xuất ra văn bản

Bảng trên cho thấy phần lớn thành phần **không** so sánh được bằng công cụ. ⚠ Nhưng đó là nhận định
về **định dạng tệp gốc của hãng**, không phải về giới hạn không vượt qua được.

⭐ **Cách vượt qua: xuất chương trình ra một định dạng văn bản, rồi so sánh và lưu bản văn bản đó.**

| Cách xuất | Có ở đâu | ⭐ Được gì | ⚠ Mất gì |
|---|---|---|---|
| **Xuất văn bản ASCII của hãng** | Hầu hết hệ đều có, dưới tên *import/export* | ⭐ Luôn sẵn, không cần công cụ ngoài | ⚠ Định dạng **riêng của hãng** — đổi hãng thì vô dụng |
| ⭐⭐ **Xuất PLCopen XML** | Nhiều hệ hỗ trợ, mức độ khác nhau | ⭐ Định dạng **mở**, chở được cả phần đồ hoạ; ⭐⭐ đúng thứ hệ quản lý phiên bản cần (Chương 14 mục 14.6b) | ⚠ **Không phải hệ nào cũng có**, và mức hỗ trợ khác nhau |
| **Chụp báo cáo / in ra PDF** | Mọi hệ | Xem được bằng mắt | ⚠⚠ **Không so sánh tự động được** — chỉ là ảnh chụp |

> ⭐⭐ **Xuất ra văn bản đổi hẳn chất của việc quản lý phiên bản.** Khi bản lưu là văn bản, bạn có
> đúng ba thứ mà tệp nhị phân của hãng không cho:
>
> | | |
> |---|---|
> | 1 | ⭐ **Xem được đã đổi chính xác dòng nào** — không phải "có khác nhau" chung chung |
> | 2 | ⭐ Tìm được **khi nào** một dòng xuất hiện, và **ai** thêm nó |
> | 3 | ⭐⭐ Đọc được bản cũ **mà không cần cài đúng phiên bản phần mềm của hãng** — thứ sẽ rất quý sau năm năm |

> ⚠⚠ **Nhưng bản xuất KHÔNG thay được bản sao lưu gốc.**
>
> Bản văn bản chở logic; nó ⚠ **không chở đủ cấu hình phần cứng, tham số thiết bị, và mọi thứ ở bảng
> trên đang để dấu ❌**. ⭐ Quy tắc: **lưu CẢ HAI** — tệp gốc của hãng để khôi phục máy, bản xuất văn
> bản để đọc và so sánh (Chương 54).
>
> ⚡ Và nhớ kiểm chứng: ⚠ **tệp xuất hợp lệ không có nghĩa là nhập lại được** — chính đặc tả PLCopen
> XML nói nội dung xuất ra *"không có kiểm chứng về tính nhất quán hay tính đúng đắn"*. ⭐ Cách duy
> nhất để biết là **thử nhập lại một lần**, đúng tinh thần *"bản sao lưu chưa thử khôi phục thì chưa
> phải bản sao lưu"* (Chương 52, Chương 54).

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
| ⚠⚠ Viết tài liệu lúc nào | ⭐ **Trong khi làm**, không dồn tới cuối | Đến cuối thì chi tiết đã quên, và **lý do** quên trước nhất |
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
11. ⚠⚠ Vì sao tài liệu dồn tới cuối dự án *"không bao giờ tốt được"* — và lý do đó **không phải** là
    lười? ⭐ Thứ gì bị quên trước nhất, và vì sao đúng thứ đó lại quan trọng nhất?

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
- **Rockwell Automation** — *Logix 5000 Controllers Add-On Instructions* (1756-PM010, bản 9/2025):
  ⭐ **chữ ký khối** *(instruction signature)* sinh mã định danh duy nhất và **niêm** khối — không sửa
  được nữa, ⚠ **kể cả chú thích nấc thang và mô tả biến**, cho tới khi gỡ chữ ký; ⭐ **bắt buộc** khi
  khối tham gia chức năng an toàn mức SIL 3; ⚠ nhưng **không khoá** các khối và kiểu dữ liệu mà nó
  tham chiếu. Và cách phân phối: **chép/dán giữa các dự án**, hoặc *nhập bản sửa đổi mới* — nền cho
  cột "chép có kiểm soát" ở mục 30.5.
- **Siemens** — *Programming Guideline for S7-1200/S7-1500*, ch. 3.7 *Libraries* (§3.7.2 *Type
  concept*, §3.7.4 *Versioning of a block*): phân biệt **master copy** với ⭐ **type**; type **có
  phiên bản** và **cập nhật tập trung mọi chỗ dùng**; ⚠⚠ **chỉ một phiên bản của một type trong cùng
  một bộ điều khiển**, và ⚠⚠ **xoá type thì mọi chỗ dùng bị xoá theo** — nền cho cột "tham chiếu tới
  kiểu" ở mục 30.5.
- **Hugh Jack** — *Automating Manufacturing Systems with PLCs*, §32.5 *Documentation*: ⭐ tài liệu
  phải **phát triển cùng dự án**, để tới cuối thì chi tiết đã quên nên vừa lâu hơn vừa thiếu; và cách
  dùng **biểu mẫu để sẵn**, đặt nơi mọi người truy cập và cập nhật được khi máy thay đổi.

> ⚡ Quy ước đặt tên ở mục 30.2 là **quy ước của cuốn sách này**, không phải chuẩn ngành. Dự án của bạn
> có thể dùng quy ước khác — điều bắt buộc là **có một quy ước, viết ra thành văn, và dùng nhất quán**.
