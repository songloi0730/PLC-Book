
# Chương 55 — Tính chu kỳ máy & năng suất

> **Lát cắt máy mẫu:** 5 — máy đầy đủ, hai trạm nối tiếp, đã chạy sản xuất.

---

## 55.1 Bài toán: cỗ máy nhanh gấp đôi mà sản lượng không đổi

Một cỗ máy hai trạm. Trạm 1 mất 4 giây, trạm 2 mất 12 giây. Khách hàng muốn nhanh hơn.

Đội kỹ thuật tối ưu trạm 1: đổi xi-lanh nhanh hơn, tăng tốc độ trục, rút thời gian từ **4 giây xuống
2 giây**. Nhanh gấp đôi. Ai cũng hài lòng.

Sản lượng sau khi cải tiến: **không đổi**.

> ⭐⭐ **Vì trạm 2 vẫn mất 12 giây, và mỗi board vẫn phải đi qua trạm 2.**
>
> Toàn bộ công sức đổ vào một trạm **không phải nút cổ chai**. Máy nhả ra một board mỗi 12 giây trước
> khi cải tiến, và một board mỗi 12 giây sau khi cải tiến.

Chương này về việc **biết trước** điều đó — bằng số học đơn giản, và bằng dữ liệu mà PLC đã có sẵn.

---

## 55.2 Chu kỳ và sản lượng

### Định nghĩa

| Khái niệm | Nghĩa |
|---|---|
| ⭐ **Chu kỳ máy** *(cycle time)* | Khoảng thời gian giữa **hai sản phẩm liên tiếp ra khỏi máy** |
| Thời gian gia công của một trạm | Trạm đó mất bao lâu cho một sản phẩm |
| ⭐ **Sản lượng giờ** *(UPH — units per hour)* | Số sản phẩm ra trong một giờ |

```text
UPH  =  3600  ÷  chu kỳ máy (giây)
```

> ⚠ **Chu kỳ máy KHÔNG phải thời gian một sản phẩm đi hết máy.**
>
> Một board có thể mất 16 giây để đi từ đầu tới cuối DP-01 — nhưng nếu máy nhả ra một board mỗi 12
> giây thì chu kỳ máy là **12 giây**, không phải 16.
>
> ⭐ Thời gian đi hết máy gọi là **thời gian thông qua** *(throughput time)*. Nó quan trọng với việc
> khác — bao nhiêu sản phẩm đang nằm trong máy, mất bao lâu để xả hết máy khi đổi lô — nhưng **không**
> quyết định sản lượng.

### ⭐ Nhầm lẫn này gây ra gì

| Nhầm | Hậu quả |
|---|---|
| Cộng thời gian các trạm lại | ⭐ Báo sản lượng **thấp hơn thực tế** → mất hợp đồng |
| Lấy trạm nhanh nhất | ⚠ Hứa sản lượng **cao hơn thực tế** → không nghiệm thu được |
| ⭐ **Lấy trạm chậm nhất** | ⭐⭐ **Đúng** — với máy nối tiếp có đệm giữa các trạm |

---

## 55.3 ⭐⭐ Nút cổ chai

### Vì sao chu kỳ bằng trạm chậm nhất

Với máy nhiều trạm nối tiếp, các trạm làm việc **song song trên các sản phẩm khác nhau**: trong lúc
trạm 2 xử lý board A, trạm 1 đã xử lý board B.

```text
Thời gian →
Trạm 1 (4 s):  [A][B][C][D][E][F]...   ← chờ nhiều
Trạm 2 (12 s): [·····A·····][·····B·····][·····C·····]
Ra máy:                     A            B            C
                            └── 12 s ────┘
```

⭐ Máy nhả sản phẩm theo nhịp của **trạm chậm nhất** — trạm đó gọi là **nút cổ chai** *(bottleneck)*.

```text
Chu kỳ máy  =  thời gian của trạm CHẬM NHẤT   (không phải tổng)
```

