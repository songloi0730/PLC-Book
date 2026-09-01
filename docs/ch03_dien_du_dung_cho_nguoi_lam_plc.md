# Chương 3 — Điện đủ dùng cho người làm PLC

---

> ⚠⚠ **ĐỌC TRƯỚC — phạm vi và giới hạn của chương này**
>
> Điện giật giết người, và nó giết ở mức điện áp thấp hơn nhiều so với điều đa số người ta tưởng.
>
> Chương này cho bạn **lượng điện tối thiểu để làm việc được với PLC và để hiểu vì sao các quy tắc an
> toàn tồn tại**. Nó **không**:
> - không thay thế **khoá đào tạo an toàn điện** do cơ sở của bạn tổ chức;
> - không thay thế **quy định và quy trình** tại nơi bạn làm việc;
> - không cấp cho bạn quyền làm việc trên thiết bị mang điện.
>
> Ở hầu hết nơi, làm việc với điện lưới đòi hỏi **đào tạo và cho phép chính thức**. Người **có thẩm
> quyền** — có chuyên môn và được phép — là người làm những việc mà chương này chỉ mô tả. Đọc để hiểu
> và để đặt câu hỏi đúng, không phải để tự làm.
>
> Nếu bạn chỉ nhớ một câu từ chương này: **khi không chắc, đừng chạm — hỏi.**

---

## 3.1 Vì sao người lập trình cần chương này

Bạn viết chương trình, không đấu tủ. Vậy vì sao phải học điện?

Bốn lý do rất cụ thể, và cả bốn đều đã xuất hiện trong sách:

- **Bạn sẽ cầm đồng hồ vạn năng.** Chẩn đoán sự cố PLC là công việc đo đạc trước, đọc code sau
  (Chương 51). Không đo được thì bạn chỉ đoán.
- **Bạn quyết định những thứ có hậu quả điện.** Chọn kiểu ngõ ra, chọn cảm biến PNP hay NPN, quyết
  định tín hiệu nào phải dùng tiếp điểm NC — đều là quyết định điện (Chương 4, Chương 9, Chương 15).
- **Rất nhiều "lỗi phần mềm" thực ra là lỗi điện.** Nguồn thiếu công suất, nhiễu, dòng rò, tiếp xúc
  kém. Không biết những thứ này thì bạn sẽ đi tìm trong code — nơi không có lỗi nào (Chương 8, 9).
- **Mạch tự giữ trong ladder có gốc là một mạch rơ-le thật.** Hiểu cái gốc đó làm Chương 15 dễ hơn
  hẳn — mục 3.6.

---

## 3.2 Ba đại lượng và một công thức

| Đại lượng | Ký hiệu | Đơn vị | Hình dung bằng nước |
|---|---|---|---|
| **Điện áp** *(voltage)* | U (hoặc V) | vôn, V | **Áp lực** đẩy nước trong ống |
| **Dòng điện** *(current)* | I | ampe, A | **Lưu lượng** nước chảy qua |
| **Điện trở** *(resistance)* | R | ôm, Ω | **Độ hẹp** của ống, cản dòng chảy |

**Định luật Ohm** buộc ba đại lượng lại:

```text
U = I × R        I = U / R        R = U / I
```

Và **công suất** *(power)*, đơn vị oát (W):

```text
P = U × I
```

### Ba hệ quả bạn dùng hằng ngày

**1. Điện trở nhỏ → dòng lớn.** Một chỗ chạm chập gần như không có điện trở, nên dòng vọt lên rất
cao. Đó là lý do phải có cầu chì và aptomat: chúng cắt trước khi dây kịp nóng chảy.

**2. Tiếp xúc kém → sụt áp → nóng.** Một đầu cốt lỏng tạo thêm điện trở ở chỗ đó. Dòng vẫn phải chảy
qua, nên chỗ đó **sinh nhiệt** theo `P = I² × R`. Đây là nguyên nhân của phần lớn sự cố "cháy đầu
nối", và nó **nặng dần theo thời gian**: nóng làm oxy hoá, oxy hoá làm điện trở tăng, điện trở tăng
làm nóng hơn.

