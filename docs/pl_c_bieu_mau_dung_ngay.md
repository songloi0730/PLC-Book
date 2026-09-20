
# Phụ lục C — Biểu mẫu dùng ngay

> **Mười một biểu mẫu trống, chép ra dùng được cho dự án của bạn.**
>
> Mỗi biểu mẫu có: ⭐ **một dòng nói nó dùng để làm gì**, các cột với giải thích ngắn, một hàng ví dụ
> lấy từ DP-01, và ⚠ **danh mục kiểm trước khi coi là xong**.

---

> ⭐ **Nguyên tắc chung cho cả mười một biểu mẫu: một biểu mẫu phải điền được trong thời gian hợp
> lý, nếu không nó sẽ không được điền.**
>
> Nếu bạn thấy một cột không bao giờ dùng tới, bỏ cột đó đi. ⚠ Một biểu mẫu bị bỏ trống hoàn toàn tệ
> hơn một biểu mẫu đơn giản được điền đầy đủ.

---

## C.1 Bảng I/O

⭐ **Dùng để:** làm tài liệu nền của cả dự án — đầu vào cho sơ đồ điện, đánh số dây, chương trình, HMI
và hồ sơ bàn giao. ⚠ **Làm trước khi đấu tủ** (Chương 23, 49).

| Tag | Mô tả | Loại thiết bị | NO/NC | PNP/NPN | Trạng thái nghỉ | Địa chỉ | Số dây | Cầu đấu | Ghi chú |
|---|---|---|---|---|---|---|---|---|---|
| `DI_BoardStn1` | Board tới vị trí trạm keo | Quang thu-phát | NO | PNP | 0 | %I0.3 | 214 | X2:14 | Ví dụ DP-01 |
| | | | | | | | | | |

| Cột | Vì sao có |
|---|---|
| ⭐ **Tag** | Tên dùng trong chương trình — **phải giống nhãn HMI và khớp số dây** |
| NO/NC | ⚠ Quyết định logic; tín hiệu an toàn quan trọng dùng **NC** |
| PNP/NPN | ⭐ Sai cái này thì module không nhận dù cảm biến sáng đèn |
| Trạng thái nghỉ | Giá trị khi máy đứng yên — ⭐ dùng khi kiểm tra I/O |
| ⭐ **Số dây · Cầu đấu** | ⭐⭐ Nối bảng này với tủ thật — thứ giúp đi từ triệu chứng tới sợi dây |

> ⚠ **Trước khi coi là xong:**
>
> - [ ] Mỗi tag có **một** ý nghĩa, không kiêm nhiệm
> - [ ] Đã chừa **20 % kênh dự phòng** trên mỗi module
> - [ ] Tín hiệu an toàn đã tách riêng và đánh dấu rõ
> - [ ] ⭐ Số dây khớp sơ đồ điện **và** khớp nhãn trong tủ
> - [ ] Đã kiểm dòng tổng qua chân chung của từng module ngõ ra

---

## C.2 Bảng tag nội bộ

⭐ **Dùng để:** đặt tên biến trong chương trình một cách nhất quán, để người sau đọc được (Chương 24).

| Tag | Kiểu | Ý nghĩa | Ai ghi | Ai đọc | Giữ qua mất điện | Ghi chú |
|---|---|---|---|---|---|---|
| `Stn1_Step` | INT | Bước hiện tại trạm 1 | Khối trạm 1 | HMI, chẩn đoán | Không | Ví dụ DP-01 |
| `Cnt_GoodTotal` | ⭐ DINT | Tổng board đạt | Khối thống kê | HMI, MES | ⭐ **Có** | ⚠ DINT để không tràn |
| | | | | | | |

> ⭐⭐ **Cột "Ai ghi" là cột giá trị nhất và hay bị bỏ.** Một bit được ghi ở hai chỗ khác nhau là
> nguồn của những lỗi khó nhất — bit nhấp nháy, hoặc không bao giờ giữ được trạng thái.
>
> ⭐ Quy tắc: **mỗi biến có đúng một nơi ghi.** Nếu bảng này có hai tên ở cột "Ai ghi", đó là một
> thiết kế cần xem lại.

