# 0005 — Kế hoạch hoàn thiện: tổ chức chương trình, cấu trúc mã, cách thực hiện lệnh, mã mẫu

**Trạng thái:** ✅ **ĐÃ DUYỆT** — chủ dự án chọn phương án đề xuất ở cả bốn câu hỏi, và *"làm hết 5 đợt theo thứ tự"*. ✅ **Cả 5 đợt xong** — đợt 58 ngày 2026-09-26, đợt 62 (cuối) ngày 2026-09-28 (mục 6).
**Ngày:** 2026-09-23
**Phạm vi:** bốn trục chủ dự án chỉ định — tổ chức chương trình · cấu trúc mã lệnh · cách thực hiện
lệnh · các đoạn mã ví dụ.

---

## 1. Bối cảnh — đo trước, không đọc lại

⭐ Theo đúng bài học của các đợt 48–57: **đo** hiện trạng bằng script trên toàn bộ 72 tệp, không đọc
lại từng chương.

### 1.1 Mã mẫu

| Chỉ số | Giá trị | Nhận xét |
|---|---|---|
| Khối ST (`iecst`) | **192** · 2289 dòng · TB 11,9 dòng/khối | |
| Khối ladder / sơ đồ (`text`) | **208** | |
| ⚠⚠ Khối ST **không khai báo biến** | **153 / 192 = 79 %** | Người đọc **không chép vào phần mềm thật được** — phải tự đoán kiểu |
| ⚠⚠ POU **hoàn chỉnh** trong cả sách | **3** `FUNCTION_BLOCK` · **1** `FUNCTION` · **1** `PROGRAM` | Quá ít cho một cuốn có Ch.27 và Ch.30 về kiến trúc và tái sử dụng |
| Khối ST ≤ 3 dòng | 34 | Đoạn trích — chấp nhận được nếu có quy ước |
| ✔ Phong cách | `//` 178/192 · thụt 4 dấu cách · `END_IF;` · `TRUE` · `T#` | ⭐ **Đã nhất quán** — chỉ thiếu **văn bản quy ước** |

### 1.2 Tổ chức chương trình — khái niệm IEC 61131-3

| Nhóm | Số lần xuất hiện |
|---|---|
| `PROGRAM` · `FUNCTION_BLOCK` · `FUNCTION` | 4 · 5 · 6 — ⚠ mỏng |
| `VAR_INPUT/OUTPUT/IN_OUT/TEMP` · `RETAIN` · `STRUCT` | 7–17 — đủ |
| ⚠ `VAR_EXTERNAL` | **0** |
| ⚠⚠ **Phần hướng đối tượng của bản 3 (2013)**: `METHOD` · `PROPERTY` · `INTERFACE` · `EXTENDS` · `IMPLEMENTS` · `REFERENCE` · `FB_init` | **0 · 0 · 0 · 0 · 0 · 0 · 0** |
| ⚠ **Mô hình giao diện khối `Execute` / `Enable`** | Sách **dùng** ở Ch.37–44 (khối của hãng) nhưng **Ch.27 và Ch.30 không dạy** người đọc thiết kế khối của chính mình theo mô hình đó |

> ⚠⚠ **Khoảng trống hướng đối tượng đặc biệt đáng chú ý vì sách lấy CODESYS làm cột neo ở Phụ lục
> A** — mà CODESYS và các hệ dựa trên nó (InoProShop của Inovance, Machine Expert, TwinCAT) hỗ trợ
> đầy đủ phần này.

### 1.3 Cách thực hiện lệnh

| Nhóm | Hiện trạng |
|---|---|
| `TON` `TOF` `TP` `CTU` `CTD` `R_TRIG` | ✔ Đủ; Ch.17 có Hình 17.1 sơ đồ thời gian |
| Làm tròn khi ép kiểu | ✔ Có, cả bẫy làm tròn về số chẵn của một hãng (Ch.19) |
| ⚠ `MUX` · `MIN` · `MAX` · `SQRT` · `MOD` · `SHL` · `SHR` · `ROL` · `ROR` | 1–2 lần mỗi lệnh — mỏng |
| ⚠⚠ **Hàm chuỗi** `LEN` `LEFT` `MID` `CONCAT` `FIND` | **0** — trong khi Ch.42 (mã vạch, mã 2D) nói "chuỗi" 9 lần mà **không có một khai báo `STRING` nào** |
| ⚠ **Hành vi ở vòng quét đầu**: `R_TRIG` khi ngõ vào đã TRUE lúc cấp điện | **0** — bẫy thật (công tắc Auto giữ nguyên → một cạnh giả → khởi động ngoài ý muốn) |
| ⚠ Chỉ số chuỗi bắt đầu từ 1 | **0** |
| Phụ lục B (tra nhanh lệnh) | 333 dòng, **không có sơ đồ thời gian** nào |