**3. Dây dài → sụt áp.** Dây có điện trở. Với dòng lớn và dây dài, điện áp ở cuối dây thấp hơn ở đầu.
Đây là lý do phải đo 24 V **tại thiết bị**, không phải tại bộ nguồn (Chương 8, mục 8.7).

> 💡 **Ba con số đáng nhớ cho công việc PLC**
> - Cảm biến quang điển hình: vài chục **mA**.
> - Cuộn van điện từ 24 V: vài trăm **mA**.
> - Ngõ ra transistor của module PLC: thường chịu được vài trăm mA mỗi kênh.
>
> Ba con số này cho bạn **cảm giác về độ lớn**, đủ để phát hiện ngay khi có gì đó vô lý. Số liệu
> chính xác thì tra datasheet (Chương 9).

---

## 3.3 DC và AC — và vì sao công nghiệp chọn 24 VDC

| | **DC** — một chiều *(direct current)* | **AC** — xoay chiều *(alternating current)* |
|---|---|---|
| Chiều dòng | Không đổi | Đảo chiều đều đặn, 50 hoặc 60 lần mỗi giây |
| Có cực tính | ⚠ **Có** — đấu ngược có thể hỏng thiết bị | Không |
| Dùng ở đâu trong tủ | Mạch điều khiển, cảm biến, PLC | Nguồn vào, động cơ, tải công suất |
| Đo bằng đồng hồ | Chọn thang **DC V** | Chọn thang **AC V** |

### Vì sao 24 VDC là chuẩn của mạch điều khiển

Bốn lý do, xếp theo tầm quan trọng:

- ⭐ **An toàn hơn đáng kể.** 24 V một chiều nằm trong dải **điện áp cực thấp** *(extra-low voltage)*.
  Với da khô và điều kiện bình thường, nó thường không gây giật nguy hiểm. ⚠ Nhưng xem cảnh báo ở
  mục 3.7 — "an toàn hơn" không phải "an toàn".
- **Đủ để đi xa trong tủ và trong máy** mà sụt áp còn chấp nhận được.
- **Hầu hết thiết bị công nghiệp đều có bản 24 VDC** — cảm biến, van, rơ-le, đèn báo. Một chuẩn chung
  nghĩa là ít loại nguồn hơn, ít phụ tùng hơn.
- **Dễ dự phòng bằng ắc-quy** khi cần duy trì mạch điều khiển.

> ⚠ **24 V an toàn hơn với NGƯỜI, nhưng không "hiền" với THIẾT BỊ.**
> Chạm nhầm hai dây 24 V có thể làm hỏng module PLC, và một chỗ chập 24 V dòng lớn vẫn gây cháy. An
> toàn cho người và an toàn cho thiết bị là hai chuyện khác nhau.

---

## 3.4 ⭐ Đồng hồ vạn năng — dùng đúng cách

Đây là mục thực hành quan trọng nhất chương. **Đồng hồ vạn năng** *(multimeter)* là công cụ chẩn đoán
số một của người làm PLC (Chương 51).

### Quy tắc vàng: đo áp SONG SONG, đo dòng NỐI TIẾP

```text
ĐO ĐIỆN ÁP — đặt hai que SONG SONG với tải
                    ┌─── tải ───┐
   +24V ────────────┤           ├──────────── 0V
                    │           │
                   (V)─────────(V)      ← que đo đặt hai bên tải

ĐO DÒNG ĐIỆN — cắt mạch, đưa đồng hồ vào NỐI TIẾP
   +24V ────(A)──── tải ─────────────────── 0V
             ↑
        đồng hồ nằm TRONG đường đi của dòng
```

