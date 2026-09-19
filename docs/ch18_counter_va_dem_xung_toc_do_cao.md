# Chương 18 — Counter & đếm xung tốc độ cao

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 18.1 Bài toán: con số đúng, nhưng đúng chuyện khác

Cuối ca, màn hình DP-01 báo **1 240 board**. Phiếu kiểm kho đếm được **1 187**.

Chênh 53 board. Không ai tìm ra 53 board đó ở đâu, và cũng không ai chứng minh được chúng chưa từng
tồn tại. Sản lượng là số liệu đi vào báo cáo, vào lương khoán, vào kế hoạch vật tư — nên chênh lệch
không giải thích được là chuyện lớn hơn nó có vẻ.

Nguyên nhân, tìm ra sau hai ngày: bộ đếm gắn vào cảm biến đầu chuyền vào. Board đi qua nhanh, nhưng
thỉnh thoảng một board bị đẩy lùi nhẹ khi board sau chạm vào, rồi tiến lên lại. Cảm biến thấy: có —
không — có. Bộ đếm ghi **hai** board.

Không có board nào biến mất. Có 53 lần một board được đếm hai lần.

Chương này về ba việc: đếm cho đúng, biết khi nào PLC **không đếm nổi**, và biết con số của mình
thật ra đang đo cái gì.

---

## 18.2 Ba khối đếm chuẩn

Chuẩn IEC 61131-3 định nghĩa ba khối bộ đếm *(counter)*. Mọi hệ đều có cả ba.

| Khối | Tên đầy đủ | Làm gì |
|---|---|---|
| **CTU** | *Count Up* — đếm lên | Mỗi cạnh lên ở `CU`, giá trị `CV` tăng 1. `Q` lên khi `CV >= PV` |
| **CTD** | *Count Down* — đếm xuống | Mỗi cạnh lên ở `CD`, `CV` giảm 1. `Q` lên khi `CV <= 0` |
| **CTUD** | *Count Up/Down* — đếm hai chiều | Có cả hai ngõ vào; dùng khi cần biết **số lượng đang có**, không phải tổng đã qua |

Các chân dùng chung:

| Chân | Nghĩa |
|---|---|
| `CU` / `CD` | Ngõ vào đếm — **kích theo cạnh lên** |
| `R` (CTU) / `LD` (CTD) | Đặt lại về 0 / nạp giá trị đặt |
| `PV` | **Giá trị đặt** *(preset value)* — mốc để `Q` lên |
| `CV` | **Giá trị hiện tại** *(current value)* — con số đang đếm |
| `Q` | Ngõ ra, lên khi đã tới mốc |

```iecst
VAR
    C_Board : CTU;
END_VAR

// Đếm board vào trạm 1; đủ 50 thì báo đầy khay
C_Board(CU := DI_BoardStn1,
        R  := DI_ResetPB,
        PV := 50);

M_TrayFull  := C_Board.Q;
BoardInTray := C_Board.CV;
```

> ⚡ **LƯU Ý — khối đếm chuẩn đã tự bắt cạnh**
> Chân `CU` kích theo **cạnh lên**, nên khối `CTU` không đếm 400 lần khi board nằm im trước cảm biến.
> Đây là khác biệt so với việc tự viết `Count := Count + 1` như ở Chương 16, mục 16.5 — chỗ đó bạn
> **phải** tự thêm `R_TRIG`.
>
> Đừng suy ra rằng vấn đề đã hết. Khối đếm bắt được cạnh, nhưng **cạnh giả thì nó vẫn đếm** — đó là
> đúng cỗ máy ở mục 18.1, và là nội dung mục 18.4.

### ⭐ Cùng khối đếm đó, viết bằng ladder

```text
                      ┌──────────────────┐
                      │  C_Board     CTU │
   DI_BoardStn1       │                  │          M_TrayFull
 ────┤ ├──────────────┤ CU             Q ├──────────( )───
   DI_ResetPB         │                  │
 ────┤ ├──────────────┤ R             CV ├──────────► BoardInTray
                   50─┤ PV               │
                      └──────────────────┘
```

> ⭐⭐ **Chân `CV` nối ra một thanh ghi là thứ nên làm ngay từ đầu.** ⚡ Nó cho người vận hành thấy
> **con số đang đếm tới đâu** mà không cần mở phần mềm lập trình — và cho người chẩn đoán biết bộ
> đếm có nhích hay không.
>
> ⚠ Nhắc lại cảnh báo ở trên, vì ở ladder nó **dễ quên hơn**: chân `CU` đã tự bắt cạnh, nhưng
> ⭐ **cạnh giả thì nó vẫn đếm** — mục 18.4.

> ⚠⚠ **Và một bẫy chỉ có ở ladder:** ⭐ **cực tính chân `R` khác nhau giữa các hãng** (mục 18.6b).
> Ở ST bạn viết rõ `R := DI_ResetPB`; ở ladder, một số hệ đặt lại khi nấc **thông**, số khác khi nấc
> **hở**. ⚠ Nối nhầm thì bộ đếm **bị xoá mỗi vòng quét** và luôn đọc bằng 0 — hoặc **không bao giờ
> xoá được**.

### CTUD — khi con số cần giảm

CTU trả lời *"đã có bao nhiêu board đi qua?"*. Nhiều bài toán lại cần *"đang có bao nhiêu board trong
máy?"* — con số này phải giảm khi board đi ra.

