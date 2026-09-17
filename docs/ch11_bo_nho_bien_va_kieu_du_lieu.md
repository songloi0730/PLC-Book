# Chương 11 — Bộ nhớ, biến & kiểu dữ liệu

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 11.1 Bài toán: một tag, hai thiết bị

Một cỗ máy chạy ổn định hai năm. Người bảo trì thêm một cảm biến kiểm tra, cắm thêm một module vào
khe trống **ở giữa** rack, cập nhật cấu hình phần cứng, nạp lại chương trình.

Máy chạy. Nhưng bây giờ khi trình tự ra lệnh nâng kẹp, **van tra keo mở**.

Nguyên nhân: chương trình dùng **địa chỉ tuyệt đối** — `%Q0.3`, `%Q0.4`… Thêm module vào giữa làm địa
chỉ của mọi module phía sau dịch đi một khoảng. `%Q0.3` bây giờ trỏ vào một chân khác. Chương trình
biên dịch không lỗi, CPU chạy không báo gì, và mỗi lệnh ngõ ra đang điều khiển nhầm thiết bị.

Nếu chương trình dùng **tag có tên**, việc thêm module chỉ cần sửa ánh xạ ở một chỗ, và mọi dòng lệnh
gọi `DO_Clamp1Vlv` vẫn trỏ đúng cái van đó.

Chương này về cách dữ liệu được đặt tên, được phân loại, và được tổ chức — ba thứ quyết định chương
trình của bạn dễ đọc hay khó đọc, dễ sửa hay dễ hỏng.

---

## 11.2 Kiểu dữ liệu — bảng phải thuộc

| Kiểu | Độ rộng | Dải | Dùng cho |
|---|---|---|---|
| `BOOL` | 1 bit | đúng / sai | Mọi tín hiệu số, cờ, kết quả so sánh |
| `BYTE` | 8 bit | — | **Nhóm 8 bit**, không phải số |
| `WORD` | 16 bit | — | **Nhóm 16 bit**, không phải số |
| `DWORD` | 32 bit | — | **Nhóm 32 bit** |
| `SINT` | 8 bit | −128 … 127 | Ít dùng |
| `INT` | 16 bit | −32 768 … 32 767 | ⚠ Số nguyên thông dụng — **rất dễ tràn** |
| `DINT` | 32 bit | ≈ ±2,1 tỉ | Bộ đếm tích luỹ, thời gian tính bằng mili-giây |
| `UINT` | 16 bit | 0 … 65 535 | Khi chắc chắn không âm |
| `REAL` | 32 bit | ≈ ±3,4 × 10³⁸, khoảng 7 chữ số có nghĩa | Đại lượng vật lý có phần lẻ |
| `LREAL` | 64 bit | rộng và chính xác hơn nhiều | Khi `REAL` không đủ chính xác |
| `TIME` | — | viết `T#2S`, `T#500MS` | Tham số của timer |
| `STRING` | thay đổi | chuỗi ký tự | Mã sản phẩm, bản tin — hay gặp khi nối mạng (Chương 42) |

### ⭐ `WORD` không phải `INT` — và nhầm chúng là lỗi thật

Hai kiểu này cùng chiếm 16 bit, nên người mới hay coi chúng như nhau. Chúng **khác nhau về ý nghĩa**:

| | `INT` | `WORD` |
|---|---|---|
| Là gì | Một **con số** có dấu | Một **nhóm 16 bit** |
| Phép hợp lệ | Cộng, trừ, nhân, chia, so sánh lớn/nhỏ | AND, OR, XOR, dịch bit, tách từng bit |
| Bit cao nhất nghĩa là | **Dấu âm** | Chỉ là bit thứ 16, không có nghĩa đặc biệt |
| Giá trị `1111 1111 1111 1111` | **−1** | Mười sáu bit đều bằng 1 |

