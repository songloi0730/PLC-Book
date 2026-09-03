# Nhật ký đối chiếu nguồn

> **Ghi lại từng khẳng định đã được đối chiếu với tài liệu gốc — kể cả những khẳng định ĐÚNG.**
>
> Mục đích kép: (1) không phải kiểm lại thứ đã kiểm; (2) ⭐ **nhìn ra chương nào CHƯA được đối
> chiếu** — thứ mà một danh sách chỉ ghi lỗi không cho biết.

Quy trình: `.claude/skills/doi-chieu-nguon/SKILL.md` · Công cụ: `python tools/tra_nguon.py "<từ khoá>"`

---

## Ký hiệu

| | Nghĩa |
|---|---|
| ✅ | **XÁC NHẬN** — nguồn nói đúng như sách |
| ⚠ | **ĐÃ SỬA** — nguồn nói khác, sách đã được sửa |
| ➕ | **ĐÃ BỔ SUNG** — sách không sai, nhưng thiếu chi tiết quan trọng có trong nguồn |
| ❔ | **KHÔNG CÓ NGUỒN** — bộ tài liệu không phủ; đã tra ngoài hoặc đã hạ giọng |

---

## Đợt 1 — 2026-09-02

Trọng tâm: các khẳng định **hành vi từng hãng** trong Phụ lục A1/A2 (viết gần nhất, chưa từng đối
chiếu, và dễ sai nhất), cộng chương an toàn lớn nhất.

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 1 | A1.5 | Rockwell ControlLogix cập nhật I/O **bất đồng bộ** với việc chạy logic; một tag đọc hai lần trong một task có thể cho hai giá trị | ✅ | Rockwell 1756-PM004 |
| 2 | A1.5 | Cách khắc phục: sao chép giá trị vào biến ở đầu đoạn | ✅➕ | Rockwell 1756-PM004 — hãng gọi là *"buffer the values"*; **đã bổ sung thuật ngữ này vào sách** |
| 3 | A2.2 | Độ phân giải bộ định thời Mitsubishi tuỳ **dải thiết bị `T`** | ⚠ | Mitsubishi FX5 Programming (Instructions/FB) — **SAI MỘT NỬA**: độ phân giải đến từ **lệnh** (`OUT` 100 ms / `OUTH` 10 ms / `OUTHS` 1 ms) và cũng có kiểu thiết bị. **Đã sửa + thêm bảng và dải giá trị đặt** |
| 4 | A1.4 | Rockwell AOI có dữ liệu riêng theo từng thể hiện | ✅ | Rockwell 1756-PM010 — dữ liệu hiển thị theo *"that specific instance"*, có local tags riêng |
| 5 | A2.7 | PLCopen Motion là chuẩn hoá nhưng **mức tuân thủ khác nhau** | ✅➕ | PLCopen *Function Blocks for Motion Control*, phụ lục Compliance — cơ chế cụ thể là **B (bắt buộc) / E (mở rộng) / V (riêng hãng)** + bảng khai tuân thủ. **Đã bổ sung cơ chế vào sách** |
| 6 | A1.6 | CODESYS `RETAIN` và `PERSISTENT` khác nhau ở việc sống sót qua tải xuống | ✅➕ | ❔ **Không có trong bộ tài liệu** → tra tài liệu CODESYS trực tuyến 2026-09-02. Đúng; **đã nâng cấp thành bảng hành vi 5 thao tác** |
| 7 | Ch.47 | Bảng Category B/1/2/3/4 — dự phòng và tự kiểm | ✅➕ | DGUV/IFA Report 2/2017e — **thiếu hai chi tiết**: Cat 2 cần tần suất kiểm **≥100×** tần suất yêu cầu; Cat 3 **vẫn mất** chức năng khi hỏng tích luỹ. **Đã bổ sung** |
| 8 | Ch.06 | Viện dẫn ISO 6431 cho kích thước xy-lanh | ⚠ | iso.org — **ISO 6431 đã bị THU HỒI**, thay bằng ISO 15552. **Đã sửa + nêu rõ tên cũ vẫn dùng trên catalogue** |
| 9 | Ch.45, 46, 47 | Viện dẫn "ISO 13849" không có số phần | ⚠ | Phần định nghĩa PL là **ISO 13849-1**. **Đã sửa 4 chỗ** |

### Kết quả đợt 1

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **9** |
| ✅ Xác nhận đúng | 5 |
| ⚠ Phát hiện sai, đã sửa | 3 |
| ➕ Bổ sung chi tiết còn thiếu | 4 |

> ⭐⭐ **Nhận xét quan trọng: tỉ lệ "đúng nhưng thiếu" (4/9) cao hơn tỉ lệ "sai hẳn" (3/9).**
>
> Nghĩa là giá trị lớn nhất của bước đối chiếu **không phải bắt lỗi** — mà là ⭐ **tìm ra chi tiết cụ
> thể mà bản viết từ trí nhớ luôn bỏ sót**. Con số "100 lần" của Category 2 và cơ chế "B/E/V" của
> PLCopen là loại nội dung không thể nhớ ra, chỉ có thể tra.

---

## Đợt 2 — 2026-09-02 (sau khi mở rộng bộ nguồn)

Trọng tâm: hai mảng mà đợt 1 khai nhầm là "không có nguồn".

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 10 | — | *"Bộ tài liệu không có CODESYS và Inovance"* | ⚠ | **SAI — đã đính chính.** `PLC/en/` và `PLC/Manual/` có đủ |
| 11 | A1.2 | Inovance dùng mô hình thiết bị `X`/`Y`/`M`/`D` giống Mitsubishi | ✅➕ | H5U Instruction Guide — đúng, và ⭐ **bổ sung**: `X`/`Y` đánh số **bát phân** (`X0`–`X1777` = 1024 điểm, không có `X8`/`X9`) |
| 12 | A1.6 | Inovance giữ dữ liệu bằng "dải thiết bị latched" | ✅➕ | H5U Instruction Guide — đúng, và ⭐ **bổ sung quy luật cụ thể**: 1000 phần tử đầu của **mọi** loại (`M`,`S`,`B`,`D`,`R`,`W`) đều mất khi mất điện |
| 13 | A1.6 | Inovance "tuỳ dòng" (viết mơ hồ) | ➕ | InoProShop User Manual — ⭐ **cụ thể hoá**: AutoShop dùng dải thiết bị; InoProShop nền CODESYS dùng biến `PERSISTENT` |
| 14 | A1.6 | *(chưa có trong sách)* | ➕ | InoProShop *Persistent Rules* — ⚠⚠ **bẫy mới: đổi TÊN biến persistent làm MẤT giá trị**; đổi địa chỉ/chú thích/kiểu thì giữ. **Đã bổ sung** |
| 15 | A1.6 | CODESYS `RETAIN` vs `PERSISTENT` (đợt 1 tra web) | ✅ | Đã có nguồn nội bộ xác nhận cơ chế persistent trên nền CODESYS của Inovance |

### Kết quả đợt 2

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **6** |
| ✅ Xác nhận đúng | 3 |
| ⚠ Phát hiện sai, đã sửa | 1 *(chính kết luận của đợt 1)* |
| ➕ Bổ sung chi tiết còn thiếu | 4 |

> ⭐⭐ **Phát hiện giá trị nhất của đợt 2 là mục 14 — một cái bẫy sách hoàn toàn chưa nhắc.**
>
> Trên nền CODESYS của Inovance, **đổi tên một biến persistent làm mất giá trị của nó**. Nghĩa là một
> lần "dọn dẹp cho gọn tên biến" xoá sạch bộ đếm tích luỹ nhiều năm. ⭐ Không ai đoán ra được điều đó
> — chỉ tra tài liệu mới biết.

---