> ⚠ **Trước khi coi là xong:**
>
> - [ ] Mọi bộ đếm tích luỹ dùng **DINT**, không phải INT
> - [ ] Mọi biến cần giữ qua mất điện đã đánh dấu — ⚠ **và đã thử nạp lại chương trình để kiểm**
> - [ ] Không biến nào có hai nơi ghi

---

## C.3 Đặc tả trình tự

⭐ **Dùng để:** mô tả máy làm gì, theo thứ tự nào, và chuyển bước khi nào (Chương 21, 23).

| Bước | Hành động | Điều kiện chuyển tiếp | Hết giờ | Nếu hết giờ thì | Ghi chú |
|---|---|---|---|---|---|
| S1.40 | Nâng kẹp board | `DI_Clamp1Up` = 1 | 2 s | Báo lỗi 3041, dừng trạm 1 | Ví dụ DP-01 |
| | | | | | |

> ⭐⭐ **Cột "Điều kiện chuyển tiếp" phải là TÍN HIỆU PHẢN HỒI THẬT, không phải bộ định thời.**
>
> Cột "Hết giờ" chỉ để **báo lỗi**. Nếu hai cột này giống nhau — chuyển bước bằng chính bộ định thời
> — thì máy **không biết khi cơ cấu không tới nơi**, và nó sẽ chạy tiếp như thể mọi thứ ổn
> (Chương 21).

> ⚠ **Trước khi coi là xong:**
>
> - [ ] ⭐ Mọi bước có điều kiện chuyển tiếp là **phản hồi thật**
> - [ ] Mọi bước có thời gian hết giờ và **hành động khi hết giờ**
> - [ ] Đã mô tả điều gì xảy ra khi **dừng giữa bước này**
> - [ ] ⚠ Đã kiểm: bước nào chạm mối nguy thì **thứ tự đã qua phân tích**, không tuỳ ý

---

## C.4 Bảng chuyển trạng thái

⭐ **Dùng để:** mô tả các chế độ của máy và điều kiện chuyển giữa chúng (Chương 25).

| Từ trạng thái | Sự kiện | Điều kiện | Sang trạng thái | Việc phải làm khi chuyển |
|---|---|---|---|---|
| Idle | Nhấn Start | Đủ điều kiện cho phép chạy | Running | Bật đèn xanh, ghi log |
| Running | Bất kỳ lỗi nào | — | Alarm | ⭐ Dừng an toàn, giữ vị trí, báo động |
| | | | | |

> ⭐ **Bảng này bắt được một lỗi thiết kế mà sơ đồ trạng thái không bắt được: trạng thái nào KHÔNG có
> đường ra.**
>
> Đọc cột "Từ trạng thái" — nếu một trạng thái không xuất hiện ở cột đó, ⚠ **máy vào đó rồi không ra
> được**.

> ⚠ **Trước khi coi là xong:**
>
> - [ ] Mọi trạng thái đều có **ít nhất một đường ra**
> - [ ] ⚠⚠ Sau khi mất điện rồi có lại, máy **KHÔNG tự vào Running**
> - [ ] Chuyển sang Alarm mô tả rõ **cơ cấu nào dừng thế nào**
> - [ ] Đã mô tả chuyển Manual ↔ Auto — ⭐ **không giật**

---

## C.5 Bảng công thức sản phẩm

⭐ **Dùng để:** tách tham số sản phẩm khỏi logic, để đổi hàng không phải sửa chương trình
(Chương 32).

| Tham số | Đơn vị | Kiểu | ⭐ Dải hợp lệ | Giá trị mặc định | Dùng ở bước | Ai được sửa |
|---|---|---|---|---|---|---|
| Thời gian sấy UV | s | REAL | ⭐ **5 – 120** | 8,0 | S2.40 | Kỹ thuật |
| Nhiệt độ keo đặt | °C | REAL | 20 – 60 | 45,0 | S1.50 | Kỹ thuật |
| | | | | | | |

