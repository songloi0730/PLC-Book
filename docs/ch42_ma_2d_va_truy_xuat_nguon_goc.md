# Chương 42 — Mã vạch, mã 2D & truy xuất nguồn gốc

> **Lát cắt máy mẫu:** 4 — thêm mạng: mã 2D, MES, SMEMA, màn hình vận hành, và bộ điều khiển nhiệt độ
> keo nối RS-485.

---

## 42.1 Bài toán: một lô hàng bị trả về, không ai biết lô nào

Khách hàng trả về một lô board mạch: keo bảo vệ không bám, bong ra sau vài tuần.

Câu hỏi đầu tiên từ bộ phận chất lượng: **những board nào khác cũng bị ảnh hưởng?**

Nếu trả lời được "chỉ 200 board chạy trong ca đêm ngày 14, khi đèn UV đã yếu" thì thu hồi 200 board.
Nếu không trả lời được, phải thu hồi **toàn bộ hàng đã giao trong tháng đó** — có thể là hàng chục
nghìn board.

Chênh lệch giữa hai kết quả là toàn bộ giá trị của **truy xuất nguồn gốc**.

Và truy xuất bắt đầu từ một việc rất đơn giản: **biết board đang nằm trên máy là board nào**.

---

## 42.2 Mã 1D và mã 2D

| | **Mã vạch 1D** *(barcode)* | ⭐ **Mã 2D** *(Data Matrix, QR)* |
|---|---|---|
| Chứa được | Ít ký tự | ⭐ Nhiều hơn hẳn |
| Diện tích cần | Dài, hẹp | ⭐ **Vuông, nhỏ** |
| Đọc được khi bẩn/xước | ⚠ Kém | ⭐ **Tốt** — có sửa lỗi |
| Hướng đọc | ⚠ Phải đúng hướng | ⭐ Đọc được ở mọi góc xoay |
| Khắc trực tiếp lên vật | Khó | ⭐ **Được** — khắc laser, in mực |
| Dùng ở đâu | Nhãn kho, bao bì | ⭐ **Sản xuất điện tử** |

> ⭐ **Ba lý do điện tử dùng mã 2D:**
> - **Diện tích** — board mạch chật, mã 2D vài mi-li-mét vuông là đủ.
> - ⭐ **Khắc trực tiếp lên board** — nhãn dán bong ra, mã khắc thì không. Đây là lý do quan trọng
>   nhất: mã phải sống suốt vòng đời sản phẩm.
> - **Sửa lỗi** — board đi qua nhiều công đoạn, mã bị xước hoặc dính keo vẫn đọc được.

### ⚠ Chất lượng mã quyết định tỉ lệ đọc được

Mã khắc quá nhạt, quá đậm, tương phản kém, hoặc bề mặt bóng đều làm giảm tỉ lệ đọc.

> ⚠ **Nếu tỉ lệ đọc thấp, hãy nghi mã trước khi nghi đầu đọc.**
> Có tiêu chuẩn về chất lượng mã và có thiết bị chấm điểm chất lượng mã. Khi tỉ lệ đọc thấp, đo chất
> lượng mã là bước chẩn đoán **rẻ và nhanh hơn** so với đổi đầu đọc.

---

## 42.2b ⭐⭐ Hai lý do "mã không đọc được" mà không nằm ở đầu đọc

Khi tỉ lệ đọc kém, người ta đổi đầu đọc, chỉnh đèn, chỉnh tiêu cự. ⭐ **Hai nguyên nhân dưới đây nằm
ở chính CÁI MÃ**, và không có đầu đọc nào cứu được.

**Một — ⚠⚠ vùng yên tĩnh bị lấn**

Mã 2D cần một **viền trống** quanh nó — gọi là **vùng yên tĩnh** *(quiet zone)*. Đầu đọc dùng viền
đó để tìm ra ranh giới và **mẫu định vị hình chữ L** của mã.

| Yêu cầu | Nội dung |
|---|---|
| Tối thiểu theo đặc tả | ⭐ **Một ô** *(module)* trống ở **cả bốn phía** |
| ⭐ Khuyến nghị thực dụng | **2–4 ô** khi nền nhiễu, bề mặt phản xạ, hoặc gần chi tiết khác |
| ⚠ Trong vùng đó | **Không được có** hoa văn, chữ, đường viền, mép chi tiết |

> ⚠⚠ **Đây là lỗi thiết kế cơ khí, không phải lỗi thị giác.**
>
> Mã in sát mép board, sát một đường mạch in, hay sát một lỗ khoan → ⭐ **đầu đọc không tìm được mẫu
> định vị**, và nó báo "không đọc được" chứ không báo "vùng yên tĩnh bị lấn".
>
> ⭐ Triệu chứng đặc trưng: ⚠ **mã đọc được khi cầm tay soi ở góc khác, nhưng đầu đọc cố định thì
> không** — vì góc nhìn khác làm mép chi tiết lọt vào hoặc ra khỏi khung.
>
> ⭐ **Quyết định vị trí đặt mã là việc của giai đoạn thiết kế** (Chương 57 giai đoạn 1) — sửa sau khi
> đã có board thì phải đổi cả bản vẽ board.

**Hai — ⭐ ô mã quá nhỏ so với độ phân giải camera**

Kích thước một ô của mã *(module / X-dimension)* quyết định camera cần bao nhiêu điểm ảnh.

```text
So diem anh tren mot o  =  do phan giai camera tren vung nhin  x  kich thuoc o
```

