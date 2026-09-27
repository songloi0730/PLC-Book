
# Chương 57 — Case study đầy đủ: DP-01 từ trang giấy tới máy chạy

> **Lát cắt máy mẫu:** 5 — toàn bộ cỗ máy, và toàn bộ sách.

---

## 57.1 Chương này dùng thế nào

Suốt 56 chương, DP-01 xuất hiện từng mảnh: một cảm biến ở Chương 4, một trình tự ở Chương 21, một
vòng điều khiển ở Chương 35. Mỗi mảnh được dạy đúng lúc bạn đủ nền để hiểu nó.

Chương này **ráp tất cả lại theo thứ tự của một dự án thật** — từ lúc nhận yêu cầu tới lúc bàn giao.

| Cách dùng | |
|---|---|
| ⭐ **Đọc một mạch** | Thấy được hình dạng của cả một dự án — thứ mà đọc từng chương không thấy |
| ⭐ **Dùng làm danh mục kiểm** | Áp vào dự án của bạn: bước nào bạn đang bỏ qua? |
| Dùng làm bản đồ ngược | Mỗi bước dẫn về đúng chương đã dạy nó |

> ⚠ **Chương này KHÔNG dạy kiến thức mới.** Nếu một bước dưới đây bạn thấy lạ, hãy quay lại chương
> được dẫn. Ở đây chỉ có **thứ tự** và **mối nối** giữa các phần.

---

## 57.2 Nhắc lại: DP-01 là máy gì

| Hạng mục | Nội dung |
|---|---|
| Chức năng | Tra keo lên board mạch, rồi sấy UV cho keo cứng |
| Bố trí | ⭐ **Hai trạm nối tiếp** trên một băng tải, không có chỗ đệm giữa hai trạm |
| Trạm 1 | Gantry 3 trục chạy đường keo (X 0–150 · Y 0–120 · Z 0–50 mm), ⭐ **cả ba trục đều servo** |
| Trạm 2 | Buồng sấy UV, ⭐ **6–12 s tuỳ công thức** |
| Board | 100 × 80 mm |
| Năng suất | ⭐ **300 board/giờ → chu kỳ 12,0 s** |
| Nhận diện | Đầu đọc mã 2D trên board, kết nối Ethernet |
| Gia nhiệt keo | Bộ điều khiển nhiệt độ độc lập, kết nối RS-485 |
| Kết nối lên trên | Báo cáo kết quả từng board lên hệ thống trên |
| Giao tiếp máy trước/sau | Bắt tay theo chuẩn chuyền lắp ráp điện tử |

Số liệu đầy đủ: **Phụ lục J**.

---

## 57.3 Giai đoạn 1 — Đặc tả *(functional specification)*

⭐ **Đây là giai đoạn quyết định phần lớn kết quả, và là giai đoạn hay bị rút ngắn nhất.**

| Việc | Chương |
|---|---|
| Viết đặc tả chức năng: máy làm gì, ở chế độ nào, xử lý lỗi ra sao | 23 |
| ⭐ **Danh sách chế độ vận hành** — tự động · tay · về gốc · bảo trì | 23, 25 |
| ⭐⭐ **Đánh giá rủi ro** | ⚠ **6** — làm ở đây, không phải ở cuối |
| Xác định chỉ tiêu năng suất và cách đo | 55 |
| Danh sách sản phẩm và điểm khác nhau giữa chúng → cơ sở cho công thức | 32 |
| ⭐ Câu hỏi "máy làm gì khi X hỏng" cho mọi X | 43, 51 |

> ⭐⭐ **Đánh giá rủi ro nằm ở giai đoạn 1, không phải giai đoạn cuối.** Nó quyết định: cần rèm quang
> hay cửa khoá, cần mấy kênh, cần mức hiệu năng nào — và những thứ đó ⭐ **quyết định giá và quyết
> định bố trí máy**.
>
> Làm nó sau khi đã thiết kế xong nghĩa là hoặc bạn sẽ sửa thiết kế, hoặc bạn sẽ hạ chuẩn an toàn cho
> vừa thiết kế. ⚠ Cả hai đều tệ.

### ⭐ Đầu ra của giai đoạn 1

| Tài liệu | Ai duyệt |
|---|---|
| Đặc tả chức năng | Khách hàng |
| ⚠ Hồ sơ đánh giá rủi ro | ⭐ **Người có thẩm quyền về an toàn** |
| Chỉ tiêu năng suất, kèm ⭐ **định nghĩa cách đo** | Khách hàng — Ch.55 mục 55.7 |
| Danh sách sản phẩm và tham số | Khách hàng |
| ⭐ Thoả thuận bàn giao mã nguồn | ⭐ **Ký ở đây** — Ch.54 mục 54.6 |

---

## 57.4 Giai đoạn 2 — Bảng I/O và chọn phần cứng

