# Phụ lục N — Quy ước viết mã

> **Mã mẫu trong sách này vốn đã viết theo một quy ước nhất quán — nhưng quy ước đó chưa từng được
> viết ra.** Phụ lục này viết nó ra, đối chiếu với một bộ quy tắc trung lập của ngành, và chỉ rõ chỗ
> sách **theo**, chỗ sách **lệch có chủ ý**, và chỗ sách **từng sai rồi đã sửa**.

---

## N.1 ⭐ Vì sao phải viết quy ước ra giấy

Một người viết một mình thì nhất quán **trong đầu**. ⚠ Một nhóm ba người thì không — và một chương
trình PLC sống lâu hơn nhóm đã viết nó (Chương 22, 30).

| Không có quy ước viết ra | Có quy ước viết ra |
|---|---|
| Mỗi người một kiểu, và **mỗi kiểu đều "đúng"** | Tranh luận một lần, rồi thôi |
| Người sau phải **đoán** ý người trước | Người sau **tra** được |
| Soát mã = soát khẩu vị | ⭐ Soát mã = soát theo danh mục |
| Không đo được | ⭐ **Đo được** — phần lớn quy tắc kiểm được bằng công cụ |

> ⭐⭐ **Quy ước là hợp đồng giữa người viết hôm nay và người đọc hai năm sau.** Hợp đồng chỉ có giá
> trị khi **được viết ra**.

---

## N.2 Bộ quy tắc dùng làm chuẩn: PLCopen Coding Guidelines

⭐ Sách dùng **PLCopen Coding Guidelines v1.0** (2016) làm chuẩn đối chiếu — một bộ quy tắc **trung
lập hãng**, viết riêng cho IEC 61131-3, miễn phí, và được soạn để làm **cơ sở cho quy ước nội bộ** của
từng đơn vị.

| Nhóm | Mã | Nội dung | Số quy tắc |
|---|---|---|---|
| Đặt tên | **N** | Tên biến, khối, kiểu, tác vụ | 10 |
| Chú thích | **C** | Chú thích nói gì, viết thế nào | 6 |
| Thực hành viết mã | **CP** | Khởi tạo, tác vụ, ngõ ra, kiểu dữ liệu, so sánh… | 28 |
| Ngôn ngữ | **L** | Riêng cho LD, FBD, SFC, ST | 17 |
| Phần mở rộng của hãng | **E** | Con trỏ, cấp phát bộ nhớ | 3 |

⭐ Mỗi quy tắc có một **mức ưu tiên**: **Cao**, **Trung bình**, **Thấp**.

> ⭐⭐ **Có hai loại quy tắc rất khác nhau, và phải phân biệt ngay từ đầu:**
>
> | Loại | Ví dụ | Nó đòi gì |
> |---|---|---|
> | **Quy định** | *"Mỗi ngõ ra vật lý chỉ ghi một lần mỗi vòng quét"* | Làm, hoặc không làm |
> | ⭐ **"Hãy tự định nghĩa…"** | *"Định nghĩa độ dài dòng tối đa"* | ⚡ **Bắt BẠN phải chọn** — tài liệu chỉ gợi ý |
>
> ⭐ Loại thứ hai là loại hay bị bỏ qua nhất: không ai cấm bạn chọn gì, nên người ta **không chọn gì
> cả**. Mục N.6 là câu trả lời của sách cho từng quy tắc loại này.

> ⚡ **Một chi tiết nhỏ khi đọc bản gốc:** bảng tổng hợp ở cuối tài liệu ghi mã **L22**, nhưng thân tài
> liệu gọi cùng quy tắc đó là **L12** — lỗi in trong chính tài liệu. Phụ lục này dùng **L12**.

---

## N.3 ⭐⭐ Các quy tắc mức CAO — và sách áp dụng ở đâu

⭐ Cột cuối: ✔ **theo** · ⭐ **sách từng sai, đã sửa** · ⚠ **lệch có chủ ý** (xem N.5) · ◯ **sách không
dùng tới** (quy tắc vẫn đúng) · ➕ **chưa chương nào bàn — quy tắc nêu tại phụ lục này**.

