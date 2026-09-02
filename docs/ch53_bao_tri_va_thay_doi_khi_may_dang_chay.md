
# Chương 53 — Bảo trì & thay đổi khi máy đang chạy

> **Lát cắt máy mẫu:** 5 — máy đầy đủ, đã bàn giao và đang sản xuất.

---

## 53.1 Bài toán: một dòng lệnh lúc hai giờ chiều

Máy đang chạy. Có một lỗi nhỏ: cảm biến báo board hơi sớm nên đôi khi trạm 1 bắt đầu tra keo trước
khi board dừng hẳn. Không hỏng board, chỉ hơi lệch.

Kỹ sư kết nối, sửa một dòng: thêm 200 ms trễ. Nạp xuống. **Máy đang chạy** — không dừng, không mất
sản lượng, sửa xong trong hai phút. Ai cũng vui.

Ba tuần sau, máy có lỗi lạ ở trạm 2. Người khác mở chương trình ra xem, đối chiếu với bản in trong
tủ hồ sơ — **bản in không có dòng trễ 200 ms đó**. Bản trên máy khác bản trong hồ sơ. Không ai biết
còn khác chỗ nào nữa.

> ⭐ **Sửa trong hai phút. Mất niềm tin vào toàn bộ tài liệu.**
>
> Từ lúc đó, mọi câu hỏi "chương trình làm gì ở đây?" đều phải trả lời bằng cách **đọc chương trình
> trên máy**, vì không còn tin được bản nào khác. Và mỗi lần đọc là một lần dừng máy hoặc một lần
> kết nối vào máy đang chạy.

Chương này về hai việc gắn với nhau: **thay đổi có kiểm soát** và **bảo trì nhìn từ PLC**.

---

## 53.2 ⚠⚠ Sửa trực tuyến *(online edit)*

Hầu hết PLC cho phép sửa chương trình **trong lúc máy đang chạy** và nạp thay đổi mà không dừng chu
trình.

Đây là một trong những khả năng nguy hiểm nhất trong nghề.

### Vì sao nó nguy hiểm

| Rủi ro | Giải thích |
|---|---|
| ⚠⚠ **Cơ cấu có thể chuyển động ngay** | Sửa xong, ngõ ra đổi trạng thái **trong vòng một chu kỳ quét** — người đang đứng cạnh máy không được báo trước |
| ⚠ **Không quay lại được** | Nhiều hệ thống không có "hoàn tác" sau khi đã nạp |
| ⚠ **Trạng thái đang chạy dở** | Bước 5 đang chạy, bạn sửa bước 5 — máy đang ở đâu trong bước đó? |
| ⭐ **Thay đổi không được ghi lại** | Đây là cỗ máy ở mục 53.1 |
| **Sửa vội thì không kiểm thử** | Cả quy trình ở Chương 50 bị bỏ qua |

> ⚠⚠ **Trước khi sửa trực tuyến, hãy trả lời được: nếu ngõ ra đổi trạng thái ngay lúc này, có ai bị
> thương không?**
>
> Nếu không chắc chắn trả lời được **"không"**, thì dừng máy đã. Chương 6 và Chương 47 nói về việc
> bảo vệ người khỏi chuyển động bất ngờ; sửa trực tuyến là cách **tự tạo ra** chuyển động bất ngờ.

### ⭐ Khi nào sửa trực tuyến là hợp lý

Nó không phải điều cấm tuyệt đối — có những lúc nó là lựa chọn đúng:

| Trường hợp | Điều kiện |
|---|---|
| Sửa thứ **không tác động ngõ ra** | Thêm bit chẩn đoán, sửa văn bản báo động, thêm bộ đếm |
| Chỉnh **tham số**, không chỉnh logic | ⭐ Và tốt hơn nữa: đưa tham số đó lên HMI để **không cần sửa chương trình** (Chương 44) |
| Quy trình liên tục **không dừng được** | ⚠ Có kế hoạch, có người canh máy, có duyệt |
| Đang **chẩn đoán** với máy ở chế độ an toàn | Không ai trong vùng nguy hiểm |