> ⭐⭐ **Hệ quả thực dụng, và là ý quan trọng nhất chương:**
>
> | Cải tiến ở đâu | Kết quả |
> |---|---|
> | ⭐ **Nút cổ chai** | ⭐ **Sản lượng tăng** |
> | Trạm bất kỳ khác | ⚠ **Sản lượng không đổi** — đúng cỗ máy ở mục 55.1 |
>
> Trước khi tối ưu bất cứ thứ gì, hãy **tìm ra nút cổ chai**. Tối ưu chỗ khác là công sức đổ đi.

### ⭐ Nút cổ chai di chuyển

Sau khi bạn cải tiến nút cổ chai, **một trạm khác trở thành nút cổ chai**.

Với ví dụ ở trên: rút trạm 2 từ 12 giây xuống 5 giây thì chu kỳ mới là **5 giây** (trạm 2 vẫn chậm
nhất). Rút tiếp xuống 3 giây thì chu kỳ là **4 giây** — nút cổ chai đã chuyển sang trạm 1.

> ⭐ **Nghĩa là: cải tiến nút cổ chai có giới hạn lợi ích rõ ràng.** Rút trạm 2 xuống dưới 4 giây
> **không còn tăng sản lượng nữa**, trừ khi bạn cũng cải tiến trạm 1.
>
> Biết trước điều này giúp bạn dừng đúng lúc — và giúp bạn trả lời câu "làm nhanh nữa được không?"
> bằng số, chứ không bằng cảm giác.

### ⚠ Điều kiện để công thức đúng

| Điều kiện | Nếu không có thì sao |
|---|---|
| ⭐ **Có chỗ đệm giữa các trạm** | ⚠ Không có đệm thì các trạm **khoá lẫn nhau** — xem bên dưới |
| Thời gian chuyển sản phẩm nhỏ so với thời gian gia công | Nếu không, phải cộng nó vào |
| Các trạm chạy độc lập, không dùng chung tài nguyên | Dùng chung một robot thì phải tính khác |

> ⚠⚠ **Máy không có đệm — trường hợp của DP-01.**
>
> Nếu board đi thẳng từ trạm 1 sang trạm 2 mà **không có chỗ chờ**, thì trạm 1 xong sớm cũng phải
> **giữ board lại** cho tới khi trạm 2 rảnh. Chu kỳ vẫn bằng trạm chậm nhất, nhưng ⭐ **phải cộng thêm
> thời gian chuyển board** vì việc chuyển không chồng lấn được với gia công:
>
> ```text
> Chu kỳ  =  thời gian trạm chậm nhất  +  thời gian chuyển giữa các trạm
> ```
>
> Đây là lý do một chỗ đệm cho **đúng một board** giữa hai trạm thường là cải tiến rẻ nhất và hiệu
> quả nhất trên máy nối tiếp.

---

## 55.4 ⭐ Tính lý thuyết so với đo thật

### Tính lý thuyết — làm khi thiết kế

Cộng các động tác trong trạm nút cổ chai:

```text
Trạm 2 (sấy UV) của DP-01:
  Board vào vị trí, kẹp              1,0 s
  Đèn UV bật, sấy                    8,0 s
  Đèn tắt, chờ nguội                 1,0 s
  Nhả kẹp, board ra                  1,0 s
  ─────────────────────────────────────────
  Tổng                              11,0 s
```

> ⚠ **Con số lý thuyết luôn lạc quan hơn thực tế.** Nó bỏ qua: thời gian đáp ứng cảm biến, thời gian
> quét PLC, gia tốc thật của cơ cấu, độ trễ van khí, và những khoảng chờ nhỏ mà không ai nghĩ tới.
>
> ⭐ **Thực tế thường cao hơn lý thuyết 10–30 %.** Khi báo sản lượng cho khách, hãy nói rõ con số của
> bạn là lý thuyết hay đo thật.

### ⭐⭐ Đo thật bằng PLC — dữ liệu gần như miễn phí

Đây là ý mà rất ít người khai thác: **PLC đã biết mọi mốc thời gian rồi**, chỉ cần ghi lại.

