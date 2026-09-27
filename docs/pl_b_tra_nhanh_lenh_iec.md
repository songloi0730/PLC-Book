
# Phụ lục B — Tra nhanh lệnh IEC 61131-3

> **Thiết kế để in ra và dán cạnh màn hình.** Đây là bản tra cứu — phần giải thích *vì sao* nằm ở
> các chương được dẫn.

---

> ⚠ **Đây là chuẩn IEC, không phải một hãng cụ thể.** Tên lệnh và ký hiệu ở đây theo IEC 61131-3.
> ⭐ **Từng hãng có thể đặt tên khác, hoặc bổ sung lệnh riêng** — xem **Phụ lục A2** để đối chiếu.
>
> Khi hãng bạn dùng khác chuẩn, ⭐ **cột IEC ở đây cho biết khái niệm gốc là gì** — hữu ích khi đọc
> tài liệu của hãng khác hoặc chuyển giữa các nền.

---

## B.1 Kiểu dữ liệu

### Số nguyên

| Kiểu | Số bit | Dải | Dùng khi |
|---|---|---|---|
| `BOOL` | 1 | 0 / 1 | Bit trạng thái, tín hiệu số |
| `SINT` | 8 có dấu | −128 … 127 | Hiếm dùng |
| `USINT` · `BYTE` | 8 không dấu | 0 … 255 | Dữ liệu truyền thông |
| ⭐ `INT` | 16 có dấu | **−32 768 … 32 767** | ⚠ Cẩn thận tràn |
| `UINT` · `WORD` | 16 không dấu | 0 … 65 535 | Thanh ghi Modbus |
| ⭐ `DINT` | 32 có dấu | **−2 147 483 648 … 2 147 483 647** | ⭐ **Mọi bộ đếm tích luỹ** |
| `UDINT` · `DWORD` | 32 không dấu | 0 … 4 294 967 295 | |
| `LINT` · `LWORD` | 64 | rất lớn | Ít dùng trên PLC nhỏ |

### Số thực, thời gian, chuỗi

| Kiểu | Nội dung | Ghi chú |
|---|---|---|
| `REAL` | Số thực 32 bit | ⚠ **Không so sánh bằng** — so bằng dung sai |
| `LREAL` | Số thực 64 bit | Nhiều PLC nhỏ không hỗ trợ |
| `TIME` | Khoảng thời gian | `T#1s`, `T#500ms`, `T#1h30m` |
| `DATE` · `TOD` · `DT` | Ngày · giờ trong ngày · ngày-giờ | |
| `STRING` | Chuỗi ký tự | ⚠ Kiểm độ dài tối đa của hãng |

> ⚠⚠ **`INT` tràn sau 32 767 — với một máy làm 300 sản phẩm/giờ, đó là khoảng 4,5 ngày.**
> ⭐ Dùng `DINT` cho mọi bộ đếm tích luỹ. Xem Chương 11, 19.

---

## B.2 Toán tử — thứ tự ưu tiên

Từ **cao xuống thấp**:

| Mức | Toán tử | Ghi chú |
|---|---|---|
| 1 | `( )` | ⭐ **Khi nghi ngờ, dùng ngoặc** |
| 2 | Gọi hàm | |
| 3 | `**` | Luỹ thừa |
| 4 | `-` (một ngôi), `NOT` | |
| 5 | `*`, `/`, `MOD` | |
| 6 | `+`, `-` | |
| 7 | `<`, `>`, `<=`, `>=` | |
| 8 | `=`, `<>` | ⚠ `=` là **so sánh**; gán là `:=` |
| 9 | `AND`, `&` | |
| 10 | `XOR` | |
| 11 | `OR` | |

> ⭐ **`AND` ưu tiên cao hơn `OR`** — `a OR b AND c` nghĩa là `a OR (b AND c)`.
> ⚠ Đây là nguồn lỗi im lặng; ⭐ **viết ngoặc rõ ràng** dù không bắt buộc.

---

## B.3 Lệnh logic bit

