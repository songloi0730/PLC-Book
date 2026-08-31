# Chương 16 — Latch, Set/Reset & bắt cạnh

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 16.1 Ba câu hỏi mà chương này trả lời

Chương 15 đã cho bạn nấc thang và bốn tổ hợp tiếp điểm. Nhưng ladder thuần chỉ mô tả được thứ **đang
đúng ngay lúc này**: tiếp điểm đóng thì cuộn dây lên, tiếp điểm mở thì cuộn dây tắt. Vòng quét sau,
mọi thứ tính lại từ đầu (Chương 10).

Máy thật cần nhiều hơn thế. Nó cần **nhớ**:

| Câu hỏi | Công cụ trong chương này |
|---|---|
| Nhấn nút rồi nhả ra, máy vẫn phải chạy tiếp — làm sao? | **Tự giữ** hoặc **SET/RESET** (mục 16.2–16.3) |
| Mất điện rồi bật lại, máy nhớ gì và quên gì? | **Biến giữ được** *(retentive)* (mục 16.4) |
| Board đi qua cảm biến một lần, sao chương trình đếm thành 40 lần? | **Bắt cạnh** *(edge detection)* (mục 16.5) |

Ba công cụ này nhỏ, nhưng dùng sai cả ba đều dẫn tới cùng một hậu quả: **máy không biết mình đang ở
đâu**. Và một cỗ máy không biết mình đang ở đâu là cỗ máy sẽ làm điều bất ngờ vào lúc bạn không có
mặt.

---

## 16.2 Tự giữ — nhắc lại đủ để so sánh

Mạch tự giữ *(seal-in / latch)* đã xuất hiện ở Chương 15, mục 15.4. Nhắc lại ở đây **chỉ để đặt cạnh
SET/RESET**, vì so sánh hai cách mới là nội dung của chương này.

```text
   DI_StartPB   DI_StopPB                          M_Running
──────┤ ├──────────┤ ├───────────┬───────────────────( )──────
                               │
   M_Running                   │
──────┤ ├───────────────────────┘
```

Nhánh thứ hai — tiếp điểm của chính `M_Running` — là nhánh "tự giữ": khi cuộn dây đã lên, nó tự cấp
điều kiện cho chính mình, nên nhả nút Start ra thì mạch vẫn giữ.

Ba tính chất cần nhớ để so với mục sau:

- **Điều kiện dừng nằm ngay trên đường dẫn.** `DI_StopPB` nối tiếp, nên hễ nó mất là cuộn dây tắt —
  không có cách nào lọt.
- **Không có bộ nhớ riêng.** Trạng thái được duy trì bằng chính logic, tính lại mỗi vòng quét.
- **Mất điện là mất trạng thái.** Bật lại, `M_Running` bằng 0. Với một mạch chạy máy, đây là **hành
  vi đúng và mong muốn** — máy không được tự chạy lại sau khi có điện (Chương 48).

---

## 16.3 SET / RESET — và cái giá của nó

### Hai lệnh, hai vị trí riêng biệt

Chuẩn IEC 61131-3 có hai lệnh cuộn dây nhớ: **SET** *(latch, S)* và **RESET** *(unlatch, R)*.

```text
   DI_StartPB                                       M_Running
──────┤ ├──────────────────────────────────────────────(S)─────

   DI_StopPB                                         M_Running
──────┤/├──────────────────────────────────────────────(R)─────
```

- `(S)` — khi đường dẫn đúng, đặt bit lên 1 và **để đó**. Đường dẫn mất đi cũng không tắt.
- `(R)` — khi đường dẫn đúng, đưa bit về 0 và để đó.
- Cả hai đường dẫn cùng sai → bit **giữ nguyên giá trị cũ**.

Đây chính là điểm khác biệt cốt lõi: cuộn dây thường trả lời câu hỏi *"ngay bây giờ điều kiện có đúng
không?"*; SET/RESET trả lời câu hỏi *"lần cuối có ai bảo tôi đổi, họ bảo gì?"*

### Bảng đối chiếu