> ⭐⭐ **Quy tắc thực dụng: nếu thay đổi có thể chờ tới lần dừng máy kế tiếp, thì hãy để nó chờ.**
>
> Áp lực "máy đang chạy, đừng dừng" là có thật và mạnh. Nhưng hầu hết thay đổi **chờ được vài giờ** —
> và vài giờ đó đổi lấy: có thời gian kiểm thử, có sao lưu, có người thứ hai xem lại, và không có ai
> đứng cạnh cơ cấu lúc nó bất ngờ động đậy.

### ⚡ Nếu buộc phải sửa trực tuyến

| Bước | Việc |
|---|---|
| 1 | ⭐ **Sao lưu bản đang chạy TRƯỚC** — xem mục 53.4 và Chương 54 |
| 2 | ⚠ **Kiểm tra không có ai trong vùng nguy hiểm**, và báo cho người vận hành |
| 3 | Xem lại thay đổi trên **bản ngoại tuyến** trước, nếu công cụ cho phép |
| 4 | ⭐ Xác định trước: **nếu sai thì quay lại bằng cách nào** |
| 5 | Nạp thay đổi |
| 6 | ⭐ **Quan sát ít nhất vài chu trình đầy đủ** trước khi rời máy |
| 7 | ⭐⭐ **Ghi lại ngay** — trong ngày, không phải "để mai" |

> ⚠ **Bước 7 là bước hay bị bỏ nhất, và là bước tạo ra vấn đề ở mục 53.1.** Sửa xong thì máy chạy,
> mọi người đi làm việc khác, và ghi chép trôi mất.

---

## 53.3 Quy trình thay đổi có kiểm soát

"Có kiểm soát" nghe nặng nề, nhưng thực chất chỉ là **năm câu hỏi** trả lời được trước khi sửa.

| # | Câu hỏi | Vì sao |
|---|---|---|
| 1 | ⭐ **Vì sao thay đổi?** | Ghi lý do, không chỉ ghi nội dung. Sáu tháng sau, "vì sao" mới là thứ cần |
| 2 | ⭐ **Ai duyệt?** | Với thay đổi chạm mạch an toàn: ⚠ **bắt buộc có người thứ hai** |
| 3 | ⭐ **Đã sao lưu bản đang chạy chưa?** | Không sao lưu thì không có đường lùi |
| 4 | **Kiểm thử thế nào?** | Chương 50 — mô phỏng, chạy khô, chạy có phôi |
| 5 | ⭐ **Ai cần biết?** | Người vận hành ca sau, bảo trì, và người viết tài liệu |

### ⭐ Mức độ theo rủi ro

Không phải thay đổi nào cũng cần cùng mức nghiêm ngặt:

| Mức | Ví dụ | Yêu cầu |
|---|---|---|
| **Thấp** | Sửa văn bản báo động, thêm bit chẩn đoán | Ghi lại là đủ |
| **Vừa** | Đổi thời gian trễ, đổi ngưỡng, đổi thứ tự bước | Sao lưu + kiểm thử + ghi lại |
| ⚠ **Cao** | Chạm logic chuyển động, đổi ánh xạ I/O | ⭐ Sao lưu + **người thứ hai xem** + kiểm thử đầy đủ + ghi lại |
| ⚠⚠ **Rất cao** | ⭐ **Chạm mạch an toàn, chương trình an toàn, cấu hình thiết bị an toàn** | Toàn bộ mức Cao + ⚠ **kiểm định lại theo Chương 47–48**; ⚠ **không bao giờ sửa trực tuyến** |

> ⚠⚠ **Dòng cuối là ranh giới cứng.** Chức năng an toàn được đánh giá và nghiệm thu như một tổng
> thể (Chương 48). Sửa một mảnh của nó mà không đánh giá lại thì **kết quả đánh giá cũ không còn giá
> trị** — dù thay đổi trông nhỏ đến đâu.

### ⭐ Điều làm quy trình này sống được

Quy trình thay đổi thất bại vì cùng một lý do ở mọi nơi: **nó làm việc gấp trở nên chậm**. Nên:

| Nguyên tắc | Nội dung |
|---|---|
| ⭐ **Ghi chép phải mất dưới hai phút** | Một biểu mẫu ngắn, không phải ba trang |
| ⭐ **Ghi ngay tại máy** | Sổ trong tủ điện, hoặc một mục trên HMI — không phải máy tính ở phòng khác |
| **Có đường "khẩn cấp"** | Cho phép sửa trước, ⭐ **duyệt và ghi trong 24 giờ** — thà vậy còn hơn không ghi gì |
| **Người duyệt phải sẵn có** | Nếu chỉ một người duyệt được và người đó nghỉ phép, quy trình sẽ bị lách |

> ⭐ **Một quy trình bị lách còn tệ hơn không có quy trình** — vì nó tạo cảm giác an toàn giả, trong
> khi thực tế các thay đổi vẫn xảy ra, chỉ là không ai ghi lại.

---

## 53.4 Tài liệu **as-built** và bản thiết kế

Hai thứ khác nhau, và lẫn lộn chúng là nguồn của rất nhiều giờ lãng phí.

| | **Bản thiết kế** | ⭐ **Tài liệu as-built** |
|---|---|---|
| Mô tả | Máy **sẽ** như thế nào | ⭐ Máy **hiện đang** như thế nào |
| Làm lúc nào | Trước khi chế tạo | ⭐ **Cập nhật suốt vòng đời** |
| Ai dùng | Người chế tạo | ⭐ **Người sửa máy lúc hai giờ sáng** |
| Khi hai bản khác nhau | | ⭐ **as-built là bản đúng** |

### Gồm những gì

| Hạng mục | Ghi chú |
|---|---|
| ⭐ **Chương trình PLC hiện hành** | Kèm số phiên bản và ngày (Chương 54) |
| Sơ đồ điện đã sửa theo thực tế | ⚠ Kể cả những sợi dây "đấu tạm" |
| Bảng I/O hiện hành | Chương 23 |
| Danh sách tham số / công thức đang dùng | Chương 32 |
| ⭐ **Nhật ký thay đổi** | Ngày · người · nội dung · **lý do** |
| Cấu hình mạng và địa chỉ | Chương 40 |
| Cấu hình thiết bị an toàn | ⚠ Kèm hồ sơ kiểm định (Chương 48) |

> ⚠ **"Đấu tạm" là thứ nguy hiểm nhất trong danh mục trên.** Một sợi dây nối tắt để chạy tạm qua ca
> đêm sẽ **ở lại đó ba năm** nếu không ai ghi. Và người phát hiện ra nó thường là người đang tìm một
> lỗi khác, lúc nửa đêm.
>
> ⭐ **Nếu buộc phải đấu tạm: ghi vào nhật ký, dán nhãn tại chỗ, và ghi ngày dự kiến gỡ.**

### ⭐ Vì sao as-built luôn lạc hậu

Vì cập nhật nó là **việc làm sau khi đã xong việc** — và lúc đó máy đã chạy, mọi người đã nhẹ nhõm,
áp lực đã hết.

Cách duy nhất hiệu quả là làm nó thành **một phần của việc sửa**, không phải việc riêng sau đó:

| Cách | Nội dung |
|---|---|
| ⭐ **Chú thích trong chính chương trình** | Chương 24 — comment ngay chỗ sửa, kèm ngày và lý do; nó **đi theo chương trình**, không lạc mất |
| ⭐ **Sao lưu là hành động ghi chép** | Tên tệp sao lưu chứa ngày + lý do (Chương 54) |
| **Ảnh chụp** | Nhanh hơn vẽ lại sơ đồ; ⚡ đủ dùng cho thay đổi nhỏ |
| **Một trang duy nhất trong tủ** | Nhật ký thay đổi in sẵn, treo trong tủ điện |

> ⭐⭐ **Chú thích trong chương trình là dạng tài liệu duy nhất không thể lạc mất bản.** Sơ đồ giấy
> thất lạc, tệp trên máy tính bị thay, nhưng comment nằm trong chương trình thì **luôn đi cùng bản
> đang chạy** — kể cả khi ai đó tải nó từ PLC về.
>
> Đây là lý do Chương 24 nhấn mạnh comment giải thích **vì sao**, không phải **cái gì**.

