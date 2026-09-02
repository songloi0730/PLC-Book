# Chương 33 — Cảm biến quá trình thường gặp

> **Lát cắt máy mẫu:** 3 — thêm analog (áp suất, nhiệt độ, cường độ UV) và trục gantry XY+Z servo.

---

## 33.1 Bài toán: nhiệt độ đúng, keo vẫn hỏng

Bộ gia nhiệt keo của DP-01 được đặt 60 °C. Màn hình hiện **60,0 °C**, ổn định, không dao động. Bộ điều
khiển nhiệt độ báo đã đạt điểm đặt.

Nhưng keo ra vẫn đặc bất thường, và đường keo không đều.

Nguyên nhân, tìm ra sau nửa ngày: cảm biến nhiệt được lắp **ở vỏ ngoài của bình keo**, không phải
trong lòng keo. Vỏ nóng lên nhanh và ổn định ở 60 °C; **keo bên trong chỉ 48 °C**.

Phép đo đúng. Thiết bị đúng. Con số đúng. **Chỗ đo sai.**

Đây là mẫu chung của cả chương: với cảm biến quá trình, phần lớn sai lầm không nằm ở chọn sai loại
cảm biến, mà ở **lắp sai chỗ** hoặc **hiểu sai cái mình đang đo**.

---

## 33.2 Áp suất

Phổ biến nhất trên máy tự động hoá, và cũng là loại người ta ít nghi ngờ nhất.

### Hai loại giá trị đo

| Loại | Đo so với | Ký hiệu hay gặp |
|---|---|---|
| **Áp suất tương đối** *(gauge pressure)* | Áp suất khí quyển | `bar(g)`, `barg` |
| **Áp suất tuyệt đối** *(absolute pressure)* | Chân không hoàn toàn | `bar(a)`, `bara` |

> ⚠ **Chênh nhau khoảng 1 bar — và cả hai đều "đúng".**
> Cảm biến tương đối chỉ 0 bar khi mở ra ngoài trời; cảm biến tuyệt đối chỉ khoảng 1 bar ở cùng điều
> kiện. Lắp nhầm loại thì mọi phép đo lệch một hằng số, và nó **trông hoàn toàn hợp lý**.
>
> Với khí nén công nghiệp, mặc định gần như luôn là **tương đối**. Nhưng ⚠ với **chân không**
> (Chương 6, mục 6.6) thì phải đọc kỹ — cách ghi dải rất khác nhau giữa các hãng.

### Ba bẫy lắp đặt

| Bẫy | Hậu quả |
|---|---|
| **Lắp sau van tiết lưu hoặc chỗ hẹp** | Đo áp ở chỗ đó, không phải áp cấp cho cơ cấu |
| ⚠ **Xung áp khi van đóng mở** | Giá trị nhảy vọt tức thời; có thể **phá cảm biến** theo thời gian |
| **Lắp ở điểm thấp của đường ống** | Nước ngưng đọng lại chỗ cảm biến (Chương 6, mục 6.2) |

Với xung áp, giải pháp phần cứng là **bộ giảm chấn** *(snubber thuỷ lực)* hoặc một đoạn ống mềm. ⚠
Giải pháp phần mềm — lọc mạnh — **không bảo vệ được cảm biến**, chỉ giấu triệu chứng đi (Chương 32,
mục 32.6).

---

## 33.3 ⭐ Nhiệt độ — RTD và can nhiệt

Hai họ cảm biến nhiệt phổ biến, hành xử rất khác nhau. Chọn nhầm không phải thảm hoạ, nhưng đấu nhầm
thì có.

| | **RTD** *(Resistance Temperature Detector)* — Pt100, Pt1000 | **Can nhiệt** *(thermocouple)* — loại K, J, T… |
|---|---|---|
| Nguyên lý | Điện trở kim loại đổi theo nhiệt độ | Hai kim loại khác nhau sinh **điện áp nhỏ** theo chênh lệch nhiệt |
| Dải đo | Vừa — khoảng −200 đến 600 °C | ⭐ **Rất rộng** — lên tới hơn 1000 °C tuỳ loại |
| Độ chính xác | ⭐ **Cao hơn** | Thấp hơn |
| Độ ổn định lâu dài | ⭐ **Tốt hơn** | Trôi theo thời gian |
| Đáp ứng | Chậm hơn | ⭐ **Nhanh hơn** |
| Giá cảm biến | Cao hơn | ⭐ **Rẻ hơn** |
| ⚠ Yêu cầu đặc biệt | **Bù điện trở dây** — mục 33.4 | **Bù đầu lạnh** — mục 33.5 |
| Dây nối dài | Dây đồng thường | ⚠ **Phải dùng dây bù chuyên dụng** |

