---
name: danh-gia-chuong
description: Đánh giá một chương sách PLC đã viết — chạy kiểm tra máy trước, rồi rà thủ công 7 trục chất lượng, kết luận có kèm bằng chứng dòng cụ thể. Dùng khi cần review/nghiệm thu một chương, hoặc khi người dùng nói "đánh giá lại chương N".
---

# Đánh giá chương sách PLC

## Quy tắc vàng

**KHÔNG kết luận bất kỳ điều gì trước khi đã grep ra bằng chứng.**

Mọi nhận xét phải kèm **số dòng + trích dẫn**. Nhận xét kiểu "chương này hơi
mỏng phần X" mà không chỉ được dòng nào là nhận xét vô giá trị — bỏ đi.
Lý do: người viết (kể cả AI) rất dễ "nhớ" ra thiếu sót không có thật, rồi
sửa một chỗ vốn đã đúng và làm hỏng nó.

---

## Bước 0 — Chạy máy trước, mắt sau

```bash
python tools/kiem_tra_chuong.py <N>
```

Bộ kiểm tra bắt được: mục bắt buộc thiếu, tên phần mềm hãng lọt vào thân sách,
vi phạm lát cắt, hình hỏng/thiếu chú thích, tiêu chuẩn chưa viện dẫn, mẫu code
đáng ngờ. **Đừng rà tay những thứ này** — máy chính xác hơn và không mệt.

Chỉ khi máy sạch mới sang Bước 1. Mức TIN không chặn, nhưng phải mở từng chỗ
xem, vì đó là các bẫy trung tâm của sách (chuyển bước bằng timer, vòng lặp
trong môi trường quét, suy tư thế từ cảm biến đối diện).

---

## Bước 1 — Bảy trục rà thủ công

Máy không kiểm được những trục dưới đây. Với **mỗi trục**, ghi một trong ba
kết luận: `ĐẠT` · `SỬA` (kèm dòng) · `KHÔNG ÁP DỤNG` (kèm lý do).

### T1. Chương này có tự đứng được không? (B6)

Người đọc chỉ có các chương trước nó — có hiểu trọn không?

- Grep mọi thuật ngữ chuyên môn xuất hiện lần đầu; mỗi cái phải được định
  nghĩa tại chỗ hoặc dẫn về đúng chương đã dạy nó.
- Dẫn chiếu **lùi** ("đã nói ở Chương 10") phải đúng chương đó có dạy thật.
- Dẫn chiếu **tiến** ("sẽ nói ở Chương 37") chỉ được dùng để trấn an, không
  được là chỗ dựa để hiểu đoạn đang đọc.

### T2. Ví dụ có bám máy mẫu DP-01 không? (B8)

- Mọi tín hiệu nêu tên phải có trong `docs/case_study_may_mau.md`. Grep từng
  cái. Tên bịa ra giữa chừng là lỗi nặng — phá vỡ tính nhất quán xuyên sách.
- Nếu chương cần một thiết bị chưa thuộc lát cắt của nó: hoặc đổi ví dụ,
  hoặc chuyển chương, **không** lặng lẽ kéo thiết bị về sớm.

### T3. Kết luận có nguồn không? (B2)

Với mỗi câu khẳng định mang tính kỹ thuật cứng (con số, ngưỡng, "phải", "không
bao giờ"), hỏi: **căn cứ ở đâu?**

- Tiêu chuẩn → phải ghi số hiệu + điều khoản nếu biết.
- Tài liệu trong `../PLC/reference/` → ghi tên file + trang.
- Kinh nghiệm nghề, không có nguồn → **phải nói rõ là kinh nghiệm**, không
  đội lốt tiêu chuẩn. Đây là lỗi hay gặp nhất và nguy hiểm nhất.

### T4. Cảnh báo an toàn có đặt đúng chỗ không? (B3)

- ⚠ NGUY HIỂM đặt **trước** thao tác, không phải sau.
- Chương nào chạm tới điện/khí nén/chuyển động phải có cảnh báo, kể cả khi
  chương đó "chỉ nói về lập trình".
- Không có câu nào ngụ ý PLC thường có thể đảm nhiệm chức năng an toàn.
- Nếu chương thuộc danh sách `chuong_an_toan`: kiểm dòng miễn trừ trách nhiệm.

### T5. Bảng chốt có thật sự chốt không? (B14)

Bảng chỉ liệt kê lại tiêu đề các mục là bảng vô dụng. Bảng tốt trả lời được
"khi nào dùng cái nào" hoặc "sai thì hiện tượng ra sao".

### T6. Song ngữ đủ chưa? (B11)

Tiêu chí là **ĐỦ, không phải tiết chế**. Duyệt các khái niệm chính của chương:
mỗi khái niệm mà người đọc sẽ gặp lại trong tài liệu tiếng Anh của hãng đều
phải có tiếng Anh ở lần xuất hiện đầu.

Nếu `kiem_tra_chuong.py` báo dưới 4 cặp song ngữ, gần như chắc chắn có gap.

### T7. Bẫy có phải bẫy thật không? (B5)

Bẫy tốt = lỗi mà người mới **thật sự mắc**, kèm hiện tượng quan sát được và
cách sửa. Bẫy dở = lời khuyên chung chung ("nên cẩn thận khi...").

Mỗi bẫy phải trả lời: sai thế nào → **thấy gì trên máy** → sửa ra sao.

---

## Bước 2 — Xếp mức và dừng đúng lúc

| Mức | Nghĩa | Xử lý |
|-----|-------|-------|
| **CHẶN** | Sai kỹ thuật, sai an toàn, hoặc thiếu mục bắt buộc | Sửa ngay, không phát hành chương |
| **NÊN SỬA** | Đúng nhưng thiếu/khó hiểu/thiếu nguồn | Sửa trong đợt này |
| **GHI NHẬN** | Có thể hay hơn | Ghi vào `docs/00_Muc_luc.md`, không sửa ngay |

### Tiêu chí dừng

Nếu đã rà **từ vòng 3 trở đi** và mọi góp ý còn lại đều rơi vào bốn nhóm:

1. "có thể thêm ví dụ nữa"
2. "có thể diễn đạt gọn hơn"
3. "có thể thêm hình minh hoạ"
4. "có thể mở rộng phần X"

→ **DỪNG**. Chương đã đủ. Rà tiếp chỉ tạo sửa đổi vô ích và làm loãng.

**Ngoại lệ tuyệt đối:** không bao giờ áp tiêu chí dừng cho một mục **CHẶN** có
bằng chứng dòng cụ thể — nhất là mục an toàn. Bao nhiêu vòng cũng phải sửa.

---

## Bước 3 — Báo cáo

```
## Chương N — <tên>

Máy:  X LỖI · Y CẢNH BÁO · Z TIN
Vòng: <thứ mấy>

### CHẶN
- [dòng 142] <vấn đề> → <cách sửa>

### NÊN SỬA
- [dòng 88] <vấn đề> → <cách sửa>

### GHI NHẬN
- <ý tưởng cho lần sau>

Kết luận: ĐẠT / ĐẠT SAU KHI SỬA / CHƯA ĐẠT
```

Nếu không có mục nào ở một cấp, ghi "không có" — đừng bỏ trống, người đọc
không biết là đã rà mà sạch hay là quên rà.
