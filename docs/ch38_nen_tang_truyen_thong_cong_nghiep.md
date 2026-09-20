# Chương 38 — Nền tảng truyền thông công nghiệp

> **Lát cắt máy mẫu:** 4 — thêm mạng: mã 2D, MES, SMEMA, màn hình vận hành, và bộ điều khiển nhiệt độ
> keo nối RS-485.

---

## 38.1 Bài toán: hai thiết bị đúng, cáp đúng, không nói chuyện được

PLC của DP-01 cần đọc nhiệt độ từ bộ điều khiển nhiệt độ keo qua RS-485. Cả hai thiết bị đều tốt, cáp
đúng loại, đấu đúng chân A và B.

Không có gì đọc về được. PLC báo timeout, bộ điều khiển không phản hồi.

Sau nửa ngày, tìm ra ba vấn đề cùng lúc:

- **Tốc độ baud** của bộ điều khiển đặt 9600, PLC đặt 19200.
- **Bit chẵn lẻ** một bên là chẵn, một bên là không dùng.
- Cáp dài 15 m, **không có điện trở đầu cuối** ở hai đầu.

Ba thứ này không có cái nào hiển nhiên khi nhìn, và không cái nào báo lỗi cụ thể. Cả ba cho cùng một
triệu chứng: **im lặng**.

Chương này về nền tảng truyền thông nối tiếp — thứ mà mọi giao thức công nghiệp đứng trên. Nếu tầng
này sai, không giao thức nào cứu được.

---

## 38.2 Ba kiểu kết nối

| Kiểu | Cấu trúc | Ví dụ |
|---|---|---|
| **Điểm–điểm** *(point-to-point)* | Hai thiết bị, một đường | RS-232; IO-Link (Chương 12) |
| **Bus** | Nhiều thiết bị **trên một đường chung** | RS-485; Modbus RTU (Chương 39) |
| **Mạng** *(network)* | Nhiều thiết bị, có chuyển mạch, có địa chỉ | Ethernet công nghiệp (Chương 40) |

> ⭐ **Phân biệt "bus" với "mạng" quan trọng khi chẩn đoán.**
> Trên **bus**, mọi thiết bị dùng chung một đôi dây — một thiết bị hỏng làm nhiễu **cả bus**, và một
> đầu dây lỏng làm **mọi thiết bị** mất liên lạc.
> Trên **mạng có chuyển mạch**, mỗi thiết bị có đường riêng tới bộ chuyển mạch — hỏng một cái không
> ảnh hưởng cái khác.
>
> Đây là lý do gỡ lỗi bus khó hơn gỡ lỗi mạng nhiều: **triệu chứng không chỉ đúng thủ phạm**.

---

## 38.3 RS-232, RS-422, RS-485

Ba chuẩn giao diện điện, thường bị gọi chung là "cổng nối tiếp".

| | **RS-232** | **RS-422** | ⭐ **RS-485** |
|---|---|---|---|
| Tín hiệu | **Đơn cực** — so với đất chung | **Vi sai** | ⭐ **Vi sai** |
| Số thiết bị | 2 | 1 phát, nhiều nhận | ⭐ **Nhiều phát, nhiều nhận** |
| Chiều | Hai chiều đồng thời | Một chiều (có bản hai chiều) | ⭐ **Hai chiều luân phiên** *(half-duplex)* |
| Khoảng cách | Ngắn — vài chục mét | Xa | ⭐ **Xa** — khuyến nghị tới **1200 m** (mục 38.3b) |
| Chống nhiễu | ⚠ Kém | Tốt | ⭐ **Tốt** |
| Số dây tín hiệu | 3 trở lên | 4 | ⭐ **2** (cộng dây đất) |
| Vị thế hiện nay | Đang lùi dần | Ít gặp | ⭐ **Phổ biến nhất trong công nghiệp** |

### ⭐ Vì sao tín hiệu vi sai chống nhiễu tốt hơn

Đây là ý tưởng đáng nắm chắc, vì nó lặp lại ở nhiều nơi khác.

**RS-232** truyền mức điện áp **so với đất chung**. Nhiễu cảm ứng vào dây tín hiệu cộng thẳng vào giá
trị đọc được. Và ⚠ nếu điện thế đất ở hai đầu chênh nhau — chuyện rất bình thường trong nhà máy — thì
mức tín hiệu đã sai ngay từ đầu.

**RS-485** truyền trên **hai dây**, và thông tin nằm ở **hiệu điện áp giữa chúng**, không ở giá trị
tuyệt đối:

```text
   Nhiễu cảm ứng vào CẢ HAI dây gần như bằng nhau
        dây A:  2,5 V  +  nhiễu 3 V  =  5,5 V
        dây B:  0,5 V  +  nhiễu 3 V  =  3,5 V
                              hiệu:  2,0 V  ← KHÔNG ĐỔI
```

Vì hai dây đi cạnh nhau (và **xoắn** vào nhau), nhiễu cảm ứng vào chúng gần như bằng nhau — nên nó
**triệt tiêu trong phép trừ**. Đây gọi là **triệt nhiễu đồng pha** *(common-mode rejection)*.

> ⭐ Đây cũng là lý do **đôi dây xoắn** là bắt buộc, không phải tuỳ chọn: xoắn làm hai dây chịu cùng
> một môi trường nhiễu. Dùng hai sợi rời song song thì hiệu quả kém hẳn.
>
> 💡 Cùng nguyên lý này giải thích vì sao vòng dòng 4–20 mA chống nhiễu tốt (Chương 31, mục 31.4) và
> vì sao Ethernet công nghiệp dùng đôi xoắn (Chương 40).

