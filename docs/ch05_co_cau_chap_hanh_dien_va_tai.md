# Chương 5 — Cơ cấu chấp hành điện & tải

---

## 5.1 Bài toán: ngõ ra chết dần trong sáu tháng

Một cỗ máy chạy ổn. Sau khoảng bốn tháng, một kênh ngõ ra bắt đầu **thỉnh thoảng không tác động** —
van không mở, người vận hành nhấn Reset, lần sau lại chạy. Hai tháng nữa thì kênh đó chết hẳn.

Thay module, chạy tiếp. Bốn tháng sau, kênh khác chết theo cùng kiểu.

Nguyên nhân: các cuộn van được đấu thẳng vào ngõ ra **không có mạch dập**. Mỗi lần cắt dòng, cuộn dây
sinh ra một xung áp ngược hàng trăm vôn. Transistor trong module chịu được — cho tới lần thứ vài trăm
nghìn.

Chi phí sửa: một linh kiện vài nghìn đồng cho mỗi cuộn van, lắp lúc đấu tủ. Chi phí không sửa: thay
module định kỳ, cộng những giờ dừng máy không báo trước.

Chương này về những gì nằm ở **đầu ra** của PLC — và về mấy quyết định nhỏ, rẻ, làm một lần, quyết
định máy chạy được bao lâu.

---

## 5.2 Van điện từ

**Van điện từ** *(solenoid valve)* là cơ cấu chấp hành phổ biến nhất trên máy tự động hoá: PLC cấp
điện cho cuộn hút, cuộn hút đẩy lõi van, van đổi đường khí (Chương 6).

Về mặt **điện**, van điện từ chỉ là một cuộn dây. Ba thông số cần đọc:

| Thông số | Vì sao cần |
|---|---|
| **Điện áp và loại** (24 VDC / 230 VAC) | Quyết định kiểu ngõ ra dùng được (Chương 9) |
| **Dòng làm việc** | Cộng vào phụ tải nguồn 24 V; thường là phụ tải lớn nhất |
| ⚠ **Có sẵn mạch dập trong đầu nối không** | Quyết định bạn có phải lắp thêm hay không — mục 5.4 |

> ⚡ **Nhiều van có đầu nối kèm diode hoặc đèn báo.** Kiểm bằng cách đọc mã đầu nối, hoặc đo. **Đừng
> giả định theo cả hai hướng**: giả định có mà thực ra không thì hỏng ngõ ra; giả định không rồi lắp
> thêm thì có thể lắp hai diode nối tiếp và van nhả chậm bất thường.

### Van giữ hai vị trí

Một số van cần **hai cuộn**: một cuộn đẩy sang trái, một cuộn đẩy sang phải, và van **giữ nguyên vị
trí** khi cả hai cuộn mất điện.

> ⚠⚠ **NGUY HIỂM — hai cuộn cùng có điện**
> Cấp điện đồng thời hai cuộn của van giữ hai vị trí làm van kẹt ở giữa hoặc hành xử không đoán được,
> và cuộn dây **nóng lên** vì phải giữ điện liên tục.
>
> Hai biện pháp, **dùng cả hai**:
> - **Khoá lẫn trong chương trình**: hai ngõ ra loại trừ nhau về logic.
> - ⭐ **Khoá lẫn bằng phần cứng**: tiếp điểm rơ-le cắt chéo nhau. Vì logic PLC có thể sai, có thể bị
>   cưỡng bức (Chương 51), hoặc CPU có thể dừng ở trạng thái xấu.
>
> Nguyên tắc: **thứ gì hỏng thì gây hại vật lý, đừng chỉ bảo vệ bằng phần mềm.**

---

## 5.3 Contactor và động cơ

**Contactor** đã giới thiệu ở Chương 3, mục 3.5. Phần liên quan tới PLC:

| Điểm | Điều cần biết |
|---|---|
| Cuộn hút | Thường 24 VDC hoặc 230 VAC. ⚠ **Là tải cảm** — cần mạch dập |
| Dòng cuộn hút | Nhỏ, PLC điều khiển trực tiếp được; nhưng xem mục 5.5 |
| ⭐ **Tiếp điểm phụ** | Cho PLC biết contactor **thật sự đã đóng chưa** |
| Rơ-le nhiệt / bảo vệ động cơ | Tiếp điểm báo lỗi nên đưa về PLC |