Hàng cuối là chỗ gây bất ngờ nhất. Cùng một mẫu bit, đọc theo `INT` ra `−1`, đọc theo `WORD` ra một
nhóm bit toàn 1. Nếu bạn nhận một từ trạng thái từ thiết bị khác và khai báo nó là `INT`, bạn sẽ thấy
những con số âm vô lý — trong khi thật ra mỗi bit trong đó là một cờ trạng thái riêng.

> **Quy tắc: cái gì là SỐ thì khai `INT`/`DINT`; cái gì là TẬP CỜ thì khai `WORD`.**
> Từ trạng thái thiết bị, mặt nạ bit, mã lỗi dạng bit — đều là `WORD`.

### ⚠ Hai bẫy sẽ gặp lại ở Chương 19

Nêu ở đây để bạn biết chúng tồn tại; Chương 19 mổ xẻ đầy đủ.

- **Tràn số nguyên** *(overflow)*: `INT` chạm 32 767 rồi cộng thêm 1 thì ở phần lớn hệ **quay vòng về
  −32 768**, im lặng, không báo lỗi. `32 767` nghe lớn nhưng thời gian tính bằng mili-giây thì đó chỉ
  là **33 giây**.
- **So sánh bằng với số thực**: `IF ActualLength = 12.5 THEN` gần như không bao giờ đúng, vì phần lớn
  số thập phân không biểu diễn chính xác được ở dạng nhị phân. **Không bao giờ dùng `=` với `REAL`.**

---

## 11.3 ⭐ Địa chỉ tuyệt đối và tag có tên

### Hai cách gọi cùng một chỗ nhớ

```text
Địa chỉ tuyệt đối:  %I0.2      ← "bit thứ 2 của byte ngõ vào 0"
Tag có tên:         DI_BoardStn1   ← "cảm biến board ở trạm 1"
```

Địa chỉ tuyệt đối mô tả **chỗ nhớ nằm ở đâu**. Tag mô tả **nó là cái gì**. Hai cách này không loại trừ
nhau — ở hầu hết hệ, tag được **ánh xạ** vào một địa chỉ, và bạn viết chương trình bằng tag.

### Vì sao ngành đã chuyển sang tag

| Vấn đề của địa chỉ tuyệt đối | Hậu quả |
|---|---|
| ⚠ **Địa chỉ dịch khi đổi phần cứng** | Đúng cỗ máy ở mục 11.1 — chương trình chạy, điều khiển nhầm thiết bị, không báo lỗi |
| Không đọc được ý nghĩa | `%I0.2` không nói gì; phải tra bảng I/O cho **từng** dòng lệnh |
| Không tìm được bằng tên | Muốn biết "cảm biến board dùng ở đâu" thì phải nhớ địa chỉ của nó |
| Dễ gõ nhầm | `%I0.2` và `%I0.3` khác nhau một ký tự, và gõ nhầm không gây lỗi biên dịch |
| Không mang được ý nghĩa qua dự án | Sang máy khác, `%I0.2` là thứ hoàn toàn khác |

Tag giải quyết cả năm. Đổi lại, bạn phải **duy trì bảng ánh xạ** — nhưng bảng đó chính là bảng I/O mà
bạn đã phải làm rồi (Chương 23).

> ⚠⚠ **Đây không phải chuyện thẩm mỹ.**
> Lỗi ở mục 11.1 — lệnh nâng kẹp mở van tra keo — là loại lỗi **không có triệu chứng ở chỗ có lỗi**.
> Chương trình đúng, cấu hình đúng, chỉ có ánh xạ sai. Người đi tìm sẽ đọc logic hàng giờ mà không
> thấy gì.
>
> Dùng tag không loại bỏ hoàn toàn rủi ro, nhưng nó **thu vấn đề về một chỗ duy nhất** — bảng ánh xạ
> — thay vì rải khắp chương trình. Và sau **mọi** thay đổi phần cứng, vẫn phải **kiểm I/O 1-1 lại**
> (Chương 52, mục 52.4). Không có ngoại lệ "chỉ thêm một module thôi mà".

### Đặt tên tag — quy ước của sách

Sách dùng quy ước này xuyên suốt, và nó đã xuất hiện trong mọi ví dụ:

```text
   DI_BoardStn1
   ││ │     └── vị trí hoặc số thứ tự
   ││ └──────── đối tượng
   │└────────── (viết hoa đầu mỗi từ)
   └─────────── tiền tố loại tín hiệu
```

| Tiền tố | Nghĩa |
|---|---|
| `DI_` | Ngõ vào số *(digital input)* |
| `DO_` | Ngõ ra số *(digital output)* |
| `AI_` / `AO_` | Ngõ vào / ra analog (Chương 32) |
| `M_` | Cờ nhớ trong chương trình, không nối ra ngoài |
| `T_` | Thể hiện của timer |
| `C_` | Thể hiện của bộ đếm |

Ba quy tắc quan trọng hơn bản thân quy ước:

- **Nhất quán quan trọng hơn đẹp.** Nhiều cách đặt tên đều hợp lý; trộn tuỳ hứng nhiều cách trong một
  chương trình thì luôn sai, vì người đọc mất khả năng đoán. ⭐ **Bốn quy ước hay gặp, cùng một ví dụ,
  kèm ưu và nhược: Chương 30 mục 30.2** — đọc trước khi chốt quy ước cho dự án của bạn.
- ⭐ **Đưa đơn vị vào tên** khi giá trị có đơn vị: `CycleTimeMs`, `LengthTenthMm`, `YieldPctX10`. Đơn
  vị ngầm hiểu là nguồn của lỗi quy đổi gấp 10, 100, 1000 lần (Chương 19, Bẫy 9).
- **Tên nói *là gì*, không nói *ở đâu*.** `DI_BoardStn1` tốt; `DI_Input2` vô dụng vì nó chỉ lặp lại
  địa chỉ bằng chữ.

---

## 11.4 Biến giữ được và không giữ được

Khái niệm đã nhắc ở Chương 8 (pin và bộ nhớ); ở đây là mặt biến, và Chương 16 sẽ cho quy tắc thiết kế.

| Loại | Sau khi mất điện rồi bật lại |
|---|---|
| **Không giữ** *(non-retentive)* | Về giá trị khởi tạo, thường là 0 |
| **Giữ được** *(retentive / latched)* | Giữ nguyên giá trị trước khi mất điện |

Câu hỏi phải hỏi cho **mỗi** biến quan trọng:

> **"Mất điện rồi bật lại, biến này NÊN bằng mấy?"**

Không phải "nó sẽ bằng mấy" — mà **nên** bằng mấy. Đó là quyết định thiết kế, và mặc định của hệ chưa
chắc đúng cho máy của bạn.

Nguyên tắc chọn, đầy đủ ở Chương 16 mục 16.4:

> **Giữ lại thứ mô tả THẾ GIỚI THẬT. Đừng giữ thứ mô tả Ý ĐỊNH của chương trình.**

Số board đã làm là sự thật đã xảy ra → giữ. `M_Running` là ý định của chương trình → **không giữ**,
vì giữ nó nghĩa là máy tự chạy lại khi có điện trở lại.

> ⚠ Cách khai báo khác nhau **rất nhiều** giữa các hãng — có hệ theo dải địa chỉ, có hệ theo thuộc
> tính của biến, và có hệ **mặc định là giữ**. Bảng đối chiếu ở Chương 16, mục 16.7. Đây là chỗ
> chuyển chương trình giữa hai hệ hay sai nhất.

---

## 11.5 ⭐ Kiểu dữ liệu người dùng — mô hình hoá một trạm

### Bài toán

DP-01 có hai trạm gần giống nhau. Mỗi trạm cần theo dõi: bước hiện tại, bước đang lỗi, cờ lỗi, số
board đã làm, board hiện tại có NG không.

Cách ngây thơ — khai báo rời rạc:

```iecst
VAR
    Stn1_Step       : INT;
    Stn1_FaultStep  : INT;
    Stn1_AnyFault   : BOOL;
    Stn1_DoneCount  : DINT;
    Stn1_BoardIsNG  : BOOL;

    Stn2_Step       : INT;
    Stn2_FaultStep  : INT;
    Stn2_AnyFault   : BOOL;
    Stn2_DoneCount  : DINT;
    Stn2_BoardIsNG  : BOOL;
END_VAR
```

