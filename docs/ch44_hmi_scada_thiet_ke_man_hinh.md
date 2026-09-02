# Chương 44 — HMI/SCADA: thiết kế màn hình vận hành

> **Lát cắt máy mẫu:** 4 — thêm mạng: mã 2D, MES, SMEMA, màn hình vận hành, và bộ điều khiển nhiệt độ
> keo nối RS-485.

---

## 44.1 Bài toán: 47 báo động, không ai đọc

Một cỗ máy dừng. Màn hình hiện danh sách báo động: **47 dòng**.

Người vận hành nhìn một lượt, không hiểu cái nào quan trọng, và làm điều mà mọi người vận hành trên
thế giới đều làm: **nhấn "xác nhận tất cả"** rồi thử khởi động lại.

Máy không chạy. Anh gọi kỹ thuật. Kỹ thuật tới sau hai mươi phút, cuộn danh sách lịch sử báo động,
tìm ra dòng thứ ba mươi tám: *"Áp suất khí thấp"*. Mọi dòng còn lại là **hệ quả** — timeout của từng
xy-lanh, lỗi từng bước, cảnh báo từng trạm.

Một sự cố. Bốn mươi bảy dòng. Hai mươi phút để tìm ra dòng có ích.

> ⭐ **Hệ báo động đó không thất bại vì thiếu thông tin — nó thất bại vì thừa.**

Chương này về việc thiết kế giao diện cho **người**, và phần lớn nội dung xoay quanh việc **bớt đi**
chứ không phải thêm vào.

---

## 44.2 Phân cấp màn hình

Người vận hành cần thông tin ở nhiều mức chi tiết khác nhau, tuỳ tình huống. Bốn mức là cấu trúc
thông dụng và đủ dùng:

| Mức | Nội dung | Trả lời câu hỏi |
|---|---|---|
| **1 — Tổng quan** | Cả máy trên một màn hình: trạng thái, sản lượng, cảnh báo đang có | *"Máy đang ổn không?"* |
| **2 — Cụm** | Một trạm hoặc một hệ thống con | *"Trạm 1 đang làm gì?"* |
| **3 — Chi tiết** | Từng cơ cấu, từng giá trị | *"Van kẹp có đang được lệnh không?"* |
| **4 — Chẩn đoán** | ⭐ Trạng thái I/O, biến trình tự, lịch sử | *"Vì sao nó không chạy?"* |

> ⭐ **Quy tắc: từ mức 1, người vận hành phải đi tới thông tin cần thiết trong ít bước nhất.**
> Khi máy dừng vì mất khí, màn hình tổng quan phải **chỉ thẳng** vào đó — không bắt người ta đi tìm
> qua bốn màn hình.

### ⭐ Màn hình tổng quan nên có gì

| Thành phần | Vì sao |
|---|---|
| **Trạng thái máy** — bằng chữ, to, rõ | `Đang chạy` / `Chờ hàng` / `Lỗi` / `Chờ về gốc` (Chương 25) |
| ⭐ **Cảnh báo cần xử lý ngay** — chỉ những cái đó | Không phải toàn bộ danh sách |
| **Sản lượng ca**: OK, NG, tỉ lệ | Chương 18 |
| ⭐ **Điều kiện đang thiếu để chạy** | Xem bên dưới |
| Công thức đang chạy — **tên**, không chỉ mã số | Chương 29 |
| Trạng thái kết nối: MES, đầu đọc, servo | Chương 40, 42 |

> ⭐⭐ **"Điều kiện đang thiếu để chạy" là thành phần có giá trị nhất của màn hình tổng quan, và hay
> bị bỏ nhất.**
>
> Khi người vận hành nhấn Start mà máy không chạy, câu hỏi duy nhất của họ là **"thiếu cái gì?"**.
> Chương trình đã có câu trả lời — đó chính là biểu thức `M_CanStart` mà bạn đã xây dần qua các chương
> (Chương 40, mục 40.9).
>
> Hiển thị từng điều kiện với dấu ✓ hoặc ✗ biến một cuộc gọi kỹ thuật thành một cái liếc mắt. Đây là
> lý do Chương 24 mục 24.7 khuyên **viết đủ từng điều kiện thay vì gom vào cờ tổng**.

