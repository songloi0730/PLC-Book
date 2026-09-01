# Chương 36 — Động cơ & biến tần

> **Lát cắt máy mẫu:** 3 — thêm analog (áp suất, nhiệt độ, cường độ UV) và trục gantry XY+Z servo.

---

## 36.1 Bài toán: chuyền chạy chậm dần, không ai biết

Chuyền của DP-01 chạy bằng động cơ ba pha qua biến tần. PLC đặt tốc độ 70 % bằng tín hiệu analog
`AO_ConvSpeed` (Chương 32).

Ba tháng sau, chu kỳ máy dài ra khoảng 8 %. Sản lượng giảm nhẹ, nhưng đủ để lệch kế hoạch.

Đi tìm nguyên nhân: người ta kiểm chương trình, kiểm cảm biến, kiểm khí nén. Mọi thứ bình thường.

Cuối cùng phát hiện: **biến tần đang giới hạn dòng**. Băng tải bị kẹt nhẹ do bụi keo tích tụ ở con
lăn, mô-men cần tăng, và biến tần tự giảm tốc để không quá dòng — đúng như nó được thiết kế.

Biến tần **biết** điều này. Nó có bit trạng thái báo đang giới hạn dòng, có giá trị dòng thực tế, có
tốc độ thực tế. Nhưng PLC chỉ nối với nó bằng **một sợi dây analog một chiều** — ra lệnh mà không đọc
lại gì.

Chương này về động cơ và biến tần từ góc nhìn người lập trình PLC. Và câu hỏi trung tâm không phải
"đặt tốc độ thế nào", mà **"làm sao biết nó có chạy đúng không"**.

---

## 36.2 Động cơ ba pha — đủ dùng

Động cơ **không đồng bộ ba pha** *(three-phase induction motor)* là cơ cấu chấp hành quay phổ biến
nhất trong công nghiệp: bền, rẻ, gần như không cần bảo trì.

Bốn thông số trên nhãn động cơ mà bạn cần đọc được:

| Thông số | Nghĩa | Vì sao người lập trình cần |
|---|---|---|
| **Công suất** (kW) | Công suất cơ trục | Chọn biến tần — phải đủ hoặc lớn hơn |
| **Điện áp và cách đấu** (sao / tam giác) | ⚠ Đấu sai thì cháy hoặc thiếu lực | Đưa vào tài liệu; kiểm khi chạy thử (Chương 52) |
| **Dòng định mức** (A) | Dòng ở tải định mức | ⭐ Ngưỡng để đặt bảo vệ và để **giám sát tải** |
| **Tốc độ định mức** (vòng/phút) | Tốc độ ở tần số danh định | Tính tỉ số truyền và quy đổi ra tốc độ chuyền |

> ⚠ **Tốc độ động cơ tỉ lệ với tần số cấp vào.** Đó là cơ sở của biến tần: đổi tần số thì đổi tốc độ.
> Nhưng ⚠ **mô-men không giữ nguyên trên toàn dải** — xem mục 36.4.

---

## 36.3 DOL hay biến tần

**Khởi động trực tiếp** *(Direct On Line, DOL)* qua contactor: đóng contactor, động cơ chạy tốc độ
định mức. Cắt contactor, động cơ dừng theo quán tính.

| | **DOL qua contactor** | **Biến tần** *(VFD / inverter)* |
|---|---|---|
| Tốc độ | Một tốc độ duy nhất | ⭐ **Đổi được** |
| Khởi động | ⚠ **Dòng khởi động rất lớn** — nhiều lần dòng định mức | ⭐ Êm, dòng có kiểm soát |
| Dừng | Theo quán tính, hoặc phanh cơ | ⭐ Giảm tốc có kiểm soát |
| Đảo chiều | Cần hai contactor + khoá lẫn | ⭐ Một tham số |
| Bảo vệ động cơ | Rơ-le nhiệt riêng | ⭐ Tích hợp, nhiều lớp |
| ⭐ Chẩn đoán | Gần như không có | ⭐ **Dòng, tốc độ, mô-men, mã lỗi** |
| Giá | Rẻ | Cao hơn |
| ⚠ Nhiễu | Ít | **Nguồn nhiễu mạnh** — mục 36.7 |