```iecst
VAR
    C_InMachine : CTUD;
    TrigIn      : R_TRIG;
    TrigOut     : R_TRIG;
END_VAR

TrigIn(CLK  := DI_BoardInfeed);
TrigOut(CLK := DI_BoardOutfeed);

C_InMachine(CU := TrigIn.Q,        // board vào  → +1
            CD := TrigOut.Q,       // board ra   → −1
            R  := M_MachineEmpty,  // xác nhận máy rỗng → về 0
            PV := 2);              // DP-01 chứa tối đa 2 board

M_MachineFull := C_InMachine.CV >= 2;
```

Con số này dùng được ngay cho hai việc thật: chặn không cho board thứ ba vào, và biết khi nào máy đã
**xả hết** *(drained)* để được phép đổi mã hàng hoặc dừng cuối ca.

> 🔍 **BẪY — bộ đếm hai chiều trôi dần**
> `CV` của CTUD là kết quả **tích luỹ của mọi lần cộng và trừ** từ lần đặt lại gần nhất. Chỉ cần một
> lần đếm sót hoặc đếm thừa, sai số đó **ở lại vĩnh viễn** và mọi con số sau đều lệch.
>
> Vì vậy CTUD phải có **điểm đồng bộ về sự thật**: khi máy chắc chắn rỗng (không cảm biến nào thấy
> board, chuyền đã chạy đủ lâu), ép `CV` về 0 thay vì tin vào phép cộng trừ. Không có điểm đồng bộ,
> sau vài ca con số sẽ vô nghĩa.

---

## 18.3 Đếm cạnh, không đếm mức — và đếm cạnh nào

Chương 16 đã nói vì sao phải đếm cạnh. Ở đây thêm một câu hỏi mà chương trước chỉ nêu ra: **cạnh
nào?**

| Đếm ở | Con số nghĩa là | Dùng cho |
|---|---|---|
| **Cạnh lên** của cảm biến vào | Số board **đã vào** máy | Kiểm soát dòng vào, chặn quá tải |
| **Cạnh xuống** của cảm biến trạm | Số board **đã làm xong** ở trạm đó | Sản lượng, tính chu kỳ |
| **Cạnh lên** của cảm biến ra | Số board **đã rời** máy | Đối chiếu với máy sau (Chương 41) |

Ba con số này khác nhau, và hiệu số giữa chúng chính là số board đang nằm trong máy. Đó không phải
sai số — đó là thông tin.

> ⚠ **Con số báo cáo ra ngoài phải là số board ĐÃ LÀM XONG.**
> Đếm ở đầu vào cho con số **lớn hơn thực tế**: nó tính cả những board đang dở dang và những board sẽ
> bị loại. Đây là nguồn gốc phổ biến nhất của chênh lệch giữa số máy báo và số kho đếm — và nó luôn
> lệch về phía có lợi cho người vận hành, nên rất lâu mới bị phát hiện.

Trên DP-01, sản lượng đúng phải đếm ở nơi board rời trạm 2, và phải tách OK với NG:

```iecst
VAR
    TrigDone : F_TRIG;
END_VAR

TrigDone(CLK := DI_BoardStn2);        // cạnh xuống = board rời trạm UV

IF TrigDone.Q THEN
    IF M_Board2IsNG THEN
        NgCount := NgCount + 1;
    ELSE
        OkCount := OkCount + 1;
    END_IF;
END_IF;

TotalOut := OkCount + NgCount;        // luôn khớp với số board rời máy
```

---

## 18.4 Đếm trùng — bốn nguyên nhân và cách chặn

Cỗ máy ở mục 18.1 đếm trùng vì board bị đẩy lùi rồi tiến lên. Đó chỉ là một trong bốn nguyên nhân,
và cả bốn đều tạo ra **cạnh thật** mà khối đếm không có cách nào phân biệt với cạnh mong muốn.

| Nguyên nhân | Hiện tượng | Cách chặn |
|---|---|---|
| **Sản phẩm rung / lùi lại** | Đếm thừa, số lẻ tẻ | Khoảng chết theo thời gian (bên dưới) |
| **Cảm biến nhiễu** | Đếm thừa ngẫu nhiên, cả khi không có sản phẩm | Lọc rung bằng `TON`; kiểm nối đất, đi dây tách khỏi cáp động lực (Chương 51) |
| **Sản phẩm trong suốt / bề mặt lỗ** | Một sản phẩm cho nhiều cạnh khi đi qua | Đổi loại cảm biến; hoặc chốt trạng thái bằng cơ cấu chặn |
| **Rung tiếp điểm** (nếu đếm từ nút bấm hoặc tiếp điểm cơ khí) | Một lần tác động ra nhiều cạnh | Lọc rung **trước** khi đưa vào chân đếm (Chương 17, mục 17.4) |

### Khoảng chết — cách chặn thông dụng nhất

Ý tưởng: sau khi đếm một lần, **không nhận cạnh mới** trong một khoảng thời gian ngắn hơn khoảng cách
tối thiểu giữa hai sản phẩm thật.

```iecst
VAR
    T_Deb    : TON;
    TrigCnt  : R_TRIG;
    C_Board  : CTU;
END_VAR

// Tín hiệu phải ổn định 30 ms mới được coi là thật
T_Deb(IN := DI_BoardStn1, PT := T#30MS);

TrigCnt(CLK := T_Deb.Q);              // bắt cạnh trên tín hiệu ĐÃ LỌC
C_Board(CU := TrigCnt.Q, R := DI_ResetPB, PV := 9999);
```