> ⚠⚠ **NGUY HIỂM — lỗi kinh điển: để đồng hồ ở thang ĐO DÒNG rồi đo điện áp**
>
> Ở thang đo dòng, hai que đo gần như **nối tắt với nhau** (điện trở rất nhỏ — đó là điều kiện để đo
> dòng mà không ảnh hưởng mạch). Chạm hai que vào hai cực điện áp nghĩa là **tạo một chỗ ngắn mạch**.
>
> Kết quả: nổ cầu chì trong đồng hồ nếu may mắn; hồ quang, hỏng đồng hồ, và **bỏng tay** nếu ở mạch
> có công suất lớn.
>
> **Thói quen bắt buộc:** sau mỗi lần đo dòng, **vặn ngay về thang đo áp**. Và trước mỗi lần đo, nhìn
> lại vị trí que đo và vị trí núm xoay — hai giây.

### Bốn phép đo hay dùng nhất

| Phép đo | Thang | Cách làm | Dùng khi |
|---|---|---|---|
| **Điện áp DC** | DC V | Que đen vào 0 V, que đỏ vào điểm cần đo | Kiểm nguồn, kiểm tín hiệu cảm biến |
| **Thông mạch** | Chuông / Ω | ⚠ **Mạch phải MẤT ĐIỆN** | Kiểm dây đứt, kiểm tiếp điểm |
| **Điện trở** | Ω | ⚠ **Mạch phải MẤT ĐIỆN** | Đo cuộn dây, kiểm cách điện thô |
| **Dòng điện** | A | Cắt mạch, mắc nối tiếp | Kiểm tải tiêu thụ bao nhiêu |

> ⚠ **Đo thông mạch và đo điện trở trên mạch CÒN ĐIỆN cho kết quả sai và có thể hỏng đồng hồ.**
> Hai thang này hoạt động bằng cách đồng hồ **tự cấp** một dòng nhỏ. Có điện từ ngoài vào thì phép đo
> vô nghĩa.

### Ampe kìm — đo dòng mà không cắt mạch

**Ampe kìm** *(clamp meter)* đo dòng bằng cách **kẹp quanh dây**, không cần cắt mạch. Với việc kiểm
tra dòng tải trong tủ đang chạy, đây là công cụ đúng.

Hai điều dễ sai:

- ⚠ **Kẹp quanh MỘT sợi dây thôi.** Kẹp cả bó hoặc cả cáp hai dây thì dòng đi và dòng về triệt tiêu
  nhau — đồng hồ đọc gần bằng 0, và bạn kết luận sai là "không có dòng".
- **Nhiều ampe kìm rẻ chỉ đo được AC.** Đo dòng DC cần loại có cảm biến Hall. Trong tủ PLC phần lớn
  tải là DC, nên kiểm tính năng này trước khi mua.

---

## 3.5 Rơ-le và contactor

### Nguyên lý chung

Cả hai là **công tắc điều khiển bằng điện**: cấp điện cho **cuộn hút** *(coil)* thì lực từ hút các
**tiếp điểm** *(contacts)* đóng hoặc mở.

```text
        cuộn hút                    tiếp điểm
     ┌──────────┐              ─────o  o─────   NO (thường mở)
   ──┤   COIL   ├──
     └──────────┘              ─────o──o─────   NC (thường đóng)
      A1      A2
```

Điểm mấu chốt: **mạch cuộn hút và mạch tiếp điểm hoàn toàn tách rời**. Cuộn hút 24 VDC từ PLC có thể
điều khiển tiếp điểm đóng cắt 400 VAC cho động cơ. Đây là **cách ly thật** — và là lý do rơ-le vẫn
tồn tại dù transistor nhanh hơn (Chương 9, mục 9.3).

### Phân biệt

