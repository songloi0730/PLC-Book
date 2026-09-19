# Chương 2 — PLC là gì, và khi nào **không** nên dùng PLC

---

## 2.1 Bài toán gốc: tủ rơ-le và cái giá của việc đổi đời xe

Cuối những năm 1960, dây chuyền lắp ráp ô tô được điều khiển bằng **tủ rơ-le**: hàng trăm, có khi
hàng nghìn rơ-le đấu dây với nhau. Logic của cỗ máy **chính là cách đi dây** — mạch tự giữ ở Chương 3
mục 3.6, nhân lên hàng nghìn lần.

Nó hoạt động. Vấn đề nằm ở chỗ khác.

Mỗi khi hãng xe **đổi đời xe** — chuyện xảy ra hàng năm — dây chuyền phải đổi theo. Và đổi logic
nghĩa là **đi lại dây**: tháo, đấu lại, dò lỗi, thử. Việc này mất nhiều tuần, tốn rất nhiều công, và
trong suốt thời gian đó dây chuyền **không sản xuất**.

Yêu cầu đặt ra rất rõ ràng:

> **Một thiết bị điều khiển mà đổi logic không phải đi lại dây** — chịu được môi trường xưởng, và
> **người thợ điện đang có sẵn phải dùng được**, không cần tuyển lập trình viên máy tính.

Câu trả lời xuất hiện năm 1968: **Modicon 084**, do nhóm của **Dick Morley** phát triển. Đó là bộ
điều khiển logic khả trình đầu tiên — **PLC** *(Programmable Logic Controller)*.

### Ba quyết định thiết kế còn nguyên giá trị

Yêu cầu ở trên định hình PLC tới tận hôm nay, và giải thích rất nhiều thứ trong cuốn sách này:

| Quyết định | Vì sao | Hệ quả bạn thấy hôm nay |
|---|---|---|
| **Ngôn ngữ nhìn giống sơ đồ mạch** | Để thợ điện dùng được ngay | ⭐ **Ladder** vẫn thống trị ở tầng máy (Chương 15, Chương 20 mục 20.6) |
| **Chạy lặp một vòng cố định** | Để hành vi đoán trước được, giống mạch rơ-le | **Vòng quét** (Chương 10) — nền của gần như mọi chương sau |
| **Chịu được môi trường xưởng** | Nhiệt, rung, nhiễu, bụi | Phần cứng chắc chắn, tuổi đời rất dài (mục 2.3) |

> ⭐ **Ladder không phải di sản lỗi thời.** Nó là một **quyết định thiết kế có chủ đích** — và cái lý
> do ban đầu (người bảo trì phải đọc được) vẫn còn nguyên sau gần sáu mươi năm. Chương 20 mục 20.6
> quay lại chuyện này khi bàn chọn ngôn ngữ.

---

## 2.2 PLC khác máy tính thường ở đâu

Đây là câu hỏi mà người có nền công nghệ thông tin hay hỏi: *"sao không dùng một máy tính nhỏ, rẻ hơn
nhiều?"*

Bốn khác biệt, và không cái nào là chuyện tốc độ.

### 1. Môi trường

| | Máy tính văn phòng | PLC |
|---|---|---|
| Nhiệt độ làm việc | Phòng có điều hoà | Dải rộng, trong tủ nóng |
| Rung | Đặt yên trên bàn | Gắn trên máy đang chuyển động |
| Nhiễu điện | Môi trường sạch | ⚠ Cạnh biến tần, máy hàn, contactor lớn |
| Bụi, dầu, ẩm | Không | Có |
| Mất điện đột ngột | Có UPS, tắt có trình tự | ⚠ **Mất là mất** — phải chịu được |

Yêu cầu môi trường được chuẩn hoá và **kiểm chứng bằng phép thử** (IEC 61131-2). Đó là một phần lý do
PLC đắt hơn phần cứng máy tính có năng lực tính toán tương đương.

### 2. ⭐ Tính tất định

**Tất định** *(deterministic)* nghĩa là: **cùng đầu vào thì luôn cho cùng hành vi, trong cùng khoảng
thời gian**.

Máy tính đa nhiệm không bảo đảm điều đó. Hệ điều hành có thể chen ngang để cập nhật, quét vi-rút, dọn
bộ nhớ. Với soạn thảo văn bản thì không sao — chậm nửa giây không ai chết. Với một cơ cấu đang chuyển
động, nửa giây là khoảng cách giữa "dừng đúng chỗ" và "va chạm".

