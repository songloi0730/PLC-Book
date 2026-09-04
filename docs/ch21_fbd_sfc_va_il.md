# Chương 21 — FBD, SFC (và IL — đủ để đọc di sản)

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 21.1 Ba ngôn ngữ còn lại

Chương 15 cho bạn Ladder, Chương 20 cho bạn Structured Text. Chương này hoàn tất bộ năm:

| Ngôn ngữ | Vị thế thực tế | Bạn cần biết tới mức nào |
|---|---|---|
| **FBD** | Dùng nhiều ở xử lý analog và điều khiển quá trình | **Đọc và viết được** |
| **SFC** | Dùng cho trình tự; mức phổ biến khác nhau theo hãng và theo ngành | **Đọc và viết được** |
| **IL** | ⚠ Di sản — **đã bị rút khỏi bản mới của chuẩn** | **Chỉ cần đọc hiểu** |

Ba ngôn ngữ này không thay thế LD và ST. Chúng lấp hai chỗ mà LD và ST làm kém: **luồng tín hiệu**
(FBD) và **trình tự có thứ tự trước sau** (SFC).

---

## 21.2 FBD — luồng tín hiệu đi từ trái sang phải

### Ý tưởng

Trong FBD, mỗi phép xử lý là một **khối** có chân vào bên trái và chân ra bên phải. Bạn nối chân ra
của khối này vào chân vào của khối kia. Tín hiệu chảy từ trái sang phải.

```text
   DI_AirOK ──┐
              │  ┌───────┐        ┌────────┐
   DI_EStopOK─┼──┤  AND  ├────────┤  TON   ├──── M_ReadyStable
              │  │       │        │ PT=1s  │
   DI_Door1 ──┘  └───────┘        └────────┘
```

Đọc hình trên: ba điều kiện AND với nhau, kết quả đưa vào một timer, timer giữ 1 giây rồi mới cho ra
`M_ReadyStable`. Toàn bộ ý đồ nằm trong một hình, không cần đọc chữ.

### FBD mạnh ở đâu

| Việc | Vì sao FBD hợp |
|---|---|
| **Chuỗi xử lý tín hiệu** | Quy đổi thang → lọc → so ngưỡng → ra quyết định. Mỗi bước một khối, thấy được cả đường đi |
| **Xử lý analog** | Đây là quê hương của FBD (Chương 32, Chương 35) |
| **Nối nhiều khối chức năng** | Chân ra nối thẳng vào chân vào, không cần biến trung gian |
| **Logic có nhiều đầu vào** | Một khối `AND` tám chân gọn hơn tám tiếp điểm nối tiếp |

### FBD yếu ở đâu

| Việc | Vì sao FBD dở |
|---|---|
| Logic liên động dày đặc | ⚠ Người bảo trì quen ladder đọc chậm hơn hẳn; và "dòng điện" không còn là ẩn dụ dẫn đường |
| Rẽ nhánh phức tạp | Không có `IF/ELSE` — phải mô phỏng bằng khối chọn, rất rườm |
| Tính toán chuỗi dài | Mỗi phép một khối; một công thức năm phép thành năm khối nối nhau, ST viết một dòng |
| Sơ đồ lớn | Đường nối chằng chịt còn khó đọc hơn code |
| ⚠⚠ **Có hồi tiếp** | ⭐ **Chuẩn KHÔNG quy định thứ tự thực thi** — xem cảnh báo dưới |

> ⚠⚠ **"Trái sang phải, trên xuống dưới" là GIẢ ĐỊNH HỢP LÝ, không phải bảo đảm của chuẩn.**
>
> Khi ngõ ra của một khối được đưa ngược lại làm ngõ vào cho khối **đứng trước nó**, ⭐ chuẩn
> **không** nói bộ xử lý phải làm gì — điều đó **tuỳ hiện thực của từng hãng**.
>
> ⚠ Hệ quả: cùng một sơ đồ FBD có hồi tiếp **có thể cho kết quả khác nhau trên hai hệ khác nhau**, và
> khác biệt đó ⚠⚠ **không lộ ra khi đọc sơ đồ**.
>
> ⭐ Chính vì vậy **có hãng không cho vẽ đường hồi tiếp tường minh** — để thứ tự thực thi luôn rõ ràng.
>
> ⭐⭐ **Quy tắc thực dụng:** cần hồi tiếp thì ⭐ **đưa nó qua một biến trung gian có tên**, đừng vẽ
> đường vòng lại. Khi đó thứ tự đọc–ghi rõ ràng, và nó trở về đúng bài toán quen thuộc ở Chương 10
> (thứ tự trong vòng quét). ⚠ Và **tra tài liệu hãng** trước khi tin vào bất kỳ giả định nào về thứ
> tự thực thi FBD.