| Việc | Chương |
|---|---|
| ⭐⭐ **Lập bảng I/O** — tên tag, kiểu, thiết bị, ghi chú | 23 |
| Chọn cảm biến cho từng vị trí | 4 |
| ⭐ Chọn kiểu tín hiệu: PNP/NPN, NO/NC — ⚠ **NC cho tín hiệu an toàn quan trọng** | 4, 47 |
| Chọn cơ cấu chấp hành và cách điều khiển | 5, 9 |
| ⭐ Tính công suất nguồn 24 V | 8 mục 8.7 |
| ⭐ **Tính tuổi thọ**: đóng cắt van, uốn cáp xích | 9 mục 9.3, 49 mục 49.7 |
| Chọn CPU: số I/O, ⭐ **chừa 20 % dự phòng**, thời gian quét | 7, 8 |
| Chọn module analog và dải tín hiệu | 31 |
| Chọn thiết bị mạng và kiến trúc | 40 |
| ⚠ Chọn thiết bị an toàn theo mức đã xác định ở giai đoạn 1 | 47, 48 |

### ⭐ Đầu ra của giai đoạn 2

⚠ Bảng trên liệt kê **việc phải làm**. ⭐ Còn đây là **thứ phải cầm được trên tay** khi giai đoạn này
kết thúc — vì một giai đoạn không đẻ ra tài liệu thì không có cách nào biết nó đã xong.

| Tài liệu | Biểu mẫu | ⭐ Coi là xong khi | Ai duyệt |
|---|---|---|---|
| ⭐⭐ **Bảng I/O** | **C.1** | Mọi tag có một nghĩa · ⭐ còn **≥ 20 %** kênh dự phòng · tín hiệu an toàn tách riêng | Nội bộ, khách xem |
| Bảng công tác chọn PLC | **§13.4** | Đủ **11 mục**, ⚠ kể cả ba mục hay để trống: bản quyền · thời gian có hàng thay thế · dòng còn sản xuất bao lâu | Nội bộ |
| ⭐ **Bảng cấu hình phần cứng** | **C.10** | ⭐ Phép thử một phút đạt; khe dự phòng ở **cuối** rack; firmware đã ghi | Nội bộ |
| ⭐ **Danh mục vật tư** | **C.11** | Mọi dòng có cột *"Sinh từ"*; ⚠ **thời gian có hàng** điền bằng tuần cho mọi dòng | Mua hàng |
| Các phép tính | — | Công suất nguồn 24 V · tuổi thọ van và cáp — ⭐ **có ghi giả định**, đã nhân hệ số dự phòng | Nội bộ |

> ⭐⭐ **Hai tài liệu giữa bảng là hai tài liệu mà Phiếu bàn giao đòi.** Bộ sao lưu bảy hạng mục ở
> C.9 có *"cấu hình phần cứng"* là mục 2, và phiếu bàn giao có *"danh mục vật tư + phụ tùng khuyến
> nghị"* là mục 9. ⚡ Lập chúng **ở đây** thì cuối dự án chỉ việc cập nhật; ⚠ để tới lúc bàn giao
> mới lập thì chúng sẽ được **dựng lại từ trí nhớ**, và sẽ sai.

> ⚠⚠ **Giai đoạn này là điểm không quay lại của phần cứng.** ⭐ Sau khi đặt hàng, mọi thay đổi về số
> kênh, kiểu ngõ ra hay kiểu đấu **đều tốn tiền và tốn thời gian chờ hàng**. ⚡ Đó là lý do bảng I/O
> phải xong **trước**, không phải song song — chín bước và quan hệ chặn ở **Chương 23 mục 23.2b**.

### ⭐ Bảng I/O rút gọn của DP-01

| Nhóm | Tag tiêu biểu | Chương |
|---|---|---|
| **DI — trạm 1** | `DI_BoardStn1` · `DI_Clamp1Up` · `DI_Stop1Up` / `DI_Stop1Dn` | 4, 23 |
| **DI — trạm 2** | `DI_BoardStn2` · `DI_ShutterClosed` | 4 |
| **DI — an toàn** | ⚠ `DI_EStopOK` · `DI_CurtainOK` · `DI_Door1Closed` / `DI_Door2Closed` | 47 |
| **DI — chuyền** | `DI_SmemaInAvail` · `DI_SmemaOutRdy` | 41 |
| **DO — trạm 1** | `DO_Clamp1Vlv` · `DO_DispVlv` · `DO_SuckBack` | 5, 9 |
| **DO — trạm 2** | `DO_UvLamp` · `DO_Clamp2Vlv` | 9 |
| **DO — báo hiệu** | `DO_LampRed/Yellow/Green` · `DO_Buzzer` | 43, 44 |
| **AI** | `AI_AirPress` · `AI_GluePress` · ⭐ `AI_UvIntensity` | 31, 53 |
| **AO** | `AO_GluePressSet` | 31 |
| **Trục** | `AX_X` · `AX_Y` · `AX_Z` — ⭐ **cả ba đều servo** | 37 |
| **Mạng** | `NET_Scanner` (Ethernet) · `NET_TempCtrl` (RS-485) · `NET_MES` · `NET_Drives` | 38, 40, 42 |

> ⚠ **Bảng trên là bản rút gọn.** Bảng I/O đầy đủ của DP-01 — kèm loại thiết bị, trạng thái nghỉ,
> dải kỹ thuật và lát cắt — nằm ở **Phụ lục J**. Tên tag trong sách luôn theo bảng đó.

