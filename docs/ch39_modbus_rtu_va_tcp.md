# Chương 39 — Modbus RTU & Modbus TCP

> **Lát cắt máy mẫu:** 4 — thêm mạng: mã 2D, MES, SMEMA, màn hình vận hành, và bộ điều khiển nhiệt độ
> keo nối RS-485.

---

## 39.1 Bài toán: đọc đúng thanh ghi, sai một ô

Tài liệu bộ điều khiển nhiệt độ ghi: *"Nhiệt độ thực tế: thanh ghi **40001**"*.

Kỹ sư viết lệnh đọc thanh ghi **40001**. Không đọc được gì — thiết bị báo lỗi "địa chỉ không hợp lệ".

Thử đọc **1**. Đọc được, nhưng ra con số vô nghĩa.

Thử đọc **0**. Đọc được `603` — đúng 60,3 °C.

Ba lần thử, ba kết quả khác nhau, cho **cùng một thanh ghi** theo tài liệu. Không có gì sai với thiết
bị, cũng không sai với PLC.

Đây là **bẫy kinh điển số một của Modbus**, và gần như mọi người dùng Modbus đều mất thời gian với nó
ít nhất một lần. Mục 39.4 giải thích.

---

## 39.2 Vì sao Modbus ở khắp nơi

Modbus ra đời từ những năm 1970 và ⭐ **vẫn có mặt ở gần như mọi nhà máy** — hiếm thiết bị công
nghiệp nào không hỗ trợ nó ở dạng nào đó. Lý do không phải vì nó tốt nhất.

> ⚠ **Không nên phát biểu thành "giao thức phổ biến nhất".** ⭐ Đếm theo **số nút mạng** thì các
> giao thức Ethernet công nghiệp ở Chương 40 đã vượt từ lâu ở máy đời mới; đếm theo **số chủng loại
> thiết bị có hỗ trợ** thì Modbus vẫn dẫn. ⚡ Hai cách đếm, hai câu trả lời — nên câu đáng nói là
> **"ở đâu cũng gặp"**, không phải **"nhiều nhất"**.

| Lý do | Giải thích |
|---|---|
| ⭐ **Mở và miễn phí** | Không phải trả phí bản quyền, không cần gia nhập tổ chức nào |
| ⭐ **Rất đơn giản** | Đọc và ghi thanh ghi — hết. Học trong một buổi |
| ⭐ **Ai cũng có** | Gần như mọi thiết bị công nghiệp đều hỗ trợ, dù nó dùng giao thức chính là gì |
| Chạy trên nhiều tầng vật lý | RS-485, RS-232, Ethernet — cùng một mô hình dữ liệu |
| Công cụ gỡ lỗi sẵn có | Nhiều phần mềm chủ giả lập miễn phí |

> ⭐ **Modbus là "tiếng phổ thông" của ngành**: không phải ngôn ngữ đẹp nhất, nhưng là ngôn ngữ mà hai
> thiết bị bất kỳ nhiều khả năng cùng nói được.
>
> Khi bạn cần nối một thiết bị lạ vào PLC và không có tuỳ chọn nào chung, **Modbus thường là mẫu số
> chung**.

### ⚠ Và những gì nó **không** có

| Không có | Hệ quả |
|---|---|
| **Bảo mật** | ⚠ Không xác thực, không mã hoá — Chương 45 |
| **Tự mô tả dữ liệu** | ⚠ Thanh ghi 100 là gì? Chỉ tài liệu biết |
| **Kiểu dữ liệu** | Mọi thứ là thanh ghi 16 bit; số thực, 32 bit đều phải **ghép tay** — mục 39.5 |
| **Sự kiện** | Chủ–tớ: tớ không tự báo được (Chương 38, mục 38.6) |
| **Đồng bộ thời gian** | Không phù hợp cho chuyển động phối hợp |

> ⚠⚠ **Modbus không dùng cho tín hiệu an toàn.** Không có cơ chế phát hiện thiết bị chết, không có
> giao thức an toàn, không được chứng nhận. An toàn cần thiết bị và giao thức chuyên dụng
> (Chương 47).

---

## 39.3 Bốn vùng dữ liệu

Modbus tổ chức dữ liệu thành bốn vùng, phân biệt theo **kích thước** và **quyền ghi**.

| Vùng | Kích thước | Quyền | Dùng cho |
|---|---|---|---|
| **Coil** — cuộn | 1 bit | Đọc **và ghi** | Lệnh bật/tắt |
| **Discrete Input** — ngõ vào rời rạc | 1 bit | ⚠ **Chỉ đọc** | Trạng thái bit |
| ⭐ **Holding Register** — thanh ghi giữ | 16 bit | Đọc **và ghi** | ⭐ Phổ biến nhất — tham số, điểm đặt |
| **Input Register** — thanh ghi vào | 16 bit | ⚠ **Chỉ đọc** | Giá trị đo |

> 💡 **Trong thực tế, phần lớn thiết bị dùng gần như toàn bộ là Holding Register** — kể cả cho dữ
> liệu chỉ đọc. Đừng ngạc nhiên khi tài liệu nói "thanh ghi giữ" cho một giá trị đo.

### Mã hàm hay dùng

