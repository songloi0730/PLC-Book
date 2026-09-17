# Chương 50 — Mô phỏng & kiểm thử trước khi ra hiện trường

> **Lát cắt máy mẫu:** 5 — máy đầy đủ, gồm cả mạch an toàn, analog, chuyển động và mạng.

---

## 50.1 Vì sao tìm lỗi ở bàn rẻ hơn nhiều

Cùng một lỗi logic, chi phí để tìm và sửa nó phụ thuộc rất mạnh vào **thời điểm phát hiện**:

| Phát hiện ở đâu | Bạn có gì | Bạn mất gì |
|---|---|---|
| **Trên bàn, khi mô phỏng** | Thời gian tuỳ ý; sửa và thử lại trong vài giây; không ai chờ | Chỉ thời gian của bạn |
| **Ở xưởng lắp ráp** | Máy có nhưng chưa giao; sửa được nhưng chậm hơn | Thời gian của bạn + tiến độ dự án |
| **Ở nhà máy khách hàng, lúc chạy thử** | Áp lực thời gian; thiếu dụng cụ; khách hàng đứng xem | Trên + uy tín + chi phí đi lại |
| **Sau khi bàn giao, máy đang sản xuất** | Không được dừng máy; sửa trong khung giờ hẹp | Trên + **thiệt hại sản xuất của khách hàng** |

Chênh lệch giữa hàng đầu và hàng cuối không phải vài lần — thường là **hàng chục lần**, và ở hàng cuối
còn có những chi phí không quy ra tiền được.

Chương này là cách **dịch càng nhiều lỗi càng tốt lên hàng đầu tiên**.

> ⚡ **LƯU Ý — điều chương này KHÔNG hứa**
> Mô phỏng không thay được chạy thử trên máy thật. Có những lớp lỗi **chỉ** lộ ra trên máy thật — xem
> mục 50.6. Mục tiêu là loại bỏ hết lỗi logic **trước khi** ra hiện trường, để thời gian ở hiện trường
> dành cho những thứ chỉ làm được ở đó.

---

## 50.2 Ba mức mô phỏng

**Mô phỏng** *(simulation)* ở đây nghĩa là cho chương trình chạy với tín hiệu **giả lập**
*(simulated I/O)* thay cho tín hiệu từ thiết bị thật. Nó khác với **cưỡng bức** *(forcing)* — cưỡng
bức là đè giá trị lên một điểm I/O của máy thật đang có điện, và là thao tác nguy hiểm có quy trình
riêng (Chương 51). Mỗi tình huống đem ra thử gọi là một **ca kiểm thử** *(test case)*.

| Mức | Cần gì | Kiểm được gì | Không kiểm được |
|---|---|---|---|
| **1 — Mô phỏng trong chương trình** | Chỉ phần mềm lập trình | Logic, trình tự, máy trạng thái, xử lý lỗi | Phần cứng, thời gian thật, nhiễu |
| **2 — PLC thật + I/O giả lập** | PLC + hộp công tắc/đèn | Trên + cấu hình phần cứng, thời gian quét thật, cách đấu I/O | Cơ cấu thật, thời gian cơ khí thật |
| **3 — PLC thật + mô phỏng cơ cấu 3D** | Trên + phần mềm mô phỏng | Trên + trình tự với thời gian cơ khí gần thật, va chạm | Nhiễu, dung sai cơ khí, thiết bị hỏng thật |

Với máy cỡ DP-01, **mức 1 và mức 2 là đủ để loại gần hết lỗi logic**. Mức 3 đáng đầu tư khi máy có
nhiều trục phối hợp hoặc khi rủi ro va chạm cao.

---

## 50.3 Mức 1 — mô phỏng trong chính chương trình

Ý tưởng: thêm một lớp mỏng cho phép **thay tín hiệu thật bằng tín hiệu giả**, bật/tắt bằng một cờ.

### Giả lập ngõ vào

```iecst
VAR
    M_SimMode : BOOL;                 // bật chế độ mô phỏng
    Sim_BoardStn1 : BOOL;             // giá trị giả, đặt bằng tay khi mô phỏng
END_VAR

// Lớp chọn nguồn tín hiệu — đặt ở đầu chương trình, trước mọi logic
IF M_SimMode THEN
    X_BoardStn1 := Sim_BoardStn1;     // dùng giá trị giả
ELSE
    X_BoardStn1 := DI_BoardStn1;      // dùng cảm biến thật
END_IF;
```

