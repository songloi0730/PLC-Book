# Chương 12 — IO-Link & lớp cảm biến thông minh

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 12.1 Bài toán: thay một cảm biến mất bốn mươi phút

Cảm biến quang ở trạm 1 hỏng lúc hai giờ sáng. Có cảm biến dự phòng cùng mã trong kho. Việc thay lẽ
ra mất năm phút.

Nó mất bốn mươi phút, vì:

- cảm biến cũ đã được **chỉnh độ nhạy bằng tay** khi lắp máy, và không ai ghi lại giá trị đó;
- cảm biến mới ra khỏi hộp với thông số mặc định, nhận nhầm cả bóng của khung máy;
- người thay phải chỉnh lại bằng vít chỉnh nhỏ xíu, thử đi thử lại với board thật;
- chỉnh xong "chạy được", nhưng **không ai biết nó có giống lúc trước không**.

Ba tuần sau, tỉ lệ lỗi ở trạm 1 tăng nhẹ. Không ai nối hai việc đó với nhau.

Đây là một loại vấn đề mà lớp đấu nối rời rạc truyền thống **không giải được**: sợi dây chỉ mang được
**một bit**, và mọi thứ khác — tham số, sức khoẻ, danh tính thiết bị — nằm ngoài hệ thống.

Chương này về một cách khác để nối cảm biến, và về việc khi nào nó đáng dùng.

---

## 12.2 Giới hạn của lớp đấu nối truyền thống

Với cảm biến số cổ điển (Chương 4), sợi tín hiệu mang đúng **một bit**: có vật hay không.

Những gì PLC **không** biết được:

| Không biết | Hậu quả |
|---|---|
| Cảm biến đang đặt tham số gì | Thay thiết bị là mất tham số — đúng mục 12.1 |
| Tín hiệu đang **mạnh hay yếu** | Cảm biến bẩn dần, tín hiệu yếu dần, tới ngày nó chỉ đơn giản là ngừng báo |
| Thiết bị lắp ở đó có **đúng loại** không | Lắp nhầm mã cảm biến vẫn chạy — cho tới khi gặp trường hợp biên |
| Đã chạy bao nhiêu giờ, đóng cắt bao nhiêu lần | Không lập được lịch bảo trì theo tình trạng |
| Cảm biến có đang báo lỗi nội bộ không | Không có khái niệm này |

Hàng thứ hai là hàng đáng giá nhất. **Độ dự trữ tín hiệu** giảm dần là **cảnh báo sớm** — nó cho bạn
vài tuần để lên kế hoạch thay, thay vì một sự cố lúc hai giờ sáng.

Với cảm biến analog (Chương 32) thì khá hơn: dây mang một giá trị thay vì một bit. Nhưng vẫn không
mang được tham số, danh tính, hay chẩn đoán.

---

## 12.3 IO-Link là gì — và **không** là gì

**IO-Link** là một giao thức truyền thông **điểm–điểm** giữa một thiết bị (cảm biến, cơ cấu chấp
hành) và một **cổng IO-Link** trên module chủ.

```text
   PLC ──[ mạng công nghiệp ]── IO-Link master ──┬── cổng 1 ── cảm biến IO-Link
                                                  ├── cổng 2 ── cảm biến IO-Link
                                                  ├── cổng 3 ── cảm biến số thường
                                                  └── cổng 4 ── cơ cấu IO-Link
```

Điểm mấu chốt: **dây vẫn là dây cảm biến ba lõi thông thường**, không đổi gì về mặt vật lý. Cái đổi
là **thứ chạy trên sợi dây đó**: thay vì một bit, nó truyền một khung dữ liệu số.

### ⭐ IO-Link **không phải** bus trường

Đây là hiểu nhầm phổ biến nhất, và nó dẫn tới kỳ vọng sai:

| | **Bus trường** *(fieldbus)* — PROFINET, EtherCAT… | **IO-Link** |
|---|---|---|
| Cấu trúc | Nhiều thiết bị trên **một** đường chung | ⭐ **Điểm–điểm** — mỗi thiết bị một cổng riêng |
| Địa chỉ | Mỗi thiết bị có địa chỉ mạng | Không có — cổng nào thì thiết bị nấy |
| Cáp | Cáp mạng chuyên dụng | ⭐ **Cáp cảm biến ba lõi thông thường** |
| Khoảng cách | Hàng chục tới hàng trăm mét | Ngắn — khoảng vài chục mét |
| Vai trò | Nối **các cụm** với nhau (Chương 40) | Nối **từng thiết bị** vào một cụm |

> **Cách hiểu đúng: IO-Link là lớp NẰM DƯỚI bus trường, không thay thế nó.**
> Bus trường đưa dữ liệu từ cụm I/O về PLC. IO-Link đưa dữ liệu từ **từng cảm biến** vào cụm đó. Hai
> lớp bổ sung nhau (Chương 8, mục 8.5).

### Ba loại dữ liệu

| Loại | Là gì | Cập nhật |
|---|---|---|
| **Dữ liệu quá trình** *(process data)* | Giá trị chính — bit có vật, hoặc giá trị đo | Liên tục, mỗi chu kỳ |
| **Dữ liệu tham số** *(parameter data)* | Cấu hình của thiết bị — độ nhạy, ngưỡng, chế độ | Khi cần đọc hoặc ghi |
| **Dữ liệu chẩn đoán và sự kiện** | Cảnh báo, lỗi, độ dự trữ tín hiệu, giờ chạy | Khi có sự kiện, hoặc khi hỏi |

Hai loại sau là thứ mà lớp đấu nối truyền thống **hoàn toàn không có**.

---

## 12.4 ⭐ Thay thiết bị mà không phải chỉnh lại bằng tay

Đây là lợi ích thực tế lớn nhất, và nó giải đúng bài toán ở mục 12.1.

### Cách hoạt động

Cổng IO-Link chủ **giữ một bản sao tham số** của thiết bị cắm vào nó — cơ chế này trong đặc tả gọi là
**kho tham số** *(Data Storage)*. Khi phát hiện một thiết bị mới:

```text
   1. Thiết bị mới cắm vào cổng
   2. Master đọc danh tính thiết bị (mã hãng, mã sản phẩm)
   3. So với danh tính đã lưu cho cổng đó
        ├─ KHỚP    → tự nạp bộ tham số đã lưu xuống thiết bị mới
        └─ KHÔNG   → báo lỗi "sai loại thiết bị", KHÔNG nạp
   4. Thiết bị mới chạy với đúng tham số của thiết bị cũ
```

Hai điều được giải quyết cùng lúc:

- **Tham số tự khôi phục.** Không ai phải nhớ, không ai phải chỉnh tay. Việc thay trở lại đúng năm
  phút.
- ⭐ **Lắp nhầm loại thì bị phát hiện ngay**, thay vì lộ ra sau ba tuần dưới dạng tỉ lệ lỗi tăng nhẹ.

> ⭐ **Điểm thứ hai đáng giá không kém điểm thứ nhất.**
> Với cảm biến thường, lắp nhầm một mã gần giống vẫn chạy được — và sai lệch chỉ lộ ra ở trường hợp
> biên, khi đó không ai còn nhớ đã thay cảm biến. IO-Link biến lỗi im lặng đó thành một **thông báo
> tại chỗ**.
>
> Đây là cùng một nguyên tắc với tiếp điểm cưỡng bức ở Chương 3 mục 3.5 và với "lỗi mà máy không tự
> phát hiện được" ở Chương 48: **làm cho hỏng hóc trở nên phát hiện được.**

### ⚠ Điều kiện để nó hoạt động

Cơ chế này **không tự có** — nó phải được cấu hình:

- Bộ tham số phải được **lưu vào master** sau khi chỉnh xong lần đầu.
- Chế độ nạp lại tự động phải được **bật**.
- ⚠ Và bản thân **cấu hình master** phải nằm trong bản sao lưu dự án (Chương 54) — nếu không, thay
  master là mất toàn bộ tham số của mọi cảm biến trên nó.

Gạch đầu dòng cuối là bẫy mà người ta chỉ phát hiện khi đã muộn.

