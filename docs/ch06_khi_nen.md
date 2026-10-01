# Chương 6 — Khí nén cho máy tự động hoá

---

> ⚠⚠ **ĐỌC TRƯỚC — phạm vi và giới hạn của chương này**
>
> Khí nén là **năng lượng tích trữ**: một hệ đã ngắt nguồn vẫn còn đủ khí để đẩy cơ cấu đi hết hành
> trình. Vì vậy chương này chạm tới an toàn tính mạng, không chỉ tới tuổi thọ thiết bị.
>
> Chương này giúp bạn **hiểu hệ khí nén đủ để điều khiển nó cho đúng**. Nó **không**:
> - không thay thế **thiết kế hệ khí nén** cho cỗ máy cụ thể của bạn;
> - không thay thế việc **tính chọn** xy-lanh, van và đường ống theo tài liệu nhà sản xuất;
> - không thay thế **quy trình cô lập năng lượng (LOTO)** do cơ sở của bạn ban hành.
>
> Ba việc trên phải do **người có thẩm quyền** thực hiện, dựa trên bản gốc tiêu chuẩn (ISO 4414,
> IEC 60204-1) và trên đúng cỗ máy đó. Các hệ số và quy tắc thực dụng trong chương là để bạn **ước
> lượng và đặt câu hỏi đúng**, không phải để bạn tự kết luận.

---

## 6.1 Vì sao chương này có trong một cuốn sách về PLC

Bạn viết chương trình điều khiển. Bạn không thiết kế hệ khí nén. Vậy vì sao phải đọc chương này?

Ba lý do rất thực tế:

- **Phần lớn cơ cấu bạn điều khiển là xy-lanh khí.** Bạn ra lệnh cho van; hiểu van và xy-lanh làm gì
  sau lệnh đó là điều kiện để viết đúng.
- **Quyết định "mất khí thì cơ cấu về đâu" là quyết định điều khiển**, nhưng nó được thực hiện bằng
  **cách chọn van** — một quyết định cơ khí. Nếu bạn không tham gia lúc chọn van, bạn sẽ phải sống với
  hậu quả ở Chương 48.
- **Rất nhiều sự cố "lỗi phần mềm" thực ra là vấn đề khí nén**: xy-lanh chậm dần vì rò, cơ cấu giật
  cục vì tiết lưu sai chiều, van kẹt vì khí bẩn. Không biết những thứ này thì bạn sẽ đi tìm lỗi trong
  code — nơi không có lỗi nào.

Chương này là lượng khí nén **tối thiểu đủ để làm việc**, viết cho người điều khiển chứ không cho
người thiết kế hệ khí.

---

## 6.2 Chuẩn bị khí — khâu quyết định tuổi thọ

Khí từ máy nén đi ra mang theo ba thứ không mong muốn: **nước**, **hạt bụi**, và **dầu** từ máy nén.
Cả ba đều phá van và xy-lanh.

Cụm chuẩn bị khí quen gọi tắt là **FRL** *(Filter – Regulator – Lubricator: lọc – điều áp – tra dầu)*:

| Khối | Làm gì | Ghi chú |
|---|---|---|
| **Lọc** *(filter)* | Tách nước và hạt | ⭐ Quan trọng nhất. Nước là thứ giết van nhiều nhất |
| **Điều áp** *(regulator)* | Đặt áp suất làm việc ổn định | Áp vào dao động, áp ra phải ổn định |
| **Tra dầu** *(lubricator)* | Đưa dầu bôi trơn vào khí | ⚠ **Van hiện đại phần lớn không cần dầu** — xem cảnh báo dưới |

> ⚠ **NGUY HIỂM CHO THIẾT BỊ**
> Van hiện đại thường được bôi trơn sẵn từ nhà máy và **thiết kế để chạy với khí khô**. Cho dầu vào
> có thể **rửa trôi lớp bôi trơn gốc** và làm van hỏng nhanh hơn.
>
> Và quan trọng hơn: một khi đã tra dầu thì **không quay lại được** — hệ đã nhiễm dầu, mọi van thay
> mới sau đó cũng phải tiếp tục được tra dầu. Đây là quyết định một chiều.
>
> **Tra dầu hay không phải theo yêu cầu của nhà sản xuất van**, không theo thói quen.

