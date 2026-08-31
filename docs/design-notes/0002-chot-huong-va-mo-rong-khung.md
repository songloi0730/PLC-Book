# 0002 — Chốt 5 quyết định & mở rộng khung sách

- **Ngày:** 2026-08-29
- **Trạng thái:** ✅ Đã chốt bởi chủ dự án — thay thế phần "Điểm còn treo" của ADR 0001
- **Phạm vi:** hướng đi, máy mẫu, bộ hãng, quy mô sách, ngôn ngữ

---

## Tóm tắt quyết định

| # | Câu hỏi (ADR 0001) | Quyết định | Hệ quả |
|---|---|---|---|
| 1 | A+C hay B? | ✅ **Giữ A+C** — trung lập hãng + máy mẫu xuyên suốt | Bất biến B1 giữ nguyên; Phụ lục A tồn tại |
| 2 | Máy mẫu PS-01? | ❌ **Đổi** — ưu tiên máy thuộc **lĩnh vực điện tử** | PS-01 bị loại, thay bằng **DP-01** (xem §2) |
| 3 | Bộ hãng cho Phụ lục A? | ✅ **Siemens · Mitsubishi · Inovance** làm chính, **CODESYS** làm nền trung lập, **Rockwell** giữ làm đối chiếu bổ sung | Phụ lục A từ 3 cột → **5 cột** (xem §3) |
| 4 | 43 chương có dài quá? | ❌ **Không** — càng chi tiết, đầy đủ, toàn diện càng tốt, để người đọc **không phải tìm tài liệu khác** | Mở rộng **43 → 58 chương**, **9 → 11 phụ lục** (xem §4) |
| 5 | Ngôn ngữ? | ✅ **Song ngữ cho thuật ngữ chung** | Bất biến mới **B11** (xem §5) |

---

## §1 — Vì sao quyết định #4 là quyết định quan trọng nhất

Ba quyết định đầu chỉ đổi *nội dung*. Quyết định #4 đổi *bản chất cuốn sách*: từ "sách nhập môn có
chiều sâu" thành **sách tra cứu tự đủ cho cả vòng đời một máy**. Điều này siết chặt chứ không nới
lỏng kỷ luật viết:

- Bất biến **B6 (tự đủ)** trước đây cho phép "lược bỏ chi tiết vượt phạm vi". Nay ranh giới dịch ra
  xa hơn: nếu người đọc **cần** kiến thức đó để làm xong việc, phải viết — chỉ được lược khi nội dung
  thật sự thuộc về datasheet của một mã hàng cụ thể.
- Nguy cơ mới: **sách phình mà loãng**. Chống bằng cách giữ nguyên khung chương cố định trong
  `CLAUDE.md` — mỗi chương vẫn phải có mục "bẫy thường gặp" và "tự kiểm", không được biến thành
  bài giảng dàn trải.
- Nguy cơ thứ hai: **bỏ dở giữa chừng**. Chống bằng thứ tự viết theo đợt trong `PROJECT_STATUS.md`
  — sau 3 đợt đầu đã có sản phẩm dùng được kể cả nếu dừng.

---

## §2 — Máy mẫu mới: DP-01

### Vì sao bỏ PS-01

PS-01 (trạm khoan & phân loại phôi) là máy **gia công cơ khí**. Nó dạy đủ kỹ năng PLC cơ bản nhưng
không chạm được những thứ đặc trưng và bắt buộc của sản xuất điện tử: truy xuất nguồn gốc từng board,
ghép nối trong dây chuyền, ESD, công thức sản phẩm theo mã hàng, tích hợp vision.

### Các phương án máy điện tử đã cân nhắc

| Phương án | Dạy tốt | Yếu ở |
|---|---|---|
| **A. Trạm tra keo & sấy UV trên chuyền board mạch** | Chuyền + bắt tay máy-máy, chặn/nâng/kẹp board, đọc mã 2D & MES, gantry XY + trục Z, analog (áp keo, chân không, nhiệt), PID (gia nhiệt keo), **2 trạm nối tiếp → dạy được pipeline & song song**, đèn UV cho mối nguy an toàn *có lý do thật* | Phức tạp — phải thiết kế để chương đầu chỉ dùng một lát cắt |
| **B. Trạm ép vít tự động cho cụm điện tử** | Giám sát lực/mô-men, đường cong siết, trục Z | Ít analog, ít mạng, không có bài toán song song |
| **C. Trạm kiểm tra chức năng (FCT) & phân loại** | Giao tiếp với máy đo qua serial/TCP, phân loại, truy xuất | Rất ít chuyển động — mất gần hết Phần V |
| **D. Máy tách board (depaneling) & phân loại** | Chuyển động nhiều, vision căn chỉnh, hút bụi | Trùng nhiều với PS-01 cũ về bản chất (gia công + phân loại) |

### Phương án chọn: **A — DP-01**

**DP-01 · Trạm tra keo & sấy UV trên chuyền board mạch**
*(Dispensing & UV-cure station on a PCB conveyor line)*