### 1.4 Việc tồn đọng phát hiện khi đo

⚠ `PROJECT_STATUS.md` vẫn ghi *"18/58 chương, session 8, 31/08"* — **cũ ba tuần**, trong khi sách đã
đủ 58 chương + 14 phụ lục qua 57 đợt rà. Nhật ký đối chiếu (`00d_`) được cập nhật đều, còn tệp trạng
thái thì không.

---

## 2. Nguồn — kho hiện có không đủ cho hai mảng

| Mảng | Kho hiện có | Kết luận |
|---|---|---|
| Hàm chuỗi | ✔ Rockwell 1756-RM003 (`CONCAT` `MID` `FIND` `STOD`…), Inovance (`ASCI` `HEX` `DABIN` `BINDA`) | **Đủ** |
| Mô hình `Execute`/`Enable` | ⚠ Chỉ gián tiếp qua đặc tả PLCopen Motion | **Thiếu** |
| Quy ước viết mã | ⚠ Siemens Styleguide (một hãng); **không có** bộ quy tắc trung lập | **Thiếu** |
| ⚠⚠ Hướng đối tượng | ❌ InoProShop chỉ có `STRUCT … EXTENDS`; Hanssen **0** | **Thiếu hoàn toàn** |

### 2.1 Đề xuất tải — bốn tài liệu miễn phí, chính thức của PLCopen

⭐ Cả bốn thuộc bộ **"Software Construction Guidelines"** của PLCopen, tải từ `plcopen.org`, và đặt
vào `../PLC/reference/08_Open_Specs/` cạnh các đặc tả PLCopen đã có.

| # | Tệp | Dung lượng | Dùng cho |
|---|---|---|---|
| 1 | `PLCopen_Coding_Guidelines_version_1.0.pdf` *(2016)* | máy chủ không báo trước | ⭐⭐ **63 quy tắc**: đặt tên · chú thích · thực hành viết mã · ngôn ngữ · phần mở rộng riêng của hãng |
| 2 | `Creating_PLCopen_compliant_Function_Block_libraries.pdf` *(2017)* | 537 KB | ⭐⭐ Mô hình **`Execute`** và **`Enable`** cho giao diện khối |
| 3 | `PLCopen_OOP_Guidelines.pdf` *(2021)* | 80 KB | ⭐⭐ Hướng đối tượng theo bản 3 |
| 4 | `plcopen_structuring_with_sfc.pdf` *(2018)* | 186 KB | SFC — nên và không nên |

⭐ Kèm **đọc (không tải)** trợ giúp trực tuyến của CODESYS về `METHOD`, `INTERFACE`, `EXTENDS`,
`FB_init` để đối chiếu cú pháp cụ thể.

---

## 3. Bốn quyết định có nhiều cách làm — và đề xuất

### 3.1 Đặt nội dung hướng đối tượng ở đâu

| Phương án | Ưu | Nhược |
|---|---|---|
| **A.** Mục mới trong **Ch.14** (tổng quan IEC) | Đúng chỗ về mặt ngôn ngữ | ⚠ Ch.14 thuộc lát cắt 1 — quá sớm cho người đọc; vi phạm tinh thần bóc lớp B8 |
| ⭐ **B.** Mục mới trong **Ch.30** (chuẩn hoá & tái sử dụng) + một câu trỏ từ Ch.14 | ⭐ Động cơ của hướng đối tượng **chính là** tái sử dụng — đúng mạch của Ch.30; lát cắt 2 hợp độ khó | Ch.30 đã dài nhất sách (≈ 900 dòng) |
| **C.** Phụ lục riêng | Không làm phình chương | ⚠ Tách khỏi lý do dùng — người đọc học cú pháp mà không biết khi nào nên |

⭐ **Đề xuất B.** Và theo bất biến B18, mục đó phải có **bảng so sánh cùng một bài toán giải ba cách**:
khối thuần có ngõ vào chọn chế độ · khối có phương thức · nhiều khối riêng — kèm ⚠ **hệ nào hỗ trợ**,
vì dự án thật dùng Mitsubishi hay Siemens đời cũ sẽ không dùng được phần này.

### 3.2 Xử lý 153 khối ST không khai báo biến