> 💡 **Luôn đưa tiếp điểm phụ về PLC nếu có.**
> Không có nó, chương trình chỉ biết **đã ra lệnh**, không biết **đã xảy ra**. Cuộn hút đứt, tiếp điểm
> hàn dính, hay aptomat nhánh nhảy — cả ba đều không phát hiện được.
>
> Đây là nguyên tắc "giám sát phản hồi thay vì tin lệnh" (Chương 48) áp ở tầng điện, và nó rẻ: một
> ngõ vào số.

Điều khiển tốc độ động cơ bằng biến tần là chuyện của Chương 36; ở đây chỉ cần biết contactor cho
đóng/cắt đơn giản.

---

## 5.4 ⭐ Tải cảm và mạch dập

Đây là mục quan trọng nhất chương, và là nguyên nhân của cỗ máy ở mục 5.1.

### Vì sao xung áp ngược xuất hiện

Cuộn dây tích trữ năng lượng trong từ trường. Khi cắt dòng đột ngột, từ trường sụp đổ và cuộn dây
**cố duy trì dòng** bằng cách sinh ra điện áp — theo:

```text
V = L × (di/dt)
```

`di/dt` là tốc độ thay đổi dòng. Cắt càng nhanh thì `di/dt` càng lớn, nên `V` càng cao.

> ⚠ **Transistor cắt rất nhanh — micro-giây.** Nên xung áp ngược từ một cuộn van 24 V có thể lên tới
> **hàng trăm vôn**. Nó tồn tại rất ngắn, nhưng đủ để phá lớp bán dẫn.

Ba hậu quả, và cả ba đều gặp trong thực tế:

| Hậu quả | Biểu hiện |
|---|---|
| **Phá transistor ngõ ra** | Kênh chết dần rồi chết hẳn — đúng mục 5.1 |
| **Ăn mòn tiếp điểm rơ-le** | Hồ quang mỗi lần cắt; tiếp điểm rỗ, điện trở tăng, rồi hàn dính |
| ⭐ **Phát nhiễu ra cả tủ** | Ngõ vào khác đọc sai, mạng rớt gói, CPU khởi động lại — **triệu chứng trông hoàn toàn không liên quan** |

Hậu quả thứ ba là hậu quả tốn thời gian nhất, vì không ai nghĩ tới việc thiếu một con diode khi đi
tìm nguyên nhân "mạng thỉnh thoảng rớt".

### Chọn mạch dập

| Tải | Mạch dập | Cách đấu |
|---|---|---|
| **DC** | ⭐ **Diode ngược** *(flyback diode)* | Song song với cuộn, **cực âm về phía dương nguồn** |
| **DC**, cần nhả nhanh | Diode + điện trở, hoặc **diode Zener** | Như trên, thêm phần tử hạn áp |
| **AC** | **Mạch RC** *(snubber)* hoặc **varistor** *(MOV)* | Song song với cuộn |

```text
DIODE NGƯỢC cho tải DC
                    ┌──────┤◄├──────┐     ← cực âm (vạch) về phía +24V
   +24V ────────────┤              │
                    │   CUỘN VAN   │
   ngõ ra PLC ──────┤              │
                    └──────────────┘
```

> ⚠⚠ **NGUY HIỂM CHO THIẾT BỊ — đấu diode ngược chiều là ngắn mạch nguồn**
> Diode đấu đúng thì **không dẫn** khi mạch hoạt động bình thường; nó chỉ dẫn khi xung ngược xuất
> hiện. Đấu ngược chiều thì nó **dẫn ngay khi cấp điện** — tạo một đường ngắn mạch từ +24 V xuống
> ngõ ra.
>
> Kết quả: nổ cầu chì, hỏng bộ nguồn, hoặc hỏng ngõ ra.
>
> **Kiểm bằng đồng hồ ở thang đo diode trước khi cấp điện.** Ba mươi giây, và nó loại hẳn một lỗi
> đắt.

