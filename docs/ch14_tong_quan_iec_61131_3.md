# Chương 14 — Tổng quan IEC 61131-3

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 14.1 Vì sao có một chuẩn, và nó thật sự cho bạn cái gì

Trước khi có chuẩn, mỗi hãng PLC là một thế giới riêng: ngôn ngữ riêng, tên lệnh riêng, cách tổ chức
chương trình riêng. Chuyển hãng nghĩa là học lại từ đầu.

**IEC 61131-3** ra đời để chấm dứt chuyện đó. Nó định nghĩa năm ngôn ngữ, một cách tổ chức chương
trình, và một bộ kiểu dữ liệu chung. Ngày nay gần như mọi hãng đều tuyên bố tuân theo nó.

Nhưng có một điều phải nói thẳng ngay từ đầu, vì hiểu nhầm nó sẽ dẫn tới những kỳ vọng sai:

> ⚠ **Chuẩn làm cho KỸ NĂNG của bạn chuyển được giữa các hệ. Nó hiếm khi làm cho CODE chuyển được.**

Bạn học ladder, timer, bộ đếm, máy trạng thái ở một hệ rồi chuyển sang hệ khác — kiến thức đi theo
bạn gần như trọn vẹn, và bạn làm việc được sau vài ngày làm quen. Đó là giá trị thật của chuẩn, và
nó rất lớn.

Nhưng lấy tệp chương trình từ hệ này nạp sang hệ khác thì **không chạy**. Mục 14.6 nói vì sao.

---

## 14.2 Năm ngôn ngữ — và vì sao cần tới năm

Chuẩn định nghĩa năm ngôn ngữ. Không phải vì thừa, mà vì **năm nhóm bài toán khác nhau**, và ép tất
cả vào một ngôn ngữ thì luôn có nhóm bị thiệt.

| Ngôn ngữ | Dạng | Sinh ra cho | Chương |
|---|---|---|---|
| **LD** — *Ladder Diagram* | Đồ hoạ, giống sơ đồ mạch rơ-le | Logic nhị phân, liên động, điều khiển ngõ ra | 15 |
| **FBD** — *Function Block Diagram* | Đồ hoạ, các khối nối bằng đường tín hiệu | Luồng tín hiệu, xử lý analog, chuỗi khối chức năng | 21 |
| **ST** — *Structured Text* | Văn bản, giống Pascal | Tính toán, thuật toán, mảng, máy trạng thái | 20 |
| **SFC** — *Sequential Function Chart* | Đồ hoạ, bước và chuyển tiếp | **Trình tự** có thứ tự trước sau | 21, 26 |
| **IL** — *Instruction List* | Văn bản, giống hợp ngữ | ⚠ Di sản — chỉ để **đọc** chương trình cũ | 21 |

### Chọn ngôn ngữ theo bài toán

| Bài toán | Ngôn ngữ hợp nhất | Vì sao |
|---|---|---|
| "Van chỉ mở khi cửa đóng và có khí và không lỗi" | **LD** | Liên động nhìn thấy được; người bảo trì chẩn đoán bằng mắt |
| "Nếu tín hiệu vượt ngưỡng thì lọc rồi đưa qua bộ điều khiển" | **FBD** | Luồng tín hiệu đi từ trái sang phải, thấy được đường đi |
| "Tính hiệu suất, quy đổi thang đo, xử lý mảng" | **ST** | Ladder làm việc này rất tệ |
| "Bước 10 chờ board, bước 20 nâng kẹp, bước 30…" | **SFC** hoặc **ST (`CASE`)** | Trình tự là cấu trúc, không phải logic tổ hợp |
| "Đọc chương trình máy 1998 để sửa" | **IL** | Không có lựa chọn — xem mục 21 |

> ⚠ **Nhắc lại quy tắc quan trọng nhất về chọn ngôn ngữ** (Chương 20, mục 20.6):
> **chọn theo người sẽ SỬA chương trình, không theo người viết nó.** Bảng trên nói cái gì *hợp*; câu
> hỏi "ai sẽ mở nó ra lúc hai giờ sáng" mới là câu quyết định.

> 💡 **Không phải chọn một ngôn ngữ cho cả dự án.**
> Mọi hệ hiện đại cho phép **mỗi khối một ngôn ngữ**. Đó chính là điều kiện để làm được bảng phân
> chia ở Chương 20: liên động và ngõ ra bằng LD, trình tự bằng ST hoặc SFC, tính toán bằng ST.

---

## 14.3 ⭐ POU — ba loại đơn vị tổ chức chương trình

Đây là khái niệm trung tâm của chuẩn, và là thứ phân biệt người hiểu chuẩn với người chỉ biết gõ lệnh.

**Đơn vị tổ chức chương trình** *(Program Organization Unit, POU)* là một mẩu chương trình có thể gọi
được. Chuẩn có ba loại, và **điểm phân biệt duy nhất là bộ nhớ**:

| Loại POU | Có bộ nhớ riêng? | Nghĩa là |
|---|---|---|
| **Function** *(hàm, FUN)* | **Không** | Cùng đầu vào luôn cho cùng đầu ra. Không nhớ gì giữa các lần gọi |
| **Function Block** *(khối chức năng, FB)* | ⭐ **Có** | Nhớ trạng thái giữa các lần gọi. Mỗi chỗ dùng cần một **thể hiện** riêng |
| **Program** *(chương trình, PRG)* | Có | POU mức cao nhất, được gán vào một tác vụ để chạy |

### Vì sao "có bộ nhớ hay không" là câu hỏi quan trọng

Xét hai thứ bạn đã dùng nhiều lần:

```iecst
// ABS là FUNCTION — không cần nhớ gì
AbsValue := ABS(Deviation);          // gọi bao nhiêu lần cũng được, không cần khai báo gì

// TON là FUNCTION BLOCK — phải nhớ đã đếm tới đâu
VAR
    T_Step20 : TON;                  // ⭐ phải khai báo một THỂ HIỆN
END_VAR
T_Step20(IN := (Stn1_Step = 20), PT := T#3S);
```

`ABS` không cần nhớ gì — đưa vào −5 thì luôn ra 5. `TON` **phải** nhớ nó đã đếm được bao lâu, và bộ
nhớ đó nằm ở **thể hiện** *(instance)* `T_Step20`.

> ⚠⚠ **Đây là gốc của một nhóm bẫy đã gặp ba lần trong sách.**
> Dùng chung một thể hiện FB cho hai việc khác nhau thì hai việc **ghi đè bộ nhớ của nhau**:
> - Chương 16, Bẫy 2 — hai tín hiệu dùng chung một khối bắt cạnh;
> - Chương 18 — hai bộ đếm dùng chung một thể hiện;
> - Chương 20, Bẫy 7 — hai bước dùng chung một timer.
>
> Cả ba là **cùng một lỗi**, và bây giờ bạn biết tên của nó: **dùng chung thể hiện của khối chức
> năng**. Quy tắc: **mỗi chỗ dùng, một thể hiện riêng.** Không có ngoại lệ.

### Thể hiện — hiểu bằng một hình ảnh

Khối chức năng là **bản thiết kế**; thể hiện là **cái máy được làm ra từ bản thiết kế đó**.

```text
   FB "TON"  ← bản thiết kế: biết cách đếm thời gian
      │
      ├── thể hiện T_Step20   ← bộ nhớ riêng: đang đếm tới 1,2 s
      ├── thể hiện T_Step40   ← bộ nhớ riêng: chưa bắt đầu
      └── thể hiện T_AirLow   ← bộ nhớ riêng: đã xong
```

Ba thể hiện dùng chung một bản thiết kế, nhưng **mỗi cái nhớ việc của mình**. Nếu bạn chỉ tạo một thể
hiện rồi dùng cho cả ba chỗ, cả ba cùng ghi vào một mẩu bộ nhớ — và không cái nào đúng.

### ⚠ "FB có bộ nhớ" đúng với THỂ HIỆN, không đúng với mọi biến bên trong nó

Có một loại biến ⭐ **không nhớ gì cả, kể cả khi nằm trong một FB**:

| Từ khoá | Hành vi giữa hai lần gọi |
|---|---|
| `VAR` (trong FB) | ⭐ **Giữ giá trị** — đây là bộ nhớ của thể hiện |
| ⚠⚠ `VAR_TEMP` | ⭐ **Khởi tạo lại mỗi lần gọi POU** — giá trị lần trước **mất sạch** |

> ⚠⚠ **Bẫy:** khai một biến đếm bằng `VAR_TEMP` rồi cộng dồn vào nó. Nó **không bao giờ cộng được** —
> mỗi lần gọi, biến quay về giá trị khởi tạo của kiểu. ⚠ Không có báo lỗi; chỉ có một con số mãi
> không tăng.
>
> ⭐ Ngược lại, `VAR_TEMP` là **lựa chọn đúng** cho biến trung gian dùng xong bỏ — biến đếm vòng lặp,
> kết quả tạm của một phép tính. Nó nói rõ ý định *"cái này không mang thông tin sang lần sau"*, và
> ⭐ **tránh được đúng loại lỗi ở Chương 11 mục 11.7** (hai POU vô tình chia nhau một biến).

### ⭐ Ba hướng tham số — và hướng thứ ba ít ai biết

Khi khai báo giao diện của một POU, chuẩn có **ba** hướng, không phải hai:

| Từ khoá | Chiều | ⭐ Truyền cái gì |
|---|---|---|
| `VAR_INPUT` | Vào | **Bản sao giá trị** — POU được gọi không sửa được biến gốc |
| `VAR_OUTPUT` | Ra | Kết quả trả về cho bên gọi |
| ⭐⭐ `VAR_IN_OUT` | **Vào và ra cùng lúc** | ⭐ **Chính vị trí bộ nhớ** — POU được gọi **sửa thẳng biến của bên gọi** |