---

## 53.5 Bảo trì phòng ngừa nhìn từ PLC

PLC biết những thứ mà không ai khác biết — nó đếm được. Dùng nó cho bảo trì là việc rẻ và bị bỏ qua
nhiều nhất.

### ⭐ Đếm cái gì

| Đếm | Dùng để | Chương |
|---|---|---|
| ⭐ **Số lần đóng cắt của từng ngõ ra** | So với tuổi thọ rơ-le / van | 9 mục 9.3 |
| ⭐ **Số chu trình của cơ cấu chuyển động** | So với tuổi thọ cáp xích, vòng bi, dây đai | 49 mục 49.7 |
| **Giờ chạy của động cơ, bơm, quạt** | Lịch thay dầu, thay bộ lọc | 36 |
| ⭐ **Thời gian thực hiện từng bước** | ⭐ **Xu hướng tăng = thứ gì đó đang mòn** | 55 |
| Số lần báo động theo mã | Mã nào tăng dần = hỏng hóc đang tới | 43 |
| Số lỗi mạng | Cáp hoặc đầu nối đang xuống cấp | 40 mục 40.6 |
| Dòng động cơ ở cùng tải | So với mốc lúc nghiệm thu | 36 mục 36.8 |

> ⭐⭐ **Hàng quan trọng nhất là "thời gian thực hiện từng bước".**
>
> Một xi-lanh sắp hỏng **không hỏng đột ngột** — nó chậm dần. Một bộ lọc khí tắc dần làm mọi động
> tác khí nén chậm dần. Máy vẫn chạy đúng, sản lượng vẫn đủ, không có báo động nào — nhưng con số
> đang trôi.
>
> ⭐ **Ghi con số đó lại thì bạn thấy nó trôi. Không ghi thì bạn chỉ thấy lúc nó dừng hẳn.**

### Ba mức, từ rẻ tới đắt

| Mức | Cách làm | Chi phí |
|---|---|---|
| **1 — Đếm** | ⭐ Bộ đếm giữ được qua mất điện (Chương 12), hiện trên HMI | Gần như bằng không |
| **2 — Ngưỡng** | Báo *nhắc nhở* khi bộ đếm vượt ngưỡng — ⚡ **nhắc, không phải dừng máy** | Vài giờ lập trình |
| **3 — Xu hướng** | Ghi số liệu ra ngoài, xem đồ thị theo thời gian | Cần Chương 45 |

> ⚡ **Mức 2 phải là báo nhắc nhở, không được là lỗi dừng máy.** Một máy tự dừng vì "đã tới hạn thay
> van" sẽ bị người vận hành tìm cách vô hiệu hoá trong vòng một tuần — và khi đó bạn mất luôn cả mức
> 1.

### ⭐ Đặt ngưỡng thế nào

```text
Ngưỡng nhắc  =  tuổi thọ theo datasheet  ×  0,7        (còn thời gian đặt hàng)
Ngưỡng cảnh báo = tuổi thọ theo datasheet × 0,9        (nên thay ở lần dừng máy tới)
```

Với van khí ở DP-01 (Chương 9 mục 9.3 tính được 2,88 triệu lần đóng cắt mỗi năm), nếu datasheet ghi
tuổi thọ 20 triệu lần:

```text
Ngưỡng nhắc     = 14 000 000 lần  →  khoảng năm thứ 5
Ngưỡng cảnh báo = 18 000 000 lần  →  khoảng năm thứ 6
```

> ⭐ **Phép tính này chỉ có ý nghĩa nếu bộ đếm sống sót qua mất điện và qua việc nạp lại chương
> trình.** Xem Chương 12 về vùng nhớ giữ được, và ⚠ **kiểm tra thực tế** — nhiều người phát hiện bộ
> đếm bảo trì của mình bị xoá mỗi lần nạp chương trình, sau khi đã đếm được ba năm.

---

## 53.6 Trên máy mẫu DP-01

