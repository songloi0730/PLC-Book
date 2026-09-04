# Chương 7 — ESD & môi trường sản xuất điện tử

---

## 7.1 Bài toán: cỗ máy làm hỏng sản phẩm mà không để lại dấu vết

Một dây chuyền lắp ráp board mạch chạy ổn định. Mọi board đều qua kiểm chức năng và được đánh dấu OK.
Tỷ lệ lỗi tại xưởng gần bằng không.

Sáu tháng sau, tỷ lệ trả hàng từ thị trường tăng gấp ba. Board hỏng ở tay người dùng, sau vài tháng
hoạt động bình thường. Không có mẫu nào hỏng giống mẫu nào.

Truy ngược mãi mới ra: một gá kẹp bằng nhựa thay mới ba tháng trước — **nhựa thường, không phải nhựa
tiêu tán tĩnh điện**. Mỗi lần board trượt vào gá, ma sát tích điện. Khi board chạm vào chốt định vị
bằng thép nối đất, điện tích phóng qua **một chân linh kiện**.

Phần lớn board không hỏng ngay. Chúng bị **hỏng tiềm ẩn** — lớp cách điện bên trong linh kiện bị đánh
thủng một phần, vẫn hoạt động, nhưng tuổi thọ giảm mạnh.

Không máy nào báo lỗi. Không phép kiểm nào bắt được. Cỗ máy làm hỏng hàng trăm nghìn sản phẩm trong ba
tháng mà **không để lại một dấu vết nào**.

Đây là lý do chương này tồn tại, và là lý do nó nằm ở Phần I — trước cả khi bạn chạm vào PLC.

---

## 7.2 Vì sao ESD là mối nguy đặc biệt

**Phóng tĩnh điện** *(electrostatic discharge, ESD)* khác mọi loại hỏng hóc khác trong sách này ở ba
điểm, và cả ba đều làm nó khó đối phó hơn:

| | Hỏng hóc thông thường | ESD |
|---|---|---|
| **Người có nhận biết được không** | Có — nghe, thấy, ngửi thấy | ❌ Ngưỡng cảm nhận của người khoảng vài nghìn vôn; **linh kiện hỏng ở mức thấp hơn nhiều** |
| **Máy có phát hiện được không** | Thường có — cảm biến, timeout | ❌ Không, trừ khi được thiết kế riêng |
| **Hậu quả xuất hiện khi nào** | Ngay | ⚠ **Ngay hoặc sau nhiều tháng** |

Dòng đầu là điều đáng sợ nhất: **bạn có thể phóng đủ điện để phá một linh kiện mà không hề cảm thấy
gì**. Cảm giác "giật" chỉ xuất hiện ở mức cao hơn hẳn ngưỡng gây hỏng.

### Hỏng ngay và hỏng tiềm ẩn

| Loại | Tỷ lệ | Biểu hiện | Ai phát hiện |
|---|---|---|---|
| **Hỏng ngay** *(catastrophic)* | Thiểu số | Linh kiện chết hẳn | Kiểm cuối chuyền bắt được |
| ⚠ **Hỏng tiềm ẩn** *(latent)* | **Đa số** | Vẫn hoạt động, tuổi thọ giảm | ❌ **Không ai** — cho tới khi hỏng ngoài thị trường |

Hỏng tiềm ẩn là phần nguy hiểm. Nó biến một vấn đề kỹ thuật thành một vấn đề **không nhìn thấy được
bằng bất kỳ phép kiểm nào trong xưởng**, và biến chi phí từ "một board hỏng" thành "uy tín và bảo hành".

---

## 7.3 Điện tích sinh ra từ đâu

### Nhiễm điện do ma sát

Hai vật liệu khác nhau chạm rồi tách ra sẽ **trao đổi điện tử**. Vật này nhiễm dương, vật kia nhiễm âm.
Hiện tượng gọi là **nhiễm điện do ma sát** *(triboelectric charging)*.

Điều quan trọng với người thiết kế máy: chuyện này xảy ra ở **mọi** chỗ có tiếp xúc rồi tách trong máy:

| Hoạt động trong máy | Nhiễm điện ở đâu |
|---|---|
| Board trượt trên băng tải hoặc thanh dẫn | Mặt dưới board ↔ mặt băng tải |
| Board vào/ra gá kẹp | Board ↔ vật liệu gá |
| Giác hút chân không nhấc board | Board ↔ đệm cao su giác hút |
| Bóc lớp phim bảo vệ | Rất mạnh — bóc phim là một trong những nguồn tích điện mạnh nhất |
| Khí nén thổi ra | Luồng khí và hạt trong khí tích điện cho vật nó thổi vào |
| Người đi trên sàn | Người tích điện, rồi chạm vào board |

Dòng cuối là dòng người ta hay nghĩ tới nhất. Trong một cỗ máy tự động, nó lại **ít quan trọng nhất** —
vì ít người chạm vào sản phẩm. Các dòng trên mới là nguồn chính.

### Ba mô hình phóng điện

Ngành điện tử mô tả ESD bằng ba mô hình, tương ứng ba tình huống khác nhau:

| Mô hình | Chuyện gì xảy ra | Quan trọng ở đâu |
|---|---|---|
| **Người** *(Human Body Model, HBM)* | Người tích điện chạm vào linh kiện | Lắp ráp thủ công, sửa chữa |
| **Máy** *(Machine Model, MM)* | Vật kim loại tích điện chạm vào linh kiện | Dụng cụ, gá kim loại |
| ⭐ **Thiết bị tích điện** *(Charged Device Model, CDM)* | **Chính board tích điện**, rồi phóng qua một chân khi chạm vật nối đất | ⭐ **Máy tự động** |

> ⚡ **LƯU Ý — điểm quan trọng nhất của chương với người thiết kế máy**
> Trong lắp ráp thủ công, mô hình **người** chiếm ưu thế, và biện pháp là dây đeo cổ tay, thảm, áo choàng.
>
> Trong **máy tự động**, mô hình chiếm ưu thế là **thiết bị tích điện**: sản phẩm tự tích điện khi di
> chuyển trong máy, rồi phóng qua một chân duy nhất khi chạm vào một điểm nối đất. Phóng điện kiểu này
> có **thời gian rất ngắn và dòng đỉnh rất cao**, và nó gây hỏng ở mức điện áp thấp hơn hẳn mô hình người.
>
> Hệ quả thực tế: **dây đeo cổ tay không cứu được máy tự động.** Cái cứu được là kiểm soát vật liệu
> trong máy và ion hoá — mục 7.5 và 7.6.

---

## 7.4 Ba loại đất — và vì sao phải phân biệt

Đây là chỗ người mới nhầm nhiều nhất, và nhầm ở đây gây hậu quả cả về an toàn lẫn chất lượng.

| Loại đất | Ký hiệu thường gặp | Mục đích | Yêu cầu điện trở |
|---|---|---|---|
| **Đất bảo vệ** | PE | **An toàn cho người** — dẫn dòng sự cố để thiết bị bảo vệ cắt | **Rất thấp** — phải dẫn được dòng lớn |
| **Đất tín hiệu** | 0 V, GND | **Mốc quy chiếu** cho mạch điện tử | Thấp, nhưng khác mục đích với PE |
| **Đất ESD** | thường ký hiệu riêng | **Xả điện tích chậm và có kiểm soát** | ⭐ **Có điện trở** — xem dưới |

### Vì sao đất ESD phải có điện trở

Trực giác nói: muốn xả điện tích thì nối đất càng chắc càng tốt. **Sai** — vì hai lý do độc lập, và cả
hai đều quan trọng.

**Lý do 1 — an toàn cho người.** Dây đeo cổ tay nối người xuống đất. Nếu nối bằng dây dẫn tốt và người
đó **vô tình chạm vào vật mang điện áp nguy hiểm**, thì cơ thể trở thành đường dẫn dòng xuống đất —
tình huống có thể gây chết người.

> ⚠ **NGUY HIỂM**
> Vì vậy dây đeo cổ tay **luôn có một điện trở nối tiếp** (thường cỡ một mega-ôm). Điện trở đó **không
> ảnh hưởng tới khả năng xả tĩnh điện** — tĩnh điện là điện tích rất nhỏ, xả qua điện trở đó vẫn nhanh
> hơn tốc độ tích điện rất nhiều — nhưng nó **hạn chế dòng xuống mức không gây chết người** nếu có sự cố.
>
> **Không bao giờ tự chế dây đeo cổ tay bằng dây dẫn thường.** Không bao giờ bỏ qua điện trở đó.