---

## 12.4b ⭐⭐ Một thiết bị IO-Link vẫn chạy được như cảm biến thường

Đây là tính chất quyết định khi **mua sắm**, và nó hay bị bỏ qua vì nghe quá đơn giản.

> ⭐⭐ **Thiết bị IO-Link có hai chế độ, và chế độ thứ hai là cảm biến số bình thường.**

| Chế độ | Thiết bị làm gì |
|---|---|
| ⭐ **IO-Link** *(SDCI)* | Truyền thông đầy đủ — tham số, chẩn đoán, danh tính (các mục trên) |
| ⭐⭐ **SIO** — *Standard Input/Output* | ⭐ **Bỏ qua toàn bộ tầng truyền thông**, đưa thẳng tín hiệu DI hoặc DO ra ngoài như một cảm biến số thường |

**Ba hệ quả thực tế:**

| | |
|---|---|
| 1 | ⭐⭐ **Cắm được vào module DI thường.** Đặc tính điện của chân DI/DO ở chế độ SIO lấy theo **IEC 61131-2 kiểu 1** — đúng loại ngõ vào ở Chương 9. Không cần cổng IO-Link chủ |
| 2 | ⭐ **Chọn chế độ bằng CẤU HÌNH, không bằng đấu dây.** Cùng một thiết bị, cùng một sợi cáp 3 dây — chuyển chế độ là việc của cấu hình master |
| 3 | ⭐ **Nâng cấp được theo giai đoạn.** Mua cảm biến có IO-Link ngay bây giờ, dùng như cảm biến thường; khi nào cần chẩn đoán và tự nạp tham số thì **đổi module, giữ nguyên thiết bị và dây** |

> ⭐⭐ **Hệ quả 3 làm đổi hẳn phép tính chi phí ở mục 12.7.**
>
> Câu hỏi *"có nên dùng IO-Link không"* thường được đặt thành **một quyết định phải chốt ngay**. Nhưng
> với chế độ SIO, ⭐ **nó không phải quyết định một lần** — chênh lệch giá cảm biến có IO-Link so với
> cảm biến thường thường nhỏ, và nó **giữ cửa mở** cho việc nâng cấp sau này.
>
> ⚡ Ngược lại, ⚠ mua cảm biến **không** có IO-Link để tiết kiệm hôm nay nghĩa là ⚠⚠ **muốn nâng cấp
> phải thay cả thiết bị hiện trường** — công việc nằm ngoài tủ điện, tốn hơn nhiều lần.

> ⚠ **Điều SIO KHÔNG cho bạn:** ở chế độ đó thiết bị **chỉ là một cảm biến số**. ⚠ Không có tham số
> tự nạp (mục 12.4), không có dữ liệu chẩn đoán (mục 12.5), không có kiểm danh tính. ⭐ Nó là **đường
> lui và bước đệm**, không phải cách dùng IO-Link.

---

## 12.5 Dữ liệu chẩn đoán — thứ cảm biến rời rạc không có

| Dữ liệu | Dùng để làm gì |
|---|---|
| ⭐ **Độ dự trữ tín hiệu** *(signal margin / excess gain)* | Tín hiệu còn mạnh hơn ngưỡng bao nhiêu lần. Giảm dần → cảm biến bẩn, lệch, hoặc thiết bị sắp hỏng |
| Số giờ chạy, số lần đóng cắt | Bảo trì theo tình trạng thay vì theo lịch cứng |
| Nhiệt độ bên trong thiết bị | Cảnh báo môi trường xấu đi |
| Điện áp cấp tại thiết bị | ⭐ Phát hiện sụt áp **tại nơi tiêu thụ** (Chương 8, mục 8.7) |
| Sự kiện lỗi nội bộ | Thiết bị tự báo mình có vấn đề |

### Vì sao độ dự trữ tín hiệu là số liệu đáng giá nhất

Một cảm biến quang bị bẩn dần **không đổi hành vi** cho tới lúc nó vượt ngưỡng — rồi đột ngột ngừng
báo. Từ góc nhìn của PLC truyền thống, nó chạy hoàn hảo rồi hỏng ngay lập tức.

