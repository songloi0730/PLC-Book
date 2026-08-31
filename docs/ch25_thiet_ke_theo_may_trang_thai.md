# Chương 25 — Thiết kế theo máy trạng thái

> **Lát cắt máy mẫu:** 2 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp, cộng thêm mô hình
> trạng thái hai trạm và trình tự song song.

---

## 25.1 Bài toán: cỗ máy ở hai trạng thái cùng lúc

Một kỹ sư viết chương trình cho DP-01. Cách làm rất tự nhiên: mỗi tình huống một cờ.

```text
M_Running     — máy đang chạy tự động
M_Paused      — máy đang tạm dừng
M_Homing      — máy đang về gốc
M_Fault       — máy đang lỗi
```

Mỗi cờ được bật/tắt ở chỗ cần thiết. Chạy thử: tốt. Thêm chế độ tay: vẫn tốt. Thêm xử lý mất khí: vẫn
tốt. Thêm nút Reset: **bắt đầu lạ**.

Một hôm máy dừng giữa chu trình. Kỹ thuật viên mở phần mềm xem, thấy:

```text
M_Running = 1        M_Paused  = 1
M_Homing  = 0        M_Fault   = 1
```

Máy **đang chạy, đang tạm dừng, và đang lỗi — cùng một lúc**. Không ai biết nên tin cờ nào. Không ai
biết nhấn Reset thì máy sẽ làm gì.

Đây không phải lỗi lập trình cẩu thả. Đây là **hậu quả toán học tất yếu** của cách tổ chức đó: bốn cờ
độc lập sinh ra 16 tổ hợp, mà chỉ 4 tổ hợp có nghĩa. Mười hai tổ hợp còn lại là vùng chưa ai định
nghĩa — và chương trình càng lớn thì xác suất rơi vào đó càng cao.

Chương này là cách thoát khỏi vùng đó: thay vì nhiều cờ độc lập, dùng **một biến duy nhất** cho biết
máy đang ở đâu.

---

## 25.2 Máy trạng thái là gì

**Máy trạng thái** *(state machine)* là một cách mô tả hệ thống bằng ba thứ, và chỉ ba thứ:

1. **Tập trạng thái** — danh sách đầy đủ những chỗ máy có thể ở. Hữu hạn, đặt tên rõ ràng.
2. **Trạng thái hiện tại** — **đúng một** trạng thái tại mỗi thời điểm. Không hai, không không.
3. **Các chuyển tiếp** *(transition)* — từ trạng thái nào sang trạng thái nào, với điều kiện gì.

Bất biến quan trọng nhất nằm ở dòng thứ hai:

> **Tại mọi thời điểm, máy ở đúng một trạng thái.**
>
> Không phải quy ước cho gọn — đây là **tính chất được bảo đảm bởi cấu trúc dữ liệu**: nếu trạng thái
> được lưu trong *một* biến, thì việc "ở hai trạng thái cùng lúc" **không biểu diễn được**, nên không
> xảy ra được.

So sánh trực tiếp với cách dùng cờ rải rác:

| | Nhiều cờ độc lập | Một biến trạng thái |
|---|---|---|
| Số tổ hợp biểu diễn được | 2ⁿ (n cờ → 16 với 4 cờ) | Đúng bằng số trạng thái đã định nghĩa |
| Tổ hợp vô nghĩa | **Có, và nhiều hơn tổ hợp có nghĩa** | **Không tồn tại** |
| Muốn biết máy đang ở đâu | Đọc n bit rồi tự suy luận | **Đọc một biến** |
| Thêm một trạng thái mới | Thêm một cờ → số tổ hợp nhân đôi | Thêm một giá trị → tuyến tính |
| Kiểm thử | Phải thử 2ⁿ tổ hợp | Thử từng trạng thái và từng chuyển tiếp |

Cột cuối là lý do thực tế nhất. Với bốn cờ, kiểm thử đầy đủ nghĩa là thử 16 tổ hợp — và bạn sẽ không
làm. Với một biến bốn trạng thái, bạn thử bốn trạng thái. Việc đó làm được.

