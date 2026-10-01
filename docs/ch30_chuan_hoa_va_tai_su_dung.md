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
M_    biến nội bộ         X_    tín hiệu đã qua tầng ánh xạ vào (Chương 27 mục 27.3c, Chương 50)
T_    thể hiện timer      C_    thể hiện counter
S_    bit trạng thái      FB_   kiểu khối chức năng
```

Ví dụ từ DP-01:

| Tag | Đọc ra là | |
|---|---|---|
| `DI_BoardStn1` | ngõ vào số · board · trạm 1 | |
| `DO_Clamp1Vlv` | ngõ ra số · van kẹp · trạm 1 | |
| `M_Stn1_ClampReq` | biến nội · trạm 1 · yêu cầu kẹp | ⭐ yêu cầu, không phải lệnh ra van (Chương 27) |
| `Stn2.Ready` | giao diện công bố của trạm 2 — một trường của `Stn2 : ST_Station` | không có tiền tố `M_` vì nó là giao diện, không phải biến nội (mục 30.3) |
| `Stn1_Step` | bước của trình tự trạm 1 — **ruột** của trạm | ⭐ biến của chương trình trạm, không ai khác đọc; tiền tố `Stn1_` chỉ để đoạn trích đứng một mình vẫn biết của trạm nào (Phụ lục N mục N.7) |

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
VAR_GLOBAL
    M_Stn1_Ready     : BOOL;
    M_Stn1_Busy      : BOOL;
    M_Stn1_Fault     : BOOL;
    M_Stn1_FaultStep : INT;
END_VAR

// ✓ Gói lại — một kiểu, dùng cho mọi trạm (Chương 11 mục 11.5)
TYPE ST_Station :                      // giao diện CÔNG BỐ của một trạm — chỉ trạm đó ghi
STRUCT
    Ready       : BOOL;                // sẵn sàng nhận board mới
    Busy        : BOOL;                // đang xử lý
    Fault       : BOOL;                // trạm có lỗi — cờ đã chốt (Chương 25 mục 25.5c)
    FaultStep   : INT;                 // bước lúc lỗi, 0 nếu không lỗi
    BoardDone   : BOOL;                // board đã xong, chờ chuyển đi
    DoneCount   : DINT;                // ⭐ DINT, không phải INT — sẽ tràn
    LastCycleMs : DINT;                // ⭐ đơn vị trong tên
END_STRUCT
END_TYPE

VAR_GLOBAL
    Stn1 : ST_Station;                 // ⭐ CHỈ trạm 1 ghi vào Stn1 — mọi nơi khác chỉ đọc
    Stn2 : ST_Station;
END_VAR
```

Ba lợi ích, và lợi ích thứ ba là lớn nhất:

1. Thêm trạm thứ ba chỉ cần thêm **một dòng khai báo**.
2. Thêm một trường cho mọi trạm chỉ cần sửa **một chỗ**.
3. ⭐ **Không thể quên** — khi bạn tạo `Stn3`, nó tự động có đủ mọi trường. Với biến rời rạc, bạn sẽ
   quên ít nhất một cái.

#### ⭐⭐ Gói những gì — ba cách, và vì sao `Step` ở ngoài

Câu hỏi thật không phải *"gói hay không"*, mà là **gói những gì**. Cùng bài toán — trạm 1 chờ trạm 2
trống rồi nhả board — viết theo ba cách:

```iecst
// ✗ A · Gói TẤT CẢ, kể cả bước — Stn2.Step là biến toàn cục
IF Stn1.BoardDone AND Stn2.Step = 0 THEN  M_Stn1_ReleaseBoard := TRUE;  END_IF;

// B · Để rời tất cả
IF Stn1_BoardDone AND Stn2_Ready THEN  M_Stn1_ReleaseBoard := TRUE;  END_IF;

// C · Gói phần CÔNG BỐ, để bước là ruột — cách của sách
IF Stn1.BoardDone AND Stn2.Ready THEN  M_Stn1_ReleaseBoard := TRUE;  END_IF;
```

| Cách | ⭐ Ưu | ⚠ Nhược |
|---|---|---|
| A — gói tất cả | Một biến chứa mọi thứ về trạm | ⚠⚠ Bước thành toàn cục: đọc `Stn2.Step` ở trạm 1 dễ như đọc `Stn2.Ready` — đúng lỗi *"nhìn vào ruột"* của Chương 27 mục 27.4, và **không có gì ngăn** |
| B — để rời | Chạy trên mọi hệ, kể cả hệ chưa có kiểu cấu trúc | Mọi nhược của mục này: chép tay, quên trường, không truyền được cả cụm; và ⚠ không nhìn tên mà biết biến nào được phép đọc |
| ⭐ C — gói phần công bố | ⭐ **Dấu chấm = hợp đồng**: thứ gì đọc được qua `Stn2.` là thứ trạm 2 hứa giữ nghĩa; bước nằm trong chương trình trạm nên người khác **không với tới** một cách vô tình | Hai kiểu tên cho hai loại biến — phải giải thích một lần, như ở đây |