> ⭐⭐ **Bảng I/O là tài liệu nền của cả dự án.** Nó là đầu vào cho: sơ đồ điện, đánh số dây (Ch.49),
> chương trình, HMI, và tài liệu bàn giao. ⚠ **Làm nó trước khi đấu tủ** — nếu không, số dây và tên
> tag sẽ không khớp nhau suốt vòng đời máy.

---

## 57.5 Giai đoạn 3 — Thiết kế điện và đấu tủ

| Việc | Chương |
|---|---|
| Sơ đồ điện, chia nhánh cầu chì 24 V | 8, 49 mục 49.5 |
| ⚠ Mạch an toàn: rơ-le an toàn, hai kênh, giám sát tiếp điểm | 47 |
| ⭐ Tách máng: động lực · tín hiệu · an toàn | 49 mục 49.3 |
| ⭐⭐ **Nối đất: 0 V nối PE ở đúng một điểm** | 49 mục 49.4 |
| ⭐ Vỏ chống nhiễu: analog **một đầu**, cáp động cơ **hai đầu**, kẹp 360° | 31, 36, 49 |
| Cáp chịu uốn trong xích gantry | 49 mục 49.7 |
| Đánh số dây hai đầu, khớp bảng I/O | 49 mục 49.6 |
| Chống quá áp lan truyền | 49 mục 49.5 |

> ⚠ Phần này do **người có thẩm quyền** về điện thực hiện. Việc của người lập trình là **nghiệm thu**
> nó theo danh mục ở Chương 49 mục 49.10 — và ⭐ **ghi lại các mốc đo**.

---

## 57.6 Giai đoạn 4 — Kiến trúc chương trình

⭐ **Quyết định kiến trúc trước khi viết dòng lệnh đầu tiên.**

### Cấu trúc tổng thể *(program architecture)*

```text
Chương trình chính
 ├── Xử lý an toàn & chế độ vận hành         ← Ch.25, 28, 47
 ├── Điều khiển băng tải & bắt tay chuyền    ← Ch.36, 41
 ├── Trạm 1 — tra keo      (máy trạng thái)  ← Ch.21, 26, 27
 ├── Trạm 2 — sấy UV       (máy trạng thái)  ← Ch.21, 27
 ├── Điều phối giữa hai trạm                 ← Ch.26
 ├── Công thức & tham số sản phẩm            ← Ch.29
 ├── Analog; giám sát nhiệt qua RS-485       ← Ch.31, 35
 ├── Chuyển động gantry                      ← Ch.37
 ├── Truyền thông: mã 2D, nhiệt, lên trên    ← Ch.38, 42, 45
 ├── Báo động & chẩn đoán                    ← Ch.44, 51
 └── Thống kê: chu kỳ, bộ đếm bảo trì        ← Ch.53, 55
```

### ⭐ Bốn quyết định kiến trúc, và lý do

| Quyết định | Vì sao |
|---|---|
| ⭐⭐ **Mỗi trạm là một máy trạng thái độc lập** | Chạy song song trên các board khác nhau; ⭐ **và tách được để kiểm thử riêng** (Ch.26, 27) |
| ⭐ **Điều phối giữa hai trạm là một khối riêng** | ⚠ Không có đệm → hai trạm phải bắt tay; để logic này lẫn vào trạm là nguồn của bế tắc (Ch.26) |
| ⭐ **Động tác lặp lại đóng thành khối hàm** | Kẹp/nhả, chờ có phản hồi kèm hết giờ — dùng lại ở cả hai trạm (Ch.30) |
| ⭐⭐ **Mọi tham số sản phẩm nằm trong công thức, không nằm trong logic** | ⭐ Đổi sản phẩm **không phải sửa chương trình** (Ch.29) |

> ⭐⭐ **Quyết định thứ tư là thứ phân biệt một máy dùng được lâu với một máy phải gọi kỹ sư mỗi lần
> đổi hàng.** Mọi con số đặc thù sản phẩm — đường chạy keo, áp keo, thời gian sấy, nhiệt độ — phải là
> **dữ liệu**, không phải mã lệnh.

### ⭐ Quy ước đặt tên

| Loại | Mẫu | Chương |
|---|---|---|
| Ngõ vào số | `DI_<chỗ><cái gì>` | 23 |
| Ngõ ra số | `DO_<chỗ><cái gì>` | 23 |
| Analog | `AI_/AO_<đại lượng>` | 31 |
| Giao diện công bố của trạm | `Stn1.<trường>` — kiểu `ST_Station` | 11, 27 |
| Ruột của trình tự trạm | `Stn1_<tên>` — bước, giới hạn thời gian bước | 26 |
| Yêu cầu trạm gửi tầng cơ cấu | `M_Stn1_<cơ cấu>Req` | 27 |
| Tham số công thức | ⭐ **Không** tiền tố riêng — là thành phần của cấu trúc: `ActiveRecipe.<tham số>`, kiểu `ST_Recipe` | 29 |