⭐ Đầu đọc cần **vài điểm ảnh cho mỗi ô** mới giải mã ổn định — ⚠ **con số tối thiểu cụ thể ghi trong
datasheet đầu đọc**, và nó khác nhau giữa mã in và mã khắc trực tiếp.

| Muốn cải thiện | Cách |
|---|---|
| ⭐ **Làm ô mã to hơn** | ⭐ Rẻ nhất và hiệu quả nhất — nếu còn chỗ trên sản phẩm |
| Thu hẹp vùng nhìn | Đưa đầu đọc gần hơn, hoặc dùng ống kính tiêu cự dài hơn |
| Tăng độ phân giải đầu đọc | ⚠ Đắt, và ⭐ **không cứu được mã quá nhỏ** |

> ⭐⭐ **Thứ tự đúng khi tỉ lệ đọc kém: kiểm CÁI MÃ trước, đầu đọc sau.**
>
> | Kiểm theo thứ tự | |
> |---|---|
> | 1 | ⭐ Vùng yên tĩnh có bị lấn không |
> | 2 | ⭐ Ô mã có đủ lớn cho độ phân giải hiện tại không |
> | 3 | Tương phản và chất lượng in/khắc (mục 42.9) |
> | 4 | Chiếu sáng và góc đặt |
> | 5 | Cấu hình đầu đọc |
>
> ⚠ Người ta thường bắt đầu từ mục 5 và đi ngược lên — mất nhiều ngày cho một vấn đề nằm ở mục 1.

*(Đối chiếu: ISO/IEC 16022 — đặc tả ký hiệu Data Matrix — quy định vùng yên tĩnh tối thiểu; hướng
dẫn GS1 khuyến nghị mở rộng khi môi trường nhiễu. ⚠ Sách này **không dẫn số điều khoản**; con số cụ
thể và yêu cầu điểm ảnh trên ô phải lấy từ **bản gốc đặc tả** và **datasheet đầu đọc**. Tra cứu
2026-09-03.)*

---

## 42.3 Đầu đọc — cố định hay cầm tay

| | ⭐ **Cố định** *(fixed-mount)* | **Cầm tay** *(handheld)* |
|---|---|---|
| Ai kích | ⭐ **PLC** | Người bấm nút |
| Vị trí đọc | Cố định, đã căn chỉnh | Người đưa tới |
| Dùng cho | ⭐ **Tự động** — trên chuyền | Nhập tay, xử lý ngoại lệ |
| Tỉ lệ đọc | Ổn định nếu căn đúng | Phụ thuộc người |

Ba yếu tố quyết định đầu đọc cố định hoạt động tốt hay không:

| Yếu tố | ⚠ Điều cần chú ý |
|---|---|
| **Tiêu cự** *(focus)* | Mã phải nằm trong khoảng tiêu cự. ⚠ Board cong hoặc gá lỏng làm mã ra ngoài vùng nét |
| ⭐ **Chiếu sáng** | Quan trọng hơn cả đầu đọc. Bề mặt bóng cần chiếu sáng góc thấp hoặc khuếch tán |
| **Góc đặt** | Tránh phản xạ trực tiếp vào ống kính |

> ⭐ **Chiếu sáng là thứ quyết định nhiều nhất, và là thứ hay bị coi nhẹ nhất.**
> Một đầu đọc bình thường với chiếu sáng đúng đọc tốt hơn hẳn một đầu đọc đắt tiền với chiếu sáng sai.
> Đây là cùng bài học với cảm biến quang ở Chương 4 và với laser ở Chương 33 mục 33.6: ⭐ **thử trên
> vật thật, trong điều kiện thật.**

---

## 42.4 Ghép đầu đọc vào PLC

| Cách | Ghi chú |
|---|---|
| ⭐ **Ethernet** | Phổ biến nhất hiện nay; đọc kết quả qua giao thức của hãng hoặc qua Modbus TCP (Chương 39) |
| **Nối tiếp** (RS-232/485) | Đơn giản; ⚠ chuỗi ký tự phải phân tích trong PLC (Chương 38) |
| **I/O số** | Chỉ báo "đọc được / không đọc được" — ⚠ **không lấy được nội dung mã** |

> ⭐ **DP-01 dùng Ethernet** (Phụ lục J §J.1) — theo thực tế thị trường.

### Luồng cơ bản

```text
   1. PLC gửi lệnh kích đọc  ─────────────►  Đầu đọc
   2. Đầu đọc chụp và giải mã
   3. Đầu đọc trả về:  chuỗi mã, hoặc báo KHÔNG ĐỌC ĐƯỢC
   4. PLC nhận, kiểm hợp lệ, xử lý
```

```iecst
// TrigReadCode được gọi TRƯỚC đoạn này, ngoài CASE: TrigReadCode(CLK := (Stn1_Step = 20)) — mục 42.7
IF TrigReadCode.Q THEN                       // ⭐ lệnh đọc MỚI → xoá kết quả của board TRƯỚC
    M_CodeValid := FALSE;
END_IF;

// ⭐ Kích đọc bằng cạnh lên, có timeout (Chương 38, mục 38.8)
ReadCode(Execute := TrigReadCode.Q,
         Timeout := T#2S,
         Done    => M_CodeRead,
         Error   => M_CodeError,
         Data    => CodeString);

IF M_CodeRead THEN
    IF KiemTraMaHopLe(CodeString) THEN
        CurrentBoardCode := CodeString;
        M_CodeValid := TRUE;
    ELSE
        M_CodeValid := FALSE;
        M_NoReadCount := M_NoReadCount + 1;      // ⭐ đếm để theo dõi xu hướng
    END_IF;
ELSIF M_CodeError THEN
    M_CodeValid := FALSE;
    M_NoReadCount := M_NoReadCount + 1;
END_IF;
```

