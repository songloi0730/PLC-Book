---
name: kiem-tra-an-toan
description: Soi một chương sách PLC theo ma trận tiêu chuẩn an toàn/chức năng (ISO 12100, ISO 13849, IEC 60204-1, IEC 61508, IEC 62061, IEC 62682, IEC 62381...). Dùng khi viết hoặc rà chương có chạm tới điện, khí nén, chuyển động, dừng khẩn, cảnh báo, hoặc nghiệm thu.
---

# Soi chương theo tiêu chuẩn an toàn

## Nguyên tắc bất di dịch

1. **Không trích nguyên văn tiêu chuẩn.** IEC/ISO có bản quyền. Được phép:
   nêu số hiệu, tên, phạm vi, và **diễn giải bằng lời của mình**. Không được:
   chép bảng, chép định nghĩa nguyên văn, chép sơ đồ.
2. **Không tự phong là căn cứ pháp lý.** Sách hướng dẫn hiểu tiêu chuẩn, không
   thay tiêu chuẩn. Mọi chương an toàn phải nói rõ điều đó.
3. **Không viện dẫn điều khoản mà chưa tra.** Ghi "IEC 60204-1" thì được; ghi
   "IEC 60204-1 §9.2.5.4.2" mà chưa mở bản gốc ra xem là bịa. Nếu chưa tra
   được, ghi số hiệu tiêu chuẩn và mô tả nội dung, **không** ghi số điều khoản.
4. **PLC thường ≠ PLC an toàn.** Bất kỳ đoạn nào có thể bị hiểu là "dùng PLC
   thường làm chức năng an toàn" đều là mục CHẶN.

---

## Ma trận tiêu chuẩn

### Nhóm A — An toàn máy (chương chạm chuyển động, che chắn, dừng)

| Số hiệu | Phạm vi | Soi chương bằng câu hỏi |
|---|---|---|
| **ISO 12100** | Nguyên tắc chung thiết kế an toàn máy; đánh giá & giảm rủi ro | Chương có nói rõ thứ tự ba bước: **thiết kế vốn đã an toàn → che chắn/bảo vệ → thông tin cho người dùng**? Có chỗ nào nhảy thẳng sang "cảnh báo người vận hành" trong khi lẽ ra phải sửa thiết kế? |
| **ISO 13849-1** | Bộ phận liên quan an toàn của hệ điều khiển — thiết kế; PL a–e, Category B/1/2/3/4 | Có chỗ nào nêu mức PL/Category mà không kèm điều kiện đạt được nó? Có nhầm "dùng linh kiện an toàn" = "đạt PL" không? |
| **ISO 13849-2** | Kiểm chứng (validation) | Chương nghiệm thu có phân biệt **kiểm chứng thiết kế** với **thử chức năng** không? |
| **IEC 62061** | An toàn chức năng hệ điều khiển máy (hướng SIL) | Nếu chương nhắc SIL cho máy: có nói rõ quan hệ với PL không? |
| **IEC 61508** | An toàn chức năng hệ E/E/PE — tiêu chuẩn gốc, SIL 1–4 | Chương có giải thích 13849/62061 **bắt nguồn từ** 61508 không? Có nhầm SIL của quá trình với PL của máy không? |
| **ISO 13850** | Chức năng dừng khẩn cấp — nguyên tắc thiết kế | E-Stop có được mô tả là **biện pháp bổ trợ**, không phải biện pháp bảo vệ chính? |
| **ISO 14119** | Thiết bị khoá liên động gắn với che chắn | Có bàn tới việc **đánh lừa (defeat)** khoá liên động không? Đây là lỗi thực tế phổ biến nhất. |

### Nhóm B — Điện & thiết bị (chương chạm tủ điện, đấu nối, nguồn)