> **Quy tắc chọn thực dụng:**
> - Dưới ~400 °C, cần chính xác và ổn định → **RTD**. Đây là phần lớn máy tự động hoá.
> - Rất nóng, hoặc cần đáp ứng nhanh, hoặc rất nhiều điểm đo giá rẻ → **can nhiệt**.
>
> Trên DP-01, cả gia nhiệt keo (60 °C) và buồng sấy UV đều dùng **RTD Pt100** — đúng vùng RTD mạnh.

---

## 33.4 ⭐ RTD 2, 3 và 4 dây — vì sao 3 dây là mặc định

Đây là mục quan trọng nhất chương, và câu trả lời rất gọn.

### Vấn đề

RTD đo nhiệt độ bằng **điện trở**. Pt100 có điện trở 100 Ω ở 0 °C, và tăng khoảng **0,385 Ω mỗi độ**.

Nhưng **dây nối cũng có điện trở**. Với cách đấu hai dây, module đo được:

```text
R_đo  =  R_cảm_biến  +  R_dây_đi  +  R_dây_về
```

Module không phân biệt được phần nào là cảm biến, phần nào là dây. Nó quy đổi **toàn bộ** thành nhiệt
độ — nên kết quả **luôn cao hơn thực tế**.

### Sai số đó lớn tới đâu

Một đôi dây đồng dài 20 m, tiết diện nhỏ, có điện trở khoảng vài ôm. Với Pt100:

```text
2 Ω  /  0,385 Ω/°C  ≈  5 °C sai lệch
```

> ⚠ **Năm độ là sai số rất lớn với một phép đo mà bạn dùng để điều khiển nhiệt độ keo.**
> Và nó **không phải nhiễu** — nó là một độ lệch **ổn định, luôn dương**, nên nó trông y hệt một phép
> đo bình thường. Không có cách nào phát hiện từ dữ liệu.

### Ba cách đấu

```text
2 DÂY — module không tách được điện trở dây
   [RTD] ══════════════ [module]        ⚠ sai số cộng thẳng vào

3 DÂY — thêm một dây để module ĐO ĐƯỢC điện trở dây và trừ đi
   [RTD] ══════════════ [module]
         ══════════════
         ══════════════                 ⭐ bù được, chỉ cần 3 sợi

4 DÂY — hai dây cấp dòng, hai dây đo áp, hoàn toàn không chịu ảnh hưởng dây
   [RTD] ══════════════ [module]
         ══════════════
         ══════════════
         ══════════════                 ⭐ chính xác nhất
```

| Cách đấu | Bù điện trở dây | Dùng khi |
|---|---|---|
| **2 dây** | ❌ Không | Chỉ khi dây **rất ngắn** và không cần chính xác |
| ⭐ **3 dây** | ✅ Có — giả định ba dây điện trở bằng nhau | **Mặc định của ngành** — đủ tốt cho gần như mọi ứng dụng máy |
| **4 dây** | ✅ Có — không cần giả định gì | Phòng thí nghiệm, phép đo chuẩn, dây rất dài |

> ⭐ **Vì sao 3 dây là mặc định:** nó bù được gần hết sai số với **chi phí thêm đúng một sợi dây**.
> Bước từ 2 sang 3 dây cải thiện rất nhiều; bước từ 3 sang 4 dây cải thiện thêm rất ít trong điều
> kiện máy công nghiệp.
>
> ⚠ Giả định của cách 3 dây là **ba sợi có điện trở bằng nhau** — đúng khi chúng cùng loại, cùng
> chiều dài, đi cùng một cáp. Nối thêm một đoạn dây khác loại vào **một** sợi sẽ phá giả định đó.

### ⚠ Hai chi tiết nữa về RTD, cả hai đều gây sai lệch có hệ thống

**Một — Pt100 có HAI hệ số, và trộn nhầm thì lệch cả thang.**

| Hệ số alpha | Quen gọi | Ghi chú |
|---|---|---|
| ⭐ **0,00385** | "châu Âu" | ⭐ **Phổ biến nhất**, kể cả ngoài châu Âu |
| 0,00392 | "Mỹ" | Ít gặp hơn |

⚠ Cảm biến theo một hệ số mà module cấu hình theo hệ số kia thì phép đo **lệch một cách có hệ
thống** — không nhảy, không nhiễu, chỉ **sai đều**. ⭐ Đây là loại sai số **rất khó phát hiện** vì
đồ thị trông hoàn toàn bình thường.

⭐ **Cách kiểm:** đối chiếu hệ số ghi trên datasheet cảm biến với cấu hình kênh trong phần mềm.

**Hai — RTD tự làm nóng chính nó.**

Muốn đo điện trở thì phải **cho dòng chạy qua** RTD. Dòng đó sinh nhiệt ngay trên phần tử đo:

```text
P  =  I² × R
```

⚠ Nhiệt đó làm RTD **nóng hơn môi trường xung quanh** → phép đo **luôn cao hơn thực tế một chút**.
⭐ Đây là **sai số một chiều**, không phải nhiễu ngẫu nhiên — nên lấy trung bình **không** khử được.

| Yếu tố | Ảnh hưởng |
|---|---|
| ⭐ Dòng kích lớn | Sai số lớn hơn — nhưng tín hiệu khoẻ hơn, ít nhiễu hơn |
| Dòng kích nhỏ | Sai số nhỏ hơn, nhưng ⚠ **tỉ lệ tín hiệu/nhiễu xấu đi** |
| ⭐ **Môi trường tản nhiệt kém** | ⚠ Nặng nhất trong **không khí tĩnh**; nhẹ hơn nhiều trong chất lỏng chảy |

> ⭐⭐ **Đây là một đánh đổi, không phải một lỗi cần sửa.** Module tốt giải quyết bằng cách **cấp dòng
> theo xung** — chỉ cho dòng chạy trong khoảnh khắc lấy mẫu rồi ngắt. ⭐ Cách đó dùng được vì phép đo
> nhiệt độ vốn **chậm**, không cần lấy mẫu nhanh.
>
> ⚡ **Với người lập trình máy:** bạn thường không chỉnh được dòng kích. Điều cần biết là ⭐ **nếu phép
> đo cao hơn thiết bị chuẩn một chút và ổn định, hãy nghi tự gia nhiệt trước khi nghi cảm biến hỏng**
> — nhất là khi đo trong không khí tĩnh.

*(Đối chiếu: Kuphaldt — Lessons in Industrial Instrumentation, mục RTD self-heating error và mục
về hệ số alpha của RTD bạch kim.)*

### ⚠ Ba lỗi đấu RTD hay gặp

| Lỗi | Hiện tượng |
|---|---|
| **Đấu RTD 3 dây vào module cấu hình 2 dây** | Sai số dây không được bù — đọc cao hơn thực tế, ổn định |
| **Nối chung sợi thứ ba sai chân** | Bù sai — có thể đọc thấp hơn thực tế |
| ⚠ **Ba sợi không cùng chiều dài/tiết diện** | Bù không chính xác; sai lệch nhỏ nhưng dai dẳng |

> 💡 **Cách kiểm nhanh khi nghi sai số dây:** đo bằng một nhiệt kế cầm tay ở cùng vị trí. Chênh lệch
> **ổn định và luôn cùng chiều** là dấu hiệu điển hình của sai số dây, không phải của cảm biến hỏng.
> Kiểm tiếp bằng cách xem cấu hình kênh trong phần mềm: 2, 3 hay 4 dây.

---

## 33.5 ⭐ Can nhiệt và bù đầu lạnh

Can nhiệt hoạt động theo một nguyên lý làm nảy sinh một yêu cầu mà người mới hay bỏ qua.

### Vấn đề

Can nhiệt không đo **nhiệt độ**. Nó sinh ra một điện áp tỉ lệ với **chênh lệch nhiệt độ giữa hai
đầu**: đầu nóng (chỗ đo) và đầu lạnh (chỗ nối vào module).

```text
   [đầu nóng]  ─── dây can nhiệt ───  [đầu lạnh = đầu nối vào module]
    600 °C                              nhiệt độ trong tủ điện
        └────── điện áp sinh ra tỉ lệ với CHÊNH LỆCH ──────┘
```

Muốn biết nhiệt độ đầu nóng, phải biết **nhiệt độ đầu lạnh**. Đó là việc của **bù đầu lạnh**
*(cold junction compensation, CJC)*: module có một cảm biến nhiệt riêng đo chính nhiệt độ tại hàng
kẹp của nó, rồi cộng vào.

> ⚠⚠ **Hệ quả rất thực tế: nhiệt độ trong tủ điện ảnh hưởng phép đo.**
> Nếu bù đầu lạnh sai — cấu hình sai, hoặc cảm biến bù đặt xa hàng kẹp thật — thì phép đo **trôi theo
> nhiệt độ tủ**. Triệu chứng đặc trưng: giá trị đọc **đổi theo giờ trong ngày** hoặc theo việc tủ có
> mở cửa hay không, trong khi quá trình thật không đổi.
>
> Đây là loại lỗi rất khó chẩn đoán nếu không biết cơ chế — và biết rồi thì nó gần như tự lộ.

### ⚠ Dây bù — không được nối bằng dây đồng

Điểm thứ hai, và là lỗi đấu nối phổ biến nhất với can nhiệt:

> **Mọi mối nối trên đường từ can nhiệt về module đều tạo ra một cặp nhiệt điện mới.**