> **Chọn DOL khi:** một tốc độ là đủ, khởi động không thường xuyên, tải nhẹ, và ngân sách chặt.
> Ví dụ: quạt hút, bơm khí, động cơ chạy liên tục cả ca.
>
> **Chọn biến tần khi:** cần đổi tốc độ, cần khởi động/dừng êm, đảo chiều thường xuyên, hoặc ⭐ **cần
> chẩn đoán**.

> ⭐ **Hàng "chẩn đoán" đáng giá hơn người ta tưởng, và nó chính là bài học ở mục 36.1.**
> Biến tần đo dòng động cơ liên tục. Dòng là **chỉ số tải cơ khí** — nó tăng khi cơ cấu kẹt, khi vòng
> bi mòn, khi băng tải căng quá. Đọc dòng về PLC cho bạn một phép đo sức khoẻ cơ khí **miễn phí**, và
> nó phát hiện được thứ mà không cảm biến nào khác trên máy thấy được.

---

## 36.4 ⚠ Biến tần đã tự lo những gì

Đây là mục quan trọng nhất về mặt kiến trúc, và nó nối thẳng với Chương 35 mục 35.12 Bẫy 8.

Biến tần hiện đại **không chỉ đổi tần số**. Nó có sẵn:

| Chức năng | Nghĩa |
|---|---|
| **Vòng điều khiển tốc độ** | Giữ tốc độ ổn định khi tải đổi — ⭐ **đây đã là một vòng kín** |
| **Dốc tăng/giảm tốc** *(ramp)* | Đi từ tốc độ này sang tốc độ kia trong thời gian đặt trước |
| **Giới hạn dòng** | Tự giảm tốc thay vì để quá dòng — ⚠ đúng cỗ máy ở mục 36.1 |
| **Bảo vệ** | Quá dòng, quá áp, thấp áp, quá nhiệt, mất pha, quá tải động cơ |
| **Hãm** | Hãm bằng điện trở xả hoặc hãm DC |

> ⚠⚠ **Đừng viết PID trên PLC để điều khiển tốc độ qua biến tần.**
> Biến tần **đã có vòng tốc độ bên trong**. Thêm một vòng nữa ở PLC là **chồng hai vòng** — chúng
> "đánh nhau", hệ dao động theo cách khó hiểu, và chỉnh vòng ngoài không cải thiện được (Chương 35,
> Bẫy 8).
>
> PLC chỉ nên **đặt điểm đặt tốc độ** và **giám sát kết quả**.
>
> Ngoại lệ hợp lệ: khi bạn điều khiển một đại lượng **khác** tốc độ — ví dụ giữ áp suất bằng cách đổi
> tốc độ bơm. Khi đó vòng PID ở PLC điều khiển **áp suất**, và biến tần vẫn lo tốc độ. Hai vòng
> **lồng nhau có chủ đích**, không chồng lên nhau.

### Bốn tham số tối thiểu phải hiểu

Biến tần có hàng trăm tham số. Bốn cái này quyết định hành vi cơ bản:

| Tham số | Nghĩa | ⚠ Đặt sai thì |
|---|---|---|
| **Tần số nhỏ nhất / lớn nhất** | Dải tốc độ cho phép | Vượt tốc độ cơ khí chịu được; hoặc quá chậm gây quá nhiệt động cơ |
| ⭐ **Thời gian tăng tốc** *(accel ramp)* | Bao lâu để đi từ 0 tới tốc độ đặt | Quá ngắn → quá dòng, biến tần báo lỗi; quá dài → chu kỳ máy dài ra |
| ⭐ **Thời gian giảm tốc** *(decel ramp)* | Bao lâu để dừng | Quá ngắn → **quá áp** (động cơ thành máy phát); quá dài → sản phẩm trượt |
| **Giới hạn dòng / mô-men** | Trần bảo vệ | Quá thấp → máy chạy chậm hơn lệnh mà không rõ lý do (mục 36.1) |

> ⚠ **Thời gian giảm tốc quá ngắn gây lỗi quá áp — hiện tượng phản trực giác.**
> Khi giảm tốc nhanh, động cơ bị tải quay cưỡng bức và **hoạt động như máy phát**, đẩy năng lượng
> ngược vào biến tần. Điện áp một chiều bên trong tăng lên, và biến tần báo lỗi quá áp để tự bảo vệ.
>
> Ba cách xử lý: kéo dài thời gian giảm tốc, lắp **điện trở xả** *(braking resistor)*, hoặc dùng biến
> tần trả năng lượng về lưới.

