# Chương 52 — Chạy thử & bàn giao

> **Lát cắt máy mẫu:** 5 — máy đầy đủ, gồm cả mạch an toàn, analog, chuyển động và mạng.

---

## 52.1 Bài toán: cỗ máy chạy đúng ngay lần đầu — và hỏng ba tiếng sau

Một cỗ máy vừa lắp xong. Kỹ sư nóng lòng muốn xem nó chạy. Bật nguồn, nạp chương trình, chuyển sang
Auto, nhấn Start.

Máy chạy. Mọi cơ cấu hoạt động, sản phẩm ra đúng. Cả nhóm thở phào.

Ba tiếng sau, module ngõ ra bốc khói. Nguyên nhân: một dây từ module tới cuộn van bị **đấu nhầm sang
chân 24 V** — tạo ngắn mạch qua transistor ngõ ra. Nó không cháy ngay vì transistor chịu được một lúc;
nó cháy sau khi nóng dần.

Nếu có ai **đo từng điểm I/O trước khi chạy logic**, sai sót đó lộ ra trong hai phút, tốn không đồng nào.

Chương này là thứ tự bắt buộc để chuyện đó không xảy ra — và những gì phải làm trước khi được nói
"máy đã xong".

---

## 52.2 Thứ tự bắt buộc — không được nhảy bước

> ⚠⚠ **NGUY HIỂM**
> Thứ tự dưới đây **không phải gợi ý**. Mỗi bước tồn tại để chặn một loại sự cố cụ thể, và nhảy bước
> nghĩa là chấp nhận loại sự cố đó. Cám dỗ nhảy thẳng tới bước 5 là rất lớn — hãy nhớ cỗ máy ở mục 52.1.

| Bước | Việc | Chặn được gì | Điện |
|---|---|---|---|
| **1** | **Kiểm nguội** | Đấu sai, thiếu dây, sai thiết bị | ❌ Không cấp điện |
| **2** | **Bật nguồn từng nhánh** | Ngắn mạch, chọn sai điện áp | ⚡ Cấp dần |
| **3** | ⭐ **Kiểm I/O 1-1** | Đấu nhầm kênh, sai kiểu, sai chiều | ⚡ Có điện, **chưa chạy logic** |
| **4** | **Kiểm chức năng an toàn** | Mạch an toàn không đúng | ⚡ |
| **5** | **Chạy khô** *(dry-run)* | Lỗi trình tự, va chạm | ⚡ Không sản phẩm |
| **6** | **Chạy có sản phẩm** | Lỗi liên quan sản phẩm thật | ⚡ |
| **7** | ⭐ **Thử tạo lỗi cố ý** | Xử lý bất thường sai | ⚡ |
| **8** | **Chạy liên tục** | Lỗi tích luỹ, quá nhiệt, trôi | ⚡ |

### ⭐ Ba mốc nghiệm thu — từ vựng bạn sẽ nghe ngay ngày đầu đi dự án

Tám bước ở trên là **việc kỹ thuật**. Trong hợp đồng và trong lời nói hằng ngày ở dự án, người ta
chia chúng theo **địa điểm và thời điểm** thành ba mốc. Tiêu chuẩn nghiệm thu hệ tự động hoá đặt tên
cho ba mốc này, và bạn cần biết chúng vì tiền và trách nhiệm gắn vào đúng ba cái tên đó:

| Mốc | Tên đầy đủ | Ở đâu | Chứng minh điều gì | Bước 1–8 tương ứng |
|---|---|---|---|---|
| **FAT** | *Factory Acceptance Test* — nghiệm thu tại xưởng chế tạo | Xưởng của **bên làm máy** | Máy làm đúng chức năng đã cam kết, trước khi tháo đi | 1–8, với sản phẩm mẫu |
| **SAT** | *Site Acceptance Test* — nghiệm thu tại hiện trường | Nhà máy của **bên mua** | Máy vẫn đúng sau khi vận chuyển, lắp lại, đấu vào nguồn và khí thật của nhà máy | 1–8, lặp lại |
| **SIT** | *Site Integration Test* — thử tích hợp tại hiện trường | Nhà máy của bên mua | Máy làm việc đúng **với các máy khác** trong chuyền và với hệ thống trên | Ghép chuyền, bắt tay, truyền dữ liệu |

Ba điều quan trọng mà người mới hay hiểu sai:

- **SAT không phải là FAT làm lại cho có.** Vận chuyển làm lỏng đầu nối; nguồn điện nhà máy khác
  nguồn xưởng; khí nén nhà máy có thể bẩn hơn hoặc áp thấp hơn; nhiệt độ và độ ẩm khác. Rất nhiều
  lỗi **chỉ xuất hiện** ở SAT. Đó là lý do tồn tại của nó.
- **SIT là nơi lỗi đắt nhất xuất hiện.** Máy chạy hoàn hảo một mình vẫn có thể sai khi ghép chuyền:
  bắt tay không khớp, chu kỳ không ăn nhau, dữ liệu gửi lên sai định dạng. Ở FAT không ai phát hiện
  được, vì lúc đó chưa có máy bên cạnh.
- **Ký FAT thường gắn với một đợt thanh toán.** Vì vậy có áp lực rất thật lên việc ký sớm. Cách tự
  bảo vệ duy nhất là **biên bản có danh mục cụ thể** — cái gì đã thử, cái gì chưa, cái gì có điều
  kiện. "Đã nghiệm thu" mà không kèm danh mục là câu vô nghĩa khi có tranh chấp.

> ⚡ **LƯU Ý**
> Với máy nhỏ, ba mốc có thể gộp lại — nhưng **gộp phải là quyết định có ghi lại**, không phải là
> chuyện quên làm. Ghi rõ trong biên bản: "SIT gộp vào SAT do máy chạy độc lập, không ghép chuyền."

---

## 52.3 Bước 1–2 — kiểm nguội và cấp nguồn

### Kiểm nguội

Làm khi **chưa cấp điện**, đối chiếu với bản vẽ và bảng I/O:

| Kiểm | Cách |
|---|---|
| Đúng thiết bị, đúng mã | Đối chiếu nhãn với danh mục vật tư (**Phụ lục C.11**) |
| Dây đúng cỡ, đầu cốt siết đủ chặt | Kéo nhẹ từng dây; siết lại theo lực quy định |
| Không có dây thừa, không có đầu dây hở | Nhìn kỹ; đầu hở là nguồn ngắn mạch |
| Nối đất đầy đủ | Đo thông mạch từ vỏ tủ tới thanh đất |
| Cách điện | Megôm kế — ⚠ **tháo rời thiết bị điện tử trước** (Chương 51) |
| Cơ cấu cô lập năng lượng **khoá được** | Thử gắn khoá thật vào (Chương 47) |

### Cấp nguồn từng nhánh

Không bật tất cả một lúc. Bật từng nhánh, đo trước khi bật nhánh sau:

```text
1. Nguồn tổng → đo điện áp vào, đo sau aptomat
2. Biến áp / bộ nguồn 24 V → đo 24 V khi KHÔNG tải
3. Nhánh cấp nguồn PLC → đo, kiểm đèn nguồn
4. Từng nhánh I/O → đo trước khi cắm module
5. Nhánh động lực → sau cùng
```

> 💡 **MẸO**
> Đo **điện áp 24 V khi tải nặng** ngay từ lúc này, và ghi lại con số. Nó là mốc so sánh cho suốt vòng
> đời máy — khi bộ nguồn lão hoá vài năm sau, bạn có gì để đối chiếu (Chương 51, mục 51.8).

---

## 52.4 Bước 3 — kiểm I/O 1-1 ⭐

Đây là bước hay bị bỏ nhất và là bước **trả lại nhiều nhất**.

> **Nguyên tắc: kiểm từng điểm I/O một cách độc lập, TRƯỚC khi chạy bất kỳ logic nào.**
>
> Chương trình chưa chạy. CPU ở STOP hoặc chạy một chương trình rỗng. Bạn kiểm **đường dây**, không
> kiểm logic.

### Kiểm ngõ vào

Với **từng** ngõ vào, theo bảng I/O:

1. Tác động thiết bị thật (đẩy cảm biến, nhấn nút, gạt công tắc).
2. Xem **đúng bit đó** lên trong phần mềm — không phải bit khác.
3. Nhả ra, xem bit về 0.
4. Ghi vào biên bản: đạt / không đạt.

Ba lỗi bước này bắt được mà mô phỏng không bắt được:

| Lỗi | Biểu hiện khi kiểm |
|---|---|
| **Đấu nhầm kênh** | Tác động cảm biến A, bit B lên |
| **Sai kiểu đấu** (PNP/NPN) | Đèn cảm biến sáng, bit không lên (Chương 4) |
| **Sai trạng thái nghỉ** | Bit đang là 1 khi chưa tác động, hoặc ngược lại (Chương 15) |

### Kiểm ngõ ra

Với **từng** ngõ ra:

1. Ép ngõ ra bật bằng chức năng cưỡng bức — theo đúng quy trình ở Chương 51.
2. Xem **đúng cơ cấu đó** hoạt động.
3. Đo dòng bằng ampe kìm nếu là tải lớn.
4. Gỡ cưỡng bức. Ghi biên bản.

> ⚠⚠ **NGUY HIỂM — kiểm ngõ ra là lúc máy chuyển động lần đầu**
> - Kiểm **từng cơ cấu một**, không bao giờ nhiều cái cùng lúc.
> - **Không ai được ở trong vùng máy.** Người thao tác đứng ở chỗ nhìn được toàn bộ cơ cấu.
> - Với cơ cấu có thể va chạm, **đưa về vị trí an toàn bằng tay trước**, hoặc tháo tạm khớp nối.
> - **Gỡ mọi cưỡng bức** ngay sau mỗi phép thử — không để tích luỹ.
> - Chuẩn bị sẵn cách dừng: tay đặt gần nút E-Stop trong suốt quá trình.

> 💡 **MẸO**
> Kiểm I/O 1-1 cho máy cỡ DP-01 mất khoảng nửa ngày. Đó là nửa ngày **rẻ nhất** trong cả dự án. Mọi
> giờ bỏ ra ở đây tiết kiệm nhiều giờ ở bước 5–8, nơi lỗi khó tách hơn nhiều vì logic đã tham gia.

---

## 52.5 Bước 4 — chức năng an toàn

> ⚠⚠ **NGUY HIỂM**
> Kiểm định chức năng an toàn phải do **người có thẩm quyền** thực hiện, theo tiêu chuẩn hiện hành, và
> có biên bản (Chương 47). Nội dung dưới đây là **danh mục tối thiểu để bạn biết cái gì phải được thử**
> — không phải quy trình kiểm định.

| Kiểm | Cách thử | Kỳ vọng |
|---|---|---|
| E-Stop tác dụng ở **mọi chế độ** | Nhấn ở Auto, Manual, Home, và **ở từng bước** của chu trình | Mọi chuyển động dừng theo loại dừng đã thiết kế |
| E-Stop **từng nút** riêng lẻ | Nhấn từng nút, không phải chỉ một cái | Mỗi nút đều tác dụng |
| **Từng kênh** của mạch hai kênh | Ngắt riêng kênh 1, rồi riêng kênh 2 | Mạch phát hiện được lệch kênh |
| Cửa khoá liên động | Mở từng cửa **trong lúc máy chạy** | Dừng; và cửa không mở được khi chưa an toàn |
| Rèm quang | Cắt tia ở nhiều vị trí, kể cả rìa | Dừng ở mọi vị trí |
| Muting | Cho sản phẩm qua; **rồi thử qua bằng vật khác** | Sản phẩm qua được; vật khác **không** kích hoạt muting |
| STO | Kích STO khi trục đang chạy | Mất mô-men; kiểm cả **quãng trôi theo đà** |
| Khởi động lại | Gỡ E-Stop | Máy **không** tự chạy (Chương 47) |

---

## 52.6 Bước 5–6 — chạy khô rồi chạy có sản phẩm

**Chạy khô** *(dry-run)*: chu trình chạy đầy đủ, không có sản phẩm. Cần cờ `M_DryRun` để các bước chờ
sản phẩm không báo lỗi giả (Chương 28).

Chạy khô lần đầu: **chạy từng bước một**, dừng sau mỗi bước, kiểm cơ cấu đúng vị trí trước khi cho
bước tiếp. Chỉ khi cả chu trình đã đi qua từng bước an toàn mới cho chạy liên tục.

**Chạy có sản phẩm**: bắt đầu bằng **một sản phẩm**, quan sát toàn bộ hành trình. Rồi hai. Rồi liên tục.

