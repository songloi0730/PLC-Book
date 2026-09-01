# Chương 34 — Cân & đo lực: load cell, giám sát lực/mô-men

> **Lát cắt máy mẫu:** 3 — thêm analog (áp suất, nhiệt độ, cường độ UV) và trục gantry XY+Z servo.

---

## 34.1 Bài toán: connector cắm "xong" mà không tiếp xúc

Một trạm cắm connector vào board. Cơ cấu ép xuống, một cảm biến tiệm cận báo **đã tới vị trí cuối**,
chương trình coi là xong và cho board đi tiếp.

Tỉ lệ lỗi ở công đoạn kiểm cuối tăng dần. Khi mổ xẻ các board lỗi, phát hiện: connector **cắm nghiêng**
hoặc **chưa vào hết chân**, nhưng cơ cấu vẫn đi tới vị trí cuối vì nó đủ lực để làm cong chân
connector thay vì cắm đúng.

Cảm biến vị trí trả lời câu hỏi: *"cơ cấu đã tới chỗ chưa?"* — và câu trả lời là **có**.

Câu hỏi đáng lẽ phải hỏi là: *"nó tới chỗ đó với lực bao nhiêu?"*

> ⭐ **Một connector cắm đúng và một connector cắm cong đều kết thúc ở cùng một vị trí. Chúng khác
> nhau ở ĐƯỜNG ĐI TỚI ĐÓ.**

Chương này về cách đo lực, và quan trọng hơn — về cách dùng **quan hệ giữa lực và vị trí** làm tiêu
chí chất lượng.

---

## 34.2 Load cell — nguyên lý đủ dùng

**Load cell** *(cảm biến lực / cảm biến cân)* biến lực thành tín hiệu điện bằng **cầu điện trở**
*(strain gauge bridge)*.

### Cách hoạt động

Bốn điện trở dán trên một khối kim loại, đấu thành cầu Wheatstone. Khi khối kim loại biến dạng dưới
tác dụng của lực, điện trở đổi rất nhỏ, và cầu mất cân bằng — sinh ra một **điện áp lệch**.

```text
        +Vkích
          │
      ┌───┴───┐
     R1       R2
      │       │
   +Vra ───────── −Vra      ← điện áp ra, RẤT NHỎ
      │       │
     R3       R4
      └───┬───┘
          │
        −Vkích
```

> ⚠ **Điện áp ra rất nhỏ — cỡ mi-li-vôn.** Đó là lý do load cell **luôn cần bộ khuếch đại**, và là
> lý do nó **rất nhạy với nhiễu** (mục 34.4).

### Ba thông số phải đọc

| Thông số | Nghĩa | ⚠ Vì sao quan trọng |
|---|---|---|
| **Tải định mức** *(rated capacity)* | Lực tối đa đo được | ⭐ Chọn **vừa đủ** — sai số tính theo % tải định mức (Chương 32, mục 32.3) |
| **Độ nhạy** (mV/V) | Điện áp ra trên mỗi vôn kích, ở tải định mức | Quyết định cấu hình bộ khuếch đại |
| ⚠ **Quá tải cho phép** | Lực vượt định mức mà cảm biến còn chịu được | Vượt ngưỡng này là **hỏng vĩnh viễn**, không phục hồi |

> ⚠⚠ **Quá tải là cách phổ biến nhất làm hỏng load cell**, và nó thường xảy ra **không phải khi máy
> chạy** mà khi lắp đặt, vận chuyển, hoặc khi ai đó tì tay lên cơ cấu.
>
> Với cơ cấu ép, phải có **cữ cơ khí** giới hạn hành trình sao cho lực không bao giờ vượt quá tải cho
> phép — cùng nguyên tắc ba lớp ở Chương 37, mục 37.6.

### Hai cách nối vào PLC

| Cách | Nghĩa | ✅ / ⚠ |
|---|---|---|
| **Module cân chuyên dụng** | Module PLC có sẵn mạch kích, khuếch đại, lọc | ⭐ Đơn giản nhất; tốc độ đọc thường đủ |
| **Bộ khuếch đại rời** → analog | Bộ khuếch đại ngoài đưa ra 4–20 mA hoặc 0–10 V | Linh hoạt; ⚠ thêm một tầng có thể sai |

