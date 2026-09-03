
# Chương 56 — Nâng cấp máy cũ *(retrofit)*

> **Lát cắt máy mẫu:** 5 — toàn bộ kiến thức của sách, áp vào một cỗ máy không phải của bạn.

---

> ⚠⚠ **ĐỌC TRƯỚC — chương này chạm vào nghĩa vụ pháp lý**
>
> Nâng cấp một cỗ máy cũ có thể làm phát sinh **nghĩa vụ pháp lý mới** với người thực hiện — trong
> một số trường hợp, bạn trở thành **nhà chế tạo** dưới góc nhìn của luật, với toàn bộ trách nhiệm
> đi kèm.
>
> ⚠ Mục 56.7 nêu vấn đề này để bạn **biết mà hỏi đúng người**. Chương này:
>
> - **không thay thế** tư vấn pháp lý — quy định khác nhau giữa các nước, các ngành và các loại máy;
> - **không thay thế** đánh giá rủi ro do **người có thẩm quyền** thực hiện (Chương 6, ISO 12100);
> - **không thay thế** việc kiểm định chức năng an toàn (Chương 48).
>
> ⚠⚠ Trước một dự án nâng cấp có chạm phần an toàn: **hỏi bộ phận pháp chế và một chuyên gia an toàn
> máy** — trước khi báo giá, không phải sau. Mọi công việc chạm mạch điện lực và mạch an toàn phải do
> **người có thẩm quyền** thực hiện hoặc kiểm tra.

---

## 56.1 Bài toán: cỗ máy không ai giải thích được

Bạn được giao nâng cấp một cỗ máy chạy mười lăm năm. Yêu cầu nghe đơn giản: **thay PLC** vì dòng cũ
đã ngừng sản xuất, không mua được phụ tùng.

Ngày đầu tiên, bạn phát hiện:

| Thực trạng | |
|---|---|
| Sơ đồ điện | Có — nhưng là bản **lúc chế tạo**, khác thực tế nhiều chỗ |
| Chương trình PLC | ⚠ Tải về được, **không có chú thích**, tên biến kiểu `%M12.3` |
| Người viết | Không còn liên lạc được |
| Người vận hành | ⭐ **Biết máy làm gì, không biết vì sao** |
| Một hộp kim loại đấu thêm ngoài tủ | ⚠⚠ **Không có trong bất kỳ tài liệu nào** |

Bạn hỏi cái hộp đó là gì. Người vận hành nói: *"Cái đó có từ lâu rồi, đừng đụng vào, đụng là máy
dừng."*

> ⭐⭐ **Đây là điều kiện làm việc bình thường của nghề, không phải trường hợp cá biệt.**
>
> Sách này đến đây đã dạy cách làm một cỗ máy đúng đắn từ đầu. Chương này về việc **phần lớn công
> việc thực tế không như vậy** — bạn nhận một cỗ máy đã có, với lịch sử mà không ai kể lại được.

---

## 56.2 ⭐ Nguyên tắc nền: hiểu trước khi đổi

Sai lầm lớn nhất trong retrofit là **bắt đầu bằng việc viết chương trình mới**.

| Cách sai | Cách đúng |
|---|---|
| Đọc yêu cầu → viết chương trình mới → thay vào | ⭐ **Khảo sát → dựng lại tài liệu → mới viết** |
| Giả định máy làm đúng như mô tả | ⭐ **Giả định máy làm điều gì đó bạn chưa biết** |
| Bỏ đi phần "không hiểu vì sao có" | ⚠⚠ **Tìm cho ra vì sao có, rồi mới quyết** |

> ⭐⭐ **Quy tắc vàng của retrofit: mọi thứ khó hiểu trong một cỗ máy đang chạy đều có lý do — bạn chỉ
> chưa biết lý do đó.**
>
> Đoạn logic kỳ quặc kia có thể là: một sửa lỗi sau tai nạn · một cách né lỗi phần cứng · một yêu cầu
> của khách hàng đã quên · hoặc đúng là rác. ⚠ **Ba khả năng đầu chiếm đa số**, và xoá nhầm một trong
> ba thì bạn tái tạo lại chính vấn đề mà nó được viết ra để giải quyết.

---

## 56.3 Khảo sát máy không có tài liệu

### ⭐ Dựng lại bảng I/O từ tủ thật

Đây là việc nền tảng — mọi thứ khác dựa vào nó (Chương 23).