> ⭐ **Luôn kiểm định dạng mã, đừng tin chuỗi nhận được.**
> Đầu đọc có thể đọc nhầm một mã khác trong tầm nhìn — nhãn vận chuyển, mã của đồ gá, mã của board
> bên cạnh. Kiểm độ dài, tiền tố, và ký tự hợp lệ **trước khi** dùng nó.

### ⭐ Kiểm định dạng và tách mã lô — hàm chuỗi làm việc thật

Định dạng mã do **khách hàng** quy định trong đặc tả (Chương 23). Giả sử đặc tả ghi: `DP1-L2409A-000457`
— tiền tố 3 ký tự, gạch nối, **mã lô** 6 ký tự bắt đầu bằng `L`, gạch nối, số thứ tự 6 chữ số, tổng
17 ký tự. ⚠ Định dạng này là **ví dụ**; định dạng thật lấy từ đặc tả của bạn.

```iecst
FUNCTION KiemTraMaHopLe : BOOL
VAR_INPUT
    Ma : STRING(40);
END_VAR
VAR
    i  : INT;
    OK : BOOL;
END_VAR

// Vị trí đếm TỪ 1:  D P 1 - L 2 4 0 9 A  -  0  0  0  4  5  7
//                   1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
OK := (LEN(Ma) = 17)
      AND (LEFT(Ma, 3) = 'DP1')
      AND (MID(Ma, 1, 4) = '-')              // MID(chuỗi, SỐ KÝ TỰ, VỊ TRÍ)
      AND (MID(Ma, 1, 5) = 'L')
      AND (MID(Ma, 1, 11) = '-');
IF OK THEN
    FOR i := 12 TO 17 DO                     // sáu ký tự cuối phải là chữ số
        IF FIND('0123456789', MID(Ma, 1, i)) = 0 THEN
            OK := FALSE;                     // FIND trả 0 = không thấy trong tập chữ số
        END_IF;
    END_FOR;
END_IF;
KiemTraMaHopLe := OK;
END_FUNCTION
```

Rồi tách mã lô để ghi vào bản ghi truy xuất:

```iecst
LotCode := MID(CurrentBoardCode, 6, 5);     // 6 ký tự, bắt đầu ở vị trí 5 → 'L2409A'
```

⭐ Hàm như thế này phải đi kèm **bảng ca thử** — cả ca đúng lẫn ca sai — và chạy lại mỗi khi sửa
(Chương 50). Tám ca dưới đây đã chạy qua đúng hàm trên:

| Chuỗi nhận được | Kết quả | Vì sao |
|---|:-:|---|
| `DP1-L2409A-000457` | ✔ | Đúng định dạng |
| `DP1-L2409A-00045` | ✘ | Thiếu một chữ số — độ dài 16 |
| `DP1-L2409A-00045X` | ✘ | Ký tự lạ ở phần số |
| `XX1-L2409A-000457` | ✘ | Sai tiền tố |
| `DP1-K2409A-000457` | ✘ | Mã lô không bắt đầu bằng `L` |
| `DP1_L2409A-000457` | ✘ | Sai dấu phân cách |
| ⭐ `SHIP-2409-000123-AB` | ✘ | **Nhãn vận chuyển** trong tầm nhìn đầu đọc — đúng tình huống ở trên |
| *(chuỗi rỗng)* | ✘ | Đầu đọc trả về rỗng |

> ⚠⚠ **Ba chi tiết quyết định hàm này đúng hay sai** — bảng đầy đủ ở Phụ lục B mục B.6b:
>
> - **Vị trí đếm từ 1**, không từ 0.
> - ⚠ `MID(chuỗi, SỐ KÝ TỰ, VỊ TRÍ)` — **số ký tự đứng trước vị trí**. Đảo hai tham số vẫn biên dịch
>   được, và cho ra một chuỗi **trông hợp lý** — `MID(Ma, 5, 1)` trả `'DP1-L'`. ⭐ Chính một giáo trình
>   quốc tế cũng in ví dụ lệch một vị trí; hãy thử mọi hàm chuỗi với một chuỗi mà **mỗi ký tự khác
>   nhau** trước khi tin nó.
> - `FIND` trả **0** khi không thấy — nên `FIND('0123456789', c) = 0` là phép thử *"c có phải chữ số
>   không"* ngắn nhất, không cần so sánh lớn nhỏ trên chuỗi.

> ⭐ **Đếm số lần không đọc được và theo dõi xu hướng.**
> Tỉ lệ không đọc tăng dần là cảnh báo sớm: ống kính bẩn, đèn yếu, hoặc chất lượng mã của lô mới kém
> hơn. Đây là mức **"cảnh báo, vẫn chạy"** (Chương 48, mục 48.6), và là cùng kỹ thuật với độ dự trữ
> tín hiệu ở Chương 12 mục 12.5.

---

## 42.5 ⭐ Luồng truy xuất đầy đủ

Đây là mục trung tâm của chương. Truy xuất không phải "ghi lại kết quả" — nó là một **cuộc đối thoại**
với hệ thống trên, xảy ra **trước** khi gia công.

