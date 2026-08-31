# CLAUDE.md — PLC Programming Book

> Sổ tay lập trình PLC & điều khiển máy tự động hoá. Tiếng Việt.
> Hướng dẫn dành cho Claude khi làm việc với dự án sách này.

## Đọc trước khi làm bất cứ việc gì

1. `PROJECT_STATUS.md` — trạng thái, chương nào xong/đang viết, việc kế tiếp
2. `CLAUDE.md` (file này) — quy ước viết, bất biến
3. `docs/00_Muc_luc.md` — khung mục lục đầy đủ (58 chương / 11 phụ lục) + trạng thái từng chương
4. `docs/case_study_may_mau.md` — hồ sơ máy mẫu **DP-01** dùng xuyên suốt từ Ch.8, kèm quy tắc bóc lớp
5. `docs/design-notes/0001-*.md` — vì sao sách chọn hướng trung lập hãng, các phương án đã loại
6. `docs/design-notes/0002-*.md` — ⭐ **5 quyết định đã chốt** (máy mẫu, bộ hãng, quy mô, song ngữ);
   thay thế phần "Điểm còn treo" của 0001

Tài liệu nguồn (không nằm trong repo này): `../PLC/reference/` — xem `../PLC/reference/00_INDEX.md`.

---

## Sách này là gì

Sổ tay cho người vào nghề tự động hoá: **lập trình PLC theo nguyên lý, không theo phần mềm của một
hãng**, kèm những phần mà tutorial online gần như luôn bỏ qua — thiết kế logic có cấu trúc, an toàn
máy, chạy thử, và **chẩn đoán sự cố ngoài hiện trường**.

**Mục tiêu bao trùm (chốt session 2):** người đọc **không phải đi tìm tài liệu khác** để làm xong một
cỗ máy — từ lúc nhận yêu cầu đến lúc bàn giao và bảo trì. Đây là lý do sách có 58 chương chứ không
phải 43: xem ADR 0002 §1 để hiểu ràng buộc mà mục tiêu này đặt lên cách viết.

**Đối tượng:** người mới đến ~3 năm kinh nghiệm, từ 3 xuất phát điểm (chuyển ngành không biết điện /
thợ điện đi lên / dân lập trình phần mềm sang). **Trọng tâm ngành: sản xuất điện tử.**
**Không phải:** sách lý thuyết điều khiển hàn lâm; không phải hướng dẫn sử dụng một phần mềm.

### Bộ hãng cho Phụ lục A — thứ tự ưu tiên đã chốt

| Cột | Hệ | Vai trò | Tài liệu nguồn |
|---|---|---|---|
| 1 | **Siemens** (TIA Portal) | Phổ biến nhất ở Việt Nam | `../PLC/plc s7-1200.pdf`, bộ 8 chương tiếng Việt |
| 2 | **Mitsubishi** (GX Works) | Phổ biến trong máy Nhật/Hàn | `../PLC/Huong dan lap trinh PLC Mitsubishi…pdf` |
| 3 | **Inovance** (AutoShop) | Phân khúc giá tốt, đang lên nhanh | `../PLC/Manual/` (đầy đủ) |
| 4 | **CODESYS** | ⭐ **Cột neo trung lập** — khi 4 hệ khác nhau thì cột này cho biết chuẩn IEC *nói* gì | `../PLC/en/` (đầy đủ) |
| 5 | **Rockwell** (Studio 5000) | Đối chiếu bổ sung — có tài liệu ngôn ngữ IEC tách bạch & công khai nhất | `../PLC/reference/03_Vendor_Manuals/` (11 quyển) |

> ⚡ Phụ lục A **mô tả khác biệt, không xếp hạng hãng**. Chỗ nào một hãng làm khác chuẩn thì ghi rõ là
> khác chuẩn — đó là dữ kiện cần biết khi chuyển hệ, không phải lời chê.

### ⭐ Sách này là dự án ĐỘC LẬP