> ⭐ Quy ước phải **khớp với số dây trong tủ** (Ch.49 mục 49.6) và **khớp với nhãn trên HMI** (Ch.44).
> Ba nơi, một tên — đó là thứ giúp người sửa máy đi từ triệu chứng tới sợi dây trong ba bước.

---

### ⭐⭐ Khung chương trình chính — sơ đồ ở trên viết ra thành mã

Sơ đồ hộp ở đầu mục này nói *có những phần nào*. ⭐ Còn đây là **đúng sơ đồ đó viết thành mã**, với
tên thật của DP-01. Cả cuốn sách hội tụ về khoảng ba mươi dòng này:

```iecst
PROGRAM Main          // tác vụ chu kỳ, chạy liên tục — Ch.10, Ch.27 mục 27.6

  Prg_IoRead();        //  1  lọc rung, bắt cạnh, ánh xạ tag        Ch.4, 16, 17, 23
  Prg_Safety();        //  2  chế độ vận hành, M_AllPermissive      Ch.25, 28, 47
  Prg_Mechanisms();    //  3  Stop1/Clamp1/Stop2/Clamp2, gantry     Ch.27, 30, 37
  Prg_AntiCollision(); //  4  tầng chống va chạm                    Ch.27 mục 27.3b
  Prg_Alarm();         //  5  báo động + GOM LỖI (một chỗ gán)      Ch.25 mục 25.5c, 44 · L.11
  Prg_Machine();       //  6  tầng máy: tài nguyên chung, pipeline  Ch.26, 27 mục 27.5
  Prg_Stn1Dispense();  //  7  trình tự trạm 1                       Ch.21, 26 · khung L.6
  Prg_Stn2Cure();      //  8  trình tự trạm 2                       Ch.21, 26 · khung L.6
  Prg_Handshake();     //  9  bắt tay máy trước / máy sau           Ch.41
  Prg_Recipe();        // 10  nạp tham số của công thức đang chọn   Ch.29
  Prg_Comm();          // 11  mã 2D, nhiệt RS-485, báo cáo lên trên Ch.38, 42, 45
  Prg_Stats();         // 12  chu kỳ, sản lượng, bộ đếm bảo trì     Ch.53, 55
  Prg_OutputMap();     // 13  GOM ngõ ra — đúng một chỗ ghi mỗi tag Ch.22, 27 Bẫy 2
  Prg_Hmi();           // 14  dữ liệu cho màn hình và đèn tháp      Ch.5, 44
  M_FirstScan := FALSE; // 15 ⭐ dòng CUỐI — hết vòng quét đầu       Ch.16 Bẫy 9, Phụ lục M.4

END_PROGRAM
```

Và `Prg_OutputMap` — khối ngắn nhất, nhưng là khối giữ cho chương trình còn đọc được sau ba năm:

```iecst
// Mỗi ngõ ra xuất hiện ĐÚNG MỘT LẦN trong toàn chương trình, và là ở đây.
DO_Stop1Vlv  := Stop1.Valve;                      // Ch.27 — FB_Cylinder2Pos
DO_Clamp1Vlv := Clamp1.Valve;
DO_UvLamp    := M_Stn2_UvReq AND M_AllPermissive AND DI_ShutterClosed;
DO_LampRed   := M_AnyFault;                       // Ch.5, 25 — mẫu đèn tháp L.13
```

### ⭐ Ba điều trong khung này đáng nói hơn cả danh sách

| Điều | Nội dung |
|---|---|
| ⚠⚠ **Không có `IF` nào bao quanh các lệnh gọi** | ⭐ Mọi khối chạy **mỗi vòng quét**. Bọc một lệnh gọi trong `IF` là đóng băng mọi timer bên trong nó, và ⚠ **ngõ ra thì giữ nguyên giá trị cũ** — Ch.17 Bẫy 3, Ch.15 mục 15.4b |
| ⭐⭐ **Thứ tự KHÔNG tuỳ ý** | Cơ cấu → **gom lỗi** → máy → trạm → ghi ngõ ra (Ch.27 mục 27.6). ⭐ Gọi tầng cơ cấu **trước** để `Done` và `Fault` mà trình tự đọc là **của vòng quét này**, không phải vòng trước. ⭐ Gom lỗi đứng ngay trước tầng máy để máy vào `Alarm` trong **cùng** vòng quét lỗi được chốt (Ch.25 mục 25.5c) |
| ⭐ **Ghi ngõ ra gom vào một khối cuối** | ⚠ Đây là cách rẻ nhất để bảo đảm *"đúng một chỗ ghi cho mỗi tag"* — dấu hiệu số một của chương trình lành mạnh khi người khác đọc lại (Ch.22 mục 22.2) |

> ⚠⚠ **Thứ tự GỌI khác thứ tự VIẾT.** Bảng ở mục 57.7 ngay dưới đây là thứ tự **viết** — an toàn viết
> trước vì mọi thứ phụ thuộc nó. ⭐ Còn thứ tự **gọi** là danh sách trên, do luồng dữ liệu trong một
> vòng quét quyết định. ⚡ Hai thứ tự này khác nhau, và **lẫn lộn chúng là một lỗi kiến trúc thật**.