Từ đó, **toàn bộ chương trình chỉ dùng `X_BoardStn1`**, không dùng `DI_BoardStn1` trực tiếp. Logic
không biết mình đang chạy thật hay giả.

> ⚠⚠ **NGUY HIỂM — cờ mô phỏng là cờ nguy hiểm nhất trong chương trình**
> Nó làm chương trình **tin vào những thứ không có thật**. Nếu máy chạy sản xuất với `M_SimMode = TRUE`,
> nó sẽ vận hành như thể mọi cảm biến đều báo đúng — kể cả cảm biến an toàn.
>
> Bốn biện pháp bắt buộc, làm cả bốn:
> 1. Cờ mô phỏng **không bao giờ giữ qua mất điện** — luôn khởi tạo bằng FALSE.
> 2. Máy **không được vào `Running`** khi cờ đang bật, trừ trên bàn thử không nối cơ cấu.
> 3. Đèn tháp và màn hình hiển thị **rõ ràng và khác biệt** khi đang mô phỏng.
> 4. Cờ này nằm trong **danh mục kiểm bắt buộc trước bàn giao** (Chương 52).
>
> Và tuyệt đối: **tín hiệu an toàn không bao giờ được đưa qua lớp mô phỏng.** `DI_EStopOK`,
> `DI_Door1Closed`, `DI_CurtainOK` phải luôn đọc thẳng từ phần cứng.

### Giả lập thời gian cơ cấu

Cảm biến giả mà lên ngay lập tức thì không kiểm được timeout và không kiểm được trình tự có chờ đúng
không. Thêm độ trễ giả:

```iecst
// Xy-lanh giả: nhận lệnh → sau 800 ms thì "tới đích"
T_SimClamp1(IN := M_Stn1_ClampReq, PT := T#800MS);
Sim_Clamp1Up := T_SimClamp1.Q;

T_SimClamp1R(IN := NOT M_Stn1_ClampReq, PT := T#800MS);
Sim_Clamp1Dn := T_SimClamp1R.Q;
```

Bây giờ trình tự chạy với nhịp gần thật, và bạn kiểm được cả trường hợp **cơ cấu chậm**: chỉ cần đổi
`T#800MS` thành `T#5S` là timeout phải kích.

---

## 50.4 Danh sách ca kiểm thử

Đây là phần quan trọng nhất của chương. Kiểm thử không có danh sách thì bạn chỉ thử những gì bạn nghĩ ra
lúc đó — tức là những gì bạn đã nghĩ tới khi viết code, tức là **những chỗ ít có lỗi nhất**.

### Nhóm A — Luồng chính

| # | Ca kiểm | Kỳ vọng |
|---|---|---|
| A1 | Chu trình đầy đủ, một sản phẩm | Chạy hết, về `Idle` hoặc chờ sản phẩm mới |
| A2 | Chu trình liên tục, nhiều sản phẩm | Pipeline hoạt động; hai trạm chạy song song (Chương 27) |
| A3 | Đổi công thức sản phẩm | Tham số mới có hiệu lực đúng thời điểm |

### Nhóm B — Điều kiện biên

| # | Ca kiểm | Kỳ vọng |
|---|---|---|
| B1 | **Không có sản phẩm nào** trong thời gian dài | Chờ yên; **không** báo lỗi giả (Chương 26) |
| B2 | **Hai sản phẩm vào sát nhau** | Trạm 1 giữ sản phẩm thứ hai lại |
| B3 | **Trạm 2 chậm hơn trạm 1** | Trạm 1 chờ ở bước 50; không nhả sang |
| B4 | **Xả cạn** — dừng cấp sản phẩm mới | Máy chỉ coi là hết việc khi **mọi trạm** đều rỗng |
| B5 | Sản phẩm bị lấy ra bằng tay giữa chu trình | Trình tự phát hiện và báo lỗi, không chạy tiếp mù |

### Nhóm C — Thao tác người vận hành

| # | Ca kiểm | Kỳ vọng |
|---|---|---|
| C1 | Nhấn **Stop ở từng bước** của chu trình | Dừng có kiểm soát; giữ nguyên vị trí; chạy tiếp được |
| C2 | Nhấn **Start khi chưa về gốc** | Bị từ chối, có thông báo rõ |
| C3 | Chuyển **Auto ↔ Manual** giữa chu trình | Chỉ chuyển được ở trạng thái cho phép (Chương 28) |
| C4 | Nhấn **Reset khi nguyên nhân lỗi còn nguyên** | Không xoá được lỗi; không quay vòng `Alarm ↔ Resetting` |
| C5 | Ở Manual, thử **thao tác sai thứ tự** | Liên động chặn lại (Chương 28, mục 28.3) |