| Phương án | Ưu | Nhược |
|---|---|---|
| **A.** Thêm `VAR` vào cả 153 khối | Chép chạy được ngay | ⚠⚠ Phình ~1500 dòng; khai báo lặp lại vô nghĩa ở khối 3 dòng; **che mất ý chính** của đoạn trích |
| ⭐ **B.** **Quy ước tường minh** *(khối ngắn là đoạn trích; tag theo Phụ lục J)* + ⭐ **mỗi chương trọng tâm có ÍT NHẤT MỘT ví dụ hoàn chỉnh chép chạy được** | Giữ đoạn trích gọn; người đọc biết chỗ nào chép được | Phải chọn đúng ví dụ nào làm bản hoàn chỉnh |
| **C.** Dự án đi kèm biên dịch được *(tệp dự án hoặc PLCopen XML)* | ⭐ Mạnh nhất — mọi ví dụ được **chứng minh** biên dịch | ⚠ Khối lượng lớn; phụ thuộc phần mềm của một hãng |

⭐ **Đề xuất B ngay, C để sau** khi B xong.

### 3.3 Quy ước viết mã đặt ở đâu

| Phương án | Ưu | Nhược |
|---|---|---|
| ⭐ **A.** **Phụ lục N mới** — *"Quy ước viết mã"*, rút từ 63 quy tắc PLCopen, đối chiếu với quy ước sách đang dùng | Tra cứu được; người đọc mang đi dùng cho đơn vị mình | Thêm một phụ lục |
| **B.** Mở rộng Ch.30 mục 30.2 | Gần chỗ bàn về đặt tên | Ch.30 đã rất dài |
| **C.** Chỉ ghi vào `CLAUDE.md` | Rẻ | ⚠ Chỉ người viết thấy, người đọc không |

⭐ **Đề xuất A**, kèm một bất biến mới trong `CLAUDE.md` để người viết giữ đúng.

### 3.4 Kiểm cú pháp mã mẫu

⚠ Hiện **năm bộ kiểm không bộ nào đọc chính mã ST** — trong khi mã mẫu là phần người đọc chép nhiều
nhất.

| Phương án | Ưu | Nhược |
|---|---|---|
| ⭐ **A.** Bộ kiểm thứ sáu bằng Python: cân `IF/END_IF`, `CASE/END_CASE`, `FOR/END_FOR`, ngoặc; bắt `=` dùng nhầm thay `:=`; biến dùng mà không khai báo **trong các khối tự nhận là hoàn chỉnh** | Không cần cài gì; chạy trong `gop_sach.sh` | Không bắt được lỗi kiểu dữ liệu |
| **B.** Cài trình biên dịch ST mã nguồn mở để **biên dịch thật** các ví dụ hoàn chỉnh | ⭐⭐ Chứng minh được | ⚠ Phải tải và cài phần mềm — cần duyệt riêng; phương ngữ có thể lệch |
| **C.** Không kiểm | — | Lỗi cú pháp lọt ra ngoài |

⭐ **Đề xuất A ngay; B là lựa chọn sau, cần duyệt riêng.**

---

## 4. Kế hoạch theo đợt

| Đợt | Nội dung | Tệp chính | Thành công = gì |
|---|---|---|---|
| ⭐ **58 — nền** | Tải và đọc 4 tài liệu · **Phụ lục N** quy ước viết mã · **bộ kiểm cú pháp ST** (thứ 6) · cập nhật `PROJECT_STATUS.md` | `pl_n_*` · `tools/kiem_cu_phap_st.py` · `PROJECT_STATUS.md` | Bộ kiểm chạy sạch trên 192 khối, **đã thử bằng lỗi giả**; Phụ lục N dẫn nguồn từng quy tắc |
| **59 — tổ chức chương trình** | ⭐⭐ Mô hình **`Execute` / `Enable`** cho khối tự viết · phạm vi biến (`VAR_GLOBAL` / `VAR_EXTERNAL` và vì sao hạn chế toàn cục) · **khung POU chuẩn** cho FB / FUNCTION / PROGRAM | Ch.27, Ch.30, Phụ lục L | Người đọc thiết kế được khối **theo cùng mô hình với khối của hãng** |
| **60 — hướng đối tượng** | `METHOD` · `PROPERTY` · `INTERFACE` · `EXTENDS` · `IMPLEMENTS` · `REFERENCE` · `FB_init` — một bài toán giải ba cách + bảng hãng hỗ trợ | Ch.30 (mục mới) · trỏ từ Ch.14 · Phụ lục A1 | ⭐ Mọi cú pháp đối chiếu được với tài liệu PLCopen và CODESYS |
| **61 — cách thực hiện lệnh** | Phụ lục B: **hành vi thực thi** từng khối chuẩn *(cập nhật khi nào · vòng quét đầu · khi không được gọi)* · bẫy `R_TRIG` ở vòng quét đầu · ⭐⭐ **hàm chuỗi** + ví dụ thật tách mã lô từ mã 2D ở Ch.42 · dịch bit, `MUX`, `MIN`/`MAX` | Phụ lục B, Ch.16, Ch.19, Ch.42 | Mỗi lệnh chuẩn có **một dòng hành vi thực thi** kiểm được |
| **62 — mã mẫu** | Mỗi chương trọng tâm (Ch.14–30) có **≥ 1 ví dụ hoàn chỉnh** · SFC nên/không nên (Ch.21, 26) · quy ước *"đoạn trích"* ghi ở Ch.1 | Ch.14–30, Ch.21, Ch.26 | Bộ kiểm cú pháp xác nhận mọi ví dụ hoàn chỉnh đạt |