> ⭐⭐ **Vì sao DP-01 chỉ có MỘT tác vụ.** Danh mục kiểm ở Chương 27 mục 27.8 hỏi: *"có bao nhiêu tác
> vụ, và mỗi tác vụ thêm có lý do định lượng không?"* ⭐ Câu trả lời của DP-01 là **một** — vì mọi
> vòng điều khiển liên tục của nó đều đã **giao cho thiết bị chuyên dụng**: biến tần lo tốc độ, servo
> drive lo vị trí, bộ điều khiển rời lo nhiệt độ keo (mục 35.9, 35.11).
>
> ⚡ Đó không phải may mắn — ⭐ đó là **hệ quả trực tiếp của các quyết định ở giai đoạn 2**, và nó đổi
> lại một chương trình PLC đơn giản hơn hẳn.

> ⭐ **Thân của từng khối thì không lặp lại ở đây.** Trình tự trạm dùng nguyên **khung L.6**; xy-lanh
> dùng **`FB_Cylinder2Pos`** ở Chương 27 mục 27.3; đèn tháp dùng **L.13**; tự giữ dùng **L.1**. ⚡ Đó
> chính là điều đáng nói: ⭐ **đến chương này thì không còn gì phải phát minh nữa** — chỉ còn việc
> ghép các mẫu đã có theo đúng thứ tự.

---

## 57.7 Giai đoạn 5 — Viết chương trình theo thứ tự

⭐ **Thứ tự viết không phải thứ tự chương trình chạy.** Viết theo thứ tự phụ thuộc, và luôn giữ được
một bản chạy được.

| Thứ tự | Viết gì | Vì sao trước | Chương |
|---|---|---|---|
| 1 | ⚠ **Xử lý an toàn & chế độ vận hành** | ⭐ **Mọi thứ khác phụ thuộc nó**; và không được "thêm vào sau" | 25, 47 |
| 2 | Đọc I/O, lọc rung, ánh xạ tag | Nền cho mọi logic | 4, 23 |
| 3 | ⭐ **Chuyển động tay và về gốc** | ⭐ Cần nó để **kiểm tra phần cứng** trước khi có trình tự | 37, 25 |
| 4 | Khối hàm dùng chung (kẹp, chờ có hết giờ) | Trình tự sẽ gọi chúng | 30 |
| 5 | Trình tự trạm 1 | Đơn giản hơn trạm 2 | 21, 26 |
| 6 | Trình tự trạm 2 | | 21 |
| 7 | ⭐ **Điều phối hai trạm** | ⭐ Chỉ làm được khi đã có cả hai trạm | 26 |
| 8 | Công thức và tham số | Trình tự đã biết cần tham số nào | 32 |
| 9 | Analog; giám sát bộ điều khiển nhiệt rời | Độc lập với trình tự | 31, 35 |
| 10 | Truyền thông: mã 2D, nhiệt, chuyền | Cắm vào trình tự đã có | 38, 41, 42 |
| 11 | ⭐ **Báo động và chẩn đoán** | ⭐ Viết khi đã biết **cái gì có thể sai** | 43, 51 |
| 12 | HMI | Cần biết có gì để hiện | 44 |
| 13 | Thống kê, bộ đếm bảo trì, đo chu kỳ | ⭐ Rẻ, và ⚠ **thêm sau thì thường không bao giờ thêm** | 53, 55 |
| 14 | Kết nối lên trên | Cuối cùng, ⚠ có ranh giới an ninh riêng | 45 |

> ⭐⭐ **Ba điểm đáng chú ý trong bảng này:**
>
> | Điểm | Nội dung |
> |---|---|
> | ⚠ **An toàn viết trước, không phải sau** | Nó là điều kiện của mọi thứ khác; ⚠ ghép vào sau là cách tạo ra lỗ hổng |
> | ⭐ Chuyển động tay trước trình tự tự động | Bạn cần một cách **cử động máy** để kiểm tra phần cứng — trước khi có trình tự |
> | ⭐ Báo động viết **sau** trình tự | Vì lúc đó bạn mới biết **cái gì có thể sai** — viết trước thì chỉ đoán |

---

## 57.8 Giai đoạn 6 — Kiểm thử *(testing)*

| Mức | Nội dung | Chương |
|---|---|---|
| 1 | ⭐ **Mô phỏng trên bàn** — không phần cứng | 50 |
| 2 | ⭐ Kiểm từng I/O trên máy thật — ⚠ **tác động thật, xem bit thật** | 50, 52 |
| 3 | Chạy khô từng cơ cấu ở chế độ tay | 52 |
| 4 | Chạy khô cả trình tự, không có board | 52 |
| 5 | Chạy có board, ⭐ **tốc độ chậm** | 52 |
| 6 | Chạy tốc độ làm việc | 52 |
| 7 | ⭐⭐ **Kiểm thử tình huống xấu** — xem bên dưới | 50, 43 |
| 8 | ⚠⚠ **Nghiệm thu chức năng an toàn** | 48, 52 |
| 9 | Chạy liên tục, ⭐ đo chu kỳ thật | 55 |

### ⭐⭐ Kiểm thử tình huống xấu — mức bị bỏ nhiều nhất