> 💡 **MẸO — cách nhận ra chương trình đang cần máy trạng thái**
> Nếu bạn thấy mình viết một dòng kiểu `IF M_Running AND NOT M_Paused AND NOT M_Fault THEN…` — nghĩa là
> bạn **đang tự tay dựng lại** một trạng thái từ nhiều mảnh. Đó là dấu hiệu rõ ràng: hãy đặt tên cho
> trạng thái đó và lưu nó vào một biến.

---

## 25.3 Mô hình trạng thái chuẩn cho một cỗ máy

Máy tự động hoá, dù làm gì, gần như luôn quy về **bảy trạng thái** dưới đây. Bạn có thể bớt (máy đơn
giản không cần `Hold`) nhưng hiếm khi cần thêm.

![Máy trạng thái chuẩn cho một cỗ máy](../assets/ch25/hinh_25_1_may_trang_thai.svg)

*Hình 25.1 — Bảy trạng thái và các chuyển tiếp hợp lệ. Mũi tên đỏ từ mọi trạng thái vào Alarm là điểm
mấu chốt: lỗi có thể xảy ra ở bất cứ đâu.*

| Trạng thái | Máy đang làm gì | Ra khỏi bằng cách nào |
|---|---|---|
| **Uninitialized** | Vừa cấp nguồn. Chưa biết cơ cấu đang ở đâu | Người vận hành yêu cầu về gốc |
| **Homing** | Đang đưa các cơ cấu về vị trí gốc đã biết | Về gốc xong → `Idle`; lỗi → `Alarm` |
| **Idle** | Đã về gốc, đủ điều kiện, đang chờ lệnh | Nhấn Start → `Running`; chọn tay → `Manual` |
| **Running** | Đang chạy chu trình tự động | Nhấn Hold; nhấn Stop; hoặc phát sinh lỗi |
| **Hold** | Đã dừng có kiểm soát, **giữ nguyên vị trí và sản phẩm** | Tiếp tục → `Running`; huỷ → `Idle` |
| **Alarm** | Có lỗi. Mọi chuyển động đã dừng | Xử lý xong nguyên nhân → nhấn Reset |
| **Resetting** | Đang xoá lỗi và kiểm tra điều kiện | Sạch lỗi → `Homing` (không về thẳng `Idle` — xem dưới) |

### Ba quyết định thiết kế cần hiểu, không chỉ chép

**Vì sao `Uninitialized` tách khỏi `Idle`.** Vừa cấp nguồn, PLC **không biết** xy-lanh đang ra hay vào,
board đang nằm ở đâu. `Idle` nghĩa là "đã biết mọi thứ ở đâu và sẵn sàng chạy" — một lời hứa mà máy
chưa về gốc không giữ được. Gộp hai trạng thái này là mời máy khởi động từ một tư thế không xác định.

**Vì sao `Resetting` không về thẳng `Idle`.** Sau khi lỗi được xoá, các cơ cấu vẫn đang ở tư thế dở
dang từ lúc sự cố. `Idle` đòi hỏi đã về gốc. Nên đường đúng là `Resetting → Homing → Idle`. Đây là
một trong những chỗ người mới hay cắt ngắn, và hậu quả là **máy khởi động lại từ tư thế bất kỳ** —
Chương 28 mổ xẻ đầy đủ.

**Vì sao mọi trạng thái đều có đường vào `Alarm`.** Lỗi không xin phép. Mất khí có thể xảy ra lúc đang
`Homing`, cảm biến có thể hỏng lúc đang `Idle`. Nếu bạn chỉ cho phép `Running → Alarm` thì lỗi phát
sinh ở trạng thái khác sẽ **không có chỗ đi** — máy kẹt ở một trạng thái mà điều kiện của nó không còn
đúng nữa.

