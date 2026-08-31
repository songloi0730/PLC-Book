# 0001 — Cấu trúc sách PLC: các phương án đã cân nhắc và lý do chọn

- **Ngày:** 2026-08-28
- **Trạng thái:** Đề xuất (chờ chủ dự án chốt)
- **Phạm vi:** khung tổng thể của sách — không phải nội dung từng chương

---

## Bối cảnh

Yêu cầu: dựng dàn ý chi tiết cho một sách hướng dẫn PLC, lấy đầu vào từ bài sticky
"READ FIRST: How to learn PLCs and get into the Industrial Automation World" của cộng đồng r/PLC
(bản lưu 2025-03-28), gồm toàn văn bài viết + 96 bình luận, cùng các tài liệu mở được nhắc tới.

### Cái gì đọc được từ nguồn — và vì sao nó định hình cấu trúc

Bài sticky bản thân nó chỉ là **danh mục tài nguyên** (phần mềm miễn phí, khoá học, kênh YouTube,
diễn đàn, sách). Giá trị thật để thiết kế sách nằm ở **phần bình luận** — nơi lộ ra những khoảng
trống mà danh mục kia không lấp được:

| Quan sát từ nguồn | Hệ quả lên cấu trúc sách |
|---|---|
| Rất nhiều người hỏi vào nghề từ nền tảng **không phải điện** (cơ khí, IT, kinh doanh, HVAC) | Phần I "Trước khi chạm vào PLC" + 3 lộ trình đọc A/B/C ở Ch.1 |
| Nhiều ý kiến nhấn mạnh: không có nền điện thì **sai lầm sẽ tốn kém**, không chỉ khó học | Ch.3–5 là bắt buộc với lộ trình A, không phải phụ lục |
| Có yêu cầu rõ ràng: *"thêm phần kỹ thuật — ví dụ chẩn đoán PLC bằng tay ngoài hiện trường"* | Ch.39 (xử lý sự cố) được nâng thành chương trọng tâm ⭐⭐, kèm bảng ~30 triệu chứng |
| Có câu hỏi lặp lại: *"tự học xong thì **chứng minh** với nhà tuyển dụng bằng cách nào?"* | Ch.43 có mục xây hồ sơ năng lực; Ch.42 case study đầy đủ chính là sản phẩm để trưng ra |
| Một luồng riêng khẳng định **truyền thông là thứ đáng sợ nhất**, và luồng đó phân họ giao thức theo cơ chế (TCP thường / hỏi-đáp đồng bộ / dồn khung) | Ch.33 tổ chức theo **3 họ cơ chế** thay vì liệt kê 20 cái tên ngang hàng |
| Có góp ý: danh mục **thiếu hẳn tài nguyên an toàn máy** (ISO 13849) | Ch.36–37 + Phụ lục D; gắn cờ ⚠⚠ cần chuyên gia duyệt |
| Ý kiến trái chiều đáng chú ý: *"cứ mua con PLC rẻ nhất mà lập trình, đọc nhiều tài liệu chỉ làm chậm"* | Ch.10 có mục dựng bàn thực hành; sách không được biến thành lý thuyết suông |
| Một tài liệu mở uy tín có hẳn mục *"How to teach yourself PLC programming"*: tự dựng PLC trainer, viết chương trình "Hello World" cho **từng lệnh** và comment kỹ để sau này tra lại | Ch.10 (bàn thực hành) và Ch.25 (comment như nhật ký kỹ thuật) lấy trực tiếp tư duy này |
| Một giáo trình mở khác mạnh bất thường ở **phương pháp thiết kế** (Boolean → logic có cấu trúc → lưu đồ → máy trạng thái) — thứ mà tutorial online gần như luôn bỏ | Phần IV được tách thành một phần riêng, là điểm khác biệt chính của sách |

---

## Phương án A — Trung lập hãng theo IEC 61131-3, phương ngữ hãng gom vào phụ lục