| Hạng mục | Quyết định |
|---|---|
| ⚠ **Sửa trực tuyến** | Cho phép với thay đổi **không tác động ngõ ra**; ⚠⚠ **cấm với mạch an toàn và logic chuyển động** |
| Nhật ký thay đổi | Một trang in, treo trong tủ điện; ⭐ ghi ngay tại máy |
| Người duyệt | Thay đổi mức Cao trở lên: ⭐ **người thứ hai xem** |
| Chú thích khi sửa | ⭐ Comment tại chỗ, kèm **ngày + lý do** |
| Sao lưu | ⭐ **Trước mọi thay đổi**, và sau khi thay đổi ổn định (Chương 54) |
| Bộ đếm bảo trì | Van keo · van kẹp · chu trình gantry · giờ chạy đèn UV · giờ chạy chuyền |
| ⭐ Đo thời gian bước | Trạm 1 tra keo · trạm 2 sấy UV · gantry về gốc (Chương 55) |
| Ngưỡng | ⚡ **Báo nhắc nhở**, hiện trên HMI, ⚠ **không dừng máy** |

### ⭐ Hạng mục riêng của đèn UV

Đèn UV là ví dụ điển hình cho cả mục 53.5:

| Đặc điểm | Hệ quả |
|---|---|
| ⭐ **Cường độ giảm dần theo giờ chạy** | Board vẫn "được sấy" nhưng keo **cứng chưa đủ** — và không có báo động nào |
| Không nhìn ra bằng mắt | Ánh sáng vẫn có, chỉ yếu đi |
| Phát hiện muộn | ⚠ Thường là khi khách hàng phản ánh, hàng tuần sau |

Cách xử lý trên DP-01:

| Cách | Nội dung |
|---|---|
| ⭐ **Đếm giờ chạy đèn**, so với tuổi thọ nhà sản xuất công bố | Mức 1 |
| ⭐ **Đọc `AI_UvIntensity`** và ghi lại theo thời gian | Mức 3 — thấy xu hướng giảm |
| Báo nhắc khi cường độ xuống dưới ngưỡng | ⚡ Nhắc, kèm số liệu |

> ⭐⭐ **Đây là lý do `AI_UvIntensity` tồn tại trên máy mẫu.** Nó không dùng để điều khiển — nó dùng
> để **biết một thứ đang xấu đi trước khi nó gây ra hàng lỗi**.
>
> Rất nhiều tín hiệu analog đáng thêm vào máy có cùng lý do như vậy: không phải để điều khiển, mà để
> **nhìn thấy sự trôi**.

---

## 53.7 Bẫy thường gặp

### 🔍 BẪY 1 — Sửa trực tuyến khi có người cạnh máy

**Hiện tượng:** ⚠⚠ cơ cấu chuyển động ngay khi nạp; người đứng cạnh không được báo trước.
**Cách sửa:** kiểm tra vùng nguy hiểm và **báo người vận hành** trước khi nạp (mục 53.2).

### 🔍 BẪY 2 — Sửa xong quên ghi

**Hiện tượng:** ⭐ đúng cỗ máy ở mục 53.1 — bản trên máy khác bản trong hồ sơ, và **không ai biết còn
khác chỗ nào**.
**Cách sửa:** ghi ngay trong ngày; comment tại chỗ trong chương trình (mục 53.4).

### 🔍 BẪY 3 — Sửa mạch an toàn "một chút"

**Hiện tượng:** ⚠⚠ kết quả đánh giá an toàn cũ **không còn giá trị**, nhưng hồ sơ vẫn nói là có.
**Cách sửa:** mọi thay đổi chạm an toàn → ⚠ **đánh giá lại theo Chương 47–48**, không sửa trực tuyến.

### 🔍 BẪY 4 — Không sao lưu trước khi sửa

**Hiện tượng:** sửa sai, và **không có đường lùi** — phải đi tìm bản cũ nhất còn giữ được.
**Cách sửa:** sao lưu là **bước 1**, không phải bước cuối (mục 53.2, Chương 54).

### 🔍 BẪY 5 — Quy trình nặng tới mức bị lách

