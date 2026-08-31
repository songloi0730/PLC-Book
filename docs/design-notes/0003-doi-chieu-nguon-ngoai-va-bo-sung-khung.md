# 0003 — Đối chiếu khung sách với nguồn ngoài & các bổ sung

- **Ngày:** 2026-08-30
- **Trạng thái:** Đã áp dụng vào `docs/00_Muc_luc.md`
- **Phạm vi:** kiểm chứng khung 58 chương bằng nguồn độc lập; ghi lại cái gì thiếu và đã thêm gì

---

## Bối cảnh

Khung 58 chương (ADR 0002) được dựng từ **phân tích khoảng trống** trong thảo luận cộng đồng. Đó là
nguồn tốt để biết *người học vướng ở đâu*, nhưng không phải nguồn tốt để biết *một cuốn sách PLC đầy
đủ thì gồm những gì*. Session này đối chiếu khung với ba nguồn độc lập:

1. **Bốn giáo trình thương mại** chủ dự án vừa mua (Hanssen, Petruzella ×2 + Activities Manual, Rabiee).
2. **Một trang chuyên đề PLC** (43 bài, có bài dài tới ~14.800 từ) — đọc bài về sách, bài 50 bài tập,
   bài chẩn đoán sự cố, bài giao thức truyền thông.
3. **Đặc tả chuẩn mở** tải được (Modbus, IO-Link, PLCopen Motion) — kiểm tra xem chương liên quan có
   dựa được vào nguồn cấp một không.

---

## §1 — Điều khung sách làm đúng (được xác nhận độc lập)

| Luận điểm của dự án | Bằng chứng độc lập |
|---|---|
| ⭐ **Phương pháp thiết kế xứng đáng một phần riêng** (Phần IV) | Giáo trình Hanssen chia 5 phần, trong đó **"Methodic" là một phần ngang hàng** với Hardware và Programming. Giáo trình Hugh Jack dành 4 chương liền cho Boolean → logic có cấu trúc → lưu đồ → trạng thái. Đây là hai nguồn hoàn toàn độc lập cùng chỉ về một chỗ |
| ⭐ **Chẩn đoán sự cố là chương phải có, không phải mục phụ** | Bài chuyên đề dài nhất trên trang tham khảo (~14.800 từ) chính là bài chẩn đoán. Petruzella cũng dành nguyên Ch.13 cho "lắp đặt, sửa & chẩn đoán" |
| **Máy trạng thái là ranh giới năng lực** | Nguồn ngoài mô tả đúng hiện tượng đã nêu ở Ch.25: người học **chững lại** ở mức tuần tự, và cách sai là "chồng thêm mạch tự giữ cho tới khi không còn chạy nổi" |
| **Bài tập phải phân mức và ghi rõ khái niệm được rèn** | Bộ 50 bài tập tham khảo chia đúng 5 mức trùng với cấu trúc Phụ lục I đã dự kiến |
| **Viết bảng I/O trước khi lập trình** | Nguồn ngoài nêu đây là "thói quen phân biệt người có kế hoạch với người mò mẫm" — trùng luận điểm Ch.23 |

Kết luận: **không phải sửa cấu trúc.** Khung 8 phần / 58 chương giữ nguyên.

---

## §2 — Điều khung sách thiếu (đã bổ sung)

