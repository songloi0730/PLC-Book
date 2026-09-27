# Chương 37 — Điều khiển chuyển động servo

> **Lát cắt máy mẫu:** 3 — thêm analog (áp suất, nhiệt độ, cường độ UV) và trục gantry XY+Z servo.

---

## 37.1 Bài toán: trục Z đâm xuống board

Gantry của DP-01 đang tra keo. Đầu keo chạy theo đường trong công thức, cách mặt board vài mi-li-mét.

Một sáng, sau khi kỹ thuật viên sửa một lỗi khác và nạp lại chương trình, trục Z **đâm thẳng xuống**
board và làm gãy đầu tra keo.

Nguyên nhân: chương trình có **giới hạn phần mềm** cho trục Z — không cho đi quá 50 mm. Giới hạn đó
được so với **vị trí hiện tại** của trục. Nhưng sau khi nạp lại chương trình, trục **chưa về gốc**,
nên vị trí hiện tại là một con số vô nghĩa. Lệnh "đi tới 45 mm" được tính từ một gốc sai.

Giới hạn phần mềm hoạt động đúng như nó được viết. Nó chỉ **không biết** rằng con số nó đang bảo vệ
là con số rác.

> ⭐ **Bài học trung tâm của cả chương:**
> **Giới hạn phần mềm bảo vệ chống lỗi lập trình. Nó không bảo vệ chống việc hệ toạ độ bị sai.**
> Thứ bảo vệ được điều đó là **công tắc giới hạn phần cứng** — và nó phải đi thẳng vào driver, không
> qua PLC.

---

## 37.2 Servo khác biến tần ở đâu

Chương 36 cho bạn biến tần: điều khiển **tốc độ**. Servo điều khiển **vị trí**.

| | **Biến tần + động cơ thường** | **Servo** |
|---|---|---|
| Điều khiển | Tốc độ | ⭐ **Vị trí** (và tốc độ, mô-men) |
| Phản hồi vị trí | ⚠ Không có | ⭐ **Encoder gắn trên động cơ** |
| Vòng điều khiển | Một vòng tốc độ | ⭐ **Ba vòng lồng nhau**: vị trí → tốc độ → dòng |
| Biết mình đang ở đâu | ❌ Không | ✅ Có |
| Độ chính xác vị trí | Không đảm bảo | Cao |
| Giá | Thấp hơn | Cao hơn đáng kể |
| Dùng cho | Chuyền, quạt, bơm | Gantry, trục định vị, cấp phôi chính xác |

### Ba vòng lồng nhau

```text
   Lệnh vị trí ──►[ vòng VỊ TRÍ ]──► lệnh tốc độ ──►[ vòng TỐC ĐỘ ]──► lệnh dòng ──►[ vòng DÒNG ]──► động cơ
                        ▲                                ▲                              ▲
                        │                                │                              │
                   vị trí đo được                   tốc độ đo được                 dòng đo được
                        └──────────── encoder ───────────┘
```

> ⭐ **Cả ba vòng nằm trong servo drive, không nằm trong PLC.** Đây là điểm quan trọng nhất về mặt
> kiến trúc, và nó là hệ quả trực tiếp của cảnh báo ở Chương 35 mục 35.12 Bẫy 8 và Chương 36 mục 36.4:
>
> **Đừng viết PID vị trí trên PLC.** Drive chạy các vòng đó ở tần số hàng kHz — nhanh hơn vòng quét
> PLC vài bậc độ lớn. PLC **ra lệnh chuyển động** và **giám sát kết quả**; drive lo phần còn lại.

### ⚠ Sai số bám

Servo không bao giờ ở đúng vị trí lệnh trong lúc đang chạy — luôn có một khoảng chênh gọi là **sai số
bám** *(following error / lag)*. Đó là bình thường.

Cái không bình thường là **sai số bám vượt ngưỡng**: nghĩa là trục **không theo kịp lệnh** — vì tải
nặng bất thường, vì cơ cấu kẹt, vì đai trượt, hoặc vì tham số sai.

> ⭐ **Ngưỡng sai số bám là bộ phát hiện va chạm rẻ nhất bạn có.** Drive tự giám sát và báo lỗi khi
> vượt. Đặt ngưỡng hợp lý là một trong những việc quan trọng nhất khi cấu hình servo — quá rộng thì
> nó không bắt được gì, quá hẹp thì báo lỗi giả khi tăng tốc.

---

## 37.3 ⭐ Về gốc — và vì sao nó khó

**Về gốc** *(homing)* là việc thiết lập **hệ toạ độ**: nói cho trục biết "chỗ này là số 0".

### Vì sao cần

Encoder gia số *(incremental)* chỉ đếm được **đã đi bao xa**, không biết **đang ở đâu** (Chương 18,
mục 18.5). Mất điện là mất hệ toạ độ.

Encoder tuyệt đối *(absolute)* giữ được vị trí qua mất điện — nhưng ⚠ vẫn cần về gốc **một lần** khi
lắp máy, để gắn hệ toạ độ của encoder vào hệ toạ độ cơ khí của máy.

### Các kiểu tìm gốc

| Kiểu | Cách làm | ✅ Mạnh | ⚠ Yếu |
|---|---|---|---|
| **Chạm cữ giới hạn** | Chạy tới khi công tắc giới hạn tác động | Đơn giản, không cần thêm cảm biến | Độ lặp lại kém; ⚠ dùng cữ an toàn làm cữ gốc là **trộn hai chức năng** |
| **Cảm biến gốc riêng** | Chạy tới khi cảm biến gốc tác động | Tách chức năng rõ ràng | Độ lặp lại phụ thuộc cảm biến và tốc độ |
| ⭐ **Cảm biến gốc + xung Z** | Tìm cảm biến gốc, rồi chạy chậm tới **xung Z** đầu tiên của encoder | ⭐ **Độ lặp lại rất cao** — xung Z là mốc cơ khí chính xác | Cần encoder có kênh Z |
| **Chạm cữ cứng** *(hard stop)* | Chạy vào vật cản cơ khí, phát hiện bằng mô-men tăng | Không cần cảm biến nào | ⚠ Va chạm có kiểm soát — không hợp với cơ cấu mảnh |
| **Encoder tuyệt đối** | Đọc thẳng vị trí | ⭐ Không cần chạy về gốc mỗi lần bật máy | Đắt hơn; vẫn cần đặt gốc một lần khi lắp |

> 💡 **Kiểu "cảm biến gốc + xung Z" là mặc định tốt cho trục cần chính xác.**
> Cảm biến gốc cho biết đang ở gần vùng gốc; xung Z cho mốc chính xác. Độ lặp lại đạt tới mức phân
> giải của encoder, và nó **không phụ thuộc tốc độ chạy về gốc**.

### ⚠ Bốn điều bắt buộc trong trình tự về gốc