**Lý do 2 — xả nhanh cũng gây hỏng.** Một vật tích điện nối đột ngột vào đất dẫn tốt sẽ xả với **dòng
đỉnh rất cao trong thời gian rất ngắn** — và chính xung dòng đó là thứ phá linh kiện. Vật liệu tiêu tán
tĩnh điện làm điện tích chảy đi **chậm và đều**, tránh xung.

Đó là lý do bàn thao tác, thảm, và gá dùng vật liệu **tiêu tán** *(dissipative)*, không dùng vật liệu
**dẫn điện** *(conductive)* và cũng không dùng vật liệu **cách điện** *(insulative)*:

| Loại vật liệu | Điện tích chảy đi | Vấn đề |
|---|---|---|
| **Cách điện** (nhựa thường) | ❌ Không chảy | Tích điện và giữ mãi — nguồn gốc sự cố ở mục 7.1 |
| **Tiêu tán** | ✅ Chảy chậm, có kiểm soát | Đây là thứ cần dùng |
| **Dẫn điện** | ⚠ Chảy rất nhanh | Xung dòng cao khi tiếp xúc đột ngột |

---

## 7.5 Đường thoát tĩnh điện của một cỗ máy

Nguyên tắc: **mọi vật dẫn trong vùng làm việc phải được nối về cùng một điểm quy chiếu, qua đường tiêu
tán**. Vật gì không nối được (vì là chất cách điện) thì phải xử lý bằng ion hoá — mục 7.6.

Với một cỗ máy như DP-01, danh mục kiểm:

| Bộ phận | Yêu cầu | Lỗi thường gặp |
|---|---|---|
| **Khung máy, vỏ tủ** | Nối đất chắc chắn | Sơn cách điện tại điểm bắt vít → mất liên tục |
| **Mặt băng tải / thanh dẫn board** | Vật liệu tiêu tán, có nối về điểm quy chiếu | Dùng dây đai nhựa thường |
| **Gá, chốt định vị, thanh chặn** | Vật liệu tiêu tán | ⭐ Sự cố ở mục 7.1 — thay gá bằng nhựa thường |
| **Đệm giác hút** | Cao su tiêu tán | Cao su thường tích điện rất mạnh |
| **Bàn thao tác, ghế, thảm sàn** | Tiêu tán, có nối đất | Thảm rời không nối |
| **Dụng cụ cầm tay** | Cán tiêu tán | Tua vít cán nhựa thường |
| **Bao bì, khay đựng board** | Khay chuyên dụng tiêu tán | Dùng khay nhựa thường vì rẻ hơn |

> 💡 **MẸO — sai lầm hay gặp nhất khi lắp máy**
> Bắt vít khung máy vào tấm nền **có lớp sơn** rồi coi như đã nối đất. Sơn là chất cách điện; mối nối
> đó có thể có điện trở rất cao. Phải cạo sơn tại điểm tiếp xúc, hoặc dùng vòng đệm răng cắn qua sơn,
> và **đo kiểm sau khi lắp** — đừng giả định.

### Điểm quy chiếu chung

Mọi đường thoát tĩnh điện phải về **một điểm chung**, không phải mỗi thứ về một chỗ. Nếu bàn nối về
điểm A còn gá nối về điểm B, và giữa A và B có chênh điện thế, thì board đi từ bàn sang gá vẫn phóng
điện — dù cả hai đều "đã nối đất".

Đây là cùng một nguyên lý với **vòng lặp đất** ở Chương 51: hai điểm đều gọi là đất mà chênh nhau vài
vôn.

---

## 7.6 Bộ khử tĩnh điện — và vì sao PLC phải biết nó còn sống

### Vì sao cần ion hoá

Có những thứ **không thể nối đất được**: chính board mạch (là vật cách điện phần lớn), lớp phim bảo vệ,
bao bì, và mọi chi tiết nhựa bắt buộc phải dùng.

Với chúng, cách duy nhất là **trung hoà điện tích bằng không khí có ion**. **Bộ khử tĩnh điện**
*(ionizer)* tạo ra cả ion dương và ion âm; vật tích điện dương hút ion âm và ngược lại, nên điện tích
được trung hoà.

