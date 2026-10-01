# Chương 8 — Kiến trúc phần cứng PLC

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 8.1 Vì sao người lập trình phải hiểu phần cứng

Bạn có thể viết chương trình mà không biết bên trong tủ có gì. Rất nhiều người làm vậy, cho tới lần
đầu gặp một trong bốn tình huống sau:

- Máy chạy đúng ở bàn thử, sai ở hiện trường — vì I/O phân tán có **thời gian đáp ứng khác** với I/O
  gắn ngay trên CPU.
- Thêm một cảm biến, phải sửa **toàn bộ địa chỉ** của các module phía sau — vì cách đánh địa chỉ phụ
  thuộc vị trí cắm.
- Mất điện cuối tuần, sáng thứ Hai máy **không còn chương trình** — vì pin đã hết từ tháng trước.
- Người bảo trì gạt công tắc trên CPU để "thử", và cỗ máy **dừng toàn bộ ngõ ra giữa chu trình**.

Bốn tình huống này đều là quyết định phần cứng, và ba trong bốn được chốt **trước khi** ai đó viết
dòng code đầu tiên. Chương này là lượng kiến trúc tối thiểu để bạn tham gia được vào các quyết định
đó, và để hiểu vì sao chương trình của bạn hành xử như nó đang hành xử.

---

## 8.2 Năm khối của một hệ PLC

```text
   ┌──────────────────────────────────────────────────────────┐
   │  ┌────────┐  ┌────────┐  ┌────────┐  ┌────────┐          │
   │  │ NGUỒN  │  │  CPU   │  │  DI    │  │  DO    │  ...     │
   │  │  PSU   │  │        │  │ 16 kênh│  │ 16 kênh│          │
   │  └────────┘  └────────┘  └────────┘  └────────┘          │
   │  ════════════ BACKPLANE / bus nối các module ════════════ │
   └──────────────────────────────────────────────────────────┘
              │                    │            │
         nguồn 24 V          cảm biến      cơ cấu chấp hành
```

| Khối | Việc của nó | Điều người lập trình cần biết |
|---|---|---|
| **Nguồn** *(power supply, PSU)* | Cấp điện cho CPU và module | Công suất phải đủ cho **cả tải I/O**, không chỉ cho CPU — mục 8.7 |
| **CPU** | Chạy chương trình, quản lý vòng quét | Bộ nhớ, tốc độ, số module tối đa, cổng mạng có sẵn |
| **Backplane / bus** | Nối CPU với các module | Quyết định **thứ tự địa chỉ** và số khe cắm |
| **Module vào/ra** | Cầu nối giữa tín hiệu điện và bit trong bộ nhớ | Kiểu ngõ vào/ra — Chương 9 |
| **Module chức năng** | Việc chuyên biệt: analog, đếm tốc độ cao, truyền thông, chuyển động | Phải chọn **lúc mua**, không thêm được bằng phần mềm |

### Ba dáng hình phổ biến

| Dáng | Mô tả | Hợp với | Ví dụ dòng sản phẩm |
|---|---|---|---|
| **Nguyên khối** *(brick / compact)* | CPU + I/O + nguồn trong một khối, mở rộng hạn chế | Máy nhỏ, số I/O cố định, giá thấp | Siemens S7-1200 · Mitsubishi FX5U · Rockwell Micro850 · Inovance H5U |
| **Module hoá** *(modular / rack)* | CPU riêng, cắm module vào rack theo nhu cầu | Máy vừa và lớn, cần linh hoạt | Siemens S7-1500 · Mitsubishi iQ-R · Rockwell ControlLogix · Inovance AM600 |
| **PLC mềm** *(soft-PLC)* | Chương trình chạy trên máy tính công nghiệp hoặc bộ điều khiển nhúng | Cần tích hợp với PC, thị giác máy, nhiều trục | Beckhoff TwinCAT · CODESYS trên phần cứng của nhiều hãng |

> ⚡ **LƯU Ý — số liệu chi tiết phải tra tài liệu hiện hành**
> Sách nêu **tên dòng sản phẩm để bạn biết đường tìm và so sánh**. Số kênh, dung lượng bộ nhớ, số
> module tối đa, tốc độ xử lý đổi theo từng đời và từng phiên bản firmware. Mọi con số cụ thể phải
> lấy từ **catalogue và datasheet hiện hành của hãng**, kèm ngày kiểm tra — đừng lấy từ sách, kể cả
> sách này (xem `docs/00c_Tai_lieu_tham_khao.md`).

---

## 8.3 CPU — cái gì ở bên trong

Bốn thứ bạn cần biết về CPU của mình:

| Thông số | Nghĩa thực tế | Hậu quả khi thiếu |
|---|---|---|
| **Bộ nhớ chương trình** | Chứa được chương trình lớn tới đâu | Chương trình lớn dần theo năm; hết bộ nhớ giữa dự án là thảm hoạ tiến độ |
| **Bộ nhớ dữ liệu** | Số biến, mảng, khối dữ liệu | Thanh ghi dịch và bảng công thức ăn bộ nhớ nhanh (Chương 19, 29) |
| **Tốc độ xử lý** | Thường ghi theo thời gian cho 1 000 lệnh nhị phân | Quyết định thời gian quét — Chương 10 |
| **Số module / số I/O tối đa** | Trần mở rộng | Chạm trần nghĩa là **đổi CPU**, không phải mua thêm module |