### Vì sao nước là kẻ thù số một

Khí nén nóng chứa được nhiều hơi nước. Khi nó nguội đi trên đường ống, **nước ngưng tụ**. Nước trong hệ:

- Rửa trôi lớp bôi trơn trong van và xy-lanh → mòn nhanh, kẹt.
- Gây gỉ ở chi tiết thép.
- Đọng lại rồi bị thổi vào van thành từng ngụm khi máy khởi động.
- Với máy trong phòng lạnh: nguy cơ đóng băng ở chỗ giãn nở.

Vì vậy: lọc phải có **xả nước** — tự động thì tốt, thủ công thì phải có người xả. Bộ lọc đầy nước là
bộ lọc không còn tác dụng.

### Van khởi động êm

Khi cấp khí lại sau khi dừng, áp suất dựng lên đột ngột làm **mọi xy-lanh chuyển động cùng lúc, rất
nhanh**. Đó là tình huống nguy hiểm và cũng làm hỏng cơ cấu.

**Van khởi động êm** *(soft-start)* cho áp tăng từ từ. Nó thường đi cùng van cô lập có khoá — xem mục 6.7.

---

## 6.3 Van điều khiển — và câu hỏi "mất điện thì về đâu"

### Cách đọc tên van

Van khí ký hiệu theo dạng **số cửa / số vị trí**:

| Ký hiệu | Nghĩa | Dùng cho |
|---|---|---|
| **3/2** | 3 cửa, 2 vị trí | Xy-lanh tác động đơn (lò xo về), chân không |
| **5/2** | 5 cửa, 2 vị trí | ⭐ Xy-lanh tác động kép — loại phổ biến nhất |
| **5/3** | 5 cửa, 3 vị trí | Khi cần vị trí giữa — xem dưới |

### 5/2 — hai kiểu, hành xử khác hẳn khi mất điện

| Kiểu | Cấu tạo | Mất điện thì | Dùng khi |
|---|---|---|---|
| **Một cuộn, lò xo về** | 1 cuộn hút + lò xo | ⭐ **Về vị trí lò xo** — xác định được | Khi có một vị trí an toàn rõ ràng |
| **Hai cuộn (có nhớ)** | 2 cuộn hút, không lò xo | ⭐ **Giữ nguyên vị trí đang có** | Khi cần giữ nguyên hiện trạng |

Đây là **quyết định điều khiển quan trọng nhất trong chương**, và nó nối thẳng vào Chương 48:

> **Van một cuộn lò xo về** = "mất điện thì về vị trí đã định trước".
> **Van hai cuộn** = "mất điện thì giữ nguyên đang ở đâu".
>
> Chọn cái nào phụ thuộc **trạng thái nào là an toàn** cho cơ cấu đó — và câu trả lời khác nhau tuỳ
> cơ cấu (Chương 48, mục 48.2).

Với DP-01: van chặn dùng **một cuộn lò xo về vị trí chặn nâng** (mất điện thì chặn lên, board không
đi qua). Van kẹp dùng **hai cuộn** (mất điện thì giữ kẹp, board không trôi).

### ⚠⚠ Mất ĐIỆN và mất KHÍ là hai chuyện khác nhau

Bảng trên trả lời câu *"mất điện thì về đâu"*. ⭐ **Nó KHÔNG trả lời câu "mất khí thì về đâu"** — và
người mới rất dễ gộp hai câu đó làm một.

| Mất cái gì | Van hai cuộn làm gì | ⭐ Xy-lanh làm gì |
|---|---|---|
| **Mất điện** (còn khí) | Giữ nguyên vị trí van | ⭐ Giữ nguyên — vẫn còn áp đẩy |
| ⚠⚠ **Mất khí** | Giữ nguyên vị trí van | ⚠ **MẤT LỰC HOÀN TOÀN** — vị trí do ngoại lực quyết định |