### So sánh trực tiếp với ladder

Cùng một logic, hai cách vẽ:

```text
LADDER
   DI_AirOK   DI_EStopOK   DI_Door1Closed          M_Ready
──────┤ ├────────┤ ├───────────┤ ├──────────────────( )──────

FBD
   DI_AirOK ──────┐
   DI_EStopOK ────┼── AND ────────────────────────── M_Ready
   DI_Door1Closed ┘
```

Với ba điều kiện, hai cách tương đương. Khác biệt lộ ra khi:

- **Nhiều điều kiện hơn** — FBD gọn hơn, ladder phải kéo nấc thang rất dài.
- **Có khối chức năng ở giữa chuỗi** — FBD nối thẳng, ladder phải đặt hộp trên nấc rồi lấy chân ra
  qua biến trung gian.
- **Cần chẩn đoán trực tuyến** — ⭐ ladder thắng rõ ràng: người bảo trì nhìn tiếp điểm nào không sáng
  là biết đứt ở đâu, không cần hiểu ngôn ngữ.

Dòng cuối là lý do bảng phân chia ở Chương 20 mục 20.6 vẫn đặt **liên động và ngõ ra cuối cùng vào
ladder**, kể cả khi FBD gọn hơn.

---

## 21.3 SFC — ngôn ngữ sinh ra cho trình tự

### Ba thành phần

**SFC** *(Sequential Function Chart)* mô tả trình tự bằng ba thứ, và chỉ ba thứ:

| Thành phần | Là gì | Vẽ thành |
|---|---|---|
| **Bước** *(step)* | Một trạng thái của trình tự | Hình chữ nhật |
| **Chuyển tiếp** *(transition)* | Điều kiện để rời bước này sang bước kế | Vạch ngang kèm điều kiện |
| **Hành động** *(action)* | Việc làm khi đang ở một bước | Hộp gắn bên cạnh bước |

```text
        ┌──────────────────┐
        │  S10  Chờ board  │◄──────────────┐
        └────────┬─────────┘               │
                 │                         │
            ─────┼─────  DI_BoardStn1      │
                 │                         │
        ┌────────┴─────────┐               │
        │  S20  Nâng kẹp   │── N: M_Stn1_ClampReq
        └────────┬─────────┘               │
                 │                         │
            ─────┼─────  DI_Clamp1Up       │
                 │                         │
        ┌────────┴─────────┐               │
        │  S30  Gia công   │               │
        └────────┬─────────┘               │
                 │                         │
            ─────┼─────  M_ProcessDone     │
                 └─────────────────────────┘
```

So với cùng trình tự viết bằng `CASE` (Chương 20, mục 20.2): SFC **thấy được toàn cảnh** — bao nhiêu
bước, đi theo đường nào, quay lại chỗ nào. Với người đọc lần đầu, đây là lợi thế lớn.

### Hai kiểu nhánh

**Nhánh song song** *(parallel / simultaneous divergence)* — hai nhánh chạy **cùng lúc**, và trình tự
chỉ đi tiếp khi **cả hai** đã xong:

```text
              ═══════╦═══════        ← vạch đôi = song song
                     ║
          ┌──────────╨──────────┐
      ┌───┴───┐             ┌───┴───┐
      │ Trạm 1│             │ Trạm 2│
      └───┬───┘             └───┬───┘
          └──────────┬──────────┘
              ═══════╩═══════        ← chờ CẢ HAI xong
```

**Nhánh lựa chọn** *(selective divergence)* — chọn **một** trong nhiều đường, tuỳ điều kiện nào đúng:

```text
              ───────┬───────        ← vạch đơn = lựa chọn
          ┌──────────┼──────────┐
      ─── ┼ ─ OK     ┼ ─ NG     │
      ┌───┴───┐  ┌───┴───┐
      │Chuyển │  │ Loại  │
      │ tiếp  │  │  bỏ   │
      └───────┘  └───────┘
```