| Điều | Vì sao |
|---|---|
| ⭐ **Về gốc phải chạy CHẬM** | Nếu trục đang ở phía sai của cữ, nó sẽ đi nhầm hướng — chậm thì dừng kịp |
| ⭐ **Có timeout** | Cữ hỏng hoặc dây đứt thì trục chạy mãi tới khi đâm vào cữ cứng (Chương 17, Chương 26) |
| ⭐ **Thứ tự trục có thể quan trọng** | Trên gantry, ⚠ **Z phải lên trước** X và Y — nếu không thì đầu tra keo quét ngang qua board |
| **Cờ "đã về gốc" phải xoá khi mất điện** | ⚠⚠ Xem cảnh báo bên dưới |

> ⚠⚠ **NGUY HIỂM — cờ "đã về gốc" tuyệt đối không được giữ qua mất điện.**
> Đây là ứng dụng trực tiếp của quy tắc ở Chương 16 mục 16.4. Nếu `M_Homed` là biến giữ được, thì sau
> khi mất điện máy **tin rằng nó biết mình đang ở đâu** — trong khi trục có thể đã bị tay người đẩy
> đi, hoặc tụt xuống do trọng lực.
>
> Đúng cỗ máy ở mục 37.1: hệ toạ độ sai, giới hạn phần mềm vô dụng, và lệnh chuyển động đưa trục tới
> chỗ không ai muốn.
>
> **`M_Homed` phải là biến KHÔNG giữ, và mọi lệnh chuyển động tuyệt đối phải kiểm nó.**

---

## 37.4 Các kiểu lệnh chuyển động

| Lệnh | Nghĩa | Dùng khi |
|---|---|---|
| **Tuyệt đối** *(absolute)* | Đi tới toạ độ X = 45,0 mm | ⭐ Phần lớn trường hợp — vị trí xác định trong hệ toạ độ |
| **Tương đối** *(relative)* | Đi thêm 10 mm từ chỗ đang đứng | Bước lặp, dịch chuyển nhỏ |
| **Chạy chậm** *(jog)* | Chạy liên tục khi giữ nút, dừng khi nhả | Chỉnh tay, dạy vị trí |
| **Về gốc** *(home)* | Trình tự tìm gốc | Sau khi bật máy, sau lỗi |
| **Dừng** *(stop / halt)* | Dừng có kiểm soát theo dốc giảm tốc | Dừng bình thường |

> ⚠ **Lệnh tuyệt đối chỉ có nghĩa khi đã về gốc.** Lệnh tương đối thì không cần — nhưng ⚠ **sai số
> tích luỹ**: mỗi lệnh tương đối cộng thêm một chút sai lệch, và sau nhiều lần thì vị trí trôi đi.
>
> Quy tắc: **dùng tuyệt đối bất cứ khi nào có thể**. Tương đối chỉ cho những dịch chuyển thật sự có
> nghĩa "thêm một khoảng".

### ⚠ Jog là chế độ nguy hiểm

Chạy chậm là lúc **người đứng gần máy nhất** và **cơ cấu chuyển động dưới điều khiển trực tiếp**.

| Yêu cầu | Vì sao |
|---|---|
| **Tốc độ jog phải chậm** | Người phải kịp phản ứng |
| ⭐ **Chỉ chạy khi giữ nút** — nhả là dừng | Không có chế độ "chạy liên tục" khi jog |
| **Giới hạn phần mềm vẫn phải hoạt động** | ⚠ Đây là chỗ hay bị bỏ qua "cho tiện" |
| **Chỉ ở chế độ Manual**, có điều kiện cho phép | Chương 28 |
| ⚠ Nếu chưa về gốc thì jog thế nào | Xem bên dưới |

> ⚠⚠ **Jog khi chưa về gốc là tình huống phải thiết kế có chủ đích.**
> Chưa về gốc nghĩa là **giới hạn phần mềm không dùng được** (mục 37.1). Nhưng bạn *cần* jog được khi
> chưa về gốc — chính là để đưa trục ra khỏi vị trí kẹt trước khi về gốc.
>
> Cách thường dùng: cho phép jog khi chưa về gốc, nhưng **tốc độ rất chậm**, và ⭐ **dựa hoàn toàn vào
> công tắc giới hạn phần cứng** để bảo vệ. Đây là lý do nữa cho mục 37.6.

---

## 37.5 Biên dạng vận tốc

Trục không thể đi từ 0 tới tốc độ đặt tức thì — gia tốc vô hạn cần lực vô hạn. Chuyển động thật đi
theo một **biên dạng vận tốc** *(velocity profile)*.

### Hình thang

```text
   tốc độ
     ▲
     │      ┌──────────────────┐
     │     ╱                    ╲
     │    ╱                      ╲
     │   ╱                        ╲
     └──┴──────────────────────────┴──► thời gian
        tăng tốc    tốc độ đều    giảm tốc
```

Ba tham số: **tốc độ**, **gia tốc**, **giảm tốc**. Đây là biên dạng mặc định và đủ cho phần lớn ứng
dụng.

### Làm mượt

Biên dạng hình thang có **gia tốc thay đổi đột ngột** ở hai điểm gãy. Đạo hàm của gia tốc gọi là
**giật** *(jerk)*, và ở hai điểm đó nó vô hạn về lý thuyết.

Hậu quả thực tế: **rung cơ khí** ở đầu và cuối mỗi chuyển động. Với gantry mang đầu tra keo, rung
nghĩa là đường keo không đều ở đoạn đầu.

**Biên dạng chữ S** *(S-curve)* làm tròn hai góc — gia tốc tăng dần thay vì nhảy bậc:

| | Hình thang | Chữ S |
|---|---|---|
| Thời gian di chuyển | ⭐ Ngắn hơn | Dài hơn một chút |
| Rung cơ khí | ⚠ Nhiều hơn | ⭐ Ít hơn hẳn |
| Hao mòn cơ cấu | Nhiều hơn | Ít hơn |
| Cấu hình | Ba tham số | Thêm tham số giật |

> 💡 **Với gantry tra keo, chữ S thường đáng giá** — chất lượng đường keo phụ thuộc chuyển động êm.
> Với trục chỉ đi từ điểm A tới điểm B rồi dừng hẳn, hình thang là đủ.
>
> ⚠ Chữ S làm **chu kỳ dài hơn**. Với DP-01 đang sát trần 12 giây (Phụ lục J §J.1), đây là đánh đổi
> phải đo, không đoán.

---

## 37.6 ⭐⭐ Giới hạn phần mềm không thay được giới hạn phần cứng

Đây là mục quan trọng nhất chương.

### Ba lớp bảo vệ