---

## 38.3b ⭐⭐ Khoảng cách và tốc độ đánh đổi với nhau — không con số nào đứng một mình

Câu hỏi hay gặp nhất về RS-485 là *"đi được bao xa?"*. ⚠ Câu hỏi đó **thiếu một nửa**: xa bao nhiêu
**ở tốc độ nào**.

| Con số | Nội dung |
|---|---|
| Khuyến nghị thường trích | ⭐ **1200 m** cho cả RS-422 và RS-485 |
| ⭐⭐ Quan hệ tốc độ–chiều dài | **Tốc độ tối đa tỉ lệ nghịch với chiều dài cáp** |
| ⚠ Nên hiểu 1200 m là | **Một điểm trên đường đánh đổi**, không phải bức tường |

**Ba dữ kiện làm rõ ý này**

| Trường hợp | Kết quả |
|---|---|
| Cáp 30 m *(100 ft)*, ⚠ **không có điện trở đầu cuối** | ~**200 kbps** |
| ⭐ Cùng cáp 30 m, **có** điện trở đầu cuối ở đầu nhận | ⭐ **1 Mbps** — gấp năm lần |
| Cáp **5 km**, cáp chất lượng cao, đi dây cẩn thận | Chạy được ở **1200 bps** |

> ⭐⭐ **Ba dòng trên nói ba điều khác nhau, và cả ba đều đáng nhớ:**
>
> | | |
> |---|---|
> | 1 | ⭐ **Điện trở đầu cuối không phải chi tiết nhỏ** — cùng sợi cáp đó, có nó thì nhanh gấp năm lần (mục 38.5) |
> | 2 | ⭐ **1200 m không phải giới hạn cứng** — hạ tốc độ xuống thì đi xa hơn nhiều |
> | 3 | ⚠ Nhưng cái giá của việc đi xa là **cáp tốt và đi dây cẩn thận**, không phải may mắn |

**Hệ quả khi thiết kế**

> ⭐ **Chọn tốc độ thấp nhất mà chu kỳ máy chấp nhận được.**
>
> Người ta hay đặt baud cao *"cho chắc"*. ⚠ Ngược lại: baud cao **thu hẹp biên an toàn** của mọi thứ
> khác — chiều dài cáp, nhánh rẽ, chất lượng đấu nối, điện trở đầu cuối. Một mạng 9600 bps tha thứ
> cho nhiều sai sót mà mạng 115200 bps thì không.
>
> ⭐ Hãy tính ngược từ nhu cầu: cần đọc bao nhiêu byte, bao lâu một lần (mục 38.8) — rồi chọn baud
> vừa đủ, không chọn baud lớn nhất mà thiết bị hỗ trợ.

> 🔍 **BẪY — "hôm qua chạy được".**
>
> Một mạng đang chạy ở rìa biên an toàn **vẫn chạy được** — cho tới khi có người nối thêm một thiết
> bị, kéo dài thêm mười mét, hay dựng một biến tần bên cạnh. ⚠ Lúc đó lỗi xuất hiện và **không ai
> liên hệ nó với việc baud đang đặt quá cao từ đầu**.
>
> ⭐ Đây cũng là lý do ⚠ **hạ baud xuống mà hết lỗi** là một phép thử chẩn đoán rất mạnh — nó chỉ
> thẳng vào tầng vật lý (mục 38.5, và Chương 51).

*(Đối chiếu: Kuphaldt, *Lessons In Industrial Instrumentation*, §15.6 — khuyến nghị 1200 m, quan hệ
tỉ lệ nghịch tốc độ–chiều dài, thí nghiệm của Texas Instruments về ảnh hưởng của điện trở đầu cuối,
và ghi chú về mạng 5 km chạy ở 1200 bps do Park, Mackay & Wright ghi nhận.)*

---

## 38.4 Bốn tham số phải khớp

Hai thiết bị nói chuyện được chỉ khi **cả bốn tham số này giống hệt nhau**. Lệch một cái là im lặng
hoặc rác.

| Tham số | Là gì | Giá trị hay gặp |
|---|---|---|
| ⭐ **Tốc độ baud** *(baud rate)* | Số bit truyền mỗi giây | 9600, 19200, 38400, 115200 |
| **Số bit dữ liệu** | Bit trong mỗi ký tự | 8 (gần như luôn) |
| ⭐ **Bit chẵn lẻ** *(parity)* | Bit kiểm lỗi đơn giản | Không (N), chẵn (E), lẻ (O) |
| **Bit dừng** *(stop bit)* | Đánh dấu kết thúc ký tự | 1 hoặc 2 |

Thường viết gọn: **`19200, 8, N, 1`** — 19200 baud, 8 bit dữ liệu, không chẵn lẻ, 1 bit dừng.

> ⚠⚠ **Lệch tham số cho hai triệu chứng, và cả hai đều khó chẩn đoán:**
>
> - **Lệch baud, hoặc lệch bit dừng** → thường là **im lặng hoàn toàn**. Bên nhận không dựng lại được
>   ký tự nào.
> - **Lệch chẵn lẻ** → ⚠ **nhận được nhưng báo lỗi khung**, hoặc tệ hơn: nhận được **dữ liệu rác trông
>   như dữ liệu thật**.
>
> Trường hợp thứ hai nguy hiểm hơn. Nó là lý do **luôn kiểm tra tính toàn vẹn ở tầng giao thức**
> (Chương 39, phần CRC), chứ không tin vào bit chẵn lẻ.

