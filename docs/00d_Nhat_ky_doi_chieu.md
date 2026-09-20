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

## Đợt 19 — 2026-09-03 · Ch.20 (ST) — vòng lặp thứ ba, và nguyên tắc sách chưa phát biểu

⭐ §20.5 là mục có cảnh báo ⚠⚠ mạnh nhất chương. Nội dung **đúng**, nhưng đối chiếu Hanssen §11.8 cho
thấy nó ⚠ **thiếu một vòng lặp, thiếu một nguyên tắc, và bỏ ngỏ một lối thoát mà người đọc chắc chắn
sẽ nghĩ tới**.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 101 | Ch.20 §20.5 — thiếu `REPEAT` | Chuẩn có **ba** vòng lặp; Ch.20 chỉ dạy `FOR` và `WHILE`. ⚠ **Phụ lục B đã có `REPEAT`, chương dạy thì không** — đúng mẫu lỗi đợt 16 | ⚠➕ |
| 102 | Ch.20 — hai bẫy riêng của `REPEAT` | Hanssen: chạy **CHO TỚI KHI** điều kiện đúng (⚠ ngược cực tính với `WHILE`), và thân vòng ⭐ **luôn chạy ít nhất một lần** | ➕ |
| 103 | ⭐⭐ Ch.20 — nguyên tắc tổng quát | Hanssen: rủi ro vòng lặp vô hạn ⭐ **lớn nhất khi điều kiện thoát phụ thuộc thứ BÊN NGOÀI**; nên dùng điều kiện phụ thuộc biến **cập nhật bên trong vòng lặp**. ⭐ Nguyên tắc này giải thích cả ba ví dụ của sách bằng **một câu** — sách chưa từng phát biểu nó | ➕➕ |
| 104 | Ch.20 — lối thoát bỏ ngỏ | Người đã đọc Ch.10 sẽ nghĩ: *dùng **truy cập trực tiếp** thì vòng lặp thoát được*. ⭐ **Đúng kỹ thuật, tệ hơn về hậu quả** — CPU đứng chờ vài trăm ms, ⚠⚠ **nút dừng không được đọc**. Đã viết hẳn ra và bác bỏ | ➕ |
| 105 | Ch.20 — `EXIT` và `CONTINUE` | Hanssen: `EXIT` ở vòng trong ⚠ **không dừng vòng bao ngoài**. ⭐ `CONTINUE` không thoát vòng lặp nên **không phải van an toàn** | ➕ |
| 106 | ⭐ Quét gốc: Phụ lục B | Thêm **phép kiểm một câu** và hai điểm khác biệt của `REPEAT` vào bảng tra nhanh | ➕ |

### Kết quả đợt 19

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **6** |
| ➕➕ Nguyên tắc mới, giá trị cao nhất | 1 |
| ➕ Bổ sung có nguồn | 4 |
| ⚠➕ Thiếu nội dung, đã bổ sung | 1 |
| Nơi đã sửa | Ch.20 (3 mục mới + cú pháp + 4 dòng Bảng chốt + 3 câu Tự kiểm + nguồn) · Phụ lục B |

> ⭐⭐ **Mục 103 là kiểu bổ sung đáng giá nhất mà đối chiếu nguồn mang lại: không phải một sự kiện mới,
> mà một NGUYÊN TẮC gói gọn những gì sách đã dạy rời rạc.**
>
> Sách đã có ba lời khuyên đúng — đừng chờ trong vòng lặp, `FOR i := 0 TO n` với `n` tính ra là rủi
> ro, `EXIT` không cứu được `WHILE` chờ tín hiệu. ⚠ Nhưng ba lời khuyên rời nhau thì người đọc phải
> **nhớ ba thứ**, và không suy ra được trường hợp thứ tư.
>
> ⭐ Nguyên tắc của Hanssen — *điều kiện thoát phải phụ thuộc biến cập nhật bên trong vòng lặp* — biến
> cả ba thành **hệ quả của một câu**, và cho người đọc một **phép kiểm áp được vào vòng lặp chưa từng
> gặp**.
>
> ⚡ **Bài học quy trình:** đối chiếu nguồn không chỉ để **bắt lỗi**. Nguồn tốt còn cho **cách tổ chức
> lại cái đã đúng** — và đó là thứ ⚠ ba bộ kiểm tự động không bao giờ tìm ra được.

---

## Đợt 20 — 2026-09-03 · Ch.15 — ⚠⚠ bảng 4 tổ hợp không nói giới hạn của chính nó

⭐ §15.3 là một trong những mục viết tốt nhất sách: bảng 4 tổ hợp NO/NC, tổ hợp 2 "giết người", quy
tắc *tiếp điểm vật lý NC + lệnh `┤ ├`*. ⭐ **Mọi câu đều đúng.**

⚠⚠ Nhưng cả bảng được xây trên **một kiểu hỏng duy nhất — mạch bị HỞ** — và nó ⚠ **không nói ra điều
đó**. Người đọc rời mục 15.3 với kết luận *"NC + `┤ ├` = an toàn"*, chấm hết.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 107 | ⚠⚠ Ch.15 §15.3 — phạm vi của bảng | Thêm mục nêu **hai lớp hỏng**: HỞ (đứt dây, tuột cốt) → bit 0 → tổ hợp 3 xử lý được; ⚠⚠ **CHẬP** (chạm dây, chập 24 V, **tiếp điểm hàn dính**) → bit **kẹt ở mức bình thường** → ⚠ tổ hợp 3 **KHÔNG** xử lý được | ⚠⚠➕ |
| 108 | Ch.15 — nối vào cơ chế đã có | ⭐ Bảng 4 tổ hợp là điều kiện **CẦN, không phải ĐỦ**. Ba cơ chế chống hỏng kiểu chập **đã có sẵn trong sách**: tiếp điểm dẫn động cưỡng bức (3.5), hai kênh + kiểm chéo (47), xung kiểm tra OSSD (47.7) — ⭐ nay được nối lại thành một mạch lập luận | ➕ |
| 109 | Ch.15 — phép kiểm nhanh | Thêm câu hỏi thứ tư: *"nếu tín hiệu này **kẹt ở mức bình thường** thì sao?"* — nếu đáp án là *"máy sẽ không dừng"* thì ⭐ **đây là chức năng an toàn**, nấc thang không đủ | ➕ |
| 110 | Ch.48 §48.4 | ⚠ Bảng NO/NC ở Ch.48 mang **cùng phạm vi ngầm**. Đã thêm ghi chú phạm vi — ⭐ **chỉ dẫn chiếu, không thêm quy định an toàn mới** | ⚠➕ |
| 111 | ⭐ Quét gốc | Ch.3, Ch.4, Ch.16, Ch.48, `case_study`, Phụ lục C — ⭐ **không nơi nào khác trình bày bảng này như điều kiện đủ**; Ch.4 là bảng PNP/NPN khác hẳn, không liên quan | ✅ |

### Kết quả đợt 20

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **5** |
| ⚠⚠➕ Phạm vi ngầm nguy hiểm, đã nêu rõ | 1 |
| ➕ Bổ sung / nối lại lập luận | 3 |
| ✅ Quét sạch | 1 |
| Nơi đã sửa | Ch.15 (mục mới + phép kiểm + 2 câu Tự kiểm + nguồn) · Ch.48 (ghi chú phạm vi) |

> ⚠⚠ **ĐIỂM CẦN CHUYÊN GIA AN TOÀN XEM — ghi lại để không quên.**
>
> ⭐ Nội dung thêm ở đợt này **siết chặt** chứ không nới lỏng: nó nói bảng 4 tổ hợp **hẹp hơn** người
> đọc tưởng, và đẩy chức năng an toàn về Chương 47. Đó là hướng an toàn hơn, và mọi cơ chế được dẫn
> đều **đã có sẵn trong sách**, không có quy định mới nào do tôi tự đặt ra.
>
> ⚠ Nhưng §15.3 là mục **kê đơn cách đấu nút Dừng**, nên nó thuộc phạm vi cần người thật duyệt — ngang
> với Ch.3, 6, 47, 48. ⭐ **Đề xuất: đưa Ch.15 §15.3 vào danh sách chờ chuyên gia an toàn.** Quyết định
> này thuộc về chủ dự án, không phải công cụ.

> ⭐⭐ **Đây là biến thể sâu nhất của bài học đợt 18** — *"người đọc dựng mô hình gì trong đầu"*.
>
> Đợt 18: sách gộp hai thao tác làm một. ⭐ Đợt này nặng hơn: sách trình bày một bảng **hoàn chỉnh và
> thuyết phục** đến mức chính sự hoàn chỉnh đó ⚠⚠ **làm người đọc ngừng hỏi tiếp**. Một bảng có đủ
> bốn hàng, có hàng ✅ và hàng ❌, đọc như thể nó đã vét hết mọi khả năng.
>
> ⚡ **Câu hỏi nên hỏi ở mọi bảng "đầy đủ" trong sách:** ⭐ *"bảng này ngầm giả định điều gì, và nó
> có nói ra giả định đó không?"*

---

## Đợt 21–22 — 2026-09-03 · Ch.21 (SFC/FBD) và Ch.14 (POU) — Hanssen

⭐ Hai đợt gộp chung vì cùng một nguồn (**Hanssen**, *IEC 61131-3 using CoDeSys*) và cùng một kiểu
phát hiện: ⚠ **sách bỏ sót những thứ chuẩn CÓ**, chứ không phải nói sai những thứ chuẩn không có.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 112 | ⭐⭐ Ch.21 §21.3 — biến của bước SFC | Hanssen §12.3.1: mỗi bước tự có **`TênBước.X`** (BOOL) và ⭐⭐ **`TênBước.T`** (TIME) — **timer nội, tự chạy khi vào bước, tự về `t#0s` khi rời**. Cả hai **chỉ đọc** | ➕➕ |
| 113 | Ch.21 — nối với Ch.17 | ⭐ Ch.17 §17.4 dạy mỗi bước chờ phải có timeout, ở LD/ST là **một `TON` cho từng bước**. Trong SFC ⭐ **không phải khai gì** — và `.T` tự về 0, tránh đúng lỗi quên đặt lại (Ch.17 Bẫy 2) | ➕ |
| 114 | Ch.21 — bổ ngữ hành động | Sách chỉ có `N`/`S`/`R`. Hanssen bảng 12.2: thêm ⭐ **`P`** (một lần mỗi lần vào bước) · **`L`** (tự dừng sau khoảng) · **`D`** (bắt đầu sau khoảng) — ⭐ mỗi cái **thay được một khối chức năng** | ➕ |
| 115 | ⚠⚠ Ch.21 §21.2 — thứ tự thực thi FBD | Tiêu đề mục nói *"luồng tín hiệu đi từ trái sang phải"* như một sự thật. Hanssen §10.3: ⚠ **chuẩn KHÔNG quy định** cách xử lý hồi tiếp — **tuỳ hiện thực**; trái-sang-phải chỉ là *"giả định hợp lý"*, và ⭐ **có hãng không cho vẽ hồi tiếp tường minh** chính vì lý do đó | ⚠➕ |
| 116 | Ch.21 — luật cấu trúc | Hanssen: ⚠ **không được đặt hai bước liền nhau không có bước chuyển**; ⭐ nhưng **nhiều bước được phép cùng hoạt động** (cơ chế nhánh song song) | ➕ |
| 117 | ⭐⭐ Ch.14 — `VAR_IN_OUT` | ⚠⚠ **Không xuất hiện MỘT LẦN NÀO trong cả cuốn sách** — trong khi Ch.27 và Ch.29 dùng `VAR_INPUT`/`VAR_OUTPUT` và là **đúng chỗ cần nó**. Hanssen §6.6: POU được gọi nhận ⭐ **chính vị trí bộ nhớ**, sửa thẳng biến bên gọi | ➕➕ |
| 118 | Ch.14 — `VAR_TEMP` | ⭐ Khởi tạo lại **mỗi lần gọi POU** → *"FB có bộ nhớ"* đúng với **thể hiện**, ⚠ **không đúng với mọi biến bên trong nó**. Bẫy: biến đếm khai `VAR_TEMP` **không bao giờ cộng được**, không báo lỗi | ➕ |
| 119 | ⭐ Bộ kiểm bắt lỗi của tôi | Bản nháp Ch.21 nhắc *"màn hình vận hành"* — ⚠ khái niệm **lát cắt 4** trong chương **lát cắt 1**. `kiem_tra_chuong.py` báo CẢNH BÁO B8, đã sửa | ⚠ |

### Kết quả đợt 21–22

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **8** |
| ➕➕ Bổ sung giá trị cao | 2 |
| ➕ Bổ sung có nguồn | 4 |
| ⚠➕ Nói chắc hơn mức chuẩn bảo đảm, đã siết | 1 |
| ⚠ Lỗi kỷ luật lát cắt (máy bắt) | 1 |

> ⭐⭐ **Hai mục ➕➕ có chung một đặc điểm: chúng là thứ người đọc KHÔNG BIẾT MÌNH ĐANG CÓ.**
>
> `Step.T` — người viết SFC vẫn khai `TON` cho từng bước, vì không ai nói cho họ biết mỗi bước đã có
> sẵn một timer. `VAR_IN_OUT` — người ta chép `STRUCT` vào rồi chép ra, tạo hai bản dễ lệch nhau, vì
> không ai nói cho họ biết có hướng tham số thứ ba.
>
> ⚠ **Đây là loại thiếu sót mà không bộ kiểm nào bắt được**, vì sách không hề mâu thuẫn — nó chỉ
> **không nhắc tới**. ⭐ Chỉ có đọc nguồn có hệ thống mới tìm ra.
>
> ⚡ Và đó chính là lập luận cho việc **lập bảng ánh xạ nguồn ↔ chương** (đợt tiếp theo): ⚠ tôi tìm ra
> `VAR_IN_OUT` **do tình cờ** grep một từ khoá khác. ⭐ Không có gì bảo đảm những chỗ tương tự trong
> 112 tài liệu còn lại sẽ được tình cờ như vậy.

---

## Đợt 23 — 2026-09-03 · ⭐⭐ ĐỢT ĐẦU TIÊN ĐƯỢC BẢN ĐỒ DẪN ĐƯỜNG — Ch.25

⭐⭐ **Khác mọi đợt trước ở một điểm quyết định: tôi không chọn chương này.** Bản đồ nguồn mới lập
(`docs/00e_Ban_do_nguon.md`) chỉ ra ⚠ **Hugh Jack — 860 trang — chưa được chương nào dẫn**, và mục lục
nhúng của nó có hẳn **chương 12 *State Based Design* dài 58 trang** — đúng chủ đề Ch.25.

⚠⚠ **Và nhật ký này, ngay ở bảng cuối, đã xếp nhóm chương thiết kế vào diện *"chủ yếu là phương pháp
và kinh nghiệm nghề, ít đối chiếu được bằng tài liệu"*. Kết luận đó SAI.** Nguồn tốt nhất cho đúng
nhóm đó vẫn nằm nguyên, chưa mở.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 120 | ⭐⭐ Ch.25 §25.5b — bất biến | Hugh Jack §12.1.2.2 phát biểu bằng **một câu**: *trạng thái BẬT nếu đã bật sẵn, HOẶC vừa được một chuyển tiếp đưa vào — và chưa bị chuyển tiếp nào đưa ra*. ⭐ Sách có **hai cách hiện thực** nhưng chưa từng nêu **cái mà cả hai đang cưỡng chế** | ➕➕ |
| 121 | Ch.25 — ba vế, ba loại lỗi | Thiếu vế *"đã bật sẵn"* → tắt ngay vòng sau · thiếu vế *"vừa được đưa vào"* → không vào được · ⚠⚠ thiếu vế *"chưa bị đưa ra"* → **vào được không ra được** = đúng Bẫy 2 sẵn có | ➕ |
| 122 | ⚠⚠ Ch.25 — **hai chuyển tiếp cùng đúng** | ⭐ Sách **không phủ** trường hợp này. Hugh Jack có hẳn *Ladder Logic with Prioritization*. Với `CASE` thì ⚠ **nhánh `IF` viết trước thắng** — ưu tiên tồn tại **dù tác giả có ý thức hay không**; với bit trạng thái thì ⚠⚠ **có thể bật hai bit hoặc tắt cả hai** | ➕➕ |
| 123 | Ch.25 — thứ tự ưu tiên mặc định | ⭐ `Alarm` → `Stopping` → chuyển tiếp quy trình. Lý do: **an toàn và ý muốn người vận hành thắng tiến độ sản xuất** | ➕ |
| 124 | Ch.25 — đánh đổi của cách bit trạng thái | Hugh Jack: block logic *"produce larger programs… much larger and less efficient"* nhưng *"simple to understand, and easy to debug"*. ⭐ Củng cố đúng kết luận sách đã có ở §25.5 — nay **có nguồn**, không còn là ý kiến | ✅➕ |
| 125 | ⭐ Ch.47 — nguồn an toàn bị tổng quát hoá | Bản đồ báo SICK/DGUV *"chưa dẫn"*. Kiểm: thân chương **nêu đích danh**, danh sách nguồn lại viết *"nhà sản xuất thiết bị an toàn"*. ⭐ **Đã sửa thành tên thật** | ⚠ |

### Kết quả đợt 23

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **6** |
| ➕➕ Bổ sung giá trị cao | 2 |
| ➕ Bổ sung có nguồn | 2 |
| ✅➕ Nguồn xác nhận kết luận sẵn có | 1 |
| ⚠ Sửa truy vết nguồn | 1 |
| Nơi đã sửa | Ch.25 (§25.5b mới + 3 dòng Bảng chốt + 3 câu Tự kiểm + nguồn) · Ch.47 (danh sách nguồn) |

> ⭐⭐ **Bài học lớn nhất của cả quy trình tới giờ, và nó nằm ở CÁCH chọn việc, không ở nội dung.**
>
> Suốt 22 đợt, tôi chọn chương để kiểm bằng **trực giác** — chương nào *nghe có vẻ* dễ sai. Trực giác
> đó có ích, nhưng nó ⚠ **chỉ nhìn được vào chỗ tôi đã biết là có gì ở đó**.
>
> Bản đồ nhìn từ **phía ngược lại**: không hỏi *"chương nào đáng ngờ"* mà hỏi ⭐ **"tài liệu nào đang
> có trong tay mà chưa ai mở?"** — và câu hỏi đó lập tức chỉ ra một cuốn **860 trang** mà tôi đã tự
> tay ghi vào nhật ký là *"khó đối chiếu"*.
>
> ⚡ **Đo được thì cải thiện được:** số nguồn chưa dẫn là **9 nguồn / ~4.439 trang** sau đợt này. ⭐ Con
> số đó phải **giảm dần qua từng đợt** — nếu nó đứng yên, đợt đó chỉ đào sâu chỗ đã quen.

---

## Đợt 24 — 2026-09-04 · Ch.26, 27, 30 — khai thác tiếp Hugh Jack theo bản đồ

⭐ Bản đồ chỉ tiếp: Hugh Jack còn **ba chương chưa dùng** ứng với nhóm thiết kế — ch.10 *Structured
Logic Design*, §32.4.1 *Developing a Program Structure*, §32.5 *Documentation*.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 126 | ⭐⭐ Ch.26 §26.2b — phương pháp thứ hai | Sách chỉ dạy **lưu đồ → bit bước**. Hugh Jack ch.10 có **thiết kế theo sơ đồ thời gian** kèm ⚠⚠ **điều kiện áp dụng**: chỉ hợp lệ cho quy trình *"phụ thuộc duy nhất vào thời gian"* | ➕➕ |
| 127 | Ch.26 — nối với bài học Ch.17 | ⭐ Điều kiện đó **củng cố** thay vì mâu thuẫn luận điểm trung tâm của sách: dùng sơ đồ thời gian khi CÓ phản hồi thật là ⚠⚠ **quay lại đúng sai lầm lớn nhất ở Chương 17** | ➕ |
| 128 | Ch.26 — phép thử một câu | *"Có cảm biến nào cho tôi biết bước này xong chưa?"* — ba đáp án, ba hành động. ⭐ Đáp án thứ ba (*"có nhưng lắp thêm tốn"*) là ⚠⚠ **quyết định của người trả tiền, không phải của người lập trình** | ➕ |
| 129 | ⭐⭐ Ch.27 §27.2 — cách **suy ra** kiến trúc | Sách **cho sẵn** ba tầng nhưng không dạy cách tự chia cho máy khác. Hugh Jack §32.4.1 có **bốn câu hỏi**: chạy cùng lúc? · độc lập? · có trình tự rõ? · ⭐ **có ranh giới vật lý?** | ➕➕ |
| 130 | Ch.27 — câu đáng tin nhất | ⭐ **Ranh giới vật lý** là ranh giới đã được thực tế kiểm chứng; chia theo nó thì chương trình **soi gương** cấu trúc máy. ⚡ Áp bốn câu vào DP-01 **ra đúng ba tầng sách đã có** — kiến trúc nay **suy ra được**, không còn là dictum | ➕ |
| 131 | Ch.30 §30.5b — thời điểm viết tài liệu | Hugh Jack §32.5: tài liệu dồn tới cuối ⚠⚠ **không bao giờ tốt được** — không phải vì lười mà vì **chi tiết đã quên**. ⭐ Thứ quên trước nhất là **lý do**, đúng thứ người đọc sau cần nhất | ➕ |
| 132 | ⭐ Ch.24 — kiểm rồi, **không sửa** | Đối chiếu Hugh Jack ch.6–7 (Boolean, Karnaugh): sách đã phủ đủ, và §24.7 *"khi nào KHÔNG nên tối ưu"* còn **chín hơn** cách trình bày kinh điển | ✅ |

### Kết quả đợt 24

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **7** |
| ➕➕ Bổ sung giá trị cao | 2 |
| ➕ Bổ sung có nguồn | 4 |
| ✅ Kiểm ra đủ, giữ nguyên | 1 |
| Nơi đã sửa | Ch.26 (§26.2b + 2 dòng Bảng chốt + 2 câu Tự kiểm + nguồn) · Ch.27 (mục mới + 2 dòng + 3 câu + nguồn) · Ch.30 (mục mới + 1 dòng + 1 câu + nguồn) |

> ⭐⭐ **Hai mục ➕➕ có chung một dạng: sách đưa KẾT QUẢ đúng nhưng giấu mất CÁCH ĐI TỚI nó.**
>
> Ch.27 cho ba tầng kiến trúc — đúng, đã kiểm chứng — nhưng người đọc có máy khác DP-01 thì ⚠ **không
> suy ra được gì**. Ch.26 dạy một phương pháp thiết kế và không nói có phương pháp thứ hai, nên người
> đọc gặp nó trong code người khác sẽ ⚠ **tưởng đó là code sai**.
>
> ⭐ Nguồn tốt bổ khuyết đúng chỗ này: nó không thêm sự kiện mới, nó **thêm con đường**.
>
> ⚡ **Và mục 132 cũng đáng ghi ngang các mục kia:** đối chiếu ra kết luận *"sách đã đủ, không sửa"*.
> ⚠ Một đợt đối chiếu mà **mục nào cũng phải sửa** là dấu hiệu đáng ngờ — hoặc bản thảo rất kém, hoặc
> người đối chiếu đang sửa cho có.

---

## Đợt 25 — 2026-09-04 · Khảo sát nguồn quốc tế + ⭐⭐ Ch.47 (lập trình PLC an toàn)

⭐ Đợt này bắt đầu từ ngoài: khảo sát các cộng đồng PLC (Anh, Trung) xem tài liệu kinh điển của ngành
là gì, và **tải về những gì tải được hợp pháp**.

### Kết quả khảo sát

| Tài liệu | Trạng thái |
|---|---|
| ⚠ **Bryan & Bryan** — *Programmable Controllers: Theory and Implementation* | Kinh điển, cộng đồng Anh ngữ nhắc nhiều nhất. ⚠⚠ **Có bản quyền, ghi rõ cấm sao chép** — mọi bản *"free download"* trên mạng là bản lậu. ⭐ **KHÔNG tải.** Muốn có phải mua |
| ⚠ **Kelvin T. Erickson** — *PLC: An Emphasis on Design and Application* | Thương mại — phải mua |
| Giáo trình Trung ngữ (西门子/三菱 hướng) | Thương mại; ⭐ nội dung không vượt các tài liệu hãng đã có trong bộ |
| ⭐ **PLCopen — 5 đặc tả** | ⭐⭐ **PLCopen phát hành chính thức, miễn phí — ĐÃ TẢI** |

**Đã tải (từ `plcopen.org/downloads`, bản chính thức):**

| Tệp | Trang | Dùng cho |
|---|--:|---|
| ⭐ `PLCopen_Safety_Part1_v2.10.pdf` | **194** | ⭐⭐ Ch.47, Ch.48 |
| `PLCopen_Safe_Motion_v1.0.pdf` | 45 | Ch.37, Ch.47 |
| `PLCopen_Motion_Control_Part3_v2.0.pdf` | 94 | Ch.37 |
| `PLCopen_XML_technical_doc_v2.01.pdf` | 80 | Ch.30 |
| `PLCopen_Structuring_Program_Development_IEC61131-3.pdf` | 4 | Ch.14, Ch.27 |

⭐ Bộ tài liệu: **63 → 68 tệp · 23.139 → 23.556 trang**. Cả 5 tệp trích được text và có mục lục.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 133 | ⭐⭐ Ch.47 §47.4b — **lập trình PLC an toàn** | Bảng §47.4 ghi *"lập trình an toàn có quy trình riêng"* rồi ⚠ **bỏ lửng**. PLCopen Safety §4: đó là ⭐ **tập con bị cắt bớt có chủ ý** của IEC 61131-3 — và ⭐ **công cụ cưỡng chế**, không phải người tự giữ kỷ luật | ➕➕ |
| 134 | ⚠⚠ Ch.47 — **ba mức người dùng và ranh giới chi phí** | Mức **cơ bản** chỉ nối khối **đã chứng nhận** → nghiệm thu nhanh. ⚠⚠ Ngay khi **tự viết một khối** → sang mức **mở rộng**, và **cả chương trình** phải qua kiểm định đầy đủ. ⭐ *"Tự viết một khối nhỏ thôi mà"* là **câu hỏi ngân sách, không phải câu hỏi kỹ thuật** | ➕➕ |
| 135 | Ch.47 — giới hạn ngôn ngữ | ⭐ **FBD/LD ưu tiên** (một tập con đã định) · **ST chỉ ở mức mở rộng** · ⚠ **IL và SFC không được đặt vấn đề**. Lý do: kiểm thử và thẩm định ngôn ngữ **văn bản** phức tạp và dễ sai hơn ngôn ngữ **đồ hoạ** | ➕ |
| 136 | Ch.47 — nối với Ch.20 | ⚡ Đây là một trong số ít chỗ **ladder thắng ST dứt khoát**, và lý do **trùng đúng** nguyên tắc ở §20.6: *thứ người khác phải đọc và xác nhận được thì viết bằng cái họ đọc được* — ở đây "người khác" là ⭐ **người thẩm định** | ➕ |
| 137 | ⭐ Hai tệp Rockwell 1 trang | `1756-pm001` và `1756-qs001` chỉ có **trang bìa** — không hỏng, Rockwell phát hành kiểu đó. ⭐ Ghi nhận để **không tính chúng là nguồn** | ✅ |
| 138 | Bản đồ — mở rộng theo dõi | Thêm 9 bí danh: 36 nhãn / 56 tệp (trước: 28 / 46). ⚠ Số chưa dẫn **tăng** 8 → 10 — ⭐ **đúng như mong đợi**: theo dõi kỹ hơn thì lộ ra nhiều lỗ hơn | ➕ |

### Kết quả đợt 25

| | Số lượng |
|---|---|
| Tài liệu mới tải về | **5** (417 trang) |
| Tài liệu xác định **không tải được hợp pháp** | 2 (Bryan & Bryan · Erickson) |
| ➕➕ Bổ sung giá trị cao | 2 |
| ➕ Bổ sung có nguồn | 3 |
| Nơi đã sửa | Ch.47 (§47.4b mới + 2 dòng danh mục + 3 câu Tự kiểm + nguồn) |

> ⭐⭐ **Phát hiện của đợt này thuộc loại chưa từng gặp: một CÂU BỎ LỬNG.**
>
> Bảng §47.4 có ô ghi *"lập trình an toàn có quy trình riêng"* — ⭐ **đúng, nhưng nói xong rồi thôi**.
> Người đọc chọn cột *"PLC an toàn"* mang theo một mô hình sai: *"giống lập trình thường, chỉ cẩn thận
> hơn"*. ⚠⚠ Thực tế là **ngôn ngữ bị cắt bớt** và **chi phí nhảy vọt ở một ranh giới không ai nói cho
> họ biết trước**.
>
> ⚡ **Bài học quy trình:** ngoài *"chỗ này đúng không"* và *"người đọc dựng mô hình gì"* (đợt 18), nay
> thêm câu thứ ba — ⭐ **"chỗ nào sách nêu một khác biệt rồi KHÔNG giải thích nó?"** Những ô bảng ghi
> *"có quy trình riêng"*, *"khác nhau tuỳ hệ"*, *"cần đào tạo thêm"* là **danh sách việc còn nợ**.
>
> ⭐ **Và về nguồn:** khảo sát ngoài xác nhận bộ tài liệu **đã đủ mạnh** — thứ kinh điển còn thiếu đều
> có bản quyền, còn thứ tải được hợp pháp thì lấp đúng lỗ hổng lớn nhất còn lại (lập trình an toàn).

---

## Đợt 26 — 2026-09-04 · ⭐ Bryan & Bryan vào bộ — Ch.51, Ch.52

⭐ Chủ dự án đã bổ sung **Bryan & Bryan, *Programmable Controllers: Theory and Implementation*** —
cuốn mà đợt 25 xác định là kinh điển nhưng **không tải hợp pháp được**. ⭐ **1.047 trang, 194 mục,
trích được text.** Bộ tài liệu: **69 tệp · 24.603 trang**.

⭐ Mục lục nó có hẳn **ch. 20 *PLC Start-Up and Maintenance*** — đúng hai chương còn nợ (51, 52).

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 139 | ⭐⭐ Ch.52 §52.6 — **chế độ thử của bộ điều khiển** | Sách dựng cờ `M_DryRun` **tự viết**. Bryan §20-5: nhiều bộ điều khiển có sẵn ⭐ **TEST mode — chạy chương trình với ngõ ra bị VÔ HIỆU**. ⭐⭐ An toàn hơn vì ngõ ra tắt **ở tầng hệ thống**, không phụ thuộc chương trình của bạn chạy đúng | ➕➕ |
| 140 | ⚠⚠ Ch.52 — **nấc thang tạm** | Bryan: *"remove all of the temporary rungs that may have been used"*. ⭐ Sách phủ **cưỡng bức** rất kỹ nhưng ⚠ **không hề nhắc logic tạm** — cùng loại nguy hiểm, và **tệ hơn một điểm**: ⚠⚠ **cưỡng bức có danh sách để kiểm, nấc tạm thì không** — nó trông y hệt code thật | ➕➕ |
| 141 | Ch.52 — cách phòng | 4 bước, làm **ngay lúc chèn**: đánh dấu comment thống nhất · ghi vào danh sách cùng chỗ với cưỡng bức · ⭐ **so sánh dự án** với bản trước khi thử · thêm mục riêng vào danh mục nghiệm thu | ➕ |
| 142 | ⭐⭐ Ch.51 §51.7 — **quét đơn** | Bryan: *single scan* — thực thi **đúng một vòng quét** rồi dừng. ⭐⭐ **Công cụ duy nhất cho lỗi phụ thuộc THỨ TỰ**: xem trực tuyến chỉ cho giá trị **sau khi cả vòng quét chạy xong**, nên lỗi *"nấc 5 đọc giá trị vòng trước"* (Ch.10, Ch.15) ⚠ **trông hoàn toàn bình thường** trên màn hình | ➕➕ |
| 143 | Ch.51 §51.11 — **bảo trì cho chính PLC** | Bảng sẵn có là PLC **giám sát máy**. Bryan §20-6 bổ sung chiều ngược lại: phin lọc tủ · ⚠⚠ **bụi bám cánh tản nhiệt chặn thoát nhiệt** (CPU và I/O **không được thiết kế kín bụi**) · siết đầu nối · thay pin | ➕ |
| 144 | Ch.51 — hai nguyên tắc lập lịch | ⭐ **Ghép lịch PLC vào lịch máy** để máy chỉ dừng một lần; ⭐ **tần suất theo MÔI TRƯỜNG chứ không theo PLC** — cùng một CPU trong phòng sạch và cạnh máy cắt là **hai lịch khác hẳn** | ➕ |

### Kết quả đợt 26

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **6** |
| ➕➕ Bổ sung giá trị cao | 3 |
| ➕ Bổ sung có nguồn | 3 |
| Nơi đã sửa | Ch.52 (mục mới + 1 dòng danh mục + nguồn) · Ch.51 (2 dòng bảng công cụ + mục mới + nguồn) |

> ⭐⭐ **Mục 140 là loại phát hiện đắt nhất: một khoảng trống nằm NGAY CẠNH chỗ sách làm rất kỹ.**
>
> Sách dành hẳn một mục cho **cưỡng bức I/O**, có quy trình bốn bước, có cảnh báo ⚠⚠, có mục trong
> danh mục nghiệm thu. Nhưng **nấc thang tạm** — thứ cùng loại nguy hiểm và **khó phát hiện hơn** —
> ⚠ **không xuất hiện một lần nào trong cả cuốn sách**.
>
> ⭐ Lý do rất người: cưỡng bức **có tên riêng và có nút bấm trong phần mềm**, nên nó *"trông giống một
> chủ đề"*. Nấc tạm thì chỉ là **code bạn tự gõ thêm** — nó không có tên, nên không ai nghĩ nó là một
> chủ đề cần bàn.
>
> ⚡ **Bài học quy trình:** ⭐ **chỗ nào sách làm rất kỹ, hãy hỏi ngay *"còn thứ gì cùng loại mà KHÔNG
> có tên gọi riêng không?"*** — thứ không có tên là thứ không ai đi tìm.

---

## Đợt 27 — 2026-09-04 · Ch.23 (đặc tả) và Ch.12 (IO-Link)