### ⚠ Đánh đổi: diode làm van nhả chậm hơn

Diode ngược là cách dập rẻ nhất và bảo vệ tốt nhất, nhưng nó có giá:

Diode tạo một đường cho dòng **chạy vòng trong cuộn** sau khi cắt. Dòng đó tắt dần chứ không dứt
ngay, nên từ trường giữ lâu hơn, nên **van nhả chậm hơn** — thường thêm vài mili-giây tới hơn chục
mili-giây.

| Trường hợp | Vài ms có quan trọng không |
|---|---|
| Van chặn, van kẹp trên DP-01 | ❌ Không — cơ cấu mất hàng trăm ms để chuyển động |
| Van tra keo tác động nhanh | ⭐ **Có** — thời gian nhả quyết định lượng keo |
| Van khí điều khiển nhịp cao | ⭐ Có |

Khi thời gian nhả quan trọng, dùng **diode + điện trở** hoặc **diode Zener**: chúng cho phép điện áp
ngược cao hơn diode đơn (nhưng vẫn trong giới hạn an toàn), nên dòng tắt nhanh hơn và van nhả nhanh
hơn.

> 💡 **Quy tắc thực dụng:** mặc định dùng **diode đơn**. Chỉ chuyển sang phương án nhả nhanh khi có
> **lý do đo được** — đã đo thời gian nhả và nó thật sự ảnh hưởng chất lượng sản phẩm. Đừng tối ưu
> trước khi có số liệu.

### Đặt mạch dập ở đâu

> ⭐ **Càng gần cuộn dây càng tốt** — lý tưởng là ngay tại đầu nối của van.
>
> Đặt xa (ví dụ trong tủ, cách van ba mét) thì đoạn dây giữa mạch dập và cuộn vẫn **phát nhiễu ra
> môi trường**. Bảo vệ được ngõ ra, nhưng không giải quyết được hậu quả thứ ba ở bảng trên.

---

## 5.5 ⭐ Rơ-le trung gian — vì sao gần như luôn cần

**Rơ-le trung gian** *(interposing relay)* là một rơ-le nhỏ đặt giữa ngõ ra PLC và tải thật:

```text
   ngõ ra PLC ──► cuộn rơ-le trung gian ──► tiếp điểm ──► TẢI THẬT
      (nhỏ)                                              (lớn, hoặc ở xa)
```

Cám dỗ là bỏ nó đi: *"module chịu được 0,5 A, van chỉ ăn 0,3 A, đấu thẳng cho gọn."*

### Sáu lý do vẫn nên có

| Lý do | Giải thích |
|---|---|
| **Dòng tải không đi qua module** | Module chỉ cấp dòng nhỏ cho cuộn rơ-le — kéo dài tuổi thọ đáng kể |
| ⭐ **Thay rẻ hơn nhiều** | Rơ-le hỏng thì rút ra cắm cái mới trong một phút. Module hỏng thì thay cả module, và **mất luôn các kênh khác đang tốt** |
| **Cách ly thật** | Tiếp điểm cơ khí — không dòng rò (Chương 9, mục 9.3) |
| **Đóng cắt được điện áp khác** | Ngõ ra 24 VDC điều khiển tải 230 VAC |
| ⭐ **Điểm đo rõ ràng khi chẩn đoán** | Nghe tiếng "tách", nhìn đèn trên rơ-le, đo hai bên tiếp điểm — cô lập được ngay lỗi nằm ở PLC hay ở tải (Chương 51) |
| **Giải quyết bài toán dòng chân chung** | Dòng tải không cộng vào giới hạn chân chung của module (Chương 9, mục 9.4) |

Lý do thứ hai và thứ năm là hai lý do thực dụng nhất, và cả hai đều nói về **lúc máy hỏng**, không
phải lúc máy chạy.

### Cái giá

