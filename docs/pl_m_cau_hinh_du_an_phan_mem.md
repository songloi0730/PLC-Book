# Phụ lục M — Cấu hình dự án phần mềm: phần trường không dạy

> **Ở trường, một bài PLC thường gồm: khai vài tag, viết logic, bấm mô phỏng, xong.**
>
> ⭐ Trên máy thật, phần đó là **một phần nhỏ** của một dự án phần mềm PLC. Phần còn lại không phải
> lập trình — nó là **cấu hình**, và nó quyết định máy có chạy được hay không nhiều hơn logic.

---

## M.1 ⭐⭐ Khoảng cách giữa bài tập và dự án thật

| Ở trường | ⭐ Trên máy thật |
|---|---|
| Tag có sẵn, hoặc tự đặt tuỳ ý | ⭐ Tag phải khớp **số dây trong tủ** và **nhãn trên màn hình** (Chương 23, 49, Phụ lục C.1) |
| PLC là một hộp trừu tượng trong bộ mô phỏng | ⭐ Phải **khai đúng CPU, đúng module, đúng khe**, đúng phiên bản firmware (Phụ lục C.10) |
| Ngõ vào là ô tích chuột | Ngõ vào có **kiểu đấu**, **thời gian lọc**, **dải analog**, **hành vi khi đứt dây** — mỗi thứ là một tham số phải đặt |
| Không có mạng | ⭐ Có **địa chỉ IP, tên trạm, giao thức** — và một sơ đồ địa chỉ phải quản lý |
| Bật mô phỏng là chạy | ⭐ Có **STOP / STARTUP / RUN**, có vòng quét đầu tiên, có khởi động lại sau mất điện |
| Sai thì sửa rồi chạy lại | ⚠⚠ Sai thì **cơ cấu chuyển động thật**, và có người đứng cạnh |
| Xong bài là xong | ⭐ Còn **sao lưu, mật khẩu, bàn giao, khôi phục** (Chương 54) |

> ⭐⭐ **Một cách đo khoảng cách đó rất gọn: đếm xem có bao nhiêu thứ phải đặt ĐÚNG trước khi dòng
> lệnh đầu tiên có ý nghĩa.**
>
> ⚡ Trong bộ mô phỏng: gần như không có gì. ⭐ Trên máy thật: **cấu hình phần cứng · tham số từng
> module · địa chỉ mạng · vùng nhớ giữ được · đồng hồ · mức truy cập** — sáu nhóm, và **logic của
> bạn chạy sai hoặc không chạy nếu bất kỳ nhóm nào sai**, mà phần lớn chúng **không báo lỗi biên
> dịch**.

---

## M.2 Cấu hình phần cứng trong phần mềm

⭐ Đây là bước đầu tiên của mọi dự án thật, và là bước **không tồn tại** trong bài tập mô phỏng.

| Việc | Nội dung | ⚠ Sai thì |
|---|---|---|
| Khai **CPU** | Đúng mã, ⭐ **đúng phiên bản firmware** | Nạp không xuống được, hoặc thiếu chức năng |
| Khai **từng module, đúng khe** | Theo bản đồ khe cắm (**Phụ lục C.10**) | ⚠⚠ Địa chỉ **dịch** — mọi tag trỏ sang thiết bị khác (Chương 8 mục 8.4) |
| Đặt **tham số từng module** | Xem bảng dưới | ⭐ Chương trình đúng mà phép đo vẫn sai |
| Khai **thiết bị trên mạng** | Tên trạm, địa chỉ, tệp mô tả thiết bị | Thiết bị không lên mạng |

### ⭐ Tham số module — nhóm bị bỏ quên nhiều nhất

⚠ Đây là chỗ *"chương trình đúng mà máy vẫn sai"* hay xuất phát, vì ⭐ **không có gì trong mã nguồn
cho thấy các tham số này tồn tại**.

