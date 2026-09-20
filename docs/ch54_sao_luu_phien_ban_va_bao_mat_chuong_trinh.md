
# Chương 54 — Sao lưu, phiên bản & bảo mật chương trình

> **Lát cắt máy mẫu:** 5 — máy đầy đủ, đã bàn giao và đang sản xuất.

---

## 54.1 ⚠⚠ Bài toán: chiếc máy không ai dựng lại được

Một cỗ máy chạy tám năm. Người viết chương trình đã nghỉ việc từ lâu. Công ty làm máy đã đóng cửa.

CPU chết.

Người ta mua CPU mới, cùng đời. Rồi đi tìm chương trình:

| Nơi tìm | Kết quả |
|---|---|
| Máy tính của kỹ sư cũ | ⚠ Đã thanh lý |
| Đĩa CD bàn giao | Tìm thấy — nhưng là bản **lúc bàn giao**, tám năm trước |
| CPU cũ | ⚠⚠ **Đã chết — không đọc ra được** |

Bản trên đĩa CD không có tám năm sửa đổi: các chỉnh sửa sau khi chạy thật, các công thức mới, các
sửa lỗi. Máy nạp bản cũ vào thì chạy sai.

Họ mất **sáu tuần** dựng lại, bằng cách đọc dây trong tủ và hỏi người vận hành xem máy "vốn làm gì".

> ⭐⭐ **Điểm mấu chốt: sao lưu duy nhất còn dùng được nằm trong CPU — và CPU chính là thứ vừa hỏng.**
>
> Đây không phải chuyện hiếm. Nó là **cách thất bại mặc định** của mọi cỗ máy không có quy trình sao
> lưu: bản sao lưu tồn tại, nhưng nó cũ, và không ai biết nó cũ cho tới lúc cần.

---

## 54.2 ⭐ Vì sao "tải từ PLC về" không cứu được bạn

Nhiều người yên tâm vì "lúc nào cần thì tải từ PLC về là có". Điều đó đúng **một phần**, và phần sai
của nó rất đắt.

| Vấn đề | Giải thích |
|---|---|
| ⚠⚠ **CPU hỏng thì không tải được** | Đúng lúc cần nhất thì không có |
| ⭐ **Mất chú thích và tên biến** | Nhiều dòng PLC **không lưu comment trong CPU** — tải về được logic trần, không đọc nổi |
| **Mất cấu trúc dự án** | Tên khối, chú thích khối, tổ chức thư mục |
| ⚠ **Không có phần ngoài CPU** | Cấu hình biến tần, dự án HMI, tham số thiết bị mạng — xem mục 54.3 |
| **Có thể cần mật khẩu** | Mà không ai còn giữ (mục 54.6) |

> ⭐⭐ **Kiểm tra ngay hôm nay với máy bạn đang phụ trách: tải chương trình từ CPU về một thư mục
> trống, mở ra, và xem có còn chú thích và tên biến không.**
>
> Câu trả lời quyết định liệu "tải từ PLC về" là một phương án khôi phục hay chỉ là **ảo tưởng**.
> Với nhiều dòng PLC, kết quả là hàng nghìn dòng logic với tên biến kiểu `%MW120` và **không một dòng
> chú thích**.

---

## 54.3 ⭐⭐ Sao lưu cái gì — tám thứ, không phải một

Đây là mục quan trọng nhất chương. Hầu hết người ta sao lưu **một** thứ và tưởng là đã xong.