| Đánh đổi | Mức |
|---|---|
| Thêm linh kiện và chỗ trong tủ | Nhỏ |
| Thêm một điểm hỏng | Có thật — nhưng rơ-le là thứ **dễ thay nhất** trong tủ |
| ⚠ Thêm trễ vài mili-giây | Đáng kể **chỉ khi** cần đáp ứng nhanh |
| ⚠ Cuộn rơ-le cũng là tải cảm | **Cũng cần mạch dập** — đừng quên |

> **Quy tắc thực dụng:**
> - Tải **đi ra khỏi tủ**, tải **lớn**, tải **AC**, hoặc tải **đóng cắt rất nhiều** → dùng rơ-le
>   trung gian.
> - Tải nhỏ, trong tủ, cần nhanh → đấu thẳng, nhưng **vẫn phải có mạch dập**.
>
> Trên DP-01: van khí đấu thẳng vào ngõ ra transistor (Chương 9, mục 9.7) vì cần nhịp nhanh và tải
> nhỏ; tín hiệu bắt tay đi sang máy bên cạnh thì qua rơ-le vì cần cách ly thật (Chương 41).

---

## 5.6 Đèn tháp và còi

**Đèn tháp** *(stack light / tower light)* là giao diện đầu tiên giữa máy và người — và thường là
giao diện duy nhất nhìn thấy được từ xa.

### Quy ước màu

| Màu | Nghĩa thông dụng | Người vận hành làm gì |
|---|---|---|
| 🔴 **Đỏ** | Sự cố, máy dừng bất thường | Phải xử lý ngay |
| 🟡 **Vàng** | Bất thường, cần chú ý — máy **chưa** dừng | Chuẩn bị xử lý |
| 🟢 **Xanh lá** | Máy chạy bình thường | Không cần làm gì |
| 🔵 Xanh dương | Cần thao tác của người | Thao tác theo yêu cầu |
| ⚪ Trắng | Thông tin chung | |

> ⚠ **Quy ước màu là quy ước có tiêu chuẩn, không phải sở thích.** Người vận hành đi qua nhiều máy
> trong một ca, và họ phản ứng theo **thói quen** chứ không đọc kỹ. Một máy dùng đỏ để báo "đang
> chạy" là một máy nguy hiểm.
>
> Quy ước cụ thể lấy từ tiêu chuẩn hiện hành và từ quy định của cơ sở — **thống nhất trong toàn nhà
> máy quan trọng hơn** việc chọn phương án nào.

### Bốn nguyên tắc thiết kế

- ⭐ **Trạng thái đèn nối thẳng vào biến trạng thái máy**, không có logic đèn riêng. Có logic riêng là
  có khả năng đèn nói một đằng, máy làm một nẻo (Chương 25, mục 25.9).
- **Nhấp nháy mang thêm thông tin.** Ví dụ: xanh sáng liên tục = đang chạy; xanh nhấp nháy = sẵn sàng
  nhưng chưa chạy. Đừng dùng nhấp nháy tuỳ tiện — mỗi kiểu nháy phải có nghĩa xác định.
- **Còi để báo sự kiện, không để báo trạng thái.** Còi kêu liên tục sẽ bị tắt hoặc bị tháo. Dùng xung
  có độ dài xác định khi có báo động **mới** (Chương 17, mục 17.2).
- ⚠ **Đèn tháp không phải thiết bị an toàn.** Nó thông báo, không bảo vệ. Chức năng an toàn nằm ở
  mạch an toàn (Chương 47).

---

## 5.7 Tính công suất nhánh 24 VDC

Chương 8 mục 8.7 và Chương 9 mục 9.5 nói cách tính tổng. Ở đây là phần thuộc về **tải**.

### Dòng khởi động

> ⚠ **Cuộn dây và đèn hút dòng cao hơn dòng làm việc trong vài mili-giây đầu.**
>
> Với cuộn dây, dòng tăng dần theo điện cảm. Với đèn sợi đốt, điện trở khi nguội thấp hơn nhiều khi
> nóng nên dòng ban đầu rất cao. Tính phụ tải theo **dòng làm việc** rồi bỏ qua giai đoạn này là lý
> do phổ biến khiến nguồn bị thiếu đúng lúc nhiều cơ cấu cùng tác động.

### Cách tính đúng