Lý do: A là phương án duy nhất chạm được **cả bảy** nhóm kỹ năng sách cần dạy (rời rạc, tuần tự,
analog, PID, chuyển động, mạng & truy xuất, an toàn) **và** có sẵn một mối nguy vật lý thật (bức xạ
UV) để chương an toàn không phải nói lý thuyết suông.

Điểm thiết kế quan trọng: DP-01 gồm **hai trạm nối tiếp trong cùng một máy** (tra keo → sấy UV).
Nhờ vậy dạy được thứ máy một trạm không dạy nổi:

- **Ch.25 (máy trạng thái):** mỗi trạm có máy trạng thái riêng + một máy trạng thái tổng của máy.
- **Ch.26–27 (trình tự & kiến trúc):** hai trạm chạy **song song** trên hai board khác nhau —
  bài toán pipeline thật, không phải ví dụ giả định.
- **Ch.28 (phục hồi):** dừng khi board A đang ở trạm keo và board B đang ở trạm UV — phải xử lý cả hai.

Để chương đầu không bị ngợp, DP-01 được **bóc lớp dần**: Phần II–III chỉ dùng chuyền + chặn + kẹp +
cảm biến (thuần rời rạc); Phần V mới thêm analog & trục; Phần VI mới thêm mã 2D, MES, bắt tay chuyền;
Phần VII mới thêm mạch an toàn đầy đủ.

> ⚠ DP-01 là máy **phiếm chỉ**, dựng riêng để dạy học. Không dựa trên máy/dự án/khách hàng cụ thể nào.
> Hồ sơ đầy đủ: `docs/case_study_may_mau.md`.

---

## §3 — Phụ lục A: 5 hệ thay vì 3

Thứ tự cột phản ánh mức ưu tiên chủ dự án đã nêu:

| Cột | Hệ | Vai trò trong phụ lục | Tài liệu nguồn đã có |
|---|---|---|---|
| 1 | **Siemens** (TIA Portal) | Phổ biến nhất ở Việt Nam; là hệ nhiều người đọc gặp đầu tiên | `PLC/plc s7-1200.pdf`, bộ 8 chương tiếng Việt, `Học tia portal.docx` |
| 2 | **Mitsubishi** (GX Works) | Rất phổ biến trong máy Nhật/Hàn tại Việt Nam | `PLC/Huong dan lap trinh PLC Mitsubishi…pdf` |
| 3 | **Inovance** (AutoShop) | Đang lên nhanh ở phân khúc giá tốt | `PLC/Manual/` — AutoShop CHM + H1U/H2U/H3U + H5U&Easy (đầy đủ) |
| 4 | **CODESYS** | ⭐ **Cột neo trung lập** — là nền IEC 61131-3 mà nhiều hãng OEM dùng lại; khi 4 hệ khác nhau thì CODESYS cho biết chuẩn *nói* gì | `PLC/en/` — User Manual, Command Manual, Motion Control, SoftMotion (đầy đủ) |
| 5 | **Rockwell** (Studio 5000) | Đối chiếu bổ sung; giữ vì đây là hệ **có tài liệu ngôn ngữ IEC tách bạch và công khai nhất** — đặc biệt quyển riêng về mức độ tuân thủ IEC 61131-3 | `PLC/reference/03_Vendor_Manuals/` — 11 quyển đã tải |

**Hệ quả:** Phụ lục A nặng hơn hẳn dự kiến ban đầu. Vì vậy nó được tách thành **A1 (đối chiếu khái
niệm)** và **A2 (đối chiếu lệnh + cùng một đoạn logic DP-01 viết 5 lần)**, và vẫn chỉ viết sau khi
thân sách ổn định.

> ⚡ Rủi ro cần canh: 5 cột dễ khiến người viết trượt vào so sánh hãng nào hơn hãng nào. Phụ lục A
> **mô tả khác biệt, không xếp hạng**. Chỗ nào một hãng làm khác chuẩn thì ghi rõ là khác chuẩn —
> đó là dữ kiện, không phải chê.

---

## §4 — Mở rộng khung: 43 → 58 chương, 9 → 11 phụ lục

15 chương mới, chọn theo đúng tiêu chí chủ dự án đặt ra: **thứ người đọc sẽ phải đi tìm tài liệu khác
nếu sách không có**.