⭐ Mỗi đợt kết thúc như các đợt trước: **năm (thành sáu) bộ kiểm 0 lỗi**, nhật ký đối chiếu, ghép sách,
đẩy lên kho phát hành.

---

## 5. Hệ quả nếu duyệt

- ⭐ Sách có bộ **quy tắc viết mã viết ra**, thay vì một sự nhất quán ngầm chỉ người viết biết.
- ⭐ Người đọc được dạy **thiết kế khối của mình theo cùng mô hình với khối của hãng** — thứ hiện
  chỉ thấy khi *dùng* khối Motion/truyền thông mà không ai giải thích.
- ⚠ Sách tăng khoảng **1 phụ lục + 3–4 mục lớn**; Ch.30 dài thêm — cân nhắc tách ở đợt 60 nếu vượt
  ngưỡng đọc được.
- ⚠ Mục hướng đối tượng **chỉ áp dụng được cho một số hệ** — phải nói rõ ngay đầu mục, không để người
  dùng Mitsubishi đời cũ đọc xong mới biết.

---

## 6. Tiến độ

### Đợt 58 — xong 2026-09-26

| Hạng mục | Kết quả |
|---|---|
| Tài liệu PLCopen | ⚠ Tải 4 tệp đã duyệt — **chỉ bộ Coding Guidelines là bản đầy đủ** (127 tr); ba tệp kia là tờ giới thiệu 1–4 trang. Bản đầy đủ của ba tài liệu đó **chưa tải** — cần duyệt riêng |
| Phụ lục N | ✅ 64 quy tắc đối chiếu; chỗ theo · chỗ lệch có chủ ý · chỗ từng sai đã sửa |
| Bộ kiểm thứ sáu | ✅ `tools/kiem_cu_phap_st.py`, nối vào `gop_sach.sh`; ⭐ thử bằng **11 lỗi cài cố ý — bắt đủ 11**. ⚠ Khác đề xuất ở 3.4: **chưa** kiểm biến chưa khai báo (dời sang đợt 62, cùng lúc làm ví dụ hoàn chỉnh); không kiểm khối `MC_*` (không có đặc tả Part 1 trong bộ tài liệu cục bộ). ⭐ Làm **thêm** việc đề xuất không có: so giao diện **và thân** mọi khối cùng tên, kiểm tên chân khi gọi/đọc khối chuẩn |
| Lỗi tìm ra khi soát theo PLCopen | `RETURN` trong khung trình tự (L.6, Ch.26, Ch.29) · khung L.6 xoá bước khi chỉ tạm dừng · vòng `REPEAT` đọc phần tử chưa gán (Ch.20) · *"số nguyên thì `=` an toàn"* (Ch.19) · 3 bẫy chưa dạy (CP4, L12, L13) |
| Lỗi bộ kiểm thứ sáu tìm ra | 6 khối không đóng · ⭐⭐ **hai khối `FB_Cylinder2Pos` khác nhau** — kéo theo hai lỗi hành vi thật khi ghép Ch.25 với Ch.27 → design note 0006 |
| Ngoài phạm vi, phát hiện dọc đường | ⭐ Cụm con trỏ theo **số chương cũ** còn sót sau đợt 13: 51 chỗ / 13 tệp (công thức → Ch.32, báo động → Ch.43, đánh giá rủi ro → Ch.6…) · mục lục thanh bên HTML lộ nguyên `**` · 7 dòng Mục lục có `**` không đóng · Mục lục ghi *"hiện tại 18/58"* |

### Đợt 59 — xong 2026-09-26