```text
   ┌─────────────────────────────────────────────────────────────┐
   │  Vùng làm việc bình thường          0 … 50 mm               │
   │  ┌───────────────────────────────────────────────────────┐  │
   │  │ 1. GIỚI HẠN PHẦN MỀM        −1 mm  và  51 mm          │  │
   │  │    trong PLC hoặc drive — chống lỗi lập trình         │  │
   │  └───────────────────────────────────────────────────────┘  │
   │  2. CÔNG TẮC GIỚI HẠN PHẦN CỨNG   −3 mm  và  53 mm         │
   │     ⭐ đi THẲNG vào drive — chống hệ toạ độ sai             │
   │  3. CỮ CƠ KHÍ CỨNG                −5 mm  và  55 mm         │
   │     ⭐ chống mọi thứ khác — kể cả drive hỏng                │
   └─────────────────────────────────────────────────────────────┘
```

| Lớp | Bảo vệ chống | ⚠ Không bảo vệ chống |
|---|---|---|
| **Giới hạn phần mềm** | Lỗi lập trình, công thức sai, người nhập nhầm | ⚠ **Hệ toạ độ sai** (chưa về gốc) · lỗi drive · lỗi encoder |
| **Công tắc giới hạn phần cứng** | Hệ toạ độ sai · lỗi lập trình · phần lớn lỗi drive | ⚠ Công tắc hỏng · dây đứt (nếu không dùng NC) |
| **Cữ cơ khí** | Mọi thứ còn lại | Không có gì — nhưng nó **làm hỏng cơ cấu** |

### ⭐ Vì sao công tắc giới hạn phải đi thẳng vào drive

> **Nếu công tắc giới hạn đi qua PLC, thì việc dừng phụ thuộc vào PLC đang chạy đúng.**
>
> Nhưng những tình huống bạn cần nó nhất lại chính là những tình huống PLC **không đáng tin**: chương
> trình sai, CPU đang STOP, vòng quét bị treo, hoặc ai đó đang cưỡng bức I/O (Chương 51).
>
> Drive có ngõ vào giới hạn riêng. Tín hiệu vào đó làm drive **dừng ngay lập tức**, không qua vòng
> quét, không qua chương trình. ⭐ **Đó là cả điểm của việc có nó.**

Ba yêu cầu đi kèm:

- ⭐ **Tiếp điểm NC** — đứt dây thì trục dừng (Chương 3, mục 3.6; Chương 15).
- **PLC vẫn nên đọc trạng thái công tắc** — để **biết** và báo lỗi rõ ràng. Nhưng việc **dừng** không
  phụ thuộc PLC.
- ⚠ **Đừng dùng công tắc giới hạn làm cữ gốc.** Trộn hai chức năng làm cả hai kém đi: gốc kém chính
  xác, và giới hạn bị tác động thường xuyên nên mòn nhanh.

> ⚠⚠ **Và nhắc lại điều quan trọng nhất: cả ba lớp trên đều KHÔNG phải chức năng an toàn cho người.**
> Chúng bảo vệ **cơ cấu**. Bảo vệ người khi trục chuyển động là việc của mạch an toàn, che chắn, và
> các chức năng an toàn của truyền động (Chương 47; Chương 36, mục 36.6).

---

## 37.6b ⭐⭐ Chức năng an toàn của truyền động — cả một họ, không chỉ STO

Mục 37.6 dựng ba lớp bảo vệ **cơ khí và logic**. Còn một lớp nữa nằm **bên trong chính bộ truyền
động**, và phần lớn người mới chỉ biết đúng một thành viên của nó: **STO**.

> ⚠⚠ **Mục này giới thiệu TỪ VỰNG, không thiết kế an toàn.** Chọn dùng chức năng nào, ở mức toàn vẹn
> nào, với kiến trúc nào — là kết quả của **đánh giá rủi ro do người có thẩm quyền thực hiện**
> (Chương 47). ⭐ Mục đích ở đây là để bạn **biết những gì tồn tại** mà hỏi cho đúng, thay vì mặc định
> rằng STO là lựa chọn duy nhất.

### Vì sao chỉ biết STO là không đủ

Chương 47 mục 47.8 đã cảnh báo hai điều STO **không** làm, và cảnh báo quan trọng nhất là:

> ⚠ **STO không hãm.** Động cơ ngừng sinh mô-men, nhưng tải có quán tính **trôi theo đà** — và trục
> đứng có tải treo thì **rơi**.

⭐ Câu hỏi tự nhiên tiếp theo là *"vậy dùng gì?"* — và câu trả lời nằm ở chỗ **có cả một họ chức năng
an toàn cho truyền động**, được định nghĩa trong tiêu chuẩn về truyền động điện *(IEC 61800-5-2)*.

### Bốn chức năng dừng — khác nhau ở chỗ nào

| Ký hiệu | Tên | Làm gì | ⭐ Trả lời tình huống |
|---|---|---|---|
| **STO** | *Safe torque off* | ⭐ **Cắt năng lượng sinh chuyển động** khỏi động cơ | Tải nhẹ, ma sát đủ giữ, hoặc đã có phanh cơ |
| ⭐ **SS1** | *Safe stop 1* | **Giảm tốc có kiểm soát, rồi mới STO** | ⭐⭐ Đúng câu trả lời cho *"tải có quán tính lớn"* |
| ⭐ **SS2** | *Safe stop 2* | Giảm tốc có kiểm soát, **rồi chuyển sang SOS** | Khi dừng xong vẫn phải **giữ nguyên vị trí** |
| ⭐⭐ **SOS** | *Safe operating stop* | ⭐ **Giữ trục đứng yên — vẫn còn mô-men** | ⚠ **Trục đứng có tải treo**; hoặc cần giữ vị trí giữa chu trình |

> ⭐⭐ **Khác biệt SS1 với SS2/SOS là khác biệt đáng nhớ nhất của cả mục này.**
>
> Cả hai đều giảm tốc có kiểm soát. Nhưng ⚠ **SS1 kết thúc bằng STO — hết mô-men**, còn ⭐ **SS2 kết
> thúc bằng SOS — còn mô-men để giữ chỗ**.
>
> ⚡ Với trục Z mang đầu công tác, chọn nhầm SS1 thay vì SS2 nghĩa là: máy dừng êm, đúng quy trình,
> **rồi trục rơi xuống** — vì sau khi giảm tốc xong thì mô-men bị cắt.

### Các chức năng giám sát — cho phép máy vẫn chạy, nhưng chạy trong giới hạn

| Ký hiệu | Tên | Giữ cho cái gì trong giới hạn |
|---|---|---|
| ⭐⭐ **SLS** | *Safely-limited speed* | **Tốc độ** không vượt ngưỡng |
| **SSR** | *Safe speed range* | Tốc độ nằm trong một **dải** |
| ⭐ **SLP** | *Safely-limited position* | **Vị trí** không vượt giới hạn |
| **SLI** | *Safely-limited increment* | Mỗi lần chỉ đi **một bước ngắn** |
| ⭐ **SDI** | *Safe direction* | Chỉ cho đi **một chiều** — chặn chiều không mong muốn |
| **SLA** · **SAR** | *Safely-limited / safe range acceleration* | **Gia tốc** |
| **SLT** · **STR** | *Safely-limited / safe range torque* | **Mô-men hoặc lực** |
| **SMT** | *Safe motor temperature* | **Nhiệt độ động cơ** |

