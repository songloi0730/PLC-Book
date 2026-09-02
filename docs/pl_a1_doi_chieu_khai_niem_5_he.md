
# Phụ lục A1 — Đối chiếu khái niệm 5 hệ

> **Thân sách dạy khái niệm theo IEC 61131-3. Phụ lục A là nơi khái niệm đó gặp giao diện thật của
> từng hãng.**
>
> A1 đối chiếu **khái niệm**; **Phụ lục A2** đối chiếu **lệnh** và viết cùng một đoạn logic trên cả
> năm hệ.

---

> ⚠⚠ **ĐỌC TRƯỚC — giới hạn và mục đích**
>
> | | |
> |---|---|
> | ⭐ **Mục đích** | Giúp bạn **chuyển kiến thức** giữa các hệ, và đọc được tài liệu của hệ mình chưa dùng |
> | ⚠ **KHÔNG phải mục đích** | ⭐⭐ **Xếp hạng hãng.** Phụ lục này **mô tả khác biệt**, không nói hệ nào hơn |
> | ⚠⚠ **Giới hạn** | Chi tiết **thay đổi theo dòng sản phẩm và phiên bản phần mềm** — một hãng có thể có nhiều dòng làm khác nhau |
> | ⭐ **Cách dùng đúng** | Dùng bảng để **biết cần tìm gì**, rồi ⭐ **đọc tài liệu của dòng cụ thể bạn đang dùng** |
>
> ⚠ **Đừng dùng bảng này làm căn cứ kỹ thuật cho một dự án.** Dùng nó để định hướng, rồi xác nhận
> bằng tài liệu chính thức.

---

## A1.1 Năm hệ, và vì sao chọn năm hệ này

| Hệ | Phần mềm | Vì sao có mặt |
|---|---|---|
| **Siemens** | TIA Portal | ⭐ Phổ biến rộng ở châu Âu và Việt Nam |
| **Mitsubishi** | GX Works | ⭐ Phổ biến trong điện tử, ô tô ở châu Á |
| **Inovance** | AutoShop · InoProShop | ⭐ Xuất hiện nhiều ở Việt Nam gần đây |
| ⭐⭐ **CODESYS** | CODESYS Development System | ⭐ **CỘT NEO** — xem bên dưới |
| **Rockwell** | Studio 5000 | ⭐ Chiếm ưu thế ở Bắc Mỹ |

### ⭐⭐ Vì sao CODESYS là cột neo

Khi bốn hệ kia làm khác nhau, ⭐ **cột CODESYS cho biết chuẩn IEC 61131-3 nói gì**.

| | |
|---|---|
| ⭐ Bám chuẩn IEC sát nhất trong năm hệ | Nó **là** hiện thực tham chiếu của chuẩn |
| Nhiều hãng dùng nó làm nền | Nên học nó là học được nhiều nền cùng lúc |
| ⭐ Dùng để **phân biệt hai loại khác biệt** | Xem bên dưới |

> ⭐⭐ **Có hai loại khác biệt giữa các hệ, và phân biệt được chúng rất quan trọng:**
>
> | Loại | Nghĩa | Ví dụ |
> |---|---|---|
> | ⭐ **Khác về TÊN GỌI** | Cùng khái niệm, khác từ dùng | *"Data Block"* ↔ *"Global Variable List"* |
> | ⚠⚠ **Khác về HÀNH VI** | ⭐ **Khái niệm thật sự khác nhau** | Cách xử lý ảnh I/O, cách giữ dữ liệu qua mất điện |
>
> Loại đầu chỉ gây khó chịu khi đọc tài liệu. ⚠ **Loại sau gây lỗi khi chuyển chương trình giữa các
> hệ** — và là lý do Chương 56 nhấn mạnh phải kiểm thử đầy đủ dù "cùng logic".

---

## A1.2 Cách gọi tên biến và địa chỉ