> 💡 **Cách chẩn đoán nhanh khi im lặng:** thử đổi baud của PLC qua từng giá trị thông dụng. Nếu ở một
> giá trị nào đó bắt đầu **nhận được rác thay vì im lặng**, bạn đã gần đúng — có thể chỉ còn lệch
> chẵn lẻ hoặc bit dừng.

---

## 38.5 ⭐ Ba thứ của RS-485 mà người ta hay quên

RS-485 là bus, và bus có ba yêu cầu vật lý mà điểm–điểm không có.

### 1. Điện trở đầu cuối

Tín hiệu chạy tới cuối dây sẽ **phản xạ ngược lại** nếu không có gì hấp thụ nó — giống sóng dội lại ở
đầu bịt của một ống. Sóng phản xạ chồng lên tín hiệu gốc và làm hỏng nó.

```text
   ┌─[R]─┬──────────┬──────────┬──────────┬─[R]─┐
        TB1        TB2        TB3        TB4
   ⭐ Điện trở đầu cuối ở HAI ĐẦU của bus, không ở giữa
```

| Điều | Nội dung |
|---|---|
| Đặt ở đâu | ⭐ **Hai đầu vật lý** của bus — không phải ở thiết bị đầu tiên và cuối cùng theo địa chỉ |
| Bao nhiêu cái | **Đúng hai** |
| ⚠ Nhiều quá | Tải nặng, tín hiệu yếu, khoảng cách giảm |
| ⚠ Thiếu | Phản xạ, lỗi ngẫu nhiên — ⭐ **nặng hơn khi baud cao và cáp dài** |

> ⚠ **Triệu chứng đặc trưng của thiếu điện trở đầu cuối: hoạt động ở tốc độ thấp, hỏng ở tốc độ cao.**
> Nếu hạ baud xuống thì chạy được, đó là dấu hiệu rất mạnh của vấn đề tầng vật lý — điện trở đầu cuối
> hoặc chất lượng cáp.

Nhiều thiết bị có điện trở đầu cuối **tích hợp**, bật bằng công tắc gạt hoặc cầu nối. ⚠ Kiểm xem nó
đang bật hay tắt — và **ghi vào bản vẽ**.

### 2. Phân cực

Khi **không thiết bị nào đang phát**, bus ở trạng thái thả nổi. Nhiễu có thể làm bên nhận hiểu nhầm
là có dữ liệu.

**Điện trở phân cực** *(bias / fail-safe biasing)* kéo hai dây về một trạng thái xác định khi bus rỗi.

> ⚠ Nhiều thiết bị có phân cực tích hợp. **Chỉ cần một bộ phân cực trên toàn bus** — nhiều bộ cùng
> bật sẽ làm tải nặng.
>
> Triệu chứng khi thiếu phân cực: **lỗi ngẫu nhiên khi bus rỗi**, thường ở dạng byte rác xuất hiện
> giữa các bản tin.

### 3. Cấu trúc bus, không phải hình sao

```text
   ✓ ĐÚNG — bus, nhánh rẽ NGẮN
   ─┬──────────┬──────────┬──────────┬─
    │          │          │          │   ← nhánh rẽ càng ngắn càng tốt
   TB1        TB2        TB3        TB4

   ✗ SAI — hình sao, nhánh dài
              ┌────────── TB2
   TB1 ───────┼────────── TB3          ⚠ mỗi nhánh là một đường phản xạ
              └────────── TB4
```

> ⚠ **RS-485 là bus, không phải hình sao.** Đấu hình sao tạo ra nhiều đầu dây không có điện trở đầu
> cuối, mỗi đầu là một nguồn phản xạ. Nó có thể "chạy được" ở tốc độ thấp và cáp ngắn — rồi hỏng khi
> ai đó tăng baud hoặc thêm thiết bị.

### Bảng chốt tầng vật lý RS-485

| Hạng mục | Yêu cầu |
|---|---|
| Cáp | ⭐ **Đôi xoắn có vỏ chống nhiễu** |
| Cấu trúc | **Bus**, nhánh rẽ ngắn |
| Điện trở đầu cuối | ⭐ **Đúng hai**, ở hai đầu vật lý |
| Phân cực | **Một bộ** trên toàn bus |
| Vỏ chống nhiễu | Nối đất — ⚠ theo hướng dẫn nhà sản xuất (Chương 31, mục 31.6) |
| Dây đất tín hiệu | ⚠ Nhiều thiết bị cần dây thứ ba nối đất tín hiệu — kiểm datasheet |
| Tách xa cáp động lực | ⭐ Bắt buộc — biến tần là nguồn nhiễu mạnh (Chương 36, mục 36.7) |

---

## 38.6 Chủ–tớ và sản xuất–tiêu thụ

Hai mô hình tổ chức việc ai được nói khi nào.

### Chủ–tớ

**Chủ–tớ** *(master/slave)*: một thiết bị **chủ** hỏi, các thiết bị **tớ** chỉ trả lời khi được hỏi.

```text
   CHỦ ──"TB1, cho tôi nhiệt độ"──► TB1
   TB1 ──"60,3 °C"────────────────► CHỦ
   CHỦ ──"TB2, cho tôi trạng thái"─► TB2
   ...
```

| ✅ Mạnh | ⚠ Yếu |
|---|---|
| Đơn giản, dễ hiểu, dễ gỡ lỗi | Tớ **không tự báo** được — phải chờ chủ hỏi |
| Không bao giờ đụng độ trên bus | ⭐ Thời gian phản hồi phụ thuộc **số thiết bị** và chu kỳ hỏi vòng |
| Chạy trên bus hai dây | Chủ hỏng là cả bus im |

