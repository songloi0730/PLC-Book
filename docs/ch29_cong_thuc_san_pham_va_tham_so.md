# Chương 29 — Công thức sản phẩm & quản lý tham số

> **Lát cắt máy mẫu:** 2 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp, hai trạm, trình
> tự song song, công thức sản phẩm.

---

## 29.1 Bài toán: đổi mã hàng bằng cách sửa chương trình

Một cỗ máy chạy hai mã hàng. Người viết chương trình đặt thẳng con số vào code:

```iecst
// ✗ SAI — tham số nằm trong logic
T_Cure(IN := (Stn2_Step = 30), PT := T#8S);      // thời gian sấy UV
```

Đổi sang mã hàng thứ hai cần sấy 12 giây. Cách làm: **mở phần mềm lập trình, sửa con số, nạp lại**.

Ba tháng đầu chạy được. Rồi lần lượt:

- Ca đêm cần đổi mã hàng. Người có phần mềm và mật khẩu đang ngủ. Dây chuyền chờ tới sáng.
- Có người sửa `T#12S` thành `T#1.2S` do gõ nhầm. Cả lô không đủ độ bám keo, và **không có triệu
  chứng tại chỗ** — lỗi chỉ lộ ra ở khách hàng cuối.
- Khách hàng hỏi lô hàng tháng trước chạy với thông số nào. Không ai biết, vì con số nằm trong code
  và code không có lịch sử.
- Máy thứ hai được lắp. Hai máy có hai bản chương trình khác nhau, và không ai chắc khác nhau chỗ nào.

Bốn hậu quả này đều đến từ **một** quyết định: để tham số nằm trong logic.

Chương này về cách tách chúng ra — và về những thứ đi kèm mà người ta hay quên: kiểm tra hợp lệ, thời
điểm được phép đổi, và vết truy xuất.

---

## 29.2 Tách tham số khỏi logic

### Nguyên tắc

> **Logic trả lời câu hỏi "máy làm gì theo thứ tự nào". Tham số trả lời câu hỏi "làm với con số bao
> nhiêu". Hai thứ đó đổi với tần suất khác nhau, do người khác nhau, nên phải nằm ở chỗ khác nhau.**

| | Logic | Tham số |
|---|---|---|
| Đổi khi nào | Khi **quy trình** đổi — hiếm | Khi **mã hàng** đổi — hàng ngày |
| Ai đổi | Kỹ sư lập trình | Người vận hành hoặc kỹ thuật viên |
| Cần gì để đổi | Phần mềm lập trình, quyền, kiến thức | Màn hình vận hành (Chương 44) |
| Đổi sai thì | Máy chạy sai trình tự — thường lộ ngay | ⚠ Sản phẩm sai — **có thể không lộ ngay** |

Hàng cuối là lý do mục 29.4 tồn tại.

### Cùng đoạn code, viết đúng

```iecst
// ✓ ĐÚNG — logic không chứa con số; con số đến từ công thức
T_Cure(IN := (Stn2_Step = 30), PT := ActiveRecipe.CureTimeMs);
```

Logic bây giờ nói: *"sấy trong khoảng thời gian mà công thức quy định"*. Nó đúng với mọi mã hàng, và
không cần sửa khi thêm mã hàng mới.

### Cái gì là tham số, cái gì không

| Là tham số | **Không** phải tham số |
|---|---|
| Thời gian sấy, áp keo (Chương 32), chiều dài đoạn keo | ⚠ **Thời gian timeout của bước** — xem bên dưới |
| Kích thước board, vị trí tra keo | Thứ tự các bước |
| Số lượng mỗi khay | ⚠ **Điều kiện an toàn và liên động** |
| Tốc độ chuyền cho từng loại board | Trạng thái an toàn của ngõ ra khi mất điện |

> ⚠⚠ **NGUY HIỂM — hai thứ không bao giờ được đưa vào công thức**
>
> **1. Điều kiện an toàn và liên động.** Nếu "cửa phải đóng mới cho chạy" là một tham số, thì tồn tại
> một công thức tắt được nó. Điều kiện an toàn thuộc về **logic**, và chức năng an toàn thật thì thuộc
> về **mạch an toàn phần cứng** (Chương 47).
>
> **2. Timeout của bước.** Timeout là **bộ phát hiện hỏng hóc**, không phải tham số công nghệ
> (Chương 17, Chương 22 mục 22.9). Cho phép đổi nó qua công thức nghĩa là cho phép **làm mù bộ phát
> hiện** mà không ai duyệt.
>
> Ngoại lệ hợp lý: nếu một bước có thời gian **thật sự** phụ thuộc mã hàng — ví dụ bước sấy dài 8 hay
> 12 giây — thì timeout của bước đó nên được **tính từ tham số** cộng một biên, chứ không phải là một
> ô riêng người vận hành gõ vào:
> `StepTimeoutMs := ActiveRecipe.CureTimeMs + 2000;`

