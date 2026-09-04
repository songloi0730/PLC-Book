# Chương 23 — Từ yêu cầu tới đặc tả điều khiển

> **Lát cắt máy mẫu:** 2 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp, hai trạm, trình
> tự song song, công thức sản phẩm.

---

## 23.1 Hai loại sai — và loại đắt hơn nhiều

Có hai cách một cỗ máy sai.

**Loại thứ nhất: code sai.** Bạn viết nhầm một điều kiện, quên một timeout, đảo hai bước. Loại này khó
chịu nhưng **rẻ**: nó lộ ra khi chạy thử, bạn sửa vài dòng, xong.

**Loại thứ hai: đặc tả sai.** Code chạy **chính xác như đã viết**, nhưng cái đã viết không phải cái
khách hàng cần. Máy nghiệm thu xong, chạy sản xuất một tuần, rồi khách hàng hỏi:

> *"Sao mất điện giữa chu trình xong bật lại, máy lại vứt board đang gia công?"*

Không ai từng nói với bạn phải giữ board đó. Cũng không ai từng nói phải vứt. **Câu hỏi chưa bao giờ
được đặt ra.** Giờ để sửa, bạn phải thêm bộ nhớ giữ được khi mất điện, thêm trình tự khôi phục, thêm
màn hình xác nhận — và có thể phải thêm cả cảm biến.

Loại thứ hai đắt hơn loại thứ nhất **một hoặc hai bậc độ lớn**, và nó gần như luôn bắt nguồn từ cùng
một chỗ: **mở phần mềm lập trình trước khi viết xong đặc tả**.

Chương này là cách tránh loại sai thứ hai.

> ⚡ **LƯU Ý**
> "Viết đặc tả" ở đây không có nghĩa là làm một tập hồ sơ dày. Với một máy cỡ DP-01, bộ đặc tả đủ dùng
> là **khoảng mười trang** — và phần lớn là bảng. Cái tốn thời gian không phải viết, mà là **hỏi cho
> ra những câu chưa ai hỏi**.

---

## 23.2 Bộ đặc tả gồm sáu phần

Toàn bộ tập tài liệu này thường được gọi chung là **đặc tả chức năng** *(functional specification,
FS — có nơi gọi là functional design specification, FDS)*. Nó được viết để trả lời **bản yêu cầu của
người dùng** *(user requirement specification, URS)* — thứ khách hàng đưa cho bạn, thường ngắn hơn và
mơ hồ hơn nhiều. Hai cái tên viết tắt này bạn sẽ gặp ngay trong email đầu tiên của một dự án.

| # | Phần | Tên tiếng Anh hay gặp | Trả lời câu hỏi | Chương liên quan |
|---|---|---|---|---|
| 1 | **Bảng I/O** | *I/O list* | Máy có những tín hiệu gì, mỗi tín hiệu nghĩa là gì | 4, 5, 9 |
| 2 | **Danh sách chế độ** | *operating modes* | Máy có mấy chế độ, mỗi chế độ ai được dùng và làm được gì | 25, 28 |
| 3 | **Mô tả trình tự** | *sequence of operations, SOO* | Chu trình tự động gồm những bước nào | 26 |
| 4 | **Xử lý bất thường** | *exception / fault handling* | Mỗi loại lỗi thì máy làm gì | 26, 28 |
| 5 | **Tham số & công thức** | *parameters & recipe* | Cái gì đổi theo mã hàng, dải hợp lệ bao nhiêu | 29 |
| 6 | **Tiêu chí nghiệm thu** | *acceptance criteria* | Làm sao biết máy đã xong | 50, 52 |

Sáu phần này viết **theo thứ tự**, vì phần sau dùng kết quả của phần trước. Nhưng phần 6 — tiêu chí
nghiệm thu — nên **phác trước, hoàn thiện sau**: xem mục 23.6.

> ⚡ **LƯU Ý — vì sao cần nhớ cả tên tiếng Anh**
> Tài liệu mẫu, phần mềm quản lý dự án, và người nước ngoài trong dự án đều dùng các tên viết tắt
> này. Khi ai đó hỏi *"đã có SOO chưa?"*, họ đang hỏi phần 3. Không biết từ này thì bạn mất thời gian
> hỏi lại, hoặc tệ hơn, gật đầu nhầm thứ.

---

## 23.3 Bảng I/O — làm trước, không làm sau