Chọn thời gian lọc theo nguyên tắc:

> **Lớn hơn nhiều lần chu kỳ quét · lớn hơn thời gian rung dự kiến · nhỏ hơn nhiều lần khoảng cách
> thật giữa hai sản phẩm.**

Trên DP-01, board cách nhau ít nhất khoảng 2 giây, chu kỳ quét khoảng 10 ms. Cửa sổ chọn rất rộng —
30 ms nằm thoải mái ở giữa. Khi cửa sổ đó **hẹp** hoặc **không tồn tại** (sản phẩm đi rất nhanh, sát
nhau), thì lọc thời gian không còn là công cụ đúng: cần đổi cảm biến, đổi cơ cấu, hoặc chuyển sang
bộ đếm phần cứng ở mục 18.5.

> 💡 **MẸO — chẩn đoán bằng chính bộ đếm**
> Nghi đếm trùng thì thêm một bộ đếm thứ hai trên tín hiệu **chưa lọc**, và hiển thị cả hai. Hiệu số
> giữa hai con số chính là số cạnh giả — bạn đo được vấn đề thay vì đoán, và biết được việc lọc có
> thật sự cần thiết không.

---

## 18.5 Khi nào PLC không đếm nổi — bộ đếm tốc độ cao

### Giới hạn nằm ở đâu

Bộ đếm chuẩn được cập nhật **mỗi lần khối được gọi**, tức một lần mỗi vòng quét (Chương 10). Hệ quả
trực tiếp và không thể vòng tránh:

> **Xung nào lên rồi xuống trọn vẹn trong khoảng giữa hai lần quét thì PLC không hề thấy nó.**

Ngoài ra ngõ vào số còn có **thời gian lọc phần cứng** riêng — thường vài trăm micro-giây tới vài
mili-giây — được thiết kế để chống nhiễu, và nó chặn luôn cả xung nhanh thật (Chương 9).

### Công thức quyết định

Gọi `f` là tần số xung cần đếm, `Tq` là chu kỳ quét.

| Điều kiện | Kết luận |
|---|---|
| `f < 1 / (10 × Tq)` | ✅ Bộ đếm phần mềm dùng được, biên an toàn tốt |
| `1/(10×Tq) ≤ f < 1/(2×Tq)` | ⚠ Vùng xám — đếm được về lý thuyết nhưng **sót khi quét dài ra**. Không dùng cho số liệu quan trọng |
| `f ≥ 1 / (2 × Tq)` | ❌ **Bắt buộc dùng bộ đếm tốc độ cao phần cứng (HSC)** |

Hệ số 10 không phải con số thiêng — nó là biên dự phòng cho việc **chu kỳ quét không cố định**. Quét
dài ra khi có thêm nhánh logic chạy, khi truyền thông bận, khi ai đó thêm chức năng vào tháng sau.
Một thiết kế nằm sát ranh giới hôm nay sẽ hỏng sau một lần cập nhật chương trình — và hỏng theo kiểu
tệ nhất: **âm thầm đếm thiếu**.

Ví dụ với `Tq = 10 ms`:

| Nguồn xung | Tần số | Kết luận |
|---|---|---|
| Board qua cảm biến trên DP-01 | ~0,5 Hz | ✅ Thoải mái |
| Nút bấm người nhấn | < 5 Hz | ✅ |
| Cảm biến đếm chai trên chuyền nhanh | 50 Hz | ⚠ Vùng xám — nên dùng HSC |
| **Encoder 1024 xung/vòng, 600 vòng/phút** | **10 240 Hz** | ❌ HSC bắt buộc |

### HSC là gì

**Bộ đếm tốc độ cao** *(high-speed counter, HSC)* là mạch đếm **nằm trong phần cứng**, chạy độc lập
với vòng quét. Nó đếm liên tục ở tần số hàng chục tới hàng trăm kHz; chương trình chỉ **đọc giá trị**
mỗi vòng quét, không tham gia vào việc đếm.

Ba điều cần biết trước khi dùng:

- **Chỉ một số ngõ vào cụ thể mới nối được với HSC.** Không phải kênh nào cũng dùng được — phải tra
  tài liệu và **quyết định lúc chọn phần cứng**, không phải lúc viết chương trình (Chương 8, Chương 13).
- **HSC phải được cấu hình, không chỉ gọi khối.** Chế độ đếm, hướng, giá trị so sánh, hành vi khi
  tràn — đặt trong phần cấu hình phần cứng.
- **Ngõ ra so sánh của HSC nhanh hơn vòng quét.** Nhiều HSC bật được một ngõ ra ngay khi giá trị đạt
  mốc, không chờ tới giai đoạn ghi ngõ ra. Đây là lý do người ta dùng HSC cả khi tần số không cao:
  cần **phản ứng nhanh và có thời gian trễ ổn định**, ví dụ cắt vật liệu theo chiều dài.

### Encoder — đếm để biết vị trí

**Bộ mã hoá vòng quay** *(rotary encoder)* biến chuyển động quay thành xung. Hai loại:

| Loại | Cho biết | Mất điện thì |
|---|---|---|
| **Gia số** *(incremental)* | Đã quay **bao nhiêu** kể từ mốc | ⚠ Mất vị trí — phải **về gốc** lại |
| **Tuyệt đối** *(absolute)* | Đang ở **vị trí nào** | Vẫn biết vị trí |

