
# Phụ lục F — Thuật ngữ Việt–Anh

> ⭐⭐ **Vì sao phụ lục này tồn tại: tài liệu nhà sản xuất, diễn đàn nghề, và mã lỗi thiết bị đều bằng
> tiếng Anh.**
>
> Bạn học khái niệm bằng tiếng Việt, nhưng khi cần tra cứu — thường là lúc máy đang dừng — bạn phải
> ⭐ **gõ đúng từ tiếng Anh** vào ô tìm kiếm. Phụ lục này nối hai thứ đó.

---

> ⭐ **Cách dùng.** Phần F.1–F.11 sắp **theo chủ đề** — dùng khi bạn biết mình đang ở lĩnh vực nào.
> Phần F.12 sắp **theo vần** — dùng khi bạn chỉ nhớ một từ.
>
> ⚠ Một số thuật ngữ có nhiều cách dịch sang tiếng Việt; cột tiếng Anh là cột **tra cứu được**, nên
> khi nghi ngờ hãy dùng nó.

---

## F.1 Nền tảng PLC

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Bộ điều khiển logic khả trình | Programmable Logic Controller (PLC) | | 1, 2 |
| ⭐ Vòng quét | scan cycle · scan time | ⭐ Khái niệm nền của cả cuốn sách | 10 |
| Ảnh ngõ vào | input image · process image | Bản chụp trạng thái đầu vòng quét | 10 |
| Ảnh ngõ ra | output image | | 10 |
| Chu kỳ quét | cycle time (scan) | ⚠ Khác *cycle time* của máy (Ch.55) | 10, 55 |
| Bộ nhớ giữ được | retentive memory · retain | Giữ qua mất điện | 11 |
| Thời gian đáp ứng | response time | | 9, 10 |
| Ngắt | interrupt | | 10 |
| Tác vụ theo chu kỳ | cyclic task | | 10 |
| Giám sát treo máy | watchdog | | 10 |
| Khe cắm · Giá đỡ | slot · rack | | 8 |
| Module vào/ra phân tán | remote I/O · distributed I/O | | 8 |

---

## F.2 Tín hiệu và thiết bị hiện trường

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Ngõ vào số · Ngõ ra số | digital input (DI) · digital output (DO) | | 4, 9 |
| Ngõ vào analog · Ngõ ra analog | analog input (AI) · analog output (AO) | | 31 |
| ⭐ Thường mở · Thường đóng | normally open (NO) · normally closed (NC) | ⚠ Quyết định hành vi khi đứt dây | 4, 47 |
| Cảm biến kiểu nguồn · kiểu chìm | PNP (sourcing) · NPN (sinking) | ⭐ Sai loại → module không nhận | 4 |
| Cảm biến tiệm cận | proximity sensor | | 4 |
| Cảm biến quang thu-phát | through-beam sensor | | 4 |
| Cảm biến quang phản xạ | retro-reflective sensor | | 4 |
| Cảm biến từ trên xy-lanh | reed switch · magnetic cylinder sensor | | 4, 6 |
| Tiếp điểm khô | dry contact · volt-free contact | | 9 |
| Cách ly quang | opto-isolation | | 9, 41 |
| Chống rung tiếp điểm | debounce | | 17 |
| Encoder tăng dần · tuyệt đối | incremental · absolute encoder | | 18, 37 |
| Bộ đếm xung tốc độ cao | high-speed counter (HSC) | | 18 |
| Cặp nhiệt điện | thermocouple | | 33 |
| Nhiệt điện trở | RTD (resistance temperature detector) | Pt100, Pt1000 | 33 |
| Bù đầu lạnh | cold junction compensation (CJC) | ⚠ Cặp nhiệt điện | 33 |
| Bộ khử tĩnh điện | ionizer | | 7 |
| Tĩnh điện | ESD (electrostatic discharge) | | 7 |

---