| Bước | Việc |
|---|---|
| 1 | Liệt kê mọi tải 24 V theo bảng I/O |
| 2 | Tra **dòng làm việc** từng loại — từ datasheet, không đoán |
| 3 | ⭐ Từ **mô tả trình tự** (Chương 23), tìm bước có **nhiều tải cùng bật nhất** |
| 4 | Cộng dòng tại bước đó |
| 5 | Nhân **1,3–1,5** cho dòng khởi động và dự phòng |

Bước 3 là bước hay bị bỏ. Cộng dòng của **tất cả** tải cho ra con số quá lớn (lãng phí); cộng dòng
**trung bình** cho ra con số quá nhỏ (nguy hiểm). Con số đúng là **trường hợp xấu nhất thực tế xảy
ra**, và nó nằm trong mô tả trình tự.

### Tách nhánh

> 💡 **Dùng nhánh cầu chì riêng cho ba nhóm:** (1) CPU và module, (2) cảm biến, (3) cơ cấu chấp hành.
>
> Lợi ích khi có sự cố: một cuộn van chập **không kéo sập CPU**, và khi chẩn đoán bạn cô lập được
> từng nhóm bằng cách rút một cầu chì (Chương 51). Chi phí thêm rất nhỏ.

---

## 5.8 ⭐ Chọn gì cho tải nào — bảng tra khi thiết kế

| Tải | Kiểu ngõ ra | Mạch dập | Rơ-le trung gian |
|---|---|---|---|
| Van khí 24 VDC, nhịp cao | **Transistor** (Chương 9) | ⭐ **Diode** bắt buộc | Không — cần nhanh |
| Van tra keo tác động nhanh | **Transistor** | Diode + điện trở / Zener | Không |
| Cuộn contactor 24 VDC | Transistor hoặc rơ-le | ⭐ **Diode** | Tuỳ dòng cuộn |
| Cuộn contactor 230 VAC | **Rơ-le** | ⭐ **RC hoặc varistor** | Thường là chính nó |
| Đèn tháp, còi 24 VDC | Transistor | Không cần (tải trở) | Không |
| Tín hiệu sang máy khác | **Rơ-le** | Diode cho cuộn rơ-le | ⭐ **Có** — cần cách ly thật |
| Tải lớn hoặc ngoài tủ | — | Theo loại tải | ⭐ **Có** |

---

## 5.9 Bẫy thường gặp

### 🔍 BẪY 1 — Không lắp mạch dập cho tải cảm

**Hiện tượng:** ngõ ra **chết dần** trong vài tháng — đúng cỗ máy ở mục 5.1. Hoặc nhiễu lan khắp tủ
làm các ngõ vào khác đọc sai, mạng rớt gói — **triệu chứng trông hoàn toàn không liên quan**.
**Cách sửa:** diode cho tải DC, RC hoặc varistor cho tải AC. Đặt càng gần cuộn càng tốt (mục 5.4).

### 🔍 BẪY 2 — Đấu diode ngược chiều

**Hiện tượng:** ngắn mạch ngay khi cấp điện — nổ cầu chì, hỏng nguồn hoặc hỏng ngõ ra.
**Cách sửa:** cực âm (vạch trên thân diode) về phía **+24 V**. Kiểm bằng đồng hồ thang đo diode
**trước khi cấp điện**.

### 🔍 BẪY 3 — Lắp thêm diode cho van đã có sẵn diode

**Hiện tượng:** van nhả chậm bất thường; ở van tác động nhanh thì ảnh hưởng chất lượng sản phẩm.
**Cách sửa:** kiểm đầu nối van trước khi lắp thêm (mục 5.2).

### 🔍 BẪY 4 — Cấp điện đồng thời hai cuộn của van giữ hai vị trí

**Hiện tượng:** van kẹt giữa, hành xử không đoán được, cuộn nóng.
**Cách sửa:** khoá lẫn **cả trong chương trình lẫn bằng phần cứng** (mục 5.2).

### 🔍 BẪY 5 — Không đưa tiếp điểm phụ contactor về PLC

