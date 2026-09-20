
# Phụ lục I — Bài tập: 5 mức, 50 bài

> **Đọc sách không làm bạn lập trình được. Làm bài tập thì có.**
>
> 50 bài, chia 5 mức theo độ khó. Mỗi bài ghi rõ ⭐ **khái niệm được rèn** — vì mục đích không phải
> làm xong bài, mà là **nắm được khái niệm đó**.

---

## I.0 ⭐⭐ Quy tắc bắt buộc cho mọi bài

| # | Quy tắc | Vì sao |
|---|---|---|
| 1 | ⭐⭐ **VIẾT BẢNG I/O TRƯỚC KHI VẼ RUNG ĐẦU TIÊN** | ⭐ Đây là thói quen quan trọng nhất của cả cuốn sách (Chương 23, 57) |
| 2 | ⭐ **Viết ra: "chạy đúng nghĩa là gì?"** trước khi viết chương trình | Không có tiêu chí thì không biết lúc nào xong |
| 3 | ⭐ **Nghĩ tình huống xấu**: mất điện giữa chừng, nhấn nút hai lần, cảm biến hỏng | Chương 57 mục 57.8 |
| 4 | Chú thích giải thích **vì sao**, không phải **cái gì** | Chương 30 mục 30.4 |
| 5 | ⭐ Chạy thử **cả trường hợp sai**, không chỉ trường hợp đúng | Chương 50 |

> ⭐⭐ **Quy tắc 1 nghe thừa với bài "đèn giao thông" — và đó chính là lý do phải làm.**
>
> Thói quen hình thành ở bài dễ. Nếu bạn bỏ qua bảng I/O ở 20 bài đầu, bạn sẽ bỏ qua nó ở dự án thật
> — lúc mà nó đáng giá nhất.

> ⚠ **Về lời giải.** Khoảng hai phần ba số bài có gợi ý lời giải trong mục **I.6**; phần còn lại
> **cố ý không có** — ⭐ vì tới lúc đó bạn phải tự đứng được.
>
> Đọc gợi ý **sau khi đã thử ít nhất 30 phút**. Đọc trước thì bài tập mất tác dụng.

---

## I.1 Mức 1 — Logic cơ bản (12 bài)

⭐ **Cần trước:** Chương 4, 9, 15. **Rèn:** tư duy logic, NO/NC, tự giữ, khoá liên động.

| # | Bài | ⭐ Khái niệm được rèn | Giải |
|---|---|---|---|
| **1.1** | **Mạch tự giữ cơ bản.** Nút Start bật động cơ, nút Stop tắt. Nhả tay khỏi Start thì động cơ vẫn chạy. | Tự giữ *(latch)* | ✅ |
| **1.2** | **AND / OR / NOT.** Đèn sáng khi: (cảm biến A **và** B) **hoặc** (C **và không** D). | Tổ hợp logic cơ bản | ✅ |
| **1.3** | ⭐⭐ **NO vs NC khi đứt dây.** Làm bài 1.1 hai lần: một lần nút Stop dùng tiếp điểm NO, một lần dùng NC. Với mỗi bản, mô phỏng **đứt dây nút Stop** và ghi lại máy làm gì. | ⭐⭐ **Hỏng theo hướng an toàn** — bài quan trọng nhất mức 1 | ✅ |
| **1.4** | **Khoá chéo.** Động cơ quay thuận và quay nghịch. ⚠ **Không bao giờ được bật cả hai cùng lúc**, kể cả khi nhấn cả hai nút. | Khoá chéo *(mutual interlock)* | ✅ |
| **1.5** | **Biểu quyết 2/3.** Ba cảm biến. Đầu ra bật khi **ít nhất hai** cảm biến tác động. | Logic dư thừa | ✅ |
| **1.6** | **SET / RESET.** Bài 1.1 viết lại bằng cuộn dây Set/Reset. So sánh với bản tự giữ: khác nhau ở đâu khi CPU khởi động lại? | Set/Reset vs tự giữ | ✅ |
| **1.7** | **Bắt cạnh lên.** Mỗi lần nhấn nút, đầu ra **đảo trạng thái** (nhấn bật, nhấn nữa tắt). | ⭐ Bắt cạnh — nếu không bắt cạnh, đầu ra nhấp nháy mỗi vòng quét | ✅ |
| **1.8** | **Mạch lật hai nút.** Nút A bật, nút B tắt. Nếu nhấn cả hai cùng lúc thì **tắt thắng**. | Ưu tiên trong flip-flop | ✅ |
| **1.9** | **Báo động có xác nhận.** Cảm biến lỗi → đèn nháy + còi. Nhấn Ack → còi tắt, ⭐ **đèn chuyển sang sáng liên tục** cho tới khi hết lỗi. | ⭐ Ba trạng thái báo động (Ch.44) | ✅ |
| **1.10** | ⭐ **Chuỗi cho phép.** Máy chỉ chạy khi đủ 5 điều kiện. Khi thiếu, ⭐ **phải chỉ ra điều kiện nào đang thiếu**, không chỉ "chưa sẵn sàng". | ⭐⭐ Chuỗi cho phép — thứ tiết kiệm hàng giờ khi máy không khởi động | ✅ |
| **1.11** | **Kiểm đèn.** Nhấn nút Test → mọi đèn và còi bật 2 giây rồi về trạng thái thật. | ⭐ Vì sao cần: đèn báo lỗi bị cháy = lỗi vô hình | ✅ |
| **1.12** | **Ưu tiên dừng.** Ba nút Start ở ba vị trí, hai nút Stop. Bất kỳ nút Stop nào cũng dừng được. | ⚠ Stop luôn thắng Start | — |