> ⭐⭐ **Cột "Dải hợp lệ" là hàng rào bảo vệ máy khỏi dữ liệu sai — và nó thuộc về chương trình PLC,
> không phải thuộc về hệ thống cấp trên.**
>
> Nếu công thức tải từ MES có nhiệt độ 600 °C do lỗi nhập liệu, ⚠ **máy phải từ chối và báo lỗi**.
> Tin rằng "MES đã kiểm rồi" là cách để một lỗi nhập liệu trở thành một đám cháy.

> ⚠ **Trước khi coi là xong:**
>
> - [ ] ⭐ Mọi tham số có dải hợp lệ, và chương trình **thực sự kiểm**
> - [ ] Đã quyết: công thức sai thì **từ chối chạy**, không phải "kẹp về biên"
> - [ ] Có phân quyền: ai được sửa tham số nào
> - [ ] ⭐ Công thức **nằm trong bộ sao lưu** (Phụ lục J, Chương 54)

---

## C.6 Biên bản kiểm I/O một–một

⭐ **Dùng để:** xác nhận từng kênh I/O đấu đúng chỗ — ⚠ **bằng cách tác động thật**, không tin sơ đồ
(Chương 50, 52, 56).

| Tag | Cách tác động | Kỳ vọng | Kết quả | Người kiểm | Ngày |
|---|---|---|---|---|---|
| `DI_BoardStn1` | Đặt board vào vị trí trạm 1 | Bit lên 1 | ☐ Đạt ☐ Không | | |
| `DO_Clamp1Vlv` | ⚠ Cưỡng bức ngõ ra ở chế độ tay | Kẹp nâng, `DI_Clamp1Up` lên | ☐ Đạt ☐ Không | | |
| | | | | | |

> ⚠⚠ **Với ngõ ra: cưỡng bức làm cơ cấu chuyển động THẬT.**
>
> Chỉ làm khi: đã **cô lập năng lượng cho phần không cần thử**, đã kiểm tra **không có ai trong vùng
> nguy hiểm**, và có **người thứ hai** (Chương 3, 6).

> ⚠ **Trước khi coi là xong:**
>
> - [ ] ⭐ **Mọi kênh** đã kiểm, kể cả kênh dự phòng đã đấu dây
> - [ ] Kênh nào đấu dây mà chương trình không dùng — đã **giải thích được vì sao**
> - [ ] ⚠ Chức năng an toàn **không kiểm bằng biểu mẫu này** — dùng C.8

---

## C.7 Danh sách ca kiểm thử

⭐ **Dùng để:** kiểm thử có hệ thống thay vì "chạy thử xem sao" (Chương 50, 52).

| # | Ca kiểm | Cách tạo tình huống | Kỳ vọng | Kết quả | Ngày |
|---|---|---|---|---|---|
| 1 | Chu trình bình thường | Chạy 10 board liên tục | 10 board đạt, chu kỳ ≤ 12 s | | |
| 2 | ⚠ **Mất khí giữa chu trình** | Đóng van khí chính khi board đang kẹp | ⭐ Dừng an toàn, **giữ kẹp**, báo rõ | | |
| 3 | ⚠ **Mất điện rồi có lại** | Cắt nguồn khi đang chạy | ⚠⚠ **KHÔNG tự khởi động lại** | | |
| 4 | Mất mạng với MES | Rút cáp mạng | ⭐ Máy **vẫn chạy**, đệm dữ liệu | | |
| 5 | Công thức ngoài dải | Nạp công thức có nhiệt độ 600 °C | Từ chối, báo rõ thiếu/sai gì | | |
| | | | | | |

> ⭐⭐ **Ca 2–5 là nhóm "tình huống xấu" — mức kiểm thử bị bỏ nhiều nhất và quan trọng nhất.**
>
> Máy chạy tốt khi mọi thứ đúng là điều dễ đạt. ⭐ **Cách nó cư xử khi có sự cố mới là thứ quyết định
> nó có dùng được không** (Chương 57 mục 57.8).