### Nhóm D — Tạo lỗi cố ý ⭐

Nhóm này là nhóm phân biệt kiểm thử nghiêm túc với kiểm thử hình thức.

| # | Ca kiểm | Kỳ vọng |
|---|---|---|
| D1 | **Rút từng cảm biến** khi đang chạy | Timeout đúng bước, thông báo nêu rõ bước và tín hiệu chờ |
| D2 | Giả lập **cơ cấu chậm bất thường** (tăng thời gian mô phỏng) | Timeout kích, không "đi tiếp cho qua" |
| D3 | **Mất khí** giữa chu trình | Dừng; trạng thái an toàn đúng bảng ở Chương 48 |
| D4 | **Mất kết nối** màn hình / máy lân cận / hệ thống trên | Phản ứng đúng như đã định nghĩa; nhịp tim phát hiện được |
| D5 | Tín hiệu analog **ngoài dải** | Phát hiện, dùng giá trị thay thế an toàn, báo lỗi |
| D6 | **Đưa cả hai cảm biến của một xy-lanh cùng lên** | Phát hiện tình huống bất khả → báo hỏng cảm biến (Chương 27) |
| D7 | Ép **thời gian quét tăng vọt** | Watchdog kích; ngõ ra về trạng thái đã cấu hình (Chương 10) |
| D8 | **Mất điện đột ngột** rồi cấp lại | Máy không tự chạy; yêu cầu Reset có chủ ý (Chương 47) |

### Nhóm E — Máy trạng thái

Kiểm bằng cách **ép máy vào từng trạng thái** rồi thử mọi lối ra:

| # | Ca kiểm | Kỳ vọng |
|---|---|---|
| E1 | Từng trạng thái → thử **mọi chuyển tiếp có trong bảng** | Chuyển đúng, hành động khi vào đúng |
| E2 | Từng trạng thái → thử các **chuyển tiếp KHÔNG có trong bảng** | Bị từ chối (Chương 25, Bẫy 4) |
| E3 | Gây lỗi **ở từng trạng thái** | Mọi trạng thái đều vào được `Alarm` |
| E4 | Kiểm **đèn tháp** ở từng trạng thái | Suy trực tiếp từ biến trạng thái, không mâu thuẫn |

### Nhóm F — Về gốc

| # | Ca kiểm | Kỳ vọng |
|---|---|---|
| F1–F5 | Về gốc từ **năm tư thế xuất phát** ở Chương 28, Bẫy 2 | Không va chạm ở bất kỳ tư thế nào |
| F6 | Về gốc khi có sản phẩm **ở cả hai trạm** | Xả từ trạm cuối về trạm đầu |
| F7 | Cơ cấu **kẹt** trong lúc về gốc | Timeout, mã lỗi nêu rõ bước |

> ⚠ **NGUY HIỂM — nhóm G không có trong danh sách này**
> Kiểm thử **chức năng an toàn** (E-Stop, cửa, rèm quang, STO) **không được làm bằng mô phỏng**. Chúng
> phải được thử trên máy thật, với thiết bị thật, và do người có thẩm quyền kiểm định (Chương 47).
> Mô phỏng chỉ kiểm được **phản ứng của PLC** với việc mạch an toàn đã tác động — không kiểm được bản
> thân mạch an toàn.

---

## 50.5 Ghi lại kết quả

Kiểm thử không ghi lại thì không có giá trị chứng minh, và không tái lập được.

Mỗi ca kiểm ghi tối thiểu:

| Cột | Nội dung |
|---|---|
| Mã ca | D1, F3… |
| Ngày, người thử | |
| Phiên bản chương trình | ⭐ Quan trọng — kết quả chỉ có giá trị cho đúng phiên bản đó |
| Cách tạo điều kiện | "rút dây `DI_Clamp1Up` tại cầu đấu X2-14" |
| Kết quả thật | "dừng sau 3,1 s; màn hình hiện S1.20…" |
| Đạt / Không đạt | |
| Ghi chú | Nếu không đạt: đã sửa gì, thử lại lúc nào |