Mười biến, chép hai lần. Thêm trạm thứ ba là chép lần nữa. Thêm một trường mới là sửa ba chỗ — và
quên một chỗ là lỗi.

### Cách đúng: một kiểu, nhiều biến

**Kiểu dữ liệu người dùng** *(user-defined type, UDT — còn gọi là `STRUCT`)* cho phép gom các trường
liên quan thành **một kiểu**:

```iecst
TYPE ST_Station :
STRUCT
    Step        : INT;      // bước hiện tại
    FaultStep   : INT;      // bước đang lỗi, 0 nếu không lỗi
    AnyFault    : BOOL;
    DoneCount   : DINT;
    BoardIsNG   : BOOL;
END_STRUCT
END_TYPE

VAR
    Stn1 : ST_Station;
    Stn2 : ST_Station;
END_VAR
```

Dùng bằng dấu chấm:

```iecst
IF Stn1.Step = 20 AND DI_Clamp1Up THEN
    Stn1.Step := 30;
END_IF;

TotalDone := Stn1.DoneCount + Stn2.DoneCount;
```

Bốn lợi ích cụ thể:

- **Thêm trường là sửa một chỗ** — mọi trạm có ngay trường mới.
- **Không thể quên trạm nào**, vì cấu trúc là chung.
- **Truyền cả cụm** vào một khối chức năng bằng một tham số, thay vì năm tham số rời.
- **Đọc rõ nghĩa**: `Stn2.AnyFault` nói ngay nó thuộc về ai.

### Mảng — khi các đối tượng đánh số được

Khi số lượng nhiều và **truy cập theo chỉ số** là tự nhiên, dùng **mảng** *(array)*:

```iecst
VAR
    Stations : ARRAY[1..2] OF ST_Station;   // gộp cả UDT lẫn mảng
    BoardNG  : ARRAY[0..3] OF BOOL;         // thanh ghi dịch (Chương 19)
END_VAR
```

Mảng cho phép dùng vòng lặp:

```iecst
TotalDone := 0;
FOR i := 1 TO 2 DO
    TotalDone := TotalDone + Stations[i].DoneCount;
END_FOR;
```

> ⚠⚠ **Chỉ số mảng vượt dải là lỗi nguy hiểm.**
> Tuỳ hệ, có **ba** hậu quả: CPU báo lỗi và **chuyển sang STOP**; hoặc **ghi đè lên vùng nhớ của biến
> khác**, gây hỏng hóc ở chỗ hoàn toàn không liên quan; hoặc ⚠⚠ — thứ khó phát hiện nhất —
> ⭐ **hệ tự kẹp im lặng về phần tử đầu/cuối mảng rồi chạy tiếp**, khiến dữ liệu của hai sản phẩm khác
> nhau đè lên cùng một ô nhớ mà không có dấu hiệu gì. Mọi chỉ số đến từ tính toán phải được **kẹp
> trong dải** trước khi dùng — ⚠ **đừng trông vào việc hệ tự kẹp**. Chương 19, mục 19.7.

### Khi nào dùng mảng, khi nào dùng biến rời

| Dùng **mảng** khi | Dùng **biến rời** khi |
|---|---|
| Các đối tượng **giống hệt nhau** | Các đối tượng **khác nhau** |
| Cần duyệt bằng vòng lặp | Chỉ vài cái, mỗi cái xử lý riêng |
| Số lượng có thể đổi | Số lượng cố định và nhỏ |
| Dữ liệu đi kèm sản phẩm dọc chuyền | Tên riêng dễ đọc hơn chỉ số |

Với **hai** trạm của DP-01, `Stn1` và `Stn2` đọc rõ hơn `Stations[1]` và `Stations[2]`. Nếu là **tám**
trạm thì mảng thắng. Đây là quyết định về **tính dễ đọc**, không phải về kỹ thuật.