---

## 29.3 Cấu trúc một công thức

Dùng kiểu dữ liệu người dùng (Chương 11, mục 11.5) — công thức là một ví dụ điển hình của UDT:

```iecst
TYPE ST_Recipe :
STRUCT
    // ── Nhận dạng ──
    Id              : INT;          // mã số công thức
    Name            : STRING[20];   // tên đọc được, hiện trên màn hình
    Version         : INT;          // ⭐ tăng mỗi lần sửa
    // ── Tham số trạm 1: tra keo ──
    DispenseLenTenthMm : INT;       // ⭐ đơn vị trong tên (Chương 11)
    DispenseSpeed      : INT;
    // ── Tham số trạm 2: sấy UV ──
    CureTimeMs      : DINT;
    // ── Tham số chung ──
    ConvSpeedPct    : INT;
END_STRUCT
END_TYPE

VAR_GLOBAL RETAIN
    RecipeTable  : ARRAY[1..20] OF ST_Recipe;   // kho công thức
    ActiveRecipe : ST_Recipe;                    // ⭐ bản đang dùng
    ActiveId     : INT;
END_VAR
```

### ⭐ Vì sao có `ActiveRecipe` riêng, không dùng thẳng `RecipeTable[ActiveId]`

Đây là quyết định thiết kế quan trọng nhất của mục này.

Nếu logic đọc thẳng `RecipeTable[ActiveId].CureTimeMs`, thì:

- ⚠ **Sửa bảng công thức trong lúc máy đang chạy sẽ đổi tham số ngay giữa chu trình.** Một board đang
  sấy có thể bị đổi thời gian sấy giữa chừng.
- ⚠ Chỉ số `ActiveId` sai (vượt dải, hoặc chưa nạp) thì logic đọc phải rác — hoặc tệ hơn, đọc vào
  vùng nhớ khác (Chương 11, Bẫy 6).

Với một bản sao `ActiveRecipe`:

- Logic **chỉ đọc bản sao**, không bao giờ đọc bảng.
- Việc nạp từ bảng sang bản sao xảy ra ở **một điểm được kiểm soát**, sau khi đã kiểm tra hợp lệ.
- Sửa bảng lúc máy đang chạy **không ảnh hưởng** tới board đang gia công.

```text
   RecipeTable[]  ──[ nạp có kiểm soát ]──►  ActiveRecipe  ──►  logic đọc
   (người sửa)          ↑                     (chỉ đọc)
                   kiểm hợp lệ + đúng thời điểm
```

---

## 29.4 ⭐ Kiểm tra hợp lệ là việc của PLC

### Vì sao không phải việc của hệ thống trên

Công thức có thể đến từ nhiều nguồn: người vận hành gõ, hệ thống trên gửi xuống (Chương 42), hoặc
nạp từ tệp. Cám dỗ là tin nguồn gửi — *"hệ thống trên đã kiểm rồi"*.

Bốn lý do không được tin:

- **PLC là nơi cuối cùng trước khi con số thành chuyển động thật.** Mọi thứ sai ở tầng trên đều đi qua
  đây; đây là chốt chặn cuối.
- **Nguồn gửi có thể sai** — lỗi mạng làm hỏng dữ liệu, phiên bản phần mềm không khớp, người cấu hình
  nhầm.
- **PLC biết giới hạn vật lý của máy này**, hệ thống trên thì không. Nó không biết trục của bạn chỉ
  đi được 300 mm.
- ⚠ **Khi mất kết nối, người vận hành sẽ nhập tay** — và lúc đó không còn tầng kiểm nào ở trên nữa.

> ⚠⚠ **Nguyên tắc: PLC phải TỪ CHỐI công thức không hợp lệ, không phải "cố chạy với nó".**
> Máy dừng với thông báo rõ ràng là kết quả **tốt**. Máy chạy với tham số vô lý và làm hỏng cả lô là
> kết quả tệ, và nó tệ theo cách mà không ai phát hiện cho tới khi hàng tới khách.

### Kiểm những gì

| Loại kiểm | Ví dụ trên DP-01 |
|---|---|
| **Dải hợp lệ** cho từng tham số | `CureTimeMs` phải trong 3 000 … 30 000 |
| **Quan hệ giữa các tham số** | Chiều dài đoạn keo không vượt kích thước board |
| **Giới hạn vật lý của máy** | Vị trí tra keo phải nằm trong hành trình cơ khí |
| **Đầy đủ** | Mọi trường bắt buộc đã có giá trị, không còn 0 mặc định |
| **Nhận dạng** | `Id` tồn tại trong bảng; `Version` không rỗng |