> ⭐⭐ **Vì sao `VAR_IN_OUT` quan trọng khi chương trình lớn lên:**
>
> | Tình huống | Với `VAR_INPUT`/`VAR_OUTPUT` | ⭐ Với `VAR_IN_OUT` |
> |---|---|---|
> | FB cần **sửa một `STRUCT`** của bên gọi | Phải chép vào, sửa, chép ra — ⚠ hai bản dễ lệch nhau | Sửa thẳng, **một bản duy nhất** |
> | Truyền một **mảng lớn** | ⚠ Chép cả mảng mỗi lần gọi | ⭐ Chỉ truyền chỗ nó nằm |
>
> ⭐ Đây chính là công cụ cho mẫu **"một FB trạm, dùng cho nhiều trạm"** ở Chương 27, và cho việc
> ⭐ **truyền cả bản ghi công thức vào một khối xử lý** ở Chương 29 — thay vì liệt kê ba mươi tham số
> đầu vào rời rạc.
>
> ⚠ **Cái giá:** vì POU sửa thẳng biến gốc, ⭐ **bạn mất tính chất "gọi hàm không có tác dụng phụ"**.
> Khi đọc code người khác, một tham số `VAR_IN_OUT` nghĩa là ⚠ **giá trị của bạn có thể đã bị đổi sau
> lời gọi** — điều mà `VAR_INPUT` bảo đảm là không.

### Khi nào viết FB của riêng mình

Khi bạn thấy mình **chép đi chép lại cùng một đoạn logic cho nhiều đối tượng giống nhau**.

Trên DP-01 có bốn xy-lanh hai vị trí — hai chặn, hai kẹp — và logic điều khiển chúng giống hệt nhau:
ra lệnh, chờ phản hồi, timeout thì báo lỗi. Thay vì viết bốn lần, viết **một FB** rồi tạo **bốn thể
hiện**:

```iecst
VAR
    Cyl_Stop1  : FB_Cylinder2Pos;
    Cyl_Clamp1 : FB_Cylinder2Pos;
    Cyl_Stop2  : FB_Cylinder2Pos;
    Cyl_Clamp2 : FB_Cylinder2Pos;
END_VAR
```

Sửa một lỗi trong FB là sửa cho cả bốn. Chương 27 và Chương 30 nói kỹ cách viết FB dùng lại được.

---

## 14.4 Tác vụ — chương trình chạy khi nào

**Tác vụ** *(task)* quyết định POU nào chạy, chạy khi nào, và với mức ưu tiên nào.

| Loại tác vụ | Chạy khi | Dùng cho |
|---|---|---|
| **Chu kỳ** *(cyclic / periodic)* | Đều đặn theo chu kỳ đặt trước | Phần lớn logic máy |
| **Sự kiện** *(event / interrupt)* | Khi có sự kiện — sườn tín hiệu, lỗi phần cứng | Việc cần đáp ứng nhanh, không chờ được vòng quét |
| **Tự do** *(freewheeling / continuous)* | Chạy xong lại chạy tiếp, không có chu kỳ cố định | Chương trình chính ở các hệ đơn giản |

Ba điều cần nhớ:

- **Tác vụ chu kỳ ngắn hơn không phải lúc nào cũng tốt hơn.** Chu kỳ 1 ms cho logic không cần nhanh
  chỉ làm CPU bận và đẩy các tác vụ khác ra rìa.
- ⚠ **Tác vụ có mức ưu tiên.** Tác vụ ưu tiên cao chen ngang tác vụ ưu tiên thấp. Nếu hai tác vụ cùng
  ghi vào một biến, kết quả phụ thuộc thời điểm chen ngang — một loại lỗi rất khó tái hiện.
- **Mỗi tác vụ có watchdog riêng** ở nhiều hệ (Chương 20, mục 20.8).

> 💡 Với máy cỡ DP-01, **một tác vụ chu kỳ là đủ**. Chỉ thêm tác vụ khi có lý do đo được — ví dụ cần
> đọc một tín hiệu nhanh hơn chu kỳ chính, và bạn đã xác nhận bằng số liệu chứ không phải bằng cảm
> giác (Chương 10).

---

## 14.5 Kiểu dữ liệu — bảng tra nhanh

Chuẩn định nghĩa một bộ kiểu dữ liệu chung. Chương 11 nói kỹ; đây là bảng để bạn nhận mặt.

