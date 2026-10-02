# 0013 — Đợt 67: bảng I/O và quy hoạch địa chỉ rút từ tài liệu nội bộ của người làm nghề

**Trạng thái:** ✅ **XONG 2026-10-03**
**Ngày:** 2026-10-03
**Thuộc:** đợt 67 — chủ dự án đưa một thư mục tài liệu nội bộ của một nhà tích hợp máy (bảng I/O và trang
quy hoạch địa chỉ của các dự án thật) và hỏi *"có thể bổ sung gì cho sách không"*.

---

## 1. Ràng buộc trước khi đọc

| Ràng buộc | Áp dụng thế nào |
|---|---|
| **B1b** — chỉ ẩn danh dự án thật, nhưng ẩn **hết** | Sách không mang tên công ty, tên khách hàng, mã dự án, tên tệp; mọi ví dụ đặt lại vào DP-01 |
| Tài liệu nội bộ có chủ | Chỉ rút **quy tắc** đã tổng quát hoá — không chép bảng, không chép danh mục vật tư, không chép chữ nguyên văn |
| Một tệp bị phần mềm bảo vệ tài liệu mã hoá | **Không mở**, không tìm cách mở — đó là biện pháp bảo vệ của chủ tài liệu. Tệp khoá tạm của bảng tính cũng bỏ qua |
| B2 — không khẳng định suông | Quy tắc thấy ở *một* bộ tài liệu được ghi là **thực hành của nghề**, gắn nhãn [Nghề] ở Phụ lục O; chi tiết về hành vi PLC (`IST` chiếm `S0`–`S19`) phải tra tài liệu hãng — đã tra |

## 2. Thấy gì — và sách đang thiếu gì

| Thấy trong tài liệu | Sách đang có | Thiếu |
|---|---|---|
| Bảng I/O chia theo module có dòng tiêu đề; cặp cảm biến xy-lanh liền nhau; cuộn van kép liền nhau; dự phòng nằm trong nhóm; bắt tay qua rơ-le có số; hộp chia M12 | Ch.23 mục 23.3 — sáu cột của một dòng; C.1 | ⚠ **Quy tắc xếp địa chỉ**; ⚠ C.1 thiếu hai cột mà Ch.23 bắt buộc |
| Trang chia vùng rơ-le bước theo khối 100 | Ch.26 mục 26.2a — rơ-le bước là một loại thiết bị | ⚠ **Quy hoạch vùng nhớ** trên hệ kiểu thiết bị — sách chỉ dạy hệ có tag |
| Bảng báo động theo khối và số thứ tự cơ cấu — *không về gốc*, *không tới đích* tách riêng | Ch.44 mục 44.3 — phép thử, ba mức, chống lụt, nội dung một dòng | ⚠ **Cách đánh số** — và cách tách hai chiều của một xy-lanh |
| Mảng cờ tín hiệu trạm đánh số, nghĩa nằm ở bảng tính | Ch.27 mục 27.4 — giao diện trạm bằng trường có tên | ⚠ Không nói tới dạng hay gặp nhất khi nhận chương trình làm sẵn |
| Bảng động cơ: STO, gốc/giới hạn, phanh hai trục dùng chung một ngõ ra | C.10 — khe cắm, thiết bị mạng | ⚠ Không có bảng **trục và động cơ** |
| Bảng I/O PLC an toàn riêng, hai kênh liền nhau | Ch.47 — chức năng an toàn | Quy ước ghi bảng — đưa vào quy tắc 6 ở Ch.23, không đụng nội dung thiết kế an toàn |
| Bảng các bước của từng trạm | Ch.23 mục 23.4, C.3 | Đã đủ — không thêm |
| Ba cảm biến mỗi trạm chuyền (tới, giảm tốc, đúng vị trí) cho khay nặng | — | Chưa thêm — ngoài phạm vi DP-01 (board nhẹ); để ngỏ |

## 3. Quyết định — đặt mỗi thứ ở đâu

| Nội dung | Phương án | Chọn | Lý do |
|---|---|---|---|
| Quy tắc xếp địa chỉ | Ch.23 · C.1 · thẻ O.2 | ⭐ **Ch.23 mục 23.3**; C.1 và O.2 trỏ về | Giải thích *vì sao* thuộc chương (B4); biểu mẫu và thẻ chỉ giữ cột và danh mục kiểm |
| Quy hoạch vùng nhớ | Ch.11 · Ch.15 mục 15.6 · Phụ lục A1 | ⭐ **Ch.11 mục 11.8b** | Ch.11 là chỗ sách dạy địa chỉ; nằm trong phần lõi của lộ trình D; Ch.15 nói phong cách viết, A1 là tra cứu |
| Đánh số báo động | Ch.44 · Ch.25 mục 25.5c | ⭐ **Ch.44 mục 44.3** | Số báo động phục vụ màn hình và nhật ký; Ch.25 nói đường đi của lỗi, không nói số |
| Mảng cờ trạm | Bẫy mới · ô ⚖ ở Ch.27 mục 27.4 | ⭐ **Ô ⚖** | Không phải lỗi — là cách làm có lý do thật, cần ranh giới (đúng định nghĩa ô ⚖) |
| Trục và động cơ | Biểu mẫu mới · C.10.3 | ⭐ **C.10.3** | Cùng họ với bản đồ khe cắm và thiết bị mạng — một bảng cấu hình phần cứng |

## 4. Không lấy

- Tên công ty, khách hàng, mã dự án, tên tệp.
- Mã sản phẩm cụ thể của dự án — module, đảo van, động cơ, cáp.
- Quy ước đặt tên biến riêng của họ (kể cả cho tín hiệu an toàn) — sách giữ quy ước của mình (Phụ lục N).
- Mọi chi tiết về cách đấu mạch an toàn — chỉ lấy **quy ước ghi bảng** (B3).

## 5. Hệ quả

- ⭐ Sách nay dạy được cả hai họ PLC ở khâu cấp chỗ nhớ: hệ có tag (đặt tên, cấu trúc) và hệ kiểu thiết bị
  (quy hoạch khối).
- `FB_Cylinder2Pos` không phải sửa — thông tin để tách hai chiều đã có; mục 44.3 chỉ cách dùng.
- Lệch C.1 ↔ Ch.23 được sửa luôn (nhật ký #739).
- Chi tiết: nhật ký đối chiếu, đợt 67 (#737–#749).