---

## 36.5 ⭐ Đặt tốc độ: analog hay mạng

Hai cách nối PLC với biến tần, và lựa chọn này quyết định bạn **chẩn đoán được bao nhiêu**.

### So sánh

| | **Analog + I/O số** | **Mạng công nghiệp** |
|---|---|---|
| Đặt tốc độ | 0–10 V hoặc 4–20 mA | Một thanh ghi |
| Lệnh chạy / dừng / đảo chiều | Ngõ ra số riêng cho từng lệnh | Bit trong từ điều khiển |
| ⭐ **Đọc về** | ⚠ Chỉ vài tiếp điểm: "đang chạy", "có lỗi" | ⭐ **Tốc độ thật, dòng, mô-men, mã lỗi cụ thể, giờ chạy** |
| Đi dây | Nhiều sợi | ⭐ Một cáp mạng cho nhiều biến tần |
| Cấu hình | Đơn giản, ai cũng hiểu | Phải cấu hình mạng, cần hiểu bản đồ thanh ghi |
| Chẩn đoán khi hỏng | ⭐ Đo được bằng đồng hồ | Cần công cụ mạng (Chương 40) |
| Khi mất kết nối | Tín hiệu analog vẫn còn — ⚠ xem cảnh báo | ⭐ Phát hiện được ngay |
| Số biến tần nhiều | ⚠ Tốn I/O và dây | ⭐ Thắng rõ ràng |

### Đánh đổi thật

> ⭐ **Analog đơn giản hơn; mạng cho bạn biết chuyện gì đang xảy ra.**
>
> Cỗ máy ở mục 36.1 là hậu quả trực tiếp của việc chọn analog: PLC ra lệnh 70 % và **không có cách nào
> biết** biến tần đang giới hạn dòng. Với kết nối mạng, bit "đang giới hạn dòng" đọc về được, và vấn
> đề lộ ra trong ngày đầu tiên thay vì sau ba tháng.
>
> Ngược lại, khi máy hỏng lúc hai giờ sáng, một tín hiệu analog **đo được bằng đồng hồ vạn năng**
> (Chương 3) — người thợ điện tự kiểm được. Với mạng thì phải có phần mềm và biết dùng.

> 💡 **Phương án trộn, rất phổ biến và thường là lựa chọn tốt nhất:**
> - **Lệnh chạy/dừng bằng ngõ ra số**, đi dây thẳng — đơn giản, đo được, và ⭐ **không phụ thuộc mạng**.
> - **Đặt tốc độ và đọc trạng thái qua mạng** — được đầy đủ dữ liệu chẩn đoán.
>
> Cách này giữ được điểm mạnh của cả hai, và quan trọng hơn: **lệnh dừng không đi qua mạng**.

### ⚠⚠ Mất kết nối và lệnh chạy

> **Câu hỏi phải trả lời cho mọi biến tần: nếu mất kết nối với PLC, biến tần làm gì?**
>
> - **Với tín hiệu analog:** dây tín hiệu đứt → biến tần đọc 0 V → hiểu là "đặt 0 %". Động cơ dừng.
>   Nhưng ⚠ **nếu lệnh chạy vẫn còn** thì biến tần vẫn ở trạng thái chạy, chỉ là tốc độ 0 — và nó
>   **không báo lỗi gì**, vì với nó mọi thứ bình thường (Chương 31, mục 31.4).
> - **Với mạng:** biến tần có tham số quy định hành vi khi mất truyền thông — dừng, giữ tốc độ cuối,
>   hoặc chạy ở tốc độ dự phòng. ⚠ **Giá trị mặc định chưa chắc đúng cho máy của bạn** — phải đặt có
>   chủ đích.
>
> Đây là quyết định thuộc phân tích trạng thái an toàn ở Chương 48, mục 48.2, và nó phải nằm trong
> đặc tả (Chương 23) chứ không phải để mặc định của nhà sản xuất quyết.

---

## 36.6 ⚠⚠ Biến tần và an toàn

Điểm này ngắn nhưng không được bỏ qua.

> ⚠⚠ **NGUY HIỂM — "đặt tốc độ 0" KHÔNG phải dừng an toàn.**
>
> Khi biến tần ở tốc độ 0, động cơ vẫn **được cấp điện** và vẫn có mô-men giữ. Một lỗi trong biến
> tần, một nhiễu trên đường tín hiệu, hoặc một tham số bị đổi có thể làm nó quay lại **bất cứ lúc
> nào**.
>
> Người đưa tay vào máy khi thấy động cơ đứng im là người đang tin vào một trạng thái **không có gì
> bảo đảm**.