| Nhóm | Kiểu | Ghi chú |
|---|---|---|
| Nhị phân | `BOOL` | Một bit — đúng/sai |
| Số nguyên | `SINT` `INT` `DINT` `LINT` | 8 / 16 / 32 / 64 bit, có dấu |
| Số nguyên không dấu | `USINT` `UINT` `UDINT` | |
| Bit gộp | `BYTE` `WORD` `DWORD` | Dùng như một nhóm bit, không phải như số |
| Số thực | `REAL` `LREAL` | 32 / 64 bit — ⚠ không so sánh bằng (Chương 19) |
| Thời gian | `TIME` `DATE` `TIME_OF_DAY` | `TIME` viết dạng `T#2S`, `T#500MS` |
| Chuỗi | `STRING` `WSTRING` | Ít dùng ở tầng máy; hay gặp khi nối mạng (Chương 42) |
| Người dùng tự định nghĩa | `STRUCT`, `ARRAY`, kiểu liệt kê | Chương 11, Chương 30 |

---

## 14.6 ⭐ Sự thật về "tính khả chuyển"

Đây là mục mà người mới hay hiểu sai, và hiểu sai nó dẫn tới quyết định dự án sai.

### Cái gì chuyển được

| Chuyển được | Mức độ |
|---|---|
| **Kiến thức và kỹ năng của bạn** | ⭐ Gần như trọn vẹn |
| **Cấu trúc chương trình** — cách chia POU, cách tổ chức trình tự | Cao |
| **Thiết kế** — bảng I/O, máy trạng thái, mô tả trình tự | ⭐ Trọn vẹn, vì nó không phải code |
| Khái niệm ngôn ngữ — nấc thang, `CASE`, thể hiện FB | Cao |

### Cái gì **không** chuyển được

| Không chuyển được | Vì sao |
|---|---|
| **Tệp dự án** | Định dạng riêng của từng hãng, không có định dạng chung được dùng rộng rãi |
| **Địa chỉ và ánh xạ I/O** | Cách đánh địa chỉ khác nhau hoàn toàn (Chương 8, mục 8.4) |
| **Cấu hình phần cứng** | Gắn với đúng dòng CPU và module |
| **Lệnh mở rộng của hãng** | Mỗi hãng một bộ lệnh riêng ngoài chuẩn — và người ta dùng chúng rất nhiều |
| ⚠ **Chi tiết hành vi** | Chia cho 0, làm tròn, tràn số, biến giữ được — Chương 16, 19 đã cho thấy khác nhau tới mức nào |

### Vì sao thực tế lại như vậy

Chuẩn định nghĩa **ngôn ngữ**, không định nghĩa **định dạng tệp** hay **thư viện lệnh đầy đủ**. Mỗi
hãng hiện thực chuẩn rồi thêm phần mở rộng của mình — và phần mở rộng đó thường là phần tiện nhất,
nên người ta dùng, nên chương trình trở nên gắn chặt với hãng.

> ⚠ **Hệ quả thực tế cho dự án:**
> Đừng lập kế hoạch dựa trên giả định "sau này chuyển hãng cũng dễ". **Việc chọn hãng là một quyết
> định dài hạn** (Chương 13, tiêu chí 6 và 7), và chi phí đổi hãng giữa chừng là chi phí viết lại,
> không phải chi phí chuyển đổi.
>
> Ngược lại, **đừng sợ học một hãng cụ thể vì lo phí công**. Kỹ năng chuyển được; chỉ có tệp là không.

> 💡 **CODESYS là mốc đối chiếu hữu ích.**
> Nó bám chuẩn sát nhất và chạy trên phần cứng của nhiều hãng. Học trên đó thì bạn học **chuẩn**, ít
> lẫn phương ngữ của một hãng — nên khi chuyển sang hệ khác, bạn nhận ra ngay cái gì là chuẩn và cái
> gì là phần thêm của hãng. Đó là lý do sách dùng nó làm mốc.

---

## 14.6b ⭐⭐ "Tuân thủ IEC" là một BẢNG TÍCH, không phải một dấu tích

Mục 14.6 nói code không khả chuyển. Mục này nói một điều sắc hơn, và nó đổi cách bạn nói chuyện với
người bán hàng: ⭐ **"tuân thủ IEC 61131-3" không phải một tính chất có hoặc không.**

### Vì sao nó không thể là một dấu tích

⚠⚠ **Bộ lệnh mà chuẩn quy định là TUỲ CHỌN.** Chuẩn liệt kê một tập lệnh giới hạn; ⭐ hãng nào **có**
hiện thực lệnh đó thì phải làm đúng cách thực thi và cách biểu diễn đã quy định — nhưng chuẩn
**không bắt phải có**, và cũng **không giới hạn** hãng thêm lệnh của riêng mình.

Hệ quả, và đây là câu đáng nhớ:

> ⚠⚠ **Lệnh mở rộng của hãng không được chuẩn định nghĩa, nên KHÔNG có gì bảo đảm hai hãng hiện thực
> giống nhau — và dùng chúng có thể khiến logic không chuyển đi đâu được.**
>
> ⭐ Trớ trêu ở chỗ: lệnh mở rộng thường là **lệnh tiện nhất** — chẩn đoán, các phép điều khiển
> chuyên dụng, xử lý khối dữ liệu. Nghĩa là ⚠ **càng dùng những thứ giúp làm việc nhanh, chương
> trình càng dính chặt vào hãng.**

