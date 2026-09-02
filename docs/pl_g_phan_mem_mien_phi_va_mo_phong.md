
# Phụ lục G — Phần mềm miễn phí & mô phỏng

> **Bạn học được PLC mà không cần mua PLC.** Phụ lục này nói học bằng gì.

---

> ⚠⚠ **ĐỌC TRƯỚC — giới hạn của phụ lục này**
>
> ⭐ **Điều kiện bản quyền của phần mềm THAY ĐỔI THƯỜNG XUYÊN.** Một công cụ miễn phí năm nay có thể
> đổi sang thu phí năm sau; một bản dùng thử 30 ngày có thể thành 21 ngày; giới hạn số tag có thể đổi.
>
> ⚠ Vì vậy phụ lục này **cố ý KHÔNG liệt kê điều kiện bản quyền cụ thể**. Nó cho bạn:
>
> - ⭐ **biết công cụ nào tồn tại** và mỗi loại làm được gì;
> - ⭐ **danh mục câu hỏi phải tự kiểm** trước khi dùng (G.5);
> - ⚠ **cảnh báo về những chỗ dễ vi phạm bản quyền mà không biết**.
>
> ⭐⭐ **Trước khi tải hoặc dùng bất kỳ công cụ nào: tự đọc điều khoản trên trang chính thức của nhà
> sản xuất, và ghi lại ngày bạn kiểm.** Đừng tin bảng nào — kể cả bảng này.

---

## G.1 ⭐ Bốn loại công cụ, và bạn cần loại nào

| Loại | Làm được gì | Khi nào cần |
|---|---|---|
| 1 — **Phần mềm lập trình của hãng** | Viết chương trình cho PLC của hãng đó | ⭐ **Ngay từ đầu** — chọn một hãng và thành thạo nó |
| 2 — **Mô phỏng PLC** | Chạy chương trình **không cần phần cứng** | ⭐ Ngay từ đầu, đi kèm loại 1 |
| 3 — **Mô phỏng máy 3D** | Dựng máy ảo để chương trình điều khiển | ⭐⭐ Khi muốn có **video làm bằng chứng** (Ch.58) |
| 4 — **Phần cứng rẻ** | PLC cũ, bộ kit học tập | Khi muốn trải nghiệm phần cứng thật |

> ⭐⭐ **Loại 1 + 2 là đủ để đi hết mức 4 của Phụ lục I.** Đừng chờ có phần cứng mới bắt đầu — phần lớn
> việc học nằm ở tư duy logic, và tư duy đó rèn được hoàn toàn trên mô phỏng.

---

## G.2 Phần mềm lập trình — theo hãng

⚠ **Cột "Ghi chú" mô tả tính chất chung, KHÔNG phải điều kiện bản quyền hiện hành.** Kiểm theo G.5.

| Hãng | Phần mềm | Ghi chú |
|---|---|---|
| **Siemens** | TIA Portal | ⭐ Phổ biến rất rộng ở châu Âu và Việt Nam; ⚠ có nhiều phiên bản với phạm vi khác nhau |
| **Mitsubishi** | GX Works | ⭐ Phổ biến trong ngành điện tử và ô tô ở châu Á |
| **Rockwell / Allen-Bradley** | Studio 5000 · Connected Components Workbench | ⭐ Chiếm ưu thế ở Bắc Mỹ |
| **Omron** | Sysmac Studio · CX-Programmer | |
| **Schneider** | EcoStruxure Control Expert · Machine Expert | Nền CODESYS cho dòng máy |
| **Delta** | ISPSoft · WPLSoft | ⭐ Thường gặp ở phân khúc máy vừa và nhỏ |
| **Inovance** | AutoShop · InoProShop | ⭐ Xuất hiện nhiều ở Việt Nam những năm gần đây |
| **Beckhoff** | TwinCAT | Chạy trên PC, hướng IEC mạnh |
| ⭐ **CODESYS** (không thuộc một hãng máy) | CODESYS Development System | ⭐⭐ **Đáng chú ý nhất cho người học** — xem bên dưới |

### ⭐⭐ Vì sao CODESYS đáng chú ý riêng

| Lý do | |
|---|---|
| ⭐ **Bám IEC 61131-3 sát nhất** | Học ở đây thì kiến thức **chuyển được** sang hãng khác |
| Nhiều hãng dùng nó làm nền | Một số dòng PLC của Schneider, Wago, Festo, Bosch Rexroth và nhiều hãng khác |
| Có mô phỏng tích hợp | Chạy chương trình không cần phần cứng |
| ⭐ Là **cột neo của Phụ lục A** | Khi bốn hãng khác làm khác nhau, cột CODESYS cho biết **chuẩn IEC nói gì** |