> ⚠ **Trước khi coi là xong:**
>
> - [ ] Có ca cho **mọi tình huống xấu** đã liệt kê ở đặc tả
> - [ ] Có ca cho **mỗi báo động** — báo động chưa từng thấy xuất hiện là báo động chưa được kiểm
> - [ ] ⭐ Kết quả đã **ghi lại**, không chỉ "đã chạy thử rồi"

---

## C.8 ⚠ Biên bản nghiệm thu chức năng an toàn

⚠⚠ **Biểu mẫu này khác các biểu mẫu khác: nó là hồ sơ pháp lý, không phải ghi chép nội bộ.**

⭐ **Dùng để:** ghi lại việc từng chức năng an toàn đã được kiểm và đạt (Chương 48).

| SF | Chức năng | Cách kiểm | Kỳ vọng | Kết quả | Người kiểm | Ngày |
|---|---|---|---|---|---|---|
| SF1 | Dừng khẩn cấp | Nhấn từng nút E-Stop khi máy đang chạy | Mọi chuyển động dừng theo loại đã thiết kế | ☐ Đạt | | |
| SF2 | ⚠ Đèn UV tắt khi mở cửa | Mở cửa buồng UV khi đèn đang bật | ⭐ Đèn tắt **qua mạch an toàn**, không qua PLC | ☐ Đạt | | |
| SF5 | Không tự khởi động lại | Cắt và cấp lại nguồn khi đang chạy | ⚠⚠ Máy **không tự vào Running** | ☐ Đạt | | |
| | | | | | | |

> ⚠⚠ **Yêu cầu bắt buộc với biểu mẫu này:**
>
> | Yêu cầu | |
> |---|---|
> | ⭐ **Kiểm từng thiết bị riêng lẻ**, không kiểm gộp | Ba nút E-Stop phải thử **cả ba** |
> | ⭐ Ghi **mã kiểm tra** của chương trình an toàn tại thời điểm nghiệm thu | Chương 54 |
> | ⚠ Người kiểm phải là **người có thẩm quyền** | Không phải người viết chương trình tự nghiệm thu |
> | ⚠⚠ **Mọi thay đổi sau này chạm phần an toàn → kiểm lại** | Chương 53 mục 53.3 |
>
> ⚠ **Biểu mẫu này không thay thế đánh giá rủi ro và không thay thế kiểm định theo quy định hiện
> hành.** Xem Chương 6, 47, 48.

---

## C.9 Phiếu bàn giao

⭐ **Dùng để:** đảm bảo không thiếu thứ gì khi giao máy — và để người sau bạn làm việc được
(Chương 52, 53, 54).

| # | Hạng mục | Có | Ghi chú |
|---|---|---|---|
| 1 | Đặc tả chức năng (bản cuối, khớp máy thật) | ☐ | |
| 2 | ⚠ Hồ sơ đánh giá rủi ro + biên bản nghiệm thu an toàn (C.8) | ☐ | |
| 3 | Sơ đồ điện **as-built** | ☐ | ⚠ Đã sửa theo thực tế |
| 4 | Bảng I/O khớp số dây (C.1) | ☐ | |
| 5 | ⭐ Chương trình PLC **có chú thích** | ☐ | |
| 6 | ⭐⭐ **Bộ sao lưu bảy hạng mục** | ☐ | Xem bên dưới |
| 7 | ⭐ **Quy trình khôi phục một trang** | ☐ | ⚠ Đã thử ít nhất một lần |
| 8 | Hướng dẫn vận hành và xử lý báo động | ☐ | |
| 9 | Danh mục vật tư + phụ tùng khuyến nghị | ☐ | |
| 10 | ⭐ **Mốc đo lúc nghiệm thu** | ☐ | Xem bên dưới |
| 11 | Sổ nhật ký thay đổi (để trống, treo trong tủ) | ☐ | |
| 12 | Biên bản đào tạo người vận hành | ☐ | |

### ⭐ Bộ sao lưu bảy hạng mục (mục 6)

