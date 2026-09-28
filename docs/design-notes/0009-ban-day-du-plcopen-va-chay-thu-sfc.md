# 0009 — Đợt 63: bản đầy đủ ba tài liệu PLCopen, và chạy thử SFC

**Trạng thái:** ✅ **XONG 2026-09-28**
**Ngày:** 2026-09-28
**Thuộc:** đợt 63 — sau kế hoạch 0005. Chủ dự án chọn: *"Tải cả 3"* và *"Chạy thử ví dụ SFC Ch.21"*.

---

## 1. Bối cảnh

- Đợt 58 được duyệt tải bốn tài liệu PLCopen; ba trong số đó hoá ra là **tờ giới thiệu** 1–4 trang.
  Ch.21, Ch.30 dẫn các tờ đó, và Ch.30 ghi thẳng *"bản đầy đủ chưa có trong bộ tài liệu"*.
- Đợt 62 dựng bộ chạy thử ST; ví dụ hoàn chỉnh **SFC dạng văn bản** của Ch.21 vẫn chỉ được kiểm tĩnh
  — trong khi chính Ch.21 hứa *"viết sao cho đúng với cả hai hệ"* (`.T` giữ hay về 0 khi rời bước).

## 2. Quyết định 1 — bộ chạy thử thực thi SFC theo thứ tự nào

Chuẩn **không** quy định chi tiết một vòng quét của SFC; tài liệu PLCopen (mục 3.6.1) chỉ mô tả một
*cách thực thi điển hình*, và nói thẳng *"chi tiết hiện thực có thể ảnh hưởng đáng kể tới ngữ nghĩa"*.

| Phương án | Ưu | Nhược |
|---|---|---|
| A. Theo thứ tự của CODESYS (hành động trước, chuyển tiếp sau, bước mới sống từ vòng sau) | Khớp một hệ cụ thể, phổ biến | ⚠ Gắn bộ thử vào một hãng — trái tinh thần trung lập của sách |
| ⭐ **B. Theo cách thực thi điển hình của PLCopen** (xét chuyển tiếp theo trạng thái đầu vòng → đổi bước → chạy hành động theo trạng thái mới) | Có nguồn trung lập; đơn giản; mỗi bước sống ít nhất một vòng, đúng luật tiến triển (mục 2.4) | Có thể lệch một vòng quét so với hệ thật |
| C. Cài cả hai thứ tự và chạy mọi kịch bản hai lần | Bắt được ví dụ nhạy với thứ tự | Gấp đôi mã và thời gian; ví dụ của sách không có hành động đoạn mã nên không nhạy với thứ tự |

⭐ **Chọn B**, cộng **một** tham số được chạy cả hai chiều: `.T` khi rời bước — *giữ* (chuẩn, mục 2.1) hay
*về 0* (mô tả của giáo trình Hanssen). Đó mới là chỗ ví dụ có thể hỏng giữa hai hệ; thứ tự thực thi thì
không, vì mọi hành động của ví dụ là biến BOOL bổ ngữ `N`.

Giới hạn cố ý: chỉ bổ ngữ `N` trên biến BOOL; chưa có `ACTION … END_ACTION`. Gặp thứ chưa hỗ trợ thì
**báo lỗi khi nạp**, không đoán — để ví dụ mới dùng bổ ngữ khác buộc phải mở rộng bộ thử trước.

## 3. Quyết định 2 — quy tắc 5 của hợp đồng `Execute`/`Done` (kích lại khi đang bận)

Bản đầy đủ *Creating PLCopen Compliant Libraries* cho thấy chính PLCopen có **hai** câu trả lời:

| Phương án | Nguồn | Hệ quả cho khối tự viết |
|---|---|---|
| Lệnh mới thay lệnh cũ, lệnh cũ không có phản hồi | Quy tắc chung của khối chuyển động (Phụ lục 4) | Hợp với lệnh chuyển động đổi đích giữa chừng; ⚠ bên gọi phải hiểu `Done` có thể **không bao giờ** tới cho lệnh trước |
| ⭐ **Bỏ qua sườn lên khi đang bận** | Khối mẫu `ETrig` cho người viết thư viện (mục 5.1) | Khối đơn giản, dễ đoán; bên gọi muốn lệnh mới thì chờ `Busy` tắt |

⭐ **Giữ khuyến nghị cũ — bỏ qua** — nay có gốc: `FB_BoardTransfer` theo đúng `ETrig`. Việc có điểm kết
thúc như chuyển một board không có nghĩa *"đổi đích giữa chừng"*.

## 4. Quyết định 3 — tên tín hiệu *"xử lý xong"* của ví dụ SFC

Ch.21 dùng `M_ProcessDone`, Ch.26 dùng `M_Stn1_ProcessDone` cho cùng một tín hiệu. Chọn tên của Ch.26 —
đúng quy ước `M_Stn1_` (Phụ lục N mục N.7). Sơ đồ chữ ở Ch.21 giữ nguyên độ rộng để không lệch cột.

## 5. Kết quả

| Hạng mục | Kết quả |
|---|---|
| Tải | 3 tệp, tên và dung lượng khớp trang Downloads — 59 + 27 + 89 trang |
| Đối chiếu | 25 khẳng định (nhật ký #651–#675): 10 xác nhận, 10 sửa, 5 bổ sung |
| Ch.21 | `.T` theo chuẩn; cờ bước cục bộ trong POU; `P` theo chuẩn so với CODESYS; lần quét cuối là lựa chọn của hệ; dòng 10 *hành động độc lập*; dòng 5 cách viết lại `X AND NOT Y`; hạn chế `S`/`R`; ví dụ ghi kết quả chạy thử |
| Ch.30 | Quy tắc 3, 5 theo bản gốc; `Busy` có thể không bao giờ thấy; mã lỗi `0`/`1` dành sẵn; bẫy 5 có ví dụ lò hơi; chi phí lời gọi qua interface; nguồn cập nhật |
| Ch.14 | Ghi chú *SFC không hẳn là ngôn ngữ thứ năm* |
| Bộ chạy thử | SFC dạng văn bản trong `st_mini.py`; kịch bản `ch21_sfc` 16 phép × hai kiểu `.T`; tổng **98** phép; cài 8 lỗi — bắt **8/8** |

## 6. Hệ quả

- ⭐ Mọi ví dụ hoàn chỉnh trừ LD (Ch.15) nay được **chạy**, không chỉ đọc.
- ⚠ Ví dụ SFC mới dùng bổ ngữ khác `N` hay `ACTION … END_ACTION` sẽ làm bộ thử **báo lỗi khi nạp** —
  cố ý: mở rộng bộ thử trước, rồi mới in ví dụ.
- Còn treo, không đổi: chuyên gia an toàn cho Ch.3, 6, 47, 48, 56 và Phụ lục D.