> ⚡ **LƯU Ý — `Hold` khác `Stop` ở chỗ nào**
> `Hold` là **dừng có kiểm soát, giữ nguyên hiện trạng** để chạy tiếp được: board vẫn kẹp, vị trí vẫn
> giữ, chu trình nhớ đang ở bước nào. `Stop` là **kết thúc chu trình**: nhả sản phẩm, về gốc, quay lại
> `Idle`. Hai thứ này thường bị gộp làm một, và hậu quả là người vận hành nhấn "dừng" rồi không biết
> máy sẽ giữ hay nhả board đang gia công.

> ⚠ **NGUY HIỂM**
> Không trạng thái nào ở đây là **dừng khẩn cấp**. E-Stop **không phải một trạng thái trong máy trạng
> thái** — nó là mạch cứng cắt nguồn cơ cấu, hoạt động kể cả khi CPU treo. Máy trạng thái chỉ *phản
> ứng* với việc E-Stop đã bị nhấn (chuyển sang `Alarm`), chứ **không thực hiện** việc dừng. Chương 47.

---

## 25.4 Bảng chuyển trạng thái — công cụ làm việc thật

Sơ đồ để nhìn tổng thể; **bảng để làm việc**. Bảng chuyển trạng thái là thứ bạn điền *trước khi* viết
dòng code đầu tiên, và là thứ đội kiểm thử dùng để soát.

Mỗi dòng là một chuyển tiếp, và phải trả lời đủ bốn cột:

| Từ | Điều kiện chuyển | Sang | Hành động khi vào trạng thái mới |
|---|---|---|---|
| Uninitialized | `DI_ResetPB` và không có lỗi | Homing | Bật đèn vàng; bắt đầu trình tự về gốc |
| Homing | Mọi cơ cấu báo đã ở gốc | Idle | Bật đèn vàng; xoá bước chu trình về 0 |
| Homing | Quá thời gian cho phép | Alarm | Ghi mã lỗi "về gốc quá thời gian" |
| Idle | `DI_StartPB` và cửa đóng và khí đủ | Running | Bật đèn xanh; cho phép chuyền chạy |
| Running | `DI_StopPB` (nút Hold) | Hold | Bật đèn vàng; **giữ nguyên mọi ngõ ra vị trí** |
| Running | Bất kỳ điều kiện lỗi nào | Alarm | Bật đèn đỏ + còi; cắt lệnh chuyển động |
| Hold | `DI_StartPB` | Running | Bật đèn xanh; chạy tiếp từ bước đang nhớ |
| Hold | Giữ `DI_StopPB` quá 2 giây | Idle | Nhả sản phẩm theo quy trình an toàn, về gốc |
| Alarm | `DI_ResetPB` và nguyên nhân đã hết | Resetting | Xoá cờ lỗi; tắt còi |
| Resetting | Đã xoá xong | Homing | Bắt đầu trình tự về gốc |
| **Mọi trạng thái** | Mất khí / mất mạch an toàn / lỗi cơ cấu | Alarm | Như trên |

Cột thứ tư — **hành động khi vào trạng thái** *(entry action)* — là cột người mới hay bỏ trống, và đó
là nguồn của rất nhiều lỗi. Xem Bẫy 1.

> 💡 **MẸO**
> Điền bảng này **bằng bút trên giấy, cùng với người vận hành**, trước khi mở phần mềm. Người vận hành
> sẽ hỏi những câu bạn không nghĩ tới: *"đang chạy mà mất điện thì board còn kẹp không?"*, *"nhấn Reset
> lúc còn board trong máy thì nó làm gì?"*. Mỗi câu như vậy là một dòng còn thiếu trong bảng.

---

## 25.5 Hiện thực hoá — hai cách

Máy trạng thái không phụ thuộc ngôn ngữ. Dưới đây là cùng một mô hình, viết hai kiểu.

### Cách 1 — biến trạng thái + `CASE` (Structured Text)

Cách gọn nhất khi ngôn ngữ có `CASE`.