⭐ **Khuyến nghị: C** — cho DP-01 và cho mọi máy có từ hai trạm. Dùng **B** chỉ khi hệ của bạn không có
kiểu cấu trúc. ⚠ Tránh **A**: nó trông gọn nhất, nhưng biến ranh giới giữa các trạm thành một lời hứa
miệng.

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

## 30.5b ⭐⭐ Viết khối của mình theo cùng "hợp đồng" với khối của hãng

Bạn sẽ gặp khối chuyển động (Chương 37) và khối truyền thông (Chương 38) ở vai **người dùng**: kích
`Execute`, chờ `Done`, xem `Error`. Mục này là phía **người viết**. ⭐ Khối bạn tự viết nên theo đúng
hợp đồng đó — vì người dùng khối của bạn, kể cả bạn sau sáu tháng, đã quen hợp đồng đó từ khối của hãng.

### Hai hợp đồng — và một loại khối không thuộc hợp đồng nào

PLCopen chia khối có hành vi kéo dài thành **hai loại**, mỗi loại một cặp chân:

| Loại | Cặp chân | Chạy khi nào | Ví dụ |
|---|---|---|---|
| ⭐ **Kích bằng sườn** | `Execute` ↔ `Done` (kèm `Busy`, `Error`, `ErrorID`) | **Một việc**: từ sườn lên của `Execute` tới khi xong hoặc lỗi | Chuyển một board sang trạm sau (ngay dưới) · một lệnh di chuyển (Chương 37) · đọc một thanh ghi qua mạng (Chương 38) |
| ⭐ **Điều khiển theo mức** | `Enable` ↔ `Valid` | **Liên tục, chừng nào** `Enable` còn bật; `Enable` tắt thì khối **ngừng và xoá ngõ ra** | Cấp nguồn cho một trục (Chương 37) · đọc trạng thái thiết bị theo chu kỳ |
| Khối thiết bị, lệnh theo mức | `Req` + `Permit` ↔ `Done` + `Fault` | **Luôn chạy**, gọi mỗi vòng, bám theo lệnh | `FB_Cylinder2Pos` (Chương 27 mục 27.3) |

⭐ **Chọn loại nào:**

- Việc **có điểm kết thúc** — chuyển xong một board, đi tới một vị trí — thì kích bằng sườn.
- Hoạt động **kéo dài, không có điểm kết thúc** — giữ nguồn, đọc liên tục — thì điều khiển theo mức.
- ⚡ Và một lý do kỹ thuật tài liệu PLCopen nêu thẳng: **phát hiện sườn cần hai vòng quét**. Khối phải
  nhận một giá trị mới **ở mỗi vòng** thì không thể dùng mô hình sườn — phải dùng mô hình mức.
- Khối điều khiển **một thiết bị** bám theo lệnh — như xy-lanh — không cần khớp hai hợp đồng trên; nó
  là loại thứ ba, và ⚠ **đừng mượn tên chân của hai loại kia** cho nó.

> ⚠⚠ **Dùng tên chân của hợp đồng thì phải theo đúng nghĩa của hợp đồng.** `Enable` là tên dành cho
> mô hình mức — tắt là **xoá ngõ ra**. Chân cho phép của khối xy-lanh mà đặt tên `Enable`, người quen
> PLCopen sẽ hiểu *"tắt Enable là tắt van"* — đúng lỗi ở Chương 27 Bẫy 7. Vì vậy sách đặt tên nó là
> `Permit`.

### ⭐⭐ Năm quy tắc của hợp đồng `Execute` / `Done`

Quy tắc chung cho khối của PLCopen (Phụ lục 4 của tài liệu *Creating PLCopen Compliant Libraries*) và
tài liệu thư viện khối chuyển động của **hai hãng** nói giống nhau ở bốn điểm đầu — ⚠ còn điểm thứ năm
thì **chính PLCopen có hai câu trả lời**:

| # | Quy tắc | Vi phạm thì người gọi gặp gì |
|:-:|---|---|
| 1 | Tham số được **chốt ở sườn lên** của `Execute`; đổi tham số giữa chừng **không** ảnh hưởng việc đang chạy | Đổi giới hạn thời gian giữa chừng và khối *tự* đổi hành vi |
| 2 | `Busy` bật **ngay ở sườn lên** và giữ tới khi xong hoặc lỗi; trong lúc `Busy`, khối phải được **gọi mỗi vòng** | Khối không được gọi thì **đứng yên** — không xong, không lỗi (Chương 14 mục 14.3) |
| 3 | `Busy`, `Done`, `Error` — và `Aborted` nếu khối có chân huỷ — **loại trừ nhau**; khi `Execute` đang TRUE thì luôn có **đúng một** cái bật | Thấy vừa `Done` vừa `Error`, không biết tin cái nào |
| 4 | ⭐ `Done`/`Error` **xoá ở sườn xuống** của `Execute`; nếu `Execute` tắt **giữa chừng**, kết quả vẫn **hiện ít nhất một vòng quét** lúc xong | Người gọi dùng `Execute` dạng xung **không bao giờ thấy** `Done` |
| 5 | ⚠ Kích lại khi **đang `Busy`** | ⚠ **Không thống nhất — ngay trong PLCopen**: quy tắc chung của khối chuyển động ghi lệnh trước **mất phản hồi** (lệnh mới thay nó); còn khối mẫu `ETrig` PLCopen đưa cho người viết thư viện thì **không nhìn** `Execute` khi đang bận — tức **bỏ qua**. Tài liệu hãng cũng chia hai phe như vậy. ⭐ Khối của bạn theo `ETrig`: **bỏ qua**; còn người gọi thì **đừng làm** — chờ `Busy` tắt |

```text
  Execute giữ mức tới khi xong          Execute chỉ là một xung
  Execute ▁▁████████████▁▁▁▁            Execute ▁▁█▁▁▁▁▁▁▁▁▁▁▁▁▁
  Busy    ▁▁██████▁▁▁▁▁▁▁▁▁▁            Busy    ▁▁██████▁▁▁▁▁▁▁▁
  Done    ▁▁▁▁▁▁▁▁██████▁▁▁▁            Done    ▁▁▁▁▁▁▁▁█▁▁▁▁▁▁▁   ← đúng MỘT vòng quét
```

> ⚡ **Hai chi tiết của khối mẫu PLCopen đáng chép theo.** Việc xong **ngay trong lần gọi đầu** thì `Busy`
> **không bao giờ** được thấy — người gọi đừng chờ thấy `Busy` mới coi là khối đã nhận lệnh. Và mã lỗi
> `0` = không lỗi, `1` = quá thời gian là hai mã PLCopen **dành sẵn** cho mọi thư viện: mỗi thư viện có
> miền mã riêng, mã của thư viện con phải **dịch** sang miền của mình chứ không đẩy thẳng ra — khối dưới
> dùng đúng hai mã đó (tài liệu thư viện, mục 3.4 và 3.5).

### Một khối viết theo đúng năm quy tắc

Bài toán: đưa board từ trạm 1 sang trạm 2 — bước 60 ở Chương 26. Xin chuyền chạy, chờ tới nơi, và
không được chờ mãi.

```iecst
// ✔ VÍ DỤ HOÀN CHỈNH — khối kích bằng sườn theo hợp đồng Execute/Done (giống hệt Phụ lục L mục L.8b)
FUNCTION_BLOCK FB_BoardTransfer
VAR_INPUT
    Execute   : BOOL;            // ⭐ SƯỜN LÊN = bắt đầu · tham số được CHỐT tại sườn này
    Arrived   : BOOL;            // "đã tới nơi" — board tới chặn, hoặc đã rời trạm, tuỳ chỗ gọi
    TimeOut   : TIME := T#10S;   // thời gian tối đa cho một lần chuyển
END_VAR
VAR_OUTPUT
    Busy      : BOOL;            // ⭐ Busy · Done · Error LOẠI TRỪ nhau
    Done      : BOOL;
    Error     : BOOL;
    ErrorID   : INT;             // 0 = không lỗi · 1 = quá thời gian
    ConvReq   : BOOL;            // xin tầng máy chạy chuyền — chuyền là tài nguyên chung (Chương 27)
END_VAR
VAR
    ExecEdge  : R_TRIG;
    T_Out     : TON;
    LimitCopy : TIME;            // bản CHỐT của TimeOut
END_VAR
VAR_TEMP
    Start     : BOOL;            // vòng này vừa NHẬN một lệnh mới
    NewResult : BOOL;            // kết quả vừa có trong vòng này
END_VAR

ExecEdge(CLK := Execute);

// ── 1. Sườn lên khi đang rỗi → nhận lệnh, CHỐT tham số. Sườn lên khi đang bận → bỏ qua ──
Start := ExecEdge.Q AND NOT Busy;
IF Start THEN
    Busy      := TRUE;
    Done      := FALSE;
    Error     := FALSE;
    ErrorID   := 0;
    LimitCopy := TimeOut;
END_IF;

// ── 2. Đang bận: chờ tới nơi, giám sát thời gian. T_Out gọi đúng MỘT lần, về 0 ở vòng nhận lệnh ──
T_Out(IN := Busy AND NOT Start, PT := LimitCopy);
IF Busy AND Arrived THEN
    Busy      := FALSE;
    Done      := TRUE;
    NewResult := TRUE;
ELSIF Busy AND T_Out.Q THEN
    Busy      := FALSE;
    Error     := TRUE;
    ErrorID   := 1;
    NewResult := TRUE;
END_IF;
ConvReq := Busy;                 // ngõ ra suy ra SAU khi trạng thái đã cập nhật

// ── 3. Execute đã tắt và việc đã xong → xoá kết quả. Kết quả VỪA có thì vẫn hiện
//       ít nhất MỘT vòng, kể cả khi Execute đã tắt từ giữa chừng ──
IF NOT Execute AND NOT Busy AND NOT NewResult THEN
    Done    := FALSE;
    Error   := FALSE;
    ErrorID := 0;
END_IF;
END_FUNCTION_BLOCK
```