| Mã | Quy tắc | Sách dạy ở đâu | |
|---|---|---|:-:|
| N1 | Tránh địa chỉ vật lý viết cứng | Ch.11 mục 11.3 — dùng tag có tên | ✔ |
| N3 | Định nghĩa các từ phải tránh trong tên | Mục N.6 | ✔ |
| N4 | Cách dùng chữ hoa phải **rõ và nhất quán** | Mục N.5, N.6 | ⚠ |
| N5 | Tên cục bộ không được che tên toàn cục | Tiền tố vai trò (N.6) khiến gần như không thể trùng | ✔ |
| C1 | ⭐ Chú thích mô tả **Ý ĐỊNH** của mã, không kể lại mã | Ch.30 mục 30.4 | ✔ |
| C2 | Mọi POU, kiểu, biến đều có chú thích | Ch.30 mục 30.4 | ✔ |
| CP1 | Truy cập thành phần cấu trúc bằng **tên**, không bằng độ lệch | Ch.11 | ✔ |
| CP2 | Không có mã chết | Ch.22 | ✔ |
| CP3 | ⭐ Mọi biến được **gán trước khi đọc** — ở mọi chu kỳ: khởi động nguội, khởi động nóng, vòng quét đầu | Phụ lục M mục M.4 · Ch.20 (sửa ví dụ vòng lặp) | ⭐ |
| CP4 | Vùng nhớ địa chỉ trực tiếp không được chồng lấn | Phụ lục B mục B.10 | ⭐ |
| CP5 | Thiết kế ứng dụng **trước khi** viết | Ch.23, 27 | ✔ |
| CP6 | Tránh biến ngoài (`VAR_EXTERNAL`) trong hàm và khối | Ch.11 mục 11.6 — *"khối không đọc biến toàn cục, mọi thứ qua chân"* · Ch.30 mục 30.5 | ✔ |
| CP7 | Thông tin lỗi trả về phải được kiểm và xử lý | Ch.37 — ngõ ra `Error` của khối chuyển động | ✔ |
| CP8 | Không dùng `=` / `<>` với **số thực** | Ch.19 mục 19.3 | ✔ |
| CP28 | ⭐ Không dùng `=` / `<>` để dò ngưỡng **thời gian hay đại lượng đo — kể cả ở dạng số nguyên** | Ch.19 mục 19.3 | ⭐ |
| CP9 | Giới hạn độ phức tạp của mã trong một POU | Mục N.6 | ➕ |
| CP10 | Một biến chỉ được ghi từ **một** tác vụ | Ch.27 mục 27.6 | ✔ |
| CP11 | Quản lý đồng bộ khi các tác vụ chia sẻ dữ liệu | Ch.27 mục 27.6 — vùng đệm | ✔ |
| CP12 | ⭐ Mỗi ngõ ra vật lý chỉ ghi **một lần mỗi vòng quét** | Ch.22 · Ch.27 Bẫy 2 · Ch.57 khối `Prg_OutputMap` | ✔ |
| CP13 | Không dùng đệ quy | Sách không dùng; ⚠ đệ quy trên PLC là rủi ro tràn ngăn xếp | ◯ |
| CP14 | ⭐ POU chỉ có **một điểm thoát** — tránh `RETURN` | Phụ lục L mục L.6 · Ch.26 · Ch.29 | ⭐ |
| CP15 | Đọc một biến do tác vụ khác ghi **chỉ một lần mỗi vòng** | Ch.27 mục 27.6 | ✔ |
| CP16 | Tác vụ chỉ gọi `PROGRAM`, không gọi thẳng khối | Ch.57 — `PROGRAM Main` | ✔ |
| CP17 | Dùng tham số đúng chiều khai báo: vào thì đọc, ra thì ghi | Ch.14 | ✔ |
| CP18 | Hạn chế biến toàn cục | Ch.30 mục 30.5 | ✔ |
| L7 | Đóng đúng các nhánh song song trong SFC | Ch.26 mục 26.5 | ✔ |
| E1 | Không cấp phát bộ nhớ động | Sách không dùng | ◯ |
| E2 | Không tính toán trên con trỏ | Sách không dùng; áp cho `REFERENCE` ở Ch.30 | ◯ |
| E3 | Không dùng `<` `>` `<=` `>=` trên con trỏ hay tham chiếu | Như trên | ◯ |

