# 0008 — Đợt 62: giao diện trạm, ví dụ hoàn chỉnh, SFC — quyết định và phát hiện

**Trạng thái:** ĐANG LÀM — nghiên cứu xong, **chưa sửa chương nào**. Phiên sau bắt đầu từ mục 6.
**Ngày:** 2026-09-27
**Thuộc:** đợt 62 (đợt cuối) của kế hoạch 0005.

---

## 1. Bối cảnh — đo trước

| Chỉ số | Giá trị |
|---|---|
| Chương 14–30 có POU đầy đủ | Chỉ Ch.27 (`FB_Cylinder2Pos`), Ch.29 (`KiemTraCongThuc`), Ch.30 (`FB_BoardTransfer`, `FB_Foo`) |
| Chương không có khối ST nào | Ch.15 (LD), Ch.21 (FBD/SFC), Ch.23 (đặc tả) |
| Biến trạm dạng rời `Stn1_X` | ~200 lần / 16 tệp (`Stn1_Step` 88) · dạng `M_Stn1_X` ~50 lần |
| Biến trạm dạng cấu trúc `Stn1.X` | 14 lần / 4 tệp (Ch.11, 22, 30, 37) |
| ⚠ Định nghĩa `TYPE ST_Station` | **Ba bản khác nhau**: Ch.11 mục 11.5 · Ch.11 mục 11.7 · Ch.30 mục 30.3 |
| ⚠ Tên chương trình trạm 1 | Ch.11 `Prg_Stn1Seq` ≠ Ch.14, Ch.57 `Prg_Stn1Dispense` |

## 2. Quyết định 1 — biến của trạm: rời hay cấu trúc

Mâu thuẫn: Ch.11 gọi khai báo rời là *"cách ngây thơ"*, Ch.30 đánh dấu ✗ — mà ~200 chỗ mã mẫu dùng
đúng cách đó. Nhưng Ch.27 mục 27.4 lại dạy **trạm chỉ công bố một giao diện nhỏ, bước là ruột riêng** —
gói mọi thứ (kể cả `Step`) vào một cấu trúc toàn cục thì phá chính nguyên tắc đó.

| Phương án | Ưu | Nhược |
|---|---|---|
| A. Mọi thứ vào `Stn1 : ST_Station` | Khớp Ch.11, Ch.30 | ⚠ `Step` thành toàn cục — trái Ch.27; cấu trúc ~16 trường |
| B. Giữ rời, sửa lời Ch.11/30 thành "tuỳ" | Ít sửa nhất | ⚠ Sách khuyên một đằng, mã mẫu làm một nẻo; người đọc bắt chước mã |
| ⭐ **C. Tách hai phần** | Khớp cả Ch.11, 27, 30, 30.3b; đổi tên **giữ nguyên độ dài** (`_` → `.`) nên sơ đồ ladder không lệch cột | ~70 chỗ sửa + lời ở 6 chương |

⭐ **Chọn C:**

- **Giao diện công bố** → `Stn1 : ST_Station` (toàn cục, CHỈ trạm 1 ghi). Trường: `Ready`, `Busy`,
  `Fault`, `FaultStep`, `BoardDone`, `DoneCount`, `BoardIsNG`. `AnyFault` của Ch.11/22 đổi thành
  `Fault` (theo 0007). **Một** định nghĩa duy nhất, các bản chép phải giống hệt.
- **Ruột của trạm** → giữ rời `Stn1_Step`, `Stn1_StepPrev`, `Stn1_StepLimit`, `Stn1_BranchA/B`… Ghi rõ
  ở Phụ lục N mục N.5: trong dự án thật đó là biến cục bộ `Step` của `Prg_Stn1Dispense`; sách thêm
  `Stn1_` để đoạn trích đứng một mình vẫn biết của trạm nào.
- **Yêu cầu gửi tầng cơ cấu** `M_Stn1_ClampReq`… giữ nguyên (họ `M_`, Ch.27).
- Sửa kèm: Ch.22, Ch.37 `Stn1.Step` → `Stn1_Step`; Ch.57 bảng quy ước (dòng *"Bit trạng thái"*);
  Ch.30 dòng bảng `Stn2_Ready`; Ch.11 thống nhất `Prg_Stn1Dispense`.

## 3. Quyết định 2 — "ví dụ hoàn chỉnh" nghĩa là gì, kiểm thế nào

| Phương án | Nhược |
|---|---|
| Có `VAR` là hoàn chỉnh (lời Phụ lục N mục N.7 hiện nay) | ⚠ Sai sự thật: nhiều khối có `VAR` vẫn dùng tag không khai báo |
| ⭐ **Dấu hiệu tường minh** — dòng đầu `// ✔ VÍ DỤ HOÀN CHỈNH` | Người đọc thấy ngay; bộ kiểm biết khối nào phải nghiêm |

⭐ Khối có dấu hiệu phải **tự đủ khai báo biến** (kể cả I/O qua `VAR_GLOBAL`/`VAR_EXTERNAL` trong
chính khối); **kiểu** (`FB_…`, `ST_…`, `E_…`, `MC_…`) được phép định nghĩa ở nơi khác trong sách nhưng
phải tồn tại. Với LD/FBD/SFC: khối khai báo `iecst` có dấu hiệu, sơ đồ ở khối kế tiếp — bộ kiểm soát
mọi tên trong sơ đồ đã khai báo. Ch.22, Ch.23 là chương phương pháp → không bắt buộc.