```text
   ┌─ ĐIỀU KIỆN CHẠY ─────────────────┐
   │  ✓ Đã về gốc                     │
   │  ✓ Đã nạp công thức: BOARD-B     │
   │  ✗ Áp suất khí          ← THIẾU  │
   │  ✓ Dừng khẩn cấp OK              │
   │  ✓ Cửa đóng                      │
   │  ✓ Nhiệt độ keo: 60,2 °C         │
   └──────────────────────────────────┘
```

---

## 44.3 ⭐⭐ Thiết kế báo động

Đây là mục quan trọng nhất chương. Chương 48 mục 48.6 đã nêu phép thử một dòng; ở đây là thiết kế đầy
đủ.

### Phép thử cho mọi báo động

> **Mỗi báo động phải ứng với một hành động mà người vận hành cần làm, và phải còn đủ thời gian để
> làm việc đó.**
>
> Thiếu một trong hai vế thì nó **không phải báo động** — hãy đưa xuống mức ghi nhận.

Áp phép thử này lên danh sách của bạn, và một phần lớn sẽ rớt. ⭐ **Đó là kết quả tốt.**

### Ba mức, không nhiều hơn

| Mức | Nghĩa | Người vận hành làm gì |
|---|---|---|
| 🔴 **Báo động** *(alarm)* | Máy dừng hoặc sắp dừng; cần xử lý **ngay** | Xử lý ngay |
| 🟡 **Cảnh báo** *(warning)* | Bất thường, máy vẫn chạy | Lên kế hoạch xử lý |
| ⚪ **Ghi nhận** *(event)* | Thông tin, không cần hành động | ⭐ **Không hiện trên màn hình chính** |

> ⚠ **Đừng tạo năm, sáu mức ưu tiên.** Người vận hành không phân biệt được "mức 3" với "mức 4" lúc
> đang vội. Ba mức là đủ, và ranh giới giữa chúng phải rõ ràng.

### ⭐⭐ Chống lụt báo động

Cỗ máy ở mục 44.1 gặp **lụt báo động** *(alarm flood)*: một sự cố gốc kéo theo hàng chục báo động hệ
quả.

Ba kỹ thuật, dùng kết hợp:

**1. Ức chế báo động hệ quả**

```iecst
// ⭐ Mất khí là NGUYÊN NHÂN GỐC — ức chế mọi timeout cơ cấu khí nén
M_SuppressPneumaticAlarms := M_AirPressFault;

// Timeout xy-lanh chỉ báo khi KHÔNG phải do mất khí
IF T_Clamp1Timeout.Q AND NOT M_SuppressPneumaticAlarms THEN
    RaiseAlarm(ALM_CLAMP1_TIMEOUT);
END_IF;
```

> ⚠ **Ức chế phải có điều kiện rõ ràng và tự gỡ.** Ức chế tuỳ tiện là cách người ta vô hiệu hoá hệ
> báo động mà vẫn tưởng nó đang chạy.
>
> ⭐ **Và vẫn ghi báo động bị ức chế vào nhật ký**, kể cả khi không hiển thị. Lúc điều tra, thứ tự các
> sự kiện mới là dữ liệu quý.

**2. Báo động đầu tiên**

Ghi lại và làm nổi bật **báo động xuất hiện đầu tiên** trong một chuỗi. Nó gần như luôn là nguyên
nhân gốc.

```iecst
IF NOT M_AnyAlarmActive AND M_NewAlarm THEN
    FirstAlarmCode := NewAlarmCode;              // ⭐ nguyên nhân gốc
    FirstAlarmTime := CurrentTime;
END_IF;
```

**3. Trễ trước khi báo**

Nhiều báo động không cần báo ngay. Một tín hiệu dao động quanh ngưỡng, một mất kết nối thoáng qua —
chờ vài giây rồi mới báo sẽ loại được phần lớn báo giả (Chương 32, mục 32.6; Chương 38, mục 38.9).