> ⚠ **Vạch đôi và vạch đơn là khác biệt sống còn, và chúng trông rất giống nhau.**
> Vẽ nhầm vạch đơn thành vạch đôi nghĩa là trình tự chờ một nhánh **không bao giờ chạy** — máy đứng
> im vĩnh viễn, không báo gì. Đúng cỗ máy ở Chương 26, mục 26.1.
>
> Khi đọc SFC của người khác, **đếm số vạch** trước khi kết luận về luồng.

### Kiểu hành động

Chuẩn có nhiều **bổ ngữ hành động** *(action qualifier)*; ba cái bạn gặp nhiều nhất:

| Bổ ngữ | Nghĩa |
|---|---|
| **N** — *non-stored* | Hành động chạy **suốt thời gian** đang ở bước đó, tự tắt khi rời bước |
| **S** — *set* | Bật và **giữ**, kể cả sau khi rời bước — phải có `R` ở đâu đó để tắt |
| **R** — *reset* | Tắt một hành động đã `S` |

> ⚠ Dùng `S` mà quên `R` là biến thể SFC của bẫy SET/RESET ở Chương 16: một thứ được bật rồi không ai
> tắt. Quy tắc giống hệt — **mỗi `S` phải có một `R` tương ứng**, và bạn phải chỉ ra được nó ở đâu.

**Ba bổ ngữ nữa đáng biết, vì mỗi cái thay được cả một khối chức năng:**

| Bổ ngữ | Nghĩa | ⭐ Nó thay cho cái gì |
|---|---|---|
| **P** — *pulse* | Chạy **đúng một lần** mỗi khi bước được kích hoạt | ⭐ Khối bắt cạnh `R_TRIG` (Chương 16) |
| **L** — *time limited* | Chạy rồi **tự dừng sau một khoảng**, hoặc khi rời bước | ⭐ Một `TP` (Chương 17) |
| **D** — *time delayed* | ⭐ **Bắt đầu sau một khoảng**, nếu lúc đó vẫn còn ở bước | ⭐ Một `TON` |

Chuẩn còn vài bổ ngữ kết hợp nữa (lưu kèm trễ…). ⚠ Số bổ ngữ **thực sự được hiện thực** khác nhau
theo hãng — tra tài liệu trước khi dùng cái ngoài `N`/`S`/`R`.

> ⭐⭐ **Ý quan trọng hơn danh sách: SFC gói sẵn ba mẫu mà ở ngôn ngữ khác bạn phải tự dựng.**
> *"Làm đúng một lần"* · *"làm trong 2 giây rồi thôi"* · *"chờ 500 ms rồi mới làm"* — ở LD hay ST là
> ba khối chức năng kèm ba thể hiện riêng; ở SFC là **ba chữ cái**.

### ⭐⭐ Mỗi bước tự có hai biến — và một trong hai là timer miễn phí

Đây là thứ hữu ích nhất của SFC mà người mới không biết mình đang có. ⭐ Mỗi bước được cấp **hai biến,
tự động, không phải khai báo**:

| Biến | Kiểu | Nội dung |
|---|---|---|
| `TênBước.X` | `BOOL` | ⭐ **TRUE khi bước đang hoạt động**, FALSE khi không |
| ⭐⭐ `TênBước.T` | `TIME` | ⭐ **Thời gian đã ở trong bước** — chạy từ lúc vào bước, **về `t#0s`** khi rời bước |

> ⚠ **Cả hai chỉ đọc.** Chương trình không sửa được; sửa thì trình biên dịch báo lỗi. Đó là điều tốt —
> chúng luôn nói đúng sự thật về trạng thái trình tự.

> ⭐⭐ **Công dụng một — timeout của bước gần như miễn phí.**
>
> Chương 17 mục 17.4 dạy: mỗi bước chờ cơ cấu phải có **timeout để báo lỗi**. Ở LD/ST điều đó nghĩa là
> một `TON` riêng cho **từng** bước. ⭐ Trong SFC thì không phải khai báo gì:
>
> ```iecst
> IF Step30_Clamp.T > T#3s THEN
>     M_Alarm_ClampTimeout := TRUE;      // bước 30 chờ kẹp quá 3 giây
> END_IF;
> ```
>
> ⚡ Và vì `.T` **tự về 0 khi rời bước**, bạn không phải nhớ đặt lại timer — ⚠ đúng cái hay quên nhất
> khi tự dựng bằng `TON` (Chương 17, Bẫy 2).