| | Siemens | Mitsubishi | Inovance | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|---|
| **Cách chính** | ⭐ Tag có kiểu | ⭐ **Thiết bị** (device) | Thiết bị hoặc tag tuỳ dòng | ⭐ **Biến khai báo** | ⭐⭐ **Tag, không có địa chỉ vật lý** |
| Ngõ vào | `%I0.0` · tag | `X0` | `X0` hoặc `%IX0.0` | `%IX0.0` | Tag gán qua cấu hình |
| Ngõ ra | `%Q0.0` · tag | `Y0` | `Y0` hoặc `%QX0.0` | `%QX0.0` | Tag |
| Bit nội | `%M0.0` · tag | `M0` | `M0` | Biến `BOOL` | Tag `BOOL` |
| Thanh ghi | `%MW0` · DB | `D0` | `D0` | Biến `INT`/`WORD` | Tag |
| Bộ định thời | Khối `IEC_Timer` | ⭐ `T0` — **thiết bị riêng** | `T0` | Thể hiện `TON` | Tag `TIMER` |

> ⭐⭐ **Đây là khác biệt về HÀNH VI, không chỉ tên gọi.**
>
> Trong hệ kiểu **thiết bị** (Mitsubishi và các dòng nhỏ của Inovance), `D0` là **một ô nhớ có địa
> chỉ cố định**; bạn gán tên cho nó, nhưng ô nhớ vẫn ở đó và ⭐ **truy cập được bằng địa chỉ**.
>
> Trong hệ kiểu **tag thuần** (Rockwell ControlLogix), ⭐ **không có địa chỉ vật lý để truy cập** —
> tag là thực thể duy nhất, và bộ nhớ do hệ thống cấp phát.
>
> ⚠ **Hệ quả khi chuyển chương trình:** mã dựa vào việc *"D100 tới D149 nằm liền nhau"* — một cách
> viết rất phổ biến ở hệ kiểu thiết bị — ⭐ **không chuyển được trực tiếp** sang hệ tag thuần
> (Chương 56).

> ⭐ **Lời khuyên áp dụng cho MỌI hệ:** dùng **tên**, không dùng địa chỉ trực tiếp — kể cả trên hệ cho
> phép. `DI_BoardStn1` đọc được; `X12` thì không (Chương 24, Phụ lục B.10).

---

## A1.3 Tổ chức dữ liệu

| | Siemens | Mitsubishi | Inovance | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|---|
| **Gom biến toàn cục** | ⭐ **Data Block (DB)** | Vùng `D` + nhãn | Tuỳ dòng | ⭐ **Global Variable List (GVL)** | ⭐ **Controller Tags** |
| **Kiểu do người dùng định nghĩa** | ⭐ **UDT** | Structure (dòng mới) | Tuỳ dòng | ⭐ `TYPE ... STRUCT` | ⭐ **UDT** |
| **Biến cục bộ của khối** | Static / Temp trong khối | Ít dùng ở dòng cũ | Tuỳ dòng | `VAR` trong POU | Program Tags |
| **Mảng** | Có | Qua vùng `D` liên tiếp | Có | ⭐ `ARRAY[..] OF ..` | Có |

> ⭐⭐ **Khái niệm quan trọng nhất trong bảng này là kiểu do người dùng định nghĩa (UDT / STRUCT).**
>
> Nó cho phép bạn gom **mọi dữ liệu của một trạm** thành một kiểu, rồi tạo hai biến `Stn1` và `Stn2`
> cùng kiểu đó. Không có nó, bạn phải nhân đôi mọi biến bằng tay — và ⚠ **mỗi lần sửa phải nhớ sửa
> cả hai chỗ**.
>
> ⭐ Đây là nền của "mỗi trạm là một máy trạng thái độc lập" ở Chương 57 mục 57.6 và Chương 30.

> ⚠ **Với dòng PLC nhỏ đời cũ** (nhiều dòng của Mitsubishi và Inovance ở phân khúc nhỏ), ⭐ **kiểu do
> người dùng định nghĩa có thể không có**. Khi đó cách thay thế là **quy ước địa chỉ**: trạm 1 dùng
> `D100–D149`, trạm 2 dùng `D200–D249`, cùng độ lệch cho cùng ý nghĩa.
>
> ⭐ Nó hoạt động được, nhưng ⚠ **quy ước đó chỉ nằm trong đầu người viết** — nên phải ghi vào tài liệu
> (Chương 24).

---

## A1.4 Khối chương trình và thể hiện khối hàm