Người đọc **không được yêu cầu mở bất kỳ tài liệu/sách nào khác** để hiểu hoặc áp dụng một chương.
Bản thảo **không nhắc tên bất kỳ sách/dự án nào khác** của tác giả. File nội bộ (`CLAUDE.md`,
`PROJECT_STATUS.md`, `docs/design-notes/`) vẫn được phép ghi chú quá trình làm việc — ranh giới:
**không dòng nào trong `docs/chNN_*.md` hay phụ lục phát hành được nhắc tên dự án/sách khác.**

---

## Bất biến — vi phạm là viết lại

| # | Quy tắc |
|---|---|
| **B1** | ⭐ **Trung lập hãng trong thân sách.** Không dạy click theo giao diện của bất kỳ phần mềm nào ở Ch.1–58. Khái niệm dạy theo IEC 61131-3. Mọi thứ phụ thuộc hãng → Phụ lục A. Mỗi lần định viết "ở phần mềm X bạn bấm…" trong thân sách là một lần vi phạm. |
| **B2** | **Không khẳng định suông về hành vi PLC.** Mọi phát biểu về vòng quét, thời gian, giới hạn lệnh, hành vi khi mất điện phải truy được về tài liệu hãng hoặc tiêu chuẩn — ghi nguồn ở cuối chương theo mẫu `docs/00c_Tai_lieu_tham_khao.md`. Chỗ nào các hãng khác nhau thì **nói rõ là khác nhau**, không chọn một hãng rồi phát biểu như chân lý chung. |
| **B3** | ⭐ **An toàn đi trước, và không có ngoại lệ "cho nhanh".** Chương nào chạm E-Stop, mạch an toàn, forcing I/O, online edit, hay điện áp nguy hiểm phải nêu rõ: cái gì KHÔNG được làm, tại sao, hậu quả. Tuyệt đối không đưa cách "đấu tắt", "bỏ qua interlock để test". |
| **B3b** | **Cảnh báo trách nhiệm pháp lý.** Chương an toàn (Ch.3, 6, 47, 48, 56, Phụ lục D) phải có dòng: nội dung là định hướng, không thay thế đánh giá rủi ro và kiểm định của người có thẩm quyền cho máy cụ thể. Giữ cờ ⚠/⚠⚠ trong mục lục cho tới khi có chuyên gia duyệt. |
| **B4** | **Giải thích SÂU, không liệt kê bảng chung chung.** Mỗi khái niệm phải trả lời được *vì sao lại thế* và *áp dụng thế nào*, không dừng ở "có 3 loại timer: TON, TOF, TP". Bảng chỉ để tra nhanh **sau khi** đã giải thích. |
| **B5** | **Mỗi bẫy là một mục có tên.** Những chỗ người mới sai (NPN/PNP, NC trong code vs NC vật lý, double coil, Modbus base-0/base-1, timer thay phản hồi, quên gỡ force) phải có mục riêng đặt tên rõ, không giấu trong đoạn văn. |
| **B6** | ⭐ **Tự đủ (self-contained) — ranh giới đã dịch ra xa, session 2.** Không viết "xem tài liệu khác" để né nội dung cần thiết. Nếu người đọc **cần** kiến thức đó để làm xong việc thì phải viết — kể cả khi nó không phải "kiến thức PLC" (khí nén, ESD, đo lực, tính chu kỳ…). Chỉ được lược khi nội dung thật sự thuộc **datasheet của một mã hàng cụ thể**; khi đó nêu nguyên tắc chung để người đọc tự tra, không dẫn chiếu sang nơi khác. |
| **B7** | **Sơ đồ tự vẽ SVG, khái quát hoá.** Mọi sơ đồ vẽ bằng SVG trong `assets/`. Không chụp/chép từ tài liệu hãng hay bản vẽ dự án thật. Ví dụ luôn dùng tên phiếm chỉ. |
| **B8** | ⭐ **Máy mẫu DP-01 xuyên suốt + quy tắc bóc lớp.** Mọi ví dụ từ Ch.8 trở đi dùng chung máy mẫu ở `docs/case_study_may_mau.md`, để Ch.57 ráp lại được thành một dự án hoàn chỉnh. **Chương thuộc lát cắt nào chỉ được nhắc thiết bị của lát cắt đó trở về trước** — Ch.15 (Ladder) không được lấy ví dụ về servo. Khi đổi số liệu máy mẫu: cập nhật file đó **trước**, rồi rà lại các chương đã dùng số cũ. |
| **B9** | **Code mẫu phải chạy được về mặt logic.** Đoạn LD/ST nào đưa vào sách phải tự kiểm: không double coil, không vòng lặp vô hạn, có xử lý điều kiện biên, có timeout cho mọi bước chờ, và chuyển tiếp bằng phản hồi chứ không bằng timer. |
| **B10** | **Thông tin có hạn sử dụng phải ghi ngày.** License phần mềm miễn phí, giá, tình trạng sản phẩm (Phụ lục G) — ghi rõ "kiểm tra ngày …" và cảnh báo người đọc tự xác nhận lại. |
| **B11** | ⭐ **Song ngữ thuật ngữ — siết session 5.** Thuật ngữ chuyên môn ghi **tiếng Việt trước, tiếng Anh trong ngoặc nghiêng**, ở **lần xuất hiện đầu tiên của mỗi chương**; sau đó dùng tiếng Việt. ⭐ **Tiêu chí là ĐỦ, không phải tiết chế:** nếu thiếu tiếng Anh khiến người đọc không tra cứu được hoặc không chắc đang nói về khái niệm nào, thì **phải ghi** — kể cả khi trông rườm. Thà thừa một cặp ngoặc còn hơn để người đọc đoán. Ví dụ: vòng quét *(scan cycle)*, tự giữ *(seal-in)*, khối chức năng *(function block, FB)*. **Giữ nguyên tiếng Anh, không dịch:** tên lệnh & từ khoá (`TON`, `CTU`, `MOVE`, `CASE`), tên chuẩn & giao thức (IEC 61131-3, Modbus TCP, PROFINET, EtherCAT, IO-Link), thuật ngữ đã thành tên riêng trong nghề (PLC, HMI, SCADA, MES, STO, LOTO, SMEMA), và tên tag trong code mẫu. Lý do đầy đủ: ADR 0002 §5. |
| **B12** | ⭐ **Không đặt trần số từ — sửa session 5.** Độ dài chương do **nội dung quyết định**, không do hạn mức. Viết đủ để người đọc làm được việc, rồi dừng. Điều bắt buộc không phải là ngắn, mà là **không loãng**: mỗi mục phải trả lời một câu hỏi thật. Mọi chương vẫn phải giữ khung cố định bên dưới, đặc biệt mục *Bẫy thường gặp* và *Tự kiểm* — chương mất hai mục đó coi như **chưa viết xong**. |
| **B13** | ⭐ **Hình phải tự vẽ, và chỉ vẽ khi hình nói được điều chữ không nói được — mới, session 5.** Mọi hình là **SVG tự vẽ** trong `assets/chNN/`, nhãn tiếng Việt, theo bộ token thị giác ở mục "Quy ước hình" bên dưới. ⚠ **Tuyệt đối không tải hình từ tài liệu hãng, sách thương mại, hay web** — vi phạm bản quyền và phá vỡ tính nhất quán. Tiêu chí quyết định có vẽ hay không: *đường đi của dòng điện, quan hệ thời gian, cấu trúc không gian, và máy trạng thái* thì vẽ; *danh sách, so sánh, phân loại* thì dùng bảng. |
| **B14** | ⭐ **Bảng tổng hợp cho nội dung quan trọng — mới, session 5.** Mỗi khái niệm trọng tâm phải có **một bảng chốt lại** để người đọc tra sau này mà không phải đọc lại cả chương (ví dụ: bảng 4 tổ hợp NO/NC, bảng 4 tổ hợp PNP/NPN). Bảng đặt **sau** phần giải thích, không thay cho giải thích (B4). |