Bảng I/O là thứ **duy nhất** trong đặc tả mà cả bốn bên đều dùng: người thiết kế điện đấu dây theo nó,
người lập trình đặt tên tag theo nó, người chạy thử kiểm theo nó, người bảo trì tra theo nó.

Mỗi dòng phải đủ sáu cột:

| Cột | Nội dung | Vì sao cần |
|---|---|---|
| **Tag** | Tên dùng trong chương trình | Thống nhất giữa bản vẽ và code |
| **Mô tả** | Bằng tiếng người, không viết tắt | Người bảo trì đọc được |
| **Loại thiết bị** | Quang thu-phát PNP, reed, nút NC… | Quyết định cách đấu (Chương 4) |
| **Trạng thái nghỉ** | Bit bằng mấy khi bình thường | Quyết định lệnh dùng trong code (Chương 15) |
| **Phân loại** | ⭐ **An toàn** hay **quy trình** | Quyết định cách xử lý khi mất tín hiệu |
| **Hành vi khi mất** | Máy phải làm gì nếu tín hiệu này biến mất | Đầu vào cho Chương 48 |

### Cột phân loại là cột quan trọng nhất

Đây là cột người mới hay bỏ trống, và là cột quyết định nhiều thứ nhất về sau.

| | **Tín hiệu an toàn** | **Tín hiệu quy trình** |
|---|---|---|
| Mất nó thì | **Phải dừng máy** | Sai sản phẩm hoặc kẹt chu trình |
| Tiếp điểm vật lý | **Bắt buộc NC** (Chương 4) | Tuỳ, thường NO |
| Trong code | Tổ hợp 3 — `┤ ├` với tiếp điểm NC | Tuỳ ngữ cảnh |
| Xử lý khi mất | Dừng ngay, báo động | Timeout rồi báo lỗi |
| Ví dụ ở DP-01 | `DI_StopPB`, `DI_AirOK` | `DI_BoardStn1`, các reed xy-lanh |

Việc phân loại này phải làm **lúc lập bảng I/O**, không phải lúc viết code — vì nó quyết định **loại
thiết bị phải mua** và **cách đấu dây**. Phát hiện muộn nghĩa là phải đổi phần cứng.

> 💡 **MẸO**
> Với mỗi dòng, hỏi đúng một câu: *"nếu sợi dây này đứt lúc máy đang chạy, máy nên làm gì?"* Trả lời
> "phải dừng" → an toàn. Trả lời "báo lỗi rồi chờ người xử lý" → quy trình. Câu hỏi này quyết định cả
> năm cột còn lại.

---

## 23.4 Mô tả trình tự bằng lời có cấu trúc

Trước khi vẽ lưu đồ (Chương 26), viết trình tự **bằng lời** — vì lời là thứ khách hàng đọc và duyệt
được, còn lưu đồ thì không phải ai cũng đọc.

Nhưng viết tự do sẽ mơ hồ. Dùng mẫu câu cố định:

```text
Bước <số> — <tên bước>
  Điều kiện vào:   <cái gì phải đúng để bắt đầu bước này>
  Hành động:       <máy làm gì>
  Điều kiện xong:  <tín hiệu nào cho biết đã xong>
  Thời gian tối đa: <giây>  → nếu quá: <máy làm gì>
```

Áp cho trạm 1 của DP-01:

```text
Bước 20 — Nâng kẹp giữ board
  Điều kiện vào:   chặn đã nâng (DI_Stop1Up = 1) và có board (DI_BoardStn1 = 1)
  Hành động:       cấp lệnh nâng kẹp trạm 1
  Điều kiện xong:  DI_Clamp1Up = 1
  Thời gian tối đa: 3 giây  → nếu quá: dừng máy, báo "S1.20 chờ DI_Clamp1Up",
                              gợi ý kiểm tra cảm biến reed / áp khí / xy-lanh kẹt
```

Bốn dòng này ép bạn trả lời **bốn câu hỏi bắt buộc** cho mọi bước. Dòng cuối — thời gian tối đa và
hành động khi quá — là dòng người mới hay bỏ trống, và đó chính là bẫy trung tâm của Chương 26.

> ⚡ **LƯU Ý**
> Nếu bạn không điền được dòng "điều kiện xong" bằng một **tín hiệu thật**, mà chỉ điền được "sau 2
> giây", thì đó là dấu hiệu **máy thiếu cảm biến**. Phát hiện điều đó ở giai đoạn đặc tả thì thêm cảm
> biến còn rẻ; phát hiện lúc chạy thử thì đã muộn.