| | Siemens | Mitsubishi | Inovance | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|---|
| **Đơn vị chương trình** | OB · FB · FC | Chương trình chính + chương trình con | Tuỳ dòng | ⭐ **POU**: PROGRAM · FB · FUNCTION | ⭐ **Routine** trong Program |
| **Khối có bộ nhớ riêng** | ⭐ **FB + Instance DB** | ⚠ Dòng cũ: không có khái niệm này | Tuỳ dòng | ⭐ **Thể hiện FB** | ⭐ **Add-On Instruction (AOI)** |
| **Khối không bộ nhớ** | FC | Chương trình con | | FUNCTION | Routine thường |
| **Điểm vào chương trình** | OB1 (và OB khác) | Quét từ đầu chương trình chính | | ⭐ Task gọi PROGRAM | ⭐ **Task → Program → Routine** |

> ⭐⭐ **Đây là chỗ khác biệt lớn nhất giữa năm hệ, và là chỗ hay gây hiểu nhầm nhất.**
>
> | Câu hỏi cốt lõi | Vì sao quan trọng |
> |---|---|
> | ⭐ **Khối này có bộ nhớ riêng theo từng lần dùng không?** | ⚠ Nếu **không**, thì dùng cùng một khối ở hai chỗ sẽ **ghi đè lẫn nhau** |
>
> Trên hệ có thể hiện (Siemens FB, CODESYS FB, Rockwell AOI): mỗi lần dùng khai báo một thể hiện
> riêng → hai chỗ độc lập.
>
> ⚠ Trên hệ **không có** khái niệm này (nhiều dòng nhỏ đời cũ): chương trình con dùng chung vùng nhớ
> → ⭐ **bạn phải tự quản lý bằng cách truyền địa chỉ hoặc dùng độ lệch** — và ⚠ **quên điều đó là một
> lỗi rất khó tìm**.
>
> Xem Chương 30 và Phụ lục B.9.

---

## A1.5 Task, chu kỳ và ảnh I/O

| | Siemens | Mitsubishi | Inovance | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|---|
| **Chạy tuần hoàn** | OB1 (chu kỳ tự do) | Quét tự do | Quét tự do | ⭐ Task chu kỳ hoặc tự do | ⭐ **Continuous Task** |
| **Chạy theo chu kỳ cố định** | OB chu kỳ | Chương trình ngắt định kỳ | Ngắt định kỳ | ⭐ **Cyclic task có chu kỳ đặt** | ⭐ **Periodic Task** |
| **Ngắt sự kiện** | OB ngắt | Chương trình ngắt | Ngắt | Event task | Event Task |
| **Nhiều task ưu tiên khác nhau** | Có | ⚠ Hạn chế ở dòng nhỏ | Tuỳ dòng | ⭐ Có | ⭐ Có |
| ⭐ **Ảnh I/O** | ⭐ Đọc đầu · ghi cuối vòng quét | Đọc đầu · ghi cuối | Đọc đầu · ghi cuối | Theo cấu hình task | ⭐⭐ **Cập nhật KHÔNG đồng bộ với quét** |

> ⚠⚠ **Hàng cuối là khác biệt về HÀNH VI có hậu quả thật.**
>
> Mô hình cổ điển — đọc toàn bộ ngõ vào ở đầu vòng quét, chạy chương trình, ghi toàn bộ ngõ ra ở cuối
> — làm cho ⭐ **giá trị ngõ vào KHÔNG đổi trong suốt một vòng quét** (Chương 7).
>
> ⚠ Ở hệ mà I/O cập nhật không đồng bộ với việc quét chương trình (đặc trưng của Rockwell
> ControlLogix), giả định đó **không còn đúng** — cùng một tag ngõ vào có thể cho hai giá trị khác
> nhau ở hai chỗ trong một lần quét.
>
> ⭐ **Hệ quả thực dụng:** khi cần một giá trị nhất quán trong một đoạn logic, hãy **sao chép nó vào
> một biến ở đầu đoạn** và dùng biến đó. ⭐ Cách này đúng trên **mọi** hệ, nên đáng làm thành thói
> quen.

---

## A1.6 Vùng nhớ giữ qua mất điện