> 💡 Với **giám sát lực theo hành trình** (mục 34.5), tốc độ đọc quan trọng — cần đủ nhanh để lấy được
> nhiều điểm trong một chu trình ép chỉ kéo dài dưới một giây. ⚠ **Kiểm tốc độ cập nhật của module
> trước khi thiết kế**, cùng vấn đề với module nhiệt độ ở Chương 33 mục 33.11.

---

## 34.3 Hiệu chuẩn bằng quả cân chuẩn

Với cân, **hiệu chuẩn là bắt buộc** — không phải tuỳ chọn. Chương 32 mục 32.8 đã phân biệt hiệu chuẩn
với đặt dải; ở đây là quy trình cụ thể.

| Bước | Việc | ⚠ Chú ý |
|---|---|---|
| 1 | **Zero** — không tải, đặt điểm 0 | ⚠ Phải có **đúng phần cơ khí sẽ luôn nằm trên cảm biến** (đồ gá, mâm) |
| 2 | **Span** — đặt quả cân chuẩn đã biết, chỉnh cho khớp | Dùng khối lượng gần **cuối dải làm việc**, không phải cuối dải cảm biến |
| 3 | **Kiểm tuyến tính** — thử vài mức trung gian | Sai lệch lớn ở giữa là dấu hiệu cơ khí có vấn đề |
| 4 | **Kiểm lặp lại** — đặt và nhấc cùng một quả cân nhiều lần | ⭐ Đây là phép kiểm nói lên nhiều nhất |
| 5 | **Ghi hồ sơ** — ngày, quả cân dùng, kết quả | Cần khi khách hàng hỏi |

> ⭐ **Bước 4 là bước có giá trị nhất và hay bị bỏ.**
> Một cân có thể **chính xác mà không lặp lại**: đặt 1 kg lần đầu ra 1,00 kg, lần hai ra 1,03 kg, lần
> ba ra 0,98 kg. Trung bình đúng, nhưng từng phép đo thì không dùng được.
>
> Độ lặp lại kém gần như luôn là vấn đề **cơ khí**, không phải điện: ma sát ở cơ cấu dẫn hướng, cáp
> load cell bị kéo căng, đồ gá tì vào thành máy, hoặc bu-lông lỏng.

> ⚠ **Quả cân chuẩn phải có vết truy nguyên** nếu phép cân dùng cho mục đích thương mại hoặc cho hồ
> sơ chất lượng. Một cục sắt "khoảng 1 kg" không phải quả cân chuẩn (Chương 32, mục 32.8).

---

## 34.4 ⚠ Nhiễu — cơ học và điện

Load cell nhạy với cả hai loại nhiễu, và nhiễu **cơ học** thường lớn hơn nhiễu điện.

| Nguồn nhiễu | Biểu hiện | Cách xử lý |
|---|---|---|
| ⭐ **Rung cơ khí** từ máy bên cạnh, từ chính máy | Giá trị dao động khi không có gì đổi | Cách rung cho cơ cấu cân; lọc; ⭐ **đo khi cơ cấu đứng yên** |
| **Ma sát ở cơ cấu dẫn hướng** | Độ lặp lại kém, có trễ | Vấn đề cơ khí — sửa cơ khí, không sửa bằng phần mềm |
| **Cáp load cell bị kéo, bị rung** | Giá trị nhảy | Cố định cáp; ⚠ **không cắt ngắn hay nối dài** cáp load cell tuỳ tiện |
| **Nhiệt độ đổi** | Giá trị trôi chậm | Bù nhiệt nếu module có; hoặc zero lại định kỳ |
| **Nhiễu điện** | Giá trị run | Cáp có vỏ chống nhiễu, nối vỏ theo hướng dẫn; tách xa cáp động lực (Chương 31, mục 31.6) |