---

## 11.6 Phạm vi biến — biến toàn cục và biến cục bộ

| Phạm vi | Nhìn thấy từ đâu | Dùng cho |
|---|---|---|
| **Toàn cục** *(global)* | Mọi POU | Tag I/O, cờ dùng chung giữa các phần |
| **Cục bộ** *(local)* | Chỉ trong POU khai báo nó | Biến trung gian, biến đếm vòng lặp |
| **Của thể hiện** | Thuộc về một thể hiện khối chức năng | Trạng thái riêng của từng thể hiện (Chương 14) |

> 💡 **Quy tắc: để biến ở phạm vi HẸP NHẤT còn dùng được.**
> Biến toàn cục có thể bị ghi từ bất kỳ đâu, nên khi giá trị sai bạn phải tìm khắp chương trình.
> Biến cục bộ thì danh sách nghi phạm chỉ gồm một POU.
>
> Ngoại lệ hiển nhiên: tag I/O phải toàn cục, vì nhiều phần cần đọc chúng.

Biến đếm vòng lặp `i` là ví dụ điển hình của biến **phải** cục bộ. Nếu nó toàn cục và hai POU cùng
dùng, một vòng lặp có thể phá chỉ số của vòng lặp kia.

---

## 11.7 Trên máy mẫu DP-01 — khai báo hoàn chỉnh

Gom cả chương thành một khối khai báo dùng được:

```iecst
// ── Kiểu dữ liệu của một trạm ──
TYPE ST_Station :
STRUCT
    Step        : INT;                 // bước hiện tại
    FaultStep   : INT;                 // bước đang lỗi
    AnyFault    : BOOL;
    DoneCount   : DINT;                // ⭐ DINT, không phải INT — sẽ tràn
    NgCount     : DINT;
    BoardIsNG   : BOOL;
    LastCycleMs : DINT;                // ⭐ đơn vị trong tên
END_STRUCT
END_TYPE

VAR_GLOBAL
    // Tag I/O — ánh xạ tới địa chỉ trong cấu hình phần cứng
    DI_StartPB      : BOOL;
    DI_StopPB       : BOOL;            // ⚠ từ tiếp điểm NC — bình thường bằng 1
    DI_EStopOK      : BOOL;            // ⚠ từ mạch an toàn, NC (Chương 47)
    DI_AirOK        : BOOL;
    DI_BoardStn1    : BOOL;
    DI_Clamp1Up     : BOOL;
    DI_Clamp1Dn     : BOOL;
    DO_Clamp1Vlv    : BOOL;
    // … phần còn lại theo bảng I/O, Phụ lục J

    // Trạng thái máy
    M_Running       : BOOL;            // ⚠⚠ KHÔNG giữ qua mất điện (Chương 16)
    M_AnyFault      : BOOL;

    Stn1            : ST_Station;      // ⚠ Step KHÔNG giữ qua mất điện
    Stn2            : ST_Station;
END_VAR

VAR_GLOBAL RETAIN
    // ⭐ Chỉ những thứ mô tả THẾ GIỚI THẬT
    ShiftOkCount    : DINT;            // sản lượng ca
    ShiftNgCount    : DINT;
    TotalCycleCount : DINT;            // tổng chu trình trọn đời — cho lịch bảo trì
    CurrentRecipeId : INT;             // mã hàng đang chạy
END_VAR
```

Ba điều đáng chú ý trong khối trên:

- **Bộ đếm dùng `DINT`, không dùng `INT`.** Sản lượng một ca có thể vượt 32 767 ở máy chạy nhanh, và
  tổng chu trình trọn đời thì chắc chắn vượt.
- **`LastCycleMs` mang đơn vị trong tên.** Không có nó, người sửa sau sáu tháng phải đoán là giây hay
  mili-giây.
- ⚠ **`Stn1.Step` nằm ở nhóm không giữ.** Đây là quyết định an toàn, không phải quyết định tiện lợi:
  giữ số bước qua mất điện nghĩa là máy chạy tiếp từ bước cũ trong khi cơ cấu có thể đã ở tư thế khác
  (Chương 16, Bẫy 4; Chương 28).