Với độ dự trữ tín hiệu, bạn thấy con số giảm từ 8 lần xuống 5, xuống 3, xuống 1,5. Bạn có **vài tuần**
để lau hoặc thay, vào giờ hành chính, có kế hoạch.

> 💡 **Cách dùng thực dụng nhất, và cũng đơn giản nhất:**
> đọc độ dự trữ tín hiệu, so với ngưỡng cảnh báo, và đưa vào **mức "cảnh báo, vẫn chạy"** ở
> Chương 48 mục 48.6 — không dừng máy, chỉ báo để lên kế hoạch.
>
> Đừng đưa nó vào mức "cấm chạy". Một cảnh báo sớm mà làm dừng máy sẽ bị vô hiệu hoá sau lần thứ ba.

---

## 12.6 Lập trình phía PLC

Với người viết chương trình, thiết bị IO-Link xuất hiện dưới hai dạng:

| Dạng | Truy cập thế nào |
|---|---|
| **Dữ liệu quá trình** | Như I/O bình thường — một hoặc nhiều byte trong ảnh quá trình |
| **Tham số và chẩn đoán** | Qua khối chức năng chuyên dụng: đọc/ghi theo chỉ số tham số |

```iecst
// Dữ liệu quá trình: dùng y như cảm biến thường
IF DI_BoardStn1 THEN ...

// Chẩn đoán: đọc theo yêu cầu, KHÔNG đọc mỗi vòng quét
IF TrigReadDiag.Q THEN
    // gọi khối đọc tham số của hệ đang dùng
    // → lấy độ dự trữ tín hiệu vào SignalMarginStn1
END_IF;

M_Stn1SensorWarn := SignalMarginStn1 < RecipeMarginWarnLimit;
```

> ⚠⚠ **Đừng đọc tham số và chẩn đoán ở mỗi vòng quét.**
> Việc đọc tham số đi qua kênh riêng, **chậm hơn nhiều** so với dữ liệu quá trình, và nó **không đồng
> bộ** với vòng quét. Gọi liên tục sẽ làm thời gian quét biến động và có thể làm nghẽn kênh.
>
> Đọc **theo chu kỳ chậm** — vài giây tới vài phút một lần là quá đủ cho dữ liệu sức khoẻ thiết bị.
> Bắt cạnh của một xung định kỳ (Chương 16, Chương 17).

Ba điều nữa cần biết:

- **Byte dữ liệu quá trình phải được diễn giải theo tài liệu thiết bị.** Một cảm biến có thể gói
  nhiều bit trạng thái trong một byte — dùng kiểu `BYTE`/`WORD`, không dùng `INT` (Chương 11, mục 11.2).
- **Trạng thái cổng cũng là dữ liệu.** Master báo được cổng nào đang mất kết nối, cổng nào có thiết bị
  sai loại. Đây là thông tin phải xử lý tường minh, giống mất kết nối I/O phân tán (Chương 48, mục 48.5).
- **Tệp mô tả thiết bị** *(IODD — IO Device Description)* do hãng cung cấp. Nó cho công cụ cấu hình
  biết thiết bị có những tham số nào. ⚠ Tệp này phải được lưu cùng dự án.

---

## 12.7 ⚠ Khi nào IO-Link **không** đáng dùng

Cân bằng lại — chương này không phải quảng cáo.

| Tình huống | Vì sao không đáng |
|---|---|
| **Cảm biến đơn giản, không có tham số gì để chỉnh** | Reed xy-lanh, công tắc hành trình. Không có gì để lưu, không có gì để chẩn đoán |
| **Máy nhỏ, ít cảm biến** | Chi phí master và công cấu hình vượt lợi ích |
| **Đội bảo trì chưa quen** | ⚠ Xem cảnh báo bên dưới |
| **Cần đáp ứng rất nhanh** | Chu kỳ IO-Link chậm hơn ngõ vào số trực tiếp; việc đếm xung tốc độ cao vẫn cần HSC (Chương 18) |
| **Cảm biến không có bản IO-Link** | Không phải loại nào cũng có, và bản IO-Link thường đắt hơn |
| **Khoảng cách xa** | Vượt giới hạn chiều dài cáp |

