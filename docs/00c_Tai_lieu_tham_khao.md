# Tài liệu tham khảo & nguồn học

> Hai mục đích: (1) mẫu ghi nguồn cuối mỗi chương — xem §0; (2) kho nguyên liệu cho **Phụ lục G**
> (phần mềm miễn phí & mô phỏng) và **Phụ lục H** (nguồn mở & đọc thêm).
>
> ⚠ **Trạng thái kiểm tra: 2026-08-28.** Chính sách license, giá và tình trạng sản phẩm của mọi
> mục dưới đây **đều thay đổi theo thời gian**. Trước khi đưa vào bản phát hành phải kiểm tra lại
> và ghi ngày kiểm tra (bất biến B10).

---

## §0 — Mẫu ghi nguồn ở cuối mỗi chương

```markdown
---
### Nguồn tham khảo chương N

- IEC 61131-3 — Programmable controllers, Part 3: Programming languages. *(tiêu chuẩn có bản quyền;
  nội dung chương chỉ diễn giải ở mức khái niệm, không thay thế bản gốc)*
- [Tên tài liệu hãng], số hiệu [xxx], mục [y.z] — dùng cho số liệu [gì cụ thể]
- [Tài liệu mở], giấy phép [CC BY / GNU FDL], mục [y] — dùng cho [gì]
```

Quy tắc: **mỗi số liệu, ngưỡng, công thức trong chương phải truy được về một dòng ở đây.**
Chỗ nào các hãng làm khác nhau thì ghi rõ đã đối chiếu những hãng nào (bất biến B2).

---

## §1 — Tài liệu mở đã tải về (dùng làm nguyên liệu viết)

Đã tải đầy đủ vào `../PLC/reference/`. Chỉ mục chi tiết + số trang: `../PLC/reference/00_INDEX.md`.

| Nhóm | Nội dung | Phục vụ chương |
|---|---|---|
| Giáo trình đo lường công nghiệp (CC BY, 3311 tr) | Vật lý/điện nền tảng, tài liệu đo lường, đo rời rạc & liên tục, chương PLC riêng, 4–20 mA, mạng số & Modbus, van điều khiển, PID, an toàn quá trình, an ninh mạng OT, **chiến lược chẩn đoán sự cố** | Phần I, V, VI, VII |
| Giáo trình PLC đại học (GNU FDL, 860 tr) | Phần cứng, cảm biến, cơ cấu chấp hành, Boolean & Karnaugh, **thiết kế logic có cấu trúc / lưu đồ / trạng thái**, 5 ngôn ngữ IEC, analog, truyền thông, fail-safe, kỹ nghệ phần mềm PLC, chọn PLC. Bài tập **có lời giải** | Phần II, III, **IV** |
| Bộ giáo trình mạch điện (5 tập, ~2350 tr) | DC, AC, bán dẫn, số, tra cứu | Ch.3 |
| Tài liệu ngôn ngữ IEC của một hãng lớn (9 quyển) | LD / ST / FBD / SFC tách bạch, **tài liệu riêng về mức độ tuân thủ IEC 61131-3**, task–program–routine, tag & UDT, mã lỗi | Ch.10–11, 14–21, 27, 51, Phụ lục A/B |
| Hướng dẫn an toàn máy của nhà sản xuất thiết bị an toàn (2 quyển, 298 tr) | Sáu bước tới máy an toàn, giới thiệu PL/SIL, chọn thiết bị bảo vệ quang điện, đối chiếu khung Bắc Mỹ | Ch.47, 48 |

> ⚠ Tài liệu hãng và hướng dẫn của nhà sản xuất **không phải bản gốc tiêu chuẩn**. ISO 13849-1,
> IEC 62061, IEC 61131-3, IEC 62443 đều có bản quyền và phải mua từ tổ chức phát hành.

---

## §2 — Tiêu chuẩn cần đối chiếu (phải mua bản gốc)