> ⭐ **Công dụng hai — `.X` là cách đúng để phần còn lại của chương trình biết trình tự đang ở đâu.**
>
> Dùng cho đèn báo, cho điều kiện liên động, cho chẩn đoán — ⚠ **thay vì tự nuôi một biến "bước hiện
> tại" song song**, thứ chắc chắn sẽ lệch với thực tế vào một ngày nào đó.

> ⚠ **Một luật cấu trúc dễ vi phạm khi vẽ: không được đặt hai bước liền nhau mà không có bước chuyển
> ở giữa.** Nghe hiển nhiên, nhưng khi **chèn thêm bước vào sơ đồ có sẵn** thì đây là lỗi hay gặp —
> ⭐ may là trình biên dịch bắt được, nên nó chỉ tốn thời gian chứ không nguy hiểm.
>
> ⚡ Ngược lại, ⭐ **nhiều bước được phép hoạt động cùng lúc** — đó chính là cơ chế của nhánh song song.

### SFC mạnh ở đâu, yếu ở đâu

| ✅ Mạnh | ❌ Yếu |
|---|---|
| Trình tự tuyến tính có thứ tự rõ | ⚠ **Chế độ máy** — xem cảnh báo bên dưới |
| Thấy toàn cảnh, biết đang ở bước nào | Logic tổ hợp thuần (dùng LD) |
| Nhánh song song diễn đạt tự nhiên | Tính toán (dùng ST) |
| ⭐ Giám sát trực tuyến rất trực quan — bước đang chạy được tô sáng | Thay đổi cấu trúc trình tự tốn công vẽ lại |

> ⚠⚠ **SFC không phải câu trả lời cho máy trạng thái ở Chương 25.**
> Máy trạng thái chế độ cần đường **"từ mọi trạng thái đều nhảy được vào `Alarm`"**. Trong SFC, mỗi
> đường nhảy phải vẽ tường minh — nghĩa là từ tám bước phải vẽ tám đường về `Alarm`, và sơ đồ trở
> thành mớ bòng bong.
>
> Cách thường dùng trong thực tế: **chế độ máy bằng `CASE` hoặc LD; trình tự bên trong chế độ
> `Running` thì bằng SFC.** Chương 25 mục 25.8 và Chương 26 nói kỹ.

### Quan hệ với GRAFCET

SFC bắt nguồn từ **GRAFCET**, một phương pháp mô tả trình tự có trước, xuất phát từ Pháp. Bạn sẽ gặp
tên này trong tài liệu và trong bản vẽ của một số nhà chế tạo máy.

Điểm cần nắm: **GRAFCET là phương pháp mô tả, SFC là ngôn ngữ lập trình.** Bạn có thể vẽ GRAFCET trên
giấy để thiết kế trình tự (Chương 26) rồi hiện thực bằng bất kỳ ngôn ngữ nào — SFC, `CASE`, hay bit
trình tự trong ladder. Vẽ GRAFCET không bắt buộc bạn phải lập trình bằng SFC.

---

## 21.4 IL — chỉ để đọc di sản

### Nó trông như thế nào

**IL** *(Instruction List)* là ngôn ngữ dạng văn bản, mỗi dòng một lệnh, làm việc trên một **thanh
ghi tích luỹ** *(accumulator)* — rất giống hợp ngữ.

```text
LD    DI_StartPB        (* nạp giá trị vào bộ tích luỹ *)
OR    M_Running         (* OR với giá trị hiện có *)
AND   DI_StopPB
AND   DI_EStopOK
ST    M_Running         (* lưu kết quả ra biến *)
```

Đoạn trên chính là mạch tự giữ Start/Stop của Chương 15, viết bằng IL.

Vài lệnh hay gặp, đủ để bạn dò được logic:

| Lệnh | Nghĩa |
|---|---|
| `LD` / `LDN` | Nạp giá trị / nạp giá trị đảo vào bộ tích luỹ |
| `ST` | Lưu bộ tích luỹ ra biến |
| `AND` / `OR` / `XOR` | Phép logic với bộ tích luỹ |
| `ANDN` / `ORN` | Như trên nhưng với giá trị đảo |
| `S` / `R` | Đặt / xoá bit |
| `JMP` / `CAL` / `RET` | Nhảy / gọi POU / trở về |