Dừng an toàn phải là một trong hai:

| Cách | Nghĩa |
|---|---|
| **Cắt nguồn động lực** qua tiếp điểm của mạch an toàn | Không còn điện thì không quay được |
| ⭐ **Chức năng STO** *(Safe Torque Off)* của biến tần | Mạch chuyên dụng trong biến tần cắt mô-men, **được chứng nhận** cho chức năng an toàn |

> **STO khác "đặt tốc độ 0" ở chỗ nào?**
> STO là **mạch phần cứng riêng biệt**, có hai kênh, được thiết kế và chứng nhận theo tiêu chuẩn an
> toàn chức năng (IEC 61800-5-2). Nó không đi qua bộ vi xử lý điều khiển của biến tần, nên một lỗi
> phần mềm trong biến tần **không vô hiệu hoá được nó**.
>
> ⚠ Nhưng STO **không phải cách ly nguồn** — động cơ vẫn có điện áp trên đầu cực. Với công việc bảo
> trì thì vẫn phải LOTO (Chương 3, mục 3.7).

Chi tiết ở Chương 47, mục 47.8. Đây là hạng mục phải do **người có thẩm quyền** thiết kế.

---

## 36.7 ⚠ Biến tần là nguồn nhiễu

Biến tần tạo ra điện áp dạng xung tần số cao để điều khiển động cơ. Đó là nguyên lý hoạt động của nó,
và cũng là lý do nó là **nguồn nhiễu điện từ mạnh nhất trong tủ**.

| Biện pháp | Vì sao |
|---|---|
| ⭐ **Cáp động cơ có vỏ chống nhiễu**, nối vỏ **cả hai đầu** | ⚠ Đây là **ngoại lệ** của quy tắc ở Chương 31 mục 31.6: với nhiễu tần số cao, nối hai đầu mới chắn hiệu quả |
| **Tách cáp động lực khỏi cáp tín hiệu** | Nguồn nhiễu chính vào tín hiệu analog (Chương 31) |
| **Nối đất biến tần theo hướng dẫn nhà sản xuất** | Đường về của dòng nhiễu tần số cao |
| **Lọc đầu vào** nếu nhà sản xuất yêu cầu | Giảm nhiễu dẫn ngược vào lưới |
| ⚠ **Chiều dài cáp động cơ có giới hạn** | Cáp dài gây phản xạ xung, hại cách điện động cơ; vượt giới hạn thì cần cuộn kháng đầu ra |

> ⚠ **Hàng đầu tiên là chỗ dễ nhầm.**
> Chương 31 mục 31.6 dạy nối vỏ chống nhiễu **một đầu** cho cáp tín hiệu analog — để tránh vòng lặp
> đất. Với **cáp động cơ của biến tần** thì ngược lại: nối **hai đầu**, vì mục tiêu là chắn nhiễu tần
> số cao chứ không phải chống dòng vòng tần số thấp.
>
> Hai quy tắc khác nhau cho hai bài toán khác nhau. **Theo hướng dẫn của nhà sản xuất biến tần** —
> họ đã tính cho sản phẩm của họ.

---

## 36.8 ⭐ Giám sát biến tần — phép đo sức khoẻ miễn phí

Nếu nối qua mạng, bạn đọc về được những thứ mà không cảm biến nào khác trên máy cho:

| Đọc về | Dùng để làm gì |
|---|---|
| ⭐ **Dòng động cơ** | **Chỉ số tải cơ khí** — tăng dần nghĩa là cơ cấu đang nặng dần |
| **Tốc độ thực tế** | So với tốc độ đặt — lệch nghĩa là đang bị giới hạn |
| ⭐ **Bit "đang giới hạn dòng"** | ⚠ Đúng vấn đề ở mục 36.1 |
| **Mã lỗi cụ thể** | "Quá dòng" và "thấp áp" dẫn tới hai hướng kiểm tra khác nhau |
| Giờ chạy, số lần khởi động | Lịch bảo trì theo tình trạng |
| Nhiệt độ tản nhiệt | Cảnh báo môi trường tủ xấu đi |