| Bước | Cách làm |
|---|---|
| 1 | ⭐ **Chụp ảnh có hệ thống trước khi đụng vào bất cứ thứ gì** — xem bên dưới |
| 2 | Liệt kê module, khe cắm, địa chỉ theo thứ tự vật lý |
| 3 | ⭐ Đi từ **cầu đấu** ra thiết bị: mỗi kênh đấu tới cái gì |
| 4 | ⭐⭐ **Xác nhận từng kênh bằng cách tác động thật** — xem bên dưới |
| 5 | Ghi kiểu tín hiệu: NO/NC, PNP/NPN, dải analog (Chương 4, 31) |
| 6 | Đối chiếu với chương trình: kênh nào **không được dùng** trong chương trình? |

> ⭐⭐ **Bước 4 là bước không được bỏ.** Sơ đồ nói kênh DI 3 là "cảm biến board vào" — nhưng sơ đồ đã
> sai ở ba chỗ khác rồi. Cách duy nhất chắc chắn: **tác động cảm biến thật và xem bit nào đổi**.
>
> ⚡ Với ngõ ra thì ngược lại và ⚠ **nguy hiểm hơn nhiều**: cưỡng bức một ngõ ra làm cơ cấu chuyển
> động thật. Chỉ làm khi đã ⚠ **cô lập năng lượng cho phần không cần thử**, đã kiểm tra vùng nguy
> hiểm, và có người thứ hai (Chương 3, Chương 6).

> ⭐ **Bước 6 hay lộ ra thứ thú vị:** một kênh được đấu dây nhưng không dùng trong chương trình
> thường là **tàn tích của một chức năng đã bỏ** — hoặc của cái hộp kim loại ở mục 56.1.

### ⭐ Chụp ảnh có hệ thống

Nghe tầm thường, nhưng đây là công cụ mạnh nhất và rẻ nhất của khảo sát:

| Nguyên tắc | Vì sao |
|---|---|
| ⭐ **Chụp TRƯỚC khi tháo bất cứ thứ gì** | ⚠ Sau khi tháo thì không dựng lại được |
| Từ tổng thể tới chi tiết | Toàn cảnh tủ → từng hàng → từng cầu đấu |
| ⭐ **Có vật đánh dấu trong khung ảnh** | Nhãn cầu đấu, số hàng — để biết ảnh chụp chỗ nào |
| Chụp cả **mặt sau** và bên trong máng | Chỗ hay có dây đấu thêm |
| ⭐ Chụp **nhãn thiết bị** rõ nét | Mã hàng, phiên bản — cần khi đi tìm hàng thay thế |
| Nhiều hơn bạn nghĩ là cần | ⭐ Ảnh rẻ; ⚠ **quay lại nhà máy thì không** |

> ⭐ **Đặt tên và sắp xếp ảnh ngay trong ngày.** Ba trăm ảnh không tên, chụp cách đây hai tuần, có
> giá trị gần bằng không.

### ⚠ Dò dây an toàn

| Quy tắc | |
|---|---|
| ⚠⚠ **Cô lập năng lượng trước** | Chương 3 — điện, khí nén, và ⚠ **năng lượng tích trữ** |
| ⭐ Dò bằng thiết bị đo, không dò bằng cách kéo dây | Kéo dây làm lỏng đầu cốt ở đầu kia |
| Đánh số ngay khi xác định được | Chương 49 mục 49.6 — ⭐ **cả hai đầu** |
| ⚠ Ghi lại các "đấu tạm" phát hiện được | Chương 53 mục 53.4 |
| ⚠⚠ **Không tự ý gỡ thứ chưa hiểu** | Mục 56.2 |

---

## 56.4 Đọc chương trình PLC đời cũ

### ⭐ Đọc thế nào khi không có chú thích

| Cách | Nội dung |
|---|---|
| 1 | ⭐ **Bắt đầu từ ngõ ra, đi ngược** — chọn một cơ cấu, tìm điều kiện làm nó chạy |
| 2 | ⭐⭐ **Tìm bộ đếm bước / thanh ghi trạng thái** — đây là xương sống trình tự (Chương 21) |
| 3 | Đối chiếu với ⭐ **quan sát máy chạy thật** — xem thứ tự động tác |
| 4 | ⭐ **Hỏi người vận hành**: máy làm gì, khi nào dừng, họ phải can thiệp lúc nào |
| 5 | Ghi chú lại **ngay trong lúc đọc**, dựng dần bảng tương ứng bit ↔ ý nghĩa |
| 6 | Tách riêng: phần trình tự · phần khoá liên động · ⚠ **phần an toàn** · phần báo động |

> ⭐⭐ **Bước 4 là nguồn thông tin bị đánh giá thấp nhất.** Người vận hành biết những thứ không có
> trong tài liệu nào: máy hay kẹt ở đâu, phải làm gì khi kẹt, "cái nút này đừng bấm khi đang chạy",
> và ⭐ **các thao tác né lỗi mà họ đã quen tới mức không nghĩ là bất thường**.
>
> Hỏi họ *"anh/chị phải làm gì mà máy đáng lẽ nên tự làm?"* — câu trả lời thường là danh sách việc
> cần sửa.

