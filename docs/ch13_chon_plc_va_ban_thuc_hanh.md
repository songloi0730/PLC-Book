# Chương 13 — Chọn PLC & dựng bàn thực hành của riêng bạn

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

> ⚠⚠ **ĐỌC TRƯỚC — phạm vi và giới hạn của chương này**
>
> Phần thứ hai của chương hướng dẫn **tự dựng một bàn thực hành có đấu điện lưới**. Điện lưới giết
> người, và một bàn tự dựng không có ai kiểm định thay bạn.
>
> Chương này **không**:
> - không thay thế **kiến thức an toàn điện** — nếu bạn chưa đọc Chương 3, dừng lại và đọc trước;
> - không thay thế **quy định của cơ sở** nơi bạn đặt bàn (trường, xưởng, nhà);
> - không cho phép bạn tự kết luận bàn của mình là an toàn.
>
> Phần đấu nối từ ổ cắm điện lưới tới bộ nguồn phải do **người có thẩm quyền** làm hoặc kiểm tra —
> người có chuyên môn điện và được phép làm việc đó ở nơi bạn đang ở. Phần 24 V phía sau bộ nguồn thì
> bạn tự làm được, và mục 13.7 chỉ rõ ranh giới ấy.
>
> ⚡ **Thông tin có hạn sử dụng.** Chương này nhắc tới dòng sản phẩm, chính sách bản quyền phần mềm và
> mức giá tương đối. **Ba thứ đó đổi liên tục.** Mọi con số và tình trạng sản phẩm phải được kiểm lại
> trên trang chính thức của hãng tại thời điểm bạn đọc (Phụ lục G).

---

## 13.1 Hai câu hỏi, hai chương khác nhau

Chương này trả lời hai câu hỏi tách biệt, đừng lẫn chúng:

| | Câu hỏi | Ai hỏi | Mục |
|---|---|---|---|
| **A** | Chọn PLC nào cho **dự án thật** của khách hàng? | Người đi làm | 13.2–13.5 |
| **B** | Mua gì để **tự học** ở nhà, với tiền của mình? | Người mới vào nghề | 13.6–13.9 |

Tiêu chí của hai câu này **gần như không giao nhau**. PLC tốt nhất để học có thể là lựa chọn tệ cho
dự án, và ngược lại. Nhầm hai câu là lý do nhiều người mua nhầm thiết bị đầu tiên.

---

## 13.2 Bảy tiêu chí chọn PLC cho dự án thật

Xếp theo thứ tự **thường bị bỏ qua nhiều nhất ở cuối**, không phải theo tầm quan trọng.

### 1. Số I/O — và dự phòng

Đếm từ bảng I/O (Chương 23), cộng **20 % dự phòng** (Chương 8, mục 8.3). Tách riêng theo loại: DI,
DO, AI, AO, và các kênh chuyên biệt như đếm tốc độ cao.

> ⚠ Đếm cả những thứ người ta hay quên: tín hiệu bắt tay với máy bên cạnh, tín hiệu báo lên hệ thống
> trên, ngõ vào từ mạch an toàn để PLC **biết** trạng thái, đèn báo và còi, nút bấm ở nhiều vị trí.

### 2. Loại I/O

Từ Chương 9: ngõ vào sink hay source, ngõ ra rơ-le hay transistor. Đây là quyết định **lúc mua**, sửa
sau nghĩa là thay module và đấu lại dây.

### 3. Thời gian quét cần thiết

Từ Chương 10 và Chương 18: tính tần số tín hiệu nhanh nhất phải bắt được, so với thời gian quét dự
kiến. Nếu vào vùng cần bộ đếm tốc độ cao thì **CPU phải có kênh HSC**, và số kênh phải đủ.

### 4. Mạng

Máy có phải nối với gì không — máy bên cạnh, hệ thống trên, biến tần, I/O phân tán? Nếu có thì:

- cổng mạng **có sẵn trên CPU** hay phải mua module thêm;
- giao thức nào — và **phía bên kia dùng gì** (Chương 40, Chương 42);
- nếu dùng I/O phân tán, mạng đó có phù hợp không (Chương 8, mục 8.5).