## F.3 Cơ cấu chấp hành và khí nén

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Cơ cấu chấp hành | actuator | | 5 |
| Xy-lanh khí nén | pneumatic cylinder | | 6 |
| Van điện từ | solenoid valve | | 6, 9 |
| Van 5/2 lò xo về | 5/2 spring-return valve | ⭐ Trạng thái khi mất điện là **xác định** | 6 |
| Van 5/2 hai cuộn | 5/2 double-solenoid valve | ⚠ Giữ nguyên vị trí khi mất điện | 6 |
| Van tiết lưu | flow control valve | Chỉnh tốc độ xy-lanh | 6 |
| Bộ lọc–điều áp–tra dầu | FRL unit (filter-regulator-lubricator) | | 6 |
| Giác hút chân không | vacuum cup · suction cup | | 6 |
| Diode dập xung | flyback diode · freewheeling diode | ⚠ Bắt buộc với tải cảm | 9 |
| Contactor | contactor | | 5, 9 |
| Rơ-le trung gian | interposing relay | | 5, 9 |
| Tuổi thọ cơ · điện | mechanical · electrical life | ⭐ Hai con số khác nhau trong datasheet | 5, 9 |

---

## F.4 Ngôn ngữ lập trình

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Biểu đồ bậc thang | Ladder Diagram (LD) | | 15 |
| Sơ đồ khối chức năng | Function Block Diagram (FBD) | | 21 |
| Văn bản có cấu trúc | Structured Text (ST) | | 20 |
| Biểu đồ chức năng tuần tự | Sequential Function Chart (SFC) | | 21 |
| Danh sách lệnh | Instruction List (IL) | ⚠ Đã bị loại khỏi tiêu chuẩn | 21 |
| Khối hàm | function block (FB) | | 14, 30 |
| Hàm | function (FUN) | | 14, 30 |
| Thể hiện của khối hàm | function block instance | ⭐ Mỗi thể hiện có bộ nhớ riêng | 14, 30 |
| Khối dữ liệu | data block (DB) | | 11, 30 |
| Kiểu dữ liệu do người dùng định nghĩa | user-defined type (UDT) · structure | | 14, 30 |
| Biến toàn cục · cục bộ | global · local variable | | 11 |
| Bắt cạnh lên · cạnh xuống | rising edge · falling edge | | 16 |
| Tự giữ | latch · seal-in | | 15, 16 |
| Đặt · Xoá | set · reset | | 16 |
| Cưỡng bức | force | ⚠⚠ Nguy hiểm — Ch.50 | 50, 51 |

---

## F.5 Bộ định thời và bộ đếm

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Bộ định thời | timer | | 17 |
| Trễ khi bật | TON (on-delay timer) | | 17 |
| Trễ khi tắt | TOF (off-delay timer) | | 17 |
| Xung | TP (pulse timer) | | 17 |
| Bộ đếm lên · xuống | CTU · CTD (count up · down) | | 18 |
| Giá trị đặt · giá trị hiện tại | preset value · current value | | 17, 18 |
| Thanh ghi dịch | shift register | ⭐ Theo dõi sản phẩm trên chuyền | 18, 41 |

---

## F.6 Trình tự, trạng thái và thiết kế

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Trình tự | sequence | | 21, 26 |
| Bước | step | | 21, 26 |
| Điều kiện chuyển tiếp | transition condition | ⭐ Phải là **phản hồi thật** | 21, 26 |
| Hết giờ | timeout | ⭐ Chỉ để **báo lỗi** | 26 |
| Máy trạng thái | state machine | | 25 |
| Khoá liên động | interlock | | 27, 47 |
| Khoá chéo | mutual interlock | | 27, 47 |
| ⭐ Chờ bận | busy-wait | ⚠ Cách viết cần tránh | 27 |
| Bế tắc | deadlock | | 26 |
| Về gốc | homing | ⭐ Bài toán khó nhất thực tế | 28 |
| Công thức sản phẩm | recipe | | 29 |
| Chế độ tay · tự động | manual · automatic mode | | 28 |
| Đặc tả chức năng | functional specification | | 23 |
| Bảng vào/ra | I/O list · I/O schedule | | 23 |
| Chuỗi cho phép | permissive chain · ready chain | ⭐ Máy phải nói **thiếu điều kiện nào** | 44 |

---

