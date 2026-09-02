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

## Chương CHƯA được đối chiếu

⚠ **Đây là phần quan trọng nhất của nhật ký.** Chương không có trong bảng trên nghĩa là **chưa ai
kiểm**, không phải "không có lỗi".

| Nhóm | Chương | Nguồn sẵn có | Ưu tiên |
|---|---|---|---|
| ⚠⚠ **An toàn** | 3, 6, 48, Phụ lục D | SICK ×3, Schneider, DGUV/IFA, PPSA | ⭐⭐ **Cao nhất** |
| Đo lường & analog | 31, 33, 34, 35 | Kuphaldt *Lessons in Industrial Instrumentation* | ⭐ Cao |
| Truyền thông | 38, 39, 40, 42 | ⭐ **Đặc tả Modbus gốc**, IO-Link, EtherCAT/TSN | ⭐ Cao |
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

| Mảng | Hệ quả với sách |
|---|---|
| ⚠ **CODESYS** — không có tài liệu | Mọi khẳng định về CODESYS trong Phụ lục A phải tra ngoài (xem mục 6 ở trên) |
| ⚠ **Inovance** — không có tài liệu | ⭐ Sách hiện đã viết thận trọng ("tuỳ dòng") — **giữ nguyên cách đó** cho tới khi có tài liệu |
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