```iecst
FUNCTION KiemTraCongThuc : BOOL
VAR_INPUT
    r : ST_Recipe;
END_VAR
VAR_OUTPUT
    LyDo : INT;          // ⭐ mã lý do — để nói được SAI Ở ĐÂU
END_VAR

    LyDo := 0;
    KiemTraCongThuc := FALSE;

    IF r.Id < 1 OR r.Id > 20 THEN
        LyDo := 1; RETURN;                       // mã công thức ngoài dải
    END_IF;
    IF r.CureTimeMs < 3000 OR r.CureTimeMs > 30000 THEN
        LyDo := 2; RETURN;                       // thời gian sấy ngoài dải
    END_IF;
    IF r.DispenseLenTenthMm < 50 OR r.DispenseLenTenthMm > 2000 THEN
        LyDo := 3; RETURN;                       // chiều dài đoạn keo ngoài dải
    END_IF;
    IF r.ConvSpeedPct < 10 OR r.ConvSpeedPct > 100 THEN
        LyDo := 4; RETURN;
    END_IF;

    KiemTraCongThuc := TRUE;
END_FUNCTION
```

> ⭐ **Mã lý do quan trọng ngang kết quả đúng/sai.**
> Thông báo *"công thức không hợp lệ"* làm người vận hành bế tắc. Thông báo *"thời gian sấy 45 s vượt
> giới hạn 30 s"* cho họ biết phải làm gì. Đây cũng là nguyên tắc của Chương 44: **thông báo lỗi phải
> nói làm gì tiếp, không chỉ nói cái gì hỏng.**

### ⚠ Giới hạn kiểm tra tự động

Kiểm tra dải bắt được tham số **vô lý**. Nó **không** bắt được tham số **hợp lệ nhưng sai mã hàng** —
sấy 8 giây là hợp lệ, nhưng nếu mã hàng này cần 12 giây thì cả lô vẫn hỏng.

Chống chuyện đó cần **truy xuất**: đọc mã sản phẩm, hỏi hệ thống trên xem board này thuộc mã hàng nào,
và đối chiếu với công thức đang nạp (Chương 42). Trước khi có truy xuất, biện pháp thực dụng là
**hiển thị to tên công thức đang chạy** trên màn hình và yêu cầu xác nhận khi đổi.

---

## 29.5 Đổi công thức khi đang chạy — được phép ở điểm nào

### Vấn đề

Đổi tham số giữa chu trình có thể tạo ra sản phẩm **lai**: nửa đầu gia công theo công thức cũ, nửa
sau theo công thức mới. Sản phẩm đó không đạt cả hai mã hàng, và nó **trông bình thường**.

### Ba mức chính sách

| Mức | Quy tắc | Hợp với |
|---|---|---|
| **Chặt** | Chỉ đổi khi máy **đã xả hết sản phẩm** và ở trạng thái `Idle` | Mặc định — an toàn nhất |
| **Vừa** | Đổi được khi đang chạy, nhưng chỉ **có hiệu lực với sản phẩm vào sau đó** | Máy có truy xuất từng sản phẩm |
| **Lỏng** | Đổi có hiệu lực ngay | ⚠ Gần như không bao giờ đúng cho máy gia công |

Với DP-01, mức **chặt** là mặc định đúng: máy chứa tối đa hai board, xả hết mất chưa tới một phút.

```iecst
// Điều kiện cho phép đổi công thức
M_RecipeChangeAllowed := (MachineState = STATE_IDLE)
                     AND M_MachineEmpty          // đã xả hết board
                     AND NOT M_AnyFault;

// Nạp — chỉ ở điểm được kiểm soát, và chỉ khi hợp lệ
IF TrigLoadRecipe.Q AND M_RecipeChangeAllowed THEN
    IF KiemTraCongThuc(RecipeTable[RequestedId], LyDo => M_RecipeErrCode) THEN
        ActiveRecipe := RecipeTable[RequestedId];    // ⭐ sao chép nguyên cụm
        ActiveId     := RequestedId;
        M_RecipeLoaded := TRUE;
        // ghi vết: ai đổi, lúc nào, từ công thức nào sang công thức nào
    ELSE
        M_RecipeRejected := TRUE;                   // giữ nguyên công thức cũ
    END_IF;
END_IF;
```

Bốn chi tiết đáng chú ý:

- **`TrigLoadRecipe` là cạnh lên** (Chương 16). Không bắt cạnh thì lệnh nạp chạy mỗi vòng quét, ghi
  đè mọi thay đổi người vận hành đang gõ dở (Chương 19, Bẫy 8).
- **Sao chép nguyên cụm UDT** bằng một phép gán — cả công thức chuyển sang cùng lúc, không có khoảnh
  khắc nào một nửa cũ một nửa mới.
- **Từ chối thì giữ nguyên công thức cũ.** Máy không rơi vào trạng thái "không có công thức".
- **Ghi vết ngay tại đây**, vì đây là điểm duy nhất công thức đổi.

> ⚠ **Máy phải biết mình chưa có công thức.**
> Sau khi nạp lại chương trình, hoặc lần chạy đầu tiên, `ActiveRecipe` có thể toàn số 0. Cờ
> `M_RecipeLoaded` phải là điều kiện **cho phép vào `Running`** (Chương 25). Không có nó, máy sẽ chạy
> với thời gian sấy 0 giây.

---

## 29.6 Phiên bản và vết thay đổi

### Vì sao cần

Câu hỏi sẽ đến, thường vào lúc không mong đợi:

> *"Lô hàng ngày 15 tháng trước bị khách trả về. Lúc đó máy chạy với thông số gì?"*

Trả lời được câu này cần ba thứ:

| Cần | Nghĩa là |
|---|---|
| **Phiên bản công thức** | Mỗi lần sửa tham số là một phiên bản mới, không ghi đè im lặng |
| **Vết thay đổi** *(audit trail)* | Ai đổi, đổi lúc nào, đổi từ gì sang gì |
| **Gắn với sản phẩm** | Bản ghi sản xuất lưu **mã và phiên bản công thức** đã dùng |

Hai thứ đầu nằm trong PLC. Thứ ba cần hệ thống trên hoặc ít nhất một bản ghi có thời gian (Chương 42).

### Ghi vết tối thiểu

```iecst
TYPE ST_RecipeLog :
STRUCT
    TimeStamp   : DATE_AND_TIME;
    UserLevel   : INT;          // ai đổi — theo phân quyền màn hình (Chương 44)
    OldId       : INT;
    OldVersion  : INT;
    NewId       : INT;
    NewVersion  : INT;
END_STRUCT
END_TYPE

VAR_GLOBAL RETAIN
    RecipeLog    : ARRAY[0..49] OF ST_RecipeLog;   // vòng, giữ 50 lần đổi gần nhất
    RecipeLogIdx : INT;
END_VAR
```

> 💡 **Bộ nhớ PLC hữu hạn — giữ 50 bản ghi gần nhất là đủ cho việc tra tại chỗ.**
> Lịch sử dài hạn thuộc về hệ thống trên hoặc về tệp xuất định kỳ. Nhưng **50 bản ghi trong PLC vẫn
> có giá trị riêng**: nó trả lời được câu hỏi lúc 2 giờ sáng, khi không ai truy cập được hệ thống
> trên.

### Ai được sửa

Phân quyền là **yêu cầu bắt buộc** với công thức, không phải tính năng thêm:

| Cấp | Được làm gì |
|---|---|
| Người vận hành | **Chọn** công thức từ bảng; không sửa giá trị |
| Kỹ thuật viên | Sửa tham số trong dải cho phép |
| Kỹ sư | Sửa dải cho phép, thêm công thức mới |

Cơ chế phân quyền nằm ở màn hình vận hành (Chương 44), nhưng ⚠ **PLC vẫn phải tự kiểm dải** — vì
màn hình có thể bị thay, bị bỏ qua, hoặc công thức có thể đến từ hệ thống trên (mục 29.4).

---

## 29.6b ⭐⭐ "Được duyệt" và "đã chứng thực" là HAI câu hỏi khác nhau

Mục trên lo việc **ghi vết ai sửa gì**. Còn một câu hỏi nữa mà công thức phải trả lời được trước khi
đem ra chạy hàng — và ⚠ nhiều hệ gộp nó làm một, gây ra đúng loại sự cố khó truy.

| Câu hỏi | Ai trả lời | Ý nghĩa |
|---|---|---|
| ⭐ **Công thức này ĐÃ ĐƯỢC DUYỆT chưa?** | Kỹ thuật quá trình, quản lý sản xuất | Nội dung công thức là **đúng về mặt công nghệ** |
| ⭐⭐ **Nó ĐÃ ĐƯỢC CHỨNG THỰC trên MÁY NÀY chưa?** | Người chạy thử trên chính cỗ máy đó | Đã chạy thật ở đây và **cho kết quả đạt** |