| Loại module | Tham số phải đặt | Chương |
|---|---|---|
| **Ngõ vào số** | ⭐ **Thời gian lọc ngõ vào** — ⚠ đặt quá dài thì mất xung ngắn, quá ngắn thì nhiễu lọt | 9 mục 9.3b · 10 mục 10.3 |
| **Ngõ ra số** | Trạng thái ngõ ra ⭐ **khi CPU chuyển sang STOP** — giữ giá trị cuối hay về 0 | ⚠ **8 mục 8.8** · 48 |
| **Analog vào** | Kiểu tín hiệu (áp/dòng) · dải · ⭐ **lọc/trung bình hoá** · ⭐⭐ **bật chẩn đoán đứt dây** | 31 mục 31.3 · 32 |
| **Analog ra** | Dải · ⭐ giá trị khi CPU dừng | 31 · 48 |
| **Nhiệt độ** | ⭐ Loại cảm biến (Pt100/Pt1000, loại cặp nhiệt) · **số dây** · hệ số alpha · bù đầu lạnh | ⚠ **33** |
| **Bộ đếm tốc độ cao** | Chế độ đếm · kênh nào dùng được · hướng | 18 mục 18.5 |

> ⚠⚠ **Ba tham số dưới đây sai thì KHÔNG có báo lỗi nào, và triệu chứng trông y hệt lỗi lập trình:**
>
> | Tham số sai | Triệu chứng |
> |---|---|
> | Kiểu tín hiệu analog (áp thay vì dòng) | Giá trị luôn ở đáy hoặc đỉnh thang (**Phụ lục E.5**) |
> | Loại cảm biến nhiệt / số dây | Nhiệt độ lệch **có hệ thống**, đồ thị trông bình thường (Chương 33) |
> | Thời gian lọc ngõ vào đặt quá dài | ⭐ Xung ngắn **biến mất** — và mã đếm của bạn không sai một chữ nào |

> ⭐⭐ **Vì vậy bảng cấu hình phần cứng (C.10) phải ghi cả tham số module, không chỉ khe cắm.** ⚡ Nó
> là **mục số 2 của bộ sao lưu tám hạng mục** (Phụ lục C.9) đúng vì lý do này: không có nó thì một
> CPU mới nạp chương trình vào **vẫn không chạy đúng**.

### ⭐ Biến thể phần cứng trong cùng một dự án

Máy đóng theo lô thường **không giống hệt nhau**: lô đầu dùng đảo van của hãng này, lô sau đổi sang
hãng khác vì giá hay vì hàng về chậm. Hai cách quản lý, cùng bài toán *"hai loại đảo van trên mạng"*:

| Cách | Làm thế nào | Ưu | Nhược |
|---|---|---|---|
| **A — hai dự án** | Mỗi biến thể một bản dự án riêng | Mỗi bản sạch, không có thiết bị thừa | ⚠⚠ Sửa một lỗi phải sửa **hai nơi**; sau vài lần sửa, hai bản lệch nhau mà không ai biết |
| ⭐ **B — một dự án, khai cả hai, tắt cái không lắp** | Cấu hình mạng khai cả hai thiết bị; cái không lắp đánh dấu **không dùng**; chương trình chọn biến thể bằng **một tham số** | **Một** nguồn duy nhất; đổi biến thể ngay lúc chạy thử | ⚠ Bật nhầm cái không lắp thì mạng không lên — phải có cách nhận ra ngay |

⭐ **Khuyến nghị: cách B**, kèm ba quy tắc — một máy đang chạy mà tôi đọc được cấu hình làm đúng cách
này: hai đảo van khác hãng cùng nằm trong cấu hình, một cái bị tắt, và ghi chú đầu chương trình nhắc
*phải xác nhận lắp hãng nào*.

1. Tham số biến thể nằm ở **một** chỗ, ghi vào bảng cấu hình phần cứng (**Phụ lục C.10**) và hiện
   trên màn hình chẩn đoán.
2. Ngay sau khởi động, **so** thiết bị đã khai với thiết bị thật sự trả lời trên mạng; lệch thì báo một
   lỗi **có tên** — *"cấu hình biến thể sai"* — thay vì một lỗi *"mất kết nối"* chung chung.