> ⭐ **Hệ quả quan trọng: sự kiện gấp không được báo ngay.**
> Nếu chủ hỏi vòng 10 thiết bị, mỗi lần 50 ms, thì một thiết bị có sự cố phải **chờ tới lượt** — có
> thể nửa giây. Với thông tin trạng thái thì không sao; với việc cần phản ứng nhanh thì đây là vấn
> đề.
>
> ⚠⚠ Và với **tín hiệu an toàn** thì mô hình này hoàn toàn không phù hợp — an toàn cần giao thức
> chuyên dụng và thiết bị được chứng nhận (Chương 47).

Modbus RTU (Chương 39) là ví dụ điển hình của chủ–tớ.

### Sản xuất–tiêu thụ

**Sản xuất–tiêu thụ** *(producer/consumer)*: thiết bị **tự phát** dữ liệu khi có, ai cần thì nhận.

| ✅ Mạnh | ⚠ Yếu |
|---|---|
| ⭐ Sự kiện báo được **ngay** | Phức tạp hơn |
| Nhiều thiết bị nhận cùng một dữ liệu | Cần mạng có khả năng xử lý đụng độ |
| Hiệu quả hơn khi nhiều thiết bị | Gỡ lỗi khó hơn |

Phần lớn mạng Ethernet công nghiệp hiện đại theo mô hình này (Chương 40).

---

## 38.7 Đọc một khung bản tin bằng tay

Kỹ năng đáng có: nhìn một chuỗi byte và **hiểu nó nói gì**. Khi gỡ lỗi truyền thông, đây thường là
cách duy nhất biết ai sai.

### Cấu trúc chung

Gần như mọi giao thức nối tiếp đều có bốn phần:

```text
   ┌─────────┬──────────┬─────────────────┬──────────┐
   │ Địa chỉ │  Chức    │    Dữ liệu      │  Kiểm    │
   │ /Bắt đầu│  năng    │                 │  tra     │
   └─────────┴──────────┴─────────────────┴──────────┘
```

| Phần | Trả lời |
|---|---|
| **Địa chỉ** hoặc ký tự bắt đầu | Bản tin này gửi cho ai / bắt đầu từ đâu |
| **Mã chức năng** | Yêu cầu làm gì — đọc, ghi |
| **Dữ liệu** | Nội dung |
| ⭐ **Kiểm tra** — CRC hoặc tổng kiểm | Bản tin có bị hỏng trên đường không |

### Ví dụ — đọc nhiệt độ từ bộ điều khiển

Bản tin Modbus RTU (Chương 39) hỏi thiết bị địa chỉ 1, đọc 1 thanh ghi từ địa chỉ 0:

```text
   01   03   00 00   00 01   84 0A
   ▲    ▲    ▲       ▲       ▲
   │    │    │       │       └─ CRC — kiểm tra toàn vẹn
   │    │    │       └───────── số lượng thanh ghi: 1
   │    │    └───────────────── địa chỉ bắt đầu: 0
   │    └────────────────────── mã hàm 03: đọc holding register
   └─────────────────────────── địa chỉ thiết bị: 1
```

Trả lời:

```text
   01   03   02   02 5B   xx xx
   ▲    ▲    ▲    ▲       ▲
   │    │    │    │       └─ CRC
   │    │    │    └───────── dữ liệu: 0x025B = 603 → 60,3 °C
   │    │    └────────────── số byte dữ liệu: 2
   │    └─────────────────── mã hàm 03 (khớp yêu cầu)
   └──────────────────────── địa chỉ thiết bị 1 (khớp)
```

> 💡 **Ba điều đọc được ngay từ khung trả lời, và chúng đủ để chẩn đoán phần lớn vấn đề:**
> - Địa chỉ và mã hàm **khớp yêu cầu** → thiết bị hiểu đúng câu hỏi.
> - Số byte hợp lý → khung không bị cắt.
> - Giá trị `603` có nghĩa với đơn vị 0,1 °C → ⚠ **đơn vị phải tra tài liệu**, không đoán (Chương 32).

> ⭐ **Công cụ:** dùng phần mềm giám sát cổng nối tiếp trên máy tính, hoặc bộ phân tích giao thức. Với
> Modbus, một phần mềm **chủ giả lập** cho phép bạn hỏi thiết bị trực tiếp — **tách PLC ra khỏi bài
> toán** (Chương 39, Chương 51).

---

## 38.8 ⚠ Truyền thông trong môi trường vòng quét

Điểm đặc thù của PLC mà người có nền lập trình hay vấp.

> **Truyền thông nối tiếp mất hàng chục tới hàng trăm mili-giây. Vòng quét là vài mili-giây.**

Nên khối truyền thông **không thể trả kết quả ngay** — cùng vấn đề với khối chuyển động ở Chương 37
mục 37.8, và giải bằng cùng một mẫu:

```iecst
// ⭐ Mẫu Execute/Done — giống khối chuyển động
ReadTemp(Execute := TrigReadTemp.Q,      // cạnh lên
         SlaveId := 1,
         StartAddr := 0,
         Quantity := 1,
         Done    => M_ReadDone,
         Busy    => M_ReadBusy,
         Error   => M_ReadError,
         Data    => TempRawBuf);

IF M_ReadDone THEN
    GlueTempX10 := TempRawBuf[0];
    M_TempCommOk := TRUE;
END_IF;
```

⚠ Ba điều bắt buộc:

- ⭐ **Không hỏi ở mỗi vòng quét.** Nhiệt độ đổi chậm — hỏi mỗi 1–2 giây là quá đủ. Hỏi liên tục làm
  nghẽn bus và không được gì thêm (Chương 12, mục 12.6).
- ⭐ **Phải có timeout.** Thiết bị không trả lời thì khối phải bỏ cuộc, không treo mãi.
- ⭐ **Phải xử lý mất truyền thông tường minh** — mục 38.9.

> ⚠ **Đừng gọi nhiều khối truyền thông cùng lúc trên cùng một cổng.** Bus chỉ có một đường; hai yêu
> cầu cùng lúc thì hoặc lỗi, hoặc phải xếp hàng. Nhiều hệ tự xếp hàng, nhưng ⚠ **đừng giả định** —
> tra tài liệu, hoặc tự tuần tự hoá bằng máy trạng thái (Chương 26).

---

## 38.9 ⭐ Mất truyền thông là một trạng thái, không phải một lỗi

Đây là nguyên tắc quan trọng nhất về mặt thiết kế trong chương.

> **Câu hỏi phải trả lời cho mọi kết nối: nếu thiết bị này ngừng trả lời, máy làm gì?**

Sai lầm phổ biến: coi mất truyền thông là "lỗi lạ" và để chương trình dùng **giá trị cuối cùng nhận
được**. Nhưng giá trị đó có thể đã cũ hàng phút, và thực tế đã đổi.

```iecst
// ⭐ Đếm số lần lỗi liên tiếp — một lần lỗi không đủ để kết luận
IF M_ReadError THEN
    CommErrCount := CommErrCount + 1;
ELSIF M_ReadDone THEN
    CommErrCount := 0;                    // thành công thì xoá
END_IF;

// Ba lần liên tiếp mới coi là mất kết nối — chống báo giả do nhiễu lẻ tẻ
M_TempCommFault := CommErrCount >= 3;

// ⚠⚠ Mất kết nối → KHÔNG dùng giá trị cũ cho quyết định
IF M_TempCommFault THEN
    M_TempValid := FALSE;
    M_AnyFault  := TRUE;                  // theo phân tích ở Chương 48
END_IF;

M_CanStart := ... AND M_TempValid AND NOT M_TempCommFault;
```

> ⭐ **Đếm lỗi liên tiếp thay vì phản ứng ngay là kỹ thuật đáng nhớ.**
> Một bản tin lỗi do nhiễu là chuyện bình thường trên bus công nghiệp — giao thức có CRC chính là để
> phát hiện và bỏ qua nó. Báo lỗi ngay ở lần đầu sẽ cho **rất nhiều báo giả**.
>
> Ba lần liên tiếp là quy tắc thực dụng thường dùng; con số đúng phụ thuộc chu kỳ hỏi và mức độ quan
> trọng.

> ⚠⚠ **Bộ điều khiển vẫn làm việc khi mất truyền thông — nhưng bạn không còn biết nó làm gì.**
> Với bộ điều khiển nhiệt độ của DP-01: nó vẫn giữ nhiệt, quá trình vẫn chạy. Nhưng PLC **mù** — không
> biết nhiệt độ, không biết có báo lỗi không, không đặt được điểm đặt khi đổi công thức.
>
> Chạy tiếp trong trạng thái mù là chấp nhận rủi ro chất lượng mà không đo được. Quyết định "chạy
> tiếp hay dừng" thuộc về **đặc tả** (Chương 23), không phải do người lập trình tự quyết
> (Chương 35, mục 35.9).

---

## 38.10 Vì sao serial vẫn sống dai

Ethernet nhanh hơn, dễ hơn, phổ biến hơn. Nhưng RS-485 vẫn có mặt khắp nơi, và sẽ còn lâu.

| Lý do | Giải thích |
|---|---|
| ⭐ **Rẻ** | Chỉ cần hai dây và một mạch thu phát đơn giản |
| **Đủ dùng** | Bộ điều khiển nhiệt độ đổi giá trị mỗi giây — không cần băng thông Ethernet |
| ⭐ **Thiết bị nhỏ không có chỗ cho Ethernet** | Cổng Ethernet tốn chỗ, tốn điện, tốn tiền |
| **Đi xa với hai dây** | Hàng trăm mét không cần bộ chuyển mạch |
| ⭐ **Cơ sở lắp đặt khổng lồ** | Hàng triệu thiết bị đang chạy; không ai thay cái đang hoạt động |
| **Đơn giản để gỡ lỗi** | Không có DHCP, không có VLAN, không có tường lửa — chỉ có bốn tham số |

> 💡 **Gạch đầu dòng cuối đáng suy nghĩ.** Ethernet mạnh hơn nhưng cũng **nhiều thứ có thể sai hơn**.
> Với một liên kết chỉ cần đọc một con số mỗi giây, sự đơn giản của RS-485 là một **ưu điểm thật**,
> không phải hạn chế.

---

## 38.11 Trên máy mẫu DP-01

Theo số liệu đã chốt (Phụ lục J §J.1):

| Liên kết | Giao diện | Vì sao |
|---|---|---|
| **Bộ điều khiển nhiệt độ keo** | ⭐ **RS-485, Modbus RTU** | ⚠ Ghép nối tiếp vẫn thường gặp ở thiết bị loại này — ⭐ nhưng xem Phụ lục J mục J.9; đủ dùng cho dữ liệu đổi chậm |
| Đầu đọc mã 2D | **Ethernet** | Theo thực tế thị trường (Chương 42) |
| Màn hình vận hành | Ethernet | Chương 44 |
| Hệ thống trên (MES) | Ethernet | Chương 42, 45 |
| Servo drive | Ethernet công nghiệp | Chương 37, 40 |
| Máy trước / máy sau | **SMEMA** — tín hiệu số, không phải mạng | Chương 41 |

