# Chương 45 — Kết nối lên trên: dữ liệu, MES & an ninh mạng OT

> **Lát cắt máy mẫu:** 4 — thêm mạng: mã 2D, MES, SMEMA, màn hình vận hành, và bộ điều khiển nhiệt độ
> keo nối RS-485.
>
> ⚠ **Chương này trình bày nguyên lý phòng thủ.** Nó không hướng dẫn tấn công, và không thay thế
> chuyên gia an ninh. Mục đích: để bạn **biết phải hỏi gì** và **không tự tạo ra lỗ hổng**.

---

## 45.1 Bài toán: một bảng tính làm dừng chuyền

Phòng kỹ thuật muốn theo dõi sản lượng theo thời gian thực. Ai đó viết một bảng tính đọc thẳng dữ liệu
từ PLC qua Modbus TCP — nhanh, tiện, không tốn gì.

Bảng tính được chia sẻ cho vài người. Mỗi người mở nó, mỗi bản lại hỏi PLC mỗi giây.

Một buổi chiều, năm người cùng mở. PLC nhận **năm luồng yêu cầu liên tục**. Thời gian quét tăng vọt.
Chuyển động gantry bắt đầu không đều, rồi một trục báo lỗi sai số bám.

Chuyền dừng bốn mươi phút. Nguyên nhân: **một bảng tính**.

> ⭐ Và đó mới là kịch bản **vô hại**. Cùng đường truy cập đó, một người không có ý tốt — hoặc một
> phần mềm độc hại trên máy tính văn phòng — **ghi được vào PLC**. Modbus không có xác thực
> (Chương 39, mục 39.6).

Chương này về hai việc đi liền nhau: **đưa dữ liệu lên trên cho đúng cách**, và **không mở cửa cho
thứ không nên vào**.

---

## 45.2 Ghi dữ liệu sản xuất — ghi gì

Không phải mọi thứ đều đáng ghi. Ghi quá nhiều tốn dung lượng và làm dữ liệu khó dùng; ghi quá ít thì
khi cần không có.

| Nhóm | Ví dụ | Tần suất | Giữ bao lâu |
|---|---|---|---|
| ⭐ **Theo sản phẩm** | Mã board, OK/NG, lý do NG, số liệu quá trình (Chương 42) | Mỗi board | ⭐ Lâu — theo yêu cầu truy xuất |
| **Sản lượng** | Số OK, NG, tỉ lệ, theo ca | Mỗi ca | Nhiều tháng |
| ⭐ **Xu hướng quá trình** | Nhiệt độ keo, cường độ UV, dòng chuyền, chu kỳ | Vài giây–vài phút | Vài tháng |
| **Sự kiện** | Báo động, đổi công thức, đăng nhập, cưỡng bức I/O | Khi xảy ra | Lâu |
| **Thời gian dừng máy** | Dừng vì gì, bao lâu, chờ máy trước/sau (Chương 41) | Khi xảy ra | Nhiều tháng |

> ⭐ **Hàng "xu hướng quá trình" là hàng bị đánh giá thấp nhất.**
> Nó không cần cho vận hành hằng ngày. Nhưng khi có sự cố chất lượng, một đồ thị nhiệt độ keo ba tháng
> qua trả lời được câu hỏi mà không gì khác trả lời được — và đó là cùng công cụ đã cần ở Chương 35
> mục 35.10 để chỉnh định.

### Ba câu hỏi trước khi ghi bất cứ thứ gì

> **1. Ai sẽ đọc dữ liệu này, và để trả lời câu hỏi gì?**
> Không trả lời được thì đừng ghi. Dữ liệu không ai đọc là dữ liệu tốn tiền lưu trữ.
>
> **2. Nếu không có nó, tôi mất gì?**
> Câu này lọc rất tốt. Mất số liệu chu kỳ → không phân tích được nút cổ chai. Mất số bước hiện tại của
> trình tự → không mất gì, vì nó chỉ có nghĩa ngay lúc đó.
>
> **3. Giữ bao lâu là đủ?**
> ⚠ Yêu cầu truy xuất của ngành có thể quy định thời gian tối thiểu — hỏi khách hàng.

---

## 45.3 Ghi ở đâu

