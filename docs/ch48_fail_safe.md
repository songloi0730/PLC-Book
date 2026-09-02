# Chương 48 — Fail-safe & thiết kế phòng sự cố

> **Lát cắt máy mẫu:** 5 — máy đầy đủ, gồm cả mạch an toàn, analog, chuyển động và mạng.

---

> ⚠ Chương này bàn về **thiết kế phòng sự cố ở tầng điều khiển**. Nó bổ sung cho Chương 47, **không
> thay thế**: những gì thuộc về chức năng an toàn vẫn phải do lớp an toàn độc lập thực hiện và do
> người có thẩm quyền kiểm định. Chương này **đang chờ chuyên gia rà soát** trước khi phát hành.

---

## 48.1 Bài toán: cỗ máy hỏng sản phẩm suốt ba tuần mà không ai biết

Khách hàng của một nhà máy điện tử báo tỷ lệ hỏng ngoài thị trường tăng đột biến. Truy ngược lô hàng,
tất cả đều đi qua một cỗ máy.

Máy đó chạy hoàn hảo. Không báo động nào trong ba tuần. Sản lượng đúng. Mọi board đều qua kiểm và được
đánh dấu OK.

Nguyên nhân: **bộ khử tĩnh điện** *(ionizer)* đã hỏng từ ba tuần trước. Board đi qua máy tích điện,
và tĩnh điện phóng qua linh kiện nhạy cảm. Phần lớn board hỏng **tiềm ẩn** — vẫn hoạt động lúc kiểm
tra, hỏng sau vài tháng ở tay người dùng (Chương 7).

Máy không hề nói dối. Nó chỉ **không được thiết kế để biết**. Không ai đưa tín hiệu tình trạng của
ionizer vào PLC. Với chương trình, ionizer không tồn tại.

Đây là loại lỗi tệ nhất trong sản xuất: **hỏng hóc không có triệu chứng tại chỗ**. Chương này là cách
thiết kế để những thứ như vậy **buộc phải lộ ra**.

---

## 48.2 Trạng thái an toàn — quyết định cho từng ngõ ra

Câu hỏi phải hỏi cho **mọi** ngõ ra, không sót cái nào:

> **Khi mất năng lượng, cơ cấu này về đâu — và trạng thái đó có an toàn không?**

"Mất năng lượng" gồm ba tình huống khác nhau, và **chúng không giống nhau**:

| Tình huống | Cái gì mất | Cơ cấu hành xử thế nào |
|---|---|---|
| Mất điện điều khiển | Lệnh từ PLC mất | Van về vị trí lò xo |
| Mất khí nén | Áp lực mất | Xy-lanh mất lực giữ, trôi theo tải hoặc đứng im do ma sát |
| Đứt dây tín hiệu | Chỉ một lệnh mất | Chỉ cơ cấu đó về vị trí lò xo, các cơ cấu khác vẫn hoạt động |

Tình huống thứ ba hay bị bỏ sót và là tình huống **nguy hiểm nhất**, vì nó tạo ra một tổ hợp trạng
thái mà không ai từng nghĩ tới: một cơ cấu về vị trí nghỉ trong khi các cơ cấu khác vẫn ở vị trí làm
việc.

### Chọn trạng thái an toàn — không có đáp án chung

Người mới thường nghĩ "mất điện thì mọi thứ nhả ra là an toàn nhất". **Sai trong nhiều trường hợp.**

Ví dụ trực tiếp từ DP-01 — van kẹp board:

| Lựa chọn | Mất khí thì | Hậu quả |
|---|---|---|
| Van **lò xo về nhả kẹp** | Kẹp nhả, board tự do | Board rơi xuống chuyền không kiểm soát; nếu chuyền còn quán tính thì board trôi và va chạm (Chương 28) |
| Van **giữ nguyên trạng thái** *(kiểu duy trì)* | Kẹp **vẫn giữ** board | ✅ Board đứng yên, xử lý được có kiểm soát khi khôi phục |

Với DP-01, **giữ kẹp là lựa chọn an toàn hơn** — và đó là quyết định thiết kế đã ghi trong SF6 ở
Chương 47.

Nhưng đảo ngược tình huống thì đáp án đảo ngược theo:

| Cơ cấu | Trạng thái an toàn khi mất năng lượng | Vì sao |
|---|---|---|
| Kẹp giữ **board mạch** (nhẹ, nằm ngang) | **Giữ** | Nhả ra thì board trôi, va chạm |
| Kẹp giữ **chi tiết nặng treo trên cao** | ⚠ Phải phân tích riêng | Giữ thì tốt — nhưng nếu áp tụt dần, chi tiết rơi **muộn**, lúc người đã vào máy |
| Cơ cấu **kẹp quanh tay người có thể chạm tới** | **Nhả** | Người phải thoát ra được |
| Trục **đứng có tải treo** | **Phanh cơ khí giữ** | Mất mô-men là rơi (Chương 47, STO) |
| Van cấp **vật liệu nguy hiểm** | **Đóng** | Không được để chảy tiếp |

> ⚠ **NGUY HIỂM**
> Không có quy tắc chung "mất điện thì nhả" hay "mất điện thì giữ". Câu trả lời đúng phụ thuộc vào
> **mối nguy cụ thể**, và nó là kết quả của đánh giá rủi ro (Chương 47), không phải của thói quen.
>
> Đặc biệt cảnh giác với **"giữ" bằng áp suất còn lại**: khí trong ống xả dần, và cơ cấu nhả ra **sau
> vài phút** — đúng lúc người đã tin là máy đã dừng và đang thò tay vào. Nếu chọn "giữ", phải giữ
> bằng cơ cấu **không phụ thuộc năng lượng** (chốt cơ khí, van một chiều có khoá), không phải bằng
> khí còn sót.

### Bảng trạng thái an toàn của DP-01

Bảng này phải có trong bộ đặc tả (Chương 23), cột cuối của bảng I/O.

| Ngõ ra | Mất điện điều khiển | Mất khí | Đứt dây tín hiệu | Đánh giá |
|---|---|---|---|---|
| `DO_Clamp1Vlv` | Giữ kẹp | Giữ kẹp (van duy trì + chốt) | Giữ kẹp | ✅ An toàn — board không trôi |
| `DO_Stop1Vlv` | Chặn **nâng** (lò xo về vị trí chặn) | Chặn nâng | Chặn nâng | ✅ An toàn — board không đi qua trạm |
| `DO_ConvRun` | Chuyền dừng | — | Chuyền dừng | ✅ An toàn |
| `DO_UvLamp` | Đèn tắt | — | Đèn tắt | ✅ An toàn |
| `DO_ShutterVlv` | Cửa chắn **đóng** | Cửa chắn đóng | Cửa chắn đóng | ✅ An toàn — che nguồn UV |
| `DO_DispVlv` | Van tra keo đóng | Van đóng | Van đóng | ✅ Không nhỏ keo bừa |
| `DO_IonizerEn` | Ionizer tắt | — | Ionizer tắt | ⚠ **An toàn cho người, nhưng hỏng sản phẩm âm thầm** — xem mục 48.6 |

Dòng cuối là dòng đáng chú ý nhất: trạng thái "an toàn" theo nghĩa không gây thương tích, nhưng **gây
thiệt hại vô hình**. Đó chính là sự cố ở mục 48.1.

---

## 48.3 Đứt dây phải dẫn tới trạng thái an toàn

Nguyên tắc đã gặp ở Chương 4 và Chương 15, giờ phát biểu ở dạng tổng quát:

> **Mọi hỏng hóc dự đoán được phải dẫn tới trạng thái an toàn, không phải trạng thái nguy hiểm.**

Áp cho tín hiệu vào:

| Loại tín hiệu | Tiếp điểm vật lý | Vì sao |
|---|---|---|
| Mất nó là **phải dừng** (Dừng, cửa, áp suất, phản hồi mạch an toàn) | **NC** | Đứt dây → bit 0 → dừng |
| Mất nó chỉ làm **sai sản phẩm** | Tuỳ, thường NO | Xử lý bằng timeout và báo lỗi |

Áp cho tín hiệu analog — đây là chỗ Chương 31 đã chuẩn bị:

> Vòng dòng **4–20 mA** cho phép phân biệt "giá trị bằng 0" với "đứt dây": giá trị hợp lệ nhỏ nhất là
> 4 mA, nên **dưới 3,6 mA nghĩa là đứt dây hoặc hỏng**, không phải "áp suất bằng 0".
>
> Tín hiệu **0–10 V không có tính chất này** — đứt dây cho 0 V, và 0 V cũng là một giá trị hợp lệ.
> Đây là lý do 4–20 mA được ưu tiên cho tín hiệu quan trọng.