### Nên hỏi người bán hàng câu gì

Vì vậy hãng nghiêm túc **không** trả lời *"có, chúng tôi tuân thủ IEC"*. Họ đưa ra một **bảng tuân
thủ**, mỗi dòng là một đặc trưng của chuẩn, kèm cột ⭐ **"phần mở rộng và ghi chú hiện thực"**:

| Số bảng | Số đặc trưng | Mô tả đặc trưng | Phần mở rộng / ghi chú |
|---|---|---|---|
| … | … | Chú thích một dòng `// …` | *có, và hỗ trợ thêm `/* … */`* |
| … | … | Định danh có gạch dưới ở đầu | *áp cho tên tác vụ, chương trình, cấu trúc…* |

⭐⭐ **Câu hỏi đúng không phải *"có tuân thủ không"* mà là *"cho tôi xem bảng tuân thủ"*** — rồi đọc
cột cuối. Đó là chỗ mọi khác biệt thật nằm.

> ⚡ **Hai ví dụ cho thấy khác biệt nhỏ tới mức nào, và vẫn đủ gây chuyện:**
>
> | Chuẩn nói | Một hệ thực tế làm |
> |---|---|
> | Định danh phải hỗ trợ **tối thiểu sáu ký tự** | Hỗ trợ từ **một** ký tự — rộng hơn, nhưng ⚠ tên một ký tự sẽ **không chuyển ngược** sang hệ chỉ làm đúng mức tối thiểu |
> | ⚠ **Không quy định** đơn vị thời gian cho tác vụ chu kỳ | Đặt được từ **1 ms** — con số này là của hãng, ⚠ **không phải của chuẩn** (Chương 10) |
>
> ⭐ Cả hai đều là "tuân thủ". Cả hai đều là chỗ chương trình có thể vấp khi đổi hệ.

### ⭐ Có một định dạng trao đổi chung — nhưng nó không đến từ chuẩn

Mục 14.6 nói *"không có định dạng chung được dùng rộng rãi"*. Nói cho đủ: ⭐ **có một định dạng chung
tồn tại**, tên là **PLCopen XML** *(TC6 XML)* — và câu chuyện của nó giải thích chính xác vấn đề.

| | |
|---|---|
| Ai làm | ⭐ **PLCopen** — một tổ chức độc lập, ⚠ **không phải ban soạn thảo chuẩn** |
| Vì sao có | Người dùng muốn trao đổi chương trình giữa các môi trường phát triển — ⚠⚠ **"dù đó không phải chủ ý của bản thân chuẩn"** |
| Chở được gì | Chương trình, thư viện, cả dự án — ⭐ kể cả **thông tin đồ hoạ**, không chỉ văn bản |
| Dùng vào việc gì | Trao đổi giữa công cụ · ⭐ **đưa vào hệ quản lý phiên bản** · sinh tài liệu · công cụ kiểm tra · phân phối thư viện khối |

⚠ Và đây là phần trung thực mà chính đặc tả tự nói ra:

| ⚠ Giới hạn do chính đặc tả nêu | Nghĩa thực tế |
|---|---|
| Chuyển sang hệ khác *"có thể cần **một lượng công thủ công nhất định**"* | ⭐ Nó **giảm** công, **không xoá** công |
| Dùng song song nhiều hệ cũng *"có thể cần một lượng công thủ công"* | Không có chuyện xuất ra rồi nhập vào là xong |
| Nội dung xuất ra ⚠ *"có thể đang dở dang, nên **không có kiểm chứng** về tính áp dụng được, tính nhất quán hay tính đúng đắn"* | ⚠⚠ **Tệp XML hợp lệ không có nghĩa là chương trình chạy được** |

> ⭐⭐ **Chốt lại cho đúng, và đây là bản sửa cho một câu hay bị nói quá:**
>
> ⚠ Sai: *"IEC 61131-3 cho phép chuyển chương trình giữa các hãng."*
> ⭐ Đúng: **chuẩn không định nghĩa định dạng tệp — đó là một điểm yếu của nó** — nên một tổ chức
> độc lập đã làm một định dạng bù vào, và định dạng ấy ⭐ **giảm được công chuyển đổi, nhưng vẫn để
> lại phần việc tay.**
>
> ⚡ Giá trị lớn nhất của PLCopen XML với đa số người đọc sách này **không nằm ở việc đổi hãng** — mà
> ở chỗ nó biến chương trình thành **văn bản so sánh được và lưu trữ được** (Chương 30 mục 30.6).

---

## 14.7 Trên máy mẫu DP-01 — chương trình được tổ chức thế nào

Áp tất cả khái niệm của chương vào một bố cục cụ thể:

```text
   Tác vụ chu kỳ (ví dụ 10 ms)
      │
      ├── PRG_Main ─────────────── gọi các phần theo thứ tự
      │     │
      │     ├── PRG_Safety     (LD)  ── đọc trạng thái mạch an toàn, điều kiện cho phép
      │     ├── PRG_Mode       (ST)  ── máy trạng thái: chế độ máy (Ch.25)
      │     ├── PRG_Stn1Seq    (ST)  ── trình tự trạm 1 bằng CASE (Ch.26)
      │     ├── PRG_Stn2Seq    (ST)  ── trình tự trạm 2
      │     ├── PRG_Outputs    (LD)  ── ⭐ điều khiển ngõ ra cuối cùng, có liên động
      │     └── PRG_Stats      (ST)  ── đếm, tính chu kỳ, hiệu suất (Ch.19)
      │
      └── các thể hiện FB dùng chung:
            Cyl_Stop1, Cyl_Clamp1, Cyl_Stop2, Cyl_Clamp2  : FB_Cylinder2Pos
```

Bốn điều rút ra từ bố cục này:

- **Ngôn ngữ chọn theo từng phần**, đúng bảng phân chia ở Chương 20 mục 20.6. `PRG_Safety` và
  `PRG_Outputs` là LD vì đó là chỗ người bảo trì nhìn đầu tiên.
- **Thứ tự gọi có ý nghĩa.** An toàn và chế độ chạy trước, trình tự chạy giữa, ngõ ra chạy **cuối
  cùng** — để mọi quyết định đã xong trước khi ghi ra thế giới thật (Chương 10).
- **Ngõ ra được ghi ở đúng một chỗ**: `PRG_Outputs`. Trình tự chỉ đặt **yêu cầu** (`M_Stn1_ClampReq`),
  không chạm trực tiếp vào `DO_`. Đây là cách tránh lỗi ghi trùng một cách có hệ thống, chứ không
  dựa vào việc nhớ (Chương 15 Bẫy 1, Chương 20 Bẫy 2).
- **Bốn xy-lanh dùng chung một FB, bốn thể hiện riêng** — đúng quy tắc ở mục 14.3.

Bố cục này là thứ bạn sẽ xây dần qua các chương còn lại của Phần III và Phần IV.

---

## 14.8 Khác biệt giữa các hãng

Chuẩn thì chung; mức độ và cách hiện thực thì khác.

| Khía cạnh | Siemens | Mitsubishi | Rockwell | CODESYS / TwinCAT |
|---|---|---|---|---|
| Tên gọi ST | **SCL** | ST | ST | ST |
| POU mức chương trình | Khối tổ chức **OB**, cộng FC (hàm) và FB | Khối chương trình, FB, FUN | **Program** trong **Task**, gồm nhiều **Routine** | POU: PRG / FB / FUN |
| ⚠ Cách gọi POU chính | Chương trình chu kỳ nằm trong **OB1** | Chương trình chính quét tuần tự | ⭐ **Bắt buộc khai báo Task** và gán Program vào đó | **Bắt buộc khai báo Task** |
| Bộ nhớ thể hiện FB | Khối dữ liệu thể hiện *(instance DB)* | Vùng thiết bị được gán | Tag kiểu FB (Add-On Instruction) | Biến kiểu FB |
| Khối tự viết dùng lại | FB / FC | FB | **AOI** — *Add-On Instruction* | FB |
| SFC | **S7-GRAPH** | **SFC / MELSAP3** | Routine kiểu **SFC** | SFC |
| ⚠ Lệnh ngoài chuẩn | Rất nhiều, và rất tiện | Nhiều, gắn với mô hình thiết bị | Nhiều, mô hình tag rất mạnh | Ít nhất — bám chuẩn sát nhất |

> ⚠ **Hàng cuối là hàng giải thích vì sao code không chuyển được.**
> Bộ lệnh mở rộng của mỗi hãng chính là phần tiện nhất để dùng, nên chương trình thật gần như luôn
> chứa chúng. Chuẩn chỉ phủ phần lõi.

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

---

## 14.9 Bẫy thường gặp

### 🔍 BẪY 1 — Dùng chung một thể hiện khối chức năng

Bẫy trung tâm của chương, và đã xuất hiện ở Chương 16, 18, 20 dưới ba hình dạng khác nhau.

**Hiện tượng:** timer báo sai bước; bộ đếm nhảy loạn; bắt cạnh lúc được lúc không. Triệu chứng khó
đoán vì hai chỗ dùng ghi đè lẫn nhau theo thứ tự gọi.
**Cách sửa:** mỗi chỗ dùng một thể hiện riêng, đặt tên theo chỗ dùng (`T_Step20`, không phải `T1`).

### 🔍 BẪY 2 — Tưởng chuẩn nghĩa là chuyển được tệp dự án

**Hiện tượng:** lập kế hoạch dự án dựa trên giả định sai; hoặc bỏ nhiều ngày tìm cách chuyển đổi tự
động rồi vẫn phải viết lại tay.
**Cách sửa:** mục 14.6. Chuẩn cho **kỹ năng** khả chuyển, không cho **code** khả chuyển.