| | **Rơ-le** *(relay)* | **Contactor** |
|---|---|---|
| Tải | Nhỏ — đèn, van, tín hiệu | Lớn — động cơ, gia nhiệt |
| Số tiếp điểm | Nhiều, thường 2–4 cặp | Ít, nhưng chịu dòng cao |
| Dập hồ quang | Cơ bản | ⭐ Có buồng dập hồ quang |
| Tiếp điểm phụ | Ít | Thường có, để báo trạng thái về PLC |

> 💡 **Tiếp điểm phụ của contactor là thứ nên dùng.** Nó cho PLC biết contactor **thật sự đã đóng
> chưa**, thay vì chỉ biết là đã ra lệnh. Đây chính là nguyên tắc "giám sát phản hồi thay vì tin
> lệnh" (Chương 48) áp ở tầng điện.

### ⭐ Tiếp điểm cưỡng bức — vì sao nó tồn tại

**Tiếp điểm dẫn động cưỡng bức** *(forcibly guided contacts / mechanically linked contacts)* là loại
rơ-le mà các tiếp điểm NO và NC **bị nối cứng cơ khí** với nhau.

Ý nghĩa: nếu một tiếp điểm NO bị **hàn dính** — hỏng hóc rất thực tế sau nhiều lần đóng cắt — thì
tiếp điểm NC **không thể đóng lại được**. Bản thân sự hỏng hóc trở nên **phát hiện được**.

```text
Rơ-le thường:  NO hàn dính  →  NC vẫn đóng bình thường  →  không ai biết
Cưỡng bức:     NO hàn dính  →  NC KHÔNG đóng được       →  mạch giám sát phát hiện
```

> ⚠ **Đây là lý do rơ-le an toàn dùng loại này**, và là một ví dụ rất rõ của nguyên tắc "hỏng hóc phải
> phát hiện được" (Chương 47, Chương 48). Rơ-le thường **không** thay thế được ở vị trí này, dù nhìn
> bề ngoài giống nhau.

---

## 3.6 ⭐ Mạch tự giữ bằng rơ-le — gốc của "latch"

Trước khi có PLC, mạch Start/Stop được dựng bằng rơ-le. Hiểu mạch này làm Chương 15 và Chương 16 dễ
hơn hẳn, vì ladder **chính là bản vẽ của mạch này**.

```text
   L                                                        N
   │                                                        │
   ├──[ STOP ]──┬──[ START ]──┬────────( K1 )───────────────┤
   │    NC      │     NO      │         cuộn hút            │
   │            │             │                             │
   │            └──[ K1 ]─────┘                             │
   │             tiếp điểm phụ của chính K1                 │
```

Hoạt động:

1. Trạng thái nghỉ: `STOP` (NC) đóng, `START` (NO) mở → cuộn `K1` không có điện.
2. **Nhấn START**: dòng đi qua `STOP` → `START` → cuộn `K1`. Rơ-le hút.
3. Rơ-le hút làm **tiếp điểm phụ `K1` đóng**, tạo đường dẫn song song với nút START.
4. **Nhả START**: dòng vẫn đi qua tiếp điểm `K1` → cuộn vẫn có điện. **Mạch tự giữ.**
5. **Nhấn STOP**: cắt đường dẫn ở gốc → cuộn mất điện → tiếp điểm `K1` nhả → mạch không tự phục hồi.

### Ba bài học chuyển thẳng sang PLC

**1. Nhánh tự giữ.** Tiếp điểm `K1` song song với nút START chính là nhánh tự giữ trong ladder
(Chương 15, mục 15.4; Chương 16, mục 16.2). Cùng một ý tưởng, vẽ giống hệt.

**2. ⭐ Vì sao nút STOP dùng tiếp điểm NC.** Đây là bài học quan trọng nhất của mục này.

Giả sử dây nối tới nút STOP **bị đứt**:

| Nút STOP là | Dây đứt thì | Kết quả |
|---|---|---|
| **NC** (thường đóng) | Mạch **mở** ra | ✅ Cuộn mất điện, **máy dừng** — an toàn |
| NO (thường mở) | Mạch giữ nguyên | ❌ Máy **vẫn chạy**, và nút STOP **không còn tác dụng** |

