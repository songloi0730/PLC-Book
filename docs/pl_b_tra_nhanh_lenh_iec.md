
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
> ⭐ Dùng `DINT` cho mọi bộ đếm tích luỹ. Xem Chương 14.

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
| `S` | Đặt (giữ 1) | Cuộn dây Set | 15 |
| `R` | Xoá (giữ 0) | Cuộn dây Reset | 15 |
| `R_TRIG` | ⭐ Bắt **cạnh lên** | Tiếp điểm P | 16 |
| `F_TRIG` | ⭐ Bắt **cạnh xuống** | Tiếp điểm N | 16 |
| `SR` | Flip-flop ưu tiên Set | | 15 |
| `RS` | Flip-flop ưu tiên Reset | | 15 |

> ⭐⭐ **`SR` và `RS` khác nhau ở chỗ: khi CẢ HAI đầu vào cùng lên, cái nào thắng.**
>
> ⚠ Với mạch liên quan an toàn, câu hỏi "cái nào thắng" **không được để mặc định** — nó phải là một
> quyết định có lý do (Chương 15, 22).

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
> tới**. Một bộ định thời không biết khi cơ cấu không tới nơi (Chương 21).

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

> ⚠ **Không so sánh bằng hai số `REAL`.** Dùng `ABS(a - b) < dung_sai` (Chương 14).

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
| `MAX` · `MIN` | Lớn nhất · nhỏ nhất | |
| ⭐ `LIMIT` | **Kẹp vào khoảng** | `LIMIT(MN, IN, MX)` |
| `MUX` | Chọn theo số | `MUX(K, IN0, IN1, …)` |

> ⭐ **`LIMIT` rất hữu ích cho giá trị analog và tham số công thức** — nhưng ⚠ **kẹp về biên KHÔNG
> phải cách xử lý công thức sai**. Công thức ngoài dải phải bị **từ chối và báo lỗi**, không phải âm
> thầm kẹp về giới hạn (Chương 32).

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
> Nó tránh cả **tràn số** lẫn **mất phần thập phân do chia số nguyên** (Chương 14, Phụ lục K.6).

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

EXIT;      // thoát vòng lặp
RETURN;    // thoát khối
```

> ⚠⚠ **`WHILE` và `REPEAT` nguy hiểm trên PLC.** Nếu điều kiện thoát không bao giờ đạt, ⭐ **vòng quét
> không kết thúc** và CPU vào lỗi giám sát treo máy.
>
> ⭐ Ưu tiên `FOR` với số vòng lặp **có giới hạn rõ ràng**. Nếu buộc dùng `WHILE`, thêm bộ đếm vòng
> lặp tối đa làm van an toàn (Chương 20).

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
    TimerKep  : TON;        // ← khai báo thể hiện
    Stn1      : FB_Station; // ← mỗi trạm một thể hiện riêng
END_VAR

TimerKep(IN := DangKep, PT := T#2s);
IF TimerKep.Q THEN ... END_IF;
```

> ⭐⭐ **Điểm dễ nhầm nhất: hai chỗ dùng CÙNG một thể hiện `TON` sẽ ghi đè lẫn nhau.**
>
> Mỗi chỗ cần một bộ định thời riêng phải có **thể hiện riêng**. Đây là lý do khối hàm phải khai báo
> thể hiện, còn hàm thì không (Chương 30).

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
> đổi module hoặc đổi khe cắm, mọi địa chỉ dịch đi (Chương 24, 56).

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
| Thuật ngữ Việt–Anh | **Phụ lục F** |

> ⚠ **Giới hạn.** Bảng này theo **IEC 61131-3**. ⭐ Từng hãng có thể: đặt tên lệnh khác, thêm chân cho
> khối chuẩn, hoặc có hành vi khác ở trường hợp biên (nạp lại chương trình, tràn số, chia cho 0).
>
> ⚠ **Khi hành vi ở trường hợp biên quan trọng với máy của bạn, hãy đọc tài liệu của hãng và thử thực
> tế** — đừng suy từ bảng này.