| | **Tự giữ** | **SET / RESET** |
|---|---|---|
| Số nấc thang | 1 | 2 (dễ nằm cách xa nhau) |
| Điều kiện dừng | **Nằm trên đường dẫn**, không lọt được | Ở một nấc khác — phải đi tìm |
| Đọc chương trình | Nhìn một nấc là hiểu | Phải tìm **mọi** nấc có `(S)`/`(R)` của bit đó |
| Khi hai điều kiện cùng đúng | Stop thắng (vì nối tiếp) | ⚠ **Nấc nào chạy sau thì thắng** |
| Mất điện | Về 0 | Tuỳ khai báo biến — xem mục 16.4 |
| Hợp với | Mạch chạy/dừng, cho phép cơ cấu | Cờ trạng thái, cờ lỗi, đánh dấu sản phẩm |

> ⚠ **NGUY HIỂM — "nấc nào chạy sau thì thắng" không phải chi tiết nhỏ**
> Nếu `DI_StartPB` và `DI_StopPB` cùng đúng, kết quả phụ thuộc **thứ tự nấc thang trong chương trình**.
> Đặt `(R)` sau `(S)` thì dừng thắng; đặt ngược lại thì chạy thắng.
>
> Quy tắc bắt buộc: **nấc RESET luôn đặt SAU nấc SET** khi bit đó liên quan tới việc dừng hoặc tới an
> toàn. Đây là một trong số ít chỗ mà thứ tự nấc thang có ý nghĩa sinh mạng.
>
> Và ngay cả khi làm đúng: **không dùng SET/RESET cho chức năng an toàn**. Chức năng an toàn nằm ở
> mạch an toàn phần cứng, không nằm trong logic PLC thường (Chương 47).

### Khi nào dùng cái nào

Quy tắc thực dụng, đúng trong hầu hết trường hợp:

> **Cái gì mô tả "máy đang làm gì" → tự giữ.**
> **Cái gì mô tả "đã có chuyện gì xảy ra" → SET/RESET.**

Áp lên DP-01:

| Bit | Cách làm | Vì sao |
|---|---|---|
| `M_Running` — máy đang chạy | **Tự giữ** | Điều kiện dừng phải nối tiếp, không được lọt |
| `M_ConvEnable` — cho phép chuyền chạy | **Cuộn dây thường** | Phụ thuộc điều kiện hiện tại, không cần nhớ |
| `M_AnyFault` — đã có lỗi | **SET/RESET** | Lỗi phải **dính** cho tới khi người vận hành xác nhận, dù nguyên nhân đã hết |
| `M_Board1IsNG` — board ở trạm 1 bị đánh dấu lỗi | **SET/RESET** | Đánh dấu một lần, giữ tới khi board rời trạm |

Trường hợp `M_AnyFault` cho thấy rõ vì sao SET/RESET tồn tại. Giả sử mất khí trong 200 ms rồi có lại.
Nếu dùng cuộn dây thường, cờ lỗi lên rồi tắt ngay — người vận hành quay lại chỉ thấy máy đứng im mà
không có lỗi nào. Với SET/RESET, lỗi **dính**, và chỉ mất khi có người nhấn Reset:

```iecst
// SET: bất kỳ nguyên nhân nào cũng đặt cờ lỗi
IF M_AirFault OR M_Stn1Timeout OR M_Stn2Timeout THEN
    M_AnyFault := TRUE;
END_IF;

// RESET: chỉ người vận hành gỡ được, VÀ chỉ khi nguyên nhân đã hết
IF DI_ResetPB AND NOT M_AirFault
              AND NOT M_Stn1Timeout
              AND NOT M_Stn2Timeout THEN
    M_AnyFault := FALSE;
END_IF;
```

Dòng `AND NOT …` ở nhánh RESET là chỗ người mới hay bỏ. Không có nó, người vận hành nhấn Reset khi
vẫn còn mất khí thì cờ lỗi tắt trong một vòng quét rồi lên lại — máy nháy đèn lỗi liên tục và không
ai hiểu chuyện gì.

### ⚠ Vì sao lạm dụng SET/RESET làm máy "không biết mình đang ở đâu"

Đây là lý do chương này tồn tại.

SET/RESET rất tiện: cần nhớ gì thì đặt một bit. Nhưng mỗi bit như vậy là **một mẩu trạng thái nằm rời
rạc**, và chúng không ràng buộc nhau. Sau vài tháng, một chương trình có thể có ba mươi bit `(S)/(R)`
rải khắp nơi.

Hậu quả cụ thể:

- **Tổ hợp trạng thái không hợp lệ trở nên khả thi.** `M_Stn1Busy` và `M_Stn1Empty` cùng bằng 1 là vô
  nghĩa về mặt vật lý, nhưng không có gì trong chương trình ngăn nó xảy ra — vì hai bit được đặt ở
  hai nấc khác nhau, không ai kiểm chéo.
- **Không ai trả lời được câu "máy đang ở trạng thái nào".** Câu trả lời là một tổ hợp ba mươi bit, và
  không tồn tại danh sách các tổ hợp hợp lệ.
- **Sau sự cố, không khôi phục được.** Muốn đưa máy về trạng thái đã biết chắc, bạn phải nhớ xoá đúng
  những bit nào — và danh sách đó chỉ nằm trong đầu người viết.

Cách chữa **không** phải là dùng SET/RESET cẩn thận hơn. Cách chữa là: khi trạng thái bắt đầu có nhiều
mảnh phụ thuộc nhau, chuyển sang **một biến trạng thái duy nhất** — máy trạng thái (Chương 25) và
biến bước của trình tự (Chương 26). Một biến `Stn1_Step` bằng 20 nói rõ hơn mười bit cờ, và nó
**không thể** ở hai trạng thái cùng lúc.

> 💡 **MẸO — phép thử ba mươi giây**
> Đếm số bit dùng `(S)` hoặc `(R)` trong chương trình. Dưới mười: bình thường. Trên hai mươi: gần như
> chắc chắn bạn đang mô phỏng một máy trạng thái bằng cờ rời rạc, và nên đọc Chương 25 trước khi viết
> thêm.

---

## 16.4 Mất điện thì nhớ gì — biến giữ được

Một bit đã SET có sống qua lần mất điện không? Câu trả lời **không nằm ở lệnh SET**, mà nằm ở **cách
khai báo biến**.

| Loại biến | Sau khi mất điện rồi bật lại |
|---|---|
| Thường *(non-retentive)* | Về giá trị khởi tạo, thường là 0 |
| **Giữ được** *(retentive / latched)* | Giữ nguyên giá trị trước khi mất điện |

Cách khai báo khác nhau theo hệ (mục 16.7), nhưng nguyên tắc chọn thì giống nhau ở mọi hệ:

> **Giữ lại thứ mô tả THẾ GIỚI THẬT. Đừng giữ thứ mô tả Ý ĐỊNH của chương trình.**

Áp lên DP-01:

| Dữ liệu | Giữ? | Lý do |
|---|---|---|
| Số board đã làm trong ca | ✅ Giữ | Là sự thật đã xảy ra; mất đi là mất số liệu sản xuất |
| Tổng giờ chạy của cơ cấu | ✅ Giữ | Dùng cho lịch bảo trì |
| Mã hàng đang chạy | ✅ Giữ | Vẫn là mã đó sau khi có điện lại |
| `M_Running` — máy đang chạy | ❌ **Không giữ** | ⚠ Giữ nó thì máy **tự chạy lại** khi có điện |
| `Stn1_Step` — bước hiện tại | ❌ **Không giữ** | Sau mất điện, cơ cấu có thể đã ở tư thế khác; chạy tiếp từ bước cũ là nguy hiểm |
| `M_AnyFault` — có lỗi | ⚠ Tuỳ | Xem ghi chú bên dưới |

> ⚠⚠ **NGUY HIỂM — hai bit không bao giờ được giữ**
> `M_Running` và biến bước của trình tự. Giữ `M_Running` nghĩa là **máy tự khởi động lại khi có điện
> trở lại** — cỗ máy chuyển động mà không ai ra lệnh, đúng vào lúc người ta đang đứng cạnh nó vì mất
> điện. Việc khởi động lại phải luôn là **hành động có chủ ý của người** *(intentional restart)*, yêu
> cầu của IEC 60204-1 (Chương 28, Chương 48).
>
> Giữ biến bước còn tinh vi hơn: chương trình tin nó đang ở bước 40, trong khi lúc mất điện xy-lanh
> đã tụt về do hết khí. Bước 40 ra lệnh cho cơ cấu tiếp theo chạy, tin rằng board đang được kẹp. Nó
> không được kẹp.

Với `M_AnyFault`: giữ thì sau khi có điện lại máy vẫn báo lỗi cũ — người vận hành phải Reset có chủ
ý, và đó thường là điều tốt. Nhưng nếu giữ, phải bảo đảm nguyên nhân được đánh giá lại chứ không chỉ
hiển thị cờ cũ. Đơn giản nhất: **không giữ cờ lỗi, nhưng luôn vào trạng thái yêu cầu về gốc** sau khi
có điện lại — cách này không phụ thuộc bộ nhớ giữ được, nên ít sai hơn.