## Đợt 3 — 2026-09-02 · Ch.39 (Modbus) và Ch.47 (an toàn)

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 16 | Ch.39 §39.4 | *"Đọc `40001` → vượt dải → lỗi địa chỉ"* | ⚠ | Đặc tả Modbus — **thiếu chính xác**: `40001` (`0x9C41`) **hợp lệ** với trường địa chỉ 16 bit; nó lỗi vì **thiết bị không có thanh ghi ở đó** → ngoại lệ 02. **Đã sửa** |
| 17 | Ch.39 | *(chưa có trong sách)* — **bảng mã ngoại lệ** | ➕ | ⚠⚠ Chương có hẳn mục "Quy trình gỡ lỗi Modbus" nhưng **không có mã ngoại lệ nào** → người đọc không giải mã được lỗi thiết bị trả về. **Đã bổ sung bảng 6 mã + nối vào quy trình gỡ lỗi** |
| 18 | Ch.39 | *(chưa có)* — mã 02 nói về **tổ hợp** địa chỉ + số lượng | ➕ | Đặc tả nêu ví dụ: thiết bị 100 thanh ghi, bắt đầu 96 đọc 4 → OK; đọc 5 → **ngoại lệ 02**. ⭐ Đúng địa chỉ vẫn lỗi nếu đọc quá dài. **Đã bổ sung** |
| 19 | Ch.39 | *(chưa có)* — **giới hạn 125 thanh ghi/lần đọc** | ➕ | Đặc tả FC 0x03: `Quantity of Registers` = 1–125 (`0x7D`). **Đã bổ sung** kèm 123 (ghi) và 2000 (bit) |
| 20 | Ch.39 | *(chưa có)* — mã 03 **KHÔNG** nghĩa là "giá trị ngoài dải quy trình" | ➕ | ⭐ Đặc tả nói rõ ngược lại điều người ta hay nghĩ: Modbus **không biết ý nghĩa** của giá trị. **Đã bổ sung cảnh báo** |
| 21 | Toàn sách | **OSSD** — ngõ ra thiết bị an toàn | ➕ | ⚠⚠ **Từ "OSSD" KHÔNG xuất hiện ở bất kỳ đâu** trong 58 chương + 12 phụ lục. Bổ sung mục 47.7: định nghĩa, xung kiểm tra, và ⭐ **bẫy đấu OSSD vào ngõ vào thường → bit nhấp nháy**. Nối vào Ch.49 (danh sách lỗi chập chờn, nay 8 mục) và Phụ lục E.10 |

### Kết quả đợt 3

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **6** |
| ⚠ Phát hiện sai, đã sửa | 1 |
| ➕ Bổ sung nội dung còn thiếu | 5 |

> ⭐⭐ **Đợt 3 khác hai đợt trước: phần lớn phát hiện là NỘI DUNG THIẾU, không phải nội dung sai.**
>
> Ch.39 dạy gỡ lỗi Modbus mà không dạy đọc mã lỗi. Cả cuốn sách nhắc "lỗi chập chờn" hàng chục lần
> mà chưa từng nhắc **OSSD** — một trong những nguyên nhân chập chờn kinh điển nhất.
>
> ⭐ **Bài học về quy trình:** đối chiếu nguồn không chỉ để kiểm cái đã viết, mà để phát hiện ⭐ **cái
> đáng lẽ phải viết mà không ai nghĩ ra** — vì người viết không biết cái mình không biết.

---

## Đợt 4 — 2026-09-02 · Ch.6 (khí nén) và Ch.3 (điện) — hai chương mang cờ ⚠

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 22 | Ch.6 §6.3 | Bảng "mất điện thì về đâu" cho van 5/2 | ✅➕ | Đúng, nhưng ⚠⚠ **chương KHÔNG trả lời "mất KHÍ thì về đâu"**. Van hai cuộn giữ vị trí **van**, không giữ **tải** — khí nén được và mọi con trượt đều rò. **Đã bổ sung bảng phân biệt + hai cơ cấu giữ tải** |
| 23 | Ch.6 | Viện dẫn ISO 4414 | ✅ | Thư mục DGUV/IFA — tên và phạm vi đúng: *Pneumatic fluid power — General rules and safety requirements*. ⚠ Chi tiết kỹ thuật giữ tải **không có trong bộ tài liệu** → tra ngoài; ⭐ **không dẫn số điều khoản** |
| 24 | Ch.48 BẪY 2 · Phụ lục J SF6 | "Giữ kẹp khi mất khí" | ✅➕ | ⭐ Ch.48 **đã có nguyên tắc đúng** ("giữ bằng cơ cấu không phụ thuộc năng lượng") nhưng thiếu tên cơ cấu. **Đã nối ba tài liệu** cho nhất quán |
| 25 | Ch.3 §3.3 | *"24 V nằm trong dải điện áp cực thấp → an toàn hơn"* | ⚠➕ | ⚠⚠ **Thiếu điều kiện quyết định**: ELV chỉ nói về **mức điện áp**; cái bảo vệ người là **cách ly an toàn** (SELV/PELV). Từ "SELV" **không xuất hiện ở bất kỳ đâu** trong sách. **Đã bổ sung mục mới** |
| 26 | Ch.3 · Ch.8 | Yêu cầu với bộ nguồn 24 V | ➕ | Siemens S7-1200 System Manual, Wiring guidelines: nguồn cho mạch 24 V/I/O/truyền thông **phải đạt SELV, PELV, Class 2, Limited Voltage hoặc Limited Power** theo EN 61131-2; ⚠ nguồn **không cách ly** làm **điện áp lưới xuất hiện trên dây cảm biến**. **Đã bổ sung cả hai chương** |
| 27 | Ch.49 §49.4 | Nối đất một điểm duy nhất | ✅ | Siemens S7-1200, Guidelines for grounding — khuyến nghị nối mọi điểm chung về **một điểm duy nhất** rồi nối đất. Khớp với sách |
| 28 | Ch.3 §3.7 | An toàn điện: dòng giết người · tự kiểm đồng hồ · một tay trong túi · năng lượng tích trữ | ✅ | Không mâu thuẫn với các tài liệu an toàn trong bộ; ⭐ nội dung chắc, giữ nguyên |

### Kết quả đợt 4

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **7** |
| ✅ Xác nhận đúng | 4 |
| ⚠ Thiếu điều kiện quan trọng, đã sửa | 1 |
| ➕ Bổ sung nội dung còn thiếu | 4 |

> ⭐⭐ **Phát hiện nặng nhất từ trước tới nay là mục 25–26.**
>
> Sách viết *"24 V nằm trong dải điện áp cực thấp nên an toàn hơn"* — đúng chữ nhưng **thiếu điều
> kiện quyết định**. Bảo vệ đến từ **cách ly**, không từ con số 24. Một bộ nguồn không cách ly hỏng
> có thể đưa điện áp lưới lên **dây cảm biến** — thứ mọi người cầm bằng tay trần vì tin "chỉ có 24 V".
>
> ⚠ Đây là loại thiếu sót mà bộ kiểm tự động **không thể** bắt: câu văn đúng ngữ pháp, đúng khung,
> nghe hợp lý, và nguy hiểm.

---

## Đợt 5 — 2026-09-02 · Ch.33 (đo lường)

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 29 | Ch.33 §33.4 | Pt100 = 100 Ω ở 0 °C, tăng ~**0,385 Ω/°C** | ✅➕ | Kuphaldt — alpha 0,00385 là giá trị "châu Âu", **phổ biến nhất kể cả ở Mỹ**. ⭐ **Bổ sung**: còn giá trị 0,00392 ("Mỹ"); trộn nhầm cảm biến/module gây **sai số có hệ thống, đồ thị vẫn đẹp** |
| 30 | Ch.33 | *(chưa có trong sách)* — **sai số tự gia nhiệt RTD** | ➕ | Kuphaldt, mục Self-heating error: dòng đo sinh nhiệt `P = I²R` trên chính phần tử → phép đo **luôn cao hơn**. ⭐ Là sai số **một chiều**, lấy trung bình không khử được; nặng nhất trong **không khí tĩnh**. **Đã bổ sung**, kèm cách module giải quyết (cấp dòng theo xung) |
| 31 | Ch.33 §33.4 | RTD 3 dây là mặc định của ngành; giả định ba sợi bằng nhau | ✅ | Kuphaldt, mục Proper RTD sensor connections — không mâu thuẫn |