| Số hiệu | Phạm vi | Soi chương bằng câu hỏi |
|---|---|---|
| **IEC 60204-1** | Thiết bị điện của máy — yêu cầu chung | Có phân biệt **Stop Category 0 / 1 / 2** không? Có nhầm "dừng" với "cách ly nguồn" không? Màu nút bấm/đèn có theo quy ước không? |
| **IEC 60947-5-1** | Khí cụ điện hạ áp — thiết bị mạch điều khiển | Tiếp điểm an toàn có nêu yêu cầu **mở cưỡng bức (direct opening action)** không? Chỗ này hay bị bỏ. |
| **IEC 61131-2** | PLC — yêu cầu thiết bị và phép thử | Thông số ngõ vào/ra (loại 1/2/3, dòng rò, thời gian đáp ứng) có dẫn về đây không? |
| **IEC 61800-5-2** | Biến tần/servo — yêu cầu an toàn chức năng | Các hàm STO/SS1/SLS có được gọi đúng tên không? Có nhầm STO với "cắt lệnh chạy" không? |
| **IEC 61643** (bộ) | Thiết bị chống sét lan truyền hạ áp | Chương nhiễu/nối đất có phân biệt SPD nguồn với SPD tín hiệu không? |
| **IEC 61340-5-1 / -5-2** | Bảo vệ linh kiện điện tử khỏi tĩnh điện (ESD) | Máy mẫu DP-01 chạy PCB — chương có nhắc EPA, vòng đeo tay, ionizer đúng vai trò không? |
| **ISO 4414** | Truyền động khí nén — quy tắc chung và an toàn | Có bàn **xả áp dư** trước khi bảo trì không? Van 5/3 và tư thế khi mất khí có được nói không? |

### Nhóm C — Vận hành & bàn giao (chương chạm cảnh báo, HMI, nghiệm thu, mạng)

| Số hiệu | Phạm vi | Soi chương bằng câu hỏi |
|---|---|---|
| **IEC 62682** | Quản lý hệ thống cảnh báo | Có nói tới **vòng đời cảnh báo** và **lụt cảnh báo (alarm flood)** không? Có tiêu chí "mỗi cảnh báo phải kèm hành động ứng phó" không? *(Bản quốc tế của ISA-18.2 — dùng số hiệu IEC để tránh vướng bản quyền ANSI.)* |
| **IEC 62381** | Nghiệm thu tự động hoá: FAT / SAT / SIT | Chương nghiệm thu có phân biệt rõ ba mốc này không? Có nói ai ký, ký cái gì không? |
| **IEC 62443** (bộ) | An ninh mạng hệ điều khiển công nghiệp | Có khái niệm **zone/conduit** không? Có chỗ nào khuyên nối PLC thẳng ra mạng văn phòng không? |
| **IEC 62541** | OPC UA | Có phân biệt OPC UA với OPC Classic/DA không? |
| **IEC 61784 / IEC 61158** | Profile & đặc tả fieldbus công nghiệp | Tên giao thức có gọi đúng theo profile không? |

> **IEC 62366** (kỹ thuật khả dụng) chỉ áp cho **thiết bị y tế**. Không viện dẫn
> cho máy công nghiệp. Nếu cần nói về khả dụng HMI, dùng nguyên tắc thiết kế
> chung và nói rõ đó là thực hành tốt, không phải yêu cầu tiêu chuẩn.

---

## Quy trình soi một chương

1. **Xác định nhóm.** Chương chạm cái gì → lấy đúng các dòng trong ma trận.
   Không soi toàn bộ ma trận cho mọi chương — sẽ ra một đống "không áp dụng".

2. **Với mỗi dòng đã chọn, grep chương tìm bằng chứng.** Ba kết quả:
   - `CÓ, ĐÚNG` — chương đã bàn và bàn đúng.
   - `CÓ, SAI/THIẾU` — chương có nhắc nhưng sai hoặc thiếu → **CHẶN**.
   - `KHÔNG CÓ` — cân nhắc: thiếu thật, hay thuộc chương khác? Nếu thuộc
     chương khác, kiểm xem đã có dẫn chiếu chưa.

3. **Cập nhật `tools/cau_hinh_kiem_tra.json`** mục `tieu_chuan_theo_chuong`
   nếu phát hiện chương cần thêm tiêu chuẩn — để lần sau máy tự nhắc.

4. **Kết luận:**

```
## Soi an toàn — Chương N

Nhóm áp dụng: A, B
| Tiêu chuẩn | Kết quả | Bằng chứng |
|---|---|---|
| ISO 12100 | CÓ, ĐÚNG | dòng 88–104 nêu đủ ba bước |
| IEC 60204-1 | CÓ, THIẾU | dòng 152 nói "dừng máy" không phân Category |

CHẶN: <danh sách>
Cần chuyên gia người thật duyệt: CÓ / KHÔNG
```

---

## Cờ chờ chuyên gia

Chương chạm **trực tiếp** tới thiết kế mạch an toàn (hiện tại: Ch.47, Ch.48)
phải mang cờ `⚠ chờ chuyên gia an toàn duyệt` trong `docs/00_Muc_luc.md` cho
tới khi có người thật có thẩm quyền xem. Bộ kiểm tra máy **không** gỡ được cờ
này, và skill này cũng không. Chỉ người dùng gỡ.