3. Nhật ký sửa đổi ghi rõ **lô máy nào** dùng biến thể nào (Chương 30 mục 30.6).

**✅ Đạt khi:** đặt tham số biến thể và tắt đúng thiết bị → máy lên mạng không lỗi; cố ý bật nhầm thiết
bị → thông báo nói đúng *"cấu hình biến thể sai"*, không phải lỗi chung.

---

## M.3 ⭐ Mạng: địa chỉ IP, tên trạm, và một sơ đồ phải quản lý

⚠ Bài tập mô phỏng không có mạng. ⭐ Máy thật thì gần như luôn có — và **địa chỉ là thứ phải thiết
kế, không phải thứ gõ đại cho chạy**.

| Hạng mục | Phải quyết định | ⚠ Bỏ qua thì |
|---|---|---|
| ⭐⭐ **Địa chỉ tĩnh hay cấp động** | ⭐ Thiết bị điều khiển **luôn dùng địa chỉ tĩnh** | ⚠⚠ Cấp động thì sau một lần mất điện, thiết bị **đổi địa chỉ** và máy mất kết nối |
| **Dải địa chỉ của máy** | Một dải riêng cho máy, ghi lại từng địa chỉ đã dùng | ⚠ Trùng địa chỉ với máy khác khi đưa vào chuyền |
| ⭐ **Tên trạm** *(device name)* | Nhiều giao thức định danh thiết bị **bằng tên**, không bằng IP | Thay thiết bị mới mà quên đặt tên → không lên mạng |
| **Mặt nạ mạng và cổng ra** | Thiết bị cùng máy nên **cùng một mạng con** | Hai thiết bị không thấy nhau dù dây đúng |
| ⭐⭐ **Tách mạng máy khỏi mạng nhà máy** | Máy chạy được **kể cả khi mạng trên chết** | ⚠⚠ Sự cố mạng văn phòng làm dừng sản xuất (Chương 45) |
| **Sơ đồ địa chỉ** | Một bảng: thiết bị · IP · tên trạm · cổng switch | ⭐ Không ai biết cái gì ở đâu khi có sự cố |

> ⭐⭐ **Địa chỉ IP là một tài sản của dự án, không phải một thiết lập.** ⚡ Nó phải nằm trong
> **Phụ lục C.10.2**, phải nằm trong **bộ sao lưu** (Phụ lục C.9, hạng mục 7), và phải **dán nhãn
> trong tủ**.

> ⭐ **Một chi tiết đáng biết về việc xoá bộ nhớ CPU.** Trên một số hệ, lệnh **xoá bộ nhớ** xoá sạch
> vùng nhớ làm việc và cả vùng giữ được — ⭐ **nhưng KHÔNG xoá địa chỉ IP đã lưu và KHÔNG xoá bộ đệm
> chẩn đoán**.
>
> ⚡ Nghĩa là: sau khi xoá bộ nhớ, ⭐ **CPU vẫn giữ địa chỉ mạng** (nên bạn vẫn kết nối được), và
> ⭐⭐ **lịch sử sự cố vẫn còn để đọc**. ⚠ Nhưng đừng suy ngược rằng mọi hệ đều vậy — **kiểm tài liệu
> CPU của bạn trước khi dựa vào điều đó**.

---

## M.4 ⭐⭐ Khởi động: STOP, STARTUP, RUN — và vòng quét đầu tiên

⚠ Trong bộ mô phỏng, "chạy" là một trạng thái. ⭐ Trên máy thật có **ba** trạng thái, và **đèn trên
CPU cho biết đang ở trạng thái nào** — đây là thứ đầu tiên phải nhìn khi tới máy.

| Trạng thái | Xảy ra gì | ⭐ Việc bạn làm được |
|---|---|---|
| **STOP** | CPU **không chạy** chương trình | ⭐ Nạp dự án xuống |
| ⭐ **STARTUP** | Khối khởi động (nếu có) chạy **đúng một lần**; ⚠ **ngắt chưa được xử lý** | Khởi tạo giá trị ban đầu |
| **RUN** | Vòng quét chạy lặp mãi; ngắt được xử lý | Chạy máy; ⭐ một phần dự án nạp được ngay khi đang RUN |