| Lệnh | Nghĩa | Ladder | Chương |
|---|---|---|---|
| `AND` · `&` | Và | Tiếp điểm nối tiếp | 15 |
| `OR` | Hoặc | Tiếp điểm song song | 15 |
| `NOT` | Đảo | Tiếp điểm thường đóng | 15 |
| `XOR` | Hoặc loại trừ | | 15 |
| `:=` | Gán | Cuộn dây | 15 |
| `S` | Đặt (giữ 1) | Cuộn dây Set | 16 |
| `R` | Xoá (giữ 0) | Cuộn dây Reset | 16 |
| `R_TRIG` | ⭐ Bắt **cạnh lên** | Tiếp điểm P | 16 |
| `F_TRIG` | ⭐ Bắt **cạnh xuống** | Tiếp điểm N | 16 |
| `SR` | Flip-flop ưu tiên Set | | 16 |
| `RS` | Flip-flop ưu tiên Reset | | 16 |
| `SHL` · `SHR` | Dịch trái · phải N bit, chỗ trống **điền 0** | | 19 |
| `ROL` · `ROR` | Xoay trái · phải N bit — bit rơi ra đầu này **quay lại** đầu kia | | 19 |

> ⭐⭐ **`SR` và `RS` khác nhau ở chỗ: khi CẢ HAI đầu vào cùng lên, cái nào thắng.**
>
> ⚠ Với mạch liên quan an toàn, câu hỏi "cái nào thắng" **không được để mặc định** — nó phải là một
> quyết định có lý do (Chương 16, 22).
>
> ⚠ Dịch bit làm việc trên **chuỗi bit** (`BYTE`, `WORD`, `DWORD`), không trên số có dấu. Dịch trái
> một bit **không** an toàn để "nhân 2" một số có thể âm — dùng phép nhân. Ứng dụng thật của dịch
> bit là **thanh ghi dịch** theo dõi sản phẩm dọc chuyền (Chương 19 mục 19.6).

---

## B.4 Bộ định thời

| Khối | Nghĩa | Hành vi |
|---|---|---|
| `TON` | ⭐ **Trễ khi bật** | `IN` lên → sau `PT` thì `Q` lên; `IN` xuống → `Q` xuống **ngay** |
| `TOF` | ⭐ **Trễ khi tắt** | `IN` lên → `Q` lên **ngay**; `IN` xuống → sau `PT` thì `Q` xuống |
| `TP` | **Xung** | `IN` lên → `Q` lên đúng `PT` rồi tự xuống, ⭐ **bất kể `IN` còn hay không** |

| Chân | Nghĩa |
|---|---|
| `IN` | Đầu vào kích |
| `PT` | Preset Time — thời gian đặt (`T#2s`) |
| `Q` | Đầu ra |
| `ET` | Elapsed Time — thời gian đã trôi |

```text
TON:  IN ▔▔▔▔▔▔▁▁▁      TOF:  IN ▔▔▔▔▁▁▁▁▁      TP:  IN ▔▔▁▁▁▁▁▁▁
      Q  ▁▁▔▔▔▔▁▁▁            Q  ▔▔▔▔▔▔▁▁▁           Q  ▔▔▔▔▔▁▁▁▁
         └PT┘                        └PT┘               └─PT─┘
```

> ⚠⚠ **Bộ định thời KHÔNG dùng để chuyển bước trình tự.**
>
> ⭐ Chuyển bước bằng **tín hiệu phản hồi thật**; bộ định thời chỉ để **báo lỗi khi phản hồi không
> tới**. Một bộ định thời không biết khi cơ cấu không tới nơi (Chương 17, 26).

---

## B.5 Bộ đếm

| Khối | Nghĩa | Chân chính |
|---|---|---|
| `CTU` | Đếm lên | `CU` (đếm), `R` (xoá), `PV` (đặt), `Q` (đạt), `CV` (hiện tại) |
| `CTD` | Đếm xuống | `CD`, `LD` (nạp), `PV`, `Q`, `CV` |
| `CTUD` | Đếm lên–xuống | `CU`, `CD`, `R`, `LD`, `PV`, `QU`, `QD`, `CV` |

> ⭐ **`CU` đếm theo CẠNH LÊN**, không theo mức. Nếu tín hiệu vào giữ ở 1, bộ đếm **không** đếm liên
> tục.
>
> ⚠ **Tên chân không giống nhau ở mọi hệ.** Chuẩn đặt chân xoá của `CTU` là `R`; thư viện chuẩn của
> CODESYS đặt là `RESET`, và kiểu của `PV`, `CV` là `WORD`. Gọi theo tên chân thì phải theo đúng tên
> của hệ đang dùng.
>
> ⚠ Với xung tần số cao — nhanh hơn khoảng **1 / (2 × thời gian quét)** — phải dùng **bộ đếm tốc độ
> cao** của phần cứng; bộ đếm phần mềm sẽ ⚠ **bỏ sót xung một cách âm thầm** (Chương 18, Phụ lục K.5).