> ⚠⚠ **"Đội bảo trì chưa quen" là lý do nghiêm túc, không phải cái cớ.**
>
> Một cảm biến thường hỏng lúc hai giờ sáng: thợ điện tháo ra, cắm cái mới, chỉnh vít, xong.
>
> Một cảm biến IO-Link hỏng lúc hai giờ sáng: nếu **mọi thứ được cấu hình đúng**, việc thay còn nhanh
> hơn — tham số tự nạp. Nhưng nếu cấu hình sai, hoặc master báo "sai loại thiết bị", thì người thợ
> cần **biết cách đọc thông báo đó và xử lý** — và điều đó đòi hỏi đào tạo.
>
> **Quyết định dùng IO-Link đi kèm nghĩa vụ đào tạo và tài liệu.** Không có phần đó, bạn đã đổi một
> vấn đề cũ lấy một vấn đề mới khó hơn.

### Cách áp dụng hợp lý

> 💡 **Không phải chuyện được ăn cả ngã về không.** Master IO-Link thường có cả cổng thường: dùng
> IO-Link cho **những cảm biến thật sự hưởng lợi** — loại có tham số cần chỉnh, loại đắt, loại nằm ở
> chỗ khó với tới, loại mà chẩn đoán sớm có giá trị — và dùng ngõ vào thường cho phần còn lại.

---

## 12.8 Trên máy mẫu DP-01

Áp bảng ở mục 12.7 vào từng cảm biến của lát cắt 1:

| Cảm biến | IO-Link? | Vì sao |
|---|---|---|
| `DI_BoardStn1`, `DI_BoardStn2` — quang thu-phát | ⭐ **Đáng** | Có độ nhạy cần chỉnh; ⭐ độ dự trữ tín hiệu cảnh báo sớm khi bẩn — đúng bài toán ở mục 12.1 |
| `DI_BoardInfeed`, `DI_BoardOutfeed` — quang | Đáng | Cùng lý do |
| `DI_Stop1Up/Dn`, `DI_Clamp1Up/Dn` — reed xy-lanh | ❌ **Không** | Không có tham số; rẻ; thay là xong |
| `DI_StartPB`, `DI_StopPB` — nút bấm | ❌ Không | Tiếp điểm cơ khí thuần |
| `DI_EStopOK`, `DI_Door1Closed` — tín hiệu an toàn | ⚠⚠ **Không** | Xem cảnh báo bên dưới |
| `DI_AirOK` — công tắc áp suất | Tuỳ | Nếu thay bằng cảm biến áp suất IO-Link thì đọc được **giá trị áp thật**, không chỉ đạt/không đạt — hữu ích cho bài toán ở Chương 22 mục 22.9 |

> ⚠⚠ **NGUY HIỂM — IO-Link thông thường không dùng cho chức năng an toàn**
> `DI_EStopOK`, `DI_Door1Closed`, `DI_CurtainOK` đến từ **rơ-le an toàn phần cứng** (Chương 47).
> Truyền tín hiệu an toàn qua một kênh truyền thông đòi hỏi giao thức an toàn chuyên dụng và thiết bị
> được chứng nhận — đây là cùng nguyên tắc với I/O phân tán ở Chương 8 mục 8.5.
>
> **Không tự làm.** Việc này do người có thẩm quyền thiết kế.

Hàng cuối bảng đáng chú ý: đổi công tắc áp suất (một bit đạt/không đạt) lấy cảm biến áp suất đọc được
giá trị thật sẽ biến bài toán "vì sao trạm 1 chậm vào buổi trưa" từ **giả thuyết** thành **số liệu**.
Đó là ví dụ rõ nhất của việc lớp cảm biến thông minh trả về giá trị gì.

---

## 12.9 Khác biệt giữa các hãng

IO-Link là **chuẩn mở** (IEC 61131-9), nên thiết bị của hãng này cắm vào master của hãng khác được.
Nhưng công cụ cấu hình và cách tích hợp thì khác nhau.