> ⭐⭐ **Bài 1.3 là bài phân loại của mức này.** Nếu bạn hiểu được vì sao nút Stop phải là NC, bạn đã
> nắm được nguyên tắc quan trọng nhất của lập trình máy: ⭐ **thiết bị hỏng theo hướng nào?**

---

## I.2 Mức 2 — Bộ định thời & bộ đếm (12 bài)

⭐ **Cần trước:** Chương 11, 12. **Rèn:** TON/TOF/TP, bộ đếm, và ⚠ **biết khi nào KHÔNG dùng timer**.

| # | Bài | ⭐ Khái niệm được rèn | Giải |
|---|---|---|---|
| **2.1** | **Khởi động trễ.** Nhấn Start → còi kêu 3 giây → rồi băng tải mới chạy. | TON; ⭐ và vì sao có cảnh báo trước khi chạy | ✅ |
| **2.2** | **Quạt chạy dư.** Tắt lò → quạt làm mát **chạy thêm 5 phút** rồi mới tắt. | TOF | ✅ |
| **2.3** | **Mạch nháy.** Đèn nháy chu kỳ 1 s bật / 1 s tắt, dùng **hai TON**. | Ghép hai bộ định thời | ✅ |
| **2.4** | ⚠ **Sao–tam giác.** Đổi nối sao sang tam giác sau 5 giây, ⚠ **có khoảng chết 100 ms** giữa hai lần đóng. | ⚠ **Khoảng chết bắt buộc** — thiếu nó là ngắn mạch | ✅ |
| **2.5** | **Kéo dài xung.** Cảm biến cho xung rất ngắn (20 ms). Tạo tín hiệu giữ 1 giây để PLC và HMI kịp thấy. | TP | ✅ |
| **2.6** | **Đếm mẻ.** Đếm đủ 12 sản phẩm → dừng chuyền, bật đèn, chờ Reset. | CTU | ✅ |
| **2.7** | **Đếm lên–xuống.** Đếm số sản phẩm đang nằm trong một đoạn chuyền: vào thì +1, ra thì −1. | CTUD; ⭐ và bài toán "còn bao nhiêu trong máy" | ✅ |
| **2.8** | **Đếm phế có ngưỡng.** Đếm sản phẩm lỗi. ⭐ Nếu **3 lỗi liên tiếp** → dừng máy. Một sản phẩm tốt xen vào thì đếm lại từ đầu. | ⭐ "Liên tiếp" khác "tổng cộng" | ✅ |
| **2.9** | **Đồng hồ giờ chạy.** Đếm tổng số giờ động cơ đã chạy, ⚠ **giữ được qua mất điện**. | ⭐ Vùng nhớ giữ được; ⚠ **DINT không phải INT** | ✅ |
| **2.10** | **Watchdog trình tự.** Nếu một bước không xong trong thời gian cho phép → báo lỗi kèm ⭐ **số bước đang kẹt**. | ⭐⭐ Timeout dùng để **báo lỗi**, không phải để chuyển bước | ✅ |
| **2.11** | **Chống rung tiếp điểm.** Nút bấm cơ khí có nhiễu rung. Lọc để một lần nhấn cho đúng một xung. | Debounce | ✅ |
| **2.12** | ⭐ **Đo thời gian chu kỳ.** Đo thời gian giữa hai sản phẩm liên tiếp; lưu ⭐ **ba giá trị: gần nhất, trung bình, lớn nhất**. | ⭐⭐ Nền của Chương 55 — dữ liệu gần như miễn phí | ✅ |