### ⚠⚠ Khởi động lại nóng và xoá bộ nhớ — hai thứ rất khác nhau

| | **Khởi động lại nóng** *(warm restart)* | **Xoá bộ nhớ** *(memory reset)* |
|---|---|---|
| Dữ liệu **không giữ được** | ⭐ Đưa về **giá trị ban đầu** | Xoá |
| ⭐⭐ Dữ liệu **giữ được** | ⭐ **Được giữ lại** | ⚠⚠ **Bị xoá** |
| Bộ đệm chẩn đoán | Giữ | ⭐ **Giữ** |
| Địa chỉ IP đã lưu | Giữ | ⭐ **Giữ** |

> ⚠⚠ **Và đây là cái bẫy mà không bài tập nào dạy: NẠP LẠI một khối dữ liệu có thể đặt giá trị giữ
> được về giá trị khởi tạo.** ⭐ Tuỳ hệ và tuỳ đời phần mềm, nạp xuống một khối dữ liệu làm cả phần
> giữ được lẫn phần không giữ được **quay về giá trị ban đầu** ở lần vào RUN kế tiếp.
>
> ⚡ Nghĩa là: bộ đếm sản lượng, bộ đếm tuổi thọ vật tư, số giờ chạy — ⚠ **về 0 sau một lần sửa
> chương trình**, và không ai nhận ra cho tới khi cần con số đó (Chương 16 mục 16.4, Chương 53).
>
> ⭐⭐ **Việc phải làm trước mỗi lần nạp: đọc và ghi lại các con số tích luỹ.** Và đưa việc đó vào
> quy trình thay đổi ở Chương 53 mục 53.3.

### ⭐ Vòng quét đầu tiên — thứ phải khởi tạo, và thứ tuyệt đối không

| ⭐ Nên làm ở vòng quét đầu | ⚠⚠ KHÔNG được làm |
|---|---|
| Đặt biến trạng thái về giá trị an toàn đã biết | ⚠⚠ **Tự động cho phép chuyển động** |
| Xoá các cờ tạm không giữ được | ⚠⚠ **Tự động về gốc** — Chương 28 nói rõ vì sao |
| Nạp tham số công thức đang chọn (Chương 29) | ⚠ Giả định cơ cấu đang ở vị trí nghỉ |
| ⭐ Đặt cờ *"chưa về gốc"* = TRUE | Xoá lịch sử báo động |
| ⭐ **Che sườn lên** của vòng này bằng cờ `M_FirstScan` (Chương 16 Bẫy 9) | ⚠⚠ **Tin một sườn lên** ở vòng này — nút kẹt hay cảm biến đang che cũng thành *"vừa nhấn"*, *"vừa tới"* |

> ⭐⭐ **Nguyên tắc: sau khi có điện lại, máy phải ở trạng thái AN TOÀN và BIẾT RẰNG MÌNH KHÔNG BIẾT
> GÌ** — chưa về gốc, chưa biết vị trí cơ cấu, chưa biết có sản phẩm trong máy hay không.
>
> ⚠ Bài tập mô phỏng không bao giờ dạy điều này vì trong mô phỏng **không có mất điện giữa chừng**.

---

## M.5 ⭐ Đồng hồ và dấu thời gian

⚠ Hạng mục này bị bỏ qua gần như mọi lần, và nó **âm thầm làm hỏng giá trị của mọi bản ghi**.

| Việc | Vì sao cần |
|---|---|
| Đặt **đồng hồ CPU** | ⭐ Mọi báo động, mọi bản ghi sản xuất đều đóng dấu bằng đồng hồ này |
| ⭐⭐ **Đồng bộ thời gian tự động** | ⚠ Đồng hồ CPU **trôi**. Sau vài tháng, dấu thời gian lệch tới mức không đối chiếu được với máy khác |
| **Múi giờ và quy ước ghi** | ⭐ Quan trọng khi báo cáo lên hệ thống trên (Chương 45) |
| ⭐ **Pin hoặc nguồn nuôi đồng hồ** | ⚠ Hết pin → mỗi lần mất điện, đồng hồ về mốc mặc định |