Chương trình phải **dùng** tính chất đó, không chỉ có nó:

```iecst
// Phát hiện ngoài dải → không tin giá trị, báo lỗi
IF AI_AirPress_mA < 3.6 OR AI_AirPress_mA > 20.5 THEN
    M_AirPressFault := TRUE;
    AirPress_bar    := AirPress_Fallback;   // giá trị thay thế đã định trước
ELSE
    AirPress_bar    := Scale(AI_AirPress_mA);
END_IF;
```

> ⚠ **NGUY HIỂM**
> Giá trị thay thế `AirPress_Fallback` phải là giá trị **an toàn**, không phải giá trị "hợp lý". Với
> áp suất khí, an toàn nghĩa là **coi như không đủ khí** — để máy dừng — chứ không phải lấy giá trị
> đo được lần cuối. Lấy giá trị cuối là để máy chạy tiếp với một con số không còn thật.

---

## 48.4 Giám sát phản hồi thay vì tin lệnh

Đây là nguyên tắc trung tâm, và nó đã xuất hiện ở nhiều chương trước dưới các dạng khác nhau. Ở đây
nó được phát biểu đầy đủ.

> **Lệnh không phải là kết quả. Mọi lệnh tác động vật lý phải được xác nhận bằng một tín hiệu độc lập,
> kèm thời hạn.**

Ba lớp của nguyên tắc:

| Lớp | Sai | Đúng |
|---|---|---|
| **Cơ cấu** | Ra lệnh kẹp rồi chuyển bước | Ra lệnh kẹp → **chờ reed xác nhận** → timeout báo lỗi (Chương 26) |
| **Thiết bị phụ trợ** | Bật ionizer rồi coi như nó chạy | Bật → **đọc tín hiệu tình trạng** từ chính thiết bị |
| **Hệ thống khác** | Gửi lệnh sang máy bên rồi đi tiếp | Gửi → **chờ xác nhận** → timeout (mục 48.5) |

### Vì sao timer không thay được phản hồi

Đã nêu ở Chương 17 và 26. Nhắc lại ở đây vì đây là chương phát biểu nguyên tắc:

Một timer trả lời câu hỏi *"đã trôi qua bao nhiêu thời gian?"*. Nó **không** trả lời *"cơ cấu đã tới
đích chưa?"*. Hai câu hỏi đó trùng nhau khi mọi thứ bình thường, và **tách nhau đúng lúc có sự cố** —
tức là đúng lúc bạn cần câu trả lời đúng.

### Phản hồi phải độc lập

Một chi tiết dễ bỏ qua: tín hiệu xác nhận phải **độc lập với lệnh**, không được suy ra từ lệnh.

```iecst
// ✗ SAI — "phản hồi" chỉ là chính cái lệnh
M_Clamp1Confirmed := DO_Clamp1Vlv;

// ✗ SAI — suy từ cảm biến đối diện (Chương 28, Bẫy 1)
M_Clamp1Confirmed := NOT DI_Clamp1Dn;

// ✓ ĐÚNG — cảm biến đích, độc lập với lệnh
M_Clamp1Confirmed := DI_Clamp1Up;
```

Dòng đầu nghe vô lý khi viết ra như vậy, nhưng nó xuất hiện thường xuyên dưới dạng ẩn: chương trình
dùng chính biến lệnh làm điều kiện cho bước sau.

---

## 48.5 Nhịp tim và watchdog giữa các hệ

Chương 10 nói về watchdog **bên trong CPU**. Ở máy có nhiều thành phần, cần thêm một lớp giám sát nữa:
làm sao biết **thành phần bên kia còn sống**?

Vấn đề: nếu màn hình vận hành treo, hoặc mạng đứt, thì PLC **không nhận được lệnh mới** — nhưng nó
cũng không nhận được thông báo nào về việc đó. Với PLC, "không có lệnh mới" và "đối tác đã chết" trông
giống hệt nhau.

### Cơ chế nhịp tim

**Nhịp tim** *(heartbeat)* giải quyết bằng cách biến sự im lặng thành thông tin:

```iecst
// Bên A: đảo bit đều đặn, ví dụ mỗi 500 ms
IF T_Heartbeat.Q THEN
    Hb_ToB := NOT Hb_ToB;
END_IF;

// Bên B: giám sát bit đó có đổi không
IF Hb_FromA <> Hb_FromA_Prev THEN
    T_HbTimeout(IN := FALSE);         // có nhịp → đặt lại đồng hồ
    Hb_FromA_Prev := Hb_FromA;
END_IF;
T_HbTimeout(IN := TRUE, PT := T#2S);

IF T_HbTimeout.Q THEN
    M_PartnerLost := TRUE;            // bên A đã im quá lâu
END_IF;
```

Điểm mấu chốt: bit phải **đổi trạng thái**, không phải giữ mức 1. Một bit kẹt ở 1 vì đối tác treo
trông giống hệt một bit đang được cập nhật thành 1.

### Ba nơi cần nhịp tim ở DP-01

| Cặp | Mất kết nối thì | Máy phải làm gì |
|---|---|---|
| PLC ↔ màn hình vận hành | Người vận hành mất khả năng điều khiển và không thấy trạng thái | Hoàn thành chu trình đang chạy rồi về `Idle`; **không** nhận chu trình mới |
| PLC ↔ máy lân cận trên chuyền | Bắt tay giao/nhận sản phẩm không còn tin được | Không giao board sang; giữ board lại, báo động (Chương 41) |
| PLC ↔ hệ thống quản lý sản xuất | Không hỏi được công thức, không báo được kết quả | ⚠ Quyết định của khách hàng — dừng hay chạy tạm rồi gửi bù (Chương 42) |

> ⚡ **LƯU Ý**
> Phản ứng khi mất nhịp tim **không phải lúc nào cũng là dừng ngay**. Dừng đột ngột giữa chu trình có
> thể tệ hơn hoàn thành nốt chu trình rồi dừng có kiểm soát. Đây là quyết định thiết kế phải ghi trong
> đặc tả (Chương 23), không phải mặc định.

---

## 48.6 Lỗi mà máy không tự phát hiện được

Quay lại sự cố ở mục 48.1. Đây là loại lỗi cần một cách nghĩ riêng.

### Ba loại hỏng hóc theo mức độ dễ phát hiện

| Loại | Ví dụ | Máy tự biết không |
|---|---|---|
| **Lộ ngay** | Xy-lanh không tới đích, mất khí, mất mạng | ✅ Có — timeout, cảm biến, nhịp tim |
| **Lộ muộn** | Cơ cấu chậm dần, cảm biến trôi | ⚠ Chỉ khi có giám sát **xu hướng** (Chương 51) |
| **⭐ Không bao giờ lộ** | Ionizer hỏng, quạt hút yếu, nhiệt độ sai mà không đo | ❌ **Không** — trừ khi được thiết kế để biết |

Loại thứ ba là loại phải xử lý ở giai đoạn **thiết kế**, vì sau khi máy đã lắp thì thường phải thêm
phần cứng.

### Câu hỏi phải hỏi cho mọi thiết bị phụ trợ

> **Nếu thiết bị này hỏng, máy có biết không? Nếu không — làm sao để nó biết?**

Áp cho DP-01:

| Thiết bị phụ trợ | Hỏng thì hậu quả | Máy tự biết? | Cách làm cho máy biết |
|---|---|---|---|
| **Ionizer** | Board tích điện → hỏng tiềm ẩn, **vô hình** | ❌ Không | Đưa tín hiệu tình trạng của ionizer vào một ngõ vào; coi nó là **điều kiện cho phép chạy** |
| **Quạt hút buồng UV** | Khí thải tích tụ | ❌ Không | Cảm biến lưu lượng hoặc áp suất chênh, đưa vào PLC |
| **Đèn UV yếu dần** | Keo không cứng hết → hỏng muộn | ❌ Không | Cảm biến cường độ UV, giám sát ngưỡng tối thiểu (Chương 33) |
| **Bộ lọc khí bẩn** | Van mòn nhanh, hỏng muộn | ❌ Không | Cảm biến chênh áp qua bộ lọc |
| **Gia nhiệt keo lệch** | Keo sai độ nhớt → chất lượng kém | ⚠ Một phần | Đã có cảm biến nhiệt — nhưng phải **giám sát cả sai lệch**, không chỉ giá trị |