### Vì sao vẫn gặp

- **Máy cũ.** Chương trình viết những năm 1990–2000 còn chạy tốt, và không ai viết lại một thứ đang
  chạy được.
- **Vài hệ vẫn hiển thị ladder dưới dạng danh sách lệnh** khi bạn xem ở chế độ văn bản.
- **Tài liệu cũ và ví dụ cũ** trên mạng.

### ⚠ IL đã bị rút khỏi chuẩn

Bản mới của IEC 61131-3 **không còn IL** như một ngôn ngữ được duy trì — nó được xếp vào diện lỗi
thời. Hệ quả thực tế:

- **Đừng viết code mới bằng IL.** Không có lý do kỹ thuật nào để làm vậy hôm nay.
- **Vẫn phải đọc được nó**, vì máy cũ không biến mất theo tiêu chuẩn.
- Công cụ mới có thể không còn hỗ trợ tạo POU kiểu IL, dù vẫn mở được chương trình cũ.

> 💡 **MẸO — dò logic IL nhanh**
> Đọc từ `LD` tới `ST` gần nhất: đó là **một biểu thức trọn vẹn**. `LD` bắt đầu, các lệnh ở giữa biến
> đổi bộ tích luỹ, `ST` kết thúc và lưu kết quả. Chia chương trình thành các đoạn `LD … ST` rồi dịch
> từng đoạn sang lời — bạn sẽ dò được logic mà không cần thành thạo IL.

---

## 21.5 Bảng "bài toán nào → ngôn ngữ nào"

Bảng tổng hợp của cả Phần III, gom lại ở đây để tra:

| Bài toán | Ngôn ngữ | Lý do chính |
|---|---|---|
| Liên động, điều kiện cho phép | ⭐ **LD** | Người bảo trì chẩn đoán bằng mắt, không cần đọc code |
| Điều khiển ngõ ra cuối cùng | ⭐ **LD** | "Vì sao van không mở" phải trả lời được bằng một nấc thang |
| Chuỗi xử lý tín hiệu analog | **FBD** | Thấy được đường đi của tín hiệu |
| Nối nhiều khối chức năng | **FBD** | Chân ra nối thẳng chân vào |
| Trình tự tuyến tính, có nhánh song song | **SFC** | Sinh ra cho đúng việc này; giám sát trực quan |
| Chế độ máy (Idle / Running / Alarm…) | **ST (`CASE`)** hoặc **LD** | ⚠ SFC diễn đạt "mọi trạng thái → Alarm" rất tệ |
| Tính toán, quy đổi thang, thống kê | **ST** | Ladder và FBD đều làm kém |
| Mảng, thanh ghi dịch, vòng lặp | **ST** | LD và FBD không có vòng lặp |
| Xử lý bản tin truyền thông | **ST** | Thao tác chuỗi và mảng |
| Đọc chương trình máy đời cũ | **IL** | Không có lựa chọn |

> ⚠ **Bảng này nói cái gì *hợp về kỹ thuật*.** Câu hỏi quyết định vẫn là câu ở Chương 20 mục 20.6:
> **ai sẽ mở chương trình này ra lúc hai giờ sáng, và họ đọc được gì?** Khi hai câu trả lời mâu
> thuẫn, **người bảo trì thắng**.

---

## 21.6 Trên máy mẫu DP-01

Cùng một đoạn chức năng, ba cách viết, để bạn thấy khác biệt bằng mắt.

### Điều kiện cho phép — LD (chọn cách này)

```text
   M_Stn1_ClampReq  DI_EStopOK  DI_AirOK  DI_Door1Closed      DO_Clamp1Vlv
─────────┤ ├───────────┤ ├────────┤ ├──────────┤ ├───────────────( )──────
```

### Cùng logic đó — FBD

```text
   M_Stn1_ClampReq ─┐
   DI_EStopOK ──────┤
   DI_AirOK ────────┼── AND ──────────────────────── DO_Clamp1Vlv
   DI_Door1Closed ──┘
```

FBD gọn hơn một chút. Nhưng khi máy hỏng lúc hai giờ sáng, người bảo trì nhìn **nấc thang** thấy ngay
tiếp điểm nào không sáng. Nhìn khối `AND` bốn chân thì phải mở từng chân ra xem. **LD thắng ở đây**,
và đó là lý do bảng ở mục 21.5 xếp nó vào LD.