### ⭐ Dựng bảng tương ứng

```text
%M12.3  →  Bit "đã có board ở trạm 1"       (suy ra từ: dùng làm điều kiện cho DO kẹp)
%M12.4  →  ? xuất hiện ở 4 nơi, chưa rõ     ← ⭐ đánh dấu và quay lại
%MW20   →  Bộ đếm bước trạm 1 (giá trị 0–7)
```

> ⭐ **Ghi cả những chỗ CHƯA HIỂU, và đánh dấu chúng.** Danh sách "chưa hiểu" co lại dần khi bạn đọc
> tiếp — và ⚠ **những mục còn lại cuối cùng chính là rủi ro của dự án**. Chúng phải được giải quyết
> trước khi thay chương trình, không phải bỏ qua.

### ⚠ Chuyển sang nền mới

| Cách | Đánh đổi |
|---|---|
| ⭐ **Dịch sát từng đoạn** | ⭐ An toàn nhất; ⚠ khiêng theo cả **sai sót cũ** và cấu trúc khó đọc |
| **Viết lại theo cấu trúc mới** | ⭐ Sạch, dễ bảo trì; ⚠⚠ **rủi ro bỏ sót hành vi cũ** cao nhất |
| ⭐⭐ **Kết hợp**: dịch sát trước, chạy được, rồi cấu trúc lại từng phần | ⭐ **Thường là lựa chọn đúng** |

> ⭐⭐ **Vì sao cách kết hợp thắng:** nó tách hai rủi ro ra làm hai bước. Bước 1 chỉ đổi nền phần cứng
> — nếu máy sai thì lỗi nằm ở việc dịch. Bước 2 chỉ đổi cấu trúc — nếu máy sai thì lỗi nằm ở việc
> viết lại, và bạn **đã có một bản chạy được để so**.
>
> Làm cả hai cùng lúc thì khi máy chạy sai, bạn không biết nhìn vào đâu.

### ⚠ Đối chiếu tập lệnh và thời gian quét

| Điểm khác | Hậu quả nếu bỏ qua |
|---|---|
| ⚠ **Thời gian quét khác** | ⭐ Logic phụ thuộc thời gian quét sẽ **chạy khác** (Chương 7) |
| Cách xử lý bộ định thời khi bị ngắt giữa chừng | Hành vi khác nhau giữa các dòng |
| ⭐ **Kiểu dữ liệu và tràn số** | Chương 14 — một phép tính chạy đúng 15 năm có thể tràn trên nền mới |
| Thứ tự quét khối / ngắt | Chương 19 |
| Vùng nhớ giữ được qua mất điện | ⭐ Chương 11 — ⚠ **bộ đếm bảo trì, số lô, tổng sản lượng** |
| Cách làm tròn số thực | Chương 14 |

> ⚠⚠ **Hàng đầu là cái bẫy đặc trưng của retrofit.** PLC mới thường quét **nhanh hơn nhiều**. Một
> đoạn logic dựa vào việc "mỗi vòng quét khoảng 20 ms" — có thể là một bộ đếm dùng làm bộ định thời
> thô sơ — sẽ chạy **nhanh gấp mấy lần** trên nền mới.
>
> ⭐ Đây là lý do bước "dịch sát" vẫn cần **kiểm thử đầy đủ**: cùng logic không có nghĩa là cùng hành
> vi.

---

## 56.5 ⭐ Rủi ro đặc thù của retrofit

### Hành vi cũ không ai mô tả được nhưng người dùng đã quen

| Ví dụ | Nếu bạn "sửa cho đúng" |
|---|---|
| Nút Reset cũng xoá luôn bộ đếm lô | ⚠ Người vận hành mất cách xoá bộ đếm mà họ vẫn dùng |
| Máy chạy tiếp sau khi mở cửa ở chế độ tay | ⚠⚠ **Đây là lỗi an toàn — phải sửa, nhưng phải báo trước** |
| Nhấn Start hai lần thì bỏ qua trạm kiểm tra | ⭐ Có thể là **tính năng không ghi chép**, có thể là lỗi — ⚠ **hỏi trước** |
| Thời gian trễ 200 ms không rõ lý do | Chương 53 mục 53.1 — ⚠ **rất có thể có lý do thật** |

> ⭐⭐ **Nguyên tắc: liệt kê mọi thay đổi hành vi, kể cả thay đổi làm máy "đúng hơn", và thoả thuận
> trước.**
>
> Một cải tiến bất ngờ vẫn là một bất ngờ. Người vận hành làm việc bằng thói quen; đổi hành vi mà
> không báo thì họ sẽ ⚠ **phát hiện ra vào lúc tệ nhất** — giữa ca sản xuất.