> 💡 **MẸO — quy tắc dự phòng 20 %**
> Chọn CPU và số I/O dư ít nhất 20 % so với nhu cầu tính toán. Lý do không phải "phòng hờ" chung
> chung: gần như **mọi** máy đều được thêm chức năng sau khi nghiệm thu — thêm một cảm biến kiểm tra,
> thêm một đèn báo, thêm tín hiệu bắt tay với máy bên cạnh. Không còn khe cắm nghĩa là phải dừng máy
> đang sản xuất để thay rack (Chương 13).

### Đèn trạng thái trên CPU

Mọi CPU đều có một nhóm đèn báo, và chúng là **thứ đầu tiên nhìn khi tới máy hỏng**:

| Đèn | Thường có nghĩa |
|---|---|
| **RUN** | Chương trình đang chạy |
| **STOP** | CPU dừng — không quét chương trình, ngõ ra ở trạng thái đã cấu hình |
| **ERROR / FAULT** | Lỗi CPU hoặc lỗi cấu hình |
| **BAT / MAINT** | Pin yếu hoặc cần bảo trì |
| Đèn cổng mạng | Có liên kết vật lý / đang truyền |

Ý nghĩa chính xác — nhất là kiểu nháy — **khác nhau giữa các hãng**, và đây là chỗ đọc nhầm rất tốn
thời gian. Bảng đối chiếu đèn theo từng hệ nằm ở Phụ lục A; Chương 51 dùng nó trong quy trình chẩn
đoán.

---

## 8.4 Backplane và cách đánh địa chỉ module

### Vấn đề

Chương trình gọi tên `DI_BoardStn1`. Nhưng bit đó nằm ở kênh nào, module nào, khe nào? Câu trả lời
là **cấu hình phần cứng** — một phần của dự án, tách khỏi chương trình.

Hai cách gán địa chỉ, và khác biệt giữa chúng ảnh hưởng trực tiếp tới việc bảo trì:

| Cách | Cơ chế | Hậu quả khi thêm/bớt module |
|---|---|---|
| **Theo vị trí** *(slot-based)* | Địa chỉ suy ra từ khe cắm; module ở khe 3 luôn có địa chỉ cố định | Thêm module vào **giữa** rack có thể **dịch địa chỉ** của mọi module phía sau |
| **Gán tường minh** | Người kỹ sư đặt địa chỉ đầu cho từng module trong cấu hình | Ổn định hơn; nhưng phải quản lý để không trùng |

> ⚠ **NGUY HIỂM — dịch địa chỉ là lỗi im lặng và rất nguy hiểm**
> Nếu địa chỉ dịch mà chương trình vẫn dùng địa chỉ tuyệt đối cũ, thì mỗi tag bây giờ **trỏ vào một
> thiết bị khác**. Chương trình vẫn biên dịch được, CPU vẫn chạy, không có báo lỗi nào — nhưng lệnh
> "nâng kẹp" có thể đang mở van tra keo.
>
> Hai biện pháp, dùng cả hai:
> - **Dùng tag có tên, không dùng địa chỉ tuyệt đối** trong chương trình (Chương 11). Khi đó chỉ cần
>   sửa ánh xạ ở một chỗ.
> - **Sau bất kỳ thay đổi phần cứng nào, kiểm I/O 1-1 lại** cho các kênh bị ảnh hưởng — Chương 52,
>   mục 52.4. Không có ngoại lệ "chỉ thêm một module thôi mà".

### Chừa khe trống

Chừa sẵn khe trống ở **cuối** rack, không phải ở giữa. Thêm module vào cuối thì địa chỉ các module cũ
không đổi.

### ⭐⭐ Bản đồ khe cắm phải là một TÀI LIỆU

⭐ Hai mục trên dẫn tới một kết luận mà người ta hay bỏ qua: nếu **thứ tự khe quyết định địa chỉ**,
thì ⭐⭐ **thứ tự khe là một phần của chương trình** — chỉ có điều nó **không nằm trong tệp dự án**.
Nó nằm trong cái rack, và trong đầu người đã lắp.

> ⚠⚠ **Cả hai chỗ đó đều không đáng tin sau hai năm.** Người lắp đã đổi việc; còn cái rack thì
> ⭐ **không nói được vì sao khe 5 để trống** — để dự phòng, hay vì module ở đó đã tháo đi mà chưa
> ai cập nhật gì?

⭐ Vì vậy cấu hình phần cứng phải được ghi thành một bảng, và bảng đó phải trả lời được **bốn câu**:

| # | Câu hỏi | ⚠ Không trả lời được thì |
|---|---|---|
| 1 | Tag này nằm ở **module nào, khe nào, kênh nào**? | Phải mở tủ đếm — mỗi lần chẩn đoán mất thêm mười phút |
| 2 | ⭐ **Còn bao nhiêu kênh dự phòng** trên mỗi module? | Không trả lời được khách khi họ hỏi *"thêm một cảm biến được không"* |
| 3 | Module này **phiên bản firmware nào**? | ⚠ Thay bằng module cùng mã khác phiên bản có thể **đổi hành vi** mà không báo gì |
| 4 | ⭐⭐ Khe trống này để **dự phòng** hay là **chỗ module đã tháo**? | ⚠ Người sau sẽ cắm vào đó, và **địa chỉ dịch** — đúng lỗi im lặng ở khung trên |