Thêm vào `kiem_cu_phap_st.py`: (1) biến chưa khai báo trong khối có dấu hiệu; (2) `TYPE` cùng tên phải
giống hệt (bản có dấu lược được là tập con); (3) `X.trường` phải là trường có thật của kiểu cấu trúc.

## 4. ⚠⚠ Phát hiện đã kiểm — chưa sửa

| # | Chỗ | Lỗi | Nguồn đối chiếu |
|---|---|---|---|
| 1 | Ch.21 mục 21.3, bảng tóm tắt | `.T` *"về t#0s khi rời bước"* — ⚠ Horner và Rockwell: **giữ nguyên** tới lần vào bước sau (Hanssen nói ngược lại → khác nhau theo hệ). Đoạn `IF Step30_Clamp.T > T#3s THEN …` có thể **khoá chết** báo động (bước từng quá 3 s rồi mới đi) → sửa thành `Step30_Clamp.X AND Step30_Clamp.T > T#3S` | Horner Cscape help "IEC SFC"; Rockwell 1756-PM006L (9/2024) tr.18; Hanssen ch.12 |
| 2 | Ch.21 bảng bổ ngữ | `P` *"chạy đúng một lần, thay R_TRIG"* — ⚠ CODESYS: `P` chạy **đúng hai lần** (vào và rời bước). Một lần khi vào bước là **`P1`** (Rockwell, Fernhill có; bảng của CODESYS không liệt kê) | CODESYS "Qualifiers for Actions in SFC"; Beckhoff TC2 SFC; Fernhill "SFC Step" |
| 3 | Ch.21 bảng bổ ngữ | `N` *"tự tắt khi rời bước"* — chỉ đúng khi hành động là **biến BOOL**. Hành động là đoạn mã thì giá trị đã gán **ở nguyên**; CODESYS còn chạy nó **thêm một lần** sau khi rời bước; Rockwell mặc định *Don't scan*: *mọi dữ liệu giữ giá trị* | CODESYS "SFC Element: Action", "Processing Order"; Rockwell PM006 tr.36 |
| 4 | Ch.21 | `.X`/`.T` *"sửa thì trình biên dịch báo lỗi"* — Fernhill: gán là lỗi; ⚠ CODESYS **cho ghi** để ép bước, kèm cảnh báo mất ổn định | CODESYS "Implicit Variables"; Fernhill |
| 5 | Ch.25 mục 25.5 | Đèn gán `:= TRUE` trong nhánh `CASE`, không bao giờ tắt → Running→Hold **đèn xanh vẫn sáng** — đúng triệu chứng Bẫy 5 của chính Ch.25. `M_CycleEnable`, `M_HomingRun` ở lại TRUE khi vào `Alarm` qua khối lỗi; `M_MotionEnable` tắt mà không chỗ nào bật lại → sửa: mọi cờ/ngõ ra suy từ trạng thái, gán **ngoài `CASE`** (cùng bệnh với hành động `N` của SFC) | Đọc mã, mô phỏng tay |
| 6 | Phụ lục B mục B.9b · L.6 | ⚠ **CHƯA KIỂM XONG**: *"TON không được gọi thì đứng yên"* — nhiều hiện thực tính `ET` theo đồng hồ hệ thống, nên lần gọi lại có thể **nhảy vọt** → khung L.6 (timer bước nằm trong nhánh, cố ý đứng khi Hold) có thể báo lỗi giả ngay khi chạy tiếp. Cần nguồn trước khi viết | Trang TON của CODESYS không nói; cần tìm tiếp |

## 5. Tài liệu SFC có trong kho (không cần tải thêm)

PLCopen Coding Guidelines v1.0: **L7** đóng đúng nhánh song song (Cao) · **L8** không viết hành động
bằng SFC (TB) · **L9** giới hạn ~32 phần tử (TB) · biến chỉ báo của hành động bị bỏ ở bản 3. Tờ
PLCopen SFC: SFC chỉ trong FB/PROGRAM; một phần POU là SFC thì cả POU. Rockwell PM006: *"không nối
vào, ra, hay giữa một nhánh song song"*; cỡ bước; bước đầu để khởi tạo. CODESYS: điều kiện chuyển
**không** chứa phép gán/gọi khối; cờ `SFCInit`/`SFCReset`/`SFCError`. ⭐ Ch.26 mục 26.5: thoát khỏi
vùng song song vì lỗi mà không đưa **mọi** nhánh về 0 → nhánh sót chạy tiếp ở chu trình sau (L7 dạng
`CASE`).

## 6. Việc còn lại — theo thứ tự

1. Mở rộng bộ kiểm (mục 3), thử bằng lỗi cài.
2. Đổi tên theo quyết định 1; thống nhất `ST_Station`, `Prg_Stn1Dispense`.
3. Sửa phát hiện 1–5; kiểm xong phát hiện 6 rồi mới sửa B.9b/L.6.
4. Ch.21 mục mới *"SFC — nên và không nên"*; Ch.26 thêm ghi chú L7.
5. Ví dụ hoàn chỉnh: Ch.14, 15, 16, 17, 18, 19, 20, 21, 24, 25 (chính là 25.5 đã sửa), 26, 28 viết
   mới hoặc nâng khối sẵn có; đánh dấu các POU đã đủ ở Ch.27, 29, 30.
6. Ch.1 mục *"Ví dụ code"*: bỏ lời hứa *"mọi đoạn code đều tự kiểm được"*, thay bằng quy ước đoạn
   trích / ví dụ hoàn chỉnh; Phụ lục N mục N.7 theo quyết định 2.
7. Nhật ký đối chiếu, `PROJECT_STATUS.md`, ghép sách, phát hành.