| Mã | Tên | Làm gì |
|---|---|---|
| `01` | Read Coils | Đọc nhiều bit ghi được |
| `02` | Read Discrete Inputs | Đọc nhiều bit chỉ đọc |
| ⭐ `03` | **Read Holding Registers** | ⭐ Đọc nhiều thanh ghi 16 bit — dùng nhiều nhất |
| `04` | Read Input Registers | Đọc thanh ghi chỉ đọc |
| `05` | Write Single Coil | Ghi một bit |
| ⭐ `06` | **Write Single Register** | Ghi một thanh ghi |
| `15` | Write Multiple Coils | Ghi nhiều bit |
| ⭐ `16` | **Write Multiple Registers** | ⭐ Ghi nhiều thanh ghi — dùng khi nạp cả bộ tham số |

> ⚠ **Mã hàm phải khớp vùng dữ liệu.** Dùng hàm `03` để đọc một Input Register sẽ bị thiết bị từ chối
> — và thông báo lỗi thường chỉ nói "địa chỉ không hợp lệ", không nói "sai mã hàm". Đây là nguyên
> nhân thứ hai của tình huống ở mục 39.1.

---

## 39.4 ⭐⭐ Bẫy kinh điển 1 — địa chỉ

Đây là mục quan trọng nhất chương.

### Hai cách đánh số cùng tồn tại

| Cách | Dùng ở đâu | Ví dụ |
|---|---|---|
| ⭐ **Địa chỉ trong khung tin** — bắt đầu từ **0** | Thứ thật sự truyền trên dây | `0` |
| **Số hiệu trong tài liệu** — bắt đầu từ **1**, có tiền tố vùng | Tài liệu thiết bị, sách cũ | `40001` |

Quy ước tiền tố truyền thống:

| Tiền tố | Vùng | Địa chỉ khung tin |
|---|---|---|
| `0xxxx` | Coil | số hiệu − 1 |
| `1xxxx` | Discrete Input | số hiệu − 10001 |
| `3xxxx` | Input Register | số hiệu − 30001 |
| ⭐ `4xxxx` | **Holding Register** | ⭐ **số hiệu − 40001** |

Nên: tài liệu ghi **40001** → địa chỉ thật trong khung tin là **0**.

```text
   Tài liệu:  40001    40002    40003    40010
   Khung tin:     0        1        2        9
```

> ⭐ **Đây chính là ba lần thử ở mục 39.1:**
> - Đọc `40001` → PLC gửi địa chỉ 40001 trong khung tin. ⚠ Con số đó **hợp lệ với giao thức** (trường
>   địa chỉ là 16 bit, `0x0000`–`0xFFFF`), nhưng **thiết bị không có thanh ghi ở đó** → nó trả về
>   **ngoại lệ 02** (xem mục 39.8).
> - Đọc `1` → gửi địa chỉ 1, tức thanh ghi **thứ hai** → **giá trị của thứ khác**.
> - Đọc `0` → đúng.

### ⚠ Và chuyện còn rắc rối hơn

Không phải tài liệu nào cũng theo quy ước `4xxxx`. Bạn sẽ gặp cả ba kiểu:

| Tài liệu ghi | Nghĩa là gì |
|---|---|
| `40001` | Holding register, địa chỉ khung tin **0** |
| `4x0001` hoặc `4:0001` | Cũng holding register, địa chỉ **0** |
| `0` hoặc `0x0000` | ⭐ Đã là **địa chỉ khung tin** — dùng thẳng |
| Chỉ ghi "thanh ghi 1" | ⚠ **Không đoán được** — phải thử |

> 💡 **Quy trình thực dụng khi tài liệu không rõ:**
> 1. Thử **đúng số ghi trong tài liệu**.
> 2. Nếu lỗi, thử **số đó − 1**.
> 3. Nếu vẫn lỗi, thử **số đó − 40001**.
> 4. Khi đọc được, ⭐ **xác nhận bằng một giá trị bạn biết trước** — đổi điểm đặt trên mặt thiết bị và
>    xem con số đọc về có đổi theo không.
>
> Bước 4 là bước không được bỏ. Đọc được **một con số** không có nghĩa là đọc **đúng thanh ghi** —
> thanh ghi bên cạnh cũng trả về một con số trông hợp lý.

### ⚠ Tham số của PLC cũng có quy ước riêng

Rắc rối thêm một tầng: **khối lệnh Modbus của từng hệ PLC** cũng có quy ước riêng cho chân địa chỉ.
Có hệ nhận địa chỉ khung tin, có hệ nhận số hiệu kiểu `4xxxx` và tự trừ.

> ⚠⚠ **Ba tầng quy ước có thể lệch nhau: tài liệu thiết bị, khối lệnh PLC, và khung tin thật.**
> Cách chắc chắn duy nhất: **bắt khung tin thật trên dây** bằng phần mềm giám sát, và xem địa chỉ nào
> thật sự được gửi đi (mục 39.8).

---

## 39.5 ⭐⭐ Bẫy kinh điển 2 — dữ liệu 32 bit và thứ tự

### Vấn đề

Thanh ghi Modbus là **16 bit**. Nhưng nhiều đại lượng cần 32 bit: bộ đếm lớn, số thực, thời gian tính
bằng mili-giây (Chương 11, mục 11.2).

Cách làm: dùng **hai thanh ghi liền nhau**. Nhưng thanh ghi nào chứa nửa cao, thanh ghi nào chứa nửa
thấp?