```iecst
// Khai báo trạng thái bằng kiểu liệt kê — KHÔNG dùng số trần
TYPE E_MachineState :
    (Uninitialized, Homing, Idle, Running, Hold, Alarm, Resetting);
END_TYPE

VAR
    MachineState : E_MachineState := Uninitialized;
END_VAR

// ── Chuyển tiếp ưu tiên cao nhất: lỗi từ BẤT KỲ trạng thái nào ──
// Đặt TRƯỚC khối CASE để nó luôn thắng
IF M_AnyFault AND MachineState <> Alarm AND MachineState <> Resetting THEN
    MachineState := Alarm;
    DO_LampRed  := TRUE;
    DO_Buzzer   := TRUE;
    M_MotionEnable := FALSE;          // cắt mọi lệnh chuyển động
END_IF;

CASE MachineState OF

    Uninitialized:
        DO_LampYellow := TRUE;
        IF R_TRIG_Reset.Q THEN                 // bắt sườn lên nút Reset
            MachineState := Homing;
        END_IF;

    Homing:
        M_HomingRun := TRUE;                   // gọi trình tự về gốc (Ch.28)
        IF M_HomingDone THEN
            M_HomingRun := FALSE;
            M_CycleStep := 0;                  // xoá bước chu trình
            MachineState := Idle;
        END_IF;
        // timeout xử lý bên trong trình tự về gốc → bật M_AnyFault

    Idle:
        DO_LampYellow := TRUE;
        IF R_TRIG_Start.Q AND M_AllPermissive THEN
            MachineState := Running;
        END_IF;

    Running:
        DO_LampGreen   := TRUE;
        M_CycleEnable  := TRUE;                // cho phép trình tự chạy (Ch.26)
        IF R_TRIG_Stop.Q THEN
            M_CycleEnable := FALSE;            // dừng nhưng GIỮ nguyên vị trí
            MachineState  := Hold;
        END_IF;

    Hold:
        DO_LampYellow := TRUE;
        IF R_TRIG_Start.Q THEN
            MachineState := Running;           // chạy tiếp từ bước đang nhớ
        ELSIF T_StopHeld.Q THEN                // giữ nút Stop quá 2 giây
            MachineState := Idle;              // huỷ chu trình, về gốc
        END_IF;

    Alarm:
        DO_LampRed := TRUE;
        IF R_TRIG_Reset.Q AND NOT M_AnyFault THEN   // nguyên nhân phải hết TRƯỚC
            MachineState := Resetting;
        END_IF;

    Resetting:
        M_ClearFaults := TRUE;
        DO_Buzzer     := FALSE;
        IF M_FaultsCleared THEN
            M_ClearFaults := FALSE;
            MachineState  := Homing;           // KHÔNG về thẳng Idle
        END_IF;

END_CASE;
```

Ba điểm đáng chú ý trong đoạn trên:

- **Khối lỗi đặt ngoài và trước `CASE`.** Nhờ vậy nó thắng mọi trạng thái, đúng như dòng cuối bảng
  chuyển trạng thái. Nếu nhét điều kiện lỗi vào từng nhánh `CASE` thì bạn phải nhớ lặp lại ở bảy chỗ,
  và sẽ quên ít nhất một chỗ.
- **Dùng kiểu liệt kê, không dùng số trần.** `MachineState := 3` không nói lên điều gì khi bạn xem
  trạng thái trực tuyến lúc hai giờ sáng; `Running` thì nói.
- **Reset đòi hỏi `NOT M_AnyFault`.** Nhấn Reset khi nguyên nhân còn nguyên thì không được chuyển —
  nếu không, máy sẽ quay vòng `Alarm → Resetting → Alarm` liên tục.

### Cách 2 — bit trạng thái (Ladder Diagram)

Khi phải viết bằng ladder — thường vì đội bảo trì tại nhà máy chỉ đọc được ladder (xem Chương 20) —
dùng **một bit cho mỗi trạng thái**, kèm một quy tắc bắt buộc.

```text
// Mỗi trạng thái một bit
S_Uninit   S_Homing   S_Idle   S_Running   S_Hold   S_Alarm   S_Resetting
```