| Tiêu chuẩn | Nội dung | Chương dùng |
|---|---|---|
| IEC 61131-3 | Ngôn ngữ lập trình PLC (LD, ST, FBD, SFC, IL) | Ch.11, 14–21, Phụ lục A/B/N |
| IEC 61131-2 | Yêu cầu thiết bị & thử nghiệm (đặc tính ngõ vào/ra) | Ch.4, 5, 8, 9 |
| ISO 13849-1/-2 | An toàn máy — bộ phận liên quan an toàn của hệ điều khiển (PL, Category) | Ch.47 |
| IEC 62061 | An toàn máy — hệ điều khiển điện/điện tử lập trình (SIL) | Ch.47 |
| IEC 60204-1 | Trang bị điện của máy (dừng khẩn cấp, màu nút, nối đất) | Ch.3, 5, 47, 49 |
| ISO 12100 | Nguyên tắc chung thiết kế — đánh giá & giảm thiểu rủi ro | Ch.23, 47 |
| IEC 62443 | An ninh mạng hệ thống tự động hoá công nghiệp | Ch.45 |
| IEC 61784 / 61158 | Bus trường & mạng công nghiệp | Ch.39, 40 |

---

## §3 — Phần mềm & mô phỏng (nguyên liệu cho Phụ lục G)

> Phụ lục G phải trình bày dưới dạng bảng: **công cụ → làm được gì → giới hạn license thật →
> phù hợp giai đoạn học nào**, kèm ngày kiểm tra. Danh sách dưới đây là nguyên liệu thô, chưa xác
> minh lại điều kiện license.

### Môi trường lập trình có bản dùng được miễn phí

| Công cụ | Ghi chú thu thập từ nguồn (chưa xác minh lại) |
|---|---|
| CODESYS | Bản 3.5 dùng được miễn phí cho phát triển, có mô phỏng tích hợp; ghép được với phần mềm mô phỏng nhà máy 3D qua OPC. ⭐ Ứng viên mạnh nhất cho hệ "trung lập" vì là nền IEC 61131-3 nhiều hãng OEM dùng lại |
| Beckhoff TwinCAT | Tải miễn phí sau đăng ký; runtime chạy được ngay trên máy lập trình; hỗ trợ Git cho cấu trúc dự án |
| Rockwell Connected Components Workbench | Miễn phí; từ một phiên bản trở đi có kèm bộ mô phỏng PLC để chạy thử I/O |
| AutomationDirect Do-more Designer | Miễn phí, có emulator và nhiều tài liệu đào tạo kèm theo |
| OpenPLC | Mã nguồn mở, cả phần mềm lẫn phần cứng; chạy được trên máy tính nhúng giá rẻ |
| Horner Cscape | Miễn phí (cần tạo tài khoản); phần cứng PLC/HMI tích hợp giá thấp — hợp để học trên phần cứng thật thay vì mô phỏng |
| LS GMWIN (dòng GLOFA) | Miễn phí; hỗ trợ LD/IL/SFC |
| Phoenix Contact PLCnext Engineer | Phần mềm cơ bản + add-on mô phỏng cho một model controller cấp thấp là miễn phí; HMI nền web tích hợp sẵn trong PLC |

### HMI / SCADA có bản dùng thử hoặc miễn phí giới hạn

| Công cụ | Ghi chú |
|---|---|
| Ignition | Bản dùng thử đầy đủ chức năng, phải bấm gia hạn định kỳ. Có bản Maker Edition miễn phí cho học tập & dự án cá nhân |
| VTScada (VTScadaLight) | License 50 tag phát triển + runtime kèm đủ driver I/O, miễn phí |
| Red Lion Crimson | Miễn phí, có emulator ở một số phiên bản; ghép được với emulator PLC qua Modbus để có bộ PLC+HMI ảo trên máy bàn |
| IPESOFT D2000 | Bản Raspberry Pi miễn phí tới 50 tag; bản demo cho Windows/RPi không dùng thương mại |
| AdvancedHMI | Mã nguồn mở; phức tạp hơn giải pháp công nghiệp đóng gói |

### Mô phỏng & luyện tập

| Công cụ | Ghi chú |
|---|---|
| Phần mềm mô phỏng nhà máy 3D (sandbox) | Trả phí, có bản dùng thử; ghép được với nhiều hãng PLC. Có phiên bản giá thấp theo năm dành cho học viên, đi kèm một trình mô phỏng PLC |
| Trình soạn ladder chạy trên trình duyệt | Miễn phí; có sẵn khoá luyện bài tập (cổng logic, timer, counter, toán, so sánh, thanh ghi dịch) — hợp cho Phụ lục I |
| Bộ mô phỏng bài tập kinh điển (cửa gara, đèn giao thông, silo, băng tải, thang máy) | Phần mềm cũ, trả phí thấp; nhiều trường kỹ thuật dùng dạy. Nguồn ý tưởng cho **Phụ lục I** |