Bảng này chính là **bằng chứng nghiệm thu** ở Chương 52 — và nó tiết kiệm rất nhiều tranh cãi về sau.

> 💡 **MẸO**
> Ghi cả những ca **đã thử và không phát hiện vấn đề**. Sáu tháng sau khi có sự cố, câu hỏi đầu tiên
> sẽ là *"lúc nghiệm thu đã thử tình huống này chưa?"* — và bảng này trả lời được.

---

## 50.5b ⭐⭐ Kiểm thử hồi quy — sửa một chỗ, phải thử lại những gì

Mục 50.4 cho một danh sách ca kiểm thử để chạy **lần đầu**. Nhưng phần lớn đời sống của một chương
trình không phải lần đầu — nó là **lần thứ hai mươi**, sau một lần sửa nhỏ lúc máy đang chạy
(Chương 53).

Và đây là câu hỏi không ai trả lời được nếu chưa chuẩn bị trước:

> ⚠⚠ **"Tôi vừa đổi một dòng. Giờ phải thử lại những gì?"**
>
> ⭐ Trả lời *"thử lại hết"* thì không ai làm — vì không có thời gian. ⚠ Trả lời *"chắc không ảnh
> hưởng gì"* thì đó chính là câu nói ngay trước phần lớn sự cố sau bảo trì.

**Kiểm thử hồi quy** *(regression testing)* là việc chạy lại một tập ca kiểm thử **đã từng đạt**, để
chắc rằng thay đổi mới không phá cái cũ.

### ⭐ Ba vòng, chọn theo mức rủi ro của thay đổi

| Vòng | Chạy những gì | Mất bao lâu | Dùng khi |
|---|---|---|---|
| **Tối thiểu** | Nhóm A (luồng chính) + ca đúng chỗ vừa sửa | Vài phút | Sửa thông báo, đổi một hằng số hiển thị |
| ⭐ **Tiêu chuẩn** | Trên + nhóm B (điều kiện biên) + nhóm F (về gốc) | ~nửa giờ | ⭐ **Mặc định** cho mọi thay đổi logic |
| **Đầy đủ** | Toàn bộ A–F | Vài giờ | ⚠ Đổi máy trạng thái, đổi liên động, đổi bất cứ thứ gì liên quan an toàn, hoặc **đổi phiên bản phần mềm/firmware** |

> ⭐⭐ **Chọn vòng nào là quyết định về RỦI RO, nên nó không thuộc về người sửa.** Người vừa sửa luôn
> là người đánh giá thấp nhất ảnh hưởng của thay đổi đó — họ vừa nghĩ về nó, và nó rõ ràng trong đầu
> họ. ⭐ Đây là lý do quy trình thay đổi có kiểm soát ở Chương 53 mục 53.3 yêu cầu **người thứ hai**.

### ⚠ Bốn thay đổi trông vô hại nhưng bắt buộc vòng ĐẦY ĐỦ

| Thay đổi | Vì sao nguy hiểm hơn vẻ ngoài |
|---|---|
| ⚠⚠ **Đổi phiên bản firmware hoặc phần mềm lập trình** | ⭐ Bạn **không đổi một dòng nào**, nhưng nền bên dưới đã đổi: hành vi biên, thời gian quét, cách xử lý tràn số (Chương 19) |
| ⚠ **Thêm một khối vào tác vụ đang chạy** | Thời gian quét dài ra — ảnh hưởng **mọi phép đo thời gian** trong chương trình (Chương 10) |
| ⚠ **Đổi một khối trong thư viện dùng chung** | Chạm vào **mọi cơ cấu** đang dùng khối đó, không chỉ cơ cấu bạn đang nghĩ tới (mục 30.5) |
| ⚠⚠ **Đổi một hằng số dùng nhiều nơi** | Tra chéo trước khi đổi. ⭐ *"Chỉ một con số"* là câu mở đầu quen thuộc của một sự cố |

### ⭐ Điều kiện để việc này khả thi: ca kiểm thử phải **ghi lại được và chạy lại được**

Kiểm thử hồi quy chỉ làm được nếu ca kiểm thử **tồn tại dưới dạng viết ra**, không nằm trong đầu ai.