> ⭐⭐ **Vì sao chuyện nhỏ này đáng một mục riêng:** ⚡ khi đi tìm nguyên nhân một sự cố, thứ giá trị
> nhất là **đối chiếu thời điểm** giữa bản ghi của PLC, bản ghi của màn hình, và bản ghi của hệ
> thống trên (Chương 51, Phụ lục E.1 câu 1).
>
> ⚠ Ba đồng hồ lệch nhau vài phút thì **phép đối chiếu đó vô nghĩa** — và bạn mất đúng công cụ mạnh
> nhất của mình. ⭐ Đây cũng là lý do hạng mục *"mốc đo lúc nghiệm thu"* ở **Phụ lục C.9** đòi ghi
> **điều kiện đo**, không chỉ con số.

---

## M.6 ⭐⭐ Chẩn đoán của chính CPU — thứ phải đọc TRƯỚC khi đọc code

⚠ Khi máy có sự cố, phản xạ của người mới là **mở chương trình ra đọc**. ⭐ Phản xạ đúng là **đọc
những gì CPU đã tự ghi lại**.

| Nguồn | Nó cho biết gì | ⭐ Vì sao đọc trước |
|---|---|---|
| ⭐⭐ **Đèn trên CPU và trên module** | Trạng thái vận hành; có lỗi phần cứng hay không | ⚡ **Không cần máy tính** — nhìn là biết ở STOP hay RUN |
| ⭐⭐ **Bộ đệm chẩn đoán** *(diagnostic buffer)* | ⭐ Danh sách sự kiện **kèm dấu thời gian**: lỗi module, chuyển STOP, mất kết nối | ⭐ **Nó sống sót qua cả lệnh xoá bộ nhớ** — là bản ghi pháp y của CPU |
| **Mã lỗi hệ thống** | Loại lỗi cụ thể | Tra thẳng trong tài liệu hãng |
| ⭐ **Thời gian quét lớn nhất** | So với con số lúc nghiệm thu | Phát hiện trôi (Chương 36, 51) |

### ⚠⚠ Lỗi nặng, lỗi nhẹ, và một cái bẫy an toàn

⭐ Các hệ phân biệt **lỗi làm dừng CPU** với **lỗi chỉ ghi nhận rồi chạy tiếp**:

| Loại | Hành vi | Ví dụ |
|---|---|---|
| ⚠⚠ **Lỗi nặng** | ⭐ **Dừng thực thi**, CPU vào trạng thái lỗi, đèn báo lỗi | Truy cập ngoài mảng · chia cho 0 ở một số hệ · lỗi cấu hình |
| **Lỗi nhẹ** | Ghi vào bộ đệm, ⭐ **chương trình chạy tiếp** | ⭐ Tác vụ chồng lên chính nó (Chương 27 mục 27.6) |

> ⚠⚠ **Và đây là cái bẫy: nhiều hệ cho bạn viết một "thủ tục xử lý lỗi" để XOÁ lỗi nặng và chạy
> tiếp.**
>
> ⭐ Về kỹ thuật nó hoạt động: lỗi được xoá, lệnh gây lỗi **không chạy**, chương trình chạy tiếp từ
> lệnh kế. ⚡ Về an toàn, ⚠⚠ **nó là một trong những thứ nguy hiểm nhất bạn có thể viết** — vì nó
> biến *"máy dừng vì có gì đó sai"* thành *"máy chạy tiếp và không ai biết"*.
>
> ⭐⭐ **Quy tắc:** chỉ dùng thủ tục xử lý lỗi để **đưa máy về trạng thái an toàn rồi dừng có kiểm
> soát và báo rõ**, ⚠ **không bao giờ** dùng nó để giấu lỗi cho dây chuyền khỏi dừng. ⚡ Nếu áp lực
> sản lượng đòi điều đó, thì vấn đề cần giải là **nguyên nhân gốc**, không phải cái báo lỗi
> (Chương 48, 51).

