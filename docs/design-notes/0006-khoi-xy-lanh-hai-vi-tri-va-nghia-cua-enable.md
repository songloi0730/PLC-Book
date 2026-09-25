# 0006 — Khối xy-lanh hai vị trí: một khối duy nhất, và nghĩa của `Enable` với van một cuộn

- **Ngày:** 2026-09-26
- **Trạng thái:** Đã áp dụng (đợt 58) — Ch.27 mục 27.3 + Bẫy 7, Phụ lục L mục L.8, Ch.14, Phụ lục N
- **Cập nhật đợt 59:** chân `Enable` đổi tên **`Permit`** — PLCopen dành chữ `Enable` cho khối theo mức, tắt là xoá ngõ ra, đúng nghĩa ngược với chân này; chân `Reset` nay nối **`M_ClearFaults`** (lệnh xoá của trạng thái `Resetting`) thay vì sườn nút Reset — design note 0007
- **Phạm vi:** khối `FB_Cylinder2Pos` — khối dùng lại quan trọng nhất của máy mẫu DP-01, được Ch.14,
  26, 27, 30, 57 và Phụ lục L dùng tới

---

## Bối cảnh

Bộ kiểm thứ sáu (`tools/kiem_cu_phap_st.py`, đợt 58) báo ngay ở lần chạy đầu: **sách có hai khối
khác nhau cùng mang tên `FB_Cylinder2Pos`**.

| | Ch.27 mục 27.3 (bản dạy) | Phụ lục L mục L.8 (bản để chép) |
|---|---|---|
| Chân vào | `Extend` · `AtExtend` · `AtRetract` · `TimeoutMs` · `Enable` | `Req` · `SensWork` · `SensHome` · `Limit` |
| Chân ra | `Valve` · `Done` · `Fault` · `Unknown` | `SolOut` · `Done` · `Fault` · `FaultCode` |
| Xoá lỗi | ⚠ **Không có cách nào** — chú thích ghi *"cần Reset"* nhưng khối không có chân Reset | Tự xoá khi yêu cầu đổi |
| Cổng cho phép | `Valve := Extend AND Enable AND NOT Fault` | Không có |
| `END_FUNCTION_BLOCK` | ⚠ Thiếu | Có |

Người đọc chép khối ở Phụ lục L, rồi đọc Ch.57 gọi `Stop1.Valve` — **không biên dịch được**. Nhưng soát
kỹ thì hai bản còn giấu những lỗi nặng hơn chuyện đặt tên:

1. ⚠⚠ **Bản Ch.27 làm máy kẹt ở `Alarm`.** `Fault` chốt mà không có đường xoá. Chương 25 chỉ cho
   Reset khi `NOT M_AnyFault` — nếu lỗi xy-lanh góp vào `M_AnyFault`, máy **không bao giờ** ra khỏi
   `Alarm` được nữa, trừ khi tắt nguồn.
2. ⚠⚠ **Bản Ch.27 thả kẹp khi máy báo lỗi.** Chương 25 cắt `M_MotionEnable` khi vào `Alarm`; bản
   Ch.27 AND `Enable` thẳng vào van. Với van 5/2 lò xo về, tắt van **là một lệnh chuyển động**: kẹp
   nhả. Điều này trái ngược trực tiếp **chức năng an toàn SF6** của DP-01 (Phụ lục J): *"mất khí khi
   board đang bị kẹp → GIỮ kẹp"* — khi khí có lại, van đã tắt, kẹp nhả, board rơi.
3. ⚠ **Bản Ch.27 còn AND `NOT Fault` vào van** — một cảm biến hỏng cũng đủ làm cơ cấu chuyển động.
4. ⚠ **Bản L.8 gọi `T_Move` hai lần trong một vòng quét** để đếm lại từ đầu — vi phạm PLCopen CP20,
   đúng lỗi mà chính sách dạy tránh ở Ch.17 Bẫy 5.
5. Thể hiện được đặt tên **ba kiểu**: `Stop1` (Ch.26, 27, 57), `Cyl_Stop1` (Ch.14), `FB_Cyl_Clamp1`
   (Phụ lục L — dùng tiền tố **kiểu** `FB_` cho một **thể hiện**).

⭐ Lỗi 1 và 2 không lộ ra khi đọc từng chương riêng: mỗi chương đúng một mình. Chúng chỉ lộ ra khi
**ghép** Ch.25 với Ch.27 — đúng chỗ người đọc sẽ ghép khi dựng máy thật.

---

## Năm câu hỏi thiết kế

### Q1 — Giữ giao diện nào?

| Phương án | Ưu | Nhược |
|---|---|---|
| Giao diện Ch.27 (`Extend` / `AtExtend`) | Ch.57 đang dùng `Valve` | "Ra/về" gắn với chiều cơ khí; một cái kẹp đi **lên** để kẹp thì `Extend` đọc sai nghĩa |
| Giao diện L.8 (`Req` / `SensWork` / `SensHome`) | ⭐ "Làm việc/gốc" đúng với **mọi** hướng lắp | `SolOut` khó đọc với thợ bảo trì |
| ⭐ **Trộn có chủ ý** | `Req` · `SensWork` · `SensHome` (tổng quát) + `Valve` (dễ đọc, Ch.57 giữ nguyên) + `Enable` · `Reset` · `Unknown` · `FaultCode` | 11 chân — nhỉnh hơn gợi ý ~10 của PLCopen CP23 |