Nguyên tắc rút ra:

> **Mọi thiết bị mà hỏng hóc của nó ảnh hưởng tới chất lượng sản phẩm nhưng không ảnh hưởng tới hoạt
> động của máy, đều phải được giám sát bằng một tín hiệu độc lập.**
>
> Nếu không, bạn đang dựa vào việc con người sẽ phát hiện — và con người không phát hiện được thứ vô hình.

> 💡 **MẸO — cách bán ý tưởng này cho người quyết định ngân sách**
> Thêm một cảm biến chênh áp cho bộ lọc tốn rất ít. So sánh nó với chi phí của **ba tuần sản phẩm hỏng
> ngoài thị trường** — con số đó thường thuyết phục hơn mọi lập luận kỹ thuật. Hãy chuẩn bị con số đó
> khi đề xuất.

### Xử lý khi thiết bị phụ trợ hỏng

Không phải mọi thiết bị phụ trợ hỏng đều phải dừng máy ngay. Ba mức phản ứng:

| Mức | Khi nào | Ví dụ |
|---|---|---|
| **Cấm chạy** | Hỏng làm sản phẩm chắc chắn không đạt | Ionizer hỏng → không cho vào `Running` |
| **Cảnh báo, vẫn chạy** | Suy giảm dần, còn trong dung sai | Đèn UV giảm còn 85 % → báo để lên kế hoạch thay |
| **Ghi nhận** | Không ảnh hưởng ngay | Số giờ chạy của bộ lọc |

### ⭐ Phép thử một dòng cho mọi cảnh báo

Tự phát hiện lỗi chỉ có giá trị nếu người vận hành **làm được gì đó** với thông tin đó. Tiêu chuẩn
quản lý hệ thống cảnh báo *(alarm management)* đặt ra một phép thử rất gọn, và nó là phép thử tốt
nhất bạn có thể mang theo:

> **Mỗi cảnh báo phải ứng với một hành động mà người vận hành cần làm, và phải còn đủ thời gian để
> làm việc đó.** Thiếu một trong hai vế thì nó không phải cảnh báo — nó là thông tin, hãy đưa xuống
> mức ghi nhận.

Áp phép thử này lên danh sách cảnh báo của bạn, và một phần lớn sẽ rớt. Đó là kết quả tốt.

**Lụt cảnh báo** *(alarm flood)* là hiện tượng một sự cố gốc kéo theo hàng chục cảnh báo hệ quả đổ
ra cùng lúc. Người vận hành khi đó không đọc nữa — họ xác nhận hàng loạt cho hết màn hình. Cảnh báo
quan trọng nhất chìm trong đám đông đúng vào lúc cần nó nhất.

Trên DP-01, mất khí nén là ví dụ điển hình: một sự cố gốc, nhưng nếu không thiết kế thì sẽ nổ ra
"chặn 1 không lên", "chặn 2 không lên", "kẹp không giữ", "quá thời gian bước 4"… Cách xử lý:

- **Cảnh báo gốc phải chặn cảnh báo hệ quả.** Khi `AI_AirPress` dưới ngưỡng, các timeout cơ cấu
  khí nén bị **ức chế** *(suppressed)*, không phát ra.
- **Ức chế phải có điều kiện rõ ràng và tự gỡ**, không phải tắt vĩnh viễn. Ức chế tuỳ tiện là cách
  người ta vô hiệu hoá hệ cảnh báo mà vẫn tưởng nó đang chạy.
- **Ghi lại cảnh báo bị ức chế vào nhật ký**, kể cả khi không hiển thị. Lúc điều tra sự cố, thứ tự
  các sự kiện mới là dữ liệu quý.

> ⚡ **LƯU Ý**
> Cảnh báo là **thứ có vòng đời**: xác định → thiết kế → vận hành → theo dõi → sửa hoặc bỏ. Danh sách
> cảnh báo được thêm vào suốt ba năm mà chưa bao giờ bị rà lại là danh sách đã hỏng. Chương 44 nói kỹ
> phần thiết kế và trình bày cảnh báo trên màn hình vận hành.

---

## 48.7 Bẫy thường gặp

### 🔍 BẪY 1 — Mặc định "mất điện thì nhả ra là an toàn"