| # | Hạng mục | ⚠ Bỏ quên thì hậu quả |
|---|---|---|
| 1 | ⭐ **Dự án PLC** (logic + chú thích + tên biến) | Có logic nhưng không đọc được |
| 2 | ⭐ **Cấu hình phần cứng** *(hardware configuration)* — khe cắm, module, địa chỉ, tham số module; ⭐ biểu mẫu **Phụ lục C.10** | CPU mới không nhận I/O |
| 3 | ⭐ **Tham số biến tần / servo driver** — ⚠⚠ **kể cả tham số CHỨC NĂNG AN TOÀN của drive** | ⚠ **Động cơ chạy sai hoặc không chạy**; chỉnh lại tay mất hàng ngày (Chương 36–37). ⚠⚠ Và nếu thiếu tham số an toàn: máy **chạy bình thường** nhưng chức năng an toàn **không còn như đã nghiệm thu**, ⭐ **không báo động nào nói điều đó** (Chương 37 mục 37.6b) |
| 4 | ⭐ **Dự án HMI / SCADA** | Có máy chạy nhưng ⚠ **không ai điều khiển được** (Chương 44) |
| 5 | **Công thức và tham số sản phẩm** | Mất toàn bộ dữ liệu sản phẩm (Chương 32) |
| 6 | ⚠⚠ **Chương trình và cấu hình thiết bị an toàn** | Không khôi phục được chức năng an toàn; ⚠ **và phải kiểm định lại** (Chương 48) |
| 7 | **Cấu hình mạng** — địa chỉ IP, tên trạm, tệp mô tả thiết bị | Thiết bị không nhận nhau (Chương 40) |
| 8 | ⭐⭐ **Chương trình và ĐIỂM DẠY của bộ điều khiển ngoài** — robot, tay gắp thông minh | ⚠⚠ **Điểm dạy là dữ liệu nhưng có vai trò như code**: mất nó thì phải dạy lại từng điểm trên máy thật, và ⚠ không có cách nào kiểm rằng đã dạy đúng như cũ (Chương 46 mục 46.5) |

> ⭐ **Mục 3 là mục bị quên nhiều nhất, và nó gây bất ngờ khó chịu nhất.**
>
> Người ta nhớ chương trình PLC vì nó "là phần mềm". Nhưng một biến tần có hàng trăm tham số đã được
> chỉnh cho đúng cỗ máy này — thời gian tăng tốc, giới hạn dòng, cấu hình phản hồi, thông số động cơ.
> Thay biến tần mới mà không có bản sao tham số thì bạn đang **chỉnh lại từ đầu trên một máy đang cần
> chạy**.
>
> ⚡ Nhiều biến tần cho phép **sao chép tham số vào bảng điều khiển rời** rồi nạp sang bộ khác — dùng
> nó, và **kèm cả tệp sao lưu tham số** vào bộ sao lưu chung.

> ⭐⭐ **Mục 8 hay bị bỏ vì nó "không thuộc PLC".**
>
> Robot có bộ nhớ riêng, phần mềm riêng, người lập trình riêng — nên rất dễ mặc định rằng *"bên robot
> họ tự lo"*. ⚠ Nhưng khi máy hỏng lúc nửa đêm, người đứng đó là bạn. ⭐ **Bộ sao lưu của cỗ máy phải
> là bộ sao lưu của CẢ CỖ MÁY**, không phải của riêng phần mình làm (Chương 46).

### ⭐ Mục 6 là hạng mục đặc biệt

Chương trình an toàn không chỉ cần khôi phục — nó cần **khôi phục đúng bản đã được kiểm định**.

| Yêu cầu | Vì sao |
|---|---|
| ⭐ Sao lưu kèm **mã kiểm tra** *(checksum)* của bản đã nghiệm thu | Để chứng minh bản khôi phục đúng là bản đã duyệt |
| ⭐ Lưu kèm **hồ sơ kiểm định** | Chương 48 |
| ⚠ Sau khôi phục, **kiểm tra lại chức năng an toàn** | Ngay cả khi mã kiểm tra khớp |

---

## 54.4 Sao lưu khi nào, cất ở đâu

### ⭐ Khi nào

| Thời điểm | Bắt buộc? |
|---|---|
| ⭐ **Trước mọi thay đổi** | ⭐⭐ **Bắt buộc** — Chương 53 mục 53.2 |
| Sau khi thay đổi đã chạy ổn định vài ngày | Bắt buộc |
| Sau nghiệm thu, trước khi rời nhà máy | Bắt buộc |
| Định kỳ (tháng/quý) kể cả khi không sửa gì | ⭐ Nên — nó **phát hiện những thay đổi không ai ghi** |
| Trước khi bảo trì lớn | Nên |