> ⭐ **Đây là khác biệt cốt lõi, và nó quan trọng hơn tốc độ.**
> PLC không nhanh hơn một máy tính hiện đại. Nó **đều đặn** hơn. Vòng quét 10 ms nghĩa là 10 ms mỗi
> vòng, không phải "thường là 10 ms nhưng thỉnh thoảng 200 ms" (Chương 10).

### 3. Khởi động lại

| | Máy tính | PLC |
|---|---|---|
| Có điện thì | Khởi động hệ điều hành, mất hàng chục giây | Chạy chương trình gần như ngay |
| Cần thao tác của người | Có thể có | Không |
| Trạng thái sau khi có điện lại | Tuỳ | ⭐ **Xác định và cấu hình được** (Chương 8, mục 8.6) |

Một cỗ máy mất điện lúc 3 giờ sáng phải sẵn sàng ngay khi có điện lại, không chờ ai bấm gì.

### 4. Tuổi đời

> **Một cỗ máy công nghiệp sống 15–20 năm, và bộ điều khiển phải sống cùng nó.**

Điều đó đòi hỏi: phụ tùng còn mua được sau mười năm; phần mềm còn mở được dự án cũ; và không có bản
cập nhật bắt buộc nào làm hỏng thứ đang chạy.

Đây là tiêu chí **khả năng cung ứng dài hạn** ở Chương 13, và là lý do thị trường PLC thay đổi chậm
hơn nhiều so với thị trường máy tính.

### 5. ⭐⭐ Sửa được chương trình trong lúc máy đang chạy

⭐ Đây là khác biệt ít được nhắc nhất, mà lại là khác biệt **thay đổi cả cách làm nghề**.

| | Phần mềm máy tính thường | PLC |
|---|---|---|
| Đổi một dòng lệnh | Dừng chương trình, nạp bản mới, chạy lại | ⭐ **Nạp thay đổi trong lúc máy vẫn đang chạy** |
| Cái phải trả giá | Thời gian dừng | ⚠⚠ **Rủi ro ngay tại thời điểm nạp** |

> ⭐ **Vì sao thiết bị này được thiết kế như vậy:** một dây chuyền dừng nửa tiếng để nạp lại chương
> trình có thể tốn hơn cả tháng lương người sửa. ⚡ Nên khả năng **đổi mà không dừng** không phải
> tiện nghi — với nhiều nhà máy nó là **điều kiện để chấp nhận thiết bị**.

> ⚠⚠ **Nhưng nó là con dao hai lưỡi, và đây là chỗ nguy hiểm nhất trong cả chương này.** ⭐ Sửa lúc
> máy đang chạy nghĩa là cơ cấu **đang ở giữa chừng một hành trình** khi logic điều khiển nó đổi.
> ⚠ Người đứng cạnh máy **không được cảnh báo gì cả** — máy không dừng, không có đèn nào đổi màu.
>
> ⚡ Cả một chương của sách dành cho việc làm chuyện này an toàn: **Chương 53**. ⭐ Ở đây chỉ cần
> nhớ một điều: ⚠⚠ **PLC cho phép bạn làm điều đó KHÔNG có nghĩa là bạn nên làm.**

---

---

## 2.3 PLC, PAC, DCS, IPC hay vi điều khiển

Năm loại thiết bị điều khiển, mỗi loại thắng ở một chỗ.

| Loại | Là gì | Thắng ở đâu | ⚠ Yếu ở đâu |
|---|---|---|---|
| **PLC** | Bộ điều khiển logic khả trình | Máy rời rạc, trình tự, I/O số — ⭐ **địa hạt của cuốn sách này** | Tính toán nặng, xử lý dữ liệu lớn |
| **PAC** *(Programmable Automation Controller)* | PLC mạnh hơn, thiên về xử lý dữ liệu và chuyển động | Máy phức tạp, nhiều trục, cần tính toán | Giá cao hơn; ranh giới với PLC ngày càng mờ |
| **DCS** *(Distributed Control System)* | Hệ điều khiển phân tán cho nhà máy quá trình | Nhà máy hoá chất, lọc dầu, nhiệt điện — hàng nghìn điểm đo, chạy liên tục | Quá nặng và quá đắt cho một cỗ máy |
| **IPC** *(Industrial PC)* + PLC mềm | Máy tính công nghiệp chạy phần mềm điều khiển | Cần tích hợp thị giác máy, cơ sở dữ liệu, giao diện phong phú | Phụ thuộc hệ điều hành; tính tất định cần cấu hình cẩn thận |
| **Vi điều khiển** *(microcontroller)* | Chip nhỏ lập trình bằng C hoặc tương đương | Sản phẩm hàng loạt, giá rất thấp, chức năng cố định | ⚠ Không có hệ sinh thái công nghiệp; **không ai bảo trì được ngoài người viết** |