```text
   PLC  ──►  HMI / SCADA  ──►  Kho dữ liệu  ──►  Báo cáo, phân tích
    │             │                  │
  đệm tạm    đệm + hiển thị     lưu dài hạn
```

| Nơi | Hợp với | ⚠ Giới hạn |
|---|---|---|
| **Trong PLC** | ⭐ Đệm tạm khi mất kết nối; vài chục bản ghi gần nhất | ⚠ Bộ nhớ rất hạn chế (Chương 8) |
| **HMI/SCADA** | Lịch sử báo động, đồ thị vài ngày | ⚠ Dung lượng vừa phải; HMI hỏng là mất |
| ⭐ **Kho dữ liệu** *(historian)* / cơ sở dữ liệu | ⭐ **Lưu dài hạn**, phân tích, báo cáo | Cần hạ tầng và người quản lý |

> ⭐ **PLC là nơi tệ nhất để lưu dữ liệu dài hạn, nhưng là nơi tốt nhất để đệm tạm.**
> Khi mất kết nối lên trên, PLC phải giữ được dữ liệu đủ lâu để gửi bù khi có lại — đó là yêu cầu ở
> Chương 42 mục 42.6. Vài chục tới vài trăm bản ghi là hợp lý; nhiều hơn thì phải xét bộ nhớ.

---

## 45.4 OPC UA và MQTT — khi nào dùng cái nào

Hai cách phổ biến để đưa dữ liệu từ tầng máy lên tầng trên.

| | **OPC UA** | **MQTT** |
|---|---|---|
| Mô hình | ⭐ **Máy khách hỏi máy chủ**, hoặc đăng ký nhận | ⭐ **Xuất bản – đăng ký** qua một máy trung gian |
| Mô tả dữ liệu | ⭐ **Tự mô tả** — có kiểu, đơn vị, cấu trúc | ⚠ Không — nội dung do bạn định nghĩa |
| Bảo mật | ⭐ **Có sẵn** — xác thực, mã hoá, phân quyền | Có, nếu cấu hình đúng |
| Độ phức tạp | Cao hơn | ⭐ Đơn giản hơn |
| Hợp với | ⭐ Trao đổi có cấu trúc với MES, SCADA | ⭐ Gửi nhiều điểm dữ liệu lên nền tảng phân tích |
| Qua tường lửa / mạng kém | Khó hơn | ⭐ Tốt hơn — kết nối đi ra |

> ⭐ **Điểm mạnh lớn nhất của OPC UA là dữ liệu tự mô tả.**
> Với Modbus, thanh ghi 100 là gì thì chỉ tài liệu biết (Chương 39, mục 39.2). Với OPC UA, thiết bị
> nói cho bạn biết: tên, kiểu, đơn vị, dải. Nó loại bỏ cả hai bẫy kinh điển của Chương 39.
>
> ⭐ **Điểm mạnh lớn nhất của MQTT là chiều kết nối.** Máy **đi ra** kết nối tới máy trung gian, thay
> vì chờ ai đó **đi vào**. Điều đó rất hợp với nguyên tắc an ninh ở mục 45.6.

> ⚠ **Cả hai đều KHÔNG dành cho điều khiển thời gian thực.** Chúng là kênh **dữ liệu**, không phải
> kênh điều khiển. Đừng dùng chúng cho việc phối hợp chuyển động hay bắt tay máy–máy (Chương 40, 41).

---

## 45.5 ⭐⭐ Vì sao không cho hệ IT truy cập trực tiếp PLC

Đây là mục quan trọng nhất chương.

### Bốn lý do

| Lý do | Giải thích |
|---|---|
| ⭐ **PLC không chịu được tải hỏi** | Đúng cỗ máy ở mục 45.1 — PLC thiết kế cho vài kết nối, không cho hàng chục |
| ⭐⭐ **Giao thức công nghiệp không có bảo mật** | Modbus, và nhiều giao thức khác, **không xác thực** — ai vào được mạng là ghi được (Chương 39, mục 39.6) |
| **PLC không vá được như máy tính** | Không có bản cập nhật hằng tháng; nâng cấp firmware phải dừng máy |
| ⚠ **Một truy vấn sai làm dừng chuyền** | Và người viết truy vấn thường không biết điều đó |