Encoder gia số thường có ba kênh: **A**, **B** lệch pha nhau một phần tư chu kỳ, và **Z** phát một
xung mỗi vòng. Lệch pha giữa A và B cho biết **chiều quay** — kênh nào đổi trước thì quay theo chiều
đó. Kênh Z dùng làm mốc để đồng bộ lại.

> ⚡ **LƯU Ý — "×4" và độ phân giải thật**
> HSC thường đếm được cả bốn cạnh trong một chu kỳ A/B *(quadrature ×4)*, nên độ phân giải thật gấp
> **bốn lần** số xung ghi trên nhãn encoder — và tần số vào HSC cũng gấp bốn. Encoder 1024 xung/vòng
> ở chế độ ×4 cho 4096 vị trí mỗi vòng. Nhầm hệ số này khi tính là sai gấp bốn ở mọi phép quy đổi
> sang đơn vị chiều dài.

> ⚠ **NGUY HIỂM — encoder không phải thiết bị an toàn**
> Vị trí đọc từ encoder thường **không được dùng làm căn cứ cho chức năng an toàn**. Encoder có thể
> trượt khớp nối, đứt cáp, hoặc mất xung mà giá trị đếm vẫn trông hợp lý. Giám sát vị trí an toàn cần
> thiết bị và kiến trúc chuyên dụng — Chương 47.

DP-01 dùng encoder ở lát cắt 3 (trục gantry, Chương 37). Ở lát cắt hiện tại, tất cả việc đếm đều nằm
thoải mái trong khả năng của bộ đếm phần mềm.

---

## 18.5b ⭐⭐ Encoder cầu phương — đếm được CHIỀU, và nhân được độ phân giải

Bộ đếm ở các mục trước chỉ đếm **số xung**. Với một trục quay hai chiều, đếm xung thôi là không đủ:
⚠ trục quay tới rồi quay lui vẫn **cộng dồn**, và con số nói dối.

### Hai kênh, lệch pha nhau

Encoder tương đối có **hai kênh** — thường gọi là **A** và **B** — bố trí **lệch pha 90°**:

```text
A  ▔▔▁▁▔▔▁▁▔▔▁▁        Quay thuan: A som pha hon B
B  ▁▔▔▁▁▔▔▁▁▔▔▁

A  ▔▔▁▁▔▔▁▁▔▔▁▁        Quay nghich: B som pha hon A
B  ▔▁▁▔▔▁▁▔▔▁▁▔
```

⭐ **Kênh nào "đi trước" cho biết chiều quay.** Bộ đếm dùng thông tin đó để quyết định **cộng hay
trừ** — nên trục quay tới rồi lui sẽ trở về đúng số cũ.

| Số kênh | Biết được gì |
|---|---|
| Một kênh | ⭐ Chỉ **số xung** — ⚠ dùng được khi trục **chỉ quay một chiều** |
| ⭐ **Hai kênh (A, B)** | Số xung **và chiều** |
| Ba kênh (thêm **Z**) | ⭐ Thêm **một xung mỗi vòng** — dùng làm mốc, xem dưới |

### ⭐ Kênh Z — mốc một xung mỗi vòng

Kênh **Z** *(index / marker)* phát **đúng một xung cho mỗi vòng quay**. Nó dùng để:

| Việc | Vì sao cần |
|---|---|
| ⭐ **Về gốc chính xác** | Công tắc gốc cho vị trí thô; ⭐ **xung Z cho vị trí lặp lại được** (Chương 28, 37) |
| Phát hiện mất xung | ⚠ Nếu số xung giữa hai lần Z **không đúng như thiết kế** thì đã bỏ sót xung |

⭐ Hàng thứ hai là một phép tự kiểm rất rẻ mà ít ai dùng: encoder 1000 xung/vòng thì giữa hai xung Z
**phải** đếm được đúng 1000 — lệch nghĩa là có vấn đề.

### ⚠⚠ Nhân độ phân giải — x1, x2, x4

Bộ đếm có thể đếm **một, hai hoặc bốn cạnh** trong mỗi chu kỳ của cặp A/B:

| Chế độ | Đếm cạnh nào | Độ phân giải với encoder 1000 xung/vòng |
|---|---|---|
| **x1** | Một cạnh của A | 1 000 đếm/vòng |
| **x2** | Cả hai cạnh của A | 2 000 đếm/vòng |
| ⭐ **x4** | Cả hai cạnh của **cả A và B** | ⭐ **4 000 đếm/vòng** |

> ⚠⚠ **Đây là nguồn của một lỗi rất hay gặp: mọi phép quy đổi sai đúng 4 lần.**
>
> Bạn tính hệ số quy đổi từ **1000 xung/vòng** ghi trên nhãn encoder, nhưng module đang đặt **x4** —
> nên mọi khoảng cách, tốc độ, vị trí đều **sai bốn lần**. ⭐ Triệu chứng rất đặc trưng: **con số sai
> theo một tỉ lệ tròn trịa** (4, hoặc 2), không phải sai lung tung.
>
> ⭐ **Cách kiểm nhanh nhất:** quay trục **đúng một vòng bằng tay** và xem bộ đếm tăng bao nhiêu. Con
> số đó là độ phân giải **thực tế** — dùng nó để quy đổi, đừng dùng con số trên nhãn.
>
> ⚡ Đây cũng là ứng dụng thứ hai của kênh Z: quay tới khi thấy xung Z tiếp theo là **đúng một vòng**.