| Quy tắc | Dòng nào lo |
|---|---|
| 1 — chốt tham số | `LimitCopy := TimeOut;` chỉ chạy ở vòng **nhận lệnh** |
| 2 — `Busy` ngay ở sườn lên | Phần 1; và khối được gọi **mỗi vòng** bởi bên gọi, ngoài `CASE` |
| 3 — loại trừ nhau | Mỗi nhánh bật một cờ thì **tắt** hai cờ kia |
| 4 — kết quả hiện ít nhất một vòng | `NewResult` là biến `VAR_TEMP` — tính lại **mỗi lần gọi**, nên nó chỉ đúng trong chính vòng có kết quả |
| 5 — kích lại khi bận | `Start := ExecEdge.Q AND NOT Busy` — sườn lên lúc bận bị bỏ qua |

> ⚡ **Hai chi tiết mô phỏng tìm ra khi soạn khối này.** Bản nháp đầu đặt `ConvReq := Busy` **trước**
> phép kiểm tới nơi — nên ở đúng vòng board tới nơi, khối vừa báo `Done` vừa **còn xin chạy chuyền**.
> Và nếu đồng hồ không được đưa về 0 ở vòng nhận lệnh (`AND NOT Start`), một lệnh nhận **ngay vòng
> sau** khi lệnh trước vừa xong sẽ **thừa hưởng thời gian đã đếm** — rồi báo quá giờ sớm. ⭐ Cả hai
> đều không lộ ra khi đọc mã; chúng lộ ra khi chạy thử từng vòng quét (Chương 50).

### Bên gọi dùng nó thế nào

```iecst
VAR
    Xfer1 : FB_BoardTransfer;
END_VAR

// Gọi MỖI vòng quét, ngoài CASE — Execute lấy thẳng từ bước: vào bước là sườn lên, rời bước là sườn xuống
Xfer1(Execute := (Stn1_Step = 60),
      Arrived := NOT DI_BoardStn1,          // ở bước 60, "tới nơi" nghĩa là board đã RỜI trạm 1
      TimeOut := T#10S);
M_Stn1_ConvReq := Xfer1.ConvReq;            // đúng MỘT chỗ ghi yêu cầu chuyền của trạm 1

CASE Stn1_Step OF
    …
    60: // Hạ chặn, chuyển board sang — khối lo phần "chờ và giám sát"
        M_Stn1_StopReq := FALSE;
        IF Xfer1.Done THEN
            Stn1.BoardDone := FALSE;
            Stn1_Step      := 0;
        ELSIF Xfer1.Error THEN
            Stn1.Fault := TRUE;             // khối BÁO — trạm chốt cờ của nó (Chương 25 mục 25.5c)
        END_IF;
END_CASE;
```

> ⭐ So với bước 60 viết thẳng ở Chương 26: yêu cầu chuyền nay có **một** chỗ ghi thay vì hai, và giới
> hạn thời gian nằm **trong** khối — đặt giới hạn của bước 60 trong bộ đếm dùng chung về `T#0S` để
> khỏi giám sát hai lần. ⚡ Khối này đứng sẵn trong **Phụ lục L mục L.8b** để chép.

---

## 30.5c ⭐⭐ Hướng đối tượng — thêm một cách tổ chức, không thay cách cũ

Bản 3 của IEC 61131-3 (2013) đưa lập trình **hướng đối tượng** *(object-oriented programming, OOP)*
vào chuẩn; bản 4 (2025) thêm **thuộc tính** (Chương 14 mục 14.1). ⭐ Chính PLCopen nói rõ: cách lập
trình cổ điển **không bị thay thế** — hai cách cùng tồn tại, và mỗi cách dùng ở chỗ nó hợp nhất.