### 🔍 BẪY 3 — Viết một POU khổng lồ

**Hiện tượng:** một khối vài nghìn dòng làm mọi việc; không ai đọc nổi, không sửa được phần nào mà
không sợ hỏng phần khác.
**Cách sửa:** chia theo **chức năng** như bố cục ở mục 14.7. Mỗi POU trả lời một câu hỏi.

### 🔍 BẪY 4 — Chia POU theo bước trình tự

Viết `PRG_Step10`, `PRG_Step20`, `PRG_Step30`…

**Hiện tượng:** logic của cùng một xy-lanh nằm rải ở sáu khối; sửa hành vi của nó phải mở sáu chỗ.
**Cách sửa:** chia theo **cơ cấu**, không theo bước. Trình tự chỉ ra lệnh; cơ cấu tự lo phần của nó
(Chương 27, Chương 30).

### 🔍 BẪY 5 — Thêm tác vụ ưu tiên cao mà không nghĩ tới biến dùng chung

**Hiện tượng:** một biến thỉnh thoảng có giá trị "không thể xảy ra"; lỗi không tái hiện được, và biến
mất khi bạn thêm code để quan sát.
**Cách sửa:** hai tác vụ **không được cùng ghi** vào một biến. Nếu buộc phải trao đổi dữ liệu, dùng
đúng cơ chế mà hệ của bạn cung cấp cho việc đó.

### 🔍 BẪY 6 — Chọn ngôn ngữ theo sở thích cá nhân

**Hiện tượng:** không có triệu chứng nào — cho tới lần đầu máy hỏng lúc bạn vắng mặt.
**Cách sửa:** Chương 20, mục 20.6. Đây là quyết định thuộc đặc tả, và phải hỏi khách hàng.

### 🔍 BẪY 7 — Dùng hàm khi lẽ ra cần khối chức năng

Viết một hàm rồi mong nó nhớ trạng thái giữa các lần gọi.

**Hiện tượng:** giá trị "quên" mỗi vòng quét; logic đếm hoặc trễ không bao giờ hoạt động.
**Cách sửa:** cần nhớ thì phải là **khối chức năng** với thể hiện riêng. Hàm theo định nghĩa là không
có bộ nhớ (mục 14.3).

---

## 14.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Chuẩn có mấy ngôn ngữ | Năm: LD · FBD · ST · SFC · IL (IL là di sản) |
| Có phải chọn một ngôn ngữ cho cả dự án | **Không** — mỗi POU một ngôn ngữ |
| Phân biệt Function với Function Block | **Bộ nhớ**: hàm không có, khối chức năng có |
| Mỗi chỗ dùng khối chức năng cần gì | **Một thể hiện riêng** — không có ngoại lệ |
| Khi nào viết FB của mình | Khi chép đi chép lại cùng logic cho nhiều đối tượng giống nhau |
| Tác vụ quyết định gì | POU nào chạy, khi nào, ưu tiên bao nhiêu |
| Hai tác vụ cùng ghi một biến | ❌ Không được — lỗi khó tái hiện |
| Chuẩn làm gì khả chuyển | ⭐ **Kỹ năng và thiết kế** — không phải tệp dự án |
| Ngõ ra nên ghi ở đâu | **Đúng một POU**, chạy cuối cùng |
| ⚠⚠ `VAR_TEMP` | ⭐ **Khởi tạo lại mỗi lần gọi** — FB có bộ nhớ, biến này thì không |
| ⭐⭐ Hướng tham số thứ ba | **`VAR_IN_OUT`** — truyền **vị trí bộ nhớ**, POU sửa thẳng biến bên gọi |
| Khi nào cần `VAR_IN_OUT` | ⭐ FB sửa một `STRUCT` · truyền **mảng lớn** không muốn chép (Ch.27, Ch.29) |
| ⚠ Cái giá của `VAR_IN_OUT` | ⭐ **Mất bảo đảm "gọi xong biến của tôi không đổi"** |
| Chia POU theo gì | Theo **cơ cấu và chức năng**, không theo bước trình tự |

---

## 14.11 Tự kiểm

1. Kể năm ngôn ngữ của chuẩn và cho biết ngôn ngữ nào chỉ còn dùng để đọc chương trình cũ.
2. ⭐ Phân biệt **Function** với **Function Block**. Điểm phân biệt duy nhất là gì?
3. Vì sao `ABS` không cần khai báo gì trong khi `TON` phải khai báo một thể hiện?
4. ⭐ Ba bẫy ở Chương 16, 18 và 20 thực ra là **cùng một lỗi**. Lỗi đó tên là gì, và quy tắc phòng
   tránh là gì?
5. Nêu ba loại tác vụ và cho biết loại nào dùng cho phần lớn logic máy.
6. Vì sao hai tác vụ không được cùng ghi vào một biến? Mô tả triệu chứng đặc trưng của lỗi này.
7. ⭐ Chuẩn IEC 61131-3 làm cho cái gì khả chuyển và cái gì **không** khả chuyển? Nêu ít nhất ba thứ
   mỗi bên.