> ⚠⚠ **Modbus KHÔNG quy định điều này.** Mỗi hãng tự chọn.

### Bốn khả năng

Với giá trị 32 bit `0x12345678` ghép từ hai thanh ghi:

| Kiểu | Thanh ghi N | Thanh ghi N+1 | Tên hay gặp |
|---|---|---|---|
| A | `0x1234` | `0x5678` | Word cao trước — *big-endian word* |
| B | `0x5678` | `0x1234` | ⭐ Word thấp trước — *little-endian word*, **rất phổ biến** |
| C | `0x3412` | `0x7856` | Đảo byte trong word |
| D | `0x7856` | `0x3412` | Đảo cả hai |

> ⚠ **Cả bốn đều tồn tại trong thực tế.** Và tài liệu thường **không nói rõ** kiểu nào.

### Cách xác định

> ⭐ **Đừng đoán — dùng một giá trị đã biết.**
>
> 1. Đặt thiết bị về một giá trị dễ nhận: ví dụ điểm đặt **1000**.
> 2. Đọc **hai thanh ghi thô**, xem chúng bằng bao nhiêu.
> 3. `1000` là `0x000003E8`. Nếu thấy `0x0000` và `0x03E8` → kiểu A. Nếu thấy `0x03E8` và `0x0000` →
>    kiểu B.
> 4. ⭐ Xác nhận bằng **giá trị thứ hai khác hẳn** — ví dụ 12345 — để chắc chắn không trùng hợp.

```iecst
// Ghép 32 bit, kiểu B (word thấp trước) — kiểu phổ biến nhất
Value32 := DINT(RegBuf[1]) * 65536 + DINT(RegBuf[0]);

// ⚠ Kiểu A thì đảo lại:
// Value32 := DINT(RegBuf[0]) * 65536 + DINT(RegBuf[1]);
```

> ⚠ **Với số thực còn phức tạp hơn** — ngoài thứ tự word còn có định dạng dấu chấm động. Nhiều hệ có
> khối chuyển đổi sẵn; ⭐ **luôn xác nhận bằng giá trị đã biết**, không tin vào tên khối.

> 💡 **Cách tránh cả bài toán này:** nếu thiết bị cho phép chọn, hãy dùng **đơn vị nguyên nhỏ** thay
> cho số thực — nhiệt độ theo 0,1 °C là số nguyên 16 bit, không cần ghép gì (Chương 19, mục 19.5;
> Chương 32, mục 32.4). Đơn giản hơn và không có thứ tự nào để sai.

---

## 39.6 RTU và TCP

Hai biến thể của cùng một mô hình dữ liệu.

| | **Modbus RTU** | **Modbus TCP** |
|---|---|---|
| Tầng vật lý | RS-485, RS-232 (Chương 38) | Ethernet |
| Địa chỉ thiết bị | **Địa chỉ tớ** 1–247 | ⭐ **Địa chỉ IP** + cổng |
| Kiểm tra toàn vẹn | ⭐ **CRC** trong khung | Do TCP lo |
| Đồng thời | ⚠ Một yêu cầu tại một thời điểm | ⭐ Nhiều kết nối song song |
| Tốc độ | Theo baud | Nhanh hơn nhiều |
| Cấu trúc | Bus | Mạng có chuyển mạch |
| Gỡ lỗi | Bắt khung trên cổng nối tiếp | Bắt gói mạng |

> ⭐ **Mô hình dữ liệu giống hệt nhau** — cùng bốn vùng, cùng mã hàm, cùng bài toán địa chỉ và thứ tự
> word. Học một cái là biết cái kia; chỉ khác cách gói và cách địa chỉ thiết bị.

### ⚠ Modbus TCP không phải "an toàn hơn"

Chạy trên Ethernet **không** thêm bảo mật nào. Modbus TCP vẫn không xác thực, không mã hoá — và bây
giờ nó nằm trên một mạng mà nhiều thứ khác cũng nối vào.

> ⚠⚠ **Bất kỳ ai truy cập được mạng đó đều ghi được vào PLC của bạn.** Không có mật khẩu, không có
> kiểm tra quyền.
>
> Đây là lý do phân vùng mạng và kiểm soát truy cập là bắt buộc, không phải tuỳ chọn (Chương 45).

---

## 39.7 ⚠ Timeout, thử lại và CRC

### CRC — cái gì nó bắt được và không bắt được

Modbus RTU có **CRC** *(cyclic redundancy check)* trong mỗi khung. Bên nhận tính lại và so — không
khớp thì **bỏ khung đó**.

| CRC bắt được | ⚠ CRC **không** bắt được |
|---|---|
| Bit bị đảo do nhiễu | Bản tin **đúng nhưng gửi cho sai thiết bị** (trùng địa chỉ tớ) |
| Khung bị cắt | ⚠ Đọc **đúng khung, sai thanh ghi** — mục 39.4 |
| Byte rác chen vào | Giá trị đúng nhưng **diễn giải sai** — mục 39.5 |

> ⭐ **CRC bảo vệ tính toàn vẹn của khung, không bảo vệ tính đúng đắn của ý nghĩa.**
> Một chương trình đọc nhầm thanh ghi vẫn nhận được CRC hợp lệ, và không có gì báo sai.

