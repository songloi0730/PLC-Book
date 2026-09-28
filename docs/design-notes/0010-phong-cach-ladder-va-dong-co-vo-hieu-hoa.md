# 0010 — Đợt 64: phong cách ladder của từng hãng, và "đúng trên giấy nhưng người ta sẽ vượt qua"

**Trạng thái:** ✅ **XONG 2026-09-29**
**Ngày:** 2026-09-28 – 2026-09-29
**Thuộc:** đợt 64 — yêu cầu của chủ dự án: *"cách viết ladder của Siemens và các hãng khác như
Mitsubishi có vẻ khác nhau, hãy giới thiệu, hãy phản biện nội dung đã viết, có thể ghi vào sách … mã
có thể chính xác nhưng thực tế có thể làm khác, ví dụ cửa an toàn: lỗi đơn giản 1 tiếng 1 lần nhưng
thời gian mở cửa an toàn còn lâu hơn xử lý vấn đề, người vận hành nhiều máy sẽ tìm cách bỏ qua"*.

---

## 1. Bối cảnh — sách đang có gì

| Chỗ | Có | Thiếu |
|---|---|---|
| Ch.15 mục 15.6 | Khác biệt **tên lệnh** (tiếp điểm, cuộn nhớ, cảnh báo cuộn trùng) | ⚠ Khác biệt **phong cách**: tổ chức chương trình, cách đặt tên, cách viết tự giữ, lệnh kiểu xung, tín hiệu vòng quét đầu |
| Phụ lục A2 | Đối chiếu lệnh; một bước trình tự viết năm lần | ⚠ Bản Siemens viết bằng **SCL**, nên không thấy phong cách LAD của Siemens |
| Ch.47 | Thiết bị bảo vệ, muting, bẫy chế độ tay | ⚠⚠ **Không có** gì về *động cơ vô hiệu hoá* khoá liên động |
| Ch.28 mục 28.5 | Huỷ chu trình hay chạy tiếp — theo giá trị sản phẩm, độ phức tạp mã | ⚠ Thiếu chiều **tần suất lỗi × thời gian phục hồi** — và hệ quả về con người |

## 2. Phản biện — phát hiện đã kiểm

| # | Chỗ | Phát hiện | Căn cứ |
|---|---|---|---|
| 1 | A2.2 | ⚠ Mitsubishi *"trễ khi tắt, xung: phải tự dựng"* — **sai** với dòng iQ-F: có khối chuẩn `TOF`, `TP` (và biến thể `_10`, `_E`) cùng lệnh `STMR` | Sổ tay lập trình FX5 — Instructions/Standard Functions/Function Blocks, mục 5.2 và lệnh `STMR` — **chính tài liệu A2.2 đang dẫn** |
| 2 | A2.8 | ⚠ Các nhánh sau một điều kiện chung trong ladder **dùng chung kết quả đã lưu** (`MPS`/`MRD`/`MPP`) — không có `ELSIF`. `X5` và `T5` cùng bật trong một vòng quét thì nhánh lỗi viết sau **thắng** (bước 900), còn bản ST cho bước 50 | Sổ tay FX5 — `MPS` lưu, `MRD` đọc, `MPP` đọc và xoá kết quả phép toán |
| 3 | A2.8 | Siemens trình bày bằng SCL — ⭐ **có lý**: hướng dẫn phong cách của chính Siemens khuyên viết ruột khối bằng SCL, dùng LAD/FBD để nối khối trong OB và cho khối chủ yếu là logic nhị phân. Nhưng phải **nói ra**, và phải cho người đọc thấy LAD của Siemens ở chỗ khác | *Programming Styleguide for S7-1200/S7-1500* V1.2 (10/2016), mục 4.1.3 |
| 4 | Ch.15 | Sách chưa nêu tín hiệu **vòng quét đầu** của từng hệ, dù Ch.16 Bẫy 9 dùng `M_FirstScan` | FX5: `SM402`; FX cũ, Inovance H3U: `M8002`; Siemens: OB khởi động; Rockwell: `S:FS` (1756-PM005) |
| 5 | Ch.28 mục 28.5 | *"Huỷ chu trình (khuyến nghị mặc định)"* đúng với lỗi **hiếm**. Với lỗi lặp lại mỗi giờ, đường phục hồi dài nhân với số máy mỗi người trông tạo ra **động cơ vô hiệu hoá** cửa an toàn | SICK *Six Steps* mục 1-2; Schneider *Machine Safety Guide*; DGUV IFA 2/2017e; ISO 14119:2024 chương 8 |
| 6 | Ch.47 | ⚠⚠ Thiếu hẳn chủ đề **động cơ vô hiệu hoá** — trong khi ISO 14119 có nguyên một chương về nó | Như trên |