| # | Hạng mục | Có |
|---|---|---|
| 1 | Dự án PLC — kèm chú thích và tên biến | ☐ |
| 2 | Cấu hình phần cứng | ☐ |
| 3 | ⭐ **Tham số biến tần / servo driver** | ☐ |
| 4 | Dự án HMI / SCADA | ☐ |
| 5 | Công thức và tham số sản phẩm | ☐ |
| 6 | ⚠⚠ Chương trình + cấu hình thiết bị an toàn, **kèm mã kiểm tra** | ☐ |
| 7 | Cấu hình mạng — địa chỉ, tên trạm, tệp mô tả thiết bị | ☐ |

### ⭐ Mốc đo lúc nghiệm thu (mục 10)

| Đo | Giá trị đo được | Điều kiện đo |
|---|---|---|
| Điện áp 24 V khi tải nặng nhất | ______ V | Bước nào? |
| Dòng động cơ ở tải bình thường | ______ A | |
| Số lỗi mạng sau 8 giờ chạy | ______ | |
| Chu kỳ máy thật | ______ s | Mã hàng nào? |
| Thời gian từng bước — lớn nhất | (bảng riêng) | |

> ⭐⭐ **Mốc đo là mục có tỉ lệ bị bỏ cao nhất và giá trị lâu dài lớn nhất.**
>
> Sáu tháng sau, ai đó đo được 23,1 V ở tải nặng và hỏi *"cái này có bình thường không?"*. Không có
> mốc thì không ai trả lời được. ⭐ **Mười phút lúc nghiệm thu đổi lấy khả năng trả lời câu đó suốt
> vòng đời máy.**

---

## C.10 Bảng cấu hình phần cứng

⭐ **Dùng để:** ghi lại **cái gì cắm ở đâu** — bản đồ khe cắm, địa chỉ, phiên bản. Đây là tài liệu
bạn đưa cho người đấu tủ, và là tài liệu bạn cần khi **dựng lại một CPU đã hỏng** (Chương 8 mục 8.4,
Chương 54).

> ⚠⚠ **Vì sao bảng này phải là TÀI LIỆU, không phải trí nhớ.** Với hệ đánh địa chỉ theo khe, chèn một
> module vào **giữa** rack sẽ **dịch địa chỉ của mọi module phía sau** (Chương 8 mục 8.4). ⭐ Nghĩa là
> thứ tự khe **là một phần của chương trình** — chỉ có điều nó không nằm trong tệp dự án.

### C.10.1 Bản đồ khe cắm

| Rack·Khe | Mã sản phẩm | Loại | Số kênh | Địa chỉ đầu–cuối | Dùng / Dự phòng | Firmware | Nguồn cấp | Ghi chú |
|---|---|---|---|---|---|---|---|---|
| 0·PS | | Nguồn của rack | — | — | — | — | — | |
| 0·CPU | | CPU | — | — | — | | | Ghi mã **thẻ nhớ** và **pin** ở đây |
| 0·1 | | DI 16 kênh | 16 | `%I0.0`–`%I1.7` | 13 / 3 | | PSU1 | ⭐ **Sink**, chân chung 0 V |
| 0·2 | | DO transistor 16 kênh | 16 | `%Q0.0`–`%Q1.7` | 11 / 5 | | PSU1 | ⚠ Tổng dòng chân chung: ___ A |
| 0·3 | | AI 4 kênh | 4 | `%IW64`–`%IW71` | 3 / 1 | | PSU1 | 4–20 mA, **nguồn do module cấp** |
| 0·4 | | AO 2 kênh | 2 | `%QW80`–`%QW83` | 2 / 0 | | PSU1 | 0–10 V |
| 0·5 | *(để trống)* | — | — | — | — | — | — | ⭐ Khe dự phòng — ⚠ **phải ở CUỐI** |
| | | | | | | | | |