### Timeout và thử lại

```iecst
// ⭐ Ba tham số phải đặt có chủ đích
//   - Timeout: chờ trả lời bao lâu
//   - Số lần thử lại
//   - Chu kỳ hỏi

ReadTemp(Execute := TrigRead1s.Q,        // hỏi mỗi 1 giây (Chương 38)
         Timeout := T#500MS,             // ⚠ phải > thời gian trả lời chậm nhất
         ...);

// Đếm lỗi liên tiếp — không phản ứng ở lần đầu (Chương 38, mục 38.9)
IF M_ReadError THEN
    CommErrCount := CommErrCount + 1;
ELSIF M_ReadDone THEN
    CommErrCount := 0;
END_IF;
M_TempCommFault := CommErrCount >= 3;
```

> ⚠ **Timeout quá ngắn gây lỗi giả.** Thiết bị chậm — nhất là khi nó đang làm việc khác — có thể mất
> vài trăm mili-giây để trả lời. Đặt timeout 50 ms sẽ cho rất nhiều lỗi mà thực ra không có gì hỏng.
>
> ⚠ **Timeout quá dài làm trình tự chậm.** Nếu thiết bị chết hẳn, mỗi lần hỏi tốn đúng thời gian
> timeout — và nếu bạn hỏi nhiều thiết bị tuần tự thì chúng cộng dồn.
>
> 💡 Điểm khởi đầu hợp lý: **gấp 3–5 lần thời gian trả lời đo được** khi mọi thứ bình thường.

---

## 39.8 ⭐ Quy trình gỡ lỗi Modbus

Thứ tự này tiết kiệm rất nhiều thời gian, vì nó **loại dần** thay vì đoán.

| Bước | Việc | Nếu hỏng ở đây thì |
|---|---|---|
| 0 | ⭐⭐ **Đọc MÃ NGOẠI LỆ thiết bị trả về** trước khi làm gì khác | Nó nói thẳng loại lỗi — xem bảng bên dưới |
| 1 | ⭐ **Tách PLC ra** — dùng phần mềm **chủ giả lập** trên máy tính nối thẳng vào thiết bị | Vấn đề ở thiết bị hoặc tầng vật lý, **không phải ở PLC** |
| 2 | Kiểm bốn tham số nối tiếp (Chương 38, mục 38.4) | Lệch tham số |
| 3 | ⚠ Thử **đảo hai dây A/B** (Chương 38, mục 38.12) | Quy ước A/B khác nhau |
| 4 | Kiểm **địa chỉ tớ** | Sai địa chỉ thiết bị |
| 5 | Thử đọc thanh ghi theo ba cách ở mục 39.4 | Bẫy địa chỉ |
| 6 | ⭐ **Xác nhận bằng giá trị đã biết** — đổi trên mặt thiết bị, xem có đổi theo không | Đọc đúng thanh ghi chưa |
| 7 | Kiểm thứ tự word bằng giá trị đã biết (mục 39.5) | Bẫy 32 bit |
| 8 | Chuyển sang PLC, so sánh với kết quả ở bước 6 | Vấn đề ở khối lệnh PLC |

> ⭐ **Bước 1 là bước quan trọng nhất, và hay bị bỏ.**
> Nối máy tính thẳng vào thiết bị bằng bộ chuyển USB–RS485 và một phần mềm chủ giả lập miễn phí. Nếu
> đọc được ở đó, bạn đã **chứng minh** thiết bị và cáp đều tốt — và vấn đề nằm ở phía PLC. Nếu không
> đọc được, bạn đã loại PLC ra khỏi danh sách nghi phạm.
>
> Đây là ứng dụng trực tiếp của nguyên tắc "chia đôi bài toán, đừng đoán" ở Chương 51.

> 💡 **Bắt khung tin thật** bằng phần mềm giám sát cổng cho bạn thấy **chính xác** cái gì được gửi và
> nhận. Với ba tầng quy ước địa chỉ có thể lệch nhau (mục 39.4), đây là cách duy nhất chắc chắn.

---

### ⭐⭐ Đọc mã ngoại lệ — thiết bị đang nói gì với bạn

Khi thiết bị từ chối một yêu cầu, nó **không im lặng**: nó trả về khung tin lỗi có một **mã ngoại
lệ** *(exception code)*. ⭐ Đọc được mã đó rút ngắn việc gỡ lỗi từ hàng giờ xuống vài phút.

| Mã | Tên | Nghĩa thực dụng | ⭐ Nhìn vào đâu |
|---|---|---|---|
| **01** | Illegal Function | ⭐ **Thiết bị không hỗ trợ mã hàm này** — hoặc nó đang ở trạng thái không xử lý được | Sai mã hàm cho vùng dữ liệu (mục 39.3) |
| ⭐⭐ **02** | Illegal Data Address | ⭐ **Địa chỉ không có trên thiết bị này** — xem bên dưới, đây là mã hay gặp nhất | ⭐ Bẫy địa chỉ (mục 39.4) |
| **03** | Illegal Data Value | ⚠ **Cấu trúc yêu cầu sai** — ví dụ số lượng vượt giới hạn | ⚠ **KHÔNG phải** "giá trị ngoài dải quy trình" — xem cảnh báo dưới |
| **04** | Server Device Failure | Lỗi không phục hồi được **bên trong thiết bị** | Vấn đề của thiết bị, không phải của bạn |
| **05** | Acknowledge | Đã nhận, **đang xử lý, sẽ lâu** | Đừng coi là lỗi; đừng thử lại ngay |
| **06** | Server Device Busy | Thiết bị **đang bận** | Thử lại sau, có giãn cách |