---

## 11.8 Khác biệt giữa các hãng

| Khía cạnh | Siemens | Mitsubishi | Rockwell | CODESYS / TwinCAT |
|---|---|---|---|---|
| Tag có tên | Bảng tag PLC; biến trong khối dữ liệu | Nhãn *(label)* gán cho thiết bị | ⭐ **Chỉ có tag** — không có địa chỉ tuyệt đối kiểu truyền thống | Biến khai báo trong POU |
| Địa chỉ tuyệt đối | `%I0.0`, `%Q0.0`, `%MW10` | Thiết bị `X`, `Y`, `M`, `D`, `T`, `C` | Không áp dụng | `%IX0.0`, `%QX0.0` |
| Kiểu người dùng | **UDT** | Kiểu cấu trúc trong dự án có cấu trúc | **UDT** | `TYPE … STRUCT` |
| Nơi chứa dữ liệu | **Khối dữ liệu** *(DB)* | Vùng thiết bị `D`, `M`… | Tag trong bộ điều khiển hoặc trong chương trình | Biến toàn cục / cục bộ |
| ⚠ Kiểu "tự nhiên" | — | — | ⭐ **`DINT`** — dùng `INT` khiến bộ điều khiển phải chuyển đổi, chậm hơn mà không lợi gì | — |
| Khai báo giữ được | Vùng M giữ được; thuộc tính *Retain* của biến trong DB | Theo **dải thiết bị** chốt | ⭐ **Mặc định là giữ** | `VAR RETAIN` / `VAR PERSISTENT` |

### ⭐ Rockwell không có địa chỉ tuyệt đối

Dòng Logix bỏ hẳn mô hình địa chỉ truyền thống: mọi thứ là **tag**, và tag được ánh xạ tới module qua
tên module trong cấu hình. Không tồn tại khái niệm `%I0.2` để mà dịch.

Hệ quả: lỗi ở mục 11.1 **không xảy ra được** trên hệ này. Đây là một ví dụ rõ ràng của việc một quyết
định thiết kế nền tảng loại bỏ hẳn một nhóm lỗi.

> ⚠ Nhưng đừng suy ra rằng hệ đó miễn nhiễm. Đổi phần cứng vẫn có thể làm sai **ánh xạ tag tới
> module**, và triệu chứng thì giống hệt. Quy tắc **kiểm I/O 1-1 sau mọi thay đổi phần cứng** vẫn áp
> dụng ở mọi hệ, không có ngoại lệ (Chương 52).

### ⚠ Mitsubishi — vẫn phải hiểu mô hình thiết bị

Mitsubishi cho dùng nhãn, nhưng mô hình nền vẫn là **thiết bị** (`X` ngõ vào, `Y` ngõ ra, `M` cờ nhớ,
`D` thanh ghi dữ liệu, `T` timer, `C` counter). Bạn không tránh được việc phải hiểu mô hình này, vì:

- **Dải thiết bị quyết định hành vi** — giữ hay không giữ (mục 11.4), độ phân giải timer (Chương 17),
  độ rộng bộ đếm (Chương 18);
- tài liệu và chương trình cũ đều nói bằng ngôn ngữ thiết bị.

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

---

## 11.9 Bẫy thường gặp

### 🔍 BẪY 1 — Dùng địa chỉ tuyệt đối trong chương trình

**Hiện tượng:** sau khi đổi phần cứng, lệnh điều khiển **nhầm thiết bị**. Chương trình biên dịch
không lỗi, CPU không báo gì — đây là loại lỗi không có triệu chứng tại chỗ có lỗi.
**Cách sửa:** dùng tag có tên; và kiểm I/O 1-1 lại sau mọi thay đổi phần cứng (mục 11.3).

### 🔍 BẪY 2 — Khai `INT` cho thứ sẽ tràn