**Hiện tượng:** chương trình tin contactor đã đóng trong khi cuộn đứt hoặc aptomat nhánh đã nhảy;
máy chạy tiếp trình tự với một cơ cấu không hoạt động.
**Cách sửa:** một ngõ vào số, và một điều kiện chờ phản hồi (mục 5.3, Chương 48).

### 🔍 BẪY 6 — Quên mạch dập cho cuộn rơ-le trung gian

**Hiện tượng:** đã lắp rơ-le trung gian để bảo vệ ngõ ra, nhưng ngõ ra vẫn hỏng — vì **cuộn rơ-le
cũng là tải cảm**.
**Cách sửa:** mạch dập cho **mọi** cuộn dây, kể cả cuộn của rơ-le trung gian (mục 5.5).

### 🔍 BẪY 7 — Tính phụ tải theo dòng làm việc, bỏ qua dòng khởi động

**Hiện tượng:** nguồn sụt áp khi nhiều cơ cấu cùng tác động; lỗi chập chờn rất khó tìm và hay bị chẩn
đoán nhầm thành lỗi phần mềm (Chương 8, mục 8.7).
**Cách sửa:** nhân hệ số 1,3–1,5, và tính theo **bước có nhiều tải cùng bật nhất** trong trình tự.

### 🔍 BẪY 8 — Dùng màu đèn tháp theo ý mình

**Hiện tượng:** người vận hành phản ứng sai vì họ đi theo thói quen từ các máy khác trong xưởng.
**Cách sửa:** theo quy ước màu chuẩn và **thống nhất toàn nhà máy** (mục 5.6).

### 🔍 BẪY 9 — Còi kêu liên tục khi có lỗi

**Hiện tượng:** người vận hành **tháo còi** hoặc rút dây. Từ đó máy mất hẳn khả năng báo động bằng âm
thanh, và không ai nhớ điều đó.
**Cách sửa:** còi kêu bằng **xung có độ dài xác định** khi có báo động mới (mục 5.6, Chương 17).

### 🔍 BẪY 10 — Viết logic riêng cho đèn tháp

**Hiện tượng:** đèn xanh sáng trong khi máy đã dừng, hoặc đèn đỏ không sáng khi có lỗi — vì logic đèn
và logic máy lệch nhau sau vài lần sửa.
**Cách sửa:** đèn nối **thẳng** vào biến trạng thái máy (mục 5.6, Chương 25).

---

## 5.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Tải cảm gồm những gì | Cuộn van · cuộn contactor · **cuộn rơ-le trung gian** |
| Mọi tải cảm cần gì | ⭐ **Mạch dập** — không có ngoại lệ |
| Tải DC dùng gì | **Diode ngược**, cực âm về phía +24 V |
| Tải AC dùng gì | **RC** hoặc **varistor** |
| Đấu diode ngược chiều thì | ⚠⚠ **Ngắn mạch nguồn** — kiểm trước khi cấp điện |
| Diode làm van chậm đi | Vài ms. Chỉ quan trọng với van tác động nhanh |
| Đặt mạch dập ở đâu | ⭐ **Càng gần cuộn càng tốt** |
| Hậu quả khó tìm nhất khi thiếu mạch dập | ⭐ **Nhiễu lan ra cả tủ** — triệu chứng không liên quan |
| Rơ-le trung gian đáng có vì | Thay rẻ · cách ly thật · **điểm đo khi chẩn đoán** · gỡ bài toán chân chung |
| Contactor nên có gì về PLC | **Tiếp điểm phụ** — biết đã đóng thật chưa |
| Van giữ hai vị trí | Khoá lẫn **cả phần mềm lẫn phần cứng** |
| Màu đèn tháp | Theo tiêu chuẩn, **thống nhất toàn nhà máy** |
| Logic đèn tháp | ⭐ Nối **thẳng** vào biến trạng thái, không viết riêng |
| Còi | **Xung** khi có báo động mới, không kêu liên tục |
| Tính phụ tải 24 V | Bước **nhiều tải cùng bật nhất** × **1,3–1,5** |

---

## 5.11 Tự kiểm