> ⭐⭐ **Mã 02 không chỉ nói về địa chỉ bắt đầu — nó nói về TỔ HỢP địa chỉ bắt đầu và số lượng.**
>
> Ví dụ của chính đặc tả: một thiết bị có **100 thanh ghi**, đánh địa chỉ khung tin **0 đến 99**.
>
> ```text
> Bắt đầu 96, đọc 4 thanh ghi  →  chạm 96, 97, 98, 99   →  ✓ OK
> Bắt đầu 96, đọc 5 thanh ghi  →  chạm 96 … 100         →  ✗ ngoại lệ 02
> ```
>
> ⭐ Nghĩa là **địa chỉ bắt đầu đúng vẫn có thể lỗi** nếu bạn đọc quá dài. Khi gặp mã 02 mà chắc chắn
> địa chỉ đúng, ⭐ **hãy giảm số lượng thanh ghi đọc một lần**.

> ⚠⚠ **Mã 03 bị hiểu nhầm nhiều nhất, và đặc tả nói rõ ngược lại điều người ta hay nghĩ.**
>
> Nó **KHÔNG** có nghĩa *"giá trị bạn ghi nằm ngoài dải hợp lý của quy trình"*. ⭐ **Modbus không biết
> gì về ý nghĩa của giá trị** — ghi 9999 vào thanh ghi nhiệt độ đặt là hoàn toàn hợp lệ với giao
> thức.
>
> Mã 03 nói **cấu trúc yêu cầu sai** — hay gặp nhất là **số lượng vượt giới hạn**:
>
> | Mã hàm | Giới hạn một lần |
> |---|---|
> | ⭐ **0x03 / 0x04** — đọc thanh ghi | ⭐⭐ **tối đa 125 thanh ghi** |
> | 0x10 — ghi nhiều thanh ghi | tối đa 123 thanh ghi |
> | 0x01 / 0x02 — đọc bit | tối đa 2000 bit |
>
> ⚠ **Đây là lỗi rất hay gặp khi đọc một khối dữ liệu lớn**: viết lệnh đọc 200 thanh ghi, thiết bị
> trả mã 03, và thông báo trên HMI chỉ ghi "lỗi Modbus". ⭐ **Chia thành nhiều lệnh đọc.**
>
> ⭐⭐ **Hệ quả thiết kế:** việc bảo vệ máy khỏi giá trị công thức vô lý là việc của **chương trình
> PLC**, không phải của giao thức (Chương 29 mục 29.4, Phụ lục C.5).

*(Đối chiếu: MODBUS Application Protocol Specification V1.1b3 — mục MODBUS Exception Codes và các
mục mô tả mã hàm 0x01–0x10.)*

---

## 39.9 Trên máy mẫu DP-01

### Bản đồ thanh ghi bộ điều khiển nhiệt độ

Bảng dưới là **ví dụ minh hoạ cấu trúc**; bản đồ thật lấy từ tài liệu thiết bị.

| Chức năng | Vùng | Địa chỉ khung tin | Đơn vị | Chiều |
|---|---|---|---|---|
| Nhiệt độ thực tế | Holding | `0` | 0,1 °C | ⭐ Đọc, chu kỳ 1 s |
| Điểm đặt | Holding | `1` | 0,1 °C | ⚠ Ghi, **chỉ khi đổi công thức** |
| Từ trạng thái | Holding | `2` | ⚠ tập bit — kiểu `WORD` | Đọc, 1 s |
| Công suất ra | Holding | `3` | 0,1 % | Đọc, 1 s |

> ⚠ **Từ trạng thái phải khai kiểu `WORD`, không phải `INT`** — nó là tập cờ, không phải số
> (Chương 11, mục 11.2). Khai nhầm sẽ thấy những con số âm vô lý.

### Đọc theo cụm

```iecst
// ⭐ Đọc 4 thanh ghi liền trong MỘT yêu cầu — nhanh hơn 4 yêu cầu riêng
ReadTempCtrl(Execute   := TrigRead1s.Q,
             SlaveId   := 1,
             FunctionCode := 3,              // Read Holding Registers
             StartAddr := 0,                  // ⚠ địa chỉ khung tin, không phải 40001
             Quantity  := 4,
             Timeout   := T#500MS,
             Done      => M_TcRead,
             Error     => M_TcError,
             Data      => TcBuf);

IF M_TcRead THEN
    GlueTempX10     := TcBuf[0];
    GlueSetpointX10 := TcBuf[1];
    TcStatusWord    := TcBuf[2];              // ⚠ WORD, không phải INT
    TcOutputPctX10  := TcBuf[3];
    M_TcCommOk      := TRUE;
END_IF;
```