> ⚠⚠ **Hai câu này độc lập, và đó là điểm mấu chốt.**
>
> Một công thức được kỹ thuật duyệt hoàn toàn có thể ⚠ **chưa từng chạy trên máy số 3** — vì máy số 3
> có gá khác, đèn khác, hoặc vừa thay một cơ cấu. ⭐ *"Đã duyệt"* **không suy ra được** *"chạy được ở
> đây"*.
>
> ⭐ Ngược lại cũng vậy: ai đó chỉnh tham số cho chạy được trên máy số 3 thì ⚠ **đó chưa phải công
> thức đã duyệt** — nó chỉ là một bản vá tại chỗ.

### ⭐ Mức duyệt là một CON SỐ, không phải một dấu tích

Cách làm quen thuộc là một cờ *"đã duyệt: có/không"*. ⭐ Cách chặt hơn: **mức duyệt là một con số**,
và **khoá được suy ra từ con số đó**:

```text
Công thức có  Mức duyệt  ≥  Ngưỡng chỉ-đọc của kho   →  KHOÁ, không sửa được
```

| | |
|---|---|
| ⭐⭐ Vì sao hơn hẳn cờ có/không | **Khoá là HỆ QUẢ**, không phải việc ai đó phải nhớ bật |
| ⭐ Đặt ngưỡng bằng 0 | ⭐ **Mọi công thức đều bị khoá** — mặc định an toàn cho môi trường sản xuất |
| ⭐ Nhiều mức | Nháp · đã kiểm nội bộ · đã duyệt sản xuất — mỗi mức mở ra quyền khác nhau |

> ⭐ **Đây là cùng tinh thần với "làm cho hỏng hóc trở nên phát hiện được"** ở Chương 48: ⚠ thay vì
> trông vào việc **người ta nhớ khoá công thức**, hãy để trạng thái khoá **tự suy ra** từ một thuộc
> tính mà quy trình bắt buộc phải điền.

### ⭐ Vòng đời một công thức — các trạng thái đáng có

| Trạng thái | Nghĩa | Được làm gì |
|---|---|---|
| **Tạo / sửa** | Bản nháp trong kho | Sửa tự do |
| ⭐ **Đã duyệt** | Nội dung được người có thẩm quyền chấp nhận | ⚠ **Khoá** nếu mức duyệt vượt ngưỡng |
| ⭐⭐ **Đã chứng thực trên máy này** | Đã chạy thật ở đây, kết quả đạt | ⭐ **Được phép chạy sản xuất** |
| ⚠ **Bị rút chứng thực** | Máy thay đổi, hoặc kết quả không còn đạt | ⚠⚠ **Phải chứng thực lại trước khi chạy tiếp** |

> ⚠⚠ **Trạng thái cuối là trạng thái hay bị bỏ quên nhất, và nó bảo vệ đúng lúc nguy hiểm nhất.**
>
> Sau khi **thay cơ cấu, đổi cảm biến, hay sửa cơ khí** (Chương 53), ⭐ chứng thực cũ **không còn giá
> trị** — dù công thức không đổi một chữ. ⚠ Hệ nào không có trạng thái này thì sau mỗi lần bảo trì,
> máy chạy tiếp với một chứng thực **đã hết hiệu lực mà không ai biết**.
>
> ⭐ **Cách làm tối thiểu nếu hệ của bạn không có sẵn:** giữ hai trường trong bản ghi công thức —
> *"mức duyệt"* và *"lần chứng thực gần nhất trên máy này (ngày, người, kết quả)"* — và ⭐ **xoá trường
> thứ hai trong quy trình bảo trì**, cùng chỗ với việc gỡ cưỡng bức (Chương 51, mục 51.7).

---

## 29.7 Trên máy mẫu DP-01

Bảng công thức cho ba mã hàng:

| Trường | Đơn vị | Mã A | Mã B | Mã C | Dải hợp lệ |
|---|---|---|---|---|---|
| `Name` | — | `BOARD-A` | `BOARD-B` | `BOARD-C` | — |
| `Version` | — | 3 | 1 | 2 | ≥ 1 |
| `DispenseLenTenthMm` | 0,1 mm | 800 | 1 200 | 450 | 50 … 2 000 |
| `DispenseSpeed` | % | 60 | 45 | 80 | 10 … 100 |
| `CureTimeMs` | ms | 8 000 | 12 000 | 6 000 | 3 000 … 30 000 |
| `ConvSpeedPct` | % | 70 | 70 | 90 | 10 … 100 |

Ba điều rút ra từ bảng này:

- **Đơn vị nằm trong tên trường.** `DispenseLenTenthMm` = 800 nghĩa là 80,0 mm. Không có chỗ cho hiểu
  nhầm (Chương 11, mục 11.3).