> ⭐ **Gợi ý thực dụng cho người mới:** học **một** phần mềm của hãng phổ biến ở nơi bạn định làm việc,
> **và** làm quen CODESYS để hiểu chuẩn gốc. Hai thứ bổ trợ nhau: một cái cho bạn việc làm, một cái
> cho bạn khả năng chuyển nền.

---

## G.3 Mô phỏng máy

| Loại | Làm được gì | Ghi chú |
|---|---|---|
| ⭐ **Mô phỏng PLC tích hợp** | Chạy logic, xem bit, ép giá trị | ⭐ Hầu hết phần mềm hãng đều có; ⚠ **kiểm xem bản bạn có bao gồm nó không** |
| ⭐⭐ **Mô phỏng máy 3D** | Dựng băng tải, xy-lanh, cảm biến ảo; ⭐ **nối với PLC mô phỏng** | ⭐ Cho video thuyết phục nhất (Ch.58 mục 58.3) |
| **Mô phỏng nhà máy dạy học** | Các bài toán dựng sẵn (băng tải, phân loại, thang máy) | ⭐ Hợp với Phụ lục I mức 3–5 |
| **Mô phỏng HMI** | Chạy màn hình vận hành không cần panel | Ch.44 |

> ⭐⭐ **Mô phỏng máy 3D là khoản đầu tư thời gian đáng giá nhất cho người chưa có kinh nghiệm.**
>
> Nó biến "tôi biết lập trình PLC" thành ⭐ **một video 60 giây cho người ta thấy máy chạy** — và một
> video như vậy nói được nhiều hơn một trang hồ sơ (Chương 58).

### ⚠ Điều mô phỏng KHÔNG dạy được

| Mô phỏng không có | Hậu quả |
|---|---|
| ⚠ Nhiễu điện, vòng lặp đất, cáp gãy lõi | ⭐ **Cả Chương 49 không rèn được trên mô phỏng** |
| Cơ cấu kẹt, van bẩn, cảm biến lệch | Chương 51 |
| ⚠⚠ **Cảm giác về hậu quả thật** | Mô phỏng không làm ai bị thương — ⚠ **máy thật thì có** |
| Sụt áp, quá tải nguồn | Chương 8 |
| Áp lực khi cả chuyền đang chờ | Chương 52 |

> ⭐⭐ **Điều quan trọng nhất mô phỏng không dạy được là ý thức về hậu quả.** Trên mô phỏng, một lỗi
> chỉ là một dòng đỏ. Trên máy thật, cùng lỗi đó có thể là một cơ cấu chuyển động khi có người đứng
> cạnh.
>
> ⚠ Khi chuyển từ mô phỏng sang máy thật, **hãy giả định mình chưa biết gì về an toàn** và đọc lại
> Chương 3, 6, 47.

---

## G.4 Phần cứng rẻ để học

| Cách | Ưu | ⚠ Nhược |
|---|---|---|
| ⭐ **PLC cũ mua lại** | Rẻ; ⭐ trải nghiệm phần cứng thật | ⚠ Có thể không còn phần mềm hỗ trợ; ⚠ **kiểm nguồn gốc** |
| Bộ kit học tập của hãng | Đầy đủ, có tài liệu | Đắt hơn |
| PLC phân khúc nhỏ đời mới | Rẻ, phần mềm còn hỗ trợ | Ít tính năng nâng cao |
| ⚠ Bộ điều khiển không phải PLC (vi điều khiển) | Rất rẻ | ⚠⚠ **Không dạy được cách nghĩ của PLC** — vòng quét, ảnh I/O, độ tin cậy |

> ⚠ **Hàng cuối đáng nói rõ.** Một bo mạch vi điều khiển rẻ tiền chạy được logic — nhưng nó **không
> có** vòng quét, ảnh ngõ vào, hay các đặc tính độ tin cậy công nghiệp. Học trên đó thì bạn học lập
> trình nhúng, ⚠ **không phải học PLC**.
>
> ⭐ Nó vẫn hữu ích cho việc khác (mô phỏng thiết bị ngoại vi, tạo tín hiệu thử), nhưng đừng nhầm nó
> là bước đệm để học PLC.

> ⚠⚠ **Nếu bạn đấu nối phần cứng thật để học: toàn bộ Chương 3 và Phụ lục D áp dụng.** Một bàn thử
> nghiệm ở nhà vẫn có điện lưới, vẫn có cơ cấu chuyển động, và ⚠ **vẫn làm người bị thương được**.

---

## G.5 ⭐⭐ Danh mục tự kiểm trước khi dùng

⚠ **Đây là phần quan trọng nhất của phụ lục — vì nó không hết hạn.**