## F.7 Điều khiển quá trình và chuyển động

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Giá trị đặt · giá trị đo | setpoint (SP) · process value (PV) | | 35 |
| Sai lệch | error | | 35 |
| Vòng kín · vòng hở | closed-loop · open-loop | | 35 |
| Điều khiển tỉ lệ–tích phân–vi phân | PID control | | 35 |
| Vượt quá | overshoot | | 35 |
| Bão hoà tích phân | integral windup | | 35 |
| Vùng chết | deadband | | 32, 35 |
| Trễ tích luỹ | hysteresis | | 32 |
| Biến tần | VFD (variable frequency drive) · inverter | | 36 |
| Tăng tốc · giảm tốc | acceleration · deceleration ramp | | 36 |
| ⭐ Mô-men dừng an toàn | STO (Safe Torque Off) | ⚠ Chức năng an toàn của driver | 36, 47 |
| Servo drive | servo drive | | 37 |
| Trục | axis | | 37 |
| Nội suy đường thẳng · cung tròn | linear · circular interpolation | | 37 |
| Điểm dạy | taught point | | 37 |
| Công tắc hành trình gốc | home switch · reference switch | | 28, 37 |
| Giới hạn mềm · giới hạn cứng | soft limit · hard limit | | 37 |

---

## F.8 Truyền thông và mạng

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Truyền thông nối tiếp | serial communication | | 38 |
| Chủ · tớ | master · slave (client · server) | | 38, 39 |
| Thanh ghi giữ | holding register | Modbus | 39 |
| Cuộn dây · ngõ vào rời rạc | coil · discrete input | Modbus | 39 |
| Mã hàm | function code | Modbus | 39 |
| Kiểm tra dư vòng | CRC (cyclic redundancy check) | | 39 |
| Thứ tự byte | byte order · endianness | ⚠ Nguồn lỗi phổ biến | 39 |
| Điện trở đầu cuối | termination resistor | ⚠ RS-485 | 38 |
| Chuyển mạch quản lý được | managed switch | ⭐ Đọc được **bộ đếm lỗi** | 40 |
| Địa chỉ IP · mặt nạ mạng | IP address · subnet mask | | 40 |
| Bắt tay | handshake | | 41 |
| Thời gian thực | real-time | | 40 |
| Cổng một chiều | data diode · unidirectional gateway | | 45 |
| Vùng phi quân sự | DMZ (demilitarized zone) | Kiến trúc mạng | 45 |
| An ninh công nghệ vận hành | OT security | | 45 |

---

## F.9 An toàn máy

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Đánh giá rủi ro | risk assessment | ⭐ Làm ở **giai đoạn 1** | 47, 57 |
| Mối nguy | hazard | | 47 |
| Rủi ro | risk | | 6 |
| Giảm rủi ro theo thứ tự ưu tiên | hierarchy of risk reduction | | 6 |
| Chức năng an toàn | safety function | | 47 |
| ⭐ Mức hiệu năng | Performance Level (PL) | ISO 13849-1 | 47, 48 |
| ⭐ Mức toàn vẹn an toàn | Safety Integrity Level (SIL) | IEC 62061 · IEC 61508 | 47, 48 |
| Dừng khẩn cấp | emergency stop (E-Stop) | ISO 13850 | 47 |
| Dừng loại 0 · 1 · 2 | stop category 0 · 1 · 2 | IEC 60204-1 | 47 |
| Rơ-le an toàn | safety relay | | 47 |
| PLC an toàn | safety PLC | | 47 |
| Rèm quang | light curtain | | 47 |
| Khoá cửa an toàn | safety interlock switch · guard locking | ISO 14119 | 47 |
| Che tạm tín hiệu an toàn | muting | ⚠ Phải có điều kiện chặt | 47 |
| Chống khởi động lại bất ngờ | restart interlock · anti-restart | | 47, 48 |
| Giám sát tiếp điểm | EDM (external device monitoring) | | 47 |
| Hỏng theo hướng an toàn | fail-safe | | 4, 47 |
| Hỏng chung nguyên nhân | common cause failure | | 48 |
| Cô lập năng lượng | energy isolation · lockout-tagout (LOTO) | ⚠⚠ Trước mọi can thiệp | 3 |
| Người có thẩm quyền | competent person · authorized person | ⚠ Khái niệm pháp lý | 3, 47 |

---