- **Cột "dải hợp lệ" là đặc tả của hàm kiểm tra** ở mục 29.4. Nó phải được điền lúc viết đặc tả
  (Chương 23), không phải lúc viết code.
- **Mã B cần sấy 12 giây, mã C chỉ 6 giây.** Timeout của bước sấy vì vậy phải tính từ tham số
  (`CureTimeMs + 2000`), không phải một con số cố định — nếu đặt cứng 10 giây thì mã B luôn báo lỗi.

### Điều kiện cho phép vào `Running`

Gom lại từ nhiều chương, công thức đóng góp hai điều kiện:

```iecst
M_CanStart := M_Homed                    // đã về gốc (Chương 28)
          AND M_RecipeLoaded             // ⭐ đã nạp công thức
          AND NOT M_RecipeRejected       // ⭐ công thức hợp lệ
          AND DI_AirOK
          AND DI_EStopOK
          AND NOT M_AnyFault;
```

Viết đầy đủ từng điều kiện thay vì gom vào một cờ tổng — đúng nguyên tắc ở Chương 24, mục 24.7: khi
máy không khởi động được, người vận hành nhìn thấy ngay **điều kiện nào** đang thiếu.

---

## 29.8 Khác biệt giữa các hãng

| Khía cạnh | Siemens | Mitsubishi | Rockwell | CODESYS / TwinCAT |
|---|---|---|---|---|
| Nơi chứa bảng công thức | **Khối dữ liệu** *(DB)*, đặt thuộc tính *Retain* | Vùng thanh ghi `D` thuộc dải chốt | Tag mảng UDT — ⭐ giữ mặc định | `VAR_GLOBAL RETAIN` |
| Sao chép nguyên cụm UDT | Phép gán, hoặc lệnh sao chép khối | Lệnh sao chép khối thanh ghi | Phép gán tag UDT | Phép gán |
| Đọc/ghi từ màn hình vận hành (Chương 44) | Ánh xạ DB tới tag màn hình | Ánh xạ thiết bị | Ánh xạ tag | Ánh xạ biến |
| ⚠ Dung lượng vùng giữ được | **Hữu hạn và khác nhau nhiều** theo dòng CPU | Dải chốt đặt trong tham số PLC | Rộng rãi hơn | Tuỳ cấu hình |
| Lưu ra tệp / thẻ nhớ | Có, tuỳ dòng CPU | Có, tuỳ dòng | Có | Có |

> ⚠ **Kiểm dung lượng vùng nhớ giữ được TRƯỚC khi thiết kế bảng công thức.**
> Hai mươi công thức, mỗi công thức mười trường — nghe nhỏ, nhưng ở CPU dòng thấp thì vùng giữ được
> có thể rất hạn chế, và bạn còn phải chia nó với số liệu sản xuất và nhật ký (Chương 18, mục 18.6).
>
> Nếu không đủ: giữ ở PLC **một** công thức đang dùng cộng vài công thức hay chạy, còn kho đầy đủ để
> ở màn hình vận hành (Chương 44) hoặc hệ thống trên. ⚠ Nhưng khi đó **PLC vẫn phải tự kiểm hợp lệ** khi nhận —
> mục 29.4 không có ngoại lệ.

---

## 29.9 Bẫy thường gặp

### 🔍 BẪY 1 — Tham số nằm trong logic

**Hiện tượng:** đổi mã hàng phải mở phần mềm lập trình; ca đêm không đổi được; không có lịch sử thông
số đã dùng.
**Cách sửa:** tách ra công thức (mục 29.2). Đây là bẫy gốc mà cả chương giải quyết.

### 🔍 BẪY 2 — Logic đọc thẳng từ bảng công thức

`PT := RecipeTable[ActiveId].CureTimeMs`

**Hiện tượng:** sửa bảng lúc máy đang chạy làm đổi tham số **giữa chu trình**; board đang gia công
thành sản phẩm lai.
**Cách sửa:** logic chỉ đọc `ActiveRecipe`; việc nạp xảy ra ở một điểm được kiểm soát (mục 29.3).

### 🔍 BẪY 3 — Tin công thức từ hệ thống trên mà không kiểm

**Hiện tượng:** một giá trị vô lý đi thẳng vào máy; hoặc lỗi mạng làm hỏng dữ liệu mà không ai phát
hiện.
**Cách sửa:** ⚠ PLC là chốt chặn cuối. **Luôn kiểm dải**, kể cả khi nguồn "đáng tin" (mục 29.4).

### 🔍 BẪY 4 — Từ chối công thức mà không nói lý do