---

## M.7 ⭐ Mật khẩu, mức truy cập và bảo vệ mã nguồn

| Cơ chế | Nó chặn gì | ⚠ Cái giá |
|---|---|---|
| **Mật khẩu vào CPU** | Người lạ nạp chương trình khác xuống | ⚠ Mất mật khẩu = **mất quyền sửa máy của chính mình** |
| ⭐ **Nhiều mức truy cập** | Đọc / đọc-ghi / toàn quyền — cho từng vai trò | Phải quản lý nhiều mật khẩu |
| ⭐⭐ **Bảo vệ khối** *(know-how protection)* | Người khác **không mở xem được** ruột khối | ⚠⚠ Khối bị khoá thì **người bảo trì của khách cũng không sửa được** |
| **Chữ ký khối** | Bằng chứng khối chưa bị đụng vào | Ký rồi thì sửa gì cũng phải gỡ ký (Chương 30 mục 30.5) |

> ⚠⚠ **Quyết định này là quyết định HỢP ĐỒNG, không phải quyết định kỹ thuật.** ⭐ Khoá mã nguồn máy
> rồi bàn giao cho khách nghĩa là: mỗi lần khách cần sửa một con số, họ phải gọi bạn — và **lúc hai
> giờ sáng thì bạn không nghe máy**.
>
> ⭐⭐ **Phải thoả thuận bằng văn bản TRƯỚC KHI làm máy**: khách được nhận mã nguồn tới mức nào, ai
> giữ mật khẩu, và ⚠ **chuyện gì xảy ra nếu công ty bạn không còn tồn tại** (Chương 54 mục 54.6).

---

## M.8 Nạp xuống, thẻ nhớ và khôi phục

| Việc | ⭐ Điểm phải biết |
|---|---|
| **Nạp toàn bộ** | Thường phải đưa CPU về STOP — ⚠ **máy dừng** |
| ⭐ **Nạp một phần khi đang RUN** | Làm được ở nhiều hệ, ⚠⚠ nhưng là thao tác **nguy hiểm** — Chương 53 mục 53.2 |
| ⭐⭐ **Thẻ nhớ** | Ở nhiều hệ, thẻ nhớ **là** chương trình. ⚠ Rút nhầm thẻ = máy mất chương trình |
| **Khôi phục** | ⭐ Phải **thử ít nhất một lần** trước khi bàn giao (Chương 54) |

> ⭐⭐ **Thứ tự khôi phục đúng là: cấu hình phần cứng → chương trình → tham số thiết bị rời → màn
> hình.** ⚡ Đảo thứ tự thì CPU mới **không nhận I/O**, và bạn sẽ đi tìm lỗi trong chương trình
> (Chương 54).

---

## M.9 ⚠⚠ Mô phỏng KHÔNG kiểm được gì

⭐ Mô phỏng rất đáng dùng — Chương 50 nói rõ nó tiết kiệm bao nhiêu. ⚠ Nhưng phải biết **ranh giới**
của nó, vì đây đúng là chỗ người học ở trường hay nhầm.

| ⭐ Mô phỏng kiểm được | ⚠⚠ Mô phỏng KHÔNG kiểm được |
|---|---|
| Logic trình tự, điều kiện chuyển bước | ⚠⚠ **Kiểu đấu sink/source, PNP/NPN** — Hình 9.1 |
| Máy trạng thái, chế độ vận hành | ⚠ **Tham số module** (dải analog, lọc, loại cảm biến nhiệt) |
| Phép tính, quy đổi thang | ⚠⚠ **Thời gian thật của cơ cấu** — mọi timeout đều là số đoán |
| Cấu trúc chương trình, cách đặt tên | ⚠ **Thời gian quét thật** và hành vi phụ thuộc nó |
| Xử lý bất thường **đã nghĩ ra** | ⚠⚠ **Bất thường chưa nghĩ ra** — đứt dây, nhiễu, sụt áp |
| Bế tắc giữa hai trạm | ⚠⚠ **Mọi thứ thuộc về điện và lắp đặt** (Chương 49) |
| | ⚠⚠ **Chức năng an toàn** — Chương 47, 48 |