---

## Quy ước viết chương

> ⚡ **Mở chương bằng sự cố thật là TUỲ CHỌN — sửa session 5.** Cách mở này rất hiệu quả với những
> chương có một kiểu hỏng hóc kinh điển (vòng quét, ladder, cảm biến, chẩn đoán, an toàn). Nhưng
> **đừng ép mọi chương**: nhiều chương chỉ cần mở bằng *câu hỏi mà chương sẽ trả lời* hoặc *bối cảnh
> chương này nằm ở đâu trong công việc*. Mở bằng sự cố gượng ép còn tệ hơn mở thẳng.

### Khung cố định — chương "khái niệm/lệnh"

```
N.1  Mở chương — chọn MỘT trong ba cách:
       (a) một sự cố thật mà chương sẽ giải thích  ← dùng khi có kiểu hỏng kinh điển
       (b) câu hỏi thực tế mà chương trả lời
       (c) bối cảnh: chương này giải quyết khâu nào trong công việc
N.2  Khái niệm hoạt động thế nào — kèm hình/sơ đồ thời gian
N.3  Dùng trên máy mẫu DP-01 — ví dụ cụ thể, code có comment (đúng lát cắt của chương, B8)
N.4  Bẫy thường gặp — mỗi bẫy một tiểu mục có tên (B5)
N.5  Khác biệt giữa các hãng (nếu có) — nói rõ là khác, chi tiết ở Phụ lục A
N.6  Tự kiểm — "làm được gì thì coi là hiểu chương này"
```