---

## B.6 So sánh, toán học, chọn

### So sánh

| Lệnh | Nghĩa |
|---|---|
| `EQ` · `=` | Bằng |
| `NE` · `<>` | Khác |
| `LT` `LE` `GT` `GE` | Nhỏ hơn · nhỏ hơn bằng · lớn hơn · lớn hơn bằng |

> ⚠ **Không so sánh bằng hai số `REAL`.** Dùng `ABS(a - b) < dung_sai` (Chương 19 mục 19.3).

### Toán học

| Lệnh | Nghĩa | Ghi chú |
|---|---|---|
| `ADD` `SUB` `MUL` `DIV` | Cộng trừ nhân chia | ⚠ **Chia số nguyên cắt phần thập phân** |
| `MOD` | Chia lấy dư | |
| `ABS` | Trị tuyệt đối | |
| `SQRT` | Căn bậc hai | |
| `EXPT` · `**` | Luỹ thừa | |
| `LN` `LOG` `EXP` | Logarit, mũ | |
| `SIN` `COS` `TAN` `ASIN` `ACOS` `ATAN` | Lượng giác | ⚠ Đơn vị **radian** |

### Chọn và giới hạn

| Lệnh | Nghĩa | Ví dụ |
|---|---|---|
| `SEL` | Chọn theo BOOL | `SEL(G, IN0, IN1)` — G=0 lấy IN0 |
| `MAX` · `MIN` | Lớn nhất · nhỏ nhất | `MAX(ApLucA, ApLucB)` — số đầu vào tuỳ ý |
| ⭐ `LIMIT` | **Kẹp vào khoảng** | `LIMIT(MN, IN, MX)` |
| `MUX` | Chọn theo số | `MUX(K, IN0, IN1, …)` — ⭐ `K` đếm **từ 0**; ⚠ `K` ngoài khoảng thì hành vi **tuỳ hệ** — kẹp `K` bằng `LIMIT` trước khi gọi |

> ⭐ **`LIMIT` rất hữu ích cho giá trị analog và tham số công thức** — nhưng ⚠ **kẹp về biên KHÔNG
> phải cách xử lý công thức sai**. Công thức ngoài dải phải bị **từ chối và báo lỗi**, không phải âm
> thầm kẹp về giới hạn (Chương 29 mục 29.4).

### ⭐ Hàm chuỗi — vị trí đếm từ 1

| Hàm | Làm gì | Ví dụ → kết quả |
|---|---|---|
| `LEN(STR)` | Số ký tự | `LEN('SUSI')` → `4` |
| `LEFT(STR, L)` | `L` ký tự **đầu** | `LEFT('SUSI', 3)` → `'SUS'` |
| `RIGHT(STR, L)` | `L` ký tự **cuối** | `RIGHT('SUSI', 3)` → `'USI'` |
| ⭐ `MID(STR, L, P)` | `L` ký tự, **bắt đầu ở vị trí `P`** | `MID('SUSI', 2, 2)` → `'US'` |
| `CONCAT(STR1, STR2, …)` | Nối | `CONCAT('SU', 'SI')` → `'SUSI'` |
| `INSERT(STR1, STR2, P)` | Chèn `STR2` vào **sau** vị trí `P` | `INSERT('SUSI', 'XY', 2)` → `'SUXYSI'` |
| `DELETE(STR, L, P)` | Xoá `L` ký tự từ vị trí `P` | `DELETE('SUXYSI', 2, 3)` → `'SUSI'` |
| `REPLACE(STR1, STR2, L, P)` | Thay `L` ký tự từ vị trí `P` bằng `STR2` | `REPLACE('SUXYSI', 'K', 2, 2)` → `'SKYSI'` |
| ⭐ `FIND(STR1, STR2)` | Vị trí **đầu tiên** của `STR2` trong `STR1`; ⚠ **không thấy thì trả 0** | `FIND('abcdef', 'de')` → `4` |