### ⚠ Giữ nguyên hay sửa "sai sót cũ"?

| Loại | Quyết định |
|---|---|
| ⚠⚠ **Sai sót về an toàn** | ⭐⭐ **Phải sửa** — không có lựa chọn; xem mục 56.7 |
| Sai sót gây hàng lỗi hoặc dừng máy | ⭐ Nên sửa, ⭐ **báo trước và ghi vào hồ sơ bàn giao** |
| Cách làm xấu nhưng chạy đúng | ⚡ Sửa nếu tiện; ⚠ **đừng gộp vào cùng đợt với thay nền** |
| Hành vi lạ mà chưa hiểu vì sao | ⚠⚠ **Giữ nguyên cho tới khi hiểu** (mục 56.2) |

> ⭐ **Hàng thứ ba đáng nhấn mạnh.** Cám dỗ "đằng nào cũng đang sửa, dọn luôn cho sạch" rất mạnh —
> và nó là cách biến một dự án hai tuần thành hai tháng, đồng thời làm mờ ranh giới khi đi tìm lỗi.
>
> Dọn dẹp là việc tốt, nhưng nó là **đợt sau**.

### ⚠ Rủi ro về thời gian dừng máy

Retrofit thường làm trong một cửa sổ dừng máy có hạn — nghỉ lễ, cuối tuần. Rủi ro lớn nhất không
phải viết sai, mà là **không kịp và không quay lại được**.

| Biện pháp | Nội dung |
|---|---|
| ⭐⭐ **Kế hoạch quay lui** | ⭐ **Giữ nguyên PLC cũ đấu song song, hoặc giữ đủ để đấu lại** trong vài giờ |
| ⭐ Kiểm thử trước trên bàn | Chương 50 — mô phỏng toàn bộ trình tự trước khi tới nhà máy |
| Chuẩn bị sẵn tủ mới | Đấu và kiểm tra tại xưởng, tới nơi chỉ đấu cầu đấu |
| ⭐ Danh mục kiểm tra theo thứ tự | Chương 52 — không nghĩ ra tại chỗ lúc nửa đêm |
| ⭐ **Mốc quyết định** | ⚠ "Đến giờ X mà chưa xong thì **quay lui**" — quyết trước, không quyết lúc mệt |

> ⭐⭐ **Mốc quyết định là thứ hay bị bỏ và hay gây thiệt hại nhất.** Lúc 3 giờ sáng, đã làm 14 tiếng,
> còn "một lỗi nữa là xong" — đó là lúc con người ra quyết định tệ nhất. ⭐ **Đặt mốc lúc đầu óc còn
> tỉnh**, và tôn trọng nó.

---

## 56.6 Thay PLC hết vòng đời

### ⭐ Tìm hàng thay thế

| Câu hỏi | Ghi chú |
|---|---|
| Có **bộ chuyển đổi cùng hãng** không? | ⭐ Nhiều hãng có dòng kế nhiệm kèm công cụ chuyển chương trình |
| Giữ nguyên module I/O, chỉ đổi CPU được không? | ⭐ **Rẻ nhất** nếu khung và module còn hàng |
| Đổi cả sang hãng khác? | ⚠ Đắt nhất, nhưng đôi khi là lựa chọn duy nhất |
| ⭐ Phụ tùng còn mua được **bao lâu nữa**? | ⭐ Hỏi thẳng nhà cung cấp — ⚠ **đừng lặp lại vấn đề sau 5 năm** |

> ⭐ **Công cụ chuyển tự động của hãng là điểm khởi đầu, không phải kết quả.** Nó chuyển được cú pháp;
> nó **không** kiểm tra được sự khác biệt về thời gian quét, tràn số, hay hành vi bộ định thời ở mục
> 56.4. ⚠ Phải kiểm thử đầy đủ như thể viết mới.

### ⭐ Cơ hội đi kèm

Khi đã mở tủ ra, một số việc rẻ hơn nhiều so với làm riêng sau này:

| Việc | Chương |
|---|---|
| ⭐ **Dựng lại tài liệu as-built đầy đủ** | 53 mục 53.4 — ⭐ **giá trị lớn nhất của cả dự án** |
| Thêm bộ đếm bảo trì và đo thời gian bước | 53 mục 53.5, 55 mục 55.4 |
| Cải thiện báo động — nói được **phải làm gì** | 43 |
| Đánh số lại dây, sửa tách máng | 49 |
| ⭐ Thiết lập quy trình sao lưu | 54 |
| Thêm chỗ đệm nếu đó là nút cổ chai | 55 mục 55.3 |