*(Đối chiếu: Hugh Jack — *Automating Manufacturing Systems with PLCs*, mục encoder tương đối và sơ đồ
cầu phương hai kênh; tài liệu bộ đếm tốc độ cao của các hãng cho chế độ x1/x2/x4.)*

---

## 18.6 Giữ giá trị qua mất điện

Sản lượng ca là **sự thật đã xảy ra** — mất là mất số liệu thật, không dựng lại được. Theo quy tắc ở
Chương 16 mục 16.4, nó thuộc nhóm **phải giữ**.

Ba điều cần lưu ý:

- **Bộ đếm là khối chức năng, và bộ nhớ của nó nằm ở thể hiện.** Muốn giữ được thì phải khai báo
  **thể hiện của khối** là giữ được, chứ không chỉ giữ biến sao chép giá trị ra. Cách khai báo khác
  nhau giữa các hệ (mục 18.7) — đây là chỗ hay sai khi chuyển chương trình.
- **Xoá bộ đếm phải là hành động có chủ ý và có ghi lại.** Nút "xoá sản lượng" không được đặt cạnh
  nút Reset lỗi, và nên yêu cầu xác nhận. Xoá nhầm sản lượng giữa ca không khôi phục được.
- ⚠ **Đừng chỉ dựa vào vùng nhớ giữ được cho số liệu quan trọng.** Nó phụ thuộc pin hoặc siêu tụ; pin
  hết mà không ai để ý thì số liệu âm thầm biến mất (Chương 51). Số liệu sản xuất nên được ghi ra nơi
  khác định kỳ — và khi có kết nối lên hệ thống trên thì đó mới là bản ghi chính thức (Chương 42).

Ngoài ra cần một quy ước rõ ràng cho **thời điểm đặt lại**:

| Bộ đếm | Đặt lại khi nào |
|---|---|
| Sản lượng ca | Đầu ca, do người vận hành, có xác nhận |
| Sản lượng theo mã hàng | Khi đổi mã hàng (Chương 29) |
| Tổng số chu trình của cơ cấu | **Không bao giờ** — dùng cho lịch bảo trì, cần giá trị tích luỹ trọn đời |

---

## 18.6b ⚠⚠ Bộ đếm thường ĐÃ giữ sẵn — và đó mới là chỗ nguy hiểm

Mục trên nói về việc **làm cho** bộ đếm giữ được. ⚠ Nhưng ở nhiều hệ, câu hỏi đúng lại ngược lại:
⭐ **bộ đếm mặc định đã giữ rồi, và bạn phải chủ động xoá thứ không được phép giữ.**

| Điều | Nội dung |
|---|---|
| ⭐ Mặc định phổ biến | **Bộ đếm giữ giá trị qua mất điện** — giá trị lúc CPU tắt được khôi phục khi có điện lại |
| ⚠⚠ Hệ quả | Bộ đếm **điều khiển logic** sẽ khởi động lại với giá trị cũ |
| ⭐ Ngoại lệ đáng biết | ⚠ Nếu **điều kiện đặt lại đang đúng vào lúc có điện trở lại**, bộ đếm bị xoá — số liệu bạn tưởng còn thì không còn |

> ⚠⚠ **Đây là cùng một bẫy với biến giữ được ở Chương 16, mục 16.4 — chỉ khác là nó đến "miễn phí".**
>
> Với bộ đếm **sản lượng**, giữ được là điều bạn muốn. Với bộ đếm **điều khiển logic** — đếm số board
> trong một mẻ, đếm bước, đếm số lần thử lại — thì ⚠⚠ **giữ được là một lỗi an toàn**: máy có điện
> trở lại và tin rằng nó đang ở giữa mẻ thứ bảy, trong khi băng tải đã bị dọn sạch.
>
> ⭐ **Quy tắc:** với mỗi bộ đếm, trả lời dứt khoát câu hỏi ⭐ *"nếu mất điện ngay bây giờ rồi có điện
> lại, giá trị này CÒN thì đúng hay SAI?"* — rồi cấu hình theo câu trả lời, ⚠ **đừng để mặc định trả
> lời hộ**.

> ⚡ **Và đừng dựa vào việc đặt lại lúc khởi động để "chữa".** Nếu bạn định xoá bộ đếm bằng một điều
> kiện chạy lúc có điện, hãy nhớ ⚠ thứ tự thực thi lúc khởi động không phải lúc nào cũng như bạn
> tưởng — hãy **thử thật**: cho đếm tới một giá trị, cắt nguồn, cấp lại, và **xem giá trị**.

### ⚠ Cực tính chân đặt lại khác nhau giữa các hãng

⭐ Một khác biệt nhỏ nhưng đủ làm hỏng cả logic đặt lại khi chuyển chương trình:

| Hệ có thể | Yêu cầu để xoá bộ đếm |
|---|---|
| Nhóm một | Nấc / chân đặt lại phải ⭐ **ĐÚNG** *(true)* |
| Nhóm hai | Nấc / chân đặt lại phải ⭐ **SAI** *(false)* |

> ⚠ Nghĩa là cùng một đoạn logic đặt lại, chuyển sang hệ khác có thể thành ⚠⚠ **xoá bộ đếm liên tục**
> hoặc ⚠⚠ **không bao giờ xoá** — cả hai đều im lặng.
>
> ⭐ **Tra tài liệu của đúng hệ trước khi viết logic đặt lại**, và kiểm bằng cách cho đếm rồi kích
> điều kiện đặt lại trong lúc trực tuyến.

