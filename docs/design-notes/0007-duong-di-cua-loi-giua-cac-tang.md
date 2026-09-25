# 0007 — Đường đi của lỗi giữa các tầng: chốt ở nguồn, gom một chỗ, xoá qua `Resetting`

- **Ngày:** 2026-09-26
- **Trạng thái:** Đã áp dụng (đợt 59)
- **Phạm vi:** cách một lỗi đi từ chỗ phát hiện (cơ cấu, trạm, truyền thông…) lên tầng máy, và cách nó
  được xoá. Chạm Ch.16, 17, 25, 26, 27, 28, 31, 38, 40, 41, 42, 43, 46, 57 và Phụ lục L (L.6, L.9, L.11)

---

## Bối cảnh

Khi thống nhất khối `FB_Cylinder2Pos` (design note 0006), câu hỏi *"chân `Reset` của khối nối vào
đâu?"* dẫn tới một phát hiện lớn hơn: **sách dạy ba cách khác nhau để đi từ "có lỗi" tới "Reset được"**,
và ba cách đó không ghép được với nhau.

| Kiểu | Ở đâu | Cách làm |
|---|---|---|
| A — một cờ chung, SET/RESET | Ch.16 | Mọi nguyên nhân SET `M_AnyFault`; nút Reset RESET nó khi *các nguyên nhân liệt kê* đã hết |
| B — mỗi nơi ghi thẳng cờ chung | Ch.17, 26, 28, 31, 38, 40, 41, 42, 43, 46; L.6, L.9 | `M_AnyFault := TRUE;` rải ở 16 chỗ |
| C — mỗi nguồn một cờ, gom lại | Phụ lục L mục L.11 | `M_AnyFault := M_AnyAlarmActive OR Stn1_Fault OR Stn2_Fault;` |

Và tầng máy ở Ch.25 chỉ cho sang `Resetting` khi `R_TRIG_Reset.Q AND NOT M_AnyFault`, trong khi việc
xoá cờ lại nằm **trong** `Resetting` (`M_ClearFaults`).

**Hai lỗi thật khi ghép lại:**

1. ⚠⚠ **Khoá chết.** `Stn1_Fault` (quá giờ bước trạm, Ch.26) được chốt nhưng **không có dòng nào
   xoá nó**. Nó góp vào `M_AnyFault` (L.11) → `Alarm` không bao giờ sang `Resetting` → máy chỉ ra khỏi
   `Alarm` bằng cách tắt nguồn. Còn tệ hơn: thân trạm bị cửa vào chặn khi không chạy (L.6), nên bộ định
   thời của bước **không được gọi** và giữ nguyên `Q = TRUE` — kể cả khi viết thêm dòng xoá theo kiểu
   *"xoá khi nguyên nhân hết"* thì nguyên nhân vẫn trông như còn.
2. ⚠ **Phụ thuộc thứ tự gọi.** Với lỗi mất khí, việc nhấn Reset **một lần** có thành công hay không tuỳ
   vào chương trình xoá cờ chạy trước hay sau tầng máy trong vòng quét. Chạy sau thì phải nhấn hai lần.
3. ⚠ Kiểu B ghép với kiểu C là **hai nơi ghi cùng một biến**: phép gán ở L.11 ghi đè mọi
   `M_AnyFault := TRUE` chạy trước nó — lỗi có thể **biến mất** tuỳ thứ tự gọi.

### Kiểm chứng bằng mô phỏng

Mô phỏng từng vòng quét ba khối — nguồn lỗi, gom, tầng máy — ở **cả sáu thứ tự gọi** có thể:

| Kịch bản | Bản cũ | Bản chọn |
|---|---|---|
| Kẹt → hết kẹt → nhấn Reset một lần | ⚠⚠ Kẹt ở `Alarm` ở **cả 6** thứ tự | ✔ `Idle` ở cả 6 |
| Mất khí → khí có lại → nhấn Reset một lần | ⚠ `Idle` hoặc `Alarm` **tuỳ thứ tự** | ✔ `Idle` ở cả 6 |
| Mất khí → nhấn Reset khi chưa có khí | ✔ `Alarm` | ✔ `Alarm` ở cả 6 |

---

## Các phương án

| Phương án | Ưu | Nhược |
|---|---|---|
| A — một cờ chung SET/RESET | Ngắn nhất | Mất thông tin *lỗi gì*; điều kiện RESET phải liệt kê lại mọi nguyên nhân — thêm nguồn mới phải sửa **hai** chỗ, và quên chỗ thứ hai thì Reset xoá một lỗi còn nguyên nhân |
| B — mọi nguồn ghi thẳng cờ chung | Mỗi đoạn trích tự đứng được | ⚠ Nhiều nơi ghi một biến; không có đường xoá chung; chính là thứ gây khoá chết |
| ⭐ **C — chốt ở nguồn, gom một chỗ, xoá qua `Resetting`** | Mỗi cờ **một nơi ghi**; biết lỗi gì; thêm nguồn = thêm một cờ + một vế OR; ⭐ **không phụ thuộc thứ tự gọi** | Thêm một trạng thái có thời lượng (`Resetting` kéo dài vài trăm ms) và một biến lệnh xoá |