### ⭐ Nội dung một dòng báo động

| Thành phần | Ví dụ | Vì sao |
|---|---|---|
| **Thời điểm** | `14:23:07` | Dựng lại chuỗi sự kiện |
| **Vị trí** | `Trạm 1` | Đi đâu |
| **Cái gì sai** | `Kẹp không lên` | Hiện tượng |
| ⭐ **Làm gì tiếp** | `Kiểm áp khí, kiểm cảm biến reed DI_Clamp1Up` | ⭐ Thành phần quan trọng nhất |
| Mức | 🔴 | Ưu tiên |

> ⭐⭐ **"Làm gì tiếp" là thứ phân biệt một hệ báo động dùng được với một hệ báo động chỉ để có.**
>
> `Lỗi 1042` không giúp gì. `Kẹp trạm 1 không lên trong 3 giây — kiểm áp khí, kiểm cảm biến reed
> DI_Clamp1Up` cho người vận hành hai chỗ để nhìn.
>
> Đây là cùng nguyên tắc với mã lý do khi từ chối công thức (Chương 29, mục 29.4) và với cửa sổ
> lực–vị trí (Chương 34, mục 34.5): **chẩn đoán, không chỉ phán quyết.**

### Xác nhận và lịch sử

| Việc | Yêu cầu |
|---|---|
| **Xác nhận** *(acknowledge)* | Người vận hành ghi nhận đã thấy. ⚠ **Không xoá được báo động khi nguyên nhân còn** |
| ⭐ **Xác nhận từng cái** | ⚠ Nút "xác nhận tất cả" khuyến khích chính hành vi ở mục 44.1 |
| **Lịch sử** | Lưu đủ dài để điều tra — ⭐ kèm **thời điểm chính xác** |
| Lọc và tìm | Theo thời gian, theo trạm, theo mức |

> ⚠ **Cân nhắc về nút "xác nhận tất cả".** Nó tiện khi có nhiều báo động, nhưng nó cũng làm người vận
> hành bỏ qua nội dung. Nếu hệ báo động được thiết kế tốt (ức chế hệ quả, ba mức rõ ràng) thì hiếm khi
> có nhiều dòng cùng lúc — và khi đó nút này ít cần thiết.

---

## 44.4 Phân quyền người dùng

| Cấp | Làm được gì |
|---|---|
| **Vận hành** | Chạy, dừng, xác nhận báo động, **chọn** công thức |
| **Kỹ thuật viên** | + Chạy tay, sửa tham số công thức trong dải, xem chẩn đoán |
| **Kỹ sư** | + Sửa dải hợp lệ, thêm công thức, ⚠ cưỡng bức I/O |
| **Bảo trì hệ thống** | + Cấu hình, quản lý người dùng |

⚠ Bốn nguyên tắc:

| Nguyên tắc | Vì sao |
|---|---|
| ⭐ **Tự đăng xuất** sau một thời gian không thao tác | Không thì mọi người dùng chung phiên của kỹ sư |
| ⭐ **Ghi vết** các thao tác quan trọng: ai, lúc nào, đổi gì | Chương 29, mục 29.6 |
| ⚠ **PLC vẫn phải tự kiểm** | Màn hình có thể bị thay, bị bỏ qua, hoặc lệnh đến từ hệ thống trên (Chương 29, mục 29.4) |
| ⚠ **Đừng để mật khẩu chung dán trên tủ** | Chuyện xảy ra ở mọi nhà máy khi phân quyền quá phiền |

> ⚠⚠ **Phân quyền quá chặt sẽ bị đi vòng.** Nếu người vận hành phải gọi kỹ sư mỗi lần đổi mã hàng lúc
> hai giờ sáng, thì trong vòng một tuần mật khẩu kỹ sư sẽ được dán trong tủ.
>
> Thiết kế phân quyền là bài toán **cân bằng**, không phải bài toán khoá càng nhiều càng tốt. Cùng
> tinh thần với Chương 29 mục 29.9 Bẫy 10 và Chương 42 mục 42.6: **một cơ chế mà người dùng đi vòng
> được thì không phải cơ chế bảo vệ.**