Nối dài can nhiệt bằng **dây đồng thường** tạo ra một đầu lạnh **ở chỗ nối**, không phải ở module. Bù
đầu lạnh của module lúc đó bù nhầm chỗ.

Cách đúng: dùng **dây bù** *(compensating / extension cable)* đúng loại can nhiệt, và ⚠ **đúng cực
tính**. Đấu ngược cực làm giá trị đọc sai theo hướng ngược lại khi nhiệt độ tủ đổi.

> 💡 Với DP-01, cả hai điểm đo nhiệt đều dùng RTD nên không gặp bài toán này. Nhưng bạn sẽ gặp can
> nhiệt ở máy có lò, máy hàn, máy ép nhựa — và khi đó **dây bù và cực tính là hai thứ kiểm đầu tiên**.

---

## 33.6 Đo khoảng cách và vị trí

| Loại | Nguyên lý | ✅ Mạnh | ⚠ Bẫy |
|---|---|---|---|
| **Laser tam giác** *(laser triangulation)* | Chiếu điểm sáng, đo góc phản xạ | Chính xác cao, dải gần | ⚠ **Bề mặt bóng, trong suốt, hoặc màu rất tối** làm sai lệch |
| **Laser thời gian bay** *(time-of-flight)* | Đo thời gian ánh sáng đi và về | Dải xa | Kém chính xác hơn ở dải gần |
| **Siêu âm** *(ultrasonic)* | Đo thời gian sóng âm đi và về | ⭐ Không phụ thuộc màu và độ bóng | ⚠ **Phụ thuộc nhiệt độ không khí**; ⚠ vùng chết ngay trước cảm biến; bề mặt xốp hấp thụ âm |
| **Cảm ứng analog** *(inductive analog)* | Trường điện từ | Bền, chịu bẩn | Chỉ đo kim loại, dải rất ngắn |

> ⚠ **Siêu âm và nhiệt độ không khí:** tốc độ âm thanh đổi theo nhiệt độ, nên phép đo trôi theo nhiệt
> độ môi trường. Nhiều cảm biến có bù tự động — ⚠ **kiểm xem có bật không** trước khi kết luận cảm
> biến "không chính xác".

> ⭐ **Với DP-01, khoảng cách từ đầu tra keo tới mặt board là phép đo đáng cân nhắc** (Chương 37):
> board có thể cong nhẹ, và giữ đúng khoảng cách quyết định chất lượng đường keo. Bề mặt board là
> vật liệu tối, có linh kiện bóng — ⚠ đúng vùng laser tam giác gặp khó. Đây là chỗ **phải thử trên
> vật thật trước khi chốt**, không chọn theo catalogue.

---

## 33.7 Lưu lượng, mức, chân không

Nhóm này ít gặp trên máy lắp ráp điện tử nhưng phổ biến ở máy có chất lỏng và khí.

| Đo cái gì | Loại thường dùng | ⚠ Bẫy chính |
|---|---|---|
| **Lưu lượng khí** | Cảm biến nhiệt, chênh áp | Phụ thuộc áp suất và nhiệt độ — ⚠ phân biệt lưu lượng **thực tế** với **quy chuẩn** |
| **Lưu lượng chất lỏng** | Điện từ, tua-bin, Coriolis | Điện từ ⚠ chỉ đo được chất lỏng **dẫn điện** |
| **Mức chất lỏng** | Phao, siêu âm, radar, chênh áp | Chênh áp ⚠ phụ thuộc **khối lượng riêng** — đổi loại keo là đổi kết quả |
| **Chân không** | Cảm biến chân không | ⚠ Cách ghi dải rất khác nhau; xem bên dưới |

> ⚠ **Chân không — chỗ dễ nhầm nhất.**
> Cùng một mức chân không có thể ghi là `−0,8 bar`, `0,2 bar(a)`, `−80 kPa`, hay `20 % chân không`
> tuỳ hãng và tuỳ quy ước. **Đọc kỹ dải và đơn vị trong datasheet**, và khi lập bảng I/O thì ghi rõ
> quy ước đang dùng (Chương 23).
>
> Trên DP-01, giác hút của cơ cấu gắp dùng cảm biến chân không (Chương 6, mục 6.6) — và nó là ví dụ
> điển hình của nguyên tắc "chờ phản hồi thật, không chờ timer" (Chương 17).

---

## 33.8 Đo cường độ ánh sáng — trường hợp `AI_UvIntensity`

Đèn UV suy giảm cường độ theo giờ chạy. Đây là **lỗi mà máy không tự phát hiện được** nếu không đo
(Chương 48, mục 48.6): sản phẩm thiếu độ bám keo **không có triệu chứng tại chỗ**, chỉ lộ ra ở khách
hàng.

