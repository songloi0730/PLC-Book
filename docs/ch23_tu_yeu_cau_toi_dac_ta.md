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

### ⭐⭐ Sáu phần đó đạt yêu cầu khi nào — và chỗ hay thiếu nhất ở từng phần

⚠ *"Đã có đủ sáu phần"* không nói được gì về chất lượng. ⭐ Bảng dưới là **nội dung tối thiểu** và
**phát biểu kiểm được** cho từng phần — cộng với ⚠ **chỗ hay thiếu nhất**, là chỗ mà đặc tả trông
đầy đủ nhưng sẽ vỡ ở khâu lập trình.

| # | Phần | ⭐ Nội dung tối thiểu | ⭐⭐ Đạt khi | ⚠ Chỗ hay thiếu nhất |
|---|---|:--|:--|:--|
| 1 | **Bảng I/O** | Mọi tín hiệu vật lý · kiểu thiết bị · NO/NC · PNP/NPN · trạng thái nghỉ · ⭐ **phân loại** (an toàn / quá trình / chẩn đoán) | Danh mục kiểm ở **C.1** đạt hết, không mục nào bỏ trống | ⚠⚠ **Cột phân loại** — thiếu nó thì tín hiệu an toàn bị xử lý như tín hiệu thường (Bẫy 3) |
| 2 | **Danh sách chế độ** | Tên chế độ · ai được dùng · làm được gì · ⭐ **điều kiện vào VÀ điều kiện ra** · ngõ ra nào còn tác dụng trong chế độ đó | Vẽ được **bảng chuyển trạng thái C.4** mà không phải hỏi lại ai | ⚠⚠ **Điều kiện RA khỏi chế độ**, và ⭐ **cơ cấu đang giữa chừng thì sao** khi đổi chế độ |
| 3 | **Mô tả trình tự** | Từng bước: điều kiện vào · hành động · ⭐ **điều kiện ra là PHẢN HỒI THẬT** · ⭐ **thời gian tối đa** | Người khác đọc rồi **vẽ lại lưu đồ trùng với lưu đồ của bạn** | ⚠ **Thời gian tối đa từng bước** — nó chính là timeout về sau; thiếu ở đây thì lập trình sẽ **đoán** (Chương 26 mục 26.4) |
| 4 | **Xử lý bất thường** | Với mỗi lỗi: máy làm gì **ngay** · ngõ ra nào **giữ nguyên** · phục hồi ra sao · ⭐ **ai được phép reset** | ⭐⭐ **Mọi thiết bị trong bảng I/O** đều xuất hiện ít nhất một lần trong câu hỏi *"nếu cái này hỏng thì sao"* | ⚠⚠ **Phần phục hồi.** Người ta viết *"báo lỗi và dừng"* rồi hết — nhưng **dừng rồi làm sao chạy tiếp** mới là phần tốn thời gian nhất khi lập trình |
| 5 | **Tham số & công thức** | Tên · đơn vị · ⭐ **dải hợp lệ** · giá trị mặc định · ai được sửa · ⭐ **sửa được lúc nào** | Điền kín **C.5**, không ô nào để trống dải hợp lệ | ⚠ **Dải hợp lệ** và ⚠⚠ **"sửa được lúc nào"** — đổi công thức giữa chu trình là một lớp lỗi riêng (Chương 29) |
| 6 | **Tiêu chí nghiệm thu** | Mỗi chỉ tiêu: **làm gì · kỳ vọng gì · đo bao lâu** | Không dòng nào chứa từ *"ổn định"*, *"tốt"*, *"đạt yêu cầu"* — xem mục 23.6 | ⚠ **Cách đo**. Có chỉ tiêu mà không có cách đo thì nó sẽ được **đo theo cách có lợi cho bên đang vội** |

> ⭐⭐ **Phần 2 và phần 4 là nơi chi phí ẩn nấp, và cũng là hai phần bị viết sơ sài nhất.**
>
> ⚡ Phần 1, 3, 5 dễ viết vì chúng mô tả **máy chạy đúng** — ai cũng hình dung được. ⚠ Phần 2 và 4
> mô tả **máy không chạy đúng**, và đó là trạng thái mà lúc ngồi viết đặc tả **chưa ai từng thấy**.
>
> ⭐ Kinh nghiệm dùng được: khi đặc tả có phần 3 dài gấp nhiều lần phần 4, ⚠ **gần như chắc chắn
> phần 4 còn thiếu** — chứ không phải máy này ít lỗi.

