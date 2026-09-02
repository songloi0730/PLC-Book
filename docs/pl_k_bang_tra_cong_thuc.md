
# Phụ lục K — Bảng tra công thức tổng hợp

> **Tài liệu tra cứu.** Mọi công thức trong sách gom về một chỗ, mỗi công thức kèm cột ⭐ **điều kiện
> áp dụng** — vì một công thức dùng sai điều kiện còn tệ hơn không có công thức.

---

> ⚠ **Cách dùng.** Bảng này để **tra nhanh khi bạn đã hiểu**. Nếu một công thức bạn chưa hiểu vì sao
> nó như vậy, hãy quay lại chương được dẫn — ⭐ **áp một công thức mà không hiểu điều kiện của nó là
> cách tạo ra những con số sai trông rất thuyết phục**.

---

## K.1 Analog và quy đổi thang đo

### Quy đổi tuyến tính giá trị thô → giá trị kỹ thuật

```text
                 (Thô − Thô_min)
KyThuat  =  ─────────────────────────  ×  (KT_max − KT_min)  +  KT_min
              (Thô_max − Thô_min)
```

| Hạng mục | Nội dung |
|---|---|
| ⭐ **Điều kiện áp dụng** | Quan hệ **tuyến tính** giữa tín hiệu và đại lượng đo |
| ⚠ **Không áp dụng cho** | Cặp nhiệt điện và RTD ở dải rộng (quan hệ **không tuyến tính**) — dùng module chuyên dụng hoặc bảng tra (Ch.33) |
| ⚠ Bẫy | **Tràn số và chia số nguyên** — xem K.6 và Chương 14 |
| Chương | 31 mục 31.4 |

### Ví dụ trên DP-01

```text
AI_GluePress: 4–20 mA → 0–6 bar, module cho giá trị thô 0–27648
Thô = 13824  →  (13824 − 0) / 27648 × (6 − 0) + 0  =  3,00 bar
```

### ⭐ Ngưỡng phát hiện lỗi cảm biến 4–20 mA

| Điều kiện | Nghĩa |
|---|---|
| Dòng **< 3,6 mA** | ⭐⭐ **Đứt dây / hỏng cảm biến** — không phải giá trị đo bằng 0 |
| Dòng **> 21 mA** | Ngắn mạch hoặc lỗi cảm biến |
| ⚠ Điều kiện áp dụng | ⭐ **Chỉ dùng được với 4–20 mA**; tín hiệu 0–10 V và 0–20 mA **không phân biệt được đứt dây** |
| Chương | 31 mục 31.7 |

> ⭐⭐ **Đây là lý do 4–20 mA được ưa dùng hơn 0–10 V cho phép đo quan trọng:** không phải vì chống
> nhiễu tốt hơn (dù nó cũng đúng), mà vì ⭐ **0 mA là một trạng thái không thể xảy ra khi mọi thứ
> bình thường** — nên nó dùng được làm dấu hiệu lỗi.

---

## K.2 Khí nén

### Lực xy-lanh

```text
Lực đẩy (N)  =  Áp suất (bar) × 10 × Diện tích piston (cm²)
Lực kéo (N)  =  Áp suất (bar) × 10 × (Diện tích piston − Diện tích cần) (cm²)
```

| Hạng mục | Nội dung |
|---|---|
| ⭐ **Điều kiện áp dụng** | Lực **lý thuyết**; ⚠ thực tế thấp hơn do ma sát |
| ⭐ Hệ số thực dụng | Lấy **70–85 %** lực lý thuyết; ⚠ dùng con số của nhà sản xuất khi có |
| ⚠ Bẫy | ⭐ **Lực kéo LUÔN nhỏ hơn lực đẩy** vì cần piston chiếm mất diện tích — ⚠ và người ta hay quên khi hành trình về mới là hành trình phải sinh lực |
| Chương | 5 mục 5.4 |

```text
Diện tích piston (cm²)  =  π × (Đường kính mm ÷ 20)²
```

### Lưu lượng khí tiêu thụ

```text
Thể tích một hành trình (L)  =  Diện tích (cm²) × Hành trình (cm) ÷ 1000
Lưu lượng (L/phút, quy về áp suất khí quyển)
        =  Thể tích × (Áp suất bar + 1) × Số hành trình/phút
```

| Hạng mục | Nội dung |
|---|---|
| ⭐ Điều kiện áp dụng | Tính **cỡ máy nén và cỡ ống**, không phải tính tốc độ |
| ⚠ Nhớ cộng | Cả hành trình **đi và về**; và ⭐ **rò rỉ** — thực tế đáng kể |
| Chương | 5 mục 5.7 |