```text
   1. Board tới trạm         →  PLC kích đầu đọc
   2. Đọc được mã            →  PLC hỏi MES: "board ABC123 — có được làm ở đây không?"
   3. MES trả lời:
        ├─ CHO PHÉP + mã công thức  →  PLC nạp công thức, gia công
        └─ TỪ CHỐI + lý do          →  ⭐ PLC KHÔNG gia công, loại board ra
   4. Gia công xong          →  PLC báo MES: "board ABC123 — kết quả OK/NG, thông số đã dùng"
   5. MES ghi lại            →  dữ liệu truy xuất
```

### ⭐ Vì sao bước 2 và 3 là lý do tồn tại của truy xuất

Nhiều người nghĩ truy xuất chỉ là bước 4 — ghi lại kết quả. Nhưng giá trị lớn nhất nằm ở bước 2–3:
**hỏi trước khi làm**.

| Chống được gì | Giải thích |
|---|---|
| ⭐ **Nhảy cóc công đoạn** | Board chưa qua công đoạn trước mà đã tới đây → MES từ chối. Không có nó, board thiếu bước vẫn đi tiếp và lỗi lộ ra ở cuối chuyền hoặc ở khách hàng |
| ⭐ **Làm trùng** | Board đã làm rồi mà quay lại → MES từ chối. Tra keo hai lần làm hỏng sản phẩm |
| **Sai mã hàng** | Board thuộc mã hàng khác lọt vào → MES từ chối, hoặc trả về công thức đúng |
| **Board đã bị đánh NG** | Board đã hỏng ở công đoạn trước → không tốn công gia công tiếp |

> ⭐⭐ **"Chống nhảy cóc và chống làm trùng" chính là lý do hệ truy xuất tồn tại.**
> Ghi log chỉ giúp bạn **điều tra sau khi đã hỏng**. Hỏi trước khi làm giúp bạn **không hỏng**.
>
> Và nó chỉ hoạt động nếu **mọi máy trong chuyền đều hỏi** — một máy bỏ qua là một lỗ hổng cho cả dây
> chuyền.

### Bước 4 — báo kết quả

Nội dung tối thiểu nên gửi:

| Trường | Vì sao |
|---|---|
| Mã board | Nhận dạng |
| Kết quả OK/NG | Kết luận |
| ⭐ **Lý do NG** | Để phân tích nguyên nhân, không chỉ đếm số lượng |
| ⭐ **Thông số đã dùng** | Mã và **phiên bản** công thức (Chương 29, mục 29.6) |
| Thời điểm | Ghép với các sự kiện khác |
| ⭐ **Số liệu quá trình quan trọng** | Nhiệt độ keo, cường độ UV thực tế, thời gian sấy thật |

> ⭐ **Hàng cuối là hàng trả lời được câu hỏi ở mục 42.1.**
> Nếu mỗi board mang theo **cường độ UV thực tế lúc nó được sấy**, thì khi có khiếu nại, bạn lọc ra
> đúng những board chạy khi cường độ dưới ngưỡng. Không có nó, bạn chỉ biết "ca đêm ngày 14" và phải
> thu hồi theo lô.
>
> Đây là lý do các phép đo ở Chương 31–33 có giá trị vượt xa việc điều khiển: **chúng là dữ liệu truy
> xuất.**

---

## 42.6 ⚠⚠ Khi mất kết nối MES

Đây là câu hỏi khó nhất của chương, và nó **không có đáp án kỹ thuật**.

### Vấn đề

Board tới trạm. PLC đọc mã. PLC hỏi MES. **MES không trả lời.**

Hai lựa chọn, và cả hai đều có giá:

| Lựa chọn | Được | ⚠ Mất |
|---|---|---|
| **Dừng chuyền** | ⭐ Không có board nào được làm mà không kiểm tra | Dừng sản xuất — có thể cả chuyền, có thể hàng giờ |
| **Chạy tạm, gửi bù sau** | Sản xuất tiếp tục | ⚠ **Trong thời gian đó, chống nhảy cóc và chống làm trùng KHÔNG hoạt động** |

> ⚠⚠ **Đây là quyết định của khách hàng, không phải của người lập trình.**
>
> Nó là đánh đổi giữa **rủi ro chất lượng** và **thiệt hại sản xuất**, và chỉ người chịu trách nhiệm
> về cả hai mới quyết được. Sách trình bày đánh đổi; **đặc tả phải ghi câu trả lời** (Chương 23).
>
> Trong một số ngành có quy định bắt buộc về truy xuất, lựa chọn "chạy tạm" **có thể không được phép**.
> Đây là câu hỏi phải hỏi sớm.

### Nếu chọn "chạy tạm" — bốn điều bắt buộc

| Điều | Vì sao |
|---|---|
| ⭐ **Lưu lại tại chỗ** mọi board đã làm trong thời gian mất kết nối | Để gửi bù khi có kết nối lại |
| ⭐ **Đánh dấu rõ** những board này trong dữ liệu gửi bù | Chúng **chưa được kiểm** trước khi làm — chất lượng cần biết điều đó |
| **Giới hạn thời gian hoặc số lượng** | ⚠ Chạy tạm 10 phút khác hẳn chạy tạm 8 tiếng |
| ⭐ **Báo rõ ràng trên màn hình** | Người vận hành phải **biết** máy đang chạy ở chế độ giảm |