Và ba chức năng **công bố tín hiệu** thay vì hạn chế:

| Ký hiệu | Tên | Công bố điều gì |
|---|---|---|
| **SSM** | *Safe speed monitor* | Tốc độ **đang dưới ngưỡng** hay không |
| **SCA** | *Safe cam* | Trục **đang trong một dải vị trí** hay không |
| ⭐ **SBC** | *Safe brake control* | ⭐⭐ Điều khiển **phanh ngoài** bằng tín hiệu an toàn — ⚠ đây là thứ đi cùng trục đứng |

> ⭐⭐ **SLS là chức năng đổi cách làm việc nhiều nhất, và đáng biết nhất với người lập trình.**
>
> Bài toán quen thuộc: **dạy điểm, căn chỉnh, gỡ kẹt** — những việc buộc người phải vào vùng máy
> trong khi trục cần **vẫn nhúc nhích được**. ⚠ Nếu chỉ có STO thì chỉ còn hai lựa chọn, và cả hai
> đều tệ: **cắt hẳn** (không làm được việc) hoặc **chạy đủ tốc độ** (không an toàn).
>
> ⭐ SLS mở ra lựa chọn thứ ba: **cho chạy, nhưng tốc độ bị chặn ở mức an toàn — và mức chặn đó do
> phần cứng an toàn giám sát, không do chương trình**. ⚡ Ghép thêm **SDI** thì còn giới hạn được cả
> chiều: chỉ cho đi **ra xa** người, không cho đi vào.
>
> ⚠ Nhưng nhắc lại: **ngưỡng tốc độ an toàn là con số của đánh giá rủi ro**, không phải con số người
> lập trình chọn (Chương 47).

### ⭐ Hai chỗ đặt chức năng an toàn — và hệ quả với người lập trình

| | **Trong chính bộ truyền động** *(safety drive)* | **Do một PLC an toàn giám sát** |
|---|---|---|
| Cách làm | ⭐ Drive có sẵn chức năng an toàn; nó tự chuyển giữa các chức năng bằng **máy trạng thái bên trong** | Bộ điều khiển an toàn giám sát nhiều trục ở một chỗ |
| ⭐ Được gì | Phản ứng nhanh nhất, ít dây; ⭐ **không phụ thuộc mạng** | ⭐ Nhìn được **toàn máy**, phối hợp nhiều trục theo vùng |
| ⚠ Mất gì | Cấu hình nằm **trong tham số drive** — ⚠ **dễ bị quên khi thay drive** (Chương 53, Chương 54) | Phức tạp hơn; phụ thuộc mạng an toàn |
| ⚠ Hệ quả với bạn | ⭐⭐ **Tham số an toàn của drive PHẢI nằm trong bản sao lưu** — nó không nằm trong tệp chương trình PLC | Dự án an toàn là **một dự án riêng**, sao lưu riêng |

> ⚠⚠ **Hàng cuối là hàng hay gây sự cố nhất, và nó thuộc về người lập trình PLC.**
>
> Thay một drive hỏng, nạp lại tham số từ bản lưu — nhưng bản lưu ấy **chỉ có tham số vận hành**,
> không có **tham số an toàn**. ⭐ Máy chạy bình thường, mọi thứ trông đúng, và ⚠⚠ **chức năng an
> toàn thì không còn như đã nghiệm thu** — không có báo động nào nói điều đó.
>
> ⭐ Vì vậy danh mục sao lưu ở Chương 54 phải ghi **tham số an toàn của từng drive** thành một mục
> riêng, và việc thay drive phải kèm **thử lại chức năng an toàn**, không chỉ thử chạy
> (Chương 52 mục 52.5).

---

## 37.7 Phối hợp nhiều trục

Gantry XY cần hai trục chạy **cùng lúc và phối hợp**, không phải lần lượt.

| Kiểu | Nghĩa | Dùng cho |
|---|---|---|
| **Chạy độc lập** | Mỗi trục đi riêng, tới đích lúc nào tuỳ | Di chuyển không cần đường đi cụ thể |
| ⭐ **Nội suy đường thẳng** *(linear interpolation)* | Hai trục phối hợp để đầu công tác đi theo **đường thẳng** | ⭐ Tra keo theo đường |
| **Nội suy cung tròn** *(circular interpolation)* | Đi theo cung | Đường keo bo góc |
| **Trục ảo** *(virtual axis)* | Một trục không có thật làm chuẩn cho các trục thật bám theo | Đồng bộ nhiều trục |
| **Cam điện tử** *(electronic cam)* | Trục bám theo một bảng quan hệ vị trí | Thay cơ cấu cam cơ khí |

> ⚠ **Chạy độc lập cho ra đường đi không đoán trước được.** Ra lệnh X đi 100 mm và Y đi 50 mm cùng
> lúc, đầu công tác đi theo một đường cong tuỳ thuộc tốc độ và gia tốc của từng trục — nó **không đi
> theo đường thẳng**.
>
> Với việc di chuyển trong không gian trống thì không sao. Với **tra keo theo đường** thì phải nội
> suy — nếu không, đường keo không đúng hình.

Cam điện tử và trục ảo nêu ở đây ở mức khái niệm; chúng thuộc về máy phức tạp hơn DP-01.

---

## 37.8 PLCopen Motion — và vì sao khối lệnh có `Execute` / `Done` / `Busy`

Chuyển động là việc **kéo dài nhiều vòng quét**. Một lệnh "đi tới 45 mm" mất vài trăm mili-giây tới
vài giây — trong khi vòng quét là vài mili-giây.

Điều đó tạo ra một vấn đề: **khối lệnh chuyển động không thể trả kết quả ngay**.

**PLCopen Motion** chuẩn hoá một mẫu giao diện cho khối chuyển động, và mẫu đó được các hãng dùng
rộng rãi:

| Chân | Nghĩa |
|---|---|
| `Execute` | ⭐ Kích bằng **cạnh lên** — bắt đầu lệnh |
| `Done` | Lệnh đã hoàn tất thành công |
| `Busy` | Đang thực hiện |
| `Active` | Đang thật sự điều khiển trục (khi nhiều lệnh xếp hàng) |
| `CommandAborted` | Bị lệnh khác chen ngang |
| `Error` + `ErrorID` | Lỗi, kèm mã |

```iecst
VAR
    MoveZ : MC_MoveAbsolute;
END_VAR

// ⭐ Execute kích bằng cạnh lên — giữ mức TRUE không phát lệnh mới
MoveZ(Axis     := AX_Z,
      Execute  := TrigMoveZ.Q,
      Position := RecipeDispenseHeightX100,
      Velocity := ZVelocity,
      Done     => M_ZMoveDone,
      Busy     => M_ZMoveBusy,
      Error    => M_ZMoveError);

// Chuyển bước bằng PHẢN HỒI THẬT — Done, không phải timer (Chương 17)
IF Stn1_Step = 40 AND M_ZMoveDone THEN
    Stn1_Step := 50;
END_IF;
```

