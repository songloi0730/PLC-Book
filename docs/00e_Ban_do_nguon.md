# Bản đồ nguồn và chương

> ⭐⭐ **Mục đích:** bộ tài liệu nguồn quá lớn để đọc hết. Người viết chỉ tra những gì mình
> **nghĩ ra để tra** — nên tài liệu có thể phủ một chủ đề mà không ai biết, và chương liên
> quan vẫn thiếu. Bảng này trả lời câu hỏi ⚠ **tài liệu nào chưa được chương nào dẫn.**
>
> ⚠ Tệp này **sinh tự động** — đừng sửa tay. Cập nhật bằng:
> `python tools/lap_chi_muc_nguon.py` rồi `python tools/ban_do_nguon.py`

---

## 1. Quy mô bộ tài liệu

| Chỉ số | Giá trị |
|---|---|
| Tài liệu PDF | **68** |
| Tổng số trang | **23 556** |
| Mục lục nhúng đọc được | **11 613 mục** trên 51 tài liệu |
| ⚠ Không trích được text | **3** |

> ⚠⚠ **Tài liệu không trích được text — coi như KHÔNG CÓ cho tới khi OCR.**
>
> - `Manual/H5U&Easy_Manual/H5U USB驱动安装操作说明.pdf` — 7 trang
> - `Manual/H5U&Easy_Manual/H5U&Easy系列可编程逻辑控制器指令手册.PDF` — 1037 trang
> - `Programmable Logic Controllers Hardware and Programming (Max Rabiee).pdf` — 446 trang

---

## 2. ⚠⚠ Nguồn CHƯA được chương nào dẫn

⭐ Đây là phần quan trọng nhất của tệp này. Mỗi dòng là tài liệu **đang có trong tay** mà
**không chương nào dẫn** — nghĩa là hoặc nó thật sự không liên quan, hoặc ⚠ **có nội dung**
**bị bỏ sót**. Cột cuối cho biết nhật ký đối chiếu đã từng nhắc tới nó chưa.

| Nguồn | Trang | Mục lục | Nhật ký đã nhắc? |
|---|--:|--:|:--:|
| Mitsubishi FX5 — Instructions/FB | 1470 | 651 | ✔ |
| Rockwell — khác | 1432 | 788 | ✔ |
| Rabiee — Hardware and Programming | 446 | 0 | ✔ |
| Tài liệu PLC tiếng Việt | 367 | 0 | ✔ |
| Mitsubishi FX5 — Positioning | 302 | 158 | ✔ |
| IO-Link — đặc tả giao diện | 294 | 535 | ✔ |
| AutomationDirect PLC Handbook | 85 | 0 | ✔ |
| PPSA / khí nén | 71 | 65 | ⚠ **chưa** |
| Siemens S7-1500 / TIA | 37 | 0 | ✔ |
| IO-Link — mô tả hệ thống | 25 | 4 | ✔ |

---

## 3. Nguồn đã được dẫn — dẫn ở chương nào

| Nguồn | Trang | Chương dẫn |
|---|--:|---|
| Kuphaldt — Industrial Instrumentation | 3311 | 38 |
| Kuphaldt — Electric Circuits | 2354 | 38, 47 |
| Petruzella — PLC (2025) | 441 | 16, 18, 19, 51 |
| Petruzella — PLC 6th ed | 417 | 16, 18, 19, 51 |
| Petruzella — Activities Manual | 401 | 16, 18, 19, 51 |
| Hugh Jack — Automating Manufacturing | 860 | 19, 25, 26, 27, 30 |
| Hanssen — IEC 61131-3 / CoDeSys | 419 | 14, 19, 20, 21 |
| Siemens S7-1200 System Manual | 864 | 19, 25, 26, 27, 30 |
| Siemens Safety programming | 579 | 47 |
| Mitsubishi FX5 — Program Design | 136 | 14, 16, 18, 19, 20, 21, 25, 26, 27, 51 |
| Mitsubishi FX5 — MODBUS | 86 | 35, 39 |
| Rockwell — IEC 61131-3 compliance | 30 | 14, 20, 21 |
| Inovance H5U/Easy — lập trình | 808 | 19, 21, 24, 30, 43, 55 |
| Inovance H5U/Easy — lệnh | 1113 | 19 |
| Inovance H3U — lệnh & lập trình | 731 | 19, 21, 24, 30, 43, 55 |
| Inovance InoProShop / CODESYS | 1642 | 19 |
| Modbus — đặc tả | 50 | 35, 39 |
| SICK — an toàn | 322 | 47 |
| Schneider — an toàn máy | 33 | 47 |
| DGUV / IFA | 324 | 47 |
| PLCopen Safety Part 1 | 194 | 37, 47 |
| PLCopen Safe Motion | 45 | 37, 47 |
| PLCopen Motion Control | 213 | 14, 16, 18, 19, 20, 21, 37, 47, 51 |
| PLCopen — Structuring Program Development | 4 | 14, 16, 18, 19, 20, 21, 27, 37, 47, 51 |
| PLCopen XML exchange | 80 | 37, 47 |
| Kuphaldt — Instrumentation Technician | 163 | 38 |