⭐ Hai chương còn nợ, hai nguồn khác nhau: Bryan ch.11 cho Ch.23, và ⭐ **đặc tả IO-Link 294 trang —
nguồn đang nằm trong bộ mà chưa chương nào dẫn** — cho Ch.12.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 145 | ⭐⭐ Ch.23 §23.5b — **tắc khi viết trình tự là CHẨN ĐOÁN** | Bryan §11-2: nếu xây thuật toán thấy khó thì ⭐ **quay lại định nghĩa lại bài toán**. Sách dạy *cách viết* đặc tả nhưng ⚠ **không nói người viết phải làm gì khi tắc** — mà đó là tình huống ai cũng gặp | ➕➕ |
| 146 | Ch.23 — ba câu hỏi tìm chỗ thiếu | *Bước này kết thúc khi nào, đo bằng gì?* · *Không xong thì máy làm gì?* · ⚠⚠ *Ai quyết định — tôi hay khách hàng?* | ➕ |
| 147 | Ch.23 — nguyên tắc bốn chữ | ⭐ **Nghĩ trước, lập trình sau** — Bryan phát biểu thành quy tắc nền, khớp đúng Bẫy 1 sẵn có | ✅➕ |
| 148 | ⭐ Ch.23 — kiểm rồi, **không sửa** | Bryan §11-1 nói *ai* định nghĩa nhiệm vụ và *"đừng chép lại logic rơ-le cũ"* — ⭐ sách **đã có đủ** ở Bẫy 4 và Bẫy 5. Không thêm | ✅ |
| 149 | ⭐⭐ Ch.12 §12.4b — **chế độ SIO** | Đặc tả IO-Link §6: thiết bị ⭐ **bỏ qua toàn bộ tầng truyền thông**, đưa thẳng DI/DO ra ngoài như cảm biến số thường; ⭐ đặc tính điện theo **IEC 61131-2 kiểu 1**; chọn chế độ bằng ⭐ **cấu hình, không phải đấu dây**. ⚠ Sách **không nhắc một lần nào** | ➕➕ |
| 150 | Ch.12 — hệ quả mua sắm | ⭐⭐ Câu hỏi *"có nên dùng IO-Link không"* ⚠ **không còn là quyết định một lần**: mua thiết bị có IO-Link, dùng như cảm biến thường, nâng cấp module sau mà **giữ nguyên thiết bị và dây**. Ngược lại, tiết kiệm hôm nay nghĩa là ⚠⚠ **nâng cấp phải thay cả thiết bị hiện trường** | ➕➕ |
| 151 | Ch.12 §12.4 — tên chuẩn của cơ chế | Cơ chế "master giữ bản sao tham số" trong đặc tả gọi là ⭐ **kho tham số** *(Data Storage)* — bổ sung tên để tra được về bản gốc | ➕ |

### Kết quả đợt 27

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **7** |
| ➕➕ Bổ sung giá trị cao | 3 |
| ➕ Bổ sung có nguồn | 2 |
| ✅ Kiểm ra đủ, giữ nguyên | 2 |
| ⭐ **Chỉ số bản đồ** | **10 → 8 nguồn chưa dẫn** (~4.529 → ~4.210 trang) |

> ⭐⭐ **Mục 149 là bằng chứng rõ nhất cho giá trị của bản đồ nguồn.**
>
> Đặc tả IO-Link nằm trong bộ tài liệu **từ đầu**, 294 trang, và Ch.12 viết về đúng chủ đề đó — nhưng
> ⚠ **chưa chương nào dẫn nó**. Kết quả: sách bỏ sót một tính chất mà ⭐ **ai chọn mua cảm biến cũng
> cần biết**, và nó nằm ở **mục 6 của đặc tả** — không hề khó tìm, chỉ là **không ai đi tìm**.
>
> ⚡ Nếu không có bản đồ, tôi sẽ không bao giờ mở tệp đó — vì Ch.12 *"trông đã đầy đủ"*.
>
> ⭐ **Và mục 148 nhắc lại kỷ luật của đợt 24:** Bryan §11-1 có hai ý hay, kiểm ra sách **đã có cả
> hai**. Ghi *"không sửa"* vào nhật ký cũng là một kết quả — nó chứng minh vòng kiểm có thật.

---

## Đợt 28 — 2026-09-04 · Ch.28 (về gốc trục) + ⚠⚠ SỬA LỖI TRONG CHÍNH BẢN ĐỒ

⭐ Bản đồ chỉ ra **FX5 Positioning — 302 trang, 158 mục — chưa chương nào dẫn**, và mục lục nó có
**§3.2 OPR Control**: đúng chủ đề về gốc của Ch.28.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 152 | ⭐⭐ Ch.28 §28.4b — **về gốc cho TRỤC** | Ch.28 phủ về gốc cho **xy-lanh** (hai tư thế, cảm biến báo là xong). ⚠ Với **trục** — dừng được ở **vô số vị trí** — sách **không có gì**. FX5 §3.2 cho trình tự đầy đủ | ➕➕ |
| 153 | Ch.28 — **hai tín hiệu, hai vai trò** | ⭐ **Cữ báo gần gốc**: *"sắp tới, giảm tốc"* — thô. ⭐⭐ **Tín hiệu điểm không**: *"đúng điểm này"* — tinh, thường là **kênh Z encoder** (Ch.18 §18.5b). ⚠⚠ Đây là **quyết định mua sắm và đấu tủ**, không sửa được bằng phần mềm | ➕➕ |
| 154 | Ch.28 — vì sao có **tốc độ bò** | ⭐ Quãng đường dừng từ tốc độ cao phụ thuộc **tốc độ, tải, ma sát** — ba thứ đều đổi. Bò chậm làm nó nhỏ tới mức không đáng kể → **độ lặp lại**. Cùng lý do: ⚠ **luôn về gốc cùng một chiều** (khe hở cơ khí) | ➕ |
| 155 | ⚠⚠ Ch.28 — **về gốc nhanh** và điều kiện hợp lệ | Sau khi đã về gốc bằng cảm biến, hệ **biết địa chỉ gốc** → định vị tuyệt đối tới đó, ⭐ **không dùng cữ và điểm không**. ⚠⚠ **Chỉ đúng khi vị trí CHƯA từng mất** — sau mất điện với encoder gia số thì **bắt buộc** về gốc bằng cảm biến. Đề xuất cờ *"vị trí còn tin được"* | ➕➕ |
| 156 | ⚠⚠ **Lỗi trong `ban_do_nguon.py` — bản đồ báo THIẾU lỗ hổng** | Bộ so khớp dùng **chuỗi con**: từ phân biệt `"control"` của nhãn *PLCopen Motion Control* khớp **bên trong** `"Programmable Logic Controllers"` → ⚠ mọi dẫn chiếu **Petruzella** bị quy nhầm cho **PLCopen**. Đã sửa sang **so khớp theo TỪ** | ⚠⚠ |
| 157 | ⚠ Bản đồ — quy kết quá rộng | Một dẫn chiếu FX5 Positioning bị tính cho **cả bốn** nhãn Mitsubishi vì chúng chia nhau từ *"mitsubishi"*, *"fx5"*. Đã sửa: chỉ khớp bằng **từ CHỈ nhãn đó có** | ⚠ |
| 158 | ⭐ Bản đồ — thêm tầng *"dẫn chung"* | Sách dẫn *"Petruzella"* mà bộ có **ba** bản khác nhau → không truy được **bản nào**. Nay báo riêng thành mục **2b** | ➕ |

### Kết quả đợt 28

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **7** |
| ➕➕ Bổ sung giá trị cao | 3 |
| ⚠⚠ **Lỗi công cụ, đã sửa** | 2 |
| ⭐ **Chỉ số bản đồ (đã sửa)** | **13 chưa dẫn** (~4.148 tr.) · **7 dẫn chung** |

> ⚠⚠ **Mục 156 là bài học đắt nhất của đợt này, và nó nhằm vào chính công cụ tôi vừa dựng.**
>
> Bản đồ nguồn được lập để **chống việc tự trấn an mình rằng đã đọc đủ**. ⚠ Nhưng vì một lỗi so khớp
> chuỗi con, ⚠⚠ **chính nó lại trấn an tôi**: các đợt trước tôi báo *"8 nguồn / 4.210 trang"* rồi
> *"6 nguồn / 2.438 trang"* — ⭐ **cả hai con số đều SAI theo hướng lạc quan**. Con số thật ở cùng thời
> điểm là **13 chưa dẫn + 7 dẫn chung**.
>
> ⭐⭐ **Bài học: công cụ đo độ phủ cũng phải bị nghi ngờ như nội dung nó đo** — và cách nghi ngờ là
> **kiểm một trường hợp mình đã BIẾT đáp án**. Tôi biết chắc Ch.16, 18, 19 có dẫn Petruzella; thấy
> bản đồ báo *"Petruzella chưa được dẫn"* là dấu hiệu đủ để đi tìm lỗi trong công cụ, thay vì tin
> con số.
>
> ⚡ Và tầng *"dẫn chung"* mới lại lộ ra một vấn đề thật của sách: ⚠ dẫn *"Petruzella"* trong khi bộ
> có **ba** bản của tác giả đó thì **người đọc không tra lại được**.

---

## Đợt 29 — 2026-09-04 · Ch.47 — nguồn cuối cùng chưa ai đụng tới

⭐ Bản đồ chỉ ra **PPSA (IRSST RG-597, 71 trang) là nguồn DUY NHẤT chưa hề được nhắc trong nhật ký** —
không chỉ chưa dẫn, mà **chưa từng mở**. Nội dung: che chắn cơ khí, khoảng cách an toàn, chống kẹp,
điểm cuốn.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 159 | ⭐⭐ Ch.47 §47.7 — **hình học quyết định trước phần mềm** | Bảng §47.7 liệt kê **thiết bị**. ⚠ Nhưng phần lớn việc bảo vệ do **hình học** quyết định, và nó nằm **trước** mọi thiết bị lẫn mọi dòng code | ➕➕ |
| 160 | Ch.47 — **kích thước lỗ ↔ khoảng cách** | PPSA §5.3: khoảng cách an toàn phụ thuộc ⭐ **cạnh NHỎ NHẤT của lỗ** trên che chắn (cạnh ngắn của khe · một cạnh lỗ vuông · đường kính lỗ tròn). ⚠⚠ Hệ quả: **đổi lưới sang mắt to hơn cho dễ nhìn** có thể **làm mất hiệu lực** khoảng cách đang có | ➕➕ |
| 161 | Ch.47 — chống kẹp có **hai** cách | ⭐ **Khe hở tối thiểu** = **loại bỏ** mối nguy, an toàn tự thân, thuần cơ khí, ⭐ **không hỏng được**. **Giảm lực/năng lượng** = chỉ **giảm** rủi ro, mối nguy vẫn còn | ➕ |
| 162 | ⚠⚠ Ch.47 — **điểm cuốn** | Bốn cấu hình sinh ra nó, trong đó ⚠⚠ **cấu hình 4 (con lăn tiếp xúc băng tải) là cấu hình của MỌI băng tải — kể cả DP-01**. ⭐ Điều đáng sợ với người làm phần mềm: **không cảm biến nào, không logic nào bảo vệ được** — khi đã bị cuốn thì dừng máy cũng muộn | ➕➕ |
| 163 | ⭐ Ch.47 — vì sao mục này ở trong sách PLC | Để người đọc ⭐ **nhận ra khi bài toán KHÔNG phải bài toán của mình**: với ba tình huống trên, câu trả lời đúng là ⚠ *"không lập trình, mà sửa cơ khí"* | ➕ |
| 164b | ⚠ Bản đồ — **nhãn của chính tôi đặt sai** | Tệp `PPSA_Prevention_of_Mechanical_Hazards` bị tôi gán nhãn *"PPSA / khí nén"* — ⚠ **đọc tên viết tắt rồi đoán nội dung**. Thực chất là hướng dẫn **cơ khí** của IRSST. Đã đổi nhãn | ⚠ |
| 164 | ⭐ Phụ lục F — **bộ kiểm bắt lỗi thật** | Sau khi thêm nội dung, `kiem_nhat_quan.py` báo GLOS: *"Mối nguy"* dẫn **Chương 6**. Kiểm: thuật ngữ xuất hiện ⚠ **0 lần ở Ch.6**, **21 lần ở Ch.47**. Đã sửa dẫn chiếu | ⚠ |

### Kết quả đợt 29

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **6** |
| ➕➕ Bổ sung giá trị cao | 3 |
| ➕ Bổ sung có nguồn | 2 |
| ⚠ Sai, đã sửa | 2 (Phụ lục F · nhãn bản đồ) |
| ⭐ **Chỉ số bản đồ** | **13 → 12 chưa dẫn** (~4.148 → ~4.077 trang) |

> ⭐⭐ **Mục 162 là phát hiện có sức nặng nhất về an toàn trong cả quá trình, và nó đến từ đúng nguồn
> mà không ai mở.**
>
> Máy mẫu của sách **có băng tải**, tức là ⚠⚠ **có điểm cuốn** — một mối nguy mà sách bàn về an toàn
> suốt cả chương lại **không nhắc tới lần nào**. Và nó thuộc loại mối nguy mà ⭐ **toàn bộ nghề nghiệp
> của người đọc cuốn sách này — viết logic — hoàn toàn bất lực**.
>
> ⚡ **Bài học quy trình:** ⭐ tài liệu nằm ngoài chuyên môn hẹp của cuốn sách (đây là tài liệu **cơ
> khí**, không phải tài liệu PLC) ⚠ **chính là chỗ dễ bỏ sót nhất** — vì nó không nằm trong danh sách
> *"những thứ một cuốn sách PLC cần đọc"*. ⭐ Bản đồ không biết chuyên môn, nên nó không thiên vị: nó
> chỉ nói **"tệp này chưa ai mở"**.
>
> ⭐ **Và mục 164 cho thấy ba bộ kiểm vẫn đang làm việc**: chỉ vì tôi thêm nội dung vào Ch.47 mà một
> dẫn chiếu sai **có sẵn từ trước** trong Phụ lục F mới lộ ra.

---

## Đợt 30 — 2026-09-04 · Ch.49 và Ch.8 — Bryan ch.20, phần lắp đặt

⭐ Bryan ch.20 còn hai mục chưa dùng: §20-3 *Noise, Heat, and Voltage* và §20-4 *I/O Installation,
Wiring, and Precautions* — đúng chủ đề Ch.49 và Ch.8.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 166 | ⭐⭐ Ch.8 §8.7b — **bảng khoảng cách lắp có GIẢ ĐỊNH NGẦM** | Con số milimét của hãng tính cho **tình huống điển hình**: ~60 % ngõ vào BẬT · ⭐ **~30 % ngõ ra BẬT** · dòng trong đặc tả · ⭐ **không khí 40 °C**. ⚠⚠ Máy nhiều van **giữ bật liên tục** vượt xa mức 30 % → **phải nới khoảng cách** | ➕➕ |
| 167 | Ch.8 — chiều so sánh nhiệt độ | ⭐ Điển hình là **40 °C**, nên tủ ở 45 °C ⚠ **đã khắc nghiệt hơn điển hình** — không phải *"vẫn còn xa giới hạn 55 °C"* | ➕ |
| 168 | Ch.8 — quạt và phin lọc | ⚠⚠ Gió quạt **phải qua phin lọc trước**: ⭐ bụi bám bề mặt tản nhiệt **làm giảm chính khả năng thoát nhiệt** mà quạt đang cố cải thiện. Nối với Ch.51 §51.11 | ➕ |
| 169 | ⚠⚠ Ch.49 §49.6b — **cắt nguồn trước khi lắp/tháo module** | ⭐ Thay nóng là **tính năng phải ghi rõ trong tài liệu của đúng module đó**, không mặc định. ⚠ Rút module không hỗ trợ có thể làm **ngõ ra khác nhảy trạng thái**. ⭐ Và ngay cả khi hỗ trợ, câu hỏi tiếp theo vẫn là *"ngõ ra này đang giữ cái gì?"* | ➕➕ |
| 170 | Ch.49 — **bó dây theo module** | ⭐ Là việc **bảo trì**, không phải thẩm mỹ: tháo module = rút **một bó**; nhìn là biết bó nào của module nào. ⚠ **Không thay thế** quy tắc tách cáp — bó theo module, rồi các bó vẫn đi đúng máng theo loại tín hiệu | ➕ |
| 171 | Ch.49 — tiết diện dây và mã màu | ⚠⚠ Kiểm theo **dòng lớn nhất có thể**, không theo dòng lúc chạy. ⭐ Mã màu giúp **thấy sai từ xa** nhưng **không thay số dây** — hai sợi cùng màu thì không truy vết được | ➕ |
| 172 | ⚠ Lỗi gõ của tôi | Bản nháp Ch.8 có *"bụi bám vào bám vào bề mặt tản nhiệt"* — lặp từ. Đã sửa | ⚠ |

### Kết quả đợt 30

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **7** |
| ➕➕ Bổ sung giá trị cao | 2 |
| ➕ Bổ sung có nguồn | 4 |
| ⚠ Lỗi gõ, đã sửa | 1 |

> ⭐⭐ **Mục 166 là biến thể thứ ba của bài học "bảng ngầm giả định gì" (đợt 20) — và lần này giả định
> nằm trong tài liệu của CHÍNH HÃNG.**
>
> Đợt 20: bảng 4 tổ hợp của sách ngầm giả định chỉ có **một kiểu hỏng**.
> Đợt 25: một ô bảng nêu khác biệt rồi **bỏ lửng**.
> ⭐ Đợt này: **bảng khoảng cách lắp của nhà sản xuất** ngầm giả định máy của bạn *"điển hình"* — và
> ⚠ **con số 30 % ngõ ra là thứ máy thật vi phạm thường xuyên nhất mà không ai kiểm**.
>
> ⚡ Điểm chung của cả ba: ⭐ **một bảng có con số cụ thể trông như sự thật tuyệt đối**, trong khi nó
> luôn là **kết luận có điều kiện**. Câu hỏi đáng hỏi ở mọi bảng — của sách hay của hãng — là ⭐ *"con
> số này đúng KHI NÀO?"*

---

## Đợt 31 — 2026-09-04 · Ch.22, và sửa truy vết nguồn Petruzella

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 173 | ⭐⭐ Ch.22 §22.4b — **thứ lẽ ra bạn phải nhận được** | §22.4 dạy dựng bản đồ chương trình **từ con số không**. ⚠ Sách không hỏi câu tiếp theo: *vì sao phải dựng lại thứ lẽ ra đã có?* Bryan §12-2: hồ sơ đầy đủ mở đầu bằng **bản tóm tắt hệ thống** — bài toán · ⭐ **chiến lược kèm LÝ DO chọn** · mục tiêu | ➕➕ |
| 174 | Ch.22 — phần luôn mất trước | ⭐ Sơ đồ đấu dây và bảng địa chỉ thì **còn**, vì thiếu chúng thì không đấu được máy. ⚠ *"Vì sao chọn cách này"* thì **không cần tới để máy chạy** → không ai viết. ⚡ Đó là lý do §22.5 (đọc code không chú thích) tồn tại — nó là **hệ quả**, không phải kỹ năng đáng tự hào | ➕ |
| 175 | ⭐ Ch.22 — đề nghị thực dụng | Dựng xong bản đồ thì ⭐ **viết ra 2–3 trang**, ⚠ **đánh dấu rõ chỗ nào là suy đoán chưa xác nhận**. Lợi cho chính người viết: viết ra mới lộ chỗ *tưởng đã hiểu mà chưa*; và người bàn giao đọc lại có thể **đính chính** | ➕ |
| 176 | ⭐ Ch.29 — kiểm rồi, **không sửa** | Rà công thức sản phẩm: kiểm tra hợp lệ, đổi khi đang chạy, phiên bản, phân quyền — ⭐ **sách đã phủ đủ**. Không ép thêm | ✅ |
| 177 | ⚠ Truy vết **Petruzella** — bản đồ báo đúng | Bộ có **ba** cuốn Petruzella; sách dẫn *"Petruzella, Programmable Logic Controllers"* ở 4 chỗ mà **không nêu bản nào**. Kiểm cả ba bản: ⭐ **năm khẳng định đều có ở CẢ 6th ed. lẫn bản 2025**, ⚠ **không có** trong *Activities Manual* (đó là sách bài tập). Đã ghi rõ vào 4 danh sách nguồn | ⚠ |
| 178 | ⚠ Bản đồ — ngưỡng từ phân biệt | Nhãn *"Petruzella — PLC 6th ed"* không có từ phân biệt nào ≥4 ký tự → **không bao giờ khớp được**. Hạ ngưỡng xuống **3** để giữ các từ ngắn nhưng đặc trưng (`6th`, `xml`) | ⚠ |

### Kết quả đợt 31

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **6** |
| ➕➕ Bổ sung giá trị cao | 1 |
| ➕ Bổ sung có nguồn | 2 |
| ✅ Kiểm ra đủ, giữ nguyên | 1 |
| ⚠ Sửa truy vết / công cụ | 2 |
| ⭐ **Chỉ số bản đồ** | **12 chưa dẫn** (~4.441 tr.) · **dẫn chung 7 → 4** |

> ⭐⭐ **Mục 177 là loại cải thiện mà chỉ bản đồ mới đề xuất được — và nó không phải "thêm nội dung".**
>
> Sách dẫn *"Petruzella"* bốn lần. Với người viết thì rõ ràng; ⚠ với **người đọc muốn tra lại** thì
> vô nghĩa — họ phải đoán trong ba cuốn. ⭐ Việc sửa không thêm chữ nào vào kiến thức, nhưng nó biến
> một dẫn chiếu **không dùng được** thành một dẫn chiếu **dùng được**.
>
> ⚡ Và cách kiểm cũng đáng ghi: thay vì chọn bừa một bản, tôi ⭐ **tìm cùng một câu trong cả ba bản**
> — kết quả là *"có ở cả hai bản chính, không có trong sách bài tập"*, chính xác hơn bất kỳ phỏng đoán
> nào.
>
> ⭐ **Và mục 176 giữ đúng kỷ luật đã lập từ đợt 24:** Ch.29 rà xong, kết luận **không sửa**. Ghi lại
> việc đó cũng là kết quả.

---

## Đợt 32 — 2026-09-04 · Ch.7 (ESD) và Ch.32 (analog) — hai hướng bị bỏ quên

⭐ Đợt này dựng lại bộ đệm tìm kiếm cho **6 tài liệu mới** (Bryan + 5 đặc tả PLCopen), rồi tra hai
chương còn nợ.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 179 | ⭐⭐ Ch.7 §7.7b — **ESD hỏng chính bộ điều khiển** | Cả Ch.7 nói ESD hỏng **sản phẩm**. ⚠ Tài liệu Siemens S7-1200 cảnh báo lặp lại một hướng thứ hai: **cắm/rút thẻ nhớ** và **chạm chân đầu nối** có thể hỏng **thẻ nhớ hoặc khe cắm trên CPU**. Biện pháp: ⭐ **chạm bề mặt dẫn đã nối đất, hoặc đeo vòng tay nối đất** | ➕➕ |
| 180 | ⚠⚠ Ch.7 — vì sao hướng này khó truy | ⭐ Giống board sản phẩm ở §7.2, module bị phóng tĩnh điện thường **hỏng tiềm ẩn** — lỗi chập chờn xuất hiện vài tuần sau, ⚠ **không ai liên hệ với lần thay thẻ nhớ**. Đã nối vào danh sách nguyên nhân lỗi chập chờn ở Ch.51 §51.8 | ➕ |
| 181 | ⭐ Ch.7 — lỗ hổng nhất quán | ⚠ Công ty đầu tư đường thoát tĩnh điện cho **sản phẩm** mà **bàn sửa module** không có gì — ⭐ đó là mâu thuẫn nội tại, đã thêm vào danh mục kiểm | ➕ |
| 182 | ⭐⭐ Ch.32 §32.6b — **trễ là tổng BA khoản** | §32.6 nói bộ lọc gây trễ. ⚠ Nhưng đó chỉ là **một** khoản. Hanssen §3.6.2: tổng = **đáp ứng cảm biến** + **cập nhật module (có lọc)** + **chu kỳ quét**. ⭐ Khoản lớn nhất thường là **cảm biến**, trong khi người ta hay đi tối ưu **chương trình** — khoản nhỏ nhất | ➕➕ |
| 183 | ⚠⚠ Ch.32 — **dùng ít kênh KHÔNG làm module nhanh hơn** | Phân biệt **thời gian một kênh** với **chu kỳ cả module**; ⭐ chu kỳ module **không giảm** dù có kênh không dùng. Mẹo *"chỉ đấu 2 trong 8 kênh cho nhanh"* ⚠ **không có tác dụng** — muốn nhanh thì **đổi module** | ➕➕ |
| 184 | Ch.32 — khi PLC vừa đọc analog vừa chạy PID | Hai đường: đổi module nhanh hơn, hoặc ⭐⭐ **bộ điều khiển rời và PLC chỉ đặt điểm đặt** — ⚡ đúng kiến trúc bộ điều khiển nhiệt rời của máy mẫu (Ch.38 §38.11) | ➕ |

### Kết quả đợt 32

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **6** |
| ➕➕ Bổ sung giá trị cao | 3 |
| ➕ Bổ sung có nguồn | 3 |

> ⭐⭐ **Cả hai mục ➕➕ chính đều là "hướng thứ hai" của một chủ đề sách đã bàn kỹ.**
>
> Ch.7 bàn ESD suốt 11 mục — nhưng **luôn theo một chiều**: tĩnh điện từ máy hỏng sản phẩm. ⚠ Chiều
> ngược lại — **tay người hỏng module** — không xuất hiện, dù nó xảy ra ngay trên bàn của người đọc.
>
> Ch.32 bàn trễ do lọc — nhưng chỉ **khoản của mình**. ⚠ Hai khoản kia (cảm biến, module) lớn hơn và
> **không nằm trong tầm sửa của người lập trình**, nên chúng bị bỏ khỏi câu chuyện.
>
> ⚡ **Bài học quy trình, nối tiếp đợt 26:** ngoài *"còn thứ gì cùng loại mà không có tên riêng?"*, nay
> thêm ⭐ **"chủ đề này có CHIỀU NGƯỢC LẠI không, và sách có kể chiều đó không?"** — nguồn gây hại đổi
> chỗ cho đối tượng bị hại, hoặc khoản chi phí nằm ngoài tầm kiểm soát của người viết.

---

## Đợt 33 — 2026-09-05 · ⭐ BA CHƯƠNG CUỐI — Ch.43, Ch.53, Ch.55

⭐ Ba chương khó đối chiếu nhất, mỗi chương một loại nguồn khác nhau.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 185 | ⭐⭐ Ch.53 §53.2b — **sửa trực tuyến có thể BỊ TỪ CHỐI** | FX5 Program Design: sửa trực tuyến sống nhờ **vùng nhớ dự phòng**. ⚠⚠ Không đủ chỗ → **không thực hiện được**, toàn bộ chương trình phải biên dịch lại và gán lại địa chỉ → **nạp lại toàn bộ, dừng máy**. ⭐ Và nó **tích luỹ**: sửa càng nhiều lần thì lần sau càng dễ bị từ chối | ➕➕ |
| 186 | ⚠⚠ Ch.53 — **sau khi nạp, trình tự chạy tiếp từ đâu** | Dừng rồi chạy lại → **khôi phục trạng thái trước đó**; nạp trong lúc STOP → **thường bắt đầu lại**, ⚠ **trừ khi công cụ coi là "không có thay đổi"**. ⭐ Hai hành vi khác nhau một trời một vực, và thứ quyết định lại **không nhìn thấy được** | ➕➕ |
| 187 | ⭐ Ch.43 §43.5b — **bit CHO PHÉP KÍCH** | Camera có bit *trigger enable* riêng; ⚠⚠ chưa bật thì **bỏ qua mọi lệnh kích và không báo lỗi**. ⭐ Cùng loại với cưỡng bức quên gỡ: **trạng thái do người đặt, vô hình, không có gì nhắc lại** | ➕➕ |
| 188 | Ch.43 — **số liệu trễ đo được** | ~**55 ms** (kiểm đơn giản) · ~**59 ms** (phức tạp) · trễ tăng **<6 %** khi mạng chiếm 50 % băng thông. ⭐ Cho **bậc độ lớn** khi tính nhịp máy: hàng chục mili-giây | ➕ |
| 189 | ⭐⭐ Ch.43 — biểu quyết đa số, và **chiều của nó** | Ba lần chụp + biểu quyết 2/3 ở tầng PLC giảm báo lỗi giả **7,5 % → 5,4 %**. ⚠⚠ Nhưng nó làm hệ **khoan dung hơn** — có thể **lọt lỗi thật**; và giá là **ba lần chụp**. ⭐ Nguyên nhân gốc gần như luôn là **chiếu sáng dao động** | ➕➕ |
| 190 | ⭐ Ch.43 §43.5 — kiểm ra **sách MẠNH HƠN nguồn** | Bài báo ⚠ **không hề bàn** việc ghép kết quả với đúng sản phẩm — không có đánh dấu danh tính, không tương quan thời gian, không xử lý kết quả về sai thứ tự. ⭐ **Sách đã có đủ** ở §43.5 bằng **số thứ tự ảnh**, và gọi đó là *"chi tiết quan trọng nhất của mục"* | ✅ |
| 191 | ⚠⚠ Ch.55 §55.7b — **OEE không so sánh được** | Cùng một máy, cùng một ca có thể ra **72 %** hay **91 %** tuỳ tính gì vào *"thời gian dự định"*. ⭐ *"Máy phải đạt OEE 85 %"* mà chưa chốt định nghĩa thì **chưa phải yêu cầu nghiệm thu** | ➕➕ |
| 192 | Ch.55 — có tiêu chuẩn để khỏi tự định nghĩa | ⭐ **SEMI E10** (trạng thái thiết bị) và **SEMI E79** (năng suất, gồm OEE) — bộ định nghĩa của ngành điện tử. ⚠ **Có bản quyền, phải mua**; sách chỉ nêu tên để hỏi đúng câu | ➕ |
| 193 | ⭐ Ch.55 — **sáu nhóm tổn thất** | Từ vựng khách hàng sẽ dùng, ánh xạ sang danh sách thực dụng ở §55.6. ⭐⭐ Nhóm **dừng vặt** là nhóm PLC giúp nhiều nhất — mỗi lần vài giây nên **không ai ghi sổ**, nhưng **PLC biết chính xác** | ➕ |

### Kết quả đợt 33

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **9** |
| ➕➕ Bổ sung giá trị cao | 5 |
| ➕ Bổ sung có nguồn | 3 |
| ✅ Kiểm ra **sách mạnh hơn nguồn** | 1 |

> ⭐⭐ **Mục 190 là kết quả đáng ghi nhất, và nó ngược chiều mọi đợt trước.**
>
> Suốt 32 đợt, nguồn luôn **bổ khuyết cho sách**. Lần này một bài báo bình duyệt về đúng chủ đề Ch.43
> lại ⚠ **bỏ trống chính bài toán trung tâm** — ghép kết quả với đúng sản phẩm — trong khi sách đã
> giải nó bằng số thứ tự ảnh và còn gọi đó là chi tiết quan trọng nhất.
>
> ⭐ Điều này **không** có nghĩa sách hơn bài báo: bài báo là **một nghiên cứu tình huống trên một hệ**,
> còn sách là **sổ tay cho nhiều hệ**. ⚡ Nhưng nó nhắc một điều: ⚠ **"có nguồn hàn lâm" không đồng
> nghĩa với "phủ đủ"** — và đối chiếu là **hai chiều**.
>
> ⭐ **Về nguồn cho ba chương này:** vision có **một bài truy cập mở CC-BY** dùng được; OEE thì bộ định
> nghĩa chuẩn (**SEMI E10/E79**) ⚠ **có bản quyền và phải mua** — sách xử lý bằng cách **nêu tên và
> nêu câu hỏi phải hỏi**, thay vì tự chế định nghĩa.

---

## Đợt 34 — 2026-09-05 · ⭐⭐ CÓ BẢN GỐC SEMI — viết lại Ch.55, thêm hai hình

⭐ Chủ dự án bổ sung **bộ tiêu chuẩn SEMI (5.292 trang, có E10 và E79)** và **bài báo Sensors** vào bộ
tài liệu. Bộ nguồn: **72 tệp · 29.916 trang**.

⚠⚠ **Điều này làm đổi một quy tắc của dự án.** Quy tắc *"không dẫn số điều khoản"* có lý do ghi rõ ở
bảng cuối nhật ký: ⭐ **"chỉ có tài liệu diễn giải của hãng"**. Với SEMI thì lý do đó **không còn** —
nay dẫn được số mục để người đọc tra lại bản gốc. ⭐ Với ISO/IEC vẫn giữ nguyên quy tắc cũ.

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 194 | ⭐⭐ Ch.55 §55.7b — **sáu trạng thái thiết bị** | E10 mục 5: mọi khoảnh khắc phải rơi vào **đúng một** trong sáu trạng thái. ⭐ Thay bảng *"hai cách trả lời đều có lý"* bằng **đáp án dứt khoát của tiêu chuẩn** cho từng dòng | ➕➕ |
| 195 | ⭐⭐ Ch.55 — quy tắc cắt tranh cãi | E10 mục 5.2: ⭐ **phân loại theo CHỨC NĂNG, không theo TỔ CHỨC** — một việc bảo trì xếp cùng loại **dù ai làm**. ⚠ Nghĩa là *"cái này thuộc bộ phận nào"* **không phải câu hỏi đúng** | ➕➕ |
| 196 | ⚠⚠ Ch.55 — máy đứng vì chuyền | E10 xếp *"hết hàng để làm"* vào **CHỜ**, không phải dừng máy — thiết bị vẫn ở tình trạng thực hiện được chức năng. ⭐ Xếp nó vào dừng máy là **đổ lỗi sai chỗ** | ➕➕ |
| 197 | ⚠⚠ Ch.55 — **ngay CÔNG THỨC cũng khác** | E79 mục 5.2.1: khả dụng = **thiết bị lên máy ÷ TỔNG thời gian**, không phải ÷ thời gian **dự định** như cách phổ biến (và như mục 55.7). ⭐ Cùng một tuần có thể ra **85 %** hay **40 %** mà **không ai tính sai** — hai câu hỏi khác nhau | ➕➕ |
| 198 | ⭐ Ch.55 — tách "hiệu suất" làm hai | E79 mục 5.2.2: **hiệu suất vận hành** (có chạy không) × **hiệu suất nhịp độ** (chạy nhanh không). ⭐ Một con số *"70 %"* không nói phải làm gì; ⚠ **máy đứng nhiều** và **máy chạy chậm** là hai bệnh khác hẳn | ➕➕ |
| 199 | Ch.55 — sáu biến thể OEE | E79 định nghĩa **sáu** biến thể cho các mục đích khác nhau — ⭐ riêng chi tiết đó đã chứng minh *"OEE không phải MỘT con số"* | ➕ |
| 200 | ⚠⚠ Ch.55 — **tách chờ bảo trì khỏi thời gian sửa** | E10 mục 5.9: sửa chữa = chẩn đoán + khắc phục + thử thiết bị + **chạy xác nhận**; và ⭐ **chờ người/phụ tùng phải theo dõi RIÊNG**. ⚠ Gộp vào thì **MTTR đo kho vật tư chứ không đo khả năng sửa** — rồi người ta đi đào tạo thợ trong khi vấn đề là hết phụ tùng | ➕➕ |
| 201 | ⭐ **Hình 55.1** (mới) | Sáu trạng thái và các khối thời gian, kèm hai ngoặc nhóm lên máy/xuống máy. ⚠ Đã render PNG và **sửa hai lỗi bố cục** phát hiện bằng mắt: dải cuối bị hộp chú thích đè, nhãn tràn mép phải | ➕ |
| 202 | ⭐ **Hình 43.1** (mới) | Sơ đồ thời gian một vòng kích ảnh — bit cho phép, cạnh lên, camera xử lý, gói kết quả kèm số thứ tự, dải đo ~55–59 ms, và hai hộp cảnh báo. ⭐ Ch.43 trước đó **không có hình nào** | ➕ |