> ⚠ **NGUY HIỂM**
> Trước khi chạy khô lần đầu, **kiểm cờ `M_DryRun` và mọi cưỡng bức đã ở trạng thái đúng**, và kiểm
> **cờ mô phỏng đã tắt** (Chương 50). Máy chạy với cờ mô phỏng còn bật là máy chạy mù.

### ⭐ Ba công cụ của chính bộ điều khiển — kiểm tra trước khi tự dựng cờ

Cờ `M_DryRun` là giải pháp **phần mềm tự viết**. ⚠ Nhưng nhiều bộ điều khiển đã có sẵn công cụ làm
đúng việc đó, an toàn hơn vì **không phụ thuộc chương trình của bạn chạy đúng**:

| Công cụ | Nó làm gì | ⭐ Vì sao tốt hơn cờ tự viết |
|---|---|---|
| ⭐ **Chế độ thử** *(TEST mode)* | Chạy và gỡ lỗi chương trình **với ngõ ra bị vô hiệu** | ⭐⭐ Ngõ ra tắt **ở tầng hệ thống** — không có cách nào một lỗi logic bật nhầm được |
| ⭐ **Quét đơn** *(single scan)* | Thực thi **đúng một vòng quét** rồi dừng | ⭐ Quan sát **từng nấc ở từng vòng quét** — công cụ mạnh nhất cho lỗi phụ thuộc thứ tự (Chương 10) |
| Cô lập ngõ ra tại chỗ | Tháo/ngắt riêng các ngõ ra chưa thử | Dùng khi bắt buộc phải ở chế độ RUN để cập nhật ngõ ra |

> ⭐ **Tra tài liệu bộ điều khiển của bạn TRƯỚC khi tự dựng cờ chạy khô.** Nếu có chế độ thử, dùng nó
> cho vòng kiểm logic đầu tiên; cờ `M_DryRun` vẫn giữ vai trò riêng — nó cho phép chạy khô **trong chế
> độ RUN bình thường** về sau, khi máy đã bàn giao.

> ⚠⚠ **BẪY — nấc thang tạm để thử.**
>
> Trong lúc thử, người ta hay chèn **logic tạm**: một nấc bỏ qua một bước, một lệnh chặn nhóm ngõ ra
> chưa sẵn sàng, một điều kiện luôn đúng để đi tiếp. Chúng hữu ích và **hoàn toàn chính đáng**.
>
> ⚠⚠ **Nhưng chúng phải được gỡ hết trước khi chạy tổng thể** — và đây là **cùng một loại nguy hiểm
> với cưỡng bức quên gỡ** (Chương 51, mục 51.7), chỉ khác một điểm khiến nó **tệ hơn**:
>
> ⭐ **Cưỡng bức thì có danh sách để kiểm. Nấc thang tạm thì KHÔNG** — nó trông y hệt code thật.
>
> ⭐ **Cách phòng, làm ngay từ lúc chèn:**
>
> | | |
> |---|---|
> | 1 | ⭐ **Đánh dấu thống nhất** — comment mở đầu `*** TAM — GO TRUOC KHI BAN GIAO ***`, dễ tìm bằng tham chiếu chéo |
> | 2 | ⭐ Ghi vào **một danh sách** ngay khi chèn, cùng chỗ với danh sách cưỡng bức |
> | 3 | ⚠ **Đối chiếu chương trình với bản trước khi thử** — chức năng so sánh dự án (Chương 30) chỉ ra mọi thứ đã thêm |
> | 4 | ⚠⚠ Ghi vào **danh mục nghiệm thu** ở mục 52.9 như một mục riêng |

> ⭐ **Và ngay sau khi sửa bất cứ gì trong lúc chạy thử: ghi lại NGAY và cập nhật tài liệu gốc.**
> Không để tới cuối đợt — lúc đó không ai nhớ nổi đã sửa những gì (Chương 30).

---

## 52.7 Bước 7 — thử tạo lỗi cố ý ⭐

Đây là bước phân biệt nghiệm thu thật với nghiệm thu hình thức.

> **Thử máy ở điều kiện bình thường không phải là nghiệm thu. Đó mới là trình diễn.**
>
> Nghiệm thu là chứng minh máy **xử lý đúng khi có chuyện xảy ra** — vì đó chính là lúc thiệt hại
> xảy ra nếu nó xử lý sai.

Danh mục tối thiểu, thực hiện **trên máy thật** (khác với nhóm D của Chương 50 làm trên mô phỏng):