```iecst
// Chạy tạm có giới hạn
IF M_MesCommFault THEN
    M_DegradedMode := TRUE;
    DegradedCount := DegradedCount + 1;         // đếm board làm trong chế độ giảm

    // ⚠ Giới hạn — theo đặc tả, không tự đặt
    IF DegradedCount > MAX_DEGRADED_BOARDS THEN
        M_Alm_MesLost := TRUE;                  // buộc dừng — cờ chốt, gom vào M_AnyFault (Ch.25)
        M_FaultCode := 420;
    END_IF;
END_IF;
```

> ⚠ **Đếm lỗi liên tiếp trước khi kết luận mất kết nối** — cùng kỹ thuật với Chương 38 mục 38.9. Một
> lần timeout không phải mất kết nối.

### ⚠ Nhập tay có kiểm soát

Khi đầu đọc không đọc được mã (không phải mất MES), thường cần cho phép **nhập tay**.

| Yêu cầu | Vì sao |
|---|---|
| ⭐ **Có phân quyền** | Không phải ai cũng nhập được (Chương 44) |
| ⭐ **Ghi vết**: ai nhập, lúc nào, mã gì | Nhập tay là đường vòng qua cơ chế kiểm tra |
| **Vẫn hỏi MES với mã đã nhập** | Nhập tay thay cho **đầu đọc**, không thay cho **việc kiểm tra** |
| ⚠ **Đếm và theo dõi** | Số lần nhập tay tăng là dấu hiệu đầu đọc hoặc chất lượng mã có vấn đề |

> ⚠⚠ **Nhập tay không có kiểm soát là lỗ hổng lớn nhất của mọi hệ truy xuất.**
> Nếu người vận hành gõ được mã bất kỳ để cho board đi tiếp, thì toàn bộ cơ chế chống nhảy cóc và
> chống làm trùng bị vô hiệu hoá — và không ai biết.
>
> Đây là cùng loại vấn đề với "người vận hành nới dải hợp lệ của công thức" ở Chương 29 mục 29.9,
> Bẫy 10: **một cơ chế bảo vệ mà người dùng đi vòng được thì không phải cơ chế bảo vệ.**

---

## 42.7 Trên máy mẫu DP-01

### Luồng đầy đủ ở trạm 1

```iecst
// ⭐ Mọi khối gọi MỖI vòng quét, NGOÀI CASE — sườn lên sinh từ chính bước (Chương 30 mục 30.5b)
TrigReadCode(CLK := (Stn1_Step = 20));      // vào bước 20 → đúng MỘT sườn → một lần đọc
TrigAskMes(CLK := (Stn1_Step = 30));
// … khối đọc và kiểm mã của mục 42.4 chạy tại đây …
AskMes(Execute := TrigAskMes.Q,
       BoardCode := CurrentBoardCode,
       StationId := 1,
       Timeout := T#3S,
       Done => M_MesReplied,
       Error => M_MesError,
       Allowed => M_MesAllowed,
       RecipeId => MesRecipeId,
       Reason => MesRejectReason);

CASE Stn1_Step OF
    10: // Board tới trạm 1
        IF DI_BoardStn1 THEN
            Stn1_Step := 20;
        END_IF;

    20: // ⭐ Đọc mã 2D — lệnh đọc phát ra ở sườn TrigReadCode, ngoài CASE
        IF M_CodeValid THEN
            Stn1_Step := 30;
        ELSIF M_CodeError THEN
            Stn1_Step := 25;                     // xử lý không đọc được
        END_IF;

    25: // Không đọc được — chờ nhập tay hoặc loại board
        M_NeedManualEntry := TRUE;               // hiện trên màn hình (Chương 44)
        IF M_ManualCodeEntered THEN
            Stn1_Step := 30;
        ELSIF M_OperatorReject THEN
            M_Board1IsNG := TRUE;
            Stn1_Step := 90;                     // đưa ra, đánh dấu NG
        END_IF;

    30: // ⭐ HỎI MES trước khi làm — khối AskMes gọi ngoài CASE, ở trên
        IF M_MesReplied AND M_MesAllowed THEN
            RequestedRecipeId := MesRecipeId;
            Stn1_Step := 35;                     // nạp công thức
        ELSIF M_MesReplied AND NOT M_MesAllowed THEN
            M_Board1IsNG := TRUE;                // ⭐ MES từ chối — KHÔNG gia công
            M_NgReason := MesRejectReason;
            Stn1_Step := 90;
        ELSIF M_MesError THEN
            Stn1_Step := 32;                     // mất kết nối — mục 42.6
        END_IF;

    32: // ⚠ Mất kết nối MES — theo chính sách trong đặc tả
        IF M_PolicyAllowDegraded AND (DegradedCount < MAX_DEGRADED_BOARDS) THEN
            M_DegradedMode := TRUE;
            Stn1_Step := 35;                     // chạy tạm với công thức hiện tại
        ELSE
            M_Alm_MesLost := TRUE;  M_FaultCode := 420;
        END_IF;

    35: // Nạp công thức nếu khác công thức đang dùng (Chương 29)
        // ... rồi sang bước gia công

ELSE
    Stn1_Step := 0;
END_CASE;
```