> ⭐ **Mẫu `Execute`/`Done` chính là nguyên tắc trung tâm của Chương 17 và Chương 26, đóng gói sẵn:**
> ra lệnh, rồi **chờ phản hồi thật** thay vì chờ timer. Khối chuyển động cho bạn `Done` — hãy dùng
> nó, đừng đoán "chắc trục tới rồi".
>
> ⚠ Và vẫn cần **timeout song song** để báo lỗi nếu `Done` không bao giờ lên (Chương 17, mục 17.4).
> `Error` bắt được lỗi drive báo; timeout bắt được trường hợp **không có gì xảy ra cả**.

### ⚠ Ba chỗ dễ sai với khối chuyển động

| Sai | Hậu quả |
|---|---|
| **Giữ `Execute` ở mức TRUE** | Ở nhiều hệ, lệnh chỉ phát một lần ở cạnh lên; giữ mức thì lần sau không phát được |
| ⚠ **Dùng chung một thể hiện khối cho nhiều lệnh** | Cùng lỗi với Chương 14 mục 14.3 — mỗi lệnh một thể hiện riêng |
| **Không xử lý `CommandAborted`** | Lệnh bị chen ngang mà chương trình vẫn chờ `Done` → trình tự treo |

---

## 37.8b ⭐⭐ Sai lệch bám — tín hiệu chẩn đoán quan trọng nhất của servo

Đây là khái niệm nối thẳng tới bài toán mở đầu chương, và là thứ **phải giám sát trên mọi trục**.

### Nó là gì

Trong chế độ chạy đồng bộ theo vị trí, PLC **gửi vị trí đích** xuống driver theo từng chu kỳ, còn
encoder **gửi vị trí thật** ngược lên.

```text
   PLC  ──── vị trí lệnh ────►  Driver  ────►  Động cơ
    ▲                                            │
    └──────── vị trí thật (encoder) ─────────────┘

   Sai lệch bám  =  vị trí lệnh  −  vị trí thật
```

⭐ **Sai lệch này LUÔN tồn tại.** Động cơ có quán tính, driver có thời gian đáp ứng — trục không bao
giờ ở đúng chỗ lệnh bảo nó ở, nó luôn **bám theo sau** một chút.

| Sai lệch bám | Nghĩa |
|---|---|
| Nhỏ và ổn định | ⭐ **Bình thường** — trục đang bám tốt |
| ⭐ Tăng khi tăng tốc, giảm khi chạy đều | Bình thường — lớn nhất ở lúc gia tốc |
| ⚠ **Tăng dần theo thời gian** | Trục **không theo kịp** — quá tải, kẹt, hoặc chỉnh định sai |
| ⚠⚠ **Vượt giới hạn đặt** | Driver **báo lỗi và dừng trục** |

### ⭐⭐ Vì sao nó là chẩn đoán tốt nhất

Đặt **giới hạn sai lệch bám** là cách rẻ nhất để phát hiện **cơ khí có vấn đề**:

| Sai lệch bám tăng bất thường nói lên | Ví dụ |
|---|---|
| ⭐ **Có vật cản** | ⭐⭐ **Đúng bài toán mở đầu chương** — trục Z gặp board, keo khô, hoặc gá lệch |
| Ma sát tăng | Ray dẫn hướng thiếu mỡ, bụi bẩn |
| Tải nặng hơn thiết kế | Gá thêm đồ, sản phẩm nặng hơn |
| Chỉnh định driver chưa đủ cứng | Trục "mềm", bám kém |
| Phanh chưa nhả hết | ⚠ Trục kéo cả phanh — nóng driver, mòn phanh |

> ⭐⭐ **Đây là thứ hiếm trong nghề: một phép đo phát hiện được vấn đề CƠ KHÍ, miễn phí, từ trong
> chương trình.**
>
> Trục Z đâm xuống board không chỉ là lỗi lập trình vị trí — nó cũng làm **sai lệch bám tăng vọt**
> ngay khi chạm vật cản. ⭐ Giới hạn sai lệch bám đặt đúng sẽ **dừng trục trước khi hỏng đầu keo**.
>
> ⚠ Nhưng nó **không thay thế** giới hạn cứng và mạch an toàn (mục 37.6) — nó chỉ là lớp phát hiện
> thêm, và nó nằm **trong** driver nên không có mức an toàn.

### ⭐ Ghi mốc — lại một lần nữa

| Việc | Vì sao |
|---|---|
| ⭐ **Ghi sai lệch bám lớn nhất** của từng trục lúc nghiệm thu | Chương 52 — có cái để so |
| ⭐ Theo dõi xu hướng theo tháng | ⚠ **Tăng dần = cơ khí đang xấu đi** (Chương 53 mục 53.5) |
| Đặt giới hạn **cao hơn giá trị bình thường một khoảng hợp lý** | ⚠ Quá sát thì báo lỗi giả; quá rộng thì mất tác dụng bảo vệ |

⭐ Đây là lần thứ năm nguyên tắc **"ghi mốc lúc máy còn mới"** xuất hiện trong sách — cùng với điện
áp 24 V (Ch.8), dòng động cơ (Ch.36), số lỗi mạng (Ch.40) và chu kỳ máy (Ch.55).

### ⚡ Tên khối lệnh PLCopen — để tra tiếp

Mục 37.8 nói về mẫu `Execute` / `Done` / `Busy`. Các khối chuẩn có tên bắt đầu bằng `MC_`, ví dụ
`MC_Power` (cấp/ngắt mô-men), `MC_Home` (về gốc), `MC_MoveAbsolute` (chạy tới vị trí tuyệt đối),
`MC_Stop`, `MC_Reset`.

⭐ **Biết tiền tố `MC_` là đủ để tra tài liệu bất kỳ hãng nào** — kể cả hãng đặt tên khác, họ đều đối
chiếu về bộ tên này. ⚠ Nhưng nhớ mục A2.7 của Phụ lục A2: **mức tuân thủ khác nhau theo chân**, nên
vẫn phải đọc bảng khai của hãng.

*(Đối chiếu: tài liệu chuyển động của Inovance H5U/InoProShop — định nghĩa sai lệch bám là hiệu giữa
vị trí lệnh gửi xuống driver và vị trí encoder gửi lên, kèm giới hạn đặt được; PLCopen — Function
Blocks for Motion Control, tên các khối `MC_*`.)*

---

## 37.9 Trên máy mẫu DP-01

### Cấu hình gantry

Từ số liệu đã chốt (Phụ lục J §J.1): board **100 × 80 mm**, vùng làm việc **X 0–150 mm · Y 0–120 mm ·
Z 0–50 mm**, cả ba trục là **servo**.