Với NC, một sợi dây đứt làm máy dừng — phiền, nhưng an toàn. Với NO, dây đứt làm mất luôn khả năng
dừng, **và không ai biết cho tới lúc cần nhấn**.

Đây là **nguyên tắc hỏng-về-an-toàn** *(fail-safe)*, và nó bắt nguồn từ vật lý của sợi dây chứ không
từ quy ước của phần mềm. Nó đúng ở mọi hệ PLC, và Chương 15 mục 15.3 xây cả bảng bốn tổ hợp trên nền
này.

**3. Mất điện thì mạch không tự chạy lại.** Cuộn nhả, tiếp điểm tự giữ mở. Có điện trở lại thì phải
**nhấn START lần nữa** — một hành động có chủ ý của người. Đây chính là yêu cầu "khởi động lại có chủ
ý" mà Chương 16 mục 16.4 và Chương 48 nói tới, và nó có sẵn trong mạch rơ-le **miễn phí**.

> ⚠ Trong PLC, hành vi số 3 **không tự có** — nó phụ thuộc bạn khai báo biến `M_Running` là giữ được
> hay không. Mạch rơ-le đúng vì vật lý; chương trình PLC đúng vì **bạn quyết định đúng** (Chương 16).

---

## 3.7 An toàn điện và LOTO

### Điện giật — vài sự thật ngược với trực giác

> ⚠⚠ **NGUY HIỂM**
>
> - **Dòng giết người, không phải điện áp.** Dòng qua tim ở mức chỉ vài chục mili-ampe đã có thể gây
>   rung thất và tử vong. Đó là dòng **nhỏ hơn dòng của một cuộn van điện từ**.
> - **Điện áp thấp vẫn giết được trong điều kiện xấu.** Da ướt, mồ hôi, vết thương hở làm điện trở cơ
>   thể giảm mạnh. "24 V an toàn" là phát biểu **có điều kiện**, không phải quy luật.
> - **Đường đi của dòng quyết định mức độ nguy hiểm.** Tay này sang tay kia đi qua tim — nguy hiểm
>   nhất. Đây là lý do thợ điện có thói quen **để một tay trong túi** khi buộc phải đo mạch có điện.
> - **Điện lưới không cho cơ hội thứ hai.** Không có "thử một lần xem sao".

### Quy tắc làm việc

| Quy tắc | Vì sao |
|---|---|
| ⭐ **Cắt điện trước khi làm việc** | Quy tắc số một; mọi quy tắc khác là phòng khi quy tắc này không thực hiện được |
| **Kiểm tra là đã mất điện** — bằng đồng hồ | Aptomat có thể gán nhãn sai; mạch có thể được cấp từ nguồn khác |
| ⭐ **Kiểm cả đồng hồ nữa** | Đo trên nguồn đã biết là có điện → đo mạch cần làm → đo lại nguồn có điện. Nếu không làm bước cuối, một đồng hồ hỏng sẽ nói "không có điện" ở mọi chỗ |
| **Xả năng lượng tích trữ** | ⚠ Tụ điện trong bộ nguồn và biến tần giữ điện áp nguy hiểm **sau khi đã cắt nguồn** — chờ đủ thời gian nhà sản xuất quy định |
| **Một tay trong túi** khi buộc phải đo mạch có điện | Tránh đường dòng qua tim |
| **Dùng dụng cụ cách điện** | Tuốc-nơ-vít cách điện, không phải tuốc-nơ-vít thường |
| **Không làm một mình** trên mạch nguy hiểm | Cần người gọi cấp cứu và biết cách ngắt nguồn |

### LOTO — khoá và gắn thẻ

**LOTO** *(lockout–tagout)* là quy trình bảo đảm nguồn năng lượng **không thể được cấp lại** trong
lúc có người đang làm việc.