> ⚠⚠ **NGUY HIỂM — van giữ vị trí KHÔNG phải cơ cấu giữ tải.**
>
> Van hai cuộn (và cả van 5/3 vị trí giữa đóng) chỉ giữ **vị trí của con trượt trong van**. Nó không
> giữ được tải, vì hai lý do vật lý:
>
> | Lý do | Hệ quả |
> |---|---|
> | ⭐ **Khí nén được** | Tải nặng nén khối khí trong xy-lanh → cơ cấu **trôi dần** |
> | ⭐ **Mọi con trượt đều rò** | Khí thoát dần qua khe con trượt → cơ cấu **tụt từ từ** |
>
> ⚠ Với cơ cấu mà **trọng lực làm nó đi xuống**, hai lý do trên nghĩa là: mất khí thì tải **tụt** —
> chậm hoặc nhanh, nhưng nó tụt.
>
> ⭐⭐ **Muốn giữ tải thật thì phải có cơ cấu riêng**, lắp **sát cửa xy-lanh**:
>
> | Cách | Nguyên lý |
> |---|---|
> | ⭐ **Van một chiều điều khiển** *(pilot-operated check valve)* — thường dùng theo cặp | Nhốt khí lại trong xy-lanh; chỉ mở khi có tín hiệu khí điều khiển |
> | ⭐ **Khoá cần cơ khí** *(rod lock)* | Kẹp cơ khí giữ cần xy-lanh |
>
> ⚠ Lắp xa cửa xy-lanh thì đoạn ống giữa van và xy-lanh vẫn xả — và cơ cấu vẫn tụt đúng bằng thể tích
> đoạn ống đó.
>
> ⭐ **Đây là quy tắc song song với trục servo có tải treo** (Chương 37, Bẫy 6): ở đó mất mô-men là
> rơi nên cần **phanh cơ khí**; ở đây mất khí là tụt nên cần **van giữ tải hoặc khoá cần**. Cùng một
> bài học ở hai công nghệ.
>
> *(ISO 4414 — *Pneumatic fluid power: General rules and safety requirements for systems and their
> components* — nêu yêu cầu về giữ tải trong hệ khí nén. ⚠ Sách này **không dẫn số điều khoản**; khi
> thiết kế phải đọc **bản gốc tiêu chuẩn** và tài liệu nhà sản xuất.)*

> 🔍 **BẪY — van hai cuộn khi cả hai cuộn cùng có điện**
> Van hai cuộn không có lò xo, nên nếu chương trình lỡ cấp điện **cả hai cuộn cùng lúc**, hành vi
> **không xác định** — tuỳ van, có thể kẹt giữa, có thể theo cuộn nào có điện trước.
>
> Trong chương trình phải **khoá chéo**: hai lệnh không bao giờ cùng bật. Đây là việc của khối cơ cấu
> ở Chương 27 — viết một lần, áp cho mọi van hai cuộn.

### 5/3 — ⭐ ba kiểu vị trí giữa, khác nhau hoàn toàn

Van 5/3 có vị trí giữa khi **không cuộn nào có điện**. Có ba kiểu, và **chúng làm ba việc khác nhau**:

| Kiểu vị trí giữa | Ở vị trí giữa | Xy-lanh sẽ | Dùng khi |
|---|---|---|---|
| **Kín giữa** *(closed centre)* | Mọi cửa bị chặn, khí bị nhốt trong cả hai buồng | **Đứng lại tại chỗ**, nhưng ⚠ **trôi dần** do rò và do khí nén được | Cần dừng giữa hành trình |
| **Hở giữa / xả giữa** *(exhaust / open centre)* | Cả hai buồng **xả ra khí quyển** | **Tự do** — đẩy được bằng tay, và **tải sẽ kéo nó đi** | Cần đẩy bằng tay khi căn chỉnh |
| **Áp giữa** *(pressure centre)* | Cả hai buồng **cùng có áp** | ⚠ **Vẫn duỗi ra** — vì phía không có cần có diện tích lớn hơn | Trường hợp đặc biệt |