> ⚠⚠ **Đọc bảng hãng ở cuối mục TRƯỚC khi đọc cú pháp.** Hướng đối tượng chạy được trên CODESYS và
> các nền dựng trên nó. Trong TIA Portal, trên Rockwell Logix và trên dòng FX5 của Mitsubishi thì
> **không** — mục này vô ích với bạn nếu máy của bạn chạy trên các hệ đó. Cú pháp dưới đây theo
> CODESYS, viết liền thành văn bản để đọc được trên giấy.

### Năm công cụ — mỗi cái trả lời một câu hỏi

| Công cụ | Là gì | ⭐ Trả lời câu hỏi |
|---|---|---|
| `METHOD` | Một đoạn mã **thuộc về** một khối, gọi được từ ngoài: `Stn2.IsEmpty()` | *"Hỏi khối này một câu, hoặc ra một lệnh, mà không cần biết bên trong nó"* |
| `PROPERTY` | Một giá trị đọc/ghi được như biến, nhưng đi qua mã kiểm soát | *"Cho đọc giá trị này, nhưng qua một cửa có kiểm tra"* |
| ⭐ `INTERFACE` + `IMPLEMENTS` | Một **danh sách phương thức** mà nhiều loại khối cam kết cùng có | ⭐ *"Đối xử với nhiều loại khối khác nhau theo cùng một cách"* |
| `EXTENDS` | Khối mới **kế thừa** mọi biến và phương thức của khối cũ | *"Khối này là một phiên bản đặc biệt của khối kia"* |
| `REFERENCE TO` | Một **tên khác** trỏ tới một biến có sẵn | *"Làm việc trên biến ở chỗ khác mà không chép nó"* |

### Cùng một bài toán, ba cách

Bài toán — lấy thẳng từ Chương 27: tầng máy phải biết **mọi trạm đã hết board chưa** trước khi coi là
xả xong (Chương 27 mục 27.5, bảng chốt dòng 10: *"không chỉ trạm đầu"*).

```iecst
// ── A · Cách của sách: mỗi trạm công bố biến toàn cục, tầng máy đọc từng cái ──
M_AllEmpty := Stn1.Ready AND NOT Stn1.Busy
              AND Stn2.Ready AND NOT Stn2.Busy;

// ── B · Trạm là khối có phương thức: tầng máy HỎI, không đọc biến bên trong ──
M_AllEmpty := Station1.IsEmpty() AND Station2.IsEmpty();

// ── C · Interface: mọi trạm cam kết cùng một câu trả lời, tầng máy hỏi trong một vòng lặp ──
M_AllEmpty := TRUE;
FOR i := 1 TO 2 DO
    M_AllEmpty := M_AllEmpty AND aStation[i].IsEmpty();
END_FOR;
```

Cách C cần hai phần khai báo: interface, và mỗi trạm cam kết thực hiện nó.

```iecst
INTERFACE I_Station
    METHOD IsReady : BOOL        // sẵn sàng nhận board mới
    END_METHOD
    METHOD IsEmpty : BOOL        // không còn board nào trong trạm
    END_METHOD
    METHOD HasFault : BOOL
    END_METHOD
END_INTERFACE

FUNCTION_BLOCK FB_Stn2Cure IMPLEMENTS I_Station
    // … khai báo và trình tự của trạm 2 — như Chương 26, nhưng nằm trong khối;
    //   cảm biến board vào qua chân BoardIn, không đọc thẳng DI_BoardStn2 (CP6, Chương 11) …

    METHOD IsReady : BOOL
        IsReady := (Stn2_Step = 0);
    END_METHOD

    METHOD IsEmpty : BOOL
        IsEmpty := (Stn2_Step = 0) AND NOT BoardIn;
    END_METHOD

    METHOD HasFault : BOOL
        HasFault := Stn2_Fault;
    END_METHOD
END_FUNCTION_BLOCK

// ── Tầng máy ──
VAR
    Station1 : FB_Stn1Dispense;          // khối trạm 1 cũng IMPLEMENTS I_Station
    Station2 : FB_Stn2Cure;
    aStation : ARRAY[1..2] OF I_Station; // ⭐ biến kiểu interface là THAM CHIẾU tới một thể hiện
    i        : INT;
END_VAR

aStation[1] := Station1;                 // gắn — trước lần gắn đầu tiên, biến chứa 0
aStation[2] := Station2;
```