*(Đối chiếu: Petruzella, *Programmable Logic Controllers* — bộ đếm PLC **thường là giữ được**, giá trị
lúc dừng được khôi phục khi cấp nguồn lại, ⚠ trừ khi điều kiện đặt lại đang tác động lúc đó; và ⭐ cực
tính chân đặt lại **khác nhau giữa các hãng**, tài liệu khuyến cáo tra sổ tay trước khi lập trình.)*

---

## 18.7 Khác biệt giữa các hãng

| Khía cạnh | Siemens (S7-1200/1500) | Mitsubishi (FX5U / iQ-R) | Rockwell (Logix) | CODESYS / TwinCAT |
|---|---|---|---|---|
| Khối đếm | `CTU` `CTD` `CTUD` | Thiết bị `C` + lệnh `OUT`/`RST` | `CTU` `CTD` | `CTU` `CTD` `CTUD` |
| Giá trị hiện tại / đặt | `.CV` / `.PV` | Giá trị hiện tại và giá trị đặt của thiết bị `C` | `.ACC` / `.PRE` | `.CV` / `.PV` |
| ⚠ Đặt lại | Chân `R` | Lệnh `RST` | ⚠ **Bắt buộc lệnh `RES`** | Chân `R` |
| ⚠ Cực tính điều kiện đặt lại | ⭐ **Tra tài liệu** — có hệ cần ĐÚNG, có hệ cần SAI (mục 18.6b) | ⭐ Tra tài liệu | ⭐ Tra tài liệu | ⭐ Tra tài liệu |
| ⚠ Độ rộng số đếm | Chọn kiểu dữ liệu khi khai báo khối (`Int`, `DInt`…) | ⚠ **Theo dải số hiệu**: dải thấp là 16 bit, dải cao là 32 bit | `.ACC` là `DINT` 32 bit | Theo kiểu dữ liệu khai báo |
| Bộ đếm tốc độ cao | HSC tích hợp trên CPU, cấu hình trong phần cứng | ⚠ Thiết bị `C` chuyên dụng, **gắn cứng với ngõ vào cụ thể** | Module đếm chuyên dụng, hoặc ngõ vào tốc độ cao trên CPU nhỏ | Thiết bị đầu cuối EtherCAT chuyên dụng |

### ⚠ Ba chỗ dễ vấp nhất

**1. Mitsubishi — độ rộng và chức năng nằm ở SỐ HIỆU thiết bị.** Giống hệt vấn đề với timer ở Chương
17: bộ đếm `C` dải thấp là 16 bit, dải cao là 32 bit, và **dải cao nhất là bộ đếm tốc độ cao gắn cứng
với các ngõ vào nhất định trên CPU**. Nghĩa là chọn HSC nào thì **cũng là chọn luôn chân nào phải đấu
dây vào** — đây là quyết định đấu tủ, không phải quyết định lập trình. Tra bảng phân dải và bảng ánh
xạ chân **trước khi vẽ sơ đồ đấu**.

**2. Rockwell — `RES` và bẫy dùng chung.** Bộ đếm cần `RES` để về 0. Và ⚠ **một lệnh `RES` xoá cả
timer lẫn counter cùng tên tag** — dùng nhầm tag là xoá nhầm thứ.

**3. Số kênh HSC phụ thuộc dòng CPU, không phụ thuộc hãng.** Cùng một hãng, CPU nhỏ có thể có vài
kênh, CPU lớn hơn có nhiều kênh và tần số cao hơn. **Đây là con số phải tra theo đúng mã CPU** — và
phải tra **trước khi mua** (Chương 13, tiêu chí 3), vì không thêm được bằng phần mềm.

> ⚠ **Hành vi khi tràn khác nhau và ít khi được ghi rõ.** Có hệ dừng ở giá trị lớn nhất, có hệ quay
> vòng, có hệ đặt cờ lỗi. Đừng suy từ hệ này sang hệ khác — tra tài liệu, và nếu không tìm được câu
> trả lời dứt khoát thì **thử nghiệm**: đặt giá trị sát trần rồi cho đếm thêm, xem chuyện gì xảy ra.
> Mười phút thử nghiệm rẻ hơn một lỗi sản lượng âm sau ba tháng.

Chi tiết đối chiếu năm hệ: **Phụ lục A2**.

## 18.8 Bẫy thường gặp

### 🔍 BẪY 1 — Đếm ở đầu vào rồi gọi đó là sản lượng

**Hiện tượng:** số máy báo luôn lớn hơn số kho đếm, chênh lệch xấp xỉ số board đang trong máy cộng số
board bị loại.
**Cách sửa:** đếm ở nơi sản phẩm **rời máy đã hoàn tất**, và tách OK với NG (mục 18.3).

### 🔍 BẪY 2 — Bộ đếm tràn âm thầm

Bộ đếm 16 bit chạm 32 767 rồi quay vòng. Sản lượng đột nhiên là số âm hoặc về 0.

**Hiện tượng:** con số nhảy vô lý sau vài ngày chạy liên tục.
**Cách sửa:** dùng kiểu 32 bit cho bộ đếm tích luỹ; hoặc thiết kế đặt lại theo ca; và tra hành vi tràn
của đúng hệ đang dùng.

### 🔍 BẪY 3 — Đặt lại bộ đếm bằng chính điều kiện đang đếm

```iecst
// ✗ SAI — R đúng cùng lúc với CU
C_Board(CU := DI_BoardStn1,
        R  := DI_BoardStn1,      // vô nghĩa: vừa đếm vừa xoá
        PV := 50);
```