> ⚠⚠ **Điểm thứ hai đáng nhấn mạnh: rất nhiều giao thức công nghiệp được thiết kế cho một thế giới
> không có kết nối ra ngoài.**
>
> Chúng ra đời khi mạng nhà máy là mạng đóng, và ai vào được nhà máy thì đã qua cổng bảo vệ. Không có
> mật khẩu, không có mã hoá, không có kiểm tra quyền — vì lúc đó không cần.
>
> Nối chúng vào một mạng có kết nối rộng hơn mà không thêm lớp bảo vệ là **mang giả định của những
> năm 1980 vào môi trường hôm nay**.

### ⭐ Lớp trung gian

```text
   ┌──────────┐     ┌───────────────┐     ┌──────────────┐
   │   PLC    │◄───►│  LỚP TRUNG    │◄───►│  Hệ IT / MES │
   │          │     │     GIAN      │     │  Phân tích   │
   └──────────┘     └───────────────┘     └──────────────┘
    Một kết nối      Đọc PLC theo         Nhiều người dùng
    duy nhất,        chu kỳ, lưu đệm,     hỏi lớp trung gian
    có kiểm soát     phục vụ nhiều bên    (không hỏi PLC)
```

| Lớp trung gian làm gì | Được gì |
|---|---|
| ⭐ **Đọc PLC theo một chu kỳ cố định** | PLC chỉ chịu **một** tải, biết trước và ổn định |
| **Phục vụ nhiều người dùng** từ bản đệm | Năm bảng tính không thành năm luồng hỏi PLC |
| ⭐ **Chặn ghi** — chỉ cho đọc | Hệ IT **không ghi được** vào PLC |
| **Xác thực và phân quyền** | Thứ mà giao thức công nghiệp không có |
| **Ghi vết truy cập** | Ai đọc gì, lúc nào |

> ⭐ **Lớp trung gian có thể là: máy chủ OPC UA, SCADA, kho dữ liệu, hoặc một máy tính công nghiệp
> chuyên trách.** Cái nào cũng được — điều quan trọng là **có một lớp**, và PLC chỉ nói chuyện với nó.

---

## 45.6 Phân vùng mạng

### Mô hình Purdue — ở mức đủ dùng

**Mô hình Purdue** chia hệ thống nhà máy thành các tầng, và nguyên tắc là **lưu lượng đi qua từng
tầng**, không nhảy cóc.

```text
   Tầng 4–5   HỆ THỐNG DOANH NGHIỆP        (ERP, mạng văn phòng, Internet)
                       ▲
                   ┌───┴───┐
                   │  DMZ  │  ⭐ VÙNG ĐỆM — nơi hai bên gặp nhau
                   └───┬───┘
                       ▼
   Tầng 3     ĐIỀU HÀNH SẢN XUẤT           (MES, kho dữ liệu, máy chủ OPC UA)
                       ▲▼
   Tầng 2     GIÁM SÁT                     (SCADA, HMI)
                       ▲▼
   Tầng 1     ĐIỀU KHIỂN                   (PLC)
                       ▲▼
   Tầng 0     THIẾT BỊ                     (cảm biến, cơ cấu chấp hành)
```

> ⭐ **Ý tưởng cốt lõi rất đơn giản: mạng văn phòng KHÔNG nói chuyện trực tiếp với PLC.**
> Muốn lấy dữ liệu thì hỏi tầng 3; tầng 3 hỏi tầng 2 hoặc tầng 1. Mỗi ranh giới là một chỗ kiểm soát
> được.

### ⭐ Vùng đệm

**DMZ** *(vùng đệm)* là một mạng nhỏ nằm giữa mạng nhà máy và mạng doanh nghiệp. Máy chủ dữ liệu đặt
ở đó.

> ⭐ **Nguyên tắc: không kết nối nào đi xuyên qua DMZ.**
> - Tầng máy **đẩy** dữ liệu **lên** DMZ.
> - Mạng doanh nghiệp **đọc** dữ liệu **từ** DMZ.
> - ⚠ Không có kết nối trực tiếp từ mạng doanh nghiệp xuống tầng máy.
>
> Nhờ vậy, ngay cả khi một máy tính văn phòng bị xâm nhập, kẻ tấn công cũng chỉ tới được DMZ — và ở
> đó không có gì điều khiển máy móc.