| Đo gì | Cách |
|---|---|
| ⭐ **Thời gian mỗi bước** | Ghi giá trị đồng hồ khi vào bước, trừ khi ra bước |
| ⭐ **Chu kỳ máy thật** | Khoảng thời gian giữa hai lần sản phẩm ra |
| ⭐⭐ **Thời gian CHỜ của từng trạm** | ⭐ **Số quan trọng nhất** — xem bên dưới |
| Thời gian dừng máy và lý do | Ghi kèm mã báo động (Chương 43) |

```text
// Đo thời gian một bước — mẫu giả lệnh, xem Chương 21 về trình tự
KHI vào bước:      MocBatDau[buoc] := DongHoHeThong
KHI ra khỏi bước:  ThoiGianBuoc[buoc] := DongHoHeThong - MocBatDau[buoc]
                   NẾU ThoiGianBuoc[buoc] > KyLuc[buoc] THÌ
                       KyLuc[buoc] := ThoiGianBuoc[buoc]
```

> ⭐ **Lưu ba con số cho mỗi bước, không phải một:** lần gần nhất · trung bình · ⭐ **lớn nhất**.
>
> Giá trị **lớn nhất** là thứ giải thích vì sao sản lượng thực tế thấp hơn tính toán. Trung bình
> 8 giây nhưng thỉnh thoảng 20 giây — cái 20 giây đó ăn mất sản lượng, và nó vô hình trong số trung
> bình.

### ⭐⭐ Thời gian chờ — số quan trọng nhất

Với mỗi trạm, đo **bao nhiêu phần trăm thời gian nó đang chờ** thay vì đang làm việc.

| Kết quả | Nghĩa |
|---|---|
| ⭐ Trạm chờ **gần 0 %** | ⭐⭐ **Đây là nút cổ chai** |
| Trạm chờ nhiều | Còn dư năng lực — ⚠ **đừng tối ưu ở đây** |

> ⭐⭐ **Đây là cách tìm nút cổ chai bằng dữ liệu thay vì bằng phỏng đoán.** Nó tốn khoảng mười dòng
> lệnh cho mỗi trạm, và nó trả lời dứt điểm câu hỏi mà cả đội có thể tranh luận cả buổi.
>
> Và nó bắt được thứ mà tính toán không bắt được: một trạm chờ 40 % thời gian **vì máy phía trước
> không cấp đủ hàng** — nút cổ chai nằm ngoài máy của bạn.

---

## 55.5 ⭐ Tối ưu bằng song song hoá

Sau khi biết nút cổ chai, cách rẻ nhất để rút chu kỳ **không phải mua thiết bị nhanh hơn** — mà là
làm nhiều việc cùng lúc.

### Tìm việc chồng lấn được

| Câu hỏi | Ví dụ trên DP-01 |
|---|---|
| ⭐ **Động tác nào không phụ thuộc động tác nào?** | Gantry về vị trí xuất phát **trong lúc** băng tải đưa board tiếp theo vào |
| Việc nào làm được **trước** khi cần? | Đọc mã vạch board tiếp theo trong lúc board hiện tại đang sấy |
| Việc nào làm được **sau** khi đã nhả sản phẩm? | Thổi sạch đầu kim tra keo |
| ⭐ Có chờ nào **không cần thiết** không? | Chờ cố định 500 ms "cho chắc" — ⭐ thay bằng **chờ tín hiệu thật** |

> ⭐⭐ **Hàng cuối đáng soát lại trên mọi máy.** Những khoảng `Timer 500 ms` rải rác trong chương
> trình — thêm vào lúc chạy thử để "cho chắc" và không ai gỡ ra — cộng lại thành vài giây mỗi chu kỳ.
>
> Mỗi cái thay được bằng một tín hiệu phản hồi thật (Chương 9, mục 9.6) vừa **nhanh hơn** vừa **an
> toàn hơn** — vì nó biết khi cơ cấu **không** tới nơi, còn bộ định thì không.

### ⚠ Ranh giới không được vượt