| Khía cạnh | Điều cần biết |
|---|---|
| ⭐ **Tính tương thích chéo** | Đây là **điểm mạnh thật** của IO-Link: cảm biến của bất kỳ hãng nào cũng dùng được với master của hãng khác, nhờ tệp IODD chuẩn |
| Công cụ cấu hình | Siemens, Rockwell, Mitsubishi, Beckhoff đều tích hợp cấu hình IO-Link vào phần mềm lập trình của mình; giao diện khác nhau |
| Khối chức năng đọc/ghi tham số | Mỗi hệ một bộ khối riêng, tên và tham số khác nhau — tra Phụ lục A |
| ⚠ Cách lưu và nạp lại tham số | Có hệ làm gần như tự động, có hệ cần cấu hình từng cổng. **Đây là tính năng chính của chương này — kiểm nó có và đã bật chưa** |
| Nạp tệp IODD | Quy trình khác nhau; ⚠ tệp IODD phải lưu cùng dự án (Chương 54) |
| Master độc lập với mạng phía trên | Cùng một master thường có bản cho PROFINET, EtherNet/IP, EtherCAT… — chọn theo mạng bạn đang dùng (Chương 40) |

---

## 12.10 Bẫy thường gặp

### 🔍 BẪY 1 — Tưởng IO-Link là bus trường

**Hiện tượng:** thiết kế sai kiến trúc mạng — ví dụ định nối nhiều cảm biến vào chung một đường, hoặc
tính khoảng cách như cáp mạng.
**Cách sửa:** IO-Link là **điểm–điểm**, mỗi thiết bị một cổng, và nó nằm **dưới** bus trường
(mục 12.3).

### 🔍 BẪY 2 — Không bật chế độ lưu và nạp lại tham số

**Hiện tượng:** thay cảm biến vẫn phải chỉnh tay — tức là **mất đúng lợi ích lớn nhất** mà bạn đã trả
tiền để có.
**Cách sửa:** lưu bộ tham số vào master sau khi chỉnh xong, và bật chế độ nạp lại tự động (mục 12.4).

### 🔍 BẪY 3 — Không sao lưu cấu hình master

**Hiện tượng:** master hỏng, thay cái mới, và **mất tham số của mọi cảm biến trên nó** cùng lúc. Tệ
hơn nhiều so với mất một cảm biến.
**Cách sửa:** cấu hình master và tệp IODD nằm trong bản sao lưu dự án, và bản sao lưu đó phải **đã
thử khôi phục** (Chương 54).

### 🔍 BẪY 4 — Đọc tham số ở mỗi vòng quét

**Hiện tượng:** thời gian quét biến động; đôi khi vọt lên và kích watchdog (Chương 20, mục 20.5).
**Cách sửa:** đọc theo **chu kỳ chậm** — vài giây tới vài phút (mục 12.6).

### 🔍 BẪY 5 — Đưa cảnh báo độ dự trữ tín hiệu vào mức "cấm chạy"

**Hiện tượng:** máy dừng vì một cảm biến vẫn đang hoạt động bình thường; sau ba lần, người ta **vô
hiệu hoá** cảnh báo — và mất luôn giá trị của nó.
**Cách sửa:** cảnh báo sớm thuộc mức **"cảnh báo, vẫn chạy"** (mục 12.5, Chương 48 mục 48.6).

### 🔍 BẪY 6 — Dùng IO-Link cho tín hiệu an toàn

**Hiện tượng:** thiết kế tưởng đạt yêu cầu an toàn nhưng không đạt — và điều đó chỉ lộ ra khi có kiểm
định, hoặc khi có tai nạn.
**Cách sửa:** ⚠⚠ tín hiệu an toàn cần giao thức an toàn và thiết bị được chứng nhận (mục 12.8,
Chương 47).

### 🔍 BẪY 7 — Dùng IO-Link cho mọi thứ vì "hiện đại hơn"

**Hiện tượng:** chi phí tăng, cấu hình phức tạp thêm, mà reed xy-lanh thì chẳng có tham số nào để
lưu.
**Cách sửa:** dùng cho cảm biến **thật sự hưởng lợi**; phần còn lại dùng ngõ vào thường (mục 12.7).