> ⭐⭐ **Các dòng ⭐ là những chỗ sách TỪNG SAI hoặc THIẾU, và đều sửa trong cùng một đợt rà.** Soát mã
> mẫu theo đúng bộ quy tắc này tìm ra: khung trình tự dùng `RETURN` ở Phụ lục L và Ch.26 (CP14); một
> ví dụ vòng lặp ở Ch.20 đọc phần tử mảng **chưa được gán** (CP3); một câu ở Ch.19 nói *"với số
> nguyên thì `=` hoàn toàn an toàn"* (CP28); và ba bẫy chưa từng được dạy — **chồng lấn địa chỉ**
> (CP4), **sửa biến đếm của `FOR`** và **dùng nó sau vòng lặp** (L12, L13). ⭐ Soát tiếp bằng máy
> tìm thêm: sách có **hai khối khác nhau cùng tên `FB_Cylinder2Pos`** — ở Ch.27 và Phụ lục L, hai
> giao diện khác nhau — và một bản gọi bộ định thời **hai lần** trong một vòng quét (CP20).
>
> ⚡ Những lỗi đó đã nằm trong sách qua hơn năm mươi đợt rà. ⭐ **Không đợt nào tìm ra, vì không đợt nào
> có một danh mục bên ngoài để soát theo.**

---

## N.4 Các quy tắc mức TRUNG BÌNH và THẤP

### Mức trung bình

| Mã | Quy tắc | Sách | |
|---|---|---|:-:|
| N6 | Độ dài tên hợp lý | Mục N.6 | ✔ |
| N7 | Quy tắc đặt tên không gian tên *(namespace)* | Mục N.6 | ◯ |
| N8 | Định nghĩa bộ ký tự được dùng | Mục N.6 | ✔ |
| N9 | Các loại phần tử khác nhau không trùng tên trong cùng phạm vi | Tiền tố vai trò | ✔ |
| CP19 | Tránh nhảy và `RETURN` trong **LD và FBD** | Ch.15 mục 15.4b — vùng điều khiển | ✔ |
| CP20 | ⭐ Mỗi **thể hiện** khối chỉ gọi **một lần** mỗi vòng quét | Ch.14 mục 14.3 · Ch.17 Bẫy 5 · Ch.27 mục 27.3 — đếm lại từ đầu **mà không** gọi lần hai | ⭐ |
| CP21 | Dùng `VAR_TEMP` cho biến tạm | Ch.14 | ✔ |
| CP22 | Chọn kiểu dữ liệu hợp với **dải** và **độ chính xác** | Ch.11 Bẫy 2 — `INT` tràn | ✔ |
| CP23 | Giới hạn số chân vào/ra của một POU — gợi ý khoảng **10** | Ch.30 mục 30.5 · mục N.6 | ✔ |
| CP24 | Không khai báo biến không dùng | Mục N.6 | ✔ |
| CP25 | Ép kiểu **tường minh**, không để trình biên dịch tự thêm | Ch.19 | ✔ |
| L2 | Tránh gán kết quả trung gian **giữa chừng** một mạng FBD | Nêu tại đây | ➕ |
| L3 | Giới hạn độ phức tạp một mạng FBD | Mục N.6 | ✔ |
| L5 | Trong LD, **cuộn dây không đứng trước tiếp điểm** | Mục N.6 | ✔ |
| L6 | Giới hạn độ phức tạp một nấc thang | Mục N.6 | ✔ |
| L8 | Không viết **hành động** của SFC bằng chính SFC | Nêu tại đây | ➕ |
| L9 | Giới hạn độ phức tạp một sơ đồ SFC | Mục N.6 | ✔ |
| L10 | Tránh `CONTINUE` và `EXIT` trong ST | Ch.20 — trần vòng lặp đặt trong điều kiện | ⭐ |
| L11 | Định nghĩa độ dài dòng tối đa — gợi ý **80** ký tự | Mục N.6 | ⚠ |
| L12 | ⭐ **Không sửa biến điều khiển** của vòng `FOR` bên trong vòng | Ch.20 mục 20.5 | ⭐ |
| L13 | ⭐ **Không dùng biến điều khiển** của `FOR` sau khi vòng kết thúc — giá trị do hãng quyết định | Ch.20 mục 20.5 | ⭐ |
| L14 | Truyền tham số **rõ ràng** — gọi có tên từng chân | Mọi ví dụ gọi khối trong sách | ✔ |
| L15 | Dùng **ngoặc** khi thứ tự ưu tiên có thể gây hiểu lầm | Phụ lục B mục B.2 | ✔ |

### Mức thấp