| # | Tạo lỗi thế nào | Kỳ vọng |
|---|---|---|
| 1 | **Rút từng cảm biến** khi đang chạy | Timeout đúng bước; thông báo nêu bước và tín hiệu chờ |
| 2 | **Ngắt khí nén** giữa chu trình | Dừng; trạng thái an toàn đúng bảng Chương 48; sản phẩm không rơi |
| 3 | **Nhấn E-Stop ở từng bước** | Dừng đúng; sau Reset, về gốc đúng thứ tự (Chương 28) |
| 4 | **Mở cửa** khi máy đang chạy | Dừng; không mở được nếu chưa an toàn |
| 5 | **Rút cáp mạng** tới màn hình / máy lân cận / hệ thống trên | Nhịp tim phát hiện; phản ứng đúng đặc tả (Chương 48) |
| 6 | **Ngắt điện đột ngột** rồi cấp lại | Không tự chạy; sản phẩm dở dang được xử lý đúng |
| 7 | **Lấy sản phẩm ra bằng tay** giữa chu trình | Phát hiện, báo lỗi, không chạy tiếp mù |
| 8 | **Cho hai sản phẩm vào sát nhau** | Giữ lại đúng, không va chạm |
| 9 | Ngắt **thiết bị phụ trợ** (ionizer, quạt hút) | Máy phát hiện và phản ứng đúng mức (Chương 48) |
| 10 | Cho **tín hiệu analog ra ngoài dải** | Phát hiện, giá trị thay thế an toàn, báo lỗi |

Mỗi ca phải ghi biên bản như Chương 50: điều kiện tạo ra, kết quả thật, đạt/không đạt.

---

## 52.8 Bước 8 — chạy liên tục và đo chu kỳ

### Chạy liên tục

Chạy đủ dài để lộ những thứ chỉ xuất hiện theo thời gian:

| Hiện tượng | Lộ ra sau |
|---|---|
| Nóng lên trong tủ | Vài giờ |
| Đầu cốt lỏng do chu kỳ nhiệt | Vài ngày tới vài tuần (Chương 51) |
| Bộ nhớ hoặc bộ đệm đầy dần | Vài giờ tới vài ngày |
| Trôi giá trị analog | Vài giờ |
| Mòn cơ khí | Dài hơn — theo dõi bằng xu hướng |

Trong lúc chạy liên tục, **ghi lại các mốc**: thời gian quét lớn nhất, điện áp 24 V nhỏ nhất, nhiệt độ
tủ, thời gian hành trình từng xy-lanh. Đây là **bộ số liệu chuẩn** để so sánh về sau (Chương 51, mục 51.11).

### Đo chu kỳ thật

Đo trên máy đang chạy ổn định, không tính lý thuyết:

1. Đếm sản phẩm ra trong **một giờ liên tục**, ở điều kiện sản xuất thật.
2. So với cam kết trong đặc tả.
3. Nếu không đạt: tìm **nút cổ chai** bằng cách đo thời gian từng bước của từng trạm (Chương 55) —
   không đoán.

> ⚡ **LƯU Ý**
> Đo trong một giờ, không đo trong năm phút rồi nhân lên. Năm phút không bao gồm thời gian chờ máy
> lân cận, đổi lô, hay các dừng vặt — mà những thứ đó mới là phần chênh lệch giữa con số lý thuyết và
> sản lượng thật.

---

## 52.9 Danh mục kiểm bắt buộc trước khi bàn giao

Đây là danh mục "không được bỏ sót" — mỗi mục đều là thứ đã từng gây sự cố ở đâu đó. Danh sách các
hạng mục còn tồn đọng tại thời điểm bàn giao gọi là **danh mục tồn** *(punch list)*: nó phải được
viết ra, có người chịu trách nhiệm và có hạn, chứ không phải "để đó rồi tính".