| Bước | Việc |
|---|---|
| 1 | Thông báo cho những người bị ảnh hưởng |
| 2 | Tắt thiết bị theo trình tự bình thường |
| 3 | **Cô lập** mọi nguồn năng lượng — điện, khí nén (Chương 6), thuỷ lực, cơ năng tích trữ |
| 4 | ⭐ **Khoá** cơ cấu cô lập bằng khoá cá nhân, và **gắn thẻ** ghi tên, ngày, lý do |
| 5 | **Xả** năng lượng tích trữ — tụ điện, khí nén trong ống, vật nặng treo |
| 6 | ⭐ **Kiểm chứng** đã mất điện bằng phép đo, và thử khởi động |

> ⚠⚠ **Ba điều làm LOTO thành vô nghĩa nếu thiếu**
>
> **1. Khoá phải là khoá cá nhân, chìa nằm trong túi người đang làm việc.** Nhiều người cùng làm thì
> mỗi người một khoá trên cùng một cơ cấu. Không ai gỡ được khoá của người khác. Đây không phải thủ
> tục hình thức — nó là thứ duy nhất bảo đảm không ai cấp điện lại khi bạn đang đưa tay vào máy.
>
> **2. Phải cô lập MỌI nguồn năng lượng.** Cắt điện nhưng còn khí nén trong ống thì xy-lanh vẫn đủ
> sức đi hết hành trình (Chương 6, mục 6.7). Một cơ cấu treo vẫn rơi được vì trọng lực.
>
> **3. Bước 6 không được bỏ.** Cắt aptomat rồi mà không đo, không thử, thì bạn đang tin vào một cái
> nhãn — và nhãn thì có thể sai.

> ⚠ **Ba yêu cầu với van/cơ cấu cô lập** — quyết định lúc **thiết kế**, rất tốn để sửa sau
> (Chương 6, mục 6.7; Chương 47, mục 47.10):
> khoá được · có cửa xả · đặt ở chỗ với tới được.

Quy trình LOTO cụ thể do **cơ sở của bạn ban hành**. Nội dung trên là để bạn hiểu logic đằng sau nó —
không phải để thay nó.

---

## 3.8 Trên máy mẫu DP-01

Chương này chưa dùng máy mẫu ở mức chi tiết, nhưng ba điều đã áp dụng được:

| Điều | Áp ở đâu |
|---|---|
| `DI_StopPB` và `DI_EStopOK` là tín hiệu từ **tiếp điểm NC** | Bảng I/O — và mục 3.6 giải thích **vì sao** |
| Cuộn van khí là **tải cảm**, cần mạch dập | Chương 5, Chương 9 |
| Máy phải cô lập được **cả điện lẫn khí nén** | Chương 6, Chương 47 |

Bảng I/O đầy đủ ở Phụ lục J; từ Chương 4 trở đi máy mẫu được dùng liên tục.

---

## 3.9 Bẫy thường gặp

### 🔍 BẪY 1 — Để đồng hồ ở thang đo dòng rồi đo điện áp

**Hiện tượng:** nổ cầu chì trong đồng hồ; ở mạch công suất lớn thì hồ quang và bỏng.
**Cách sửa:** thói quen **vặn về thang đo áp ngay sau mỗi lần đo dòng**; nhìn núm xoay trước mỗi phép
đo.

### 🔍 BẪY 2 — Kẹp ampe kìm quanh cả cáp hai dây

**Hiện tượng:** đồng hồ đọc gần 0, kết luận sai là "không có dòng", đi tìm nhầm hướng.
**Cách sửa:** kẹp quanh **một** sợi.

### 🔍 BẪY 3 — Đo thông mạch trên mạch còn điện

**Hiện tượng:** kết quả vô nghĩa; có thể hỏng đồng hồ.
**Cách sửa:** cắt điện trước, và **kiểm chứng đã mất điện** rồi mới đo thông mạch.

### 🔍 BẪY 4 — Tin aptomat đã cắt mà không kiểm chứng