> ⭐ **Sao lưu định kỳ có một tác dụng phụ quý hơn cả mục đích chính:** nếu bản sao lưu tháng này khác
> bản tháng trước mà **không có ghi chép nào**, thì ai đó đã sửa mà không ghi. Bạn phát hiện ra sau
> một tháng, không phải sau ba năm.
>
> Đây là cách kiểm tra chéo cho quy trình ở Chương 53 — và nó tự động.

### ⭐ Cất ở đâu — quy tắc ba bản

| Bản | Nơi | Vì sao |
|---|---|---|
| 1 | ⭐ **Ngay tại máy** — thẻ nhớ trong tủ, hoặc máy tính công nghiệp tại chỗ | Lấy được lúc 2 giờ sáng, ⚡ **không cần mạng** |
| 2 | Máy chủ / kho lưu trữ của nhà máy | Có sao lưu tự động, có phân quyền |
| 3 | ⭐ **Ngoài nhà máy** *(off-site)* | ⚠ Cháy, ngập, mã độc tống tiền *(ransomware)* — thứ xoá sạch cả bản 1 và 2 |

> ⚠ **Bản 3 tồn tại vì mã độc tống tiền là mối đe doạ có thật với nhà máy.** Một bản sao lưu nằm trên
> ổ đĩa mạng luôn kết nối sẽ **bị mã hoá cùng lúc với mọi thứ khác**. Bản ngoài nhà máy — hoặc một bản
> **ngắt kết nối vật lý** — là thứ còn lại.
>
> Xem thêm Chương 45 về an ninh mạng công nghiệp.

### ⚡ Bản "ngay tại máy" đáng giá hơn nó có vẻ

Người sửa máy lúc 2 giờ sáng thường **không có** quyền truy cập máy chủ, không có mật khẩu VPN, và
không có ai để gọi. Một thẻ nhớ dán trong tủ điện, ghi rõ ngày và phiên bản, đôi khi là thứ duy nhất
đứng giữa "sửa xong trong một giờ" và "chờ tới sáng mai".

---

## 54.5 ⭐⭐ Bản sao lưu chưa thử khôi phục không phải bản sao lưu

Đây là câu quan trọng nhất chương, và nó không phải cách nói cho kêu.

### Vì sao bản sao lưu thất bại

| Nguyên nhân | Bạn chỉ biết khi thử |
|---|---|
| ⚠ **Tệp hỏng** | Sao chép lỗi, thẻ nhớ xuống cấp |
| ⚠ **Thiếu hạng mục** | Có dự án PLC, ⭐ **thiếu cấu hình phần cứng** — không nạp được |
| **Sai phiên bản phần mềm** | Bản sao tạo bằng phần mềm đời cũ, máy tính hiện tại không mở được |
| ⚠⚠ **Thiếu giấy phép phần mềm** | ⭐ Có tệp, **không mở được** — mục 54.7 |
| **Thiếu mật khẩu** | Mục 54.6 |
| **Không biết quy trình khôi phục** | Có đủ mọi thứ, ⚠ **không ai biết làm theo thứ tự nào** |

### ⭐ Thử khôi phục *(restore)* thế nào

| Cách | Khi nào |
|---|---|
| ⭐ **Nạp vào CPU dự phòng trên bàn** | Cách tốt nhất — không chạm máy đang chạy |
| Nạp vào máy trong lần dừng máy theo kế hoạch | Tốn thời gian dừng, nhưng thật nhất |
| ⚡ **Ít nhất: mở tệp ra trên máy tính** | Kém nhất, nhưng bắt được lỗi tệp hỏng, sai phiên bản, thiếu giấy phép |