| # | Câu hỏi | Vì sao |
|---|---|---|
| 1 | ⭐ **Bản này miễn phí hay dùng thử?** Bao lâu? | ⚠ Bản dùng thử hết hạn giữa dự án là tình huống tệ |
| 2 | ⭐⭐ **Có được dùng cho mục đích thương mại không?** | ⚠⚠ **Nhiều bản miễn phí CHỈ cho học tập** — dùng cho việc có trả tiền là vi phạm |
| 3 | Giới hạn gì? Số tag, số I/O, dòng sản phẩm hỗ trợ | Có thể chặn đúng thứ bạn cần |
| 4 | ⭐ **Có bao gồm mô phỏng không?** | Nếu không thì bạn cần phần cứng |
| 5 | Có yêu cầu kết nối mạng thường xuyên không? | ⚠ Máy tính tại nhà máy thường không có mạng |
| 6 | ⭐ **Chương trình viết bằng bản này có mở được bằng bản đầy đủ không?** | ⚠ Tránh làm xong rồi không chuyển giao được |
| 7 | Tải từ **trang chính thức của nhà sản xuất** chứ? | ⚠⚠ **Không tải từ nguồn không rõ** — Chương 45 |
| 8 | Chạy trên hệ điều hành nào, cần gì? | Nhiều công cụ chỉ chạy trên một nền |

> ⚠⚠ **Câu 2 là câu nhiều người vi phạm mà không biết.**
>
> Bạn học bằng bản miễn phí, rồi nhận một việc nhỏ có trả tiền, rồi dùng luôn bản đó. ⭐ **Đó thường
> là vi phạm điều khoản** — và nó là loại vi phạm lộ ra vào lúc tệ nhất: khi khách hàng hoặc chủ lao
> động cần bằng chứng về bản quyền phần mềm.
>
> ⭐ Khi chuyển từ học sang làm, ⭐ **kiểm lại điều khoản** và mua bản phù hợp nếu cần.

### ⭐ Mẫu ghi lại kết quả kiểm

| Công cụ | Phiên bản | ⭐ **Ngày kiểm** | Miễn phí / dùng thử | Cho thương mại? | Giới hạn | Nguồn tải |
|---|---|---|---|---|---|---|
| | | | | | | |
| | | | | | | |

> ⭐ **Ghi ngày kiểm là bắt buộc**, vì câu trả lời hôm nay có thể sai sau sáu tháng. Đây là cùng
> nguyên tắc với "ghi mốc đo" ở Chương 49 và Phụ lục D.6: ⭐ **một thông tin chỉ có nghĩa khi biết nó
> đúng vào lúc nào.**

---

## G.6 ⭐ Lộ trình dùng công cụ theo mốc học

Đối chiếu với bốn mốc ở Chương 58 mục 58.2:

| Mốc | Cần gì | Làm gì |
|---|---|---|
| **0 → 3 tháng** | Phần mềm hãng + mô phỏng PLC | ⭐ Phụ lục I mức 1–3 |
| **3 tháng → 1 năm** | + mô phỏng máy 3D · + phần cứng thật nếu có | ⭐ Phụ lục I mức 4–5; ⭐⭐ **quay video làm bằng chứng** |
| **1 năm → 3 năm** | + phần mềm HMI · + công cụ mạng | Dựng một máy hoàn chỉnh theo Chương 57 |
| **3 năm trở đi** | + công cụ chẩn đoán mạng · + môi trường an toàn của hãng | ⚠ Phần an toàn cần **đào tạo chính thức**, không chỉ công cụ |

---

## G.7 Dẫn về đâu

| Bạn cần | Đọc |
|---|---|
| Bài tập để làm bằng các công cụ này | ⭐ **Phụ lục I** |
| Lộ trình học và cách chứng minh năng lực | ⭐ **Chương 58** |
| Thao tác cụ thể theo giao diện từng hãng | **Phụ lục A** |
| Danh mục một máy hoàn chỉnh gồm những gì | **Chương 57** |
| ⚠ An toàn khi dùng phần cứng thật | ⚠ **Chương 3** · **Phụ lục D** |

---

> ⚠⚠ **Nhắc lại, vì đây là điều dễ bị bỏ qua nhất.**
>
> Phụ lục này **không khẳng định** bất kỳ công cụ nào hiện đang miễn phí, hay được phép dùng cho mục
> đích thương mại. ⭐ **Điều kiện bản quyền là thứ bạn phải tự kiểm tại trang chính thức của nhà sản
> xuất, mỗi lần bạn bắt đầu dùng cho một mục đích mới.**
>
> ⚠ Tải phần mềm công nghiệp từ nguồn không chính thức là rủi ro an ninh nghiêm trọng — nó là một
> trong những đường lây phổ biến vào mạng nhà máy (Chương 45).