### Kết quả đợt 5

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **3** |
| ✅ Xác nhận đúng | 2 |
| ➕ Bổ sung nội dung còn thiếu | 2 |

---

## Đợt 6 — 2026-09-02 · Ch.31 (analog 4–20 mA)

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 32 | Ch.31 §31.3 | Ngưỡng phát hiện đứt dây ~**3,6 mA**, lỗi cao ~**21 mA** | ✅➕ | Kuphaldt, mục NAMUR signal levels — đúng, nhưng ⭐ **bảng NAMUR chi tiết hơn nhiều**. **Đã bổ sung bảng 5 dải** |
| 33 | Ch.31 | *(chưa có)* — ⭐⭐ phân biệt **"đo dưới dải" (3,8–4,0 mA)** với **"cảm biến hỏng" (<3,6 mA)** | ➕ | ⚠ Sách gộp làm một. Hệ quả: đặt ngưỡng lỗi ở 4,0 mA sinh **báo động giả** mỗi khi đại lượng thật xuống hơi dưới điểm đầu thang. **Đã bổ sung** + nối tới Ch.43 (báo động giả làm người vận hành học cách bỏ qua) |
| 34 | Ch.31 | Cảm biến tuân NAMUR giữ dòng trong dải nào khi bình thường | ➕ | **3,8 mA đến dưới 21 mA**. **Đã bổ sung** |

### Kết quả đợt 6

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **3** |
| ✅ Xác nhận đúng | 1 |
| ➕ Bổ sung nội dung còn thiếu | 3 |

---

## Đợt 7 — 2026-09-02 · Phụ lục D và Ch.35 (PID)

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 35 | Phụ lục D §D.2 | *"Điện áp đo cách điện cao sẽ phá module"* | ✅➕ | Kuphaldt (DC), mục megohmmeter — megôm kế tạo **điện áp DC tới 1000 V**. **Đã bổ sung con số** để cảnh báo có sức nặng |
| 36 | Phụ lục D §D.2 | *(chưa có)* — kiểm nhãn **SELV/PELV** của bộ nguồn | ➕ | ⭐ Nối từ phát hiện đợt 4 (Ch.3). **Đã thêm mục kiểm nguội** |
| 37 | Phụ lục D §D.5 | *(chưa có)* — kiểm **đấu OSSD đúng chỗ** | ➕ | ⭐ Nối từ phát hiện đợt 3 (Ch.47). **Đã thêm mục kiểm chức năng an toàn** |
| 38 | Ch.35 | *(chưa có)* — ⚠⚠ **chiều tác động thuận/nghịch** | ➕ | ⚠⚠ **Chương PID không hề nhắc.** Đặt sai chiều biến vòng điều khiển thành **phản hồi dương** — ngõ ra chạy thẳng tới giới hạn. Với gia nhiệt, hậu quả có thể là cháy. **Đã bổ sung mục 35.6b** kèm triệu chứng nhận ra ngay và yêu cầu bảo vệ quá nhiệt độc lập |
| 39 | Ch.35 | *(chưa có)* — đơn vị khâu tích phân | ➕ | Kuphaldt: **phút/lần lặp** và **lần lặp/phút** là **nghịch đảo nhau**; số lớn mang nghĩa ngược nhau. ⭐ Là lý do kỹ thuật cho quy tắc "không chép tham số PID giữa hai máy" ở Phụ lục A2. **Đã bổ sung** |

### Kết quả đợt 7

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **5** |
| ✅ Xác nhận đúng | 1 |
| ➕ Bổ sung nội dung còn thiếu | 5 |

> ⭐⭐ **Mục 38 là phát hiện nặng thứ hai của cả quá trình, sau SELV.**
>
> Một chương PID dài 14 mục, có cả chống bão hoà tích phân và chỉnh định từng bước, mà **không nhắc
> chiều tác động** — thứ phải đặt đúng **trước** khi chỉnh định có ý nghĩa, và đặt sai thì vòng điều
> khiển chạy loạn thay vì dao động.
>
> ⭐ Nó lọt lưới vì **bộ kiểm tự động không thể biết một chương thiếu khái niệm gì** — chỉ đối chiếu
> với tài liệu chuyên ngành mới lộ ra.

---

## Đợt 8 — 2026-09-02 · Ch.40 (Ethernet công nghiệp)

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 40 | Ch.40 §40.6 | Bảng chuyển mạch quản lý được vs không | ✅➕ | Đúng, nhưng ⚠ **thiếu hai chức năng quyết định** — xem hai mục dưới |
| 41 | Ch.40 | *(chưa có)* — **IGMP snooping** cho lưu lượng multicast | ➕ | Tài liệu EtherNet/IP của Inovance H5U và InoProShop: cần chuyển mạch hỗ trợ **IGMP Snooping** để lọc gói multicast không liên quan. ⚠ Thiếu nó thì **mọi thiết bị nhận lưu lượng của mọi thiết bị**; thiết bị yếu rớt mạng trong khi thiết bị mạnh vẫn chạy. **Đã bổ sung** |
| 42 | Ch.40 | *(chưa có)* — **vòng lặp mạng** và giao thức dự phòng | ➕ | Rockwell *Resilient Converged Plantwide Ethernet*: cấu trúc vòng cần giao thức dự phòng (cây khung / giao thức vòng chuyên dụng). ⚠⚠ Vòng **không có giao thức** không phải dự phòng — **gói quảng bá chạy vô tận, mạng chết**. Cũng là điều xảy ra khi cắm nhầm hai cổng vào nhau. **Đã bổ sung** kèm triệu chứng nhận ra |

### Kết quả đợt 8

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **3** |
| ✅ Xác nhận đúng | 1 |
| ➕ Bổ sung nội dung còn thiếu | 3 |

> ⭐ **Cả hai bổ sung có cùng đặc điểm với các đợt trước: chúng hỏng theo kiểu KHÔNG lộ ra ngay.**
> Mạng chạy tốt lúc nghiệm thu với ít thiết bị, rồi xấu dần khi máy được mở rộng.

---

## Đợt 9 — 2026-09-02 · Ch.37 (chuyển động servo)

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 43 | Ch.37 | *(chưa có)* — ⭐⭐ **sai lệch bám** *(following error)* | ➕ | ⚠ **Chương servo không hề nhắc chẩn đoán cơ bản nhất của servo.** Tài liệu chuyển động Inovance: sai lệch bám = hiệu giữa vị trí lệnh gửi xuống driver và vị trí encoder gửi lên, có **giới hạn đặt được**, vượt thì driver báo lỗi và dừng trục. **Đã bổ sung mục 37.8b** |
| 44 | Ch.37 §37.8 | Mẫu `Execute` / `Done` / `Busy` của PLCopen | ✅➕ | Đúng, nhưng ⚠ **không nêu tên khối nào** nên người đọc không tra tiếp được. **Đã bổ sung tiền tố `MC_`** và ví dụ (`MC_Power`, `MC_Home`, `MC_MoveAbsolute`, `MC_Stop`, `MC_Reset`) |

### Kết quả đợt 9

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **2** |
| ✅ Xác nhận đúng | 1 |
| ➕ Bổ sung nội dung còn thiếu | 2 |

> ⭐⭐ **Sai lệch bám là loại nội dung có giá trị cao bất thường: một phép đo phát hiện được vấn đề
> CƠ KHÍ, miễn phí, từ trong chương trình.**
>
> Nó nối thẳng vào bài toán mở đầu chương ("trục Z đâm xuống board") — chạm vật cản làm sai lệch bám
> tăng vọt ngay lập tức. ⭐ Và nó là lần thứ **năm** nguyên tắc *"ghi mốc lúc máy còn mới"* xuất hiện
> trong sách.

---

## Đợt 10 — 2026-09-02 · Quét thiếu khái niệm trên diện rộng

