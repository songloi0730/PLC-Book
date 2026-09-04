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
| Tài liệu PDF | **63** |
| Tổng số trang | **23 139** |
| Mục lục nhúng đọc được | **11 231 mục** trên 47 tài liệu |
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
| Siemens S7-1200 System Manual | 864 | 610 | ✔ |
| Hugh Jack — Automating Manufacturing | 860 | 554 | ✔ |
| Siemens Safety programming | 579 | 405 | ✔ |
| Rabiee — Hardware and Programming | 446 | 0 | ✔ |
| DGUV / IFA | 324 | 158 | ⚠ **chưa** |
| SICK — an toàn | 322 | 0 | ✔ |
| IO-Link — đặc tả giao diện | 294 | 535 | ✔ |
| Mitsubishi FX5 — Program Design | 136 | 73 | ✔ |
| AutomationDirect PLC Handbook | 85 | 0 | ✔ |
| PPSA / khí nén | 71 | 65 | ⚠ **chưa** |
| Siemens S7-1500 / TIA | 37 | 0 | ✔ |
| Schneider — an toàn máy | 33 | 0 | ✔ |
| Rockwell — IEC 61131-3 compliance | 30 | 17 | ✔ |
| IO-Link — mô tả hệ thống | 25 | 4 | ✔ |

---

## 3. Nguồn đã được dẫn — dẫn ở chương nào

| Nguồn | Trang | Chương dẫn |
|---|--:|---|
| Kuphaldt — Industrial Instrumentation | 3311 | 38 |
| Kuphaldt — Electric Circuits | 2354 | 38 |
| Petruzella — PLC (2025) | 441 | 16, 18, 19, 51 |
| Petruzella — PLC 6th ed | 417 | 16, 18, 19, 51 |
| Petruzella — Activities Manual | 401 | 16, 18, 19, 51 |
| Hanssen — IEC 61131-3 / CoDeSys | 419 | 14, 19, 20, 21 |
| Mitsubishi FX5 — MODBUS | 86 | 39 |
| Inovance H5U/Easy — lập trình | 808 | 19, 22, 23, 24, 30 |
| Inovance H5U/Easy — lệnh | 1113 | 19 |
| Inovance H3U — lệnh & lập trình | 731 | 19, 22, 23, 24, 30 |
| Inovance InoProShop / CODESYS | 1642 | 19 |
| Modbus — đặc tả | 136 | 39 |

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
| `reference/03_Vendor_Manuals/Mitsubishi_MELSEC_iQ-F_FX5_Positioning_Control.pdf` | 302 |
| `Huong dan lap trinh PLC Mitsubishi voi cac lenh co ban.pdf` | 200 |
| `reference/01_Instrumentation/Kuphaldt_So_You_Want_To_Be_An_Instrumentation_Technician.pdf` | 163 |
| `plc s7-1200.pdf` | 130 |
| `Manual/H5U&Easy_Manual/Easy系列可编程逻辑控制器用户手册.PDF` | 123 |
| `reference/08_Open_Specs/PLCopen_Function_Blocks_for_Motion_Control.pdf` | 119 |
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
| IEC 60204-1 | 29 |
| IEC 61131-3 | 20 |
| IEC 61131-2 | 15 |
| Bảng I/O và số liệu đã chốt của DP-01 | 7 |
| Bảng I/O của DP-01 | 6 |
| Tài liệu lập trình của từng hệ trong Phụ lục A | 6 |
| ISO 12100 | 5 |
| IEC 60947-5-1 | 4 |
| IEC 61131-1 | 3 |
| IEC 62682 | 3 |
| Datasheet cảm biến | 3 |
| IEC 61800-5-2 | 3 |
| IEC 61800-3 | 3 |
| Bảng I/O, bảng công thức và số liệu đã chốt của DP-01 | 3 |
| Bảng I/O và mô tả trình tự của DP-01 | 2 |
| IEC 60381-1 và -2 | 2 |
| Datasheet module analog | 2 |
| Số liệu đã chốt của DP-01 | 2 |
| IEC 61918 | 2 |
| IEC 62381 | 2 |
| IEC 62443 (bộ) | 2 |
| IEC 61508 và ISO 13849-1 | 2 |
| Tư liệu lịch sử về **Modicon 084** và về bối cảnh ra đời của | 1 |
| Catalogue của các hãng nêu ở Chương 8 và Chương 13 | 1 |
| IEC 60947-5-4 và các tài liệu liên quan tới **tiếp điểm dẫn  | 1 |
| IEC 61140 | 1 |
| Quy định an toàn điện và quy trình LOTO của cơ sở nơi bạn là | 1 |
| Datasheet cảm biến của các hãng | 1 |
| Cấu hình I/O của DP-01 | 1 |
| Datasheet của van điện từ, contactor và rơ-le | 1 |