---

## 4. Tệp trong bộ chưa gán nhãn

⭐ Các tệp này chưa có bí danh trong `tools/cau_hinh_ban_do.json`, nên **không được theo dõi**.
Bổ sung bí danh nếu tài liệu có giá trị; bỏ qua nếu không.

| Tệp | Trang |
|---|--:|
| `Manual/H5U&Easy_Manual/H5U&Easy系列可编程逻辑控制器指令手册.PDF` | 1037 |
| `Manual/H5U&Easy_Manual/H5U&Easy系列可编程逻辑控制器编程手册.pdf` | 894 |
| `Manual/H1UH2UH3U_Manual/H3U系列可编程逻辑控制器指令及编程手册.pdf` | 744 |
| `en/Motion Control.pdf` | 344 |
| `Manual/H5U&Easy_Manual/Easy系列可编程逻辑控制器用户手册.PDF` | 123 |
| `Manual/H5U&Easy_Manual/Easy321&Easy511可编程逻辑控制器用户手册.PDF` | 117 |
| `reference/03_Vendor_Manuals/Siemens_Programming_Guideline_S7-1200_1500_v14.pdf` | 109 |
| `reference/03_Vendor_Manuals/Siemens_Programming_Styleguide_S7-1200_1500_v12.pdf` | 44 |
| `Manual/H5U&Easy_Manual/AutoShop V4.11.0.0版本说明书.pdf` | 28 |
| `Manual/H5U&Easy_Manual/H5U系列可编程逻辑控制器用户手册.pdf` | 19 |
| `reference/07_Networks_Whitepapers/EtherCAT_Technology_Group_EtherCAT_and_TSN_Whitepaper.pdf` | 8 |
| `Manual/H5U&Easy_Manual/H5U USB驱动安装操作说明.pdf` | 7 |

---

## 5. Nguồn nằm NGOÀI bộ tài liệu

⭐ Các tên này được chương dẫn nhưng **không có bản gốc trong tay** — chủ yếu là tiêu chuẩn
có bản quyền, datasheet, và số liệu của máy mẫu. ⚠ Đây là lý do sách **không dẫn số điều khoản**.

| Tên nguồn | Số chương dẫn |
|---|--:|
| IEC 60204-1 \| IEC 60204-1 — *Safety of machinery — Electrica | 26 |
| IEC 61131-3 \| IEC 61131-3 — *Programmable controllers, Part  | 19 |
| IEC 61131-2 \| IEC 61131-2 — *Programmable controllers, Part  | 15 |
| Bảng I/O và số liệu đã chốt của DP-01 \| Bảng I/O và số liệu  | 7 |
| Tài liệu lập trình của từng hệ trong Phụ lục A \| Tài liệu lậ | 6 |
| ISO 12100 \| ISO 12100 — *Safety of machinery — General princ | 5 |
| IEC 60947-5-1 \| IEC 60947-5-1 — *Low-voltage switchgear and  | 4 |
| IEC 61131-1 \| IEC 61131-1 — *Programmable controllers, Part  | 3 |
| IEC 61800-5-2 \| IEC 61800-5-2 — *Adjustable speed electrical | 3 |
| Bảng I/O, bảng công thức và số liệu đã chốt của DP-01 \| Bảng | 3 |
| Bảng I/O và mô tả trình tự của DP-01 \| Bảng I/O và mô tả trì | 2 |
| Bảng I/O của DP-01 \| Bảng I/O của DP-01 — Phụ lục J. | 2 |
| IEC 62682 \| IEC 62682 — *Management of alarm systems for the | 2 |
| IEC 60381-1 và -2 \| IEC 60381-1 và -2 — *Analogue signals fo | 2 |
| Datasheet module analog \| **Datasheet module analog** của hệ | 2 |
| Bảng I/O của DP-01 \| Bảng I/O của DP-01 — Phụ lục J; bảng ở  | 2 |
| IEC 61800-3 \| IEC 61800-3 — *EMC requirements for adjustable | 2 |
| IEC 62381 \| IEC 62381 — *Automation systems in the process i | 2 |
| IEC 62443 (bộ) \| IEC 62443 (bộ) — *Industrial communication  | 2 |
| IEC 61508 và ISO 13849-1 \| IEC 61508 và ISO 13849-1 — yêu cầ | 2 |
| Tư liệu lịch sử về **Modicon 084** và về bối cảnh ra đời của | 1 |
| Catalogue của các hãng nêu ở Chương 8 và Chương 13 \| Catalog | 1 |
| IEC 60947-5-4 và các tài liệu liên quan tới **tiếp điểm dẫn  | 1 |
| IEC 61140 \| IEC 61140 — *Protection against electric shock*: | 1 |
| Quy định an toàn điện và quy trình LOTO của cơ sở nơi bạn là | 1 |
| Datasheet cảm biến của các hãng \| Datasheet cảm biến của các | 1 |
| Cấu hình I/O của DP-01 \| Cấu hình I/O của DP-01 — Phụ lục J. | 1 |
| Datasheet của van điện từ, contactor và rơ-le \| **Datasheet  | 1 |
| ISO 4414 \| ISO 4414 — *Pneumatic fluid power — General rules | 1 |
| ISO 15552 \| ISO 15552 — *Pneumatic fluid power — Cylinders w | 1 |