⭐ **Đổi cách làm:** thay vì đối chiếu từng chương, quét xem **khái niệm nào của ngành vắng mặt trong
cả cuốn sách**. Cách này có tỉ lệ phát hiện cao hơn ở giai đoạn này.

| # | Khái niệm | Có trong sách? | KQ | Nguồn & xử lý |
|---|---|---|:--:|---|
| 45 | ⭐⭐ **Dòng rò ngõ ra bán dẫn** | ⚠ **Không, ở bất kỳ đâu** | ➕ | Petruzella: ngõ ra bán dẫn ở trạng thái tắt **vẫn có dòng rò vài mA**. ⚠ Gây lỗi kinh điển "ngõ ra đã tắt mà thiết bị vẫn chạy". **Đã bổ sung mục 9.3b** kèm ba cách xử lý |
| 46 | ⭐ **Thời gian đáp ứng / bộ lọc ngõ vào** | ⚠ **Không** | ➕ | Petruzella: *input ON/OFF delay*. ⚠ Lọc dài hơn độ rộng xung thì **PLC không bao giờ thấy xung** — mà đèn cảm biến vẫn nháy đúng. **Đã bổ sung** |
| 47 | ⭐⭐ **Encoder cầu phương A/B/Z** | ⚠ **Không** | ➕ | Hugh Jack: hai kênh lệch pha 90° cho **chiều quay**; kênh Z cho **một xung mỗi vòng**. ⚠ Chương HSC dạy đếm xung mà không dạy đếm chiều. **Đã bổ sung mục 18.5b** |
| 48 | ⚠⚠ **Chế độ x1 / x2 / x4** | ⚠ **Không** | ➕ | Đặt sai làm **mọi phép quy đổi sai đúng 4 lần** — sai theo **tỉ lệ tròn trịa**, dấu hiệu rất đặc trưng. **Đã bổ sung** kèm phép kiểm một phút (quay đúng một vòng bằng tay) |
| 49 | Bìa Karnaugh · BCD · FIFO · độ trễ ngắt | ⚠ Không | ❔ | ⭐ **Cân nhắc và quyết định KHÔNG bổ sung**: bìa Karnaugh không phục vụ tư duy trình tự của sách; BCD là di sản; FIFO đã được thay bằng thanh ghi dịch ở Ch.41. Ghi lại để lần sau không phải cân nhắc lại |

### Kết quả đợt 10

| | Số lượng |
|---|---|
| Khái niệm đã quét | **8** |
| ➕ Bổ sung | 4 |
| ❔ Cân nhắc và quyết định không bổ sung | 4 |

> ⭐⭐ **Bốn bổ sung của đợt này có chung một đặc điểm rất đáng chú ý: cả bốn đều biến một vấn đề
> PHẦN CỨNG thành triệu chứng trông giống lỗi PHẦN MỀM.**
>
> Ngõ ra "đã tắt" mà thiết bị vẫn chạy · cảm biến nháy đúng mà PLC đếm thiếu · quy đổi sai đúng bốn
> lần. Người lập trình sẽ đi tìm trong chương trình — và không bao giờ tìm thấy.
>
> ⭐ Đây chính là loại nội dung mà một cuốn sách PLC **phải** có mà tutorial online gần như luôn thiếu.

---

## Đợt 11 — 2026-09-02 · Quét đợt hai + hiệu chỉnh chính mình

| # | Khái niệm / khẳng định | KQ | Nguồn & xử lý |
|---|---|:--:|---|
| 50 | ⚠ **Dòng rò "vài mA"** *(chính bổ sung của đợt 10)* | ⚠ | Petruzella nói rõ hơn: **1–2 mA**, và ⭐ **"thường KHÔNG đủ làm thiết bị tác động nhầm"** — chỉ đáng lo với tải rất nhạy. ⭐ Tôi đã **nói quá mức rủi ro**. **Đã hiệu chỉnh** thêm đoạn cân bằng |
| 51 | ⭐ **Mức cách ly điện của module** | ➕ | Petruzella: thường ghi 1500 hoặc 2500 V AC. **Đã bổ sung** vào Ch.9, nối tới Ch.49 (chênh điện thế đất) |
| 52 | ⚠⚠ **Lắp module đứng giảm nhiệt độ cho phép** | ➕ | Siemens S7-1200 Manual, mục CAUTION: lắp đứng **giảm 10 °C** nhiệt độ môi trường tối đa; bảng thông số cho −20…60 °C ngang so với −20…50 °C đứng. **Đã bổ sung mục 8.7b** |
| 53 | ⭐ **Cấp bảo vệ: module vs vỏ tủ** | ➕ | Siemens: module đạt cấp chống vật rắn lớn, **không chống nước**. ⭐ Cấp bảo vệ thật của hệ là của **vỏ tủ** → ⚠ mở cửa tủ cho mát là bỏ luôn lớp bảo vệ. **Đã bổ sung** |
| 54 | ⭐ Rung mạnh → lắp vít thay ray DIN | ➕ | Siemens: khuyến nghị lắp tấm đế khi rung mạnh hoặc lắp đứng. **Đã bổ sung** |

### Kết quả đợt 11

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **5** |
| ⚠ **Tự hiệu chỉnh nội dung mình vừa thêm** | 1 |
| ➕ Bổ sung nội dung còn thiếu | 4 |

> ⭐⭐ **Mục 50 đáng ghi lại như một bài học về quy trình.**
>
> Bổ sung của đợt 10 về dòng rò **đúng về cơ chế nhưng nói quá về mức rủi ro** — vì tôi viết nó từ
> hiểu biết chung trước khi đọc kỹ nguồn. Đọc tiếp cùng tài liệu thì thấy hãng nói rõ *"thường không
> đủ để kích nhầm"*.
>
> ⚠ **Nội dung mới thêm cũng phải được đối chiếu như nội dung cũ** — không được miễn trừ chỉ vì nó
> vừa được viết ra từ một nguồn.

---

## Đợt 12 — 2026-09-02 · Ch.44 (báo động) và ⚠⚠ SỬA LỖI HỆ THỐNG Ở PHỤ LỤC F

| # | Chương / mục | Khẳng định được kiểm | KQ | Nguồn đối chiếu |
|---|---|---|:--:|---|
| 55 | Ch.44 §44.3 | Ba kỹ thuật chống lụt báo động | ✅➕ | Đúng, nhưng ⚠ **thiếu vùng chết cho báo động**. Kuphaldt: không có vùng chết thì công tắc **tự gỡ ngay khi giá trị về đúng ngưỡng** → dao động 0,1 độ sinh hàng chục báo động. ⭐ **Trễ và vùng chết sửa hai bệnh khác nhau** — đã bổ sung kỹ thuật thứ tư |
| 56 | Ch.44 | Vùng chết là tham số có sẵn của khối PID hãng | ➕ | Rockwell 1756-RM003: khối PID có `PVDB` và `DVDB` — vùng chết riêng cho báo động theo giá trị đo và theo sai lệch. **Đã bổ sung** |
| 57 | ⚠⚠ **Phụ lục F** | **Số chương dẫn cho từng thuật ngữ** | ⚠⚠ | ⭐⭐ **SAI HỆ THỐNG — 57 dòng.** Xem bên dưới |
| 58 | Phụ lục E | *"Chương 43 gọi đây là chuỗi cho phép"* | ⚠ | Ch.43 là **vision**. Thuật ngữ đó **không xuất hiện ở bất kỳ chương nào**. Đã sửa thành Ch.44 và bỏ cách nói "chương gọi là" |
| 59 | Ch.44 *(nội dung tôi vừa thêm)* | *"trễ tích luỹ ở Chương 34"* | ⚠ | Ch.34 là **Cân & đo lực**; vùng chết/trễ tích luỹ ở **Ch.32**. ⭐ Lỗi tôi **tự tạo ra trong chính đợt này** |

### ⚠⚠ Lỗi hệ thống ở Phụ lục F — và vì sao nó lọt lưới

Phụ lục F (thuật ngữ Việt–Anh) có cột "Chương" cho mỗi thuật ngữ. ⚠ **57 dòng dẫn sai số chương**,
vì khi viết phụ lục tôi dùng một **bản đồ chương sai trong đầu**.