| Trục | Vai trò | Về gốc | Giới hạn phần cứng |
|---|---|---|---|
| `AX_X` | Ngang board | Cảm biến gốc + xung Z | Hai đầu, tiếp điểm NC, vào drive |
| `AX_Y` | Dọc board | Cảm biến gốc + xung Z | Hai đầu, NC, vào drive |
| `AX_Z` | ⭐ Nâng/hạ đầu keo, đặt độ cao theo công thức | Cảm biến gốc ở **vị trí trên** | ⚠ Xem bên dưới |

> ⚠⚠ **Trục Z có tải treo — đây là trục nguy hiểm nhất của máy.**
>
> Khi mất điện hoặc khi drive nhả mô-men, trục Z **rơi xuống do trọng lực**. Ba hệ quả:
> - Cần **phanh cơ khí** trên động cơ Z, tự nhả khi có điện và tự kẹp khi mất điện.
> - ⚠ Phanh phải kẹp **trước** khi drive nhả mô-men — thứ tự này là tham số phải đặt đúng.
> - Về gốc trục Z phải đi **lên**, không đi xuống — nếu cữ gốc ở dưới thì một lỗi làm trục đâm xuống.
>
> Đây là hạng mục thuộc phân tích trạng thái an toàn ở Chương 48 mục 48.2, và phần bảo vệ người thuộc
> Chương 47.

### Thứ tự về gốc

```iecst
// ⭐ Gọi MỖI vòng quét, NGOÀI CASE — Execute lấy thẳng từ bước: vào bước là sườn lên,
//    rời bước là sườn xuống, nên lần về gốc SAU cũng phát được lệnh (Chương 30 mục 30.5b)
HomeZ(Axis := AX_Z, Execute := (HomeStep = 10));
HomeX(Axis := AX_X, Execute := (HomeStep = 20));
HomeY(Axis := AX_Y, Execute := (HomeStep = 20));

CASE HomeStep OF
    10:  // ⭐ Z LÊN TRƯỚC — nếu không, đầu keo quét ngang qua board
        IF HomeZ.Done THEN  HomeStep := 20;  END_IF;

    20:  // X và Y về gốc được, sau khi Z đã an toàn
        IF HomeX.Done AND HomeY.Done THEN  HomeStep := 30;  END_IF;

    30:
        M_Homed := TRUE;        // ⚠⚠ biến KHÔNG giữ qua mất điện (mục 37.3)
        HomeStep := 0;

ELSE
    HomeStep := 0;              // giá trị lạ → về trạng thái đã biết (Chương 20)
END_CASE;

// Timeout song song — cữ hỏng thì trục chạy mãi (Chương 17, Chương 26)
T_HomeTimeout(IN := (HomeStep > 0), PT := T#30S);
IF T_HomeTimeout.Q OR HomeZ.Error OR HomeX.Error OR HomeY.Error THEN
    M_HomeFault := TRUE;
    // dừng mọi trục
END_IF;
```

### Điều kiện cho phép chạy

Gom từ nhiều chương, gantry đóng góp hai điều kiện:

```iecst
M_CanStart := M_Homed                    // ⭐ đã về gốc — mục 37.3
          AND NOT M_AxisFault            // không trục nào báo lỗi
          AND M_RecipeLoaded             // Chương 29
          AND NOT M_RecipeRejected
          AND DI_AirOK
          AND DI_EStopOK
          AND NOT M_AnyFault;
```

> ⭐ Viết đầy đủ từng điều kiện thay vì gom vào cờ tổng — đúng nguyên tắc ở Chương 24 mục 24.7: khi
> máy không khởi động được, người vận hành nhìn thấy ngay **điều kiện nào** đang thiếu.

### Chu kỳ và đường keo

Với chu kỳ 12 s/board đã chốt và trạm sấy UV sát trần, thời gian gantry chạy đường keo **phải nằm gọn
trong phần chu kỳ của trạm 1**.

> ⚠ Đây là chỗ ba quyết định gặp nhau và có thể xung đột:
> - **Chiều dài đường keo** theo công thức (Chương 29) — dài hơn thì lâu hơn.
> - **Biên dạng chữ S** cho đường keo đều (mục 37.5) — êm hơn nhưng chậm hơn.
> - **Chu kỳ mục tiêu 12 giây** (Phụ lục J §J.1).
>
> Không có cách nào thoả cả ba bằng lập luận. Phải **đo** — Chương 55.

---

## 37.10 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| ⭐ **PLCopen Motion** | Nhiều hãng theo mẫu `Execute`/`Done`/`Busy`/`Error` — ⭐ **đây là chỗ tính khả chuyển kỹ năng cao nhất trong cả cuốn sách**. Học một hệ, đọc được hệ khác |
| ⚠ Mức độ tuân theo | Tên khối và chân **gần giống** nhưng chi tiết khác: hành vi khi chen lệnh, cách xử lý lỗi, đơn vị. ⚠ Đừng giả định giống hệt |
| Nơi chạy vòng điều khiển | Luôn ở **drive**. Nhưng có hệ tính biên dạng chuyển động ở PLC, có hệ tính ở drive |
| Mạng tới drive | EtherCAT, PROFINET IRT, EtherNet/IP với đồng bộ, hoặc mạng riêng của hãng (Chương 40). ⭐ Chọn theo hệ PLC |
| ⚠ Đơn vị kỹ thuật | Có hệ làm việc bằng **đơn vị người dùng** (mm, độ) sau khi khai báo tỉ số truyền; có hệ làm việc bằng **xung encoder**. Nhầm là sai theo tỉ lệ |
| Cấu hình về gốc | Số kiểu về gốc hỗ trợ và cách chọn khác nhau nhiều |
| Ngõ vào giới hạn của drive | ⭐ Gần như mọi drive đều có — **kiểm và dùng nó** (mục 37.6) |
| Phanh cơ khí | Cách điều khiển và **thứ tự nhả/kẹp** là tham số của drive — ⚠ đặt sai thì trục rơi |

> ⚠ **Hàng "đơn vị kỹ thuật" là chỗ sai theo tỉ lệ.** Khai báo tỉ số truyền sai thì lệnh "đi 45 mm"
> có thể thành 4,5 mm hoặc 450 mm — và con số trên màn hình vẫn hiện 45. Kiểm bằng cách **cho trục đi
> một quãng đã biết và đo bằng thước** (Chương 18, Bẫy 8; Chương 52).

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

---

## 37.11 Bẫy thường gặp

### 🔍 BẪY 1 — Giữ cờ "đã về gốc" qua mất điện

**Hiện tượng:** ⚠⚠ đúng cỗ máy ở mục 37.1 — máy tin rằng biết vị trí, giới hạn phần mềm bảo vệ một hệ
toạ độ sai, và trục đi tới chỗ không ai muốn.
**Cách sửa:** `M_Homed` là biến **không giữ**; mọi lệnh tuyệt đối phải kiểm nó (mục 37.3, Chương 16
mục 16.4).

### 🔍 BẪY 2 — Công tắc giới hạn đi qua PLC