### Vùng và ống dẫn

Bộ tiêu chuẩn an ninh cho hệ điều khiển công nghiệp (IEC 62443) dùng hai khái niệm:

| Khái niệm | Nghĩa |
|---|---|
| **Vùng** *(zone)* | Nhóm thiết bị có **cùng yêu cầu an ninh** — ví dụ: một chuyền, một khu |
| ⭐ **Ống dẫn** *(conduit)* | Đường liên lạc **được kiểm soát** giữa hai vùng |

> ⭐ **Ý tưởng thực dụng: chia máy móc thành vùng, và mọi liên lạc giữa các vùng phải đi qua một chỗ
> kiểm soát được.**
>
> Điều này cũng giới hạn thiệt hại: nếu một vùng có vấn đề, các vùng khác không bị ảnh hưởng ngay.

---

## 45.7 ⭐ Những việc thực tế người lập trình PLC làm được

Bạn không phải chuyên gia an ninh. Nhưng có những việc thuộc phạm vi của bạn, và làm chúng loại được
phần lớn rủi ro dễ gặp nhất.

| Việc | Vì sao |
|---|---|
| ⭐ **Tách mạng máy khỏi mạng văn phòng** | Biện pháp đơn giản nhất và hiệu quả nhất (Chương 40, mục 40.9) |
| ⭐ **Đổi mật khẩu mặc định** trên mọi thiết bị | ⚠ Mật khẩu mặc định của mọi thiết bị công nghiệp đều công khai |
| **Tắt dịch vụ không dùng** trên PLC và thiết bị mạng | Bớt cửa vào |
| ⭐ **Đặt PLC ở chế độ khoá khi chạy sản xuất** | Nhiều CPU có công tắc hoặc tham số chặn sửa từ xa (Chương 8, mục 8.8) |
| **Không để máy tính lập trình cắm thường trực** vào mạng máy | Máy tính là đường lây phổ biến nhất |
| ⚠ **Quét USB trước khi cắm vào máy tính lập trình** | Một trong những đường lây kinh điển vào mạng cách ly |
| ⭐ **Sao lưu chương trình và cấu hình, giữ ngoại tuyến** | ⭐ Phòng thủ cuối cùng — Chương 54 |
| **Ghi lại ai có quyền truy cập gì** | Không có danh sách thì không kiểm soát được |

> ⚠⚠ **"Mạng máy đã cách ly rồi nên không sao" là giả định nguy hiểm nhất.**
> Cách ly hoàn toàn hiếm khi tồn tại lâu: ai đó cắm máy tính xách tay để lập trình, ai đó nối tạm để
> lấy dữ liệu, ai đó thêm một modem để nhà cung cấp hỗ trợ từ xa — và không ai gỡ nó ra.
>
> ⭐ **Bảo mật nhiều lớp** nghĩa là: kể cả khi lớp ngoài bị vượt qua, vẫn còn lớp trong.

### ⚠ Truy cập từ xa

Nhà cung cấp máy thường muốn truy cập từ xa để hỗ trợ. Đây là nhu cầu chính đáng và cũng là rủi ro
lớn.

| Yêu cầu tối thiểu | Vì sao |
|---|---|
| ⭐ **Bật khi cần, tắt khi xong** — không để thường trực | Cửa đóng thì không ai vào được |
| ⭐ **Người tại nhà máy chủ động cho phép** từng phiên | Không phải nhà cung cấp tự vào lúc nào cũng được |
| **Ghi vết**: ai vào, lúc nào, làm gì | Điều tra được khi có chuyện |
| ⚠ **Đưa vào hợp đồng** | Ai chịu trách nhiệm nếu có sự cố qua đường này |

---

## 45.8 ⚠⚠ An ninh và an toàn là hai chuyện khác nhau

Điểm này ngắn nhưng phải nói rõ.

| | **An toàn** *(safety)* | **An ninh** *(security)* |
|---|---|---|
| Bảo vệ chống | Hỏng hóc và sai sót **ngẫu nhiên** | Hành vi **có chủ đích** |
| Tiêu chuẩn | ISO 13849, IEC 62061, IEC 61508 | IEC 62443 |
| Chương | 47, 48 | Chương này |