### 5. Hệ sinh thái phần mềm

| Câu hỏi | Vì sao quan trọng |
|---|---|
| Phần mềm có **miễn phí** không, hay phải mua bản quyền? | Ảnh hưởng cả chi phí dự án và **khả năng khách hàng tự sửa máy** |
| Bản quyền tính theo máy tính, theo người, hay theo dự án? | Đội bảo trì của khách có được cấp bản quyền không? |
| Có hỗ trợ **ngôn ngữ** bạn định dùng không? | Không phải dòng CPU nào cũng có Structured Text (Chương 20, mục 20.8) |
| Có mô phỏng không cần phần cứng không? | Quyết định bạn kiểm thử được bao nhiêu trước khi có máy (Chương 50) |
| Tài liệu và cộng đồng | Chỗ bạn tra khi kẹt lúc hai giờ sáng |

> ⚠⚠ **Câu hỏi bản quyền là câu hỏi bàn giao, không phải câu hỏi kỹ thuật.**
> Nếu khách hàng không có bản quyền phần mềm, họ **không mở được chương trình của chính máy họ**. Khi
> máy hỏng và bạn không liên lạc được, dây chuyền của họ dừng. Đây phải là một điều khoản trong hợp
> đồng, bàn từ đầu — không phải phát hiện lúc bàn giao (Chương 54).

### 6. ⭐ Khả năng cung ứng dài hạn

Tiêu chí bị bỏ qua nhiều nhất, và là tiêu chí gây thiệt hại lớn nhất về sau.

Một cỗ máy công nghiệp sống 10–20 năm. Câu hỏi phải hỏi **trước khi mua**:

- Dòng sản phẩm này còn được sản xuất bao lâu nữa? Hãng có công bố lộ trình không?
- Mua được **ở địa phương** không, hay phải nhập và chờ nhiều tuần?
- Khi CPU hỏng lúc 2 giờ sáng, **bao lâu có hàng thay**?
- Phụ tùng có sẵn trên thị trường không?

> ⚠ **Một CPU rẻ hơn nhưng phải chờ sáu tuần để thay là CPU đắt hơn nhiều.**
> Chi phí thật là **thời gian dừng máy**, không phải giá mua. Với dây chuyền sản xuất, một ngày dừng
> có thể vượt giá trị cả cái tủ điện.

Hệ quả thực dụng: nhiều đơn vị **chuẩn hoá theo một hãng** cho toàn nhà máy, dù hãng đó không tối ưu
cho mọi máy. Họ đổi tính tối ưu lấy: trữ phụ tùng chung, đội bảo trì chỉ cần biết một hệ, một bộ bản
quyền phần mềm. Đó thường là quyết định đúng.

### 7. Khách hàng đã chuẩn hoá theo hãng nào

Câu hỏi này **thường quyết định tất cả** những câu trên. Nếu nhà máy đã có ba mươi máy dùng một hãng,
máy thứ ba mươi mốt gần như chắc chắn phải cùng hãng — dù bạn thấy hãng khác hợp hơn.

**Hỏi câu này trước tiên.** Nó thuộc về đặc tả (Chương 23), và nó tiết kiệm cho bạn cả buổi so sánh
vô ích.

---

## 13.3 Bảng đối chiếu các hệ phổ biến

Nêu tên để bạn **biết đường tra và so sánh**, không phải để khuyến nghị. Cột "đặc điểm" là những thứ
tương đối ổn định; **mọi số liệu cụ thể phải lấy từ catalogue hiện hành**.