> ⚠⚠ **Đừng nối dài hay cắt ngắn cáp load cell.**
> Nhiều load cell được **hiệu chuẩn cùng với cáp của nó** — điện trở cáp nằm trong phép hiệu chuẩn.
> Đổi chiều dài cáp là đổi kết quả.
>
> Nếu buộc phải nối dài, dùng load cell **6 dây** *(sense wires)*: hai dây phụ đo điện áp kích **tại
> cảm biến**, nên bộ khuếch đại bù được sụt áp trên cáp. Đây là cùng ý tưởng với RTD 3 dây ở Chương 33
> mục 33.4 — **đo và bù thay vì giả định**.

### ⚠ Lọc và độ trễ — nhắc lại từ Chương 32

Lọc mạnh làm giá trị mượt hơn nhưng **chậm hơn** (Chương 32, mục 32.6). Với cân tĩnh thì không sao.
Với **giám sát lực theo hành trình** thì độ trễ làm lệch đường cong lực–vị trí — và tiêu chí OK/NG
dựa trên đường cong đó.

> **Quy tắc: cân tĩnh lọc mạnh được; giám sát động thì lọc nhẹ.**

---

## 34.5 ⭐⭐ Cửa sổ lực–vị trí — tiêu chí OK/NG thật sự

Đây là mục quan trọng nhất chương, và là lý do chương này tồn tại trong một cuốn sách về lắp ráp điện
tử.

### Vì sao cảm biến ON/OFF không đủ

Quay lại mục 34.1. Cơ cấu ép đi tới vị trí cuối. Cảm biến báo "tới rồi". Nhưng:

| Tình huống | Vị trí cuối | Lực khi đi | Cảm biến vị trí thấy |
|---|---|---|---|
| ✅ Cắm đúng | Đạt | Tăng đều, đỉnh vừa phải | **OK** |
| ❌ Connector nghiêng | Đạt | ⚠ Lực **cao bất thường** ngay từ đầu | **OK** |
| ❌ Thiếu connector | Đạt | ⚠ Lực **gần bằng 0** suốt hành trình | **OK** |
| ❌ Có dị vật | Đạt | ⚠ Lực tăng vọt **sớm hơn bình thường** | **OK** |
| ❌ Chân cong | Đạt | Đường cong lực **khác hẳn** | **OK** |

**Năm tình huống, một kết quả.** Cảm biến vị trí không phân biệt được cái nào.

### Đường cong lực theo hành trình

Ghi lại **lực tại mỗi vị trí** trong suốt hành trình ép, ta được một đường cong:

```text
   lực
    ▲
    │                              ┌────┐  ← đỉnh khi chạm đáy
    │                          ┌───┘    │
    │              ┌───────────┘        │
    │    ┌─────────┘  ← vùng cắm vào    │
    │────┘  ← tiếp cận tự do            │
    └───────────────────────────────────┴──► vị trí
    0                                   hết hành trình
```

Đường cong này là **chữ ký** của một lần lắp ráp đúng. Lần nào khác chữ ký đó là lần có vấn đề.

### Cửa sổ lực–vị trí

Cách dùng thực dụng: định nghĩa các **cửa sổ** — vùng mà lực **phải** nằm trong tại một khoảng vị trí
nhất định.

```text
   lực
    ▲
    │           ┌╌╌╌╌╌╌╌┐        ┌╌╌╌╌╌╌╌╌┐
    │           ╎ CỬA SỔ ╎        ╎ CỬA SỔ ╎
    │           ╎   2    ╎        ╎   3    ╎
    │  ┌╌╌╌╌┐   └╌╌╌╌╌╌╌┘        └╌╌╌╌╌╌╌╌┘
    │  ╎ CS ╎
    │  ╎ 1  ╎     ← đường cong phải đi QUA cả ba cửa sổ
    └──└╌╌╌╌┘──────────────────────────────────► vị trí
```

| Cửa sổ | Kiểm gì | Bắt được lỗi gì |
|---|---|---|
| **1 — tiếp cận** | Lực phải **thấp** | Có dị vật; cơ cấu kẹt |
| **2 — cắm vào** | Lực trong dải giữa | Connector nghiêng (lực cao); thiếu connector (lực thấp) |
| **3 — chạm đáy** | Lực đạt đỉnh trong dải | Chưa vào hết; ép quá mạnh |