> ⚠⚠ **NGUY HIỂM — đây là một trong những nhầm lẫn nguy hiểm nhất về khí nén**
>
> Hai loại "5/3" nghe gần giống nhau nhưng **hành xử ngược nhau khi mất điện**:
> - **Kín giữa**: cơ cấu **đứng lại** — nhưng trôi dần, nên **không được coi là giữ an toàn**.
> - **Hở giữa**: cơ cấu **tự do**. Nếu là trục đứng hoặc có tải, nó sẽ **rơi hoặc bị tải kéo đi ngay lập tức**.
>
> Đặt nhầm loại là đổi từ "cơ cấu đứng yên" thành "cơ cấu rơi". Và trên sơ đồ, hai loại chỉ khác nhau
> ở ký hiệu ô giữa — rất dễ nhìn lướt qua.
>
> **Không loại nào trong ba loại trên là biện pháp giữ an toàn cho người.** Muốn giữ an toàn phải có
> **chốt cơ khí** hoặc **van khoá** đặt sát xy-lanh (Chương 47, 48).

---

## 6.4 Xy-lanh — tính lực và chọn cỡ

### Công thức lực

> 📐 **Lực đẩy ra** (phía không có cần):
> **F_đẩy = p × (π/4) × D²**
>
> 📐 **Lực kéo về** (phía có cần):
> **F_kéo = p × (π/4) × (D² − d²)**
>
> trong đó: `p` = áp suất **tương đối** (áp kế đọc được), `D` = đường kính trong xy-lanh, `d` = đường
> kính cần.
>
> **Điều kiện áp dụng:** lực **tĩnh lý thuyết**; bỏ qua ma sát; bỏ qua áp đối kháng phía xả; xy-lanh
> chuyển động chậm hoặc đứng yên.

Hai hệ quả phải nhớ:

**Một — lực kéo về luôn nhỏ hơn lực đẩy ra**, vì cần chiếm mất một phần diện tích. Chênh lệch có thể
đáng kể với cần to. Nếu công việc nặng nằm ở chiều kéo về, phải tính theo chiều đó.

**Hai — lực thật nhỏ hơn lực lý thuyết.** Ma sát, áp đối kháng do tiết lưu, và tổn thất trên đường ống
đều lấy bớt. Trong thực tế phải nhân với một **hệ số hiệu suất** và chọn xy-lanh có dự trữ:

| Kiểu làm việc | Nên chọn lực lý thuyết gấp bao nhiêu lần tải |
|---|---|
| Giữ tĩnh, chậm | khoảng **1,3–1,5 lần** |
| Chuyển động bình thường | khoảng **2 lần** |
| Chuyển động nhanh, cần gia tốc | **2 lần trở lên**, và phải xét cả năng lượng động |

> ⚡ **LƯU Ý**
> Các hệ số trên là **quy tắc thực dụng để chọn sơ bộ**, không phải giá trị chuẩn hoá. Với ứng dụng
> quan trọng, dùng bảng chọn và phần mềm tính của nhà sản xuất — chúng tính cả áp đối kháng, ma sát
> thật của loại xy-lanh đó, và năng lượng va đập ở cuối hành trình.

### Vì sao không có công thức đơn giản cho tốc độ

Người mới hay hỏi công thức tính tốc độ xy-lanh. **Không có công thức đơn giản đáng tin**, vì tốc độ
phụ thuộc vào cả một chuỗi:

lưu lượng van → tiết diện và chiều dài ống → co nối → tiết lưu → tải và ma sát → áp đối kháng.

Cách làm đúng: dùng **bảng chọn của nhà sản xuất** (tra theo cỡ xy-lanh, hành trình, tải, thời gian
mong muốn), rồi **đo lại trên máy thật** và chỉnh tiết lưu.

> 💡 **MẸO**
> Ghi lại **thời gian hành trình thật của từng xy-lanh** lúc máy vừa chạy tốt. Nó vừa là căn cứ đặt
> timeout ở Chương 26, vừa là mốc để phát hiện xy-lanh chậm dần ở Chương 51.

### Tiêu thụ khí

Cần cho việc chọn máy nén và chọn cỡ ống:

> 📐 **Thể tích khí tự do cho một hành trình:**
> **V = A × L × (p + p₀) / p₀**
>
> `A` = diện tích piston, `L` = hành trình, `p` = áp tương đối, `p₀` = áp khí quyển.
>
> **Điều kiện áp dụng:** một chiều hành trình; chưa tính thể tích ống và tổn thất; kết quả là **thể
> tích khí ở áp suất khí quyển**.