> ⚠⚠ **Thứ tự tham số là chỗ sai nhiều nhất — kể cả trong sách giáo khoa.** Một giáo trình quốc tế
> dùng trong sách này in ví dụ `MID` chọn **lệch một vị trí** so với chính quy ước nó mô tả. ⭐ Cách tự
> vệ rẻ nhất: thử hàm với một chuỗi **mỗi ký tự khác nhau** (`'ABCDEF'`) trước khi dùng — nhìn kết quả
> là biết ngay tham số nào là độ dài, tham số nào là vị trí.
>
> ⚠ **Vị trí đếm từ 1, không từ 0.** Tài liệu CODESYS ghi rằng `P = 0` được coi như vị trí 1 — và tự
> ghi luôn là `DELETE`, `REPLACE` **xử lý `P = 0` chưa đúng**. Đừng bao giờ truyền 0.
>
> ⚠ **Độ dài có giới hạn.** `STRING` không khai độ dài thì mặc định **80** ký tự ở CODESYS, và các hàm
> chuỗi của thư viện chuẩn trả về tối đa 255 ký tự — phần thừa **bị cắt im lặng**.
>
> ⚠ **Không phải hệ nào cũng đủ bộ.** Bảng tuân thủ IEC 61131-3 của Logix liệt kê `LEN`, `MID`,
> `CONCAT`, `INSERT`, `DELETE`, `FIND` — không có `LEFT`, `RIGHT`, `REPLACE`; `LEFT(S, 3)` viết thành
> `MID(S, 3, 1)`.
>
> ⚠⚠ **Chữ tiếng Việt có dấu không nằm được trong `STRING`.** Một ký tự `CHAR` chỉ có 256 giá trị, và
> các chữ như `ệ`, `ở` nằm ngoài khoảng đó. Cần chuỗi hai byte `WSTRING`, hoặc chuỗi UTF-8 `USTRING`
> mà bản 4 của chuẩn (2025) mới thêm — ⚠ khi đó số **byte** không còn bằng số **ký tự**, và bản 4
> thêm `LEN_CODE_UNIT` để đếm byte, `LEN_MAX` để biết độ dài đã khai.
>
> ⭐ Ví dụ thật: kiểm định dạng mã 2D và tách mã lô — Chương 42 mục 42.4.

---

## B.7 Ép kiểu

| Mẫu | Nghĩa |
|---|---|
| `INT_TO_REAL(x)` | Số nguyên → số thực |
| `REAL_TO_INT(x)` | Số thực → số nguyên — ⚠ **làm tròn**, kiểm cách hãng làm tròn |
| `DINT_TO_REAL(x)` · `REAL_TO_DINT(x)` | Như trên, cho 32 bit |
| `BOOL_TO_INT(x)` | Bit → số nguyên (0 hoặc 1) |
| `TIME_TO_DINT(x)` | Thời gian → mili giây |

> ⭐ **Quy tắc thực dụng:** ép sang `REAL` **trước** khi tính, ép về số nguyên **sau** khi tính xong.
> Nó tránh cả **tràn số** lẫn **mất phần thập phân do chia số nguyên** (Chương 11, 19, Phụ lục K.6).

> ⚠ **Bản 4 của IEC 61131-3 (2025) dọn lại nhóm này.** `TRUNC(x)` không ghi kiểu **bị bỏ** — dùng dạng
> có kiểu như `TRUNC_DINT(x)`; các hàm đổi **BCD** bị đánh dấu **không khuyến khích**; và có thêm phép
> đổi giữa chuỗi với mảng byte. ⭐ Hệ theo bản 3 vẫn giữ nguyên các hàm cũ — kiểm hệ của bạn theo bản
> nào (Chương 14 mục 14.1).

---

## B.8 Cấu trúc điều khiển trong ST

```text
IF điều_kiện THEN
    ...
ELSIF điều_kiện_2 THEN
    ...
ELSE
    ...
END_IF;

CASE biến OF
    0:      ...
    1, 2:   ...
    3..5:   ...
ELSE
    ...
END_CASE;

FOR i := 0 TO 9 BY 1 DO  ...  END_FOR;
WHILE điều_kiện DO       ...  END_WHILE;
REPEAT  ...  UNTIL điều_kiện  END_REPEAT;

EXIT;      // thoát vòng lặp — ⚠ PLCopen L10: nên tránh; đặt trần ngay trong điều kiện vòng lặp
RETURN;    // thoát khối     — ⚠ PLCopen CP14: nên tránh; mỗi POU chỉ một điểm thoát (Phụ lục N)
```