| # | Kiểm | Vì sao |
|---|---|---|
| 1 | ⭐ **Không còn cưỡng bức I/O nào** — ⚠⚠ kể cả loại **đã cài nhưng đang tắt** | Chương 51 — nguyên nhân tai nạn phổ biến |
| 1b | ⚠⚠ **Không còn nấc thang / logic tạm** nào của đợt thử | ⭐ Không có danh sách sẵn như cưỡng bức — phải **so sánh dự án** |
| 2 | ⭐ **Cờ mô phỏng đã tắt** và không giữ qua mất điện | Chương 50 |
| 3 | ⭐ **Cờ chạy khô đã tắt** | Chương 28 |
| 4 | **Chương trình đang chạy khớp với bản sao lưu** | Dùng chức năng so sánh — không tin trí nhớ |
| 5 | **Đã sao lưu đầy đủ** và **đã thử khôi phục** | Chương 54 — bản sao lưu chưa thử không phải bản sao lưu |
| 6 | Mọi **thông báo lỗi** hiển thị đúng và đọc được | Người vận hành phải hiểu được |
| 7 | **Đèn tháp** đúng ở mọi trạng thái | Chương 25, Bẫy 5 |
| 8 | **Biên bản kiểm định an toàn** đã có, có người ký | Chương 47 |
| 9 | **Bộ số liệu chuẩn** đã ghi (quét, 24 V, chu kỳ, thời gian hành trình) | Mốc so sánh cho vòng đời máy |
| 10 | **Tài liệu bàn giao** đầy đủ — mục 52.10 | |

---

## 52.10 Bàn giao

### Tài liệu

| Tài liệu | Ghi chú |
|---|---|
| Bản vẽ điện **hoàn công** *(as-built)* | ⭐ Phản ánh máy **thật**, không phải bản thiết kế ban đầu |
| Bảng I/O cuối cùng | Khớp với chương trình và với nhãn tại cầu đấu |
| Chương trình PLC + HMI, **có comment** | Chương 30 |
| Bản sao lưu đầy đủ, ghi rõ phiên bản | Gồm cả cấu hình phần cứng và tham số thiết bị |
| Đặc tả và **biên bản kiểm thử** | Chương 23, 50 |
| Biên bản kiểm định an toàn | Chương 47 |
| Bộ số liệu chuẩn | Mục 52.8 |
| Hướng dẫn vận hành và xử lý sự cố thường gặp | Viết cho người vận hành, không cho kỹ sư |
| Danh mục vật tư và linh kiện dự phòng khuyến nghị | Chương 51, mục 51.10 |

> ⚠ **NGUY HIỂM**
> Bản vẽ **as-built** không phải chi tiết hành chính. Người sửa máy lúc hai giờ sáng sẽ tin vào bản vẽ.
> Nếu bản vẽ nói dây X2-14 là cảm biến kẹp mà thực tế đã đổi sang X2-16, người đó sẽ đo nhầm chỗ, kết
> luận nhầm, và có thể chạm vào thứ đang có điện. **Cập nhật bản vẽ ngay khi thay đổi**, không để dồn.

### Đào tạo người vận hành

Đào tạo không phải đọc lại tài liệu. Bốn thứ phải làm được sau buổi đào tạo:

1. Khởi động máy từ trạng thái tắt, chạy một lô, dừng đúng cách.
2. **Đọc được thông báo lỗi và biết bước đầu tiên phải làm.**
3. Xử lý được ba tình huống thường gặp nhất — cho họ **tự làm**, không xem người khác làm.
4. Biết **khi nào phải dừng và gọi kỹ thuật**, thay vì tự xử lý.

> 💡 **MẸO**
> Kết thúc buổi đào tạo bằng cách **tự tay tạo một lỗi** rồi để người vận hành xử lý. Đó là phép kiểm
> duy nhất chứng minh buổi đào tạo có tác dụng — và nó thường lộ ra rằng thông báo lỗi của bạn chưa
> đủ rõ.

---

## 52.11 Bẫy thường gặp

### 🔍 BẪY 1 — Nhảy thẳng tới bước chạy

Bẫy trung tâm của chương, và là cỗ máy ở mục 52.1. Cám dỗ rất lớn vì chạy được máy cho **cảm giác tiến
triển**, còn đo từng điểm I/O thì không.

### 🔍 BẪY 2 — Kiểm I/O bằng chương trình thay vì bằng cưỡng bức

*"Cứ chạy chương trình rồi xem cơ cấu nào động"* — cách này trộn hai biến số: nếu cơ cấu không động,
bạn không biết do dây hay do logic. Bước 3 tồn tại để **tách hai thứ đó ra**.