### Q2 — `Enable` = FALSE nghĩa là gì?

| Phương án | Ưu | Nhược |
|---|---|---|
| A — `Valve := Req AND Enable` | Ngắn | ⚠⚠ Mất phép **gây ra** chuyển động (lò xo); trái SF6 |
| ⭐ B — `IF Enable THEN Valve := Req; END_IF;` | Mất phép = **không có chuyển động mới**, vị trí được giữ — đúng nghĩa "dừng" của `Hold`/`Alarm` | Khối có nhớ; `Done` phải so với **yêu cầu** |
| C — Không có cổng | Khối đơn giản nhất | Liên động rải khắp tầng trạm |

### Q3 — Xoá lỗi thế nào?

| Phương án | Ưu | Nhược |
|---|---|---|
| Không xoá (bản Ch.27 cũ) | — | ⚠⚠ Kẹt `Alarm` (lỗi 1) |
| Tự xoá khi yêu cầu đổi (bản L.8 cũ) | Không cần thêm chân | ⚠ Lỗi biến mất **không cần ai xác nhận** — chỉ cần trình tự đổi yêu cầu |
| ⭐ Chân `Reset`, xoá **trước** các phép kiểm | Reset chỉ có tác dụng khi nguyên nhân **đã hết**: còn nguyên nhân thì lỗi chốt lại ngay trong cùng vòng quét — tầng máy đọc sau không thấy một vòng "hết lỗi" giả | Thêm một chân |

### Q4 — Lỗi có tác động lên van không?

⭐ **Không.** Khối **báo** (`Fault`, `FaultCode`); tầng máy **quyết định** phản ứng (Ch.28). Muốn đưa
cơ cấu về một vị trí xác định khi có sự cố thì đó là một quyết định phục hồi hoặc một chức năng an
toàn, phải viết ra có chủ ý — không để xảy ra như tác dụng phụ.

### Q5 — Bản chuẩn đặt ở đâu?

| Phương án | Ưu | Nhược |
|---|---|---|
| Chỉ ở Ch.27, Phụ lục L trỏ sang | Không trùng lặp | Phụ lục L mất tính "chép dùng ngay" |
| ⭐ **Giống hệt ở cả hai nơi, có máy kiểm** | Ch.27 dạy, L.8 để chép | Hai bản có thể trôi — ⭐ nên bộ kiểm thứ sáu **so cả giao diện lẫn thân** mọi khối cùng tên |

---

## Kiểm chứng trước khi đưa vào sách

Mô phỏng từng vòng quét (bước 10 ms, xy-lanh hành trình 300 ms, `Limit` 3 s), tám kịch bản:

| # | Kịch bản | Kết quả |
|---|---|---|
| 1 | Chạy thường: ra lệnh → chưa `Done` → tới đích → `Done`, không lỗi | ✔ |
| 2 | Mất cho phép **giữa** hành trình | ✔ van giữ, xy-lanh tới đích, `Done` đúng |
| 3 | Đổi yêu cầu khi **không** có phép | ✔ van không đổi, `Done` = FALSE, không báo quá giờ |
| 4 | Kẹt → lỗi 1; Reset khi **còn** kẹt | ✔ lỗi chốt lại ngay; hết kẹt + Reset → hết lỗi |
| 5 | Hai cảm biến cùng báo; Reset khi còn hỏng | ✔ vẫn lỗi; sửa xong + Reset → hết |
| 6 | Đổi lệnh van → đếm lại từ đầu | ✔ hai hành trình 2,5 s liên tiếp không lỗi; `T_Move` gọi đúng 1 lần/vòng |
| 7 | SF6: `Alarm` khi đang kẹp, khí mất rồi có lại | ✔ **vẫn kẹp** |
| 8 | Đối chứng: bản Ch.27 cũ, cùng kịch bản 7 | ✔ tái hiện được lỗi — kẹp **nhả** khi khí có lại |

---

## Hệ quả

- Ch.27 mục 27.3: khối mới + bảng **bốn quyết định không hiển nhiên**; lời gọi mới; ⭐ **Bẫy 7** — cổng
  cho phép viết bằng AND vào van, kèm bảng so sánh ba cách; bảng chốt thêm dòng 13 (và sửa thứ tự
  dòng 10); tự kiểm thêm câu 12.
- Phụ lục L mục L.8: đúng cùng khối; hộp ladder vẽ lại với sáu chân vào; thể hiện tên `Clamp1`.
- Ch.14: thể hiện đổi `Cyl_Stop1` → `Stop1` cho khớp Ch.26, 27, 57.
- Phụ lục N: CP20 thành ⭐ (sách từng sai); CP23 ghi 11 chân; N10 thêm *"tiền tố kiểu không dùng cho
  thể hiện"*.
- ⚠ **Việc còn lại cho đợt 59:** `M_AnyFault` ở tầng máy phải được **tính lại mỗi vòng** từ các nguồn
  lỗi (như Phụ lục L mục L.11), không chốt riêng ở nhiều chỗ — nếu chốt riêng thì chính nó phải được
  Reset xoá, nếu không lỗi 1 quay lại dưới dạng khác. Và khối này là ví dụ **điều khiển theo mức**
  (`Enable`-style); đợt 59 thêm ví dụ **điều khiển theo sườn** (`Execute`/`Done`) để hoàn chỉnh mô hình
  PLCopen.