### Cấu hình liên kết RS-485

| Hạng mục | Giá trị / quyết định |
|---|---|
| Tham số | `19200, 8, E, 1` — ⚠ **phải khớp hai đầu** (mục 38.4) |
| Địa chỉ tớ | 1 |
| Cấu trúc | Điểm–điểm về mặt vật lý (chỉ một thiết bị), nhưng vẫn dùng chuẩn RS-485 |
| ⭐ Điện trở đầu cuối | **Hai cái** — ở PLC và ở bộ điều khiển |
| Phân cực | Một bộ, thường ở phía PLC |
| Cáp | Đôi xoắn có vỏ chống nhiễu, ⚠ **tách xa cáp động cơ chuyền** (Chương 36, mục 36.7) |
| Chu kỳ hỏi | **1 giây** — nhiệt độ đổi chậm |
| Ngưỡng mất kết nối | **3 lần lỗi liên tiếp** |

> ⚠ **Dù chỉ có một thiết bị, vẫn phải có điện trở đầu cuối ở hai đầu.** Đây là yêu cầu của tầng vật
> lý, không phụ thuộc số thiết bị — cáp vẫn có hai đầu, và sóng vẫn phản xạ.

### Dữ liệu trao đổi

| Chiều | Nội dung | Chu kỳ |
|---|---|---|
| **Đọc** | Nhiệt độ thực tế, trạng thái báo động, điểm đặt hiện tại | 1 s |
| **Ghi** | Điểm đặt nhiệt độ theo công thức | ⭐ Chỉ khi đổi công thức — Chương 29 |

> ⚠ **Ghi điểm đặt phải bắt cạnh**, không ghi mỗi vòng quét (Chương 16). Ghi liên tục vào bộ nhớ
> không mất của thiết bị có thể **làm mòn bộ nhớ đó** — nhiều thiết bị có giới hạn số lần ghi.
>
> Đây là chi tiết ít được nói nhưng gây hỏng thiết bị thật: một chương trình ghi điểm đặt mỗi giây
> suốt vài năm sẽ vượt xa giới hạn ghi của thiết bị.

---

## 38.12 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| Cổng nối tiếp có sẵn | ⚠ Nhiều CPU **không có** cổng nối tiếp — phải mua module. Kiểm ở giai đoạn chọn phần cứng (Chương 13, tiêu chí 4) |
| Khối chức năng truyền thông | Mỗi hệ một bộ khối riêng; ⭐ nhưng phần lớn theo mẫu `Execute`/`Done`/`Busy`/`Error` |
| ⚠ Tự xếp hàng yêu cầu | Có hệ tự xếp hàng nhiều yêu cầu trên một cổng, có hệ không. **Đừng giả định** |
| Cấu hình cổng | Trong cấu hình phần cứng hoặc bằng khối lệnh — tuỳ hệ |
| Điện trở đầu cuối tích hợp | ⭐ Nhiều module có, bật bằng công tắc gạt. **Kiểm và ghi vào bản vẽ** |
| Chuẩn đoán tầng vật lý | Một số module có đèn báo phát/nhận — ⭐ rất hữu ích khi gỡ lỗi |
| ⚠ Đánh số chân | RS-485 gọi hai dây là A/B, hoặc D+/D−, hoặc TxD+/TxD−. ⚠ **Quy ước A/B không thống nhất giữa các hãng** — xem bên dưới |

> ⚠⚠ **Quy ước A/B của RS-485 KHÔNG thống nhất.**
> Một số hãng gọi dây dương là A, số khác gọi là B. Đấu ngược thì **không cháy gì**, nhưng **không
> liên lạc được** — và triệu chứng giống hệt lệch tham số.
>
> 💡 **Cách xử lý thực dụng: nếu đã kiểm hết bốn tham số mà vẫn im lặng, thử đảo hai dây.** Mất ba
> mươi giây, và nó là một trong những nguyên nhân phổ biến nhất. Sau khi tìm ra, **ghi vào bản vẽ**
> cách đấu đúng.

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

---

## 38.13 Bẫy thường gặp

### 🔍 BẪY 1 — Bốn tham số không khớp

**Hiện tượng:** im lặng hoàn toàn (lệch baud), hoặc ⚠ **dữ liệu rác trông như thật** (lệch chẵn lẻ).
**Cách sửa:** đối chiếu cả bốn tham số ở **cả hai đầu**; ghi vào tài liệu máy (mục 38.4).

### 🔍 BẪY 2 — Thiếu điện trở đầu cuối

**Hiện tượng:** ⭐ rất đặc trưng — **chạy được ở baud thấp, hỏng ở baud cao**; lỗi ngẫu nhiên tăng theo
chiều dài cáp.
**Cách sửa:** đúng **hai** điện trở, ở **hai đầu vật lý** của bus (mục 38.5).

### 🔍 BẪY 3 — Đấu RS-485 kiểu hình sao

**Hiện tượng:** chạy được lúc ít thiết bị và cáp ngắn, hỏng khi thêm thiết bị hoặc tăng baud.
**Cách sửa:** cấu trúc **bus**, nhánh rẽ ngắn (mục 38.5).

### 🔍 BẪY 4 — Đảo hai dây A/B