> ⭐⭐ **Hàng đầu tiên đáng giá hơn cả bản thân việc thay PLC.** Bạn vừa bỏ nhiều tuần để hiểu cỗ máy
> này. Nếu không ghi lại, ⚠ **người sau sẽ bỏ ra đúng ngần ấy thời gian lần nữa** — và lần đó có thể
> là chính bạn, ba năm sau.

---

## 56.7 ⚠⚠ Nâng cấp phần an toàn — nghĩa vụ phát sinh

Đây là mục quan trọng nhất chương và là lý do chương này mang cờ ⚠.

### Vấn đề

Máy cũ được chế tạo theo yêu cầu an toàn **của thời điểm đó**. Yêu cầu hiện hành thường **cao hơn**:
khái niệm mức hiệu năng, chẩn đoán lỗi, giám sát tiếp điểm, chống khởi động lại bất ngờ (Chương 47,
48).

Khi bạn chạm vào máy, câu hỏi đặt ra: **máy sau nâng cấp phải đạt mức an toàn nào — của khi nó được
chế tạo, hay của hôm nay?**

### ⭐ Điều có thể nói chắc

| Nguyên tắc | |
|---|---|
| ⭐⭐ **Thay đổi lớn có thể làm bạn thành "nhà chế tạo" trước pháp luật** | ⚠ Với toàn bộ trách nhiệm về đánh giá rủi ro, hồ sơ kỹ thuật, và tuyên bố phù hợp |
| ⭐ **Ranh giới "lớn" đến đâu là câu hỏi PHÁP LÝ**, không phải kỹ thuật | ⚠⚠ **Phải hỏi, không được đoán** |
| ⭐ **Thay đổi làm tăng rủi ro thì gần như chắc chắn phải đánh giá lại** | Tăng tốc độ, thêm chuyển động, đổi chế độ vận hành |
| ⚠⚠ **Không được làm máy kém an toàn hơn trước** | ⭐ Đây là ranh giới không cần luật sư cũng biết |
| ⭐ Phát hiện lỗi an toàn thì **phải báo bằng văn bản** | ⚠ Kể cả khi chủ máy không muốn sửa — xem bên dưới |

> ⚠⚠ **Tình huống khó nhất, và nó xảy ra thường xuyên:** bạn được thuê thay PLC, và trong lúc khảo
> sát phát hiện ⚠ **mạch dừng khẩn không đạt yêu cầu** — nó chỉ cắt tín hiệu qua PLC thường, không
> có rơ-le an toàn (Chương 47).
>
> Việc đó **nằm ngoài phạm vi hợp đồng**. Nhưng bạn đã biết.
>
> ⭐ **Việc phải làm: báo bằng văn bản, mô tả rủi ro cụ thể, đề xuất cách khắc phục, và lưu bản
> sao.** Chủ máy quyết định có sửa hay không — đó là quyền và trách nhiệm của họ. Nhưng ⚠ **im lặng
> thì trách nhiệm chuyển một phần sang bạn**, và về mặt nghề nghiệp thì im lặng là điều không chấp
> nhận được.

### ⭐ Việc nên làm ngay từ đầu dự án

| Bước | Khi nào |
|---|---|
| ⭐ **Đánh giá rủi ro cho máy SAU nâng cấp** | ⭐ **Trước khi báo giá** — Chương 6 |
| ⚠ Hỏi pháp chế về ranh giới "thay đổi lớn" | Trước khi ký |
| ⭐ Ghi rõ trong hợp đồng: ai chịu trách nhiệm phần an toàn | ⚠ **Mập mờ ở đây là rủi ro lớn nhất của dự án** |
| Lập hồ sơ những gì đã kiểm tra và đã báo | Suốt dự án |
| ⭐ Nghiệm thu phần an toàn riêng | Chương 48, 52 |

> ⭐⭐ **Đưa việc đánh giá rủi ro vào TRƯỚC khi báo giá là lời khuyên thực dụng nhất của mục này.**
>
> Nếu nâng cấp an toàn là bắt buộc, nó phải nằm trong giá. Phát hiện sau khi đã ký giá thấp thì bạn
> ở vào thế phải chọn giữa **lỗ** và **làm ngơ** — và đó là một vị trí không ai nên tự đặt mình vào.

> ⚠⚠ **Nhắc lại: mục này nêu vấn đề để bạn biết mà hỏi. Nó không phải tư vấn pháp lý, và các quy
> định cụ thể khác nhau giữa các nước, các ngành, và các loại máy.**

---

## 56.8 Liên hệ với máy mẫu DP-01

DP-01 là máy làm mới, nên chương này áp vào nó theo hướng ngược lại: ⭐ **cỗ máy bạn làm hôm nay là
cỗ máy ai đó sẽ retrofit trong mười năm nữa.**