> ⭐ **Tiêu chí OK là: đường cong đi qua ĐỦ cả ba cửa sổ.** Trượt một cửa sổ nào là NG, và ⭐ **cửa sổ
> nào trượt cho biết lỗi gì** — đây là chẩn đoán, không chỉ là phán quyết.
>
> Đây chính là nguyên tắc "thông báo lỗi phải nói làm gì tiếp" (Chương 44) áp cho kiểm chất lượng.

### Hiện thực trên PLC

```iecst
// Ghi mẫu lực theo vị trí trong lúc ép
IF M_PressActive AND (ZPositionX100 <> LastSampledPos) THEN
    // Cửa sổ 1 — tiếp cận, lực phải thấp
    IF ZPositionX100 >= W1_POS_MIN AND ZPositionX100 <= W1_POS_MAX THEN
        IF ForceX10 > W1_FORCE_MAX THEN
            M_PressNg := TRUE;  M_NgReason := 1;      // dị vật hoặc kẹt
        END_IF;
        M_W1Passed := TRUE;
    END_IF;

    // Cửa sổ 3 — chạm đáy, lực phải đạt đỉnh trong dải
    IF ZPositionX100 >= W3_POS_MIN THEN
        IF ForceX10 < W3_FORCE_MIN THEN
            M_PressNg := TRUE;  M_NgReason := 3;      // chưa vào hết
        ELSIF ForceX10 > W3_FORCE_MAX THEN
            M_PressNg := TRUE;  M_NgReason := 4;      // ép quá mạnh
        END_IF;
        M_W3Passed := TRUE;
    END_IF;

    LastSampledPos := ZPositionX100;
END_IF;

// ⭐ Kết luận: phải đi QUA đủ mọi cửa sổ, không chỉ "không vi phạm cửa sổ nào"
IF M_PressDone THEN
    M_PressOk := M_W1Passed AND M_W2Passed AND M_W3Passed AND NOT M_PressNg;
END_IF;
```

> ⭐ **Dòng cuối là chỗ dễ sai nhất.**
> Kiểm "không vi phạm cửa sổ nào" là **chưa đủ** — nếu cơ cấu dừng sớm, nó không vi phạm cửa sổ 3 vì
> **nó chưa bao giờ tới đó**. Phải kiểm cả **đã đi qua** từng cửa sổ.
>
> Đây là cùng loại lỗi với "suy tư thế từ cảm biến đối diện" ở Chương 28: **vắng mặt bằng chứng không
> phải bằng chứng vắng mặt**.

### ⚠ Xây cửa sổ từ dữ liệu, không từ suy đoán

> **Đừng đặt giới hạn cửa sổ bằng cách đoán.**
> Quy trình đúng: chạy vài chục sản phẩm **tốt đã biết**, ghi lại đường cong, xem chúng phân tán thế
> nào, rồi đặt cửa sổ bao quanh vùng đó với biên hợp lý.
>
> Sau đó chạy vài sản phẩm **lỗi cố ý** — thiếu connector, đặt nghiêng, có dị vật — và xác nhận cửa
> sổ **bắt được chúng**. Đây chính là "thử tạo lỗi cố ý" ở Chương 52 mục 52.7, áp cho kiểm chất lượng.

---

## 34.6 Giám sát mô-men khi siết vít

Cùng ý tưởng, áp cho việc siết vít — và đây là ứng dụng phổ biến nhất của giám sát lực trong lắp ráp
điện tử.

| Đại lượng | Đo gì |
|---|---|
| **Mô-men** *(torque)* | Lực xoắn khi siết |
| **Góc** *(angle)* | Vít đã quay bao nhiêu độ |

Cùng logic cửa sổ, nhưng trên mặt phẳng **mô-men – góc**:

| Tình huống | Mô-men | Góc | Phát hiện bằng |
|---|---|---|---|
| ✅ Siết đúng | Đạt mô-men mục tiêu | Trong dải góc dự kiến | Cả hai trong cửa sổ |
| ❌ **Trờn ren** *(cross-thread)* | ⚠ Mô-men cao **sớm** | Góc nhỏ | Mô-men đạt ở góc quá nhỏ |
| ❌ **Cháy ren** *(stripped)* | Mô-men **không bao giờ đạt** | Góc rất lớn | Góc vượt trần |
| ❌ Thiếu vít | Mô-men gần 0 | Góc rất lớn | Cả hai |
| ❌ Vít ngắn / lỗ sâu | Mô-men đạt muộn | Góc lớn hơn dự kiến | Góc ngoài dải |

> ⭐ **Mô-men một mình không đủ** — đây là điểm mấu chốt.
> Một vít trờn ren đạt mô-men mục tiêu rất sớm và máy báo OK. Chỉ khi nhìn **mô-men cùng với góc** mới
> phân biệt được "siết chặt" với "trờn ren".
>
> Đây là cùng bài học với mục 34.5: **một đại lượng không đủ; quan hệ giữa hai đại lượng mới là chữ
> ký của quy trình đúng.**

Máy vặn vít công nghiệp hiện đại thường có sẵn chức năng này và trả kết quả OK/NG về PLC qua tín hiệu
số hoặc qua mạng — ⭐ tương tự nguyên tắc ở Chương 2: **mỗi bên làm việc mình giỏi**, PLC quyết định
làm gì tiếp với kết quả đó.

---

## 34.7 Khi nào **không** cần đo lực

Cân bằng lại — không phải trạm nào cũng cần.

| Không cần khi | Vì sao |
|---|---|
| **Thao tác không có lỗi im lặng** | Nếu sai thì thấy ngay bằng mắt hoặc bằng cảm biến vị trí |
| **Đã có kiểm tra ở công đoạn sau** | Kiểm điện, kiểm chức năng bắt được lỗi rẻ hơn |
| **Sản lượng thấp, kiểm bằng người** | Chi phí thiết bị và công cấu hình không đáng |
| ⚠ **Không ai xây và duy trì được cửa sổ** | Cửa sổ đặt sai còn tệ hơn không có — nó loại nhầm hàng tốt |

> ⚠ **Hàng cuối là hàng thật nhất.**
> Cửa sổ lực–vị trí cần **xây từ dữ liệu** và **xem lại khi quy trình đổi** — đổi nhà cung cấp
> connector, đổi lô vật liệu, cơ cấu mòn dần. Không có người làm việc đó thì sau vài tháng cửa sổ
> hoặc loại nhầm hàng tốt, hoặc bị nới rộng ra tới mức vô nghĩa.
>
> Cùng câu hỏi với Chương 35 mục 35.3 và Chương 20 mục 20.6: **ai sẽ duy trì cái này?**

---

## 34.8 Trên máy mẫu DP-01

DP-01 **không có** trạm ép hay siết vít, nên không có load cell trong bảng I/O. Nhưng nguyên tắc của
chương áp được vào hai chỗ:

### Nếu thêm trạm kiểm lực

Giả sử mở rộng DP-01 thêm một trạm cắm connector. Khi đó:

| Hạng mục | Quyết định |
|---|---|
| Cảm biến | Load cell trên trục ép, module cân chuyên dụng |
| ⚠ Bảo vệ quá tải | **Cữ cơ khí** giới hạn hành trình — không dựa vào phần mềm (mục 34.2, Chương 37 mục 37.6) |
| Tiêu chí OK/NG | ⭐ **Cửa sổ lực–vị trí**, không phải cảm biến vị trí đơn thuần |
| Kết quả NG | Đánh dấu board bằng **thanh ghi dịch** để loại ở cuối chuyền (Chương 19, mục 19.6) |
| Tham số cửa sổ | Trong **công thức sản phẩm** — mỗi mã hàng một bộ (Chương 29) |
| Ghi log | Lưu đường cong của board NG để phân tích sau (Chương 42) |

> ⭐ **Hàng "tham số cửa sổ trong công thức" là hệ quả trực tiếp của Chương 29.** Mỗi mã hàng có
> connector khác nhau, lực khác nhau — đây đúng là loại tham số phải tách khỏi logic.
>
> ⚠ Nhưng nhớ ràng buộc ở Chương 29 mục 29.2: **PLC vẫn phải kiểm dải hợp lệ** của các tham số cửa sổ.
> Một cửa sổ rộng vô lý làm mất tác dụng kiểm tra mà không ai biết.