| Thuật ngữ | F dẫn | Chương thật |
|---|---|---|
| Vòng quét · ảnh ngõ vào/ra | 7 | ⭐ **10** *(Ch.7 là ESD)* |
| Bộ định thời TON/TOF/TP | 11 | ⭐ **17** |
| Latch · Set/Reset · bắt cạnh | 11, 15 | ⭐ **16** |
| Bộ đếm · thanh ghi dịch | 12 | ⭐ **18** |
| Bộ nhớ giữ được · biến | 12, 24 | ⭐ **11** |
| Xy-lanh khí nén · van 5/2 · FRL | 5 | ⭐ **6** *(Ch.5 là cơ cấu ĐIỆN)* |
| FBD · IL | 16, 15 | ⭐ **21** |
| Công thức sản phẩm | 32 | ⭐ **29** |
| Setpoint · vòng kín/hở · vùng chết | 34 | ⭐ **32, 35** *(Ch.34 là cân & đo lực)* |
| Khoá liên động · chờ bận | 22, 26 | ⭐ **27, 47** |
| Đánh giá rủi ro | 6 | ⭐ **47** |

> ⚠⚠ **Vì sao lỗi này nguy hiểm hơn nó có vẻ:** một bảng thuật ngữ dẫn sai chương **chủ động gây hại**
> — người đọc tra "vòng quét → Chương 7" rồi lạc vào chương ESD, và kết luận sách viết ẩu.
>
> ⭐⭐ **Vì sao ba bộ kiểm không bắt được:** số chương nằm trong **ô bảng**, không theo mẫu `Chương N`.
> Với `kiem_nhat_quan.py` nó chỉ là một chữ số, không phải một dẫn chiếu.
>
> ⭐ **Đã thêm nhóm kiểm `GLOS`**: lấy thuật ngữ **tiếng Anh** (đặc trưng hơn tiếng Việt), đếm tần suất
> ở mọi chương, cảnh báo nếu chương được dẫn không nằm trong nhóm dẫn đầu. Từ 41 nghi ngờ → sửa 57
> dòng → còn 12, đã rà tay và đăng ký vào `glossary_da_duyet`.

### Kết quả đợt 12

| | Số lượng |
|---|---|
| Khẳng định đã đối chiếu | **5** |
| ⚠ Phát hiện sai, đã sửa | 3 *(gồm **57 dòng** ở Phụ lục F và 1 lỗi tự tạo)* |
| ➕ Bổ sung nội dung còn thiếu | 2 |
| ⭐ Luật kiểm mới | **GLOS** |

> ⭐⭐ **Bài học lớn nhất của cả 12 đợt, rút ra ở đây: tôi tin vào bản đồ chương trong đầu mình suốt
> nhiều phiên mà chưa một lần đối chiếu với tiêu đề chương thật.**
>
> Cùng loại sai lầm với đợt 2 (khai "không có tài liệu CODESYS" mà chưa quét hết thư mục). ⭐ **Thứ
> mình tưởng đã biết là chỗ ít được kiểm nhất** — và vì thế là chỗ sai lâu nhất.

---

## Đợt 13 — 2026-09-03 · Quét lỗi số chương ra TOÀN BỘ phụ lục

⭐ **Đợt 12 sửa Phụ lục F. Đợt này hỏi câu tiếp theo đúng đắn: các phụ lục khác có cùng bệnh không?**
Có — lan ra **bảy phụ lục và ba chương**.

| # | Nơi | Lỗi | KQ |
|---|---|:--|:--:|
| 60 | Phụ lục E (14 dòng) | Ch.43 (vision) dùng cho **báo động** → 44 · Ch.32 dùng cho **công thức** → 29 · Ch.24 (đại số Boolean) dùng cho **đọc/sửa chương trình** → 22 · Ch.12 (IO-Link) dùng cho **bộ nhớ giữ được** → 11 · Ch.5 (cơ cấu điện) dùng cho **khí nén** → 6 · Ch.21 dùng cho **trình tự/timeout** → 26 | ⚠ |
| 61 | Phụ lục K (5) | **Lực xy-lanh · lưu lượng khí** dẫn Ch.5 → **6** · **thời gian quét** dẫn Ch.7, 19 → **10** · kiểu dữ liệu dẫn Ch.14 → **11, 19** | ⚠ |
| 62 | Phụ lục B (2) | `R_TRIG` / `F_TRIG` dẫn Ch.11 → **16** | ⚠ |
| 63 | Phụ lục C (1) | "Viết chương trình" dẫn Ch.24 → **22** | ⚠ |
| 64 | Phụ lục H (4) | ISO 12100 dẫn Ch.6 → bỏ · IEC 61131-1/-2 dẫn Ch.7 → **8, 10** · ISO 4414 dẫn Ch.5 → **6** · IEC 62682 dẫn Ch.43 → **44** | ⚠ |
| 65 | Phụ lục I (3) | Báo động dẫn Ch.43 → **44** | ⚠ |
| 66 | Ch.53, 55, 56 + A1 (7) | *"Chương 12 về vùng nhớ giữ được"* — Ch.12 là **IO-Link**, đúng là **Ch.11** | ⚠ |
| 67 | Phụ lục K, A2, E (3) | Ngưỡng phát hiện 4–20 mA dẫn **mục 31.7** (là "Trên máy mẫu DP-01") → **31.3** | ⚠ |
| 68 | Ch.33, Ch.42 | Cùng dẫn 31.7 — ⭐ **KIỂM RA LÀ ĐÚNG**: §31.7 thật sự bàn quyết định 0–10 V của `AI_UvIntensity` | ✅ |

### Kết quả đợt 13

| | Số lượng |
|---|---|
| Nơi đã kiểm | **9** |
| ⚠ Sai, đã sửa | 8 nhóm — **39 dẫn chiếu** |
| ✅ Kiểm ra đúng, giữ nguyên | 1 |

> ⭐⭐ **Cùng một nguyên nhân gốc với đợt 12, và đó mới là điều đáng ghi:** tôi viết mọi phụ lục bằng
> **một bản đồ chương sai trong đầu**, nên lỗi không nằm ở một file — nó nằm ở **mọi file tôi viết
> trong giai đoạn đó**.
>
> ⭐ **Bài học quy trình:** khi tìm ra một lỗi có nguyên nhân là "hiểu sai nền", ⚠ **đừng sửa chỗ tìm
> thấy rồi dừng** — phải hỏi *"cái hiểu sai đó còn chảy vào đâu nữa?"* và quét hết.
>
> ⚡ Và mục 68 cho thấy vì sao vẫn phải kiểm từng cái: hai dẫn chiếu **trông giống lỗi** nhưng đúng.
> Sửa hàng loạt theo mẫu mà không đọc ngữ cảnh sẽ **tạo ra lỗi mới**.

---

## Đợt 14 — 2026-09-03 · Ch.34 (cân & lực), Ch.42 (mã 2D), Ch.38 (RS-485)