> ⭐ **Đọc theo cụm là kỹ thuật quan trọng.** Một yêu cầu đọc 4 thanh ghi liền nhanh hơn hẳn 4 yêu
> cầu riêng — mỗi yêu cầu có phần đầu khung, thời gian quay vòng, và thời gian chờ.
>
> ⚠ Điều kiện: các thanh ghi phải **liền nhau**. Đây là lý do nên đọc bản đồ thanh ghi **trước** khi
> thiết kế, và nhóm những gì đọc cùng chu kỳ vào một cụm.

### Ghi điểm đặt — chỉ khi đổi

```iecst
// ⚠⚠ Chỉ ghi khi giá trị THẬT SỰ đổi — Chương 38, Bẫy 9
IF ActiveRecipe.GlueTempSetX10 <> LastWrittenSetpoint THEN
    M_NeedWriteSetpoint := TRUE;
END_IF;

IF M_NeedWriteSetpoint AND NOT M_TcBusy THEN
    WriteSetpoint(Execute := TRUE,
                  SlaveId := 1,
                  FunctionCode := 6,          // Write Single Register
                  Addr := 1,
                  Value := ActiveRecipe.GlueTempSetX10,
                  Done => M_WriteDone);
    IF M_WriteDone THEN
        LastWrittenSetpoint := ActiveRecipe.GlueTempSetX10;
        M_NeedWriteSetpoint := FALSE;
    END_IF;
END_IF;
```

Ba điểm thiết kế:

- ⭐ **So với giá trị đã ghi lần trước**, không ghi mỗi lần công thức được nạp — bộ nhớ thiết bị có
  giới hạn số lần ghi (Chương 38, Bẫy 9).
- **Không ghi khi đang bận** — bus chỉ có một đường (Chương 38, mục 38.8).
- **Chỉ cập nhật `LastWrittenSetpoint` khi `Done`** — nếu ghi thất bại thì lần sau thử lại.

### Xử lý mất kết nối

```iecst
// Theo Chương 38, mục 38.9 và Chương 35, mục 35.9
M_TempCommFault := TcErrCount >= 3;

M_GlueTempFault := M_TempCommFault                          // mất truyền thông
                OR (GlueTempX10 < ActiveRecipe.TempMinX10)  // ngoài dải
                OR (GlueTempX10 > ActiveRecipe.TempMaxX10)
                OR TcStatusWord.X0;                          // thiết bị tự báo lỗi

M_CanStart := ... AND NOT M_GlueTempFault;
```

> ⚠⚠ Nhắc lại điểm quan trọng nhất: **bộ điều khiển vẫn giữ nhiệt khi mất truyền thông, nhưng PLC
> không còn biết nhiệt độ.** Chạy tiếp trong trạng thái mù là quyết định phải nằm trong đặc tả
> (Chương 23), không phải mặc định của người lập trình.

---

## 39.10 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| ⚠⚠ **Quy ước địa chỉ ở chân khối lệnh** | Có hệ nhận **địa chỉ khung tin** (bắt đầu từ 0), có hệ nhận **số hiệu `4xxxx`** và tự trừ. ⭐ **Đây là tầng quy ước thứ ba** — mục 39.4 |
| Khối lệnh Modbus | Mỗi hệ một bộ; phần lớn theo mẫu `Execute`/`Done`/`Busy`/`Error` (Chương 38) |
| Tự xếp hàng nhiều yêu cầu | ⚠ Có hệ tự xếp hàng, có hệ không — **đừng giả định** |
| Modbus TCP có sẵn không | Nhiều CPU có Ethernet nhưng ⚠ **không phải CPU nào cũng có Modbus TCP** — có thể cần thư viện hoặc module |
| Làm tớ hay chủ | Phần lớn PLC làm được cả hai; ⚠ cấu hình khác nhau |
| Số kết nối TCP đồng thời | Có giới hạn — kiểm nếu nối nhiều thiết bị |
| Ghép 32 bit | Một số hệ có khối chuyển đổi sẵn cho các kiểu thứ tự khác nhau; ⭐ **vẫn phải xác nhận bằng giá trị đã biết** |

> ⚠ **Đừng chép cấu hình Modbus từ dự án cũ** nếu thiết bị khác. Bản đồ thanh ghi, quy ước địa chỉ và
> thứ tự word đều **thuộc về thiết bị cụ thể** — cùng loại cảnh báo với Chương 32 mục 32.10 và
> Chương 36 mục 36.10.

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

---

## 39.11 Bẫy thường gặp

### 🔍 BẪY 1 — Nhầm số hiệu tài liệu với địa chỉ khung tin

**Hiện tượng:** ⭐ đúng cỗ máy ở mục 39.1 — lỗi địa chỉ, hoặc đọc được **giá trị của thanh ghi bên
cạnh**.
**Cách sửa:** `40001` → địa chỉ `0`. Thử ba cách ở mục 39.4, rồi **xác nhận bằng giá trị đã biết**.

### 🔍 BẪY 2 — Đọc được một con số rồi kết luận là đúng

**Hiện tượng:** thanh ghi bên cạnh cũng trả về một con số **trông hợp lý**; sai lệch chỉ lộ ra khi
giá trị thật đổi mà con số đọc về không đổi theo.
**Cách sửa:** ⭐ **đổi giá trị trên mặt thiết bị và xem con số đọc về có đổi không** (mục 39.4, bước 4).

### 🔍 BẪY 3 — Đoán thứ tự word khi ghép 32 bit