| Hệ | Dòng cho máy nhỏ–vừa | Phần mềm | Đặc điểm đáng cân nhắc |
|---|---|---|---|
| **Siemens** | S7-1200, S7-200 SMART | TIA Portal | Hệ sinh thái rất rộng, tài liệu và cộng đồng nhiều; PROFINET chủ đạo; ⚠ bản quyền phần mềm là khoản chi đáng kể |
| **Mitsubishi** | FX5U / iQ-F | GX Works3 | Rất phổ biến ở máy châu Á và ở Việt Nam; nhiều máy cũ trong xưởng dùng dòng FX đời trước |
| **Inovance** | H5U, Easy series | AutoShop, InoProShop | ⭐ Giá cạnh tranh, **dễ mua và có hỗ trợ tại Việt Nam**; tích hợp tốt với biến tần và servo cùng hãng (Chương 36, 37) |
| **Rockwell** | Micro800, CompactLogix | Connected Components Workbench, Studio 5000 | Chiếm ưu thế ở Bắc Mỹ; mô hình tag rất mạnh; ⚠ chi phí bản quyền cao ở dòng lớn |
| **Omron** | NX1P, CP2E | Sysmac Studio | Mạnh về chuyển động và tích hợp thị giác máy |
| **Delta** | DVP, AS series | ISPSoft / WPLSoft | Giá thấp, phổ biến ở máy nhỏ và ở thị trường Việt Nam |
| **Beckhoff** | CX series, PLC mềm | TwinCAT | PLC mềm trên PC; EtherCAT; hợp khi cần nhiều trục hoặc tích hợp PC |
| **CODESYS** | Chạy trên phần cứng nhiều hãng | CODESYS Development System | Trung lập hãng, **bám chuẩn IEC 61131-3 sát nhất** — sách dùng làm mốc đối chiếu; học ở đây thì kiến thức chuyển sang hệ khác dễ nhất |

> ⚡ **Cách dùng bảng này cho đúng**
> Đừng chọn theo dòng nào "trông tốt nhất". Hãy đi qua bảy tiêu chí ở mục 13.2 theo thứ tự — bắt đầu
> bằng tiêu chí 7 (khách hàng đã dùng hãng nào) — rồi loại dần. Thường chỉ còn một hoặc hai lựa chọn
> thật, và quyết định trở nên dễ.

---

## 13.4 Bảng công tác chọn PLC

Điền bảng này trước khi hỏi giá. Nó biến một quyết định cảm tính thành một quyết định có căn cứ, và
nó cũng là thứ bạn đưa ra khi cần giải thích lựa chọn cho người khác.

| # | Mục | Trả lời của bạn |
|---|---|---|
| 1 | Khách hàng đã chuẩn hoá theo hãng nào? | |
| 2 | DI / DO / AI / AO cần, đã cộng 20 % | |
| 3 | Kênh chuyên biệt: HSC, ngõ ra xung, cân, nhiệt độ | |
| 4 | Loại ngõ vào (sink/source) và ngõ ra (rơ-le/transistor) | |
| 5 | Tín hiệu nhanh nhất phải bắt — tần số? Cần HSC không? | |
| 6 | Nối với gì, giao thức nào, phía kia dùng gì | |
| 7 | Ngôn ngữ lập trình sẽ dùng (Chương 20, mục 20.6) | |
| 8 | Bản quyền phần mềm: ai trả, khách có được cấp không | |
| 9 | Thời gian có hàng thay khi CPU hỏng | |
| 10 | Dòng này còn sản xuất bao lâu | |
| 11 | Còn khe / còn bộ nhớ để mở rộng không | |

Mục 8, 9, 10 là ba mục hay để trống. Chúng cũng là ba mục gây đau đớn nhất về sau.

---

## 13.5 Sai lầm thường gặp khi chọn

| Sai lầm | Hậu quả |
|---|---|
| Chọn theo giá mua thấp nhất | Thời gian dừng máy và chi phí bản quyền vượt xa khoản tiết kiệm |
| Chọn vừa khít nhu cầu hiện tại | Không mở rộng được; phải đổi CPU khi khách yêu cầu thêm chức năng |
| Quên tính chi phí bản quyền phần mềm | Vượt ngân sách, hoặc khách không tự sửa được máy |
| Không hỏi khách đã dùng hãng nào | Nhà máy phải trữ thêm một loại phụ tùng, đội bảo trì phải học thêm một hệ |
| Chọn dòng sắp ngừng sản xuất | Vài năm sau không mua được phụ tùng |
| Quên kênh chuyên biệt (HSC, ngõ ra xung) | Phát hiện khi lập trình → đổi CPU giữa dự án |

---