**Hiện tượng:** sản lượng nhảy sang số âm; hoặc thời gian tích luỹ vô lý sau chưa tới một phút
(32 767 ms = 33 giây).
**Cách sửa:** `DINT` cho mọi bộ đếm tích luỹ và mọi phép tính thời gian (mục 11.2, Chương 19).

### 🔍 BẪY 3 — Nhầm `WORD` với `INT`

**Hiện tượng:** một từ trạng thái nhận từ thiết bị khác hiện ra thành số âm vô lý — trong khi thật ra
mỗi bit là một cờ riêng.
**Cách sửa:** cái gì là **số** thì `INT`/`DINT`; cái gì là **tập cờ** thì `WORD` (mục 11.2).

### 🔍 BẪY 4 — Tên biến không mang đơn vị

**Hiện tượng:** sai gấp 10, 100 hoặc 1000 lần ở một phép quy đổi. Thường phát hiện rất muộn, vì con
số vẫn "trông hợp lý".
**Cách sửa:** `CycleTimeMs`, `LengthTenthMm`, `YieldPctX10`. Vài ký tự, loại hẳn một nhóm lỗi.

### 🔍 BẪY 5 — Chép khối biến cho trạm thứ hai

**Hiện tượng:** thêm một trường mới, sửa được trạm 1 và trạm 2 nhưng **quên trạm 3**. Trạm 3 hành xử
khác và không ai biết vì sao.
**Cách sửa:** dùng UDT — thêm trường một lần, mọi trạm có ngay (mục 11.5).

### 🔍 BẪY 6 — Chỉ số mảng không kẹp trong dải

**Hiện tượng:** CPU chuyển sang STOP; hoặc hỏng hóc ở một chỗ **hoàn toàn không liên quan** vì vùng
nhớ biến khác bị ghi đè; hoặc ⚠⚠ **không có triệu chứng gì** vì hệ tự kẹp về phần tử đầu/cuối.
**Cách sửa:** kẹp mọi chỉ số đến từ tính toán trước khi dùng (Chương 19, mục 19.7).

### 🔍 BẪY 7 — Để mọi biến ở phạm vi toàn cục

**Hiện tượng:** một giá trị sai mà không biết ai ghi vào; phải dò tham chiếu chéo khắp chương trình.
Nặng nhất là khi hai vòng lặp dùng chung biến đếm `i`.
**Cách sửa:** phạm vi hẹp nhất còn dùng được (mục 11.6).

### 🔍 BẪY 8 — Giữ nhầm biến qua mất điện

**Hiện tượng:** máy **tự chạy lại** khi có điện trở lại; hoặc chạy tiếp từ bước cũ trong khi cơ cấu
đã ở tư thế khác.
**Cách sửa:** không bao giờ giữ `M_Running` và biến bước. Nguyên tắc đầy đủ ở Chương 16, mục 16.4.

### 🔍 BẪY 9 — Đặt tên theo vị trí thay vì theo ý nghĩa

`DI_Input2`, `M_Flag7`, `D100`.

**Hiện tượng:** chương trình chỉ đọc được khi mở kèm bảng I/O; người bảo trì lúc hai giờ sáng không
có bảng đó.
**Cách sửa:** tên nói **là gì**, không nói **ở đâu** (mục 11.3, Chương 30).

---

## 11.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Bộ đếm tích luỹ khai kiểu gì | **`DINT`** — `INT` sẽ tràn |
| Thời gian tính bằng mili-giây | **`DINT`** — 32 767 ms chỉ là 33 giây |
| Từ trạng thái, mặt nạ bit | **`WORD`** — không phải `INT` |
| So sánh bằng với `REAL` | ❌ **Không bao giờ** — so trong dung sai (Chương 19) |
| Trong chương trình dùng gì để gọi I/O | ⭐ **Tag có tên**, không dùng địa chỉ tuyệt đối |
| Sau khi đổi phần cứng | **Kiểm I/O 1-1 lại** — mọi hệ, không ngoại lệ |
| Tên biến có đơn vị | ⭐ Đưa đơn vị **vào tên** |
| Nhiều đối tượng giống nhau | **UDT**; nhiều và đánh số được thì thêm **mảng** |
| Chỉ số mảng từ tính toán | **Luôn kẹp trong dải** trước khi dùng |
| Phạm vi biến | **Hẹp nhất còn dùng được** |
| Câu hỏi cho mọi biến quan trọng | *"Mất điện rồi bật lại, biến này **nên** bằng mấy?"* |
| Hai biến không bao giờ giữ | ⚠⚠ `M_Running` và **biến bước** |