**Hiện tượng:** giá trị vô lý — thường lớn hoặc nhỏ hơn rất nhiều lần, hoặc nhảy loạn khi giá trị thật
đổi nhẹ.
**Cách sửa:** xác định bằng **hai giá trị đã biết khác hẳn nhau** (mục 39.5).

### 🔍 BẪY 4 — Sai mã hàm cho vùng dữ liệu

**Hiện tượng:** thiết bị từ chối, và thông báo lỗi thường chỉ nói "địa chỉ không hợp lệ" — dẫn bạn đi
tìm nhầm hướng.
**Cách sửa:** mã hàm phải khớp vùng (mục 39.3).

### 🔍 BẪY 5 — Khai từ trạng thái là `INT`

**Hiện tượng:** thấy những con số **âm vô lý**, trong khi thật ra mỗi bit là một cờ.
**Cách sửa:** kiểu `WORD` cho tập cờ (mục 39.9, Chương 11 mục 11.2).

### 🔍 BẪY 6 — Timeout quá ngắn

**Hiện tượng:** lỗi truyền thông lẻ tẻ mà không có gì hỏng; thiết bị chỉ đang bận.
**Cách sửa:** timeout gấp 3–5 lần thời gian trả lời đo được (mục 39.7).

### 🔍 BẪY 7 — Đọc từng thanh ghi bằng nhiều yêu cầu riêng

**Hiện tượng:** chu kỳ đọc chậm; bus bận không cần thiết.
**Cách sửa:** ⭐ **đọc theo cụm** các thanh ghi liền nhau (mục 39.9).

### 🔍 BẪY 8 — Ghi tham số mỗi lần công thức được nạp

**Hiện tượng:** ⚠ mòn bộ nhớ không mất của thiết bị sau vài năm.
**Cách sửa:** ⭐ so với **giá trị đã ghi lần trước**, chỉ ghi khi thật sự đổi (mục 39.9).

### 🔍 BẪY 9 — Tin rằng CRC bảo đảm dữ liệu đúng

**Hiện tượng:** CRC hợp lệ nhưng **đọc nhầm thanh ghi** hoặc **diễn giải sai** — không có gì báo sai.
**Cách sửa:** CRC bảo vệ **khung**, không bảo vệ **ý nghĩa**. Xác nhận bằng giá trị đã biết
(mục 39.7).

### 🔍 BẪY 10 — Tin rằng Modbus TCP an toàn hơn

**Hiện tượng:** ⚠⚠ bất kỳ ai truy cập được mạng đều **ghi được vào PLC**.
**Cách sửa:** Modbus không có bảo mật ở bất kỳ biến thể nào. Phân vùng mạng và kiểm soát truy cập
(mục 39.6, Chương 45).

### 🔍 BẪY 11 — Gỡ lỗi từ phía PLC trước

**Hiện tượng:** mất nhiều giờ nghi ngờ chương trình, trong khi vấn đề ở tầng vật lý hoặc ở thiết bị.
**Cách sửa:** ⭐ **tách PLC ra trước** — dùng chủ giả lập trên máy tính (mục 39.8, bước 1).

---

## 39.12 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Vì sao Modbus phổ biến | **Mở · đơn giản · ai cũng có** — không phải vì nó tốt nhất |
| Bốn vùng dữ liệu | Coil · Discrete Input · ⭐ **Holding Register** · Input Register |
| Mã hàm dùng nhiều nhất | ⭐ `03` đọc · `06` ghi một · `16` ghi nhiều |
| ⭐⭐ Tài liệu ghi `40001` nghĩa là | **Địa chỉ khung tin `0`** |
| ⭐⭐ Thiết bị báo lỗi thì làm gì trước | **Đọc mã ngoại lệ** — 01 sai mã hàm · **02 sai địa chỉ** · 03 cấu trúc/số lượng sai |
| ⭐ Mã 02 nói về cái gì | ⚠ **Tổ hợp địa chỉ bắt đầu VÀ số lượng** — đúng địa chỉ vẫn lỗi nếu đọc quá dài |
| ⚠ Mã 03 KHÔNG nghĩa là gì | **Không** phải "giá trị ngoài dải quy trình" — Modbus không biết ý nghĩa giá trị |
| ⭐ Giới hạn một lần đọc | **125 thanh ghi** (ghi nhiều: 123 · đọc bit: 2000) |
| Ba tầng quy ước có thể lệch | Tài liệu thiết bị · **khối lệnh PLC** · khung tin thật |
| Đọc được một con số nghĩa là | ⚠ **Chưa chắc đúng thanh ghi** — phải xác nhận bằng giá trị đã biết |
| ⭐⭐ Ghép 32 bit | Modbus **không quy định thứ tự word** — bốn khả năng, phải **thử** |
| Cách xác định thứ tự word | **Hai giá trị đã biết khác hẳn nhau** |
| Cách tránh cả bài toán 32 bit | Dùng **đơn vị nguyên nhỏ** nếu thiết bị cho phép |
| RTU và TCP khác nhau ở | Tầng vật lý và cách địa chỉ — ⭐ **mô hình dữ liệu giống hệt** |
| ⚠ Modbus TCP có an toàn hơn không | ❌ **Không** — không xác thực, không mã hoá |
| CRC bảo vệ gì | **Tính toàn vẹn của khung**, ⚠ không bảo vệ **ý nghĩa** |
| Timeout đặt bao nhiêu | **3–5 lần** thời gian trả lời đo được |
| Kết luận mất kết nối sau | **Ba lần lỗi liên tiếp** (Chương 38) |
| Đọc nhiều thanh ghi | ⭐ **Một yêu cầu theo cụm**, không nhiều yêu cầu riêng |
| Ghi tham số vào thiết bị | ⭐ **Chỉ khi giá trị đổi** — so với lần ghi trước |
| Từ trạng thái khai kiểu | ⚠ **`WORD`**, không phải `INT` |
| Bước gỡ lỗi đầu tiên | ⭐ **Tách PLC ra** — chủ giả lập trên máy tính |
| ⚠⚠ Modbus cho tín hiệu an toàn | ❌ **Không bao giờ** |