| # | Chương · chủ đề | Việc đã làm | KQ |
|---|---|:--|:--:|
| 69 | Ch.34 — đơn vị **mV/V** | Kuphaldt xác nhận: cầu **mất cân bằng** thì điện áp kích **có ảnh hưởng** *("In an unbalanced bridge circuit, however, source voltage value matters!")* → mV/V tồn tại vì ngõ ra tỉ lệ với kích | ✅➕ |
| 70 | Ch.34 — vì sao **bốn** tem biến dạng | Kuphaldt: cấu hình cầu **triệt tiêu ảnh hưởng nhiệt độ** | ✅➕ |
| 71 | Ch.34 — **từ biến** *(creep)* | ⚠ Bộ tài liệu **không phủ** → tra ngoài, ghi ngày, **hạ giọng**: đặc tả %FSO/~30 phút, con số lấy từ datasheet | ❔➕ |
| 72 | Ch.34 — **đặt lệch tâm** | ⚠ Không phủ → tra ngoài. ⭐ Chốt điểm đắt nhất: **sai số cơ khí, hiệu chuẩn điện không sửa được** | ❔➕ |
| 73 | Ch.42 — **vùng yên tĩnh** | ⚠ `tra_nguon` trả **rỗng** cho `quiet zone` → tra ngoài: ISO/IEC 16022 tối thiểu **1 ô** bốn phía; GS1 khuyến nghị **2–4 ô** khi nhiễu. ⚠ **Không dẫn số điều khoản** | ❔➕ |
| 74 | Ch.42 — **kích thước ô** *(X-dimension)* | ⚠ Không phủ → tra ngoài. ⭐ Viết theo nguyên lý (điểm ảnh trên mỗi ô), ⚠ **con số tối thiểu để datasheet đầu đọc trả lời** | ❔➕ |
| 75 | Ch.38 — **1200 m** và tốc độ | Kuphaldt §15.6 xác nhận: khuyến nghị **1200 m**, ⭐ **tốc độ tối đa tỉ lệ nghịch với chiều dài** | ✅➕ |
| 76 | Ch.38 — **điện trở đầu cuối đổi được tốc độ** | Kuphaldt dẫn thí nghiệm Texas Instruments: cùng cáp 30 m — **200 kbps** không có, **1 Mbps** khi có | ✅➕ |
| 77 | Ch.38 — 1200 m có phải tường cứng | Kuphaldt chú thích: Park, Mackay & Wright ghi nhận mạng **5 km ở 1200 bps** → ⭐ **1200 m là một điểm trên đường đánh đổi** | ✅➕ |
| 78 | Thuật ngữ — *cross-reference* | Chú tiếng Anh xuất hiện ở 3 chương với 3 cụm khác nhau → ⭐ **chỉ chú một lần ở lần dùng đầu** (Ch.15), Ch.19 và Ch.25 bỏ chú | ⚠ |

### Kết quả đợt 14

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **10** |
| ✅➕ Nguồn xác nhận **và** bổ sung nội dung mới | 5 |
| ❔➕ ⚠ **Nguồn không phủ** — tra ngoài, ghi ngày, hạ giọng | 4 |
| ⚠ Sai, đã sửa | 1 |
| Mục mới thêm vào sách | **§34 (mV/V)** · **§42.2b** · **§38.3b** + 15 dòng Bảng chốt + 10 câu Tự kiểm |

> ⭐⭐ **Điều đáng ghi của đợt này: bốn trên mười khẳng định KHÔNG có nguồn nội bộ.**
>
> Cả bốn đều là kiến thức "ai làm nghề cũng biết" — từ biến, đặt lệch tâm, vùng yên tĩnh, kích thước
> ô. ⚠ **Chính loại kiến thức đó là chỗ dễ viết sai nhất mà không ai phát hiện**, vì nó nghe quá hiển
> nhiên để đi kiểm.
>
> ⭐ Cách xử lý đã theo đúng quy tắc của kỹ năng `doi-chieu-nguon`: ❔ **không được tính là xác nhận**.
> Bốn mục trên vào sách với **con số tối thiểu**, kèm câu chỉ người đọc về **bản gốc đặc tả** và
> **datasheet của chính thiết bị họ mua** — thay vì chép một con số tôi không kiểm được.
>
> ⚡ Mục 78 là loại lỗi mà **chỉ máy tìm ra**: ba cách gọi cùng một thứ, nằm ở ba chương cách xa nhau,
> không người đọc nào bắt được — nhưng `kiem_nhat_quan.py` thì có.

---

## Đợt 15 — 2026-09-03 · Ch.19 và Ch.11 — ⚠⚠ SỬA MỘT LỜI KHUYÊN SAI

⭐⭐ **Đợt này bắt đầu bằng một sai lầm của chính quy trình, đáng ghi lại.**

Tôi quét từ khoá để tìm *khái niệm còn thiếu* ở Ch.11 và Ch.19, và bảng quét báo **"thiếu ép kiểu,
thiếu chỉ số mảng"**. ⚠ **Sai** — cả hai đều đã có, chỉ là nằm ở chương kia và viết bằng từ khác từ
tôi grep. ⭐ **Quét từ khoá đo được cái tôi nghĩ ra, không đo được cái sách có.**

Nên tôi đổi câu hỏi: thay vì *"còn thiếu gì"*, hỏi *"cái đang có đã ĐÚNG chưa"*. Câu hỏi đó ra kết quả
ngay.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 79 | Ch.19 §19.5 — chia cho 0 | Bảng cũ có **3 hành vi**. Nguồn cho thấy có ít nhất **5** — thiếu *cờ lỗi nhẹ* (Petruzella) và ⚠⚠ *tự thay mẫu số bằng 1 rồi chạy tiếp* (Inovance H5U §6.1.9.1, báo bằng **đèn LED nhấp nháy Er50/Er81**) | ⚠➕ |
| 80 | ⚠⚠ Ch.19 — **lời khuyên phòng tránh SAI với `REAL`** | Sách viết *"bọc bằng phép kiểm khác 0"*. ⚠ **Chưa đủ**: số thực có thể khác 0 nhưng cực nhỏ. Tài liệu InoProShop chỉ rõ phải so với **ngưỡng** — **1e-6** (32 bit), tới **1e-15** (64 bit) | ⚠⚠ |
| 81 | Ch.19 — ba nguyên nhân mẫu số bằng 0 | InoProShop: biến **chưa khởi tạo** · biến **khởi tạo sau khi bị gọi** · ⭐ biến **toàn cục ghi ở nhiều tác vụ/POU** (khó tái hiện nhất) | ➕ |
| 82 | Ch.19 — công cụ tìm chỗ chia cho 0 | CODESYS có *"POU for implicit checks" → Division Checks*, sinh `CheckDivInt`/`CheckDivReal`… ⭐ Đặt điểm dừng ở đó là cách nhanh nhất định vị | ➕ |
| 83 | Ch.19 Bẫy 7 + Ch.11 Bẫy 6 — chỉ số mảng | Sách nói 2 hậu quả (STOP · ghi đè). Inovance §6.1.9.2: có hệ ⚠⚠ **kẹp im lặng** — vượt trên vào phần tử cuối, vượt dưới vào phần tử 0, **không dừng, không báo** | ⚠➕ |
| 84 | Phụ lục K §K.6 | Thêm dòng ngưỡng cho mẫu số số thực — quét cả sách, ⭐ **không còn chỗ nào khác** khuyên "kiểm khác 0" thiếu vế | ➕ |

### Kết quả đợt 15

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **6** |
| ⚠⚠ **Lời khuyên sai, đã sửa** | 1 |
| ⚠➕ Thiếu hành vi quan trọng, đã bổ sung | 2 |
| ➕ Bổ sung mới có nguồn | 3 |
| Nơi đã sửa | Ch.19 (bảng · code · 2 mục mới · Bảng chốt · 3 câu Tự kiểm · nguồn) · Ch.11 (2 chỗ) · Phụ lục K |

> ⚠⚠ **Mục 80 là lỗi nặng nhất tìm được từ đầu quy trình tới giờ, vì nó là lời khuyên chứ không phải
> thông tin.** Người đọc làm đúng theo sách vẫn dính lỗi. Một khẳng định sai thì người đọc còn có thể
> nghi ngờ; ⭐ **một lời khuyên sai thì họ làm theo.**
>
> ⭐⭐ **Chủ đề chung của cả đợt — "tự xử lý" là bẫy.** Ba chỗ độc lập trong tài liệu hãng cho thấy hệ
> **tự sửa lỗi rồi chạy tiếp**: thay mẫu số bằng 1, kẹp chỉ số mảng, và (đã có từ trước) giá trị thay
> thế của analog. ⚠ Cả ba **biến một lỗi ồn ào thành một lỗi im lặng** — và lỗi im lặng đắt hơn nhiều.
> Sách nay nói thẳng nguyên tắc đó ở Ch.19 và nối nó với Ch.31 và Ch.38.
>
> ⚡ **Bài học quy trình:** quét từ khoá tìm *thiếu* đã hết tác dụng — nó chỉ tìm được cái tôi nghĩ ra.
> Từ đây, ⭐ **đọc cái đang có và hỏi nó có đúng không** là cách còn tìm ra lỗi.