> ⭐⭐ **Ngay cả cách thấp nhất — mở tệp ra xem — cũng bắt được ba trong sáu nguyên nhân thất bại.**
> Nó mất mười phút mỗi quý. Hãy làm ít nhất điều đó.

### ⭐ Ghi lại quy trình khôi phục

Bản sao lưu tốt nhất vẫn vô dụng nếu người cầm nó không biết dùng. Viết một trang, cất **cùng chỗ với
bản sao lưu**:

| Nội dung | Ví dụ |
|---|---|
| Thứ tự khôi phục | Cấu hình phần cứng → chương trình → tham số driver → HMI |
| Phần mềm và **phiên bản** cần có | Kèm nơi lấy giấy phép |
| Mật khẩu lấy ở đâu | ⚠ Không phải chính mật khẩu — mà **nơi giữ nó** |
| Việc phải làm sau khi khôi phục | ⭐ Về gốc các trục, ⚠ **kiểm tra chức năng an toàn**, đối chiếu công thức |
| Ai gọi khi bí | Tên, số điện thoại |

---

## 54.6 ⚠ Khoá chương trình bằng mật khẩu

Đây là chỗ có xung đột lợi ích thật sự, và sách này nêu cả hai phía.

### Hai phía

| Phía nhà chế tạo máy | Phía người dùng máy |
|---|---|
| Bảo vệ chất xám đã bỏ ra | ⭐ **Máy là tài sản của họ** |
| Tránh khách sửa sai rồi đổ lỗi | ⚠⚠ **Không sửa được máy của chính mình lúc 2 giờ sáng** |
| Giữ hợp đồng bảo trì | ⚠ Phụ thuộc hoàn toàn vào một nhà cung cấp |
| Tránh đối thủ sao chép | ⚠ Nhà cung cấp phá sản → máy thành **hộp đen không sửa được** |

> ⚠⚠ **Trường hợp xấu nhất là có thật:** nhà chế tạo đóng cửa, chương trình bị khoá, không ai mở
> được. Cỗ máy vẫn chạy — cho tới lần hỏng đầu tiên cần sửa chương trình. Sau đó nó là **sắt vụn có
> giá trị của một cỗ máy**.
>
> Đây chính là kết cục mà cỗ máy ở mục 54.1 suýt gặp.

### ⭐ Cách dung hoà hay dùng

| Cách | Nội dung |
|---|---|
| ⭐ **Khoá một phần** | Khoá khối chứa bí quyết công nghệ; ⭐ **để mở phần trình tự và I/O** để khách chẩn đoán được |
| ⭐ **Ký gửi mã nguồn** *(source code escrow)* | Bên thứ ba giữ mã và mật khẩu, giao cho khách nếu nhà chế tạo ngừng hoạt động |
| **Giao mật khẩu, ràng buộc bằng hợp đồng** | Bảo vệ bằng pháp lý thay vì bằng kỹ thuật |
| **Phân quyền theo cấp** | Xem được nhưng không sửa được; sửa được tham số nhưng không sửa được logic |

> ⭐⭐ **Điều phải rõ trong hợp đồng, ký trước khi làm máy:**
>
> | Câu hỏi | Vì sao |
> |---|---|
> | Khách có được **nhận mã nguồn** không? | Tranh cãi sau khi máy đã chạy thì không giải quyết được |
> | Nếu có, ở **định dạng nào**? | Bản in PDF **không phải** mã nguồn — không nạp lại được |
> | Có **mật khẩu** không, ai giữ? | |
> | Ai chịu chi phí nếu **mất chương trình**? | ⭐ Câu hỏi này làm mọi người nghiêm túc rất nhanh |
> | Khách sửa thì bảo hành có mất không? | Nên rõ ràng thay vì mập mờ |

### ⚠ Nếu bạn là người đặt mật khẩu