### Ranh giới thực tế

Đừng học thuộc bảng trên — chỉ cần ba câu hỏi:

> **1. Đây là một CỖ MÁY hay một NHÀ MÁY?**
> Cỗ máy rời rạc, có chu trình lặp → PLC. Quá trình liên tục quy mô nhà máy → DCS.
>
> **2. Ai sẽ bảo trì nó?**
> Đội bảo trì nhà máy → PLC (họ biết ladder). Đội phần mềm chuyên trách → IPC hoặc PAC khả thi.
>
> **3. Làm bao nhiêu cái?**
> Một tới vài chục → PLC. Hàng nghìn cái giống hệt nhau, chức năng cố định → vi điều khiển.

Câu thứ hai thường quyết định nhiều hơn câu thứ nhất — và nó là cùng một câu hỏi với Chương 20 mục
20.6 và Chương 13.

---

## 2.4 ⭐ Khi nào PLC là lựa chọn **sai**

Sách về PLC hiếm khi nói phần này. Nhưng chọn sai công cụ là sai lầm tốn kém, và nó xảy ra theo cả
hai hướng.

### Trường hợp 1 — Nguyên mẫu một lần, làm xong bỏ

Bạn cần một thiết bị thử nghiệm chạy vài tuần rồi tháo.

| PLC | Lựa chọn hợp hơn |
|---|---|
| Chi phí phần cứng và bản quyền phần mềm cao | Vi điều khiển, hoặc bo mạch phát triển |
| Nhiều thời gian đấu tủ | Đấu tạm trên bàn |
| Độ tin cậy 20 năm — **không cần** | Đủ chạy vài tuần |

⚠ **Ngoại lệ quan trọng:** nếu thiết bị đó có **chuyển động gây thương tích được**, thì lập luận
"chỉ dùng tạm" không áp dụng cho phần an toàn. Mạch an toàn vẫn phải đúng (Chương 47).

### Trường hợp 2 — Xử lý ảnh nặng

Kiểm tra ngoại quan bằng camera độ phân giải cao, phân loại theo hình ảnh.

PLC **không sinh ra cho việc này**. Kiến trúc đúng: một hệ thị giác chuyên dụng hoặc IPC làm phần xử
lý ảnh, rồi trả về PLC một kết quả đơn giản — đạt hay không đạt, hoặc một toạ độ.

> 💡 **Đây là mẫu rất phổ biến và rất nên nhớ: mỗi bên làm việc mình giỏi.**
> Hệ thị giác quyết định *"board này có lỗi không"*; PLC quyết định *"vậy thì làm gì tiếp"* — dừng
> chuyền, đánh dấu, loại bỏ (Chương 19, mục 19.6). Ranh giới giữa hai bên là **một vài bit và vài
> con số**, không phải hình ảnh.

### Trường hợp 3 — Sản phẩm hàng loạt giá rẻ

Bạn làm một thiết bị bán ra hàng nghìn cái. Giá thành từng cái quyết định sản phẩm sống hay chết.

Một PLC cho mỗi thiết bị là quá đắt. Vi điều khiển là câu trả lời — chức năng cố định, sản lượng lớn,
chi phí đơn vị rất thấp.

### Trường hợp 4 — Việc thuần công nghệ thông tin

Thu thập dữ liệu, dựng báo cáo, phân tích xu hướng dài hạn, giao diện web.

PLC làm được một phần, nhưng rất kém. Kiến trúc đúng: PLC lo điều khiển, tầng trên lo dữ liệu
(Chương 42, Chương 45).

### ⚠ Và hướng ngược lại — khi PLC là lựa chọn **đúng** mà người ta lại né

Sai lầm này ít được nói tới nhưng gặp thường xuyên, nhất là với người có nền lập trình:

> *"Tôi viết được cái này bằng máy tính nhỏ, rẻ hơn nhiều."*

Đúng là rẻ hơn — **về phần cứng**. Nhưng cỗ máy đó sẽ:

- ⚠ **Không ai bảo trì được ngoài bạn.** Đội bảo trì nhà máy biết ladder, không biết ngôn ngữ bạn dùng.
- **Không có hệ sinh thái**: không có module I/O cắm vào là chạy, không có tài liệu chuẩn, không có
  người thay thế bạn.
- **Không chịu được môi trường** nếu không tự làm phần cứng công nghiệp.
- ⚠ **Không có đường đi rõ ràng cho phần an toàn** (Chương 47).
- **Sống được bao lâu?** Bo mạch đó còn mua được sau năm năm không?