### Trình tự trạm 1 — SFC so với `CASE`

| | SFC | `CASE` trong ST |
|---|---|---|
| Thấy toàn cảnh | ⭐ Có — nhìn sơ đồ là biết | Phải đọc hết khối |
| Giám sát trực tuyến | ⭐ Bước đang chạy được tô sáng | Xem giá trị biến bước |
| Thêm một bước vào giữa | Vẽ lại một đoạn | Thêm một nhánh `CASE` |
| Xử lý "mọi bước → Alarm" | ❌ Phải vẽ nhiều đường | ⭐ Một lệnh gán, hoặc nhánh `ELSE` |
| Chép cho trạm 2 | Vẽ lại | ⭐ Chép khối, đổi tiền tố tên |

Với DP-01 có **hai trạm gần giống nhau**, hàng cuối là hàng quyết định: `CASE` chép và sửa dễ hơn
nhiều. Sách chọn `CASE` cho trình tự, và Chương 26 đi theo hướng đó.

Nếu máy của bạn chỉ có **một** trình tự dài, không lặp lại, và đội bảo trì quen SFC — thì SFC là lựa
chọn tốt hơn. Không có đáp án chung.

---

## 21.7 Khác biệt giữa các hãng

| Ngôn ngữ | Siemens | Mitsubishi | Rockwell | CODESYS / TwinCAT |
|---|---|---|---|---|
| **FBD** | Có, dùng nhiều | Có | Có | Có |
| **SFC** | **S7-GRAPH** — gói riêng | **SFC / MELSAP3** | Routine kiểu **SFC** | SFC theo chuẩn |
| ⚠ Bản quyền SFC | S7-GRAPH thường **nằm trong gói cao hơn** | Tuỳ phiên bản GX Works | Tuỳ ấn bản Studio 5000 | Có sẵn |
| **IL** | **STL** — *Statement List*, phương ngữ riêng của Siemens, mạnh hơn IL chuẩn | Danh sách lệnh của dòng FX | Không dùng | Có nhưng đã lỗi thời |

> ⚠ **Siemens STL không phải IL chuẩn.**
> STL là phương ngữ riêng, có nhiều lệnh vượt ngoài IL của chuẩn, và ở các dòng CPU cũ nó rất phổ
> biến — nhiều chương trình S7-300/400 viết hoàn toàn bằng STL. Nếu bạn tiếp quản một máy Siemens
> đời cũ, **STL là thứ bạn sẽ phải đọc**, và nó khó hơn IL chuẩn.
>
> ⚠ Ở các dòng mới hơn, STL bị hạn chế hoặc không còn khả dụng — một lý do nữa để **không viết mới**
> bằng ngôn ngữ này.

> ⚠ **Kiểm bản quyền SFC trước khi thiết kế dựa vào nó.**
> Nếu bạn thiết kế trình tự bằng SFC rồi phát hiện gói đó không có trong bản quyền của khách hàng —
> hoặc đội bảo trì của họ không mở được — thì phải viết lại. Đây là câu hỏi thuộc Chương 13, tiêu
> chí 5.

Chi tiết đối chiếu năm hệ: **Phụ lục A2**.

---

## 21.8 Bẫy thường gặp

### 🔍 BẪY 1 — Nhầm nhánh song song với nhánh lựa chọn trong SFC

**Hiện tượng:** trình tự đứng im ở một bước, không báo gì — vì đang chờ một nhánh không bao giờ chạy.
**Cách sửa:** vạch **đôi** là song song (chờ cả hai), vạch **đơn** là lựa chọn (đi một đường). Đếm số
vạch khi đọc sơ đồ của người khác.

### 🔍 BẪY 2 — Dùng bổ ngữ `S` mà quên `R`

**Hiện tượng:** một hành động bật rồi không bao giờ tắt; cơ cấu giữ nguyên trạng thái qua nhiều bước
sau đó.
**Cách sửa:** mỗi `S` phải có một `R` tương ứng, và bạn phải chỉ được nó ở đâu. Nếu chỉ cần chạy
trong lúc ở bước đó thì dùng `N`, không dùng `S`.

### 🔍 BẪY 3 — Dùng SFC cho chế độ máy

