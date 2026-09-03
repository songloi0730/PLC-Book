
# Phụ lục C — Biểu mẫu dùng ngay

> **Chín biểu mẫu trống, chép ra dùng được cho dự án của bạn.**
>
> Mỗi biểu mẫu có: ⭐ **một dòng nói nó dùng để làm gì**, các cột với giải thích ngắn, một hàng ví dụ
> lấy từ DP-01, và ⚠ **danh mục kiểm trước khi coi là xong**.

---

> ⭐ **Nguyên tắc chung cho cả chín biểu mẫu: một biểu mẫu phải điền được trong thời gian hợp lý, nếu
> không nó sẽ không được điền.**
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

## C.10 Cách dùng bộ biểu mẫu này

| Giai đoạn dự án | Biểu mẫu | Chương |
|---|---|---|
| Đặc tả | C.3 · C.4 · C.5 | 23, 25, 32 |
| Bảng I/O & phần cứng | ⭐ **C.1** | 23 |
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