> ⚡ **LƯU Ý — bộ nhớ giữ được dựa vào pin hoặc tụ**
> Ở nhiều hệ, vùng nhớ giữ được duy trì bằng pin hoặc siêu tụ. Pin hết mà không ai để ý thì dữ liệu
> "giữ được" âm thầm biến mất — và cả số liệu sản xuất đi theo. Thay pin là hạng mục bảo trì phòng
> ngừa có thật (Chương 51). Dữ liệu nào thực sự quan trọng thì đừng chỉ dựa vào vùng nhớ giữ được:
> ghi ra nơi khác.

---

## 16.5 Bắt cạnh — công cụ nhỏ, lỗi lớn

### Bài toán

Trên DP-01, mỗi board đi qua cảm biến `DI_BoardStn1`. Ta muốn đếm số board:

```iecst
// ✗ SAI — ĐỪNG CHÉP
IF DI_BoardStn1 THEN
    BoardCount := BoardCount + 1;
END_IF;
```

Board dừng ở trạm khoảng 4 giây. Thời gian quét 10 ms. Chương trình đếm **400 lần cho một board**.

Lỗi này hiển nhiên khi chỉ ra, và vẫn là một trong những lỗi bị mắc nhiều nhất — vì đoạn code trên
đọc **rất thuận tai**: "nếu có board thì tăng số đếm".

Gốc rễ nằm ở Chương 10: chương trình chạy lại **toàn bộ, mỗi vòng quét**. `IF DI_BoardStn1 THEN` không
hỏi *"board vừa tới phải không?"* — nó hỏi *"ngay lúc này có board không?"*, và câu trả lời là "có"
suốt 400 vòng quét liên tiếp.

### Mức với cạnh — phân biệt cho rõ

| | **Mức** *(level)* | **Cạnh** *(edge)* |
|---|---|---|
| Trả lời câu hỏi | Ngay bây giờ tín hiệu bằng mấy? | Tín hiệu **vừa đổi** phải không? |
| Đúng trong bao lâu | Suốt thời gian tín hiệu giữ mức | **Đúng một vòng quét** |
| Ví dụ | "Đang có board" | "Board vừa tới" |

Có hai loại cạnh: **cạnh lên** *(rising edge, R\_TRIG)* — tín hiệu từ 0 lên 1; và **cạnh xuống**
*(falling edge, F\_TRIG)* — từ 1 xuống 0. Kết quả của việc bắt cạnh còn hay được gọi là **xung một
nhịp** *(one-shot / one-scan pulse)*.

### Cách hoạt động

Bắt cạnh không có gì thần bí: nó là **so sánh với giá trị của vòng quét trước**.

```iecst
// ✓ ĐÚNG — nguyên lý bắt cạnh lên, viết tay
M_BoardEdge := DI_BoardStn1 AND NOT M_BoardPrev;   // 1 khi vừa đổi 0→1
M_BoardPrev := DI_BoardStn1;                        // nhớ cho vòng sau
```

Dòng thứ hai **phải nằm sau** dòng thứ nhất. Đảo lại thì `M_BoardPrev` đã bằng giá trị mới trước khi
được so sánh, và `M_BoardEdge` **không bao giờ** lên — một lỗi im lặng khó tìm.

Trong thực tế bạn dùng khối chuẩn thay vì viết tay:

```iecst
VAR
    TrigBoard1 : R_TRIG;      // khối chuẩn IEC 61131-3
END_VAR

TrigBoard1(CLK := DI_BoardStn1);
IF TrigBoard1.Q THEN
    BoardCount := BoardCount + 1;    // đúng 1 lần cho mỗi board
END_IF;
```

> ⚠ **Mỗi tín hiệu cần một thể hiện *(instance)* riêng của khối bắt cạnh.**
> Dùng chung một khối `R_TRIG` cho hai tín hiệu là lỗi kinh điển: khối chỉ nhớ được một giá trị trước
> đó, nên hai tín hiệu ghi đè lẫn nhau và cả hai cạnh đều sai. Trong ladder, lỗi tương đương là dùng
> **cùng một bit nhớ** cho hai lệnh bắt cạnh khác nhau.