**Hiện tượng:** ⭐ mọi người vẫn sửa, chỉ là **không ai ghi** — tệ hơn không có quy trình.
**Cách sửa:** ghi chép dưới hai phút, ghi tại máy, có đường khẩn cấp (mục 53.3).

### 🔍 BẪY 6 — Đấu tạm không dán nhãn

**Hiện tượng:** ⚠ sợi dây nối tắt ở lại **ba năm**, và người phát hiện là người đang tìm lỗi khác lúc
nửa đêm.
**Cách sửa:** ghi vào nhật ký, dán nhãn tại chỗ, ghi **ngày dự kiến gỡ** (mục 53.4).

### 🔍 BẪY 7 — Bộ đếm bảo trì bị xoá khi nạp chương trình

**Hiện tượng:** ⚠ đếm được ba năm rồi phát hiện số về không sau một lần nạp.
**Cách sửa:** dùng vùng nhớ giữ được (Chương 12), và ⭐ **kiểm tra thực tế bằng cách nạp thử**.

### 🔍 BẪY 8 — Ngưỡng bảo trì làm dừng máy

**Hiện tượng:** ⚡ người vận hành vô hiệu hoá tính năng trong một tuần — mất luôn cả bộ đếm.
**Cách sửa:** ngưỡng chỉ **nhắc**, không dừng (mục 53.5).

### 🔍 BẪY 9 — Chỉ theo dõi lỗi, không theo dõi sự trôi

**Hiện tượng:** ⭐ mọi thứ "bình thường" cho tới ngày dừng hẳn; xi-lanh chậm dần mà không ai thấy.
**Cách sửa:** ⭐ **đo thời gian thực hiện từng bước** và ghi lại (mục 53.5, Chương 55).

### 🔍 BẪY 10 — Chỉ ghi "cái gì", không ghi "vì sao"

**Hiện tượng:** sáu tháng sau, người khác thấy dòng trễ 200 ms, **không biết vì sao có**, và xoá nó
đi khi "dọn dẹp".
**Cách sửa:** ⭐ lý do là trường **quan trọng nhất** trong nhật ký thay đổi (mục 53.3, Chương 24).

---

## 53.8 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| ⚠⚠ Sửa trực tuyến nguy hiểm ở đâu | **Cơ cấu có thể chuyển động ngay**, không quay lại được, không được ghi lại |
| Câu hỏi phải trả lời trước khi sửa trực tuyến | ⚠ **"Nếu ngõ ra đổi trạng thái ngay lúc này, có ai bị thương không?"** |
| ⭐⭐ Quy tắc thực dụng | **Chờ được tới lần dừng máy kế tiếp thì hãy để nó chờ** |
| Bước 1 của mọi thay đổi | ⭐ **Sao lưu bản đang chạy** |
| Bước hay bị bỏ nhất | ⭐ **Ghi lại** — làm ngay trong ngày |
| Năm câu hỏi của quy trình | Vì sao · ai duyệt · đã sao lưu chưa · kiểm thử thế nào · ai cần biết |
| ⚠⚠ Thay đổi chạm mạch an toàn | **Đánh giá lại** (Ch.47–48); **không bao giờ sửa trực tuyến** |
| Vì sao quy trình bị lách | Nó làm việc gấp trở nên chậm → ⭐ ghi chép **dưới hai phút**, **tại máy** |
| ⭐ as-built vs bản thiết kế | as-built = máy **hiện đang** thế nào; khi khác nhau, **as-built là bản đúng** |
| Dạng tài liệu không lạc được bản | ⭐⭐ **Comment trong chính chương trình** |
| Đấu tạm | ⚠ Ghi nhật ký + dán nhãn + **ngày dự kiến gỡ** |
| PLC đếm gì cho bảo trì | Số lần đóng cắt · số chu trình · giờ chạy · ⭐ **thời gian từng bước** · số báo động · lỗi mạng |
| ⭐⭐ Vì sao đo thời gian bước | **Thứ sắp hỏng thì chậm dần, không hỏng đột ngột** |
| Ngưỡng bảo trì phải là gì | ⚡ **Nhắc nhở**, không dừng máy |
| Đặt ngưỡng ở đâu | ~0,7 tuổi thọ (nhắc) và ~0,9 (cảnh báo) |
| ⚠ Kiểm tra bắt buộc với bộ đếm | **Nó có sống sót qua lần nạp chương trình không?** |