**Hiện tượng:** `CV` luôn bằng 0 hoặc 1 — ở hầu hết hệ, chân `R` có **ưu tiên cao hơn** chân đếm.
**Cách sửa:** điều kiện đặt lại phải độc lập với điều kiện đếm.

### 🔍 BẪY 4 — Dùng `Q` thay cho việc so sánh `CV`

`Q` lên khi `CV >= PV` và **giữ nguyên** cho tới khi đặt lại. Nếu bạn cần "cứ đủ 10 board thì làm một
việc", `Q` sẽ đúng liên tục từ board thứ 10 trở đi.

**Hiện tượng:** hành động lặp lại mãi thay vì xảy ra một lần mỗi 10 board.
**Cách sửa:** bắt cạnh lên của `Q`, và đặt lại bộ đếm ngay sau đó; hoặc so sánh `CV` với phép chia lấy
dư.

### 🔍 BẪY 5 — Lọc rung đặt sau khi bắt cạnh

```iecst
// ✗ SAI — bắt cạnh trên tín hiệu thô, lọc sau thì đã muộn
TrigCnt(CLK := DI_BoardStn1);
T_Deb(IN := TrigCnt.Q, PT := T#30MS);
```

`TrigCnt` đã sinh ra nhiều cạnh trước khi bộ lọc kịp làm gì. Tệ hơn: `TrigCnt.Q` chỉ đúng **một vòng
quét**, ngắn hơn 30 ms, nên `T_Deb.Q` **không bao giờ** lên.

**Hiện tượng:** hoặc vẫn đếm trùng, hoặc không đếm gì cả.
**Cách sửa:** lọc **trước**, bắt cạnh **sau** — như mục 18.4.

### 🔍 BẪY 6 — Tin bộ đếm hai chiều mà không có điểm đồng bộ

**Hiện tượng:** sau vài ca, "số board trong máy" là 3 trong khi máy rỗng, hoặc là −1.
**Cách sửa:** ép về 0 khi máy chắc chắn rỗng (mục 18.2).

### 🔍 BẪY 7 — Thiết kế sát ranh giới tần số

Tính ra `f` bằng khoảng một nửa `1/Tq`, thấy "vẫn đếm được" khi thử, nên để nguyên.

**Hiện tượng:** chạy tốt lúc nghiệm thu; vài tháng sau, sau một lần thêm chức năng, bắt đầu **đếm
thiếu** — không có báo lỗi nào.
**Cách sửa:** giữ biên 10 lần. Nằm trong vùng xám thì dùng HSC ngay từ đầu, vì đổi sau nghĩa là đổi
phần cứng.

### 🔍 BẪY 8 — Quên hệ số ×4 của encoder

**Hiện tượng:** mọi phép quy đổi từ xung sang chiều dài sai đúng **bốn lần** — hoặc gấp bốn, hoặc một
phần tư, tuỳ hướng nhầm.
**Cách sửa:** xác nhận chế độ đếm trong cấu hình HSC, rồi **đo kiểm bằng thực tế**: cho cơ cấu đi một
quãng đã biết, so số xung đếm được với tính toán. Chỉ hai phút và loại hẳn cả nhóm lỗi này.

---

## 18.9 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| ⭐⭐ Encoder hai kênh A/B cho biết gì | Số xung **và CHIỀU** — trục quay tới rồi lui trả về đúng số cũ |
| ⭐ Kênh Z dùng làm gì | **Một xung mỗi vòng** — về gốc chính xác, và **tự kiểm bỏ sót xung** |
| ⚠⚠ x1 / x2 / x4 | ⭐ Đặt sai làm **mọi phép quy đổi sai đúng 4 lần** — sai theo tỉ lệ tròn trịa |
| ⭐ Cách kiểm độ phân giải thật | **Quay đúng một vòng bằng tay**, xem bộ đếm tăng bao nhiêu |
| Đếm tổng đã qua | `CTU` |
| Đếm số đang có trong máy | `CTUD` + **điểm đồng bộ khi máy rỗng** |
| Con số nào là sản lượng thật | Đếm ở nơi sản phẩm **rời máy đã xong**, tách OK/NG |
| Đếm trùng | Lọc **trước**, bắt cạnh **sau**; kiểm nhiễu và cơ cấu |
| Có cần HSC không | `f < 1/(10×Tq)` → không cần · `f ≥ 1/(2×Tq)` → **bắt buộc** · ở giữa → nên dùng |
| Vì sao biên tới 10 lần | Chu kỳ quét **không cố định** và sẽ dài ra khi chương trình lớn lên |
| Sản lượng có giữ qua mất điện không | Có — khai báo **thể hiện của khối** là giữ được, và vẫn ghi ra nơi khác |
| ⚠⚠ Mặc định của bộ đếm ở nhiều hệ | ⭐ **ĐÃ giữ sẵn** — nguy hiểm với bộ đếm **điều khiển logic** |
| ⭐ Câu hỏi phải trả lời cho mọi bộ đếm | *"Mất điện rồi có lại — giá trị này CÒN thì đúng hay sai?"* |
| ⚠ Ngoại lệ khi có điện lại | Điều kiện đặt lại đang đúng lúc đó → ⭐ **bộ đếm bị xoá** |
| ⚠ Cực tính chân đặt lại | ⭐ **Khác nhau giữa các hãng** — có hệ cần ĐÚNG, có hệ cần SAI |
| Encoder gia số sau mất điện | Mất vị trí → **phải về gốc** (Chương 28) |
| Encoder dùng cho an toàn được không | **Không** — Chương 47 |