> ⚠⚠ **`WHILE` và `REPEAT` nguy hiểm trên PLC.** Nếu điều kiện thoát không bao giờ đạt, ⭐ **vòng quét
> không kết thúc** và CPU vào lỗi giám sát treo máy.
>
> ⭐ Ưu tiên `FOR` với số vòng lặp **có giới hạn rõ ràng**. Nếu buộc dùng `WHILE`, thêm bộ đếm vòng
> lặp tối đa làm van an toàn (Chương 20).
>
> ⭐⭐ **Phép kiểm một câu cho mọi vòng lặp:** *điều kiện thoát có phụ thuộc một biến được cập nhật
> **bên trong** vòng lặp không?* ⚠ Nếu nó phụ thuộc tín hiệu vào, giá trị từ mạng, hay biến do tác vụ
> khác ghi — ⚠⚠ **đó là vòng lặp không bảo đảm kết thúc**.
>
> ⚠ `REPEAT` khác `WHILE` hai điểm: điều kiện **ngược cực tính** (chạy *cho tới khi* đúng), và thân
> vòng ⭐ **luôn chạy ít nhất một lần**. ⚠ `EXIT` chỉ thoát **một tầng**.

> ⭐⭐ **`CASE` là cấu trúc tự nhiên cho máy trạng thái và trình tự** — mỗi nhánh là một bước, biến
> điều khiển là số bước hiện tại (Chương 20, 21).

---

## B.9 Khối hàm và hàm

| | `FUNCTION` | `FUNCTION_BLOCK` |
|---|---|---|
| Bộ nhớ riêng | ⚠ **Không** | ⭐ **Có, theo từng thể hiện** |
| Cùng đầu vào → cùng đầu ra | ⭐ Luôn đúng | Không nhất thiết |
| Dùng cho | Tính toán thuần tuý | ⭐ **Bộ định thời, bộ đếm, trình tự, thiết bị** |
| Khai báo thể hiện | Không cần | ⭐ **Bắt buộc** |

```text
VAR
    T_Clamp1  : TON;        // ← khai báo thể hiện
    Stn1      : FB_Station; // ← mỗi trạm một thể hiện riêng
END_VAR

T_Clamp1(IN := M_Stn1_ClampReq, PT := T#2S);
IF T_Clamp1.Q THEN ... END_IF;
```

> ⭐⭐ **Điểm dễ nhầm nhất: hai chỗ dùng CÙNG một thể hiện `TON` sẽ ghi đè lẫn nhau.**
>
> Mỗi chỗ cần một bộ định thời riêng phải có **thể hiện riêng**. Đây là lý do khối hàm phải khai báo
> thể hiện, còn hàm thì không (Chương 14 mục 14.3).

---

## B.9b ⭐⭐ Hành vi thực thi — khối chạy thế nào ở vòng đầu, và khi KHÔNG được gọi

Ba câu hỏi mà bảng lệnh không trả lời, nhưng quyết định chương trình có chạy đúng không:

| Khối | ⭐ Cập nhật khi nào | Lần gọi đầu sau khởi động | ⚠ Khi **không** được gọi |
|---|---|---|---|
| `TON` · `TOF` · `TP` | **Chỉ trong lần gọi** — `ET`, `Q` tính lại ở mỗi lần gọi | `ET` = 0, `Q` = FALSE; `IN` đã TRUE thì bắt đầu đếm từ lần này | Ngõ ra **đứng yên** — `ET`, `Q` không cập nhật. ⚠⚠ Nhưng **không tạm dừng**: lần gọi kế tiếp tính **cả khoảng không được gọi** (Siemens: *bây giờ trừ lúc bắt đầu*; Rockwell: *cộng thời gian từ lần quét trước*) — `ET` **nhảy vọt**, `Q` có thể lên ngay. Khác hẳn lệnh `OUT` bộ định thời của hệ kiểu thiết bị: điều kiện tắt là **về 0** (Phụ lục A2 mục A2.8) |
| `R_TRIG` | So `CLK` với giá trị **ở lần gọi trước** | ⚠⚠ `CLK` đã TRUE thì báo **một sườn lên giả** (Chương 16 Bẫy 9) | Không thấy những gì xảy ra lúc không gọi; lần gọi sau so với một giá trị **có thể đã rất cũ** |
| `F_TRIG` | Như trên | ⭐ `CLK` đã FALSE thì **không** báo sườn — ⚠ **không đối xứng** với `R_TRIG` | Như trên |
| `CTU` · `CTD` · `CTUD` | Đếm theo **sườn** của `CU` / `CD` | ⚠ Sườn được nhận như `R_TRIG` — đầu vào đã TRUE ở lần đầu thì có thể đếm một lần; kiểm trên hệ | Không đếm những sườn xảy ra lúc không gọi |
| `SR` · `RS` | Mỗi lần gọi | `Q1` = FALSE, trừ khi khai giữ được | Giữ nguyên |
| Khối `Execute` / `Done` (chuyển động, truyền thông, khối tự viết) | Tham số chốt ở **sườn lên** của `Execute` | Như `R_TRIG`: `Execute` đã TRUE ở lần đầu thì **có thể** phát một lệnh — kiểm trên hệ | ⚠⚠ **Đứng yên** giữa chừng — không xong, không lỗi. Phải gọi **mỗi vòng** trong lúc `Busy` (Chương 30 mục 30.5b) |
| Hàm (`LIMIT`, `MID`, `MAX`…) | Không có bộ nhớ — kết quả chỉ phụ thuộc đầu vào của chính lần gọi | — | — không có gì để giữ |
| Biến trong **phương thức** | Khởi tạo lại **mỗi lần gọi** | — | — (Chương 30 mục 30.5c) |

> ⭐⭐ **Một quy tắc gói cả bảng: gọi mọi thể hiện khối ĐÚNG MỘT LẦN mỗi vòng quét, NGOÀI mọi nhánh
> điều kiện, với đầu vào lấy từ trạng thái.** Muốn bộ định thời chạy ở bước 20 thì viết
> `T_Step20(IN := (Stn1_Step = 20), …)` ngoài `CASE` — rời bước là tự xoá, không bao giờ đứng yên với
> giá trị cũ, và không bao giờ phải gọi lần hai để xoá (PLCopen CP20, Phụ lục N).
>
> ⚠⚠ **Muốn bộ định thời ngưng đếm khi máy giữ (Hold), đưa điều kiện giữ vào `IN`** — đừng đặt khối
> vào một nhánh không chạy. Tắt `IN` là xoá về 0, bật lại là đếm lại từ đầu; còn khối bị bỏ không gọi
> thì lúc gọi lại **tính luôn** khoảng thời gian đã bỏ qua, và báo quá giờ ngay vòng quét đầu (Phụ lục L
> mục L.6). ⭐ Bộ kiểm mã của sách báo lỗi mọi thể hiện khối được gọi bên trong nhánh `IF`/`CASE`.
>
> *Nguồn cho cột "khi không được gọi" của `TON`/`TOF`/`TP`: tài liệu hệ thống S7-1200 (mục 7.2 —
> bộ định thời lưu thời điểm bắt đầu lấy từ đồng hồ chạy liên tục của CPU, cập nhật khi lệnh được gọi
> hoặc khi `Q`/`ET` được đọc); tài liệu lệnh chung Logix 5000 (mục "How a Timer Runs" — `ACC` cộng
> thời gian kể từ lần quét trước, và phải quét lại trong vòng 69 phút). Kiểm 2026-09-28. Hệ khác: thử
> trên hệ của bạn trước khi dựa vào.*

---

## B.10 Địa chỉ trực tiếp

```text
%IX0.3    %I0.3      ← bit ngõ vào
%QX1.0    %Q1.0      ← bit ngõ ra
%MX10.2   %M10.2     ← bit vùng nhớ
%IW4                 ← word ngõ vào (analog)
%QW6                 ← word ngõ ra
%MD100               ← double word vùng nhớ
```

| Ký tự vị trí | Nghĩa | Ký tự cỡ | Nghĩa |
|---|---|---|---|
| `I` | Input | `X` | Bit |
| `Q` | Output | `B` | Byte (8 bit) |
| `M` | Memory | `W` | Word (16 bit) |
| | | `D` | Double word (32 bit) |
| | | `L` | Long word (64 bit) |