> ⭐⭐ **Bài 2.10 và 2.12 là hai bài đáng giá nhất mức này, và cả hai đều về cùng một ý:** bộ định thời
> dùng để **biết khi có gì đó không ổn**, không phải để **giả định mọi thứ ổn**.

---

## I.3 Mức 3 — Tuần tự & trạng thái (10 bài)

⭐ **Cần trước:** Chương 21, 25, 26. **Rèn:** trình tự, máy trạng thái, chuyển chế độ.

| # | Bài | ⭐ Khái niệm được rèn | Giải |
|---|---|---|---|
| **3.1** | **Đèn giao thông.** Một ngã tư hai chiều, có đèn vàng. | Trình tự cơ bản theo thời gian | ✅ |
| **3.2** | **Nút bộ hành có nhớ.** Thêm nút cho người đi bộ: nhấn lúc nào cũng được, ⭐ **hệ thống nhớ và phục vụ ở chu kỳ tiếp theo**. | ⭐ Lưu yêu cầu, không phục vụ ngay | ✅ |
| **3.3** | ⭐⭐ **Cùng bài, hai cách.** Làm bài 3.1 hai lần: (a) chỉ dùng bộ định thời nối tiếp, (b) dùng **thanh ghi bước**. So sánh: cách nào dễ thêm một pha đèn mới? | ⭐⭐ **Vì sao trình tự có cấu trúc thắng chuỗi timer** | ✅ |
| **3.4** | **Trạm trộn.** Mở van A đủ lượng → mở van B đủ lượng → khuấy 30 s → xả. Có Start/Stop/Reset. | Trình tự nhiều bước có điều kiện | ✅ |
| **3.5** | **Cổng bãi xe.** Xe tới → mở cổng → chờ xe qua hẳn → đóng. ⚠ **Không được đóng khi xe còn dưới cổng**. | ⚠ Khoá liên động an toàn trong trình tự | ✅ |
| **3.6** | ⭐ **Báo động first-out.** Năm nguyên nhân đều làm máy dừng. Hiển thị ⭐ **nguyên nhân xảy ra TRƯỚC TIÊN**, không phải cả năm. | ⭐⭐ First-out — thứ phân biệt báo động hữu ích với tràn báo động (Ch.44) | ✅ |
| **3.7** | **Timeout từng bước.** Thêm timeout riêng cho mỗi bước của bài 3.4, mỗi timeout có **mã lỗi riêng**. | Chẩn đoán được từ báo động | ✅ |
| **3.8** | ⭐⭐ **Chuyển Manual ↔ Auto không giật.** Máy đang chạy Auto, chuyển sang Manual rồi quay lại. ⚠ **Cơ cấu không được nhảy vị trí**, trình tự phải biết mình đang ở đâu. | ⭐⭐ Bài khó nhất mức 3 — và là vấn đề thật trên mọi máy | — |
| **3.9** | **Bỏ bước theo công thức.** Trình tự 6 bước; công thức quyết định bước 3 và 5 **có chạy hay không**. | ⭐ Tham số là **dữ liệu**, không phải mã (Ch.32) | — |
| **3.10** | ⭐ **Hai trạm, một chỗ trống.** Hai trạm nối tiếp, không có đệm. Trạm 1 chỉ được nhả sản phẩm khi trạm 2 rỗng. ⚠ **Không được dùng chờ bận**. | ⭐⭐ Pipeline và đồng bộ giữa trạm (Ch.26) | — |