---

## 39.13 Tự kiểm

1. Nêu ba lý do Modbus phổ biến. Lý do nào **không** nằm trong danh sách đó?
2. Kể bốn vùng dữ liệu Modbus, phân biệt theo kích thước và quyền ghi. Vùng nào dùng nhiều nhất trong
   thực tế?
3. ⭐⭐ Tài liệu ghi "thanh ghi 40010". Địa chỉ nào phải gửi trong khung tin? Nêu ba cách thử khi tài
   liệu không rõ.
4. ⭐ Bạn đọc được một con số từ thanh ghi. Vì sao đó **chưa đủ** để kết luận đã đọc đúng? Cách xác
   nhận là gì?
5. ⭐⭐ Vì sao ghép 32 bit từ hai thanh ghi Modbus lại là bẫy? Nêu bốn khả năng và cách xác định.
6. Cách nào **tránh được hẳn** bài toán 32 bit, và nó liên hệ với chương nào?
7. Modbus RTU và TCP khác nhau ở những điểm nào? Điểm nào **giống hệt** nhau?
8. ⚠ Modbus TCP có an toàn hơn Modbus RTU không? Vì sao?
9. ⭐ CRC bắt được gì và **không** bắt được gì? Nêu hai tình huống CRC hợp lệ nhưng dữ liệu vô nghĩa.
10. Timeout quá ngắn và quá dài mỗi cái gây vấn đề gì?
11. ⭐ Nêu bước đầu tiên khi gỡ lỗi một liên kết Modbus, và vì sao nó tiết kiệm nhiều thời gian nhất.
12. Vì sao nên đọc **theo cụm** thay vì từng thanh ghi riêng? Điều kiện là gì?
13. Vì sao **không** được ghi điểm đặt mỗi lần công thức được nạp?
14. ⚠ Từ trạng thái của thiết bị phải khai kiểu gì, và khai nhầm thì triệu chứng là gì?

> Câu 3, 4, 5, 9 và 11 là năm câu phân loại. Câu 4 là tinh thần của cả chương: **đọc được một con số
> không có nghĩa là đọc đúng — và Modbus không có gì nói cho bạn biết bạn đang đọc nhầm.**

---

### Chương tiếp theo

Chương 40 — **Mạng Ethernet công nghiệp**. Modbus cho bạn mẫu số chung. Chương sau về các mạng chuyên
dụng — PROFINET, EtherNet/IP, EtherCAT — nhanh hơn, xác định thời gian hơn, và là thứ nối servo drive
của DP-01 với PLC.

### Nguồn tham khảo chương 39

- **Đặc tả Modbus** — *Modbus Application Protocol Specification* và *Modbus over Serial Line
  Specification*, công bố công khai bởi tổ chức quản lý chuẩn. ⭐ Đây là tài liệu gốc, **miễn phí và
  đáng đọc** — nó ngắn hơn nhiều so với đa số đặc tả giao thức.
- IEC 61158 / IEC 61784 — *Industrial communication networks*: Modbus nằm trong bộ tiêu chuẩn này.
  *(tiêu chuẩn có bản quyền)*
- **Tài liệu thiết bị tớ** — dùng cho ⚠ **bản đồ thanh ghi**, quy ước địa chỉ, ⚠ **thứ tự word cho
  giá trị 32 bit**, đơn vị của từng thanh ghi, và ⚠ **giới hạn số lần ghi**.
- **Tài liệu khối lệnh Modbus** của hệ PLC đang dùng — dùng cho ⚠ **quy ước địa chỉ ở chân khối**,
  vốn là tầng quy ước thứ ba có thể lệch (mục 39.4).
- Số liệu đã chốt của DP-01 — Phụ lục J §J.1.

> ⚡ Bản đồ thanh ghi ở mục 39.9 là **ví dụ minh hoạ cấu trúc**, không phải bản đồ của một thiết bị
> có thật. Bản đồ thật **luôn** phải lấy từ tài liệu của đúng model bạn dùng — và ⚠ nó có thể khác
> nhau giữa các phiên bản firmware của cùng một model.
>
> ⚠ Quy ước tiền tố `0xxxx`/`1xxxx`/`3xxxx`/`4xxxx` ở mục 39.4 là **quy ước truyền thống** rất phổ
> biến nhưng **không nằm trong đặc tả Modbus**. Nhiều tài liệu hiện đại ghi thẳng địa chỉ khung tin.
> Đó chính là lý do phải **thử và xác nhận** thay vì tin vào một quy ước duy nhất.