## 13.6 Phần B — bàn thực hành: bốn đường học

Chuyển sang câu hỏi thứ hai: **tự học thì mua gì?**

| Đường | Chi phí | Giống thực tế | Giá trị khi phỏng vấn | Hợp với ai |
|---|---|---|---|---|
| **A. PLC mới, dòng nhỏ giá thấp** | Trung bình | ⭐ Cao — phần cứng thật, phần mềm thật | ⭐ Cao — nói được "tôi đã đấu và chạy" | Người quyết tâm theo nghề |
| **B. PLC cũ mua lại** | Thấp | Cao, nhưng ⚠ có thể là đời đã lỗi thời | Trung bình–cao | Người eo hẹp ngân sách, chấp nhận rủi ro |
| **C. PLC mềm + mô phỏng trên máy tính** | ⭐ Rất thấp (thường miễn phí) | Trung bình — **không có phần cứng, không có đấu dây** | Trung bình | Người muốn thử trước khi bỏ tiền |
| **D. Mã nguồn mở trên máy tính nhúng** | Thấp | Thấp về mặt hệ công nghiệp | Thấp cho vị trí PLC | Người thích tự làm, đã biết lập trình |

### Nhận xét thẳng về từng đường

**A — PLC mới dòng nhỏ.** Đường tốt nhất nếu bạn định theo nghề. Bạn chạm vào **cả ba thứ** mà công
việc thật đòi hỏi: phần mềm thật của hãng, phần cứng thật, và **việc đấu dây** — thứ mà không mô
phỏng nào dạy được. Chọn hãng nào thì theo mục 13.3, ưu tiên hãng **phổ biến ở nơi bạn định xin
việc** và **có phần mềm miễn phí hoặc bản dùng thử đủ dùng**.

**B — PLC cũ.** Rẻ và học được nhiều, nhưng ba rủi ro thật: có thể **hỏng sẵn** mà bạn không đủ kinh
nghiệm để biết; có thể **bị khoá mật khẩu** bởi chủ cũ; và phần mềm cho đời cũ có thể **không chạy
trên hệ điều hành hiện tại**. Nếu chọn đường này, ưu tiên dòng vẫn còn được hỗ trợ.

**C — PLC mềm và mô phỏng.** Cách rẻ nhất để biết mình có thích nghề này không. Học được **logic,
trình tự, tư duy máy trạng thái** — phần lớn nội dung Chương 15 tới Chương 30. Không học được: đấu
dây, sink/source, nhiễu, chẩn đoán bằng đồng hồ, và cảm giác về cái tủ điện. ⚠ Đây là **một nửa
nghề**, và nửa còn lại là nửa hay bị hỏi khi phỏng vấn.

**D — mã nguồn mở trên máy tính nhúng.** Học được nhiều về lập trình và về hệ thống, nhưng thứ bạn
làm ra **không phải PLC công nghiệp** — không có độ tin cậy, không có chứng nhận, không có hệ sinh
thái. Thú vị như một dự án cá nhân; đừng nhầm nó với kinh nghiệm PLC khi đi xin việc, và **đừng dùng
nó điều khiển thứ gì có thể gây thương tích**.

> 💡 **MẸO — lộ trình rẻ mà hiệu quả**
> Bắt đầu bằng **C** để xác nhận bạn thích nghề, trong vài tuần. Nếu thích thì chuyển sang **A** với
> một bộ nhỏ. Tổng chi phí thấp hơn mua nhầm ngay từ đầu, và bạn có cả hai loại kinh nghiệm.

---

## 13.7 ⚠ Ranh giới an toàn khi dựng bàn

Trước khi tới danh sách vật tư, phải rõ ranh giới này.

```text
   Ổ cắm điện lưới  ──►  [ Cầu dao + cầu chì ]  ──►  [ Bộ nguồn 24 VDC ]  ──►  24 V
   ╰──────────── VÙNG NGUY HIỂM ────────────────────────────╯    ╰─ VÙNG BẠN TỰ LÀM ─╯
        người có thẩm quyền làm hoặc kiểm tra                    tự làm được sau Ch.3
```