| Cần có | Vì sao |
|---|---|
| ⭐ **Danh sách ca đánh số** — mục 50.4 và Phụ lục C | Nói *"chạy lại ca B3, B7"* mới có nghĩa |
| ⭐⭐ **Mỗi ca ghi rõ: đặt gì vào, chờ thấy gì** | ⚠ Ca không có kết quả mong đợi thì **không thể trượt** — nên nó không kiểm gì cả |
| **Kết quả lần chạy trước** (mục 50.5) | Để biết ca này **từng đạt**, nếu không thì trượt lần này chưa chắc là hồi quy |
| ⭐ **Cờ mô phỏng còn dùng được** | ⚠ Lớp mô phỏng ở mục 50.3 hay bị bỏ rơi sau khi giao máy — ⭐ **giữ nó sống** thì mỗi lần sửa về sau rẻ đi rất nhiều |

> ⚡ **Hàng cuối là hàng tiết kiệm nhiều thời gian nhất trong cả chương, và cũng là hàng hay bị bỏ
> nhất.** Lớp mô phỏng được viết cho lần chạy thử đầu tiên, rồi bị coi là xong việc. ⭐ Nếu giữ nó —
> và giữ cho nó vẫn đúng khi chương trình đổi — thì ba năm sau, việc thử một thay đổi vẫn làm được
> **trên bàn**, thay vì phải chờ dừng máy (mục 50.1).

---

## 50.6 Giới hạn của mô phỏng

Thành thật về những gì mô phỏng **không** phát hiện được, để bạn không có cảm giác an toàn giả:

| Chỉ lộ ra trên máy thật | Vì sao |
|---|---|
| **Nhiễu điện từ** | Cần biến tần, servo, máy hàn thật đang chạy (Chương 49) |
| **Vòng lặp đất và chênh điện thế** | Cần hệ nối đất thật |
| **Dung sai cơ khí** | Sản phẩm lệch vài mm, gá mòn, rung |
| **Thời gian cơ khí thật** | Xy-lanh thật nhanh/chậm khác giá trị bạn giả lập |
| **Đấu dây sai** | Mô phỏng dùng biến nội, không đi qua dây |
| **Hành vi thiết bị bên thứ ba** | Máy lân cận, đầu đọc mã, hệ thống trên — mỗi cái có nét riêng |
| **Trạng thái ngõ ra khi CPU lỗi** | Phải thử thật (Chương 10, mục 10.5) |
| **Chức năng an toàn** | Bắt buộc thử thật, do người có thẩm quyền |

Vì vậy trình tự đúng là: **mô phỏng để loại hết lỗi logic → ra hiện trường chỉ để xử lý những thứ chỉ
làm được ở đó**. Chương 52.

---

## 50.7 Bẫy thường gặp

### 🔍 BẪY 1 — Chỉ thử luồng chính

Nhóm A trong danh sách là nhóm dễ nhất và ít giá trị nhất. Nếu bạn chỉ thử nhóm A rồi kết luận "chạy
tốt", bạn chưa kiểm thử — bạn mới **trình diễn**.

Tỷ lệ thời gian hợp lý: nhóm A khoảng **một phần năm**, phần còn lại cho các nhóm B–F.

### 🔍 BẪY 2 — Quên tắt cờ mô phỏng

Đã cảnh báo ở mục 50.3. Đây là bẫy có thể gây hậu quả nghiêm trọng nhất trong chương, và nó xảy ra vì
lý do rất tầm thường: hết giờ, về, hôm sau người khác tiếp tục.

Bốn biện pháp ở mục 50.3 tồn tại vì **kỷ luật cá nhân là không đủ**.

### 🔍 BẪY 3 — Mô phỏng cả tín hiệu an toàn

```iecst
// ✗✗ SAI NGHIÊM TRỌNG
IF M_SimMode THEN
    X_EStopOK := TRUE;        // "cho tiện thử"
```

Không bao giờ. Tín hiệu an toàn đọc thẳng từ phần cứng, không đi qua lớp mô phỏng, không có ngoại lệ.

### 🔍 BẪY 4 — Cơ cấu giả phản hồi tức thì

Cảm biến giả lên ngay khi có lệnh thì trình tự chạy qua mọi bước trong một vòng quét. Bạn không kiểm
được timeout, không kiểm được thứ tự, và không phát hiện được lỗi "chuyển bước bằng timer".

Luôn thêm độ trễ giả, và **thử cả trường hợp trễ vượt ngưỡng**.

### 🔍 BẪY 5 — Không ghi phiên bản chương trình

Kết quả kiểm thử của phiên bản 1.3 không nói gì về phiên bản 1.7. Nếu bảng kết quả không ghi phiên bản,
nó vô giá trị ngay khi ai đó sửa một dòng.