---

## 23.5 ⭐ Những câu phải hỏi khách hàng

Đây là phần giá trị nhất của chương. Danh sách dưới đây là những câu **người mới hầu như luôn quên**,
và mỗi câu quên là một lần sửa đắt về sau.

### Nhóm A — Bất thường và phục hồi

| Câu hỏi | Vì sao quan trọng |
|---|---|
| **Mất điện giữa chu trình rồi bật lại — máy làm gì?** | Quyết định có cần bộ nhớ giữ được không, và trình tự khôi phục ra sao (Chương 28) |
| **Sản phẩm đang gia công dở khi dừng — giữ, bỏ, hay hỏi người?** | Quyết định có cần chỗ chứa riêng, có cần đánh dấu NG không |
| **Ai được phép nhấn Reset?** | Quyết định có cần phân quyền không |
| **Sau khi hết lỗi, chạy tiếp hay bắt đầu chu trình mới?** | Quyết định độ phức tạp của trình tự khôi phục (Chương 28) |
| **Có cần ghi lại lịch sử lỗi không? Giữ bao lâu?** | Quyết định bộ nhớ và cách ghi log |

### Nhóm B — Sản phẩm và chất lượng

| Câu hỏi | Vì sao quan trọng |
|---|---|
| **Máy chạy mấy mã hàng? Khác nhau ở tham số nào?** | Quyết định có cần công thức sản phẩm không (Chương 29) |
| **Đổi mã hàng giữa ca — làm thế nào? Có cần xả hết máy trước không?** | Quyết định trình tự chuyển đổi |
| **Sản phẩm lỗi xử lý ra sao — máy loại, hay người lấy ra?** | Quyết định có cần cơ cấu loại bỏ |
| **Có cần truy xuất từng sản phẩm không?** | Quyết định có cần đầu đọc mã và kết nối lên hệ thống trên (Chương 42) |
| **Hai sản phẩm vào cùng lúc thì sao?** | Trường hợp biên hay bị bỏ sót |

### Nhóm C — Vận hành hằng ngày

| Câu hỏi | Vì sao quan trọng |
|---|---|
| **Ai vận hành máy? Trình độ thế nào?** | Quyết định độ phức tạp cho phép của màn hình |
| **Đầu ca làm gì? Cuối ca làm gì?** | Thường phát sinh chế độ hoặc trình tự chưa ai nghĩ tới |
| **Bao lâu vệ sinh máy một lần? Có cần chế độ riêng không?** | Có thể phát sinh một chế độ vận hành mới |
| **Máy đứng chờ bao lâu thì coi là bất thường?** | Quyết định ngưỡng cảnh báo "máy đứng chờ" (Chương 26) |
| **Có ai cần biết máy đang làm gì từ xa không?** | Quyết định có cần kết nối lên hệ thống trên |

### Nhóm D — An toàn và ranh giới

| Câu hỏi | Vì sao quan trọng |
|---|---|
| **Ai được phép mở cửa bảo vệ? Khi nào?** | Quyết định loại khoá cửa và điều kiện mở (Chương 47) |
| **Máy nằm trong dây chuyền hay đứng độc lập?** | Quyết định có cần bắt tay với máy lân cận |
| **Máy trước / máy sau là máy gì, của ai?** | Quyết định giao diện ghép nối và ai chịu trách nhiệm phần nào |
| **Đã có đánh giá rủi ro chưa? Ai làm?** | ⚠ Nếu chưa có, đây là việc phải làm **trước** khi thiết kế mạch an toàn |

> ⚠ **NGUY HIỂM**
> Câu cuối của nhóm D không phải câu hỏi thủ tục. **Đánh giá rủi ro phải có trước khi thiết kế chức
> năng an toàn** — vì nó quyết định mức hiệu năng cần đạt, và mức đó quyết định phải dùng thiết bị
> loại nào. Thiết kế trước rồi đánh giá sau thì thường phải làm lại. Chương 47.

> 💡 **MẸO — cách hỏi cho ra câu trả lời thật**
> Đừng hỏi *"anh có yêu cầu gì về xử lý lỗi không?"* — câu trả lời gần như luôn là "không, cứ làm bình
> thường". Hãy **mô tả một tình huống cụ thể**:
>
> *"Giả sử đang chạy, board đã kẹp xong, đúng lúc đó mất điện. Điện có lại sau ba phút. Lúc đó anh
> muốn máy làm gì với board đó?"*
>
> Câu này luôn ra câu trả lời, vì người vận hành **hình dung được**. Và câu trả lời thường làm cả hai
> bên phát hiện ra một yêu cầu chưa ai nói.