> ⭐ **Biểu mẫu sẵn có: Phụ lục C.10.** Nó cũng là **mục số 2** trong bộ sao lưu tám hạng mục ở
> Phụ lục C.9 — ⚡ nghĩa là không có nó thì **bộ sao lưu của bạn chưa đầy đủ**, dù tệp dự án PLC đã
> lưu đủ (Chương 54).

---

## 8.5 I/O tại chỗ, mở rộng, và phân tán

Ba cách đưa tín hiệu về CPU:

| Kiểu | Vị trí | Nối bằng | Thời gian đáp ứng |
|---|---|---|---|
| **Tại chỗ** *(local / on-board)* | Ngay trên CPU | Mạch trong | Nhanh nhất |
| **Mở rộng** *(expansion)* | Cùng rack hoặc rack kề, cạnh CPU | Backplane | Nhanh |
| **Phân tán** *(remote I/O / distributed I/O)* | Đặt rải trong máy, gần thiết bị | **Mạng công nghiệp** | ⚠ Chậm hơn, và **phụ thuộc mạng** |

### Vì sao I/O phân tán thắng khi máy dài

Với một cỗ máy dài vài mét trở lên, đưa mọi dây cảm biến về một tủ trung tâm nghĩa là:

- hàng trăm sợi dây dài, mỗi sợi là một chi phí và một điểm hỏng;
- máng cáp lớn, khó đi, khó sửa;
- ⚠ **dây tín hiệu dài chạy song song dây động lực** — nguồn nhiễu chính (Chương 49, Chương 51);
- lắp ráp và chạy thử chậm, vì mọi việc dồn về một chỗ.

I/O phân tán đặt một khối I/O nhỏ **ngay tại vùng thiết bị**, rồi nối về CPU bằng **một** sợi cáp
mạng. Trên một máy như DP-01 mở rộng thành dây chuyền nhiều trạm, cách này thắng rõ ràng.

Các mạng hay dùng cho I/O phân tán (chi tiết từng mạng ở Chương 40): PROFINET và PROFIBUS của
Siemens, EtherNet/IP của Rockwell, EtherCAT của Beckhoff, CC-Link IE của Mitsubishi — cả bốn đều
được nhiều hãng khác hỗ trợ — và Modbus TCP, thứ gần như mọi hãng đều có (Chương 40).

### Cái giá phải trả

> ⚠⚠ **NGUY HIỂM — I/O phân tán đưa mạng vào giữa chương trình và thiết bị**
>
> - **Thời gian đáp ứng dài hơn và biến động.** Tín hiệu phải đi qua chu kỳ cập nhật của mạng, cộng
>   thêm vào vòng quét. Với logic thường thì không sao; với việc cần phản ứng nhanh và **ổn định** —
>   bắt vị trí, đếm xung, cắt theo chiều dài — thì phải kiểm tính toán, hoặc để việc đó tại chỗ.
> - **Mất mạng nghĩa là mất cả cụm I/O.** Chương trình phải **phát hiện và xử lý** được, không phải
>   chạy tiếp như thể mọi cảm biến đều bằng 0. Đây là nội dung Chương 48, mục 48.5.
> - ⚠ **I/O phân tán thông thường không phải I/O an toàn.** Truyền tín hiệu an toàn qua mạng cần
>   giao thức an toàn chuyên dụng và thiết bị được chứng nhận. Không tự làm — Chương 47.

Trên DP-01, `DI_EStopOK` và `DI_Door1Closed` đến từ **rơ-le an toàn phần cứng** (Chương 47), không
phải từ một khối I/O phân tán thường. PLC chỉ **đọc để biết** trạng thái mạch an toàn; nó không tham gia vào việc
thực hiện chức năng an toàn đó.

---

## 8.6 Giữ chương trình khi mất điện — pin, thẻ nhớ, bộ nhớ trong

Ba thứ khác nhau, hay bị gộp làm một:

| | Giữ gì | Mất khi |
|---|---|---|
| **Bộ nhớ chương trình không mất** *(flash / EEPROM)* | Chương trình và cấu hình phần cứng | Gần như không mất — không cần pin |
| **Thẻ nhớ** *(memory card)* | Bản sao chương trình; ở một số hệ là **nơi chứa chính** | Rút thẻ ra |
| **Pin / siêu tụ** | Vùng nhớ **giữ được** *(retentive)* và đồng hồ thời gian thực | ⚠ Pin hết |

> ⚠ **NGUY HIỂM — hai hiểu nhầm phổ biến, hậu quả khác nhau**
>
> **Hiểu nhầm 1: "hết pin là mất chương trình".** Với phần lớn PLC hiện đại, chương trình nằm trong
> bộ nhớ flash và **không** phụ thuộc pin. Hết pin thì mất **dữ liệu giữ được** — số liệu sản xuất,
> tổng giờ chạy, đồng hồ (Chương 16, mục 16.4; Chương 18, mục 18.6).
>
> **Hiểu nhầm 2: "chương trình luôn an toàn".** Với một số hệ, **thẻ nhớ là nơi chứa chính** — rút
> thẻ hoặc thẻ hỏng thì CPU không có chương trình để chạy. Và với PLC đời cũ dùng RAM có pin nuôi thì
> hết pin **đúng là** mất chương trình.
>
> **Phải tra tài liệu của đúng hệ mình đang dùng.** Đây là chỗ suy từ hệ khác sang là sai.

Ba việc bắt buộc, không phụ thuộc hệ nào:

- **Có bản sao lưu chương trình ở ngoài máy**, và **đã thử khôi phục ít nhất một lần**. Bản sao lưu
  chưa thử khôi phục không phải bản sao lưu (Chương 54).
- **Thay pin theo lịch**, trước khi đèn báo yếu — thay khi CPU còn điện, để không mất dữ liệu giữ
  được trong lúc thay (Chương 51).
- **Số liệu sản xuất quan trọng không chỉ nằm trong vùng nhớ giữ được** — ghi ra nơi khác định kỳ.

---

## 8.7 Tính công suất nguồn 24 V

Đây là phép tính hay bị bỏ, và hậu quả của nó là loại sự cố khó chịu nhất: **máy chạy được, nhưng
chập chờn**.

Bộ nguồn 24 V phải cấp cho:

| Phụ tải | Ghi chú |
|---|---|
| CPU và module (nếu dùng chung nguồn) | Tra dòng tiêu thụ từng module |
| **Cảm biến** | Mỗi cảm biến vài chục mA; nhân với số lượng |
| **Cuộn van điện từ** | Vài trăm mA mỗi cuộn — đây là phụ tải lớn nhất |
| Đèn báo, đèn tháp, còi | |
| Rơ-le trung gian, rơ-le an toàn (Chương 47) | |
| Thiết bị mạng, bộ chuyển mạch | |

> ⚠⚠ **Trước khi tính công suất, kiểm một điều kiện KHÔNG thương lượng được: bộ nguồn phải là loại
> cách ly an toàn** — đạt **SELV / PELV / Class 2 / Limited Power**. Công suất đủ mà cách ly sai thì
> ⚠ **điện áp lưới có thể xuất hiện trên dây cảm biến** (Chương 3, mục 3.3).

Cộng lại rồi **nhân hệ số dự phòng 1,3–1,5**. Ba lý do cụ thể, không phải "cho chắc":

- **Dòng khởi động** *(inrush current)* của cuộn van và đèn cao hơn dòng làm việc trong vài mili-giây.
- **Trường hợp xấu nhất**: có thời điểm nhiều cơ cấu cùng tác động — tính theo lúc đó, không theo
  trung bình.
- **Máy sẽ được thêm thiết bị** sau khi nghiệm thu.

> ⚠ **Triệu chứng của nguồn thiếu công suất — đáng nhớ vì rất dễ chẩn đoán nhầm**
> Máy chạy bình thường phần lớn thời gian. Khi nhiều cơ cấu cùng tác động, điện áp **sụt** trong vài
> chục mili-giây. CPU có thể khởi động lại, hoặc một số ngõ vào đọc sai, hoặc mạng rớt gói.
>
> Triệu chứng trông **giống hệt lỗi phần mềm**: "thỉnh thoảng máy bị lỗi lạ ở bước 4". Người ta đi
> tìm trong chương trình — nơi không có lỗi nào. Cách xác nhận: **đo điện áp 24 V bằng máy hiện sóng
> đúng lúc nhiều cơ cấu cùng tác động**, không đo bằng đồng hồ vạn năng (đồng hồ trung bình hoá và
> giấu mất cú sụt). Chương 51, Chương 52 mục 52.3.

> 💡 **MẸO — tách nguồn theo nhóm**
> Dùng nguồn riêng, hoặc ít nhất là **nhánh cầu chì riêng**, cho ba nhóm: (1) CPU và module, (2) cảm
> biến, (3) cơ cấu chấp hành. Nhờ vậy một cuộn van chập không kéo sập CPU, và khi chẩn đoán bạn cô
> lập được từng nhóm. Chi phí thêm rất nhỏ so với giá trị lúc sự cố.

---

## 8.7b ⚠ Nhiệt và cách lắp — con số datasheet đổi theo cách bạn gắn module

Mục 8.7 tính dòng. Nhưng ⭐ **mọi con số định mức trong datasheet đều gắn với một điều kiện nhiệt**,
và điều kiện đó dễ bị vi phạm hơn người ta tưởng.

### ⚠⚠ Lắp đứng làm giảm nhiệt độ cho phép

Module PLC toả nhiệt và dựa vào **đối lưu tự nhiên** — không khí nóng đi lên qua các khe tản nhiệt.
⭐ Xoay module 90° là phá hướng đối lưu đó.

| Cách lắp | Nhiệt độ môi trường cho phép |
|---|---|
| ⭐ **Nằm ngang** (hướng thiết kế) | Định mức đầy đủ |
| ⚠ **Lắp đứng** | ⭐⭐ **Giảm khoảng 10 °C** so với định mức |

> ⚠⚠ **Con số 10 °C đó thường là khác biệt giữa "chạy được" và "không".**
>
> Một module ghi 0–55 °C lắp ngang chỉ còn khoảng 0–45 °C khi lắp đứng. ⭐ Trong một tủ điện mùa hè
> không có quạt, nhiệt độ bên trong vượt 45 °C là chuyện bình thường.
>
> ⚠ Triệu chứng: máy chạy tốt suốt mùa mát, ⭐ **bắt đầu lỗi chập chờn vào buổi chiều mùa nóng**, rồi
> tự khỏi vào sáng hôm sau. Người ta đi tìm trong chương trình (Phụ lục E.10, nghi phạm số 7).

### ⭐ Ba điều kiện lắp đặt khác cũng có trong datasheet

