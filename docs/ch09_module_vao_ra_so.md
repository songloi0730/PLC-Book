# Chương 9 — Module vào/ra số: chọn đúng kiểu

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 9.1 Bài toán: module ngõ ra cháy sau ba tiếng

Một cỗ máy vừa lắp xong. Bật nguồn, nạp chương trình, chạy thử. Mọi thứ hoạt động.

Ba tiếng sau, module ngõ ra bốc khói.

Nguyên nhân: một cuộn van 24 VDC được đấu vào module ngõ ra **rơ-le** — đúng loại, không sao. Nhưng
người thiết kế tủ đã đấu **tám cuộn van vào chung một chân chung** *(common)*, và tổng dòng qua chân
chung đó vượt giới hạn của module. Mỗi kênh riêng lẻ đều nằm trong định mức; **tổng thì không**.

Datasheet có ghi con số đó. Nó nằm ở một dòng khác với dòng ghi "2 A mỗi kênh", và không ai đọc tới.

Chương này về việc chọn đúng loại module và đọc đúng những con số quyết định — trước khi đấu dây, vì
sau đó thì phải đấu lại.

---

## 9.2 Ngõ vào số — sink hay source

Chương 4 đã dạy PNP/NPN từ phía **cảm biến**. Chương này nhìn từ phía **module**, và hai cách gọi này
hay bị nhầm lẫn.

| | Ngõ vào kiểu **sink** | Ngõ vào kiểu **source** |
|---|---|---|
| Module làm gì | **Nhận** dòng từ cảm biến | **Cấp** dòng ra cảm biến |
| Ghép với cảm biến | **PNP** | **NPN** |
| Chân chung nối vào | 0 V | +24 V |

> ⚠ **Quy tắc nhớ: ngõ vào sink ghép với cảm biến PNP.**
> Hai chữ khác nhau nhưng đi cùng nhau. Lý do: cảm biến PNP **đẩy** +24 V ra dây tín hiệu, nên module
> phải **nhận** dòng đó về — tức là sink. Nhớ nhầm cặp này là nguồn gốc của loạt lỗi ở Chương 4.

Nhiều module hiện nay là **kiểu chuyển được** *(sink/source selectable)*: đấu chân chung vào 0 V thì
thành sink, đấu vào +24 V thì thành source. Rất tiện — và cũng là một chỗ dễ đấu sai, vì cùng một
module có thể hành xử hai kiểu tuỳ cách đấu một sợi dây.

> 💡 **MẸO** — ghi rõ kiểu đã chọn **trên bản vẽ và trên nhãn trong tủ**, không chỉ trong đầu người
> thiết kế. Người sửa máy hai năm sau không đoán được từ hình dáng module.

### Ba thông số phải đọc

| Thông số | Nghĩa | Hậu quả khi bỏ qua |
|---|---|---|
| **Điện áp danh định** | Thường 24 VDC ở máy tự động hoá; cũng có loại 110/230 VAC | Sai điện áp: không đọc được, hoặc hỏng module |
| **Loại ngõ vào theo IEC 61131-2** (loại 1 / 2 / 3) | Quy định ngưỡng áp và dòng để coi là mức 0 hoặc mức 1 | Cảm biến "dính" ở mức 1 — xem bên dưới |
| **Thời gian lọc** *(input filter time)* | Lọc nhiễu phần cứng, thường vài trăm µs tới vài ms | Xung nhanh **không được nhìn thấy** (Chương 18, mục 18.5) |

### ⚠ Dòng rò làm ngõ vào "dính"

Cảm biến hai dây và một số thiết bị bán dẫn có **dòng rò** *(leakage current)* — vẫn cho một dòng nhỏ
chạy qua ngay cả khi ở trạng thái tắt.

Nếu dòng rò đủ lớn so với ngưỡng của ngõ vào, module đọc thành mức 1 **dù cảm biến đang tắt**. Triệu
chứng: một ngõ vào **luôn bằng 1**, hoặc bằng 1 khi lẽ ra phải bằng 0, và đo bằng đồng hồ vạn năng
thì thấy điện áp "gần 24 V".

Ba cách chữa, theo thứ tự ưu tiên:

1. **Dùng cảm biến ba dây** thay cho hai dây, nếu còn kịp chọn.
2. **Chọn module có loại ngõ vào chịu được dòng rò cao hơn** (ngưỡng dòng tối thiểu để coi là mức 1
   lớn hơn).
3. **Lắp điện trở xả** *(bleeder resistor)* song song với ngõ vào để dòng rò chảy qua đó — cách cuối
   cùng, vì nó thêm linh kiện và thêm nhiệt trong tủ.

Chi tiết về cảm biến hai dây ở Chương 4.

---

## 9.3 ⭐ Ngõ ra số — ba loại, ba bài toán khác nhau

Đây là mục quan trọng nhất chương. Chọn sai loại ngõ ra là lỗi **không sửa được bằng phần mềm**.

| | **Rơ-le** *(relay)* | **Transistor** | **Triac** |
|---|---|---|---|
| Đóng cắt được | **AC và DC** | **Chỉ DC** | **Chỉ AC** |
| Dòng mỗi kênh | Lớn nhất (thường vài ampe) | Nhỏ hơn (thường vài trăm mA) | Trung bình |
| Tốc độ đóng cắt | **Chậm** — vài mili-giây | **Nhanh** — micro-giây | Trung bình |
| Tuổi thọ | ⚠ **Hữu hạn** — số lần đóng cắt cơ khí | Gần như không giới hạn | Không có tiếp điểm cơ khí |
| Dòng rò khi tắt | **Không** (cách ly cơ khí thật) | ⚠ Có | ⚠ Có |
| Sụt áp khi dẫn | Rất nhỏ | Có, khoảng 0,5–1,5 V | Có |
| Giá | Thấp | Trung bình | Trung bình |

### Chọn theo ba câu hỏi

> **Câu 1 — Tải là AC hay DC?**
> DC → rơ-le hoặc transistor. AC → rơ-le hoặc triac. Đây là câu loại trừ đầu tiên.
>
> **Câu 2 — Đóng cắt bao nhiêu lần trong đời máy?**
> Đây là câu người mới hay bỏ qua, và là câu quyết định giữa rơ-le với transistor.
>
> **Câu 3 — Cần nhanh tới mức nào?**
> Vài mili-giây có chấp nhận được không? Nếu không thì phải transistor.

### ⚠ Tuổi thọ rơ-le — phép tính phải làm

Tiếp điểm rơ-le mòn theo **số lần đóng cắt**, không theo thời gian. Datasheet ghi tuổi thọ cơ khí và
tuổi thọ điện (tuổi thọ điện thấp hơn nhiều, và phụ thuộc loại tải).

Phép tính bắt buộc khi định dùng rơ-le cho tải đóng cắt thường xuyên:

```text
Số lần/chu trình  ×  chu trình/giờ  ×  giờ/ngày  ×  ngày/năm  =  số lần/năm
```

Với DP-01: van chặn trạm 1 đóng cắt **2 lần mỗi board**, máy làm ~1 200 board mỗi ca, 2 ca mỗi ngày,
300 ngày mỗi năm:

```text
2 × 1200 × 2 × 300 = 1 440 000 lần/năm
```

Một triệu tư lần mỗi năm. Với tuổi thọ điện điển hình của rơ-le trong module I/O, con số này nghĩa là
**thay module sau vài tháng tới hơn một năm** — và thay vào lúc nào thì không biết trước, tức là dừng
máy đột xuất.

> **Kết luận cho DP-01: mọi van khí dùng ngõ ra transistor, không dùng rơ-le.**
> Đây là quyết định **lúc mua module**. Phát hiện sau khi máy đã chạy nghĩa là thay module, đấu lại
> dây, và có thể phải đổi cả cách bố trí tủ.

Ngược lại, rơ-le hợp với: contactor động cơ (đóng cắt vài lần mỗi ca), đèn báo, còi, tín hiệu báo ra
ngoài — những tải đóng cắt **thưa** hoặc cần **cách ly thật**.

### ⚠ Dòng rò của ngõ ra transistor và triac

Transistor và triac **không cắt hoàn toàn** — vẫn có một dòng rò nhỏ khi tắt.

Với cuộn van thì không sao. Nhưng với **tải trở kháng cao** — ngõ vào của một PLC khác, ngõ vào biến
tần, đèn LED công suất rất nhỏ — dòng rò có thể đủ để **thiết bị nhận đọc thành mức 1 dù đã tắt**.