**Hiện tượng:** im lặng hoàn toàn, giống hệt lệch tham số — nên rất tốn thời gian.
**Cách sửa:** ⚠ quy ước A/B không thống nhất giữa các hãng. **Thử đảo** sau khi đã kiểm tham số
(mục 38.12).

### 🔍 BẪY 5 — Hỏi ở mỗi vòng quét

**Hiện tượng:** bus nghẽn, thời gian quét biến động, và không được thêm dữ liệu nào có ích.
**Cách sửa:** chu kỳ hỏi khớp tốc độ dữ liệu thật đổi — vài giây cho nhiệt độ (mục 38.8).

### 🔍 BẪY 6 — Không có timeout

**Hiện tượng:** thiết bị mất điện, khối truyền thông **treo mãi**, trình tự đứng.
**Cách sửa:** mọi khối truyền thông phải có timeout (mục 38.8, Chương 17).

### 🔍 BẪY 7 — Dùng giá trị cuối cùng khi mất kết nối

**Hiện tượng:** máy điều khiển theo một con số đã cũ hàng phút; ⚠ triệu chứng là **không có triệu
chứng** cho tới khi sản phẩm hỏng.
**Cách sửa:** ⚠⚠ mất kết nối → **không dùng giá trị cũ**; xử lý tường minh theo đặc tả (mục 38.9).

### 🔍 BẪY 8 — Báo lỗi ngay ở bản tin lỗi đầu tiên

**Hiện tượng:** rất nhiều báo giả; người vận hành học cách bỏ qua cảnh báo truyền thông — và bỏ qua
luôn lần mất kết nối thật (Chương 48, mục 48.6).
**Cách sửa:** **đếm lỗi liên tiếp**, ba lần mới kết luận (mục 38.9).

### 🔍 BẪY 9 — Ghi tham số vào thiết bị ở mỗi vòng quét

**Hiện tượng:** ⚠ **mòn bộ nhớ không mất** của thiết bị sau vài năm — thiết bị hỏng theo cách không
ai nghĩ tới.
**Cách sửa:** ghi **chỉ khi giá trị đổi**, bắt cạnh (mục 38.11, Chương 16).

### 🔍 BẪY 10 — Đi cáp RS-485 cạnh cáp động cơ

**Hiện tượng:** lỗi truyền thông **đúng lúc biến tần chạy tải nặng**; không tái hiện được khi máy
chạy không tải.
**Cách sửa:** tách máng cáp; dùng đôi xoắn có vỏ chống nhiễu (mục 38.5, Chương 36 mục 36.7).

---

## 38.14 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Ba kiểu kết nối | **Điểm–điểm** · **bus** · **mạng** |
| Vì sao gỡ lỗi bus khó hơn | Dùng chung một đường — **triệu chứng không chỉ đúng thủ phạm** |
| Vì sao vi sai chống nhiễu tốt | Nhiễu cộng vào **cả hai dây** rồi **triệt tiêu trong phép trừ** |
| Đôi dây xoắn là | ⭐ **Bắt buộc**, không phải tuỳ chọn |
| Bốn tham số phải khớp | **Baud** · bit dữ liệu · **chẵn lẻ** · bit dừng |
| Lệch baud → | Im lặng |
| Lệch chẵn lẻ → | ⚠ **Dữ liệu rác trông như thật** — nguy hiểm hơn |
| Điện trở đầu cuối | ⭐ **Đúng hai**, ở **hai đầu vật lý** |
| Triệu chứng thiếu điện trở đầu cuối | ⭐ **Chạy ở baud thấp, hỏng ở baud cao** |
| ⭐⭐ "Đi được bao xa" | ⚠ **Câu hỏi thiếu một nửa** — xa bao nhiêu **ở tốc độ nào** |
| Khuyến nghị chiều dài | ⭐ **1200 m**; ⭐ **tốc độ tối đa tỉ lệ nghịch với chiều dài** |
| Cùng một sợi cáp, thêm điện trở đầu cuối | ⭐ **200 kbps → 1 Mbps** |
| ⭐ Chọn baud thế nào | ⭐ **Thấp nhất mà chu kỳ máy chấp nhận được** — không phải cao nhất thiết bị hỗ trợ |
| Baud cao làm gì | ⚠ **Thu hẹp biên an toàn** của cáp, nhánh rẽ, đấu nối |
| ⭐ Hạ baud xuống thì hết lỗi | Phép thử chẩn đoán mạnh — chỉ thẳng vào **tầng vật lý** |
| Phân cực | **Một bộ** trên toàn bus |
| Cấu trúc RS-485 | **Bus**, không phải hình sao |
| ⚠ Quy ước A/B | **Không thống nhất** giữa các hãng — thử đảo |
| Chủ–tớ có hạn chế gì | Tớ **không tự báo** được; phản hồi phụ thuộc chu kỳ hỏi vòng |
| Khối truyền thông theo mẫu | `Execute` (**cạnh lên**) → `Done` / `Busy` / `Error` |
| Chu kỳ hỏi | Khớp **tốc độ dữ liệu thật đổi** |
| Mất kết nối là | ⭐ **Một trạng thái**, không phải một lỗi lạ |
| Kết luận mất kết nối sau | **Ba lần lỗi liên tiếp** |
| ⚠⚠ Khi mất kết nối | **Không dùng giá trị cũ** cho quyết định |
| ⚠ Ghi tham số vào thiết bị | **Chỉ khi đổi** — ghi liên tục làm mòn bộ nhớ |

---

## 38.15 Tự kiểm