Bốn câu hỏi trước khi đặt một bộ đếm:

1. Con số này sẽ được ai đọc, và họ tưởng nó đo cái gì?
2. Một sản phẩm có thể tạo ra mấy cạnh ở tín hiệu này — trong trường hợp xấu nhất?
3. Tần số cao nhất là bao nhiêu, và chu kỳ quét dài nhất là bao nhiêu?
4. Ai được xoá con số này, và xoá nhầm thì dựng lại bằng cách nào?

---

## 18.10 Tự kiểm

1. Nêu ba chân của khối `CTU` và cho biết chân nào kích theo cạnh, chân nào theo mức.
2. Vì sao khối `CTU` chuẩn không đếm 400 lần khi board nằm im trước cảm biến, trong khi
   `Count := Count + 1` thì có?
3. ⭐ Máy báo 1 240 board, kho đếm 1 187. Nêu **hai** nguyên nhân khả dĩ khác nhau về bản chất, và
   cách phân biệt chúng.
4. Chu kỳ quét 12 ms. Tần số xung cao nhất mà bạn còn dám dùng bộ đếm phần mềm là bao nhiêu? Vì sao
   không lấy sát ngưỡng `1/(2×Tq)`?
5. Encoder 2500 xung/vòng, chế độ ×4, trục quay 300 vòng/phút. Tần số vào HSC là bao nhiêu?
6. ⭐ Vì sao bộ đếm hai chiều **bắt buộc** phải có điểm đồng bộ về sự thật? Điều gì xảy ra nếu không có?
7. Trong đoạn lọc rung, vì sao `TON` phải đặt **trước** `R_TRIG`? Chuyện gì xảy ra nếu đảo ngược?
8. Phân biệt encoder gia số với encoder tuyệt đối. Cái nào cần về gốc sau khi mất điện, vì sao?
9. Bộ đếm nào trên DP-01 **không bao giờ** được đặt lại? Vì sao?
10. ⭐ Vì sao encoder không được dùng làm căn cứ cho chức năng an toàn, dù giá trị nó đọc ra trông
    hoàn toàn hợp lý?
11. ⚠⚠ Bộ đếm ở nhiều hệ **mặc định đã giữ được**. Nêu một bộ đếm mà điều đó là **đúng ý muốn**, và
    một bộ đếm mà điều đó là **lỗi an toàn**. Câu hỏi nào giúp phân biệt hai loại?
12. ⭐ Bạn định xoá bộ đếm bằng một điều kiện chạy lúc khởi động. Nêu **hai** lý do không nên tin vào
    thiết kế đó mà không thử thật.

> Câu 3, 6 và 10 là ba câu phân loại. Câu 3 là tinh thần của cả chương: **một con số sai hiếm khi
> sai vì phép đếm — nó sai vì đang đếm nhầm thứ.**

⭐⭐ **Bổ sung.** Vì sao encoder một kênh không dùng được cho trục quay hai chiều? Hai kênh A/B xác
định chiều bằng cách nào?

⚠⚠ **Bổ sung.** Mọi phép quy đổi vị trí của bạn sai đúng **4 lần**. Nguyên nhân khả dĩ nhất là gì, và
phép kiểm nào xác nhận trong một phút?

---

### Chương tiếp theo

Chương 19 — **So sánh, toán học & xử lý dữ liệu**. Bạn đã có bit, cạnh, thời gian và số đếm. Chương
sau làm việc với **giá trị**: so sánh, tính toán, và những chỗ phép tính trong PLC hành xử khác với
điều bạn quen ở máy tính thường.

### Nguồn tham khảo chương 18

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: định nghĩa các khối đếm
  chuẩn `CTU` / `CTD` / `CTUD` và ý nghĩa từng chân. *(tiêu chuẩn có bản quyền)*
- IEC 61131-2 — *Programmable controllers, Part 2: Equipment requirements and tests*: đặc tính ngõ
  vào số, trong đó có thời gian lọc phần cứng — cơ sở cho giới hạn tần số ở mục 18.5.
- Tài liệu CPU và module của từng hệ trong Phụ lục A — dùng cho số kênh HSC, tần số tối đa, chế độ
  đếm, và hành vi khi tràn. Đây là các thông số **phải tra theo đúng dòng sản phẩm**, không suy đoán.
- Bảng I/O của DP-01 — Phụ lục J.
- **Petruzella, Frank D.** — *Programmable Logic Controllers* *(nội dung dẫn có ở **cả bản 6th ed. lẫn bản 2025**)* — ⭐ bộ đếm PLC **thường là giữ được**: giá trị lúc
  CPU dừng được khôi phục khi cấp nguồn lại, ⚠ trừ khi **điều kiện đặt lại đang tác động** lúc đó; và
  ⭐ **cực tính điều kiện đặt lại khác nhau giữa các hãng** — nền cho mục 18.6b.

> ⚡ Công thức chọn HSC ở mục 18.5 là **quy tắc thiết kế thực dụng**, không phải yêu cầu tiêu chuẩn.
> Hệ số 10 là biên dự phòng do chu kỳ quét biến động; đơn vị của bạn có thể chọn biên khác, nhưng phải
> chọn **có ý thức** và ghi lại lý do — không lấy sát ngưỡng lý thuyết.