| Quy tắc | Nội dung |
|---|---|
| ⚠⚠ **Ghi lại ở nơi tổ chức truy cập được** | Không phải chỉ trong đầu bạn hoặc trong máy tính cá nhân |
| ⭐ **Nhiều hơn một người biết** | Người duy nhất biết mật khẩu nghỉ việc là một sự cố chờ xảy ra |
| Kèm mật khẩu vào **quy trình khôi phục** | Đúng hơn: kèm **nơi lấy** mật khẩu (mục 54.5) |
| ⚡ Xem lại khi có người rời tổ chức | Cùng lý do với mọi hệ thống khác (Chương 45) |

---

## 54.7 Quản lý phiên bản *(version control)*

### ⭐ Quy ước đặt tên tối thiểu

```text
DP01_PLC_v2.4_2026-08-15_them-tre-200ms-tram1.zip
└────┬───┘ └┬┘ └─┬┘ └────┬───┘ └──────────┬──────┘
   máy    phần  bản    ngày            lý do
```

| Thành phần | Vì sao cần |
|---|---|
| ⭐ **Tên máy** | Kho sao lưu chứa nhiều máy; nhầm máy là tai nạn |
| **Phần nào** | PLC · HMI · biến tần · an toàn (bảy hạng mục ở mục 54.3) |
| **Số phiên bản** | Thứ tự rõ ràng |
| ⭐ **Ngày** | ⭐ **Sắp xếp được, và trả lời "bản này có mới hơn không"** |
| ⭐⭐ **Lý do** | Biến tên tệp thành **nhật ký thay đổi** — Chương 53 mục 53.4 |

> ⭐⭐ **Trường "lý do" là thứ biến một thư mục sao lưu thành tài liệu.**
>
> Nhìn danh sách tệp, bạn đọc được lịch sử của cỗ máy mà không phải mở tệp nào. Và khi cần lùi về,
> bạn biết **lùi về đâu** — chứ không phải thử từng bản.

### ⭐ Đánh số phiên bản

| Kiểu thay đổi | Tăng số nào | Ví dụ |
|---|---|---|
| Sửa lỗi nhỏ, chỉnh tham số | Số sau | 2.3 → 2.4 |
| Thêm chức năng, đổi trình tự | Số trước | 2.4 → 3.0 |
| ⚠ **Chạm mạch an toàn** | ⭐ Số trước + **ghi rõ trong tên**, và ⚠ kiểm định lại (Ch.48) | 3.0 → 4.0_AN-TOAN |

> ⭐ **Số phiên bản phải xuất hiện ở ba nơi và khớp nhau:**
>
> | Nơi | Vì sao |
> |---|---|
> | Tên tệp sao lưu | Tìm được |
> | ⭐ **Một biến trong chương trình PLC** | ⭐⭐ **Đọc được từ máy đang chạy** |
> | ⭐ **Hiển thị trên HMI** | ⭐ Người vận hành đọc cho bạn **qua điện thoại** |
>
> Hàng thứ ba đáng giá bất ngờ: khi hỗ trợ từ xa, câu hỏi đầu tiên luôn là "máy đang chạy bản nào?" —
> và nếu người vận hành đọc được nó trên màn hình, bạn tiết kiệm nửa giờ.

### ⚡ Có nên dùng công cụ quản lý phiên bản như bên phần mềm?

| Tình huống | Nhận xét |
|---|---|
| Dự án PLC lưu dạng **tệp văn bản** (một số hệ thống, hoặc xuất ra được) | ⭐ **Rất đáng** — so sánh được hai bản, thấy đúng dòng nào đổi |
| Dự án lưu dạng **tệp nhị phân đóng gói** | ⚡ Vẫn dùng được để lưu lịch sử, nhưng **không so sánh được nội dung** |
| Đội một người, máy ít | Quy ước đặt tên ở trên là đủ |

> ⭐ **Điều cần nhất không phải công cụ, mà là kỷ luật: mỗi bản có ngày, có lý do, và có một chỗ duy
> nhất được coi là chính thức.**

---

## 54.8 Trên máy mẫu DP-01