1. Phân biệt điểm–điểm, bus và mạng. Vì sao gỡ lỗi bus khó hơn gỡ lỗi mạng?
2. ⭐ Giải thích vì sao tín hiệu **vi sai** chống nhiễu tốt hơn tín hiệu so với đất chung. Vì sao đôi
   dây phải **xoắn**?
3. Nêu bốn tham số phải khớp. Lệch baud và lệch chẵn lẻ cho hai triệu chứng khác nhau thế nào — cái
   nào nguy hiểm hơn?
4. ⭐ Điện trở đầu cuối đặt ở đâu, bao nhiêu cái? Nêu **triệu chứng đặc trưng** khi thiếu.
5. Vì sao RS-485 phải đấu kiểu bus chứ không phải hình sao? Vì sao lỗi này có thể "chạy được" một thời
   gian?
6. Điện trở phân cực giải quyết vấn đề gì? Cần bao nhiêu bộ trên một bus?
7. So sánh chủ–tớ với sản xuất–tiêu thụ. ⭐ Hạn chế quan trọng nhất của chủ–tớ là gì?
8. Đọc khung `01 03 00 00 00 01 84 0A` và giải thích từng phần.
9. Vì sao khối truyền thông dùng mẫu `Execute`/`Done` thay vì trả kết quả ngay? Liên hệ với chương nào?
10. ⭐ Vì sao **không** nên báo lỗi ngay ở bản tin lỗi đầu tiên? Hậu quả của việc báo giả nhiều là gì?
11. ⭐⭐ Mất truyền thông với bộ điều khiển nhiệt độ: nó vẫn giữ nhiệt, quá trình vẫn chạy. Vì sao vẫn
    là vấn đề? Được phép dùng giá trị nhiệt độ cuối cùng không?
12. Vì sao **không** được ghi điểm đặt vào thiết bị ở mỗi vòng quét?
13. Nêu ba lý do RS-485 vẫn phổ biến dù Ethernet mạnh hơn.
14. ⚠ Đã kiểm hết bốn tham số mà vẫn im lặng. Việc nên thử tiếp theo là gì, và vì sao nó hay xảy ra?
15. ⭐⭐ Vì sao câu hỏi *"RS-485 đi được bao xa?"* là câu hỏi **thiếu**? Phải hỏi lại thế nào cho đúng?
16. ⭐ Cùng một sợi cáp 30 m: không điện trở đầu cuối đạt ~200 kbps, có thì đạt 1 Mbps. Con số này nói
    gì về tầm quan trọng của điện trở đầu cuối?
17. ⭐ Vì sao nên chọn **baud thấp nhất đủ dùng** thay vì baud cao nhất thiết bị hỗ trợ? Liên hệ với
    bẫy "hôm qua chạy được".

> Câu 2, 4, 10 và 11 là bốn câu phân loại. Câu 11 là tinh thần của cả chương: **mất truyền thông không
> làm quá trình dừng — nó làm bạn mù. Và chạy tiếp trong trạng thái mù là quyết định phải có người
> đưa ra, không phải mặc định.**

---

### Chương tiếp theo

Chương 39 — **Modbus RTU & Modbus TCP**. Bạn đã có tầng vật lý. Chương sau về giao thức chạy trên nó —
"tiếng phổ thông" của tự động hoá công nghiệp, cùng hai cái bẫy kinh điển đã làm mất thời gian của
gần như mọi người từng dùng nó.

### Nguồn tham khảo chương 38

- **TIA/EIA-232**, **TIA/EIA-422**, **TIA/EIA-485** — các chuẩn giao diện điện. *(tiêu chuẩn có bản
  quyền)*
- IEC 61131-2 — *Programmable controllers, Part 2*: yêu cầu với giao diện truyền thông của PLC.
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu đi dây và chống
  nhiễu — nền cho mục 38.5.
- **Tài liệu module truyền thông** của hệ đang dùng — dùng cho khối chức năng, ⚠ **có tự xếp hàng yêu
  cầu không**, điện trở đầu cuối tích hợp, và ⚠ **quy ước đánh số chân A/B**.
- **Tài liệu bộ điều khiển nhiệt độ** — dùng cho tham số truyền thông, bản đồ thanh ghi, và ⚠ **giới
  hạn số lần ghi** vào bộ nhớ không mất.
- **Kuphaldt, Tony R.** — *Lessons In Industrial Instrumentation*, §15.6: tín hiệu vi sai, khuyến nghị
  ⭐ **1200 m**, ⭐ **quan hệ tỉ lệ nghịch tốc độ–chiều dài**, thí nghiệm Texas Instruments về ảnh hưởng
  của điện trở đầu cuối, và ⚠ **quy ước nhãn A/B không được chuẩn hoá** — nền cho mục 38.3b và 38.13.
- Bảng I/O và số liệu đã chốt của DP-01 — Phụ lục J §J.1 và §J.2.

> ⚡ Các con số về **khoảng cách và số thiết bị tối đa** của RS-485 phụ thuộc tốc độ baud, chất lượng
> cáp, và loại mạch thu phát — chúng đánh đổi lẫn nhau. Sách không nêu con số cụ thể vì con số đúng
> phải lấy từ **datasheet của thiết bị bạn dùng**, và nó thay đổi theo cấu hình thật.
>
> ⚠ Quy tắc "ba lần lỗi liên tiếp" ở mục 38.9 là **quy tắc thực dụng**, không phải giá trị chuẩn hoá.
> Con số đúng phụ thuộc chu kỳ hỏi và mức độ quan trọng của dữ liệu — với dữ liệu đổi nhanh và quan
> trọng thì ít hơn, với dữ liệu chậm thì có thể nhiều hơn.