**Hiện tượng:** sơ đồ đầy đường nhảy chéo về `Alarm`; không ai đọc nổi, và thêm một trạng thái mới là
phải vẽ thêm một đường từ mọi bước.
**Cách sửa:** chế độ máy bằng `CASE` hoặc LD; SFC cho trình tự bên trong (mục 21.3, Chương 25).

### 🔍 BẪY 4 — Sơ đồ FBD quá lớn

**Hiện tượng:** đường nối chằng chịt, phải cuộn màn hình hai chiều để lần theo một tín hiệu; khó hơn
hẳn so với đọc code.
**Cách sửa:** tách thành nhiều khối nhỏ, mỗi khối một chức năng. Nếu vẫn rối thì bài toán đó có lẽ
thuộc về ST.

### 🔍 BẪY 5 — Viết code mới bằng IL hoặc STL

**Hiện tượng:** vài năm sau không ai trong đội đọc được; và công cụ mới có thể không còn hỗ trợ tạo
mới.
**Cách sửa:** IL đã bị rút khỏi chuẩn. Viết mới bằng LD, ST hoặc SFC. IL và STL chỉ để **đọc**.

### 🔍 BẪY 6 — Dùng FBD cho liên động rồi khó chẩn đoán

**Hiện tượng:** máy không chạy, người bảo trì nhìn khối `AND` tám chân mà không biết chân nào sai;
phải mở bảng theo dõi từng biến.
**Cách sửa:** liên động và ngõ ra cuối để ở LD. Đây là quy tắc, không phải sở thích (mục 21.5).

### 🔍 BẪY 7 — Thiết kế bằng SFC mà chưa kiểm bản quyền

**Hiện tượng:** thiết kế xong mới biết khách hàng không có gói SFC, hoặc đội bảo trì không mở được.
Phải viết lại.
**Cách sửa:** kiểm ở giai đoạn chọn hệ (Chương 13, tiêu chí 5), không phải lúc lập trình.

### 🔍 BẪY 8 — Tưởng vẽ GRAFCET thì bắt buộc lập trình bằng SFC

**Hiện tượng:** ép dùng SFC dù `CASE` hợp hơn với máy nhiều trạm giống nhau.
**Cách sửa:** GRAFCET là **cách mô tả**; SFC là **cách hiện thực**. Vẽ GRAFCET trên giấy rồi hiện
thực bằng ngôn ngữ nào cũng được (mục 21.3, Chương 26).

---

## 21.9 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| FBD hợp với | Chuỗi xử lý tín hiệu, analog, nối nhiều khối chức năng |
| FBD dở với | Liên động cần chẩn đoán nhanh · rẽ nhánh phức tạp · tính toán chuỗi dài |
| Ba thành phần của SFC | **Bước · chuyển tiếp · hành động** |
| Vạch đôi trong SFC | **Song song** — chờ **cả hai** nhánh xong |
| Vạch đơn trong SFC | **Lựa chọn** — đi **một** đường |
| Bổ ngữ `N` / `S` / `R` | Chạy trong bước / bật và giữ / tắt. **Mỗi `S` phải có một `R`** |
| SFC dùng cho chế độ máy? | ❌ **Không** — dùng `CASE` hoặc LD |
| GRAFCET với SFC | GRAFCET là **cách mô tả**, SFC là **ngôn ngữ**. Không bắt buộc đi cùng nhau |
| IL | ⚠ Đã bị **rút khỏi chuẩn** — chỉ đọc, không viết mới |
| Siemens STL | Phương ngữ riêng, mạnh hơn IL chuẩn; phổ biến ở S7-300/400 đời cũ |
| ⭐⭐ Mỗi bước SFC tự có | `TênBước.X` (đang ở bước) và ⭐ **`TênBước.T` — timer sẵn, tự về 0** |
| Timeout bước trong SFC | ⭐ **Không phải khai `TON`** — dùng thẳng `.T` |
| Bổ ngữ `P` / `L` / `D` | Thay cho `R_TRIG` / `TP` / `TON` |
| ⚠⚠ Thứ tự thực thi FBD khi có hồi tiếp | ⭐ **Chuẩn KHÔNG quy định** — tuỳ hãng; đưa hồi tiếp qua **biến trung gian có tên** |
| Khi bảng kỹ thuật mâu thuẫn với người bảo trì | ⭐ **Người bảo trì thắng** |

---

## 21.10 Tự kiểm