### Kết quả đợt 34

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **9** |
| ➕➕ Bổ sung giá trị cao | 6 |
| ➕ Bổ sung / hình mới | 3 |
| ⭐ Hình mới | **2** (Hình 55.1, Hình 43.1) |

> ⭐⭐ **Mục 197 là phát hiện đắt nhất, và nó làm luận điểm của §55.7b từ "cảnh báo" thành "chứng minh".**
>
> Đợt 33 tôi viết *"OEE của hai máy không so sánh được nếu chưa chung định nghĩa"* — dựa trên lập luận
> về cách ghi sổ. ⭐ Có bản gốc rồi mới thấy vấn đề **sâu hơn nhiều**: ⚠⚠ **ngay công thức cũng khác**.
> Cách phổ biến chia cho **thời gian dự định**; E79 chia cho **TỔNG thời gian**. Chênh lệch có thể là
> 85 % so với 40 % trên cùng một cỗ máy.
>
> ⚡ **Bài học quy trình:** ⚠ **lập luận đúng không thay được bản gốc.** Tôi đã lập luận đúng hướng ở
> đợt 33, nhưng ⭐ **thiếu đúng cái làm nó thuyết phục** — và cái đó chỉ có trong tài liệu gốc.
>
> ⭐ **Và mục 194–196 cho thấy chiều ngược lại của cùng một chuyện:** đợt 33 tôi viết *"hai cách trả
> lời đều có lý"* cho năm câu hỏi định nghĩa. ⚠ **Sai** — tiêu chuẩn trả lời dứt khoát cả năm. Tôi
> đã trình bày một vấn đề **đã được giải** như thể nó còn mở, chỉ vì chưa đọc được lời giải.

---

## Đợt 35 — 2026-09-06 · Rà nhất quán toàn sách · SEMI E42 và E30 · hai hình mới

⭐ Đợt này ba việc: **rà nhất quán trình bày**, **khai thác tiếp bộ SEMI**, và **thêm hình ở chỗ chữ
không diễn đạt được**.

### A — Rà nhất quán (viết script quét toàn bộ 58 chương)

| # | Phát hiện | Xử lý |
|---|:--|:--:|
| 203 | ⭐ **Đánh số mục: sạch** — không chương nào sai số chương trong tiêu đề, không mục nào nhảy cóc | ✅ |
| 204 | ⚠ **Ch.5 có HAI mục tên "Bảng chốt"** — §5.8 là bảng nội dung, §5.10 là mục khung. ⭐ Trùng tên với một mục khung là gây nhầm | ⚠ |
| 205 | ⚠ **Ch.4, Ch.10, Ch.15 KHÔNG có "Bảng chốt"** — trong khi **54/58 chương có**. Bộ kiểm không báo vì mục này **không bắt buộc**, nhưng ⭐ thiếu ở đúng ba chương nền tảng là bất nhất về trải nghiệm đọc | ⚠ |

⭐ Đã sửa: đổi tên §5.8 thành *"Chọn gì cho tải nào"*; viết **ba Bảng chốt mới** cho Ch.4, Ch.10, Ch.15.
⚠ Kiểm trước khi đánh số lại: mục bị đẩy số (Tự kiểm) **không có dẫn chiếu nào** trỏ tới — an toàn.

### B — Khai thác tiếp bộ SEMI

| # | Nơi | Việc đã làm | KQ |
|---|---|:--|:--:|
| 206 | ⭐⭐ Ch.29 §29.6b — **"đã duyệt" ≠ "đã chứng thực"** | E42 mục 8.1–8.2.8: vòng đời công thức có **hai thuộc tính độc lập** — *mức duyệt* (nội dung đúng) và *đã chứng thực trên **máy này***. ⚠ Vòng 31 tôi kết luận Ch.29 *"đã phủ đủ"* — đúng với nguồn khi đó, nhưng ⭐ **thiếu hẳn chiều thứ hai này** | ➕➕ |
| 207 | ⭐⭐ Ch.29 — khoá là **hệ quả**, không phải cờ | E42 mục 8.2.5: công thức bị khoá khi **mức duyệt ≥ ngưỡng chỉ-đọc của kho**. ⭐ Thay vì trông vào việc ai đó **nhớ bật cờ khoá**, trạng thái khoá **tự suy ra** — cùng tinh thần *"làm cho hỏng hóc trở nên phát hiện được"* (Ch.48) | ➕➕ |
| 208 | ⚠⚠ Ch.29 — **rút chứng thực sau bảo trì** | Sau khi thay cơ cấu, chứng thực cũ **hết giá trị dù công thức không đổi một chữ**. ⭐ Đề xuất: xoá trường *"lần chứng thực gần nhất"* trong quy trình bảo trì, cùng chỗ với việc gỡ cưỡng bức | ➕➕ |
| 209 | ⭐ Ch.45 §45.4b — **SECS/GEM** | ⚠ Không xuất hiện lần nào trong sách, dù DP-01 là máy **điện tử** và khách hàng ngành đó sẽ hỏi đích danh. Thêm mục gọn: **ba tầng** (vận chuyển · nội dung bản tin **SECS-II** · ⭐ **hành vi thiết bị GEM**) | ➕ |
| 210 | ⭐⭐ Ch.45 — bất đối xứng của GEM | E30 mục 1.2: GEM quy định hành vi của **THIẾT BỊ**, ⚠ **không** quy định hành vi của **cấp trên** — cấp trên khởi xướng bất kỳ kịch bản nào, bất kỳ lúc nào. ⭐ Nên *"máy chúng tôi hỗ trợ GEM"* là **cam kết một chiều**; vẫn phải hỏi cấp trên sẽ gọi gì | ➕➕ |

### C — Hình mới

| # | Hình | Vì sao cần hình |
|---|---|:--|
| 211 | ⭐ **Hình 35.1** — ba đường đáp ứng P / P+I / P quá lớn | ⚠ Khối ASCII **không vẽ được đường cong**. Sai lệch tĩnh là khái niệm **thị giác thuần tuý** |
| 212 | ⭐ **Hình 21.1** — vạch đôi và vạch đơn của SFC | ⭐ Sách nói khác biệt này *"sống còn"* và vẽ nhầm thì **máy đứng im vĩnh viễn**. ⚡ Đúng loại khác biệt mà **nhìn thì không thể nhầm, đọc thì rất dễ nhầm** |

⚠ Cả hai đều render PNG và soát bằng mắt. ⭐ Hình 35.1 phải sửa **ba lần**: đường đỏ vọt khỏi khung ·
nhãn chồng đường vàng · và ⚠⚠ **đường đỏ xuất phát sai từ 66 % thay vì 0** — lỗi mô hình, không phải
lỗi bố cục. Đã thay bằng **đáp ứng bậc hai đúng dạng**.

### Kết quả đợt 35

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **10** |
| ➕➕ Bổ sung giá trị cao | 4 |
| ⚠ Sửa nhất quán | 2 nhóm (4 chương) |
| ⭐ Hình mới | **2** — sách nay có **13 hình** trên 58 chương |

> ⭐⭐ **Mục 206 đáng ghi vì nó lật một kết luận cũ của chính tôi.**
>
> Vòng 31 tôi rà Ch.29 và ghi *"sách đã phủ đủ, KHÔNG SỬA"* — và đó là **kết luận đúng với nguồn tôi
> có lúc đó**. ⚠ Nhưng E42 cho thấy còn một chiều hẳn: sách lo *"công thức này có đúng không"*, mà
> không lo *"nó đã được chứng minh trên CỖ MÁY NÀY chưa"*.
>
> ⭐ **Bài học: "đã kiểm, không sửa" luôn có kèm một mệnh đề ngầm — "với những gì tôi đọc được tính
> tới lúc đó".** Nguồn mới vào thì kết luận cũ phải mở lại, ⚠ **kể cả những chương đã đóng**.
>
> ⚡ **Và mục 211 nhắc một điều về hình:** XML hợp lệ, script báo OK, ba bộ kiểm đều xanh — nhưng
> ⚠⚠ **đường cong bắt đầu sai chỗ**. ⭐ Chỉ có **nhìn bằng mắt** mới bắt được, đúng như quy ước hình
> của dự án đã cảnh báo.

---

## Đợt 36 — 2026-09-13 · Phụ lục L (thư viện mẫu code) và ⚠⚠ chỗ mù của bộ kiểm

⭐ Đợt này khác mọi đợt trước: **không đối chiếu sách với nguồn ngoài, mà đối chiếu một tài liệu MỚI
với chính cuốn sách**. Phụ lục L gom 14 mẫu code thường dùng — và bản nháp đầu của nó **mâu thuẫn với
sáu chỗ trong thân sách**.

### A — Bản nháp Phụ lục L mâu thuẫn với thân sách

| # | Chỗ mâu thuẫn | Sách nói gì | KQ |
|---|:--|:--|:--:|
| 213 | ⚠⚠ Mẫu analog viết bằng **số thực**, và **ghi cứng** dải thô `3200…32000` | Ch.32 mục 32.4: dùng **`DINT` đơn vị nhỏ**, **nhân trước chia sau**, và ⚠⚠ `RAW_MAX` là **con số đầu tiên phải TRA DATASHEET** — ghi cứng một dải là dạy đúng cái bẫy Ch.32 Bẫy 4 | ⚠ |
| 214 | ⚠⚠ Ngưỡng báo động lấy **giá trị ĐÃ LỌC** | Ch.32 mục 32.9: lọc **chỉ cho hiển thị và ghi log**; ngưỡng dùng giá trị **chưa lọc**, vì bộ lọc cộng thêm trễ vào chuỗi trễ của cả máy (mục 32.6) | ⚠ |
| 215 | ⚠ Timeout từng bước **tự cộng mili-giây** mỗi vòng quét | Ch.26: **một `TON` dùng chung** với `Stn1_StepLimit : TIME`, tự đặt lại khi bước đổi. ⭐ Cộng tay là tự viết lại một khối chuẩn đã có, và sai khi tác vụ bị trượt nhịp | ⚠ |
| 216 | ⚠ Đặt ra cờ mới `M_PositionTrusted` | Ch.37 mục 37.3 đã có `M_Homed`, và nói rõ nó **không được giữ qua mất điện**. ⭐ Hai tên cho một khái niệm chính là định nghĩa của trôi dạt | ⚠ |
| 217 | ⚠ Dùng `M_AnyAlarm` làm cờ gom lỗi | `M_AnyFault` là tên dùng ở **17 chương**; `M_AnyAlarmActive` + `FirstAlarmCode` là tên của Ch.44. ⭐ `M_AnyAlarm` không tồn tại ở đâu khác | ⚠ |
| 218 | ⚠ Gọi nút vật lý là `M_StartPB` / `M_StopPB` | Bảng I/O chính thức J.2 có `DI_StartPB`, `DI_StopPB`. ⭐ Tiền tố `M_` để dành cho **bit nội bộ**, không phải ngõ vào | ⚠ |

⭐ Cả sáu đều đã sửa; Phụ lục L bản cuối dùng đúng khối chuẩn, đúng tên biến và đúng hằng của sách.

### B — ⚠⚠ Bộ kiểm KHÔNG nhìn thấy sáu lỗi trên

| # | Phát hiện | Hệ quả |
|---|:--|:--:|
| 219 | ⚠ Bộ kiểm không thấy sáu lỗi trên. ⚠⚠ **ĐÍNH CHÍNH đợt 39 — chẩn đoán ban đầu SAI**, xem đợt 39 mục 238. Lý do thật không phải "khối code bị bỏ qua" mà là: nhóm TAG **chỉ soi tiền tố vào/ra** (`DI_ DO_ AI_ AO_ AX_ NET_`), còn sáu lỗi kia là **tên biến nội bộ và lựa chọn kỹ thuật** — ⭐ **không nhóm kiểm nào của bộ công cụ được thiết kế để bắt loại đó** | ⚠ |
| 220 | ⭐ Ngược lại, `kiem_tra_chuong.py` **bắt được** một lỗi mà mắt tôi bỏ qua: dẫn chiếu mới ở Ch.30 nhắc *"servo"* — thiết bị **lát cắt 3** trong một chương **lát cắt 2**, vi phạm B8 | ✅ |

⭐ Đã thêm dẫn chiếu tới Phụ lục L từ Phụ lục B, E, J, K và Ch.30 mục 30.5 — chỗ nói về **ba yêu cầu
của một khối đáng đưa vào thư viện**, vì Phụ lục L chính là hiện thực của yêu cầu số 3
(*"có ghi rõ giả định"*).

### Kết quả đợt 36

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **8** |
| ⚠ Sửa mâu thuẫn nội bộ | **6** (đều trong bản nháp, chưa từng phát hành) |
| ⭐ Tài liệu mới | Phụ lục L — **14 mẫu**, sách nay có **13 phụ lục** |

> ⭐⭐ **Bài học lớn nhất của đợt này: bộ kiểm có một chỗ mù, và nó nằm ở phần code.**
>
> Bốn công cụ đều xanh trong khi bản nháp mâu thuẫn với Ch.26, Ch.32, Ch.37 và Ch.44 ở sáu chỗ.
>
> ⚠⚠ **ĐÍNH CHÍNH (đợt 39):** lời giải thích ban đầu ở đây — *"vì `kiem_nhat_quan.py` cố ý bỏ khối
> code"* — là **SAI**, và tôi đã dùng nó để đề xuất một thay đổi công cụ **không cần thiết**. Sự thật:
> nhóm XREF bỏ khối code, nhưng ⭐ **nhóm TAG thì KHÔNG** — nó đọc văn bản thô. Chỗ mù thật nằm ở
> **phạm vi**, không ở **vùng văn bản**: nhóm TAG chỉ soi tiền tố vào/ra, nên tên biến nội bộ `M_*`,
> hằng số và lựa chọn kỹ thuật (số thực hay số nguyên, lọc trước hay sau) ⚠ **không thuộc phạm vi của
> bất kỳ nhóm kiểm nào**. Chi tiết ở đợt 39 mục 238.
>
> ⚡ Sáu lỗi trên chỉ lộ ra vì tôi tra thẳng trong sách *"chương nào đã DẠY thứ này?"* trước khi viết —
> đúng quy trình đã ghi ở đợt 24. ⚠ Nếu viết theo trí nhớ thì cả sáu đã vào bản phát hành, và chúng
> **nguy hiểm hơn một câu văn sai**: mẫu code là thứ người đọc chép nguyên.
>
> ⚠⚠ **Đề xuất ghi ở đây ĐÃ BỊ RÚT (đợt 39):** *"cho `kiem_nhat_quan.py` quét tên tag bên trong khối
> code"* — ⭐ **nó đã quét sẵn rồi**. Đề xuất thay thế, hẹp hơn và đúng chỗ hơn, nằm ở đợt 39 mục 238.

---

## Đợt 37 — 2026-09-13 · Đối chiếu với MỘT CHƯƠNG TRÌNH MÁY THẬT

⭐ Nguồn của đợt này khác hẳn mọi đợt trước: không phải sách hay tiêu chuẩn, mà là **một chương trình
điều khiển máy sản xuất đang chạy**, viết trên nền **Inovance AutoShop**, khoảng 40 chương trình con,
21 khối chức năng dùng lại và hơn 40 kiểu dữ liệu người dùng.

> ⚠ **Theo bất biến B1b, danh tính dự án/khách hàng không được ghi ở bất kỳ đâu.** Chỉ ghi nền công cụ
> (tên hãng là thông tin được phép — B1). ⭐ Mọi thứ rút ra đều đã viết lại thành **tình huống chung**,
> không mang số liệu quy trình hay tên trạm của dự án đó.
>
> ⚠ Thân chương trình lưu dạng biên dịch nên **không đọc được mã**. ⭐ Thứ đọc được — và cũng là thứ
> đáng giá nhất — là **kiến trúc**: cây thư mục, danh sách khối, và toàn bộ **kiểu dữ liệu kèm chú
> thích**.

### A — Bốn thứ sách THIẾU hẳn

| # | Nơi bổ sung | Nội dung | KQ |
|---|---|:--|:--:|
| 221 | ⭐⭐ **Ch.51 mục 51.7b** — cờ bỏ qua thiết kế sẵn | Sách dạy cưỡng bức I/O nguy hiểm thế nào, nhưng ⚠ **không trả lời câu đứng ngay sau đó**: *"camera hỏng, mai phụ tùng mới về, đêm nay vẫn phải ra hàng"*. Chương trình thật có hẳn một **tập cờ bỏ qua có tên** — theo trạm, theo camera, theo đầu đọc mã, theo việc tải dữ liệu lên, theo ô khay. ⭐ Đó là **thứ duy nhất thay thế được việc cưỡng bức**: không có nó, người ta tự làm bằng cách tệ hơn | ➕➕ |
| 222 | ⭐⭐ **Ch.27 mục 27.3b** — tầng chống va chạm | Sách nhắc *"liên động chống va chạm"* ở Ch.27, 28, 46 nhưng ⚠ **chưa bao giờ coi nó là một TẦNG riêng**. Chương trình thật có một mảng cờ chống va chạm và **một nhóm báo động riêng** cho nó. ⭐⭐ Điểm mấu chốt: cờ nằm ở **tầng cơ cấu**, nên chế độ tay **không thể đi vòng qua** — đúng chỗ va chạm thật sự xảy ra | ➕➕ |
| 223 | ⭐⭐ **Ch.30 mục 30.3b** — hợp đồng ba phần `Cmd · Data · Resp` | Mục 30.3 gói trạng thái vào một UDT nhưng **trộn lẫn thứ người ngoài ghi với thứ khối tự ghi**. Chương trình thật tách **ba phần cho mọi cơ cấu** — xy-lanh, trục, điện xy-lanh, đầu ép, khay, kho, chân không — cùng một khuôn tên. ⭐ Nhờ đó câu *"chỗ nào ghi vào phản hồi của xy-lanh 3?"* trả lời được bằng **một lần tra chéo** | ➕➕ |
| 224 | ⭐⭐ **Ch.55 mục 55.7c** — đo và cất số liệu OEE ở đâu | Ch.55 giải thích OEE và SEMI E10/E79 rất kỹ nhưng ⚠ **không nói PLC phải làm gì**. Chương trình thật có bốn đồng hồ (bật máy · chạy · dừng · chờ) và cấu trúc lưu **24 giờ × 3 ca × ~31 ngày × 2 tháng**. ⭐⭐ Bổ sung kèm **bất biến kiểm được**: `chạy + dừng + chờ = bật máy` | ➕➕ |

### B — Bốn thứ sách có nhưng còn mỏng

| # | Nơi bổ sung | Nội dung | KQ |
|---|---|:--|:--:|
| 225 | ⭐ **Ch.44 mục 44.5b** — cửa sổ nhắc thao tác | Chương trình thật có năm nút do PLC điều khiển: xác nhận · lặp lại · bỏ qua · tiếp tục · huỷ. ⭐ Sách chỉ có **báo động**, mà báo động nói *"đã có lỗi"* — còn đây là *"đang chờ bạn"*. ⚠⚠ Kèm cảnh báo về nút *"Tiếp tục"*: không có phân quyền và không đánh dấu truy xuất thì nó là **cái nút biến hàng lỗi thành hàng đạt** | ➕➕ |
| 226 | ⭐ **Ch.30 mục 30.3b** — chia thư mục theo vai trò | Sáu nhóm: cấu hình hệ thống · khởi tạo · thao tác tay · **báo động (mỗi nguyên nhân một chương trình con)** · trình tự trạm · cấu hình trục. ⭐ Và **trình tự chạy khô là một chương trình con RIÊNG**, thay vì rải `IF M_DryRun` khắp trình tự thật | ➕ |
| 227 | ⭐ **Phụ lục L.15** — hút chân không có thổi ngược | Sách nhắc chân không ở Ch.5, 6, 33, 46 nhưng ⚠ **không có mẫu code**. Ba điều phân biệt nó với xy-lanh hai vị trí: ngừng hút ≠ nhả · thổi ngược phải **tắt** sau một nhịp · ⚠⚠ *"mất chân không giữa chừng"* là báo động **riêng** (sản phẩm đã rơi đâu đó trong máy) | ➕ |
| 228 | **Ch.53 mục 53.5 · Phụ lục L.16** — đếm tuổi thọ vật tư | ⭐ Sách **đã có** hai ngưỡng 0,7 / 0,9 và đã nói *"nhắc, không được dừng máy"* — ✅ **không sửa**. Thứ còn thiếu là **gói thành một khối có tham số**: viết tay từng bộ đếm thì người ta theo dõi ba thứ rồi thôi. ⚡ Và hiện **phần trăm đã dùng**, không hiện số lần đếm được | ➕ |
| 229 | ⭐ **Phụ lục K.7b** — lưới khay dạy ba điểm | Công thức nội suy hai chiều từ ba ô đã dạy. ⭐⭐ Vì sao **ba** điểm chứ không phải hai: ba điểm bắt được cả **khay bị xoay khi gá** — hai điểm thì ô xa nhất sai nhiều nhất | ➕ |

### C — Đã xem và CỐ Ý không thêm

| Thứ có trong chương trình thật | Vì sao không thêm |
|:--|:--|
| Theo dõi từng vòi hút / từng ô khay của máy gắp linh kiện | ⚠ Quá đặc thù một loại máy — vi phạm tinh thần B6 (tự đủ ≠ phủ mọi ngành) |
| Điều khiển lực ép có PID, bù hiệu chuẩn, ngưỡng chạm | ⭐ Ch.34 và Ch.35 đã phủ nguyên lý; phần còn lại là tham số của một đầu ép cụ thể |
| Kho đệm vào trước ra trước / vào sau ra trước, đếm giờ từng ô | ⭐ Đáng thêm, nhưng thuộc Ch.41 và cần viết cẩn thận — **để đợt sau** |
| Bản đồ thanh ghi Modbus của xy-lanh điện | ⭐ Ch.39 đã có bẫy *"thanh ghi không dấu đọc ra số âm"*; phần còn lại là datasheet một mã hàng |
| Điều khiển hai tay | ⚠⚠ Ch.47 mới có **một dòng** trong bảng. Có tiêu chuẩn riêng quy định con số cụ thể, mà ⚠ **bộ tài liệu nội bộ KHÔNG có bản gốc** — theo B2 không được viết số liệu từ trí nhớ. ⭐ **Cần mua tiêu chuẩn** |

### Kết quả đợt 37

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **9** |
| ➕➕ Bổ sung giá trị cao | 5 |
| ➕ Bổ sung | 4 |
| ✅ Kiểm rồi không sửa | 1 (Ch.53 hai ngưỡng bảo trì) |
| Mục mới trong thân sách | 5 — Ch.27, 30, 44, 51, 55 |
| Mẫu code mới | 2 — Phụ lục L nay có **16 mẫu** |