**Hiện tượng:** khi PLC lỗi hoặc đang STOP — đúng lúc bạn cần nó nhất — giới hạn **không tác dụng**.
**Cách sửa:** đi **thẳng vào drive**, tiếp điểm NC. PLC đọc để **biết**, không để **dừng** (mục 37.6).

### 🔍 BẪY 3 — Tin rằng giới hạn phần mềm là đủ

**Hiện tượng:** hoạt động tốt trong mọi thử nghiệm bình thường, rồi hỏng đúng lúc hệ toạ độ sai.
**Cách sửa:** ba lớp bảo vệ, mỗi lớp chống một nhóm lỗi khác nhau (mục 37.6).

### 🔍 BẪY 4 — Về gốc không có timeout

**Hiện tượng:** cữ gốc hỏng hoặc dây đứt → trục chạy tới khi đâm vào cữ cứng.
**Cách sửa:** timeout song song, và tốc độ về gốc chậm (mục 37.3, Chương 17).

### 🔍 BẪY 5 — Sai thứ tự về gốc trên gantry

**Hiện tượng:** đầu tra keo **quét ngang qua board** hoặc qua đồ gá khi X/Y về gốc trước Z.
**Cách sửa:** ⭐ **Z lên trước**, rồi mới X và Y (mục 37.9).

### 🔍 BẪY 6 — Quên phanh cho trục có tải treo

**Hiện tượng:** ⚠⚠ trục Z **rơi xuống** khi mất điện hoặc khi drive nhả mô-men.
**Cách sửa:** phanh cơ khí, và ⚠ **thứ tự kẹp trước khi nhả mô-men** phải đặt đúng trong tham số
drive (mục 37.9).

### 🔍 BẪY 7 — `Execute` không bao giờ hạ xuống

**Hiện tượng:** lệnh chạy được lần đầu, những lần sau **không phát được** — trình tự treo ở bước đó.
⚠ Hai cách viết gây ra nó, và cả hai trông vô hại: gọi với **hằng** `Execute := TRUE`, hoặc gọi khối
**bên trong** nhánh `CASE` — rời bước thì khối không được gọi nữa, nên nó **không bao giờ thấy**
`Execute` hạ xuống (Phụ lục B mục B.9b). Chính đoạn về gốc ở mục 37.9 từng mắc lỗi này.
**Cách sửa:** lệnh kích bằng **cạnh lên**, nên giữa hai lệnh phải có **cạnh xuống**. Gọi khối **mỗi
vòng, ngoài `CASE`**, với `Execute := (HomeStep = 10)` — giữ TRUE suốt bước, tự hạ khi rời bước — hoặc
bằng một xung sườn lên như Phụ lục L mục L.9 (Chương 30 mục 30.5b, Chương 16).

### 🔍 BẪY 8 — Dùng chung một thể hiện khối chuyển động

**Hiện tượng:** lệnh này ghi đè trạng thái lệnh kia; `Done` báo sai bước.
**Cách sửa:** mỗi lệnh một thể hiện riêng — cùng lỗi với Chương 14, mục 14.3.

### 🔍 BẪY 9 — Không xử lý `CommandAborted`

**Hiện tượng:** lệnh bị chen ngang, `Done` không bao giờ lên, trình tự **chờ vĩnh viễn**.
**Cách sửa:** xử lý cả `Done`, `Error` **và** `CommandAborted`; cộng timeout (mục 37.8).

### 🔍 BẪY 10 — Chuyển bước bằng timer thay vì `Done`

**Hiện tượng:** ⚠ bước sau chạy khi trục **chưa tới đích** — đúng bẫy trung tâm của Chương 17.
**Cách sửa:** chờ `Done`; timer chỉ để **báo lỗi**, không để tiến bước.

### 🔍 BẪY 11 — Dùng lệnh tương đối cho vị trí xác định

**Hiện tượng:** vị trí **trôi dần** sau nhiều chu trình do sai số tích luỹ.
**Cách sửa:** dùng lệnh **tuyệt đối** bất cứ khi nào có thể (mục 37.4).

### 🔍 BẪY 12 — Khai báo tỉ số truyền sai

**Hiện tượng:** mọi chuyển động sai theo tỉ lệ, trong khi con số trên màn hình vẫn "đúng".
**Cách sửa:** ⭐ **cho trục đi một quãng đã biết và đo bằng thước** (mục 37.10, Chương 52).

### 🔍 BẪY 13 — Tắt giới hạn phần mềm khi jog "cho tiện"

**Hiện tượng:** jog vượt vùng làm việc, đâm vào đồ gá hoặc vào chính board.
**Cách sửa:** giới hạn phần mềm vẫn hoạt động khi jog; jog chưa về gốc thì chạy **rất chậm** và dựa
vào giới hạn phần cứng (mục 37.4).

---

## 37.12 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| ⭐⭐ Sai lệch bám là gì | **Vị trí lệnh − vị trí thật**; nó **luôn tồn tại**, trục luôn bám sau một chút |
| ⭐ Sai lệch bám tăng bất thường nói gì | ⭐⭐ **Cơ khí có vấn đề** — vật cản, ma sát, quá tải, phanh chưa nhả |
| ⚠ Giới hạn sai lệch bám có thay được giới hạn cứng không | **Không** — nó nằm trong driver, không có mức an toàn |
| Servo khác biến tần | Servo điều khiển **vị trí**, có **encoder phản hồi** |
| Ba vòng của servo | Vị trí → tốc độ → dòng, **tất cả trong drive** |
| ⚠ Đừng viết gì trên PLC | **PID vị trí** — drive chạy nhanh hơn vòng quét nhiều bậc |
| Sai số bám dùng để làm gì | ⭐ **Bộ phát hiện va chạm rẻ nhất** |
| Kiểu về gốc chính xác nhất | **Cảm biến gốc + xung Z** |
| Bốn điều bắt buộc khi về gốc | Chạy **chậm** · có **timeout** · đúng **thứ tự trục** · cờ **không giữ** |
| ⚠⚠ Cờ `M_Homed` | **Không bao giờ giữ** qua mất điện |
| Lệnh tuyệt đối cần gì | Đã về gốc |
| Lệnh tương đối có vấn đề gì | ⚠ **Sai số tích luỹ** |
| Ba lớp bảo vệ vùng làm việc | Giới hạn **phần mềm** → công tắc **phần cứng** → **cữ cơ khí** |
| ⭐ Công tắc giới hạn đi vào đâu | **Thẳng vào drive**, tiếp điểm NC — không qua PLC |
| Vì sao không qua PLC | Lúc cần nó nhất là lúc **PLC không đáng tin** |
| ⚠ Ba lớp đó có phải an toàn cho người | ❌ **Không** — chúng bảo vệ cơ cấu (Chương 47) |
| Biên dạng chữ S đổi lấy gì | Êm hơn, ít rung — **chậm hơn** |
| Tra keo theo đường cần | **Nội suy đường thẳng**, không chạy độc lập |
| Mẫu PLCopen | `Execute` (**cạnh lên**) → `Done` / `Busy` / `Error` / `CommandAborted` |
| Chuyển bước sau lệnh chuyển động | ⭐ Chờ **`Done`**, không chờ timer |
| Trục có tải treo cần | **Phanh cơ khí**, ⚠ kẹp **trước** khi nhả mô-men |
| Kiểm tỉ số truyền bằng | ⭐ Đi một quãng **đã biết** và **đo bằng thước** |