---

## 23.5b ⭐⭐ Viết mãi không xong trình tự — đó là chẩn đoán, không phải kém cỏi

Có một tín hiệu rất đáng tin mà ít ai đọc đúng. Bạn ngồi viết mô tả trình tự ở mục 23.4, viết được
vài bước rồi **tắc**; sửa đi sửa lại, mỗi lần đọc lại thấy vẫn thiếu chỗ nào đó.

> ⭐⭐ **Phản xạ sai: cố viết tiếp cho xong.**
> ⭐ **Phản xạ đúng: quay lại mục 23.5 và hỏi thêm.**

Vì thứ tự thật sự của công việc là ba bước, và **bước sau phụ thuộc bước trước**:

| Bước | Việc | Nếu bước này thiếu |
|---|---|---|
| 1 | ⭐ **Định nghĩa nhiệm vụ** — *máy phải làm gì* | ⚠ Bước 2 **không thể** viết được |
| 2 | **Trình tự các bước** — *làm theo thứ tự nào* | ⚠ Bước 3 sẽ phải viết lại nhiều lần |
| 3 | Viết chương trình | — |

> ⭐ **Nói cách khác: viết trình tự khó không phải vì bạn nghĩ chậm, mà vì bài toán chưa đủ dữ kiện.**
>
> Không ai chỉ được đường từ đây tới một nơi mà **cả hai đầu đều chưa xác định** — và cũng không chỉ
> được nếu chưa biết ⚠ **phải đi bằng gì** và ⚠ **có hạn thời gian không**. Trình tự cũng vậy: nó
> không viết ra được khi còn thiếu điều kiện biên.

⭐ **Ba câu hỏi để tìm chỗ thiếu**, khi thấy mình tắc:

| | Hỏi |
|---|---|
| 1 | ⭐ Bước này kết thúc khi nào — và **tôi đo bằng gì**? *(nếu không đo được: Chương 26, mục 26.2b)* |
| 2 | ⚠ Nếu bước này **không xong** thì máy làm gì? *(nếu chưa có đáp án: quay lại mục 23.5 nhóm A)* |
| 3 | ⚠⚠ Ai quyết định điều đó — **tôi hay khách hàng**? *(nếu là khách hàng thì đừng tự quyết)* |

> ⭐⭐ **Nguyên tắc gói cả mục này trong bốn chữ: NGHĨ TRƯỚC, LẬP TRÌNH SAU.**
>
> Cân nhắc vài cách giải khác nhau và **để thời gian mài lại trình tự** trước khi mở phần mềm — đúng
> tinh thần Bẫy 1 ở mục 23.7. ⚡ Thời gian bỏ ra ở đây **rẻ hơn nhiều lần** so với sửa cùng vấn đề đó
> ở bước 3.

---

## 23.6 Tiêu chí nghiệm thu — viết từ đầu, không viết cuối

Tiêu chí nghiệm thu là **định nghĩa của "xong"**. Viết nó ở đầu dự án có ba tác dụng, và tác dụng thứ
ba là quan trọng nhất:

1. Hai bên thống nhất được thế nào là hoàn thành.
2. Bạn biết phải chuẩn bị thử những gì.
3. ⭐ **Nó phơi ra những yêu cầu chưa ai nói.** Khi bạn viết *"nghiệm thu bằng cách nhấn E-Stop giữa
   chu trình và kiểm tra máy dừng đúng"*, khách hàng sẽ hỏi *"thế board đang kẹp thì sao?"* — và bạn
   vừa phát hiện một yêu cầu ở nhóm A.

Tiêu chí phải **đo được**, không được mơ hồ:

| ✗ Mơ hồ | ✓ Đo được |
|---|---|
| "Máy chạy ổn định" | "Chạy liên tục 8 giờ, không dừng ngoài kế hoạch quá 2 lần" |
| "Xử lý lỗi tốt" | "Rút cảm biến `DI_Clamp1Up` khi đang chạy → máy dừng trong 3 giây, màn hình hiện đúng mã lỗi S1.20" |
| "Năng suất đạt yêu cầu" | "Ra ít nhất 280 board mỗi giờ, đo trong 1 giờ liên tục" |
| "An toàn" | "Nhấn E-Stop ở từng bước của chu trình → mọi chuyển động dừng; kiểm 7 bước" |