### Khi nào **bắt buộc** bắt cạnh

Quy tắc gọn: **bất cứ khi nào hành động phải xảy ra ĐÚNG MỘT LẦN cho mỗi sự kiện.**

| Việc | Vì sao bắt buộc | Hậu quả nếu quên |
|---|---|---|
| **Đếm** | Mỗi board một lần | Số đếm sai gấp hàng trăm lần (Chương 18) |
| **Kích chuyển bước** | Mỗi lần nhấn một bước | Nhấn giữ nút → nhảy vọt qua nhiều bước |
| **Gửi lệnh ra mạng** | Mỗi sự kiện một bản tin | Ngập bản tin, nghẽn mạng, hệ nhận từ chối (Chương 39) |
| **Ghi nhật ký / báo lỗi mới** | Mỗi lần một dòng | Hàng nghìn dòng trùng, nhật ký thành vô dụng |
| **Đảo trạng thái** (nút bấm bật/tắt cùng một nút) | Mỗi lần nhấn đảo một lần | Trạng thái nhấp nháy suốt thời gian giữ nút |
| **Nạp công thức sản phẩm** | Mỗi lần chọn một lần | Ghi đè liên tục, tham số bị đặt lại giữa chu trình (Chương 29) |

Ngược lại, **không** cần bắt cạnh khi hành động là "duy trì một điều kiện": `DO_ConvRun := M_ConvEnable;`
đúng ở mọi vòng quét và phải như vậy.

> 💡 **MẸO — phép thử một câu**
> Đọc dòng lệnh rồi hỏi: *"nếu dòng này chạy 400 lần liên tiếp thì có sao không?"*
> Không sao → dùng mức. Có sao → **phải bắt cạnh**.

### Cạnh xuống dùng làm gì

Cạnh lên phổ biến hơn, nhưng cạnh xuống có chỗ dùng riêng và thường là chỗ tinh tế hơn:

```iecst
VAR
    TrigLeave : F_TRIG;
END_VAR

// Board vừa RỜI trạm 1 — đây mới là lúc trạm thật sự trống
TrigLeave(CLK := DI_BoardStn1);
IF TrigLeave.Q THEN
    M_Stn1Occupied := FALSE;
    Stn1CycleCount := Stn1CycleCount + 1;   // đếm chu trình đã hoàn tất
END_IF;
```

Đếm ở cạnh xuống đếm **board đã làm xong**; đếm ở cạnh lên đếm **board đã vào**. Hai con số này khác
nhau đúng bằng số board đang nằm trong máy — và nhầm lẫn giữa chúng là nguồn gốc của những báo cáo
sản lượng lệch mà không ai giải thích được.

---

## 16.6 Trên máy mẫu DP-01 — ba mẩu logic hoàn chỉnh

### Cho phép chạy — tự giữ, có mọi điều kiện trên đường dẫn

```text
  DI_StartPB  DI_StopPB  DI_EStopOK  DI_AirOK  M_AnyFault      M_Running
─────┤ ├────────┤ ├────────┤ ├────────┤ ├────────┤/├────────────( )─────
                                                              │
  M_Running                                                   │
─────┤ ├──────────────────────────────────────────────────────┘
```

Bốn điều kiện nối tiếp, đặt **trước** điểm nối của nhánh tự giữ. Nhờ vậy mất bất kỳ điều kiện nào —
Stop, dừng khẩn, khí, hoặc có lỗi — thì `M_Running` tắt ngay và **không tự lên lại**. Muốn chạy tiếp
phải nhấn Start lần nữa: một hành động có chủ ý của người.

> ⚠ Nhắc lại từ Chương 15: `DI_StopPB` và `DI_EStopOK` là tín hiệu từ **tiếp điểm NC**, nên bình
> thường chúng bằng 1. Trong nấc thang, chúng dùng lệnh tiếp điểm **thường mở** `┤ ├`. Đứt dây → tín
> hiệu về 0 → mạch mở → máy dừng. Đó là tổ hợp 3 trong bảng bốn tổ hợp.

### Đánh dấu board lỗi — SET/RESET đúng chỗ