| Cột | Vì sao có |
|---|---|
| **Rack·Khe** | ⭐ Thứ tự khe quyết định địa chỉ — đây là cột không được sai |
| **Mã sản phẩm** | ⭐⭐ Mã **đầy đủ kèm hậu tố**; hai module khác nhau ở một chữ cái cuối có thể khác cả kiểu ngõ ra |
| ⭐ **Dùng / Dự phòng** | ⚠ Cột trả lời câu *"còn chỗ không"* mà không phải mở tủ. Mục tiêu: **≥ 20 % dự phòng** (Chương 13 mục 13.2) |
| ⭐⭐ **Firmware** | ⚠ Thay module cùng mã nhưng **khác phiên bản firmware** có thể đổi hành vi. Ghi lúc nghiệm thu, không ghi sau |
| **Nguồn cấp** | Module này ăn từ nhánh 24 V nào — ⭐ cần khi tính phụ tải và khi tìm nguyên nhân sụt áp (Chương 8 mục 8.7, Chương 49 mục 49.5) |
| **Ghi chú** | ⭐ Nơi ghi **kiểu đấu sink/source đã chọn** — thứ không nhìn ra được từ hình dáng module (Chương 9, Hình 9.1) |

### C.10.2 Thiết bị trên mạng

| Tên thiết bị | Vai trò | Giao thức | Địa chỉ / trạm | Tệp mô tả thiết bị | Phiên bản | Ghi chú |
|---|---|---|---|---|---|---|
| `NET_Scanner` | Đầu đọc mã 2D | Ethernet | | | | Ví dụ DP-01 |
| `NET_TempCtrl` | Bộ điều khiển nhiệt keo | RS-485, Modbus RTU | Trạm ___ | — | | ⭐ Tốc độ baud, chẵn lẻ, bit dừng |
| `NET_Drives` | 3 servo drive | Ethernet công nghiệp | | | | |
| | | | | | | |

> ⭐ **Cột "Tệp mô tả thiết bị" là cột hay bị bỏ và tốn nhất khi thiếu.** ⚠ Không có đúng tệp và đúng
> phiên bản thì **không dựng lại được cấu hình mạng** trên một máy tính mới — mục 7 của bộ sao lưu ở
> C.9 đòi chính thứ này.

### ⭐⭐ Yêu cầu với kết quả — bảng này đạt khi

> ⚠ **Trước khi coi là xong:**
>
> - [ ] ⭐ **Mọi khe đều có một dòng**, kể cả khe trống — khe trống cũng là thông tin
> - [ ] Khe dự phòng nằm ở **cuối** rack, không nằm giữa (Chương 8 mục 8.4)
> - [ ] Mỗi module ngõ ra có **tổng dòng qua chân chung** đã tính và ghi (Chương 9 Bẫy 1)
> - [ ] Kiểu **sink / source** đã chọn được ghi rõ — ⚠ và **cũng đã ghi lên nhãn trong tủ**
> - [ ] Dải địa chỉ trong bảng này **khớp cột "Địa chỉ" của C.1**, không sai một kênh
> - [ ] ⭐ Phiên bản firmware của CPU và mọi module đã ghi, **ghi lúc nghiệm thu**
> - [ ] Còn **≥ 20 %** kênh dự phòng trên mỗi loại module
> - [ ] Bảng này đã nằm trong bộ sao lưu (C.9, mục 2 của bộ bảy hạng mục)

> ⭐⭐ **Phép thử một phút.** Đưa bảng cho một người **chưa từng mở tủ này**, hỏi:
> *"tín hiệu `DI_BoardStn1` vào module nào, khe mấy, kênh mấy?"* ⚡ Trả lời được trong một phút
> thì bảng đạt. ⚠ Phải mở tủ ra đếm mới biết thì bảng chưa đạt — và **sáu tháng nữa nó sẽ vô dụng**.

---

## C.11 Danh mục vật tư

⭐ **Dùng để:** đặt hàng, đối chiếu khi nhận hàng, đối chiếu nhãn khi nghiệm thu đấu tủ, và **quyết
định mua phụ tùng dự phòng** (Chương 49 mục 49.10, Chương 52, Phụ lục D).