---

## 44.5 Nguyên tắc trình bày

| Nguyên tắc | Nội dung |
|---|---|
| ⭐ **Màu chỉ dùng khi có nghĩa** | Xem bên dưới |
| **Chữ đủ lớn** | Người vận hành đứng cách màn hình, có thể đeo kính bảo hộ |
| **Số kèm đơn vị** | ⭐ Luôn hiện đơn vị — Chương 32, mục 32.1 |
| **Số chữ số khớp độ chính xác** | ⚠ Chương 32, mục 32.3 |
| **Bố cục nhất quán** | Cùng vị trí cho cùng loại thông tin trên mọi màn hình |
| ⚠ **Nút nguy hiểm cần xác nhận hai bước** | Xoá sản lượng, cưỡng bức I/O, xoá công thức |
| **Trạng thái bằng chữ, không chỉ bằng màu** | ⚠ Xem bên dưới |

### ⭐ Màu chỉ dùng khi có nghĩa

> **Nếu mọi thứ đều có màu, thì màu không còn nói lên điều gì.**

Quy ước thực dụng:

| Màu | Chỉ dùng cho |
|---|---|
| 🔴 Đỏ | Báo động cần xử lý ngay |
| 🟡 Vàng | Cảnh báo |
| 🟢 Xanh lá | Trạng thái bình thường — ⚠ dùng **tiết chế** |
| Xám / trắng | Mọi thứ còn lại |

> ⭐ **Màn hình lúc bình thường nên chủ yếu là màu trung tính.** Khi có gì đó đỏ hoặc vàng, mắt người
> tìm thấy nó ngay.
>
> Màn hình đầy màu sắc trông "chuyên nghiệp" trong bản trình bày nhưng **vô dụng khi có sự cố**.

> ⚠ **Đừng chỉ dùng màu để truyền thông tin quan trọng.**
> Một phần người vận hành gặp khó khi phân biệt màu — thường là đỏ và xanh lá. Trạng thái phải đọc
> được **bằng chữ hoặc bằng ký hiệu**, màu chỉ là lớp bổ trợ.
>
> Đây cũng là lý do đèn tháp có **quy ước vị trí** ngoài quy ước màu (Chương 5, mục 5.6).

---

## 44.6 ⚠⚠ Ba điều HMI không được làm

### 1. Không chứa logic điều khiển

> ⚠⚠ **Logic điều khiển nằm trong PLC. HMI chỉ hiển thị và gửi lệnh.**

Nhiều hệ HMI có khả năng viết kịch bản. Cám dỗ là để nó làm một chút logic — "khi nhấn nút này thì
đặt biến kia rồi chờ 2 giây rồi đặt biến nọ".

Bốn lý do đừng:

| Lý do | Giải thích |
|---|---|
| ⭐ **HMI có thể mất kết nối** | Khi đó nửa logic của máy biến mất, và máy ở trạng thái nào thì không ai biết |
| **HMI không có tính tất định** | Nó chạy trên hệ điều hành thường (Chương 2, mục 2.2) |
| ⭐ **Logic nằm hai chỗ** | Người bảo trì đọc chương trình PLC sẽ **không thấy** phần đó (Chương 22) |
| **HMI dễ bị thay** | Đổi màn hình là mất logic |

> ⭐ **Phép thử: rút cáp mạng của HMI ra. Máy phải tiếp tục chạy chu trình hiện tại một cách an toàn.**
> Nếu không, bạn đã đặt logic sai chỗ.

### 2. Không thực hiện chức năng an toàn

> ⚠⚠ **Nút dừng khẩn cấp trên màn hình cảm ứng KHÔNG phải nút dừng khẩn cấp.**

| Lý do | Giải thích |
|---|---|
| Phụ thuộc HMI còn sống, mạng còn thông, phần mềm chưa treo | Ba thứ đều có thể hỏng |
| Không được chứng nhận cho chức năng an toàn | Chương 47 |
| ⚠ Người dùng có thể **tin nhầm** rằng nó là nút dừng khẩn | Đây mới là nguy hiểm nhất |