| Kiểu | Đặc điểm | Dùng khi |
|---|---|---|
| **Thanh ion** | Đặt dọc theo đường sản phẩm đi | Băng tải, cửa vào/ra máy |
| **Quạt ion** | Thổi khí có ion vào một vùng | Bàn thao tác, vùng hở |
| **Vòi ion** | Thổi tập trung, thường kèm khí nén | Điểm cục bộ — chỗ bóc phim, chỗ giác hút |

### ⭐ Vì sao tín hiệu tình trạng của ionizer phải vào PLC

Đây là mối liên hệ trực tiếp giữa chương này và phần lập trình, và nó là lý do Chương 48 lấy ionizer
làm ví dụ trung tâm.

Ionizer hỏng thì:

- Máy **vẫn chạy bình thường** — không cơ cấu nào phụ thuộc vào nó.
- Sản phẩm **vẫn qua mọi phép kiểm** — hỏng tiềm ẩn không lộ ra.
- Không ai biết, cho tới khi hàng trả về từ thị trường.

Nói cách khác: **đây đúng là loại hỏng hóc mà máy không tự phát hiện được** (Chương 48, mục 48.6).

> ⚠ **NGUY HIỂM**
> Mọi bộ khử tĩnh điện lắp trên máy tự động **phải có tín hiệu tình trạng đưa về PLC**, và tín hiệu đó
> phải là **điều kiện cho phép chạy** — không phải chỉ là một dòng hiển thị.
>
> Lý do: nếu chỉ hiển thị, người vận hành sẽ bỏ qua nó (Chương 44 — "mọi thứ đều báo động = không có
> báo động nào"). Nếu là điều kiện cho phép chạy, máy **không chạy được** khi ionizer hỏng, và vấn đề
> được xử lý ngay.

Hai thứ nữa cần giám sát, vì ionizer suy giảm dần chứ không hỏng đột ngột:

| Cần giám sát | Vì sao | Cách |
|---|---|---|
| **Đầu phát bị bẩn** | Bụi bám làm giảm hiệu quả dần dần | Nhiều loại có tín hiệu báo cần vệ sinh; hoặc đặt lịch theo giờ chạy (Chương 51, mục 51.11) |
| **Cân bằng ion lệch** | Nếu lệch, ionizer **tự nó tích điện cho sản phẩm** thay vì trung hoà | Kiểm định kỳ bằng thiết bị đo; một số loại tự giám sát |

Dòng thứ hai đáng chú ý: một ionizer lệch cân bằng **có hại hơn là không có ionizer**.

---

## 7.7 Ảnh hưởng tới thiết kế cơ cấu

Chương này không chỉ là chuyện chọn vật liệu. Nó đổi cả cách thiết kế cơ cấu chạm vào sản phẩm:

| Nguyên tắc | Vì sao | Ví dụ |
|---|---|---|
| **Giảm ma sát trượt** | Trượt tích điện nhiều hơn nhấc-đặt | Nhấc board lên rồi đặt xuống, thay vì đẩy trượt |
| **Giảm tách nhanh** | Tách càng nhanh, tích điện càng mạnh | Nhả giác hút từ từ; tránh bóc phim tốc độ cao mà không có ion |
| **Chạm vào mép board, không chạm mặt linh kiện** | Giảm nguy cơ phóng qua chân linh kiện | Gá kẹp mép |
| **Nối đất gá trước khi board chạm vào** | Tránh chênh điện thế lúc tiếp xúc | Gá tiêu tán, đã nối về điểm quy chiếu |
| **Đặt ion hoá tại chỗ tích điện, không phải chỗ xa** | Ion có tầm tác dụng giới hạn | Vòi ion ngay tại vị trí giác hút |

> 💡 **MẸO**
> Câu hỏi để rà soát một thiết kế cơ cấu: **"ở chỗ nào trong máy có hai vật chạm nhau rồi tách ra?"**
> Mỗi chỗ như vậy là một nguồn tích điện, và mỗi chỗ cần một câu trả lời: vật liệu tiêu tán, hay ion hoá.

---

## 7.7b ⚠ ESD còn làm hỏng CHÍNH BỘ ĐIỀU KHIỂN — không chỉ sản phẩm

Cả chương tới đây nói về tĩnh điện làm hỏng **sản phẩm**. ⭐ Nhưng có một hướng thứ hai, gần bạn hơn
nhiều: ⚠ **chính module PLC trong tay bạn cũng nhạy với ESD** — và tài liệu hãng cảnh báo điều đó ở
những chỗ rất cụ thể.

| Thao tác | Cái gì hỏng |
|---|---|
| ⚠⚠ **Cắm / rút thẻ nhớ** | ⭐ Hỏng **thẻ nhớ** hoặc **chính khe cắm trên CPU** |
| ⚠ **Chạm vào chân của đầu nối module** | Hỏng module |
| Cầm module chưa lắp | Hỏng linh kiện bên trong |

> ⭐⭐ **Hai biện pháp mà tài liệu hãng nêu — đơn giản tới mức dễ bị bỏ qua:**
>
> | | |
> |---|---|
> | 1 | ⭐ **Chạm vào một bề mặt dẫn điện đã nối đất** trước khi cầm module hoặc thẻ nhớ |
> | 2 | ⭐ Hoặc **đeo vòng đeo tay tiêu tán tĩnh điện đã nối đất** |
>
> ⚡ Cùng nguyên lý với đường thoát tĩnh điện của cỗ máy ở mục 7.5 — ⭐ **xả điện tích của bạn về cùng
> một điểm quy chiếu trước khi tiếp xúc**, thay vì để nó phóng qua linh kiện.

> ⚠⚠ **Vì sao hướng này nguy hiểm hơn vẻ ngoài của nó.**
>
> Hỏng do ESD **hiếm khi hỏng ngay**. Giống board sản phẩm ở mục 7.2, module PLC bị phóng tĩnh điện
> thường ⭐ **hỏng tiềm ẩn**: chạy tiếp vài tuần rồi bắt đầu lỗi chập chờn — ⚠ và lúc đó **không ai
> liên hệ nó với lần thay thẻ nhớ ba tuần trước**.
>
> ⭐ Đây chính là **một mục nữa cho danh sách bốn nguyên nhân vật lý của lỗi chập chờn** ở Chương 51
> mục 51.8: ⚠ *"module này đã từng bị ai cầm mà không xả tĩnh điện chưa?"*

> ⭐ **Hệ quả tổ chức:** khu vực bảo trì tủ điện nên có sẵn **một điểm nối đất và một vòng đeo tay**,
> đúng như khu vực thao tác sản phẩm. ⚠ Nếu công ty đã đầu tư đường thoát tĩnh điện cho **sản phẩm**
> mà bàn sửa chữa module thì không có gì, ⭐ **đó là một lỗ hổng nhất quán**.

---

## 7.8 Môi trường: độ ẩm và phòng sạch

### Độ ẩm

Không khí ẩm dẫn điện tốt hơn không khí khô, nên **độ ẩm thấp làm tích điện nặng hơn nhiều**. Đây là lý
do sự cố ESD thường tăng vọt vào mùa khô, hoặc trong phòng có điều hoà hút ẩm mạnh.

> ⚡ **LƯU Ý**
> Tăng độ ẩm **giảm** vấn đề nhưng **không giải quyết** nó. Nó không thay thế được vật liệu tiêu tán
> và ion hoá. Và độ ẩm cao lại gây vấn đề khác — ăn mòn, ngưng tụ. Đây là yếu tố cần kiểm soát trong
> dải, không phải cần tối đa hoá.

### Phòng sạch — đủ để hiểu ràng buộc thiết kế

Nếu máy đặt trong phòng sạch, có thêm ràng buộc ảnh hưởng trực tiếp tới thiết kế:

| Ràng buộc | Ảnh hưởng tới máy |
|---|---|
| Vật liệu **không sinh hạt** | Hạn chế loại nhựa, dây đai, chổi quét |
| **Không dùng dầu mỡ hở** | Ổ dẫn hướng, xy-lanh phải loại phù hợp |
| **Xả khí nén ra ngoài phòng** | Van xả phải nối ống dẫn ra, không xả tự do |
| **Bề mặt lau chùi được** | Không góc chết, không khe hở tích bụi |
| Vào ra qua **buồng đệm** | Kích thước máy bị giới hạn bởi cửa buồng đệm |

Dòng thứ ba đáng chú ý với người làm điều khiển: van khí trong phòng sạch **không được xả tự do** —
điều này ảnh hưởng tới cách bố trí van và ống, và đôi khi tới cả tốc độ cơ cấu.

---

## 7.9 Bẫy thường gặp

### 🔍 BẪY 1 — Thay linh kiện cơ khí bằng loại "tương đương" mà không xét vật liệu

Sự cố ở mục 7.1. Người thay gá thấy hai miếng nhựa giống hệt nhau về hình dạng và cứng như nhau — và
không có cách nào **nhìn** ra một miếng là tiêu tán, một miếng là cách điện.

**Cách phòng:** ghi rõ yêu cầu vật liệu tiêu tán **trong danh mục vật tư và trên bản vẽ**, không chỉ
trong đầu người thiết kế. Và dán nhãn trên chi tiết đó.

### 🔍 BẪY 2 — Tin rằng "không thấy giật thì không sao"

Ngưỡng cảm nhận của người cao hơn ngưỡng gây hỏng linh kiện rất nhiều. **Không cảm thấy gì không có
nghĩa là không có phóng điện.**

### 🔍 BẪY 3 — Dây đeo cổ tay tự chế, hoặc bỏ điện trở

⚠ Đây là bẫy **nguy hiểm cho người**, không chỉ cho sản phẩm. Xem cảnh báo ở mục 7.4.

Ngoài ra: dây đeo cổ tay cần **kiểm tra định kỳ** — dây đứt ngầm bên trong rất phổ biến, và nhìn bên
ngoài không thấy. Nhiều nơi có trạm kiểm tra dây đeo ở lối vào khu vực.

### 🔍 BẪY 4 — Nối đất khung máy qua lớp sơn

Đã nêu ở mục 7.5. Bẫy này phổ biến vì mối nối **trông** chắc chắn. Phải đo kiểm sau khi lắp.

### 🔍 BẪY 5 — Coi biện pháp cho lắp ráp thủ công là đủ cho máy tự động

Dây đeo cổ tay, thảm, áo choàng đều nhắm vào **mô hình người**. Máy tự động chủ yếu gặp **mô hình
thiết bị tích điện** — và không biện pháp nào ở trên chạm tới nó.

Biện pháp cho máy tự động: **vật liệu tiêu tán trong máy** và **ion hoá tại các điểm tích điện**.

### 🔍 BẪY 6 — Ionizer không có tín hiệu tình trạng

Bẫy trung tâm nối chương này với phần lập trình. Xem mục 7.6 và Chương 48.

### 🔍 BẪY 7 — Ionizer lệch cân bằng mà không ai kiểm

Ionizer không hỏng hẳn nhưng phát lệch về một cực sẽ **tích điện cho sản phẩm** thay vì trung hoà —
có hại hơn không có nó. Cần kiểm định kỳ bằng thiết bị đo, không chỉ xem đèn báo nguồn.

### 🔍 BẪY 8 — Dùng khí nén thổi sạch board mà không ion hoá

Khí nén thổi ra **tích điện rất mạnh** cho vật nó thổi vào. Thổi sạch bụi bằng khí thường là đổi một
vấn đề (bụi) lấy một vấn đề nặng hơn (tĩnh điện). Nếu phải thổi, dùng **vòi có ion hoá**.

---

## 7.10 Bảng chốt — danh mục kiểm ESD cho một cỗ máy

| # | Kiểm | Đạt khi |
|---|---|---|
| 1 | Liệt kê **mọi chỗ có tiếp xúc rồi tách** trong máy | Có danh sách; mỗi chỗ có biện pháp |
| 2 | **Vật liệu tiêu tán** cho mọi bộ phận chạm sản phẩm | Ghi rõ trong danh mục vật tư **và** trên bản vẽ |
| 3 | Mọi vật dẫn nối về **một điểm quy chiếu chung** | Đo kiểm sau lắp, không giả định |
| 4 | Nối đất khung **không qua lớp sơn** | Đã cạo sơn hoặc dùng vòng đệm răng; đã đo |
| 5 | **Ion hoá tại các điểm tích điện**, không phải ở xa | Vị trí đặt khớp danh sách ở mục 1 |
| 6 | ⭐ **Tín hiệu tình trạng ionizer vào PLC**, là điều kiện cho phép chạy | Có |
| 7 | Kế hoạch **kiểm định kỳ**: dây đeo cổ tay, cân bằng ion, điện trở bề mặt | Có lịch, có người chịu trách nhiệm |
| 8 | **Độ ẩm** được theo dõi và nằm trong dải | Có |
| 9 | Cơ cấu thiết kế theo **năm nguyên tắc** ở mục 7.7 | Đã rà soát |
| 10 | Khí nén thổi sản phẩm đều **có ion hoá** | Có |
| 11 | ⚠ **Bàn sửa chữa module** cũng có điểm nối đất và vòng đeo tay | ⭐ Có — ESD hỏng **cả module PLC**, không chỉ sản phẩm (mục 7.7b) |

---

## 7.11 Tự kiểm

1. Kể lại sự cố ở mục 7.1. Vì sao **không phép kiểm nào trong xưởng** bắt được nó?
2. Phân biệt **hỏng ngay** và **hỏng tiềm ẩn**. Cái nào chiếm đa số, và vì sao cái đó nguy hiểm hơn?
3. Vì sao *"tôi không thấy giật nên chắc không sao"* là suy luận sai?
4. Nêu **ba mô hình phóng điện**. Mô hình nào chiếm ưu thế trong **máy tự động**, và hệ quả thực tế
   của điều đó là gì?
5. Nêu **ba loại đất** và mục đích của từng loại.
6. Vì sao dây đeo cổ tay **phải có điện trở**? Nêu **cả hai** lý do.
7. Vì sao vật liệu tiêu tán tốt hơn vật liệu dẫn điện cho bàn và gá?
8. Vì sao **tín hiệu tình trạng của ionizer phải là điều kiện cho phép chạy**, không chỉ là dòng hiển thị?
9. Một ionizer lệch cân bằng nguy hiểm thế nào so với không có ionizer?
10. Câu hỏi nào dùng để rà soát một thiết kế cơ cấu về mặt ESD?
11. ⚠ Ngoài sản phẩm, ESD còn làm hỏng cái gì trong tủ điện? ⭐ Nêu **hai** thao tác rủi ro nhất và
    **hai** biện pháp phòng.
12. ⭐⭐ Vì sao hỏng module do ESD **khó truy nguyên nhân** hơn hỏng ngay? Liên hệ với danh sách nguyên
    nhân lỗi chập chờn ở Chương 51.

Câu 4, 6 và 8 là ba câu phân loại. Câu 4 quyết định bạn chọn đúng biện pháp cho máy tự động hay áp
nhầm biện pháp của lắp ráp thủ công; câu 6 là câu về **an toàn cho người**; câu 8 là chỗ chương này
nối vào phần lập trình.

---

### Chương tiếp theo

**Chương 8 — Kiến trúc phần cứng PLC.** Hết Phần I. Từ chương sau, bạn bắt đầu làm việc với chính bộ
điều khiển — và mọi ví dụ dùng chung máy mẫu DP-01.

---

### Nguồn tham khảo chương 7

- IEC 61340-5-1 — *Electrostatics — Protection of electronic devices from electrostatic phenomena —
  General requirements*: yêu cầu với khu vực bảo vệ chống tĩnh điện, vật liệu, và kiểm định.
  *(tiêu chuẩn có bản quyền)*
- IEC 61340-5-2 — hướng dẫn áp dụng đi kèm tiêu chuẩn trên.
- Các tiêu chuẩn thử nghiệm linh kiện theo ba mô hình phóng điện (người, máy, thiết bị tích điện) —
  dùng cho mục 7.3.
- Tài liệu kỹ thuật của nhà sản xuất thiết bị ion hoá và vật liệu chống tĩnh điện — dùng cho phần
  diễn giải nguyên lý ở mục 7.4 và 7.6.
- **Siemens S7-1200 System Manual** — cảnh báo ESD lặp lại ở các thao tác **cắm/rút thẻ nhớ** và
  **chạm chân đầu nối module**: ⭐ *phóng tĩnh điện có thể làm hỏng thẻ nhớ hoặc khe cắm trên CPU*;
  biện pháp nêu là ⭐ **chạm bề mặt dẫn điện đã nối đất và/hoặc đeo vòng tay nối đất** — nền cho
  mục 7.7b.

> ⚠ Chương này diễn giải khái niệm ở mức đủ để **thiết kế máy có tính tới ESD** và **trao đổi với
> người phụ trách chương trình kiểm soát tĩnh điện** của nhà máy. Việc xây dựng và kiểm định một khu
> vực bảo vệ chống tĩnh điện đầy đủ là một chương trình riêng, có tiêu chuẩn riêng, và cần đo đạc
> bằng thiết bị chuyên dụng — **không kết luận được từ nội dung chương này**.