Ba điều cần biết khi đo cường độ UV:

| Điểm | Nội dung |
|---|---|
| **Cảm biến phải đúng dải bước sóng** | UV có nhiều vùng; cảm biến đo vùng khác vùng đèn phát ra sẽ cho số vô nghĩa |
| ⚠ **Vị trí đo quyết định con số** | Cường độ giảm nhanh theo khoảng cách. Đo sát đèn và đo tại mặt board cho hai con số rất khác nhau — ⭐ **đo tại nơi sản phẩm nằm** |
| ⚠ **Cảm biến cũng bám bẩn** | Cường độ đọc được giảm dần có thể là đèn yếu **hoặc** cửa sổ cảm biến bẩn. Phân biệt bằng cách lau rồi đo lại |

> ⚠ **Nhắc lại vấn đề đã nêu ở Chương 31, mục 31.7 và ghi trong hồ sơ máy mẫu §8:**
> `AI_UvIntensity` hiện là **0–10 V**, nên **không phân biệt được "cường độ 0" với "đứt dây"**. Với
> một phép đo mà toàn bộ lý do tồn tại là **phát hiện suy giảm âm thầm**, đây là điểm yếu đáng cân
> nhắc đổi sang 4–20 mA — dù dây ngắn.
>
> Hạng mục này đang chờ chủ dự án quyết.

---

## 33.9 ⭐ Bảng chọn — đo cái gì, dùng loại nào, bẫy gì

| Đo cái gì | Loại thường dùng | ⚠ Bẫy chính |
|---|---|---|
| Áp suất khí nén | Cảm biến áp tương đối, 4–20 mA | Lắp sau chỗ hẹp; xung áp phá cảm biến |
| Áp keo tại đầu tra | Cảm biến áp, 4–20 mA | Lắp xa điểm quan tâm → đo nhầm chỗ |
| Nhiệt độ < 400 °C, cần chính xác | ⭐ **RTD Pt100 3 dây** | Cấu hình module sai số dây; **lắp sai chỗ** (mục 33.1) |
| Nhiệt độ rất cao, hoặc cần nhanh | Can nhiệt | ⚠ Bù đầu lạnh; **dây bù** và cực tính |
| Khoảng cách, bề mặt bất kỳ | Siêu âm | Phụ thuộc nhiệt độ không khí; vùng chết |
| Khoảng cách, cần chính xác | Laser tam giác | ⚠ Bề mặt bóng / trong suốt / rất tối |
| Vị trí trục | Encoder (Chương 18, 37) | Encoder gia số mất vị trí khi mất điện |
| Chân không giác hút | Cảm biến chân không | ⚠ Quy ước ghi dải rất khác nhau |
| Cường độ UV | Cảm biến quang đúng bước sóng | ⭐ Đo **tại nơi sản phẩm nằm**; cảm biến cũng bẩn |
| Lực / khối lượng | Load cell (Chương 34) | — |

### Bốn câu hỏi trước khi chọn bất kỳ cảm biến quá trình nào

> **1. Tôi đang đo cái gì — và nó có phải cái tôi THẬT SỰ quan tâm không?**
> Cỗ máy ở mục 33.1 đo nhiệt độ vỏ bình khi cái đáng quan tâm là nhiệt độ keo.
>
> **2. Lắp ở đâu?** Vị trí thường quyết định nhiều hơn loại cảm biến.
>
> **3. Dải bao nhiêu?** Vừa đủ bao phủ vùng làm việc — sai số tính theo % dải (Chương 32, mục 32.3).
>
> **4. Nó hỏng thế nào, và tôi có phát hiện được không?** Hỏng đứt thì 4–20 mA phát hiện được
> (Chương 31). Hỏng **trôi dần** thì khó hơn nhiều — cần đối chiếu định kỳ với một phép đo độc lập.

Câu 1 và câu 4 là hai câu người ta hay bỏ, và chúng gây ra những sự cố tốn thời gian nhất.

---

## 33.10 Trên máy mẫu DP-01

| Phép đo | Cảm biến | Vì sao chọn vậy | ⚠ Điểm cần chú ý |
|---|---|---|---|
| `AI_AirPress` — áp khí cấp máy | Áp tương đối, 4–20 mA, 2 dây | Điều kiện an toàn — cần phân biệt đứt dây (Ch.31) | Lắp **sau** cụm lọc–điều áp, đo áp thật cấp cho cơ cấu |
| `AI_GluePress` — áp keo tại đầu tra | Áp tương đối, 4–20 mA | Ảnh hưởng trực tiếp chất lượng | ⚠ Lắp **gần đầu tra**, không lắp ở bình chứa |
| Nhiệt độ keo | **RTD Pt100 3 dây** vào bộ điều khiển rời (RS-485) | Dưới 100 °C, cần ổn định | ⚠⚠ **Lắp trong lòng keo, không lắp ở vỏ bình** — mục 33.1 |
| `AI_UvChamberTemp` — nhiệt buồng sấy | **RTD Pt100 3 dây** vào PLC | Giám sát quá nhiệt | Lắp ở vùng nóng nhất, không ở cửa gió |
| `AI_UvIntensity` — cường độ UV | Cảm biến quang UV, 0–10 V | Phát hiện đèn suy giảm | ⚠ Đo **tại mặt board**; đang chờ quyết định đổi sang 4–20 mA |