> ⭐⭐ **Nguyên tắc quan trọng nhất của biểu mẫu này: ĐỪNG viết nó như một tài liệu độc lập.**
>
> Mọi dòng phải **sinh ra từ** bảng I/O (C.1) hoặc bảng cấu hình phần cứng (C.10). ⚠ Viết tay một
> danh mục riêng nghĩa là có **ba tài liệu nói về cùng một cỗ máy**, và chúng sẽ lệch nhau trong
> vòng một tháng. ⚡ Cột *"Sinh từ"* tồn tại để chuyện đó không xảy ra âm thầm.

| Mã hãng | Mô tả | SL | Vị trí lắp | ⭐ Sinh từ | Thời gian có hàng | Phụ tùng khuyến nghị | Ghi chú |
|---|---|---|---|---|---|---|---|
| | CPU | 1 | Rack 0 · CPU | C.10 | | 0 | ⚠ Đặt khi hỏng — xem ghi chú dưới |
| | Module DI 16 kênh | 1 | Rack 0 · khe 1 | C.10 | | ⭐ 1 | |
| | Cảm biến quang thu-phát PNP | 4 | `DI_BoardStn1`, … | ⭐ **C.1** | | ⭐ 2 | Loại hay hỏng nhất |
| | Van khí 5/2 lò xo về, 24 VDC | 4 | `DO_Clamp1Vlv`, … | ⭐ **C.1** | | 1 | ⚠ Kèm diode dập |
| | Nguồn 24 V ___ A | 1 | Tủ, ray DIN | Phép tính §8.7 | | 1 | Đã nhân hệ số 1,3–1,5 |
| | Rơ-le an toàn | 1 | Tủ | ⚠ Hồ sơ rủi ro | | 0 | ⚠⚠ Đổi là phải đánh giá lại |
| | | | | | | | |

| Cột | Vì sao có |
|---|---|
| **Mã hãng** | ⚠ Mã **đầy đủ**, gồm cả hậu tố điện áp và kiểu ngõ ra |
| **Vị trí lắp** | ⭐ Với thiết bị trường thì ghi **tag**, không ghi "trạm 1" — tag mới truy ngược được |
| ⭐⭐ **Sinh từ** | Dòng này đến từ bảng nào. ⚠ Dòng **không sinh từ đâu cả** là dòng đáng ngờ — hoặc thiếu trong C.1, hoặc thừa trong đơn hàng |
| ⭐ **Thời gian có hàng** | ⚠ Là tiêu chí số 9 ở bảng công tác §13.4 — **hay để trống nhất, và đau nhất**. Ghi bằng **tuần**, không ghi "có sẵn" |
| ⭐ **Phụ tùng khuyến nghị** | C.9 mục 9 đòi cột này khi bàn giao. ⭐ Quy tắc chọn: xem bảng dưới |

### ⭐ Chọn phụ tùng dự phòng — ba câu hỏi, không phải cảm tính

| Câu hỏi | Nếu "có" thì |
|---|---|
| Hỏng cái này thì máy **dừng hẳn** không? | ⭐ Nghiêng về có dự phòng |
| ⭐ **Thời gian có hàng dài hơn mức dừng máy chấp nhận được** không? | ⭐⭐ **Bắt buộc có dự phòng** — đây là câu quyết định |
| Nó là loại **hao mòn theo số lần tác động** không? | ⭐ Dự phòng theo số lượng, không phải một cái |

> ⭐⭐ **Câu thứ hai là câu duy nhất thật sự quyết định, và nó là một phép so sánh, không phải cảm
> tính.** ⚡ Một module rẻ mà **giao hàng tám tuần** đáng dự phòng hơn một CPU đắt **có sẵn trong
> nước ngày mai**. ⚠ Phần lớn danh mục phụ tùng bị lập ngược: theo giá, không theo thời gian chờ.