```iecst
VAR
    TrigIn  : R_TRIG;
    TrigOut : F_TRIG;
END_VAR

TrigIn(CLK := DI_BoardStn1);
TrigOut(CLK := DI_BoardStn1);

// Board mới vào: xoá dấu của board TRƯỚC ĐÓ
IF TrigIn.Q THEN
    M_Board1IsNG := FALSE;
END_IF;

// Trong lúc gia công, bất kỳ chỗ nào cũng có thể đánh dấu
IF M_Stn1Timeout OR M_DispFault THEN
    M_Board1IsNG := TRUE;
END_IF;

// Board rời trạm: chốt số liệu
IF TrigOut.Q THEN
    IF M_Board1IsNG THEN  NgCount := NgCount + 1;
    ELSE                  OkCount := OkCount + 1;
    END_IF;
END_IF;
```

Ba mẩu trên minh hoạ trọn vẹn chương này: **cạnh lên** để xoá dấu đúng một lần khi board mới vào,
**SET/RESET** để dấu dính suốt thời gian gia công, **cạnh xuống** để chốt số liệu đúng một lần khi
board rời đi.

Chú ý thứ tự: nấc xoá dấu đặt **trước** nấc đánh dấu. Nếu đảo lại, một lỗi xảy ra đúng vào vòng quét
board mới vào sẽ bị xoá mất.

### Nút một chạm đổi trạng thái đèn báo

```iecst
VAR
    TrigLamp : R_TRIG;
END_VAR

// Cùng một nút: nhấn lần lẻ bật, nhấn lần chẵn tắt
TrigLamp(CLK := DI_ResetPB);
IF TrigLamp.Q THEN
    M_LampTest := NOT M_LampTest;
END_IF;
```

Không có `R_TRIG`, đèn sẽ nhấp nháy với tần số bằng tần số vòng quét suốt thời gian giữ nút, và trạng
thái cuối cùng phụ thuộc vào việc bạn nhả nút ở vòng quét chẵn hay lẻ — tức là **ngẫu nhiên**.

---

## 16.7 Khác biệt giữa các hãng

Nguyên lý giống nhau; tên gọi và cách khai báo khác nhau. Chi tiết theo từng hệ nằm ở Phụ lục A, ở
đây chỉ nêu những chỗ **dễ vấp**:

| Điểm | Điều cần biết |
|---|---|
| Tên lệnh SET/RESET | Ladder thường ký hiệu `(S)` / `(R)`; có hệ dùng `SET`/`RST`, có hệ dùng khối `SR`/`RS` với thứ tự ưu tiên **đã cố định sẵn** |
| ⚠ Khối `SR` và `RS` | `SR` ưu tiên **Set**, `RS` ưu tiên **Reset**. Hai chữ cái đảo nhau và hành vi đảo nhau — đọc kỹ trước khi dùng |
| Lệnh bắt cạnh | Chuẩn có `R_TRIG` / `F_TRIG`; ladder các hãng có ký hiệu riêng đặt ngay trên tiếp điểm (thường là `P` và `N`) |
| ⚠ Khai báo biến giữ được | Khác nhau nhiều nhất: có hệ khai báo theo **vùng địa chỉ**, có hệ theo **thuộc tính của biến**, có hệ theo **khối dữ liệu**. Đây là chỗ chuyển chương trình giữa hai hệ hay sai |
| ⚠ Phạm vi "giữ được" | Có hệ phân biệt *giữ khi mất điện* với *giữ khi CPU chuyển STOP→RUN*. Hai việc khác nhau — tra tài liệu đúng hệ |

---

## 16.8 Bẫy thường gặp

### 🔍 BẪY 1 — Quên bắt cạnh khi đếm

Đã mổ xẻ ở mục 16.5. Đứng đầu danh sách vì nó phổ biến nhất và vì con số sai **trông vẫn hợp lý** cho
tới khi ai đó đối chiếu với số board thật.

**Hiện tượng:** số đếm tăng nhanh bất thường, tỉ lệ với thời gian sản phẩm nằm trước cảm biến.
**Cách sửa:** bọc lệnh đếm bằng `R_TRIG`.

### 🔍 BẪY 2 — Dùng chung một thể hiện khối bắt cạnh cho hai tín hiệu

```iecst
// ✗ SAI — một thể hiện, hai tín hiệu
Trig(CLK := DI_BoardStn1);
IF Trig.Q THEN  Count1 := Count1 + 1;  END_IF;
Trig(CLK := DI_BoardStn2);           // ghi đè bộ nhớ của lần gọi trên
IF Trig.Q THEN  Count2 := Count2 + 1;  END_IF;
```