> ⭐ **Hàng thứ ba là bài học trung tâm của chương.** Cùng một cảm biến, cùng một bộ điều khiển, cùng
> một chương trình — **chỉ khác chỗ lắp**, và kết quả là cả lô sản phẩm hỏng mà mọi chỉ số đều xanh.
>
> Khi lập bảng I/O ở giai đoạn đặc tả (Chương 23), **vị trí lắp phải là một cột**, không phải chi
> tiết để lại cho người lắp máy tự quyết.

---

## 33.11 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| ⚠ **Module RTD trả về gì** | Phần lớn trả **thẳng đơn vị nhiệt độ** (thường 0,1 °C), **không** cần quy đổi thang như Chương 32. ⚠ Nhưng đơn vị và hệ số khác nhau — tra datasheet |
| Cấu hình số dây RTD | Đặt trong cấu hình kênh: 2, 3 hay 4 dây. ⭐ **Sai chỗ này là sai số dây không được bù** (mục 33.4) |
| Loại RTD và loại can nhiệt | Chọn Pt100/Pt1000, loại K/J/T… trong cấu hình kênh. Chọn nhầm loại → đường cong quy đổi sai |
| Bù đầu lạnh | Thường tích hợp trong module can nhiệt; một số hệ cho dùng cảm biến bù ngoài |
| Phát hiện đứt cảm biến | Nhiều module RTD/can nhiệt có bit báo đứt — ⭐ dùng nó (Chương 31, mục 31.8) |
| Thời gian cập nhật kênh | ⚠ Module nhiệt độ thường **chậm hơn** module analog thường — vài trăm ms mỗi kênh. Ảnh hưởng vòng điều khiển (Chương 35) |

> ⚠ **Hàng cuối đáng chú ý khi viết vòng điều khiển nhiệt độ.** Nếu module cập nhật 500 ms mỗi kênh
> mà bạn chạy vòng PID với chu kỳ 100 ms, thì bốn trong năm lần tính là **dựa trên cùng một giá trị
> cũ** — vòng điều khiển hoạt động không như bạn tưởng. Chương 35 quay lại điểm này.

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

---

## 33.12 Bẫy thường gặp

### 🔍 BẪY 1 — Lắp cảm biến sai chỗ

**Hiện tượng:** phép đo ổn định, thiết bị đúng, con số hợp lý — nhưng **không phản ánh cái bạn quan
tâm**. Đúng cỗ máy ở mục 33.1.
**Cách sửa:** hỏi câu 1 và câu 2 ở mục 33.9 **trước khi mua**; đưa **vị trí lắp** thành một cột trong
bảng I/O.

### 🔍 BẪY 2 — RTD 2 dây cho đường dài

**Hiện tượng:** nhiệt độ đọc **luôn cao hơn** thực tế, ổn định, không có dấu hiệu bất thường nào.
**Cách sửa:** dùng 3 dây và **cấu hình module đúng 3 dây** — cả hai việc, không phải một (mục 33.4).

### 🔍 BẪY 3 — Đấu RTD 3 dây nhưng module cấu hình 2 dây

**Hiện tượng:** giống hệt Bẫy 2 — sợi thứ ba có mà không được dùng.
**Cách sửa:** kiểm cấu hình kênh trong phần mềm. ⚠ Đây là chỗ **phần cứng đúng mà phần mềm sai**, nên
người kiểm tủ không phát hiện được.

### 🔍 BẪY 4 — Nối dài can nhiệt bằng dây đồng

**Hiện tượng:** giá trị đọc **trôi theo nhiệt độ tủ điện** — đổi theo giờ trong ngày, đổi khi mở cửa
tủ, trong khi quá trình thật không đổi.
**Cách sửa:** dùng **dây bù đúng loại**, đúng cực tính (mục 33.5).

### 🔍 BẪY 5 — Nhầm áp tương đối với áp tuyệt đối

**Hiện tượng:** mọi phép đo lệch khoảng 1 bar, ổn định, và trông hợp lý.
**Cách sửa:** đọc kỹ ký hiệu `bar(g)` / `bar(a)` trong datasheet; ghi rõ vào bảng I/O (mục 33.2).