---

## 53.9 Tự kiểm

1. ⭐ Kể lại sự việc ở mục 53.1. Thiệt hại thật sự là gì — và vì sao nó lớn hơn nhiều so với một dòng
   lệnh?
2. ⚠⚠ Nêu năm rủi ro của sửa trực tuyến. Câu hỏi nào phải trả lời được trước khi nạp?
3. Nêu bốn trường hợp sửa trực tuyến là hợp lý. Điểm chung của chúng là gì?
4. ⭐⭐ Phát biểu quy tắc thực dụng về sửa trực tuyến. Vì sao "vài giờ chờ" thường đáng giá?
5. Kể năm câu hỏi của quy trình thay đổi có kiểm soát. Câu nào hay bị bỏ nhất?
6. ⚠⚠ Vì sao thay đổi chạm mạch an toàn phải được đánh giá lại, dù thay đổi rất nhỏ?
7. ⭐ Vì sao một quy trình bị lách còn tệ hơn không có quy trình? Nêu bốn cách làm quy trình sống
   được.
8. ⭐ Phân biệt **bản thiết kế** và **tài liệu as-built** trên bốn tiêu chí. Khi hai bản khác nhau,
   tin bản nào?
9. ⭐⭐ Vì sao comment trong chương trình là dạng tài liệu **không thể lạc mất bản**?
10. Nêu bảy thứ PLC có thể đếm cho bảo trì. Thứ nào giá trị nhất, và vì sao?
11. ⭐ Tính ngưỡng nhắc và ngưỡng cảnh báo cho van khí DP-01 với tuổi thọ datasheet 20 triệu lần và
    2,88 triệu lần đóng cắt mỗi năm. Chúng rơi vào năm thứ mấy?
12. ⚡ Vì sao ngưỡng bảo trì **không được** làm dừng máy?
13. ⭐⭐ Vì sao `AI_UvIntensity` tồn tại trên DP-01, dù nó không dùng để điều khiển gì?

> Câu 4, 8, 9 và 13 là bốn câu phân loại. Câu 13 là ý sâu nhất của chương: ⭐ **một số tín hiệu tồn
> tại không phải để điều khiển, mà để nhìn thấy sự trôi trước khi nó thành hàng lỗi.**

---

### Chương tiếp theo

Chương 54 — **Sao lưu, phiên bản & bảo mật chương trình**. Chương này nói "sao lưu trước khi sửa" ở
mọi mục; chương sau nói **sao lưu cái gì, để ở đâu, và làm sao biết bản sao lưu còn dùng được**.

### Nguồn tham khảo chương 53

- IEC 62443 (bộ) — *Industrial communication networks — IT security*: quản lý thay đổi và kiểm soát
  truy cập vào hệ thống điều khiển. *(tiêu chuẩn có bản quyền)*
- IEC 61508 và ISO 13849-1 — yêu cầu **quản lý thay đổi** với chức năng an toàn: cơ sở cho ranh giới
  ở mục 53.3.
- IEC 60204-1 — yêu cầu về tài liệu kỹ thuật đi kèm máy.
- **Datasheet thiết bị** — dùng cho tuổi thọ đóng cắt, giờ chạy đèn UV, và ngưỡng ở mục 53.5.
- Số liệu chu trình DP-01 — Phụ lục J §J.1; các phép tính tuổi thọ ở Chương 9 mục 9.3 và Chương 49
  mục 49.7.

> ⚠ **Nhắc lại giới hạn.** Mục 53.3 mô tả **cách tổ chức công việc**, không phải một tiêu chuẩn cụ
> thể. Cơ sở của bạn có thể có quy định riêng — và nếu máy thuộc ngành có quản lý chặt (dược phẩm,
> thực phẩm, hàng không, y tế), ⚠ **yêu cầu về quản lý thay đổi và hồ sơ nghiêm ngặt hơn nhiều** so
> với chương này. Hỏi bộ phận chất lượng trước khi đặt ra quy trình.