> ⭐ **Và cưỡng bức ngõ RA là công cụ đúng cho việc này, đúng về mặt cơ chế:** nó chỉ chạm tới chân ra,
> ⭐ **không đổi bảng ảnh ngõ ra**, nên chương trình chạy y như cũ trong lúc bạn thử dây (Chương 51,
> mục 51.7). ⚠ Cưỡng bức ngõ **VÀO** thì ngược lại — nó lan khắp chương trình, nên **không dùng để
> kiểm dây ngõ ra**.

### 🔍 BẪY 3 — Thử E-Stop một lần rồi coi là xong

Nhấn một nút, thấy máy dừng, tích vào ô. Chưa thử: các nút khác, từng kênh riêng lẻ, các bước khác của
chu trình, và hành vi sau khi gỡ.

### 🔍 BẪY 4 — Bản vẽ không cập nhật

Trong lúc chạy thử luôn có thay đổi: đổi chân, thêm dây, đổi thiết bị. Nếu ghi lên giấy rồi "để về vẽ
lại", thường sẽ không vẽ lại.

**Cách phòng:** cập nhật bản vẽ **trong ngày**, và coi bản vẽ as-built là mục bắt buộc trong danh mục
bàn giao — không được ký nghiệm thu khi chưa có.

### 🔍 BẪY 5 — Đo chu kỳ trong điều kiện lý tưởng

Đo lúc mọi thứ hoàn hảo, không có dừng vặt, không chờ máy lân cận. Con số đẹp và **không phản ánh sản
lượng thật**. Đo trong một giờ ở điều kiện sản xuất thật.

### 🔍 BẪY 6 — Bàn giao khi còn cưỡng bức hoặc còn cờ mô phỏng

Ba mục đầu của danh mục ở 52.9 tồn tại vì cả ba đều đã từng gây sự cố nghiêm trọng. Chúng mất ba phút
để kiểm.

### 🔍 BẪY 7 — Không thử khôi phục bản sao lưu

Sao lưu xong, cất đi, coi như an toàn. Ngày cần dùng mới phát hiện file hỏng, thiếu cấu hình phần cứng,
hoặc thiếu tham số thiết bị.

**Bản sao lưu chưa thử khôi phục không phải bản sao lưu.** Chương 54.

---

## 52.11b Bảng chốt

| Chủ đề | Chốt lại |
|---|---|
| ⚠⚠ **Thứ tự tám bước** | **Không phải gợi ý.** Mỗi bước chặn một loại sự cố; nhảy bước là chấp nhận loại sự cố đó (mục 52.2) |
| ⭐ **Ba mốc nghiệm thu** | **FAT** tại xưởng · **SAT** tại hiện trường · **SIT** khi ghép chuyền. ⚠ SAT **không phải** FAT làm lại — vận chuyển, nguồn, khí và nhiệt độ đều khác |
| ⭐⭐ **Kiểm I/O 1-1** | Kiểm **từng kênh một**, bằng **cưỡng bức**, ⚠ **không bằng chương trình** — chương trình sai thì phép kiểm sai theo (Bẫy 2) |
| ⚠ **Chức năng an toàn** | Thử **từng nút, từng cửa, từng rèm** — không thử một cái rồi suy ra cái còn lại (Bẫy 3) |
| ⭐ **Thử tạo lỗi cố ý** | Bước 7 là bước phân biệt máy **chạy được** với máy **dùng được**. Cắt khí, che cảm biến, rút cáp — rồi xem máy nói gì |
| ⚠ **Đo chu kỳ** | Đo ở **điều kiện thật**: sản phẩm thật, người thật, có cả lúc chờ. ⭐ Con số đo lúc lý tưởng là con số sẽ bị đem ra cãi nhau (Bẫy 5) |
| ⭐⭐ **Trước khi bàn giao** | ⚠ Gỡ **hết** cưỡng bức — kể cả loại "đã cài nhưng đang tắt" · tắt cờ mô phỏng và chạy khô · bỏ mọi nấc thang tạm (mục 52.9) |
| ⭐ **Sao lưu** | Bản sao lưu **chưa thử khôi phục** thì chưa phải bản sao lưu (Bẫy 7, Chương 54) |
| **Bộ số liệu chuẩn** | Ghi lại lúc máy còn tốt: thời gian quét, điện áp 24 V, chu kỳ, thời gian hành trình từng cơ cấu — ⭐ **mốc so sánh cho cả vòng đời máy** (Chương 53) |
| ⚠ **Danh mục tồn** | Phải **viết ra, có người chịu trách nhiệm, có hạn**. "Để đó rồi tính" nghĩa là không bao giờ |
| ⭐ **Biên bản** | *"Đã nghiệm thu"* mà **không kèm danh mục cụ thể** là câu vô nghĩa khi có tranh chấp |
| ⭐⭐ **Bàn giao là một hoạt động, không phải một lần gửi tệp** | Tài liệu **cộng** đào tạo người vận hành. Máy tốt mà không ai biết dùng thì vẫn là máy dừng (mục 52.10) |