| Mã | Quy tắc | Sách | |
|---|---|---|:-:|
| N2 | Tiền tố tên biến — nếu dùng thì định nghĩa rõ | Mục N.5 | ⚠ |
| N10 | Tiền tố tên kiểu người dùng | Mục N.6 — `FB_` · `ST_` · `E_` | ✔ |
| C3 | Tránh chú thích lồng nhau | Sách chỉ dùng `//` | ✔ |
| C4 | ⭐ Không để lại mã bị "chú thích bỏ đi" | Ch.22 | ✔ |
| C5 | Định nghĩa ký tự chú thích | Mục N.6 | ✔ |
| C6 | Định nghĩa ngôn ngữ viết chú thích | Mục N.6 | ✔ |
| CP26 | Một biến toàn cục chỉ do **một** `PROGRAM` ghi | Ch.22 — *"đúng một chỗ ghi"* | ✔ |
| CP27 | Tránh tính năng đã lỗi thời | Ch.21 — IL *"chỉ để đọc di sản"* | ✔ |
| L1 | Định nghĩa cách thụt lề | Mục N.6 | ✔ |
| L4 | Định nghĩa quy tắc trình bày chung | Mục N.6 | ✔ |
| L16 | Định nghĩa cách dùng ký tự tab | Mục N.6 | ✔ |
| L17 | Mọi `IF` nên có `ELSE` — **thấp**, nhưng **cao với phần mềm an toàn** | Mục N.5 | ⚠ |

---

## N.5 ⭐⭐ Chỗ sách lệch khỏi PLCopen — và vì sao

⚠ Lệch không phải là sai. ⭐ Chính tài liệu PLCopen nói nó là **cơ sở** để mỗi đơn vị tự định quy ước
— miễn là **chọn có lý do và viết ra**. Dưới đây là bốn chỗ sách chọn khác, kèm lý do.

### Chữ hoa — N4 · và tiền tố — N2

⭐ PLCopen **gợi ý**: viết HOA_CÓ_GẠCH cho hằng số và kiểu người dùng; viết `UpperCamelCase` cho tên
nhiều từ; và nếu có tiền tố thì chuyển sang `lowerCamelCase`. Sách chọn khác ở hai chỗ:

| | Gợi ý của PLCopen | Sách chọn | ⭐ Lý do |
|---|---|---|---|
| Tên có tiền tố | `diBoardStn1` | `DI_BoardStn1` | ⭐⭐ Tên tag trong sách **là chữ in trên nhãn trong tủ** và trên màn hình (Chương 44). Chữ HOA có gạch tách tiền tố đọc được từ xa, và khớp cách đánh số dây (Chương 49 mục 49.6; Chương 57) |
| Loại tiền tố | Thường là tiền tố **kiểu** — `x` cho BOOL, `i` cho INT | Tiền tố **vai trò** — `DI_` `DO_` `AI_` `M_` `T_` `Stn1_` | ⭐ Tiền tố vai trò trả lời câu người sửa máy cần hỏi nhất: *"tín hiệu này từ đâu tới?"* |

**Hai cách đặt tiền tố, cùng một biến — ưu và nhược:**

| Cách | Ví dụ | ⭐ Ưu | ⚠ Nhược |
|---|---|---|---|
| Tiền tố **kiểu** | `xClampUp` · `iCount` · `rPressure` | Biết kiểu mà không cần tra khai báo | ⚠ Đổi kiểu là **đổi tên ở mọi chỗ**; không nói gì về nguồn gốc tín hiệu |
| ⭐ Tiền tố **vai trò** | `DI_Clamp1Up` · `C_Board` · `AI_AirPress` | ⭐ Nói ngay **tín hiệu từ đâu**: ngõ vào thật, cờ nội bộ, bộ đếm | Không nói kiểu — nhưng phần mềm lập trình nào cũng hiện kiểu khi di chuột |

> ⭐ **Khuyến nghị:** máy có nhiều I/O, nhiều người bảo trì → **tiền tố vai trò**. Thư viện khối dùng lại
> ở nhiều dự án, không gắn I/O cụ thể → tiền tố kiểu cũng hợp lý. ⚠⚠ **Đừng trộn hai loại trong cùng
> một dự án** — đó mới là thứ quy tắc N4 thật sự cấm.

### Mọi `IF` có `ELSE` — L17

⭐ PLCopen xếp quy tắc này mức **thấp**, nhưng **cao với phần mềm an toàn**: viết `ELSE` buộc người
viết nghĩ tới trường hợp điều kiện sai. Mã mẫu của sách **không** theo nó ở mọi chỗ, vì chức năng an
toàn trong sách **không nằm trong chương trình PLC thường** (Chương 47, 48).