> ⭐⭐ **Bài 3.8 là bài mà rất nhiều máy thật làm sai.** Chuyển chế độ mà cơ cấu nhảy vị trí là nguồn
> của cả hư hỏng lẫn tai nạn. Nếu bạn giải được nó, bạn đã vượt qua phần lớn người cùng trình độ.

---

## I.4 Mức 4 — Analog (9 bài)

⭐ **Cần trước:** Chương 14, 31, 34, 35. **Rèn:** quy đổi, kiểm tra hợp lệ, điều khiển.

| # | Bài | ⭐ Khái niệm được rèn | Giải |
|---|---|---|---|
| **4.1** | **Quy đổi thang.** Module cho giá trị thô 0–27648 ứng với 4–20 mA ứng với 0–10 bar. Viết hàm quy đổi. | ⭐ Quy đổi tuyến tính; ⚠ **thứ tự phép tính để không tràn** | ✅ |
| **4.2** | ⭐⭐ **Phát hiện ngoài dải.** Thêm vào bài 4.1: nếu dòng **< 3,6 mA** → báo **lỗi cảm biến**, dùng giá trị thay thế, ⚠ **không dùng giá trị 0**. | ⭐⭐ Phân biệt "đo được 0" với "hỏng" — bài quan trọng nhất mức 4 | ✅ |
| **4.3** | **Điều khiển có trễ tích luỹ.** Bơm bật khi mức < 20 %, tắt khi mức > 80 %. ⭐ Vì sao không dùng một ngưỡng duy nhất? | ⭐ Hysteresis — chống đóng cắt liên tục | ✅ |
| **4.4** | **PID nhiệt độ.** Điều khiển nhiệt độ một bể gia nhiệt. Chỉnh tham số để không vượt quá 2 °C. | PID cơ bản (Ch.35) | ✅ |
| **4.5** | **Vùng chết.** Thêm vùng chết ±0,5 °C vào bài 4.4. Quan sát: số lần đóng cắt cơ cấu **giảm bao nhiêu**? | ⭐ Đánh đổi giữa độ chính xác và tuổi thọ thiết bị | ✅ |
| **4.6** | ⭐ **Giới hạn tốc độ thay đổi.** Giá trị đặt tốc độ chuyền không được nhảy đột ngột — giới hạn 10 %/giây. | ⭐ Ramp — bảo vệ cơ khí | ✅ |
| **4.7** | ⚠ **Ép kiểu và tràn số.** Tính tổng lưu lượng: cộng giá trị đọc mỗi 100 ms trong 24 giờ. ⚠ **Chọn kiểu dữ liệu sao cho không tràn**, và chứng minh bằng phép tính. | ⚠⚠ Tràn số — lỗi âm thầm nhất (Ch.14) | ✅ |
| **4.8** | **Tích phân lưu lượng.** Từ tín hiệu lưu lượng tức thời, tính tổng thể tích đã chảy qua. | Tích phân rời rạc theo vòng quét | — |
| **4.9** | ⭐ **Dải báo động nhiều mức.** Một giá trị analog có 4 ngưỡng: thấp-thấp, thấp, cao, cao-cao. Mỗi ngưỡng có ⭐ **mức ưu tiên và hành động khác nhau**. | ⭐ Phân cấp báo động (Ch.44) | — |

> ⭐⭐ **Bài 4.2 là bài nên làm kể cả khi bạn thấy nó dễ.** Rất nhiều máy thật xử lý sai chỗ này: cảm
> biến đứt dây cho giá trị 0, chương trình hiểu là "áp suất bằng 0", và ⚠ **máy phản ứng như thể áp
> suất thật sự đã tụt**.

---

## I.5 Mức 5 — Đề bài dự án (7 bài)

