---
name: doi-chieu-nguon
description: Đối chiếu các khẳng định trong một chương sách PLC với tài liệu gốc (40+ PDF trong thư mục reference) để phát hiện nội dung viết từ trí nhớ, sai chi tiết, hoặc viện dẫn tiêu chuẩn đã thu hồi. Dùng khi rà lại chương, khi thêm khẳng định kỹ thuật mới, hoặc trước khi phát hành.
---

# Đối chiếu nguồn — chống "viết từ trí nhớ"

## Vấn đề mà skill này giải

Bộ kiểm tự động bắt được **lỗi hình thức** (thiếu mục, dẫn chiếu gãy, tag lệch bảng).
Nó **không bắt được** thứ nguy hiểm nhất: **một câu đúng ngữ pháp, đúng khung, nghe rất
thuyết phục — và sai sự thật.**

Loại lỗi đó chỉ lộ ra khi so với tài liệu gốc.

> ⭐ **Bằng chứng thực tế:** Phụ lục A2 từng viết *"độ phân giải bộ định thời Mitsubishi tuỳ vào
> dải thiết bị `T`"*. Manual FX5 cho thấy độ phân giải đến từ **lệnh** (`OUT`/`OUTH`/`OUTHS`),
> đồng thời cũng có kiểu thiết bị. Câu đó đúng một nửa và nói quá chắc chắn. Không có bước đối
> chiếu thì nó đã lên bản in.

---

## QUY TẮC VÀNG

> ⭐⭐ **Không sửa và không xác nhận bất kỳ khẳng định nào trước khi đã chạy `tra_nguon.py`
> và ĐỌC đoạn văn gốc.**

Ba kết luận được phép, và phải ghi rõ cái nào:

| Kết luận | Nghĩa | Việc phải làm |
|---|---|---|
| ✅ **XÁC NHẬN** | Nguồn nói đúng như sách | Ghi nguồn vào nhật ký; cân nhắc bổ sung thuật ngữ gốc để người đọc tra được |
| ⚠ **SAI / THIẾU** | Nguồn nói khác, hoặc sách nói quá chắc chắn | Sửa chương, ghi nhật ký cả nội dung cũ lẫn mới |
| ❔ **KHÔNG CÓ NGUỒN** | Bộ tài liệu không phủ chủ đề | ⚠ **KHÔNG được coi là xác nhận.** Tra nguồn ngoài, hoặc **hạ giọng** khẳng định |

⚠ **Cấm tuyệt đối:** kết luận "chắc là đúng" khi không tìm được nguồn.

---

## Quy trình 6 bước

### Bước 1 — Trích các khẳng định kiểm được

Đọc chương, liệt kê những câu **có thể sai và hậu quả đáng kể**:

| Ưu tiên | Loại khẳng định |
|---|---|
| ⭐⭐ Cao nhất | Con số cụ thể (ngưỡng, dải, độ phân giải, tuổi thọ) |
| ⭐⭐ Cao nhất | Hành vi của một hãng cụ thể ("Rockwell cập nhật I/O bất đồng bộ") |
| ⭐ Cao | Viện dẫn tiêu chuẩn — mã số, phạm vi, còn hiệu lực không |
| ⭐ Cao | Khẳng định an toàn (Ch.3, 6, 47, 48, Phụ lục D) |
| Vừa | Thực hành phổ biến ("phần lớn máy dùng…") |

⚠ **Bỏ qua**: ý kiến sư phạm, cách trình bày, ví dụ hư cấu có nhãn rõ.

### Bước 2 — Tra

```bash
python tools/tra_nguon.py "<từ khoá tiếng Anh>"
python tools/tra_nguon.py "<từ khoá>" --tep <tên hãng>   # thu hẹp
python tools/tra_nguon.py --liet-ke                       # xem có nguồn gì
```

⭐ **Tra bằng tiếng Anh** — toàn bộ tài liệu gốc là tiếng Anh.
⭐ Tra **thuật ngữ của hãng**, không phải bản dịch tiếng Việt.

### Bước 3 — ĐỌC đoạn gốc, không chỉ nhìn số chỗ khớp

⚠ Số chỗ khớp **không phải bằng chứng**. Phải đọc câu văn.

Nếu đoạn trích chưa đủ, mở PDF đúng trang bằng công cụ đọc file.

### Bước 4 — Phân loại và sửa