**Hiện tượng:** người vận hành thấy "công thức không hợp lệ" và bế tắc; gọi kỹ sư lúc 2 giờ sáng.
**Cách sửa:** mã lý do cụ thể, và thông báo nói rõ **trường nào, giá trị bao nhiêu, giới hạn bao
nhiêu**.

### 🔍 BẪY 5 — Không bắt cạnh khi nạp công thức

**Hiện tượng:** người vận hành sửa một tham số, giá trị **nhảy về giá trị cũ ngay lập tức** — vì lệnh
nạp chạy mỗi vòng quét và ghi đè.
**Cách sửa:** bắt cạnh lên của lệnh nạp (Chương 16; Chương 19, Bẫy 8).

### 🔍 BẪY 6 — Cho đổi công thức giữa chu trình

**Hiện tượng:** sản phẩm lai — nửa đầu theo công thức cũ, nửa sau theo công thức mới. **Trông bình
thường**, không phát hiện được bằng mắt.
**Cách sửa:** chính sách mức **chặt** là mặc định: chỉ đổi khi máy đã xả hết và ở `Idle` (mục 29.5).

### 🔍 BẪY 7 — Đưa timeout của bước vào công thức

**Hiện tượng:** khi cơ cấu chậm dần, người vận hành tăng timeout qua màn hình cho hết báo lỗi — và
**làm mù bộ phát hiện** mà không ai duyệt.
**Cách sửa:** timeout **tính từ** tham số cộng biên, không phải ô người vận hành gõ (mục 29.2).

### 🔍 BẪY 8 — Máy chạy khi chưa nạp công thức

**Hiện tượng:** sau khi nạp lại chương trình, `ActiveRecipe` toàn số 0; máy chạy với thời gian sấy 0
giây và cả lô đầu ca hỏng.
**Cách sửa:** `M_RecipeLoaded` là điều kiện bắt buộc để vào `Running` (mục 29.5, Chương 25).

### 🔍 BẪY 9 — Không ghi vết khi đổi công thức

**Hiện tượng:** lô hàng bị trả về, không ai trả lời được lúc đó máy chạy thông số gì, ai đổi, đổi
lúc nào.
**Cách sửa:** ghi vết ngay tại điểm nạp — thời gian, người, công thức cũ và mới (mục 29.6).

### 🔍 BẪY 10 — Cho phép sửa dải hợp lệ ngang cấp với sửa tham số

**Hiện tượng:** người vận hành gặp thông báo "vượt giới hạn" và **nới giới hạn ra** thay vì hỏi lại.
Cơ chế bảo vệ bị vô hiệu hoá từ bên trong.
**Cách sửa:** sửa **tham số** và sửa **dải hợp lệ** là hai cấp quyền khác nhau (mục 29.6).

---

## 29.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Tham số để ở đâu | Trong **công thức**, không trong logic |
| Hai thứ không bao giờ đưa vào công thức | ⚠⚠ **Điều kiện an toàn/liên động** và **timeout của bước** |
| Bước cần thời gian theo mã hàng | Timeout = **tham số + biên**, tính trong code |
| Logic đọc công thức ở đâu | ⭐ Chỉ đọc **`ActiveRecipe`**, không đọc thẳng bảng |
| Ai kiểm tra hợp lệ | ⭐ **PLC** — kể cả khi nguồn gửi đã kiểm |
| Kiểm những gì | Dải · quan hệ giữa tham số · giới hạn vật lý · đầy đủ · nhận dạng |
| Công thức không hợp lệ thì | **Từ chối**, giữ nguyên công thức cũ, **nói rõ lý do** |
| Đổi công thức lúc nào | Mặc định: **máy đã xả hết và ở `Idle`** |
| Nạp công thức | **Bắt cạnh**; sao chép **nguyên cụm** một lần |
| Chưa nạp công thức thì | ⚠ **Không cho vào `Running`** |
| Ghi vết | Thời gian · người · công thức cũ → mới, ghi **tại điểm nạp** |
| Phân quyền | Chọn / sửa tham số / sửa dải hợp lệ là **ba cấp khác nhau** |
| ⭐⭐ Hai câu hỏi độc lập | **Đã duyệt** (nội dung đúng) và ⭐ **đã chứng thực trên MÁY NÀY** |
| ⭐ Mức duyệt nên là gì | **Một con số**, và **khoá tự suy ra** khi vượt ngưỡng — không phải cờ ai đó nhớ bật |
| ⚠⚠ Sau khi bảo trì đổi cơ cấu | ⭐ **Chứng thực cũ hết hiệu lực** — phải chứng thực lại dù công thức không đổi |
| Trước khi thiết kế bảng công thức | ⚠ Kiểm **dung lượng vùng nhớ giữ được** của CPU |