> ⭐⭐ **Cách phát biểu gọn nhất về ranh giới đó:** ⚡ **mô phỏng kiểm được thứ bạn ĐÃ NGHĨ TỚI.** ⚠
> Phần lớn sự cố trên máy thật đến từ thứ **chưa ai nghĩ tới** — và đó chính là phần mà kiểm thử
> tình huống xấu (Chương 50 mục 50.5) và chạy thử tại hiện trường (Chương 52) tồn tại để bắt.

> ⚠⚠ **Và một ranh giới tuyệt đối:** ⭐ **không bao giờ dùng mô phỏng để nghiệm thu chức năng an
> toàn.** Chức năng an toàn nghiệm thu bằng **thử thật trên máy thật**, có biên bản (Phụ lục C.8,
> Chương 47, 48).

---

## M.10 ⭐ Danh mục kiểm — dự án phần mềm đã cấu hình xong chưa

> ⚠ **Đánh dấu được hết những mục dưới đây thì dự án phần mềm mới sẵn sàng để chạy thử:**
>
> **Phần cứng**
>
> - [ ] CPU và **mọi module** đã khai đúng mã, đúng khe, ⭐ đúng phiên bản firmware
> - [ ] ⭐ **Tham số từng module** đã đặt và **đã ghi vào Phụ lục C.10**
> - [ ] Trạng thái ngõ ra **khi CPU sang STOP** đã đặt có chủ ý (Chương 8 mục 8.8)
> - [ ] ⭐ Chẩn đoán **đứt dây** của kênh analog đã bật ở những kênh cần
> - [ ] Máy có **biến thể phần cứng**: thiết bị không lắp đã tắt trong cấu hình; tham số biến thể ghi
>   vào Phụ lục C.10 (mục M.2)
>
> **Mạng**
>
> - [ ] Mọi thiết bị dùng **địa chỉ tĩnh**; sơ đồ địa chỉ đã ghi lại
> - [ ] ⭐ Tên trạm đã đặt cho thiết bị định danh bằng tên
> - [ ] ⭐⭐ Máy **chạy được khi mạng nhà máy chết** — đã thử bằng cách rút dây
>
> **Khởi động và bộ nhớ**
>
> - [ ] ⭐ Đã xác định biến nào **giữ được**, biến nào không (Chương 16 mục 16.4)
> - [ ] ⭐⭐ Đã thử **mất điện giữa chu trình** rồi cấp lại — máy về trạng thái an toàn, **không tự chuyển động**
> - [ ] Con số tích luỹ (sản lượng, tuổi thọ vật tư) ⚠ **đã ghi lại trước khi nạp**
>
> **Thời gian**
>
> - [ ] Đồng hồ CPU đã đặt đúng; ⭐ đồng bộ tự động đã cấu hình
> - [ ] ⭐ Dấu thời gian của PLC, màn hình và hệ thống trên **đã đối chiếu khớp nhau**
>
> **Chẩn đoán và bảo vệ**
>
> - [ ] ⭐ Đã biết cách **mở bộ đệm chẩn đoán** và đã đọc thử một lần
> - [ ] ⚠⚠ **Không có thủ tục xử lý lỗi nào xoá lỗi nặng rồi chạy tiếp** mà không báo
> - [ ] Mật khẩu và mức truy cập đã đặt; ⭐ **đã ghi vào hồ sơ bàn giao**, không chỉ trong đầu
> - [ ] ⭐⭐ Thoả thuận bàn giao mã nguồn **đã ký** (Chương 54 mục 54.6)
>
> **Sao lưu**
>
> - [ ] ⭐ **Bộ sao lưu tám hạng mục** đã đủ (Phụ lục C.9)
> - [ ] ⭐⭐ Đã **thử khôi phục ít nhất một lần**, theo đúng thứ tự ở mục M.8