Dừng khẩn cấp là **nút cứng, tiếp điểm NC, đi vào mạch an toàn** (Chương 3, mục 3.6; Chương 47).

> ⚠ Một nút "Dừng" mềm trên màn hình là **hợp lệ và hữu ích** — nhưng nó là dừng vận hành bình thường,
> phải **trông khác hẳn** nút dừng khẩn, và không được đặt tên gây hiểu nhầm.

### 3. Không phải nơi lưu trữ chính

Dữ liệu quan trọng — sản lượng, công thức đang chạy, trạng thái — phải nằm ở PLC hoặc ở hệ thống trên.
HMI hỏng thì không được mất chúng (Chương 54).

---

## 44.7 Trên máy mẫu DP-01

### Sơ đồ màn hình

```text
   ┌─ MỨC 1: TỔNG QUAN ─────────────────────────────┐
   │  Trạng thái · Sản lượng · Báo động · ĐK chạy   │
   └──┬─────────────┬──────────────┬────────────────┘
      │             │              │
   ┌──▼──────┐  ┌───▼──────┐  ┌────▼────────┐
   │ MỨC 2   │  │ MỨC 2    │  │ MỨC 2       │
   │ Trạm 1  │  │ Trạm 2   │  │ Công thức   │
   │ tra keo │  │ sấy UV   │  │ (Chương 29) │
   └──┬──────┘  └───┬──────┘  └─────────────┘
      │             │
   ┌──▼─────────────▼──────────────────────────┐
   │ MỨC 3: chi tiết cơ cấu, giá trị analog     │
   └──┬─────────────────────────────────────────┘
      │
   ┌──▼─────────────────────────────────────────┐
   │ ⭐ MỨC 4: CHẨN ĐOÁN                         │
   │  I/O · biến bước · lịch sử báo động         │
   │  trạng thái kết nối · số liệu xu hướng      │
   └────────────────────────────────────────────┘
```

### Màn hình chẩn đoán — thứ đáng đầu tư nhất

> ⭐ **Màn hình mức 4 là màn hình tiết kiệm nhiều thời gian nhất, và hay bị cắt nhất khi dự án gấp.**

Nội dung nên có, gom từ các chương:

| Nhóm | Nội dung | Chương |
|---|---|---|
| ⭐ **Biến bước từng trạm** | Số bước hiện tại, **tên bước bằng chữ** | 20 mục 20.6, 26 |
| **Trạng thái I/O** | Tất cả DI/DO, có tên đọc được | 22 |
| ⭐ **Số liệu xu hướng** | Chu kỳ, nhiệt độ, cường độ UV, dòng chuyền theo thời gian | 35, 36, 55 |
| **Trạng thái kết nối** | MES, đầu đọc, servo, bộ điều khiển nhiệt | 38, 40, 42 |
| ⭐ **So với mốc nghiệm thu** | Dòng chuyền, cường độ UV, chu kỳ — so với giá trị ghi lúc chạy thử | 36 mục 36.8, 52 |
| **Lịch sử báo động** | Có lọc, có thời điểm chính xác | Mục 44.3 |
| Đếm thời gian chờ chuyền | Chờ máy trước, chờ máy sau | 41 mục 41.8 |

> ⭐ **"Tên bước bằng chữ" giải quyết đúng vấn đề nêu ở Chương 20 mục 20.6.**
> Trình tự viết bằng `CASE` trong ST khó đọc với người bảo trì quen ladder. Nhưng nếu màn hình hiện
> **"Trạm 1 — bước 20: nâng kẹp, chờ DI_Clamp1Up"**, thì họ chẩn đoán được **mà không cần mở phần mềm
> lập trình**.
>
> Đây là một trong bốn biện pháp giảm thiệt hại ở Chương 20 mục 20.6, và là biện pháp hiệu quả nhất.

### Ức chế báo động trên DP-01

Áp mục 44.3 vào máy mẫu:

| Nguyên nhân gốc | Ức chế những gì |
|---|---|
| ⭐ **Mất khí** (`M_AirPressFault`) | Mọi timeout xy-lanh: chặn, kẹp, cửa chắn UV |
| **Dừng khẩn cấp** | Mọi timeout chuyển động và timeout bước |
| **Mất kết nối servo** | Timeout gantry, lỗi vị trí |
| **Mất kết nối MES** | Không ức chế gì — nhưng ⚠ **chỉ báo một lần**, không báo mỗi board |

> ⚠ **Hàng cuối đáng chú ý.** Với chu kỳ 12 giây, mất kết nối MES mà báo mỗi board sẽ tạo ra **300
> dòng mỗi giờ**. Một dòng khi mất, một dòng khi khôi phục — đủ.

---

## 44.8 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| Loại thiết bị | **Màn hình HMI** chuyên dụng · **SCADA** trên PC · **giao diện web** trong PLC |
| Liên kết tag | Trực tiếp với PLC cùng hãng thì dễ; ⚠ khác hãng thì qua giao thức chung (Chương 39, 40) |
| ⚠ Khả năng viết kịch bản | Có ở phần lớn hệ — ⚠ **và đó là cám dỗ đặt logic sai chỗ** (mục 44.6) |
| Lưu lịch sử báo động | Trong HMI, trên thẻ nhớ, hoặc gửi lên hệ thống trên. ⚠ Kiểm dung lượng và thời gian lưu |
| Phân quyền | Có sẵn ở phần lớn hệ; ⚠ **PLC vẫn phải tự kiểm** (mục 44.4) |
| Đồ thị xu hướng | ⭐ Có ở phần lớn hệ — **dùng nó**, rất hữu ích cho chẩn đoán (Chương 35, mục 35.10) |
| ⚠ Sao lưu dự án HMI | **Phải nằm trong bản sao lưu chung** cùng chương trình PLC (Chương 54) |

> ⚠ **Dự án HMI là một tài sản riêng, dễ bị quên khi sao lưu.** Mất nó nghĩa là phải vẽ lại toàn bộ
> màn hình. Đây là hạng mục bắt buộc trong danh sách sao lưu (Chương 30, mục 30.6; Chương 54).

---

## 44.9 Bẫy thường gặp

### 🔍 BẪY 1 — Lụt báo động

**Hiện tượng:** ⭐ đúng cỗ máy ở mục 44.1 — 47 dòng cho một sự cố; người vận hành xác nhận tất cả rồi
thử lại.
**Cách sửa:** ức chế báo động hệ quả · ghi **báo động đầu tiên** · trễ trước khi báo (mục 44.3).

### 🔍 BẪY 2 — Báo động không nói làm gì tiếp

**Hiện tượng:** `Lỗi 1042` — người vận hành gọi kỹ thuật vì không biết bắt đầu từ đâu.
**Cách sửa:** ⭐ mỗi dòng phải có **vị trí, hiện tượng, và việc cần kiểm** (mục 44.3).

### 🔍 BẪY 3 — Không hiển thị điều kiện đang thiếu

**Hiện tượng:** nhấn Start, máy không chạy, không ai biết vì sao — trong khi chương trình **đã có câu
trả lời**.
**Cách sửa:** ⭐⭐ hiển thị từng điều kiện của `M_CanStart` với ✓/✗ (mục 44.2).

### 🔍 BẪY 4 — Đặt logic điều khiển trong HMI

**Hiện tượng:** ⚠⚠ mất kết nối HMI → nửa logic biến mất; và người bảo trì đọc chương trình PLC
**không thấy** phần đó.
**Cách sửa:** phép thử rút cáp ở mục 44.6.

### 🔍 BẪY 5 — Nút dừng khẩn cấp trên màn hình cảm ứng

**Hiện tượng:** ⚠⚠ người dùng **tin nhầm** rằng nó là nút dừng khẩn — và nó không hoạt động khi HMI
treo hoặc mất mạng.
**Cách sửa:** dừng khẩn là **nút cứng vào mạch an toàn** (mục 44.6, Chương 47).

### 🔍 BẪY 6 — Màu dùng khắp nơi