| Điều kiện | Vì sao |
|---|---|
| ⭐ **Khoảng trống trên/dưới và phía trước module** | Đối lưu cần đường đi; nhà sản xuất ghi số milimét cụ thể |
| ⚠ **Môi trường rung mạnh** | ⭐ Lắp bằng **vít vào tấm đế** chắc hơn lắp trên **ray DIN** |
| ⭐ **Cấp bảo vệ của chính module** | ⚠ Module PLC thường chỉ đạt cấp **chống vật rắn lớn, không chống nước** |

### ⚠⚠ Khoảng cách lắp trong tài liệu hãng có GIẢ ĐỊNH NGẦM — và máy của bạn dễ vi phạm

⭐ Con số milimét ở bảng trên **không phải hằng số vật lý**. Nhà sản xuất tính nó cho một **tình huống
điển hình**, và tình huống đó có bốn điều kiện:

| Điều kiện điển hình | Nghĩa là |
|---|---|
| ⭐ **~60 % ngõ vào** BẬT tại một thời điểm | Không phải mọi cảm biến cùng tác động |
| ⭐⭐ **~30 % ngõ ra** BẬT tại một thời điểm | ⚠ **Đây là điều kiện dễ vi phạm nhất** |
| Tổng dòng các module nằm trong đặc tả | Mục 8.7 |
| ⭐ Nhiệt độ không khí khoảng **40 °C** | ⚠ Không phải 25 °C như người ta hay hình dung |

> ⚠⚠ **Máy của bạn có thể không "điển hình" mà không ai để ý.**
>
> Một máy có nhiều van giữ **bật liên tục** trong suốt chu trình, hoặc dàn đèn báo luôn sáng, dễ dàng
> vượt xa mức 30 % ngõ ra. ⭐ Khi đó **khoảng cách lắp phải LỚN HƠN** con số trong tài liệu — chứ
> không phải vừa đủ theo bảng.
>
> ⭐ Và nhớ chiều so sánh: điều kiện điển hình là **40 °C**, nên tủ ở 45 °C **đã là khắc nghiệt hơn
> điển hình**, không phải "vẫn còn xa giới hạn 55 °C".

> ⭐ **Ba việc rẻ tiền khi máy không điển hình:**
>
> | | |
> |---|---|
> | 1 | ⭐ **Nới khoảng cách** giữa các module — rẻ nhất, làm lúc thiết kế tủ |
> | 2 | ⭐ **Quạt tuần hoàn** để phá điểm nóng cục bộ quanh PLC |
> | 3 | ⚠⚠ **Gió của quạt phải qua phin lọc trước** — ⭐ bụi bám vào bề mặt tản nhiệt làm **giảm chính khả năng thoát nhiệt** mà quạt đang cố cải thiện (Chương 51, mục 51.11) |
>
> ⚡ Ba việc trên xử lý được phần lớn trường hợp. Nhiệt cao **kéo dài** thì mới tính tới điều hoà tủ.

> ⭐⭐ **Hàng cuối là điều dễ hiểu nhầm: bản thân module PLC gần như không chống được bụi mịn và
> nước.** Cái chống là **vỏ tủ**. ⚠ Nghĩa là cấp bảo vệ ghi trên tủ mới là cấp bảo vệ thật của hệ —
> và mở cửa tủ để "cho mát" là **bỏ luôn lớp bảo vệ đó**, đồng thời đưa bụi dẫn điện vào trong.
>
> ⭐ Muốn mát thì dùng **quạt có lọc** hoặc **điều hoà tủ**, không phải mở cửa.

*(Đối chiếu: Siemens S7-1200 System Manual — cảnh báo lắp đứng giảm nhiệt độ môi trường cho phép,
yêu cầu khoảng trống lắp đặt, khuyến nghị lắp vít khi rung mạnh, và cấp bảo vệ của module. ⚠ Con số
cụ thể **khác nhau theo dòng** — tra datasheet của dòng bạn dùng.)*

---

## 8.8 Công tắc RUN / STOP / REM và ý nghĩa an toàn

Nhiều CPU có công tắc chọn chế độ, thường ba vị trí:

| Vị trí | Nghĩa |
|---|---|
| **RUN** | Chạy chương trình; ⚠ ở nhiều hệ, vị trí này **khoá** việc đổi chế độ từ xa |
| **STOP** | Dừng quét chương trình |
| **REM** *(remote)* | Cho phép đổi chế độ bằng phần mềm, từ xa |

> ⚠⚠ **NGUY HIỂM — chuyển sang STOP không phải là "dừng máy"**
>
> Chuyển CPU sang STOP làm **mọi ngõ ra về trạng thái đã cấu hình cùng một lúc**, giữa chu trình,
> **không theo trình tự dừng nào**. Cơ cấu đang giữ có thể nhả; cơ cấu đang chuyển động dừng giữa
> hành trình; hai cơ cấu lẽ ra phải dừng theo thứ tự thì dừng đồng thời.
>
> Đây **không** phải cách dừng máy. Cách dừng máy là nút Stop, đi qua trình tự dừng của chương trình.
> Và cách dừng khẩn cấp là **mạch an toàn phần cứng** — không phải công tắc trên CPU (Chương 47).
>
> Trạng thái ngõ ra khi CPU sang STOP là **thứ phải cấu hình có chủ ý** cho từng kênh, dựa trên phân
> tích ở Chương 48, mục 48.2. Giá trị mặc định của hãng chưa chắc đúng cho máy của bạn — với DP-01,
> kẹp phải **giữ**, không được nhả.