| Việc làm hôm nay | Cứu ai đó năm 2036 |
|---|---|
| ⭐ Chú thích giải thích **vì sao** | Chương 24 — thứ duy nhất không lạc bản (Ch.53 mục 53.4) |
| ⭐⭐ **Tài liệu as-built cập nhật** | Chương 53 — ⭐ **giá trị lớn nhất** |
| Bảng I/O khớp số dây và tên tag | Chương 23, 49 mục 49.6 |
| ⭐ Quy trình sao lưu bảy hạng mục | Chương 54 |
| Nhật ký thay đổi có ghi **lý do** | Chương 53 mục 53.3 |
| Trình tự có cấu trúc rõ, bộ đếm bước tường minh | Chương 21 — ⭐ **người sau đọc được** |
| ⭐ Không để "đấu tạm" không nhãn | Chương 53 mục 53.4 |
| Hồ sơ an toàn đầy đủ, có mã kiểm tra | Chương 48, 54 |

> ⭐⭐ **Đây là chỗ toàn bộ sách khép lại thành một vòng.**
>
> Mọi việc "phiền phức" mà các chương trước đòi hỏi — chú thích, tài liệu, nhật ký, sao lưu, đánh số
> — đều có cùng một người thụ hưởng: ⭐ **người mở tủ ra sau bạn**, với một cỗ máy đang chạy và không
> ai giải thích được.
>
> Chương này cho thấy chi phí của việc không làm những thứ đó. Nó không rơi vào bạn — nó rơi vào
> người sau. Và **rất thường xuyên, người sau chính là bạn**.

---

## 56.9 Bẫy thường gặp

### 🔍 BẪY 1 — Viết chương trình mới trước khi hiểu máy cũ

**Hiện tượng:** ⚠ máy chạy "gần đúng", và những chỗ sai là những chỗ không ai mô tả được.
**Cách sửa:** ⭐ khảo sát → dựng tài liệu → mới viết (mục 56.2).

### 🔍 BẪY 2 — Xoá đoạn logic "không hiểu vì sao có"

**Hiện tượng:** ⚠⚠ tái tạo lại chính vấn đề mà đoạn đó được viết ra để sửa — có thể là một **tai
nạn**.
**Cách sửa:** ⭐ mọi thứ khó hiểu đều có lý do; ⚠ **giữ nguyên cho tới khi hiểu** (mục 56.2, 56.5).

### 🔍 BẪY 3 — Tin sơ đồ thay vì tin tủ thật

**Hiện tượng:** bảng I/O sai vài chỗ, và những chỗ đó lộ ra lúc chạy thử.
**Cách sửa:** ⭐⭐ **xác nhận từng kênh bằng cách tác động thật** (mục 56.3).

### 🔍 BẪY 4 — Chụp ảnh sau khi đã tháo

**Hiện tượng:** ⚠ không dựng lại được trạng thái ban đầu.
**Cách sửa:** ⭐ chụp **trước**, có hệ thống, đặt tên ngay trong ngày (mục 56.3).

### 🔍 BẪY 5 — Không hỏi người vận hành

**Hiện tượng:** ⭐ bỏ lỡ nguồn thông tin **duy nhất** về hành vi thực tế của máy.
**Cách sửa:** hỏi *"anh/chị phải làm gì mà máy đáng lẽ nên tự làm?"* (mục 56.4).

### 🔍 BẪY 6 — Dịch sát và viết lại cùng một lúc

**Hiện tượng:** máy chạy sai, ⚠ **không biết lỗi ở việc dịch hay việc viết lại**.
**Cách sửa:** ⭐⭐ hai bước tách biệt — dịch sát, chạy được, rồi mới cấu trúc lại (mục 56.4).

### 🔍 BẪY 7 — Bỏ qua khác biệt thời gian quét

**Hiện tượng:** ⚠⚠ logic dựa vào vòng quét chạy **nhanh gấp mấy lần** trên PLC mới.
**Cách sửa:** đối chiếu tập lệnh và thời gian quét; ⭐ **kiểm thử như thể viết mới** (mục 56.4).

### 🔍 BẪY 8 — Đổi hành vi mà không báo trước

**Hiện tượng:** ⚠ người vận hành phát hiện thay đổi **giữa ca sản xuất**.
**Cách sửa:** ⭐ liệt kê **mọi** thay đổi hành vi, kể cả cải tiến, và thoả thuận trước (mục 56.5).

### 🔍 BẪY 9 — Gộp dọn dẹp vào cùng đợt thay nền

**Hiện tượng:** dự án hai tuần thành hai tháng; ⚠ ranh giới tìm lỗi bị mờ.
**Cách sửa:** dọn dẹp là **đợt sau** (mục 56.5).