Triệu chứng: đèn LED **mờ mờ không tắt hẳn**, hoặc thiết bị nhận báo có tín hiệu khi không có. Cách
chữa giống mục 9.2: điện trở xả, hoặc chuyển sang ngõ ra rơ-le.

> ⚠ **Đây là lý do ngõ ra rơ-le vẫn tồn tại dù transistor tốt hơn ở nhiều mặt.**
> Rơ-le cách ly **cơ khí thật** — tắt là tắt hẳn, không dòng rò, và cách ly được hai hệ điện khác
> nhau. Với tín hiệu đi ra khỏi máy, sang máy khác, hoặc sang hệ khác điện áp, rơ-le thường là lựa
> chọn đúng.

### ⚠⚠ Tải cảm — bắt buộc có mạch dập

Cuộn van, cuộn contactor, cuộn rơ-le đều là **tải cảm** *(inductive load)*. Khi cắt dòng đột ngột,
điện cảm sinh ra một xung áp ngược rất cao theo `V = L · di/dt`.

Xung này **phá tiếp điểm rơ-le** và **giết transistor**, và nó cũng là **nguồn nhiễu** lan vào cả tủ.

> ⚠⚠ **NGUY HIỂM CHO THIẾT BỊ — mạch dập không phải tuỳ chọn**
> Mọi tải cảm phải có mạch dập *(snubber / suppression)*:
> - **Tải DC**: diode ngược *(flyback diode)* đấu song song với cuộn, đúng chiều. ⚠ Đấu ngược chiều
>   sẽ **ngắn mạch nguồn**.
> - **Tải AC**: mạch RC hoặc varistor.
>
> Nhiều van điện từ đã có sẵn diode trong đầu nối — **kiểm tra, đừng giả định**. Và khi van đã có
> diode thì không lắp thêm.
>
> Chi tiết mạch dập và cách chọn ở Chương 5.

---

## 9.4 Cách ly quang và chân chung

### Cách ly quang

Phần lớn module I/O số có **cách ly quang** *(optical isolation)*: tín hiệu đi qua một cặp phát–thu
quang, nên **không có đường dẫn điện** giữa mạch hiện trường và mạch bên trong CPU.

Ba lợi ích thực tế:

- Xung áp từ hiện trường không tới được CPU.
- Vòng lặp đất *(ground loop)* giữa hai hệ khác nhau bị cắt (Chương 49).
- Một sự cố ngoài hiện trường ít khả năng lan vào và làm hỏng CPU.

> ⚠ Cách ly quang **không phải cách ly an toàn**. Nó bảo vệ thiết bị, không phải bảo vệ người, và
> không thay thế được yêu cầu về cách ly trong tiêu chuẩn an toàn điện. Xem Chương 3 và Chương 47.

### Chân chung — con số làm cháy module ở mục 9.1

Các kênh trong một module thường được nhóm lại, mỗi nhóm dùng **một chân chung**. Datasheet ghi hai
con số khác nhau, và người ta hay chỉ đọc con số đầu:

| Con số | Nghĩa |
|---|---|
| **Dòng tối đa mỗi kênh** | Một kênh chịu được bao nhiêu |
| ⚠ **Dòng tối đa qua chân chung** | Tổng của **mọi kênh trong nhóm** cộng lại |

Con số thứ hai **luôn nhỏ hơn** tổng của con số thứ nhất nhân số kênh. Nghĩa là **không thể** cho mọi
kênh chạy full tải cùng lúc.

Phép tính bắt buộc, làm theo **trường hợp xấu nhất**:

> **Cộng dòng của mọi tải trong cùng một nhóm chân chung, tại thời điểm nhiều tải nhất cùng bật.**
> So với giới hạn chân chung trong datasheet. Nếu vượt: chia tải ra nhiều nhóm, hoặc chuyển tải lớn
> ra rơ-le trung gian bên ngoài.

Trên DP-01, bốn van khí (chặn và kẹp của hai trạm) **có thể cùng bật** ở một số bước. Nếu bốn van đó
nằm chung một nhóm, phải cộng dòng của cả bốn — không phải tính từng cái một.