> ⭐ **Chi phí thật của một bộ điều khiển không phải giá mua — mà là chi phí sở hữu suốt 15 năm**, và
> phần lớn của nó là **thời gian dừng máy và công bảo trì** (Chương 13, tiêu chí 6).
>
> Một PLC "đắt" mà bất kỳ thợ điện nào cũng sửa được lúc 2 giờ sáng thường **rẻ hơn nhiều** so với một
> giải pháp tự chế mà chỉ một người hiểu.

---

## 2.5 Bẫy thường gặp

Bẫy của chương này không phải bẫy lập trình — chúng là **bẫy khi chọn**, và hậu quả của chúng kéo dài
suốt vòng đời cỗ máy.

### 🔍 BẪY 1 — So sánh bộ điều khiển bằng giá mua

**Hiện tượng:** chọn được phương án rẻ nhất lúc mua, rồi mất nhiều hơn ở bản quyền phần mềm, ở thời
gian chờ phụ tùng, và ở những giờ dừng máy.
**Cách sửa:** so bằng **chi phí sở hữu 15 năm** — giá mua + bản quyền + phụ tùng + công bảo trì +
thời gian dừng máy (mục 2.4, Chương 13).

### 🔍 BẪY 2 — Tự chế bằng máy tính nhỏ cho máy sản xuất

**Hiện tượng:** máy chạy tốt cho tới khi người viết nghỉ việc. Sau đó không ai trong nhà máy mở được,
sửa được, hay thay được — và cỗ máy trở thành hộp đen.
**Cách sửa:** năm vấn đề ở cuối mục 2.4. Câu hỏi quyết định là **"ai sẽ bảo trì nó?"**

### 🔍 BẪY 3 — Dùng PLC cho việc xử lý ảnh

**Hiện tượng:** chương trình phình to, thời gian quét vọt lên, và kết quả vẫn kém hơn một hệ thị giác
rẻ tiền.
**Cách sửa:** mỗi bên làm việc mình giỏi — hệ thị giác trả về **một kết quả đơn giản**, PLC quyết
định làm gì tiếp (mục 2.4).

### 🔍 BẪY 4 — Chọn PLC trước khi biết ai sẽ bảo trì

**Hiện tượng:** chọn xong mới biết nhà máy đã chuẩn hoá theo hãng khác; đội bảo trì phải học thêm một
hệ, kho phải trữ thêm một loại phụ tùng.
**Cách sửa:** hỏi câu đó **trước tiên** — nó thuộc về đặc tả (Chương 13, tiêu chí 7; Chương 23).

### 🔍 BẪY 5 — Coi ladder là thứ lỗi thời cần thay

**Hiện tượng:** viết toàn bộ chương trình bằng ngôn ngữ văn bản cho gọn, rồi người bảo trì không chẩn
đoán được khi máy hỏng.
**Cách sửa:** ladder là **quyết định thiết kế có chủ đích**, và lý do của nó vẫn còn nguyên
(mục 2.1, Chương 20 mục 20.6).

### 🔍 BẪY 6 — Bỏ qua yêu cầu môi trường vì "tủ có quạt rồi"

**Hiện tượng:** thiết bị hoạt động sai vào những ngày nóng, hoặc khi biến tần bên cạnh chạy tải nặng.
Triệu chứng chập chờn, rất khó tái hiện (Chương 51).
**Cách sửa:** yêu cầu môi trường của thiết bị công nghiệp là thứ **được kiểm chứng bằng phép thử**,
không phải lời quảng cáo. Tra dải nhiệt độ và mức chịu nhiễu trong datasheet (mục 2.2).

### 🔍 BẪY 7 — Lập luận "chỉ dùng tạm" áp cả cho phần an toàn

**Hiện tượng:** một thiết bị thử nghiệm có cơ cấu chuyển động được dựng tạm, không có mạch an toàn —
và nó chạy "tạm" trong hai năm.
**Cách sửa:** ⚠ lập luận "dùng tạm" **không áp dụng** cho phần an toàn. Thiết bị nào gây thương tích
được thì mạch an toàn vẫn phải đúng (mục 2.4, Chương 47).

---