### 🔍 BẪY 10 — Không có kế hoạch quay lui

**Hiện tượng:** ⚠⚠ hết cửa sổ dừng máy, máy mới chưa chạy, máy cũ **đã tháo**.
**Cách sửa:** ⭐ giữ đủ để đấu lại trong vài giờ; ⭐⭐ **đặt mốc quyết định trước, lúc còn tỉnh táo**
(mục 56.5).

### 🔍 BẪY 11 — Lặp lại vấn đề vòng đời

**Hiện tượng:** ⚠ chọn dòng thiết bị sắp ngừng sản xuất → làm lại sau 5 năm.
**Cách sửa:** hỏi thẳng nhà cung cấp về vòng đời và phụ tùng (mục 56.6).

### 🔍 BẪY 12 — Không dựng lại tài liệu sau khi đã hiểu máy

**Hiện tượng:** ⭐⭐ người sau bỏ ra **đúng ngần ấy thời gian lần nữa** — có thể chính là bạn.
**Cách sửa:** as-built là ⭐ **sản phẩm bàn giao của dự án**, không phải việc phụ (mục 56.6).

### 🔍 BẪY 13 — Báo giá trước khi đánh giá rủi ro an toàn

**Hiện tượng:** ⚠⚠ phát hiện phải nâng cấp an toàn **sau khi đã ký giá thấp** → kẹt giữa lỗ và làm
ngơ.
**Cách sửa:** ⭐ đánh giá rủi ro **trước khi báo giá**; ghi rõ trách nhiệm an toàn trong hợp đồng
(mục 56.7).

### 🔍 BẪY 14 — Im lặng về lỗi an toàn ngoài phạm vi hợp đồng

**Hiện tượng:** ⚠⚠ bạn đã biết, và **trách nhiệm chuyển một phần sang bạn**.
**Cách sửa:** ⭐ báo **bằng văn bản**, mô tả rủi ro, đề xuất khắc phục, **lưu bản sao** (mục 56.7).

---

## 56.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| ⭐⭐ Quy tắc vàng của retrofit | **Mọi thứ khó hiểu trong máy đang chạy đều có lý do — bạn chỉ chưa biết** |
| Thứ tự đúng | ⭐ **Khảo sát → dựng tài liệu → mới viết**, không ngược lại |
| ⭐⭐ Xác nhận I/O thế nào | **Tác động thật và xem bit nào đổi** — không tin sơ đồ |
| ⚠ Với ngõ ra | Chỉ thử khi đã **cô lập năng lượng** và có người thứ hai |
| Chụp ảnh | ⭐ **Trước khi tháo**, có hệ thống, đặt tên ngay trong ngày |
| Đọc chương trình không chú thích | ⭐ Đi ngược từ ngõ ra · ⭐⭐ **tìm bộ đếm bước** · quan sát máy chạy · **hỏi người vận hành** |
| ⭐ Câu hỏi hay nhất cho người vận hành | *"Anh/chị phải làm gì mà máy đáng lẽ nên tự làm?"* |
| Danh sách "chưa hiểu" | ⚠ **Chính là rủi ro của dự án** — phải giải quyết, không bỏ qua |
| ⭐⭐ Cách chuyển nền | **Dịch sát trước, chạy được, rồi cấu trúc lại** — hai bước tách biệt |
| ⚠⚠ Bẫy kỹ thuật đặc trưng | **Thời gian quét khác** — logic dựa vào vòng quét chạy nhanh gấp mấy lần |
| Hành vi cũ người dùng đã quen | ⭐ Liệt kê **mọi** thay đổi hành vi và **thoả thuận trước** |
| Sai sót cũ — sửa hay giữ | ⚠⚠ An toàn: **phải sửa** · gây lỗi: nên sửa + báo · xấu mà đúng: đợt sau · chưa hiểu: **giữ** |
| ⭐⭐ Chống rủi ro dừng máy | **Kế hoạch quay lui** + ⭐ **mốc quyết định đặt trước** |
| Cơ hội đi kèm giá trị nhất | ⭐⭐ **Dựng lại tài liệu as-built** |
| ⚠⚠ Nghĩa vụ pháp lý | Thay đổi lớn có thể làm bạn thành **nhà chế tạo** trước pháp luật |
| Ranh giới "lớn" là câu hỏi gì | ⚠ **Pháp lý — phải hỏi, không được đoán** |
| Ranh giới chắc chắn | ⚠⚠ **Không được làm máy kém an toàn hơn trước** |
| Phát hiện lỗi an toàn ngoài hợp đồng | ⭐ **Báo bằng văn bản, lưu bản sao** — chủ máy quyết định |
| Đánh giá rủi ro làm khi nào | ⭐⭐ **Trước khi báo giá** |

---