> ⭐⭐ **Nên dùng TÊN, không dùng địa chỉ trực tiếp.** `DI_BoardStn1` đọc được; `%I0.3` thì không.
>
> ⚠ Chương trình đầy địa chỉ trực tiếp là chương trình mà ⭐ **người sau bạn không đọc được** — và khi
> đổi module hoặc đổi khe cắm, mọi địa chỉ dịch đi (Chương 8 mục 8.4, Chương 11 mục 11.3, Chương 56).

> ⚠⚠ **Và một bẫy riêng của địa chỉ trực tiếp: hai biến CHỒNG LÊN NHAU.** Một giá trị rộng hơn một ô
> địa chỉ thì chiếm luôn **các ô tiếp theo**:
>
> ```iecst
> Level       : REAL AT %MW450;       // REAL 32 bit chiếm HAI ô: 450 và 451
> Temperature : INT  AT %MW451;       // ⚠ ghi vào đây là ghi đè NỬA SAU của Level
> ```
>
> ⭐ Chương trình kiểu này **chạy đúng gần như mọi lúc**, vì luồng dữ liệu thường ghi rồi đọc mỗi biến
> ở một đoạn riêng. ⚠⚠ Nó chỉ sai khi một điều kiện hiếm khiến một biến **không được ghi** — lúc đó
> chương trình đọc nhầm dữ liệu của biến kia, và không lần chạy thử nào tái hiện được.
>
> ⚡ **Mỗi giá trị chiếm bao nhiêu ô phụ thuộc hệ đánh chỉ số bộ nhớ theo byte hay theo word** — kiểm
> tài liệu của hệ bạn trước khi tính. ⭐ Cách chắc nhất vẫn là: **dùng tên, để phần mềm tự xếp chỗ**
> (Phụ lục N, quy tắc CP4).

---

## B.11 Ladder — ký hiệu

```text
   ─┤ ├─      Tiếp điểm thường mở        (đóng khi bit = 1)
   ─┤/├─      Tiếp điểm thường đóng      (đóng khi bit = 0)
   ─┤P├─      Bắt cạnh lên
   ─┤N├─      Bắt cạnh xuống
   ─( )─      Cuộn dây
   ─(S)─      Cuộn dây Set
   ─(R)─      Cuộn dây Reset
```

```text
Mạch tự giữ — mẫu cơ bản nhất:

   Start   Stop
  ──┤ ├───┤/├──┬──( Run )
            │
   Run      │
  ──┤ ├─────┘
```

> ⚠⚠ **Chú ý về nút Stop trong mạch tự giữ:** trên bản vẽ nó vẽ là tiếp điểm **thường đóng**
> (`─┤/├─`), nhưng nút bấm thật phải là loại **NC** — để ⭐ **đứt dây làm máy dừng**, không phải làm
> máy không dừng được.
>
> ⭐ Đây là ví dụ trung tâm của Chương 4 và Chương 15: ký hiệu trên chương trình và loại tiếp điểm
> ngoài thực tế là **hai thứ phải khớp nhau có chủ ý**.

---

## B.12 Dẫn về đâu

| Bạn cần | Đọc |
|---|---|
| Vì sao lệnh này tồn tại, dùng khi nào | Chương được dẫn ở mỗi bảng |
| ⭐ **Lệnh tương ứng trên hãng bạn dùng** | **Phụ lục A2** |
| Công thức tính kèm điều kiện áp dụng | **Phụ lục K** |
| ⭐ **Mẫu code cho mạch thường dùng** (tự giữ, dừng khẩn cấp, tạm dừng, tuần hoàn, servo…) | **Phụ lục L** |
| Thuật ngữ Việt–Anh | **Phụ lục F** |

> ⚠ **Giới hạn.** Bảng này theo **IEC 61131-3**. ⭐ Từng hãng có thể: đặt tên lệnh khác, thêm chân cho
> khối chuẩn, hoặc có hành vi khác ở trường hợp biên (nạp lại chương trình, tràn số, chia cho 0).
>
> ⚠ **Khi hành vi ở trường hợp biên quan trọng với máy của bạn, hãy đọc tài liệu của hãng và thử thực
> tế** — đừng suy từ bảng này.