| Cách | ⭐ Ưu | ⚠ Nhược |
|---|---|---|
| A — biến toàn cục công bố | Chạy trên **mọi hệ**; người bảo trì đọc được bằng ladder | Tầng máy phải **liệt kê từng trạm** — thêm trạm 3 mà quên sửa dòng này thì *"xả xong"* sai; và ⚠ thật ra chỉ có một chỗ ghi mỗi biến là nhờ kỷ luật, không nhờ ngôn ngữ |
| B — phương thức | Tầng máy **không thấy** bên trong trạm — đổi cách trạm tính *"trống"* không ảnh hưởng ai | Vẫn liệt kê từng trạm; chỉ chạy trên hệ có OOP |
| ⭐ C — interface | ⭐ Thêm trạm 3 = thêm **một dòng gắn** và sửa giới hạn vòng lặp; mọi trạm **buộc** phải trả lời đủ ba câu — thiếu một phương thức là **không biên dịch được** | Khó đọc nhất với người chỉ quen ladder; chỉ chạy trên hệ có OOP; ⚠ thêm một loại lỗi mới — tham chiếu chưa gắn |

⭐ **Khuyến nghị:** máy cỡ DP-01, đội bảo trì đọc ladder, hoặc máy có thể phải chuyển nền → **cách A**,
đúng như sách đang dùng. Máy có **nhiều trạm hoặc nhiều loại cơ cấu cùng vai trò**, chạy trên **một
nền có OOP suốt đời**, và đội có nền tảng phần mềm → **cách C** trả công xứng đáng. Cách B đứng giữa:
dùng khi muốn đóng gói mà chưa cần đa hình.

### ⚠⚠ Năm cái bẫy chỉ có khi dùng hướng đối tượng TRÊN PLC

Người đến từ C# hay Java mang theo thói quen đúng ở đó và **sai ở đây**, vì PLC chạy theo vòng quét.

| # | Bẫy | ⭐ Cách đúng |
|:-:|---|---|
| 1 | ⚠⚠ **Khai bộ định thời trong phương thức.** Biến khai trong phương thức là biến **tạm** — tài liệu CODESYS ghi rõ chúng được **khởi tạo lại mỗi lần gọi**. Bộ định thời ở đó về 0 ở mỗi lần gọi: **không bao giờ** tới giờ | Mọi thứ cần **nhớ qua các vòng quét** — bộ định thời, bộ đếm, cờ, bước — khai ở **khối**, không ở phương thức |
| 2 | ⚠ **Đặt logic chạy theo thời gian vào phương thức.** Phương thức chỉ chạy **khi được gọi** — không ai gọi thì nó đứng yên, y như khối không được gọi (mục 30.5b, quy tắc 2) | Logic chạy theo vòng quét nằm ở **thân khối**, và thân khối vẫn được gọi **mỗi vòng**. ⭐ Phương thức chỉ để **hỏi** và **ra lệnh** |
| 3 | ⚠⚠ **Gọi phương thức qua một biến interface chưa gắn.** Biến kiểu interface là **tham chiếu**, và bằng 0 tới lần gắn đầu tiên | Gắn **một lần** lúc khởi động; và ở chỗ nào không chắc, kiểm `aStation[i] <> 0` **trước** khi gọi |
| 4 | ⚠ **Dùng `:=` với tham chiếu để "trỏ sang chỗ khác".** Với `REFERENCE TO`, `:=` **chép giá trị** vào chỗ tham chiếu đang trỏ — muốn trỏ sang chỗ khác phải dùng `REF=`. Và không khai được **mảng các tham chiếu** | Đọc kỹ từng phép gán có tham chiếu; ⭐ và như PLCopen yêu cầu: **không** tính toán trên con trỏ, **không** so lớn–nhỏ trên con trỏ hay tham chiếu (quy tắc E2, E3, Phụ lục N) |
| 5 | ⚠ **Kế thừa theo kiểu "có liên quan".** Máy bơm **dùng** một động cơ, nhưng máy bơm **không phải là** một động cơ — cho `FB_Pump EXTENDS FB_Motor` là trộn hai quan hệ | Hỏi *"khối con **có phải là** khối cha không?"* — không phải thì **chứa** một thể hiện của nó thay vì kế thừa. ⭐ PLCopen đặt đúng câu hỏi này cho người viết thư viện: *kết hợp hay kế thừa?* — và tài liệu OOP của họ kể một chuyện thật: ví dụ lò hơi cho mọi khối kế thừa một khối mô hình hành vi, rồi không mở rộng thêm được vì một khối chỉ có **một** cha, phải chuyển sang **chứa** (mục 4.5, 5.1) |