Nhân với số hành trình mỗi phút và cộng mọi cơ cấu để ra nhu cầu tổng.

---

## 6.5 Điều tốc — ⭐ tiết lưu đường xả, không phải đường cấp

Đây là điểm kỹ thuật quan trọng nhất của chương về mặt vận hành.

Muốn xy-lanh chạy chậm lại, bạn đặt **van tiết lưu một chiều** *(flow control)*. Có hai cách lắp, và
chỉ một cách đúng cho gần như mọi trường hợp.

| Cách | Tiết lưu ở đâu | Kết quả |
|---|---|---|
| **Tiết lưu đường cấp** *(meter-in)* | Hạn chế khí **vào** buồng đẩy | ❌ Chuyển động **giật cục**, tốc độ đổi theo tải |
| ⭐ **Tiết lưu đường xả** *(meter-out)* | Hạn chế khí **ra** khỏi buồng đối diện | ✅ Chuyển động **êm**, ổn định |

### Vì sao tiết lưu đường xả cho chuyển động êm

Khí **nén được** — đó là gốc của vấn đề.

Với **tiết lưu đường cấp**: buồng đẩy nạp khí chậm, áp tăng dần. Piston đứng yên cho tới khi áp thắng
ma sát tĩnh, rồi **bật ra đột ngột**, làm áp tụt, rồi lại phải nạp tiếp. Kết quả là chuyển động
giật từng nhịp — hiện tượng quen gọi là **trượt-dính** *(stick-slip)*. Và vì buồng đối diện xả tự do,
tải thay đổi là tốc độ thay đổi theo.

Với **tiết lưu đường xả**: buồng đẩy có đủ áp ngay, còn buồng đối diện xả chậm nên **giữ lại một áp
đối kháng**. Khí bị nén ở cả hai phía tạo ra **hiệu ứng đệm** — piston bị "kẹp" giữa hai áp suất và
chuyển động mượt, ít phụ thuộc tải.

> 🔍 **BẪY — lắp ngược van tiết lưu**
> Van tiết lưu một chiều **có chiều lắp**. Lắp ngược thì nó thành tiết lưu đường cấp, và triệu chứng là:
>
> - Xy-lanh **giật cục**, nhất là khi chạy chậm.
> - Tốc độ **thay đổi theo tải** — nhanh khi không tải, chậm khi có sản phẩm.
> - Chỉnh vít tiết lưu thấy **khó ăn**, vặn nhiều mà tốc độ đổi ít hoặc đổi đột ngột.
>
> Ba triệu chứng này rất hay bị chẩn đoán nhầm thành "xy-lanh hỏng" hoặc "thiếu khí". Kiểm chiều lắp
> trước khi thay linh kiện.

**Ngoại lệ:** với tải kéo (tải kéo piston đi theo chiều chuyển động, như trục đứng đi xuống), tiết lưu
đường xả là **bắt buộc** — nếu không, tải sẽ kéo xy-lanh chạy vượt. Trường hợp này không phải ngoại
lệ mà là ví dụ mạnh nhất cho quy tắc.

---

## 6.6 Chân không & giác hút

Máy điện tử dùng chân không rất nhiều — nhấc board, giữ chi tiết mỏng, cấp phôi.

### Hai cách tạo chân không

| | **Bơm chân không** | **Bộ tạo chân không kiểu tia** *(ejector)* |
|---|---|---|
| Nguyên lý | Bơm cơ khí, thường đặt tập trung | Dùng chính khí nén thổi qua ống thu hẹp |
| Vị trí | Xa điểm dùng | ⭐ **Đặt sát giác hút** |
| Thời gian đáp ứng | Chậm hơn — đường ống dài | **Nhanh** — thể tích nhỏ |
| Tiêu thụ | Điện | **Khí nén, liên tục khi bật** |
| Hợp với | Nhiều điểm hút, chạy liên tục | ⭐ Chu kỳ ngắn, nhiều lần bật/tắt |

Với máy như DP-01 — hút board từng cái, chu kỳ ngắn — **bộ tạo chân không kiểu tia đặt sát giác hút**
thường là lựa chọn đúng, vì thời gian đáp ứng quyết định chu kỳ máy.