---

## 11.11 Tự kiểm

1. Nêu dải của `INT` và của `DINT`. Vì sao thời gian tích luỹ tính bằng mili-giây **không** được khai
   `INT`?
2. ⭐ `WORD` và `INT` cùng chiếm 16 bit. Chúng khác nhau ở điểm nào? Mẫu bit toàn 1 đọc theo hai kiểu
   cho hai giá trị gì?
3. Giải thích vì sao chương trình dùng địa chỉ tuyệt đối có thể **điều khiển nhầm thiết bị** sau khi
   thêm một module, mà không có báo lỗi nào.
4. ⭐ Dùng tag có tên có loại bỏ hoàn toàn rủi ro đó không? Việc gì vẫn phải làm sau mọi thay đổi
   phần cứng?
5. Nêu năm nhược điểm của địa chỉ tuyệt đối so với tag có tên.
6. Vì sao nên đưa đơn vị vào tên biến? Cho hai ví dụ và nêu loại lỗi mà nó phòng được.
7. ⭐ Bạn có ba trạm giống nhau, mỗi trạm cần theo dõi bảy giá trị. So sánh cách khai báo rời rạc với
   cách dùng UDT — nêu ít nhất ba lợi ích của UDT.
8. Khi nào dùng mảng, khi nào dùng biến rời? Với **hai** trạm của DP-01, sách chọn cách nào và vì sao?
9. Nêu ba phạm vi biến. Vì sao biến đếm vòng lặp `i` **phải** là biến cục bộ?
10. ⭐ Câu hỏi nào phải đặt ra cho mọi biến quan trọng khi quyết định giữ hay không giữ? Vì sao câu
    hỏi đó dùng chữ "**nên**" chứ không phải "sẽ"?

> Câu 2, 4 và 10 là ba câu phân loại. Câu 10 là tinh thần của cả chương: **hành vi của biến là thứ
> bạn THIẾT KẾ, không phải thứ bạn chấp nhận theo mặc định của hệ.**

---

### Chương tiếp theo

Chương 12 — **IO-Link & lớp cảm biến thông minh**. Bạn đã biết dữ liệu được đặt tên và tổ chức thế
nào bên trong PLC. Chương sau nói về một cách khác để đưa dữ liệu **vào** PLC: thay vì mỗi cảm biến
một sợi dây mang một bit, cảm biến gửi cả tham số và trạng thái sức khoẻ của chính nó.

### Nguồn tham khảo chương 11

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: bộ kiểu dữ liệu cơ bản,
  kiểu dẫn xuất, `STRUCT`, `ARRAY`, phạm vi biến, và từ khoá `RETAIN`. *(tiêu chuẩn có bản quyền)*
- Tài liệu lập trình của từng hệ trong Phụ lục A — dùng cho bảng ở mục 11.8: mô hình tag và địa chỉ,
  nơi chứa dữ liệu, cách khai báo biến giữ được. Đây là chỗ khác nhau nhiều nhất giữa các hãng.
- Bảng I/O của DP-01 — Phụ lục J; khối khai báo ở mục 11.7 lấy tên tag từ đó.

> ⚡ Quy ước đặt tên ở mục 11.3 là **quy ước của sách này**, không phải chuẩn. Đơn vị của bạn có thể
> đã có quy ước riêng — và nếu vậy thì **quy ước của đơn vị thắng**. Điều quan trọng không phải chọn
> quy ước nào, mà là **cả chương trình dùng một quy ước duy nhất** (Chương 30).