> ⚠⚠ **Bản trước của đoạn này có hai lỗi — và cả hai chỉ lộ ra từ board THỨ HAI.**
>
> 1. Nó gọi `TrigReadCode(CLK := TRUE)` **bên trong** nhánh bước 20. `R_TRIG` chỉ báo sườn khi `CLK`
>    đổi từ FALSE sang TRUE **giữa hai lần gọi**; gọi mãi với TRUE thì bộ nhớ của nó nằm ở TRUE, và từ
>    board thứ hai trở đi đầu đọc **không bao giờ được kích** (Phụ lục B mục B.9b).
> 2. ⚠⚠ Cờ `M_CodeValid` **không bao giờ được xoá** giữa hai board. Board thứ hai vào bước 20, thấy
>    cờ còn TRUE từ board trước, và đi tiếp với **mã của board trước** — ghi sai lịch sử của **hai**
>    sản phẩm cùng lúc, đúng loại sai sót mà cả chương này sinh ra để chống.
>
> ⭐ Cách sửa: lấy `CLK` từ chính bước và gọi **ngoài** `CASE`; và **xoá kết quả cũ đúng lúc phát lệnh
> đọc mới** (mục 42.4). ⚡ Bài học chung: một đoạn mã trình tự phải được thử với **ít nhất hai chu
> trình liên tiếp** — chu trình đầu tiên luôn chạy trên những giá trị khởi tạo sạch sẽ.

> ⭐ **Bước 30 là bước quan trọng nhất, và nó nằm TRƯỚC bước gia công.**
> Nhiều hệ đặt việc hỏi MES song song với gia công cho nhanh — và mất luôn khả năng chống nhảy cóc.
> Hỏi **trước**, và **chấp nhận mất vài trăm mili-giây**.
>
> ⚠ Với chu kỳ 12 giây đã chốt (Phụ lục J §J.1), vài trăm mili-giây là chấp nhận được. Nếu chu kỳ chặt
> hơn thì phải tính — đây là chỗ Chương 55 quay lại.

### Báo kết quả ở trạm 2

```iecst
// Board rời trạm 2 — báo kết quả kèm số liệu quá trình
IF TrigStn2Done.Q THEN
    ReportMes(Execute   := TRUE,
              BoardCode := Stn2_BoardCode,
              Result    := SEL(M_Board2IsNG, RESULT_OK, RESULT_NG),
              NgReason  := M_Ng2Reason,
              RecipeId  := ActiveRecipe.Id,
              RecipeVer := ActiveRecipe.Version,      // ⭐ phiên bản, Chương 29
              // ⭐ Số liệu quá trình — trả lời câu hỏi ở mục 42.1
              CureTimeMs    := ActualCureTimeMs,
              UvIntensity   := UvIntensityX10,         // Chương 31, 33
              GlueTempX10   := GlueTempX10,            // Chương 39
              GluePressX100 := GluePressAvgX100,       // Chương 32
              Degraded  := M_DegradedMode);            // ⚠ board này chưa được kiểm trước
END_IF;
```

> ⭐ **Trường `UvIntensity` là trường đắt giá nhất trong bản ghi này.**
> Nó biến câu hỏi "board nào bị ảnh hưởng khi đèn UV yếu" từ **không trả lời được** thành **một truy
> vấn**. Chi phí: một số nguyên trên mỗi bản ghi.
>
> Đây là lý do tôi khuyến nghị ở Chương 31 mục 31.7 và Chương 33 mục 33.8 cân nhắc đổi
> `AI_UvIntensity` sang 4–20 mA: nếu phép đo đó **hỏng mà không ai biết**, thì trường này ghi lại một
> con số vô nghĩa suốt thời gian đó — và bạn tin vào nó.

---

## 42.8 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| Giao thức đầu đọc | Mỗi hãng đầu đọc có giao thức riêng; ⭐ nhiều loại hỗ trợ **Modbus TCP** làm mẫu số chung (Chương 39) |
| ⚠ Định dạng chuỗi trả về | Có tiền tố, hậu tố, ký tự kết thúc khác nhau. ⚠ **Phân tích chuỗi phải theo tài liệu** |
| Cách kích đọc | Lệnh mạng, ngõ vào cứng, hoặc tự kích khi thấy vật. ⭐ Ngõ vào cứng chính xác về thời điểm hơn |
| Giao thức tới MES | ⚠ **Rất khác nhau** — mỗi hệ MES một kiểu; có nơi dùng chuẩn công nghiệp, có nơi dùng giao thức riêng |
| Thư viện phía PLC | Một số hệ PLC có khối kết nối MES sẵn; ⚠ phần lớn phải tự viết trên nền giao thức chung |
| Bộ đệm dữ liệu | ⚠ Lưu bản ghi tại chỗ khi mất kết nối cần **bộ nhớ** — kiểm dung lượng (Chương 8) |

> ⚠⚠ **Giao diện tới MES là hạng mục phải chốt SỚM trong dự án**, không phải cuối.
> Nó phụ thuộc hệ MES của khách hàng, và thường cần người của bên MES tham gia. Phát hiện muộn rằng
> giao thức không như dự kiến là một trong những nguyên nhân trễ tiến độ phổ biến nhất.
>
> Đây thuộc về đặc tả (Chương 23) và phải nằm trong danh sách câu hỏi cho khách hàng.

---

## 42.9 Bẫy thường gặp

### 🔍 BẪY 1 — Chỉ ghi log, không hỏi trước

**Hiện tượng:** ⭐ board nhảy cóc công đoạn hoặc bị làm trùng vẫn đi qua; lỗi lộ ra ở cuối chuyền hoặc
ở khách hàng.
**Cách sửa:** ⭐⭐ **hỏi MES trước khi gia công** — đó là lý do hệ truy xuất tồn tại (mục 42.5).

### 🔍 BẪY 2 — Tin chuỗi mã nhận được mà không kiểm định dạng