**Hiện tượng:** cả hai bộ đếm đều sai, và sai theo kiểu khó đoán — đôi khi đếm, đôi khi không.
**Cách sửa:** mỗi tín hiệu một thể hiện riêng: `Trig1`, `Trig2`.

### 🔍 BẪY 3 — Đặt nấc RESET trước nấc SET

**Hiện tượng:** nhấn Stop trong lúc vẫn giữ Start thì máy **không dừng**. Người thử nghiệm thường
không phát hiện, vì khi thử người ta nhả Start rồi mới nhấn Stop.
**Cách sửa:** nấc RESET luôn đặt sau nấc SET. Và với mạch chạy/dừng thì đừng dùng SET/RESET — dùng tự
giữ, để điều kiện dừng nằm trên đường dẫn.

### 🔍 BẪY 4 — Giữ được biến bước của trình tự

**Hiện tượng:** sau khi mất điện và có điện lại, máy chạy tiếp từ giữa chu trình và **va chạm cơ cấu**
— vì tư thế thật đã đổi trong lúc mất điện.
**Cách sửa:** biến bước **không giữ**. Sau khi có điện lại, máy vào trạng thái yêu cầu về gốc
(Chương 28).

### 🔍 BẪY 5 — Đảo thứ tự hai dòng khi tự viết bắt cạnh

```iecst
// ✗ SAI — nhớ trước, so sau
M_Prev := DI_BoardStn1;
M_Edge := DI_BoardStn1 AND NOT M_Prev;     // luôn luôn FALSE
```

**Hiện tượng:** cạnh **không bao giờ** được phát hiện; không đếm, không kích. Không có báo lỗi nào,
chỉ là "chức năng đó không chạy".
**Cách sửa:** so sánh trước, cập nhật bộ nhớ sau. Hoặc đơn giản là dùng `R_TRIG`.

### 🔍 BẪY 6 — RESET cờ lỗi mà không kiểm nguyên nhân

**Hiện tượng:** nhấn Reset, đèn lỗi tắt rồi sáng lại ngay; hoặc tệ hơn, máy chạy tiếp trong khi
nguyên nhân lỗi vẫn còn.
**Cách sửa:** thêm điều kiện `AND NOT <mọi nguyên nhân>` vào nhánh RESET, như ở mục 16.3.

### 🔍 BẪY 7 — Tưởng SET/RESET tự động giữ qua mất điện

**Hiện tượng:** thiết kế dựa vào việc cờ còn nguyên sau khi bật máy, nhưng nó về 0 — vì biến không
được khai báo là giữ được.
**Cách sửa:** SET/RESET quyết định **cách bit đổi giá trị**; khai báo biến quyết định **bit có sống
qua mất điện không**. Hai chuyện tách rời (mục 16.4).

### 🔍 BẪY 8 — Bắt cạnh trên một tín hiệu đang rung

Nút bấm cơ khí nảy vài lần trong vài mili-giây. Bắt cạnh trên tín hiệu thô sẽ ra **nhiều cạnh** cho
một lần nhấn.

**Hiện tượng:** một lần nhấn nhảy hai, ba bước; hoặc bộ đếm tăng vài đơn vị.
**Cách sửa:** lọc rung trước, bắt cạnh sau — cho tín hiệu qua `TON` ngắn rồi mới đưa vào `R_TRIG`
(Chương 17, mục 17.4). Thứ tự này quan trọng: lọc **trước**, bắt cạnh **sau**.

---

## 16.9 Bảng chốt

| Cần gì | Dùng gì | Cảnh báo chính |
|---|---|---|
| Nhấn nút rồi nhả, vẫn chạy | **Tự giữ** | Điều kiện dừng phải nối tiếp **trước** điểm nối nhánh tự giữ |
| Nhớ "đã có chuyện xảy ra" | **SET/RESET** | Nấc RESET đặt **sau** nấc SET; nhánh RESET phải kiểm nguyên nhân đã hết |
| Trạng thái có nhiều mảnh ràng buộc nhau | **Máy trạng thái** (Ch.25) | Trên 20 bit `(S)/(R)` là dấu hiệu phải chuyển |
| Sống qua mất điện | **Khai báo biến giữ được** | ⚠ Không bao giờ giữ `M_Running` và biến bước |
| Làm đúng một lần mỗi sự kiện | **`R_TRIG` / `F_TRIG`** | Mỗi tín hiệu một thể hiện riêng |
| Đếm sản phẩm | **Cạnh lên** (vào) hoặc **cạnh xuống** (xong) | Hai cách cho hai con số khác nhau — chọn có ý thức |
| Bắt cạnh trên nút bấm | **Lọc rung rồi mới bắt cạnh** | Sai thứ tự thì một lần nhấn ra nhiều cạnh |