Hai hệ quả về vận hành:

- **Máy đang sản xuất thì công tắc để ở đâu?** Nhiều đơn vị quy định để ở RUN và **niêm phong tủ**,
  để không ai chuyển chế độ từ xa khi máy đang chạy. Đây là quyết định của cơ sở, cần ghi vào tài
  liệu bàn giao (Chương 52).
- **Ai được vào tủ?** Công tắc này nằm trong tủ điện, và việc mở tủ khi máy có điện là thao tác có
  rủi ro riêng (Chương 3).

---

## 8.9 Trên máy mẫu DP-01

Cấu hình tối thiểu cho lát cắt 1, để bạn hình dung được quy mô thật:

| Hạng mục | Ước tính | Ghi chú |
|---|---|---|
| Ngõ vào số | ~24 kênh | Nút bấm, cảm biến board, reed xy-lanh, tín hiệu an toàn, tín hiệu bắt tay |
| Ngõ ra số | ~12 kênh | Van khí, cho phép biến tần, đèn tháp, còi |
| Dự phòng 20 % | thêm ~8 kênh | Theo quy tắc ở mục 8.3 |
| **Kết luận** | **32 DI · 16 DO** | Một CPU nguyên khối cỡ vừa cộng một module mở rộng là đủ |

Ở lát cắt sau, máy cần thêm module analog (Chương 32), module đếm tốc độ cao và điều khiển trục
(Chương 37), và cổng mạng để nối lên hệ thống trên (Chương 42). **Ba thứ đó phải được tính từ bây
giờ**, lúc chọn CPU — vì chạm trần mở rộng nghĩa là đổi CPU, và đổi CPU giữa dự án là chuyện tốn kém
và chậm.

Đó chính là lý do chương này nằm trước tất cả các chương lập trình: **quyết định phần cứng đến trước,
và sửa nó đắt hơn sửa code rất nhiều.**

---

## 8.10 Khác biệt giữa các hãng

Nêu tên cụ thể để bạn biết đường tra và so sánh. **Số liệu chi tiết phải lấy từ catalogue hiện hành**
— sách chỉ nêu đặc điểm cấu trúc, thứ ít đổi theo đời sản phẩm.

| Hệ | Dòng phổ biến ở máy tự động hoá | Phần mềm lập trình | Đặc điểm cấu trúc đáng chú ý |
|---|---|---|---|
| **Siemens** | S7-1200 (nguyên khối), S7-1500 (module hoá), S7-200 SMART (phổ thông) | TIA Portal | Hệ sinh thái rộng, tài liệu nhiều; PROFINET là mạng chủ đạo |
| **Mitsubishi** | FX5U / iQ-F (nguyên khối), iQ-R (module hoá) | GX Works3 | Rất phổ biến ở máy châu Á; CC-Link IE cho I/O phân tán |
| **Inovance** | H5U, Easy series (nguyên khối), AM600 (module hoá) | AutoShop, InoProShop | Giá cạnh tranh, phổ biến và dễ mua ở Việt Nam; tích hợp tốt với biến tần và servo cùng hãng (Chương 36, 37) |
| **Rockwell** | Micro800 (nhỏ), CompactLogix, ControlLogix | Connected Components Workbench, Studio 5000 | Chiếm ưu thế ở Bắc Mỹ; EtherNet/IP; mô hình tag đặt tên rất mạnh |
| **CODESYS** | Chạy trên phần cứng của nhiều hãng | CODESYS Development System | Trung lập hãng, bám chuẩn IEC 61131-3 sát nhất — sách dùng làm mốc đối chiếu |
| **Omron** | NX / NJ | Sysmac Studio | Mạnh về chuyển động và tích hợp thị giác máy |
| **Beckhoff** | CX series, PLC mềm | TwinCAT | PLC mềm trên PC; EtherCAT tốc độ cao |

Bốn điểm khác nhau đủ nhiều để **phải tra riêng cho từng hệ**:

- **Quy tắc đánh địa chỉ module** — theo vị trí hay gán tường minh (mục 8.4).
- **Vai trò của thẻ nhớ** — bản sao hay nơi chứa chính (mục 8.6).
- **Ý nghĩa đèn trạng thái**, nhất là kiểu nháy (mục 8.3).
- **Cách cấu hình trạng thái ngõ ra khi CPU sang STOP** (mục 8.8).

Hướng dẫn thao tác cho từng hệ nằm ở Phụ lục A.

> ⚡ **Về việc chọn hãng nào**
> Không có câu trả lời chung. Tiêu chí thật gồm cả những thứ không nằm trong datasheet: **có mua được
> ở địa phương không**, **có người biết dùng không**, **khách hàng đã chuẩn hoá theo hãng nào**, và
> **chi phí bản quyền phần mềm**. Chương 13 bàn đầy đủ, với bảng đối chiếu.

---

## 8.11 Bẫy thường gặp

### 🔍 BẪY 1 — Thêm module vào giữa rack

**Hiện tượng:** sau khi thêm module, một số cơ cấu hoạt động **sai chỗ** — lệnh nâng kẹp mở van khác.
Không có báo lỗi nào.
**Cách sửa:** chừa khe trống ở cuối rack; dùng tag có tên; và **kiểm I/O 1-1 lại** sau mọi thay đổi
phần cứng.