> ⚠⚠ **Biện pháp an ninh KHÔNG thay thế được chức năng an toàn, và ngược lại.**
>
> Một tường lửa không ngăn được cơ cấu kẹp tay người. Một rơ-le an toàn (Chương 47) không ngăn được
> ai đó ghi tham số sai vào PLC qua mạng.
>
> ⭐ **Nhưng chúng liên quan tới nhau theo một chiều quan trọng: một cuộc tấn công có thể tạo ra tình
> huống nguy hiểm.** Đó là lý do chức năng an toàn phải nằm ở **mạch an toàn phần cứng**, không nằm
> trong logic PLC thường — mạch an toàn không nối mạng, nên không tấn công qua mạng được (Chương 47).
>
> Đây là một lập luận nữa, ngoài các lập luận ở Chương 47, cho cùng một kết luận.

---

## 45.9 Trên máy mẫu DP-01

### Kiến trúc mạng

```text
   ┌─────────────────── MẠNG NHÀ MÁY ───────────────────┐
   │                                                     │
   │  ┌── Mạng chuyển động ──┐   ┌── Mạng chung ──────┐  │
   │  │  Drive X, Y, Z       │   │  HMI               │  │
   │  │  (Chương 40, họ 2/3) │   │  Đầu đọc mã 2D     │  │
   │  └──────────┬───────────┘   │  (Chương 42)       │  │
   │             │               └─────────┬──────────┘  │
   │          ┌──▼───────────────────────  ▼──┐          │
   │          │           PLC DP-01           │          │
   │          └──────────────┬───────────────-┘          │
   └─────────────────────────┼───────────────────────────┘
                             │  ⭐ MỘT kết nối duy nhất
                    ┌────────▼────────┐
                    │  Lớp trung gian │   ← máy chủ OPC UA / kho dữ liệu
                    │     (DMZ)       │
                    └────────┬────────┘
                             │  ⚠ đọc, không ghi xuống
                    ┌────────▼────────┐
                    │  MES / báo cáo  │
                    │  Mạng văn phòng │
                    └─────────────────┘
```

| Quyết định | Lý do |
|---|---|
| ⭐ PLC chỉ có **một** kết nối lên trên | Chống đúng cỗ máy ở mục 45.1 |
| ⭐ Lớp trung gian **chỉ đọc** từ PLC | Hệ IT không ghi được vào máy |
| Ngoại lệ: MES **ghi công thức xuống** | ⚠ Xem bên dưới |
| Mạng chuyển động **không nối lên trên** | Không có lý do gì để nó ra ngoài (Chương 40) |
| Mật khẩu mặc định **đã đổi** trên mọi thiết bị | Mục 45.7 |

> ⚠ **Ngoại lệ "MES ghi công thức xuống" là ngoại lệ có kiểm soát, không phải lỗ hổng.**
>
> Luồng ở Chương 42 mục 42.5 cần MES trả về mã công thức. Nhưng ⭐ **PLC vẫn kiểm tra hợp lệ mọi tham
> số nhận được** (Chương 29, mục 29.4) — nên kể cả khi dữ liệu sai hoặc bị can thiệp, PLC **từ chối**
> thay vì chạy với nó.
>
> Đây là lý do mục 29.4 tồn tại, và là ví dụ rõ của **bảo mật nhiều lớp**: không tin dữ liệu từ bên
> ngoài, kể cả từ nguồn "đáng tin".

### Dữ liệu gửi lên

| Nhóm | Nội dung | Tần suất |
|---|---|---|
| Theo board | Mã, OK/NG, lý do, thông số quá trình | Mỗi board (Chương 42) |
| Sản lượng | OK, NG, tỉ lệ | Mỗi phút |
| ⭐ Xu hướng | Nhiệt độ keo, cường độ UV, dòng chuyền, chu kỳ | Mỗi 10 giây |
| Sự kiện | Báo động, đổi công thức, nhập tay, cưỡng bức I/O | Khi xảy ra |
| ⭐ Thời gian chờ chuyền | Chờ máy trước, chờ máy sau | Mỗi phút (Chương 41, mục 41.8) |