Đã mổ xẻ ở mục 48.2. Đây là bẫy nguy hiểm vì nó nghe **hợp lý** và đúng trong một số trường hợp — nên
người ta áp nó cho mọi trường hợp mà không phân tích.

### 🔍 BẪY 2 — "Giữ" bằng năng lượng còn sót

Chọn "giữ kẹp khi mất khí", nhưng giữ bằng chính khí còn trong ống. Khí xả dần qua rò rỉ, và sau vài
phút kẹp nhả — **đúng lúc người đã tin máy đã dừng hẳn và đang thò tay vào**.

Nếu chọn "giữ", phải giữ bằng cơ cấu **không phụ thuộc năng lượng**.

⭐ Với khí nén, cơ cấu đó là **van một chiều điều khiển** hoặc **khoá cần**, lắp **sát cửa xy-lanh**
(Chương 6, mục 6.3). ⚠ Van hai cuộn hay van 5/3 vị trí giữa đóng **không phải** cơ cấu giữ tải —
chúng chỉ giữ vị trí con trượt trong van.

### 🔍 BẪY 3 — Giá trị thay thế "hợp lý" thay vì an toàn

Cảm biến analog ngoài dải, chương trình lấy **giá trị đo được lần cuối** làm giá trị thay thế. Máy
chạy tiếp bình thường với một con số không còn liên hệ gì với thực tế.

Giá trị thay thế phải là giá trị **an toàn** — thường là giá trị làm máy dừng.

### 🔍 BẪY 4 — Nhịp tim dùng bit giữ mức thay vì đảo trạng thái

```iecst
// ✗ SAI — bit kẹt ở 1 khi đối tác treo trông giống hệt lúc đang chạy
Hb_ToB := TRUE;
```

Nhịp tim phải **đổi trạng thái đều đặn**. Bên nhận giám sát **sự thay đổi**, không giám sát mức.

### 🔍 BẪY 5 — Xác nhận suy ra từ chính lệnh

Đã nêu ở mục 48.4. Bẫy này ẩn kỹ vì code nhìn có vẻ có kiểm tra — nhưng thứ được kiểm tra là chính
biến lệnh, nên nó **luôn đúng**. Cách phát hiện: với mỗi điều kiện chuyển bước, hỏi *"tín hiệu này đến
từ thế giới thật hay từ chính chương trình?"*

### 🔍 BẪY 6 — Thiết bị phụ trợ không có tín hiệu tình trạng

Bẫy trung tâm của chương. Nó xảy ra vì thiết bị phụ trợ thường được mua và lắp bởi người khác, ở giai
đoạn khác, và **không ai đặt câu hỏi ở mục 48.6**.

**Cách phòng:** đưa câu hỏi đó vào biểu mẫu đặc tả (Chương 23) như một mục bắt buộc, áp cho **mọi**
thiết bị trong danh mục vật tư — kể cả những thứ không nối vào PLC.

### 🔍 BẪY 7 — Báo động cho mọi thứ

Ngược lại với Bẫy 6, và cũng có hại: đưa mọi tín hiệu tình trạng vào và cho mỗi cái một báo động dừng
máy. Kết quả là máy dừng liên tục vì những chuyện nhỏ, người vận hành **học cách bỏ qua báo động** —
và rồi bỏ qua cả báo động thật.

Ba mức phản ứng ở cuối mục 48.6 tồn tại để tránh chuyện này. Chương 44 nói kỹ về phân cấp báo động.

---

## 48.8 Bảng chốt — thiết kế phòng sự cố

| # | Việc | Xong khi |
|---|---|---|
| 1 | Với **mọi ngõ ra**, xác định trạng thái an toàn cho **ba tình huống** (mất điện · mất khí · đứt dây) | Bảng đầy đủ, không dòng nào để trống |
| 2 | Kiểm mọi lựa chọn "giữ" có được **giữ bằng cơ cấu không phụ thuộc năng lượng** không | Có |
| 3 | Với **mọi tín hiệu vào**, phân loại an toàn/quy trình và chọn kiểu tiếp điểm | Tín hiệu an toàn dùng NC |
| 4 | Với **mọi tín hiệu analog quan trọng**, có phát hiện ngoài dải và **giá trị thay thế an toàn** | Có |
| 5 | Với **mọi lệnh tác động vật lý**, có **phản hồi độc lập** + timeout | Không có bước nào chuyển tiếp bằng timer |
| 6 | Với **mọi liên kết tới hệ khác**, có **nhịp tim đảo trạng thái** + phản ứng đã định nghĩa | Có, và phản ứng ghi trong đặc tả |
| 7 | Với **mọi thiết bị phụ trợ**, trả lời câu hỏi *"hỏng thì máy có biết không?"* | Mọi thiết bị ảnh hưởng chất lượng đều có tín hiệu tình trạng |
| 8 | Phân **ba mức phản ứng** (cấm chạy · cảnh báo · ghi nhận) cho từng tình trạng | Không phải mọi thứ đều dừng máy |
| 9 | **Thử tạo lỗi cố ý** cho từng mục trên | Chương 50 và 52 |