> 💡 **MẸO — tiết kiệm khí**
> Bộ tạo chân không kiểu tia **tiêu thụ khí liên tục khi bật**. Nhiều loại có chức năng **giữ chân
> không**: hút tới ngưỡng rồi tự tắt, chỉ bật lại khi độ chân không tụt. Với máy chu kỳ dài, chức năng
> này tiết kiệm đáng kể.

### ⭐ Cảm biến chân không — lại là nguyên tắc phản hồi

Bật chân không **không có nghĩa là đã hút được vật**. Giác hút có thể hở, board có thể lệch, bề mặt
có thể không kín.

> **Luôn có cảm biến chân không xác nhận đã hút được, trước khi cho cơ cấu di chuyển.**

Đây chính là **giám sát phản hồi thay vì tin lệnh** (Chương 48) áp cho chân không. Hậu quả nếu bỏ qua
rất trực quan: cơ cấu nhấc lên, board rơi giữa đường.

Và chiều ngược lại cũng cần: khi nhả, phải xác nhận **đã nhả thật**. Nhiều bộ tạo chân không có chức
năng **thổi ngược** *(blow-off)* — bơm một xung khí ngắn để đẩy vật ra, vì chỉ tắt chân không thôi thì
vật có thể còn dính.

> ⚡ **LƯU Ý — bài toán riêng của board mạch**
> Board mạch có **linh kiện nhô lên** và **bề mặt không phẳng đều**. Hút board cần:
> - Chọn **vị trí hút** ở vùng trống, không có linh kiện — vị trí này khác nhau theo mã hàng, nên nó
>   thuộc về **công thức sản phẩm** (Chương 29).
> - Giác hút **mềm, có nếp gấp** để bù độ không phẳng.
> - ⚠ Đệm giác hút phải là **cao su tiêu tán tĩnh điện** — cao su thường tích điện rất mạnh (Chương 7).

---

## 6.7 An toàn khí nén

Khí nén là **năng lượng tích trữ**. Một ống khí đã ngắt nguồn vẫn còn đủ khí để làm một xy-lanh chuyển
động hết hành trình — và nó sẽ làm vậy vào đúng lúc ai đó vừa tin là máy đã dừng.

> ⚠⚠ **NGUY HIỂM — ba yêu cầu bắt buộc, thiếu một là quy trình cô lập vô nghĩa**
>
> 1. **Van cô lập phải khoá được** — có lỗ để gắn khoá LOTO.
> 2. **Van cô lập phải có cửa xả** — cô lập mà không xả thì khí vẫn nằm trong ống phía sau van.
> 3. **Van cô lập phải đặt ở chỗ với tới được** — nếu phải leo trèo, người ta sẽ bỏ qua nó.
>
> Ba điều này quyết định lúc **thiết kế** và rất tốn để sửa sau khi máy đã lắp (Chương 47, mục 47.10).

Bốn điểm nữa:

- **Cấp khí lại là lúc nguy hiểm.** Áp dựng lên làm mọi cơ cấu chuyển động. Van khởi động êm (mục 6.2)
  giảm chuyện này, nhưng không loại bỏ — vẫn phải kiểm không có người trong máy trước khi cấp khí lại.
- **Ống bị đứt quật rất mạnh.** Ống áp cao bị đứt sẽ văng đi. Cố định ống chắc chắn; dùng cút chống
  bung ở nơi cần.
- **Không dùng khí nén thổi lên người.** Khí có thể xâm nhập qua da và gây tổn thương nghiêm trọng.
- ⚠ **Khí nén thổi tích điện rất mạnh.** Thổi sạch board bằng khí thường là đổi vấn đề bụi lấy vấn đề
  tĩnh điện — phải dùng vòi có ion hoá (Chương 7, Bẫy 8).

---

## 6.8 Bẫy thường gặp

### 🔍 BẪY 1 — Nhầm hai loại vị trí giữa của van 5/3

Bẫy nguy hiểm nhất của chương. Đã mổ xẻ ở mục 6.3: "kín giữa" và "hở giữa" hành xử **ngược nhau** khi
mất điện, và trên sơ đồ chỉ khác nhau ở ký hiệu ô giữa.

Khi nhận máy hoặc khi thay van, **kiểm bằng thực nghiệm**: ngắt khí và xem cơ cấu thật sự làm gì.