> ⭐ **Hàng cuối là hàng ít máy nào gửi, và là hàng có giá trị nhất cho việc cải thiện chuyền.**
> Với chu kỳ 12 giây đã chốt và trạm sấy UV sát trần (Phụ lục J §7.1), câu hỏi "DP-01 có phải nút cổ
> chai không" chỉ trả lời được bằng số liệu này — Chương 55.

---

## 45.10 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| Máy chủ OPC UA trong PLC | ⭐ Nhiều CPU hiện đại có sẵn; ⚠ **kiểm dòng CPU cụ thể** (Chương 13) |
| Hỗ trợ MQTT | Có ở một số hệ, hoặc qua thư viện, hoặc qua thiết bị trung gian |
| ⭐ Bảo mật của PLC | Rất khác nhau: một số hỗ trợ xác thực và mã hoá, một số **không có gì**. ⚠ Kiểm khi chọn phần cứng |
| Khoá chương trình | Cơ chế và mức độ khác nhau; ⚠ **khoá quá chặt thì khách hàng không sửa được máy của họ** (Chương 13, tiêu chí 5) |
| Ghi vết truy cập | Có ở một số hệ; ⚠ kiểm nếu có yêu cầu |
| Cập nhật firmware | ⚠ Thường phải **dừng máy** — lên kế hoạch, không làm ngẫu hứng |

> ⚠ **Cập nhật firmware để vá lỗ hổng là bài toán khó riêng của tự động hoá.**
> Máy tính văn phòng vá hằng tháng. Máy sản xuất phải **dừng** để vá — và mỗi lần dừng là tiền, mỗi
> lần cập nhật là rủi ro thứ đang chạy sẽ hỏng.
>
> ⭐ Đó là lý do **phân vùng mạng quan trọng hơn vá lỗi** trong môi trường OT: nếu thiết bị không tiếp
> cận được từ bên ngoài thì lỗ hổng của nó ít khai thác được hơn nhiều.

---

## 45.11 Bẫy thường gặp

### 🔍 BẪY 1 — Cho hệ IT đọc thẳng từ PLC

**Hiện tượng:** ⭐ đúng cỗ máy ở mục 45.1 — nhiều người dùng cùng hỏi, thời gian quét tăng vọt, chuyển
động không đều.
**Cách sửa:** ⭐ **lớp trung gian** — PLC chỉ có một kết nối lên trên (mục 45.5).

### 🔍 BẪY 2 — Nối mạng máy thẳng vào mạng văn phòng

**Hiện tượng:** ⚠⚠ bất kỳ ai trong mạng văn phòng đều **ghi được vào PLC** — giao thức công nghiệp
không xác thực.
**Cách sửa:** phân vùng và DMZ (mục 45.6).

### 🔍 BẪY 3 — Giữ mật khẩu mặc định

**Hiện tượng:** ⚠ mật khẩu mặc định của mọi thiết bị công nghiệp đều công khai trên mạng.
**Cách sửa:** đổi hết, và ghi lại ở nơi an toàn (mục 45.7).

### 🔍 BẪY 4 — Tin rằng "mạng đã cách ly nên không sao"

**Hiện tượng:** cách ly bị phá dần bởi máy tính xách tay, kết nối tạm, modem hỗ trợ từ xa — và không
ai gỡ ra.
**Cách sửa:** bảo mật **nhiều lớp**; giả định lớp ngoài có thể bị vượt qua (mục 45.7).

### 🔍 BẪY 5 — Truy cập từ xa thường trực

**Hiện tượng:** một cửa mở suốt ngày đêm mà không ai theo dõi.
**Cách sửa:** bật khi cần, tắt khi xong, **người tại nhà máy cho phép từng phiên**, có ghi vết
(mục 45.7).

### 🔍 BẪY 6 — Tin dữ liệu từ hệ thống trên

**Hiện tượng:** một giá trị sai hoặc bị can thiệp đi thẳng vào máy.
**Cách sửa:** ⭐ **PLC luôn kiểm tra hợp lệ** (Chương 29, mục 29.4) — đây là lớp bảo vệ cuối và nó
hoạt động kể cả khi các lớp trên bị vượt qua.

### 🔍 BẪY 7 — Ghi mọi thứ vào kho dữ liệu