### 🔍 BẪY 6 — Laser tam giác trên bề mặt bóng hoặc rất tối

**Hiện tượng:** giá trị nhảy, hoặc mất tín hiệu, **chỉ với một số loại sản phẩm** — nên rất khó tái
hiện khi thử.
**Cách sửa:** ⭐ thử **trên vật thật** trước khi chốt loại cảm biến, không chọn theo catalogue
(mục 33.6).

### 🔍 BẪY 7 — Siêu âm không bật bù nhiệt độ

**Hiện tượng:** phép đo trôi theo nhiệt độ môi trường; sáng và chiều cho hai kết quả khác nhau.
**Cách sửa:** kiểm xem cảm biến có bù tự động và đã bật chưa (mục 33.6).

### 🔍 BẪY 8 — Đo cường độ UV sát đèn thay vì tại mặt board

**Hiện tượng:** cường độ đọc được vẫn tốt trong khi sản phẩm thiếu độ bám keo.
**Cách sửa:** đo **tại nơi sản phẩm nằm** (mục 33.8).

### 🔍 BẪY 9 — Quy cường độ UV giảm cho đèn, quên cảm biến bẩn

**Hiện tượng:** thay đèn mới nhưng cường độ đọc được vẫn thấp.
**Cách sửa:** lau cửa sổ cảm biến rồi đo lại **trước khi** kết luận đèn yếu (mục 33.8).

### 🔍 BẪY 10 — Không biết cảm biến hỏng theo kiểu trôi dần

**Hiện tượng:** cảm biến không đứt, không báo lỗi, chỉ **lệch dần** theo tháng. Chuẩn 4–20 mA không
phát hiện được vì giá trị vẫn nằm trong dải hợp lệ.
**Cách sửa:** đối chiếu định kỳ với một phép đo độc lập — đồng hồ cơ khí, nhiệt kế cầm tay — và ghi
lại kết quả để thấy xu hướng (mục 33.9 câu 4; Chương 51).

---

## 33.13 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| ⚠ Pt100 có mấy hệ số | ⭐ **Hai** — 0,00385 (phổ biến) và 0,00392. Trộn nhầm thì **lệch có hệ thống**, đồ thị vẫn đẹp |
| ⭐ Vì sao RTD đọc cao hơn một chút | **Tự gia nhiệt** — dòng đo sinh nhiệt trên chính phần tử; ⚠ nặng nhất trong **không khí tĩnh** |
| Sai lầm phổ biến nhất với cảm biến quá trình | ⭐ **Lắp sai chỗ**, không phải chọn sai loại |
| Áp tương đối vs tuyệt đối | Chênh ~1 bar; khí nén công nghiệp mặc định **tương đối** |
| Nhiệt độ < 400 °C, cần chính xác | **RTD Pt100** |
| Nhiệt độ rất cao hoặc cần nhanh | **Can nhiệt** |
| RTD mấy dây | ⭐ **3 dây là mặc định** — bù được sai số dây, chỉ thêm một sợi |
| RTD 2 dây sai theo hướng nào | **Luôn cao hơn** thực tế, ổn định — không phát hiện được từ dữ liệu |
| Đấu 3 dây thì còn phải làm gì | ⭐ **Cấu hình module đúng 3 dây** — hai việc, không phải một |
| Can nhiệt cần gì | **Bù đầu lạnh** + **dây bù đúng loại, đúng cực** |
| Can nhiệt nối dây đồng — triệu chứng | Giá trị **trôi theo nhiệt độ tủ** |
| Laser tam giác gặp khó với | Bề mặt **bóng, trong suốt, rất tối** — thử trên vật thật |
| Siêu âm gặp khó với | **Nhiệt độ không khí**, vùng chết, bề mặt xốp |
| Cảm biến chân không | ⚠ Quy ước ghi dải **rất khác nhau** giữa các hãng |
| Đo cường độ UV ở đâu | ⭐ **Tại nơi sản phẩm nằm** |
| Bốn câu hỏi trước khi chọn | Đo cái gì · lắp ở đâu · dải bao nhiêu · **hỏng thế nào thì phát hiện được không** |
| Module RTD trả về gì | Thường **thẳng đơn vị nhiệt độ** — không cần quy đổi thang |
| ⚠ Module nhiệt độ cập nhật | **Chậm hơn** module analog thường — ảnh hưởng vòng PID (Ch.35) |

---

## 33.14 Tự kiểm

1. ⭐ Nhiệt độ hiển thị 60,0 °C, ổn định, bộ điều khiển báo đạt điểm đặt — nhưng sản phẩm vẫn hỏng.
   Nêu nguyên nhân khả dĩ nhất và bài học tổng quát.