---

## 6. ⚠ Tên nguồn chưa khớp được nhãn nào

⭐ Hoặc là nguồn ngoài bộ (thêm mẫu vào `nguon_ngoai_bo_tai_lieu`), hoặc là tệp có thật
nhưng thiếu bí danh (thêm vào `bi_danh_tep`).

| Tên | Số lần |
|---|--:|
| Thông tin về vòng đời sản phẩm và thông báo ngừng sản xuất,  | 1 |
| ⚠ **Giới hạn của bảng 4 tổ hợp** (mục 15.3): nó chỉ phủ **hỏ | 1 |
| OIML R 60 \| OIML R 60 — *Metrological regulation for load ce | 1 |
| Tài liệu **khối PID** của hệ đang dùng \| Tài liệu **khối PID | 1 |
| Tài liệu biến tần \| **Tài liệu biến tần** của dòng đang dùng | 1 |
| Tài liệu servo drive \| **Tài liệu servo drive** của hệ đang  | 1 |
| TIA/EIA-232 \| **TIA/EIA-232**, **TIA/EIA-422**, **TIA/EIA-48 | 1 |
| Tài liệu thiết bị tớ \| **Tài liệu thiết bị tớ** — dùng cho ⚠ | 1 |
| Tài liệu mạng của hệ PLC đang dùng \| **Tài liệu mạng của hệ  | 1 |
| Đặc tả giao diện SMEMA \| **Đặc tả giao diện SMEMA** — chuẩn  | 1 |
| ⚠ **Tài liệu của máy hàng xóm** \| ⚠ **Tài liệu của máy hàng  | 1 |
| ISO/IEC 16022 \| **ISO/IEC 16022** — *Data Matrix bar code sy | 1 |
| ISO/IEC 15415 \| **ISO/IEC 15415** và **ISO/IEC 29158** — chấ | 1 |
| Tài liệu hệ HMI/SCADA \| **Tài liệu hệ HMI/SCADA** đang dùng  | 1 |
| Mô hình Purdue \| **Mô hình Purdue** — mô hình phân tầng kiến | 1 |
| Tài liệu bảo mật của hệ PLC đang dùng \| **Tài liệu bảo mật c | 1 |
| ISO/TS 15066 \| **ISO/TS 15066** — *Robots and robotic device | 1 |
| Tài liệu robot \| **Tài liệu robot** của hãng đang dùng — dùn | 1 |
| Hướng dẫn lắp đặt của nhà sản xuất biến tần và PLC \| **Hướng | 1 |
| Hướng dẫn của nhà sản xuất PLC, biến tần, HMI \| **Hướng dẫn  | 1 |
| Hợp đồng và điều khoản bàn giao \| Hợp đồng và điều khoản bàn | 1 |
| Quy định pháp luật tại thị trường của bạn \| **Quy định pháp  | 1 |
| Tài liệu vòng đời sản phẩm của nhà sản xuất PLC \| **Tài liệu | 1 |
| Toàn bộ các chương được dẫn trong bảng ở mục 57.3–57.10 \| To | 1 |
| Tài liệu và khoá đào tạo của các nhà sản xuất thiết bị \| **T | 1 |

---

*Sinh tự động bởi `tools/ban_do_nguon.py`.*