⭐ **Cần trước:** toàn bộ sách. **Rèn:** ráp mọi thứ lại, và ⭐ **tự đặt ra yêu cầu còn thiếu**.

⚠ **Khác biệt của mức này: đề bài CỐ Ý thiếu chi tiết.** Một phần công việc là nhận ra thiếu gì và
tự quyết định — rồi ⭐ **ghi lại quyết định đó và lý do**, như Chương 57 yêu cầu.

| # | Bài | ⭐ Trọng tâm | Giải |
|---|---|---|---|
| **5.1** | **Máy rửa xe.** Xe vào → phun nước → xà phòng → chải → xả → sấy → ra. Có chế độ tay, có dừng khẩn cấp, có xử lý khi mất nước. | Trình tự dài + tình huống xấu | ✅ |
| **5.2** | **Qua đường cho người đi bộ.** Mở rộng bài 3.2: hai chiều, có đếm ngược, có chế độ ban đêm nháy vàng. | Nhiều chế độ vận hành | ✅ |
| **5.3** | ⚠ **Nạp silo có khoá liên động.** Nạp vật liệu từ xe bồn vào silo. ⚠ **Không được nạp khi silo đầy, khi van xả đang mở, hoặc khi chưa nối đất xe bồn**. | ⚠ Khoá liên động an toàn nhiều điều kiện | ✅ |
| **5.4** | **Luân phiên bơm chính–dự phòng.** Hai bơm, chạy luân phiên theo giờ chạy để mòn đều. ⭐ Bơm hỏng thì bơm kia gánh và **báo động**. | ⭐ Cân bằng hao mòn + xử lý hỏng hóc | — |
| **5.5** | **Điều hoà theo vùng.** Ba vùng, mỗi vùng có cảm biến và van riêng, dùng chung một nguồn lạnh có công suất giới hạn. | ⭐ Phân bổ tài nguyên có giới hạn | — |
| **5.6** | ⭐ **Thang máy 3 tầng.** Nút gọi ở mỗi tầng và trong cabin. ⭐ **Xử lý nhiều yêu cầu cùng lúc** theo thứ tự hợp lý. ⚠ Cửa không được mở khi đang di chuyển. | ⭐⭐ Bài khó nhất phụ lục — hàng đợi + an toàn + trải nghiệm người dùng | — |
| **5.7** | ⭐⭐ **Dây chuyền chiết rót có trạm loại.** Ba trạm nối tiếp: chiết → đóng nắp → kiểm. Sản phẩm lỗi bị loại ở cuối. ⭐ **Phải theo dõi được sản phẩm nào lỗi ở trạm nào** dù nó đã đi qua ba trạm. | ⭐⭐ **Thanh ghi dịch theo dõi sản phẩm** — bài gần nhất với máy thật (Ch.41) | — |

> ⭐⭐ **Bài 5.7 là bài tổng kết tốt nhất của cả cuốn sách.** Nó cần: trình tự nhiều trạm, pipeline,
> theo dõi sản phẩm, báo động chẩn đoán được, và ⭐ **quyết định phải làm gì khi máy dừng giữa chừng
> với sản phẩm đang nằm ở cả ba trạm** — đúng bài toán của DP-01 (Phụ lục J §J.4).

---

## I.6 Gợi ý lời giải

⚠ **Đọc sau khi đã thử ít nhất 30 phút.** Đây là **gợi ý hướng đi**, không phải mã hoàn chỉnh — vì
viết ra mã là phần bạn phải làm.

### Mức 1