### Nguyên tắc áp được ngay cho DP-01 hiện tại

Ý tưởng trung tâm của chương — **một đại lượng không đủ, quan hệ giữa hai đại lượng mới là chữ ký** —
áp được vào máy hiện tại mà không cần thêm thiết bị:

| Cặp đại lượng | Cho biết gì |
|---|---|
| **Công suất đèn UV đặt** ↔ **cường độ đo được** | ⭐ Sức khoẻ đèn — Chương 35, mục 35.11 |
| **Tốc độ chuyền đặt** ↔ **dòng động cơ** | ⭐ Tải cơ khí của chuyền — Chương 36, mục 36.8 |
| **Vị trí trục** ↔ **sai số bám** | ⭐ Cơ cấu có kẹt không — Chương 37, mục 37.2 |
| **Thời gian bước** ↔ **áp khí lúc đó** | Chẩn đoán cỗ máy ở Chương 22, mục 22.9 |

> ⭐ **Bốn cặp trên là cùng một kỹ thuật.** Bạn đã gặp nó bốn lần dưới bốn hình dạng khác nhau, và
> chương này đặt tên cho nó: **so lệnh với kết quả, và theo dõi quan hệ giữa chúng.**
>
> Đó là cách phát hiện những hỏng hóc **trôi dần** mà không cảm biến đơn lẻ nào thấy được
> (Chương 33, mục 33.9 câu 4; Chương 48).

---

## 34.9 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| Module cân | Có ở phần lớn hệ; ⚠ **tốc độ cập nhật khác nhau nhiều** — kiểm trước nếu cần giám sát động |
| Độ phân giải | Module cân thường có độ phân giải cao hơn module analog thường; ⚠ nhưng vẫn áp quy tắc Chương 32 mục 32.3: **độ phân giải ≠ độ chính xác** |
| Hiệu chuẩn | Có hệ hỗ trợ quy trình hiệu chuẩn bằng khối chức năng; có hệ để bạn tự tính hệ số |
| Kích load cell | Module cấp điện áp kích; ⚠ kiểm **số load cell tối đa** mắc song song được |
| Load cell 6 dây | ⚠ Không phải module nào cũng hỗ trợ — kiểm nếu cần nối dài cáp |
| Lọc tích hợp | Có, cấu hình được. ⚠ Cùng đánh đổi độ trễ ở Chương 32 mục 32.6 |
| Máy vặn vít | Giao tiếp qua I/O số, hoặc mạng. ⭐ Thường trả cả **kết quả và dữ liệu đường cong** |

---

## 34.10 Bẫy thường gặp

### 🔍 BẪY 1 — Dùng cảm biến vị trí làm tiêu chí OK/NG cho thao tác có lực

**Hiện tượng:** đúng cỗ máy ở mục 34.1 — năm loại lỗi khác nhau đều cho kết quả "OK", và lỗi lộ ra ở
công đoạn kiểm cuối hoặc ở khách hàng.
**Cách sửa:** ⭐ **cửa sổ lực–vị trí** (mục 34.5).

### 🔍 BẪY 2 — Chỉ kiểm "không vi phạm cửa sổ"

**Hiện tượng:** cơ cấu dừng sớm, **không vi phạm** cửa sổ cuối vì chưa bao giờ tới đó — và được báo OK.
**Cách sửa:** kiểm cả **đã đi qua** từng cửa sổ (mục 34.5).

### 🔍 BẪY 3 — Đặt giới hạn cửa sổ bằng cách đoán

**Hiện tượng:** loại nhầm hàng tốt, hoặc bỏ lọt hàng lỗi — và không ai biết cái nào đang xảy ra.
**Cách sửa:** xây từ **dữ liệu của sản phẩm tốt đã biết**, rồi xác nhận bằng **lỗi cố ý** (mục 34.5,
Chương 52 mục 52.7).

### 🔍 BẪY 4 — Dùng mô-men một mình để đánh giá siết vít