## F.10 Vận hành, bảo trì và chất lượng

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| Báo động | alarm | | 44 |
| Xác nhận báo động | acknowledge (ack) | | 44 |
| Báo động đầu tiên | first-out alarm | ⭐ Cái nào xảy ra **trước** | 44 |
| Tràn báo động | alarm flood | IEC 62682 | 44 |
| Sửa trực tuyến | online edit | ⚠⚠ Ch.53 | 53 |
| Tài liệu hiện trạng | as-built documentation | ⭐ Khác **bản thiết kế** | 53 |
| Quản lý thay đổi | change management | | 53 |
| Sao lưu · Khôi phục | backup · restore | | 54 |
| Mã kiểm tra | checksum | | 48, 54 |
| Quản lý phiên bản | version control | | 54 |
| Ký gửi mã nguồn | source code escrow | | 54 |
| Mã độc tống tiền | ransomware | | 45, 54 |
| Bảo trì phòng ngừa | preventive maintenance | | 53 |
| Bảo trì theo tình trạng | condition-based maintenance | | 53 |
| Nâng cấp máy cũ | retrofit | | 56 |
| Chạy thử tại xưởng · tại nhà máy | FAT · SAT (factory · site acceptance test) | | 52 |
| Nghiệm thu | acceptance | | 52 |

---

## F.11 Năng suất

| Tiếng Việt | English | Ghi chú | Chương |
|---|---|---|---|
| ⭐ Chu kỳ máy | cycle time | ⚠ **Không phải** thời gian đi hết máy | 55 |
| Thời gian thông qua | throughput time · lead time | | 55 |
| Sản lượng giờ | UPH (units per hour) | | 55 |
| ⭐⭐ Nút cổ chai | bottleneck | | 55 |
| Chỗ đệm | buffer | ⭐ Trạm đệm và thời gian nằm lại: Ch.41 mục 41.7b | 41, 55 |
| Hiệu suất thiết bị tổng thể | OEE (Overall Equipment Effectiveness) | ISO 22400 | 55 |
| Khả dụng · Hiệu suất · Chất lượng | availability · performance · quality | Ba thành phần OEE | 55 |
| Thời gian chết | downtime | | 55 |
| Dừng ngắn | micro-stop · minor stoppage | ⭐ Thường bị bỏ qua khi tính | 55 |
| Truy xuất nguồn gốc | traceability | | 42 |
| Hệ thống quản lý sản xuất | MES (Manufacturing Execution System) | | 42, 45 |

---

## F.12 Tra theo vần — tiếng Việt

| A–C | | | |
|---|---|---|---|
| Ảnh ngõ vào | input image | An ninh công nghệ vận hành | OT security |
| Bắt cạnh | edge detection | Bắt tay | handshake |
| Bảo trì phòng ngừa | preventive maintenance | Bế tắc | deadlock |
| Biến tần | VFD · inverter | Bộ định thời | timer |
| Bộ đếm | counter | Bù đầu lạnh | cold junction compensation |
| Cảm biến tiệm cận | proximity sensor | Cặp nhiệt điện | thermocouple |
| Chạy thử tại xưởng | FAT | Chế độ tay | manual mode |
| Chỗ đệm | buffer | Chống rung tiếp điểm | debounce |
| Chu kỳ máy | cycle time | Chuỗi cho phép | permissive chain |
| Chức năng an toàn | safety function | Cô lập năng lượng | LOTO |
| Công thức sản phẩm | recipe | Cưỡng bức | force |

| D–K | | | |
|---|---|---|---|
| Diode dập xung | flyback diode | Dừng khẩn cấp | emergency stop |
| Đánh giá rủi ro | risk assessment | Điện trở đầu cuối | termination resistor |
| Điều kiện chuyển tiếp | transition condition | Đường bao an toàn | safeguarding |
| Encoder | encoder | Giá trị đặt | setpoint |
| Giám sát tiếp điểm | EDM | Giới hạn mềm | soft limit |
| Hết giờ | timeout | Hỏng theo hướng an toàn | fail-safe |
| Khe cắm | slot | Khoá cửa an toàn | guard locking |
| Khoá liên động | interlock | Khối hàm | function block |