> 💡 **MẸO — rơ-le trung gian giải quyết nhiều bài toán cùng lúc**
> Cho ngõ ra PLC điều khiển một rơ-le trung gian nhỏ, rồi rơ-le đó đóng tải thật. Bạn được: dòng tải
> không đi qua module, cách ly thật, dễ thay khi hỏng (thay rơ-le rẻ hơn thay module), và có một điểm
> đo rõ ràng khi chẩn đoán.
>
> Đánh đổi: thêm linh kiện, thêm chỗ trong tủ, thêm một điểm hỏng, và thêm vài mili-giây trễ. Với tải
> lớn hoặc tải đi ra khỏi tủ thì đánh đổi này gần như luôn đáng.

---

## 9.5 Ước tính công suất nguồn 24 V cho I/O

Chương 8 mục 8.7 đã nêu nguyên tắc. Ở đây là cách làm cụ thể cho phần I/O.

| Bước | Việc |
|---|---|
| 1 | Liệt kê **mọi** thiết bị lấy nguồn 24 V, theo bảng I/O |
| 2 | Tra dòng tiêu thụ của từng loại từ datasheet — đừng đoán |
| 3 | Xác định **thời điểm nhiều tải nhất cùng bật** — đọc từ mô tả trình tự (Chương 23) |
| 4 | Cộng dòng tại thời điểm đó |
| 5 | Nhân **1,3–1,5** |

Ước tính cho lát cắt 1 của DP-01:

| Nhóm | Số lượng | Dòng mỗi cái | Ghi chú |
|---|---|---|---|
| Cảm biến quang, PNP | 4 | vài chục mA | Luôn cấp nguồn |
| Reed xy-lanh | 8 | nhỏ | Luôn cấp nguồn |
| Cuộn van khí | 4 | vài trăm mA | ⚠ **Có thể cùng bật** — đây là phụ tải quyết định |
| Đèn tháp + còi | 4 | vài chục mA | |
| Rơ-le trung gian | vài cái | vài chục mA | |

Cuộn van là phụ tải lớn nhất, và **dòng khởi động của chúng cao hơn dòng làm việc**. Đó là lý do hệ
số dự phòng không phải là sự thận trọng thừa.

> ⚠ **Nhắc lại triệu chứng của nguồn thiếu** (Chương 8, mục 8.7): máy chạy bình thường, thỉnh thoảng
> lỗi lạ khi nhiều cơ cấu cùng tác động. Rất hay bị đi tìm trong chương trình. Xác nhận bằng **máy
> hiện sóng**, không bằng đồng hồ vạn năng.

---

## 9.6 Module hỗn hợp — khi nào nên tránh

**Module hỗn hợp** *(combo / mixed I/O module)* có cả ngõ vào và ngõ ra trong một khối, đôi khi thêm
vài kênh analog.

| Ưu | Nhược |
|---|---|
| Rẻ hơn mua riêng | ⚠ Hỏng một phần thì **thay cả khối** |
| Ít chỗ trong tủ | Tỉ lệ vào/ra cố định, thường không khớp nhu cầu |
| Hợp với máy nhỏ, số I/O ít | ⚠ Khó dự phòng: phải trữ nguyên khối, không trữ được từng loại |

> **Quy tắc thực dụng:** module hỗn hợp hợp với **máy nhỏ, số I/O ít, không dự kiến mở rộng**. Với
> máy sản xuất chạy liên tục, module riêng từng loại thường đúng hơn — vì bài toán thật không phải
> giá mua, mà là **thời gian dừng máy khi hỏng** và **chi phí trữ phụ tùng**.

Cùng logic đó áp cho việc chọn số kênh: một module 32 kênh rẻ hơn hai module 16 kênh, nhưng khi nó
hỏng thì mất 32 kênh cùng lúc.

---

## 9.7 Trên máy mẫu DP-01 — chọn cho từng tải

Đây là bài tập tổng hợp của cả chương.