> ⚡ **Thêm hai điều về kế thừa trên CODESYS:** một khối chỉ kế thừa được **một** khối (nhưng thực hiện
> được **nhiều** interface); và khối con **không được** khai lại biến trùng tên với khối cha. Khi sửa
> chương trình đang chạy mà có tham chiếu interface, hệ phải định địa chỉ lại các tham chiếu đó — tài
> liệu hãng cảnh báo việc này tốn thêm thời gian và có thể gây **rung thời gian quét**.
>
> ⚡ Và về thời gian quét nói chung: tài liệu OOP của PLCopen ghi nhận một lời gọi phương thức qua
> interface (gọi "ảo") có thể tốn thời gian **hơn hẳn** một lời gọi thường, tuỳ phần cứng (mục 5.2).
> Dùng interface trong một vòng lặp dài chạy mỗi vòng quét thì **đo** trước.

### Thuộc tính — và vì sao sách dùng phương thức thay cho nó

Bản 4 của chuẩn định nghĩa thuộc tính bằng hai phương thức đặc biệt, `PROPERTY_GET` và `PROPERTY_SET`.
Đọc và ghi thuộc tính **viết như biến**, nhưng thật ra là **gọi mã**:

```iecst
FUNCTION_BLOCK FB_Foo
    VAR PRIVATE
        _nFoo : INT;             // biến thật, giấu bên trong
    END_VAR
    PROPERTY_GET PUBLIC nFoo : INT
        nFoo := _nFoo;
    END_PROPERTY
    PROPERTY_SET PUBLIC nFoo : INT
        _nFoo := nFoo;           // chỗ đặt phép kiểm giới hạn, nếu cần
    END_PROPERTY
END_FUNCTION_BLOCK
```

⚠ CODESYS có thuộc tính từ trước bản 4, với cách khai riêng — mỗi thuộc tính có hai phương thức truy
cập `Get` và `Set`. ⭐ Sách dùng **phương thức trả về giá trị** (`IsEmpty()`) thay cho thuộc tính ở ví dụ
chính, vì hai lý do: dấu `()` nói với người đọc *"đây là lời gọi, có mã chạy"* — thuộc tính thì trông
**y hệt** một biến; và cú pháp phương thức giống nhau hơn giữa các hệ.

### Hệ nào có — đối chiếu ngày 2026-09-26

| Hệ | Hướng đối tượng | Căn cứ |
|---|---|---|
| ⭐ **CODESYS** và các nền dựng trên nó | ✅ `METHOD`, `PROPERTY`, `INTERFACE`, `EXTENDS`, `IMPLEMENTS`, `THIS^`, `SUPER^`, `REFERENCE TO`, và phương thức khởi tạo riêng `FB_init` | Trợ giúp trực tuyến CODESYS |
| **Siemens** — TIA Portal (LAD / FBD / SCL) | ❌ Trong TIA Portal thì không. Hướng đối tượng nằm ở **SIMATIC AX** — môi trường viết ST riêng; thư viện AX nhập vào TIA Portal thì lớp thành FB, phương thức thành FC, và ⚠ **không dùng trực tiếp được** trong chương trình TIA | Tài liệu TIA Portal V20, mục về lập trình hướng đối tượng trong thư viện SIMATIC AX |
| **Rockwell** — Logix | ❌ Tài liệu tuân thủ IEC 61131-3 bản 3 của Logix liệt kê từng tính năng được hỗ trợ — **không có** mục nào cho lớp, phương thức hay interface. Tái dùng bằng lệnh tự định nghĩa (mục 30.5) | Tài liệu tuân thủ IEC 61131-3 của Logix, bản 3/2022 |
| **Mitsubishi** — dòng FX5 | ⚠ Không thấy `METHOD` / `INTERFACE` / `EXTENDS` trong tài liệu lệnh và khối của dòng FX5 có trong bộ nguồn — tra tài liệu lập trình của dòng bạn dùng | Tài liệu lệnh FX5 |
| **Inovance** | Dòng dựng trên CODESYS: theo nền CODESYS — ⚠ kiểm phiên bản. Dòng nhỏ (họ H5U / Easy): không thấy trong tài liệu lập trình | Tài liệu H5U / Easy |

> ⭐⭐ **Câu chốt của mục này:** hướng đối tượng là **một cách tổ chức thêm**, không phải bậc thang
> trên của lập trình PLC. Một chương trình cổ điển tổ chức tốt theo ba tầng (Chương 27) dễ bảo trì hơn
> một chương trình hướng đối tượng mà người sửa lúc hai giờ sáng không đọc nổi. ⚡ Chọn nó khi nó làm
> cho **người sửa** đỡ việc — đúng tiêu chí ở mục 30.1.

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