| Bài | Gợi ý |
|---|---|
| 1.1 | `Run := (Start OR Run) AND NOT Stop;` — ⭐ chú ý `NOT Stop` đặt **sau** để Stop luôn thắng |
| 1.3 | ⭐⭐ Với Stop dùng NO: đứt dây → bit luôn 0 → `NOT Stop` luôn đúng → ⚠ **máy không dừng được nữa**. Với NC: đứt dây → bit luôn 0 → máy dừng và **không chạy lại được**. Cái sau là hỏng theo hướng an toàn |
| 1.4 | Mỗi chiều có thêm điều kiện `AND NOT chiều_kia`. ⚠ Khoá trong chương trình **không đủ** — máy thật cần cả khoá cơ khí ở contactor |
| 1.5 | `(A AND B) OR (B AND C) OR (A AND C)` |
| 1.6 | ⭐ Khác nhau khi CPU khởi động lại: Set/Reset trong vùng nhớ giữ được sẽ **nhớ trạng thái cũ**; mạch tự giữ thì không. ⚠ Với máy, "nhớ trạng thái cũ" thường là **sai** (Ch.47 — chống khởi động lại bất ngờ) |
| 1.7 | Bắt cạnh lên rồi `Out := Out XOR Xung;` |
| 1.9 | Ba trạng thái: chưa ack + đang lỗi (nháy) · đã ack + đang lỗi (sáng) · hết lỗi (tắt). ⭐ Bit "đã ack" phải bị xoá khi lỗi tái xuất hiện |
| 1.10 | ⭐ Mỗi điều kiện một bit riêng; hiển thị **bit nào bằng 0**. ⭐⭐ Đừng gộp thành một bit "Ready" duy nhất |
| 1.11 | ⭐ Ưu tiên: chân đèn thật vẫn phải điều khiển được — dùng `SEL` giữa trạng thái thật và chế độ test |

### Mức 2

| Bài | Gợi ý |
|---|---|
| 2.1 | TON với `IN := Start`, băng tải chạy khi `TON.Q` |
| 2.3 | TON1 chạy khi đèn tắt, hết thì bật đèn và khởi TON2; TON2 hết thì tắt đèn. ⭐ Hoặc dùng bộ đếm vòng quét — nhưng ⚠ **cách đó phụ thuộc thời gian quét** (Ch.56) |
| 2.4 | ⚠ Contactor sao mở → TON 100 ms → contactor tam giác đóng. ⭐ Khoảng chết là để hồ quang tắt hẳn; thiếu nó là **ngắn mạch qua hồ quang** |
| 2.8 | Bộ đếm tăng khi lỗi, ⭐ **xoá về 0 khi có sản phẩm tốt**. Đó là điểm khác giữa "liên tiếp" và "tổng cộng" |
| 2.9 | ⚠ Dùng `DINT` trong vùng nhớ giữ được; ⭐ **thử nạp lại chương trình để kiểm bộ đếm có sống sót không** |
| 2.10 | ⭐ Một TON dùng chung, `PT` lấy từ mảng timeout theo số bước; khi `Q` lên → báo lỗi kèm `SoBuoc` |
| 2.12 | Ghi mốc thời gian khi sản phẩm ra; hiệu hai mốc là chu kỳ. ⭐ **Trung bình che mất chu kỳ dài bất thường — vì thế phải lưu cả giá trị lớn nhất** |

### Mức 3

| Bài | Gợi ý |
|---|---|
| 3.1 | Thanh ghi bước + `CASE`; mỗi bước một TON |
| 3.2 | ⭐ Bit "có yêu cầu" được Set khi nhấn, chỉ Reset khi **đã phục vụ xong** |
| 3.3 | ⭐⭐ Với chuỗi timer, thêm một pha nghĩa là **sửa toàn bộ chuỗi**. Với thanh ghi bước, thêm một nhánh `CASE` là xong. Đây là câu trả lời cho "vì sao trình tự có cấu trúc" |
| 3.5 | ⚠ Điều kiện đóng cổng phải là **cảm biến báo xe đã qua hẳn**, không phải timer. Đây là bài 1.3 ở dạng khác |
| 3.6 | ⭐⭐ Khi máy đang chạy và một nguyên nhân xuất hiện: chốt nguyên nhân đó vào một biến **và khoá lại** cho tới khi Reset. Các nguyên nhân xuất hiện sau không ghi đè |
| 3.7 | Mảng `Timeout[]` và mảng `MaLoi[]` theo số bước |

### Mức 4