---

## Đợt 16 — 2026-09-03 · Ch.17 (timer) — ⚠⚠ SỬA XONG MỘT CHỖ MÀ QUÊN CHỖ DẠY NÓ

⭐⭐ **Đợt 1 (mục 3) đã sửa Phụ lục A2: độ phân giải bộ định thời Mitsubishi đến từ HAI nguồn — lệnh
(`OUT`/`OUTH`/`OUTHS`) và kiểu thiết bị `T`.** Đợt này đọc lại Ch.17 §17.7 và thấy nó ⚠ **vẫn nói
mỗi nguồn "số hiệu thiết bị"** — tức là ⚠⚠ **bản sai vẫn nằm nguyên ở chương dạy khái niệm đó**, còn
bản đúng thì nằm trong phụ lục tra cứu.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 85 | Ch.17 §17.7 mục 1 | Viết lại: nêu **hai nguồn**, thêm bảng và ⭐ ba dòng `OUT`/`OUTH`/`OUTHS` cùng `K20` cho **2,0 s / 0,2 s / 0,02 s** — chênh **100 lần**, code trông y hệt | ⚠ |
| 86 | Ch.17 §17.7 bảng 5 hệ | Ô "Viết hằng số thời gian" của Mitsubishi: *"độ phân giải của thiết bị"* → *"do **lệnh và thiết bị** quyết định"* | ⚠ |
| 87 | Ch.17 §17.8 / §17.9 | Thêm 1 dòng danh mục kiểm và 1 câu Tự kiểm về hai nguồn độ phân giải | ➕ |
| 88 | Quét cả sách | ⭐ **Không còn chỗ nào khác** mang khẳng định thiếu vế này | ✅ |

### Kết quả đợt 16

| | Số lượng |
|---|---|
| Nơi đã kiểm | **4** |
| ⚠ Sai, đã sửa | 2 |
| ➕ Bổ sung | 1 |
| ✅ Quét sạch, không còn chỗ khác | 1 |

> ⚠⚠ **Đây là biến thể mới của bài học đợt 12–13, và nó khó thấy hơn.**
>
> Đợt 12–13: *một hiểu sai chảy vào nhiều file* → phải quét hết.
> Đợt này: ⭐ **một hiểu sai ĐÃ ĐƯỢC SỬA ở một file, nhưng bản sai vẫn sống ở file khác** — và file
> còn sai lại chính là ⚠⚠ **chỗ người đọc học khái niệm lần đầu**, còn chỗ đã đúng chỉ là bảng tra.
>
> ⭐⭐ **Bài học quy trình bổ sung:** khi sửa một khẳng định, ⚠ **câu hỏi tiếp theo không phải "còn chỗ
> nào sai nữa không"** — mà là ⭐ **"chương nào DẠY cái này? nó đã được sửa chưa?"** Phụ lục sửa dễ vì
> ngắn; chương dạy mới là chỗ quan trọng, và cũng là chỗ dễ quên.
>
> ⚡ Nhật ký đối chiếu đã giúp bắt được lỗi này — mục 3 của đợt 1 ghi rõ đã sửa *"A2.2"*, không phải
> *"cả sách"*. ⭐ **Ghi cụ thể mình đã sửa ở ĐÂU, chứ không ghi "đã sửa", là thứ làm nên giá trị của
> nhật ký.**

---

## Đợt 17 — 2026-09-03 · Ch.16, Ch.18 — "giữ được" là thuộc tính của LỆNH, không chỉ của biến

⭐ Đọc §16.7 để kiểm khẳng định nặng nhất của chương — *"máy tự chạy lại khi có điện trở lại, thứ mà
IEC 60204-1 cấm"*. Khẳng định đó **đúng**, nhưng cơ chế sách nêu thì ⚠ **chưa đủ chính xác**.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 89 | Ch.16 §16.7 — Rockwell | Sách nói *"giá trị tag được giữ mặc định"*. Petruzella cho thấy điểm quyết định là **lệnh**: `OTE` **không giữ**, `OTL`/`OTU` **giữ được**. ⭐ Ở Logix, "cách bit đổi giá trị" và "bit sống qua mất điện không" ⚠ **KHÔNG tách rời** — khác hẳn mô hình IEC | ⚠➕ |
| 90 | Ch.16 Bẫy 7 | Câu *"SET/RESET không tự động giữ qua mất điện"* ⚠ **đúng với hệ IEC nhưng sai với `OTL`/`OTU`** — đã thêm ngoại lệ | ⚠ |
| 91 | ⭐ Quét gốc: Ch.15, Phụ lục A1 | Ch.15 bảng lệnh ladder mang **cùng** khẳng định thiếu vế; A1.6 ô Rockwell ghi *"thuộc tính của tag"*. ⭐ **Đã sửa cả hai** | ⚠ |
| 92 | Ch.18 §18.6 — bộ đếm | Sách chỉ nói cách **làm cho** bộ đếm giữ được. Petruzella: ⭐ bộ đếm PLC **thường ĐÃ giữ sẵn** — giá trị lúc CPU dừng được khôi phục khi cấp nguồn lại. ⚠⚠ Rủi ro thật là **giữ ngoài ý muốn**, không phải mất số liệu | ⚠➕ |
| 93 | Ch.18 — ngoại lệ lúc khởi động | Petruzella: bộ đếm ⚠ **bị xoá nếu điều kiện đặt lại đang tác động lúc cấp nguồn lại** — số liệu tưởng còn thì không còn | ➕ |
| 94 | Ch.18 — cực tính chân đặt lại | Petruzella: ⭐ **có hãng cần nấc đặt lại ĐÚNG, có hãng cần SAI**, và khuyến cáo tra sổ tay trước khi lập trình. Chuyển hệ mà không biết → xoá liên tục hoặc không bao giờ xoá, ⚠ **cả hai đều im lặng** | ➕ |

### Kết quả đợt 17

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **6** |
| ⚠ Sai / thiếu vế, đã sửa | 4 nơi (Ch.16 ×2, Ch.15, A1.6) |
| ➕ Bổ sung mới có nguồn | 3 |
| Mục mới | **§18.6b** + 6 dòng Bảng chốt + 3 câu Tự kiểm + nguồn Petruzella cho Ch.16 và Ch.18 |

> ⭐⭐ **Bài học đợt 16 đã phát huy tác dụng ngay.** Đợt 16 rút ra: *sửa một khẳng định thì phải hỏi
> "chương nào DẠY cái này"*. Đợt này áp dụng ngược lại và cũng đúng: tìm ra lỗi ở **chương dạy**
> (Ch.16) rồi quét ra **hai nơi khác** đang chép lại nó (Ch.15, A1.6). ⭐ Quét gốc nay là bước mặc
> định, không còn là việc nhớ ra thì làm.
>
> ⚡ **Điểm chung của cả hai phát hiện chính:** sách mô tả **mô hình IEC** rồi ngầm coi nó là phổ quát.
> Nhưng hệ kiểu thiết bị và hệ Rockwell ⚠ **gộp những thứ mà IEC tách ra** — độ phân giải gộp vào
> lệnh (đợt 16), tính giữ được gộp vào lệnh (đợt này). ⭐ **Chỗ nào sách nói "hai chuyện tách rời" là
> chỗ đáng nghi ngờ nhất khi đối chiếu hệ khác.**

---

## Đợt 18 — 2026-09-03 · Ch.51 (xử lý sự cố) — cưỡng bức ngõ VÀO ≠ cưỡng bức ngõ RA