---

## K.3 Điện và nguồn

### Công suất nguồn 24 V

```text
Dòng cần  =  Tổng dòng tại BƯỚC CÓ NHIỀU TẢI NHẤT  ×  1,3 … 1,5
```

| Hạng mục | Nội dung |
|---|---|
| ⭐⭐ **Điều kiện áp dụng** | ⭐ **Bước có nhiều tải nhất**, không phải tổng tất cả tải — hầu hết tải không cùng bật |
| ⚠ Nhưng phải kiểm | ⭐ Có bước nào **mọi thứ cùng bật** không? (về gốc, kiểm đèn, reset) |
| Hệ số 1,3–1,5 | Dự phòng cho: dòng khởi động, mở rộng sau này, và ⚠ **sụt áp trên dây dài** |
| Chương | 8 mục 8.7 |

### Tuổi thọ đóng cắt / uốn cáp

```text
Số lần / năm  =  Số lần mỗi chu trình × Chu trình/giờ × Giờ/năm
```

| Hạng mục | Nội dung |
|---|---|
| ⭐ Điều kiện áp dụng | So kết quả với **tuổi thọ trong datasheet**, không phải với cảm giác |
| ⚠ Với rơ-le | ⭐ **Tuổi thọ điện thấp hơn tuổi thọ cơ rất nhiều**, và phụ thuộc loại tải (tải cảm khắc nghiệt hơn) |
| ⚠ Với cáp trong xích | Phải là **cáp chịu uốn**; ⭐ và đúng **bán kính uốn tối thiểu** |
| Chương | 9 mục 9.3 · 49 mục 49.7 |

### Ví dụ DP-01

```text
Van kẹp:   2 lần/chu trình × 300 chu trình/giờ × 4800 giờ/năm = 2 880 000 lần/năm
Cáp xích:  1 lần/chu trình × 300 chu trình/giờ × 4800 giờ/năm = 1 440 000 lần/năm
           (4800 giờ = 2 ca × 8 giờ × 300 ngày)
```

### Ngưỡng bảo trì

```text
Ngưỡng nhắc     =  Tuổi thọ datasheet × 0,7
Ngưỡng cảnh báo =  Tuổi thọ datasheet × 0,9
```

| Hạng mục | Nội dung |
|---|---|
| ⭐ Điều kiện áp dụng | Bộ đếm phải ⭐ **sống sót qua mất điện VÀ qua lần nạp chương trình** — ⚠ kiểm tra thực tế |
| ⚠ Bắt buộc | Ngưỡng chỉ **nhắc**, ⚠ **không được dừng máy** |
| Chương | 53 mục 53.5 |

---

## K.4 Chu kỳ và năng suất

### Sản lượng giờ

```text
UPH  =  3600  ÷  Chu kỳ máy (giây)
```

| Hạng mục | Nội dung |
|---|---|
| ⚠ **Chu kỳ máy là gì** | Khoảng thời gian giữa **hai sản phẩm liên tiếp RA KHỎI máy** |
| ⚠ **Không phải** | Thời gian một sản phẩm **đi hết máy** (đó là *thời gian thông qua*) |
| Chương | 55 mục 55.2 |

### ⭐⭐ Chu kỳ máy nhiều trạm

```text
Có đệm giữa các trạm:      Chu kỳ = thời gian trạm CHẬM NHẤT
Không có đệm:              Chu kỳ = thời gian trạm chậm nhất + thời gian chuyển giữa trạm
```

| Hạng mục | Nội dung |
|---|---|
| ⭐⭐ **Điều kiện áp dụng** | Các trạm **chạy song song trên các sản phẩm khác nhau** |
| ⚠ Không áp dụng khi | Các trạm **dùng chung tài nguyên** (một robot phục vụ nhiều trạm) |
| ⭐⭐ Hệ quả quan trọng nhất | **Tối ưu trạm không phải nút cổ chai KHÔNG tăng sản lượng** |
| ⚠ Bẫy phổ biến nhất | ⭐ **Cộng thời gian các trạm lại** — cho con số thấp hơn thực tế nhiều |
| Chương | 55 mục 55.3 |

### ⭐ Tìm nút cổ chai bằng dữ liệu

```text
Với mỗi trạm:  % thời gian chờ  =  Thời gian chờ  ÷  Tổng thời gian  × 100

Trạm có % thời gian chờ ≈ 0  →  ⭐ ĐÓ LÀ NÚT CỔ CHAI
```