| Hạng mục | Kết quả |
|---|---|
| Mô hình `Execute`/`Enable` cho khối tự viết | ✅ Ch.30 mục 30.5b + Phụ lục L mục L.8b — năm quy tắc đối chiếu hai tài liệu hãng; khối mẫu mô phỏng đạt |
| Phạm vi biến | ✅ Ch.11 mục 11.6 — `VAR_EXTERNAL` và quy tắc *khối không đọc biến toàn cục* (CP6). ⚠ Khác kế hoạch: đặt ở Ch.11 chứ không ở Ch.14 — Ch.11 đã có mục phạm vi biến |
| Khung POU / khung chương trình chính | ✅ Ch.14 mục 14.7 thống nhất với Ch.27, Ch.57 |
| ⭐⭐ Ngoài kế hoạch, lớn nhất | Đường đi của lỗi giữa các tầng — khoá chết Reset — design note 0007; Ch.25 mục 25.5c; sửa đồng bộ 20 tệp |
| Bộ kiểm thứ sáu | + CP20 và khai báo ngoài `VAR`; thử bằng 13 lỗi cài |

### Đợt 60 — xong 2026-09-26

| Hạng mục | Kết quả |
|---|---|
| Hướng đối tượng trong Ch.30 | ✅ Mục 30.5c — năm công cụ, cùng bài toán ba cách, năm cái bẫy riêng trên PLC, bảng hãng có căn cứ |
| Đối chiếu cú pháp CODESYS (đọc trang, không tải tệp) | ✅ Method, Property, Interface, Implementation of an Interface, Extension of a Function Block, REFERENCE TO, THIS, SUPER, FB_Init |
| E2/E3 | ✅ Áp ở bẫy 4 của 30.5c |
| Trỏ từ Ch.14 | ✅ Bảng các bản của chuẩn ở mục 14.1 trỏ sang 30.5c |
| ⚠ Ngoài kế hoạch | ⚠⚠ IEC 61131-3 bản 4 (5/2025) bỏ IL — sửa Ch.13, 14, 21, Mục lục; các thay đổi về lệnh để đợt 61 |
| ⚠ Chưa kiểm được | Thân khối cha có tự chạy khi gọi khối con không — sách né, không đoán |

### Đợt 61 — xong 2026-09-27

| Hạng mục | Kết quả |
|---|---|
| Hành vi thực thi từng khối chuẩn | ✅ Phụ lục B mục B.9b — cập nhật khi nào, lần gọi đầu, khi không được gọi |
| Bẫy `R_TRIG` ở vòng quét đầu | ✅ Ch.16 Bẫy 9 + cờ `M_FirstScan` ở L.7, Ch.57, M.4 |
| Hàm chuỗi + ví dụ Ch.42 | ✅ Phụ lục B mục B.6b; Ch.42 mục 42.4 hàm `KiemTraMaHopLe` với tám ca thử |
| Dịch bit, `MUX`, `MIN`/`MAX` | ✅ Phụ lục B B.3, B.6 (thanh ghi dịch đã có ở Ch.19 mục 19.6) |
| Thay đổi của bản 4 | ✅ `TRUNC`, BCD, `USTRING`, `LEN_MAX`, `LEN_CODE_UNIT` |
| ⚠⚠ Ngoài kế hoạch | Hai lỗi của Ch.42 chỉ lộ ra từ board thứ hai; cụm con trỏ số chương cũ tái phát lần ba → phép kiểm cố định |

### Đợt 62 — xong 2026-09-28

Quyết định và chi tiết: design note 0008. Nhật ký đối chiếu #612–#650.

| Hạng mục | Kết quả |
|---|---|
| Ví dụ hoàn chỉnh cho Ch.14–30 | ✅ 17 khối mang dấu `// ✔ VÍ DỤ HOÀN CHỈNH` (Ch.22, 23 là chương phương pháp) |
| SFC nên / không nên | ✅ Ch.21 — chín dòng có nguồn; sửa bốn lời sai về `.T`, `P`, `N`, cờ bước |
| Quy ước *đoạn trích* ở Ch.1 | ✅ Ch.1 + Phụ lục N mục N.7 |
| Kiểm biến chưa khai báo (dời từ đợt 58) | ✅ Trong phạm vi ví dụ hoàn chỉnh; bộ kiểm thứ sáu thêm bảy phép, thử 12/12 + 13/13 |
| `Stn1.Step` hay `Stn1_Step` | ✅ Cả hai có vai trò: `Stn1.` giao diện công bố (`ST_Station`), `Stn1_` ruột của trạm |
| ⭐⭐ Ngoài kế hoạch | Bộ chạy thử ST `tools/chay_thu/` (82 phép thử, bộ kiểm thứ bảy) — tìm ra lỗi *"`Done` của lệnh cũ"* ở Ch.26 mà kiểm tĩnh không thấy; năm chỗ gọi khối trong nhánh ở Ch.37–46 |