### 🔍 BẪY 2 — Lắp ngược van tiết lưu

Đã nêu ở mục 6.5, kèm ba triệu chứng nhận biết. Bẫy này tốn thời gian vì triệu chứng giống với "xy-lanh
hỏng" và "thiếu khí".

### 🔍 BẪY 3 — Coi "kín giữa" là giữ an toàn

Van kín giữa nhốt khí trong hai buồng, nên cơ cấu **đứng lại**. Nhưng khí rò qua khe hở, và cơ cấu
**trôi dần** — có thể vài mm mỗi phút, đủ để gây nguy hiểm sau vài phút.

**Không loại van nào là biện pháp giữ an toàn cho người.** Cần chốt cơ khí hoặc van khoá đặt sát xy-lanh.

### 🔍 BẪY 4 — Tra dầu vào hệ dùng van không cần dầu

Đã cảnh báo ở mục 6.2. Đây là quyết định **một chiều** — sau khi hệ đã nhiễm dầu thì phải tiếp tục mãi.

### 🔍 BẪY 5 — Bộ lọc đầy nước

Bộ lọc có bình chứa nước ngưng. Đầy rồi mà không xả thì nước bị cuốn lại vào hệ — **bộ lọc trở thành
nguồn ô nhiễm**. Cần xả tự động, hoặc một mục trong lịch bảo trì có người chịu trách nhiệm.

### 🔍 BẪY 6 — Bật chân không rồi cho di chuyển ngay

Không xác nhận đã hút được. Board rơi giữa đường. Xem mục 6.6.

### 🔍 BẪY 7 — Đặt timeout xy-lanh theo cảm tính

Timeout quá chặt → báo động giả khi khí hơi yếu. Quá lỏng → mất tác dụng phát hiện.

**Cách đúng:** đo thời gian hành trình thật trên máy, rồi cộng biên. Và ghi con số gốc lại để về sau
so sánh (Chương 51). ⭐ **Cộng bao nhiêu:** đo ít nhất 20 hành trình mỗi chiều ở điều kiện chậm nhất
còn hợp lệ — áp khí thấp nhất cho phép, tải nặng nhất — rồi đặt giới hạn bằng **2 lần giá trị lớn nhất
đo được**, tối thiểu cộng 0,5 s. Đó là quy tắc thực dụng của nghề, không phải giá trị chuẩn; lập luận
và ngưỡng nhắc đi kèm ở Phụ lục O mục O.7.

### 🔍 BẪY 8 — Van cô lập không có cửa xả

Đã cảnh báo ở mục 6.7. Lỗi thiết kế này làm toàn bộ quy trình cô lập năng lượng trở nên vô nghĩa, và
người thực hiện quy trình **tin rằng mình đang an toàn**.

---

## 6.9 Bảng chốt

| # | Việc | Xong khi |
|---|---|---|
| 1 | Chọn **kiểu van cho từng cơ cấu** theo trạng thái an toàn mong muốn | Mỗi van có lý do ghi thành văn (Chương 48) |
| 2 | Với van 5/3, **xác nhận đúng kiểu vị trí giữa** | Đã kiểm bằng thực nghiệm ngắt khí, không chỉ đọc sơ đồ |
| 3 | Van hai cuộn có **khoá chéo trong chương trình** | Có, ở tầng cơ cấu (Chương 27) |
| 4 | Tính lực xy-lanh theo **chiều làm việc nặng nhất**, có dự trữ | Có |
| 5 | Tiết lưu lắp ở **đường xả** | Đã kiểm chiều lắp từng van |
| 6 | **Đo và ghi thời gian hành trình thật** của từng xy-lanh | Có — dùng cho timeout và cho so sánh về sau |
| 7 | Chân không có **cảm biến xác nhận** và có **thổi ngược** khi nhả | Có |
| 8 | Đệm giác hút là **cao su tiêu tán tĩnh điện** | Có (Chương 7) |
| 9 | Van cô lập **khoá được · có cửa xả · với tới được** | Đủ ba |
| 10 | Bộ lọc có **xả nước** và có trong lịch bảo trì | Có, có người chịu trách nhiệm |
| ⚠⚠ **11** | Cơ cấu nào **trọng lực làm đi xuống** thì có **van giữ tải hoặc khoá cần**, lắp sát cửa xy-lanh | ⭐ Đã kiểm bằng **thực nghiệm ngắt khí** khi cơ cấu đang mang tải |