| ⚠ Không bao giờ song song hoá | Vì sao |
|---|---|
| ⚠⚠ **Kiểm tra an toàn** | Chương 47 — không có ngoại lệ về năng suất |
| ⚠ **Xác nhận vị trí trước khi chuyển động** | Chương 37 — bỏ qua để tiết kiệm 200 ms là cách gây va chạm |
| ⚠ Khoá liên động giữa các cơ cấu | Chương 22 |
| Chờ nhiệt độ / thời gian của quá trình vật lý | ⭐ Keo cần thời gian cứng; rút ngắn thì **hỏng sản phẩm**, không phải tăng năng suất |

> ⚠⚠ **Hàng cuối là cái bẫy tinh vi nhất.** Rút thời gian sấy UV từ 8 giây xuống 6 giây thì chu kỳ
> giảm thật — nhưng nếu keo chưa cứng đủ thì bạn vừa tăng sản lượng **hàng lỗi**.
>
> ⭐ Thời gian của một quá trình vật lý là **yêu cầu của quá trình**, không phải một tham số tối ưu.
> Muốn rút nó thì phải đổi quá trình — đèn mạnh hơn, keo khác — chứ không phải đổi chương trình.

---

## 55.6 ⚠ Thời gian chết ngoài chu kỳ

Chu kỳ tính được không phải sản lượng thật. Giữa các chu kỳ có những thứ ăn mất thời gian:

| Nguồn | Ghi chú |
|---|---|
| ⭐ **Chờ máy trước / máy sau** | Máy của bạn nhanh không giúp gì nếu chuyền không cấp đủ |
| Đổi lô, đổi công thức | ⭐ Cộng thời gian **xả hết máy** — đây là lúc *thời gian thông qua* mới quan trọng |
| Nạp vật tư | Keo, board, khay |
| ⭐ **Dừng do lỗi** | Chương 43 — ⭐ **thường là nguồn mất mát lớn nhất** |
| Bảo trì | Chương 53 |
| Khởi động đầu ca | Về gốc, làm nóng, chạy thử |

> ⭐⭐ **Trên rất nhiều máy, "dừng do lỗi" ăn nhiều sản lượng hơn toàn bộ công sức tối ưu chu kỳ.**
>
> Một máy có chu kỳ 12 giây mà dừng 30 phút mỗi ca vì kẹt board thì việc rút chu kỳ xuống 11 giây
> (tăng 9 %) kém giá trị hơn nhiều so với việc **hết kẹt board**.
>
> ⭐ Đây là lý do Chương 43 (báo động có ích) và mục 55.7 (OEE) quan trọng ngang mục 55.3.

---

## 55.7 Nhập môn OEE

**OEE** *(Overall Equipment Effectiveness — hiệu suất thiết bị tổng thể)* gộp ba tổn thất thành một
con số:

```text
OEE  =  Khả dụng  ×  Hiệu suất  ×  Chất lượng
```

| Thành phần | Ý nghĩa | Công thức |
|---|---|---|
| **Khả dụng** *(availability)* | Máy chạy được bao nhiêu so với thời gian dự định | Thời gian chạy ÷ thời gian dự định |
| **Hiệu suất** *(performance)* | Chạy nhanh bằng bao nhiêu so với chu kỳ thiết kế | (Chu kỳ lý thuyết × số SP) ÷ thời gian chạy |
| **Chất lượng** *(quality)* | Bao nhiêu phần trăm đạt | Số đạt ÷ tổng số làm ra |

### Ví dụ trên DP-01

```text
Ca 8 giờ = 480 phút; nghỉ theo kế hoạch 30 phút → dự định 450 phút
Dừng do lỗi 45 phút          → chạy 405 phút
Chu kỳ thiết kế 12 s → lý thuyết 405 × 60 ÷ 12 = 2025 board
Thực tế làm ra 1800 board, trong đó 36 board lỗi

Khả dụng  = 405 / 450   = 0,90
Hiệu suất = 1800 / 2025 = 0,89
Chất lượng= 1764 / 1800 = 0,98
OEE       = 0,90 × 0,89 × 0,98 = 0,78  →  78 %
```

> ⭐ **Giá trị của OEE không nằm ở con số 78 %, mà ở ba con số thành phần.**
>
> Chúng nói cho bạn biết **đầu tư công sức vào đâu**: ở đây khả dụng và hiệu suất đều kéo xuống
> tương đương, còn chất lượng đã tốt. Nếu chỉ nhìn "78 %", bạn không biết phải làm gì.