### Dùng dòng động cơ làm chẩn đoán

```iecst
// Ghi lại dòng chuyền ở tốc độ danh định, khi máy chạy ổn định
IF M_ConvAtSetSpeed AND NOT M_ConvAccel THEN
    ConvCurrentX10 := VfdActualCurrentX10;      // đọc qua mạng
END_IF;

// So với giá trị mốc ghi lúc nghiệm thu (Chương 52)
M_ConvLoadHigh := ConvCurrentX10 > (BaselineCurrentX10 * 130) / 100;   // cao hơn 30 %

// ⚠ Bit này của biến tần là dấu hiệu TRỰC TIẾP của vấn đề ở mục 36.1
M_ConvSpeedLimited := M_VfdCurrentLimiting;
```

> ⭐ **Giá trị mốc phải ghi lúc nghiệm thu, khi máy còn mới và sạch** (Chương 52, mục 52.3). Không có
> mốc thì con số dòng hôm nay chẳng nói lên điều gì — bạn không biết nó bình thường hay đã cao.
>
> Đây là cùng nguyên tắc với việc ghi lại điện áp 24 V lúc chạy thử (Chương 8, mục 8.7): **một phép
> đo chỉ có nghĩa khi có cái để so.**

> 💡 **Cảnh báo tải cao thuộc mức "cảnh báo, vẫn chạy"** (Chương 48, mục 48.6), không phải "cấm chạy".
> Nó cho bạn vài tuần để lên lịch vệ sinh con lăn, thay vòng bi — thay vì một sự cố bất ngờ.

---

## 36.9 Trên máy mẫu DP-01

Chuyền của DP-01 dùng động cơ ba pha qua biến tần.

| Hạng mục | Quyết định | Vì sao |
|---|---|---|
| DOL hay biến tần | **Biến tần** | Cần đổi tốc độ theo mã hàng (`ConvSpeedPct` trong công thức, Chương 29); cần khởi động/dừng êm để board không trượt |
| Đặt tốc độ | `AO_ConvSpeed` **0–10 V** | Dây ngắn, trong tủ (Chương 31, mục 31.4) |
| Lệnh chạy | `DO_ConvRun` **ngõ ra số** | ⭐ Không phụ thuộc mạng; đo được bằng đồng hồ khi chẩn đoán |
| Phản hồi | `DI_VfdReady` **tiếp điểm khô** | Biến tần sẵn sàng, không lỗi |
| ⚠ **Chẩn đoán** | Hiện chỉ có `DI_VfdReady` | ⚠ Xem nhận xét bên dưới |
| Dừng an toàn | **Cắt qua mạch an toàn** hoặc **STO** | Chương 47, mục 47.8 |

> ⚠⚠ **Nhận xét: cấu hình hiện tại của DP-01 chính là cỗ máy ở mục 36.1.**
>
> `DI_VfdReady` chỉ nói "biến tần không lỗi". Nó **không** nói biến tần đang giới hạn dòng, không nói
> tốc độ thật là bao nhiêu, không nói dòng động cơ đang tăng dần.
>
> Với chu kỳ mục tiêu 12 giây/board đã chốt (Phụ lục J §7) và trạm sấy UV đã sát trần, **chuyền chạy
> chậm hơn lệnh 8 % là đủ để lệch kế hoạch sản xuất** — và với cấu hình hiện tại thì không ai phát
> hiện được cho tới khi đối chiếu sản lượng.
>
> **Hướng cải thiện đáng cân nhắc:** thêm kết nối mạng tới biến tần để đọc dòng và bit giới hạn dòng,
> **giữ nguyên** lệnh chạy bằng ngõ ra số — đúng phương án trộn ở mục 36.5. Chi phí: một cổng mạng và
> ít công cấu hình. Được: một phép đo sức khoẻ cơ khí mà máy hiện chưa có.
>
> Đã ghi vào hồ sơ máy mẫu §8 làm hạng mục để bạn quyết.

### Tốc độ chuyền và chu kỳ máy

Từ số liệu đã chốt: board 100 × 80 mm, chu kỳ mục tiêu 12 s/board. Tốc độ chuyền phải đủ để **đưa
board vào và ra trong phần thời gian không dành cho gia công**.