> ⚠⚠ **NGUY HIỂM — điện lưới**
> - **Không đấu điện lưới nếu bạn chưa được đào tạo về an toàn điện.** Nhờ người có chuyên môn làm
>   phần từ ổ cắm tới đầu ra bộ nguồn, rồi bạn làm phần 24 V.
> - **Toàn bộ phần điện lưới phải nằm trong hộp kín**, không có đầu dây hở, không có điểm nào chạm
>   tay vào được khi bàn đang cắm điện.
> - **Có cầu dao và cầu chì** ở đầu vào. Không dùng dây nối trực tiếp không bảo vệ.
> - **Vỏ kim loại phải được nối đất.**
> - **Rút phích cắm trước khi đấu bất cứ thứ gì** — kể cả phần 24 V. Rút hẳn, không chỉ tắt công tắc.
> - Nếu ở nơi có yêu cầu riêng (ký túc xá, xưởng trường, nhà thuê), **hỏi trước**.

Phần 24 V phía sau bộ nguồn an toàn hơn nhiều, và đó là nơi bạn học được gần như mọi thứ về PLC.

---

## 13.8 Danh sách vật tư bàn thực hành

Cấu hình tối thiểu để chạy được các ví dụ trong sách này ở lát cắt 1.

| Hạng mục | Số lượng | Ghi chú |
|---|---|---|
| **PLC dòng nhỏ**, có sẵn DI và DO | 1 | Ưu tiên loại có ngõ ra transistor để thử được xung (Chương 9) |
| **Bộ nguồn 24 VDC**, 2–3 A | 1 | Loại gắn thanh ray, có vỏ kín |
| **Cầu dao + cầu chì** đầu vào | 1 bộ | ⚠ Bắt buộc |
| **Công tắc gạt** làm ngõ vào | 8 | Loại hai vị trí, gắn mặt |
| **Nút nhấn** (NO và NC) | 2 + 1 | ⭐ Có ít nhất **một nút NC** để hiểu Chương 15 |
| **Đèn báo 24 V** làm ngõ ra | 8 | LED, dòng nhỏ |
| **Cảm biến thật**: 1 quang PNP + 1 tiệm cận | 2 | ⭐ Quan trọng — thứ mô phỏng không dạy được (Chương 4) |
| **Thanh ray DIN + cầu đấu** | | Tập đấu dây gọn, đúng cách |
| **Dây điện nhiều màu**, đầu cốt, ống co | | Tập quy ước màu (Chương 3) |
| **Đồng hồ vạn năng** | 1 | ⭐ Không có thì không học được chẩn đoán (Chương 51) |
| Kìm bấm cốt, tuốc-nơ-vít cách điện | | |
| Tấm gỗ hoặc tấm nhôm làm đế | 1 | |

> 💡 **MẸO — hai thứ đừng tiết kiệm**
> **Cảm biến thật** và **đồng hồ vạn năng**. Công tắc gạt giả lập được tín hiệu, nhưng nó không dạy
> bạn PNP/NPN, không dạy dòng rò, không dạy cảm giác khi đèn cảm biến sáng mà bit không lên — đúng
> ba thứ mà người mới hay vấp (Chương 4, Chương 9). Và không có đồng hồ thì bạn chỉ đoán.

### Sơ đồ đấu — phần 24 V

```text
              +24 V ─────┬──────────┬───────────┬─────────────┐
                         │          │           │             │
                    [công tắc]  [công tắc]  [cảm biến PNP]     │
                         │          │           │ (dây nâu +24V)
                         │          │           │ (dây xanh 0V)
                       DI.0       DI.1        DI.2            │
                    ┌────┴──────────┴───────────┴────┐        │
                    │            PLC                 │        │
                    │  chân chung DI ── 0 V (sink)   │        │
                    │  chân chung DO ── 0 V          │        │
                    └────┬──────────┬────────────────┘        │
                       DO.0       DO.1                        │
                         │          │                         │
                      [đèn]      [đèn]                        │
                         │          │                         │
                0 V ─────┴──────────┴─────────────────────────┘
```

Ba điểm phải làm đúng, và cả ba đều là bài học thật:

- **Chân chung ngõ vào đấu 0 V** — vì cảm biến PNP cần ngõ vào kiểu **sink** (Chương 9, mục 9.2).
- **Cảm biến ba dây**: nâu về +24 V, xanh về 0 V, đen (hoặc trắng) là tín hiệu về ngõ vào. ⚠ Đấu
  nhầm nâu với đen là cách phổ biến nhất để **hỏng cảm biến** (Chương 4).
- **Một nút NC** trong bộ, để bạn tự làm được thí nghiệm ở Chương 15: rút dây nút đó ra và xem mạch
  hành xử thế nào — đây là cách hiểu "vì sao mạch dừng phải dùng tiếp điểm NC" nhanh hơn mọi lời
  giải thích.

---

## 13.9 Học gì trên bàn đó — theo thứ tự

Có bàn rồi thì làm gì? Lộ trình bám theo sách:

| Bước | Việc | Chương |
|---|---|---|
| 1 | Đấu và đo: xác nhận 24 V, xác nhận từng công tắc làm bit lên | 3, 52 (mục 52.4) |
| 2 | Đấu cảm biến PNP, xem đèn cảm biến và bit trong PLC | 4, 9 |
| 3 | Nấc thang đầu tiên: một công tắc bật một đèn | 15 |
| 4 | ⭐ Mạch tự giữ Start/Stop, và **rút dây nút Stop ra** xem chuyện gì xảy ra | 15, 16 |
| 5 | Bắt cạnh: đếm số lần nhấn nút, so với đếm không bắt cạnh | 16, 18 |
| 6 | Timer: ba loại, quan sát khác biệt khi xung ngắn hơn thời gian đặt | 17 |
| 7 | Trình tự nhiều bước bằng `CASE`, có timeout báo lỗi | 20, 26 |
| 8 | Cố tình gây lỗi rồi tự chẩn đoán bằng đồng hồ | 51 |

> ⭐ **Bước 4 và bước 8 là hai bước có giá trị nhất**, và cũng là hai bước người tự học hay bỏ.
> Bước 4 dạy bạn **vì sao** quy ước NC tồn tại — bằng cách thấy tận mắt. Bước 8 dạy kỹ năng được hỏi
> nhiều nhất khi phỏng vấn và dùng nhiều nhất khi đi làm: **tìm ra máy hỏng ở đâu**.

---

## 13.10 Bẫy thường gặp

### 🔍 BẪY 1 — Chọn PLC theo giá mua

**Hiện tượng:** tiết kiệm được một khoản lúc mua, rồi mất nhiều hơn ở chi phí bản quyền phần mềm, ở
thời gian chờ phụ tùng, và ở những giờ dừng máy.
**Cách sửa:** tính **chi phí sở hữu**: giá mua + bản quyền + phụ tùng + thời gian dừng máy dự kiến.
So sánh trên con số đó, không so trên giá catalogue.

### 🔍 BẪY 2 — Quên kênh chuyên biệt cho tới lúc lập trình

**Hiện tượng:** viết tới phần đếm xung mới phát hiện CPU không đủ kênh đếm tốc độ cao, hoặc không có
ngõ ra xung để điều khiển trục. Phải đổi CPU giữa dự án.
**Cách sửa:** liệt kê kênh chuyên biệt ở mục 3 của bảng công tác (mục 13.4), **trước khi hỏi giá**.

### 🔍 BẪY 3 — Không hỏi ai giữ bản quyền phần mềm

**Hiện tượng:** bàn giao xong, máy hỏng, khách hàng **không mở được chương trình của chính máy họ**.
Dây chuyền dừng tới khi liên lạc được với bạn.
**Cách sửa:** đưa vào hợp đồng từ đầu: ai được cấp bản quyền, khách có bản mã nguồn không, mật khẩu
bàn giao thế nào (Chương 54).

### 🔍 BẪY 4 — Chọn dòng sắp ngừng sản xuất

**Hiện tượng:** ba năm sau CPU hỏng, không mua được hàng thay cùng đời; đời mới không tương thích
chương trình hoặc không cắm vừa rack.
**Cách sửa:** hỏi nhà phân phối về vòng đời sản phẩm **trước khi mua**, và ghi câu trả lời kèm ngày
vào hồ sơ dự án.