### Khung cố định — chương "thiết kế" (Phần IV)

```
N.1  Vấn đề mà cách làm ngây thơ không giải được
N.2  Phương pháp — trình bày từng bước
N.3  Áp lên DP-01 — làm đầy đủ từ đầu tới cuối
N.4  Khi nào KHÔNG dùng phương pháp này
N.5  Sai lầm thường gặp
```

### Khung cố định — chương "chẩn đoán/an toàn" (Phần VII)

```
N.1  Nguyên tắc (vì sao làm theo thứ tự này)
N.2  Quy trình từng bước
N.3  Bảng triệu chứng → nguyên nhân khả dĩ → phép kiểm xác nhận
N.4  ⚠ Cái gì tuyệt đối không làm
N.5  Khi nào dừng lại và gọi người khác
```

### Cảnh báo trong bài
- `> ⚠ **NGUY HIỂM**` — sai là hỏng thiết bị / điện giật / máy chạy bất ngờ / thương tích
- `> ⚡ **LƯU Ý**` — sai là không chạy được hoặc không đạt chuẩn, nhưng không gây nguy hiểm
- `> 💡 **MẸO**` — kinh nghiệm thực tế
- `> 🔍 **BẪY**` — chỗ người mới sai nhiều nhất (B5)

---

## Quy ước hình — bộ token thị giác dùng chung cả 58 chương

Hình sinh bằng script Python trong `tools/`, **không vẽ tay từng file** — nhờ vậy 58 chương giữ được
một ngôn ngữ thị giác duy nhất và sửa token là sửa toàn bộ.

```
tools/sinh_hinh.py        — bộ khung dùng chung (esc/T/R/L/head/save) + các hình đa chương
tools/sinh_hinh_ch04.py   — hình chuyên biệt của Ch.4 (bốn tổ hợp đấu nối)
assets/chNN/hinh_NN_k_ten.svg
```

### Bảng màu (không đổi giữa các chương)

| Token | Mã | Dùng cho |
|---|---|---|
| `INK` | `#1A1D21` | Nét chính, dây dẫn, chữ tiêu đề |
| `INK2` | `#565E66` | Chữ phụ, nhãn |
| `RULE` | `#9AA3AB` | Đường phụ trợ, ray nguồn, lưới |
| `CUR` | `#C0392B` | ⭐ **Đường dòng điện / tín hiệu đang hoạt động** |
| `OK` | `#2E7D4F` | Cách làm đúng |
| `BAD` | `#B03A2E` | Cách làm sai, chỗ mạch đứt |
| `WARN` | `#B8860B` | Cảnh báo, khối ghi chú |
| `PANEL` | `#F4F5F7` | Nền hộp thiết bị |
| `BG` | `#FFFFFF` | Nền hình — **luôn trắng**, để in được |