Chú ý cột phải: mỗi dòng nêu rõ **làm gì**, **kỳ vọng gì**, **đo bao lâu**. Danh sách này chính là
nguyên liệu cho danh mục ca kiểm thử ở Chương 50.

---

## 23.7 Bẫy thường gặp

### 🔍 BẪY 1 — Mở phần mềm trước khi viết đặc tả

Bẫy trung tâm của chương. Nó hấp dẫn vì viết code cho **cảm giác tiến triển**, còn viết đặc tả thì không.

Hậu quả không phải code sai — code thường đúng. Hậu quả là **bạn đã quyết định hàng chục thứ mà không
nhận ra mình đang quyết định**: đặt tên tag, chia bước, chọn cách xử lý lỗi. Mỗi quyết định đó đóng
băng thành cấu trúc chương trình, và đổi về sau rất tốn.

**Ngưỡng thực dụng:** không viết dòng code nào cho tới khi có **bảng I/O đầy đủ** và **mô tả trình tự
bằng lời**. Hai thứ đó mất một ngày với máy cỡ DP-01 và tiết kiệm nhiều ngày về sau.

### 🔍 BẪY 2 — Đặc tả chỉ mô tả luồng chính

Đặc tả viết rất kỹ về chu trình bình thường, và **im lặng hoàn toàn** về bất thường. Kết quả: người
lập trình tự quyết định cách xử lý lỗi theo cảm tính, và mỗi lỗi được xử lý một kiểu khác nhau.

**Cách phòng:** với mỗi bước trong trình tự, hỏi ba câu: *cơ cấu không tới đích thì sao? · cảm biến
hỏng thì sao? · người vận hành nhấn Stop đúng lúc này thì sao?* Câu trả lời là phần 4 của bộ đặc tả.

### 🔍 BẪY 3 — Bảng I/O thiếu cột phân loại

Đã nêu ở mục 23.3. Nhắc lại vì hậu quả của nó là **phải đổi phần cứng**: phát hiện muộn rằng nút Dừng
phải là tiếp điểm NC, trong khi đã mua và lắp loại NO.

### 🔍 BẪY 4 — "Cứ làm như máy cũ"

Câu trả lời hay gặp nhất khi hỏi khách hàng. Nó nghe như một yêu cầu rõ ràng, nhưng thực ra là **chưa
có yêu cầu** — vì không ai biết máy cũ làm gì trong các tình huống bất thường.

**Cách xử lý:** ra xem máy cũ, ghi lại hành vi thật của nó trong các tình huống ở mục 23.5, rồi **viết
thành đặc tả và đưa khách hàng duyệt**. Thường khi đọc, khách hàng sẽ nói *"à cái này thì tôi muốn
khác"* — và đó chính là thứ bạn cần biết.

### 🔍 BẪY 5 — Đặc tả không ai duyệt

Bạn viết đặc tả, gửi email, không ai trả lời, bạn coi như đã đồng ý. Sáu tháng sau khi có tranh cãi,
im lặng không phải là bằng chứng.

**Cách phòng:** đi qua đặc tả **trực tiếp cùng người vận hành và người quản lý sản xuất**, từng phần
một. Buổi đó thường mất hai giờ và phát hiện ra nhiều thứ hơn cả tháng trao đổi email — vì người vận
hành nghĩ bằng tình huống cụ thể, không nghĩ bằng văn bản.

### 🔍 BẪY 6 — Tiêu chí nghiệm thu viết sau khi máy chạy

Viết tiêu chí sau khi máy đã chạy thì bạn sẽ vô thức viết những tiêu chí mà máy **đã đạt**. Nghiệm thu
thành công một cách vô nghĩa.

Tiêu chí phải viết **trước**, khi bạn còn chưa biết máy sẽ khó ở chỗ nào.

---

## 23.8 Bảng chốt — bộ đặc tả tối thiểu