---

## 52.12 Tự kiểm

1. Kể lại sự cố ở mục 52.1. **Bước nào** trong thứ tự tám bước đã có thể chặn nó, và mất bao lâu?
2. Vì sao kiểm I/O 1-1 phải làm **trước khi chạy bất kỳ logic nào**?
3. Nêu **ba lỗi** mà bước kiểm I/O bắt được nhưng mô phỏng không bắt được.
4. Nêu **năm điều bắt buộc về an toàn** khi kiểm ngõ ra — bước máy chuyển động lần đầu.
5. Vì sao *"thử máy ở điều kiện bình thường"* chưa phải là nghiệm thu?
6. Kể **năm ca thử tạo lỗi cố ý** và kỳ vọng của mỗi ca.
7. Vì sao phải đo chu kỳ trong **một giờ**, không đo năm phút rồi nhân lên?
8. Nêu **ba mục đầu** của danh mục kiểm bắt buộc trước bàn giao. Vì sao cả ba đều nguy hiểm?
9. Vì sao bản vẽ **as-built** là vấn đề an toàn, không chỉ là thủ tục?
10. Bốn thứ người vận hành phải **làm được** sau buổi đào tạo là gì? Cách kiểm buổi đào tạo có tác dụng?

Câu 2, 5 và 8 là ba câu phân loại. Câu 5 là tinh thần của cả chương: **nghiệm thu là chứng minh máy xử
lý đúng khi có chuyện, không phải chứng minh nó chạy được khi mọi thứ thuận lợi.**

---

### Chương tiếp theo

**Chương 53 — Bảo trì & thay đổi khi máy đang chạy.** Máy đã bàn giao và đang sản xuất. Từ giờ mọi
thay đổi đều diễn ra trên một cỗ máy không được phép dừng lâu — và điều đó đổi hoàn toàn cách làm việc.

---

### Nguồn tham khảo chương 52

- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: các phép thử và kiểm định
  trang bị điện của máy; yêu cầu tài liệu kỹ thuật đi kèm. *(tiêu chuẩn có bản quyền)*
- ISO 13849-2 — *Safety of machinery — Safety-related parts of control systems — Validation*: nguyên
  tắc kiểm định chức năng an toàn — nền cho mục 52.5.
- IEC 62381 — *Automation systems in the process industry — Factory Acceptance Test (FAT), Site
  Acceptance Test (SAT), Site Integration Test (SIT)*: định nghĩa và phạm vi ba mốc nghiệm thu ở
  mục 52.2, và yêu cầu về hồ sơ kèm theo từng mốc.
- Biểu mẫu **biên bản kiểm I/O 1-1**, **biên bản nghiệm thu** và **phiếu bàn giao** — Phụ lục C.
- Bảng I/O, đặc tả và bảng trạng thái an toàn của DP-01 — Phụ lục J.
- **Bryan, L.A. & Bryan, E.A.** — *Programmable Controllers: Theory and Implementation*, ch. 20 §20-5 *PLC Start-Up and
  Checking Procedures*: ⭐ **chế độ thử** *(TEST mode)* chạy chương trình với **ngõ ra bị vô hiệu**;
  **quét đơn** để soát từng nấc; cô lập ngõ ra chưa thử; ⚠⚠ **gỡ mọi nấc thang tạm** trước khi chạy
  tổng thể; và ⭐ **ghi lại mọi thay đổi NGAY**, cập nhật tài liệu gốc — nền cho mục 52.6.

> ⚠⚠ Mục 52.5 là **danh mục tối thiểu để bạn biết cái gì phải được thử**, không phải quy trình kiểm
> định. Kiểm định chức năng an toàn phải do người có thẩm quyền thực hiện theo tiêu chuẩn hiện hành
> tại thị trường của bạn, và phải có biên bản.