---

## 6.10 Tự kiểm

1. Nêu **ba lý do** một người viết chương trình PLC cần hiểu khí nén.
2. Vì sao **nước** là thứ phá hoại nhiều nhất trong hệ khí nén? Kể ba hậu quả.
3. Vì sao tra dầu vào hệ dùng van không cần dầu là quyết định **một chiều**?
4. Phân biệt van 5/2 **một cuộn lò xo về** và **hai cuộn**. Mất điện thì mỗi loại làm gì?
5. Nêu **ba kiểu vị trí giữa** của van 5/3. Hai kiểu nào hành xử **ngược nhau** khi mất điện?
6. Viết công thức **lực đẩy** và **lực kéo**. Vì sao lực kéo luôn nhỏ hơn, và điều đó ảnh hưởng tới
   việc chọn xy-lanh thế nào?
7. Vì sao **không có công thức đơn giản** để tính tốc độ xy-lanh? Cách làm đúng là gì?
8. Vì sao tiết lưu **đường xả** cho chuyển động êm còn đường cấp thì giật cục? Trả lời bằng tính chất
   vật lý của khí.
9. Nêu **ba triệu chứng** của van tiết lưu lắp ngược. Vì sao chúng hay bị chẩn đoán nhầm?
10. Nêu **ba yêu cầu bắt buộc** với van cô lập khí để quy trình LOTO có ý nghĩa.

Câu 5, 8 và 10 là ba câu phân loại. Câu 5 là nhầm lẫn nguy hiểm nhất về khí nén; câu 8 là kiến thức
làm bạn chẩn đoán được một nhóm sự cố mà người khác đoán mò; câu 10 là câu về an toàn.

⚠⚠ **11.** Van hai cuộn giữ nguyên vị trí khi **mất điện**. Nó có giữ được tải khi **mất khí**
không? Vì sao? Nêu hai cơ cấu giữ tải thật và vì sao phải lắp **sát cửa xy-lanh**.

---

### Chương tiếp theo

**Chương 7 — ESD & môi trường sản xuất điện tử.** Chương này nói về năng lượng bạn nhìn thấy. Chương 7
nói về loại năng lượng **không nhìn thấy, không cảm thấy** — và phá sản phẩm mà không để lại dấu vết.

---

### Nguồn tham khảo chương 6

- ISO 4414 — *Pneumatic fluid power — General rules and safety requirements for systems and their
  components*: yêu cầu an toàn cho hệ khí nén, gồm cô lập và xả năng lượng tích trữ (mục 6.7).
  *(tiêu chuẩn có bản quyền)*
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu về cô lập năng lượng
  và khởi động lại sau khi khôi phục nguồn.
- ISO 15552 — *Pneumatic fluid power — Cylinders with detachable mountings*: kích thước lắp đặt
  xy-lanh, dùng khi tra bảng chọn. ⚠ Tiêu chuẩn tiền nhiệm **ISO 6431 đã bị thu hồi**, nhưng
  ⭐ **tên gọi "xy-lanh ISO 6431" vẫn được nhiều hãng dùng trong catalogue** — hai loại lắp lẫn
  được, ISO 15552 mở rộng dải đường kính và thêm rãnh gắn cảm biến từ.
- Catalogue và phần mềm tính chọn của nhà sản xuất thiết bị khí nén — dùng cho hệ số hiệu suất, bảng
  chọn cỡ, và tính tiêu thụ khí.

> ⚡ **Các hệ số dự trữ ở mục 6.4 là quy tắc thực dụng để chọn sơ bộ**, không phải giá trị chuẩn hoá.
> Công thức lực chỉ đúng trong điều kiện đã ghi kèm. Với ứng dụng quan trọng — đặc biệt khi có tải
> treo, tốc độ cao, hoặc liên quan an toàn — phải dùng tài liệu tính chọn của nhà sản xuất và có người
> có chuyên môn kiểm tra.