**Hiện tượng:** chạm vào mạch vẫn còn điện — vì nhãn sai, hoặc mạch được cấp từ nguồn thứ hai.
**Cách sửa:** đo. Và **kiểm cả đồng hồ** theo quy trình ba bước ở mục 3.7.

### 🔍 BẪY 5 — Quên tụ điện còn tích điện sau khi cắt nguồn

**Hiện tượng:** bị giật từ một thiết bị "đã tắt".
**Cách sửa:** chờ đủ thời gian nhà sản xuất quy định, rồi **đo để xác nhận**.

### 🔍 BẪY 6 — Dùng nút NO cho mạch dừng

**Hiện tượng:** dây đứt làm **mất luôn khả năng dừng**, và không ai biết cho tới lúc cần nhấn.
**Cách sửa:** mạch dừng dùng tiếp điểm **NC**, không có ngoại lệ (mục 3.6, Chương 15).

### 🔍 BẪY 7 — Thay rơ-le an toàn bằng rơ-le thường vì "nhìn giống nhau"

**Hiện tượng:** một tiếp điểm hàn dính không còn phát hiện được; chức năng an toàn **âm thầm mất tác
dụng**.
**Cách sửa:** vị trí cần tiếp điểm cưỡng bức thì phải dùng đúng loại (mục 3.5, Chương 47).

### 🔍 BẪY 8 — LOTO chỉ cắt điện, quên khí nén

**Hiện tượng:** xy-lanh chuyển động khi có người đang đưa tay vào máy.
**Cách sửa:** cô lập **mọi** nguồn năng lượng, và **xả** năng lượng tích trữ (mục 3.7, Chương 6).

### 🔍 BẪY 9 — Nhiều người làm việc, một khoá

**Hiện tượng:** người thứ nhất xong việc, gỡ khoá, cấp điện lại — trong khi người thứ hai còn đang
làm.
**Cách sửa:** **mỗi người một khoá** trên cùng cơ cấu cô lập; chỉ khi khoá cuối cùng được gỡ thì mới
cấp điện lại được.

---

## 3.10 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Định luật Ohm | `U = I × R` · công suất `P = U × I` |
| Tiếp xúc kém gây gì | Sụt áp + **nóng** (`P = I²R`), và **nặng dần theo thời gian** |
| Đo 24 V ở đâu | ⭐ **Tại thiết bị**, không tại bộ nguồn |
| Đo áp | **Song song** với tải, thang DC V |
| Đo dòng | **Nối tiếp**, hoặc dùng ampe kìm quanh **một** sợi |
| Sau khi đo dòng | ⚠ **Vặn ngay về thang đo áp** |
| Đo thông mạch / điện trở | ⚠ Chỉ khi mạch **đã mất điện** |
| Cách ly thật giữa hai mạch | **Rơ-le** — cuộn hút và tiếp điểm tách rời |
| Tiếp điểm cưỡng bức để làm gì | Làm cho **hỏng hóc trở nên phát hiện được** |
| Nút dừng dùng tiếp điểm gì | ⭐ **NC** — dây đứt thì máy dừng |
| Mạch rơ-le tự giữ sau mất điện | **Không tự chạy lại** — phải nhấn START |
| Cái gì giết người | ⚠⚠ **Dòng**, ở mức chỉ vài chục mA |
| Quy tắc số một | ⭐ **Cắt điện trước khi làm việc** |
| Sau khi cắt điện | **Kiểm chứng bằng phép đo** — và kiểm cả đồng hồ |
| LOTO thiếu gì thì vô nghĩa | Khoá cá nhân · cô lập **mọi** nguồn · bước kiểm chứng |
| Khi không chắc | ⭐ **Đừng chạm — hỏi** |

---

## 3.11 Tự kiểm