> ⚠ **Đây là chỗ tốc độ chuyền, thời gian gia công và chu kỳ mục tiêu phải khớp nhau.** Nếu tăng tốc
> độ chuyền để bù cho trạm sấy chậm, board có thể trượt khi giảm tốc — nên thời gian giảm tốc
> (mục 36.4) trở thành một tham số ảnh hưởng **chất lượng**, không chỉ ảnh hưởng nhịp.
>
> Chương 55 quay lại bài toán này với số liệu đo thật.

---

## 36.10 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| ⚠ **Bản đồ tham số** | Khác nhau **hoàn toàn** giữa các hãng, và cả giữa các dòng của cùng hãng. Số hiệu tham số của biến tần này **vô nghĩa** với biến tần khác |
| Giao thức mạng | Phần lớn biến tần hỗ trợ nhiều lựa chọn: Modbus RTU/TCP (Chương 39), PROFINET, EtherNet/IP, EtherCAT (Chương 40). ⭐ Chọn theo mạng bạn đang dùng |
| ⭐ Từ điều khiển / từ trạng thái | Khi nối qua mạng, lệnh và trạng thái gói trong **các bit của một từ**. ⚠ Dùng kiểu `WORD`, không dùng `INT` (Chương 11, mục 11.2) |
| Hành vi khi mất truyền thông | ⚠ **Tham số riêng** — mặc định chưa chắc đúng cho máy của bạn (mục 36.5) |
| STO | Có ở phần lớn biến tần công nghiệp hiện đại, nhưng ⚠ **kiểm mã sản phẩm cụ thể** — không phải bản nào cũng có |
| Auto-tune động cơ | Nhiều biến tần tự đo tham số động cơ để điều khiển tốt hơn. ⚠ Chạy khi **động cơ đã lắp vào tải thật** hay chưa lắp — tuỳ hãng, đọc kỹ |
| ⚠ Đơn vị của tham số tốc độ | Có hãng đặt theo **Hz**, có hãng theo **vòng/phút**, có hãng theo **%**. Nhầm đơn vị là chạy sai tốc độ |

> ⚠ **Đừng chép cấu hình biến tần từ máy cũ sang máy mới** nếu khác dòng sản phẩm. Đây là lỗi
> chép–dán tương tự cảnh báo ở Chương 32 mục 32.10, và hậu quả ở đây là **cơ cấu chuyển động sai**.

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

---

## 36.11 Bẫy thường gặp

### 🔍 BẪY 1 — Ra lệnh mà không đọc lại gì

**Hiện tượng:** đúng cỗ máy ở mục 36.1 — máy chạy chậm dần 8 % suốt ba tháng, không ai biết, vì PLC
chỉ có một sợi dây một chiều tới biến tần.
**Cách sửa:** đọc về **tốc độ thật và dòng động cơ**; dùng phương án trộn ở mục 36.5.

### 🔍 BẪY 2 — Viết PID trên PLC để điều khiển tốc độ qua biến tần

**Hiện tượng:** hai vòng chồng nhau, hệ dao động khó hiểu, chỉnh vòng ngoài không cải thiện.
**Cách sửa:** biến tần **đã có vòng tốc độ**. PLC chỉ đặt điểm đặt và giám sát (mục 36.4, Chương 35
Bẫy 8).

### 🔍 BẪY 3 — Thời gian giảm tốc quá ngắn

**Hiện tượng:** biến tần báo **lỗi quá áp** khi dừng — phản trực giác, vì người ta trông đợi lỗi quá
dòng khi tăng tốc chứ không phải khi giảm tốc.
**Cách sửa:** kéo dài thời gian giảm tốc, hoặc lắp điện trở xả (mục 36.4).

### 🔍 BẪY 4 — Coi "tốc độ 0" là dừng an toàn

**Hiện tượng:** ⚠⚠ động cơ đứng im nhưng **vẫn có điện và có mô-men giữ**; người đưa tay vào máy đang
tin vào một trạng thái không có gì bảo đảm.
**Cách sửa:** cắt qua mạch an toàn hoặc dùng **STO** (mục 36.6, Chương 47).

### 🔍 BẪY 5 — Nối vỏ cáp động cơ một đầu

**Hiện tượng:** nhiễu nặng vào tín hiệu analog và mạng, xuất hiện đúng lúc biến tần chạy tải nặng.
**Cách sửa:** ⚠ cáp động cơ nối vỏ **hai đầu** — ngoại lệ của quy tắc ở Chương 31 mục 31.6. Theo
hướng dẫn nhà sản xuất (mục 36.7).