> ⚠ **NGUY HIỂM — quy tắc bắt buộc khi dùng bit trạng thái**
> Cách này **đưa trở lại đúng rủi ro mà máy trạng thái sinh ra để tránh**: bảy bit độc lập lại có 128
> tổ hợp. Nó chỉ an toàn nếu bạn **cưỡng chế bất biến "đúng một bit bật"** bằng cấu trúc code:
>
> - Mọi chuyển tiếp viết theo mẫu **bật bit mới, tắt bit cũ, trong cùng một nấc thang**.
> - Thêm một nấc **giám sát**: đếm số bit đang bật; khác 1 thì bật `M_AnyFault`. Nấc này là lưới an
>   toàn — nó biến một lỗi logic âm thầm thành một báo động nhìn thấy được.

```text
// Nấc chuyển tiếp: Idle → Running
   S_Idle   DI_StartPB   M_AllPermissive              S_Running
 ────┤ ├───────┤ ├───────────┤ ├────────────────┬────────( S )──
                                                │
                                                └────────( R )──  S_Idle

// Nấc giám sát bất biến — luôn có, không bao giờ bỏ
   [ĐẾM số bit trạng thái đang bật] → M_StateCount
   M_StateCount <> 1  ────────────────────────────────( M_AnyFault )
```

### Chọn cách nào

| | Biến + `CASE` | Bit trạng thái |
|---|---|---|
| Bất biến "một trạng thái" | **Được bảo đảm bởi kiểu dữ liệu** | Phải tự cưỡng chế + giám sát |
| Đọc trạng thái khi gỡ lỗi | Xem một biến | Xem bảy bit |
| Đội bảo trì đọc ladder | Không đọc được | **Đọc được** |
| Thêm trạng thái | Thêm một giá trị | Thêm một bit + sửa nấc giám sát |

Tiêu chí quyết định **không phải kỹ thuật mà là tổ chức**: ai sẽ sửa cỗ máy này lúc hai giờ sáng khi
bạn không có mặt? Viết cho người đó đọc.

---

## 25.6 Trạng thái máy tổng và trạng thái từng trạm

DP-01 có **hai trạm**. Câu hỏi tự nhiên: một máy trạng thái hay ba?

Câu trả lời: **ba** — một cho máy tổng, một cho mỗi trạm — xếp thành hai tầng.

```text
              ┌─────────────────────────────┐
              │   MachineState  (máy tổng)  │
              │   Idle / Running / Alarm …  │
              └──────────────┬──────────────┘
                             │  cho phép / cấm
              ┌──────────────┴──────────────┐
              ▼                             ▼
     ┌──────────────────┐          ┌──────────────────┐
     │  Stn1State       │          │  Stn2State       │
     │  (trạm tra keo)  │          │  (trạm sấy UV)   │
     │  Rỗng/Đang làm/  │          │  Rỗng/Đang làm/  │
     │  Chờ nhả         │          │  Chờ nhả         │
     └──────────────────┘          └──────────────────┘
```

Phân chia trách nhiệm rất rõ:

- **Máy tổng** quản lý những gì áp cho *cả cỗ máy*: đã về gốc chưa, có lỗi không, người vận hành đang
  cho phép chạy không. Nó **cho phép hoặc cấm**, không điều khiển chi tiết.
- **Trạm** quản lý *sản phẩm đang nằm ở trạm đó*: đã kẹp chưa, đã làm xong chưa, đã nhả chưa. Trạm
  chỉ chạy khi máy tổng cho phép.

Nhờ tách tầng, hai trạm **chạy song song trên hai board khác nhau** mà không giẫm chân nhau — ràng
buộc duy nhất giữa chúng là chỗ trống. Cách tổ chức tầng và cách hai trạm bắt tay là nội dung của
**Chương 27**.

> 💡 **MẸO**
> Ranh giới đúng: máy tổng **không được** biết trạm 1 đang ở bước nào. Nếu bạn thấy máy tổng phải đọc
> `Stn1Step = 4` để ra quyết định, nghĩa là trách nhiệm đã bị đặt sai tầng.