| L–R | | | |
|---|---|---|---|
| Ladder | Ladder Diagram | Mã kiểm tra | checksum |
| Máy trạng thái | state machine | Mô-men dừng an toàn | STO |
| Mối nguy | hazard | Mức hiệu năng | Performance Level |
| Nâng cấp máy cũ | retrofit | Ngắt | interrupt |
| Nghiệm thu | acceptance | Người có thẩm quyền | competent person |
| Nút cổ chai | bottleneck | PID | PID control |
| Quản lý phiên bản | version control | Rèm quang | light curtain |
| Rơ-le an toàn | safety relay | | |

| S–X | | | |
|---|---|---|---|
| Sản lượng giờ | UPH | Sao lưu | backup |
| Sửa trực tuyến | online edit | Tài liệu hiện trạng | as-built |
| Thanh ghi dịch | shift register | Thanh ghi giữ | holding register |
| Thời gian thông qua | throughput time | Thứ tự byte | endianness |
| Tĩnh điện | ESD | Tràn báo động | alarm flood |
| Trình tự | sequence | Truy xuất nguồn gốc | traceability |
| Trục | axis | Tự giữ | latch · seal-in |
| Tuổi thọ điện | electrical life | Van điện từ | solenoid valve |
| Về gốc | homing | Vòng quét | scan cycle |
| Vùng chết | deadband | Xy-lanh khí nén | pneumatic cylinder |

---

## F.13 ⭐ Vài từ dễ nhầm

| Cặp từ | Khác nhau ở đâu | Chương |
|---|---|---|
| ⭐⭐ **cycle time** (máy) ↔ **scan time** (PLC) | Một là nhịp ra sản phẩm, một là thời gian một vòng quét — ⚠ **hai đại lượng không liên quan** | 7, 55 |
| ⭐⭐ **cycle time** ↔ **throughput time** | Nhịp ra sản phẩm ↔ thời gian **một sản phẩm** đi hết máy | 55 |
| ⭐ **PE** ↔ **0 V** | Dây bảo vệ cho **người** ↔ đường về của dòng mạch điều khiển | 49 |
| **safety relay** ↔ **relay** | Có cấu trúc chống hỏng và giám sát; ⚠ không thay thế nhau | 47 |
| **interlock** ↔ **guard locking** | Khoá logic giữa các cơ cấu ↔ khoá **cơ khí** giữ cửa đóng | 22, 47 |
| ⭐ **as-built** ↔ **design** | Máy **hiện đang** thế nào ↔ máy **định** thế nào | 53 |
| **function** ↔ **function block** | Không có bộ nhớ riêng ↔ ⭐ **có bộ nhớ riêng theo thể hiện** | 30 |
| ⭐ **PL** ↔ **SIL** | Hai hệ thang đo mức an toàn khác nhau (ISO 13849-1 ↔ IEC 62061) | 47, 48 |
| **NO** ↔ **NC** | ⚠ Quyết định máy làm gì khi **đứt dây** | 4, 47 |
| **PNP** ↔ **NPN** | Cảm biến cấp dòng ra ↔ nhận dòng vào; ⭐ **sai loại thì module không nhận** | 4 |

> ⭐⭐ **Cặp đầu tiên gây nhầm lẫn nhiều nhất khi đọc tài liệu tiếng Anh:** cả hai đều gọi là *cycle
> time*. Khi tài liệu nói *"cycle time 8 ms"* thì đó là vòng quét PLC; khi khách hàng nói *"cycle time
> 12 giây"* thì đó là nhịp ra sản phẩm.
>
> ⭐ Nhìn **đơn vị** để phân biệt: mili giây → PLC; giây hoặc phút → máy.

---

> ⚠ **Giới hạn.** Bảng này ưu tiên **thuật ngữ dùng được để tra cứu**, không phải bản dịch chuẩn hoá.
> Một số từ tiếng Việt trong ngành chưa có cách dùng thống nhất — nếu tài liệu nơi bạn làm dùng từ
> khác, ⭐ **dùng từ của họ** và giữ cột tiếng Anh làm cầu nối.
>
> Thuật ngữ trong tiêu chuẩn có định nghĩa chính thức riêng; ⚠ khi làm việc với hồ sơ an toàn, **lấy
> định nghĩa từ bản gốc tiêu chuẩn**, không từ bảng này (Chương 47, 48).