### 🔍 BẪY 6 — Không đặt hành vi khi mất truyền thông

**Hiện tượng:** mất mạng, biến tần **giữ nguyên tốc độ cuối** theo mặc định và chạy tiếp — trong khi
PLC tin rằng đã ra lệnh dừng.
**Cách sửa:** đặt tham số đó **có chủ đích**, theo phân tích ở Chương 48, mục 48.2.

### 🔍 BẪY 7 — Dây analog đứt nhưng lệnh chạy vẫn còn

**Hiện tượng:** biến tần đọc 0 V, chạy ở tốc độ 0, **không báo lỗi gì** — vì với nó mọi thứ bình
thường. PLC tin rằng chuyền đang chạy.
**Cách sửa:** đọc **tốc độ thật** về, và giám sát phản hồi thay vì tin lệnh (mục 36.5, Chương 48).

### 🔍 BẪY 8 — Không ghi giá trị mốc lúc nghiệm thu

**Hiện tượng:** ba tháng sau muốn biết dòng động cơ có cao bất thường không, nhưng **không có gì để
so**.
**Cách sửa:** ghi dòng, tốc độ và các chỉ số cơ bản lúc chạy thử, khi máy còn mới (mục 36.8,
Chương 52).

### 🔍 BẪY 9 — Chép tham số biến tần từ máy khác dòng

**Hiện tượng:** cùng số hiệu tham số nhưng nghĩa khác — cơ cấu chuyển động sai, hoặc bảo vệ bị vô
hiệu hoá.
**Cách sửa:** ⚠ bản đồ tham số khác nhau hoàn toàn giữa các dòng. Cấu hình lại từ tài liệu đúng
(mục 36.10).

### 🔍 BẪY 10 — Nhầm đơn vị tham số tốc độ

**Hiện tượng:** đặt "50" mong 50 % nhưng biến tần hiểu là 50 Hz — chuyền chạy hết tốc độ.
**Cách sửa:** kiểm đơn vị trong tài liệu; và ⭐ **luôn kẹp giá trị trước khi ghi ra** (Chương 32,
mục 32.4).

---

## 36.12 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| DOL đủ khi | Một tốc độ, khởi động thưa, tải nhẹ |
| Biến tần cần khi | Đổi tốc độ · khởi động/dừng êm · đảo chiều · ⭐ **cần chẩn đoán** |
| Biến tần đã tự lo gì | ⭐ **Vòng tốc độ** · dốc tăng/giảm · giới hạn dòng · bảo vệ |
| ⚠ Đừng làm gì | **Viết PID trên PLC điều khiển tốc độ** — chồng vòng |
| Bốn tham số tối thiểu | Tần số min/max · **thời gian tăng tốc** · **thời gian giảm tốc** · giới hạn dòng |
| Giảm tốc quá nhanh gây | ⚠ **Lỗi quá áp** — động cơ thành máy phát |
| Đặt tốc độ analog hay mạng | ⭐ **Trộn**: lệnh chạy bằng ngõ ra số, tốc độ và trạng thái qua mạng |
| Vì sao lệnh chạy nên đi dây | Đơn giản, **đo được**, không phụ thuộc mạng |
| ⚠ Mất kết nối thì biến tần làm gì | **Tham số phải đặt có chủ đích** — mặc định chưa chắc đúng |
| ⚠⚠ "Tốc độ 0" có phải dừng an toàn | ❌ **Không** — động cơ vẫn có điện và mô-men giữ |
| Dừng an toàn là | Cắt qua mạch an toàn, hoặc ⭐ **STO** |
| STO có phải cách ly nguồn | ❌ Không — bảo trì vẫn phải **LOTO** |
| Vỏ cáp động cơ nối mấy đầu | ⚠ **Hai đầu** — ngoại lệ của quy tắc cáp tín hiệu |
| Phép đo sức khoẻ miễn phí | ⭐ **Dòng động cơ** — chỉ số tải cơ khí |
| Điều kiện để dòng có nghĩa | ⭐ **Ghi giá trị mốc lúc nghiệm thu** |
| Cảnh báo tải cao xếp mức | **"Cảnh báo, vẫn chạy"** |
| ⚠ Chép cấu hình biến tần | **Không** — bản đồ tham số khác nhau hoàn toàn |

---

## 36.13 Tự kiểm