| Hạng mục | Nội dung |
|---|---|
| ⭐ Điều kiện áp dụng | Đo trong ⭐ **giai đoạn chạy ổn định**, không tính lúc khởi động hay đổi lô |
| ⭐ Ưu điểm | Bắt được cả nút cổ chai **nằm ngoài máy** (máy trước không cấp đủ hàng) |
| Chương | 55 mục 55.4 |

### OEE

```text
OEE  =  Khả dụng  ×  Hiệu suất  ×  Chất lượng

Khả dụng   =  Thời gian chạy  ÷  Thời gian dự định
Hiệu suất  =  (Chu kỳ THIẾT KẾ × Số SP làm ra)  ÷  Thời gian chạy
Chất lượng =  Số SP đạt  ÷  Số SP làm ra
```

| Hạng mục | Nội dung |
|---|---|
| ⚠⚠ **Điều kiện áp dụng** | ⭐⭐ **Chu kỳ trong công thức Hiệu suất phải là chu kỳ THIẾT KẾ, cố định** |
| ⚠⚠ Cách bóp méo phổ biến nhất | Lấy **chu kỳ thực tế** làm chu kỳ thiết kế → ⭐ **hiệu suất luôn ~100 %**, chỉ số mất hết ý nghĩa |
| ⚠ So sánh giữa các máy | ⭐ **Chỉ có nghĩa khi cùng định nghĩa** — ghi rõ định nghĩa khi báo cáo |
| ⭐ Giá trị nằm ở đâu | **Ba con số thành phần**, không phải con số gộp |
| Chương | 55 mục 55.7 |

---

## K.5 Thời gian quét và bộ đếm xung

### Ước lượng thời gian quét

```text
Thời gian quét  ≈  Thời gian đọc I/O  +  Thời gian chạy chương trình  +  Thời gian ghi I/O
                    +  Tác vụ hệ thống (truyền thông, chẩn đoán)
```

| Hạng mục | Nội dung |
|---|---|
| ⚠ **Điều kiện áp dụng** | Đây là **ước lượng**, không phải bảo đảm — ⭐ **đo thời gian quét thật trên máy** |
| ⚠ Nhớ rằng | Thời gian quét **thay đổi theo đường chạy** trong chương trình — quan tâm **giá trị lớn nhất**, không phải trung bình |
| ⚠⚠ Bẫy khi đổi PLC | ⭐ **PLC mới thường quét nhanh hơn nhiều** — logic dựa vào vòng quét sẽ chạy khác (Ch.56) |
| Chương | 7 · 19 · 56 mục 56.4 |

### ⭐ Khi nào cần bộ đếm xung tốc độ cao

```text
Tần số xung (Hz)  =  Số xung mỗi vòng  ×  Số vòng mỗi giây

Nếu  Tần số xung  >  1 / (2 × Thời gian quét)   →  ⭐ PHẢI dùng bộ đếm tốc độ cao
```

| Hạng mục | Nội dung |
|---|---|
| ⭐⭐ **Vì sao chia 2** | Mỗi xung phải có ít nhất **hai lần quét** để nhận được cạnh lên và cạnh xuống |
| ⚠ Thực dụng | ⭐ **Lấy dự phòng rộng hơn nhiều** — thời gian quét không cố định, và bỏ sót xung là lỗi **âm thầm** |
| ⚠ Dấu hiệu đã sai | Giá trị đếm **thấp hơn thực tế và sai ngày càng nhiều** — không có báo động nào |
| Chương | 18 |

---

## K.6 Số học và kiểu dữ liệu

### ⚠ Dải giá trị các kiểu số nguyên thường gặp

| Kiểu | Số bit | Dải |
|---|---|---|
| `SINT` | 8 có dấu | −128 … 127 |
| `USINT` / `BYTE` | 8 không dấu | 0 … 255 |
| `INT` | 16 có dấu | ⭐ **−32 768 … 32 767** |
| `UINT` / `WORD` | 16 không dấu | 0 … 65 535 |
| `DINT` | 32 có dấu | ⭐ **−2 147 483 648 … 2 147 483 647** |
| `UDINT` / `DWORD` | 32 không dấu | 0 … 4 294 967 295 |

> ⚠⚠ **`INT` tràn ở 32 767 — con số này nhỏ hơn bạn tưởng.** Một bộ đếm sản lượng dùng `INT` tràn
> sau **32 767 sản phẩm** — với DP-01 ở 300 board/giờ, đó là **khoảng 4,5 ngày**.
>
> ⭐ Dùng `DINT` cho mọi bộ đếm tích luỹ. Xem Chương 14.