### Quy ước hình học

- `viewBox` rộng **900**, cao tuỳ nội dung. Chữ nhỏ nhất **9.5 px**, chữ nhãn **10–11 px**, tiêu đề **16 px**.
- Nét: cấu trúc `1.4–1.6`, dây `2`, **đường dòng điện `2.8`**.
- Mỗi hình **tự mang tiêu đề và một dòng giải thích** ở đầu — hình phải đọc được khi tách khỏi sách.
- Trong file `.md`, hình đi kèm **một dòng chú thích in nghiêng** bên dưới, dạng `*Hình N.k — …*`.

### Bắt buộc kiểm trước khi coi là xong

| Kiểm | Cách |
|---|---|
| XML hợp lệ | `ET.parse(path)` — script `save()` đã tự làm |
| ⚠ **Escape `&`** | Ký tự `&` trong chữ phải thành `&amp;`, nếu không XML hỏng. Hàm `esc()` lo việc này |
| Nhãn không đè nhau, không tràn khung | **Render ra PNG rồi nhìn bằng mắt** — `pymupdf.open(svg)[0].get_pixmap(dpi=110).save(...)`. Không bỏ bước này |

---

## Đọc nguồn PDF — dùng đúng công cụ

Tài liệu nguồn ở `../PLC/reference/` (xem `00_INDEX.md` ở đó). Công cụ đã kiểm chứng có sẵn:
`pymupdf` (nhanh, lấy bookmark/TOC tốt), `pdfplumber` (bảng nhiều cột — dùng `extract_text(layout=True)`),
`pypdf`. **Không** dùng `pypdf` cho bảng (trộn cột).

> ⚠ Trên máy này, `print()` tiếng Việt/ký tự đặc biệt ra console bị lỗi codec `gbk`.
> Luôn ghi ra file với `encoding='utf-8'` rồi `grep`/`sed` đọc lại, đừng in thẳng.

File `.chm` (Inovance AutoShop, CODESYS) chưa có công cụ đọc trong pipeline — nếu cần, giải nén bằng
`7z` rồi đọc HTML bên trong.

---

## Bản quyền — nói thẳng

| Loại nội dung | Trạng thái |
|---|---|
| Chữ và toàn bộ sơ đồ SVG tự vẽ | Của tác giả |
| Trích công thức/nguyên lý từ tài liệu mở (giấy phép CC / GNU FDL) | Trích dẫn có ghi nguồn + giấy phép |
| Trích từ tài liệu hãng (Rockwell/Siemens/CODESYS/Inovance) | Chỉ trích ở mức nguyên lý & số liệu tra cứu, ghi rõ số hiệu tài liệu; **không** sao chép nguyên trang/hình |
| Nội dung tiêu chuẩn (ISO 13849, IEC 61131-3, IEC 62443…) | Diễn giải ở mức khái niệm, ghi rõ **không thay thế bản gốc**; không chép bảng gốc |
| Thảo luận cộng đồng dùng làm đầu vào thiết kế | Chỉ rút ra *nhu cầu và khoảng trống*, viết lại hoàn toàn bằng ngôn ngữ của mình; không trích nguyên văn, không nêu tên tài khoản người dùng |

Giấy phép phát hành cuối cùng — **chưa chốt**, xem `PROJECT_STATUS.md`.

---

## Cuối mỗi session

```
1. Cập nhật PROJECT_STATUS.md — chương/phần nào xong, việc kế tiếp
2. Thêm entry CHANGELOG.md — file nào thay đổi, vì sao
3. git commit (repo riêng, local)
```