1. Nêu bốn thông số trên nhãn động cơ và cho biết người lập trình PLC cần chúng để làm gì.
2. So sánh DOL với biến tần trên năm tiêu chí. Tiêu chí nào hay bị đánh giá thấp nhất?
3. ⭐ Nêu năm chức năng biến tần đã tự lo. Vì sao **không** nên viết PID trên PLC để điều khiển tốc độ?
4. Trường hợp nào thì viết PID trên PLC cùng với biến tần **là hợp lệ**?
5. ⭐ Vì sao **giảm tốc quá nhanh** gây lỗi **quá áp**? Nêu ba cách xử lý.
6. So sánh đặt tốc độ bằng analog với bằng mạng. Phương án trộn là gì và vì sao nó thường tốt nhất?
7. ⭐ Dây analog đặt tốc độ bị đứt nhưng lệnh chạy vẫn còn. Biến tần làm gì, và vì sao nó **không báo
   lỗi**?
8. ⚠ Vì sao "đặt tốc độ 0" **không phải** dừng an toàn? STO khác nó ở điểm nào?
9. STO có thay thế được LOTO không? Vì sao?
10. ⭐ Vỏ cáp động cơ nối mấy đầu, và vì sao điều đó **ngược** với quy tắc cho cáp tín hiệu analog ở
    Chương 31?
11. Vì sao **dòng động cơ** là một phép đo sức khoẻ cơ khí? Điều kiện gì để con số đó có ý nghĩa?
12. ⭐ Cấu hình hiện tại của DP-01 có điểm yếu nào về chẩn đoán? Nêu hướng cải thiện và chi phí của nó.

> Câu 3, 5, 7, 8 và 10 là năm câu phân loại. Câu 7 là tinh thần của cả chương: **thiết bị không báo
> lỗi không có nghĩa là mọi thứ đúng — nó chỉ có nghĩa là thiết bị đó không thấy gì sai theo cái nó
> biết.**

---

### Chương tiếp theo

Chương 37 — **Điều khiển chuyển động servo**. Biến tần cho bạn tốc độ; servo cho bạn **vị trí**.
Chương sau về gantry XY+Z của DP-01: về gốc, biên dạng vận tốc, giới hạn phần mềm và phần cứng — và
vì sao giới hạn phần mềm không bao giờ thay được công tắc giới hạn thật.

### Nguồn tham khảo chương 36

- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu với mạch động lực,
  bảo vệ động cơ, chức năng dừng và cách ly nguồn. *(tiêu chuẩn có bản quyền)*
- IEC 61800-5-2 — *Adjustable speed electrical power drive systems — Safety requirements — Functional*:
  định nghĩa **STO** và các chức năng an toàn khác của truyền động — nền cho mục 36.6.
- IEC 61800-3 — *Adjustable speed electrical power drive systems — EMC requirements*: yêu cầu tương
  thích điện từ — nền cho mục 36.7.
- **Tài liệu biến tần** của dòng đang dùng — dùng cho ⚠ **bản đồ tham số**, đơn vị tham số tốc độ,
  hành vi khi mất truyền thông, giới hạn chiều dài cáp động cơ, và hướng dẫn nối đất/chống nhiễu.
  Đây là tài liệu **không thay thế được bằng tài liệu của dòng khác**.
- **Nhãn và catalogue động cơ** — dùng cho công suất, cách đấu, dòng và tốc độ định mức.
- Bảng I/O, bảng công thức và số liệu đã chốt của DP-01 — Phụ lục J.

> ⚡ Các nhận định về chức năng có sẵn của biến tần ở mục 36.4 mô tả **biến tần công nghiệp hiện đại
> nói chung**. Biến tần giá rẻ hoặc đời cũ có thể thiếu một số chức năng — đặc biệt là **STO** và các
> tuỳ chọn mạng. ⚠ Kiểm mã sản phẩm cụ thể trước khi thiết kế dựa vào chúng (Chương 13, tiêu chí 3).
>
> ⚠ **Về mục 36.6:** nội dung ở đây là **định hướng để bạn biết phải hỏi gì**. Việc chọn kiến trúc
> dừng an toàn cho một cỗ máy cụ thể — cắt nguồn hay dùng STO, mức hiệu năng cần đạt, cách đấu và
> kiểm chứng — phải do **người có thẩm quyền** thực hiện theo Chương 47.