| Tình huống | Cách sửa |
|---|---|
| Sách sai hẳn | Sửa lại theo nguồn |
| ⭐ Sách **đúng một nửa** | ⭐ Loại hay gặp nhất — bổ sung cơ chế còn thiếu, hạ mức chắc chắn |
| Sách đúng nhưng mơ hồ | ⭐ Bổ sung **cơ chế cụ thể** — giá trị nhất cho người đọc |
| Sách đúng | ⭐ Thêm **thuật ngữ gốc tiếng Anh** để người đọc tra tiếp được |

### Bước 5 — Dẫn nguồn trong sách

⚠⚠ **KHÔNG chép nguyên văn tiêu chuẩn có bản quyền.** Diễn đạt lại và nêu tên tài liệu:

```markdown
*(Đối chiếu: Rockwell Logix 5000 I/O and Tag Data, 1756-PM004 — mục về đệm giá trị I/O.)*
```

⭐ Với tài liệu hãng, nêu **mã tài liệu** để người đọc tự tìm.

### Bước 6 — Ghi nhật ký

Thêm dòng vào `docs/00d_Nhat_ky_doi_chieu.md`. ⭐ **Ghi cả kết luận ✅** — để lần sau không phải
kiểm lại, và để biết chương nào **chưa** được đối chiếu.

---

## Bộ nguồn có gì

| Nhóm | Mạnh về | Dùng cho chương |
|---|---|---|
| `01_Instrumentation` — Kuphaldt | ⭐ Đo lường, 4–20 mA, PID, an toàn quá trình, chẩn đoán | 31, 33, 34, 35, 51 |
| `02_PLC_Textbook` — Hugh Jack | ⭐ Phương pháp thiết kế, trạng thái, fail-safe | 15–22, 25–30 |
| `03_Vendor_Manuals` | ⭐⭐ Siemens · Mitsubishi · Rockwell | ⭐ **Phụ lục A1, A2** |
| `04_Safety_Standards` — SICK, Schneider, DGUV/IFA | ⭐⭐ An toàn máy, PL, thiết bị bảo vệ | ⚠ **3, 6, 47, 48, D** |
| `06_Electric_Circuits` — Kuphaldt | Điện DC/AC/số | 3, 8, 9 |
| `07_Networks_Whitepapers` | EtherCAT/TSN, kiến trúc Ethernet | 40 |
| `08_Open_Specs` | ⭐⭐ **Modbus · IO-Link · PLCopen Motion** (đặc tả gốc) | 37, 39, 12 |

### ⚠ Chỗ bộ nguồn KHÔNG phủ

⭐ **Biết nguồn thiếu ở đâu quan trọng ngang biết nó có gì.**

| Không có | Hệ quả |
|---|---|
| ⚠ **CODESYS** — không có tài liệu | Khẳng định về CODESYS phải tra ngoài, ghi rõ ngày |
| ⚠ **Inovance** — không có tài liệu | Như trên; ⭐ hoặc hạ giọng thành "tuỳ dòng" |
| ⚠ **Bản gốc tiêu chuẩn ISO/IEC** | Chỉ có tài liệu diễn giải của hãng — ⚠⚠ **không được dẫn số điều khoản** |
| Thị trường thiết bị hiện hành | Câu hỏi "hãng nào phổ biến" phải tra ngoài |

---

## ⚠⚠ Riêng chương an toàn

Với Ch.3, 6, 47, 48 và Phụ lục D:

| Quy tắc | |
|---|---|
| ⭐ Tài liệu trong bộ là **diễn giải của hãng**, không phải tiêu chuẩn gốc | Dùng để hiểu, ⚠ **không dùng để dẫn điều khoản** |
| ⚠⚠ Đối chiếu xong **KHÔNG gỡ được cờ ⚠** | Cờ đó chỉ **chuyên gia an toàn người thật** gỡ được |
| ⭐ Kết luận đúng: *"đã đối chiếu với tài liệu X, không mâu thuẫn"* | ⚠ Không phải: *"đã kiểm, an toàn"* |

---

## Danh mục kết thúc

- [ ] Đã liệt kê khẳng định kiểm được của chương
- [ ] Mỗi khẳng định có kết luận ✅ / ⚠ / ❔ — ⚠ **không bỏ trống**
- [ ] Mọi ⚠ đã sửa trong chương
- [ ] Mọi ❔ đã hạ giọng hoặc ghi rõ nguồn ngoài + ngày tra
- [ ] Đã ghi `docs/00d_Nhat_ky_doi_chieu.md`
- [ ] Chạy lại `kiem_tra_chuong.py` và `kiem_nhat_quan.py`