8. Vì sao chương trình thật gần như luôn gắn chặt với một hãng, dù hãng đó tuân theo chuẩn?
9. Trong bố cục ở mục 14.7, vì sao `PRG_Outputs` chạy **cuối cùng** và vì sao nó là **nơi duy nhất**
   ghi vào các tag `DO_`?
10. ⭐ Vì sao chia POU theo **cơ cấu** tốt hơn chia theo **bước trình tự**? Nêu hậu quả cụ thể của
    cách chia sai.
11. ⚠⚠ Bạn khai một biến đếm bằng `VAR_TEMP` rồi cộng dồn. Nó không bao giờ tăng. ⭐ Vì sao, và
    `VAR_TEMP` thì **đúng** cho loại biến nào?
12. ⭐⭐ Nêu **ba** hướng tham số của một POU. Hướng thứ ba truyền cái gì khác hai hướng kia, và điều
    đó cho phép làm gì mà hai hướng kia không làm được?
13. ⭐ Nêu cái giá phải trả khi dùng `VAR_IN_OUT`. Khi **đọc code người khác**, thấy tham số kiểu này
    thì phải cảnh giác điều gì?

> Câu 2, 4 và 7 là ba câu phân loại. Câu 4 là tinh thần của cả chương: **nhiều bẫy trông khác nhau
> thật ra là một khái niệm chưa nắm chắc.**

---

### Chương tiếp theo

Chương 15 — **Ladder Diagram**. Chương này đã cho bạn bản đồ; từ đây đi vào từng ngôn ngữ, bắt đầu
bằng ngôn ngữ chiếm ưu thế ở tầng máy và cũng là ngôn ngữ có cái bẫy nguy hiểm nhất trong nghề.

### Nguồn tham khảo chương 14

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: định nghĩa năm ngôn ngữ,
  ba loại POU, mô hình tác vụ, và bộ kiểu dữ liệu chuẩn. *(tiêu chuẩn có bản quyền)*
- IEC 61131-1 — *Programmable controllers, Part 1: General information*: mô hình phần mềm tổng thể.
- Tài liệu lập trình của từng hệ trong Phụ lục A — dùng cho bảng đối chiếu ở mục 14.8: tên gọi POU,
  cách khai báo tác vụ, cơ chế bộ nhớ thể hiện, và tên gói SFC của từng hãng.
- **Rockwell Automation** — *Logix 5000 Controllers IEC 61131-3 Compliance* (1756-PM018): ⭐⭐ **bộ
  lệnh của chuẩn là TUỲ CHỌN**; lệnh mở rộng của hãng không được chuẩn định nghĩa nên ⚠ **không bảo
  đảm tương thích giữa các hãng**; ⚠⚠ **chuẩn không định nghĩa định dạng trao đổi tệp — tài liệu gọi
  thẳng đó là "điểm yếu"**; và **mẫu bảng tuân thủ theo từng đặc trưng** kèm cột *phần mở rộng và ghi
  chú hiện thực* — nền cho mục 14.6b. *(tài liệu của hãng; phần trích ở đây là phát biểu về CHUẨN,
  không phải về sản phẩm)*
- **PLCopen** — *TC6 XML technical documentation v2.01*: mục đích và bốn nhóm ca sử dụng của
  **PLCopen XML**, ⚠ kèm các giới hạn do chính đặc tả nêu — chuyển hệ *"có thể cần một lượng công thủ
  công nhất định"*, và nội dung xuất ra *"không có kiểm chứng về tính áp dụng được, tính nhất quán
  hay tính đúng đắn"*. *(tài liệu mở của PLCopen)*
- **Hanssen, Dag H.** — *Programmable Logic Controllers: A Practical Approach to IEC 61131-3 using
  CoDeSys*, §6.6: ba hướng tham số `VAR_INPUT` / `VAR_OUTPUT` / ⭐ **`VAR_IN_OUT`** (POU được gọi nhận
  **chính vị trí bộ nhớ** nên sửa được biến của bên gọi), và ⚠ **`VAR_TEMP`** — khởi tạo lại ở mỗi
  lần gọi POU nên **không mang được giá trị sang lần sau**.

> ⚡ ⭐ **Cập nhật:** nhận định ở mục 14.6 trước đây chỉ là **quan sát của nghề**. Nay nó **có nguồn**
> — và nguồn đến từ chính tài liệu tuân thủ của một hãng lớn, chứ không phải từ người phê bình:
> *"đây là một điểm yếu của IEC 61131-3, vì chuẩn không định nghĩa định dạng trao đổi tệp"*, và
> *"lệnh mở rộng… không có bảo đảm rằng hai hãng hiện thực tương thích; dùng chúng có thể khiến logic
> không chuyển được giữa các hãng"*. ⭐ Chi tiết ở mục 14.6b.