**Hiện tượng:** dung lượng phình to, truy vấn chậm, và **không ai dùng phần lớn dữ liệu**.
**Cách sửa:** ba câu hỏi ở mục 45.2 — bắt đầu bằng "ai đọc và để trả lời câu hỏi gì".

### 🔍 BẪY 8 — Không đệm dữ liệu khi mất kết nối

**Hiện tượng:** mất kết nối một giờ → mất một giờ dữ liệu truy xuất, không dựng lại được.
**Cách sửa:** đệm trong PLC hoặc trong HMI, gửi bù khi có lại (mục 45.3, Chương 42 mục 42.6).

### 🔍 BẪY 9 — Dùng OPC UA hoặc MQTT cho điều khiển

**Hiện tượng:** trễ biến động làm phối hợp sai; và mất kết nối làm máy dừng vì lý do không liên quan.
**Cách sửa:** chúng là kênh **dữ liệu**, không phải kênh điều khiển (mục 45.4).

### 🔍 BẪY 10 — Nhầm an ninh với an toàn

**Hiện tượng:** ⚠⚠ tin rằng tường lửa bảo vệ được người, hoặc rơ-le an toàn (Chương 47) bảo vệ được
khỏi tấn công mạng.
**Cách sửa:** hai chuyện khác nhau, hai bộ tiêu chuẩn khác nhau (mục 45.8).

### 🔍 BẪY 11 — Khoá chương trình quá chặt

**Hiện tượng:** khách hàng **không sửa được máy của chính họ** lúc hai giờ sáng, và phải chờ nhà cung
cấp.
**Cách sửa:** cân bằng giữa bảo vệ sở hữu trí tuệ và khả năng bảo trì; đưa vào hợp đồng (mục 45.10,
Chương 13 tiêu chí 5).

---

## 45.12 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Ba câu hỏi trước khi ghi dữ liệu | **Ai đọc, để trả lời gì** · không có thì mất gì · giữ bao lâu |
| Nhóm dữ liệu bị đánh giá thấp nhất | ⭐ **Xu hướng quá trình** |
| PLC hợp để | ⭐ **Đệm tạm**, không phải lưu dài hạn |
| Điểm mạnh của OPC UA | ⭐ **Dữ liệu tự mô tả** — có kiểu, đơn vị, cấu trúc |
| Điểm mạnh của MQTT | ⭐ **Kết nối đi ra**, hợp với tường lửa |
| ⚠ Cả hai không dùng cho | **Điều khiển thời gian thực** |
| ⭐⭐ Vì sao không cho IT truy cập thẳng PLC | Tải hỏi · **giao thức không có bảo mật** · không vá được · một truy vấn sai làm dừng chuyền |
| Giải pháp | ⭐ **Lớp trung gian** — PLC chỉ một kết nối, chỉ đọc |
| Ý tưởng cốt lõi của mô hình Purdue | ⭐ **Mạng văn phòng không nói chuyện trực tiếp với PLC** |
| Nguyên tắc DMZ | ⭐ **Không kết nối nào đi xuyên qua** — đẩy lên, đọc xuống |
| Việc hiệu quả nhất mà bạn làm được | ⭐ **Tách mạng máy khỏi mạng văn phòng** |
| Truy cập từ xa | Bật khi cần · **người tại chỗ cho phép** · ghi vết · có trong hợp đồng |
| ⚠⚠ An ninh và an toàn | **Hai chuyện khác nhau**, không thay thế nhau |
| Vì sao chức năng an toàn không nối mạng | ⭐ Mạch an toàn phần cứng **không tấn công qua mạng được** |
| Vì sao phân vùng quan trọng hơn vá lỗi trong OT | ⚠ Máy sản xuất **phải dừng** để vá |
| Lớp bảo vệ cuối cùng của PLC | ⭐ **Luôn kiểm tra hợp lệ dữ liệu nhận được** |

---

## 45.13 Tự kiểm

1. ⭐ Mô tả sự cố ở mục 45.1. Vì sao nó xảy ra được, và kịch bản **tệ hơn** của cùng đường truy cập
   đó là gì?