⚡ Nhưng sách **có** dùng tinh thần của nó ở chỗ quan trọng nhất: khi một nhánh **cố ý không làm gì**,
sách viết nhánh đó ra, kèm một câu lệnh rỗng và một chú thích — đúng cách tài liệu PLCopen minh hoạ:

```iecst
IF M_Paused OR NOT M_CycleEnable THEN
    ;                                    // ⭐ CỐ Ý không làm gì: giữ bước, giữ ngõ ra
ELSE
    // … thân trình tự …
END_IF;
```

> ⭐ **Khi nào nên áp L17 đầy đủ:** chương trình của **PLC an toàn**, và bất kỳ đoạn nào người thẩm định
> sẽ đọc từng dòng. Ở đó một nhánh `ELSE` bị bỏ sót là một câu hỏi không ai trả lời.

### Độ dài dòng — L11

⭐ PLCopen gợi ý **80 ký tự**. Trong 2489 dòng mã ST của sách, chỉ **3 dòng có phần mã vượt 80**; 65
dòng khác dài hơn 80 là vì **chú thích giảng giải** ở cuối dòng — thứ chỉ có trong sách dạy, không có
trong dự án thật.

⭐ **Trong dự án thật: giữ cả dòng, kể cả chú thích, dưới 80 ký tự.**

---

## N.6 ⭐⭐ Các quyết định "hãy tự định nghĩa" — câu trả lời của sách

⭐ Đây là danh mục quyết định mà **mọi đơn vị phải tự chốt**. Cột cuối là lựa chọn của sách, dùng
được làm điểm khởi đầu.

| Mã | Câu hỏi phải trả lời | Sách chọn |
|---|---|---|
| N2 | Có dùng tiền tố cho biến không, loại nào? | ⭐ Tiền tố **vai trò**: `DI_` `DO_` `AI_` `AO_` `AX_` `NET_` · `M_` cờ nội bộ · `T_` bộ định thời · `C_` bộ đếm · `Stn1_` biến của trạm · ⭐ tham số công thức **không** có tiền tố riêng: chúng là thành phần của cấu trúc `ActiveRecipe` kiểu `ST_Recipe` (Chương 29) — truy cập bằng tên, đúng CP1 |
| N3 | Từ nào **không** được dùng trong tên? | Từ khoá và tên lệnh chuẩn (`TON`, `MOVE`…) · từ mơ hồ không nói được gì: `Temp`, `Data`, `Test`, `Flag`, `Aux` |
| N4 | Viết hoa thế nào? | Tiền tố VIẾT HOA + `_` + `UpperCamelCase`: `DI_BoardStn1` · từ khoá VIẾT HOA: `IF`, `END_IF` |
| N6 | Tên dài bao nhiêu? | ⭐ Tag của máy mẫu dài nhất **16 ký tự**; nên giữ **≤ 25** như PLCopen gợi ý |
| N7 | Có dùng không gian tên không? | Không — không phải hệ nào cũng có (Chương 30) |
| N8 | Bộ ký tự cho tên? | ⭐ **Chữ Latinh không dấu, số, gạch dưới.** Tiếng Việt có dấu **chỉ** trong chú thích |
| N10 | Tiền tố cho kiểu người dùng? | `FB_` khối chức năng · `ST_` cấu trúc · `E_` kiểu liệt kê. ⚠ Tiền tố kiểu **không** dùng cho thể hiện: thể hiện của `FB_Cylinder2Pos` tên là `Clamp1` — tên cơ cấu trên máy — không phải `FB_Clamp1` |
| C5 | Ký tự chú thích? | ⭐ Chỉ `//` — không dùng `(* *)`, nên không bao giờ có chú thích lồng nhau (C3) |
| C6 | Chú thích bằng ngôn ngữ nào? | Tiếng Việt trong sách này. ⚠ **Dự án có người nước ngoài bảo trì: tiếng Anh** |
| L1 · L16 | Thụt lề thế nào? | ⭐ **4 dấu cách**, không dùng tab |
| L4 | Quy tắc trình bày chung? | `END_IF;` có dấu chấm phẩy · `TRUE`/`FALSE` viết hoa · hằng thời gian dạng `T#500MS` · gọi khối **có tên từng chân** (L14) |
| L11 | Dòng dài tối đa? | Phần mã ≤ 80; xem N.5 |
| L3 · L6 · L9 · CP9 | Giới hạn độ phức tạp? | Sách không đặt con số. ⭐ Gợi ý dùng được ngay: **một nấc thang không vượt quá chiều rộng một màn hình**; một POU đọc hết trong **một lần cuộn**; quá thì tách |
| CP23 | Một POU tối đa bao nhiêu chân? | ⭐ Khoảng **10**, như PLCopen gợi ý. Khối xy-lanh ở Chương 27 có **11** (6 vào, 5 ra) — nhỉnh hơn gợi ý, chấp nhận vì mỗi chân trả lời một câu người bảo trì hỏi thật; ⚠ quá ~12 thì tách khối |
| — | ⭐ Tên chân của khối tự viết? | Khối thuộc một trong hai hợp đồng của PLCopen thì dùng **đúng tên và đúng nghĩa** của hợp đồng đó: `Execute`/`Done`/`Busy`/`Error`/`ErrorID` (kích bằng sườn), `Enable`/`Valid` (theo mức — tắt là xoá ngõ ra). ⚠ **Không mượn** các tên đó cho nghĩa khác: chân cho phép của khối xy-lanh tên là `Permit`, không phải `Enable` (Chương 30 mục 30.5b) |
| CP24 | Biến khai báo mà không dùng? | Xoá. Trình biên dịch nhiều hệ có cảnh báo cho chuyện này — **bật nó lên** |
| L5 | Tiếp điểm sau cuộn dây trong một nấc? | ⭐ **Không** — cuộn dây luôn ở cuối nấc |