### 🔍 BẪY 8 — Triển khai mà không đào tạo đội bảo trì

**Hiện tượng:** cảm biến hỏng lúc hai giờ sáng, master báo "sai loại thiết bị", và người thợ **không
biết thông báo đó nghĩa là gì**. Thời gian dừng máy dài hơn cả trước khi có IO-Link.
**Cách sửa:** đào tạo và tài liệu là **một phần của quyết định triển khai**, không phải việc làm sau
(mục 12.7).

### 🔍 BẪY 9 — Diễn giải byte dữ liệu quá trình bằng kiểu số

**Hiện tượng:** một byte gói nhiều bit trạng thái hiện ra thành số vô lý.
**Cách sửa:** dùng `BYTE`/`WORD` cho tập cờ, và diễn giải theo tài liệu thiết bị (Chương 11, mục 11.2).

---

## 12.11 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| IO-Link là gì | Giao thức **điểm–điểm** từ thiết bị tới cổng master |
| Có phải bus trường không | ❌ **Không** — nó nằm **dưới** bus trường |
| Cáp dùng loại gì | ⭐ **Cáp cảm biến ba lõi thông thường** |
| Ba loại dữ liệu | Quá trình · **tham số** · **chẩn đoán** |
| Lợi ích lớn nhất | ⭐ **Thay thiết bị, tham số tự nạp** — và **phát hiện lắp nhầm loại** |
| Số liệu chẩn đoán đáng giá nhất | ⭐ **Độ dự trữ tín hiệu** — cảnh báo sớm |
| Cảnh báo sớm xếp mức nào | **"Cảnh báo, vẫn chạy"** — không phải "cấm chạy" |
| Đọc tham số bao lâu một lần | **Vài giây tới vài phút** — không phải mỗi vòng quét |
| Byte dữ liệu quá trình khai kiểu gì | `BYTE`/`WORD` nếu là tập cờ |
| Phải sao lưu gì | ⚠ **Cấu hình master + tệp IODD**, cùng dự án |
| Không đáng dùng khi | Cảm biến không tham số · máy nhỏ · cần rất nhanh · khoảng cách xa |
| ⚠ Không được dùng cho | ⚠⚠ **Tín hiệu an toàn** |
| Đi kèm quyết định triển khai | **Đào tạo và tài liệu** cho đội bảo trì |
| ⭐⭐ Thiết bị IO-Link có mấy chế độ | **Hai** — IO-Link đầy đủ, và ⭐ **SIO: cảm biến số thường** |
| Ở chế độ SIO cắm vào đâu | ⭐ **Module DI thường** — đặc tính điện theo **IEC 61131-2 kiểu 1** (Chương 9) |
| Chọn chế độ bằng gì | ⭐ **Cấu hình**, không phải đấu dây — cùng một sợi cáp 3 dây |
| ⭐ Hệ quả mua sắm | **Không phải quyết định một lần** — mua thiết bị có IO-Link, nâng cấp module sau |
| Cách áp dụng hợp lý | Trộn — IO-Link cho cảm biến hưởng lợi, ngõ vào thường cho phần còn lại |

---

## 12.12 Tự kiểm

1. Nêu năm thứ mà PLC **không** biết được về một cảm biến số thông thường.
2. ⭐ IO-Link khác bus trường ở bốn điểm nào? Vì sao gọi nó là lớp "nằm dưới" bus trường?
3. Kể ba loại dữ liệu của IO-Link. Hai loại nào mà lớp đấu nối truyền thống hoàn toàn không có?
4. ⭐ Mô tả quy trình bốn bước khi cắm một thiết bị mới vào cổng IO-Link. Hai vấn đề nào được giải
   quyết cùng lúc?
5. Cơ chế nạp lại tham số tự động cần ba điều kiện gì để hoạt động? Điều kiện nào hay bị bỏ quên nhất
   và hậu quả là gì?