### ⚠⚠ Vì sao con số OEE dễ bị bóp méo

Đây là phần sách này bắt buộc phải nói, vì OEE hay bị dùng làm chỉ tiêu đánh giá con người:

| Cách bóp méo | Kết quả |
|---|---|
| ⭐ **Khai thời gian "dự định" ngắn lại** | Dừng máy chuyển thành "không dự định chạy" → khả dụng đẹp lên |
| ⭐ **Lấy chu kỳ thiết kế bằng chu kỳ thực tế** | ⭐⭐ **Hiệu suất luôn xấp xỉ 100 %** — chỉ số mất hết ý nghĩa |
| Không tính dừng ngắn | ⚠ Dừng dưới 2 phút "không đáng kể" — nhưng chúng cộng lại rất lớn |
| Đếm hàng sửa lại là hàng đạt | Chất lượng đẹp lên |
| So OEE giữa các máy khác nhau | ⚠ Vô nghĩa nếu định nghĩa khác nhau |

> ⚠⚠ **Cách bóp méo thứ hai là phổ biến nhất và nguy hiểm nhất**, vì nó trông hoàn toàn hợp lý: "lấy
> chu kỳ máy thực tế làm chuẩn". Sau đó hiệu suất luôn ~100 % và **không ai còn nhìn thấy tổn thất
> tốc độ nữa**.
>
> ⭐ **Chu kỳ dùng để tính hiệu suất phải là chu kỳ THIẾT KẾ, cố định**, ghi rõ ở đâu ra, và ⚠ **không
> được đổi để làm đẹp chỉ số**.

> ⭐⭐ **Điều quan trọng nhất về OEE, nói thẳng:** nó là công cụ để **tìm chỗ cải tiến**, không phải
> để chấm điểm con người. Khi nó bị dùng để chấm điểm, người ta sẽ tối ưu **con số** thay vì tối ưu
> **máy** — và bạn mất luôn công cụ.
>
> Là người lập trình, việc của bạn là làm cho số liệu **trung thực và tự động** (PLC không có động cơ
> làm đẹp báo cáo), rồi nói rõ định nghĩa mình dùng.

---

## 55.8 Trên máy mẫu DP-01

Số liệu đã chốt: **300 board/giờ** → chu kỳ **12,0 giây** (Phụ lục J §7.1).

| Trạm | Thời gian | Ghi chú |
|---|---|---|
| Băng tải đưa board vào, định vị | ~2 s | Chồng lấn được |
| **Trạm 1 — tra keo** | ~6 s | Gantry chạy đường keo |
| Chuyển board sang trạm 2 | ~1,5 s | ⚠ Không đệm → cộng vào chu kỳ |
| ⭐ **Trạm 2 — sấy UV** | ⭐ **6–12 s** | ⭐⭐ **NÚT CỔ CHAI** |
| Board ra | ~1,5 s | Chồng lấn được |

```text
Chu kỳ  =  trạm chậm nhất (12 s tệ nhất)  ... đã sát 12,0 s mục tiêu
```

> ⚠ **Kết luận thiết kế: với công thức sấy 12 giây, máy CHỈ VỪA ĐỦ đạt 300 board/giờ — không còn dư.**
>
> Điều đó phải nói rõ với khách hàng, kèm hai hệ quả:
>
> | Hệ quả | Nội dung |
> |---|---|
> | ⚠ Công thức sấy dài hơn 12 s | ⭐ **Không đạt 300 board/giờ** — và đây là giới hạn của **quá trình**, không phải của máy |
> | ⭐ Muốn dư năng lực | Phải rút thời gian sấy (đèn mạnh hơn / keo khác) hoặc ⭐ **thêm trạm sấy thứ hai chạy song song** |

### ⭐ Điều PLC sẽ đo trên DP-01

