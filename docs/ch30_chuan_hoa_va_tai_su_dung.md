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
| **C** Phân cấp | ⭐⭐ **Khớp với kiểu dữ liệu người dùng và mảng** — thêm trạm thứ ba tốn một dòng (mục 30.3) · trình soạn thảo gợi ý theo cấp | ⚠ Phải **thiết kế cấu trúc trước**, sửa cấu trúc về sau rất đắt · ⚠ **tra chéo theo tiền tố không còn dùng được** · tên đầy đủ dài khi viết vào hồ sơ | Máy nhiều trạm **giống nhau**; hệ hỗ trợ kiểu người dùng tốt |
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
> được bằng **một lần tra chéo** *(cross-reference)*. ⚠ Ra nhiều hơn một chỗ là có lỗi — và bạn tìm
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
- **Hugh Jack** — *Automating Manufacturing Systems with PLCs*, §32.5 *Documentation*: ⭐ tài liệu
  phải **phát triển cùng dự án**, để tới cuối thì chi tiết đã quên nên vừa lâu hơn vừa thiếu; và cách
  dùng **biểu mẫu để sẵn**, đặt nơi mọi người truy cập và cập nhật được khi máy thay đổi.

> ⚡ Quy ước đặt tên ở mục 30.2 là **quy ước của cuốn sách này**, không phải chuẩn ngành. Dự án của bạn
> có thể dùng quy ước khác — điều bắt buộc là **có một quy ước, viết ra thành văn, và dùng nhất quán**.
