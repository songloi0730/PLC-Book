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

## Chương CHƯA được đối chiếu

⚠ **Đây là phần quan trọng nhất của nhật ký.** Chương không có trong bảng trên nghĩa là **chưa ai
kiểm**, không phải "không có lỗi".

| Nhóm | Chương | Nguồn sẵn có | Ưu tiên |
|---|---|---|---|
| ⚠⚠ **An toàn** | **Phụ lục D** *(3, 6, 47, 48 đã đối chiếu đợt 1, 3, 4)* | SICK ×3, Schneider, DGUV/IFA, PPSA | ⭐⭐ **Cao nhất** |
| Đo lường & analog | 31, 33, 34, 35 | Kuphaldt *Lessons in Industrial Instrumentation* | ⭐ Cao |
| Truyền thông | 38, 40, 42 *(39 đã đối chiếu đợt 3)* | ⭐ **Đặc tả Modbus gốc**, IO-Link, EtherCAT/TSN | ⭐ Cao |
| Chuyển động | 37 | PLCopen Motion, Mitsubishi Positioning | ⭐ Cao |
| Nền tảng PLC | 7, 8, 9, 11, 12, 14, 18, 19 | Hugh Jack, AutomationDirect, Siemens/Rockwell | Vừa |
| Ngôn ngữ | 15–17, 20, 21 | Hugh Jack, Rockwell PM006/007/008/009 | Vừa |
| Thiết kế | 22–30 | ⭐ Hugh Jack (mạnh nhất mảng này) | Vừa |
| Chẩn đoán & vận hành | 43, 49, 51, 52, 53, 55 | Kuphaldt (ch. chẩn đoán), IEC 62381 | Vừa |
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