1. Nêu hai nhóm việc mà FBD làm tốt hơn ladder, và hai nhóm việc FBD làm kém hơn.
2. Kể ba thành phần của SFC và nói ngắn gọn vai trò từng cái.
3. ⭐ Phân biệt nhánh song song với nhánh lựa chọn trong SFC. Vẽ nhầm thì **triệu chứng trên máy** là
   gì?
4. Ba bổ ngữ hành động `N`, `S`, `R` khác nhau thế nào? Dùng `S` mà quên `R` gây ra chuyện gì?
5. ⭐ Vì sao SFC **không** phải lựa chọn tốt cho máy trạng thái chế độ ở Chương 25?
6. GRAFCET và SFC khác nhau ở điểm nào? Vẽ GRAFCET có bắt buộc lập trình bằng SFC không?
7. Vì sao IL bị rút khỏi chuẩn, và vì sao bạn vẫn cần đọc được nó?
8. Đọc đoạn IL sau và diễn đạt bằng lời:
   `LD DI_StartPB` / `OR M_Running` / `AND DI_StopPB` / `ST M_Running`
9. Siemens STL khác IL chuẩn ở điểm nào, và vì sao điều đó quan trọng khi tiếp quản máy Siemens cũ?
10. ⭐ Với DP-01 có hai trạm gần giống nhau, vì sao sách chọn `CASE` thay vì SFC cho trình tự? Trong
    tình huống nào thì SFC lại là lựa chọn tốt hơn?
11. ⭐⭐ Mỗi bước SFC tự có hai biến nào? Nêu **hai** việc mà `.T` làm được và giải thích vì sao nó tiện
    hơn tự dựng một `TON` cho từng bước.
12. ⭐ Bổ ngữ `P`, `L`, `D` mỗi cái thay cho khối chức năng nào ở LD/ST?
13. ⚠⚠ Một sơ đồ FBD có đường hồi tiếp chạy đúng trên hệ A, sai trên hệ B. ⭐ Vì sao điều này **không**
    phải lỗi của hãng nào? Cách viết nào tránh được hẳn?

> Câu 3, 5 và 10 là ba câu phân loại. Câu 10 là tinh thần của cả chương: **không có ngôn ngữ nào tốt
> nhất — chỉ có ngôn ngữ hợp với bài toán này, cỗ máy này, và đội ngũ này.**

---

### Chương tiếp theo

Chương 22 — **Đọc & sửa chương trình của người khác**. Bạn đã biết cả năm ngôn ngữ. Nhưng ở công việc
thật, phần lớn thời gian không phải viết mới — mà là mở một chương trình bạn chưa từng thấy, không
có tài liệu, và phải sửa nó mà không làm hỏng thứ đang chạy.

### Nguồn tham khảo chương 21

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: định nghĩa FBD, SFC (bước,
  chuyển tiếp, hành động, bổ ngữ hành động, các kiểu nhánh) và IL. *(tiêu chuẩn có bản quyền)*
- Tài liệu về **GRAFCET** — phương pháp mô tả trình tự mà SFC bắt nguồn từ đó, có tiêu chuẩn riêng.
- Tài liệu lập trình của từng hệ trong Phụ lục A — dùng cho bảng ở mục 21.7: tên gói SFC của từng
  hãng, tình trạng bản quyền, và đặc điểm của Siemens STL.
- **Hanssen, Dag H.** — *Programmable Logic Controllers: A Practical Approach to IEC 61131-3 using
  CoDeSys*, §10.3 và ch. 12: ⭐ **chuẩn không quy định thứ tự thực thi FBD khi có hồi tiếp** (tuỳ hiện
  thực; có hãng không cho vẽ hồi tiếp tường minh); ⭐⭐ **`Step.X` và `Step.T`** — mọi bước SFC có sẵn
  cờ trạng thái và **timer nội**, cả hai chỉ đọc; bảng **bổ ngữ hành động** `N`/`S`/`R`/`P`/`L`/`D`;
  và luật **không đặt hai bước liền nhau không có bước chuyển**.

> ⚡ Nhận định "IL đã bị rút khỏi bản mới của chuẩn" là **thay đổi giữa các phiên bản tiêu chuẩn**.
> Khi cần dẫn chiếu chính thức, kiểm phiên bản IEC 61131-3 đang hiệu lực tại thị trường của bạn —
> phiên bản áp dụng có thể khác nhau tuỳ nơi và tuỳ thời điểm (B10).