| Bài | Gợi ý |
|---|---|
| 4.1 | ⭐ Ép sang REAL **trước** khi nhân; xem Phụ lục K.1 và K.6 |
| 4.2 | ⭐⭐ Quy đổi ngược từ ngưỡng 3,6 mA ra giá trị thô, so sánh với giá trị đọc. Giá trị thay thế nên là **giá trị an toàn cho quá trình**, và ⚠ **phải báo động**, không âm thầm thay |
| 4.3 | Hai ngưỡng khác nhau; ⭐ với một ngưỡng duy nhất, bơm sẽ **đóng cắt liên tục** quanh ngưỡng đó |
| 4.5 | ⭐ Đếm số lần đóng cắt trước và sau khi thêm vùng chết — con số này nối thẳng tới tuổi thọ thiết bị (Ch.9, Phụ lục K.3) |
| 4.6 | Mỗi vòng quét, giá trị đặt chỉ được đổi tối đa `TocDoMax × ThoiGianQuet` |
| 4.7 | ⭐ 24 giờ × 3600 s × 10 lần/s = 864 000 mẫu. ⚠ Nhân với giá trị mỗi mẫu → **vượt xa dải INT và có thể vượt DINT**; dùng REAL hoặc LINT, và ⭐ **chứng minh bằng phép nhân trước khi chọn** |

### Mức 5

| Bài | Gợi ý |
|---|---|
| 5.1 | ⭐ Bắt đầu bằng bảng I/O và bảng chuyển trạng thái (Phụ lục C.1, C.4). ⚠ Đừng viết dòng lệnh nào trước khi có hai bảng đó |
| 5.2 | ⭐ Chế độ ban đêm là một **trạng thái riêng**, không phải một cờ rải rác trong logic |
| 5.3 | ⭐⭐ Mỗi điều kiện khoá là một bit riêng, và ⭐ **phải hiển thị được điều kiện nào đang chặn** — bài 1.10 ở quy mô thật |

> ⭐ **Bảy bài không có gợi ý — 1.12, 3.8, 3.9, 3.10, 4.8, 4.9, và cả nhóm 5.4–5.7 — là cố ý.**
>
> Tới đó, việc tự tìm ra cách làm **chính là bài tập**. Nếu bí, hãy quay lại chương liên quan và đọc
> lại mục *Bẫy thường gặp* — câu trả lời thường nằm ở đó dưới dạng một cái bẫy được đặt tên.

---

## I.7 ⭐ Sau khi làm xong

| Việc | Vì sao |
|---|---|
| ⭐⭐ **Chọn 3–5 bài làm tốt nhất, quay video máy mô phỏng chạy** | Chương 58 mục 58.3 — **bằng chứng** thay cho kinh nghiệm |
| ⭐ Viết lại một bài theo dạng **bài toán → giải pháp → kết quả** | ⭐ Dạng bằng chứng thuyết phục nhất |
| Gộp vài bài mức 5 thành **một máy hoàn chỉnh** | Áp danh mục ở Chương 57 |
| ⭐ Đưa cho ai đó xem và **nghe họ hỏi** | Chỗ bạn tưởng đã hiểu sẽ lộ ra |

> ⭐⭐ **Một máy mô phỏng nhỏ nhưng LÀM ĐẦY ĐỦ thuyết phục hơn năm mươi bài làm dở.**
>
> "Đầy đủ" nghĩa là: có chế độ tay và tự động, có về gốc, có báo động **nói được phải làm gì**, có xử
> lý tình huống xấu, và ⭐ **có chú thích giải thích vì sao**. Đó chính là danh mục Chương 57 — ở quy
> mô nhỏ.

---

> ⚠ **Giới hạn.** Các bài tập ở đây dùng để **rèn tư duy lập trình**, chạy trên **mô phỏng hoặc bàn
> thử nghiệm**.
>
> ⚠⚠ Một số đề bài mô tả tình huống có mối nguy thật (sao–tam giác, nạp silo, thang máy, cổng tự
> động). **Lời giải bài tập KHÔNG dùng được cho máy thật** — máy thật cần đánh giá rủi ro riêng, mạch
> an toàn riêng, và thiết kế do **người có thẩm quyền** thực hiện. Xem Chương 6, 47, 48.