### 🔍 BẪY 2 — Nguồn 24 V tính thiếu

**Hiện tượng:** lỗi chập chờn, không tái hiện được, xuất hiện đúng lúc nhiều cơ cấu cùng tác động.
Rất hay bị chẩn đoán nhầm thành lỗi chương trình.
**Cách sửa:** tính lại phụ tải theo trường hợp xấu nhất, nhân 1,3–1,5; đo bằng máy hiện sóng để xác
nhận (mục 8.7).

### 🔍 BẪY 3 — Dùng công tắc STOP trên CPU để dừng máy

**Hiện tượng:** cơ cấu dừng ở tư thế bất kỳ; có thể nhả kẹp đang giữ sản phẩm.
**Cách sửa:** dừng máy bằng nút Stop qua trình tự; dừng khẩn bằng mạch an toàn. Công tắc CPU là công
cụ bảo trì, không phải công cụ vận hành.

### 🔍 BẪY 4 — Tin rằng hết pin là mất chương trình (hoặc ngược lại)

**Hiện tượng:** hoặc hoảng loạn không cần thiết, hoặc mất số liệu sản xuất mà không hiểu vì sao.
**Cách sửa:** tra tài liệu đúng hệ (mục 8.6); và luôn có bản sao lưu **đã thử khôi phục**.

### 🔍 BẪY 5 — Chọn CPU vừa khít nhu cầu hiện tại

**Hiện tượng:** sáu tháng sau, khách hàng yêu cầu thêm một cảm biến kiểm tra, và không còn khe cắm
hoặc không còn bộ nhớ.
**Cách sửa:** dự phòng 20 % số I/O và bộ nhớ ngay từ đầu; và tính cả nhu cầu của các giai đoạn sau
(mục 8.9).

### 🔍 BẪY 6 — Đưa việc cần đáp ứng nhanh ra I/O phân tán

**Hiện tượng:** đếm sót xung, hoặc bắt vị trí lệch, và **mức lệch thay đổi** theo tải mạng.
**Cách sửa:** việc cần đáp ứng nhanh và ổn định thì để tại chỗ, hoặc dùng module chuyên dụng đặt tại
chỗ (Chương 18, mục 18.5).

### 🔍 BẪY 7 — Không xử lý mất kết nối I/O phân tán

**Hiện tượng:** mất cụm I/O nhưng chương trình chạy tiếp, coi mọi ngõ vào của cụm đó bằng 0 — nghĩa
là "không có board", "cửa mở", tuỳ tín hiệu. Hành vi sau đó không đoán được.
**Cách sửa:** đọc bit trạng thái của cụm I/O và xử lý tường minh (Chương 48, mục 48.5).

### 🔍 BẪY 8 — Nghĩ I/O phân tán thông thường truyền được tín hiệu an toàn

**Hiện tượng:** thiết kế tưởng đạt yêu cầu an toàn nhưng không đạt — và điều đó chỉ lộ ra khi có
kiểm định, hoặc khi có tai nạn.
**Cách sửa:** tín hiệu an toàn cần giao thức an toàn và thiết bị được chứng nhận. Chương 47, và phải
do người có thẩm quyền thiết kế.

---

## 8.12 Bảng chốt

| Quyết định | Nguyên tắc | Sửa sau thì tốn gì |
|---|---|---|
| Chọn CPU | Dự phòng **20 %** I/O và bộ nhớ; tính cả giai đoạn sau | Đổi CPU giữa dự án |
| ⚠⚠ **Hướng lắp module** | ⭐ Nằm ngang theo thiết kế; **lắp đứng giảm ~10 °C** định mức | ⚠ Lỗi chập chờn mùa nóng, rất khó truy |
| ⭐ **Làm mát tủ** | Quạt có lọc hoặc điều hoà tủ — ⚠ **không mở cửa tủ** | Bụi dẫn điện vào tủ, mất cấp bảo vệ |
| Dáng hình | Nguyên khối cho máy nhỏ · module hoá khi cần linh hoạt | Đổi toàn bộ tủ |
| Vị trí khe trống | Chừa ở **cuối** rack | Dịch địa chỉ, phải kiểm I/O lại |
| Địa chỉ trong chương trình | **Tag có tên**, không dùng địa chỉ tuyệt đối | Sửa khắp chương trình |
| I/O phân tán | Dùng khi máy dài; ⚠ **không** cho việc cần đáp ứng nhanh, ⚠ **không** cho tín hiệu an toàn | Đi lại dây, hoặc thiết kế lại |
| Nguồn 24 V | Tính theo **trường hợp xấu nhất** × 1,3–1,5; tách nhánh theo nhóm | Lỗi chập chờn rất tốn thời gian tìm |
| Ngõ ra khi CPU sang STOP | Cấu hình **có chủ ý** từng kênh theo Chương 48 | Có thể gây hỏng sản phẩm hoặc thương tích |
| Sao lưu | Có bản ngoài máy, **đã thử khôi phục** | Mất chương trình = dựng lại từ đầu |
| ⚠⚠ Khoảng cách lắp trong tài liệu hãng | ⭐ Tính cho **tình huống điển hình** | ~60 % DI · ⭐ **~30 % DO** · **40 °C** |
| ⭐ Máy không điển hình | **Nới khoảng cách** + quạt tuần hoàn | ⚠⚠ Gió **phải qua phin lọc** |
| Pin | Thay theo lịch, khi CPU còn điện | Mất số liệu sản xuất |

