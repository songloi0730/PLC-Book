# 0015 — Đợt 69: sách có nghiêng về phần cứng không? Đo, rồi bổ sung phần lập trình

**Trạng thái:** ⏳ **ĐANG LÀM** — 2026-10-09
**Ngày:** 2026-10-09
**Thuộc:** đợt 69 — nhận xét của chủ dự án: *"sách chủ yếu về những phần liên quan như mạch phần cứng
nhưng chưa nói chi tiết vào các vấn đề liên quan tới lập trình, hay phần mềm, mã PLC… hãy đánh giá và
bổ sung"*.

---

## 1. Đo trước khi tin hay cãi

Script đo trên 58 chương + 16 phụ lục (đếm dòng chữ, dòng mã trong khối ```` ``` ````, và chấm từng đoạn
văn theo từ khoá phần cứng / phần mềm).

### 1.1 Theo phần

| Phần | Dòng chữ | Dòng mã | Tỉ lệ mã | Đoạn văn nghiêng lập trình | Ví dụ hoàn chỉnh |
|---|---:|---:|---:|---:|---:|
| I — Nền tảng (điện, cảm biến, khí nén, ESD) | 1 754 | 57 | 3 % | 26 % | 0 |
| II — Phần cứng & vòng quét | 1 668 | 184 | 10 % | 48 % | 0 |
| III — Ngôn ngữ IEC 61131-3 | 2 906 | 1 066 | 27 % | 86 % | 8 |
| IV — Thiết kế logic | 2 597 | 1 328 | 34 % | 90 % | 9 |
| V — Analog, đo lường, điều khiển liên tục | 2 147 | 402 | 16 % | 37 % | 1 |
| VI — Giao tiếp & tích hợp | 2 616 | 858 | 25 % | 62 % | 1 |
| VII — An toàn, lắp đặt, kiểm thử, sự cố | 2 276 | 128 | 5 % | 51 % | 0 |
| VIII — Hiệu năng, ráp lại, vào nghề | 973 | 75 | 7 % | 64 % | 0 |
| **Toàn sách** | **16 937** | **4 098** | **19 %** | **61 %** | **19** |

⭐ **Kết luận đo:** nhận xét **đúng một nửa**. Tính theo đoạn văn, 61 % nghiêng về lập trình — nhưng mã
chỉ chiếm **19 %**, và bốn phần I, II, V, VII (gần nửa sách) nghiêng hẳn về phần cứng. Người đọc tìm
*mã* thì thấy mã tập trung ở Phần III–IV rồi thưa dần; Ch.57 *"case study đầy đủ"* chỉ có **36 dòng mã**.

### 1.2 Khoảng trống cụ thể

| # | Khoảng trống | Bằng chứng |
|---|---|---|
| 1 | ⚠⚠ **Không có chương trình hoàn chỉnh của DP-01.** Khung `Main` ở Ch.57 mục 57.6 gọi 14 chương trình con, nhưng **10** chương trình (`Prg_Safety`, `Prg_Mechanisms`, `Prg_AntiCollision`, `Prg_Alarm`, `Prg_Stn2Cure`, `Prg_Handshake`, `Prg_Recipe`, `Prg_Comm`, `Prg_Stats`, `Prg_Hmi`) **chưa từng được viết** ở đâu trong sách. Bài thử tích hợp chỉ ráp máy trạng thái với trạm 1 | Ch.57 mục 57.6; `tools/chay_thu/kich_ban.py` hàm `tich_hop` |
| 2 | ⚠ **Ráp thử đã lộ chỗ vênh:** `Prg_Machine` (Ch.25) ghi thẳng `DO_Lamp*`, trong khi Ch.27 mục 27.3c quy định mọi `DO_` chỉ ghi ở tầng ghi ra; đoạn mã ở Ch.57 lại viết `DO_LampRed := M_AnyFault` — trái với Bẫy 5 của Ch.25 (đèn phải suy từ trạng thái) | Ch.25, Ch.27 mục 27.3c, Ch.57 mục 57.6 |
| 3 | Cấu trúc dữ liệu & thuật toán dùng hằng ngày: mảng cấu trúc + `FOR` có **3 khối**; FIFO / bộ đệm vòng **3**; tìm kiếm, trung bình trượt, nội suy bảng tra **0 khối mã** | Đo chủ đề |
| 4 | **Kiểm thử đơn vị** khối chức năng: **0** lần nhắc. Ch.50 dạy mô phỏng và danh sách ca thử, chưa dạy viết bài kiểm cho một khối | Đo chủ đề |
| 5 | Chia việc nặng qua nhiều vòng quét (ngân sách thời gian quét): **0** | Đo chủ đề |
| 6 | Giao thức chuỗi qua TCP (đầu đọc, robot, máy tính): **0**; ghi dữ liệu ra tệp: chỉ nhắc, **0** khối mã | Đo chủ đề |
| 7 | Mô hình trạng thái chuẩn ngành PackML (ISA-TR88.00.02): **0** | Đo chủ đề |
| 8 | Phụ lục I có 50 bài tập nhưng chỉ có **gợi ý** — cố ý, theo I.0 | Phụ lục I mục I.6 |

## 2. Phương án

| Phương án | Nội dung | Ưu | Nhược |
|---|---|---|---|
| **A** — Viết lại cho cân: cắt bớt phần cứng | Rút gọn Phần I, II, V, VII | Tỉ lệ đẹp hơn | ⚠ Mất thứ người làm máy cần thật (đợt 66: lộ trình D đã cho người chỉ lập trình bỏ qua được các phần đó); không thêm được dòng mã nào |
| ⭐ **B** — Thêm mã ở đúng chỗ thiếu, theo thứ tự giá trị | (1) chương trình hoàn chỉnh DP-01; (2) cấu trúc dữ liệu & thuật toán; (3) kiểm thử đơn vị; (4) ngân sách vòng quét; sau đó (5) giao thức chuỗi qua TCP, (6) PackML, (7) lời giải mẫu chọn lọc | Trả lời đúng nhận xét bằng **mã chạy được**; mỗi khối có kịch bản chạy thử | Khối lượng lớn — phải chia đợt |
| **C** — Tách một tập *"Lập trình PLC"* riêng | Như TODO 12 (design note 0012 mục 3) | Rõ cho người chỉ lập trình | ⚠ Quyết định của chủ dự án; không tự làm |

⭐ **Chọn B**, chia hai đợt:

- **Đợt 69 (này):** (1) **Phụ lục P — chương trình hoàn chỉnh của DP-01**, ráp từ các khối đã dạy cộng phần
  còn thiếu, có bài thử tích hợp hai board qua hai trạm, lỗi kẹt, reset, về gốc, giữ, chạy khô; sửa chỗ
  vênh ở mục 1.2 dòng 2; (2) Ch.20 mục mới *cấu trúc dữ liệu và thuật toán*; (3) Ch.50 mục mới *kiểm thử
  đơn vị*; (4) ngân sách vòng quét.
- **Đợt 70 (đề xuất, chờ chủ dự án chọn):** giao thức chuỗi qua TCP; PackML; quy trình gỡ lỗi trên công
  cụ (Phụ lục A, vì B1); lời giải mẫu đầy đủ cho một bài mỗi mức.

## 3. Quyết định nhỏ

| Câu hỏi | Chọn | Lý do |
|---|---|---|
| Chương trình hoàn chỉnh đặt ở đâu | ⭐ **Phụ lục P** mới, Ch.57 trỏ tới | Phụ lục không chịu ràng buộc lát cắt (B8) nên ráp được cả năm lát; Ch.57 giữ vai *quy trình dự án* |
| Chương trình trục, analog, truyền thông | **Khe có tên + giao diện cờ**, mô phỏng trong bài thử | Mỗi thứ đã có chương riêng; đưa trọn vào sẽ gấp ba độ dài mà không thêm ý mới về kiến trúc. Ghi rõ là khe, không giả vờ đầy đủ |
| Khối đã dạy ở chương | **Chép nguyên văn** — bộ kiểm so từng chữ | Không được có hai phiên bản một khối (B19) |
| Đèn tháp ghi ở đâu | Sửa Ch.25: tầng máy tính `M_Lamp*`, tầng ghi ra chép ra `DO_Lamp*` | Một nơi ghi cho mỗi `DO_` (27.3c); đèn vẫn suy từ trạng thái (Bẫy 5) |

## 4. Hệ quả

- Phụ lục P mới; `tools/gop_sach.sh` thêm `p`; Mục lục, Ch.1, Ch.57 trỏ tới.
- Ch.25, Ch.57 (sửa chỗ vênh); Ch.20, Ch.50 (mục mới); Phụ lục O nếu có con số mới.
- Chi tiết: nhật ký đối chiếu, đợt 69.