Bốn câu hỏi tự đặt trước khi viết một bit nhớ:

1. Bit này mô tả *máy đang làm gì*, hay *đã có chuyện gì xảy ra*?
2. Nếu dòng lệnh này chạy 400 lần liên tiếp thì có sao không?
3. Mất điện rồi bật lại, bit này **nên** bằng mấy — và tôi đã khai báo đúng chưa?
4. Ai xoá bit này, và điều kiện xoá đã đủ chặt chưa?

---

## 16.10 Tự kiểm

1. Nêu hai khác biệt giữa mạch tự giữ và cặp SET/RESET. Vì sao mạch chạy/dừng nên dùng tự giữ?
2. Trong chương trình, nấc `(S)` đặt sau nấc `(R)` cho cùng một bit. Nhấn đồng thời cả hai điều kiện
   thì bit bằng mấy? Vì sao đây là vấn đề an toàn?
3. ⭐ Vì sao **không bao giờ** được khai báo `M_Running` là biến giữ được? Tiêu chuẩn nào đứng sau
   nguyên tắc này?
4. Board nằm trước cảm biến 4 giây, thời gian quét 8 ms. Không bắt cạnh thì bộ đếm tăng bao nhiêu cho
   một board?
5. Viết bằng lời hai dòng lệnh thực hiện bắt cạnh lên bằng tay, và giải thích vì sao **thứ tự** hai
   dòng đó không được đảo.
6. ⭐ Đếm ở cạnh lên và đếm ở cạnh xuống của cùng một cảm biến cho hai con số khác nhau. Khác nhau ở
   điểm nào, và hiệu số giữa chúng là gì?
7. Một chương trình có 34 bit dùng `(S)/(R)`. Điều đó gợi ý vấn đề gì, và chương nào giải quyết?
8. Nhấn Reset xong đèn lỗi tắt rồi sáng lại ngay. Nguyên nhân khả dĩ nhất là gì?
9. Một lần nhấn nút làm trình tự nhảy hai bước. Nêu hai nguyên nhân có thể và cách phân biệt chúng.
10. ⭐ Vì sao giữ biến bước qua mất điện nguy hiểm hơn là mất biến bước?

> Câu 3, 6 và 10 là ba câu phân loại. Câu 10 là tinh thần của cả chương: **thà thừa nhận không biết
> mình đang ở đâu, còn hơn tin nhầm rằng mình biết.**

---

### Chương tiếp theo

Chương 17 — **Timer**. Bạn đã có bộ nhớ và cạnh; timer thêm chiều thời gian. Và Chương 17 mở đầu bằng
sai lầm phổ biến nhất trong nghề, liên quan trực tiếp tới thứ vừa học ở đây: dùng đồng hồ thay cho
phản hồi thật.

### Nguồn tham khảo chương 16

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: định nghĩa cuộn dây SET/
  RESET, khối `SR`/`RS`, và các khối bắt cạnh `R_TRIG` / `F_TRIG`. *(tiêu chuẩn có bản quyền)*
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu khởi động lại phải
  là hành động có chủ ý sau khi khôi phục nguồn — cơ sở cho quy tắc "không giữ `M_Running`" ở mục 16.4.
- Bảng I/O và đặc tả trình tự của DP-01 — Phụ lục J.
- Tài liệu lập trình của từng hệ trong Phụ lục A — dùng cho phần khai báo biến giữ được ở mục 16.7,
  vì đây là chỗ khác nhau nhiều nhất giữa các hãng.

> ⚡ Quy tắc chọn giữ / không giữ ở mục 16.4 là **quy tắc thiết kế**, không phải yêu cầu tiêu chuẩn —
> trừ trường hợp khởi động lại có chủ ý, vốn là yêu cầu thật. Máy của bạn có ràng buộc khác thì đáp án
> có thể khác, nhưng hai bit ở ô ⚠⚠ thì không có ngoại lệ.