## 56.11 Tự kiểm

1. ⭐⭐ Phát biểu quy tắc vàng của retrofit. Nêu ba lý do thật có thể đứng sau một đoạn logic khó
   hiểu.
2. Vì sao "viết chương trình mới rồi thay vào" là sai lầm lớn nhất?
3. ⭐⭐ Vì sao không được tin sơ đồ khi dựng lại bảng I/O? Xác nhận một kênh DI thế nào? Một kênh DO
   thế nào, và ⚠ **cần điều kiện an toàn gì**?
4. Nêu sáu nguyên tắc chụp ảnh khảo sát. Nguyên tắc nào không thể sửa nếu làm sai?
5. ⭐ Kể sáu bước đọc một chương trình PLC không có chú thích. Bước nào cho thông tin không có trong
   tài liệu nào?
6. ⭐ Vì sao phải ghi lại cả những chỗ **chưa hiểu**? Danh sách đó nghĩa là gì với dự án?
7. ⭐⭐ Nêu ba cách chuyển sang nền mới và đánh đổi. Vì sao cách kết hợp thường thắng?
8. ⚠⚠ Nêu sáu điểm khác biệt phải đối chiếu khi đổi nền PLC. Điểm nào là bẫy đặc trưng, và nó gây ra
   gì?
9. ⭐ Vì sao phải liệt kê cả những thay đổi hành vi làm máy "đúng hơn"?
10. ⚠ Bốn loại "sai sót cũ" được xử lý thế nào? Loại nào không có lựa chọn?
11. ⭐⭐ Vì sao **mốc quyết định quay lui** phải đặt trước, và vì sao nó hay bị bỏ?
12. Nêu sáu cơ hội đi kèm khi đã mở tủ. Cơ hội nào giá trị nhất, và vì sao?
13. ⚠⚠ Trong tình huống ở mục 56.7 — phát hiện mạch dừng khẩn không đạt, nằm ngoài hợp đồng — bạn
    làm gì? Vì sao im lặng không phải lựa chọn?
14. ⭐ Vì sao đánh giá rủi ro phải làm **trước khi báo giá**?
15. ⭐⭐ Liệt kê tám việc làm hôm nay trên DP-01 sẽ giúp người retrofit nó năm 2036. Ai thật sự là
    người thụ hưởng của chúng?

> Câu 3, 7, 11 và 13 là bốn câu phân loại. Câu 15 là câu khép vòng: ⭐⭐ **chi phí của việc không ghi
> chép không rơi vào người bỏ qua nó — nó rơi vào người đến sau, và rất thường xuyên, người đến sau
> chính là bạn.**

---

### Chương tiếp theo

Chương 57 — **Case study DP-01 hoàn chỉnh**. Cả cỗ máy, từ đầu tới cuối, ráp lại thành một mạch duy
nhất: từ khảo sát yêu cầu tới nghiệm thu và bàn giao.

### Nguồn tham khảo chương 56

- ISO 12100 — *Safety of machinery — General principles for design, risk assessment and risk
  reduction*: nền cho việc đánh giá rủi ro máy **sau nâng cấp** ở mục 56.7. *(tiêu chuẩn có bản
  quyền)*
- ISO 13849-1 và IEC 62061 — mức hiệu năng và mức toàn vẹn của chức năng an toàn: cơ sở để so máy cũ
  với yêu cầu hiện hành (Chương 47, 48).
- IEC 60204-1 — yêu cầu với trang bị điện của máy, gồm tài liệu kỹ thuật.
- **Quy định pháp luật tại thị trường của bạn** về máy đã qua sử dụng và máy được sửa đổi — ⚠⚠ **đây
  là nguồn quyết định cho mục 56.7**, và nó khác nhau giữa các nước.
- **Tài liệu vòng đời sản phẩm của nhà sản xuất PLC** — dùng cho mục 56.6: dòng kế nhiệm, công cụ
  chuyển đổi, thời hạn cung cấp phụ tùng.

> ⚠⚠ **Nhắc lại giới hạn — đây là chương mang cờ ⚠.**
>
> Mục 56.7 nêu **vấn đề** về nghĩa vụ pháp lý khi nâng cấp máy; nó **không trả lời** vấn đề đó, vì
> câu trả lời phụ thuộc pháp luật từng nước, loại máy, và mức độ thay đổi.
>
> ⚠ Trước một dự án retrofit có chạm phần an toàn: hỏi **bộ phận pháp chế** về ranh giới trách
> nhiệm, và **một chuyên gia an toàn máy** về mức an toàn phải đạt. Làm việc đó **trước khi báo
> giá**. Chương này chỉ giúp bạn biết **cần hỏi điều gì** — và biết rằng câu hỏi đó tồn tại.