1. Viết định luật Ohm và công thức công suất.
2. ⭐ Vì sao một đầu cốt lỏng gây nóng, và vì sao sự cố này **nặng dần theo thời gian**?
3. Vì sao phải đo điện áp 24 V **tại thiết bị** chứ không tại bộ nguồn?
4. Nêu bốn lý do công nghiệp chọn 24 VDC cho mạch điều khiển. Phát biểu "24 V an toàn" đúng trong
   điều kiện nào?
5. ⭐ Đo áp và đo dòng khác nhau thế nào về cách mắc đồng hồ? Chuyện gì xảy ra nếu để thang đo dòng
   rồi chạm hai que vào hai cực điện áp?
6. Vì sao không được đo thông mạch trên mạch còn điện?
7. Kẹp ampe kìm quanh cả cáp hai dây thì đọc được gì, và vì sao?
8. ⭐ **Tiếp điểm cưỡng bức** giải quyết vấn đề gì mà rơ-le thường không giải quyết được?
9. ⭐ Vì sao nút STOP phải dùng tiếp điểm NC? Trả lời bằng tình huống **dây bị đứt**, cho cả hai
   trường hợp NO và NC.
10. Trong mạch rơ-le tự giữ, thành phần nào giữ cho mạch chạy tiếp sau khi nhả nút START? Nó tương
    ứng với cái gì trong ladder?
11. Vì sao mạch rơ-le tự giữ **không tự chạy lại** sau mất điện, còn chương trình PLC thì có thể? Ai
    quyết định điều đó trong PLC?
12. ⭐ Nêu ba điều làm LOTO thành vô nghĩa nếu thiếu, và giải thích ngắn gọn từng điều.

> Câu 5, 8, 9 và 12 là bốn câu phân loại. Câu 9 là tinh thần của cả chương: **quy ước an toàn trong
> lập trình PLC bắt nguồn từ vật lý của sợi dây, không từ sở thích của người viết phần mềm.**

---

### Chương tiếp theo

Chương 4 — **Cảm biến số & đấu nối**. Bạn đã có điện cơ bản và đã hiểu vì sao tiếp điểm NC quan
trọng. Chương sau là chương gây nhầm nhất của nghề: PNP và NPN, sinking và sourcing, và bảng bốn tổ
hợp mà thiếu nó thì đấu cảm biến chỉ là đoán.

### Nguồn tham khảo chương 3

- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu với mạch điều
  khiển, cách ly nguồn, chức năng dừng, và khởi động lại có chủ ý. *(tiêu chuẩn có bản quyền)*
- IEC 60947-5-1 — *Low-voltage switchgear and controlgear — Control circuit devices*: yêu cầu với
  thiết bị mạch điều khiển, trong đó có **mở cưỡng bức** của tiếp điểm.
- IEC 60947-5-4 và các tài liệu liên quan tới **tiếp điểm dẫn động cưỡng bức** dùng trong rơ-le an
  toàn — nền cho mục 3.5.
- IEC 61140 — *Protection against electric shock*: phân loại điện áp và nguyên tắc bảo vệ chống điện
  giật — nền cho mục 3.3 và 3.7.
- **Quy định an toàn điện và quy trình LOTO của cơ sở nơi bạn làm việc** — đây mới là văn bản bạn phải
  tuân theo; chương này chỉ giải thích logic đằng sau nó.

> ⚠⚠ **Nhắc lại giới hạn.** Nội dung chương này là **định hướng để hiểu và để đặt câu hỏi**, không
> phải hướng dẫn thao tác trên thiết bị mang điện. Việc phân loại điện áp, xác định điều kiện làm
> việc an toàn, và cấp phép làm việc trên hệ thống điện phải do **người có thẩm quyền** thực hiện
> theo quy định hiện hành tại nơi bạn ở. Các con số về ngưỡng dòng nguy hiểm nêu ở mục 3.7 là **mức
> độ lớn để bạn hình dung**, không phải giá trị dùng để thiết kế — giá trị thiết kế phải lấy từ tiêu
> chuẩn gốc.