| Tải | Loại | Kiểu ngõ ra chọn | Vì sao |
|---|---|---|---|
| `DO_Stop1Vlv`, `DO_Stop2Vlv` — van chặn | Cuộn van 24 VDC | **Transistor** + diode dập | Đóng cắt ~1,4 triệu lần/năm — rơ-le mòn quá nhanh (mục 9.3) |
| `DO_Clamp1Vlv`, `DO_Clamp2Vlv` — van kẹp | Cuộn van 24 VDC | **Transistor** + diode dập | Như trên |
| `DO_ConvRun` — cho phép chuyền chạy | Ngõ vào số của biến tần | **Transistor** hoặc rơ-le | ⚠ Kiểm **dòng rò** so với ngưỡng ngõ vào biến tần; nếu nghi ngờ thì dùng rơ-le |
| Đèn tháp, còi | 24 VDC, dòng nhỏ | **Transistor** | Đóng cắt thưa; transistor vẫn hợp |
| Contactor động cơ (nếu có) | Cuộn AC | **Rơ-le** + mạch RC | Tải AC — transistor không dùng được |
| Tín hiệu SMEMA sang máy bên cạnh | Sang hệ khác | **Rơ-le**, hoặc cách ly quang riêng | Cần cách ly thật giữa hai máy (Chương 41) |

Hai điều rút ra:

- **Phần lớn ngõ ra của một máy tự động hoá điển hình là transistor**, vì phần lớn tải là van khí
  24 VDC đóng cắt thường xuyên.
- **Rơ-le dành cho ba chỗ**: tải AC, tải lớn, và tín hiệu đi ra khỏi máy.

Với ngõ vào: mọi cảm biến của DP-01 đều là **PNP** (Chương 4), nên module ngõ vào phải là **kiểu
sink**, chân chung đấu 0 V.

---

## 9.8 Khác biệt giữa các hãng

Tên gọi và cách ghi thông số khác nhau; nguyên lý thì không.

| Điểm | Điều cần biết |
|---|---|
| Cách gọi sink/source | ⚠ Một số tài liệu gọi theo phía **module**, một số gọi theo phía **cảm biến** — đọc kỹ sơ đồ đấu trong datasheet thay vì tin vào chữ. Sơ đồ không nói dối |
| Module chuyển được kiểu | Siemens, Mitsubishi, Inovance, Rockwell đều có dòng cho phép chọn sink/source bằng cách đấu chân chung. Kiểm từng mã sản phẩm |
| Loại ngõ vào theo IEC 61131-2 | Không phải datasheet nào cũng ghi rõ "loại 1/2/3" — có hãng ghi thẳng ngưỡng áp và dòng. Cần con số, không cần cái tên |
| ⚠ Giới hạn dòng chân chung | **Luôn có**, nhưng vị trí trong datasheet rất khác nhau — đôi khi ở bảng chính, đôi khi ở chú thích cuối trang. **Tìm cho ra**, đây là con số làm cháy module ở mục 9.1 |
| Ngõ ra triac | Ít gặp ở máy tự động hoá dùng 24 VDC; phổ biến hơn ở ứng dụng điều khiển tải AC |
| Thời gian lọc ngõ vào | Nhiều hệ cho **cấu hình được** bằng phần mềm. Đây là chỗ đáng chỉnh khi cần đọc xung nhanh — nhưng giảm lọc thì tăng nhạy nhiễu (Chương 18) |

Hướng dẫn cấu hình cho từng hệ ở Phụ lục A. Số liệu cụ thể: catalogue và datasheet hiện hành của
hãng, kèm ngày kiểm tra.

---

## 9.9 Bẫy thường gặp

### 🔍 BẪY 1 — Vượt dòng chân chung

Đúng cỗ máy ở mục 9.1. Mỗi kênh trong định mức, tổng thì không.

**Hiện tượng:** module nóng bất thường, rồi hỏng — thường sau vài giờ tới vài ngày, không phải ngay.
**Cách sửa:** cộng dòng theo nhóm chân chung tại thời điểm nhiều tải nhất; chia nhóm hoặc dùng rơ-le
trung gian (mục 9.4).

### 🔍 BẪY 2 — Dùng ngõ ra rơ-le cho van đóng cắt liên tục

**Hiện tượng:** sau vài tháng, một kênh **thỉnh thoảng không tác động**, rồi hỏng hẳn. Tiếp điểm mòn
dần nên triệu chứng đến từ từ và dễ đổ cho cảm biến hoặc cho van.
**Cách sửa:** làm phép tính số lần đóng cắt mỗi năm **trước khi mua module** (mục 9.3).

### 🔍 BẪY 3 — Quên mạch dập cho tải cảm