2. Phân biệt áp suất tương đối với áp suất tuyệt đối. Lắp nhầm loại thì triệu chứng là gì?
3. So sánh RTD với can nhiệt trên năm tiêu chí. Với nhiệt độ 60 °C cần ổn định, chọn loại nào?
4. ⭐ Vì sao RTD đấu 2 dây cho kết quả **luôn cao hơn** thực tế? Tính sai số cho một đôi dây có tổng
   điện trở 2 Ω với Pt100.
5. ⭐ Vì sao **3 dây là mặc định của ngành** thay vì 2 hoặc 4? Giả định của cách 3 dây là gì, và điều
   gì phá vỡ giả định đó?
6. Đấu RTD 3 dây nhưng cấu hình module là 2 dây. Triệu chứng là gì, và vì sao người kiểm tủ không
   phát hiện được?
7. ⭐ Can nhiệt đo cái gì — nhiệt độ hay chênh lệch nhiệt độ? Từ đó suy ra vì sao cần **bù đầu lạnh**.
8. Vì sao **không** được nối dài can nhiệt bằng dây đồng thường? Triệu chứng đặc trưng khi làm sai là gì?
9. Bề mặt nào làm laser tam giác gặp khó? Với board mạch có linh kiện bóng, bạn làm gì trước khi chốt
   loại cảm biến?
10. Cường độ UV đọc được giảm dần. Nêu **hai** nguyên nhân khác nhau về bản chất và cách phân biệt.
11. Nêu bốn câu hỏi phải đặt trước khi chọn một cảm biến quá trình. Hai câu nào hay bị bỏ nhất?
12. ⭐ Cảm biến **trôi dần** mà không đứt: vì sao chuẩn 4–20 mA không phát hiện được, và bạn phát hiện
    bằng cách nào?

> Câu 1, 4, 5, 7 và 12 là năm câu phân loại. Câu 1 là tinh thần của cả chương: **phép đo đúng ở sai
> chỗ vẫn là phép đo sai — và nó nguy hiểm hơn phép đo hỏng, vì mọi chỉ số đều xanh.**

⚠ **Bổ sung.** Pt100 có hai hệ số alpha — trộn nhầm cảm biến và cấu hình module gây sai số kiểu gì,
và vì sao nó **khó phát hiện**? Vì sao RTD luôn đọc **cao hơn** thực tế một chút, và lấy trung bình
có khử được sai số đó không?

---

### Chương tiếp theo

Chương 34 — **Cân & đo lực**. Bạn đã có các phép đo quá trình cơ bản. Chương sau về một phép đo đặc
biệt hữu ích trong lắp ráp điện tử: **lực theo hành trình** — cách phát hiện lỗi lắp ráp mà cảm biến
đóng/tắt không bao giờ thấy được.

### Nguồn tham khảo chương 33

- IEC 60751 — *Industrial platinum resistance thermometers and platinum temperature sensors*: đặc
  tính Pt100/Pt1000, hệ số nhiệt, và cấp chính xác. *(tiêu chuẩn có bản quyền)*
- IEC 60584 (bộ) — *Thermocouples*: các loại can nhiệt, bảng chuyển đổi điện áp–nhiệt độ, dung sai,
  và ⚠ **yêu cầu với dây bù**.
- IEC 61131-2 — *Programmable controllers, Part 2*: yêu cầu với module vào analog, trong đó có module
  nhiệt độ.
- **Datasheet module nhiệt độ** của hệ đang dùng — dùng cho: đơn vị trả về, cấu hình số dây, loại
  RTD/can nhiệt hỗ trợ, ⚠ **thời gian cập nhật kênh**, và bit phát hiện đứt cảm biến.
- **Datasheet cảm biến** — dùng cho sai số, dải, ⚠ **quy ước ghi dải chân không**, và yêu cầu lắp đặt.
- Bảng I/O của DP-01 — Phụ lục J; bảng ở mục 33.10 lấy từ đó.

> ⚡ Con số **0,385 Ω/°C** cho Pt100 ở mục 33.4 là **hệ số danh định** theo đường cong chuẩn, dùng để
> ước lượng bậc độ lớn của sai số. Quan hệ điện trở–nhiệt độ thật **không hoàn toàn tuyến tính**;
> phép quy đổi chính xác theo đường cong trong tiêu chuẩn, và module đã làm việc đó cho bạn.
>
> ⚠ Các nhận định về **loại bề mặt gây khó cho từng loại cảm biến khoảng cách** ở mục 33.6 là kinh
> nghiệm nghề ở mức định hướng. Với ứng dụng thật, cách duy nhất đáng tin là **thử trên vật thật của
> bạn**, trong điều kiện chiếu sáng và rung thật của máy.