| Đo | Vì sao |
|---|---|
| Thời gian từng bước — ⭐ **gần nhất · trung bình · lớn nhất** | Thấy giá trị lớn nhất ăn sản lượng |
| ⭐⭐ **Phần trăm thời gian chờ của mỗi trạm** | ⭐ Xác nhận nút cổ chai bằng dữ liệu |
| Chu kỳ máy thật, đếm theo giờ | So với 12,0 s thiết kế |
| Thời gian dừng + mã báo động | Chương 43 — tính khả dụng |
| Số board đạt / lỗi | Tính chất lượng |
| ⭐ **Xu hướng thời gian bước theo tuần** | ⭐ Chương 53 mục 53.5 — **thấy cơ cấu đang mòn** |

> ⭐ **Hàng cuối là chỗ chương này gặp Chương 53.** Cùng một phép đo phục vụ hai mục đích: hôm nay nó
> chỉ ra nút cổ chai, sáu tháng sau nó chỉ ra thứ đang hỏng dần.
>
> Đó là lý do nên cài đặt nó **ngay từ đầu**, không phải khi có vấn đề.

---

## 55.9 Bẫy thường gặp

### 🔍 BẪY 1 — Cộng thời gian các trạm để ra chu kỳ

**Hiện tượng:** ⭐ báo sản lượng thấp hơn thực tế nhiều → mất hợp đồng không đáng.
**Cách sửa:** chu kỳ = **trạm chậm nhất**, không phải tổng (mục 55.3).

### 🔍 BẪY 2 — Tối ưu trạm không phải nút cổ chai

**Hiện tượng:** ⭐⭐ đúng cỗ máy ở mục 55.1 — nhanh gấp đôi, **sản lượng không đổi**.
**Cách sửa:** tìm nút cổ chai trước, bằng ⭐ **phần trăm thời gian chờ** (mục 55.4).

### 🔍 BẪY 3 — Quên rằng nút cổ chai di chuyển

**Hiện tượng:** đầu tư tiếp vào trạm cũ mà sản lượng không tăng thêm nữa.
**Cách sửa:** sau mỗi cải tiến, ⭐ **đo lại** để biết nút cổ chai đã chuyển đi đâu (mục 55.3).

### 🔍 BẪY 4 — Áp công thức "trạm chậm nhất" cho máy không có đệm

**Hiện tượng:** ⚠ tính ra 12 s, thực tế 13,5 s — thiếu **thời gian chuyển** giữa các trạm.
**Cách sửa:** máy không đệm thì cộng thời gian chuyển; ⭐ cân nhắc **thêm một chỗ đệm** (mục 55.3).

### 🔍 BẪY 5 — Nhầm chu kỳ với thời gian đi hết máy

**Hiện tượng:** báo sai sản lượng, hoặc tính sai thời gian xả máy khi đổi lô.
**Cách sửa:** hai khái niệm khác nhau — mục 55.2.

### 🔍 BẪY 6 — Báo con số lý thuyết như con số thật

**Hiện tượng:** ⚠ nghiệm thu không đạt vì thực tế cao hơn lý thuyết **10–30 %**.
**Cách sửa:** nói rõ con số là lý thuyết hay đo thật; có hệ số dự phòng (mục 55.4).

### 🔍 BẪY 7 — Chỉ lưu thời gian trung bình

**Hiện tượng:** ⭐ trung bình đẹp, sản lượng vẫn thiếu — vì thỉnh thoảng có chu kỳ **rất dài** mà số
trung bình che mất.
**Cách sửa:** lưu cả ⭐ **giá trị lớn nhất** (mục 55.4).

### 🔍 BẪY 8 — Bộ định thời "cho chắc" không ai gỡ

**Hiện tượng:** vài giây mỗi chu kỳ mất vào các `Timer 500 ms` rải rác.
**Cách sửa:** ⭐ thay bằng **chờ tín hiệu phản hồi thật** (mục 55.5, Chương 9 mục 9.6).

### 🔍 BẪY 9 — Song song hoá cả kiểm tra an toàn

**Hiện tượng:** ⚠⚠ tiết kiệm 200 ms, tạo ra một cách gây thương tích.
**Cách sửa:** ⚠ ranh giới ở mục 55.5 — **không có ngoại lệ về năng suất** (Chương 47).