## 3. Quyết định 1 — đặt phần "phong cách ladder" ở đâu

| Phương án | Ưu | Nhược |
|---|---|---|
| ⭐ **A. Mở rộng Ch.15 mục 15.6** — cùng nấc 1 của DP-01 viết theo ba phong cách | Người học ladder gặp nó đúng lúc; tái dùng nấc thang đã giải thích; không lệch lát cắt 1 | Ch.15 dài thêm |
| B. Mục mới trong Phụ lục A2 | Đúng chỗ "đối chiếu hãng" | Người đọc thân sách ít khi mở phụ lục; A2 vốn nói về **lệnh** |
| C. Chương mới | Đủ chỗ | ⚠ Làm loãng; phần lớn nội dung đã có rải rác |

⭐ **Chọn A**, cộng con trỏ từ A2.8 về đó. Ba phong cách: **kiểu thiết bị** (Mitsubishi, Inovance dòng
nhỏ), **kiểu khối** (Siemens TIA), **kiểu tag** (Rockwell). Kèm bảng mạnh/yếu (B18) và cặp
`SET`/`RST` so với nhánh tự giữ — cách viết khác nhau thật sự, không chỉ khác tên.

## 4. Quyết định 2 — đặt phần "động cơ vô hiệu hoá" ở đâu

| Phương án | Ưu | Nhược |
|---|---|---|
| A. Chỉ Ch.47 | Chủ đề an toàn ở chương an toàn | ⚠ Người **lập trình trình tự phục hồi** — người quyết định phục hồi mất bao lâu — đọc Ch.28, không đọc Ch.47 |
| ⭐ **B. Ch.47 (nguyên lý, biện pháp) + Ch.28 (thiết kế đường phục hồi)** | Mỗi người đọc gặp phần của mình; hai mục trỏ sang nhau | Hai chỗ phải giữ khớp |
| C. Chương mới về yếu tố con người | Đủ chỗ cho cả Ch.12, 44, 53 cùng chủ đề | Tách chủ đề khỏi nơi người ta cần nó; thêm một chương chờ chuyên gia duyệt |

⭐ **Chọn B.** Ch.47 thêm mục 47.7c và Bẫy 8; Ch.28 thêm một dòng vào bảng đánh đổi và ba nhóm lỗi
theo cách phục hồi. ⚠ Ràng buộc: **B3** — không một dòng nào mô tả cách vượt qua; chỉ mô tả **vì sao**
người ta muốn vượt và **thiết kế** để không cần vượt. **B3b** — Ch.47 giữ cờ chờ chuyên gia.

## 5. Kết quả

| Hạng mục | Kết quả |
|---|---|
| Ch.15 mục 15.6 | ⭐ *Cùng một nấc thang — ba phong cách viết*: nấc 1 theo kiểu thiết bị, kiểu khối, kiểu tag; bảng tám khía cạnh; mạnh/yếu; cặp `SET`/`RST` so với tự giữ; năm điều mang theo; lời phản biện chính cuốn sách |
| Phụ lục A2 | A2.2 sửa `TOF`/`TP` của Mitsubishi; A2.5 lệnh kiểu xung; A2.8 thêm `ANI X5` và lý do bản Siemens là SCL |
| Ch.47 | ⭐⭐ Mục 47.7c — năm tầng biện pháp; Bẫy 8; bảng chốt dòng 2c; câu tự kiểm 17 |
| Ch.28 mục 28.5 | Dòng *thời gian phục hồi*; ba nhóm lỗi theo cách phục hồi; bảng chốt dòng 12; câu tự kiểm 12 |
| Kiểm | Bảy bộ kiểm 0 lỗi; bộ kiểm bóc lớp (B8) bắt một lần nhắc *màn hình vận hành* ở Ch.28 (lát cắt 2) — đã đổi thành nút trên tủ điều khiển |

Chi tiết: nhật ký đối chiếu, đợt 64 (#676–#697).

## 6. Hệ quả

- Sách nói thẳng một **giới hạn của chính nó**: ví dụ viết theo tên tag và ST, gần phong cách Siemens,
  CODESYS, Rockwell; người đọc ở nhà máy chạy máy Nhật sẽ gặp phong cách khác — nguyên tắc giữ nguyên.
- ⭐ Nguyên tắc *"thứ gây phiền sẽ bị vô hiệu hoá"* nay nối được bốn chỗ: Ch.12 (cảnh báo sớm), Ch.44
  (ức chế báo động), Ch.53 Bẫy 5 (quy trình bị lách), Ch.47 mục 47.7c (cửa an toàn).
