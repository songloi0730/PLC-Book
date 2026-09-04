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

## Chương CHƯA được đối chiếu

⚠ **Đây là phần quan trọng nhất của nhật ký.** Chương không có trong bảng trên nghĩa là **chưa ai
kiểm**, không phải "không có lỗi".

| Nhóm | Chương | Nguồn sẵn có | Ưu tiên |
|---|---|---|---|
| ⚠⚠ **An toàn** | ⭐ **Đã đối chiếu hết** — 3, 6, 47, 48, Phụ lục D (đợt 1, 3, 4, 7). ⚠ Cờ ⚠ vẫn giữ | SICK ×3, Schneider, DGUV/IFA, PPSA | ⭐⭐ **Cao nhất** |
| Đo lường & analog | ⭐ **Đã đối chiếu** (đợt 5–7, 14) | — | — |
| Truyền thông | ⭐ **Đã đối chiếu** (đợt 3, 8, 14) | — | — |
| Chuyển động | ⭐ **Đã đối chiếu** (đợt 9) | — | — |
| Nền tảng PLC | 7 *(8, 9, 18 đợt 4, 10; 11, 19 đợt 15; 14 đợt 22; **12 đợt 27**)* | ⭐ **Bryan ch.5–8** chưa dùng | Vừa |
| Ngôn ngữ | ⭐ **Đã đối chiếu hết** — 15, 16, 17, 20, 21 (đợt 16, 17, 19, 20, 21) | — | — |
| Thiết kế | 22, 29 *(25 đợt 23; 24, 26, 27, 30 đợt 24; 23 đợt 27; **28 đợt 28**)* | Hugh Jack, Bryan ch.11 | Vừa |
| Chẩn đoán & vận hành | 43, 49, 53, 55 *(51, 52 đợt 18 và **đợt 26**)* | ⭐ **Bryan ch. 20** đã dùng; Kuphaldt, IEC 62381 | Vừa |
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