> ⚠ **Một quy tắc về người duyệt.** ⭐ Phần 1 và 3 nên có **người vận hành thật** đọc, không chỉ kỹ
> sư — họ là người phát hiện *"chỗ này thực tế không làm thế"*. ⚠⚠ Còn phần liên quan an toàn thì
> ⭐ **kỹ sư duyệt không thay được người có thẩm quyền về an toàn** (Chương 6, 47).

---

## 23.2b ⭐⭐ Chín bước đầu dự án — thứ tự, sản phẩm, và cái gì chặn cái gì

Mục trên nói **đặc tả gồm gì**. ⭐ Mục này nói **làm theo thứ tự nào, mỗi bước đẻ ra tài liệu gì, và
bước nào không xong thì kẹt bước nào** — vì sai lầm đắt nhất ở đầu dự án hiếm khi là viết sai một
tài liệu; nó là **làm đúng tài liệu nhưng sai thứ tự**.

> ⭐ Chín bước này nằm gọn trong **giai đoạn 1 và 2 của Chương 57**. Chương 57 kể chúng như một câu
> chuyện về một cỗ máy cụ thể; ⭐ ở đây chúng là một **bảng công tác** dùng được cho máy của bạn.

| # | Bước | ⭐ Sản phẩm | ⚠ Không xong thì chặn | Ai duyệt |
|---|---|---|---|---|
| 1 | Nhận yêu cầu, **hỏi bốn nhóm câu hỏi** (mục 23.5) | Biên bản họp, có **danh sách câu chưa trả lời được** | Mọi bước sau | Khách hàng |
| 2 | ⚠⚠ **Đánh giá rủi ro** | Hồ sơ rủi ro + **mức an toàn yêu cầu** cho từng chức năng | ⭐ **Bước 5 và 6** — chưa biết mức thì không chọn được thiết bị | ⭐ **Người có thẩm quyền về an toàn** |
| 3 | Viết đặc tả sáu phần (mục 23.2) | FS, kèm biểu mẫu **C.3 · C.4 · C.5** | Bước 4, và mọi việc lập trình | ⭐⭐ Khách hàng **ký** (Bẫy 5) |
| 4 | ⭐⭐ **Lập bảng I/O** (mục 23.3) | ⭐ **C.1** | Bước 5, 6, 7 và **đấu tủ** | Nội bộ + khách xem |
| 5 | Chọn PLC | Bảng công tác **§13.4** đã điền đủ 11 mục | Bước 6 | Nội bộ |
| 6 | ⭐ **Lập cấu hình phần cứng** | ⭐ **C.10** — bản đồ khe cắm + thiết bị mạng | Bước 7, **đấu tủ**, và việc dựng lại CPU sau này | Nội bộ |
| 7 | ⭐ **Lập danh mục vật tư** | ⭐ **C.11** | ⚠ **Đặt hàng** — và thời gian có hàng quyết định tiến độ | Mua hàng |
| 8 | Các phép tính | Công suất nguồn 24 V (§8.7, §9.5) · tuổi thọ van và cáp (§9.3, §49.7) | ⭐ Chốt bước 7 — đổi kết quả tính là đổi đơn hàng | Nội bộ |
| 9 | Phác **tiêu chí nghiệm thu** (mục 23.6) | Bản phác, hoàn thiện sau | — | Khách hàng |

### ⭐⭐ "Xong" nghĩa là gì — định nghĩa kiểm được cho từng bước

⚠ *"Đã viết đặc tả rồi"* không phải một trạng thái kiểm được. ⭐ Dưới đây là phát biểu kiểm được, và
⭐⭐ **mỗi dòng phải trả lời được bằng có hoặc không, không có "gần xong"**:

| # | ⭐ Bước này xong khi… |
|---|:--|
| 1 | ⭐ **Danh sách câu chưa trả lời được đã rỗng**, hoặc mỗi câu còn lại có **tên người chịu trách nhiệm và hạn** |
| 2 | Mọi mối nguy đã liệt kê đều có **biện pháp và mức yêu cầu**; ⚠ không mối nguy nào ở trạng thái *"sẽ xử lý bằng phần mềm, tính sau"* |
| 3 | ⭐⭐ Một người **không tham gia viết** đọc đặc tả và **mô tả lại được một chu trình** cùng **hai tình huống lỗi** |
| 4 | Mọi tag có **một** nghĩa; ⭐ còn **≥ 20 % kênh dự phòng**; tín hiệu an toàn đã tách riêng — xem danh mục kiểm ở **C.1** |
| 5 | Cả **11 mục** của §13.4 đã điền, ⚠ **kể cả mục 8, 9, 10** — ba mục hay để trống nhất |
| 6 | ⭐ Phép thử một phút ở **C.10** đạt: người chưa mở tủ chỉ ra được một tag nằm ở khe nào, kênh nào |
| 7 | ⭐ Phép thử một phút ở **C.11** đạt: ba tag bất kỳ đều trả lời được *mã gì, bao lâu có hàng, có dự phòng không* |
| 8 | ⭐⭐ Mọi con số đã **nhân hệ số dự phòng**, và ⚠ **ghi rõ giả định** — dòng đỉnh giả định mấy cơ cấu cùng tác động |
| 9 | Mỗi chỉ tiêu có **cách đo** đi kèm; ⚠ *"máy chạy ổn định"* không phải tiêu chí — xem mục 23.6 |

### ⚠⚠ Ba quan hệ chặn quan trọng nhất, và vì sao đảo thứ tự là tốn tiền thật

| Quan hệ | Đảo thứ tự thì sao |
|---|---|
| ⚠⚠ **Bước 2 chặn bước 5 và 6** | Chọn xong phần cứng rồi mới đánh giá rủi ro thì chỉ còn hai lối: **sửa thiết kế** (mất tiền) hoặc ⚠⚠ **hạ chuẩn an toàn cho vừa thiết kế** (không được phép). Chương 57 Bẫy 2 |
| ⭐⭐ **Bước 4 chặn bước 6, 7 và việc đấu tủ** | Đấu tủ trước khi có bảng I/O thì **số dây không khớp tên tag**, và cái lệch đó **theo máy suốt vòng đời** — không sửa được rẻ ở bất kỳ thời điểm nào sau đó. Chương 57 Bẫy 3 |
| ⭐ **Bước 8 chặn chốt bước 7** | Tính công suất nguồn **sau khi** đã đặt hàng nghĩa là hoặc đổi đơn, hoặc ⚠ dùng nguồn thiếu — và nguồn thiếu cho ra **lỗi lạ khi nhiều cơ cấu cùng tác động**, loại lỗi bị đi tìm trong chương trình (Chương 8 mục 8.7) |

> ⭐⭐ **Một cách kiểm tra rất nhanh xem dự án có đang đi đúng thứ tự không:** hỏi *"đã đặt hàng
> chưa?"* và *"bảng I/O đã ký chưa?"*. ⚠ Nếu câu đầu là **rồi** mà câu sau là **chưa**, ⭐ dự án
> đang đi ngược, và phần chênh sẽ hiện ra ở khâu đấu tủ.

> ⚡ **Về việc chín bước này mất bao lâu.** ⚠ Không có con số chung — tuỳ quy mô máy. ⭐ Nhưng có một
> tỉ lệ đáng tham khảo: với máy cỡ máy mẫu của sách, ⭐⭐ **phần việc từ bước 1 tới bước 9 thường
> chiếm 15–25 % tổng thời gian dự án**, và ⚠ nhóm nào rút nó xuống dưới 10 % gần như luôn trả lại
> phần chênh đó ở khâu chạy thử — cộng lãi.
>
> ⭐ Con số này là **kinh nghiệm nghề, không phải chuẩn**. Hãy tự đo trên hai, ba dự án của chính bạn
> rồi dùng con số của mình.

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