> ⚠ **Thiết bị an toàn là trường hợp riêng.** ⭐ Dự phòng một rơ-le an toàn **không** nghĩa là thay
> vào là chạy: đổi thiết bị trong chuỗi an toàn thường kéo theo **đánh giá lại và nghiệm thu lại**
> chức năng đó (Chương 47, 48, biểu mẫu C.8). ⭐ Ghi rõ điều này vào cột ghi chú, ngay từ lúc lập
> danh mục — để người mua hàng sáu tháng sau **không tự ý đổi sang mã tương đương**.

### ⭐⭐ Yêu cầu với kết quả — danh mục này đạt khi

> ⚠ **Trước khi coi là xong:**
>
> - [ ] ⭐ **Mọi dòng có cột "Sinh từ" điền đầy đủ** — không dòng nào mồ côi
> - [ ] Ngược lại: ⭐⭐ **mọi thiết bị trường trong C.1 đều tìm được một dòng ở đây**
> - [ ] Mọi module trong C.10 đều có mặt, kèm **nguồn của rack** và **thẻ nhớ / pin**
> - [ ] ⚠ Có cả những thứ **không nối vào PLC** nhưng cần cho an toàn (Chương 48) — che chắn, khoá cửa, biển báo
> - [ ] **Thời gian có hàng** điền bằng **tuần** cho mọi dòng, không bỏ trống dòng nào
> - [ ] Cột phụ tùng đã trả lời **ba câu hỏi** ở bảng trên, không chọn theo giá
> - [ ] ⚠⚠ Thiết bị thuộc chuỗi an toàn đã **đánh dấu rõ là không được đổi mã tự do**
> - [ ] Yêu cầu vật liệu đặc biệt (ví dụ vật liệu tiêu tán tĩnh điện) đã ghi **ở đây và trên bản vẽ** (Chương 7)

> ⭐⭐ **Phép thử một phút.** Chọn ngẫu nhiên **ba dòng bất kỳ trong bảng I/O**, rồi hỏi:
> *"thiết bị này mã gì, mua ở đâu, bao lâu có hàng, có dự phòng trong kho không?"* ⚡ Trả lời được
> cả ba dòng thì danh mục đạt. ⚠ Chỉ cần một dòng không trả lời được, ⭐ **danh mục đang thiếu đúng
> chỗ nó sẽ được cần tới** — vì người ta chỉ mở nó ra lúc có thứ hỏng.

---

## C.12 Cách dùng bộ biểu mẫu này

| Giai đoạn dự án | Biểu mẫu | Chương |
|---|---|---|
| Đặc tả | C.3 · C.4 · C.5 | 23, 25, 32 |
| Bảng I/O | ⭐ **C.1** | 23 |
| ⭐ **Chọn và cấu hình phần cứng** | ⭐ **C.10** | 8, 13 |
| ⭐ **Đặt hàng & nhận hàng** | ⭐ **C.11** | 13, 49 |
| Viết chương trình | C.2 | 22 |
| Kiểm thử | C.6 · C.7 | 50, 52 |
| ⚠ Nghiệm thu an toàn | ⚠ **C.8** | 48 |
| Bàn giao | ⭐ **C.9** | 52, 54 |

> ⭐ **Thứ tự trên là thứ tự của Chương 57.** Nếu bạn đang điền C.1 sau khi tủ đã đấu xong, ⚠ **bạn
> đang làm sai thứ tự** — và hậu quả là số dây không khớp tên tag, trả giá suốt vòng đời máy.

> ⚠⚠ **Giới hạn.** Các biểu mẫu ở đây là **điểm khởi đầu**, không phải chuẩn bắt buộc. Cơ sở của bạn
> có thể có mẫu riêng — dùng mẫu của họ. Nếu máy thuộc ngành có quản lý chặt (dược phẩm, thực phẩm,
> hàng không, y tế), ⚠ **yêu cầu hồ sơ nghiêm ngặt hơn nhiều** so với bộ này; hỏi bộ phận chất lượng
> trước.
>
> ⚠ Riêng **C.8 không thay thế** đánh giá rủi ro, kiểm định, hay yêu cầu pháp lý hiện hành tại thị
> trường của bạn.