**Hiện tượng:** vít **trờn ren** đạt mô-men mục tiêu sớm và được báo OK.
**Cách sửa:** ⭐ đánh giá **mô-men cùng với góc** (mục 34.6).

### 🔍 BẪY 5 — Quá tải load cell

**Hiện tượng:** cảm biến hỏng vĩnh viễn, thường **không phải khi máy chạy** mà khi lắp đặt hoặc khi
ai đó tì lên cơ cấu.
**Cách sửa:** **cữ cơ khí** giới hạn hành trình; không dựa vào phần mềm (mục 34.2).

### 🔍 BẪY 6 — Nối dài hoặc cắt ngắn cáp load cell

**Hiện tượng:** phép cân sai theo tỉ lệ, ổn định, trông hợp lý.
**Cách sửa:** giữ nguyên cáp; nếu buộc phải nối dài thì dùng load cell **6 dây** (mục 34.4).

### 🔍 BẪY 7 — Bỏ qua phép kiểm độ lặp lại

**Hiện tượng:** cân "chính xác" theo trung bình nhưng từng phép đo không dùng được.
**Cách sửa:** bước 4 ở mục 34.3. Độ lặp lại kém gần như luôn là vấn đề **cơ khí**.

### 🔍 BẪY 8 — Lọc mạnh khi giám sát động

**Hiện tượng:** đường cong lực–vị trí bị **lệch** do độ trễ bộ lọc; cửa sổ bắt sai.
**Cách sửa:** cân tĩnh lọc mạnh được; giám sát động thì lọc nhẹ (mục 34.4, Chương 32 mục 32.6).

### 🔍 BẪY 9 — Không xem lại cửa sổ khi quy trình đổi

**Hiện tượng:** đổi nhà cung cấp connector hoặc cơ cấu mòn dần → cửa sổ loại nhầm hàng tốt → người ta
**nới rộng cửa sổ** cho hết báo lỗi, và việc kiểm tra thành vô nghĩa.
**Cách sửa:** cửa sổ là tham số cần **duy trì**; đưa vào công thức và có quy trình xem lại (mục 34.7,
Chương 29).

---

## 34.11 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Vì sao cảm biến vị trí không đủ | ⭐ Nhiều loại lỗi **kết thúc ở cùng vị trí**, khác nhau ở **đường đi tới đó** |
| Tiêu chí OK/NG cho thao tác có lực | ⭐ **Cửa sổ lực–vị trí** |
| Kiểm cửa sổ thế nào cho đúng | ⚠ Phải **đi qua đủ** mọi cửa sổ, không chỉ "không vi phạm" |
| Xây cửa sổ từ đâu | **Dữ liệu sản phẩm tốt đã biết**, rồi xác nhận bằng **lỗi cố ý** |
| Cửa sổ nào trượt cho biết | ⭐ **Loại lỗi** — đây là chẩn đoán, không chỉ phán quyết |
| Siết vít đánh giá bằng | ⭐ **Mô-men cùng với góc** — mô-men một mình không phân biệt được trờn ren |
| Load cell hỏng vì | ⚠ **Quá tải** — thường lúc lắp đặt, không phải lúc chạy |
| Chống quá tải bằng | **Cữ cơ khí**, không bằng phần mềm |
| Cáp load cell | ⚠ **Không nối dài, không cắt ngắn**; cần dài thì dùng loại **6 dây** |
| Phép kiểm hiệu chuẩn giá trị nhất | ⭐ **Độ lặp lại** — kém thì là vấn đề **cơ khí** |
| Lọc | Cân tĩnh lọc mạnh được; **giám sát động lọc nhẹ** |
| Tham số cửa sổ để ở đâu | Trong **công thức sản phẩm**, và PLC vẫn kiểm dải hợp lệ |
| Không cần đo lực khi | Lỗi không im lặng · đã kiểm ở công đoạn sau · ⚠ **không ai duy trì được cửa sổ** |
| ⭐ Nguyên tắc tổng quát | **So lệnh với kết quả, theo dõi quan hệ giữa chúng** |

---

## 34.12 Tự kiểm