- **PLCopen** — *Creating PLCopen Compliant Libraries*, v1.0 (5/2017, 89 trang; bản đầy đủ, đối chiếu
  2026-09-28): hai loại khối — **kích bằng sườn** (`Execute` ↔ `Done`) và **điều khiển theo mức**
  (`Enable` ↔ `Valid`) (mục 2.2); ⭐ phát hiện sườn cần **hai vòng quét** nên khối phải nhận giá trị mới
  mỗi vòng thì dùng mô hình mức (mục 3.1); quy tắc khối kích bằng sườn — tham số chốt ở sườn lên, sườn
  xuống không huỷ việc, ngõ ra giữ ít nhất một lần gọi (mục 3.2); `Busy` bật ngay khi nhận lệnh, việc
  xong trong một lần gọi thì không thấy `Busy` (mục 3.4); miền mã lỗi, `0` và `1` dành sẵn (mục 3.5);
  khối mẫu `ETrig` không nhìn `Execute` khi đang bận (mục 5.1); quy tắc chung của khối chuyển động —
  loại trừ nhau, xoá ở sườn xuống, kích lại khi chưa xong thì lệnh trước không có phản hồi (Phụ lục 4)
  — nền cho mục 30.5b.
- Tài liệu thư viện khối chuyển động của **hai hãng khác nhau**, mục *quy tắc chung cho khối* theo
  PLCopen (đối chiếu 2026-09-26): tham số chốt ở sườn lên; `Busy`/`Done`/`Error` loại trừ nhau; kết
  quả xoá ở sườn xuống và vẫn hiện ít nhất một vòng nếu `Execute` tắt giữa chừng; `Enable` tắt thì
  khối ngừng và xoá ngõ ra. ⚠ Hai tài liệu **lệch nhau** ở hành vi kích lại khi đang `Busy` — đúng hai
  câu trả lời có trong chính PLCopen; bảng năm quy tắc ở mục 30.5b ghi rõ chỗ lệch.

- **PLCopen** — *Guidelines for usage of Object-Oriented Programming*, v1.0 (11/2021, 27 trang; bản đầy
  đủ, đối chiếu 2026-09-28): cách cổ điển **không bị thay thế** mà cùng tồn tại (mục 1.1); các câu hỏi
  thiết kế — chỉ dùng phương thức hay cả truy cập biến trực tiếp, interface, *kết hợp hay kế thừa* (mục
  1); bảng so sánh ở mục 2.3 — bản 3 có lớp, phương thức, interface, đa hình, nhưng **không** có thuộc
  tính và hàm tạo chỉ một phần, khớp nhận định *"thuộc tính vào chuẩn ở bản 4"* của mục 30.5c; năm
  nguyên tắc SOLID (mục 3.1); ví dụ lò hơi vướng giới hạn một cha, chuyển từ kế thừa sang chứa (mục
  4.5, 5.1); gọi phương thức "ảo" tốn thời gian khác hẳn nhau theo phần cứng (mục 5.2) — nền cho mục
  30.5c.
- **CODESYS** — trợ giúp trực tuyến (đối chiếu 2026-09-26), các mục *Method*, *Property*, *Interface*,
  *Implementation of an Interface*, *Extension of a Function Block*, *REFERENCE TO*, *THIS*, *SUPER*,
  *FB_Init*: biến trong phương thức **khởi tạo lại mỗi lần gọi**; phương thức không đọc được `VAR_TEMP`
  của khối; biến kiểu interface là tham chiếu và bằng 0 tới lần gắn đầu; `:=` với tham chiếu chép giá
  trị, `REF=` mới gắn; không có mảng tham chiếu; không đa kế thừa nhưng nhiều interface; sửa chương
  trình đang chạy có tham chiếu interface thì tốn thêm thời gian — nền cho bảng năm cái bẫy.
- **Siemens** — tài liệu TIA Portal V20, mục *Object-oriented programming in SIMATIC AX libraries*:
  hướng đối tượng thuộc SIMATIC AX; nhập vào TIA Portal thì lớp thành FB, phương thức thành FC và không
  dùng trực tiếp được.
- **Rockwell Automation** — *Logix 5000 Controllers IEC 61131-3 Compliance* (1756-PM018I, 3/2022):
  bảng tuân thủ theo từng tính năng — không có mục cho lớp, phương thức hay interface.
- **Stefan Henneken** — *IEC 61131-3: Comparison of Edition 3 and Edition 4* (6/2025): cú pháp thuộc
  tính của bản 4, ví dụ `FB_Foo` ở mục 30.5c lấy theo bài này.

> ⚡ Quy ước đặt tên ở mục 30.2 là **quy ước của cuốn sách này**, không phải chuẩn ngành. Dự án của bạn
> có thể dùng quy ước khác — điều bắt buộc là **có một quy ước, viết ra thành văn, và dùng nhất quán**.