---

## 37.13 Tự kiểm

1. Servo khác biến tần ở ba điểm nào? Ba vòng điều khiển của servo nằm ở đâu?
2. ⭐ Vì sao **không** nên viết vòng PID vị trí trên PLC?
3. **Sai số bám** là gì? Vì sao nó là bộ phát hiện va chạm hữu ích, và đặt ngưỡng quá rộng/quá hẹp
   thì sao?
4. Nêu năm kiểu về gốc. Kiểu nào cho độ lặp lại cao nhất và vì sao?
5. ⭐ Nêu bốn điều bắt buộc trong trình tự về gốc. Điều nào liên quan tới Chương 16?
6. ⭐⭐ Vì sao cờ `M_Homed` **tuyệt đối không được giữ** qua mất điện? Mô tả hậu quả bằng cỗ máy ở
   mục 37.1.
7. Phân biệt lệnh tuyệt đối với tương đối. Lệnh nào có sai số tích luỹ, và khi nào dùng lệnh kia?
8. ⭐⭐ Nêu ba lớp bảo vệ vùng làm việc. Mỗi lớp chống được gì và **không** chống được gì?
9. ⭐ Vì sao công tắc giới hạn phải đi **thẳng vào drive** chứ không qua PLC?
10. Ba lớp bảo vệ đó có phải chức năng an toàn cho người không? Nếu không thì cái gì là?
11. Biên dạng hình thang gây vấn đề gì về cơ khí? Chữ S giải quyết thế nào và đổi lấy cái gì?
12. Vì sao ra lệnh X đi 100 mm và Y đi 50 mm cùng lúc **không** cho đường đi thẳng?
13. ⭐ Vì sao khối lệnh chuyển động có `Execute`/`Done`/`Busy` thay vì trả kết quả ngay? Mẫu này liên
    hệ thế nào với bẫy trung tâm của Chương 17?
14. Trên gantry của DP-01, vì sao **Z phải về gốc trước** X và Y?
15. ⚠ Trục Z có tải treo cần thêm gì, và thứ tự nào phải đặt đúng?
16. ⭐ Khai báo tỉ số truyền sai thì triệu chứng là gì, và kiểm bằng cách nào?

> Câu 2, 5, 6, 8, 9 và 13 là sáu câu phân loại. Câu 8 và 9 là tinh thần của cả chương: **giới hạn
> phần mềm bảo vệ chống lỗi lập trình; nó không bảo vệ chống việc hệ toạ độ bị sai — và những lúc bạn
> cần bảo vệ nhất lại chính là lúc phần mềm không đáng tin.**

⭐⭐ **Bổ sung.** Vì sao sai lệch bám **luôn khác 0** kể cả khi trục hoạt động hoàn hảo? Nêu năm
nguyên nhân làm nó tăng bất thường, và giải thích vì sao nó phát hiện được vấn đề **cơ khí** từ
trong chương trình.

⚠ **Bổ sung.** Giới hạn sai lệch bám có thay thế được giới hạn cứng và mạch an toàn không? Vì sao?

---

### Chương tiếp theo

Chương 38 — **Truyền thông nối tiếp**. Bạn đã hoàn tất khối analog và chuyển động. Từ đây sách sang
lát cắt 4: nối máy với thế giới bên ngoài. Bắt đầu bằng RS-232 và RS-485 — nền của mọi giao thức
công nghiệp, và là cách bộ điều khiển nhiệt độ của DP-01 nói chuyện với PLC.

### Nguồn tham khảo chương 37

- **PLCopen** — *Safe Motion v1.0* (TC5): ⭐ **danh mục đầy đủ các chức năng an toàn của truyền động**
  theo **IEC 61800-5-2** — bốn chức năng dừng (STO · SS1 · SS2 · SOS), nhóm giới hạn (SLS, SSR, SLP,
  SLI, SDI, SLA, SAR, SLT, STR, SMT), nhóm công bố tín hiệu (SSM, SCA, SBC) — nền cho mục 37.6b;
  và **hai kiến trúc**: giám sát **trong chính drive** với máy trạng thái nội bộ, hay giám sát ở một
  **bộ điều khiển an toàn**. *(tài liệu mở của PLCopen; ⚠ bản thân IEC 61800-5-2 có bản quyền và
  KHÔNG có trong bộ tài liệu — sách chỉ nêu tên và mô tả chức năng ở mức khái niệm, không dẫn số
  điều khoản)*

- IEC 61800-5-2 — *Adjustable speed electrical power drive systems — Safety requirements — Functional*:
  các chức năng an toàn của truyền động. *(tiêu chuẩn có bản quyền)*
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu với mạch điều khiển
  chuyển động và với chức năng dừng — nền cho mục 37.6.
- **Đặc tả PLCopen Motion Control** — chuẩn hoá giao diện khối chuyển động (`Execute`/`Done`/`Busy`/
  `Error`) mà nhiều hãng theo. ⭐ Đây là tài liệu đáng đọc vì nó là chỗ **kỹ năng chuyển được giữa các
  hệ** tốt nhất.
- **Tài liệu servo drive** của hệ đang dùng — dùng cho ⚠ **đơn vị kỹ thuật và tỉ số truyền**, kiểu về
  gốc hỗ trợ, ngõ vào giới hạn phần cứng, ngưỡng sai số bám, và ⚠ **điều khiển phanh cùng thứ tự
  nhả/kẹp**.
- Bảng I/O, vùng làm việc gantry và số liệu đã chốt của DP-01 — Phụ lục J §J.1 và §J.2.

> ⚡ Các con số giới hạn ở mục 37.6 (−1/51 mm, −3/53 mm, −5/55 mm) là **minh hoạ cho nguyên tắc ba
> lớp**, không phải giá trị thiết kế. Khoảng cách giữa các lớp phụ thuộc tốc độ chạy, quán tính, và
> quãng đường dừng của trục — ⚠ **phải tính**, và phải tính cho **trường hợp xấu nhất**: tốc độ cao
> nhất, tải nặng nhất.
>
> ⚠ **Về mục 37.6 và trục Z có tải treo (mục 37.9):** nội dung ở đây là định hướng để bạn biết phải
> hỏi gì. Thiết kế bảo vệ cho trục đứng có tải treo — chọn phanh, tính quãng đường dừng, xác định mức
> hiệu năng cần đạt — phải do **người có thẩm quyền** thực hiện theo Chương 47. Trục đứng rơi tự do
> là một trong những mối nguy nghiêm trọng nhất trên máy tự động hoá.