### 🔍 BẪY 10 — Rút thời gian của quá trình vật lý

**Hiện tượng:** ⚠⚠ chu kỳ giảm, nhưng keo chưa cứng → **tăng sản lượng hàng lỗi**.
**Cách sửa:** thời gian quá trình là **yêu cầu**, không phải tham số tối ưu (mục 55.5).

### 🔍 BẪY 11 — Tối ưu chu kỳ trong khi máy dừng 30 phút mỗi ca

**Hiện tượng:** ⭐ công sức lớn đổi lấy 9 %, trong khi **thời gian chết** đang ăn nhiều hơn thế.
**Cách sửa:** đo cả ba thành phần OEE trước khi chọn việc (mục 55.6–55.7).

### 🔍 BẪY 12 — Lấy chu kỳ thực tế làm chu kỳ thiết kế khi tính OEE

**Hiện tượng:** ⚠⚠ hiệu suất **luôn ~100 %**, chỉ số mất hết ý nghĩa, tổn thất tốc độ thành vô hình.
**Cách sửa:** chu kỳ thiết kế **cố định**, ghi rõ nguồn gốc, ⚠ không đổi để làm đẹp số (mục 55.7).

---

## 55.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Chu kỳ máy là gì | Khoảng thời gian giữa **hai sản phẩm liên tiếp ra khỏi máy** |
| ⚠ Không phải là gì | **Thời gian một sản phẩm đi hết máy** (đó là thời gian thông qua) |
| Công thức sản lượng | `UPH = 3600 ÷ chu kỳ (giây)` |
| ⭐⭐ Chu kỳ máy nhiều trạm | **Bằng trạm chậm nhất**, không phải tổng |
| Trạm chậm nhất gọi là gì | ⭐ **Nút cổ chai** |
| ⭐⭐ Tối ưu ở đâu mới có tác dụng | **Chỉ ở nút cổ chai** |
| Sau khi cải tiến nút cổ chai | ⭐ **Nút cổ chai chuyển sang trạm khác** — đo lại |
| ⚠ Máy không có đệm | ⭐ Cộng thêm **thời gian chuyển giữa các trạm** |
| Lý thuyết so với thực tế | ⚠ Thực tế thường cao hơn **10–30 %** |
| ⭐⭐ Cách tìm nút cổ chai bằng dữ liệu | **Phần trăm thời gian chờ** — trạm chờ ~0 % là nút cổ chai |
| Lưu mấy con số cho mỗi bước | ⭐ **Ba**: gần nhất · trung bình · **lớn nhất** |
| Vì sao cần giá trị lớn nhất | Trung bình che mất các chu kỳ dài bất thường |
| Cách rút chu kỳ rẻ nhất | ⭐ **Song song hoá** — và gỡ các bộ định "cho chắc" |
| ⚠⚠ Không bao giờ song song hoá | **Kiểm tra an toàn** · xác nhận vị trí · khoá liên động · thời gian quá trình vật lý |
| Công thức OEE | Khả dụng × Hiệu suất × Chất lượng |
| ⭐ Giá trị của OEE nằm ở đâu | **Ba con số thành phần**, không phải con số gộp |
| ⚠⚠ Cách bóp méo phổ biến nhất | **Lấy chu kỳ thực tế làm chu kỳ thiết kế** → hiệu suất luôn ~100 % |
| ⭐ OEE dùng để làm gì | **Tìm chỗ cải tiến** — không phải chấm điểm người |
| ⚠ Nút cổ chai của DP-01 | ⭐ **Trạm 2 — sấy UV (6–12 s)**; với công thức 12 s thì **chỉ vừa đủ** 300 board/giờ |

---

## 55.11 Tự kiểm