| Hạng mục sao lưu | Nội dung |
|---|---|
| 1 — Dự án PLC | Kèm chú thích và tên biến |
| 2 — Cấu hình phần cứng | Khe cắm, module, ⭐ tham số module analog (Chương 31) |
| 3 — ⭐ **Tham số biến tần chuyền** | ⚠ Kèm cả **bản sao trong bảng điều khiển rời** (Chương 36) |
| 3b — Tham số servo trục Z | Chương 37 |
| 4 — Dự án HMI | Chương 44 |
| 5 — Công thức sản phẩm | Đường chạy keo, thời gian sấy UV theo loại board (Chương 32) |
| 6 — ⚠⚠ **Cấu hình rơ-le an toàn + mã kiểm tra** | Kèm hồ sơ kiểm định (Chương 48) |
| 7 — Cấu hình mạng | Địa chỉ scanner, bộ điều khiển nhiệt RS-485, biến tần (Chương 38, 40) |

| Quy tắc | Quyết định |
|---|---|
| Ba bản | ⭐ Thẻ nhớ trong tủ · máy chủ nhà máy · **bản ngoài nhà máy** |
| Sao lưu định kỳ | Hàng quý, kể cả khi không sửa gì |
| ⭐ Thử khôi phục | ⭐ **Mỗi quý mở tệp kiểm tra**; mỗi năm nạp thử vào CPU dự phòng |
| Phiên bản hiển thị | ⭐ Biến trong PLC **và** góc màn hình HMI |
| Quy trình khôi phục | Một trang, ⭐ **cất cùng thẻ nhớ trong tủ** |
| Mật khẩu | Ghi ở nơi tổ chức truy cập được; ⭐ **ít nhất hai người biết** |

---

## 54.9 Bẫy thường gặp

### 🔍 BẪY 1 — Tin rằng "tải từ PLC về là có"

**Hiện tượng:** ⚠⚠ CPU hỏng thì không tải được; và nếu tải được thì ⭐ **mất chú thích và tên biến**.
**Cách sửa:** ⭐ thử ngay hôm nay — tải về và xem còn chú thích không (mục 54.2).

### 🔍 BẪY 2 — Chỉ sao lưu chương trình PLC

**Hiện tượng:** khôi phục xong, ⚠ **động cơ chạy sai** vì thiếu tham số biến tần; hoặc máy chạy mà
không ai điều khiển được vì thiếu dự án HMI.
**Cách sửa:** bảy hạng mục ở mục 54.3, không phải một.

### 🔍 BẪY 3 — Bản sao lưu chưa bao giờ thử khôi phục

**Hiện tượng:** ⭐⭐ đến lúc cần mới biết tệp hỏng, thiếu hạng mục, sai phiên bản phần mềm, hoặc
**không có giấy phép để mở**.
**Cách sửa:** ⭐ ít nhất **mở tệp ra** mỗi quý; tốt hơn thì nạp vào CPU dự phòng (mục 54.5).

### 🔍 BẪY 4 — Mọi bản sao lưu nằm trên cùng một mạng

**Hiện tượng:** ⚠ mã độc tống tiền mã hoá cả bản sao lưu; hoặc cháy/ngập xoá cả hai chỗ.
**Cách sửa:** quy tắc ba bản, ⭐ bản thứ ba **ngoài nhà máy hoặc ngắt kết nối** (mục 54.4).

### 🔍 BẪY 5 — Chỉ một người biết mật khẩu

**Hiện tượng:** ⚠⚠ người đó nghỉ việc, và chương trình thành **hộp đen**.
**Cách sửa:** ghi ở nơi tổ chức truy cập được; ít nhất hai người biết (mục 54.6).

### 🔍 BẪY 6 — Không thoả thuận mã nguồn trong hợp đồng

**Hiện tượng:** ⚠ tranh cãi **sau khi máy đã chạy** — lúc đó không còn đòn bẩy nào.
**Cách sửa:** năm câu hỏi ở mục 54.6, ⭐ **ký trước khi làm máy**.