| | Siemens | Mitsubishi | Inovance | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|---|
| **Cách khai báo** | Đánh dấu retentive cho vùng M / DB | ⭐ **Dải thiết bị được cấu hình là latched** | Dải thiết bị latched | ⭐ `VAR RETAIN` · `VAR PERSISTENT` | ⭐ Thuộc tính của tag |
| **Cần pin hay không** | Tuỳ dòng | ⚠ **Dòng cũ thường cần pin** | Tuỳ dòng | Tuỳ phần cứng | Tuỳ dòng |
| ⚠ **Sống sót qua nạp chương trình?** | ⚠⚠ **PHẢI KIỂM** | ⚠⚠ **PHẢI KIỂM** | ⚠⚠ **PHẢI KIỂM** | ⚠ `RETAIN` vs `PERSISTENT` khác nhau ở chính điểm này | ⚠⚠ **PHẢI KIỂM** |

> ⚠⚠ **Hàng cuối là một trong những cái bẫy đắt nhất trong cả cuốn sách.**
>
> Rất nhiều người thiết lập bộ đếm bảo trì hoặc bộ đếm sản lượng vào vùng nhớ giữ được, chạy ba năm,
> rồi phát hiện nó **về không sau một lần nạp chương trình**.
>
> ⭐⭐ **Cách kiểm duy nhất đáng tin: nạp thử chương trình lên máy và xem giá trị còn không.** Đọc tài
> liệu là chưa đủ — hành vi khác nhau giữa "nạp thay đổi nhỏ", "nạp toàn bộ", và "nạp kèm cấu hình
> phần cứng".
>
> Xem Chương 12 và Chương 53 mục 53.5.

> ⭐ **Trên CODESYS, `RETAIN` và `PERSISTENT` là hai thứ khác nhau** — và sự khác nhau chính nằm ở
> việc giá trị có sống sót qua các thao tác tải xuống hay không. ⚠ Đọc kỹ tài liệu phiên bản bạn dùng.

---

## A1.7 Cấu hình phần cứng và đánh địa chỉ module

| | Siemens | Mitsubishi | Inovance | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|---|
| **Cấu hình** | Trong dự án, dạng giá đỡ trực quan | Cấu hình tham số PLC | Trong dự án | ⭐ Cây thiết bị | ⭐ I/O Configuration |
| **Địa chỉ module** | ⭐ Gán được, thường tự động theo khe cắm | ⭐ **Theo vị trí khe cắm** | Theo khe cắm | Theo cây thiết bị | ⭐⭐ **Tag theo tên module** |
| ⚠ **Đổi khe cắm thì sao?** | ⚠ Địa chỉ dịch — ⭐ **nếu dùng tag thì chương trình không phải sửa** | ⚠⚠ **Địa chỉ dịch, phải sửa** | ⚠ Địa chỉ dịch | Cập nhật ánh xạ | ⭐ Tag giữ nguyên |

> ⭐⭐ **Đây là lý do rất thực dụng để dùng TÊN thay vì địa chỉ trực tiếp trên mọi hệ.**
>
> Thêm một module vào giữa giá đỡ, hoặc thay một module hỏng bằng module có số kênh khác, ⚠ **làm
> dịch địa chỉ của mọi module phía sau**. Nếu chương trình viết bằng địa chỉ trực tiếp, bạn phải sửa
> **mọi chỗ** — và ⭐ **bỏ sót một chỗ nghĩa là một ngõ ra sai điều khiển một cơ cấu sai**.
>
> ⭐ Với tên và ánh xạ tập trung, bạn sửa **một chỗ** (Chương 24, 56).

---

## A1.8 ⭐ Bảng dịch nhanh — cùng khái niệm, khác tên

| Khái niệm IEC | Siemens | Mitsubishi | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|
| Đơn vị tổ chức chương trình | OB / FB / FC | Chương trình / chương trình con | ⭐ **POU** | Program / Routine |
| Khối hàm có bộ nhớ | FB + Instance DB | (dòng mới: FB) | ⭐ **Function Block** | Add-On Instruction |
| Biến toàn cục | Tag table · DB | Thiết bị `D`, `M` | ⭐ **GVL** | Controller Tags |
| Kiểu tự định nghĩa | UDT | Structure | ⭐ **STRUCT** | UDT |
| Chương trình chạy tuần hoàn | OB1 | Chương trình chính | ⭐ Task + PROGRAM | Continuous Task |
| Ngõ vào số | `%I` | `X` | `%IX` | Tag module |
| Ngõ ra số | `%Q` | `Y` | `%QX` | Tag module |
| Bit nội | `%M` | `M` | Biến `BOOL` | Tag `BOOL` |
| Thanh ghi 16 bit | `%MW` | `D` | Biến `WORD`/`INT` | Tag `INT` |
| Giữ qua mất điện | Retentive | Latched | ⭐ `RETAIN` / `PERSISTENT` | Tag retentive |
| Cưỡng bức | Force | Force | Force · Write | ⭐ Force · Toggle |