⭐ Đợt này kiểm mục nguy hiểm nhất của Ch.51: **cưỡng bức I/O**. Sách đã cảnh báo đúng và đủ mạnh về
rủi ro, nhưng ⚠ **mô tả cưỡng bức như MỘT thao tác** — trong khi nó là **hai thao tác có cơ chế khác
hẳn nhau**.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 95 | Ch.51 §51.7 — cơ chế cưỡng bức | Petruzella §9.6: ép ngõ **vào** tác động vào **bảng ảnh ngõ vào** → ⚠⚠ **lan tới MỌI chỗ dùng bit đó**; ép ngõ **ra** chỉ tác động **đúng chân ra**, ⭐ **bảng ảnh ngõ ra không đổi** → chương trình chạy y như cũ | ➕➕ |
| 96 | Ch.51 — hệ quả thực tế | ⭐ Hệ quả đắt nhất: **cưỡng bức ngõ VÀO nguy hiểm hơn ngõ RA**, dù nghe thì ngược lại — ép ngõ ra chỉ làm một cơ cấu chạy, ép ngõ vào làm cả chương trình tin vào thế giới không có thật, ⚠ **kể cả các nấc liên động** | ➕ |
| 97 | Ch.51 — hiện tượng hay gây bối rối | *"Tôi ép ngõ ra rồi mà đèn báo trên màn hình vẫn tắt"* — ⭐ **đúng thiết kế**: màn hình đọc bảng ảnh, cưỡng bức chỉ chạm chân ra | ➕ |
| 98 | Ch.51 — cài vs bật | Tài liệu cho thấy có hệ phân biệt **"đã cài cưỡng bức"** với **"đã bật cưỡng bức"** — hai trạng thái riêng. ⚠⚠ **Tắt không phải là gỡ**: lần bật sau, cưỡng bức cũ sống lại | ➕ |
| 99 | ⭐ Quét gốc: Ch.52, Phụ lục D | Ch.52 danh mục nghiệm thu và Phụ lục D checklist đều nói *"không còn cưỡng bức"* — ⭐ đã sửa thành **"GỠ, không phải tắt"** và **"kể cả loại đã cài mà đang tắt"** | ⚠ |
| 100 | Ch.52 Bẫy 2 | Cơ chế mới **củng cố** lập luận sẵn có: ⭐ cưỡng bức ngõ **ra** đúng là công cụ kiểm dây, chính vì nó **không** làm nhiễu logic — đã thêm giải thích và cảnh báo không dùng ngõ **vào** cho việc này | ➕ |

### Kết quả đợt 18

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **6** |
| ➕ Bổ sung mới có nguồn | 4 |
| ⚠ Sửa cho chặt hơn | 2 nơi (Ch.52, Phụ lục D) |
| Nơi đã sửa | Ch.51 (mục mới + 1 dòng quy trình + 1 dòng Bảng chốt + 3 câu Tự kiểm + nguồn) · Ch.52 ×2 · Phụ lục D |

> ⭐⭐ **Đây là loại phát hiện khác với các đợt trước: sách không SAI, sách THIẾU một phân biệt.**
>
> Mọi câu trong §51.7 đều đúng. Nhưng vì gộp hai thao tác làm một, người đọc ⚠ suy ra một mô hình tinh
> thần sai — và mô hình sai đó dẫn tới hai lỗi ngược chiều nhau: **ép ngõ ra rồi chờ logic phía sau
> chạy theo** (không xảy ra), và **ép ngõ vào để "thử một đoạn nhỏ"** (nó lan ra cả chương trình, kể
> cả liên động).
>
> ⚡ **Bài học quy trình:** câu hỏi *"chỗ này có đúng không"* chưa đủ. Phải hỏi thêm ⭐ *"người đọc sẽ
> DỰNG mô hình gì trong đầu từ đoạn này, và mô hình đó có đúng không"*. Một đoạn toàn câu đúng vẫn có
> thể tạo ra một mô hình sai.

---

## Chương CHƯA được đối chiếu

⚠ **Đây là phần quan trọng nhất của nhật ký.** Chương không có trong bảng trên nghĩa là **chưa ai
kiểm**, không phải "không có lỗi".

| Nhóm | Chương | Nguồn sẵn có | Ưu tiên |
|---|---|---|---|
| ⚠⚠ **An toàn** | ⭐ **Đã đối chiếu hết** — 3, 6, 47, 48, Phụ lục D (đợt 1, 3, 4, 7). ⚠ Cờ ⚠ vẫn giữ | SICK ×3, Schneider, DGUV/IFA, PPSA | ⭐⭐ **Cao nhất** |
| Đo lường & analog | ⭐ **Đã đối chiếu** (đợt 5–7, 14) | — | — |
| Truyền thông | ⭐ **Đã đối chiếu** (đợt 3, 8, 14) | — | — |
| Chuyển động | ⭐ **Đã đối chiếu** (đợt 9) | — | — |
| Nền tảng PLC | 7, 12, 14 *(8, 9, 18 đợt 4, 10; **11, 19 đợt 15**)* | Hugh Jack, AutomationDirect, Siemens/Rockwell | Vừa |
| Ngôn ngữ | 15, 20, 21 *(17 đợt 16; **16 đợt 17**)* | Hugh Jack, Rockwell PM006/007/008/009 | Vừa |
| Thiết kế | 22–30 | ⭐ Hugh Jack (mạnh nhất mảng này) | Vừa |
| Chẩn đoán & vận hành | 43, 49, 53, 55 *(**51, 52 đã đối chiếu đợt 18**)* | Kuphaldt (ch. chẩn đoán), IEC 62381 | Vừa |
| Không kiểm được bằng nguồn | 1, 2, 13, 23–29, 54, 56, 57, 58 | — | ⭐ Chủ yếu là phương pháp và kinh nghiệm nghề |

---

## ⚠ Chỗ bộ tài liệu KHÔNG phủ

⭐ **Biết nguồn thiếu ở đâu quan trọng ngang biết nó có gì.** Khẳng định thuộc các mảng dưới đây
**không được xác nhận bằng bộ tài liệu nội bộ** — phải tra ngoài và ghi ngày.

> ⚠⚠ **ĐÍNH CHÍNH (đợt 2, 2026-09-02).** Đợt 1 kết luận "không có tài liệu CODESYS và Inovance".
> ⭐ **Kết luận đó SAI** — tôi chỉ quét `PLC/reference/` mà bỏ qua thư mục cha `PLC/`, nơi có:
> `en/` (tài liệu InoProShop nền CODESYS) và `Manual/` (H5U, H3U, AutoShop — bản tiếng Anh và
> tiếng Trung), cộng sách Hanssen về IEC 61131-3 dùng CoDeSys, Petruzella, Rabiee.
>
> ⭐ **Bài học về quy trình:** kết luận "không có nguồn" phải được kiểm kỹ như kết luận "có nguồn".
> Công cụ `tra_nguon.py` đã được sửa để quét **toàn bộ** cây `PLC/` (112 tài liệu thay vì 44).

| Mảng | Hệ quả với sách |
|---|---|
| ⚠⚠ **Bản gốc tiêu chuẩn ISO/IEC** | Chỉ có tài liệu diễn giải của hãng → ⚠ **không được dẫn số điều khoản** ở bất kỳ chương nào |
| Thị trường thiết bị hiện hành | Hai giả định của máy mẫu (đầu đọc mã 2D Ethernet · bộ điều khiển nhiệt rời RS-485) vẫn **chưa xác minh** — Phụ lục J §J.9 |
| ⚠ IO-Link System Description | ⭐ **File PDF trong bộ không trích được text** — nếu cần đối chiếu Ch.12 phải mở tay |

---

> ⚠⚠ **Nhắc lại giới hạn của cả nhật ký này.**
>
> Đối chiếu với tài liệu **không** thay thế việc chuyên gia duyệt. Với Ch.3, 6, 47, 48 và Phụ lục D,
> kết luận đúng nhất mà bảng trên cho phép là: ⭐ *"đã đối chiếu với tài liệu diễn giải X, không thấy
> mâu thuẫn"* — ⚠ **không phải** *"đã kiểm, an toàn"*.
>
> Cờ ⚠ trên các chương đó ⭐ **chỉ chuyên gia an toàn người thật gỡ được**.