---

## 25.7 Bẫy thường gặp

### 🔍 BẪY 1 — Quên hành động khi vào trạng thái

Chuyển trạng thái được viết đúng, nhưng **quên làm gì đó khi vào trạng thái mới**. Ví dụ kinh điển:
chuyển sang `Alarm` mà quên tắt `M_CycleEnable`.

Kết quả: máy hiển thị đang lỗi, đèn đỏ sáng, còi kêu — mà **chu trình vẫn chạy tiếp**. Người vận hành
nhìn thấy hai thông tin mâu thuẫn và không biết tin cái nào.

**Cách phòng:** cột "hành động khi vào trạng thái" trong bảng chuyển trạng thái là **cột bắt buộc**.
Bảng nào để trống cột đó thì coi như chưa điền xong.

### 🔍 BẪY 2 — Trạng thái vào được nhưng không ra được

Bạn định nghĩa `Alarm`, viết điều kiện vào rất kỹ, rồi để điều kiện ra là `DI_ResetPB`. Nhưng nếu
nguyên nhân lỗi **vẫn còn**, nhấn Reset sẽ chuyển sang `Resetting` rồi lập tức quay lại `Alarm`. Máy
nhấp nháy giữa hai trạng thái mỗi vòng quét, đèn chớp loạn, và không ai hiểu chuyện gì.

Ngược lại cũng có: điều kiện ra chặt tới mức không bao giờ thoả. Máy kẹt vĩnh viễn, phải tắt nguồn.

**Cách phòng — hai việc, làm cả hai:**

1. Với **mỗi** trạng thái, tự hỏi: *"làm cách nào ra khỏi đây? Nếu điều kiện đó không bao giờ tới thì
   sao?"* Mọi trạng thái phải có ít nhất một đường ra khả thi.
2. Với trạng thái xử lý (`Homing`, `Resetting`), đặt **timeout** — quá thời gian thì sang `Alarm` với
   mã lỗi nói rõ kẹt ở đâu. Trạng thái không có đường thoát là trạng thái chưa thiết kế xong.

### 🔍 BẪY 3 — Nhồi trình tự vào máy trạng thái

Người mới hay tưởng mỗi *bước* của chu trình là một *trạng thái*, rồi tạo ra máy trạng thái ba mươi
trạng thái: `KepBoard`, `HaTrucZ`, `TraKeo`, `NangTrucZ`, `NhaKep`…

Đó là nhầm hai khái niệm khác nhau:

| | Trạng thái máy | Bước trình tự |
|---|---|---|
| Trả lời câu hỏi | Máy đang ở **chế độ** nào? | Chu trình đang làm **việc gì**? |
| Ai quan tâm | Người vận hành, đèn tháp, phân quyền | Chương trình, khi chạy tự động |
| Số lượng điển hình | 5–7 | 10–40 |
| Đổi khi nào | Người vận hành thao tác, hoặc có lỗi | Cơ cấu báo xong việc |

Cách đúng: **trạng thái `Running` chứa một trình tự bên trong nó**. Máy trạng thái quản lý chế độ;
trình tự bên trong quản lý các bước. Chương 26 xây phần trình tự đó.

### 🔍 BẪY 4 — Cho phép chuyển tiếp không có trong bảng

Bảng chuyển trạng thái liệt kê những chuyển tiếp **hợp lệ**. Nhưng nếu code cho phép gán
`MachineState := Idle` từ bất cứ đâu, thì bảng chỉ là tài liệu — không phải ràng buộc.

Nguy hiểm cụ thể: một đoạn code phụ nào đó đặt `MachineState := Idle` khi đang `Alarm`, và **lỗi biến
mất mà nguyên nhân còn nguyên**.