---

## 8.13 Tự kiểm

1. Kể năm khối của một hệ PLC và nói ngắn gọn việc của từng khối.
2. Phân biệt PLC nguyên khối với PLC module hoá. Mỗi loại hợp với máy như thế nào?
3. ⭐ Vì sao thêm một module vào giữa rack có thể làm máy hoạt động sai mà **không có báo lỗi nào**?
   Nêu hai biện pháp phòng.
4. Nêu ba lợi ích của I/O phân tán khi máy dài, và ba cái giá phải trả.
5. ⭐ Vì sao **không** nên đưa việc đếm xung tốc độ cao ra I/O phân tán?
6. Hết pin trên CPU thì mất gì? Câu trả lời phụ thuộc điều gì?
7. Máy có 40 cảm biến (30 mA mỗi cái) và 12 cuộn van (250 mA mỗi cuộn). Ước tính công suất nguồn
   24 V cần thiết, nêu rõ hệ số dự phòng bạn dùng và lý do.
8. ⭐ Mô tả triệu chứng của nguồn 24 V thiếu công suất, và giải thích vì sao nó hay bị chẩn đoán nhầm
   thành lỗi phần mềm. Đo bằng dụng cụ gì để xác nhận, và vì sao không dùng đồng hồ vạn năng?
9. Vì sao chuyển CPU sang STOP **không phải** là cách dừng máy? Nêu hai hậu quả cụ thể trên DP-01.
10. ⭐ Vì sao chương này nằm **trước** mọi chương lập trình trong sách?
11. ⚠⚠ Khoảng cách lắp module trong tài liệu hãng dựa trên **bốn điều kiện điển hình** nào? ⭐ Điều
    kiện nào dễ bị máy thật vi phạm nhất, và vì sao?
12. ⭐ Tủ điện ở **45 °C** — so với điều kiện điển hình thì đó là **khắc nghiệt hơn** hay **vẫn thoải
    mái**? Giải thích.

> Câu 3, 8 và 10 là ba câu phân loại. Câu 10 là tinh thần của cả chương: **quyết định phần cứng đến
> trước, và sửa nó đắt hơn sửa code rất nhiều.**

⚠⚠ **Bổ sung.** Một máy chạy tốt suốt mùa mát, rồi lỗi chập chờn vào buổi chiều mùa nóng và tự khỏi
sáng hôm sau. Nêu hai nguyên nhân liên quan tới **cách lắp module**, và vì sao mở cửa tủ cho mát là
cách xử lý **sai**.

---

### Chương tiếp theo

Chương 9 — **Module vào/ra số**. Chương này đã nói module nằm ở đâu; chương sau nói **chọn loại nào**:
ngõ vào sink hay source, ngõ ra rơ-le hay transistor hay triac, và bài toán chọn cụ thể cho từng tải
của DP-01.

### Nguồn tham khảo chương 8

- IEC 61131-1 — *Programmable controllers, Part 1: General information*: định nghĩa các khối chức
  năng của một hệ PLC. *(tiêu chuẩn có bản quyền)*
- IEC 61131-2 — *Programmable controllers, Part 2: Equipment requirements and tests*: yêu cầu về
  nguồn cấp, điều kiện môi trường, và phép thử thiết bị.
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu với mạch điều
  khiển và với hành vi khi mất rồi khôi phục nguồn — nền cho mục 8.8.
- **Catalogue và datasheet hiện hành của các hãng nêu ở mục 8.10** — dùng cho mọi số liệu cụ thể:
  số kênh, dung lượng bộ nhớ, dòng tiêu thụ module, số module tối đa, quy tắc đánh địa chỉ, vai trò
  thẻ nhớ, ý nghĩa đèn trạng thái.
- Bảng I/O của DP-01 — Phụ lục J.
- **Bryan, L.A. & Bryan, E.A.** — *Programmable Controllers: Theory and Implementation*, ch. 20 §20-3
  *Noise, Heat, and Voltage Requirements*: PLC làm mát bằng **đối lưu**, và ⭐ **khuyến nghị khoảng
  cách lắp của hãng dựa trên tình huống điển hình** — ~60 % ngõ vào và ~30 % ngõ ra BẬT, không khí
  ~40 °C; ⚠ ngoài điều kiện đó **phải nới khoảng cách**. Gió quạt phải **qua phin lọc** vì bụi làm
  giảm chính khả năng thoát nhiệt (mục 8.7b).

> ⚡ **Về các con số trong chương này.** Hệ số dự phòng 20 % (I/O) và 1,3–1,5 (nguồn) là **quy tắc
> thực dụng của nghề**, không phải giá trị chuẩn hoá. Chúng là điểm khởi đầu hợp lý, không phải kết
> luận cuối — với tải có dòng khởi động lớn hoặc máy dự kiến mở rộng nhiều, hệ số phải cao hơn.
>
> ⚠ **Về tên sản phẩm ở mục 8.10.** Sách nêu tên để bạn **biết đường tra cứu và so sánh**, không phải
> để khuyến nghị hãng nào. Dòng sản phẩm thay đổi theo thời gian: có dòng ngừng sản xuất, có dòng mới
> ra. **Kiểm tra tình trạng sản phẩm và thông số trên trang chính thức của hãng trước khi quyết định
> mua**, và ghi lại ngày kiểm tra (Phụ lục G).