---

## 48.9 Tự kiểm

1. Ba tình huống "mất năng lượng" khác nhau ở điểm nào? **Tình huống nào hay bị bỏ sót nhất** và vì sao
   nó nguy hiểm?
2. Vì sao "mất điện thì nhả ra" **không** phải quy tắc chung? Cho hai ví dụ có đáp án ngược nhau.
3. Bạn chọn "giữ kẹp khi mất khí". **Điều kiện bắt buộc** để lựa chọn đó thật sự an toàn là gì?
4. Vì sao tín hiệu 4–20 mA phân biệt được "giá trị 0" với "đứt dây", còn 0–10 V thì không?
5. Cảm biến áp suất ngoài dải. Giá trị thay thế nên chọn thế nào — và vì sao "lấy giá trị đo lần cuối"
   là sai?
6. Phát biểu nguyên tắc **giám sát phản hồi thay vì tin lệnh**. Vì sao tín hiệu xác nhận phải **độc
   lập với lệnh**?
7. Vì sao nhịp tim phải **đảo trạng thái** chứ không giữ mức 1?
8. Kể lại sự cố ionizer ở mục 48.1. **Câu hỏi nào** ở giai đoạn thiết kế đã có thể ngăn nó?
9. Nêu **ba mức phản ứng** khi thiết bị phụ trợ hỏng, và cho một ví dụ mỗi mức ở DP-01.
10. Vì sao "báo động cho mọi thứ" cũng nguy hiểm không kém "không báo động gì"?

Câu 3, 6 và 8 là ba câu phân loại. Câu 3 kiểm tra bạn không dừng ở lựa chọn mà đi tới điều kiện của
lựa chọn; câu 6 là nguyên tắc xuyên suốt cả cuốn sách; câu 8 kiểm tra bạn có phản xạ về **hỏng hóc
vô hình** — thứ đặc trưng của sản xuất điện tử.

---

### Chương tiếp theo

**Chương 49 — Lắp đặt, đấu tủ & chống nhiễu.** Thiết kế đã phòng sự cố. Nhưng một phần lớn sự cố thật
không đến từ thiết kế mà từ **cách lắp đặt** — và chúng biểu hiện dưới dạng khó chịu nhất: lỗi ngẫu
nhiên không tái hiện được.

---

### Nguồn tham khảo chương 48

- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: nguyên tắc hỏng hóc phải dẫn
  tới trạng thái an toàn; yêu cầu với mạch dừng. *(tiêu chuẩn có bản quyền)*
- ISO 12100 — *Safety of machinery — General principles for design*: phân tích mối nguy làm nền cho
  việc chọn trạng thái an toàn ở mục 48.2.
- IEC 61131-2 — *Programmable controllers, Part 2*: đặc tính tín hiệu vào/ra và phát hiện ngoài dải.
- IEC 62682 — *Management of alarm systems for the process industries*: vòng đời cảnh báo, yêu cầu
  mỗi cảnh báo phải kèm hành động ứng phó, và cách xử lý lụt cảnh báo (mục 48.6). Đây là bản quốc tế
  tương ứng của tiêu chuẩn ANSI/ISA-18.2; sách dùng số hiệu IEC.
- Bảng I/O, danh sách chức năng an toàn và danh mục thiết bị phụ trợ của DP-01 — Phụ lục J.

> ⚠ Bảng trạng thái an toàn ở mục 48.2 là **kết quả phân tích cho máy mẫu DP-01**, không phải bảng áp
> dụng chung. Máy của bạn có mối nguy khác thì đáp án khác — và đáp án đó phải đến từ đánh giá rủi ro
> của chính cỗ máy đó.