### 🔍 BẪY 7 — Nhận "mã nguồn" dạng bản in PDF

**Hiện tượng:** có hàng trăm trang giấy, ⚠ **không nạp lại được vào PLC**.
**Cách sửa:** ghi rõ **định dạng** trong hợp đồng (mục 54.6).

### 🔍 BẪY 8 — Tên tệp không có ngày và lý do

**Hiện tượng:** thư mục đầy `backup_moi.zip`, `backup_moi2.zip`, `backup_cuoi_cung.zip` — ⚠ **không
biết bản nào mới hơn**, không biết bản nào chứa gì.
**Cách sửa:** quy ước ở mục 54.7.

### 🔍 BẪY 9 — Số phiên bản không đọc được từ máy đang chạy

**Hiện tượng:** hỗ trợ từ xa, ⭐ **không ai trả lời được "máy đang chạy bản nào"**.
**Cách sửa:** biến phiên bản trong PLC **và** hiện trên HMI (mục 54.7).

### 🔍 BẪY 10 — Sao lưu chương trình an toàn như chương trình thường

**Hiện tượng:** ⚠⚠ khôi phục xong không chứng minh được đó là **bản đã kiểm định**.
**Cách sửa:** lưu kèm **mã kiểm tra** và hồ sơ kiểm định; ⚠ kiểm tra lại chức năng sau khôi phục
(mục 54.3, Chương 48).

---

## 54.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| ⚠⚠ Cách thất bại mặc định | ⭐ **Bản sao lưu duy nhất còn dùng được nằm trong CPU — và CPU là thứ vừa hỏng** |
| "Tải từ PLC về" hỏng ở đâu | CPU chết thì không tải được; và ⭐ **thường mất chú thích + tên biến** |
| ⭐⭐ Sao lưu mấy hạng mục | **Bảy**: PLC · cấu hình phần cứng · tham số driver · HMI · công thức · an toàn · mạng |
| Hạng mục hay quên nhất | ⭐ **Tham số biến tần / servo** |
| Khi nào bắt buộc sao lưu | ⭐ **Trước mọi thay đổi**; sau khi ổn định; sau nghiệm thu; định kỳ |
| Lợi ích phụ của sao lưu định kỳ | ⭐ **Phát hiện thay đổi không ai ghi** |
| Quy tắc ba bản | Tại máy · máy chủ nhà máy · ⭐ **ngoài nhà máy / ngắt kết nối** |
| Vì sao cần bản ngoài nhà máy | ⚠ Cháy, ngập, **mã độc tống tiền** |
| ⭐⭐ Câu quan trọng nhất chương | **Bản sao lưu chưa thử khôi phục không phải bản sao lưu** |
| Mức thử tối thiểu | ⚡ **Mở tệp ra xem** — bắt được 3/6 nguyên nhân thất bại |
| Cất kèm bản sao lưu | ⭐ **Quy trình khôi phục một trang** |
| Rủi ro lớn nhất của khoá mật khẩu | ⚠⚠ Nhà chế tạo biến mất → máy thành **hộp đen không sửa được** |
| Cách dung hoà | Khoá một phần · ⭐ **ký gửi mã nguồn** · ràng buộc hợp đồng · phân quyền |
| Ký hợp đồng phải rõ | Có mã nguồn không · **định dạng nào** · mật khẩu ai giữ · ai chịu chi phí nếu mất |
| Tên tệp gồm gì | Máy · phần · phiên bản · ngày · ⭐⭐ **lý do** |
| Phiên bản hiện ở đâu | Tên tệp · ⭐ biến trong PLC · ⭐ **màn hình HMI** |

---

## 54.11 Tự kiểm