Dạy khái niệm một lần theo chuẩn (scan, POU, LD/ST/FBD/SFC, tag, FB), rồi Phụ lục A đối chiếu
sang TIA Portal / Studio 5000 / CODESYS.

| Ưu | Nhược |
|---|---|
| Không chết theo phiên bản phần mềm — hãng đổi giao diện thì thân sách vẫn đúng | Người đọc chỉ có đúng 1 hãng phải tự dịch sang phương ngữ của mình |
| Người đọc dùng được ở bất kỳ nhà máy nào, không phụ thuộc hãng nơi họ xin việc | Viết tốn công gấp ~3 ở phần ví dụ đối chiếu |
| Khớp nguyên tắc "học nguyên lý, đừng học quy trình bấm nút" | Cảm giác ban đầu trừu tượng hơn, người mới dễ nản nếu không có ví dụ chạy được |
| Trung lập → không lệ thuộc chính sách license của một hãng | Không thể trình bày đủ sâu chi tiết đặc thù của bất kỳ hãng nào |

## Phương án B — Bám một hệ duy nhất từ đầu tới cuối

Chọn một nền (ví dụ CODESYS vì miễn phí và có mô phỏng, hoặc TIA Portal vì phổ biến ở Việt Nam)
và dạy trọn vẹn trên đó.

| Ưu | Nhược |
|---|---|
| Cụ thể, người đọc làm theo được ngay từ trang đầu | Trùng lặp với tài liệu hãng — mà tài liệu hãng luôn đầy đủ và cập nhật hơn |
| Viết nhanh hơn hẳn, ảnh chụp màn hình nhất quán | Lỗi thời nhanh; đổi phiên bản là phải chụp lại toàn bộ |
| Dễ làm bài tập có lời giải chạy được | Thu hẹp độc giả; người dùng hãng khác gần như không dùng được |
| | Rơi đúng vào "bệnh sách bấm nút" đã nêu ở đầu mục lục |

## Phương án C — Dẫn dắt bằng dự án ("dựng 6 cái máy")

Mỗi chương là một máy khó dần; lý thuyết được nhả ra khi bài toán cần đến.

| Ưu | Nhược |
|---|---|
| Động lực học cao nhất; sản phẩm cuối là portfolio thật | Lý thuyết bị rải rác — sau này không tra cứu được |
| Trả lời trực tiếp nhu cầu "có gì để trưng ra khi phỏng vấn" | Khó viết cho người **không** có phần cứng |
| Gần cách người ta thật sự học nghề | Người đọc khó tìm lại "cách dùng timer" khi cần tra nhanh |

---

## Phương án chọn: **A làm bộ khung + C làm phương tiện chuyển tải**

Cụ thể:

1. **Thân sách trung lập hãng** (A) — khái niệm dạy một lần theo IEC 61131-3; mọi thứ phụ thuộc
   hãng bị đẩy hết vào Phụ lục A.
2. **Một máy mẫu duy nhất xuyên suốt** (C ở mức kiểm soát được) — PS-01, xuất hiện từ Ch.6 và được
   xây dần qua từng phần, ráp hoàn chỉnh ở Ch.42. Người đọc vẫn có sản phẩm cuối để trưng ra,
   nhưng lý thuyết vẫn nằm đúng chương của nó nên tra cứu được.
3. **Ba đường tra cứu** (Ch.1): học tuần tự / tra theo việc đang làm / tra theo triệu chứng hỏng
   (Phụ lục E). Cùng một cuốn sách phục vụ được cả người học lẫn người đang đứng cạnh máy hỏng.

### Vì sao không chọn B

Không phải vì B kém — B **viết nhanh hơn và cụ thể hơn**. Lý do từ chối: sản phẩm của B cạnh tranh
trực tiếp với tài liệu chính hãng (miễn phí, đầy đủ hơn, cập nhật hơn), nên phần giá trị gia tăng
còn lại rất mỏng. Trong khi đó phần mà tài liệu hãng **không bao giờ** viết — thiết kế trạng thái,
phục hồi sau lỗi, chẩn đoán hiện trường, chọn giữa các hãng — lại chính là phần A + C làm được.