---

## §4 — Nguồn học trực tuyến & cộng đồng (nguyên liệu cho Ch.58)

| Loại | Ghi chú |
|---|---|
| Trung tâm hướng dẫn video của hãng | Siemens, Rockwell, AutomationDirect, Beckhoff đều có; miễn phí, chất lượng cao nhưng chỉ đúng hãng đó |
| Trang hướng dẫn PLC theo bài (blog kỹ thuật) | Nhiều trang có loạt bài từ cơ bản: ngõ vào/ra, vòng quét, NPN/PNP, timer/counter, HMI, các bài toán mẫu (trạm trộn, phân loại, palletizer). Nguồn ý tưởng bài tập |
| Cổng kiến thức tự động hoá có sách giáo khoa trực tuyến | Một trang lớn đã lấy giáo trình đo lường mở làm nền và mở rộng thêm; kèm diễn đàn PLC/mạng/điều khiển động cơ |
| Diễn đàn hỏi–đáp PLC lâu đời | Kho câu hỏi lớn, tìm kiếm được; không chỉ PLC mà cả SCADA và mạng công nghiệp |
| Diễn đàn hỗ trợ chính hãng | Của Siemens là ví dụ điển hình — nhiều câu hỏi đã có sẵn lời giải; giới hạn trong hệ sinh thái hãng đó |
| Kênh video kỹ thuật | Cộng đồng nhắc tới hơn 10 kênh: có kênh dạy khái niệm bằng hình ảnh, có kênh chuyên một hãng, có kênh của người trong nghề chia sẻ ca thực tế |
| Tổ chức nghề nghiệp | Hội tự động hoá quốc tế có chi hội theo vùng, sinh hoạt định kỳ — giá trị chính là **mạng lưới quan hệ** để có việc đầu tiên, không chỉ là chứng chỉ |
| Trường nghề / cao đẳng kỹ thuật địa phương | Được nhắc tới nhiều nhất như đường vào nghề rẻ và hiệu quả, đặc biệt chương trình cơ điện tử |

> 💡 **Ghi chú viết Ch.58:** cách trình bày nên là **bảng "mục tiêu học → loại nguồn phù hợp"**,
> không phải danh sách link. Link sẽ chết; tiêu chí chọn nguồn thì không.

---

## §5 — Sách thương mại nên biết

| Sách | Vì sao đáng nhắc |
|---|---|
| Petruzella — *Programmable Logic Controllers* | Giáo trình được dùng phổ biến ở trường kỹ thuật; cộng đồng khuyên mua bản cũ giá rẻ **kèm lab manual** và làm hết bài tập |
| Erickson — *Programmable Logic Controllers: An Emphasis on Design and Application* | Thiên về thiết kế & ứng dụng |
| *Programmable Logic Controllers: A Practical Approach to IEC 61131-3 using CoDeSys* (Wiley) | ⭐ Sát nhất với hướng trung lập hãng của dự án này — nên mua để đối chiếu cách tổ chức nội dung |

---

## §6 — Nguồn gốc yêu cầu dự án

Khung sách này được thiết kế từ **phân tích khoảng trống** trong một bài tổng hợp tài nguyên học PLC
của cộng đồng nghề (bản lưu 2025-03-28) cùng 96 bình luận, một luồng thảo luận riêng về giao thức
truyền thông công nghiệp, và trang wiki của cộng đồng đó. Toàn văn đã lưu ở
`../PLC/reference/05_Web_Snapshots/`.

Cách dùng nguồn này: **chỉ rút ra nhu cầu và khoảng trống** (người học vướng ở đâu, tài liệu hiện có
thiếu gì) để định hình cấu trúc sách. Không trích nguyên văn vào bản phát hành, không nêu tên tài
khoản người dùng. Bảng đối chiếu "quan sát → hệ quả lên cấu trúc" ở
`docs/design-notes/0001-cau-truc-sach-va-cac-phuong-an.md`.