---

## 6. ⚠ Tên nguồn chưa khớp được nhãn nào

⭐ Hoặc là nguồn ngoài bộ (thêm mẫu vào `nguon_ngoai_bo_tai_lieu`), hoặc là tệp có thật
nhưng thiếu bí danh (thêm vào `bi_danh_tep`).

| Tên | Số lần |
|---|--:|
| Thông tin về vòng đời sản phẩm và thông báo ngừng sản xuất,  | 1 |
| ⚠ **Giới hạn của bảng 4 tổ hợp** (mục 15.3): nó chỉ phủ **hỏ | 1 |
| Hugh Jack | 1 |
| Tài liệu về **GRAFCET** | 1 |
| Biểu mẫu **nhật ký thay đổi công thức** | 1 |
| Quy ước đặt tên và cấu trúc dùng trong sách | 1 |
| OIML R 60 | 1 |
| Tài liệu **khối PID** của hệ đang dùng | 1 |
| Tài liệu **bộ điều khiển nhiệt độ rời** | 1 |
| Tài liệu biến tần | 1 |
| Đặc tả PLCopen Motion Control | 1 |
| Tài liệu servo drive | 1 |
| TIA/EIA-232 | 1 |
| Tài liệu thiết bị tớ | 1 |
| Tài liệu mạng của hệ PLC đang dùng | 1 |
| Đặc tả giao diện SMEMA | 1 |
| ⚠ **Tài liệu của máy hàng xóm** | 1 |
| ISO/IEC 16022 | 1 |
| ISO/IEC 15415 | 1 |
| Tài liệu hệ vision | 1 |
| Tài liệu hệ HMI/SCADA | 1 |
| Mô hình Purdue | 1 |
| Tài liệu bảo mật của hệ PLC đang dùng | 1 |
| ISO/TS 15066 | 1 |
| Tài liệu robot | 1 |
| Tài liệu hướng dẫn của nhà sản xuất thiết bị an toàn và báo  | 1 |
| Hướng dẫn lắp đặt của nhà sản xuất biến tần và PLC | 1 |
| Biểu mẫu **danh sách ca kiểm thử** và **biên bản kết quả** | 1 |
| Biểu mẫu **biên bản kiểm I/O 1-1**, **biên bản nghiệm thu**  | 1 |
| Hướng dẫn của nhà sản xuất PLC, biến tần, HMI | 1 |
| Hợp đồng và điều khoản bàn giao | 1 |
| Phép đo thời gian bước và bộ đếm | 1 |
| Quy định pháp luật tại thị trường của bạn | 1 |
| Tài liệu vòng đời sản phẩm của nhà sản xuất PLC | 1 |
| Toàn bộ các chương được dẫn trong bảng ở mục 57.3–57.10 | 1 |
| Tài liệu và khoá đào tạo của các nhà sản xuất thiết bị | 1 |

---

*Sinh tự động bởi `tools/ban_do_nguon.py`.*