> Nếu chủ dự án muốn đổi sang B, điểm sửa là: bỏ Phụ lục A, đưa phương ngữ hãng vào thẳng thân sách,
> và bỏ cờ "trung lập hãng" ở phần Ghi chú phạm vi. Phần IV và Phần VII giữ nguyên giá trị.

---

## Hệ quả của lựa chọn này

- **Phải giữ kỷ luật trung lập.** Mọi lần muốn viết "ở TIA Portal bạn bấm…" trong thân sách là một
  lần vi phạm. Nội dung đó thuộc Phụ lục A.
- **Phụ lục A trở thành phụ lục nặng nhất** và phải viết sau khi thân sách ổn định, nếu không sẽ
  phải sửa 3 lần mỗi khi thân sách đổi.
- **Máy mẫu PS-01 phải chốt sớm** (bảng I/O, đặc tả trình tự) vì Ch.6 trở đi đều tham chiếu. Đổi
  máy mẫu giữa chừng = viết lại ví dụ của hàng chục chương.
- **Ch.39 và Ch.36–37 là điểm bán hàng của sách** — nếu viết hời hợt thì sách rơi lại thành một
  tutorial nữa. Ưu tiên viết sớm, không để cuối.
- Thông tin về license phần mềm miễn phí (Phụ lục G) **sẽ lỗi thời**; phải ghi rõ ngày kiểm tra và
  cảnh báo người đọc tự xác nhận lại.

---

## Điểm còn treo — ✅ ĐÃ ĐƯỢC GIẢI QUYẾT

> **Mục này đã bị thay thế bởi `0002-chot-huong-va-mo-rong-khung.md` (2026-08-29).**
> Giữ lại nguyên văn câu hỏi để đọc được mạch quyết định; **đáp án và lý do ở ADR 0002.**

| # | Câu hỏi | Ảnh hưởng | Kết quả |
|---|---|---|---|
| 1 | Chốt phương án A+C hay đổi sang B? | Toàn bộ Phụ lục A và giọng văn thân sách | ✅ **Giữ A+C** |
| 2 | Máy mẫu PS-01 (khoan & phân loại) có phù hợp không, hay muốn máy khác gần lĩnh vực đang làm hơn? | Ch.6→42 | ❌ **Đổi sang DP-01** (điện tử) — ADR 0002 §2 |
| 3 | Bộ ba hãng cho Phụ lục A: Siemens / Rockwell / CODESYS — có đổi Rockwell thành Mitsubishi hoặc Inovance cho sát thị trường Việt Nam không? | Chỉ Phụ lục A | ✅ **Thành 5 hệ**, Rockwell xuống cuối — ADR 0002 §3 |
| 4 | 43 chương có quá dài không — có muốn gộp để còn ~38 chương? | Khung mục lục | ❌ **Ngược lại: mở lên 58 chương** — ADR 0002 §1, §4 |
| 5 | Ngôn ngữ phát hành: chỉ tiếng Việt, hay song ngữ thuật ngữ? | Quy ước viết | ✅ **Song ngữ** → bất biến B11 — ADR 0002 §5 |

> 💡 Điều đáng ghi lại: câu #4 được trả lời **ngược hoàn toàn** với hướng ADR này gợi ý. Giả định ngầm
> ở đây là "sách ngắn dễ hoàn thành hơn"; chủ dự án đặt lại ưu tiên là **người đọc không phải đi tìm
> tài liệu khác**, và chấp nhận khối lượng lớn hơn để đổi lấy điều đó. Quyết định này đổi bản chất
> cuốn sách từ "nhập môn có chiều sâu" thành "sách tra cứu tự đủ cho cả vòng đời một máy".