| Chương | Thiếu gì | Vì sao quan trọng |
|---|---|---|
| **Ch.51** — chẩn đoán | ⭐ **Nguyên tắc "bắt đầu từ ngõ ra bị lỗi và truy ngược"** | Khung cũ chỉ có "chia đôi bài toán". Nguyên tắc truy ngược cụ thể hơn và **áp được ngay từ phút đầu tại máy**: triệu chứng → ngõ ra lẽ ra phải tác động → rung ra lệnh → so trạng thái trong PLC với module vật lý |
| **Ch.51** | **6 nhóm lỗi + bảng tra 2 phút** | Người đứng cạnh máy hỏng cần định hướng trước khi cần quy trình. Khung cũ nhảy thẳng vào quy trình |
| **Ch.51** | **Bộ công cụ đo tối thiểu** (8 loại) và khi nào cần cái nào | Khung cũ chỉ nhắc đồng hồ vạn năng và ampe kìm. Thiếu: máy hiện sóng, kiểm tra cáp mạng, phân tích giao thức, súng đo nhiệt, mô phỏng vòng 4–20 mA, megôm kế |
| **Ch.51** | ⭐ **4 nguyên nhân vật lý của lỗi chập chờn** | Khung cũ có mục "lỗi chập chờn" nhưng bỏ trống nguyên nhân. Bốn cái hay bị bỏ sót: vòng lặp đất, nhiễu từ biến tần/servo/máy hàn, **chu kỳ nóng-nguội làm mỏi đầu nối**, **tụ nguồn lão hoá**. Hai cái sau gần như không tài liệu nhập môn nào nhắc |
| **Ch.51** | **Sửa hay thay**, thiết bị hết vòng đời, bảo trì phòng ngừa | Câu hỏi thực tế mà người mới không có khung để trả lời |
| **Ch.40** — Ethernet CN | **Bus trường thế hệ trước** (PROFIBUS, DeviceNet, ControlNet, AS-i) | Khung cũ chỉ có PROFIBUS. Máy cũ vẫn đầy DeviceNet và AS-i — người đọc phải nhận diện được |
| **Ch.40** | **Đồng bộ thời gian (PTP)**, QoS, dự phòng mạng, **phiếu quyết định chọn giao thức** | Phiếu quyết định là cách trình bày tốt hơn bảng so sánh: dẫn người đọc tới **một** câu trả lời thay vì bày ra 20 lựa chọn |
| **Ch.45** — MES & an ninh OT | ⭐ **Mô hình Purdue** | Khung cũ có "phân vùng mạng & DMZ" nhưng thiếu tên gọi chung của mô hình. Đây là **ngôn ngữ chung** khi bàn phân vùng OT với người khác — thiếu nó thì người đọc không tham gia được vào cuộc trao đổi |
| **Phụ lục I** | Cấu trúc **5 mức ~50 bài**, mỗi bài ghi rõ khái niệm được rèn | Khung cũ chỉ nói "~20 bài có lời giải + ~12 bài tự làm" mà không có kiến trúc. Nay có danh sách đề bài cụ thể theo mức |

---

## §3 — Ranh giới dùng nguồn ngoài

Ba loại nguồn, ba mức được phép khác nhau:

| Loại nguồn | Được làm gì | Không được làm gì |
|---|---|---|
| **Đặc tả chuẩn mở** (Modbus, IO-Link, PLCopen) và tài liệu giấy phép tự do (Kuphaldt, Hugh Jack, IFA) | Trích số liệu, công thức, định nghĩa — **ghi nguồn** theo mẫu `00c_Tai_lieu_tham_khao.md` | Chép nguyên bảng/hình vào sách |
| **Tài liệu hãng** công khai | Trích ở mức nguyên lý và số liệu tra cứu, ghi số hiệu tài liệu | Chép nguyên trang; trình bày cách làm của một hãng như chân lý chung (bất biến B2) |
| ⭐ **Sách thương mại** và **bài viết trên trang chuyên đề** | Đọc để **kiểm tra khung có bỏ sót gì** và học **cách giải thích** một khái niệm khó | Chép câu chữ; tái tạo bảng/hình; bê nguyên đề bài tập; dùng ví dụ của họ thay cho DP-01 |

> Cụ thể với Phụ lục I: danh sách đề bài ở §2 là **các bài toán kinh điển của ngành** (đèn giao thông,
> thang máy, trạm trộn, sao-tam giác) — không ai sở hữu chúng. Nhưng **cách ra đề, số liệu, và lời
> giải phải tự viết**, và phải dùng tên tag theo quy ước của sách, không phải của nguồn tham khảo.

---

## §4 — Việc phát sinh

| Việc | Trạng thái |
|---|---|
| Áp 8 bổ sung ở §2 vào `00_Muc_luc.md` | ✅ xong |
| Ghi 4 sách thương mại + ranh giới sử dụng vào `../PLC/reference/00_INDEX.md` | ✅ xong |
| Tải PLC Handbook (eBook miễn phí của một hãng, 85 tr) | ✅ xong |
| Quét mục lục sách Rabiee (không có bookmark) khi bắt đầu viết Phần I–II | ⬜ để sau, không chặn |
| Cân nhắc bổ sung mục **VFD điều khiển qua mạng** vào Ch.36 — nguồn ngoài có bài riêng về chủ đề này | ⬜ đang cân nhắc, Ch.36 đã có ý này ở mức khái quát |
| Đối chiếu Phụ lục A với mục lục Petruzella Ch.15 (ControlLogix) khi viết Phụ lục A2 | ⬜ để sau |