**Hiện tượng:** tiếp điểm rơ-le cháy rỗ sau thời gian ngắn; transistor chết đột ngột; và **nhiễu lan
khắp tủ** làm các ngõ vào khác đọc sai lung tung.
**Cách sửa:** diode ngược cho tải DC (đúng chiều), RC hoặc varistor cho tải AC. Kiểm xem van đã có
sẵn diode chưa (Chương 5).

### 🔍 BẪY 4 — Đấu diode dập ngược chiều

**Hiện tượng:** ngắn mạch nguồn ngay khi bật — nổ cầu chì, hoặc hỏng nguồn.
**Cách sửa:** diode đấu **ngược chiều dòng làm việc**: cực âm về phía +24 V. Kiểm bằng đồng hồ trước
khi cấp điện.

### 🔍 BẪY 5 — Ghép nhầm PNP với ngõ vào source

**Hiện tượng:** đèn trên cảm biến sáng khi có vật, nhưng bit trong PLC **không lên**. Đây là triệu
chứng kinh điển, và nó khiến người ta nghi cảm biến hỏng.
**Cách sửa:** cảm biến PNP → ngõ vào **sink**, chân chung 0 V. Nếu module chuyển được kiểu thì đổi
cách đấu chân chung (Chương 4, Chương 52 mục 52.4).

### 🔍 BẪY 6 — Dòng rò làm ngõ vào dính ở mức 1

**Hiện tượng:** một ngõ vào luôn bằng 1; đo được điện áp "gần 24 V" ngay cả khi cảm biến tắt.
**Cách sửa:** đổi sang cảm biến ba dây; hoặc module có ngưỡng dòng cao hơn; hoặc điện trở xả (mục 9.2).

### 🔍 BẪY 7 — Dòng rò ngõ ra transistor làm thiết bị nhận đọc nhầm

**Hiện tượng:** đèn LED mờ mờ không tắt hẳn; hoặc biến tần / PLC bên cạnh báo có tín hiệu khi PLC đã
tắt ngõ ra.
**Cách sửa:** điện trở xả, hoặc chuyển kênh đó sang ngõ ra rơ-le (mục 9.3).

### 🔍 BẪY 8 — Chọn module hỗn hợp cho máy sản xuất liên tục

**Hiện tượng:** hỏng hai kênh ngõ ra, phải thay cả khối, mất luôn các kênh ngõ vào đang tốt — và
dừng máy lâu hơn dự kiến.
**Cách sửa:** cân nhắc theo **thời gian dừng máy và chi phí phụ tùng**, không chỉ theo giá mua
(mục 9.6).

### 🔍 BẪY 9 — Giảm thời gian lọc ngõ vào để "đọc nhanh hơn"

**Hiện tượng:** đọc được xung nhanh hơn thật, nhưng **thêm cả nhiễu** — ngõ vào lên xuống ngẫu nhiên,
bộ đếm nhảy.
**Cách sửa:** nếu cần đọc xung nhanh, dùng bộ đếm tốc độ cao thay vì hạ lọc (Chương 18, mục 18.5).
Hạ lọc chỉ khi đã xử lý xong nhiễu ở tầng đi dây và nối đất (Chương 49).

---

## 9.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Cảm biến PNP thì module ngõ vào loại gì | **Sink**, chân chung 0 V |
| Tải DC đóng cắt liên tục | **Transistor** |
| Tải AC | **Rơ-le** hoặc **triac** |
| Tải lớn, hoặc tín hiệu đi ra khỏi máy | **Rơ-le** — cách ly thật, không dòng rò |
| Trước khi chọn rơ-le | Tính **số lần đóng cắt mỗi năm** |
| Mọi tải cảm | **Bắt buộc** mạch dập — diode (DC) hoặc RC/varistor (AC) |
| Hai con số phải đọc trong datasheet | Dòng **mỗi kênh** *và* dòng **qua chân chung** |
| Cộng dòng thế nào | Theo **trường hợp xấu nhất** — lúc nhiều tải cùng bật |
| Ngõ vào luôn bằng 1 | Nghi **dòng rò** của cảm biến hai dây |
| Ngõ ra tắt mà thiết bị nhận vẫn thấy tín hiệu | Nghi **dòng rò** transistor/triac |
| Module hỗn hợp | Máy nhỏ thì được; máy chạy liên tục thì cân nhắc thời gian dừng máy |
| Cách ly quang | Bảo vệ **thiết bị**, ⚠ không phải cách ly an toàn cho người |