**Hiện tượng:** khi có sự cố, mắt không tìm được thông tin quan trọng giữa một màn hình đầy màu.
**Cách sửa:** màn hình bình thường chủ yếu **trung tính**; màu dành cho ý nghĩa (mục 44.5).

### 🔍 BẪY 7 — Chỉ dùng màu để truyền trạng thái

**Hiện tượng:** người vận hành khó phân biệt màu không đọc được trạng thái.
**Cách sửa:** trạng thái bằng **chữ hoặc ký hiệu**, màu là lớp bổ trợ (mục 44.5).

### 🔍 BẪY 8 — Phân quyền quá chặt

**Hiện tượng:** ⚠ mật khẩu kỹ sư dán trong tủ trong vòng một tuần.
**Cách sửa:** cân bằng — người vận hành phải làm được việc thường ngày của họ (mục 44.4).

### 🔍 BẪY 9 — Không hiển thị tên bước trình tự

**Hiện tượng:** người bảo trì phải **mở phần mềm lập trình** để biết máy đang kẹt ở bước nào.
**Cách sửa:** ⭐ hiển thị số bước **và tên bước** trên màn hình chẩn đoán (mục 44.7, Chương 20).

### 🔍 BẪY 10 — Báo động lặp lại mỗi chu kỳ

**Hiện tượng:** mất kết nối MES báo 300 dòng mỗi giờ; lịch sử báo động thành vô dụng.
**Cách sửa:** báo **một lần khi xảy ra**, một lần khi khôi phục (mục 44.7).

### 🔍 BẪY 11 — Không sao lưu dự án HMI

**Hiện tượng:** HMI hỏng, thay cái mới, và **phải vẽ lại toàn bộ màn hình**.
**Cách sửa:** dự án HMI nằm trong bản sao lưu chung (mục 44.8, Chương 54).

### 🔍 BẪY 12 — Cắt màn hình chẩn đoán khi dự án gấp

**Hiện tượng:** tiết kiệm được vài ngày lúc làm, mất nhiều hơn thế mỗi lần máy hỏng trong mười năm
sau.
**Cách sửa:** ⭐ màn hình mức 4 là hạng mục **đáng đầu tư nhất** (mục 44.7).

---

## 44.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Bốn mức màn hình | Tổng quan · cụm · chi tiết · ⭐ **chẩn đoán** |
| ⭐⭐ Thành phần giá trị nhất của màn tổng quan | **Điều kiện đang thiếu để chạy**, có ✓/✗ |
| Phép thử cho mọi báo động | ⭐ **Có hành động cần làm** và **còn đủ thời gian** để làm |
| Bao nhiêu mức báo động | **Ba** — báo động, cảnh báo, ghi nhận |
| Chống lụt báo động | Ức chế hệ quả · ghi **báo động đầu tiên** · trễ trước khi báo |
| Ức chế phải | Có điều kiện rõ ràng, **tự gỡ**, và ⭐ **vẫn ghi vào nhật ký** |
| Thành phần quan trọng nhất của một dòng báo động | ⭐⭐ **Làm gì tiếp** |
| Xác nhận báo động | ⚠ **Không xoá được** khi nguyên nhân còn |
| Phân quyền quá chặt thì | ⚠ **Bị đi vòng** — mật khẩu dán trong tủ |
| Dù có phân quyền HMI | ⚠ **PLC vẫn phải tự kiểm** |
| Màu | ⭐ **Chỉ dùng khi có nghĩa**; trạng thái phải đọc được bằng chữ |
| ⚠⚠ HMI không được | Chứa **logic điều khiển** · làm **chức năng an toàn** · là **nơi lưu trữ chính** |
| Phép thử logic đặt đúng chỗ | ⭐ **Rút cáp HMI — máy phải chạy tiếp an toàn** |
| Nút dừng khẩn trên màn cảm ứng | ❌ **Không phải dừng khẩn cấp** |
| Màn hình chẩn đoán nên có | ⭐ **Tên bước bằng chữ** · I/O · xu hướng · so với **mốc nghiệm thu** |
| Dự án HMI | ⚠ Nằm trong **bản sao lưu chung** |

---

## 44.11 Tự kiểm