> ⭐ **Cách dùng bảng này:** khi đọc tài liệu của một hệ bạn chưa dùng, tra từ lạ ở đây để tìm ⭐ **khái
> niệm tương ứng bạn đã biết**. Phần lớn khác biệt tan biến khi bạn nhận ra đó chỉ là tên khác.
>
> ⚠ **Nhưng đừng cho rằng mọi khác biệt đều là tên gọi** — bốn chỗ ở A1.2, A1.4, A1.5 và A1.6 là khác
> biệt thật về hành vi.

---

## A1.9 ⭐⭐ Bốn khác biệt về hành vi — tóm tắt

Nếu bạn chỉ nhớ bốn điều từ phụ lục này:

| # | Khác biệt | ⚠ Hậu quả nếu bỏ qua | Mục |
|---|---|---|---|
| 1 | ⭐ **Địa chỉ vật lý có tồn tại không** | Mã dựa vào ô nhớ liền nhau ⚠ **không chuyển được** sang hệ tag thuần | A1.2 |
| 2 | ⭐⭐ **Khối có bộ nhớ riêng theo thể hiện không** | ⚠ Dùng ở hai chỗ → **ghi đè lẫn nhau** | A1.4 |
| 3 | ⭐ **Ảnh I/O có cố định trong một vòng quét không** | ⚠ Một tag cho hai giá trị khác nhau trong cùng vòng quét | A1.5 |
| 4 | ⭐⭐ **Vùng nhớ giữ được có sống sót qua nạp chương trình không** | ⚠⚠ **Bộ đếm ba năm về không** | A1.6 |

> ⭐⭐ **Bốn điều này là lý do Chương 56 nói: "cùng logic không có nghĩa là cùng hành vi".**
>
> Công cụ chuyển đổi tự động của hãng dịch được **cú pháp**. Nó ⚠ **không kiểm được** bốn điểm trên —
> và cũng không kiểm được thời gian quét, tràn số, hay hành vi bộ định thời. Vì thế chương trình
> chuyển nền phải được **kiểm thử đầy đủ như thể viết mới**.

---

## A1.10 Dẫn về đâu

| Bạn cần | Đọc |
|---|---|
| ⭐ **Đối chiếu LỆNH và cùng một đoạn logic viết 5 lần** | ⭐ **Phụ lục A2** |
| Khái niệm gốc theo chuẩn IEC | Chương 13–21, 30 · **Phụ lục B** |
| Vì sao vòng quét quan trọng | Chương 7 |
| ⚠ Chuyển chương trình sang nền mới | ⚠ **Chương 56 mục 56.4** |
| Vùng nhớ giữ được | Chương 12 · Chương 53 mục 53.5 |

---

> ⚠⚠ **Nhắc lại, vì đây là điều dễ hiểu sai nhất về phụ lục này.**
>
> A1 **mô tả khác biệt, không xếp hạng hãng.** Mỗi hệ ở đây được thiết kế cho một bối cảnh và có lý do
> riêng cho các lựa chọn của nó. ⭐ **Hệ tốt nhất cho bạn thường là hệ mà nơi bạn làm việc đang dùng,
> và bạn có người để hỏi.**
>
> ⚠ Chi tiết trong mọi bảng ở đây phụ thuộc **dòng sản phẩm và phiên bản phần mềm cụ thể**. Trước khi
> dựa vào bất kỳ hàng nào cho một dự án, ⭐ **xác nhận bằng tài liệu chính thức của dòng bạn đang
> dùng** — và với những điểm ở A1.9, ⭐⭐ **xác nhận bằng cách thử thực tế trên máy**.