**Hiện tượng:** đầu đọc đọc nhầm một mã khác trong tầm nhìn — nhãn vận chuyển, mã đồ gá, board bên
cạnh.
**Cách sửa:** kiểm độ dài, tiền tố, ký tự hợp lệ **trước khi** dùng (mục 42.4).

### 🔍 BẪY 3 — Nhập tay không có kiểm soát

**Hiện tượng:** ⚠⚠ toàn bộ cơ chế chống nhảy cóc và chống làm trùng bị vô hiệu hoá — **và không ai
biết**.
**Cách sửa:** phân quyền, ghi vết, vẫn hỏi MES với mã đã nhập, và **đếm số lần** (mục 42.6).

### 🔍 BẪY 4 — Không có chính sách cho việc mất kết nối MES

**Hiện tượng:** khi mất kết nối, mỗi người xử lý một kiểu; hoặc chương trình tự quyết theo cách người
lập trình nghĩ là hợp lý.
**Cách sửa:** ⚠⚠ đây là **quyết định của khách hàng**, phải nằm trong đặc tả (mục 42.6, Chương 23).

### 🔍 BẪY 5 — Chạy tạm không giới hạn, không đánh dấu

**Hiện tượng:** tám tiếng sản xuất không được kiểm tra, và dữ liệu gửi bù **trông giống hệt** dữ liệu
bình thường.
**Cách sửa:** giới hạn thời gian/số lượng, đánh dấu rõ trong bản ghi, báo trên màn hình (mục 42.6).

### 🔍 BẪY 6 — Không ghi số liệu quá trình vào bản ghi

**Hiện tượng:** ⭐ đúng cỗ máy ở mục 42.1 — có khiếu nại nhưng **không khoanh vùng được**, phải thu
hồi theo lô lớn.
**Cách sửa:** ghi các số liệu quyết định chất lượng cùng mỗi board (mục 42.5, 42.7).

### 🔍 BẪY 7 — Không ghi phiên bản công thức

**Hiện tượng:** biết board dùng công thức nào nhưng **không biết công thức đó lúc ấy có tham số gì** —
vì nó đã bị sửa từ đó.
**Cách sửa:** ghi **mã và phiên bản** (Chương 29, mục 29.6).

### 🔍 BẪY 8 — Không theo dõi tỉ lệ không đọc được

**Hiện tượng:** tỉ lệ đọc giảm dần do ống kính bẩn hoặc chất lượng mã kém; chỉ phát hiện khi nó tệ
tới mức gây dừng máy.
**Cách sửa:** đếm và cảnh báo theo xu hướng — mức "cảnh báo, vẫn chạy" (mục 42.4).

### 🔍 BẪY 9 — Chốt giao diện MES muộn

**Hiện tượng:** cuối dự án mới phát hiện giao thức không như dự kiến; trễ tiến độ.
**Cách sửa:** chốt sớm, đưa vào đặc tả, và có người của bên MES tham gia (mục 42.8).

### 🔍 BẪY 10 — Nghi đầu đọc trước khi nghi chất lượng mã

**Hiện tượng:** đổi đầu đọc đắt tiền mà tỉ lệ đọc không cải thiện.
**Cách sửa:** ⭐ đo **chất lượng mã** và kiểm **chiếu sáng** trước — rẻ và nhanh hơn nhiều
(mục 42.2, 42.3).

---

## 42.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Vì sao điện tử dùng mã 2D | Diện tích nhỏ · ⭐ **khắc trực tiếp lên board** · có sửa lỗi |
| Tỉ lệ đọc thấp — nghi gì trước | ⭐ **Chất lượng mã và chiếu sáng**, không phải đầu đọc |
| Yếu tố quyết định nhất khi lắp đầu đọc | ⭐ **Chiếu sáng** |
| ⭐⭐ Hai nguyên nhân nằm ở **cái mã** | ⭐ **Vùng yên tĩnh bị lấn** · ⭐ **ô mã quá nhỏ so với độ phân giải** |
| Vùng yên tĩnh tối thiểu | ⭐ **Một ô** ở cả bốn phía; **2–4 ô** khi nền nhiễu |
| Triệu chứng vùng yên tĩnh bị lấn | ⚠ **Cầm tay đọc được, đầu đọc cố định thì không** |
| Cách rẻ nhất khi ô mã quá nhỏ | ⭐ **Làm ô mã to hơn** — không phải mua đầu đọc đắt hơn |
| Vị trí đặt mã quyết định ở đâu | ⭐ **Giai đoạn thiết kế** — sửa sau thì phải đổi bản vẽ board |
| Nhận chuỗi mã về thì | ⭐ **Kiểm định dạng trước khi dùng** |
| ⭐⭐ Lý do tồn tại của truy xuất | **Hỏi MES TRƯỚC khi làm** — chống nhảy cóc và chống làm trùng |
| Ghi log một mình cho gì | Chỉ giúp **điều tra sau khi đã hỏng** |
| Cơ chế chỉ hiệu quả khi | **Mọi máy trong chuyền đều hỏi** |
| Bản ghi kết quả nên có | Mã · OK/NG · **lý do NG** · **mã + phiên bản công thức** · ⭐ **số liệu quá trình** |
| ⚠⚠ Mất kết nối MES thì làm gì | **Quyết định của khách hàng**, phải nằm trong đặc tả |
| Nếu chạy tạm thì bắt buộc | Lưu tại chỗ · **đánh dấu** · **giới hạn** · báo trên màn hình |
| Nhập tay phải có | Phân quyền · ghi vết · **vẫn hỏi MES** · đếm số lần |
| ⚠⚠ Nhập tay không kiểm soát | **Lỗ hổng lớn nhất** của mọi hệ truy xuất |
| Chốt giao diện MES khi nào | ⭐ **Sớm** — thuộc đặc tả, cần bên MES tham gia |