---

## 29.11 Tự kiểm

1. Nêu bốn hậu quả của việc để tham số nằm trong logic (mục 29.1).
2. Logic và tham số khác nhau ở bốn điểm nào? Điểm nào giải thích vì sao kiểm tra hợp lệ lại quan
   trọng?
3. ⭐ Vì sao **điều kiện an toàn** và **timeout của bước** không bao giờ được đưa vào công thức?
4. Một bước sấy cần 8 giây ở mã hàng này và 12 giây ở mã hàng khác. Timeout của bước đó nên được xác
   định thế nào?
5. ⭐ Vì sao logic phải đọc `ActiveRecipe` chứ không đọc thẳng `RecipeTable[ActiveId]`? Nêu hai hậu
   quả của cách sai.
6. Nêu bốn lý do PLC phải tự kiểm tra hợp lệ dù hệ thống trên đã kiểm.
7. Vì sao **mã lý do** quan trọng ngang với kết quả đúng/sai của hàm kiểm tra?
8. Kiểm tra dải bắt được loại sai nào và **không** bắt được loại sai nào? Chống loại còn lại bằng gì?
9. Nêu ba mức chính sách đổi công thức khi đang chạy. Mức nào là mặc định đúng cho DP-01 và vì sao?
10. ⭐ Người vận hành gặp thông báo "vượt giới hạn" và nới dải hợp lệ ra. Vì sao đó là vấn đề nghiêm
    trọng, và cơ chế nào ngăn được nó?
11. ⭐⭐ Nêu **hai câu hỏi độc lập** phải trả lời trước khi cho một công thức chạy hàng. ⚠ Vì sao
    *"đã duyệt"* **không suy ra được** *"chạy được ở đây"*?
12. ⭐ Vì sao để **mức duyệt là một con số** và **khoá tự suy ra** thì chặt hơn một cờ *"đã duyệt:
    có/không"*? Liên hệ với nguyên tắc ở Chương 48.
13. ⚠⚠ Máy vừa thay một cơ cấu, công thức **không đổi một chữ**. ⭐ Có được chạy tiếp ngay không, vì
    sao? Nêu việc tối thiểu phải làm.

> Câu 3, 5 và 10 là ba câu phân loại. Câu 10 là tinh thần của cả chương: **một cơ chế bảo vệ mà người
> dùng tự nới được thì không phải cơ chế bảo vệ.**

---

### Chương tiếp theo

Chương 30 — **Chuẩn hoá & tái sử dụng**. Bạn đã có đủ công cụ để viết một chương trình đúng. Chương
sau về việc viết nó sao cho **người khác sửa được** — đặt tên, cấu trúc, chú thích, thư viện dùng
lại, và quản lý phiên bản.

### Nguồn tham khảo chương 29

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: kiểu dữ liệu dẫn xuất
  (`STRUCT`), mảng, và từ khoá `RETAIN` dùng cho bảng công thức. *(tiêu chuẩn có bản quyền)*
- IEC 62682 — *Management of alarm systems for the process industries*: nguyên tắc thông báo phải kèm
  hành động ứng phó — áp cho thông báo từ chối công thức ở mục 29.4.
- Tài liệu CPU của từng hệ trong Phụ lục A — dùng cho ⚠ **dung lượng vùng nhớ giữ được**, con số phải
  kiểm trước khi thiết kế bảng công thức.
- Bảng công thức và đặc tả tham số của DP-01 — Phụ lục J; bảng ở mục 29.7 lấy từ đó.
- Biểu mẫu **nhật ký thay đổi công thức** — Phụ lục C.
- ⭐ **SEMI E42** — *Recipe Management Standard: Concepts, Behavior, and Message Services*: vòng đời
  công thức (mục 8.1) và các thao tác **duyệt · bảo vệ · chứng thực / rút chứng thực** (mục 8.2.4–8.2.8);
  ⭐⭐ cơ chế **khoá suy ra từ ngưỡng mức duyệt** (mục 8.2.5) thay cho một cờ đặt tay — nền cho
  mục 29.6b.

> ⚡ Các dải hợp lệ ở mục 29.7 là **giá trị của máy mẫu DP-01**, không phải giá trị áp dụng chung. Dải
> của máy bạn đến từ **giới hạn vật lý của cơ cấu** và từ **yêu cầu công nghệ của sản phẩm** — hai
> thứ này phải được xác định lúc viết đặc tả (Chương 23), với sự tham gia của người hiểu quy trình
> sản xuất, không phải do người lập trình tự đặt.