> ⭐⭐ **Bài học lớn nhất: một chương trình máy ĐANG CHẠY trả lời được loại câu hỏi mà sách và tiêu
> chuẩn không trả lời.**
>
> Sách dạy *nên làm gì*. Tiêu chuẩn nói *phải đạt gì*. ⚠ Nhưng chỉ chương trình thật mới cho thấy
> **cái gì buộc phải có để máy sống được qua ca đêm** — và ba trong bốn mục ở phần A đúng là loại đó:
> cờ bỏ qua, tầng chống va chạm, cửa sổ nhắc thao tác. ⭐ Cả ba đều sinh ra từ **áp lực vận hành**,
> không từ lý thuyết, nên không sách nào nghĩ ra để viết.
>
> ⚡ **Và mục 221 là mục đáng nhớ nhất, vì nó lật cách sách đặt vấn đề.** Ch.51 coi cưỡng bức là **thứ
> phải cấm**. Chương trình thật cho thấy cưỡng bức là **triệu chứng**: người ta cưỡng bức vì chương
> trình không cho họ cách nào khác. ⭐ Cấm mà không thay thế thì chỉ đẩy việc đó vào chỗ tối hơn.
>
> ⚠ **Bộ kiểm lại bắt được hai lỗi của tôi trong đợt này**, cả hai đều là B8 (bóc lớp): Ch.27 nhắc
> *"gantry"* và Ch.30 nhắc *"HMI"* — đều là thiết bị của lát cắt sau. Cộng với một lỗi TAG:
> `DO_ZDownVlv` không có trong bảng I/O J.2, ⭐ **vì trục Z của DP-01 là servo chứ không phải van**.
> ⚡ ⚠ **ĐÍNH CHÍNH (đợt 39):** câu ở đây từng viết ba lỗi này *"nằm ngoài khối code"*. ⭐ **Sai** —
> `DO_ZDownVlv` nằm **bên trong** một khối ```` ```iecst ````, và nhóm TAG vẫn bắt được, vì nó đọc văn
> bản thô. Đây chính là bằng chứng phủ nhận chẩn đoán ở đợt 36.

---

## Đợt 38 — 2026-09-13 · Phần HMI, trạm đệm, và ⚠ một dự án KHÔNG đọc được

Đợt này ba nguồn: **khối giao diện màn hình** của chương trình máy ở đợt 37, **một chương trình máy
thứ hai** của cùng nhóm kỹ thuật, và **một dự án màn hình** mà ⚠ **không mở được**.

> ⚠ Bất biến B1b vẫn áp: không ghi tên dự án, khách hàng, hay nhà máy ở bất kỳ đâu.

### A — ⚠ Dự án màn hình: KHÔNG đọc được

| # | Việc | KQ |
|---|---|:--:|
| 230 | Dự án màn hình (Weintek EasyBuilder Pro 6.10, tệp `.cmtp` 10 MB + `.cxob` 46 MB). ⚠⚠ **Nội dung bị nén/mã hoá theo định dạng riêng của hãng** — không có chuỗi văn bản nào đọc được, không phải zlib, không phải zip. ⭐ **Không rút được gì từ nó mà không có phần mềm EasyBuilder Pro** | ❔ |

⭐ **Thứ thay thế được, và hoá ra còn tốt hơn:** khối dữ liệu **PLC ↔ màn hình** nằm trong chính
chương trình PLC và **đọc được đầy đủ** — 101 biến gốc, hơn 2 500 dòng. ⚡ Nó cho biết *màn hình trao
đổi những gì*, tức là **kiến trúc giao diện**, thay vì cách vẽ nút.

### B — Ba mục mới cho phần HMI

| # | Nơi bổ sung | Nội dung | KQ |
|---|---|:--|:--:|
| 231 | ⭐⭐ **Ch.44 mục 44.2b** — một màn hình cho mọi cơ cấu cùng loại | Khối giao diện chỉ có **MỘT** bộ biến trục cộng **một ô chỉ số**, không phải 10 bộ. PLC chép phản hồi của trục đang chọn ra, chép lệnh vào đúng trục đó. ⚠⚠ Kèm bẫy chết người: **không xoá phần Lệnh khi đổi chỉ số thì lệnh của trục 1 rơi xuống trục 2** | ➕➕ |
| 232 | ⭐ **Ch.44 mục 44.3b** — ba kênh thông điệp | Khối giao diện tách hẳn **báo động · cảnh báo · nhắc thao tác**. ⭐⭐ Và việc tách kênh thứ ba **làm đúng luôn số liệu ở Ch.55**: máy chờ người không phải máy hỏng, nên không được rơi vào *thời gian dừng* | ➕➕ |
| 233 | ⭐ **Ch.44 mục 44.2** — hiện **phiên bản chương trình PLC** trên màn hình tổng quan | Khối giao diện có hẳn một biến `Version`. ⚠ Câu hỏi đầu tiên khi hỗ trợ từ xa là *"máy đang chạy bản nào?"* — không hiện thì không ai trả lời được (Ch.54) | ➕ |

⭐ Việc **lật trang xem số liệu lịch sử** (ngày trước/ngày sau/xem tháng) cũng nằm trong PLC: màn hình
chỉ gửi một xung, PLC giữ chỉ số. ⚡ Đã ghi vào 44.2b như một ca cụ thể của mục 44.6.

### C — Trạm đệm: mục đã hoãn ở đợt 37, nay viết

| # | Nơi bổ sung | Nội dung | KQ |
|---|---|:--|:--:|
| 234 | ⭐⭐ **Ch.41 mục 41.7b** — trạm đệm | Mục 41.4 mới hỏi *"ai đang giữ sản phẩm"* với **một** sản phẩm. Trạm đệm có nhiều sản phẩm nằm cùng lúc, mỗi ô một đồng hồ. ⭐⭐ Phân biệt **đệm cân bằng nhịp** với **đệm theo thời gian** — ở loại sau, ⚠⚠ **chọn nhầm vào-sau-ra-trước là lỗi không nhìn thấy được**: máy vẫn chạy, chỉ có chất lượng sai | ➕➕ |
| 235 | ⭐⭐ Ch.41 mục 41.7b — **bật máy lên, trong đệm đang có hàng** | Mất điện giữa ca thì sản phẩm còn nằm nguyên, bộ nhớ chương trình thì không. ⭐ Lối đúng: **đọc lại cảm biến rồi HỎI người vận hành** — vì ⚠ *thời gian đã nằm* thì không cảm biến nào biết. Và dù chọn gì cũng **phải đánh dấu số sản phẩm đó** | ➕➕ |

⭐ Cách phòng rẻ nhất cho mục 234 cũng đã viết ra: **đừng lấy ra theo vị trí, hãy lấy ra theo đồng hồ**
— chọn ô nằm lâu nhất trong số ô đã đủ điều kiện, khi ấy thứ tự đúng **tự nhiên đúng**.

### D — Đo được một điều mà trước nay chỉ nói định tính

| # | Nơi bổ sung | Nội dung | KQ |
|---|---|:--|:--:|
| 236 | ⭐⭐ **Ch.30 mục 30.5** — mức 3 tái sử dụng trông như thế nào | Đối chiếu **hai cỗ máy khác nhau của cùng một nhóm**: bố cục thư mục **giống hệt**, thư viện khối **giống hệt**, bộ kiểu dữ liệu **giống hệt**, khối giao diện màn hình **trùng khoảng hai phần ba từng tên biến** (65 / 101 và 65 / 106 biến gốc). ⚠ Phần khác nhau gần như **chỉ là thư mục trình tự trạm** | ➕➕ |

> ⭐⭐ **Mục 236 là mục có giá trị nhất đợt này, vì nó biến một lời khuyên thành một hình dạng đo được.**
> Ch.30 vẫn nói *"tái sử dụng ở mức máy"* mà không ai hình dung được nó ra sao. ⭐ Nay có con số:
> **phần đặc thù của một cỗ máy thu lại thành MỘT thư mục.**

### Việc quản trị

| # | Việc | KQ |
|---|---|:--:|
| 237 | ⚠ **Sửa quy ước phiên bản theo yêu cầu của chủ dự án:** `BASE_VERSION` **chỉ tăng khi được bảo tăng**. Tôi đã tự ý tăng lên `v1.1.0` rồi `v1.2.0` trong ngày — ⭐ **sai**. Đã trả về `v1.0.0`, ghi luật vào `CLAUDE.md` và vào đầu `tools/gop_sach.sh` để lần sau không lặp lại | ⚠ |

### Kết quả đợt 38

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **8** |
| ➕➕ Bổ sung giá trị cao | 5 |
| ➕ Bổ sung | 1 |
| ❔ Không đọc được nguồn | 1 |
| Mục mới trong thân sách | 3 — Ch.41, Ch.44 (×2) |

> ⭐⭐ **Bài học: khi một nguồn không mở được, hãy hỏi xem thông tin đó có ở dạng khác không.**
>
> Dự án màn hình bị mã hoá, và phản xạ đầu tiên là báo *"không làm được"*. ⚠ Nhưng thứ tôi thật sự
> cần — **màn hình trao đổi những gì với PLC** — nằm ở **phía PLC**, và ở đó nó là văn bản thuần.
> ⭐ Nguồn đóng, nhưng **mặt tiếp giáp của nó thì mở**.
>
> ⚡ **Và mục 237 đáng ghi vì nó là lỗi quy trình, không phải lỗi nội dung.** Tôi tăng số phiên bản
> theo cảm nhận *"đợt này lớn"* — trong khi ⭐ **quyết định phát hành là của chủ dự án, không phải của
> người viết**. Luật nay nằm ở hai chỗ, và một trong hai chỗ là dòng đầu của script ghép.

---

## Đợt 39 — 2026-09-17 · Bất biến B18, và ⚠⚠ đính chính hai kết luận sai của chính tôi

Đợt này bắt đầu từ một yêu cầu của chủ dự án: ⭐ *"khi nhắc tới những thứ khác nhau, hãy cho ví dụ và
nêu ưu nhược điểm của các cái đó, ví dụ như cách đặt tên biến"*.

### A — Chỗ bị chỉ đích danh, và nó đúng

| # | Nơi | Vấn đề | KQ |
|---|---|:--|:--:|
| 238 | ⭐⭐ **Ch.30 mục 30.2** | Sách viết *"Có nhiều cách đặt tên tag hợp lý. Không cách nào đúng tuyệt đối"* rồi ⚠ **nhảy thẳng sang quy ước của sách** — chưa bao giờ cho thấy những cách khác đó là gì. Người đọc không có cơ sở nào để đánh giá, và cũng không bảo vệ được lựa chọn của mình trước đồng nghiệp | ⚠ |

⭐ Đã viết lại: **bốn quy ước có người dùng thật** — địa chỉ trần · tiền tố loại · phân cấp theo cấu
trúc · theo mã thiết bị trên bản vẽ — đặt tên cho **cùng một cảm biến**, cùng một đoạn logic viết bốn
lần, bảng ưu/nhược, cách **trộn** được chấp nhận, và bảng **chọn cái nào trong hoàn cảnh nào**.

⚡ Kèm hai câu mà mục cũ thiếu hẳn: ⭐ **điều tệ nhất không phải chọn sai quy ước mà là không chọn**;
và ⚠ khi bàn giao cho nhà máy đã có quy ước riêng thì **quy ước của họ thắng** — người sống với
chương trình mười năm tới là họ.

### B — Nâng yêu cầu đó thành bất biến, và cho công cụ canh

| # | Việc | KQ |
|---|:--|:--:|
| 239 | ⭐ **Bất biến B18** trong `CLAUDE.md`: chỗ nào nêu nhiều lựa chọn phải có đủ **bốn thứ** — liệt kê đích danh · một ví dụ thật **cùng một bài toán** cho từng cách · bảng ưu/nhược · khuyến nghị dùng cái nào khi nào. ⚠ Dừng ở *"tuỳ bạn"* là chưa viết xong | ➕ |
| 240 | ⭐ Thêm phép kiểm **B18** vào `kiem_tra_chuong.py` (mức TIN, không chặn ghép) | ➕ |
| 241 | Quét toàn sách: **8 chỗ** khớp mẫu *"nhiều cách / vài cách / tuỳ bạn…"*, ⭐ **cả 8 nay đều có bảng so sánh kề bên**. Ba chỗ chỉnh thêm: Ch.30 mục 30.2 (viết lại), Ch.11 (dẫn thẳng tới 30.2 thay vì "Chương 30"), Ch.36 (dẫn tới Chương 40 mục 40.3/40.5 thay vì *"chọn theo mạng bạn đang dùng"*) | ⚠ |
| 242 | ⭐ Ch.26 Bẫy 3 — trước chỉ nói *"đánh cách 10, chi phí bằng không"*. Nay so sánh **ba kiểu** đánh số bước (liền nhau · cách 10 · cách 100 theo trạm) kèm ưu/nhược. ⚡ Kiểu thứ ba đáng giá từ ba trạm trở lên: mã lỗi `S230` tự nói ra *trạm 2, bước 30* | ➕ |

> ⚠ **Giới hạn của phép kiểm B18, nói thẳng để không ai tin quá nó.** Nó chỉ biết *quanh đó có bảng
> hay có dẫn chiếu không* — ⭐ **nó không biết bảng đó có phải bảng SO SÁNH hay không**. Nên nó bắt
> được ca trắng trợn (một câu "có nhiều cách" nằm trơ giữa đoạn văn) và ⚠ **bỏ lọt ca tinh vi** (câu
> đó tình cờ nằm cạnh một bảng nói chuyện khác). ⚡ Đã thử trên ba ca dựng sẵn: báo đúng ca xấu, im ở
> hai ca tốt.

### C — ⚠⚠ Đính chính: hai kết luận về CÔNG CỤ của tôi ở đợt 36 và 37 đều sai

Khi thêm một tag minh hoạ vào Ch.30, nhóm TAG **báo lỗi** — dù tag đó nằm **bên trong một khối
`iecst`**. Điều đó mâu thuẫn với kết luận tôi ghi ở đợt 36. Tra lại mã nguồn:

| Nhóm kiểm | Đọc gì | Có thấy trong khối code không |
|---|---|:--:|
| **XREF** (dẫn chiếu) | `van` — đã bỏ khối code | ⚠ **Không** |
| ⭐ **TAG** (tên tag) | `tho` — **văn bản thô** | ⭐ **CÓ** |

| # | Kết luận cũ | Sự thật | KQ |
|---|:--|:--|:--:|
| 243 | Đợt 36: *"`kiem_nhat_quan.py` cố ý xoá mọi khối code, nên mọi tên tag trong code đều vô hình"* | ⚠⚠ **Sai.** Chỉ XREF bỏ code; TAG thì không | ⚠ |
| 244 | Đợt 37: *"ba lỗi này nằm ngoài khối code — đúng vùng bộ kiểm nhìn thấy"* | ⚠⚠ **Sai.** `DO_ZDownVlv` nằm **trong** khối code, và vẫn bị bắt — đây chính là bằng chứng phủ nhận mục 243 | ⚠ |
| 245 | Đợt 36 đề xuất *"cho công cụ quét tên tag bên trong khối code"* | ⚠ **Đã rút** — nó quét sẵn rồi. Tôi suýt bỏ công làm một việc đã có | ⚠ |

⭐ **Chỗ mù thật là chỗ nào, nói cho đúng:** không phải *vùng văn bản* mà là **phạm vi**. Nhóm TAG chỉ
soi tiền tố vào/ra (`DI_ DO_ AI_ AO_ AX_ NET_`). Sáu lỗi của đợt 36 là **tên biến nội bộ `M_*`, hằng
số, và lựa chọn kỹ thuật** (số thực hay số nguyên, lọc trước hay sau ngưỡng) — ⚠ **không nhóm kiểm
nào được thiết kế để bắt loại đó**, và phần lớn trong số đó thì **không công cụ nào bắt nổi**.

| # | Phát hiện phụ về công cụ | KQ |
|---|:--|:--:|
| 246 | ⚠ Biểu thức tìm tag là `(?:DI\|DO\|...)_[A-Za-z0-9]+` — **dừng ở dấu gạch dưới thứ hai**. Tag hai gạch dưới sẽ bị cắt cụt rồi mới đem so. ⭐ Bảng I/O DP-01 hiện **không có tag nào như vậy** nên chưa hại gì, nhưng đây là **bẫy nằm chờ** | ⚠ |

### Kết quả đợt 39

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **9** |
| ⚠ Đính chính kết luận cũ của chính tôi | **3** |
| ➕ Bổ sung nội dung | 3 (Ch.30 mục 30.2 viết lại · Ch.26 Bẫy 3 · Ch.36) |
| Bất biến mới | **B18** |
| Phép kiểm mới | **B18** trong `kiem_tra_chuong.py` (mức TIN) |

> ⭐⭐ **Bài học 1 — "có nhiều cách" là một lời hứa chưa trả.**
>
> Câu đó nghe khiêm tốn và công bằng, nên rất dễ viết. ⚠ Nhưng với người đọc nó **không mang thông
> tin nào**: họ vẫn phải đi tìm những cách đó ở chỗ khác, và đó đúng là việc cuốn sách nhận làm hộ.
> ⭐ Viết ra bốn cái tên, bốn dòng code, một bảng ưu/nhược tốn nửa trang — và nó thay thế một buổi tối
> tra cứu của người đọc.
>
> ⚡ **Bài học 2 — phải nghi ngờ cả kết luận về công cụ, không chỉ kết luận về nội dung.**
>
> Đợt 36 tôi ghi một chẩn đoán về chính bộ kiểm của mình, ⚠ **không thử lại**, rồi đợt 37 **viết thêm
> một câu dựa trên nó** — và câu đó chứa sẵn bằng chứng phủ nhận nó (`DO_ZDownVlv` nằm trong khối
> code). ⭐ Sai lầm sống được hai đợt vì nó **giải thích thoả đáng** hiện tượng đã thấy. ⚠⚠ Đúng cái
> bẫy mà chính nhật ký này đã ghi ở đợt 24: *phải thử công cụ trên một ca mà bạn đã biết trước câu
> trả lời*. Lần này tôi có làm việc đó cho phép kiểm **mới** (B18) — nhưng đã **không** làm cho kết
> luận về phép kiểm **cũ**.

---

## Đợt 40 — 2026-09-17 · Rà toàn sách bằng SỐ LIỆU, không bằng cảm nhận

Yêu cầu: *"rà soát lại toàn sách xem có chỗ nào cần bổ sung"*. ⚠ Rà bằng cách đọc lại 58 chương là
việc **không đáng tin** — mắt quen dần và bỏ qua đúng những chỗ đã đọc nhiều lần. ⭐ Nên đợt này đo
trước: viết một script đếm **số từ · số mục · số bẫy · số hình · số khối code · số bảng · có Bảng
chốt không · số nguồn** cho từng chương, rồi chỉ đi vào những chỗ số liệu chỉ ra.

### A — Số liệu nói gì

| Chỉ số | Kết quả |
|---|---|
| Tổng số từ thân sách | ~295 000, trung bình ~5 100 từ/chương |
| ⚠ Chương **thiếu Bảng chốt** | **2** — Ch.01 và **Ch.52** (54/58 chương còn lại đều có) |
| ⚠ Chương **không có hình** | 45/58 |
| Chương ngắn nhất | Ch.50 (~3 075 từ) · Ch.02 · Ch.17 |

### B — Lỗ hổng tìm ra và đã lấp

| # | Nơi | Nội dung | KQ |
|---|---|:--|:--:|
| 247 | ⭐⭐ **Ch.52 mục 52.11b** | Chương nghiệm thu — chương **nhiều danh mục nhất sách** — lại **không có Bảng chốt**. Đã viết, và viết **khác** mục 52.9: 52.9 là *"phải kiểm gì trước khi bàn giao"*, còn Bảng chốt là *"chương này dạy gì"* | ➕ |
| 248 | ⭐⭐ **Ch.13 mục 13.2b** | Mục 13.2 có bảy tiêu chí chọn PLC, nhưng ⚠ **thiếu hẳn ba tiêu chí**: **môi trường lắp đặt** (dải làm việc thông dụng 0–55 °C là nhiệt độ **TRONG TỦ**), **bộ nhớ** (sách không có tiêu chí nào về bộ nhớ!), và **I/O tại chỗ hay ở xa** | ➕➕ |
| 249 | ⭐ **Phụ lục K.5b** | Quy tắc ước lượng bộ nhớ chương trình: **5 word mỗi thiết bị số + 25 word mỗi thiết bị analog**, kèm điều kiện áp dụng và ⚠ nhắc **bộ nhớ dữ liệu là chuyện khác** — với máy lưu lịch sử năng suất thì bảng dữ liệu mới là thứ quyết định chọn CPU | ➕ |
| 250 | ⭐⭐ **Ch.27 mục 27.2b** | Sách nói chương trình **nên** có ba tầng, nhưng ⚠ **không nói bắt đầu từ đâu**. Bổ sung **bảy bước dựng cấu trúc** của PLCopen, đối chiếu từng bước với chương tương ứng | ➕➕ |
| 251 | ⚠ Ch.27 mục 27.2b — **giới hạn của việc chia nhỏ** | Sách đẩy mạnh việc phân rã mà chưa bao giờ nói điểm dừng. ⭐ *"Chia càng nhỏ thì công sức không biến mất — nó chuyển sang việc GHÉP."* Dấu hiệu chia quá tay: ⚠ **số biến đi lại giữa các khối tăng nhanh hơn số khối** | ➕➕ |
| 252 | ⭐ **Ch.31 — Hình 31.1** | *Ai cấp nguồn cho vòng 4–20 mA* — ba cách đấu vẽ cạnh nhau. Đúng tiêu chí B13 (**đường đi của dòng điện**), và là ⚠⚠ **bẫy làm hỏng thiết bị**. Sách nay có **15 hình** | ➕ |

### C — ⭐⭐ Bước 3 của PLCopen xác nhận một điều sách vừa thêm

PLCopen đặt *"chốt mọi tương tác của người vận hành, **mọi cách bỏ qua**, và dữ liệu giám sát"* ở
**bước 3 — TRƯỚC khi phân rã bài toán ở bước 4**.

> ⭐⭐ Nghĩa là các đường **bỏ qua (override)** được coi là **đầu vào của kiến trúc**, không phải thứ
> gắn thêm lúc máy gần xong. ⚡ Đây là **xác nhận độc lập** cho mục 51.7b vừa viết ở đợt 37 — mục đó
> lập luận từ áp lực vận hành, còn PLCopen đi tới cùng kết luận từ phía phương pháp luận.

### D — Hai nguồn rời khỏi danh sách "chưa ai dẫn"

| # | Nguồn | Dùng vào đâu | KQ |
|---|---|:--|:--:|
| 253 | **PLCopen** — *Structuring Program Development with IEC 61131-3* (4 trang) | Ch.27 mục 27.2b. ⭐ Bốn trang, và nó lấp đúng chỗ trống lớn nhất về phương pháp của Ch.27 | ➕➕ |
| 254 | **AutomationDirect** — *PLC Handbook* (85 trang) | Ch.13 mục 13.2b. ⚠ Phần lớn tài liệu là **giới thiệu sản phẩm của hãng**, nhưng chương *How to Choose a Controller* có bảng công tác chín bước dùng được. ⭐ Đây là nguồn duy nhất trong danh sách bị đánh dấu *"nhật ký CHƯA từng nhắc"* — đúng thứ bản đồ nguồn sinh ra để bắt | ➕ |

⭐ Còn **10 nguồn** chưa chương nào dẫn.

### Kết quả đợt 40

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **8** |
| ➕➕ Bổ sung giá trị cao | 4 |
| ➕ Bổ sung | 4 |
| Mục mới trong thân sách | 3 — Ch.13, Ch.27, Ch.52 |
| Mục mới trong phụ lục | 1 — K.5b |
| Hình mới | **1** — sách nay có **15 hình** |
| Nguồn hết "chưa ai dẫn" | 2 (còn 10) |

> ⭐⭐ **Bài học: đo trước, đọc sau.**
>
> Ba lỗ hổng ở phần B **không lộ ra khi đọc**. Ch.52 đọc rất đầy đặn — nó dài trên trung bình và có
> tới mười một mục; ⚠ **chỉ khi đếm mới thấy nó là 1 trong 2 chương thiếu Bảng chốt**. Ch.13 cũng
> vậy: bảy tiêu chí đọc thì thấy đủ, ⭐ **chỉ khi đặt cạnh một bảng công tác của người khác mới thấy
> thiếu ba cái**.
>
> ⚡ **Và nguồn 4 trang lại có giá trị cao hơn nguồn 85 trang.** Tài liệu PLCopen ngắn hơn hai chục
> lần nhưng lấp đúng chỗ trống về phương pháp; tài liệu 85 trang kia phần lớn là giới thiệu sản
> phẩm. ⚠ **Số trang không nói gì về giá trị** — nên danh sách "nguồn chưa ai dẫn" phải đọc **hết**,
> không được sắp theo độ dày rồi đọc từ trên xuống.

---

## Đợt 41 — 2026-09-17 · Đọc nốt nguồn nhỏ, và một câu của sách được NÂNG từ ý kiến lên có nguồn

Tiếp tục đợt 40. Lần này đi vào **ba nguồn nhỏ chưa chương nào dẫn** và **hai chương số liệu còn
chỉ ra** — cộng một phép soát mới do chủ dự án đặt ra ở bộ sách khác.

### A — ⭐⭐ Một nhận định của sách nay có nguồn, và nguồn đến từ chính hãng

| # | Nơi | Nội dung | KQ |
|---|---|:--|:--:|
| 255 | ⭐⭐ **Ch.14 mục 14.6** | Mục này nói *"code không khả chuyển"* và ⚠ **tự ghi chú rằng đó chỉ là quan sát của nghề, không phải phát biểu của tiêu chuẩn**. Nay có nguồn — và nguồn là **tài liệu tuân thủ của một hãng lớn**, không phải người phê bình: *"đây là một điểm yếu của IEC 61131-3, vì chuẩn không định nghĩa định dạng trao đổi tệp"* | ⚠ |

⭐ Đây là kiểu cải thiện đáng giá nhất theo bất biến B2: **không đổi kết luận, chỉ đổi cơ sở của
kết luận** — từ *"theo kinh nghiệm"* thành *"theo tài liệu của chính bên bán"*.

### B — Ba mục mới

| # | Nơi | Nội dung | KQ |
|---|---|:--|:--:|
| 256 | ⭐⭐ **Ch.14 mục 14.6b** — *"tuân thủ IEC" là một BẢNG TÍCH, không phải một dấu tích* | ⚠⚠ **Bộ lệnh mà chuẩn quy định là TUỲ CHỌN**: có hiện thực thì phải làm đúng, nhưng chuẩn **không bắt phải có**, và không cấm hãng thêm lệnh riêng. ⭐ Nên câu hỏi đúng với người bán hàng không phải *"có tuân thủ không"* mà **"cho tôi xem bảng tuân thủ"** — rồi đọc cột *phần mở rộng và ghi chú hiện thực*. ⚡ Trớ trêu: lệnh mở rộng là **lệnh tiện nhất**, nên càng làm nhanh càng dính hãng | ➕➕ |
| 257 | ⭐ Ch.14 mục 14.6b — **PLCopen XML** | Sách từng viết *"không có định dạng chung được dùng rộng rãi"*. Nói đủ hơn: ⭐ **có** một định dạng chung, nhưng nó do **một tổ chức độc lập** làm, ⚠⚠ *"dù đó không phải chủ ý của bản thân chuẩn"*. Kèm ba giới hạn **do chính đặc tả nêu** — nhất là ⚠ *"tệp xuất ra không có kiểm chứng về tính nhất quán hay tính đúng đắn"* | ➕➕ |
| 258 | ⭐⭐ **Ch.30 mục 30.6** — *làm cho nó so sánh được: xuất ra văn bản* | Bảng ở 30.6 liệt kê những thứ **không** so sánh được, rồi dừng ở đó. ⚠ Nhưng đó là giới hạn của **định dạng tệp gốc**, không phải giới hạn không vượt được. Bổ sung ba cách xuất kèm ưu/nhược, và ⭐⭐ ba thứ chỉ có khi bản lưu là văn bản — trong đó có **đọc được bản cũ mà không cần cài đúng phiên bản phần mềm của hãng** | ➕➕ |
| 259 | ⭐⭐ **Ch.50 mục 50.5b** — kiểm thử hồi quy | Mục 50.4 cho danh sách ca cho **lần đầu**. ⚠ Nhưng phần lớn đời sống chương trình là **lần thứ hai mươi**. Bổ sung ba vòng hồi quy theo mức rủi ro, và ⚠ **bốn thay đổi trông vô hại nhưng bắt buộc vòng đầy đủ** — đứng đầu là **đổi firmware: không sửa dòng nào mà nền bên dưới đã đổi** | ➕➕ |
| 260 | ⭐ **Ch.01 mục 1.9b** — Bảng chốt | Chương cuối cùng còn thiếu. ⭐ Nay **58/58 chương đều có Bảng chốt**. Viết thành một trang *"dùng cuốn sách này thế nào"*: bạn thuộc nhóm nào → đọc đường nào → chương nào đừng bỏ qua | ➕ |

### C — Một nguồn mở ra thì thấy **rỗng**

| # | Nguồn | Phát hiện | KQ |
|---|---|:--|:--:|
| 261 | **IO-Link — System Description** (25 trang) | ⚠⚠ Nhật ký từng ghi *"file PDF không trích được text"*. ⭐ **Sai** — text trích được bình thường. Sự thật là tệp này là **bản in một trang web**: toàn menu điều hướng, ⚠ **không một dòng nào dài quá 90 ký tự**, tức là **không có đoạn văn nào**. Không có gì để lấy | ❔ |

⭐ Đã ghi lại để đợt sau **không tra lại nó lần nữa**. ⚡ Bài học nhỏ: *"không đọc được"* và *"đọc
được nhưng rỗng"* là hai kết luận khác nhau, và ghi nhầm thì người sau sẽ đi tìm một công cụ OCR
không cần thiết.

### D — Phép soát mới: luật so sánh áp cho cả phương án MÌNH khuyến nghị

Chủ dự án bổ sung bất biến B18 khi làm ở bộ sách khác: ⭐⭐ **luật "phải so sánh được" áp cho cả
phương án mình đang khuyến nghị, không chỉ các phương án bị loại.**

| # | Phép soát | Kết quả | KQ |
|---|---|:--|:--:|
| 262 | Quét toàn sách các câu *"nên dùng / khuyến nghị / nên chọn / hãy dùng"*, kiểm quanh đó ±14 dòng có bảng so sánh hoặc từ *thay vì / đừng / không nên / đánh đổi / nhược điểm* không | **60 chỗ · 56 có đối chứng · 4 còn lại đọc kỹ đều là báo giả** (một tiêu đề chương, một câu nói *đây KHÔNG phải khuyến nghị chung*, hai câu hỏi tự kiểm). ⭐ **Sách PLC đạt** | ✅ |

### Kết quả đợt 41

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **8** |
| ➕➕ Bổ sung giá trị cao | 4 |
| ➕ Bổ sung | 1 |
| ⚠ Nâng cấp cơ sở của một nhận định cũ | 1 |
| ❔ Nguồn mở ra thấy rỗng | 1 |
| ✅ Soát toàn sách, đạt | 1 |
| Mục mới trong thân sách | 4 — Ch.01, Ch.14, Ch.30, Ch.50 |
| Nguồn hết "chưa ai dẫn" | 2 (còn **8**) |

> ⭐⭐ **Bài học 1 — "đã kiểm, đúng rồi" vẫn còn chỗ để cải thiện: cái ĐÚNG có thể chưa có CƠ SỞ.**
>
> Mục 14.6 không sai một chữ nào, và đã qua nhiều đợt rà. ⚠ Nhưng nó tự ghi chú là *"quan sát của
> nghề"* — và một quan sát của nghề thì **cãi lại được**. ⭐ Nay nó là câu trích từ tài liệu của một
> hãng lớn, và điều đó đổi hẳn sức nặng khi người đọc phải bảo vệ lập luận trước khách hàng.
>
> ⚡ **Bài học 2 — chỗ đáng sửa nhất thường là chỗ sách DỪNG LẠI, không phải chỗ sách nói sai.**
>
> Ba trong bốn mục mới đợt này đều cùng một dạng: sách nêu đúng vấn đề rồi **dừng ở chẩn đoán**.
> Mục 30.6 liệt kê những gì không so sánh được — rồi thôi. Mục 50.4 cho danh sách ca cho lần đầu —
> rồi thôi. Mục 14.6 nói không có định dạng chung — rồi thôi. ⭐ **Cả ba đều có bước tiếp theo**, và
> bước tiếp theo mới là thứ người đọc dùng được.

---

## Đợt 42 — 2026-09-17 · Rà bằng một ống kính mới: chương nào bị CÔ LẬP

Đợt 40 đo **kích thước** từng chương. Đợt này đo **liên kết**: đếm xem mỗi chương **được bao nhiêu
chương khác dẫn tới**. ⭐ Một chương không ai trỏ tới là một chương mà phần còn lại của sách **coi
như không tồn tại** — dù bản thân nó viết tốt.

### A — Kết quả đo

| Chương | Được mấy chương dẫn | Nhận xét |
|---|:--:|---|
| Ch.01 | 1 | ⭐ Bình thường — chương mở đầu |
| ⚠⚠ **Ch.46 — tích hợp robot** | **1** | ⚠ Và chỗ duy nhất đó là dòng *"chương tiếp theo"* ở cuối Ch.45. ⭐⭐ **Không một mục nội dung nào trong cả cuốn sách trỏ tới nó** |
| Ch.56 · Ch.58 | 2 | Chương kết, chấp nhận được |

> ⭐⭐ **Ch.46 bị cô lập là một lỗi thật, và nó không lộ ra bằng cách đọc.** Chương viết đủ và đúng.
> ⚠ Nhưng nghĩa của việc không ai dẫn tới nó là: người đọc Ch.27 (kiến trúc), Ch.28 (phục hồi) hay
> Ch.54 (sao lưu) **sẽ không bao giờ biết rằng có một loại cơ cấu phá vỡ giả định của ba chương đó**.

### B — Đã nối lại, và việc nối làm lộ thêm hai lỗ hổng thật

| # | Nơi | Nội dung | KQ |
|---|---|:--|:--:|
| 263 | ⭐⭐ **Ch.27 mục 27.3** — *khi "cơ cấu" lại là một bộ điều khiển khác* | Quy tắc ba tầng **vẫn giữ**, nhưng ba điều đổi: ⚠⚠ phải **chốt ai chỉ huy ai bằng văn bản trước khi viết dòng đầu** · ⚠ phục hồi khác hẳn vì cơ cấu đó **đang ở giữa chương trình của nó** · ⚠ nó có **dữ liệu phải sao lưu** không nằm trong dự án PLC của bạn | ➕➕ |
| 264 | ⭐⭐ **Ch.54 mục 54.3** — danh mục sao lưu **bảy → tám hạng mục** | Thiếu hẳn hạng mục **chương trình và ĐIỂM DẠY của bộ điều khiển ngoài**. ⭐ Điểm dạy là *dữ liệu nhưng có vai trò như code*: mất nó thì phải dạy lại từng điểm **trên máy thật**, và ⚠ không có cách nào kiểm rằng đã dạy đúng như cũ | ➕➕ |
| 265 | ⚠⚠ **Ch.54 hạng mục 3** — siết lại | Hạng mục *"tham số biến tần/servo"* **không nói tới tham số CHỨC NĂNG AN TOÀN của drive**. Thiếu nó thì ⭐ **máy chạy bình thường, mọi thứ trông đúng, nhưng chức năng an toàn không còn như đã nghiệm thu — và không báo động nào nói điều đó** | ⚠ |

### C — Nguồn mới: cả một họ chức năng mà sách chỉ biết một

| # | Nơi | Nội dung | KQ |
|---|---|:--|:--:|
| 266 | ⭐⭐ **Ch.37 mục 37.6b** | ⚠ Chương servo **không nhắc STO một lần nào** — cả cuốn sách chỉ nói về nó ở Ch.47 mục 47.8. Và Ch.47 để lại một câu hỏi bỏ ngỏ: *"STO không hãm, tải quán tính sẽ trôi, trục đứng thì rơi"* → **vậy dùng gì?** | ➕➕ |
| 267 | ⭐⭐ Ch.37 mục 37.6b — **câu trả lời là cả một họ** | Theo **IEC 61800-5-2**: bốn chức năng dừng (STO · SS1 · SS2 · SOS) và mười ba chức năng giới hạn/công bố. ⭐⭐ Khác biệt đáng nhớ nhất: **SS1 kết thúc bằng STO — hết mô-men**, còn **SS2 kết thúc bằng SOS — CÒN mô-men để giữ chỗ**. ⚡ Với trục đứng, chọn nhầm SS1 nghĩa là *máy dừng êm, đúng quy trình, rồi trục rơi* | ➕➕ |
| 268 | ⭐ Ch.37 mục 37.6b — **SLS mở ra lựa chọn thứ ba** | Dạy điểm, căn chỉnh, gỡ kẹt — người phải vào vùng máy mà trục cần **vẫn nhúc nhích được**. ⚠ Chỉ có STO thì chỉ còn *cắt hẳn* (không làm được việc) hoặc *chạy đủ tốc* (không an toàn). ⭐ **SLS**: cho chạy, nhưng tốc độ bị **phần cứng an toàn** chặn — ghép **SDI** thì chặn được cả chiều | ➕➕ |

⭐ Nguồn: **PLCopen Safe Motion v1.0** — rời khỏi danh sách "chưa ai dẫn". Còn **7 nguồn**.

> ⚠ Mục 37.6b **chỉ giới thiệu từ vựng**. Chọn chức năng nào, mức toàn vẹn nào, kiến trúc nào — là
> kết quả **đánh giá rủi ro của người có thẩm quyền** (Chương 47). ⭐ Mục đích là để người đọc **biết
> những gì tồn tại mà hỏi cho đúng**, thay vì mặc định STO là lựa chọn duy nhất.

### D — ⚠ Bộ kiểm bỏ lọt một vi phạm B8 THẬT của tôi

| # | Phát hiện | KQ |
|---|:--|:--:|
| 269 | Bản đầu của mục 27.3 mới **gọi thẳng tên "robot" và "tay gắp"** trong một chương **lát cắt 2**. ⚠⚠ Bộ kiểm **không báo** — vì hai từ đó **không có trong từ vựng lát cắt** của `cau_hinh_kiem_tra.json`. ⭐ Tôi tự phát hiện khi đối chiếu lại B8, không phải nhờ công cụ | ⚠ |

⭐ Đã sửa hai việc:

| | |
|---|---|
| 1 | Viết lại mục 27.3 **không gọi tên thiết bị lát cắt sau** — giữ nguyên luận điểm kiến trúc, và **giữ dẫn chiếu tới Ch.46** (dẫn chiếu tới chương sau thì được, gọi tên thiết bị thì không) |
| 2 | ⭐ Bổ sung từ vựng cho bộ kiểm: **`robot`, `tay gắp`** vào lát cắt 4; **`SS1 SS2 SOS SLS SDI SBC SLP`** vào lát cắt 3 — cùng lý do với `STO`: chúng là **tính năng của truyền động** |

⚡ Đã thử lại trên bốn ca dựng sẵn: báo đúng khi dùng sớm (Ch.27 + *robot*, Ch.27 + *SS1*), im đúng
khi dùng đúng chỗ (Ch.37 + *SS1*, Ch.46 + *robot*).

### Kết quả đợt 42

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **7** |
| ➕➕ Bổ sung giá trị cao | 5 |
| ⚠ Siết lại nội dung cũ | 1 |
| ⚠ Lỗi của tôi mà công cụ bỏ lọt | 1 |
| Mục mới trong thân sách | 2 — Ch.27, Ch.37 |
| Từ vựng mới cho bộ kiểm | 9 từ |
| Nguồn hết "chưa ai dẫn" | 1 (còn **7**) |
| ⭐ Ch.46 nay được **3 chương** dẫn tới | |

> ⭐⭐ **Bài học 1 — "chương viết tốt" và "chương có ích" là hai chuyện khác nhau.**
>
> Ch.46 không thiếu gì cả: đủ mục, đủ bẫy, đủ Bảng chốt, qua mọi bộ kiểm. ⚠ Nó chỉ thiếu **đường
> dẫn vào**. Người đọc Ch.54 lập danh mục sao lưu sẽ lập thiếu một hạng mục, và **không có gì trong
> Ch.54 báo cho họ biết điều đó** — cho tới đợt này.
>
> ⚡ **Bài học 2 — việc NỐI hai chương lại làm lộ ra lỗ hổng ở CHƯƠNG KIA.**
>
> Mục tiêu ban đầu chỉ là thêm dẫn chiếu tới Ch.46. Nhưng để viết được dẫn chiếu ấy, phải trả lời
> *"Ch.54 nói gì về dữ liệu của bộ điều khiển ngoài"* — và câu trả lời là **không nói gì**. ⭐ Hai
> hạng mục đắt nhất đợt này (264, 265) tìm được theo cách đó, **không phải bằng cách đọc Ch.54**.
>
> ⭐ **Bài học 3 — công cụ chỉ bắt được thứ đã có trong từ điển của nó.** Bộ kiểm B8 chạy đúng suốt
> mười mấy đợt, nhưng nó không biết từ *"robot"*. ⚠ Nghĩa là số lần nó báo **không** đo được số lần
> nó đúng. Mỗi lần thêm nội dung vào một lĩnh vực mới, phải hỏi: ⭐ **từ vựng của bộ kiểm đã có lĩnh
> vực đó chưa?**

---

## Đợt 43 — 2026-09-17 · Phán quyết về Rabiee, và ba lỗ hổng do MỤC LỤC nguồn chỉ ra

Hai việc: **quyết dứt điểm** có đọc tài liệu Rabiee 446 trang hay không, và **soi mục lục các sổ tay
lệnh của hãng** xem có chủ đề nào sách chưa có.

### A — ⭐ Rabiee: đọc mục lục xong, KẾT LUẬN KHÔNG ĐỌC TIẾP

| # | Việc | Kết quả | KQ |
|---|---|:--|:--:|
| 270 | Tệp là **bản quét thuần** — mỗi trang một ảnh, **không có lớp văn bản, không có mục lục nhúng**. Máy không cài công cụ OCR nào | ⭐ Không cần cài: **kết xuất mấy trang mục lục thành ảnh rồi đọc trực tiếp** — nhanh hơn và đủ chính xác cho việc quyết định | ✔ |
| 271 | Đối chiếu **18 chương** của Rabiee với sách | ⭐ **16/18 chương trùng chủ đề đã có**, và tài liệu gắn chặt nền **Rockwell SLC 500 / RSLogix** với bài thực hành trên phần mềm mô phỏng riêng. ⚠ Phần vendor-neutral của nó **không thêm gì** cho một cuốn sách trung lập hãng | ❔ |

> ⭐⭐ **Phán quyết: KHÔNG OCR và KHÔNG đọc tiếp. Ghi vào đây để đợt sau không cân nhắc lại.**
>
> ⚡ Nhưng **chính mục lục ấy đã trả công cho nửa giờ bỏ ra**: hai chương của nó — *Compare, Jump và
> MCR* và *Sequencer Instructions* — chỉ vào **hai chủ đề mà cả cuốn sách này không có một dòng nào**.
> ⭐ Bài học: **đọc mục lục một nguồn là việc rẻ và nên làm, kể cả khi kết luận là không đọc nguồn đó.**

### B — Ba chủ đề sách thiếu hẳn, tìm ra từ mục lục

Đối chiếu chéo với mục lục **sổ tay lệnh Mitsubishi FX5** (1 470 trang) và **Inovance H5U**
(1 113 trang) cho thấy cả ba đều là **chủ đề liên hãng**, không phải đặc sản một hãng:

| # | Nơi | Nội dung | KQ |
|---|---|:--|:--:|
| 272 | ⚠⚠ **Ch.15 mục 15.4b** — vùng điều khiển `MCR` | Cả sách **không nhắc `MCR` một lần nào**, trong khi Rockwell, Mitsubishi (*Master Control Instruction*) và Inovance (*MC/MCR*) đều có. ⭐⭐ Và nó mang **một cái tên trùng nguy hiểm**: `MCR` = *Master Control Relay*, ⚠ **cùng cụm từ** với **mạch cắt nguồn bằng phần cứng** | ➕➕ |
| 273 | ⚠⚠ Ch.15 mục 15.4b — **hai thứ trùng tên, ngược nhau về bản chất** | Lệnh `MCR` ⚠ **không cắt gì cả** — nó chỉ làm logic trong vùng ngừng chạy, và **chạy trong cùng CPU** nên **CPU treo thì nó treo theo**. Nhầm lẫn kinh điển: *"trạm này nằm trong vùng MCR rồi nên an toàn"* | ➕➕ |
| 274 | ⭐ Ch.15 mục 15.4b — ba hành vi **phải tra, không được đoán** | Ngõ ra **chốt** (SET/RESET) trong vùng thường **giữ nguyên**, không tắt · timer trong vùng **khác nhau giữa các hãng** · vùng lồng nhau **có hệ cho, có hệ không** | ➕ |
| 275 | ⭐⭐ **Ch.25 — "Chọn cách nào"** thêm **cột thứ ba** | Bảng so sánh cách hiện thực máy trạng thái chỉ có hai cột (*Biến + `CASE`* · *Bit trạng thái*), ⚠ **thiếu hẳn nhóm lệnh tuần tự của hãng** (*step ladder · sequencer · drum*) — thứ có ở cả Mitsubishi (3.4 *Step Ladder*) lẫn Inovance (4.3.2 *STL*). ⭐ Đúng một ca của bất biến **B18**: bảng so sánh thiếu một phương án thì bảng đó chưa đủ | ➕➕ |
| 276 | ⭐ Ch.25 — hàng mới trong bảng: **khả chuyển sang hãng khác** | Nhóm lệnh tuần tự có ưu điểm thật (**bất biến "chỉ một bước hoạt" do chính lệnh bảo đảm**), nhưng ⚠⚠ **khả chuyển bằng không** — và cái giá đó **chỉ hiện ra ở dự án sau** (Chương 14 mục 14.6b) | ➕➕ |
| 277 | ⚠⚠ **Ch.10** — lệnh nạp lại watchdog | Bảng khác biệt giữa các hãng có nhắc lệnh `WDT`, nhưng ⚠ **không cảnh báo cách nó bị lạm dụng**: chương trình chạm ngưỡng watchdog → thêm một lệnh nạp lại vào giữa → cảnh báo biến mất. ⭐⭐ **Vòng quét vẫn dài y như cũ; thứ duy nhất mất đi là cái báo cho bạn biết** | ➕➕ |

### Kết quả đợt 43

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **8** |
| ➕➕ Bổ sung giá trị cao | 5 |
| ➕ Bổ sung | 1 |
| ❔ Nguồn quyết định **không đọc tiếp** | 1 (Rabiee, 446 trang) |
| Mục mới trong thân sách | 1 — Ch.15 mục 15.4b |
| Mục cũ được mở rộng | 2 — Ch.25 (bảng so sánh), Ch.10 (watchdog) |

> ⭐⭐ **Bài học 1 — mục lục của một nguồn có giá trị RIÊNG, tách khỏi nội dung của nó.**
>
> Rabiee là bản quét, gắn chặt một hãng, và 16/18 chương trùng thứ sách đã có — ⭐ **đúng là không
> đáng đọc**. Nhưng danh sách 18 tiêu đề của nó là một **danh mục kiểm tra chủ đề** do người khác
> lập, và đối chiếu nó với sách mất nửa giờ mà ra **hai lỗ hổng thật**.
>
> ⚡ Điều đó đổi cách nên xử lý danh sách *"nguồn chưa ai dẫn"*: ⚠ đừng hỏi *"có nên đọc tài liệu
> này không"* — hãy hỏi ⭐ **"mục lục của nó có tên chương nào mà sách mình không có không"**. Câu
> thứ hai rẻ hơn nhiều lần và trả lời được cho **cả** những nguồn không đáng đọc.
>
> ⭐ **Bài học 2 — chỗ nguy hiểm nhất của đợt này là một CÁI TÊN.**
>
> Mục 15.4b không dạy một kỹ thuật mới; nó gỡ một **trùng tên**. `MCR` vừa là một lệnh phần mềm
> không cắt được gì, vừa là tên một **mạch phần cứng cắt nguồn thật**. ⚠⚠ Hai thứ ngược nhau về bản
> chất, và một trong hai liên quan tới tính mạng. ⭐ Sách trung lập hãng mà bỏ qua trùng tên kiểu này
> là bỏ qua đúng thứ người đọc sẽ gặp trong tài liệu của mọi hãng.

---

## Đợt 44 — 2026-09-17 · Soát ví dụ minh hoạ, và trả lời câu "khối nào dùng lại được"

Ba việc: **soát xem chỗ nào thiếu ví dụ**, **đối chiếu thư viện khối của bốn cỗ máy thật**, và
**nói rõ khối nào hãng/chuẩn đã có**.

### A — Soát: chỗ nào nhắc tới mà không có ví dụ, bảng hay hình

⭐ Đếm theo **mục** (không theo chương): mục nào dài từ 260 từ trở lên mà **không có khối code, không
bảng, không hình** thì đánh dấu.

| Kết quả | |
|---|---|
| Tổng số mục bị đánh dấu | **13** trên khoảng 700 mục |
| ⭐ Trong đó **cố ý là văn xuôi** | 12 — mở đầu kể chuyện (*"Bài toán…"*), lộ trình đọc ở Ch.1, và các danh mục kiểm ở Phụ lục D (bản thân danh sách **là** minh hoạ) |
| ⚠ **Thiếu thật** | **1** |

| # | Nơi | Vấn đề | KQ |
|---|---|:--|:--:|
| 278 | ⚠ **Ch.51 mục 51.8** — bốn nguyên nhân lỗi chập chờn | 626 từ, **bốn** nguyên nhân kể liền nhau bằng văn xuôi, ⚠ **không có bảng chốt** — vi phạm B14. Đã thêm bảng phân biệt **theo câu hỏi "lỗi xuất hiện KHI NÀO"**, vì đó là thứ tách bốn nguyên nhân ra rõ nhất | ➕ |

⭐ Kết luận chung: **sách đạt** ở tiêu chí này. ⚡ Và cách đo đáng giữ lại — nó rẻ, và nó phân biệt
được *"văn xuôi có chủ ý"* với *"quên minh hoạ"* chỉ bằng một lần đọc lại 13 mục.

### B — ⭐⭐ Bốn cỗ máy, một thư viện: con số

Đối chiếu danh sách khối chức năng của **bốn chương trình máy thật** của cùng một nhóm kỹ thuật:

| | Kết quả |
|---|---|
| ⭐⭐ Khối **giống hệt ở CẢ BỐN máy** | **25 / 27** |
| Khối chỉ có ở một số máy | 2 (hai khối chuyển đổi bit ↔ byte) |

> ⭐⭐ Đây là số đo cho luận điểm ở Chương 30 mục 30.5: **công viết thư viện trả hết ở máy thứ hai**,
> từ máy thứ ba là lãi. ⚡ Và nó cho thấy phần đặc thù của một cỗ máy nhỏ hơn nhiều so với cảm giác.

### C — ⭐⭐ Phụ lục L.17 — danh mục khối: cái nào tự viết, cái nào đã có sẵn

| # | Nơi | Nội dung | KQ |
|---|---|:--|:--:|
| 279 | ⭐⭐ **Phụ lục L.17** | Chia thư viện làm **ba nhóm** theo đúng câu hỏi *"thứ này đã có ai làm chuẩn chưa?"* | ➕➕ |
| 280 | ⚠ **Nhóm 1 — chuẩn đã có, đừng viết lại** | Trong thư viện thật có ít nhất **bốn khối viết lại thứ chuẩn IEC đã có**: khối trễ (`TON`/`TOF`), khối bắt cạnh (`R_TRIG`/`F_TRIG`), khối dịch bit (`SHL`/`SHR`), và khối so sánh hai **số nguyên** bằng nhau (chỉ cần `=`). ⭐ Ngoại lệ đáng giữ: **so sánh hai số THỰC có dung sai** — chuẩn không có, và nó là bẫy thật (Ch.19 mục 19.5) | ➕➕ |
| 281 | ⚠⚠ **Nhóm 2 — tuyệt đối không tự viết** | Thư viện thật có một **khối điều khiển hai tay tự viết**. ⭐ PLCopen Safety đã chuẩn hoá nó thành `SF_TwoHandControlTypeII` / `TypeIII` — và quan trọng hơn, ⚠⚠ **chức năng này phải chạy trên phần cứng an toàn**, không phải trong CPU thường | ➕➕ |
| 282 | ⭐ **Nhóm 3 — nên tự viết** | Mười hai loại khối thật sự đáng có, ⭐ **và sách đã có mẫu cho gần hết**: L.8 xy-lanh · L.15 chân không · L.9 chuyển động · L.16 tuổi thọ vật tư · Ch.41 41.7b kho đệm · K.7b lưới khay · Ch.55 55.7c đồng hồ máy và thống kê | ➕ |
| 283 | ⭐ **Bốn câu hỏi trước khi thêm một khối vào thư viện** | Chuẩn có chưa · ⚠⚠ **có phải chức năng an toàn không** · hãng có chưa · ⭐ **nó có xuất hiện ở máy thứ hai không** — nếu không thì viết thẳng trong chương trình máy đó, đừng nhét vào thư viện | ➕ |

### D — ⭐⭐ Ch.47 mục 47.7b: lấp nốt lỗ hổng đã treo từ đợt 37

| # | Nơi | Nội dung | KQ |
|---|---|:--|:--:|
| 284 | ⭐⭐ **Ch.47 mục 47.7b** | Đợt 37 ghi: *"điều khiển hai tay — Ch.47 mới có một dòng trong bảng; ⚠ cần MUA tiêu chuẩn mới viết được"*. ⭐ **Giải được một nửa mà không cần mua**: PLCopen Safety cho **đặc tả HÀNH VI** và tên khối chuẩn; thứ phải mua chỉ là **các CON SỐ** (cửa sổ đồng thời, khoảng cách đặt nút) | ➕➕ |
| 285 | ⭐ Ch.47 mục 47.7b — bảng **14 khối an toàn chuẩn** | `SF_EmergencyStop` · `SF_Guard` · `SF_GuardLocking` · `SF_ESPE` · `SF_MutingSeq/Par` · `SF_TwoHandControl…` · `SF_ModeSelector` · ⭐ `SF_Override` · `SF_EnableSwitch` · `SF_EDM` · `SF_ResetButton` · `SF_SafetyRequest` · `SF_Equivalent/Antivalent` · `SF_OutControl` | ➕➕ |
| 286 | ⭐⭐ Ch.47 mục 47.7b — **năm yêu cầu của điều khiển hai tay**, và bốn cái hay bị quên | Bản tự viết thường chỉ làm vế đầu (*nhấn cả hai trong một cửa sổ*). ⚠⚠ Hay thiếu: **phải NHẢ CẢ HAI rồi mới được bắt đầu lần sau** — thiếu nó thì **kẹp một nút lại là xong**; nhả một nút phải dừng ngay; phát hiện nút kẹt dính; nói được lý do từ chối | ➕➕ |

> ⚠ Vẫn giữ nguyên cờ ⚠ của Ch.47. Mục mới là **từ vựng**, không phải thiết kế — và nó ghi rõ rằng
> có tên khối chuẩn **không** làm cho bản tự viết trong CPU thường trở nên an toàn.

### E — Về việc mở chương trình bằng phần mềm

| # | Việc | Kết quả | KQ |
|---|---|:--|:--:|
| 287 | Kiểm xem có mở được chương trình PLC bằng phần mềm của hãng không | ⚠ **Không** — máy chỉ có một gói thư viện an toàn của hãng, **không có phần mềm lập trình**. ⭐ Nhưng cũng **không cần**: phần đọc được (kiểu dữ liệu, giao diện khối, danh sách khối, cây thư mục) đã đủ cho mọi kết luận ở trên; phần không đọc được là **thân khối đã nén**, mà thân khối thì ⚠ **không nên chép sang sách** dù có đọc được | ✔ |

### Kết quả đợt 44

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **10** |
| ➕➕ Bổ sung giá trị cao | 6 |
| ➕ Bổ sung | 3 |
| Mục mới | 2 — Phụ lục L.17, Ch.47 mục 47.7b |
| Bảng chốt mới | 1 — Ch.51 mục 51.8 |
| ⚠ Việc treo từ đợt 37 **đã gỡ một nửa** | điều khiển hai tay |

> ⭐⭐ **Bài học 1 — câu hỏi hay nhất về một thư viện không phải "có gì trong đó" mà "cái nào lẽ ra
> không nên có".**
>
> Thư viện thật có 27 khối và **25 dùng lại được ở cả bốn máy** — nghe rất tốt. ⚠ Nhưng soi kỹ thì ít
> nhất **bốn khối là viết lại thứ chuẩn IEC đã có**, và **một khối là chức năng an toàn nằm sai
> chỗ**. ⭐ Cái sau không phải chuyện lãng phí công — nó là chuyện an toàn.
>
> ⚡ **Bài học 2 — một việc bị chặn vì "phải mua tiêu chuẩn" đôi khi chỉ bị chặn MỘT NỬA.**
>
> Đợt 37 tôi gác lại điều khiển hai tay vì không có tiêu chuẩn để lấy số. ⭐ Nhưng thứ người đọc cần
> nhất **không phải con số** — mà là **danh sách những gì bản tự viết hay quên**, nhất là *"phải nhả
> cả hai nút"*. Phần đó có nguồn mở, và nó nằm ngay trong bộ tài liệu suốt thời gian qua.
> ⚠ **Bài học về quy trình: khi gác một việc lại, hãy ghi rõ CÁI GÌ bị chặn — không phải chặn cả mục.**

---

## Đợt 45 — 2026-09-17 · ⭐⭐ Chủ dự án đọc mã và chỉ ra: chương trình thật đánh CHỈ SỐ, không đặt tên

Nhận xét của chủ dự án sau khi đọc các dự án ví dụ: *"chương trình viết theo chỉ số mảng chứ không
phải dạng tag như sách nhắc đến"*. ⭐ **Nhận xét đúng, và nó chỉ ra một chỗ sách trình bày gây hiểu
nhầm.**

### A — Đọc kỹ: không phải "không có tag", mà là BA TẦNG, ba quy ước

| # | Phát hiện | KQ |
|---|:--|:--:|
| 288 | ⭐ Khối dữ liệu I/O là **bản sao địa chỉ vật lý**: `InX0[0..7]` … `InX370[7]`, `OutY0[0]` … ⚡ Để ý dãy số **nhảy từ 70 sang 100** — đó là **bát phân**, đúng quy ước địa chỉ mà Phụ lục A1 đã cảnh báo | ✔ |
| 289 | ⭐⭐ Khối dữ liệu trình tự: **732 biến, 647 trong đó là phần tử mảng** (~88 %) — `STSignal[0..20].Condition`, `STSignal[i].done[0..9]`, `AxisAlarm[0..20]`, `CylinderAlarm[0..34]` | ✔ |
| 290 | ⭐ Nhưng tầng logic riêng của máy **vẫn dùng tên mô tả** — có tiền tố kiểu (`b`, `x`, `i`) và viết bằng tiếng bản địa | ✔ |

⭐ **Kết luận: đây không phải "không dùng tag". Đây là BA quy ước dùng ở BA tầng khác nhau** — và
mỗi lựa chọn đều có lý ở tầng của nó.

### B — ⭐⭐ Đo được kỷ luật "địa chỉ tuyệt đối chỉ ở tầng khai báo"

Nguyên tắc PLCopen thêm vào Chương 27 mục 27.2b ở đợt 40 là **kiểm được**. Đã kiểm bằng bảng tham
chiếu chéo của chính dự án:

| # | Phép đo | Kết quả | KQ |
|---|---|:--|:--:|
| 291 | Tag I/O thô (`InX*` / `OutY*`) xuất hiện ở những chương trình con nào | ⭐⭐ **148 / 158 lần (94 %) nằm trong ĐÚNG chương trình con gán chân.** Phần còn lại: **một** chương trình con trao đổi dữ liệu với hệ trên, đọc thẳng một byte vào/ra | ✔ |

> ⭐ Con số này đáng giá gấp đôi: nó cho thấy kỷ luật **giữ được trong thực tế**, và nó cho thấy
> ⚠ **rò rỉ luôn có, luôn kèm một lý do nghe hợp lý lúc đó**.

### C — Chỗ sách trình bày gây hiểu nhầm, đã sửa

| # | Nơi | Nội dung | KQ |
|---|---|:--|:--:|
| 292 | ⚠ **Ch.30 mục 30.2** | Bày bốn quy ước **cạnh nhau như bốn lựa chọn cho cả chương trình** — ⭐ đúng thông tin, nhưng ⚠ gây hiểu nhầm rằng phải chọn **một** | ⚠ |
| 293 | ⭐⭐ **Ch.30 mục 30.2b** (mới) | *Quy ước chọn cho TỪNG TẦNG*: bảng ba tầng thật kèm ví dụ thật, và câu trả lời cho *"vì sao tầng khung BUỘC phải đánh chỉ số"* — ⭐⭐ **không thể viết một khối rồi tạo 30 thể hiện nếu mỗi thiết bị có một tên viết tay**. Thư viện dùng lại và tên riêng cho từng thiết bị là **hai thứ loại trừ nhau ở tầng đó** | ➕➕ |
| 294 | ⚠⚠ Ch.30 mục 30.2b — **cái giá, và nó nặng hơn vẻ ngoài** | Với tên mô tả, mất hết tài liệu thì **cái tên chính là tài liệu**. ⭐ Với chỉ số, mất bảng tra là **mất khả năng đọc** — thấy `[12]` báo lỗi mà không biết `[12]` là cơ cấu nào. ⚡ Nên **bảng tra chỉ số trở thành một phần của chương trình**, và phải nằm trong danh mục sao lưu (Ch.54 mục 54.3) | ➕➕ |
| 295 | ⭐ Ch.30 mục 30.2b — **cách KIỂM** | Chạy tham chiếu chéo trên một tag I/O thô, đếm số chương trình con. Ba mức kết quả và nghĩa của từng mức. ⭐ Biến một lời khuyên thành **một phép đo** | ➕➕ |
| 296 | **Ch.30** — thuật ngữ | ⚠ Bộ kiểm bắt một lỗi nhỏ của tôi: *cross-reference* bị dịch hai kiểu (**tra chéo** vs **tham chiếu chéo**) — ⭐ bản sai là do **chính tôi** viết ở đợt 40. Đã thống nhất theo Ch.22 mục 22.3 | ⚠ |

### Kết quả đợt 45

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **9** |
| ➕➕ Bổ sung giá trị cao | 3 |
| ⚠ Sửa chỗ trình bày gây hiểu nhầm | 1 |
| Mục mới | 1 — Ch.30 mục 30.2b |

> ⭐⭐ **Bài học: người đọc ngoài nhìn ra thứ người viết không nhìn ra — vì người viết biết mình
> ĐỊNH nói gì.**
>
> Mục 30.2 không sai một chữ. ⚠ Nhưng nó bày bốn quy ước theo kiểu thực đơn, nên người đọc hiểu là
> **chọn một**. ⭐ Chỉ khi đặt nó cạnh một chương trình thật mới thấy: thực tế **dùng ba cái cùng
> lúc**, và câu hỏi hay không phải *"chọn cái nào"* mà là ⭐⭐ **"ở tầng này, ai là người đọc?"**
>
> ⚡ Và nhận xét đó đến từ việc **đọc mã**, không từ việc đọc sách. ⭐ Đây là lý do tại sao đối chiếu
> với chương trình thật có giá trị mà đối chiếu với tài liệu không thay thế được.

---

## Đợt 46 — 2026-09-18 · Tham chiếu chéo khi mọi thứ là chỉ số; và khảo sát 16 dự án Mitsubishi

Hai câu hỏi của chủ dự án: ⭐ *"làm sao dùng tham chiếu chéo với máy lớn mà gần như hầu hết nội dung
là chỉ số, mà không bị nhầm"*, và ⭐ *"có vẻ một số chương trình Mitsubishi dùng địa chỉ trực tiếp
chứ không dùng tag"*.

### A — ⭐⭐ Sách nêu đúng giới hạn rồi DỪNG LẠI ở đó

| # | Phát hiện | KQ |
|---|:--|:--:|
| 297 | ⚠ **Ch.22 mục 22.3** có đúng một gạch đầu dòng: *"không tìm được chỗ ghi gián tiếp qua chỉ số mảng tính toán được"* — rồi **hết**. ⭐ Đúng chẩn đoán, ⚠ **không có bước tiếp theo** — đúng dạng lỗ hổng đã nhận ra ở đợt 41 | ⚠ |

### B — Ch.22 mục 22.3b (mới): bảy cách làm việc

| # | Nội dung | KQ |
|---|:--|:--:|
| 298 | ⭐⭐ **Hai kiểu chỉ số làm hỏng tham chiếu chéo theo hai cách khác nhau**: chỉ số vào mảng (`Cyl[i]`) và **thanh ghi chỉ số** (`D100Z1`). ⭐ Điểm chung: **thứ bạn muốn tra KHÔNG XUẤT HIỆN trong mã** — nên không công cụ nào tìm được | ➕➕ |
| 299 | ⭐⭐ **Cách ①: tra theo TRƯỜNG, đừng tra theo phần tử.** Đổi *"ai ghi vào `Cyl[12].Cmd.Req`"* thành *"có mấy nơi ghi vào `.Cmd.Req` của bất kỳ cái nào"*. ⚡ Nghe rộng hơn nhưng thực tế **hẹp lại**: chương trình có kỷ luật chỉ có hai–ba nơi. ⭐⭐ Và nếu ra **mười lăm** thì bạn vừa tìm ra vấn đề thật — nó không phải vấn đề của số 12 | ➕➕ |
| 300 | ⭐ **Cách ②: tra biến CHỈ SỐ, không tra mảng.** Chỉ số đến từ vòng lặp chạy hết dải → "ai ghi" = vòng lặp đó, **xong**. Đến từ ngoài → tra chính biến đó | ➕➕ |
| 301 | ⭐ **Cách ③: chỉ số cố định phải là HẰNG CÓ TÊN** — `Cyl[CYL_CLAMP_STN1]` thay cho `Cyl[12]`. ⭐⭐ Một dòng khai báo **lấy lại toàn bộ sức mạnh của tham chiếu chéo** cho phần tử đó | ➕➕ |
| 302 | Cách ④ đọc chương trình con cấu hình trước · ⑤ tìm chỉ số **cứng** trong bản xuất văn bản · ⑥ chuyển sang xem trực tuyến khi tra tĩnh bó tay · ⑦ bốn luật cho người viết | ➕ |
| 303 | ⚠⚠ **Cạm bẫy nặng nhất: chỉ số ngoài dải KHÔNG sai cú pháp.** `Cyl[30]` khi mảng có 20 phần tử vẫn biên dịch. Tuỳ hệ: dừng CPU, hoặc ⚠⚠ **ghi đè vùng nhớ bên cạnh** — một cơ cấu **khác hẳn** nhận lệnh, và ⭐ **tham chiếu chéo không bao giờ chỉ ra được**. Đây mới là lý do thật của việc chặn dải | ➕➕ |

### C — ⭐ Khảo sát 16 chương trình Mitsubishi: nhận xét của chủ dự án ĐÚNG

Giải nén tệp dự án (là **tệp nén** chứa cơ sở dữ liệu SQLite) và đếm trực tiếp:

| # | Phép đo | Kết quả | KQ |
|---|---|:--|:--:|
| 304 | Số **nhãn/biến** khai báo so với số **chú thích thiết bị** người viết đặt, trên **16 dự án** | ⭐⭐ **15/16 dự án có đúng cùng một con số nhãn** — tức là **người viết không khai báo biến nào**; trong khi chú thích thiết bị chạy từ **0 tới hơn 200** mỗi dự án | ✔ |
| 305 | Kiểu đặt tên thực tế | ⭐ Dùng thẳng `X3` · `Y5` · `M20` · `D13`, ý nghĩa nằm trong **chú thích thiết bị**. ⚡ Và trong bảng thanh ghi có cả `i_Index`, `n_index`, `j_index` — nghĩa là **còn chồng thêm chỉ số lên địa chỉ trực tiếp** | ✔ |
| 306 | ⭐ Phát hiện phụ về công cụ | Tệp dự án chứa sẵn một **kho quản lý phiên bản** bên trong, và một bảng riêng cho **vùng `MC`/`MCR`** — ⭐ xác nhận mục 15.4b viết ở đợt 43 là chủ đề có thật, không phải chuyện của riêng một hãng | ✔ |

### D — Ch.30 mục 30.2b: thêm kiểu thứ ba

| # | Nội dung | KQ |
|---|:--|:--:|
| 307 | ⭐⭐ Mục 30.2b trước chỉ có hai tầng dựa trên **một** chương trình. Nay thêm **kiểu thứ ba — không khai báo biến nào**, với số liệu từ 16 dự án. ⭐ Kèm nghịch lý đáng chú ý: ⚠ kiểu này làm **tham chiếu chéo chạy RẤT TỐT** (địa chỉ là chuỗi có thật trong mã) nhưng ⚠⚠ **chú thích gắn với ĐỊA CHỈ chứ không gắn với ý nghĩa** | ➕➕ |
| 308 | ⭐⭐ **Bảng ba kiểu, phân biệt bằng một câu hỏi: "mất tài liệu thì còn đọc được không?"** — tên mô tả: **còn** (cái tên chính là tài liệu) · mảng chỉ số: **mất** bảng tra · địa chỉ + chú thích: **mất** tệp chú thích. ⚡ Hai kiểu sau biến **một tệp phụ thành một phần không thể thiếu của chương trình** | ➕➕ |

### Kết quả đợt 46

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **12** |
| ➕➕ Bổ sung giá trị cao | 7 |
| ➕ Bổ sung | 1 |
| Mục mới | 1 — Ch.22 mục 22.3b |
| Mục mở rộng | 1 — Ch.30 mục 30.2b |
| Dự án thật đã khảo sát | **16** (Mitsubishi) + 4 (đợt trước) |

> ⭐⭐ **Bài học 1 — câu hỏi hỏng chứ không phải công cụ hỏng.**
>
> *"Tham chiếu chéo vô dụng với mảng"* là kết luận sai. ⭐ Đúng hơn: **hỏi sai câu**. Hỏi *"ai ghi
> vào số 12"* thì công cụ chịu; hỏi *"có mấy nơi ghi vào trường này"*, *"chỉ số nhận giá trị ở
> đâu"*, *"bảng tra nằm ở đâu"* thì **cùng một công cụ** trả lời hết. ⚡ Nên mục mới đặt tên các
> **câu hỏi**, không đặt tên các nút bấm.
>
> ⭐ **Bài học 2 — một nhận xét cảm tính của người đọc thường ĐO ĐƯỢC.**
>
> Chủ dự án nói *"có vẻ một số chương trình Mitsubishi dùng địa chỉ trực tiếp"*. ⚡ Thay vì đồng ý
> hay phản bác, tôi giải nén 16 dự án và **đếm**: 15/16 không khai báo biến nào. ⭐ Kết quả biến một
> cảm nhận thành **một dòng số liệu dùng được trong sách** — và nó mạnh hơn hẳn cách viết *"nhiều
> chương trình vẫn dùng địa chỉ trực tiếp"*.

---

## Đợt 47 — 2026-09-18 · Bổ sung bản LADDER cho thư viện mẫu code

Yêu cầu của chủ dự án: ⭐ *"thêm các ví dụ viết bằng ladder để tham khảo, chứ không chỉ dùng ST"*.

### A — ⚠ Phụ lục L tự mâu thuẫn với chính mình

| # | Phát hiện | KQ |
|---|:--|:--:|
| 309 | ⚠ Khung mở đầu Phụ lục L **khuyên** *"với logic liên động và ngõ ra cuối, cân nhắc viết bằng ladder để người bảo trì đọc được"* — nhưng ⭐ **cả 16 mẫu đều chỉ có ST**. Khuyên một đằng, làm một nẻo | ⚠ |

### B — Bảy mẫu nay có **cả hai bản**

⭐ Dùng đúng bộ ký hiệu ASCII đã có trong sách từ Chương 15: `┤ ├` tiếp điểm thường mở · `┤/├` thường
đóng · `( )` cuộn dây · `( S )` / `( R )` cuộn chốt. ⭐ Thêm hai ký hiệu mới, có định nghĩa tại chỗ:
**`┤P├` / `┤N├`** (tiếp điểm bắt cạnh) và **hộp khối chức năng** vẽ bằng ký tự khung.

| # | Mẫu | ⭐ Vì sao ladder đáng có ở đây | KQ |
|---|---|:--|:--:|
| 310 | **L.1** tự giữ | ⭐⭐ **Nhánh tự giữ NHÌN THẤY ĐƯỢC.** ⚠ Trong ST, dấu ngoặc đặt sai chỗ **trông vẫn bình thường**; trong ladder, nhánh ôm nhầm nút Dừng thì **nhìn là thấy** | ➕➕ |
| 311 | **L.2** chuỗi cho phép | ⭐⭐ Một nấc thang — khi máy không chạy, mở màn theo dõi là **thấy ngay tiếp điểm nào hở**, không cần biết lập trình. ⭐ Nhưng phần mã lý do chặn **để nguyên ST** — ví dụ điển hình của trộn đúng chỗ | ➕➕ |
| 312 | **L.4** ba lệnh dừng | Cuộn `( S )` / `( R )`; ⚠ nút bật/tắt cần **hai nấc** thay vì một dòng ST | ➕ |
| 313 | **L.7** bắt cạnh + chống rung | ⭐⭐ **Thứ tự lọc-rung-trước nhìn thấy được** — hộp `TON` bên trái, `┤P├` bên phải. ⚠ Nhưng ladder **giấu** một thứ ST nói rõ: mỗi hộp là một **thể hiện riêng** | ➕➕ |
| 314 | **L.8** gọi khối cơ cấu | ⭐ Hình dạng **quen thuộc nhất với thợ bảo trì**: hộp có tên, chân trái lệnh vào, chân phải phản hồi | ➕ |
| 315 | **L.10** khoá chéo | ⭐⭐ Đọc chéo hai nấc là **thấy ngay** khoá chéo; thiếu một trong hai nhìn ra bằng mắt | ➕➕ |
| 316 | **L.13** đèn tháp | ⭐⭐ **Chỗ ladder đáng dùng nhất cả phụ lục** — người mở chương trình khi có sự cố sẽ tìm nấc điều khiển **cái đèn đang sáng sai**. Bốn nấc tìm ra trong mười giây | ➕➕ |

### C — ⭐⭐ Mục L.18 mới: chọn ngôn ngữ nào cho mẫu nào

| # | Nội dung | KQ |
|---|:--|:--:|
| 317 | ⭐⭐ **Bảy mẫu còn lại CỐ Ý chỉ có ST** — và mục mới nói rõ vì sao, theo đúng bất biến **B18**: bảng 14 mẫu, mỗi mẫu một dòng, cột *ladder* / cột *ST* / cột **nên dùng cái nào** | ➕➕ |
| 318 | ⭐ **Quy tắc rút ra** — ladder khi: thợ bảo trì phải đọc lúc hai giờ sáng · là logic bit · điều khiển **ngõ ra cuối** · là **liên động**. ST khi: có phép tính · nhiều nhánh · trình tự `CASE` · vòng lặp và chỉ số | ➕➕ |
| 319 | ⭐⭐ **Cách TRỘN đúng, theo tầng**: bên trong khối → **ST** · gọi khối và nối khối → **ladder** · trình tự nhiều bước → **ST/SFC** · ⭐⭐ **chuỗi cho phép và ngõ ra cuối → ladder, kể cả khi cả chương trình viết bằng ST** | ➕➕ |
| 320 | ⚠ Kèm cảnh báo: **không phải hệ nào cũng cho trộn ngôn ngữ ở mọi mức** — phần lớn hệ cho mỗi **khối** một ngôn ngữ, và như vậy là đủ cho cách chia trên. ⭐ Kiểm trước khi thiết kế theo nó | ➕ |

### D — Soát trình bày

| # | Việc | KQ |
|---|:--|:--:|
| 321 | ⚠ Hai khối ladder đầu tiên **vẽ lệch cột**: hộp khối chức năng ở L.8 có cạnh phải không thẳng, và nhánh song song ở L.13 thiếu hai ký tự. ⭐ Bắt được bằng cách **đếm cột từng dòng** bằng script, rồi dựng lại hộp bằng phép tính vị trí thay vì gõ tay | ⚠ |
| 322 | ⭐ Kiểm bản ghép: ký tự khung `┤ ├` · `┤/├` · `┤P├` **sống sót nguyên vẹn** sang HTML, và `pre` dùng **phông đẳng chiều** kèm `overflow-x` nên nấc dài **cuộn ngang**, không xuống dòng vỡ hình | ✔ |
| 323 | ⚠ Nấc dài nhất ban đầu **106 ký tự** — đã nén còn **99**, ngang với các hình ASCII sẵn có trong sách | ⚠ |

### Kết quả đợt 47

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **15** |
| ➕➕ Bổ sung giá trị cao | 8 |
| ➕ Bổ sung | 3 |
| ⚠ Sửa trình bày | 2 |
| Mục mới | 1 — Phụ lục L.18 |
| Mẫu nay có **cả hai ngôn ngữ** | **7 / 16** |

> ⭐⭐ **Bài học 1 — lời khuyên trong sách phải được chính sách làm gương.**
>
> Phụ lục L khuyên dùng ladder cho liên động và ngõ ra cuối, rồi ⚠ **viết toàn bộ bằng ST**. Không
> ai bắt lỗi được điều đó bằng bộ kiểm — nó không sai một chữ nào. ⭐ Nhưng người đọc sẽ học theo
> **cái họ THẤY**, không theo cái họ được khuyên.
>
> ⚡ **Bài học 2 — "cũng cho luôn bản ladder" không phải là câu trả lời đầy đủ.**
>
> Chép cả 16 mẫu sang ladder sẽ **tệ hơn**: `CASE`, phép chia, quy đổi thang analog viết bằng ladder
> thì khó đọc hơn hẳn. ⭐ Giá trị thật nằm ở chỗ **bảy mẫu nào nên có, bảy mẫu nào không, và vì
> sao** — tức là mục L.18, chứ không phải bảy khối vẽ thêm.
>
> ⭐ **Bài học 3 — hình vẽ bằng ký tự vẫn phải soát như hình.** Hai khối lệch cột không lộ ra khi
> đọc lướt; ⚡ chúng lộ ra khi **đếm cột bằng script**. Cùng tinh thần với bài học ở đợt 35: hình
> phải nhìn, và với hình bằng ký tự thì "nhìn" nghĩa là **đo**.

---

## Đợt 48 — 2026-09-20 · Rà từng chương: ladder cho bốn chương thiếu, hai hình mới, khung DP-01, năm nguồn

Yêu cầu của chủ dự án: ⭐ *"đánh giá lại từng chương xem có gì có thể bổ sung, chỉnh sửa không"*, rồi
⭐ *"làm hết theo thứ tự"* — nên đợt này thực hiện trọn danh sách A→E đã đề xuất.

> ⭐⭐ **Cách chọn việc của đợt này: ĐO, không đọc lại.** Đọc lại 58 chương lần thứ tư sẽ tìm ra
> đúng những thứ ba lần trước đã tìm. Ba phép đo mới được dùng:
>
> | Phép đo | Cái nó lộ ra |
> |---|---|
> | Đếm **số khối ladder / số khối ST** từng chương | ⚠ Bốn chương dạy trực tiếp về ladder mà **không có khối ladder nào** |
> | Đếm **số chương trỏ tới** một chương, đối chiếu **số hình** chương đó có | ⚠ Ch.9 (13 chương trỏ tới) và Ch.36 (14 chương trỏ tới) đều **không có hình** |
> | Đếm **số lần nhật ký này nhắc tới** từng chương | ⚠ Ch.57 là chương tổng kết mà **không có một dòng mã nào** |

### A — Bốn chương dạy ladder mà không có ladder

| # | Chương | Bổ sung | KQ |
|---|---|:--|:--:|
| 324 | ⚠ **Ch.17** — cả chương về timer, ba ví dụ đều là ST | Ba hộp `TON` / `TOF` / `TP` vẽ lại **đúng ba ví dụ ST đã có**, kèm bảng chân `IN`/`PT`/`Q`/`ET`. ⭐⭐ Và điểm ladder hơn ST ở đây: **xem trực tuyến thấy `ET` đếm lên** — biết máy đang chờ chứ không treo | ➕➕ |
| 325 | ⭐⭐ Ch.17 — ba bẫy của chính chương **không biến mất** khi sang ladder | Bảng đối chiếu: ⚠⚠ Bẫy 3 (hộp nằm trong vùng `MCR` bị tắt) và Bẫy 5 (chép–dán quên đổi tên hộp) **khó thấy hơn ở ladder**; chỉ Bẫy 2 là dễ thấy hơn | ➕➕ |
| 326 | ⚠ **Ch.18** — bộ đếm | Hộp `CTU` với chân `CV` **nối ra thanh ghi** — để người vận hành thấy con số mà không cần mở phần mềm lập trình. Kèm ⚠⚠ bẫy chỉ có ở ladder: **cực tính chân `R` khác nhau giữa các hãng** | ➕➕ |
| 327 | ⚠⚠ **Ch.26** — bảng của chính chương ghi *"bit bước hợp với **Ladder**"*, và bất biến nói *"bật bit mới, tắt bit cũ trong CÙNG một nấc"* — mà **chưa từng vẽ nấc đó ra** | Hai nấc `( S )` / `( R )` trên cùng một nấc thang, cộng nấc **giám sát bất biến**. ⭐ Khoảng khắc hai bit cùng bật nếu tách hai nấc — nay nhìn thấy được | ➕➕ |
| 328 | ⚠ **Ch.28** — nguyên tắc *"chế độ tay vẫn giữ nguyên liên động"* | Nấc thang giữ đủ tiếp điểm liên động. ⭐ Ở ladder, **thiếu một tiếp điểm là nhìn ra được**; ở ST, thiếu một vế `AND` thì không | ➕➕ |
| 329 | ⭐⭐ Ch.28 — thêm **hai nấc CỐ Ý SAI** | Hai nấc cùng ghi `M_ModeFault` = **cuộn dây trùng**, đúng thứ Ch.15 Bẫy 1 cấm. Để nguyên có chủ ý, vì nó chứng minh ⭐ **ladder dễ đọc không có nghĩa là ladder khó sai** | ➕➕ |
| 330 | ⚠ Bốn khối đầu tiên **vẽ lệch cột** — nhãn ngõ ra đè lên cạnh phải của hộp | Sửa bằng cách bắt hàm sinh nhãn **phát cả hai cạnh hộp trước** rồi mới ghi nhãn bên ngoài; kiểm lại bằng script: cạnh trái cột 22, cạnh phải cột 41 ở **mọi** khối. ⭐ Cùng bài học đợt 47 — hình bằng ký tự thì "nhìn" nghĩa là "đo" | ⚠ |

### B — Hình 9.1: sink / source

| # | Nội dung | KQ |
|---|:--|:--:|
| 331 | ⚠ Ch.9 có **13 chương trỏ tới** — nhóm cao nhất sách — mà **không có hình nào**, trong khi mục 9.2 đúng là *đường đi của dòng điện*, tiêu chí số một của bất biến **B13** | ⚠ |
| 332 | ⭐ Hình hai khung: sink và source, khác nhau **đúng một sợi dây chân chung**, và từ đó khác chiều dòng | ➕➕ |
| 333 | ⭐⭐ **Sửa sau khi render PNG ra xem:** bản đầu vẽ **một chân nguồn của cảm biến bằng nét xám**, trong khi chân đó **nằm trong vòng dòng tín hiệu** (chân +24 V với PNP, chân 0 V với NPN). ⚠ Vòng dòng bị hở về mặt thị giác — mâu thuẫn với chính chú giải của hình. Đã vẽ đỏ trọn vòng | ⚠ |
| 334 | ⭐ Ghi chú kèm hình trả lời một câu hỏi của mục 9.5: dòng ngõ vào **không đi nhánh riêng** mà xuyên qua dây nguồn cảm biến; ⚠ nhưng datasheet thường ghi dòng tiêu thụ **lúc không tải** nên **vẫn phải cộng thêm** | ➕ |

### C — Ch.57 có mã: khung chương trình chính của DP-01

| # | Nội dung | KQ |
|---|:--|:--:|
| 335 | ⚠ Ch.57 là **chương tổng kết cả sách** mà không có một dòng mã nào — chỉ có sơ đồ hộp | ⚠ |
| 336 | ⭐⭐ Thêm **khung `PROGRAM Main`** 14 lệnh gọi, mỗi dòng chú thích chương nguồn; và khối `Prg_OutputMap` bốn dòng. ⭐ *"Đến chương này thì không còn gì phải phát minh — chỉ còn ghép các mẫu đã có theo đúng thứ tự"* | ➕➕ |
| 337 | ⭐⭐ Ba điểm đi kèm: ⚠⚠ **không `IF` nào bao quanh lệnh gọi** (Ch.17 Bẫy 3) · thứ tự **cơ cấu → máy → trạm → ghi ngõ ra** không tuỳ ý (Ch.27 mục 27.6) · ghi ngõ ra gom một khối cuối = *"đúng một chỗ ghi mỗi tag"* (Ch.22) | ➕➕ |
| 338 | ⭐⭐ Làm rõ một chỗ dễ lẫn: **thứ tự GỌI khác thứ tự VIẾT**. Mục 57.7 là thứ tự **viết** (an toàn trước); danh sách mới là thứ tự **gọi** (luồng dữ liệu trong một vòng quét) | ➕➕ |
| 339 | ⚠⚠ **Bản nháp đầu có HAI tác vụ** — tác vụ 500 ms cho PID nhiệt keo. ⭐ Tra lại trước khi viết thì thấy **Ch.35 mục 35.11 nói thẳng**: *"DP-01 gần như không có vòng PID nào do PLC chạy"* — nhiệt keo do **bộ điều khiển rời RS-485** lo. Đã bỏ, và biến thành điểm dạy: DP-01 chỉ **một** tác vụ, vì mọi vòng liên tục đã giao cho thiết bị chuyên dụng | ⚠ |
| 340 | ⚠ **Ch.57 tự mâu thuẫn với Phụ lục J**: mục 57.2 ghi *"trục Z dùng servo"* (ngụ ý chỉ Z), bảng I/O cùng chương ghi *"cả ba đều servo"*, Phụ lục J §J.1 và bảng trục cũng ghi **cả ba servo**. Sửa 57.2 | ⚠ |
| 341 | ⚠ Sơ đồ hộp mục 57.6 và bảng mục 57.7 đều ghi *"Analog, **PID gia nhiệt keo**"* — trái với mục 35.11. Sửa cả hai thành *"giám sát nhiệt qua RS-485"* | ⚠ |

### D — Hình 36.1: ba tháng trôi dạt

| # | Nội dung | KQ |
|---|:--|:--:|
| 342 | ⚠ Ch.36 có **14 chương trỏ tới** mà **không có hình nào** | ⚠ |
| 343 | ⭐⭐ Hình bốn băng theo thời gian: **lệnh đặt phẳng 70 %** · tốc độ thực tụt xuống 64 % · dòng động cơ leo lên 92 % · cờ *"đang giới hạn dòng"* bật dần. ⭐ Cả ba băng dưới đều **có sẵn trong biến tần**; PLC chỉ thấy băng trên cùng, và băng trên cùng thì phẳng | ➕➕ |
| 344 | ⭐ Đường **"mốc"** trong hình gắn thẳng với mục 36.11 Bẫy 8: ⚡ **không ghi giá trị lúc nghiệm thu thì có đọc về cũng không biết đã trôi bao nhiêu** | ➕➕ |
| 345 | ⚠ Kèm cảnh báo cách đọc sai: hình này **không nói biến tần hỏng**. Biến tần đang làm đúng chức năng bảo vệ; ⭐⭐ cái sai nằm ở **thiết kế đường thông tin** | ➕ |

### E — Năm chương được thêm nguồn, và mỗi nguồn kéo theo nội dung

⭐⭐ **Nguyên tắc tự đặt cho mục này: không thêm nguồn để trang trí.** Mỗi nguồn thêm vào phải
**chống lưng cho một đoạn có thật** — nên bốn trong năm chương được thêm nội dung luôn.

| # | Chương | Nguồn (đã xác minh bằng `tra_nguon.py`) | Nội dung kéo theo | KQ |
|---|---|:--|:--|:--:|
| 346 | **Ch.1** | ⭐ Kuphaldt, *Lessons In Industrial Instrumentation* §12.10 *How to teach yourself PLC programming* | ⭐⭐ Mục mới ở 1.8: **bốn việc theo thứ tự** (có PLC riêng · đọc *Getting Started* trước · **tự lắp bàn thực hành** · viết chương trình mẫu bé cho từng lệnh) và ⭐ **năm mục phải ghi trong chú thích**, trong đó có ⚠⚠ *lỗi mình đã mắc* | ➕➕ |
| 347 | **Ch.11** | Siemens, *Programming Guideline for S7-1200/1500* ch. 2.6 *Optimized blocks* | ⭐ Mục mới ở 11.8: khối **tối ưu** chỉ truy cập theo tên · ⚠ khối chuẩn **đọc một bit thì khoá cả byte** · 64 kB so với 16 MB · ⚠⚠ **chép dữ liệu giữa hai kiểu tốn nhiều thời gian xử lý**. ⭐ Nối thẳng với mục 11.1: *"khối tối ưu không có địa chỉ tuyệt đối để mà dùng sai"* | ➕➕ |
| 348 | **Ch.17** | Rockwell, *Logix 5000 Controllers General Instructions* bản 9/2025, ch. 3 | ⚡ Cập nhật cho mục 17.7: kiểu **`TIMER_T`** mới có `.PRE`/`.ACC` kiểu `TIME` — khác biệt *"Rockwell đếm bằng số nguyên mili-giây"* **đang mất dần**. ⚠ Nhưng kiểu `TIMER` cũ vẫn song song, nên ⭐⭐ **phải nhìn kiểu của biến, đừng suy từ tên hãng** | ➕ |
| 349 | **Ch.24** | Kuphaldt, *Lessons In Electric Circuits Vol. IV: Digital* ch. 7 (§7.8 DeMorgan, §7.9 bảng chân lý → biểu thức) và ch. 8 *Karnaugh Mapping* | ⭐ Thay dòng *"giáo trình đại số Boolean nói chung"* bằng một nguồn **mở, đọc được toàn văn** — chỗ để tới khi cần phần chứng minh mà chương cố ý lược | ➕ |
| 350 | **Ch.26** | Mitsubishi, *MELSEC iQ-F FX5 Programming Manual (Program Design)* ch. 8 và phần *step relay* | ⭐ Mục 26.2a mới: có hãng coi bit bước là **một loại thiết bị** (`S`), kèm bảng ưu/nhược so với cờ nhớ thường, và ⚠⚠ bẫy trong ST — **không gán thẳng** `M0 := S0;` mà phải viết bằng `IF … THEN … ELSE` | ➕➕ |

### Kết quả đợt 48

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **27** |
| ➕➕ Bổ sung giá trị cao | 15 |
| ➕ Bổ sung | 5 |
| ⚠ Sửa lỗi / sửa mâu thuẫn | 7 |
| Hình mới | 2 — Hình 9.1, Hình 36.1 |
| Mục mới | 4 — Ch.1 §1.8, Ch.11 §11.8, Ch.26 §26.2a, Ch.57 §57.6 |
| Chương nay có khối ladder | **+4** (Ch.17, 18, 26, 28) |
| Nguồn ngoài mới được dẫn | 5 |

> ⭐⭐ **Bài học 1 — ba phép đếm khác nhau tìm ra ba nhóm thiếu sót khác nhau.**
>
> Ba lượt rà trước đều là *đọc lại*, và lượt sau tìm ra ít hơn lượt trước. Đợt này đổi sang **đếm**:
> đếm khối ladder tìm ra Ch.17/18/26/28; đếm chương-trỏ-tới so với số hình tìm ra Ch.9/36; đếm số
> lần nhật ký nhắc tới từng chương tìm ra Ch.57. ⚡ **Không phép đếm nào trong ba phép trên tìm ra
> nhóm của hai phép kia.**
>
> ⭐ Suy ra cho các đợt sau: khi một cách rà bắt đầu cho ít kết quả, ⚠ đừng rà kỹ hơn — **đổi thước
> đo**.

> ⚠⚠ **Bài học 2 — tra sách TRƯỚC khi viết, không phải sau.**
>
> Khung chương trình DP-01 suýt có hai tác vụ, trong đó tác vụ thứ hai chạy một vòng PID mà ⚠ **máy
> mẫu này không hề có** — Ch.35 mục 35.11 đã nói rõ từ lâu. ⭐ Cái cứu được là thói quen `grep`
> chính cuốn sách trước khi đặt bút, đúng thói quen đã cứu Phụ lục L ở đợt 47.
>
> ⚡ Và lần tra đó **còn tìm thêm hai chỗ tự mâu thuẫn sẵn có** trong Ch.57 (số trục servo; PID nhiệt
> keo) — ⭐ tức là việc tra để **viết đúng** cũng là việc rà soát, nếu tra đủ rộng.

> ⭐ **Bài học 3 — hình phải render ra xem, mỗi lần.**
>
> Hình 9.1 bản đầu vẽ đúng về mặt sơ đồ nhưng ⚠ **sai về mặt kể chuyện**: chú giải nói *"nét đỏ là
> vòng dòng"* trong khi một đoạn của vòng dòng lại là nét xám. ⚡ Đọc mã sinh hình **không** thấy
> được điều đó; nhìn ảnh thì thấy ngay. Đây là lần thứ ba bài học này xuất hiện (đợt 35, 47, 48) —
> ⭐ nên nó đã thành quy trình: **sinh SVG → render PNG → nhìn → sửa**, không bỏ bước nào.

---

## Đợt 49 — 2026-09-20 · Rà tiếp bằng ba thước đo khác: cấu trúc chương, bất biến B18, và chỗ hãng quyết định thay bạn

Tiếp yêu cầu *"rà và bổ sung các chương còn lại"*. ⭐ Theo đúng **bài học 1 của đợt 48** — khi một
cách rà cho ít kết quả thì **đổi thước đo**, đừng rà kỹ hơn — đợt này dùng ba thước hoàn toàn mới.

| Thước đo | Cách đo | Cái nó lộ ra |
|---|---|---|
| **Bộ khung từng chương** | Đếm mục 🔍 BẪY · câu tự kiểm · khối mã · bảng · hình · có mục DP-01 không · có mục "khác biệt giữa các hãng" không, cho cả 58 chương | ⚠ Ch.27 và Ch.30 **thiếu mục khác biệt giữa các hãng** ở đúng hai chủ đề mà các hãng làm khác nhau nhất |
| ⭐ **Soát bất biến B18** | Tìm mọi câu nhắc *"N cách / N lựa chọn / N phương án"* ngoài khối mã, rồi kiểm xem trong 14 dòng kế tiếp có bảng so sánh không | ✔ **Không tìm ra vi phạm thật** — chi tiết ở phần D |
| **Hình minh hoạ có nói đúng cơ chế không** | Đọc lại từng hình ASCII sẵn có và hỏi *"hình này nói được điều gì mà chữ không nói?"* | ⚠⚠ Hình ba cách đấu RTD ở Ch.33 vẽ ba bó dây **giống hệt nhau** — không nói được gì cả |

### A — ⚠ Ch.30 nói "dùng thư viện có phiên bản" mà không nói hãng cho bạn cơ chế gì

| # | Phát hiện / bổ sung | KQ |
|---|:--|:--:|
| 351 | ⚠ Ch.30 là **chương dài nhất sách** (778 dòng) và là chương về **tái sử dụng**, nhưng mục 30.5 khuyên *"dùng thư viện có phiên bản"* mà ⭐ **không nói cơ chế đó do phần mềm hãng cung cấp** — người đọc không tự dựng được | ⚠ |
| 352 | ⭐⭐ Mục mới: **hai hướng ngược nhau**, mỗi hướng một ví dụ thật đã xác minh — **chép có kiểm soát** (Rockwell AOI) và **tham chiếu tới kiểu** (Siemens type). Bảng sáu hàng: khối sống ở đâu · cập nhật thế nào · nhiều phiên bản cùng lúc · chống sửa lén · cái giá | ➕➕ |
| 353 | ⭐⭐ Và nó **đọc lại được bảng "ba kiểu dùng lại"** sẵn có theo nghĩa cụ thể hơn: cơ chế Rockwell **chính là kiểu "chép"**, nhưng chép có bản sửa đổi, có chữ ký, có lịch sử. ⭐ Suy ra: *"chép" không tự động xấu — xấu là chép mà không biết mình chép bản nào* | ➕➕ |
| 354 | ⚠⚠ **Chữ ký khối của Rockwell niêm cả tài liệu**: ký xong thì không sửa được, **kể cả chú thích nấc thang và mô tả biến**. Đổi lại nó là bằng chứng khối chưa bị đụng — nên **bắt buộc** cho khối tham gia chức năng an toàn mức SIL 3. ⚠ Lỗ hổng: chữ ký **không khoá** các khối và kiểu dữ liệu mà nó tham chiếu | ➕➕ |
| 355 | ⚠⚠ **Xoá một "type" của Siemens là xoá mọi chỗ đang dùng nó**, và ⭐ **một bộ điều khiển chỉ chứa một phiên bản của mỗi kiểu** — nghe như hạn chế, nhưng nó chính là thứ chặn đứng "kiểu thứ ba" (chép rồi sửa tới mức không nhận ra) | ➕➕ |
| 356 | ⭐ Thêm **bốn câu hỏi tự tra cho hệ của mình**, vì không suy được từ hai cột trên. ⚠⚠ Câu thứ tư — *xoá hoặc đổi tên khối thì chỗ đang dùng ra sao* — ⭐ **phải thử thật trên một dự án bỏ đi**, vì biết vào lúc đang sửa máy chạy sản xuất là quá muộn | ➕➕ |

### B — Hình 33.1: RTD hai, ba, bốn dây

| # | Nội dung | KQ |
|---|:--|:--:|
| 357 | ⚠⚠ Hình ASCII cũ vẽ cả ba cách như **ba bó dây song song giống hệt nhau**, khác mỗi số sợi. ⭐ Nó **không** nói được điều duy nhất đáng nói: sợi nào mang dòng, áp đo ở đâu, vì sao thêm một sợi lại bù được sai số. Ch.33 trước đợt này **không có hình nào** | ⚠ |
| 358 | ⭐⭐ Hình mới vẽ **nét đỏ = sợi mang dòng kích thích**, **nét xanh = sợi chỉ để đo**, ô `R` = điện trở của chính sợi dây; cách 2 dây có thêm ký hiệu vôn kế **đặt tại chân module** để thấy phép đo dừng ở đâu | ➕➕ |
| 359 | ⭐⭐ Và nó rút cả ba cách về **một câu hỏi duy nhất**: *"sợi nào có dòng chạy qua?"* — sợi có dòng thì sụt áp và sụt áp đó cộng vào kết quả; sợi không dòng thì dẫn được điện áp thật trên RTD về module. ⭐ Suy ra được cả ba cách mà không học thuộc | ➕➕ |
| 360 | ⭐ Hình **thay** khối ASCII cũ chứ không thêm vào cạnh nó — khối cũ không còn tác dụng gì khi đã có hình | ⚠ |

### C — Ch.27 nói về tác vụ mà không có con số nào của hãng

| # | Nội dung | KQ |
|---|:--|:--:|
| 361 | ⭐⭐ Lời khuyên *"mặc định một tác vụ"* của mục 27.6 nay **có tài liệu hãng chống lưng**: tài liệu quản lý tác vụ có hẳn mục **"thận trọng với số lượng tác vụ bạn dùng"**, và câu ⭐ *bộ điều khiển chỉ chạy **một** tác vụ tại một thời điểm* — khép lại tranh luận "chạy song song cho nhanh" | ➕➕ |
| 362 | ⚠⚠ **Điều kiện chồng tác vụ** — chu kỳ tác vụ định kỳ phải **dài hơn tổng thời gian chạy của mọi chương trình gán vào nó**; không thoả thì **lỗi nhẹ**. ⭐ Và đây là lỗi **không xuất hiện lúc nghiệm thu** — nó xuất hiện tháng sau khi ai đó thêm khối, đúng cơ chế trôi dạt ở Ch.36 | ➕➕ |
| 363 | ⭐ **Mỗi tác vụ có watchdog riêng** — Ch.10 mục 10.4 mới chỉ nói watchdog của cả vòng quét. Tách tác vụ là thêm một chỗ phải đặt đúng | ➕ |
| 364 | ⭐ Bảng ba loại tác vụ kèm con số: liên tục — ⭐ **không bắt buộc có, và nếu có thì chỉ được một** · định kỳ **0,1 ms – 2000 s**, mặc định **10 ms** · theo sự kiện, ⚠ không phải bộ điều khiển nào cũng đủ loại kích hoạt | ➕➕ |
| 365 | ⭐⭐ **Mức ưu tiên có một giá trị đặc biệt**: 15 mức, và **tác vụ I/O của hệ chạy ở mức 6** — đặt 1–5 là cho tác vụ của bạn chen ngang cả việc cập nhật I/O. ⚠ Nhưng 15 **không phải hằng số**: cùng hãng, dòng chạy trên máy tính chỉ có **3** mức — nên phải tra theo đúng dòng đang dùng | ➕➕ |

### D — ⭐ Soát bất biến B18 trên toàn sách: kết quả là **không có vi phạm**

⭐⭐ **Đây là một kết quả âm tính, và nó đáng ghi lại đúng bằng một kết quả dương tính.**

| # | Việc | KQ |
|---|:--|:--:|
| 366 | Quét toàn bộ 71 tệp tìm câu nhắc *"N cách / N lựa chọn / N phương án / có thể chọn"* **ngoài khối mã**, rồi kiểm có bảng so sánh trong 14 dòng kế tiếp không. ⭐ **55 chỗ** không có bảng | ⚠ |
| 367 | ⭐ Đọc hết 55 chỗ: **không chỗ nào vi phạm B18 thật**. Phần lớn là **câu hỏi tự kiểm**, **chú thích hình**, **mục nguồn tham khảo** và **câu dẫn sang chương khác** — tức là nhắc tới phương án chứ không **giới thiệu** phương án | ✔ |
| 368 | ⭐ Nhóm còn lại là **danh sách cách chữa đã xếp theo thứ tự ưu tiên**, mỗi mục có sẵn đánh đổi viết ngay trong câu (Ch.4 mục 4.3 và 4.4, Ch.9 mục 9.2, Ch.35 mục 35.2). ⭐⭐ Đây **đúng tinh thần B18** — có tên từng cách, có đánh đổi, có khuyến nghị — chỉ là **không ở dạng bảng**. ⚠ Ép thành bảng sẽ làm loãng, không làm rõ | ✔ |

### E — Ch.2: khác biệt thứ năm, thứ ít được nhắc nhất

| # | Nội dung | KQ |
|---|:--|:--:|
| 369 | ⚠ Ch.2 là chương **nhỏ nhất sách** (305 dòng) và ⭐ **chưa từng bị soi ở 48 đợt trước**. Mục 2.2 *"PLC khác máy tính thường ở đâu"* có bốn điểm: môi trường · tính tất định · khởi động lại · tuổi đời | ⚠ |
| 370 | ⚠⚠ **Thiếu hẳn điểm thứ năm, mà lại là điểm có cả một chương dành cho nó**: PLC cho **sửa chương trình trong lúc máy đang chạy**. Ch.53 dạy rất kỹ chuyện làm việc đó an toàn, nhưng ⭐ **không chương nào giới thiệu rằng khả năng đó tồn tại** | ⚠ |
| 371 | ⭐ Bổ sung mục 2.2 điểm 5, kèm hai mặt: ⚡ với nhiều nhà máy, **đổi mà không dừng** là **điều kiện chấp nhận thiết bị**, không phải tiện nghi; nhưng ⚠⚠ cơ cấu **đang ở giữa chừng hành trình** khi logic đổi, và **người đứng cạnh máy không được cảnh báo gì cả**. ⭐ Chốt: *PLC cho phép không có nghĩa là nên làm* → Chương 53 | ➕➕ |

### Kết quả đợt 49

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **21** |
| ➕➕ Bổ sung giá trị cao | 12 |
| ➕ Bổ sung | 1 |
| ⚠ Phát hiện thiếu sót / sửa | 6 |
| ✔ Xác nhận không có vấn đề | 2 |
| Hình mới | 1 — Hình 33.1 (và **bỏ** một khối ASCII vô dụng) |
| Mục mới | 3 — Ch.2 §2.2 điểm 5, Ch.27 §27.6, Ch.30 §30.5 |
| Nguồn ngoài mới được dẫn | 3 |

> ⭐⭐ **Bài học 1 — "chương này thiếu mục X" là một thước đo, và nó rẻ.**
>
> Đếm xem chương nào **không có** mục *khác biệt giữa các hãng* cho ra 26 chương. ⭐ Phần lớn là
> đúng — chương lớp 0 thì không có gì để so sánh giữa các hãng. ⚡ Nhưng **hai** trong số đó, Ch.27
> và Ch.30, lại là đúng hai chủ đề mà **các hãng làm khác nhau nhất**: mô hình tác vụ, và cơ chế
> thư viện dùng lại. ⭐ Thước đo thô, nhưng phần dư của nó chính là chỗ cần nhìn.

> ⚠ **Bài học 2 — kết quả âm tính phải ghi lại, nếu không nó sẽ bị làm lại.**
>
> Soát B18 quét ra 55 chỗ nghi, đọc hết, và **không có vi phạm nào**. ⭐ Nếu không ghi lại thì đợt
> sau ai đó sẽ chạy đúng phép quét đó, ra đúng 55 chỗ đó, và đọc lại từ đầu. ⚡ Nhật ký này tồn tại
> để chuyện đó **không xảy ra lần thứ hai** — nên mục D ghi cả cách quét lẫn lý do bác bỏ.

> ⭐ **Bài học 3 — một hình vô dụng tệ hơn không có hình.**
>
> Khối ASCII ba cách đấu RTD ở Ch.33 tồn tại nhiều đợt mà không ai bắt lỗi, vì ⚠ **nó không sai** —
> ba cách đấu đúng là có 2, 3, 4 sợi. ⭐ Nó chỉ **không nói gì cả**: người đọc nhìn xong vẫn không
> biết vì sao sợi thứ ba bù được sai số. ⚡ Câu hỏi để bắt loại lỗi này không phải *"hình có đúng
> không?"* mà là ⭐⭐ ***"hình nói được điều gì mà chữ không nói?"*** — nếu không trả lời được, hình
> đó đang chiếm chỗ.

---

## Đợt 50 — 2026-09-20 · Quy trình khởi động dự án: hai biểu mẫu sách tự đòi mà chưa từng dạy cách lập

Câu hỏi của chủ dự án: *"sách đã có quy trình khi bắt đầu dự án PLC — lập bảng I/O, danh mục vật tư,
cấu hình PLC — chưa?"*, kèm yêu cầu ⭐ *"các đặc tả có nội dung chi tiết và yêu cầu đối với kết quả
mong muốn thì càng tốt"*.

> ⭐⭐ **Thước đo của đợt này, và nó là thước sắc nhất từng dùng: sách ĐÒI tài liệu nào mà không DẠY
> cách lập tài liệu đó?**
>
> Phiếu bàn giao C.9 là một danh mục 12 mục cộng bộ sao lưu bảy hạng mục. ⚡ Mỗi mục trong đó là một
> lời hứa: *"sách này cho rằng bạn phải có thứ này"*. ⭐ Đối chiếu ngược 19 mục đó với phần còn lại
> của sách thì ⚠ **hai mục không có chương nào dạy và không có biểu mẫu nào**.

### A — Hai lỗ hổng, và bằng chứng của chúng

| # | Phát hiện | KQ |
|---|:--|:--:|
| 372 | ⚠⚠ **Danh mục vật tư**: sách **đòi** nó ở **bốn chương và hai phụ lục** — Ch.7 (*"ghi rõ yêu cầu vật liệu tiêu tán trong danh mục vật tư"*), Ch.48, Ch.49 mục 49.10, Ch.52, Phụ lục D, và ⭐ **Phiếu bàn giao C.9 mục 9**. ⚠ Nhưng **không chương nào dạy cách lập, và không có biểu mẫu**. Thứ duy nhất có là §13.8 — danh sách vật tư **bàn thực hành**, không phải máy thật | ⚠⚠ |
| 373 | ⚠⚠ **Bảng cấu hình phần cứng**: bộ sao lưu bảy hạng mục ở C.9 có *"cấu hình phần cứng"* là **mục số 2**, Ch.54 nhắc nó **năm lần** (*"thiếu cấu hình phần cứng → không nạp được"*). ⭐ Và bảng ánh xạ giai đoạn ở cuối Phụ lục C ghi hẳn dòng **"Bảng I/O & phần cứng → C.1"** — ⚠ nhưng C.1 chỉ là bảng I/O; **phần "& phần cứng" không tồn tại** | ⚠⚠ |
| 374 | ⚠ **Không có quy trình khởi động gom về một chỗ.** Người bắt đầu dự án thật phải tự ghép từ Ch.13 (chọn PLC) + Ch.23 (đặc tả) + Ch.57 (truyện kể về máy mẫu) + Phụ lục C. ⭐ Ch.57 mục 57.3 có bảng *"Đầu ra của giai đoạn 1"*, nhưng ⚠ **mục 57.4 — giai đoạn bảng I/O và chọn phần cứng — không có bảng đầu ra tương ứng** | ⚠ |
| 375 | ⭐ Ngược lại, phần **đã có** thì khá đầy đủ: bộ đặc tả sáu phần (Ch.23 mục 23.2, có cả URS/FS/SOO), bảng I/O làm trước (23.3), biểu mẫu bảng I/O 10 cột kèm số dây và cầu đấu (C.1), 10 tiêu chí chọn PLC và bảng công tác 11 mục (§13.2, §13.2b, §13.4), đánh địa chỉ theo khe (§8.4), tính nguồn 24 V (§8.7, §9.5) | ✔ |

### B — Phụ lục C: thêm hai biểu mẫu, chín thành mười một

| # | Nội dung | KQ |
|---|:--|:--:|
| 376 | ⭐⭐ **C.10 Bảng cấu hình phần cứng** — hai bảng: **bản đồ khe cắm** (rack·khe · mã · loại · số kênh · địa chỉ đầu–cuối · ⭐ **dùng/dự phòng** · ⭐ **firmware** · nguồn cấp · ghi chú) và **thiết bị trên mạng** (giao thức · địa chỉ/trạm · ⭐ **tệp mô tả thiết bị và phiên bản**) | ➕➕ |
| 377 | ⭐ Hai cột ít ai nghĩ tới mà đắt nhất khi thiếu: ⭐ **"Dùng / Dự phòng"** trả lời câu *"thêm một cảm biến được không"* mà không phải mở tủ; ⭐⭐ **"Firmware"** — ⚠ thay module **cùng mã khác phiên bản** có thể đổi hành vi mà không báo gì | ➕➕ |
| 378 | ⭐⭐ **C.11 Danh mục vật tư** — và nguyên tắc quan trọng nhất của nó: ⚠ **đừng viết như tài liệu độc lập**. Mọi dòng phải **sinh ra từ** C.1 hoặc C.10, và có hẳn cột ⭐ **"Sinh từ"** để chuyện lệch nhau không xảy ra âm thầm | ➕➕ |
| 379 | ⭐⭐ **Chọn phụ tùng dự phòng bằng ba câu hỏi, không bằng cảm tính** — và câu quyết định là một **phép so sánh**: *thời gian có hàng có dài hơn mức dừng máy chấp nhận được không?* ⚡ Một module rẻ **giao tám tuần** đáng dự phòng hơn một CPU đắt **có sẵn ngày mai**. ⚠ Phần lớn danh mục phụ tùng bị lập ngược — theo giá | ➕➕ |
| 380 | ⚠⚠ **Thiết bị an toàn là trường hợp riêng**: dự phòng một rơ-le an toàn **không** nghĩa là thay vào là chạy — đổi thiết bị trong chuỗi an toàn thường kéo theo **đánh giá lại và nghiệm thu lại**. ⭐ Phải ghi điều này vào cột ghi chú **ngay từ lúc lập danh mục**, để người mua hàng sáu tháng sau không tự ý đổi sang "mã tương đương" | ➕➕ |
| 381 | ⭐ Mỗi biểu mẫu mới có một ⭐⭐ **phép thử một phút** — thứ biến "đã điền xong" thành một phát biểu kiểm được. C.10: *đưa bảng cho người chưa từng mở tủ, hỏi `DI_BoardStn1` nằm ở khe nào, kênh nào*. C.11: *chọn ngẫu nhiên ba tag, hỏi mã gì, bao lâu có hàng, có dự phòng không* | ➕➕ |
| 382 | ⭐ Đổi số mục *"Cách dùng bộ biểu mẫu này"* từ **C.10 → C.12**; ⭐ đã kiểm trước: **không chương nào dẫn "C.10"**, chỉ có Ch.39 dẫn C.5 và các chỗ khác dẫn "Phụ lục C" chung — đổi số an toàn | ✔ |
| 383 | ⭐ Sửa bảng ánh xạ giai đoạn: dòng **"Bảng I/O & phần cứng"** tách thành ba dòng đúng với thực tế — *Bảng I/O → C.1* · *Chọn và cấu hình phần cứng → C.10* · *Đặt hàng & nhận hàng → C.11* | ⚠ |

### C — Ch.23: chín bước đầu dự án, và yêu cầu chất lượng cho sáu phần đặc tả

| # | Nội dung | KQ |
|---|:--|:--:|
| 384 | ⭐⭐ **Mục 23.2b mới — chín bước, mỗi bước có: sản phẩm · cái nó chặn · ai duyệt.** Chín bước này nằm gọn trong giai đoạn 1 và 2 của Ch.57; ⭐ khác biệt là Ch.57 **kể chúng như một câu chuyện** về một cỗ máy, còn đây là **bảng công tác dùng được cho máy của bạn** | ➕➕ |
| 385 | ⭐⭐ **Định nghĩa "xong" kiểm được cho từng bước** — ⚠ vì *"đã viết đặc tả rồi"* không phải một trạng thái kiểm được. Chín phát biểu, mỗi phát biểu trả lời được bằng có/không, ⭐ **không có "gần xong"** | ➕➕ |
| 386 | ⚠⚠ **Ba quan hệ chặn quan trọng nhất**, kèm hậu quả khi đảo: đánh giá rủi ro chặn việc chọn phần cứng (đảo → **sửa thiết kế** hoặc ⚠⚠ **hạ chuẩn an toàn cho vừa thiết kế**) · bảng I/O chặn việc đấu tủ (đảo → số dây không khớp tên tag, **theo máy suốt vòng đời**) · phép tính nguồn chặn việc chốt đơn hàng | ➕➕ |
| 387 | ⭐⭐ **Phép kiểm nhanh xem dự án có đi đúng thứ tự không:** hỏi *"đã đặt hàng chưa?"* và *"bảng I/O đã ký chưa?"*. ⚠ Câu đầu **rồi** mà câu sau **chưa** → dự án đang đi ngược, và phần chênh sẽ hiện ra ở khâu đấu tủ | ➕➕ |
| 388 | ⭐⭐ Bảng **"sáu phần đặc tả đạt yêu cầu khi nào"** — mỗi phần có **nội dung tối thiểu**, **phát biểu kiểm được**, và ⚠ **chỗ hay thiếu nhất**. Ví dụ phần 3 hay thiếu **thời gian tối đa từng bước** — thứ về sau chính là timeout, thiếu ở đặc tả thì lập trình sẽ **đoán** | ➕➕ |
| 389 | ⭐⭐ Và một quan sát dùng được ngay: **phần 2 (chế độ) và phần 4 (xử lý bất thường) là nơi chi phí ẩn nấp**, vì ⚡ phần 1, 3, 5 mô tả **máy chạy đúng** — ai cũng hình dung được — còn phần 2 và 4 mô tả **máy không chạy đúng**, trạng thái mà lúc ngồi viết **chưa ai từng thấy**. ⭐ Dấu hiệu: phần 3 dài gấp nhiều lần phần 4 thì **phần 4 còn thiếu**, không phải máy ít lỗi | ➕➕ |

### D — Ch.8 và Ch.57: nối hai biểu mẫu mới vào chỗ chúng thuộc về

| # | Nội dung | KQ |
|---|:--|:--:|
| 390 | ⭐⭐ **Ch.8 mục 8.4** — rút ra kết luận mà hai mục trước của chính nó dẫn tới nhưng chưa nói: nếu thứ tự khe quyết định địa chỉ thì ⭐ **thứ tự khe là một phần của chương trình, chỉ có điều nó không nằm trong tệp dự án**. Nó nằm trong cái rack và trong đầu người đã lắp — ⚠ **cả hai đều không đáng tin sau hai năm** | ➕➕ |
| 391 | ⭐ Kèm **bốn câu** bảng cấu hình phải trả lời được, trong đó câu thứ tư là câu ít ai nghĩ tới: ⭐⭐ *khe trống này để **dự phòng** hay là **chỗ module đã tháo**?* ⚠ Không trả lời được thì người sau sẽ cắm vào đó và **địa chỉ dịch** — đúng lỗi im lặng mà khung cảnh báo ngay phía trên mô tả | ➕➕ |
| 392 | ⭐ **Ch.57 mục 57.4** nay có **"Đầu ra của giai đoạn 2"**, đối xứng với bảng đã có ở 57.3 — năm tài liệu, mỗi tài liệu kèm **"coi là xong khi"** và người duyệt. ⚠ Kèm cảnh báo: giai đoạn này là **điểm không quay lại của phần cứng** | ➕➕ |
| 393 | ⭐ Trỏ hai biểu mẫu mới vào **bảy chỗ đã đòi chúng**: Ch.7, Ch.13 (sau bảng công tác §13.4), Ch.48, Ch.49, Ch.52, Ch.54, Phụ lục D. ⚡ Không có các con trỏ này thì biểu mẫu tồn tại mà **không ai tìm ra** | ➕ |
| 394 | ⚠ Mục lục còn ghi Ch.57 có *"analog & **PID gia nhiệt keo** (Ch.32, 35)"* — ⭐ **đúng chỗ đã sửa trong chương ở đợt 48** (claim #341) mà **quên sửa ở mục lục**. Đã sửa | ⚠ |

### Kết quả đợt 50

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **23** |
| ➕➕ Bổ sung giá trị cao | 15 |
| ➕ Bổ sung | 1 |
| ⚠ Phát hiện thiếu sót / sửa | 5 |
| ✔ Xác nhận không có vấn đề | 2 |
| Biểu mẫu mới | **2** — C.10, C.11 (Phụ lục C: 9 → **11** biểu mẫu) |
| Mục mới | 4 — Ch.23 §23.2b và bảng chất lượng đặc tả, Ch.8 §8.4, Ch.57 §57.4 |
| Chỗ được trỏ tới biểu mẫu mới | 7 chương/phụ lục |

> ⭐⭐ **Bài học 1 — danh mục bàn giao là một thước đo ngược, và là thước rẻ nhất trong năm mươi đợt.**
>
> Phiếu bàn giao liệt kê **thứ sách cho rằng bạn phải có**. ⚡ Đối chiếu ngược từng mục với phần còn
> lại của sách trả lời được câu *"sách có dạy cách làm ra thứ nó đòi không?"* — và hai mục trong
> mười chín là **không**. ⭐ Cùng ý tưởng áp được cho bất kỳ sách kỹ thuật nào có checklist cuối:
> **checklist là lời hứa; đi ngược nó là cách kiểm lời hứa**.

> ⚠ **Bài học 2 — "sách nhắc tới nó nhiều lần" KHÔNG có nghĩa là sách đã dạy nó.**
>
> Cụm *"danh mục vật tư"* xuất hiện ở sáu chỗ, luôn ở thế **được viện dẫn**: *đối chiếu với danh mục
> vật tư · ghi rõ trong danh mục vật tư · danh mục vật tư khi bàn giao*. ⚡ Đọc lướt thì cảm giác
> chủ đề này đã được phủ kỹ. ⭐ Phép đếm đúng không phải *"nhắc bao nhiêu lần"* mà là ⭐⭐ ***"có chỗ
> nào ĐỊNH NGHĨA nó không"*** — và câu trả lời là không.

> ⭐ **Bài học 3 — mỗi biểu mẫu cần một phép thử, không chỉ một danh mục kiểm.**
>
> Danh mục kiểm trả lời *"đã điền đủ chưa"*. ⚡ Phép thử một phút trả lời một câu khác và khó hơn:
> ⭐⭐ ***"điền xong rồi thì nó có dùng được không"***. ⚠ Một bảng cấu hình điền đủ mọi ô mà vẫn
> phải mở tủ ra đếm mới biết tag nằm ở khe nào thì **đã hỏng**, dù không ô nào trống.

---

## Đợt 51 — 2026-09-20 · Soát con trỏ, và hai nhóm triệu chứng mà Phụ lục E bỏ sót

Thước đo đợt này: ⭐ **con trỏ trong sách có trỏ đúng chỗ không** — chưa bộ kiểm nào soát chuyện đó.
Và ⭐ **chỉ mục triệu chứng có phủ hết các loại triệu chứng không**.

### A — Bộ kiểm thứ ba: `kiem_tro_muc.py`

| # | Nội dung | KQ |
|---|:--|:--:|
| 395 | ⭐⭐ **Bộ kiểm mới soát mọi con trỏ dạng *"mục N.M"* · *"§N.M"* · *"Phụ lục X.N"* có trỏ tới tiêu đề CÓ THẬT không.** ⚠ `kiem_nhat_quan.py` soát **trôi dạt thuật ngữ**, không soát số mục — nên lớp lỗi này chưa từng được kiểm | ➕➕ |
| 396 | ⭐ **Kết quả: 1699 con trỏ, 0 sai.** Một kết quả âm tính — và là kết quả đáng ghi, vì nó nói rằng công sức nên dồn sang chỗ khác | ✔ |
| 397 | ⚠ **Đã THỬ bộ kiểm trước khi tin con số 0** — chèn ba con trỏ hỏng (`99.7`, `C.77`, `10.4b`) và một con trỏ đúng (`8.6`), bộ kiểm bắt đúng ba, bỏ qua đúng một. ⭐ Rút từ bài học đợt 36–37: **không tuyên bố công cụ làm được gì mà chưa chạy thử** | ✔ |
| 398 | ⭐ Nối bộ kiểm vào `gop_sach.sh` — từ nay **không ghép được sách nếu có con trỏ hỏng**. Và nó bắt lỗi ngay trong chính đợt này: 25 con trỏ mới viết ở mục D đều được kiểm tự động | ➕ |

### B — ⚠ Con trỏ ĐÚNG SỐ MỤC nhưng TRỎ NHẦM CHƯƠNG — lớp lỗi bộ kiểm không bắt được

⭐⭐ **Đây là phát hiện quan trọng nhất của đợt.** Một con trỏ có thể hoàn toàn hợp lệ về hình thức —
mục tồn tại, số đúng — mà vẫn **dẫn người đọc sang một chương không nói gì về chủ đề đó**.

| # | Chỗ sai | Bằng chứng | KQ |
|---|:--|:--|:--:|
| 399 | ⚠⚠ **Ch.56 mục 56.4**: *"Logic phụ thuộc thời gian quét sẽ chạy khác **(Chương 7)**"* | ⭐ Ch.7 là *ESD & môi trường sản xuất điện tử* và có **0 lần** nhắc "thời gian quét" hay "vòng quét"; Ch.10 có **48 lần**. Sửa thành **Chương 10** | ⚠ |
| 400 | ⚠⚠ **Phụ lục A1**: *"giá trị ngõ vào KHÔNG đổi trong suốt một vòng quét **(Chương 7)**"* | ⭐ Cùng một lỗi, cùng một chương đích sai. ⚡ Hai chỗ cùng sai như nhau gợi ý đây là **vết của một lần đánh số lại chương** chưa cập nhật hết. Sửa thành **Chương 10** | ⚠ |
| 401 | ⚠ **Ch.54**: *"Cấu hình rơ-le an toàn + mã kiểm tra — kèm hồ sơ kiểm định **(Chương 48)**"* | ⭐ Ch.48 có **0 lần** "rơ-le an toàn" và **1 lần** "kiểm định"; Ch.47 có **11** và **10**. Sửa thành **Chương 47** | ⚠ |
| 402 | ⚠⚠ **Tự động hoá lớp lỗi này** | ⚠⚠ **Đã thử và THẤT BẠI.** Cách thử: với mỗi trích dẫn *"(Chương N)"*, lấy các cụm **in đậm** trong cùng câu rồi kiểm xem cụm đó có trong Ch.N không. ⭐ Kết quả **334 nghi vấn — gần như toàn bộ là dương tính giả**, vì cụm in đậm là **diễn giải**, không phải thuật ngữ nguyên văn. ⚡ **Rút lại, không đưa vào bộ kiểm** | ⚠ |
| 403 | ⭐ **Bản thu hẹp** | ⭐ Dùng được: chỉ xét ~17 thuật ngữ lõi **có đúng một chương chủ nhà** (*thời gian quét*→10, *ESD*→7, *load cell*→34, *Modbus*→39…), và chỉ báo khi trích dẫn trỏ sang chương **không hề nhắc** thuật ngữ đó. ⭐ **10 nghi vấn, 3 sai thật** — tỉ lệ dùng được | ✔ |

> ⚠ **Hai lần tôi tự sai trong đợt này, cả hai đều do `grep` phân biệt hoa thường.**
>
> Lần một: kết luận *"Ch.17 không nhắc chống rung"* — ⭐ sai, Ch.17 mục 17.4 có hẳn tiểu mục
> **"Chống rung tiếp điểm nút bấm"** viết hoa chữ C. Lần hai: đếm sót một nửa số lần xuất hiện của
> *"lọc rung"* vì các câu bắt đầu bằng **"Lọc rung"**.
>
> ⭐⭐ **Hệ quả: một kết luận phủ định rút ra từ `grep` phải chạy lại với `-i` trước khi tin.** Cùng
> loại bài học với đợt 36–37, chỉ khác công cụ.

### C — ⭐ Nghi vấn thuật ngữ "chống rung" / "lọc rung" — tan sau khi soi kỹ

| # | Nội dung | KQ |
|---|:--|:--:|
| 404 | Sách dùng **cả hai cụm**: *"lọc rung"* 11 lần (Ch.16, 18, 57, Phụ lục L), *"chống rung"* 5 lần (Ch.4, 9, 51, Phụ lục L, và Ch.17). Thoạt nhìn giống trôi dạt thuật ngữ kiểu *"tra chéo / tham chiếu chéo"* ở đợt 40 | ⚠ |
| 405 | ⭐⭐ **Nhưng không phải trôi dạt: hai cụm nói hai tầng khác nhau.** *Chống rung* là **mục tiêu** (và là từ Phụ lục F chọn làm cặp với *debounce*); *lọc rung* là **cách làm** — cho tín hiệu qua `TON`. Ch.17 mục 17.4 dạy mục tiêu, Ch.18 dạy cách làm. ⭐ **Không mass-replace** — ép một từ sẽ làm hỏng văn ở cả hai chỗ (*"chống rung bằng TON"* dở hơn *"lọc rung bằng TON"*) | ✔ |
| 406 | ⭐ Và con trỏ *"Lọc rung trước khi đưa vào chân đếm (Chương 17, mục 17.4)"* ở Ch.18 — ⭐ **đúng**, vì mục 17.4 chính là chỗ có tiểu mục chống rung nút bấm | ✔ |

### D — Phụ lục E thiếu hai nhóm triệu chứng, và đó là hai nhóm sống lâu nhất

⭐ Đo bằng cách: ⚠ **chương nào CÓ bẫy mà Phụ lục E không dẫn tới?** *(Phép đo lần đầu cho kết quả
sai — 46 chương — vì regex bỏ sót cách Phụ lục E ghi số chương trần trong cột bảng. ⭐ Đo lại đúng:
E dẫn tới **35/58** chương.)*

| # | Nội dung | KQ |
|---|:--|:--:|
| 407 | ⭐ Phần lớn trong 23 chương còn lại **đúng là không nên có** trong một chỉ mục triệu chứng — Ch.13 *chọn PLC*, Ch.23 *đặc tả*, Ch.30 *chuẩn hoá*, Ch.50 *kiểm thử*, Ch.57 *case study*: ⚡ không ai tra chúng lúc hai giờ sáng | ✔ |
| 408 | ⚠⚠ **Nhưng năm chương thì có: Ch.16, 17, 18, 19, 29.** Chúng sinh ra triệu chứng rất thật — đếm sai, bộ định thời không chạy xong, tràn số, đổi công thức không ăn — mà **không nhóm nào trong E.2–E.12 dẫn tới** | ⚠⚠ |
| 409 | ⭐⭐ **Nguyên nhân của lỗ hổng, và nó là một nguyên nhân có hình dạng rõ ràng:** cả mười một nhóm sẵn có đều giả định **máy đã dừng hoặc đã hỏng** — không khởi động được · ngõ vào không lên · chu trình dừng · sản phẩm hỏng · chuyền tắc. ⚡ **Không nhóm nào dành cho trường hợp máy VẪN CHẠY BÌNH THƯỜNG** | ⚠⚠ |
| 410 | ⭐⭐ **E.4b mới — "Thao tác của người vận hành không ăn"**: nhấn một lần ra hai lần · phải giữ nút mới chạy · ⚠⚠ **nút Dừng không dừng được** · nút Reset không xoá được lỗi · ngõ ra bật rồi tự tắt (cuộn dây trùng) · nút chỉ ăn đôi khi | ➕➕ |
| 411 | ⭐⭐ Kèm **phép thử tách đôi bài toán trong ba mươi giây**: mở màn theo dõi, **nhìn bit của nút**. Bit không lên → phần cứng (đi tiếp E.3). Bit lên mà máy không phản ứng → logic. ⚡ Hai nhánh dẫn tới hai nhóm chương khác hẳn nhau | ➕➕ |
| 412 | ⚠⚠ Và một cảnh báo phải có ở đó: **nút Dừng trong chương trình KHÔNG phải chức năng dừng khẩn cấp**. Máy đang dựa vào nút Dừng mềm để đảm bảo an toàn thì vấn đề lớn hơn một nấc thang mắc sai (Ch.47, 48) | ➕➕ |
| 413 | ⭐⭐ **E.5b mới — "Máy chạy bình thường nhưng CON SỐ sai"**: đếm thiếu (xung ngắn hơn vòng quét) · đếm thừa (cạnh giả) · bộ đếm luôn bằng 0 (cực tính chân đặt lại) · tràn số · bộ định thời **đóng băng** vì nằm trong nhánh không được thực thi · hai bộ định thời dùng chung một thể hiện · đổi công thức mà vẫn chạy tham số cũ | ➕➕ |
| 414 | ⭐ **Phép thử rẻ nhất cho cả nhóm**: đặt **một bộ đếm thứ hai trên tín hiệu CHƯA lọc** rồi hiển thị cả hai — hiệu số **chính là số cạnh giả**. ⚡ Đo được thay vì đoán. ⭐ Tổng quát hoá: với mọi con số nghi ngờ, **thêm một phép đo độc lập rồi so**, đừng tranh luận xem con số nào đúng | ➕➕ |
| 415 | ⚠ Vì sao nhóm E.5b nguy hiểm hơn vẻ ngoài: ⭐ con số sai **không làm máy dừng** nên nó sống rất lâu, và nó đi thẳng vào chỗ người ta **ra quyết định** — báo cáo sản lượng, lịch bảo trì theo số lần tác động, truy xuất nguồn gốc. ⚡ Một bộ đếm sai 2 % làm **lịch thay vật tư lệch ba tháng** | ➕➕ |

### Kết quả đợt 51

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **21** |
| ➕➕ Bổ sung giá trị cao | 8 |
| ➕ Bổ sung | 2 |
| ⚠ Sửa lỗi thật | 3 con trỏ trỏ nhầm chương |
| ⚠ Công cụ thử rồi rút lại | 1 |
| ✔ Xác nhận không có vấn đề | 6 |
| Bộ kiểm mới | **1** — `kiem_tro_muc.py`, đã nối vào `gop_sach.sh` |
| Mục mới | 2 — Phụ lục E.4b, E.5b |
| Con trỏ được kiểm tự động từ nay | **1726** |

> ⭐⭐ **Bài học 1 — "hợp lệ" và "đúng" là hai chuyện khác nhau, và bộ kiểm chỉ bắt được cái thứ nhất.**
>
> 1699 con trỏ đều trỏ tới mục **có thật**. ⚡ Ba trong số đó vẫn dẫn người đọc sang **chương không
> nói gì về chủ đề** — và bộ kiểm không thể biết, vì về hình thức chúng hoàn hảo.
>
> ⭐ Hệ quả cho các đợt sau: sau khi một bộ kiểm báo sạch, ⚠ **đừng kết luận "phần này ổn"** — chỉ
> kết luận *"phần này không còn lỗi thuộc loại bộ kiểm đó bắt được"*.

> ⭐⭐ **Bài học 2 — cách tìm lỗ hổng trong một chỉ mục: hỏi nó GIẢ ĐỊNH gì.**
>
> Đếm chương không được dẫn tới cho ra một danh sách dài mà phần lớn là nhiễu. ⭐ Câu hỏi cho ra kết
> quả là câu khác: ***"mười một nhóm này có điểm chung gì?"*** — và điểm chung là **tất cả đều giả
> định máy đã dừng hoặc đã hỏng**.
>
> ⚡ Lỗ hổng của một chỉ mục **không nằm trong những mục nó có**; nó nằm trong **giả định chung của
> tất cả các mục**. Tìm giả định đó rồi phủ định nó — *"nếu máy vẫn chạy bình thường thì sao?"* —
> là ra ngay hai nhóm còn thiếu.

> ⚠ **Bài học 3 — `grep` phân biệt hoa thường, và kết luận phủ định thì không được phép sai.**
>
> Hai lần trong đợt này tôi kết luận *"chương X không nhắc tới Y"* và cả hai lần đều sai vì Y được
> viết hoa ở đầu câu. ⭐ Kết luận **khẳng định** sai thì dễ lộ; kết luận **phủ định** sai thì **âm
> thầm** và dẫn tới sửa nhầm thứ đang đúng. ⚡ Quy tắc từ nay: mọi *"không có X trong Y"* phải chạy
> lại bằng `grep -i` trước khi ghi vào nhật ký.

---

## Đợt 52 — 2026-09-20 · Phụ lục M: khoảng cách giữa bài tập mô phỏng và dự án thật

Nhận xét của chủ dự án: ⭐ *"ở trường chương trình PLC thường chỉ mô phỏng và lập tag I/O đơn giản;
chương trình thực tế còn phải xử lý nhiều vấn đề hơn — cấu hình, cài đặt IP…"*.

> ⭐⭐ **Thước đo của đợt này: sách 58 chương có tự mắc đúng cái lỗ hổng của trường học không?**
>
> ⚡ Đếm số tệp có nhắc tới từng hạng mục cấu hình mà một dự án thật bắt buộc phải làm. ⚠ Kết quả
> cho thấy sách dạy **kỷ luật kỹ thuật** rất kỹ, nhưng có một tầng bị bỏ trống gần như hoàn toàn:
> **những việc phải làm TRONG phần mềm lập trình**.

### A — Đo lỗ hổng

| # | Hạng mục | Số tệp có nhắc | KQ |
|---|:--|:--|:--:|
| 416 | ⚠⚠ **Bộ đệm chẩn đoán** *(diagnostic buffer)* | **0** — trong khi Ch.51 có hẳn một hàng bảo *"đọc bộ đệm lỗi trong phần mềm"* mà không chương nào nói nó là gì | ⚠⚠ |
| 417 | ⚠⚠ **Khởi động nóng / xoá bộ nhớ / vòng quét đầu tiên** | **0** — dù Ch.10 là chương vòng quét và Ch.28 là chương phục hồi | ⚠⚠ |
| 418 | ⚠⚠ **Bảo vệ know-how, bảo vệ mã nguồn** | **0** | ⚠ |
| 419 | ⚠ **Đồng bộ thời gian / múi giờ** | **0–2** — trong khi dấu thời gian là nền của báo động (Ch.43), truy xuất (Ch.42) và chẩn đoán (Ch.51) | ⚠⚠ |
| 420 | ⚠⚠ **Địa chỉ IP, mạng con** | **1 tệp** — và đó là Ch.54, nhắc như một **hạng mục sao lưu**, không phải như việc phải thiết kế | ⚠⚠ |
| 421 | ⚠⚠ **Tham số module** (dải analog, thời gian lọc, loại cảm biến nhiệt) | **1 tệp** — cũng là Ch.54, cũng chỉ như hạng mục sao lưu | ⚠⚠ |
| 422 | Phần đã có | ⭐ Ngược lại, phần **đã có** thì rất chắc: vòng quét (Ch.10), biến giữ được (15 tệp), cưỡng bức I/O (24 tệp), thẻ nhớ và firmware (7–9 tệp), giới hạn mô phỏng (Ch.50 mục 50.6) | ✔ |

> ⭐⭐ **Hình dạng của lỗ hổng rất gọn: sách dạy đầy đủ những gì xảy ra TRÊN MÁY, và dạy đầy đủ
> những gì xảy ra TRONG LOGIC — nhưng gần như không dạy những gì xảy ra TRONG PHẦN MỀM LẬP TRÌNH.**
>
> ⚡ Đó đúng là tầng mà người học ở trường không bao giờ gặp, vì bộ mô phỏng **làm hộ hết**.

### B — Phụ lục M mới

⭐ Chọn làm **phụ lục** chứ không phải chương mới: nó là **danh mục việc phải làm**, đúng thể loại của
Phụ lục C và D; và ⭐ không phải đánh số lại 58 chương.

| # | Mục | Nội dung đáng chú ý | KQ |
|---|---|:--|:--:|
| 423 | **M.1** Khoảng cách trường ↔ thực tế | Bảng bảy hàng đối chiếu. ⭐ Và một phép đo khoảng cách đó: **đếm số thứ phải đặt ĐÚNG trước khi dòng lệnh đầu tiên có ý nghĩa** — mô phỏng: gần như không có; máy thật: sáu nhóm, và ⚠ **phần lớn không báo lỗi biên dịch** | ➕➕ |
| 424 | **M.2** Cấu hình phần cứng | ⭐ Bảng **tham số từng loại module**, và ⚠⚠ ba tham số mà **sai thì không có báo lỗi nào, triệu chứng trông y hệt lỗi lập trình**: kiểu tín hiệu analog · loại cảm biến nhiệt và số dây · thời gian lọc ngõ vào đặt quá dài | ➕➕ |
| 425 | **M.3** Mạng | Địa chỉ tĩnh · tên trạm · sơ đồ địa chỉ · ⭐⭐ **tách mạng máy khỏi mạng nhà máy** để sự cố mạng văn phòng không dừng sản xuất. ⭐ Kèm chi tiết đã xác minh: **xoá bộ nhớ CPU không xoá địa chỉ IP đã lưu, cũng không xoá bộ đệm chẩn đoán** | ➕➕ |
| 426 | **M.4** Khởi động | ⭐ Bảng STOP/STARTUP/RUN; ⭐⭐ bảng đối chiếu **khởi động lại nóng** với **xoá bộ nhớ** (khác nhau ở chỗ dữ liệu giữ được **được giữ** hay **bị xoá**) | ➕➕ |
| 427 | **M.4** — bẫy khi nạp lại | ⚠⚠ Cái bẫy không bài tập nào dạy: ⭐ **nạp lại một khối dữ liệu có thể đặt giá trị giữ được về giá trị khởi tạo** — ⚡ bộ đếm sản lượng, tuổi thọ vật tư, số giờ chạy **về 0 sau một lần sửa chương trình**, và không ai nhận ra cho tới khi cần con số đó | ➕➕ |
| 428 | **M.4** — vòng quét đầu | ⭐⭐ Bảng **nên làm gì / KHÔNG được làm gì** — ⚠⚠ không tự cho phép chuyển động, không tự về gốc. Nguyên tắc: *sau khi có điện lại, máy phải ở trạng thái an toàn và **biết rằng mình không biết gì*** | ➕➕ |
| 429 | **M.5** Đồng hồ | ⭐ Vì sao đáng một mục riêng: công cụ chẩn đoán mạnh nhất là **đối chiếu thời điểm** giữa bản ghi của PLC, màn hình và hệ thống trên — ⚠ ba đồng hồ lệch vài phút thì phép đối chiếu đó **vô nghĩa** | ➕➕ |
| 430 | **M.6** Chẩn đoán của chính CPU | ⭐⭐ *Đọc thứ CPU đã tự ghi lại TRƯỚC khi mở code*. Bộ đệm chẩn đoán ⭐ **sống sót qua cả lệnh xoá bộ nhớ** — là bản ghi pháp y của CPU | ➕➕ |
| 431 | **M.6** — bẫy an toàn | ⚠⚠ **Bẫy an toàn lớn nhất của cả phụ lục:** nhiều hệ cho viết **thủ tục xử lý lỗi** để xoá lỗi nặng rồi chạy tiếp. ⭐ Về kỹ thuật nó chạy; ⚠⚠ về an toàn nó biến *"máy dừng vì có gì đó sai"* thành *"máy chạy tiếp và không ai biết"*. Quy tắc: chỉ dùng để **về trạng thái an toàn rồi dừng có kiểm soát**, không bao giờ để giấu lỗi | ➕➕ |
| 432 | **M.7** Mật khẩu và bảo vệ mã nguồn | ⭐⭐ Nêu rõ đây là **quyết định hợp đồng, không phải quyết định kỹ thuật** — khoá mã rồi bàn giao nghĩa là mỗi lần khách sửa một con số họ phải gọi bạn, ⚠ **và lúc hai giờ sáng thì bạn không nghe máy** | ➕➕ |
| 433 | **M.9** Giới hạn mô phỏng | ⚠⚠ **Mô phỏng KHÔNG kiểm được gì** — bảng hai cột. ⭐ Phát biểu gọn nhất về ranh giới: ⚡ **mô phỏng kiểm được thứ bạn ĐÃ NGHĨ TỚI**; phần lớn sự cố thật đến từ thứ chưa ai nghĩ tới. Và một ranh giới tuyệt đối: ⚠⚠ **không bao giờ nghiệm thu chức năng an toàn bằng mô phỏng** | ➕➕ |
| 434 | **M.10** Danh mục kiểm | 18 mục, chia sáu nhóm; trong đó ⭐⭐ *"đã thử **mất điện giữa chu trình** rồi cấp lại — máy về trạng thái an toàn, không tự chuyển động"* và ⭐ *"con số tích luỹ **đã ghi lại trước khi nạp**"* | ➕➕ |

### C — Nối vào phần còn lại của sách

| # | Việc | KQ |
|---|:--|:--:|
| 435 | ⭐ Ch.50 mục 50.6 *"Giới hạn của mô phỏng"* nay có thêm **nhóm giới hạn thứ hai**: bảng sẵn có chỉ nói về **thế giới vật lý**; nhóm thiếu là **cấu hình** — ⚠ logic đúng hoàn toàn mà máy vẫn sai, không báo lỗi biên dịch nào | ➕➕ |
| 436 | ⭐ Trỏ Phụ lục M vào bốn chỗ đã cần nó: Ch.1 (bảng tra nhanh, dòng *"sắp làm dự án thật đầu tiên"*), Ch.51 (hàng *"đọc bộ đệm lỗi"* nay nói được đọc ở đâu), Ch.54 (thứ tự khôi phục), Phụ lục C.10 (tham số module) | ➕ |
| 437 | ⭐ Đăng ký Phụ lục M vào `gop_sach.sh` và mục lục; **34 con trỏ mới trong M đều được `kiem_tro_muc.py` kiểm tự động ngay khi viết** — bộ kiểm dựng ở đợt 51 dùng được ngay ở đợt 52 | ✔ |

### Kết quả đợt 52

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **22** |
| ➕➕ Bổ sung giá trị cao | 13 |
| ➕ Bổ sung | 1 |
| ⚠⚠ Lỗ hổng lớn phát hiện | 6 hạng mục gần như không có trong sách |
| ✔ Xác nhận không có vấn đề | 2 |
| Phụ lục mới | **1** — Phụ lục M (13 phụ lục → **14**) |
| Nguồn ngoài mới được dẫn | 2 (Siemens S7-1200 System Manual · Rockwell 1756-PM014) |

> ⭐⭐ **Bài học 1 — một cuốn sách kỹ thuật có thể mắc đúng cái lỗ hổng mà nó phê phán.**
>
> Sách này nói rất nhiều về *"đừng chỉ học lý thuyết"*, có 58 chương về kỷ luật kỹ thuật thật, có
> case study đầy đủ. ⚡ Nhưng đo ra thì **bộ đệm chẩn đoán: 0 tệp · khởi động nóng: 0 · đồng bộ thời
> gian: 0 · IP: 1** — đúng những thứ mà người học ở trường không gặp vì **bộ mô phỏng làm hộ**.
>
> ⭐ Lý do rất con người: các hạng mục đó **không thú vị để viết**. Chúng không có bẫy hay, không có
> câu chuyện. ⚠ Nhưng chúng là thứ chặn một dự án thật ở ngày đầu tiên.

> ⭐ **Bài học 2 — câu hỏi của người ngoài tìm ra lỗ hổng mà 51 đợt tự rà không tìm ra.**
>
> Năm mươi mốt đợt trước đều rà **từ bên trong**: đếm bẫy, đếm hình, đếm con trỏ, soi bảng chốt. ⚡
> Không thước nào trong số đó phát hiện được tầng *"việc phải làm trong phần mềm lập trình"*, vì
> ⭐⭐ **mọi thước đo nội bộ đều đo những gì sách ĐÃ CÓ, so với nhau**.
>
> ⭐ Thước duy nhất tìm ra tầng thiếu là một câu hỏi từ bên ngoài: *"người mới ra trường thiếu cái
> gì?"* — ⚡ tức là **so sách với thực tế, không so sách với chính nó**.

---

## Đợt 53 — 2026-09-20 · Đối chiếu MỤC LỤC sách này với mục lục các sách giáo khoa cùng ngành

⭐ Đợt 52 rút ra: **mọi thước đo nội bộ chỉ đo những gì sách đã có, so với nhau**. Đợt này dùng tiếp
một thước **bên ngoài**, và là thước rẻ nhất trong loại đó: ⭐⭐ **so mục lục sách này với mục lục các
sách giáo khoa PLC kinh điển** — thứ mà bộ chỉ mục nguồn (`chi_muc_nguon.json`, 72 tài liệu, 13024
mục) cho làm chỉ bằng một lệnh.

### A — Chương mà ba sách giáo khoa đều có, sách này không có

| # | Nội dung | KQ |
|---|:--|:--:|
| 438 | ⭐ **Petruzella** dành hẳn *"Chapter 3 — Number Systems and Codes"* ở **cả ba bản** (6th ed · bản 2025 · Activities Manual); **Bryan & Bryan** có *"Chapter 2 — Number Systems and Codes"*; **Hugh Jack** có *"13. NUMBERS AND DATA"*. ⚠⚠ Sách này: **hex 0 tệp · BCD 0 tệp · mã Gray 0 tệp** | ⚠⚠ |
| 439 | ⭐ Kiểm xem đây có phải chủ đề *"chỉ có trong trường"* không — và **không phải**: tra bộ tài liệu hãng cho thấy **BCD là lệnh hạng nhất** trong tập lệnh của các hãng phổ biến ở Việt Nam. Đếm số chỗ khớp: **H3U 76 · H5U 41 · tài liệu Mitsubishi 15** | ⚠⚠ |
| 440 | ⭐⭐ Và hãng còn cho hẳn **lệnh chuyên dụng cho thiết bị BCD**: đọc thẳng **công tắc xoay số**, xuất thẳng ra **đèn bảy đoạn**, giải mã bảy đoạn — cộng một họ lệnh quy đổi: nhị phân ↔ BCD, hex ↔ ASCII, tách/gộp byte, tách/gộp 4 bit. ⚡ Nghĩa là người mới làm với các hệ đó **gặp BCD ngay tuần đầu** | ⚠⚠ |
| 441 | ⭐ Ngược lại, hai chủ đề khác trong mục lục các sách đó thì **bỏ đúng**: *Fuzzy Logic* (Bryan ch.17, Hugh Jack ch.26) và *Artificial Intelligence and PLC Systems* (Bryan ch.16) — ⭐ không thuộc phạm vi máy lắp ráp rời rạc | ✔ |
| 442 | ⭐ Và ba chủ đề tưởng thiếu thì **đã có**: *Sequencer* và *Shift Register* (Ch.19 mục 19.6, Ch.25), *Open Controllers* (Ch.2, 13), *Internet* (Ch.45) | ✔ |

### B — Mục 19.5b mới: ba kiểu mã hoá, và cái bẫy của BCD

| # | Nội dung | KQ |
|---|:--|:--:|
| 443 | ⭐ Viết theo hướng **thực dụng, không phải hướng trường học**: mỗi kiểu mã mở đầu bằng ***"bạn gặp nó ở đâu"*** — hex ở mã lỗi và mặt nạ bit; BCD ở công tắc xoay số, đèn bảy đoạn và thiết bị đời cũ; Gray ở bộ mã hoá vị trí tuyệt đối | ➕➕ |
| 444 | ⭐⭐ **Cái bẫy trung tâm, và nó thuộc loại tệ nhất — kết quả sai mà TRÔNG HỢP LÝ**: BCD `25` đọc như nhị phân ra **37**; BCD `99` ra **153**. ⭐ Không báo lỗi, không giá trị vô lý. ⚡ Triệu chứng nhận ra được: **con số luôn lớn hơn giá trị thật, và sai số tăng dần theo giá trị** | ➕➕ |
| 445 | ⭐ Hai điều thực dụng về BCD: nó **phí bit** (16 bit chứa 0–65535 ở nhị phân nhưng chỉ **0–9999** ở BCD), và ⚠ **không được tính toán trên BCD**. Kèm lý do nó vẫn tồn tại: ⭐ **đổi thẳng ra chữ số hiển thị mà không cần phép chia** — đèn bảy đoạn là mạch điện, không phải máy tính | ➕➕ |
| 446 | ⭐⭐ **Mã Gray giải thích bằng cơ chế, không bằng định nghĩa**: ở bộ mã hoá tuyệt đối, các bit đọc từ **các rãnh khác nhau trên cùng một đĩa**; qua ranh giới 7→8 nhị phân đổi **cả bốn bit** và chúng **không bao giờ đổi đúng cùng lúc** — khoảnh khắc đó đọc về có thể là **bất kỳ số nào từ 0 tới 15**. ⭐ Với Gray chỉ một bit đổi nên chỉ có thể ra **7 hoặc 8** | ➕➕ |
| 447 | ⭐ Và phần thực tế đi kèm: ⚡ **thường bạn không phải tự giải mã Gray** — module đã làm. ⚠ Nhưng đặt sai cấu hình Gray/nhị phân thì **vị trí nhảy loạn đúng ở các ranh giới**, một triệu chứng rất dễ bị đổ cho cơ khí | ➕➕ |
| 448 | ⭐⭐ Bảng chọn bốn kiểu theo bất biến **B18**, và một quy tắc rút gọn: ⭐ **quy đổi về nhị phân NGAY TẠI BIÊN, bên trong chương trình chỉ dùng nhị phân** — ⚡ cùng nguyên tắc với tín hiệu analog ở Chương 32 | ➕➕ |
| 449 | ⭐ Thêm **Bẫy 10** ở Ch.19 và **một hàng mới trong Phụ lục E.5b** cho triệu chứng đó — nhóm E.5b vừa dựng ở đợt 51 nhận thêm nội dung ngay đợt sau | ➕ |
| 450 | ⚠ **Hai bộ kiểm bắt lỗi của tôi ngay khi viết.** Bộ kiểm **lát cắt**: dùng chữ *"Modbus"* và *"biến tần"* (lát cắt 3–4) trong Ch.19 (lát cắt 1). Bộ kiểm **tag**: tôi bịa tag `DI_AirPressHigh` không có trong bảng I/O chính thức — ⭐ thay bằng tag thật của máy mẫu, `DI_AirOK`, và ví dụ còn hay hơn vì đó **đúng là một công tắc áp suất** | ⚠ |

### C — Mục 33.8b mới: đọc được cái tên trên bản vẽ của khách

| # | Nội dung | KQ |
|---|:--|:--:|
| 451 | ⭐ **Bryan & Bryan Phụ lục D** có bảng đầy đủ **chữ định danh thiết bị đo** (`TT-101`, `PSH-205`). Sách này có cả một chương về cảm biến quá trình (Ch.33) mà ⚠ **không nhắc quy ước đó một lần nào** | ⚠ |
| 452 | ⭐⭐ Viết gọn thành một mục, và xoáy vào điều có ích nhất cho **người lập trình**: ⚡ **chữ thứ hai quan trọng hơn chữ thứ nhất**, vì nó quyết định kênh loại nào. `PT` là **analog**, `PS` là **số** — cùng đo áp suất, hai dòng khác hẳn nhau trong bảng I/O, hai module khác nhau | ➕➕ |
| 453 | ⚠ Kèm cảnh báo ranh giới: đây là **quy ước ĐỌC HIỂU**, không phải quy ước đặt tên tag. ⭐ `PSH-205` là tên trên bản vẽ, `DI_AirPressHigh` là tên trong chương trình, và **bảng I/O là chỗ ghi cả hai cạnh nhau** | ➕ |
| 454 | ⭐ Và ghi rõ phạm vi thật: quy ước này đến từ **ngành quá trình**; máy lắp ráp rời rạc thường không vẽ bản vẽ kiểu đó — ⚡ **nhưng datasheet thiết bị đo thì vẫn dùng**, và khách ngành quá trình thì đưa bản vẽ kiểu đó cho bạn | ✔ |

### Kết quả đợt 53

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **17** |
| ➕➕ Bổ sung giá trị cao | 8 |
| ➕ Bổ sung | 2 |
| ⚠⚠ Lỗ hổng lớn phát hiện | 3 chủ đề (hex · BCD · mã Gray) + quy ước tên thiết bị đo |
| ⚠ Lỗi của tôi, bộ kiểm bắt được | 2 |
| ✔ Xác nhận không có vấn đề | 3 |
| Mục mới | 2 — Ch.19 mục 19.5b, Ch.33 mục 33.8b |
| Nguồn ngoài mới được dẫn | 1 (Bryan & Bryan Phụ lục D) |

> ⭐⭐ **Bài học 1 — mục lục của sách khác là thước đo bên ngoài rẻ nhất có thể có.**
>
> Đợt 52 tìm ra lỗ hổng nhờ một câu hỏi từ người thật. ⚡ Nhưng không phải lúc nào cũng có câu hỏi
> đó. ⭐ Bộ chỉ mục nguồn đã nằm sẵn trong kho từ lâu và **chưa lần nào được dùng theo cách này**:
> in mục lục cấp 1 của bốn sách giáo khoa cùng ngành, rồi hỏi ⭐⭐ ***"chương nào họ có mà mình
> không?"*** — mất vài phút, ra ngay một chương mà **cả ba sách đều có**.
>
> ⚠ Và nó cũng cho câu trả lời ngược, quan trọng không kém: **Fuzzy Logic** và **AI** thì cả hai
> sách kia đều có mà bỏ đúng — ⭐ **không phải cái gì sách khác có cũng là thiếu sót**.

> ⚠⚠ **Bài học 2 — "nghe như chủ đề trường học" là một thiên kiến, và nó có cách kiểm.**
>
> Hex, BCD, mã Gray bị bỏ vì **chúng nghe như bài giảng năm nhất**. ⭐ Phép kiểm để bác bỏ thiên
> kiến đó rất cụ thể: ⚡ **tra chính bộ tài liệu hãng xem nó có bao nhiêu lệnh dành cho chủ đề
> này**. Kết quả: BCD có mặt **76 lần** trong một tập lệnh, kèm lệnh chuyên dụng cho công tắc xoay
> số và đèn bảy đoạn.
>
> ⭐ Một chủ đề mà **hãng dành hẳn lệnh riêng** thì không thể là chủ đề chỉ có trong trường.

---

## Đợt 54 — Đào sâu thước ngoài: mục lục cấp 2, và một cái bẫy đánh số

⭐ Đợt 53 so mục lục **cấp 1**. Đợt này xuống **cấp 2**, và thử thêm một thước nữa: ⭐ **các đặc tả
mở và whitepaper trong kho đã được khai thác hết chưa?**

### A — Thước "dự phòng mạng": tra ra **không có lỗ hổng**

| # | Nội dung | KQ |
|---|:--|:--:|
| 455 | Kho có *Rockwell Resilient Ethernet Architecture* và *EtherCAT/TSN whitepaper*; sách **0 lần** nhắc `DLR` `MRP` `PRP` `HSR`. Thoạt nhìn giống lỗ hổng | ⚠ |
| 456 | ⭐ **Không phải.** Ch.40 mục 40.6 đã phủ đúng phần cần phủ — cấu trúc vòng, và ⭐⭐ bẫy trung tâm *"một vòng Ethernet **không có giao thức quản lý** thì không phải dự phòng — nó là **một sự cố**"*, gói quảng bá chạy vô tận làm **mạng chết hoàn toàn**. ⭐ Các tên viết tắt là **đặc thù hãng** và được trừu tượng hoá có chủ ý | ✔ |

### B — Mục lục cấp 2: một mục thật trong 49 mục nghi

| # | Nội dung | KQ |
|---|:--|:--:|
| 457 | ⚠ Phép lọc *"mục cấp 2 nào không có từ khoá nào xuất hiện trong sách"* cho **49 mục** — và ⭐ **gần như toàn bộ là dương tính giả**, vì sách viết bằng tiếng Việt nên `Contactors`, `Latching Relays`, `Cascading Timers` không khớp chuỗi dù nội dung đã có | ⚠ |
| 458 | ⭐ Nhưng một mục thì thật: **`Octal System`** — Petruzella mục 3.4, Bryan chương 2 liệt kê *"binary, **octal**, decimal, hexadecimal"* là bốn hệ dùng khi **gán địa chỉ I/O**. Sách này: chỉ **1 lần**, trong Phụ lục A1 | ⚠⚠ |

### C — Và nó không phải chuyện sách vở: hai hãng phổ biến ở Việt Nam đánh số I/O theo hệ 8

| # | Bằng chứng | KQ |
|---|:--|:--:|
| 459 | ⭐⭐ Tài liệu Inovance H5U ghi rõ: `X0 to X1777` — **1024 điểm, octal**; `Y0 to Y1777` — **1024 điểm, octal**. Xác nhận ở **hai tài liệu riêng** (Instruction Guide và Programming Guide) | ⚠⚠ |
| 460 | ⚠⚠ **Và trong CÙNG bảng thiết bị đó, `M0 to M7999` là 8000 điểm — thập phân.** ⭐ Hai hệ đếm trong một bảng, không có gì đánh dấu | ⚠⚠ |
| 461 | ⭐⭐ **Hậu quả trực tiếp: `X10` là ngõ vào thứ CHÍN, không phải thứ mười một** — và không có `X8`, `X9`. ⚡ Đánh số dây trong tủ từ 1 tới 16 rồi ánh xạ thẳng sang `X1`…`X16` là **sai từ điểm thứ tám trở đi**, mà ⚠ **trình biên dịch không báo gì** vì `X16` là địa chỉ hợp lệ — chỉ không phải cái bạn tưởng | ➕➕ |
| 462 | ⭐⭐ **Phép kiểm trong đầu, mất năm giây, và nó dùng chính con số trong tài liệu:** `1777` nếu là thập phân thì phải là 1778 điểm; tài liệu ghi **1024 điểm**, mà `1777` hệ 8 đúng bằng **1023** → ⭐ dải đó **chắc chắn bát phân**. Còn `M7999` ↔ 8000 điểm thì khớp hệ 10 | ➕➕ |
| 463 | ⭐ Bổ sung vào **Ch.11 mục 11.8** (chỗ đã bàn mô hình thiết bị), cộng **Bẫy 10** của Ch.11, một hàng ở **Phụ lục E.3** *(tám ngõ vào đầu đúng, từ cái thứ chín trở đi sai)*, và một hàng ở bảng chọn hệ đếm của **mục 19.5b** vừa viết ở đợt 53 | ➕➕ |
| 464 | ⭐ Cách né hẳn nhóm lỗi: **dùng nhãn có tên**, ánh xạ tên ↔ thiết bị ở đúng một chỗ. ⚠ Nhưng vẫn phải **đọc được** số thiết bị, vì bảng I/O, sơ đồ điện và chương trình cũ đều nói bằng ngôn ngữ đó | ➕ |

### Kết quả đợt 54

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **10** |
| ➕➕ Bổ sung giá trị cao | 3 |
| ➕ Bổ sung | 1 |
| ⚠⚠ Lỗ hổng thật | 1 — đánh số bát phân |
| ✔ Xác nhận không có vấn đề | 1 — dự phòng mạng đã phủ đủ |
| ⚠ Thước cho nhiều nhiễu | 1 — lọc từ khoá tiếng Anh trên sách tiếng Việt |

> ⭐⭐ **Bài học 1 — thước ngoài mòn nhanh hơn thước trong, và đó là chuyện bình thường.**
>
> Đợt 53 dùng mục lục cấp 1: ra một chương lớn còn thiếu. ⚡ Đợt 54 xuống cấp 2: ra **một mục**, và
> phải lọc qua 48 dương tính giả để thấy nó. ⭐ Không phải thước hỏng — mà là **thước đã làm xong
> phần việc của nó**. Ghi lại để đợt sau không xuống tiếp cấp 3 và mong đợi nhiều.

> ⚠ **Bài học 2 — lọc theo từ khoá tiếng Anh trên một cuốn sách tiếng Việt cho tỉ lệ nhiễu ~98 %.**
>
> `Contactors`, `Latching Relays`, `Hydraulics` đều báo "thiếu" trong khi nội dung đã có bằng tiếng
> Việt. ⭐ Phép lọc chỉ hữu ích cho ⭐⭐ **thuật ngữ mà tiếng Việt vẫn giữ nguyên dạng tiếng Anh** —
> `octal`, `BCD`, `Gray`, tên giao thức, tên lệnh. ⚡ Lần sau nên **giới hạn phép lọc vào đúng nhóm
> từ đó** ngay từ đầu, thay vì lọc tất rồi đọc tay 49 dòng.

> ⭐ **Bài học 3 — con số trong tài liệu hãng tự tố cáo hệ đếm của nó.**
>
> Không cần tài liệu nào nói *"đây là hệ 8"*. ⚡ Chỉ cần **số điểm** và **địa chỉ cuối** là suy ra
> được: `1777` ↔ 1024 điểm chỉ đúng ở hệ 8. ⭐⭐ Đây là loại phép kiểm đáng dạy, vì nó **không phụ
> thuộc hãng nào** và dùng được ngay cả khi tài liệu viết bằng thứ tiếng bạn không đọc được.

---

## Đợt 55 — Soát tính chính xác: một khẳng định sai do chủ dự án chỉ ra, và ba chỗ cùng bệnh

⭐ Chủ dự án đọc mục 4.5 và phản biện: *"sách nói cảm biến tiệm cận cảm ứng được dùng nhiều nhất,
nhưng các máy tôi gặp có vẻ không phải vậy."* ⚡ Kèm yêu cầu soát rộng: tính thống nhất, đánh số, và
**nội dung tự bịa**.

### A — ⚠⚠ Khẳng định sai, và sách tự mâu thuẫn với chính nó

| # | Nội dung | KQ |
|---|:--|:--:|
| 465 | ⚠⚠ Ch.4 mục 4.5 viết *"Đây là loại được dùng nhiều nhất trong máy tự động hoá"* về cảm biến tiệm cận cảm ứng. ⭐ **Không nguồn, và không đúng như một phát biểu chung** | ⚠⚠ |
| 466 | ⭐⭐ **Bằng chứng mạnh nhất nằm ngay trong sách:** đếm bảng I/O đầy đủ của máy mẫu (Phụ lục J mục J.2) được **10 cảm biến reed xy-lanh · 4 cảm biến quang · 0 cảm biến tiệm cận cảm ứng**. ⚡ Sách khẳng định một loại là phổ biến nhất trong khi **máy mẫu của chính nó không dùng cái nào** | ⚠⚠ |
| 467 | ⭐ Sửa: bỏ câu đó, thay bằng mục mới **"Loại nào dùng nhiều nhất? Đó là câu hỏi sai"** — bảng năm nhóm máy với loại chiếm đa số ở mỗi nhóm, và ⭐⭐ **bốn câu hỏi chọn cảm biến** (vật là gì · chạm được không · môi trường · tầm xa) không nhắc tới chữ *"phổ biến"* nào | ➕➕ |
| 468 | ⭐ Nêu thẳng cả hai phía để người đọc không đổi một thiên kiến lấy một thiên kiến khác: máy gia công kim loại thì **tiệm cận cảm ứng đúng là chiếm đa số**; máy lắp ráp khí nén thì **reed xy-lanh**; lắp ráp điện tử thì **quang** — ⚡ vì board mạch không phải khối kim loại liền | ➕➕ |

### B — Cùng bệnh, ba chỗ khác

| # | Chỗ | Sửa | KQ |
|---|---|:--|:--:|
| 469 | ⚠⚠ **Ch.38 và `case_study`** | *"thiết bị nối tiếp **phổ biến nhất** trong chế tạo máy"* (RS-485/Modbus RTU) — ⭐⭐ **mâu thuẫn trực tiếp với Phụ lục J mục J.9**, nơi chính sách liệt kê *"bộ điều khiển nhiệt độ rời có còn phổ biến không"* là **hạng mục CHƯA XÁC MINH**. Sửa cả hai chỗ thành *"kiểu ghép thường gặp"* và dẫn thẳng tới J.9 | ⚠⚠ |
| 470 | ⚠ **Ch.5** | *"van điện từ là cơ cấu chấp hành phổ biến nhất trên máy tự động hoá"* → thu hẹp thành **"chiếm đa số trên máy lắp ráp dùng khí nén"**, kèm đối chứng: máy gia công kim loại thì động cơ và trục chiếm đa số | ⚠ |
| 471 | ⚠ **Ch.39** | *"Modbus vẫn là giao thức phổ biến nhất"* → ⭐ **hai cách đếm cho hai câu trả lời**: theo **số nút mạng** thì Ethernet công nghiệp đã vượt ở máy đời mới; theo **số chủng loại thiết bị có hỗ trợ** thì Modbus vẫn dẫn. ⚡ Nên câu đáng nói là **"ở đâu cũng gặp"**, không phải **"nhiều nhất"** | ➕➕ |
| 472 | ⭐ Quét toàn sách | **294 câu khẳng định tuyệt đối**, lọc còn **55 câu** nhóm nguy hiểm. ⭐⭐ Phần lớn là *"lỗi phổ biến nhất"*, *"nhầm lẫn phổ biến nhất"* — **nhận định nghề, đúng thể loại, giữ nguyên**. ⚠ Chỉ nhóm **khẳng định về thị trường** mới phải sửa | ✔ |

### C — Bộ kiểm thứ tư: đánh số

| # | Nội dung | KQ |
|---|:--|:--:|
| 473 | ⭐ `kiem_danh_so.py` mới soát ba dãy số mà chưa bộ kiểm nào đụng tới: **số mục** (trùng · thủng · sai thứ tự · sai số chương), **số hình** (nhắc *Hình N.k* mà không có chú thích hình đó), **số bẫy** (dãy 1,2,3… có liền mạch không) | ➕➕ |
| 474 | ⭐⭐ **Kết quả: 0 lỗi** — và đã **thử trước khi tin**: chèn ba lỗi giả (đổi 17.5→17.7 · đổi BẪY 3→BẪY 4 · nhắc *Hình 17.9* không tồn tại), bộ kiểm bắt đủ **5 thông báo** rồi khôi phục | ✔ |
| 475 | ⭐ Nối vào `gop_sach.sh` — **bốn bộ kiểm** nay chặn việc ghép sách | ➕ |

### D — Soát số liệu bịa: ba chỗ tra ra ĐÚNG

⭐⭐ **Kết quả âm tính, và đáng ghi đúng bằng kết quả dương tính.**

| # | Con số bị nghi | Đối chiếu | KQ |
|---|:--|:--|:--:|
| 476 | Ch.9 mục 9.5 ghi máy mẫu có **8 reed**, nhưng Phụ lục J liệt kê **5 cặp = 10 reed** | ⭐ **Không sai**: mục 9.5 ước tính cho **lát cắt 1**, mà cặp reed cửa chắn thuộc **lát cắt 5**. 4 cặp × 2 = đúng 8. ⚡ Cột *"Lát cắt"* của Phụ lục J giải quyết mâu thuẫn tưởng tượng này | ✔ |
| 477 | Ch.8 mục 8.7b: **"lắp đứng giảm ~10 °C định mức"** | ⭐⭐ **Đúng nguyên văn**: tài liệu Siemens ghi *"For vertical mounting, the maximum allowable ambient temperature is reduced by 10 degrees C"*, và bảng thông số xác nhận **−20…60 °C nằm ngang → −20…50 °C lắp đứng** | ✔ |
| 478 | Ví dụ kèm theo — *"module ghi 0–55 °C lắp ngang còn 0–45 °C khi lắp đứng"* | ⭐ Là ví dụ **chung chung có chủ ý**, không phải số của Siemens; con số chịu tải của lập luận là **hiệu 10 °C** thì đã xác minh. ⭐ Giữ nguyên | ✔ |
| 479 | Khảo sát diện rộng | ⭐ **206 con số kỹ thuật** khác nhau, **90 con chỉ xuất hiện một lần**. Mẫu kiểm không tìm ra con số nào bịa — các con số đáng ngờ nhất đều có dẫn nguồn tại chỗ | ✔ |

### E — "Nhắc tới mà không nói cách phân biệt": quét xong, chỉ có đúng chỗ chủ dự án chỉ

| # | Nội dung | KQ |
|---|:--|:--:|
| 480 | ⭐ Dựng phép quét theo đúng khuôn mẫu của lỗi vừa tìm ra: **mục nào liệt kê ≥3 LOẠI có tên tiếng Anh mà không có bảng so sánh lẫn hướng dẫn chọn?** | ➕ |
| 481 | ⭐⭐ Cả sách chỉ có **hai mục ứng viên**: Ch.4 mục 4.5 *(5 loại cảm biến)* và Ch.17 mục 17.2 *(3 loại timer)*. ⚡ Ch.17 vốn đã có bảng; Ch.4 **đạt sau khi sửa ở mục A**. ⭐ Nhóm này nay sạch | ✔ |

### Kết quả đợt 55

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **17** |
| ⚠⚠ Khẳng định sai đã sửa | 4 chỗ (Ch.4 · Ch.5 · Ch.38 + case study · Ch.39) |
| ➕➕ Bổ sung giá trị cao | 4 |
| ✔ Xác nhận không có vấn đề | 7 |
| Bộ kiểm mới | **1** — `kiem_danh_so.py`, đã nối vào `gop_sach.sh` (nay **4** bộ kiểm) |
| Mục mới | 1 — Ch.4 *"Loại nào dùng nhiều nhất? Đó là câu hỏi sai"* |

> ⭐⭐ **Bài học 1 — loại sai nguy hiểm nhất của cuốn sách này không phải số liệu, mà là TÍNH TỪ SO
> SÁNH NHẤT.**
>
> Soát 206 con số kỹ thuật: không tìm ra con nào bịa, vì mỗi con số đều **có chỗ để tra**. ⚡ Nhưng
> *"phổ biến nhất"* thì **không có chỗ nào để tra** — nó trôi vào bản thảo như một câu nối, không ai
> đòi nguồn, và nó **nghe có thẩm quyền**.
>
> ⭐ Quy tắc từ nay: mỗi *"…nhất"* về **thị trường hay tần suất dùng** phải hoặc **có nguồn**, hoặc
> **thu hẹp phạm vi** (*"chiếm đa số trên nhóm máy X"*), hoặc **bị xoá**. ⚠ *"…nhất"* về **lỗi hay
> sai lầm** thì khác — đó là nhận định nghề, và sách được phép nêu.

> ⭐⭐ **Bài học 2 — máy mẫu là máy phát hiện nói dối của chính cuốn sách.**
>
> Không cần khảo sát thị trường để bác bỏ *"tiệm cận cảm ứng phổ biến nhất"*. ⚡ Chỉ cần **đếm bảng
> I/O của DP-01**: 10 reed, 4 quang, **0 tiệm cận**. ⭐ Một cuốn sách có máy mẫu xuyên suốt thì mọi
> khẳng định chung của nó đều **kiểm được ngược lại bằng chính máy mẫu** — và chỗ nào máy mẫu mâu
> thuẫn với lời khẳng định thì **ít nhất một trong hai cái sai**.

> ⚠ **Bài học 3 — người đọc thật tìm ra thứ năm mươi tư đợt tự rà không tìm ra.**
>
> Đợt 52 đã ghi *"mọi thước đo nội bộ chỉ đo những gì sách đã có, so với nhau"*. ⭐ Đợt này là ví dụ
> thứ hai, và mạnh hơn: ⚡ phép quét *"liệt kê loại mà không có cách phân biệt"* — dựng **sau** khi
> biết lỗi — quét cả sách ra **đúng hai mục**, một trong đó là mục chủ dự án đã chỉ. ⭐⭐ Phép quét đó
> **hoàn toàn dựng được trước**; chỉ là **không ai nghĩ ra nếu chưa thấy một ví dụ thật**.

---

## Đợt 56 — Thước "lịch sử git", và một cụm trích dẫn tố cáo lần đánh số lại chương

⭐ Thước mới, và là thước đáng lẽ phải dùng từ lâu vì nó **đã nằm sẵn trong kho**: ⭐⭐ **đếm số lần
commit chạm vào từng tệp chương**. ⚡ Chương nào qua 55 đợt vẫn chỉ có **một** commit thì nó
**chưa từng được rà**, bất kể nhật ký ghi gì.

### A — Chương chưa từng sửa

| # | Nội dung | KQ |
|---|:--|:--:|
| 482 | ⭐ Đếm commit từng tệp: **Ch.58** *(chương cuối sách, 433 dòng)* chỉ có **1 commit** — viết một lần, ⚠ **chưa từng sửa qua 55 đợt**. Cùng nhóm: Phụ lục G (1), Phụ lục H (2), Ch.2 · Ch.12 · Ch.46 (2 mỗi chương) | ⚠ |
| 483 | ⭐ Đọc lại Ch.58: **không có lỗi lỗi thời** — chương cố ý **không nêu tên chứng chỉ, giá, hay hãng cụ thể**, chỉ nêu nguyên tắc (*"chứng chỉ có giá trị khi nó chứng minh thứ khó tự học hoặc thứ pháp luật yêu cầu"*). ⭐ Thiết kế đúng cho một chương dễ mục nhất | ✔ |
| 484 | ⚠ Nhưng có một trích dẫn sai: câu phỏng vấn *"Bạn ghi tài liệu thế nào?"* dẫn **Chương 24**. ⭐ Ch.24 là *đại số Boolean*, có **1 lần** nhắc "tài liệu/chú thích"; Ch.30 có **21 lần** và có hẳn mục 30.4 *"Comment — viết như nhật ký kỹ thuật"*. Sửa → **Chương 30** | ⚠ |

### B — ⚠⚠ Lời hứa Ch.1 không khớp với Phụ lục G

| # | Nội dung | KQ |
|---|:--|:--:|
| 485 | ⚠⚠ Ch.1 viết: *"**Mọi mục trong Phụ lục G đều ghi ngày kiểm tra**"* và *"Phụ lục G liệt kê các phần mềm miễn phí **kèm giới hạn bản quyền thật của từng cái**"* | ⚠⚠ |
| 486 | ⭐⭐ **Phụ lục G làm điều ngược lại, và nói rõ là cố ý:** *"phụ lục này **cố ý KHÔNG liệt kê điều kiện bản quyền cụ thể**"* · *"Đừng tin bảng nào — **kể cả bảng này**"*. Nó không ghi ngày cho bất kỳ mục nào; thay vào đó cho **danh mục câu hỏi tự kiểm** (G.5) và bắt **người đọc** ghi ngày | ⚠⚠ |
| 487 | ⭐ Sửa Ch.1 để mô tả đúng — và cách làm thật của G **đáng nói hơn lời hứa cũ**: ⚡ *"một danh mục câu hỏi thì không hết hạn; một bảng điều kiện thì có"* | ➕➕ |

### C — Cụm "Chương 24" và dấu vết một lần đánh số lại chương

⭐ Mở rộng phép quét trích dẫn của đợt 51 từ 17 lên **31 thuật ngữ lõi**. Ra **19 chỗ nghi**, xét tay
còn **6 chỗ sai thật** — và chúng **không rải rác**.

| # | Chỗ sai | Bằng chứng | KQ |
|---|:--|:--|:--:|
| 488 | ⚠⚠ **Bốn chỗ** dẫn **"Chương 24"** cho việc **ghi chú thích**: Ch.53, Ch.56, Phụ lục I, và Ch.58. Chủ nhà là **Ch.30 mục 30.4** | ⭐⭐ Bốn chỗ cùng sai y hệt là dấu vết của một lần **ĐÁNH SỐ LẠI CHƯƠNG** chưa cập nhật hết — không phải bốn lần sơ ý độc lập | ⚠⚠ |
| 489 | ⚠ **Phụ lục A1**: *"Vì sao vòng quét quan trọng — **Chương 7**"* | ⭐ Ch.7 là *ESD*, **0 lần** nhắc "vòng quét". ⚡ Và đây là **chỗ thứ hai trong CÙNG tệp** — đợt 51 đã sửa một chỗ Ch.7→Ch.10 ở đây mà **bỏ sót chỗ này**, vì phép quét đợt đó chỉ bắt dạng `(Chương N)` và `Chương N mục`, không bắt dạng **ô bảng** *(Chương N đứng một mình trong một ô)* | ⚠ |
| 490 | ⚠ **Ch.18**: *"kiểm **nối đất**, đi dây tách khỏi cáp động lực (**Chương 51**)"* | ⭐ Ch.51 có **0 lần** "nối đất"; Ch.49 có **7 lần** và 3 lần "tách cáp". Sửa → **Chương 49** | ⚠ |
| 491 | Phần còn lại | ⭐ **13 chỗ là báo nhầm** — câu trích dẫn cho **một vế khác** của cùng câu (ví dụ: *"IO-Link chậm hơn… việc **đếm xung tốc độ cao** (Ch.18)"* — dẫn Ch.18 cho đếm xung, không cho IO-Link). ⭐ Đã ghi cả 13 vào danh sách bỏ qua để đợt sau không xét lại | ✔ |

### D — Bộ kiểm thứ năm: `kiem_chu_nha.py`

| # | Nội dung | KQ |
|---|:--|:--:|
| 492 | ⭐⭐ **Hai đợt liên tiếp tìm ra cùng một lớp lỗi bằng tay** (đợt 51: 3 chỗ · đợt 56: 6 chỗ) — đủ để biến thành công cụ. Bộ kiểm dùng bảng **30 thuật ngữ có đúng một chương chủ nhà**, và báo khi một dòng vừa chứa thuật ngữ vừa trích dẫn chương **không hề nhắc** thuật ngữ đó | ➕➕ |
| 493 | ⭐ Bộ kiểm này **được phép báo nhầm** — nên nó có tệp cấu hình với danh sách **bỏ qua** cho 16 trường hợp đã xét tay. ⚡ Mỗi lần xét xong một trường hợp là **xét vĩnh viễn**, không phải xét lại mỗi đợt | ➕➕ |
| 494 | ⭐ Đã **thử trước khi tin**: chèn *"cách ghi chú thích, xem Chương 12 mục 12.1"* vào Ch.30 — bắt đúng; khôi phục — về 0. Nối vào `gop_sach.sh`: nay **năm bộ kiểm** chặn việc ghép sách | ✔ |

### Kết quả đợt 56

| | Số lượng |
|---|---|
| Khẳng định đã kiểm | **13** |
| ⚠⚠ Lỗi thật đã sửa | 6 trích dẫn trỏ nhầm chương + 2 câu Ch.1 mô tả sai Phụ lục G |
| ➕➕ Bổ sung giá trị cao | 3 |
| ✔ Xác nhận không có vấn đề | 3 |
| Bộ kiểm mới | **1** — `kiem_chu_nha.py` + cấu hình (nay **5** bộ kiểm) |

> ⭐⭐ **Bài học 1 — lịch sử git là bản đồ chỗ chưa ai nhìn, và nó luôn có sẵn.**
>
> Nhật ký này ghi rất kỹ **đã rà cái gì**; nhưng nó không ghi được **chưa rà cái gì**, vì không ai
> viết nhật ký về việc mình không làm. ⚡ `git log` thì ghi hộ: **Ch.58 một commit** là một sự thật
> không cãi được, và nó chỉ mất một lệnh để biết. ⭐ Đáng chạy lại mỗi vài đợt.

> ⭐⭐ **Bài học 2 — bốn lỗi giống hệt nhau không phải bốn lỗi, mà là MỘT lỗi có bốn dấu vết.**
>
> Bốn chỗ dẫn *"Chương 24"* cho chú thích, hai chỗ dẫn *"Chương 7"* cho vòng quét. ⚡ Sơ ý độc lập
> thì sai **mỗi lần một kiểu**; sai **giống hệt nhau** thì có nguyên nhân chung — ở đây là một lần
> **đánh số lại chương**. ⭐ Hệ quả thực dụng: tìm thấy một chỗ thuộc loại này thì **phải quét cả
> sách tìm anh em của nó**, đừng sửa lẻ.

> ⚠ **Bài học 3 — phép quét của tôi ở đợt 51 đã bỏ sót vì thiếu một dạng cú pháp.**
>
> Đợt 51 bắt `(Chương N)` và `Chương N mục` nhưng **không bắt ô bảng `| Chương N |`** — nên nó sửa
> một chỗ trong Phụ lục A1 và **để lại chỗ thứ hai ngay trong cùng tệp**. ⭐ Bài học không phải
> *"cẩn thận hơn"* mà là: ⭐⭐ **khi viết phép quét, liệt kê trước MỌI DẠNG mà thứ cần tìm có thể
> mang** — ở đây là ba dạng trích dẫn, và tôi mới nghĩ ra hai.

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
| Nền tảng PLC | ⭐ **Đã đối chiếu hết** — 7–12, 14, 18, 19 (đợt 4, 10, 15, 22, 27, **32**) | — | — |
| Ngôn ngữ | ⭐ **Đã đối chiếu hết** — 15, 16, 17, 20, 21 (đợt 16, 17, 19, 20, 21) | — | — |
| Thiết kế | ⭐ **Đã đối chiếu hết** — 22–30 (đợt 23, 24, 27, 28, **31**) | — | — |
| Chẩn đoán & vận hành | ⭐ **Đã đối chiếu hết** — 43, 49, 51, 52, 53, 55 (đợt 18, 26, 30, **33**) | — | — |
| Không kiểm được bằng nguồn | 13, 23–24, 28–29, 54, 56, 58 | — | ⭐ Chủ yếu là phương pháp và kinh nghiệm nghề |
| ⭐ Đã soi ở đợt 48–49 | 1, 2, 9, 17, 18, 25–27, 30, 33, 36, 57 | Kuphaldt ×2, Siemens ×2, Rockwell ×3, Mitsubishi | — |

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
| ⭐ **SEMI (E10, E79…)** | ⭐⭐ **ĐÃ CÓ BẢN GỐC** từ 2026-09-05 → **dẫn được số mục**; vẫn ⚠ **không sao chép bảng/công thức nguyên văn** |
| Thị trường thiết bị hiện hành | Hai giả định của máy mẫu (đầu đọc mã 2D Ethernet · bộ điều khiển nhiệt rời RS-485) vẫn **chưa xác minh** — Phụ lục J §J.9 |
| ⚠ IO-Link System Description | ⚠⚠ **ĐÍNH CHÍNH đợt 41:** text trích được bình thường — nhưng tệp là **bản in một trang web**, toàn menu điều hướng, ⭐ **không có đoạn văn nào**. Không có gì để đối chiếu; đừng tra lại |

---

> ⚠⚠ **Nhắc lại giới hạn của cả nhật ký này.**
>
> Đối chiếu với tài liệu **không** thay thế việc chuyên gia duyệt. Với Ch.3, 6, 47, 48 và Phụ lục D,
> kết luận đúng nhất mà bảng trên cho phép là: ⭐ *"đã đối chiếu với tài liệu diễn giải X, không thấy
> mâu thuẫn"* — ⚠ **không phải** *"đã kiểm, an toàn"*.
>
> Cờ ⚠ trên các chương đó ⭐ **chỉ chuyên gia an toàn người thật gỡ được**.