| Tình huống | Máy phải làm gì |
|---|---|
| ⚠ Mất khí nén giữa chu trình | Dừng an toàn, báo rõ, ⚠ **không thả kẹp bất ngờ** (Ch.6) |
| Board kẹt giữa hai trạm | Báo động chỉ đúng chỗ, hướng dẫn gỡ (Ch.44 mục 44.3) |
| Mất mạng với đầu đọc mã | ⭐ Báo, và quyết định trước: dừng hay chạy tiếp không mã? (Ch.40, 42) |
| Nhấn dừng khẩn giữa lúc gantry đang chạy | ⚠⚠ **Dừng theo đúng loại đã thiết kế** (Ch.47) |
| ⭐ Mất điện giữa chu trình, rồi cấp lại | ⚠⚠ **KHÔNG được tự khởi động lại** (Ch.47) |
| Cửa buồng UV mở giữa lúc sấy | ⚠ Đèn tắt tức thì, báo động (Ch.47) |
| Công thức sai / thiếu tham số | Từ chối chạy, báo rõ thiếu gì (Ch.29 mục 29.4) |
| ⭐ Hệ thống trên không phản hồi | ⚠ **Máy vẫn chạy được** — Ch.45 |

> ⭐⭐ **Hàng cuối là nguyên tắc quan trọng: máy không được phụ thuộc vào thứ nằm ngoài nó để chạy
> được.** Mất kết nối lên trên thì máy đệm dữ liệu lại và chạy tiếp, chứ không dừng sản xuất.

---

## 57.9 Giai đoạn 7 — Chạy thử và bàn giao

| Việc | Chương |
|---|---|
| Chạy thử tại xưởng, khách hàng chứng kiến | 52 |
| Lắp đặt tại nhà máy, ⭐ nghiệm thu phần đấu tủ | 49 mục 49.10, 52 |
| Chạy thử tại chỗ, ghép với máy trước/sau | 41, 52 |
| ⭐⭐ **Đo và ghi các mốc** — 24 V tải nặng, dòng động cơ, lỗi mạng, chu kỳ | 8, 36, 40, 55 |
| ⚠ Nghiệm thu an toàn, lập hồ sơ | 48 |
| ⭐ Đào tạo người vận hành | 44, 52 |
| ⭐ Sao lưu **bảy hạng mục**, thử khôi phục | 54 |
| Bàn giao tài liệu as-built | 53 mục 53.4 |

### ⭐ Bộ hồ sơ bàn giao

| Tài liệu | Chương |
|---|---|
| Đặc tả chức năng (bản cuối, khớp máy thật) | 23 |
| ⚠ Hồ sơ đánh giá rủi ro + nghiệm thu an toàn | 6, 48 |
| Sơ đồ điện **as-built** | 49, 53 |
| Bảng I/O khớp số dây | 23, 49 |
| ⭐ Chương trình PLC **có chú thích** | 24 |
| ⭐ Bộ sao lưu bảy hạng mục + **quy trình khôi phục** | 54 |
| Hướng dẫn vận hành và xử lý báo động | 43, 44 |
| Danh mục vật tư và phụ tùng khuyến nghị | 53 |
| ⭐ Mốc đo lúc nghiệm thu | 8, 36, 40, 55 |
| Sổ nhật ký thay đổi (để trống, treo trong tủ) | 53 |

> ⭐⭐ **Hai mục có dấu ⭐ ở cuối bảng là hai mục hay bị bỏ, và là hai mục cứu người sửa máy về sau.**
>
> Mốc đo trả lời câu "cái này có bình thường không". Sổ nhật ký để trống là **lời mời ghi chép** — nó
> làm việc ghi lại dễ hơn việc không ghi, và đó là cách duy nhất khiến nó thật sự được dùng.

---

## 57.10 Giai đoạn 8 — Sau bàn giao

| Việc | Chương |
|---|---|
| Quy trình thay đổi có kiểm soát | 53 mục 53.3 |
| Sao lưu định kỳ + ⭐ **thử khôi phục** | 54 |
| Theo dõi bộ đếm bảo trì và ⭐ **xu hướng thời gian bước** | 53 mục 53.5, 55 |
| Tính OEE, ⭐ **ghi rõ định nghĩa** | 55 mục 55.7 |
| Tìm nút cổ chai bằng ⭐ **phần trăm thời gian chờ** | 55 mục 55.4 |
| ⚠ Kiểm định lại chức năng an toàn theo chu kỳ | 48 |

---

## 57.11 ⭐ Nhìn lại: những quyết định định hình cỗ máy này

Trong toàn bộ dự án, **năm quyết định** ảnh hưởng lớn hơn tất cả phần còn lại:

| # | Quyết định | Hệ quả nếu quyết sai |
|---|---|---|
| 1 | ⭐⭐ **Đánh giá rủi ro ở giai đoạn 1** | ⚠ Sửa thiết kế muộn, hoặc hạ chuẩn an toàn cho vừa thiết kế |
| 2 | ⭐⭐ **Bảng I/O trước khi đấu tủ** | Số dây không khớp tên tag — trả giá suốt vòng đời máy |
| 3 | ⭐⭐ **Tham số sản phẩm là dữ liệu, không phải mã** | Gọi kỹ sư mỗi lần đổi hàng |
| 4 | ⭐ **Trạm 2 là nút cổ chai, và 12 s là vừa đủ** | ⚠ Hứa năng suất không đạt được |
| 5 | ⭐ **Đo chu kỳ và bộ đếm bảo trì cài từ đầu** | ⚠ Thêm sau thì thường không bao giờ thêm |