**Cách phòng:** chỉ gán `MachineState` **bên trong khối `CASE`** (hoặc trong các nấc chuyển tiếp đã
định danh). Dùng tham chiếu chéo *(cross-reference)* để soát: mọi chỗ ghi vào `MachineState` phải khớp
đúng một dòng trong bảng. Đây là ứng dụng trực tiếp của quy tắc "mỗi biến chỉ được ghi ở nơi đã định"
ở Chương 10.

### 🔍 BẪY 5 — Trạng thái không phản ánh ra ngoài

Máy trạng thái chạy đúng, nhưng người vận hành **không nhìn thấy nó**. Đèn tháp bật theo một logic
riêng, màn hình hiển thị theo logic khác.

Kết quả: máy ở `Hold` mà đèn xanh vẫn sáng. Người vận hành tưởng máy đang chạy, đứng chờ, mười phút
sau mới phát hiện.

**Cách phòng:** đèn tháp và dòng trạng thái trên màn hình phải **suy ra trực tiếp từ biến trạng thái**,
không tính lại từ điều kiện khác:

```iecst
DO_LampGreen  := (MachineState = Running);
DO_LampYellow := (MachineState = Idle) OR (MachineState = Hold)
                 OR (MachineState = Homing) OR (MachineState = Uninitialized);
DO_LampRed    := (MachineState = Alarm);
```

Ba dòng, không điều kiện phụ. Đèn **không thể** nói khác biến trạng thái.

---

## 25.8 Khác biệt giữa các hãng

Khái niệm máy trạng thái **không phụ thuộc hãng** — nó là cách tổ chức tư duy, không phải tính năng
của phần mềm. Nhưng công cụ hỗ trợ thì khác nhau, và khác đủ để ảnh hưởng tới cách bạn hiện thực.

| Khía cạnh | Siemens | Mitsubishi | Rockwell | CODESYS / TwinCAT |
|---|---|---|---|---|
| **Kiểu liệt kê** *(enumeration)* | Có, khai báo trong SCL | Hạn chế hơn — thường dùng hằng số có tên | Không có kiểu liệt kê thật; dùng hằng số có tên | Có `TYPE` liệt kê đầy đủ |
| **Lệnh `CASE`** | Có trong SCL | Có trong ST của GX Works3 | Có trong routine ST | Có |
| **Ngôn ngữ SFC sẵn có** | **S7-GRAPH** | **SFC / MELSAP3** | Routine kiểu **SFC** | SFC theo chuẩn |
| **Xem trạng thái trực tuyến** | Hiện tên nếu dùng kiểu liệt kê | Thường hiện số | Hiện giá trị tag | Hiện tên nếu dùng kiểu liệt kê |

> 💡 **Hệ không có kiểu liệt kê thì làm gì?**
> Dùng **hằng số có tên**, và tuyệt đối không viết số trần trong code: `STATE_IDLE := 10`,
> `STATE_HOMING := 20`. Bạn mất khả năng hiện tên khi giám sát trực tuyến, nên bù lại bằng cách
> **hiển thị tên trạng thái trên màn hình vận hành** (Chương 44) — người vận hành và người bảo trì
> cần cái tên đó hơn bạn nhiều.

> ⚠ **Về SFC — cả ba hãng lớn đều có, nhưng nó không phải câu trả lời cho chương này.**
> SFC diễn đạt **trình tự** rất tốt (Chương 26). Nó diễn đạt **chế độ máy** kém, vì máy trạng thái ở
> chương này cần đường "từ **mọi** trạng thái đều nhảy được vào `Alarm`" — thứ mà SFC phải vẽ rất
> rườm rà. Cách thường gặp trong thực tế, và cũng là khuyến nghị của sách: **chế độ máy dùng `CASE`;
> trình tự bên trong chế độ `Running` thì dùng SFC hoặc `CASE`.**
>
> Thêm một lý do thực dụng: S7-GRAPH và các gói SFC tương đương ở hãng khác **thường nằm trong gói
> bản quyền riêng hoặc ấn bản phần mềm cao hơn**. Kiểm trước khi thiết kế dựa vào nó (Chương 13).

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