## Phương án chọn: C

Ba quy tắc:

1. **Mỗi nguồn lỗi tự chốt cờ của chính nó** — `M_Alm_…` cho nguồn chung, `Stn1_Fault` cho trạm,
   `.Fault` cho khối cơ cấu. Không ai khác ghi vào cờ đó.
2. **`M_AnyFault` được GÁN ĐÚNG MỘT CHỖ** — phép OR của mọi cờ chốt, tính lại mỗi vòng, đặt **sau**
   tầng cơ cấu và **trước** tầng máy. Không nguồn nào ghi thẳng `M_AnyFault`.
3. **Xoá đi qua `Resetting`.** `Alarm → Resetting` chỉ cần **sườn lên** nút Reset. `Resetting` bật
   `M_ClearFaults` đủ lâu cho mọi chương trình chạy qua ít nhất một lần; mỗi chủ cờ **xoá cờ của mình
   khi thấy lệnh xoá**, rồi **phát hiện lại** — nguyên nhân còn thì cờ chốt lại ngay. Hết thời lượng:
   `M_AnyFault` sạch → `Homing`; còn → quay lại `Alarm` (còi không kêu lại — người vận hành đã biết).

⭐ **Vì sao quy tắc 3 không phụ thuộc thứ tự gọi:** `M_ClearFaults` kéo dài nhiều vòng quét, nên chủ
cờ đứng trước hay sau tầng máy đều thấy nó; và tầng máy chỉ đọc kết quả **sau khi** lệnh xoá đã tắt.
Quyết định *"nguyên nhân đã hết chưa"* được giao cho **đúng nơi biết nguyên nhân** — chủ cờ — thay vì
tầng máy phải liệt kê lại.

⭐ Đây cũng là cách khối `FB_Cylinder2Pos` đã làm từ đợt 58 (*"xoá trước, phát hiện sau"*); chân
`Reset` của khối nay nối vào `M_ClearFaults` thay vì sườn nút Reset.

### Hai quyết định đi kèm

| Quyết định | Lý do |
|---|---|
| Chân cho phép của `FB_Cylinder2Pos` đổi tên `Enable` → **`Permit`** | PLCopen dành chữ `Enable` cho khối **điều khiển theo mức**: `Enable` = FALSE thì khối **ngừng và xoá ngõ ra** (hai nguồn tài liệu hãng mô tả quy tắc chung PLCopen, đối chiếu ở đợt 59). Người quen quy ước đó sẽ hiểu `Enable` = FALSE là *"tắt van"* — đúng cái lỗi Bẫy 7 của Ch.27 cảnh báo |
| Trình tự trục ở L.9: cờ lỗi **chính là** bước 90 | `M_Alm_AxisZ := (AxZ_Step = 90);` — không cần cờ riêng; `MC_Reset` kích bằng sườn lên của `M_ClearFaults` |

---

## Hệ quả

- Ch.25: mục mới **25.5c** (ba quy tắc + so sánh A/B/C + vì sao khoá chết); mã `Alarm`/`Resetting` viết
  lại; bảng chuyển trạng thái thêm dòng `Resetting → Alarm`; nấc giám sát bit trạng thái SET cờ riêng.
- Ch.16: ví dụ SET/RESET dùng **một** cờ một nguồn (`M_Alm_AirLow`), kèm chỉ dẫn sang 25.5c.
- Ch.17, 26, 28, 31, 38, 40, 41, 42, 43, 46, L.6, L.9: `M_AnyFault := TRUE` → cờ chốt của chính nguồn.
- Ch.26, L.6: trạm xoá `Stn1_Fault` khi thấy `M_ClearFaults` — đặt **ngoài** cửa vào.
- L.11: xoá bằng `M_ClearFaults`; phép gom khớp 25.5c.
- Ch.27: thứ tự gọi thêm bước **gom lỗi** giữa tầng cơ cấu và tầng máy; `Permit`, `Reset := M_ClearFaults`.
- Ch.57: `Prg_Alarm` (gom lỗi) chuyển lên **trước** `Prg_Machine`.
- ⚠ `M_FaultCode` vẫn là một biến nhiều nơi ghi (mã lỗi gần nhất) — chấp nhận vì chỉ để hiển thị; mã
  của lỗi **đầu tiên** đã có `FirstAlarmCode` ở L.11.