1. ⭐ Nêu năm tình huống lắp ráp khác nhau đều cho kết quả "đã tới vị trí cuối". Vì sao cảm biến vị
   trí không phân biệt được?
2. Load cell hoạt động theo nguyên lý gì? Vì sao nó **luôn** cần bộ khuếch đại?
3. Nêu ba thông số phải đọc của load cell. Thông số nào liên quan tới cách hỏng phổ biến nhất?
4. Vì sao chống quá tải phải bằng **cữ cơ khí** chứ không bằng phần mềm?
5. ⭐ **Cửa sổ lực–vị trí** là gì? Nêu ba cửa sổ điển hình của thao tác cắm connector và lỗi mỗi cửa
   sổ bắt được.
6. ⭐ Vì sao kiểm "không vi phạm cửa sổ nào" là **chưa đủ**? Liên hệ với bẫy nào ở Chương 28?
7. Quy trình xây cửa sổ gồm hai giai đoạn nào? Giai đoạn thứ hai liên hệ với mục nào của Chương 52?
8. ⭐ Vì sao **mô-men một mình** không đủ để đánh giá việc siết vít? Nêu hai kiểu lỗi và cách phân
   biệt chúng.
9. Vì sao không được nối dài cáp load cell? Nếu buộc phải nối dài thì dùng gì, và nó giống kỹ thuật
   nào ở Chương 33?
10. Trong quy trình hiệu chuẩn, phép kiểm nào có giá trị nhất và vì sao? Kết quả kém thường chỉ ra
    vấn đề ở đâu?
11. Khi nào **không** cần đo lực? Lý do nào là thật nhất?
12. ⭐ Nêu bốn cặp "lệnh ↔ kết quả" đã xuất hiện trong sách ở các chương trước. Chúng có chung nguyên
    tắc gì?

> Câu 1, 5, 6, 8 và 12 là năm câu phân loại. Câu 12 là tinh thần của cả chương: **một đại lượng cho
> bạn một con số; quan hệ giữa hai đại lượng cho bạn một chữ ký — và chữ ký mới phát hiện được hỏng
> hóc trôi dần.**

---

### Chương tiếp theo

Chương 35 — **Điều khiển PID trên PLC**. Bạn đã có các phép đo quá trình. Chương sau về việc dùng
chúng để **điều khiển** — và về câu hỏi quan trọng hơn: khi nào thì đừng.

### Nguồn tham khảo chương 34

- IEC 61131-2 — *Programmable controllers, Part 2: Equipment requirements and tests*: yêu cầu với
  module vào analog, áp cho module cân. *(tiêu chuẩn có bản quyền)*
- OIML R 60 — *Metrological regulation for load cells*: phân cấp và yêu cầu đo lường với load cell —
  dùng khi phép cân phục vụ mục đích thương mại.
- ISO 6789 — *Assembly tools for screws and bolts — Hand torque tools*: yêu cầu với dụng cụ siết
  mô-men — tham khảo cho phần mô-men ở mục 34.6.
- **Datasheet load cell** — dùng cho tải định mức, độ nhạy, ⚠ **quá tải cho phép**, và số dây.
- **Tài liệu module cân** của hệ đang dùng — dùng cho ⚠ **tốc độ cập nhật**, độ phân giải, số load
  cell mắc song song được, hỗ trợ 6 dây, và quy trình hiệu chuẩn.

> ⚡ Các cửa sổ lực–vị trí ở mục 34.5 là **minh hoạ cho phương pháp**, không phải giá trị áp dụng
> chung. Cửa sổ của bạn phải xây từ **dữ liệu đo trên chính sản phẩm và chính cơ cấu của bạn**, và
> phải được xem lại khi vật liệu, nhà cung cấp, hoặc tình trạng cơ khí thay đổi (mục 34.7).
>
> ⚠ Khi phép cân dùng cho **mục đích thương mại** — bán hàng theo khối lượng — thì có yêu cầu pháp lý
> về kiểm định và về vết truy nguyên của quả cân chuẩn, khác với phép cân dùng nội bộ trong quy trình.
> Kiểm quy định tại thị trường của bạn.