6. ⭐ Vì sao **độ dự trữ tín hiệu** là số liệu chẩn đoán đáng giá nhất? Mô tả cách một cảm biến quang
   bị bẩn dần hành xử với và không có số liệu này.
7. Vì sao cảnh báo độ dự trữ tín hiệu nên xếp vào mức "cảnh báo, vẫn chạy" chứ không phải "cấm chạy"?
8. Vì sao không được đọc dữ liệu tham số ở mỗi vòng quét?
9. Nêu bốn tình huống IO-Link **không** đáng dùng. Trên DP-01, cảm biến nào không nên dùng IO-Link và
   vì sao?
10. ⭐ Vì sao "đội bảo trì chưa quen" là lý do nghiêm túc để cân nhắc, và nghĩa vụ nào đi kèm quyết
    định triển khai IO-Link?
11. ⭐⭐ Nêu **hai chế độ** của một thiết bị IO-Link. Ở chế độ thứ hai nó cắm vào loại module nào, và
    theo đặc tính điện của tiêu chuẩn nào?
12. ⭐ Vì sao chế độ SIO làm câu hỏi *"có nên dùng IO-Link không"* **không còn là quyết định một lần**?
    ⚠ Nêu cái giá của việc mua cảm biến **không** có IO-Link để tiết kiệm hôm nay.
13. ⚠ Ở chế độ SIO, **ba** tính năng nào của IO-Link **không** còn?

> Câu 2, 4, 6 và 10 là bốn câu phân loại. Câu 4 là tinh thần của cả chương: **giá trị thật của lớp
> cảm biến thông minh không phải là dữ liệu — mà là biến những hỏng hóc im lặng thành thứ phát hiện
> được.**

---

### Chương tiếp theo

Chương 13 — **Chọn PLC & dựng bàn thực hành của riêng bạn**. Bạn đã có đủ hình dung về phần cứng: PLC,
module I/O, cảm biến, và lớp cảm biến thông minh. Chương sau là chương quyết định: chọn gì cho dự án
thật, và mua gì để tự học.

### Nguồn tham khảo chương 12

- IEC 61131-9 — *Programmable controllers, Part 9: Single-drop digital communication interface for
  small sensors and actuators (SDCI)* — đây là tiêu chuẩn của IO-Link. *(tiêu chuẩn có bản quyền)*
- **Đặc tả IO-Link và tài liệu IODD** do tổ chức chuẩn hoá IO-Link công bố — dùng cho cấu trúc dữ
  liệu, quy trình nhận dạng thiết bị, và định dạng tệp mô tả thiết bị.
- Tài liệu master IO-Link và tài liệu tích hợp của từng hệ trong Phụ lục A — dùng cho khối chức năng
  đọc/ghi tham số và ⚠ **cách bật chế độ lưu và nạp lại tham số**, vốn khác nhau giữa các hệ.
- Datasheet của từng cảm biến IO-Link — dùng cho cách diễn giải byte dữ liệu quá trình và danh sách
  tham số chẩn đoán có sẵn.
- Bảng I/O của DP-01 — Phụ lục J; bảng đánh giá ở mục 12.8 lấy danh sách cảm biến từ đó.
- ⭐ **IO-Link Interface and System Specification v1.1.3** *(IEC 61131-9 / SDCI)* — §6 *Standard Input
  and Output (SIO)*: thiết bị **bỏ qua tầng truyền thông** và đưa thẳng tín hiệu DI/DO ra ngoài; chuyển
  chế độ bằng **cấu hình người dùng**; ⭐ đặc tính DI/DO lấy theo **IEC 61131-2 kiểu 1**. §12 *Holistic
  view on Data Storage* — tên chuẩn của cơ chế **kho tham số** ở mục 12.4.

> ⚡ Bảng ở mục 12.8 là **kết quả cân nhắc cho máy mẫu DP-01**, không phải khuyến nghị chung. Với máy
> có nhiều cảm biến cần chỉnh tham số, hoặc cảm biến nằm ở chỗ khó với tới, cán cân nghiêng về IO-Link
> mạnh hơn nhiều. Ngược lại, một máy toàn reed xy-lanh và công tắc hành trình thì gần như không được
> lợi gì.