1. ⭐⭐ Kể lại sự việc ở mục 55.1. Vì sao cải tiến gấp đôi mà sản lượng không đổi?
2. Phân biệt **chu kỳ máy** và **thời gian thông qua**. Cái nào quyết định sản lượng?
3. Máy ba trạm mất 5 s, 9 s, 7 s, có đệm giữa các trạm. Chu kỳ là bao nhiêu? UPH là bao nhiêu?
4. ⭐ Vẫn máy đó, bạn rút trạm 2 xuống 4 s. Chu kỳ mới là bao nhiêu? Nút cổ chai bây giờ ở đâu?
5. ⭐ Rút tiếp trạm 2 xuống 3 s có tăng sản lượng không? Vì sao? Bài học là gì?
6. ⚠ Vẫn máy ở câu 3 nhưng **không có đệm**, thời gian chuyển giữa các trạm là 1,5 s. Chu kỳ là bao
   nhiêu?
7. ⭐⭐ Mô tả cách tìm nút cổ chai bằng **phần trăm thời gian chờ**. Vì sao nó tốt hơn phỏng đoán?
8. ⭐ Vì sao phải lưu **giá trị lớn nhất** chứ không chỉ trung bình của thời gian mỗi bước?
9. Nêu bốn câu hỏi để tìm việc có thể song song hoá. Câu nào nên soát lại trên mọi máy?
10. ⚠⚠ Nêu bốn thứ **không bao giờ** được song song hoá. Vì sao "thời gian quá trình vật lý" là cái
    bẫy tinh vi nhất?
11. Nêu sáu nguồn thời gian chết ngoài chu kỳ. Nguồn nào thường lớn nhất?
12. ⭐ Tính OEE cho ca sau: dự định 420 phút, dừng lỗi 60 phút, chu kỳ thiết kế 10 s, làm ra 1900 sản
    phẩm, 50 sản phẩm lỗi. Ba thành phần nói gì về nơi cần cải tiến?
13. ⚠⚠ Nêu năm cách bóp méo OEE. Cách nào nguy hiểm nhất, và vì sao nó trông hợp lý?
14. ⭐⭐ Vì sao trên DP-01 việc rút thời gian sấy UV **không phải** việc của người lập trình?

> Câu 5, 7, 10 và 13 là bốn câu phân loại. Câu 1 và 14 gắn với nhau: ⭐ **cả hai đều nói rằng công
> sức đặt sai chỗ không tạo ra kết quả, dù công sức đó rất thật.**

---

### Chương tiếp theo

Chương 56 — **Nâng cấp máy cũ (retrofit)**. Đến đây sách đã đi hết một cỗ máy làm mới. Nhưng phần
lớn công việc thực tế là **sửa máy đã có** — thường là máy không còn tài liệu, và người viết nó đã
đi từ lâu.

### Nguồn tham khảo chương 55

- **Số liệu đã chốt của DP-01** — Phụ lục J §7.1: 300 board/giờ, chu kỳ 12,0 s, trạm 2 sấy UV 6–12 s.
- IEC 62264 (bộ) — *Enterprise-control system integration*: mô hình dữ liệu sản xuất, nền cho việc
  đưa số liệu năng suất lên hệ thống trên. *(tiêu chuẩn có bản quyền)*
- ISO 22400 (bộ) — *Key performance indicators for manufacturing operations management*: ⭐ **định
  nghĩa chuẩn hoá cho các chỉ số năng suất**, gồm cả nhóm chỉ số mà OEE thuộc về. Dùng nó khi cần
  con số **so sánh được giữa các nhà máy**.
- Phép đo thời gian bước và bộ đếm — Chương 12 (vùng nhớ giữ được), Chương 21 (trình tự), Chương 43
  (báo động), Chương 53 mục 53.5 (bảo trì).

> ⚠ **Giới hạn.** Công thức OEE ở mục 55.7 là dạng phổ biến nhất, nhưng ⚠ **định nghĩa chi tiết khác
> nhau giữa các nơi** — cái gì tính là "thời gian dự định", dừng ngắn bao nhiêu thì bỏ qua, hàng sửa
> lại tính thế nào. ⭐ **Trước khi báo cáo một con số OEE, hãy ghi rõ định nghĩa bạn dùng** — và khi
> so sánh hai con số, kiểm tra chúng cùng định nghĩa. Nếu cần con số so sánh được với bên ngoài, dùng
> định nghĩa trong ISO 22400 thay vì tự đặt.