| Chương mới | Thuộc phần | Vì sao bắt buộc phải có |
|---|---|---|
| Khí nén cho máy tự động hoá | I | Gần như mọi máy lắp ráp đều dùng khí nén; không có chương này người đọc phải tra sách khác ngay từ Ch.5 |
| **ESD & môi trường sản xuất điện tử** | I | ⭐ Đặc thù bắt buộc của lĩnh vực điện tử — board hỏng vô hình, không có triệu chứng tại chỗ. Bỏ qua là sách không dùng được cho ngành này |
| IO-Link & lớp cảm biến thông minh | II | Đang thay dần đấu nối rời rạc/analog truyền thống; người mới sẽ gặp trong máy mới |
| Kiến trúc chương trình cho máy nhiều trạm | IV | Máy thật hiếm khi một trạm; đây là chỗ code người mới sụp đổ khi máy lớn lên |
| Công thức sản phẩm (recipe) & tham số | IV | Điện tử = nhiều mã hàng trên cùng một máy. Không có recipe thì phải sửa code mỗi lần đổi hàng |
| Cân & đo lực (load cell), giám sát lực/mô-men | V | Lắp ráp điện tử kiểm chất lượng bằng đường cong lực, không chỉ bằng cảm biến ON/OFF |
| Điều khiển chuyển động servo (tách khỏi chương động cơ) | V | Nội dung quá lớn để ghép chung; nhiều trục phối hợp cần chương riêng |
| Ghép nối máy-máy trong dây chuyền | VI | ⭐ Máy điện tử gần như luôn nằm trong chuyền — bắt tay, tắc chuyền, khởi động lại chuyền |
| Mã vạch/2D code & truy xuất nguồn gốc | VI | ⭐ Bắt buộc trong sản xuất điện tử; gồm cả xử lý khi mất kết nối MES |
| Tích hợp vision với PLC | VI | Rất phổ biến trong điện tử; người đọc cần biết ranh giới PLC ↔ hệ vision |
| Tích hợp robot & tay gắp | VI | Ai chỉ huy ai, vùng an toàn chung — câu hỏi thực tế thường gặp |
| Mô phỏng & kiểm thử trước khi ra hiện trường | VII | Lỗi tìm ở bàn rẻ hơn tìm ở hiện trường nhiều lần; kỹ năng này không sách nào dạy |
| Sao lưu, phiên bản & bảo mật chương trình | VII | Mất chương trình PLC là thảm hoạ có thật; khoá chương trình có đánh đổi cần nói rõ |
| Tính chu kỳ máy & năng suất | VIII | Câu hỏi khách hàng luôn hỏi: máy chạy được bao nhiêu sản phẩm/giờ |
| Nâng cấp máy cũ (retrofit) | VIII | Phần lớn công việc thực tế là sửa máy cũ không tài liệu, không phải làm máy mới |

Hai phụ lục mới: **J** (hồ sơ máy mẫu DP-01 đầy đủ để ráp lại) và **K** (bảng tra công thức tổng hợp).

---

## §5 — Bất biến mới B11: song ngữ thuật ngữ

**Quy tắc:** thuật ngữ chuyên môn ghi **tiếng Việt trước, tiếng Anh trong ngoặc, ở lần xuất hiện đầu
tiên của mỗi chương** — sau đó dùng tiếng Việt.

```
✅ vòng quét (scan cycle)          ✅ bắt cạnh lên (rising edge)
✅ tự giữ (seal-in / latch)        ✅ khối chức năng (function block, FB)
```

**Ngoại lệ — giữ nguyên tiếng Anh, không dịch:**

| Loại | Ví dụ | Lý do |
|---|---|---|
| Tên lệnh & từ khoá | `TON`, `CTU`, `MOVE`, `CASE` | Là ký hiệu trong phần mềm, dịch ra sẽ không tra được |
| Tên chuẩn & giao thức | IEC 61131-3, Modbus TCP, PROFINET, EtherCAT, IO-Link | Danh từ riêng |
| Thuật ngữ đã thành tên riêng trong nghề | STO, LOTO, SMEMA, HMI, SCADA, MES, PLC | Dịch ra gây khó hiểu hơn |
| Tên tag trong code mẫu | `DI_PartPresent` | Code phải chạy được, không dịch |

**Vì sao:** toàn bộ tài liệu hãng, thông báo lỗi trên phần mềm, và diễn đàn nghề đều bằng tiếng Anh.
Người đọc chỉ biết thuật ngữ tiếng Việt sẽ **không tra cứu được** khi gặp sự cố — đúng lúc cần tra
nhất. Phụ lục F là bảng đối chiếu đầy đủ; B11 bảo đảm người đọc không phải lật phụ lục liên tục.

---

## Hệ quả tổng hợp — việc phải làm ngay

| Việc | Trạng thái |
|---|---|
| Viết lại `docs/case_study_may_mau.md` cho DP-01 | ✅ xong session 2 |
| Mở rộng `docs/00_Muc_luc.md` lên 58 chương / 11 phụ lục, áp B11 | ✅ xong session 2 |
| Thêm B11 và cập nhật danh sách hãng trong `CLAUDE.md` | ✅ xong session 2 |
| Cập nhật `PROJECT_STATUS.md` — gỡ chặn, sửa thứ tự viết theo khung mới | ✅ xong session 2 |
| Bổ sung tài liệu nguồn Siemens & Mitsubishi chính hãng vào `../PLC/reference/` | 🟨 đang làm |
| ADR 0001 mục "Điểm còn treo" — đánh dấu đã được ADR này thay thế | ✅ xong session 2 |