## 2.6 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| PLC sinh ra để giải bài toán gì | **Đổi logic mà không phải đi lại dây** |
| Vì sao ladder trông giống sơ đồ mạch | Để **thợ điện dùng được ngay** — lý do đó vẫn còn nguyên |
| Khác biệt cốt lõi với máy tính thường | ⭐ **Tính tất định**, không phải tốc độ |
| Tính tất định nghĩa là | Cùng đầu vào → cùng hành vi, **trong cùng khoảng thời gian** |
| Tuổi đời phải tính tới | **15–20 năm** — phụ tùng, phần mềm, người biết dùng |
| Khả năng ít được nhắc nhất | ⭐ **Sửa chương trình khi máy đang chạy** — và ⚠⚠ nó nguy hiểm đúng bằng mức nó tiện (Chương 53) |
| Cỗ máy rời rạc | **PLC** |
| Nhà máy quá trình liên tục | **DCS** |
| Cần thị giác máy, cơ sở dữ liệu | **IPC / PAC**, hoặc PLC + hệ chuyên dụng |
| Sản phẩm hàng loạt giá rẻ | **Vi điều khiển** |
| Ba câu hỏi chọn nhanh | Cỗ máy hay nhà máy · **ai bảo trì** · làm bao nhiêu cái |
| PLC sai khi | Nguyên mẫu một lần · xử lý ảnh nặng · hàng loạt giá rẻ · việc thuần CNTT |
| ⚠ Sai lầm ngược lại | Tự chế bằng máy tính nhỏ → **không ai bảo trì được ngoài bạn** |
| Chi phí thật của bộ điều khiển | ⭐ **Chi phí sở hữu 15 năm**, không phải giá mua |

---

## 2.7 Tự kiểm

1. Bài toán nào dẫn tới việc PLC được phát minh? Vì sao tủ rơ-le không giải được nó?
2. Nêu ba quyết định thiết kế ban đầu của PLC và cho biết mỗi cái để lại dấu vết gì trong cách bạn
   lập trình hôm nay.
3. ⭐ Vì sao **tính tất định** quan trọng hơn tốc độ? Cho một ví dụ trên máy tự động hoá.
4. Nêu bốn khác biệt giữa PLC và máy tính văn phòng. Khác biệt nào ít liên quan tới hiệu năng nhất?
5. Vì sao tuổi đời 15–20 năm lại ảnh hưởng tới việc **chọn hãng**?
6. Phân biệt PLC với DCS bằng một câu hỏi.
7. ⭐ Nêu ba câu hỏi để chọn nhanh loại bộ điều khiển. Câu nào thường quyết định nhiều nhất, và vì sao?
8. Nêu bốn trường hợp PLC là lựa chọn sai, và cho biết lựa chọn hợp hơn ở mỗi trường hợp.
9. Máy cần kiểm tra ngoại quan bằng camera. Kiến trúc đúng là gì, và ranh giới giữa hai bên là gì?
10. ⭐ Một kỹ sư phần mềm nói *"tôi làm cái này bằng máy tính nhỏ, rẻ hơn nhiều"*. Nêu **năm** vấn đề
    của lập luận đó.

> Câu 3, 7 và 10 là ba câu phân loại. Câu 10 là tinh thần của cả chương: **chi phí của một bộ điều
> khiển không nằm ở lúc mua nó, mà ở mười lăm năm sau đó.**

---

### Chương tiếp theo

Chương 3 — **Điện đủ dùng cho người làm PLC**. Bạn đã biết PLC là gì và khi nào dùng nó. Trước khi
chạm vào bất cứ thứ gì, cần lượng điện tối thiểu để làm việc an toàn — và để hiểu vì sao mạch dừng
phải dùng tiếp điểm thường đóng.

### Nguồn tham khảo chương 2

- IEC 61131-1 — *Programmable controllers, Part 1: General information*: định nghĩa PLC và mô hình
  chức năng. *(tiêu chuẩn có bản quyền)*
- IEC 61131-2 — *Programmable controllers, Part 2: Equipment requirements and tests*: yêu cầu môi
  trường (nhiệt độ, rung, nhiễu) và các phép thử — cơ sở cho mục 2.2.
- Tư liệu lịch sử về **Modicon 084** và về bối cảnh ra đời của PLC năm 1968 — dùng cho mục 2.1.
- Catalogue của các hãng nêu ở Chương 8 và Chương 13 — dùng để đối chiếu ranh giới PLC / PAC / IPC,
  vốn đang mờ dần theo thời gian.

> ⚡ Ranh giới giữa **PLC, PAC và IPC** ở mục 2.3 đang **mờ dần**: PLC hiện đại làm được nhiều việc
> trước đây phải dùng PAC, và PLC mềm trên IPC ngày càng phổ biến. Bảng trong mục đó mô tả **xu hướng
> chung**, không phải phân loại cứng — và nó sẽ tiếp tục đổi. Ba câu hỏi ở cuối mục 2.3 bền hơn bảng.