> ⭐⭐ **Điểm chung của cả năm: chúng đều là quyết định ở GIAI ĐOẠN SỚM, và đều rẻ ở thời điểm đó.**
>
> Quyết định 1 và 2 mất vài ngày ở đầu dự án; sửa chúng sau khi máy đã đấu xong mất vài tuần. Quyết
> định 3 và 5 mất vài giờ lập trình; thêm chúng sau khi máy đã bàn giao thường **không bao giờ xảy
> ra**.
>
> Đây là hình dạng chung của mọi thứ sách này đã dạy: ⭐ **chi phí của một quyết định tăng theo thời
> gian bạn trì hoãn nó.**

---

## 57.12 Bẫy thường gặp ở mức dự án

Khác với các chương trước, đây là những bẫy **không thuộc về một kỹ thuật nào** — chúng thuộc về cách
tổ chức công việc.

### 🔍 BẪY 1 — Bắt đầu viết chương trình khi đặc tả chưa xong

**Hiện tượng:** ⚠ viết lại nhiều lần; và những phần viết sớm nhất thường là phần **khó sửa nhất**.
**Cách sửa:** đặc tả và đánh giá rủi ro là **giai đoạn 1** (mục 57.3).

### 🔍 BẪY 2 — Đánh giá rủi ro làm ở cuối

**Hiện tượng:** ⚠⚠ hoặc sửa thiết kế, hoặc **hạ chuẩn an toàn cho vừa thiết kế**.
**Cách sửa:** đánh giá rủi ro quyết định bố trí máy — nó phải đi trước (mục 57.3, Ch.23, Ch.47 mục 47.2).

### 🔍 BẪY 3 — Đấu tủ trước khi có bảng I/O

**Hiện tượng:** số dây không khớp tên tag — ⚠ trả giá suốt vòng đời máy.
**Cách sửa:** bảng I/O là **đầu vào** của thiết kế điện (mục 57.4, Ch.49 mục 49.6).

### 🔍 BẪY 4 — Ghép phần an toàn vào sau

**Hiện tượng:** ⚠⚠ lỗ hổng ở chỗ giao giữa logic thường và logic an toàn.
**Cách sửa:** an toàn là **thứ viết đầu tiên** (mục 57.7).

### 🔍 BẪY 5 — Tham số sản phẩm nằm trong logic

**Hiện tượng:** đổi board mới phải **sửa chương trình** → phải gọi kỹ sư, phải kiểm thử lại.
**Cách sửa:** mọi con số đặc thù sản phẩm là **công thức** (mục 57.6, Ch.29).

### 🔍 BẪY 6 — Bỏ mức kiểm thử tình huống xấu

**Hiện tượng:** ⭐⭐ máy chạy tốt khi mọi thứ đúng, và **cư xử khó lường khi có sự cố** — tức là đúng
lúc quan trọng nhất.
**Cách sửa:** mức 7 ở mục 57.8 là **bắt buộc**, không phải tuỳ chọn.

### 🔍 BẪY 7 — Máy phụ thuộc hệ thống bên ngoài để chạy

**Hiện tượng:** ⚠ mất mạng với hệ thống trên → **dừng sản xuất**.
**Cách sửa:** đệm dữ liệu và chạy tiếp (mục 57.8, Ch.45).

### 🔍 BẪY 8 — Không ghi mốc lúc nghiệm thu

**Hiện tượng:** sáu tháng sau không ai trả lời được "con số này có bình thường không".
**Cách sửa:** đo và ghi khi máy còn mới (mục 57.9).

### 🔍 BẪY 9 — Bàn giao thiếu bộ sao lưu và quy trình khôi phục

**Hiện tượng:** ⚠⚠ Chương 54 mục 54.1 — cỗ máy không ai dựng lại được.
**Cách sửa:** bảy hạng mục + quy trình khôi phục, ⭐ **đã thử ít nhất một lần** (mục 57.9).

### 🔍 BẪY 10 — Hoãn phần thống kê "để sau"

**Hiện tượng:** ⭐ "sau" không bao giờ tới; máy chạy ba năm mà **không ai biết nút cổ chai ở đâu**.
**Cách sửa:** đo chu kỳ và bộ đếm bảo trì là ⭐ **vài giờ lập trình lúc đầu** (mục 57.7 bước 13).

---