## 25.9 Bảng chốt — dùng khi thiết kế máy mới

| Bước | Việc phải làm | Xong khi |
|---|---|---|
| 1 | Liệt kê **tập trạng thái** | Có 5–7 trạng thái, mỗi cái đặt tên bằng một từ người vận hành hiểu |
| 2 | Vẽ **sơ đồ chuyển tiếp** | Mọi trạng thái có ít nhất một đường vào và một đường ra |
| 3 | Điền **bảng chuyển trạng thái** đủ 4 cột | Không dòng nào để trống cột "hành động khi vào" |
| 4 | Thêm dòng **"mọi trạng thái → Alarm"** | Đã liệt kê hết các nguồn lỗi |
| 5 | Đặt **timeout** cho mọi trạng thái xử lý | `Homing`, `Resetting` đều có |
| 6 | Chọn cách hiện thực | Theo tiêu chí *ai sẽ bảo trì*, không theo sở thích |
| 7 | Nối **đèn tháp và màn hình** thẳng vào biến trạng thái | Không có logic đèn riêng |
| 8 | Soát **mọi chỗ ghi vào biến trạng thái** | Khớp đúng số dòng của bảng |

---

## 25.10 Tự kiểm

1. Giải thích cho một đồng nghiệp: vì sao bốn cờ độc lập **chắc chắn** sẽ dẫn tới trạng thái vô nghĩa,
   còn một biến trạng thái thì không? Trả lời bằng **con số**, không bằng cảm tính.
2. Vẽ lại **bảy trạng thái và các chuyển tiếp** không nhìn sách.
3. Vì sao `Resetting` đi tới `Homing` chứ **không** về thẳng `Idle`? Hậu quả nếu cắt ngắn là gì?
4. Vì sao **mọi** trạng thái đều phải có đường vào `Alarm`? Cho một ví dụ lỗi phát sinh ngoài `Running`.
5. Phân biệt **trạng thái máy** với **bước trình tự** — cho một ví dụ của mỗi loại trên DP-01.
6. Bạn phải viết bằng ladder vì đội bảo trì chỉ đọc được ladder. **Hai việc bắt buộc** để cách bit
   trạng thái không quay lại đúng vấn đề của cờ rải rác là gì?
7. Máy đang `Hold` mà đèn xanh vẫn sáng. Nguyên nhân gốc nằm ở đâu, và sửa thế nào cho lỗi này **không
   thể** tái diễn?

Câu 1 và câu 3 là hai câu phân loại. Câu 1 kiểm tra bạn hiểu *vì sao* chứ không chỉ *làm thế nào*; câu
3 kiểm tra bạn có phản xạ về an toàn khi khởi động lại — thứ Chương 28 sẽ khai triển.

---

### Chương tiếp theo

**Chương 26 — Thiết kế theo lưu đồ & bit trình tự.** Chương này dựng khung *chế độ* của máy. Bên trong
trạng thái `Running` còn một chu trình gồm hàng chục bước — Chương 26 xây phần đó, kèm cách xử lý nhánh
song song và cách phát hiện bế tắc bằng timeout từng bước.

---

### Nguồn tham khảo chương 25

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: lệnh `CASE`, kiểu liệt kê,
  và ngôn ngữ SFC. *(tiêu chuẩn có bản quyền; chương này chỉ diễn giải ở mức khái niệm)*
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: phân biệt các loại lệnh dừng
  và yêu cầu về khởi động lại có chủ ý — cơ sở cho quyết định `Resetting → Homing` ở mục 25.3.
- Đặc tả trình tự và danh sách chức năng an toàn của DP-01 — Phụ lục J.

> ⚡ Bảy trạng thái ở mục 25.3 là **mô hình thực dụng đã được rút gọn cho máy tự động hoá rời rạc**,
> không phải một mô hình chuẩn hoá bắt buộc. Máy của bạn có thể cần bớt hoặc thêm — điều bắt buộc là
> *một biến, một trạng thái*, không phải con số bảy.