### 🔍 BẪY 5 — Mua PLC cũ bị khoá mật khẩu

**Hiện tượng:** thiết bị chạy được nhưng **không đọc và không sửa được chương trình** trong đó; và
thường không xoá được để nạp chương trình của mình.
**Cách sửa:** khi mua hàng cũ, yêu cầu người bán **chứng minh xoá và nạp lại được** trước khi trả
tiền. Đây là rủi ro đặc thù của đường học B (mục 13.6).

### 🔍 BẪY 6 — Học hoàn toàn bằng mô phỏng rồi đi phỏng vấn

**Hiện tượng:** trả lời tốt câu hỏi về logic và trình tự, nhưng đứng hình ở câu "cảm biến PNP thì đấu
chân chung vào đâu" hoặc "đèn cảm biến sáng mà bit không lên thì làm gì".
**Cách sửa:** mô phỏng dạy được một nửa nghề. Nửa còn lại cần phần cứng thật — ít nhất một cảm biến
và một đồng hồ vạn năng (mục 13.8).

### 🔍 BẪY 7 — Đấu nhầm dây cảm biến ba dây

**Hiện tượng:** cảm biến nóng lên, hoặc chết ngay; hoặc bit không bao giờ lên.
**Cách sửa:** nâu về +24 V, xanh về 0 V, đen là tín hiệu. **Đo trước khi cấp điện**, và cấp điện lần
đầu thì nhìn cảm biến chứ đừng nhìn màn hình (Chương 4).

### 🔍 BẪY 8 — Đấu phần điện lưới của bàn khi chưa được đào tạo

**Hiện tượng:** không có hiện tượng nào — cho tới lần chạm nhầm. Điện lưới không cho cơ hội thứ hai.
**Cách sửa:** ranh giới ở mục 13.7. Nhờ người có thẩm quyền làm phần từ ổ cắm tới đầu ra bộ nguồn.
Phần 24 V phía sau thì bạn tự làm, và nó đủ để học gần như mọi thứ trong sách này.

### 🔍 BẪY 9 — Dựng bàn xong rồi chỉ chạy ví dụ mẫu

**Hiện tượng:** đấu đúng theo hình, chương trình chạy đúng, nhưng khi máy thật hỏng thì **không biết
bắt đầu từ đâu** — vì chưa bao giờ thấy cái gì hỏng.
**Cách sửa:** bước 4 và bước 8 ở mục 13.9. **Tự gây lỗi có chủ ý** — rút một sợi dây, tháo lỏng một
cảm biến, đảo một chân chung — rồi tự tìm ra. Đây là bài tập giá trị nhất trên bàn.

---

## 13.11 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Hỏi gì **trước tiên** khi chọn PLC cho dự án | Khách hàng đã chuẩn hoá theo hãng nào |
| Ba tiêu chí hay bị bỏ nhất | Chi phí bản quyền · thời gian có hàng thay · dòng còn sản xuất bao lâu |
| Chi phí thật của một PLC | Giá mua + bản quyền + **thời gian dừng máy khi hỏng** |
| Dự phòng I/O | **20 %**, và tính cả nhu cầu giai đoạn sau |
| Kênh chuyên biệt (HSC, ngõ ra xung) | Phải chốt **lúc mua** — không thêm bằng phần mềm |
| Học rẻ nhất | PLC mềm + mô phỏng — nhưng chỉ học được **một nửa nghề** |
| Học sát thực tế nhất | PLC thật dòng nhỏ, có đấu dây |
| Hai thứ đừng tiết kiệm trên bàn thực hành | **Cảm biến thật** và **đồng hồ vạn năng** |
| ⚠ Ranh giới an toàn | Điện lưới → người có thẩm quyền · 24 V → bạn tự làm sau Chương 3 |
| Bài tập giá trị nhất trên bàn | Rút dây nút Stop NC ra và quan sát · tự gây lỗi rồi chẩn đoán |

---

## 13.12 Tự kiểm