## 57.13 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Tám giai đoạn của dự án | Đặc tả → bảng I/O → điện → kiến trúc → viết → kiểm thử → chạy thử & bàn giao → sau bàn giao |
| ⭐⭐ Đánh giá rủi ro làm khi nào | **Giai đoạn 1** — nó quyết định giá và bố trí máy |
| ⭐⭐ Bảng I/O làm khi nào | **Trước khi đấu tủ** — nó là đầu vào của thiết kế điện |
| Bốn quyết định kiến trúc | Mỗi trạm một máy trạng thái · điều phối tách riêng · khối hàm dùng chung · ⭐ **tham số là dữ liệu** |
| ⭐ Viết chương trình theo thứ tự nào | ⚠ **An toàn trước** → I/O → tay & về gốc → khối hàm → trình tự → điều phối → … → báo động → HMI → thống kê |
| Vì sao chuyển động tay viết sớm | ⭐ Cần một cách **cử động máy** để kiểm tra phần cứng |
| Vì sao báo động viết muộn | ⭐ Lúc đó mới **biết cái gì có thể sai** |
| ⭐⭐ Mức kiểm thử hay bị bỏ nhất | **Tình huống xấu** — mất khí, kẹt, mất mạng, dừng khẩn giữa chừng, mất điện rồi cấp lại |
| ⭐ Nguyên tắc về phụ thuộc bên ngoài | **Mất kết nối lên trên thì máy vẫn chạy** |
| Bàn giao gồm gì | 10 mục ở mục 57.9 — ⭐ đừng quên **mốc đo** và **sổ nhật ký để trống** |
| ⭐⭐ Năm quyết định định hình cỗ máy | Đánh giá rủi ro sớm · bảng I/O trước tủ · tham số là dữ liệu · biết nút cổ chai · thống kê cài từ đầu |
| ⭐⭐ Điểm chung của cả năm | **Đều là quyết định sớm, và đều rẻ ở thời điểm đó** |

---

## 57.14 Tự kiểm

1. ⭐ Kể tám giai đoạn của dự án DP-01 và đầu ra chính của mỗi giai đoạn.
2. ⭐⭐ Vì sao đánh giá rủi ro phải nằm ở giai đoạn 1? Nêu hai hậu quả khi làm nó ở cuối.
3. ⭐⭐ Vì sao bảng I/O phải có **trước** khi đấu tủ? Ba nơi nào phải dùng chung một quy ước tên?
4. Nêu bốn quyết định kiến trúc của DP-01 và lý do từng cái.
5. ⭐ Vì sao "tham số sản phẩm là dữ liệu, không phải mã" là quyết định phân biệt máy dùng được lâu?
6. ⭐ Vì sao xử lý an toàn là phần **viết đầu tiên**, không phải phần thêm vào sau?
7. Vì sao chuyển động tay và về gốc viết **trước** trình tự tự động?
8. ⭐ Vì sao báo động viết **sau** trình tự?
9. ⭐⭐ Kể tám tình huống xấu phải kiểm thử trên DP-01, và máy phải làm gì trong mỗi tình huống.
10. ⭐ Vì sao "máy vẫn chạy khi mất kết nối lên trên" là nguyên tắc, không phải tuỳ chọn?
11. Liệt kê bộ hồ sơ bàn giao. Hai mục nào hay bị bỏ nhất, và chúng cứu ai?
12. ⭐⭐ Nêu năm quyết định định hình cỗ máy và hệ quả nếu quyết sai. Điểm chung của chúng là gì?
13. ⭐ Áp mục 57.7 vào một dự án bạn biết: bước nào đang bị làm sai thứ tự, và hậu quả đã thấy là gì?

> Câu 2, 3, 9 và 12 là bốn câu phân loại. Câu 13 là câu quan trọng nhất — nó là lúc chương này thôi
> là một bài đọc và trở thành một công cụ.

---

### Chương tiếp theo

Chương 58 — **Học tiếp thế nào & vào nghề thật**. Cỗ máy đã xong. Chương cuối về con đường phía
trước: học gì tiếp, chứng minh năng lực thế nào khi chưa có kinh nghiệm, và bốn nhánh nghề với đánh
đổi của từng nhánh.

### Nguồn tham khảo chương 57

- **Phụ lục J** — số liệu đã chốt của DP-01: 300 board/giờ, board 100 × 80 mm, gantry X 0–150 ·
  Y 0–120 · Z 0–50 mm, trục Z servo, sấy UV 6–12 s.
- Toàn bộ các chương được dẫn trong bảng ở mục 57.3–57.10 — ⭐ **chương này không giới thiệu nguồn
  mới**, nó chỉ ráp lại những gì đã dẫn.
- ISO 12100 · ISO 13849-1 · IEC 62061 · IEC 60204-1 — nền an toàn cho giai đoạn 1, 3 và 7; xem
  Chương 6, 47, 48. *(tiêu chuẩn có bản quyền)*
- IEC 61131-3 — nền cho kiến trúc chương trình ở mục 57.6; xem Chương 20, 21, 30.

> ⚠ **Giới hạn.** DP-01 là một **máy mẫu dạy học**. Nó được thiết kế để mỗi bộ phận minh hoạ đúng một
> khái niệm của sách, không phải để tối ưu về giá hay về công nghệ. ⚠ Một cỗ máy thật sẽ có những
> đánh đổi mà máy mẫu này cố tình bỏ qua — và ⚠⚠ **phần an toàn của một máy thật phải do người có
> thẩm quyền thiết kế và kiểm định**, không sao chép từ sách.