1. Viết công thức xung áp ngược của tải cảm và giải thích vì sao transistor cắt nhanh làm xung cao hơn.
2. ⭐ Nêu **ba** hậu quả của việc thiếu mạch dập. Hậu quả nào tốn thời gian tìm nhất, và vì sao?
3. Tải DC và tải AC dùng mạch dập gì? Chuyện gì xảy ra nếu đấu diode ngược chiều, và kiểm thế nào
   trước khi cấp điện?
4. Vì sao diode ngược làm van nhả chậm hơn? Khi nào điều đó quan trọng và khi nào không?
5. Vì sao mạch dập nên đặt càng gần cuộn dây càng tốt? Đặt xa thì mất lợi ích gì?
6. ⭐ Nêu sáu lý do dùng rơ-le trung gian. Hai lý do nào nói về **lúc máy hỏng**?
7. Đã lắp rơ-le trung gian rồi mà ngõ ra vẫn hỏng. Nguyên nhân khả dĩ nhất là gì?
8. Vì sao nên đưa tiếp điểm phụ của contactor về PLC? Nêu ba hỏng hóc mà nó phát hiện được.
9. ⭐ Vì sao quy ước màu đèn tháp là **quy ước có tiêu chuẩn**, không phải sở thích thiết kế?
10. Vì sao còi không nên kêu liên tục khi có lỗi? Hậu quả thực tế là gì?
11. Vì sao logic đèn tháp không nên viết riêng mà phải nối thẳng vào biến trạng thái máy?
12. ⭐ Khi tính công suất nguồn 24 V, vì sao phải tìm **bước có nhiều tải cùng bật nhất** thay vì cộng
    tất cả hoặc lấy trung bình?

> Câu 2, 6, 9 và 12 là bốn câu phân loại. Câu 2 là tinh thần của cả chương: **linh kiện rẻ nhất trong
> tủ thường là linh kiện quyết định máy chạy được bao lâu.**

---

### Chương tiếp theo

Chương 6 — **Khí nén cho máy tự động hoá**. Chương này nói về phía **điện** của cơ cấu chấp hành;
chương sau nói về phía **khí** — van 5/2 và 5/3, xy-lanh, chân không, và quyết định quan trọng nhất
của cả hai chương: *mất năng lượng thì cơ cấu về đâu*.

### Nguồn tham khảo chương 5

- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu với mạch điều
  khiển, thiết bị chỉ báo và tín hiệu, và quy ước màu. *(tiêu chuẩn có bản quyền)*
- IEC 60947-5-1 — *Low-voltage switchgear and controlgear — Control circuit devices*: đặc tính tiếp
  điểm, loại tải, và tuổi thọ điện — dùng khi chọn rơ-le trung gian.
- IEC 61131-2 — *Programmable controllers, Part 2*: đặc tính ngõ ra của module PLC.
- **Datasheet của van điện từ, contactor và rơ-le** — dùng cho dòng làm việc, dòng khởi động, và ⚠
  **có sẵn mạch dập trong đầu nối hay không**. Đây là thông số phải tra theo đúng mã sản phẩm.
- Bảng I/O và mô tả trình tự của DP-01 — Phụ lục J; bước "nhiều tải cùng bật nhất" ở mục 5.7 lấy từ
  mô tả trình tự.

> ⚡ Hệ số dự phòng 1,3–1,5 ở mục 5.7 là **quy tắc thực dụng của nghề**, không phải giá trị chuẩn hoá.
> Với tải có dòng khởi động rất cao hoặc máy dự kiến mở rộng nhiều, hệ số phải cao hơn — và cách chắc
> chắn nhất vẫn là **đo điện áp 24 V bằng máy hiện sóng đúng lúc nhiều cơ cấu cùng tác động**
> (Chương 52, mục 52.3).
>
> ⚠ Quy ước màu ở mục 5.6 là **quy ước thông dụng**; quy ước chính thức phải lấy từ tiêu chuẩn hiện
> hành tại thị trường của bạn và từ quy định của cơ sở. Khi hai nguồn khác nhau, **quy định của cơ sở
> thắng** — vì thứ quyết định an toàn là người vận hành phản ứng đúng theo thói quen của họ.