1. Nêu bảy tiêu chí chọn PLC cho dự án thật. Tiêu chí nào nên hỏi **trước tiên**, vì sao?
2. ⭐ Vì sao "khả năng cung ứng dài hạn" quan trọng hơn giá mua? Nêu một tình huống cụ thể.
3. Vì sao chi phí bản quyền phần mềm là **câu hỏi bàn giao** chứ không phải câu hỏi kỹ thuật?
4. Một nhà máy đã có 30 máy dùng cùng một hãng. Máy thứ 31 nên dùng hãng nào, và vì sao — kể cả khi
   hãng khác hợp hơn về kỹ thuật?
5. Kênh nào **phải chốt lúc mua CPU** vì không thêm được bằng phần mềm?
6. ⭐ So sánh bốn đường học theo ba trục: chi phí, độ giống thực tế, giá trị khi phỏng vấn. Đường nào
   bạn chọn và vì sao?
7. PLC mềm và mô phỏng **không** dạy được những gì? Nêu ít nhất bốn thứ.
8. Trên bàn thực hành, vì sao phải có ít nhất **một nút NC**? Mô tả thí nghiệm bạn sẽ làm với nó.
9. ⚠ Nêu ranh giới an toàn khi dựng bàn: phần nào bạn tự làm được, phần nào phải nhờ người có thẩm
   quyền, và vì sao ranh giới nằm ở đúng chỗ đó?
10. ⭐ Vì sao **cảm biến thật** và **đồng hồ vạn năng** là hai thứ không nên tiết kiệm, dù công tắc
    gạt rẻ hơn và giả lập được tín hiệu?

> Câu 2, 6 và 10 là ba câu phân loại. Câu 10 là tinh thần của cả chương: **thứ mô phỏng không dạy
> được chính là thứ phân biệt người biết lập trình PLC với người làm được máy chạy.**

---

### Chương tiếp theo

Chương 14 — **Năm ngôn ngữ của IEC 61131-3**. Bạn đã có phần cứng và biết chọn nó. Từ đây sách chuyển
sang lập trình: chuẩn cho những ngôn ngữ nào, mỗi ngôn ngữ hợp với việc gì, và vì sao ladder vẫn
chiếm ưu thế ở tầng máy.

### Nguồn tham khảo chương 13

- IEC 61131-1 và -2 — *Programmable controllers*: cơ sở cho các tiêu chí kỹ thuật ở mục 13.2.
  *(tiêu chuẩn có bản quyền)*
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu về bảo vệ mạch,
  cách ly nguồn và nối đất — nền cho ranh giới an toàn ở mục 13.7.
- **Catalogue, bảng giá và chính sách bản quyền hiện hành của các hãng nêu ở mục 13.3** — dùng cho
  mọi số liệu và tình trạng sản phẩm.
- Thông tin về vòng đời sản phẩm và thông báo ngừng sản xuất, công bố trên trang chính thức của từng
  hãng — dùng cho tiêu chí 6.

> ⚠⚠ **Thông tin có hạn sử dụng — đọc kỹ.** Bảng ở mục 13.3 và mọi nhận định về **giá tương đối, tính
> sẵn có, chính sách bản quyền, và dòng sản phẩm** đều **đổi theo thời gian và theo thị trường**. Dòng
> đang phổ biến hôm nay có thể ngừng sản xuất; phần mềm đang miễn phí có thể chuyển sang thu phí, và
> ngược lại.
>
> **Trước khi bỏ tiền, kiểm lại trên trang chính thức của hãng và với nhà phân phối ở địa phương
> bạn**, rồi ghi ngày kiểm tra vào hồ sơ dự án của mình. Sách nêu tên để bạn biết đường tra — không
> phải để thay việc tra (Phụ lục G).
>
> ⚠ **Về phần bàn thực hành:** nội dung mục 13.7–13.8 là **định hướng cho người tự học**, không phải
> thiết kế đã được kiểm định. Bàn của bạn, ở nơi của bạn, với vật tư bạn mua — chỉ **người có thẩm
> quyền** tại chỗ mới kết luận được là an toàn. Khi nghi ngờ, hỏi trước khi cắm điện.