### 🔍 BẪY 6 — Coi mô phỏng đạt là máy đạt

Mục 50.6 tồn tại để chống bẫy này. Mô phỏng đạt nghĩa là **logic đúng**, không nghĩa là **máy chạy được**.

---

## 50.8 Bảng chốt

| # | Việc | Xong khi |
|---|---|---|
| 1 | Dựng **lớp chọn nguồn tín hiệu** cho mô phỏng | Chương trình chỉ dùng biến `X_…`, không dùng `DI_…` trực tiếp |
| 2 | **Loại tín hiệu an toàn** khỏi lớp mô phỏng | Đã kiểm từng tín hiệu an toàn |
| 3 | Áp **bốn biện pháp** chống quên cờ mô phỏng | Cả bốn |
| 4 | Thêm **độ trễ giả** cho mọi cơ cấu | Có, và thử được cả trường hợp vượt ngưỡng |
| 5 | Lập **danh sách ca kiểm** nhóm A–F | Có, và nhóm A chiếm không quá một phần năm |
| 6 | Thực hiện và **ghi lại** từng ca | Có phiên bản chương trình trên mỗi dòng |
| 7 | Rà **danh sách giới hạn** ở mục 50.6 | Biết rõ cái gì còn phải thử ở hiện trường |
| 8 | Kiểm **cờ mô phỏng đã tắt** trước khi mang máy đi | Có, nằm trong danh mục bàn giao |

---

## 50.9 Tự kiểm

1. Vì sao cùng một lỗi lại đắt lên hàng chục lần khi phát hiện muộn? Kể **bốn thời điểm** và cái mất
   ở mỗi thời điểm.
2. Nêu **ba mức mô phỏng** và cái mỗi mức **không** kiểm được.
3. Vì sao chương trình phải dùng biến `X_…` thay vì đọc thẳng `DI_…`?
4. Nêu **bốn biện pháp bắt buộc** chống quên cờ mô phỏng. Vì sao kỷ luật cá nhân không đủ?
5. Vì sao **tín hiệu an toàn tuyệt đối không được** đi qua lớp mô phỏng?
6. Cảm biến giả phản hồi tức thì thì **bạn mất khả năng kiểm thử điều gì**?
7. Kể **ba ca kiểm ở nhóm D** (tạo lỗi cố ý) và kỳ vọng của mỗi ca.
8. Vì sao bảng kết quả kiểm thử **phải ghi phiên bản chương trình**?
9. Kể **bốn thứ** chỉ phát hiện được trên máy thật, không phát hiện được bằng mô phỏng.
10. Vì sao kiểm thử chức năng an toàn **không được** làm bằng mô phỏng?

Câu 5 và câu 10 là hai câu về an toàn — nếu chưa trả lời được dứt khoát thì đừng dùng lớp mô phỏng.

---

### Chương tiếp theo

**Chương 51 — Xử lý sự cố.** Kiểm thử tốt đến mấy cũng có lỗi lọt ra hiện trường. Chương 51 là quy
trình chẩn đoán có hệ thống — thứ bạn sẽ dùng nhiều nhất sau khi đi làm.

---

### Nguồn tham khảo chương 50

- IEC 61131-3 — *Programmable controllers, Part 3*: khối `TON` dùng cho mô phỏng độ trễ cơ cấu.
  *(tiêu chuẩn có bản quyền)*
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu kiểm định trang bị
  điện; cơ sở cho ranh giới "không mô phỏng chức năng an toàn" ở mục 50.4.
- Đặc tả trình tự, bảng thời gian bước và bảng trạng thái an toàn của DP-01 — Phụ lục J.
- Biểu mẫu **danh sách ca kiểm thử** và **biên bản kết quả** — Phụ lục C.
- IEC 62381 — *Automation systems in the process industry — FAT, SAT, SIT*: bảng kết quả kiểm thử
  ở mục 50.5 chính là hồ sơ đầu vào cho FAT — xem Chương 52, mục 52.2.

> ⚠ Danh sách ca kiểm ở mục 50.4 là **khung tối thiểu cho máy cỡ DP-01**. Máy của bạn có chức năng khác
> thì có ca kiểm khác. Cách mở rộng tốt nhất: mỗi lần gặp sự cố ở hiện trường, thêm một ca kiểm để lần
> sau bắt được nó ở trên bàn.