1. ⭐ Mô tả sự cố ở mục 44.1. Vì sao nói hệ báo động đó thất bại vì **thừa** thông tin?
2. Kể bốn mức màn hình và câu hỏi mà mỗi mức trả lời.
3. ⭐⭐ Thành phần nào của màn hình tổng quan có giá trị nhất và hay bị bỏ nhất? Nó liên hệ với biểu
   thức nào trong chương trình, và với nguyên tắc nào ở Chương 24?
4. Phát biểu phép thử cho mọi báo động. Điều gì xảy ra khi áp nó lên một danh sách có sẵn?
5. ⭐ Nêu ba kỹ thuật chống lụt báo động. Ức chế phải thoả ba điều kiện gì?
6. Vì sao vẫn phải **ghi vào nhật ký** những báo động đã bị ức chế?
7. ⭐ Nêu năm thành phần của một dòng báo động. Thành phần nào quan trọng nhất và vì sao?
8. Vì sao phân quyền **quá chặt** lại phản tác dụng? Liên hệ với hai bẫy ở các chương khác.
9. ⭐ Nêu bốn lý do **không** đặt logic điều khiển trong HMI. Phép thử để kiểm là gì?
10. ⚠⚠ Vì sao nút dừng khẩn cấp trên màn hình cảm ứng **không phải** dừng khẩn cấp? Lý do nào nguy
    hiểm nhất?
11. Vì sao **màu không được là cách duy nhất** truyền trạng thái?
12. ⭐ Vì sao hiển thị **tên bước bằng chữ** trên màn hình chẩn đoán lại quan trọng? Nó giải quyết vấn
    đề nêu ở chương nào?

> Câu 3, 5, 9 và 10 là bốn câu phân loại. Câu 1 là tinh thần của cả chương: **thiết kế giao diện vận
> hành phần lớn là việc BỚT ĐI — bốn mươi bảy dòng báo động cho một sự cố không phải là nhiều thông
> tin, mà là không có thông tin nào.**

---

### Chương tiếp theo

Chương 45 — **An ninh mạng cho hệ điều khiển**. Máy của bạn đã nối với mạng, với hệ thống trên, và
có màn hình vận hành. Chương sau về việc bảo vệ nó — **nguyên lý phòng thủ, không phải hướng dẫn tấn
công** — và về một thực tế khó chịu: phần lớn giao thức công nghiệp không có bảo mật nào.

### Nguồn tham khảo chương 44

- **IEC 62682** — *Management of alarm systems for the process industries*: vòng đời báo động, phép
  thử "mỗi báo động phải có hành động ứng phó", ức chế, và xử lý lụt báo động — nền cho mục 44.3.
  *(tiêu chuẩn có bản quyền; đây là bản quốc tế tương ứng của ANSI/ISA-18.2)*
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu với thiết bị chỉ
  báo, màu sắc, và ⚠ **chức năng dừng khẩn cấp** — nền cho mục 44.6.
- **Tài liệu hệ HMI/SCADA** đang dùng — dùng cho liên kết tag, phân quyền, lưu lịch sử, và ⚠ **cách
  sao lưu dự án**.
- Bảng I/O, bảng công thức và số liệu đã chốt của DP-01 — Phụ lục J.

> ⚡ Việc chia **ba mức báo động** ở mục 44.3 và **bốn mức màn hình** ở mục 44.2 là **cấu trúc thực
> dụng thường dùng**, không phải quy định cứng của tiêu chuẩn. Một số ngành và một số đơn vị có quy
> định riêng về số mức ưu tiên và về nội dung bắt buộc của bản ghi báo động — ⭐ **quy định của cơ sở
> và của ngành luôn thắng** nội dung chương này.
>
> ⚠ Trong các ngành có **yêu cầu pháp lý về hồ sơ điện tử** — dược phẩm, thiết bị y tế — thì yêu cầu
> về ghi vết thao tác, chữ ký điện tử và lưu trữ lịch sử chặt hơn nhiều so với mục 44.4. Kiểm quy định
> áp dụng cho sản phẩm của khách hàng.