2. Nêu ba câu hỏi trước khi quyết định ghi một loại dữ liệu. Câu nào lọc tốt nhất?
3. Vì sao PLC là nơi tệ nhất để lưu dài hạn nhưng tốt nhất để đệm tạm?
4. So sánh OPC UA với MQTT. Điểm mạnh lớn nhất của mỗi cái là gì?
5. ⭐ Vì sao "dữ liệu tự mô tả" của OPC UA là ưu điểm lớn? Nó loại bỏ bẫy nào ở Chương 39?
6. ⭐⭐ Nêu bốn lý do **không** cho hệ IT truy cập trực tiếp PLC. Lý do nào bạn cho là nghiêm trọng
   nhất?
7. Lớp trung gian làm những việc gì? Nó giải quyết vấn đề ở mục 45.1 như thế nào?
8. ⭐ Phát biểu ý tưởng cốt lõi của mô hình Purdue trong một câu. Nguyên tắc của DMZ là gì?
9. Nêu năm việc thuộc phạm vi người lập trình PLC mà loại được phần lớn rủi ro dễ gặp.
10. ⚠ Vì sao "mạng máy đã cách ly rồi nên không sao" là giả định nguy hiểm?
11. ⭐⭐ Phân biệt an ninh với an toàn. Chúng liên quan tới nhau theo chiều nào, và điều đó củng cố kết
    luận nào ở Chương 47?
12. Trên DP-01, MES **ghi công thức xuống** PLC. Vì sao đó không phải lỗ hổng? Cơ chế nào bảo vệ?

> Câu 1, 6, 8 và 11 là bốn câu phân loại. Câu 12 là tinh thần của cả chương: **bảo mật nhiều lớp
> nghĩa là lớp trong vẫn làm việc của nó kể cả khi bạn giả định lớp ngoài đã bị vượt qua.**

---

### Chương tiếp theo

Chương 46 — **Tích hợp robot & tay gắp**. Chương cuối của lát cắt 4. Về một loại thiết bị mà câu hỏi
đầu tiên không phải kỹ thuật mà là tổ chức: ⭐ **ai chỉ huy ai** — PLC làm chủ hay robot làm chủ, và
hệ quả của lựa chọn đó lên toàn bộ cách viết chương trình.

### Nguồn tham khảo chương 45

- **IEC 62443** (bộ) — *Security for industrial automation and control systems*: khái niệm vùng và
  ống dẫn, mức an ninh, và yêu cầu cho từng vai trò trong chuỗi cung ứng. *(tiêu chuẩn có bản quyền)*
- **IEC 62541** — *OPC Unified Architecture*: đặc tả OPC UA. *(tiêu chuẩn có bản quyền)*
- **Mô hình Purdue** — mô hình phân tầng kiến trúc hệ điều khiển công nghiệp, được nhiều tài liệu và
  tiêu chuẩn ngành tham chiếu.
- **Tài liệu bảo mật của hệ PLC đang dùng** — dùng cho ⚠ **khả năng xác thực và mã hoá của dòng CPU
  cụ thể**, cơ chế khoá chương trình, và ghi vết truy cập.
- Bảng I/O và số liệu đã chốt của DP-01 — Phụ lục J.

> ⚠⚠ **Giới hạn của chương này.** Nội dung ở đây là **định hướng để bạn không tự tạo ra lỗ hổng và
> biết phải hỏi gì**. Nó **không** đủ để thiết kế kiến trúc an ninh cho một nhà máy.
>
> Việc đánh giá rủi ro an ninh, phân vùng, thiết kế DMZ, và xác định mức an ninh cần đạt phải do
> **người có chuyên môn về an ninh hệ điều khiển công nghiệp** thực hiện, phối hợp với bộ phận công
> nghệ thông tin của cơ sở. ⚠ Yêu cầu pháp lý về an ninh hạ tầng công nghiệp đang thay đổi ở nhiều
> nơi — kiểm quy định hiện hành tại thị trường của bạn.
>
> ⚡ Mô hình Purdue ở mục 45.6 là **mô hình tham chiếu kinh điển**, và nó được xây dựng cho kiến trúc
> phân tầng truyền thống. Với các hệ hiện đại có kết nối trực tiếp lên nền tảng đám mây, ranh giới
> giữa các tầng mờ hơn — nhưng ⭐ **nguyên tắc cốt lõi vẫn giữ nguyên: mọi liên lạc giữa các vùng phải
> đi qua một chỗ kiểm soát được.**