> ⭐⭐ **Cách dùng bảng này cho đơn vị của bạn:** chép nó ra, sửa cột cuối theo thực tế của đơn vị, rồi
> **ký duyệt** như một tài liệu dự án (Phụ lục C). ⚡ Một quy ước chỉ có giá trị khi có người **chịu
> trách nhiệm** về nó.

---

## N.7 ⭐ Quy ước mã mẫu của chính cuốn sách này

⭐ Sách có hai loại khối mã, và bạn phải phân biệt được chúng trước khi chép:

| Loại | Nhận ra bằng | Chép vào phần mềm được không |
|---|---|---|
| ⭐ **Ví dụ hoàn chỉnh** | Có khai báo `VAR … END_VAR`, hoặc là một POU đầy đủ (`FUNCTION_BLOCK … END_FUNCTION_BLOCK`) | ✅ **Được** — đủ khai báo để biên dịch |
| **Đoạn trích** | Không có khai báo | ⚠ **Không trực tiếp** — tag lấy theo bảng I/O của máy mẫu (**Phụ lục J**); biến nội bộ tự suy ra từ ngữ cảnh |

> ⭐ **Vì sao không khai báo đầy đủ trong mọi khối:** một đoạn ba dòng minh hoạ một ý, nếu kèm mười dòng
> khai báo thì **ý chính bị chìm**. ⚡ Sách chọn giữ đoạn trích gọn, và bảo đảm **mỗi chương về lập trình
> có ít nhất một ví dụ hoàn chỉnh** để bạn có một điểm xuất phát chép chạy được.

---

### Nguồn tham khảo phụ lục N

- **PLCopen** — *Coding Guidelines, version 1.0* (2016), 127 trang: toàn bộ 64 quy tắc trong năm
  nhóm N · C · CP · L · E, kèm mức ưu tiên, lý do và ví dụ nên/không nên; phụ lục 1 xếp mọi quy tắc
  theo mức ưu tiên. ⭐ Các con số gợi ý dẫn ở phụ lục này — **80 ký tự** một dòng (L11), khoảng **10**
  chân một POU (CP23), tên tối đa **25** ký tự (N6) — lấy từ đó. Tải miễn phí từ trang của PLCopen.
- Các phép đo trên mã mẫu của sách — số dòng, độ dài tag, tiền tố — do chính công cụ kiểm của dự án
  thực hiện ở đợt rà 58 (xem nhật ký đối chiếu).

> ⚡ Tài liệu PLCopen dẫn nguồn cho từng quy tắc từ các bộ quy tắc của ngành phần mềm nói chung
> (MISRA-C, JSF++) và từ công cụ phân tích tĩnh của một số hãng. ⭐ Nghĩa là nhiều quy tắc ở đây **kiểm
> được bằng công cụ** — hãy tìm chức năng phân tích tĩnh trong phần mềm lập trình bạn dùng.