### ⚠ Thứ tự phép tính để tránh tràn

```text
✗ SAI:   KetQua := (Tho * KTmax) / ThoMax        // ← tràn ở phép nhân
✓ ĐÚNG:  KetQua := Tho * (KTmax / ThoMax)        // ← mất độ chính xác nếu chia số nguyên
✓ TỐT:   KetQua := DINT_TO_REAL(Tho) * KTmax / ThoMax    // ← ép sang số thực trước
```

| Hạng mục | Nội dung |
|---|---|
| ⚠⚠ **Bẫy chính** | ⭐ **Chia số nguyên cắt bỏ phần thập phân** — `7 / 2 = 3`, không phải 3,5 |
| ⭐ Quy tắc thực dụng | ⭐ **Ép sang số thực trước khi tính**, ép về số nguyên sau khi tính xong |
| ⚠ Với số thực | ⭐ **Không so sánh bằng** hai số thực — so bằng khoảng dung sai |
| Chương | 14 |

---

## K.7 Tín hiệu và dây dẫn

### ⭐ Vỏ chống nhiễu nối mấy đầu

| Loại cáp | Nối vỏ | Lý do |
|---|---|---|
| ⭐ **Tín hiệu analog, cảm biến** | **Một đầu** — thường phía tủ | Tránh dòng vòng qua vỏ ở tần số thấp |
| ⭐ **Cáp động cơ biến tần** | **Hai đầu** | Chắn nhiễu tần số cao — bài toán khác |
| Cáp mạng | Theo hướng dẫn nhà sản xuất (thường hai đầu) | |

| Hạng mục | Nội dung |
|---|---|
| ⭐⭐ **Điều kiện tiên quyết cho cả ba** | **Kẹp trọn vòng 360°** — bện vỏ thành sợi rồi vặn vít làm vỏ mất phần lớn tác dụng |
| Chương | 31 mục 31.6 · 36 mục 36.7 · 49 mục 49.4 |

### ⚠ Nối đất

```text
0 V và PE nối với nhau ở  ĐÚNG MỘT ĐIỂM  — thường tại bộ nguồn, và ghi vào bản vẽ
```

| Hạng mục | Nội dung |
|---|---|
| ⚠⚠ **Vì sao** | Nối nhiều điểm → **vòng lặp đất**: dòng 24 V có nhiều đường về, chạy qua khung máy và máng cáp |
| ⭐ Triệu chứng vòng lặp đất | Analog run · mạng rớt gói · nhiễu tăng khi thiết bị công suất chạy |
| ⭐ Cách kiểm nhanh | ⭐ **Đo điện áp xoay chiều giữa hai điểm đất ở hai đầu máy** — có vài vôn là có vấn đề |
| Chương | 49 mục 49.4 |

---

## K.8 Bảng tra nhanh — công thức nào ở chương nào

| Cần tính | Công thức ở | Chương gốc |
|---|---|---|
| Quy đổi giá trị analog | K.1 | 31 |
| Phát hiện đứt dây cảm biến 4–20 mA | K.1 | 31 |
| Lực xy-lanh | K.2 | 5 |
| Lưu lượng khí | K.2 | 5 |
| Công suất nguồn 24 V | K.3 | 8 |
| Tuổi thọ van / rơ-le / cáp xích | K.3 | 9, 49 |
| Ngưỡng bảo trì | K.3 | 53 |
| Sản lượng giờ (UPH) | K.4 | 55 |
| ⭐ **Chu kỳ máy nhiều trạm** | K.4 | 55 |
| ⭐ **Tìm nút cổ chai** | K.4 | 55 |
| OEE | K.4 | 55 |
| Thời gian quét | K.5 | 7, 19 |
| ⭐ **Khi nào cần bộ đếm tốc độ cao** | K.5 | 18 |
| Dải kiểu dữ liệu, chống tràn | K.6 | 14 |
| Vỏ chống nhiễu, nối đất | K.7 | 31, 36, 49 |

---

> ⚠⚠ **Nhắc lại giới hạn.** Các công thức ở đây là ⭐ **công cụ ước lượng và kiểm tra**, không phải
> căn cứ thiết kế.
>
> Cho thiết kế thật: dùng **datasheet của thiết bị cụ thể** và **tiêu chuẩn hiện hành tại thị trường
> của bạn**. ⚠ Phần điện lực, tiết diện dây, tính toán bảo vệ và toàn bộ phần an toàn phải do
> **người có thẩm quyền** thực hiện — bảng này **không thay thế** thiết kế điện.