---

## 9.11 Tự kiểm

1. Cảm biến PNP ghép với ngõ vào kiểu gì? Giải thích bằng chiều dòng điện, đừng học thuộc.
2. Nêu ba loại ngõ ra số và cho biết loại nào đóng cắt được tải AC.
3. ⭐ Van khí đóng cắt 2 lần mỗi sản phẩm, máy làm 1 200 sản phẩm mỗi ca, 2 ca mỗi ngày, 300 ngày mỗi
   năm. Tính số lần đóng cắt mỗi năm và kết luận nên dùng loại ngõ ra nào.
4. Vì sao ngõ ra rơ-le vẫn được dùng dù transistor nhanh hơn và bền hơn? Nêu ba trường hợp rơ-le là
   lựa chọn đúng.
5. ⭐ Giải thích vì sao "mỗi kênh 2 A" **không** có nghĩa là module 8 kênh chịu được 16 A. Con số nào
   phải tìm trong datasheet?
6. Một ngõ vào luôn bằng 1 dù cảm biến đã tắt; đo được gần 24 V. Nguyên nhân khả dĩ nhất là gì, và
   nêu ba cách chữa theo thứ tự ưu tiên.
7. Vì sao mọi tải cảm phải có mạch dập? Nêu loại mạch dập cho tải DC và cho tải AC, và hậu quả khi
   đấu diode ngược chiều.
8. Cách ly quang bảo vệ cái gì và **không** bảo vệ cái gì?
9. Nêu ưu và nhược của module hỗn hợp. Với máy sản xuất chạy liên tục, tiêu chí nào quan trọng hơn
   giá mua?
10. ⭐ Đèn trên cảm biến sáng khi có vật, nhưng bit trong PLC không lên. Nêu **hai** nguyên nhân khả
    dĩ khác nhau về bản chất và cách phân biệt chúng bằng phép đo.

> Câu 3, 5 và 10 là ba câu phân loại. Câu 5 là tinh thần của cả chương: **con số làm hỏng thiết bị
> thường không phải con số in to nhất trong datasheet.**

---

### Chương tiếp theo

Chương 10 — **Vòng quét**. Bạn đã có phần cứng: CPU, module, cách tín hiệu đi vào đi ra. Chương sau
nói về **cách PLC chạy chương trình** — bốn giai đoạn lặp mãi mãi, và vì sao hiểu chúng là điều kiện
để hiểu mọi thứ còn lại của cuốn sách.

### Nguồn tham khảo chương 9

- IEC 61131-2 — *Programmable controllers, Part 2: Equipment requirements and tests*: phân loại ngõ
  vào số (loại 1/2/3), ngưỡng điện áp và dòng, yêu cầu với ngõ ra, và các phép thử.
  *(tiêu chuẩn có bản quyền)*
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu chung với mạch điều
  khiển và với việc bảo vệ mạch.
- IEC 60947-5-1 — *Low-voltage switchgear and controlgear — Control circuit devices*: đặc tính tiếp
  điểm và loại tải, dùng khi tra tuổi thọ điện của ngõ ra rơ-le.
- **Datasheet module I/O của các hãng** (Siemens, Mitsubishi, Inovance, Rockwell, Omron, Beckhoff…) —
  dùng cho mọi số liệu cụ thể: dòng mỗi kênh, **dòng qua chân chung**, tuổi thọ tiếp điểm, dòng rò,
  thời gian lọc ngõ vào, kiểu sink/source. Đây là các con số **phải tra theo đúng mã sản phẩm**.
- Bảng I/O và mô tả trình tự của DP-01 — Phụ lục J.

> ⚡ **Về các con số trong chương này.** Sách cố ý ghi dải ("vài trăm mA", "vài ampe") thay vì con số
> chính xác, vì chúng khác nhau giữa các mã sản phẩm và đổi theo đời. Phép tính tuổi thọ ở mục 9.3
> dùng **số lần đóng cắt của máy** — con số này bạn tính được chính xác từ trình tự của mình — rồi so
> với **tuổi thọ điện trong datasheet của module cụ thể**. Đừng lấy con số của module này áp cho
> module khác.