| # | Hạng mục | Xong khi |
|---|---|---|
| 1 | **Bảng I/O** đủ 6 cột | Mọi dòng có cột phân loại và cột hành vi khi mất tín hiệu |
| 2 | **Danh sách chế độ** | Mỗi chế độ ghi rõ ai dùng, làm được gì, điều kiện vào/ra |
| 3 | **Mô tả trình tự** theo mẫu 4 dòng | Mọi bước có "điều kiện xong" là **tín hiệu thật**, và có thời gian tối đa |
| 4 | **Xử lý bất thường** | Mỗi bước đã trả lời 3 câu ở Bẫy 2 |
| 5 | **Tham số & công thức** | Mỗi tham số có đơn vị và **dải hợp lệ** |
| 6 | **Tiêu chí nghiệm thu** | Mọi tiêu chí **đo được**: làm gì · kỳ vọng gì · đo bao lâu |
| 7 | Đã hỏi **4 nhóm câu** ở mục 23.5 | Có câu trả lời bằng văn bản, không phải bằng trí nhớ |
| 8 | Đã **đi qua trực tiếp** với người vận hành | Có biên bản, có người ký |
| 9 | ⭐⭐ Không còn bước nào **viết mãi không xong** | Mỗi chỗ tắc đã quay lại mục 23.5 hỏi thêm, không cố viết tiếp |

---

## 23.9 Tự kiểm

1. Phân biệt **hai loại sai** ở mục 23.1. Vì sao loại thứ hai đắt hơn nhiều?
2. Bảng I/O có sáu cột. **Cột nào quan trọng nhất** và vì sao? Nêu một hậu quả cụ thể nếu bỏ trống nó.
3. Một câu hỏi duy nhất giúp phân loại mọi tín hiệu vào "an toàn" hay "quy trình". Câu đó là gì?
4. Mẫu mô tả bước có bốn dòng. **Dòng nào hay bị bỏ trống nhất**, và bỏ nó dẫn tới bẫy nào ở Chương 26?
5. Bạn không điền được "điều kiện xong" bằng một tín hiệu thật, chỉ điền được "sau 2 giây". Điều đó
   **nói lên gì về máy**, và phát hiện ở giai đoạn nào thì còn rẻ?
6. Nêu **ba câu hỏi ở nhóm A** (bất thường và phục hồi) mà người mới hay quên.
7. Vì sao hỏi *"anh có yêu cầu gì về xử lý lỗi không?"* thường không ra kết quả? Cách hỏi nào hiệu quả
   hơn?
8. Vì sao tiêu chí nghiệm thu phải viết **trước** khi máy chạy, chứ không phải sau?
9. ⭐⭐ Bạn viết mô tả trình tự, viết vài bước rồi tắc, sửa mãi vẫn thấy thiếu. ⭐ Đó là dấu hiệu của
    cái gì? Nêu **ba câu hỏi** để tìm chỗ thiếu.

Câu 3 và câu 5 là hai câu phân loại. Câu 3 là công cụ bạn sẽ dùng ở mọi dự án; câu 5 kiểm tra bạn nhận
ra được **đặc tả đang phát hiện thiếu sót phần cứng** — một trong những giá trị lớn nhất của việc viết
đặc tả trước.

---

### Chương tiếp theo

**Chương 24 — Đại số Boolean & bảng chân lý dùng được.** Đặc tả đã có. Trước khi dựng máy trạng thái
và trình tự, cần một công cụ để biến các điều kiện phức tạp trong đặc tả thành biểu thức logic đúng —
và biết khi nào **không** nên rút gọn chúng.

---

### Nguồn tham khảo chương 23

- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu về tài liệu kỹ thuật
  đi kèm máy, và các loại lệnh dừng — nền cho nhóm câu hỏi D. *(tiêu chuẩn có bản quyền)*
- ISO 12100 — *Safety of machinery — General principles for design*: nguyên tắc đánh giá rủi ro phải
  đi trước thiết kế — cơ sở cho cảnh báo ở mục 23.5.
- Biểu mẫu bảng I/O, mẫu mô tả trình tự và mẫu biên bản nghiệm thu — **Phụ lục C**.
- Hồ sơ đặc tả đầy đủ của DP-01 — Phụ lục J.
- **Bryan, L.A. & Bryan, E.A.** — *Programmable Controllers: Theory and Implementation*, ch. 11
  §11-1 và §11-2: ⭐ **định nghĩa nhiệm vụ → chiến lược điều khiển → lập trình**, và quy tắc ⭐ **khi
  xây trình tự thấy khó thì quay lại định nghĩa lại bài toán**; nguyên tắc *think first, program later*
  — nền cho mục 23.5b.

> ⚡ Danh sách câu hỏi ở mục 23.5 là **điểm khởi đầu, không phải danh sách đầy đủ**. Mỗi ngành có thêm
> những câu riêng. Cách tốt nhất để mở rộng danh sách này: sau mỗi dự án, ghi lại những câu mà lẽ ra
> nên hỏi sớm hơn.