---

## M.11 Dẫn về đâu

| Bạn cần | Đọc |
|---|---|
| Bản đồ khe cắm và tham số module — biểu mẫu | ⭐ **Phụ lục C.10** |
| Bộ sao lưu và phiếu bàn giao | **Phụ lục C.9** · Chương 54 |
| Chín bước đầu dự án | ⭐ **Chương 23 mục 23.2b** |
| Vòng quét, ảnh ngõ vào, xung ngắn | ⭐ **Chương 10** |
| Biến giữ được hay không | Chương 16 mục 16.4 · Chương 11 mục 11.4 |
| Chế độ vận hành, về gốc, phục hồi | ⭐ **Chương 28** |
| Sửa chương trình khi máy đang chạy | ⚠ **Chương 53 mục 53.2** |
| Mô phỏng: dùng tới đâu | **Chương 50** |
| Tra theo triệu chứng | **Phụ lục E** |

> ⚠⚠ **Giới hạn của phụ lục này.** ⭐ Tên gọi, số bước và cách đặt của **từng hệ mỗi khác** — phụ lục
> này nêu **việc phải làm**, không nêu cách bấm. ⚡ Cách bấm nằm trong tài liệu hãng của hệ bạn dùng
> (Phụ lục A1, A2).
>
> ⚠ Và mọi con số, hành vi nêu ở đây phải **kiểm lại theo đúng dòng CPU và đúng phiên bản phần mềm**
> của bạn — ⭐ đặc biệt là hành vi **giữ / không giữ khi nạp lại**, vì nó khác nhau giữa các đời.

---

### Nguồn tham khảo phụ lục M

- **Siemens** — *S7-1200 Programmable controller System Manual*: ba chế độ **STOP / STARTUP / RUN**
  và đèn báo trên CPU; ⭐ khối khởi động chạy **một lần** và **ngắt chưa được xử lý** trong STARTUP;
  phân biệt ⭐⭐ **khởi động lại nóng** (dữ liệu không giữ được về giá trị ban đầu, dữ liệu giữ được
  **được giữ**) với **xoá bộ nhớ** (xoá cả hai) — và ⭐ **xoá bộ nhớ KHÔNG xoá bộ đệm chẩn đoán lẫn
  địa chỉ IP đã lưu**; ⚠ lưu ý **nạp lại khối dữ liệu có thể đặt giá trị giữ được về giá trị khởi
  tạo**; truy cập I/O tức thời bỏ qua ảnh quá trình — nền cho mục M.3, M.4.
- **Rockwell Automation** — *Logix 5000 Controllers Major, Minor, and I/O Faults* (1756-PM014):
  ⚠⚠ **lỗi nặng dừng thực thi** và đưa bộ điều khiển vào trạng thái lỗi (đèn OK nháy đỏ); ⭐ có thể
  viết **thủ tục xử lý lỗi** để xoá lỗi và chạy tiếp — lệnh gây lỗi **không chạy**, thực thi tiếp
  từ lệnh kế; vị trí đặt thủ tục xử lý lỗi — nền cho mục M.6.
- **Rockwell Automation** — *Logix 5000 Controllers Tasks, Programs, and Routines* (1756-PM005):
  ⚠ **lỗi nhẹ khi tác vụ chồng lên chính nó** — ví dụ ở bảng lỗi nặng / lỗi nhẹ.
- Tài liệu cấu hình của từng hệ trong **Phụ lục A1, A2** — dùng cho tên gọi và cách đặt cụ thể.

> ⚡ Các hành vi nêu trong phụ lục này **có ở dạng nào đó trên hầu hết hệ hiện đại**, nhưng ⚠ **tên
> gọi và chi tiết khác nhau**. Hai nguồn hãng ở trên được dẫn vì chúng mô tả rõ ràng và kiểm chứng
> được; ⭐ **không suy ra rằng hệ của bạn hành xử y hệt**.