---

## 42.11 Tự kiểm

1. ⭐ Một lô hàng bị trả về. Truy xuất nguồn gốc thay đổi quy mô thu hồi thế nào?
2. Nêu ba lý do sản xuất điện tử dùng mã 2D thay vì mã vạch 1D. Lý do nào quan trọng nhất?
3. Ba yếu tố quyết định đầu đọc cố định hoạt động tốt. Yếu tố nào hay bị coi nhẹ nhất?
4. Vì sao phải **kiểm định dạng** chuỗi mã nhận được? Cho một tình huống đọc nhầm.
5. ⭐⭐ Mô tả năm bước của luồng truy xuất đầy đủ. Bước nào là **lý do tồn tại** của hệ truy xuất, và
   vì sao?
6. ⭐ Nêu bốn thứ mà việc "hỏi MES trước khi làm" chống được. Cơ chế này chỉ hiệu quả khi nào?
7. Bản ghi kết quả nên chứa gì? Trường nào trả lời được câu hỏi ở mục 42.1?
8. ⭐ Vì sao phải ghi **phiên bản** công thức chứ không chỉ mã công thức?
9. ⚠⚠ Mất kết nối MES: nêu hai lựa chọn và cái giá của mỗi cái. **Ai** quyết định?
10. Nếu chọn "chạy tạm", nêu bốn điều bắt buộc phải làm.
11. ⭐ Vì sao **nhập tay không có kiểm soát** là lỗ hổng lớn nhất? Liên hệ với bẫy nào ở Chương 29?
12. Vì sao nên đếm và theo dõi **tỉ lệ không đọc được**? Nó thuộc mức cảnh báo nào?
13. ⭐⭐ Nêu **hai nguyên nhân "mã không đọc được" nằm ở chính cái mã**. Vì sao đổi đầu đọc không cứu
    được cả hai?
14. ⭐ Vùng yên tĩnh là gì, tối thiểu bao nhiêu, và đầu đọc dùng nó để làm gì? Triệu chứng đặc trưng
    khi nó bị lấn là gì?
15. Một mã đọc kém. Nêu **thứ tự năm bước kiểm** đúng. Người ta thường bắt đầu từ bước nào, và cái
    giá của việc bắt đầu sai chỗ?

> Câu 5, 6, 9 và 11 là bốn câu phân loại. Câu 5 là tinh thần của cả chương: **ghi log giúp bạn điều
> tra sau khi đã hỏng; hỏi trước khi làm giúp bạn không hỏng.**

---

### Chương tiếp theo

Chương 43 — **Tích hợp vision với PLC**. Bạn đã biết đọc mã. Chương sau về một hệ thị giác phức tạp
hơn: nhận toạ độ và góc lệch, đồng bộ lúc chụp với lúc vật đứng yên — và câu hỏi đáng giá nhất:
⭐ khi nào một cảm biến quang rẻ tiền làm được việc mà bạn định dùng camera.

### Nguồn tham khảo chương 42

- **ISO/IEC 16022** — *Data Matrix bar code symbology specification*: đặc tả mã Data Matrix, gồm
  ⭐ **yêu cầu vùng yên tĩnh** (mục 42.2b). *(tiêu chuẩn có bản quyền)*
- **Hướng dẫn GS1 về Data Matrix** — khuyến nghị **mở rộng vùng yên tĩnh** khi môi trường nhiễu.
  ⚠ Sách này **không dẫn số điều khoản** của các tiêu chuẩn trên; con số cụ thể phải lấy từ bản gốc.
- **ISO/IEC 15415** và **ISO/IEC 29158** — chấm điểm chất lượng mã in và mã khắc trực tiếp; dùng khi
  chẩn đoán tỉ lệ đọc thấp (mục 42.2).
- **Tài liệu đầu đọc mã** — dùng cho ⚠ **định dạng chuỗi trả về**, cách kích, giao thức, và yêu cầu
  về tiêu cự và chiếu sáng.
- ⚠ **Tài liệu giao diện của hệ MES tại khách hàng** — thứ phải xin **sớm** (mục 42.8).
- Bảng I/O, bảng công thức và số liệu đã chốt của DP-01 — Phụ lục J.

> ⚡ Luồng ở mục 42.5 là **mẫu phổ biến trong sản xuất điện tử**, không phải chuẩn bắt buộc. Hệ MES
> khác nhau có luồng khác nhau — một số hỏi và trả công thức trong một lần, một số tách làm hai bước,
> một số không quản lý công thức mà chỉ kiểm quyền. ⭐ **Luồng cụ thể phải chốt với bên MES ở giai
> đoạn đặc tả.**
>
> ⚠ Trong một số ngành có **yêu cầu pháp lý** về truy xuất nguồn gốc — thiết bị y tế, ô tô, hàng
> không. Ở đó, lựa chọn "chạy tạm khi mất kết nối" có thể **không được phép**, và yêu cầu về lưu trữ
> dữ liệu có thể chặt hơn nhiều so với nội dung chương này. Kiểm quy định áp dụng cho sản phẩm của
> khách hàng.