1. ⚠⚠ Kể lại sự việc ở mục 54.1. Vì sao bản sao lưu **có tồn tại** mà vẫn không cứu được?
2. ⭐ Nêu năm lý do "tải chương trình từ PLC về" không phải một phương án khôi phục đầy đủ.
3. ⭐⭐ Kể bảy hạng mục phải sao lưu. Hạng mục nào hay bị quên nhất, và hậu quả cụ thể là gì?
4. Chương trình an toàn cần sao lưu thêm gì so với chương trình thường? Vì sao?
5. Nêu năm thời điểm phải sao lưu. Thời điểm nào là bắt buộc tuyệt đối?
6. ⭐ Sao lưu định kỳ có tác dụng phụ gì liên quan tới Chương 53?
7. Phát biểu quy tắc ba bản. Vì sao bản thứ ba phải ở ngoài nhà máy hoặc ngắt kết nối?
8. ⭐⭐ Vì sao "bản sao lưu chưa thử khôi phục không phải bản sao lưu"? Nêu sáu nguyên nhân thất bại.
9. ⚡ Mức thử khôi phục thấp nhất là gì, và nó bắt được mấy trong sáu nguyên nhân đó?
10. Quy trình khôi phục một trang gồm những gì? Vì sao ghi **nơi lấy mật khẩu** chứ không ghi mật
    khẩu?
11. ⚠ Nêu lập luận của **cả hai phía** về khoá chương trình bằng mật khẩu. Trường hợp xấu nhất là gì?
12. ⭐ Nêu bốn cách dung hoà, và năm điều phải rõ trong hợp đồng **trước khi làm máy**.
13. ⭐ Đặt tên tệp sao lưu cho DP-01, bản 3.1, ngày hôm nay, lý do "đổi ngưỡng cường độ UV". Trường
    nào biến thư mục sao lưu thành tài liệu?
14. ⭐⭐ Số phiên bản phải xuất hiện ở ba nơi nào? Vì sao nơi thứ ba tiết kiệm nửa giờ khi hỗ trợ từ
    xa?

> Câu 3, 8, 11 và 14 là bốn câu phân loại. Câu 8 là tinh thần của cả chương: ⭐ **một bản sao lưu chưa
> được kiểm chứng chỉ là một niềm tin, và niềm tin đó sụp đúng vào ngày tệ nhất.**

---

### Chương tiếp theo

Chương 55 — **Tính chu kỳ máy & năng suất**. Máy đã chạy, đã có quy trình thay đổi và sao lưu. Câu
hỏi tiếp theo là câu khách hàng luôn hỏi: **máy chạy được bao nhiêu sản phẩm mỗi giờ, và vì sao
không nhanh hơn được?**

### Nguồn tham khảo chương 54

- IEC 62443 (bộ) — *Industrial communication networks — IT security*: quản lý sao lưu, kiểm soát
  truy cập, và phục hồi hệ thống điều khiển. *(tiêu chuẩn có bản quyền)*
- IEC 61508 và ISO 13849-1 — yêu cầu quản lý cấu hình và ⚠ **kiểm chứng lại** với chức năng an toàn.
- IEC 60204-1 — tài liệu kỹ thuật đi kèm máy: cơ sở cho yêu cầu bàn giao ở mục 54.6.
- **Hướng dẫn của nhà sản xuất PLC, biến tần, HMI** — dùng cho ⭐ **cách sao lưu và khôi phục cụ
  thể của từng dòng**, và cho câu hỏi ở mục 54.2 (chú thích có nằm trong CPU không).
- Hợp đồng và điều khoản bàn giao — ⚠ **vấn đề pháp lý, không phải kỹ thuật**; xem mục cảnh báo bên
  dưới.

> ⚠ **Giới hạn.** Mục 54.6 mô tả **thực hành thương mại phổ biến**, không phải tư vấn pháp lý. Điều
> khoản về sở hữu trí tuệ, bàn giao mã nguồn và ký gửi mã nguồn có hiệu lực khác nhau tuỳ pháp luật
> từng nước và từng loại hợp đồng. ⚠ **Hỏi bộ phận pháp chế trước khi soạn hoặc ký** — chương này chỉ
> giúp bạn biết **cần hỏi điều gì**.
