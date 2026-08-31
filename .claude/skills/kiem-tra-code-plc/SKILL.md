---
name: kiem-tra-code-plc
description: Rà mọi đoạn code PLC (ST, LD, SFC, giả mã) trong một chương sách — kiểm tính đúng, tính an toàn khi chạy trong môi trường quét, và tính trung lập hãng. Dùng khi chương có code block, hoặc khi cần nghiệm thu chất lượng ví dụ lập trình.
---

# Rà code PLC trong bản thảo

Code trong sách nguy hiểm hơn code trong máy: người đọc **sao chép nó**. Một
mẫu sai được in ra sẽ được nhân bản vào những cái máy mà mình không thấy.

## Bước 0 — Máy quét trước

```bash
python tools/kiem_tra_chuong.py <N>
```

Các mục mức `TIN` (C1–C4) là điểm cần mở ra xem, không phải lỗi chắc chắn.

---

## Bước 1 — Bảy phép kiểm bắt buộc, theo thứ tự

### K1. Chạy trong vòng quét thì sao?

Mã PLC chạy lại **từ đầu, mỗi vòng quét**. Với mỗi đoạn, hỏi:

- Đoạn này chạy 1000 lần/giây thì có gì hỏng không?
- Có biến nào được đọc ở vòng này nhưng chỉ được ghi ở vòng sau không?
- Có `WHILE`/`FOR` nào mà số vòng phụ thuộc dữ liệu ngoài không? → nguy cơ
  quá thời gian quét (watchdog).
- Sườn lên/xuống có được bắt bằng biến nhớ trạng thái cũ không, hay đang giả
  định "chạy một lần"?

### K2. Ngõ ra có bị ghi từ hai chỗ không?

Trong LD gọi là **double coil**; trong ST là hai lệnh gán cùng một ngõ ra ở
hai nhánh có thể cùng đúng. Grep mọi `DO_*` trong đoạn, đếm số chỗ gán.
Nếu > 1, phải kiểm bằng tay xem có loại trừ nhau thật không.

### K3. Chuyển bước dựa vào cái gì?

Đây là **bẫy trung tâm** của cả cuốn sách (Ch.17, Ch.26).

| Mẫu | Kết luận |
|---|---|
| `IF DI_Stop1Up THEN Step := Step + 1;` | Đúng — chờ **phản hồi thật** |
| `IF T_Delay.Q THEN Step := Step + 1;` | **SAI** — chờ đồng hồ, không phải chờ máy |
| `IF DI_Stop1Up AND T_Debounce.Q THEN ...` | Đúng — timer chỉ lọc rung |
| `IF T_Timeout.Q THEN Alarm := TRUE;` | Đúng — timer làm giới hạn, không làm điều kiện tiến |

Quy tắc: **timer được phép kết thúc một bước bằng lỗi, không được phép kết
thúc một bước bằng thành công** — trừ khi bản thân việc chờ chính là mục đích
(ví dụ thời gian chiếu UV), và khi đó phải nói rõ trong lời văn.

### K4. Mất điện giữa chừng thì trạng thái ở đâu?

- Biến nào cần giữ (retentive) mà đang khai báo thường?
- Biến nào đang giữ mà lẽ ra phải xoá khi khởi động lại? Giữ nguyên số bước
  cũ sau khi mất điện có thể khiến máy chạy tiếp vào một tư thế không còn
  đúng nữa — nguy hiểm hơn là mất số bước.

### K5. Tư thế cơ cấu suy ra từ đâu?

Không được suy tư thế từ **một** cảm biến hoặc từ **cảm biến đối diện**:

```
(* SAI — "không ở trên" không có nghĩa là "đang ở dưới";
   có thể đang kẹt giữa chừng, hoặc cảm biến hỏng *)
IF NOT DI_Stop1Up THEN  ...

(* ĐÚNG — trạng thái không xác định phải được xử lý riêng *)
IF DI_Stop1Dn AND NOT DI_Stop1Up THEN  (* chắc chắn ở dưới *)
ELSIF DI_Stop1Up AND NOT DI_Stop1Dn THEN (* chắc chắn ở trên *)
ELSE (* giữa chừng hoặc hỏng cảm biến — báo lỗi, không đoán *)
```

### K6. Có gì trong code chỉ đúng với một hãng không? (B1)

- Kiểu dữ liệu, tên khối chức năng, cú pháp truy cập địa chỉ phải theo
  **IEC 61131-3**, không theo phương ngữ hãng.
- Tên biến theo quy ước máy mẫu (`DI_`, `DO_`, `AI_`, `AO_`), không dùng địa
  chỉ tuyệt đối kiểu `%I0.0` trong thân sách — địa chỉ tuyệt đối để dành cho
  Phụ lục A khi nói về từng hệ cụ thể.
- Nếu buộc phải nêu khác biệt hãng, đưa vào mục N.5, không trộn vào ví dụ chính.

### K7. Chú thích có giải thích *tại sao* không?

Chú thích lặp lại code (`(* tăng bước *)`) là chú thích thừa. Chú thích tốt
nói lý do: `(* chờ phản hồi thật, không chờ timer — xem Bẫy 3 *)`.

---

## Bước 2 — Kiểm tên tín hiệu

Mọi tên tín hiệu trong code phải **có thật** trong `docs/case_study_may_mau.md`:

```bash
grep -o -E '\b(DI|DO|AI|AO)_[A-Za-z0-9]+' docs/chNN_*.md | sort -u
```

So với danh sách I/O của DP-01. Tên bịa ra giữa chừng là lỗi CHẶN — nó phá
tính nhất quán xuyên sách, thứ làm nên giá trị của việc dùng một máy mẫu.

Đồng thời kiểm **lát cắt**: chương ở lát cắt 1 chỉ được dùng tín hiệu của
lát cắt 1.

---

## Bước 3 — Báo cáo

```
## Rà code — Chương N

Số đoạn code: X

| # | Dòng | Phép kiểm | Kết luận | Ghi chú |
|---|---|---|---|---|
| 1 | 142–160 | K3 | CHẶN | dùng T_Cure.Q để tiến bước, không có phản hồi |
| 2 | 210–228 | K1 | ĐẠT | — |

Tên tín hiệu lạ: <danh sách hoặc "không có">
CHẶN: <số mục>
```

Nếu một đoạn code **cố ý sai** để minh hoạ bẫy, nó phải được đánh dấu rõ ngay
trong code (`(* SAI — minh hoạ bẫy *)`) và trong lời văn ngay trước đó. Đoạn
sai không được đánh dấu là lỗi CHẶN, kể cả khi lời văn sau đó có giải thích —
người đọc lướt sẽ chép nhầm.
