# Chương 24 — Đại số Boolean & bảng chân lý dùng được

> **Lát cắt máy mẫu:** 2 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp, hai trạm, trình
> tự song song, công thức sản phẩm.

---

## 24.1 Vì sao chương này nằm ở đây, không nằm ở đầu sách

Đại số Boolean thường được dạy ngay chương đầu của sách kỹ thuật số, trước khi người học biết nó dùng
để làm gì. Sách này để nó ở đây, sau khi bạn đã viết ladder (Chương 15), đã dùng điều kiện phức tạp
(Chương 20), và sắp thiết kế máy trạng thái (Chương 25).

Lý do: đại số Boolean **không phải kiến thức nền để bắt đầu** — nó là **công cụ để gỡ rối khi logic
trở nên phức tạp**. Bạn chỉ thấy nó có ích khi đã gặp một nấc thang mà mình không chắc nó đúng.

Chương này trả lời ba câu hỏi thực dụng:

| Câu hỏi | Mục |
|---|---|
| Làm sao đi từ *"máy phải làm gì"* tới một nấc thang **chắc chắn đúng**? | 24.4 |
| Vì sao đảo một điều kiện lại **đổi hình dạng** nấc thang? | 24.5 |
| Khi nào rút gọn logic là **sai lầm**? | 24.7 |

Câu thứ ba là câu quan trọng nhất, và nó đi ngược với thứ mà môn học kỹ thuật số thường dạy.

---

## 24.2 Bốn phép cơ bản

| Phép | Trong ladder | Trong ST | Kết quả đúng khi |
|---|---|---|---|
| **AND** | Tiếp điểm **nối tiếp** | `AND` | **Tất cả** đầu vào đúng |
| **OR** | Nhánh **song song** | `OR` | **Ít nhất một** đầu vào đúng |
| **NOT** | Tiếp điểm thường đóng `┤/├` | `NOT` | Đầu vào sai |
| **XOR** | Tổ hợp — không có ký hiệu riêng | `XOR` | **Đúng một** trong hai đầu vào đúng (hai đầu vào **khác nhau**) |

XOR ít gặp ở tầng máy nhưng có một chỗ dùng rất đắt giá:

```iecst
// ⭐ Phát hiện cảm biến mâu thuẫn: xy-lanh không thể vừa ở trên vừa ở dưới
M_Clamp1SensorFault := NOT (DI_Clamp1Up XOR DI_Clamp1Dn);
```

`XOR` đúng khi **đúng một** trong hai cảm biến báo. Đảo nó lại: cờ lỗi lên khi **cả hai cùng báo**
(vô lý về vật lý) hoặc **cả hai cùng không báo** (đang giữa hành trình, hoặc hỏng cảm biến).

Đây chính là nguyên tắc ở Chương 28 — **không suy tư thế từ một cảm biến** — viết thành một dòng.

---

## 24.3 Bảng chân lý — công cụ chống "tôi nghĩ là đúng"

**Bảng chân lý** *(truth table)* liệt kê **mọi tổ hợp** đầu vào và kết quả mong muốn cho từng tổ hợp.

Giá trị của nó không nằm ở toán học, mà ở chỗ nó **ép bạn trả lời những tổ hợp bạn chưa nghĩ tới**.

Ví dụ trên DP-01: khi nào cho phép chuyền chạy?

Ba điều kiện: `DI_AirOK` (đủ khí), `M_Stn1Empty` (trạm 1 trống), `M_AnyFault` (có lỗi).

| # | `DI_AirOK` | `M_Stn1Empty` | `M_AnyFault` | Cho chạy? | Ghi chú |
|:-:|:-:|:-:|:-:|:-:|---|
| 0 | 0 | 0 | 0 | **0** | Không đủ khí |
| 1 | 0 | 0 | 1 | **0** | |
| 2 | 0 | 1 | 0 | **0** | |
| 3 | 0 | 1 | 1 | **0** | |
| 4 | 1 | 0 | 0 | **0** | Trạm 1 còn board — chuyền dừng để không dồn |
| 5 | 1 | 0 | 1 | **0** | |
| 6 | 1 | 1 | 0 | **1** | ✅ Trường hợp duy nhất cho chạy |
| 7 | 1 | 1 | 1 | **0** | Có lỗi |

Ba điều rút ra:

- **Ba đầu vào cho 8 dòng.** Số dòng là `2ⁿ` với `n` là số đầu vào. Bốn đầu vào là 16 dòng, năm là 32.
- **Chỉ một dòng cho kết quả 1.** Nghĩa là biểu thức chính là AND của cả ba: `DI_AirOK AND
  M_Stn1Empty AND NOT M_AnyFault`.
- ⭐ **Bảng ép bạn nghĩ tới dòng 4** — có khí, không lỗi, nhưng trạm 1 còn board. Đây là dòng người ta
  hay quên khi viết thẳng từ đầu, và nó là dòng gây dồn board.

> 💡 **Khi nào đáng lập bảng chân lý**
> Không phải cho mọi nấc thang. Đáng làm khi:
> - có **từ ba điều kiện trở lên** và bạn không chắc mình đã nghĩ hết;
> - logic liên quan tới **an toàn hoặc hỏng sản phẩm**;
> - bạn đang **đọc code của người khác** và muốn kiểm nó đúng không (Chương 22);
> - có **trường hợp biên** mà khách hàng chưa trả lời — bảng chân lý biến câu hỏi mơ hồ thành danh
>   sách câu hỏi cụ thể để hỏi (Chương 23).
>
> Gạch đầu dòng cuối là công dụng bị đánh giá thấp nhất: đưa bảng cho khách hàng và hỏi *"dòng 4 thì
> máy nên làm gì?"* — dễ trả lời hơn nhiều so với câu hỏi mở.

---

## 24.4 Từ bảng chân lý tới nấc thang

Quy trình ba bước, cho ra một nấc thang **chắc chắn khớp với bảng**.

### Bước 1 — Lấy các dòng có kết quả 1

Từ bảng ở mục 24.3: chỉ dòng 6.

### Bước 2 — Mỗi dòng thành một tích AND

Với dòng 6: `DI_AirOK` = 1, `M_Stn1Empty` = 1, `M_AnyFault` = 0.

```text
DI_AirOK AND M_Stn1Empty AND NOT M_AnyFault
```

Quy tắc: đầu vào bằng **1** thì viết thẳng; bằng **0** thì viết `NOT`.

### Bước 3 — OR các tích lại

Chỉ có một dòng nên không cần OR. Nấc thang:

```text
   DI_AirOK   M_Stn1Empty   M_AnyFault            DO_ConvRun
──────┤ ├─────────┤ ├──────────┤/├───────────────────( )──────
```

### Ví dụ có nhiều dòng — khi nào bật đèn vàng

Đèn vàng của đèn tháp bật khi máy **cần chú ý nhưng chưa dừng**. Giả sử: khi thiếu khí, **hoặc** khi
đã có cảnh báo chu kỳ chậm, **nhưng** không phải khi đang có lỗi (vì lúc đó đèn đỏ sáng).

| # | `M_AirLow` | `M_CycleWarn` | `M_AnyFault` | Đèn vàng |
|:-:|:-:|:-:|:-:|:-:|
| 2 | 0 | 1 | 0 | **1** |
| 4 | 1 | 0 | 0 | **1** |
| 6 | 1 | 1 | 0 | **1** |

(Các dòng còn lại cho 0.)

Ba tích, OR lại:

```text
(M_AirLow AND NOT M_CycleWarn AND NOT M_AnyFault)
OR (NOT M_AirLow AND M_CycleWarn AND NOT M_AnyFault)
OR (M_AirLow AND M_CycleWarn AND NOT M_AnyFault)
```

Đúng nhưng dài. Nhìn kỹ: cả ba tích đều có `NOT M_AnyFault`, và ba dòng còn lại chính là "ít nhất một
trong `M_AirLow`, `M_CycleWarn`". Rút gọn:

```iecst
DO_LampYellow := (M_AirLow OR M_CycleWarn) AND NOT M_AnyFault;
```

Ngắn hơn nhiều, và — quan trọng hơn — **đọc ra được ý nghĩa**: *"có cảnh báo nào đó, và chưa tới mức
lỗi"*. Đây là cách rút gọn đúng đắn: nó làm biểu thức **gần với lời văn hơn**, không xa hơn.

Mục 24.7 nói về loại rút gọn đi theo hướng ngược lại.

---

## 24.5 ⭐ De Morgan — vì sao đảo điều kiện đổi hình dạng nấc thang

### Hai đẳng thức

**Định luật De Morgan** phát biểu:

```text
NOT (A AND B)  =  (NOT A) OR  (NOT B)
NOT (A OR  B)  =  (NOT A) AND (NOT B)
```

Cách nhớ bằng lời:

> **Đảo cả cụm = đảo từng cái, rồi đổi AND thành OR (và ngược lại).**

### Vì sao nó quan trọng với ladder

Trong ladder, AND là **nối tiếp** và OR là **song song**. Nên De Morgan không chỉ đổi công thức — nó
**đổi hình dạng nấc thang**:

```text
NOT (A AND B) — cách 1: một tiếp điểm đảo sau cụm nối tiếp
    A       B      (đảo cụm)        Y
────┤ ├────┤ ├────[ NOT ]──────────( )────

NOT (A AND B) — cách 2: hai nhánh song song, mỗi nhánh một tiếp điểm đảo
       A
   ┌──┤/├──┐
───┤       ├──────────────────────( )────
   │   B   │
   └──┤/├──┘
```

Hai hình khác hẳn nhau, **cùng một logic**.

### Vì sao bạn cần nó trong công việc thật

Ba tình huống:

**1. Ladder không có "đảo cả cụm".** Nhiều hệ không cho bạn đặt một phép NOT lên cả một nhóm tiếp
điểm. Bạn **buộc** phải dùng De Morgan để vẽ được nấc thang. Cách 2 ở trên là cách duy nhất khả thi.

**2. Đọc code người khác.** Bạn thấy một nấc thang có hai nhánh song song với hai tiếp điểm thường
đóng, và không hiểu ý đồ. Áp De Morgan ngược lại: nó là `NOT (A AND B)` — *"không phải cả hai cùng
đúng"*. Ý đồ hiện ra ngay.

**3. Chuyển giữa lời văn và code.** Yêu cầu thường viết ở dạng phủ định: *"không cho chạy nếu thiếu
khí hoặc có lỗi"*. De Morgan cho bạn chuyển nó thành dạng khẳng định để viết nấc thang:

```text
NOT (M_AirLow OR M_AnyFault)  =  (NOT M_AirLow) AND (NOT M_AnyFault)
```

Tức: cho chạy khi **đủ khí VÀ không lỗi** — dạng nối tiếp, viết ladder được ngay.

### ⚠ Chỗ dễ sai nhất

> ⚠ **Đảo một cụm KHÔNG phải là đảo từng cái mà giữ nguyên phép nối.**
>
> ```text
> ✗ SAI:  NOT (A AND B)  =  (NOT A) AND (NOT B)
> ✓ ĐÚNG: NOT (A AND B)  =  (NOT A) OR  (NOT B)
> ```
>
> Đây là lỗi phổ biến nhất khi làm việc với logic đảo, và nó **không gây lỗi biên dịch** — chương
> trình chạy, cho kết quả sai ở một số tổ hợp đầu vào và đúng ở các tổ hợp khác. Nghĩa là nó có thể
> qua được chạy thử rồi hỏng ở hiện trường.
>
> **Cách tự kiểm chắc chắn: lập bảng chân lý cho cả hai vế.** Hai cột kết quả phải giống nhau ở
> **mọi** dòng. Bốn dòng, một phút.

Kiểm nhanh cho `A=1, B=0`:

| Biểu thức | Kết quả |
|---|---|
| `NOT (A AND B)` = `NOT (1 AND 0)` = `NOT 0` | **1** |
| `(NOT A) OR (NOT B)` = `0 OR 1` | **1** ✅ khớp |
| `(NOT A) AND (NOT B)` = `0 AND 1` | **0** ❌ sai |

---

## 24.6 Bìa Karnaugh — ở mức thực dụng

**Bìa Karnaugh** *(Karnaugh map, K-map)* là cách sắp bảng chân lý thành lưới sao cho các tổ hợp **kề
nhau chỉ khác nhau một biến**. Nhóm các ô 1 kề nhau lại thì rút gọn được biểu thức.

Lấy ví dụ đèn vàng ở mục 24.4, với `M_AnyFault = 0`:

```text
                M_CycleWarn
                  0     1
              ┌─────┬─────┐
   M_AirLow 0 │  0  │  1  │
              ├─────┼─────┤
            1 │  1  │  1  │
              └─────┴─────┘
```

Ba ô bằng 1 nằm kề nhau tạo thành hình chữ L. Nhóm chúng lại: một nhóm là cả hàng dưới (`M_AirLow`
= 1, không phụ thuộc `M_CycleWarn`), một nhóm là cả cột phải (`M_CycleWarn` = 1). Kết quả:

```text
M_AirLow OR M_CycleWarn
```

Đúng bằng kết quả rút gọn bằng mắt ở mục 24.4.

### ⚠ Nói thật về bìa Karnaugh

Bìa Karnaugh là công cụ kinh điển của môn kỹ thuật số, và bạn sẽ gặp nó trong mọi giáo trình. Nhưng
với công việc PLC hàng ngày:

| Thực tế | Hệ quả |
|---|---|
| Nó chỉ tiện với **2–4 biến** | Logic máy thật thường có nhiều hơn |
| Với 5 biến trở lên nó khó dùng hơn suy luận trực tiếp | Rất ít người dùng nó ở công việc thật |
| ⭐ Bộ nhớ PLC không khan hiếm | Động cơ gốc của việc rút gọn — tiết kiệm cổng logic — **không còn** |
| ⚠ Kết quả rút gọn thường **khó đọc hơn** bản gốc | Xem mục 24.7 |

> **Vì sao vẫn nên biết nó tồn tại:** bạn sẽ gặp nó khi học, khi phỏng vấn, và khi đọc tài liệu cũ.
> Hiểu **ý tưởng** — ô kề nhau khác một biến thì gộp được — là đủ. Không cần thành thạo.
>
> Với logic nhiều biến trong công việc thật, công cụ đúng là **bảng chân lý** (để không sót trường
> hợp) và **máy trạng thái** (để không cần một biểu thức khổng lồ nào cả) — Chương 25.

---

## 24.7 ⭐ Khi nào **không** nên tối ưu

Đây là mục quan trọng nhất chương, và nó đi ngược với thói quen từ môn kỹ thuật số.

### Bài toán

Môn kỹ thuật số dạy: rút gọn biểu thức càng ngắn càng tốt, vì mỗi cổng logic là tiền và là diện tích
chip.

**Trong PLC, tiền đề đó không còn đúng.** Bộ nhớ chương trình và thời gian quét dư dả cho logic nhị
phân. Một nấc thang dài hơn vài tiếp điểm không đo được sự khác biệt.

Cái khan hiếm bây giờ là **thời gian của người đọc lúc hai giờ sáng**.

### Ví dụ

Điều kiện cho phép nâng kẹp trạm 1, viết theo lời văn của đặc tả:

```iecst
// ✓ Dài hơn, nhưng đọc ra được TỪNG lý do
M_Stn1ClampAllow := M_Running
                AND DI_AirOK
                AND DI_Door1Closed
                AND DI_BoardStn1
                AND DI_Stop1Up
                AND NOT M_AnyFault;
```

Cùng logic đó, sau khi ai đó "tối ưu" bằng cách gom các điều kiện vào một cờ tổng:

```iecst
// ✗ Ngắn hơn, nhưng KHÔNG đọc ra được lý do nào
M_Stn1ClampAllow := M_MachineOK AND M_Stn1Ready;
```

Bản thứ hai ngắn hơn. Nhưng khi kẹp không lên và người bảo trì nhìn vào:

| Bản 1 | Bản 2 |
|---|---|
| Nhìn trực tuyến, thấy ngay `DI_Door1Closed` không sáng → đi đóng cửa | Thấy `M_Stn1Ready` bằng 0 → **phải đi tìm** chỗ nào ghi vào nó |
| Một lần nhìn | Truy ngược qua hai, ba tầng cờ trung gian |
| Chẩn đoán trong 10 giây | Chẩn đoán trong 10 phút, nếu quen chương trình |

> ⚠⚠ **Quy tắc: với logic điều kiện cho phép và liên động, ƯU TIÊN ĐỌC ĐƯỢC HƠN NGẮN.**
>
> Cụ thể:
> - **Không gom** nhiều điều kiện không liên quan vào một cờ tổng chỉ để nấc thang ngắn lại.
> - **Giữ thứ tự** các điều kiện khớp với thứ tự trong đặc tả — người đọc đối chiếu được.
> - Cờ trung gian chỉ đáng có khi nó **mang một ý nghĩa gọi tên được** và được dùng ở **nhiều chỗ**.
>   `M_SafetyOK` là cờ tốt; `M_Temp3` thì không.
> - ⚠ **Không bao giờ** rút gọn logic liên quan an toàn để cho gọn. Ở đó, rõ ràng và kiểm chứng được
>   quan trọng hơn mọi thứ khác (Chương 47).

### Khi nào rút gọn **đúng đắn**

Rút gọn tốt khi nó làm biểu thức **gần với lời văn hơn**:

| Trước | Sau | Có tốt hơn không |
|---|---|---|
| Ba tích OR với nhau, mỗi tích ba biến (mục 24.4) | `(M_AirLow OR M_CycleWarn) AND NOT M_AnyFault` | ✅ **Có** — đọc ra được: "có cảnh báo, chưa tới mức lỗi" |
| Sáu điều kiện nối tiếp có tên rõ nghĩa | `M_MachineOK AND M_Stn1Ready` | ❌ **Không** — mất thông tin chẩn đoán |

Phép thử một câu:

> **Sau khi rút gọn, đọc biểu thức lên thành lời. Nếu câu đó vẫn khớp với yêu cầu trong đặc tả →
> tốt. Nếu phải đi tra ba chỗ khác mới hiểu → đã rút gọn quá tay.**

---

## 24.8 Trên máy mẫu DP-01

### Bảng chân lý cho một trường hợp biên thật

Câu hỏi ở Chương 23, nhóm B: *"hai board vào cùng lúc thì sao?"* Trên DP-01, tình huống là cả
`DI_BoardStn1` và `DI_BoardInfeed` cùng báo có board.

| # | `DI_BoardStn1` | `DI_BoardInfeed` | `M_Stn1Busy` | Chuyền chạy? | Chặn 1 nâng? |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 0 | 0 | 0 | **1** | 0 |
| 1 | 0 | 0 | 1 | 0 | 0 |
| 2 | 0 | 1 | 0 | **1** | 0 |
| 3 | 0 | 1 | 1 | 0 | 0 |
| 4 | 1 | 0 | 0 | 0 | **1** |
| 5 | 1 | 0 | 1 | 0 | 0 |
| 6 | 1 | 1 | 0 | 0 | **1** |
| 7 | 1 | 1 | 1 | 0 | 0 |

Dòng 6 là trường hợp biên: board đã ở trạm 1 **và** có board tiếp theo đang chờ. Đáp án: dừng chuyền,
nâng chặn để board thứ hai không dồn vào. Nếu không lập bảng, đây đúng là dòng bị bỏ sót — và hậu quả
là hai board chồng nhau ở trạm.

### Cảm biến mâu thuẫn — bốn tổ hợp

| `DI_Clamp1Up` | `DI_Clamp1Dn` | Kết luận |
|:-:|:-:|---|
| 0 | 1 | Chắc chắn ở **dưới** |
| 1 | 0 | Chắc chắn ở **trên** |
| 0 | 0 | ⚠ Giữa hành trình, **hoặc** hỏng cảm biến |
| 1 | 1 | ⚠⚠ **Vô lý về vật lý** — chắc chắn hỏng |

```iecst
M_Clamp1Up      := DI_Clamp1Up AND NOT DI_Clamp1Dn;
M_Clamp1Dn      := DI_Clamp1Dn AND NOT DI_Clamp1Up;
M_Clamp1Unknown := NOT (DI_Clamp1Up XOR DI_Clamp1Dn);   // hai dòng ⚠ ở trên
```

Ba dòng này là cách viết gọn của bảng bốn dòng. Điểm mấu chốt: **có một biến riêng cho "không biết"**
— chương trình không bao giờ phải đoán. Đây là nội dung Chương 28, và bảng chân lý là cách chứng minh
ba dòng code trên phủ hết bốn tổ hợp.

---

## 24.9 Khác biệt giữa các hãng

Đại số Boolean là toán học nên **không phụ thuộc hãng**. Chỉ có cách viết khác nhau.

| Phép | Siemens (SCL) | Mitsubishi (ST) | Rockwell (ST) | CODESYS |
|---|---|---|---|---|
| AND | `AND` | `AND` | `AND` | `AND` |
| OR | `OR` | `OR` | `OR` | `OR` |
| NOT | `NOT` | `NOT` | `NOT` | `NOT` |
| XOR | `XOR` | `XOR` | `XOR` | `XOR` |

| Khía cạnh | Điều cần biết |
|---|---|
| ⚠ **Đảo cả một cụm trong ladder** | Không phải hệ nào cũng cho phép. Khi không có, **buộc dùng De Morgan** để vẽ được nấc thang (mục 24.5) |
| Tiếp điểm đảo | Mọi hệ đều có tiếp điểm thường đóng — đó là `NOT` cho một biến đơn |
| ⚠ Số nhánh song song tối đa | Có giới hạn, khác nhau theo hệ và dòng CPU. Chạm giới hạn khi vẽ dạng De Morgan của một cụm lớn — khi đó tách thành nhiều nấc, hoặc chuyển sang ST |
| Lệnh Boolean trên `WORD` | Mọi hệ đều có AND/OR/XOR theo bit trên cả một từ; ⚠ đừng nhầm với phép logic trên `BOOL` (Chương 11, mục 11.2) |

---

## 24.10 Bẫy thường gặp

### 🔍 BẪY 1 — Áp De Morgan sai: giữ nguyên phép nối

`NOT (A AND B)` thành `(NOT A) AND (NOT B)`.

**Hiện tượng:** logic đúng ở một số tổ hợp và sai ở tổ hợp khác — nên có thể **qua được chạy thử** rồi
hỏng ở hiện trường khi gặp đúng tổ hợp chưa thử.
**Cách sửa:** đảo cụm thì **đổi luôn phép nối**. Kiểm bằng bảng chân lý bốn dòng (mục 24.5).

### 🔍 BẪY 2 — Không lập bảng chân lý cho logic ba biến trở lên

**Hiện tượng:** một tổ hợp đầu vào chưa từng được nghĩ tới xuất hiện ở hiện trường; máy làm điều không
ai định. Ví dụ: dòng 6 ở mục 24.8 — hai board dồn nhau.
**Cách sửa:** ba biến là 8 dòng, mười phút. Rẻ hơn nhiều so với một sự cố.

### 🔍 BẪY 3 — Rút gọn tới mức không đọc được

**Hiện tượng:** máy không chạy, người bảo trì thấy `M_Stn1Ready = 0` và phải truy ngược qua ba tầng
cờ trung gian để biết cửa đang mở.
**Cách sửa:** mục 24.7. Với liên động và điều kiện cho phép, **đọc được quan trọng hơn ngắn**.

### 🔍 BẪY 4 — Gom điều kiện không liên quan vào một cờ

`M_AllOK := DI_AirOK AND DI_Door1Closed AND M_RecipeLoaded AND DI_VfdReady;`

**Hiện tượng:** cờ này bằng 0 nhưng không nói được vì sao; và khi cần bỏ một điều kiện cho một chế độ
đặc biệt thì không tách ra được.
**Cách sửa:** cờ trung gian phải mang **một ý nghĩa gọi tên được**. `M_SafetyOK` gom các điều kiện an
toàn thì hợp lý; `M_AllOK` gom mọi thứ thì không.

### 🔍 BẪY 5 — Dùng bìa Karnaugh cho logic máy nhiều biến

**Hiện tượng:** mất thời gian với một công cụ không hợp, và kết quả ra biểu thức khó đọc.
**Cách sửa:** trên 4 biến thì bảng chân lý + máy trạng thái là công cụ đúng (mục 24.6, Chương 25).

### 🔍 BẪY 6 — Quên tổ hợp "cả hai cảm biến cùng báo"

**Hiện tượng:** một cảm biến reed hỏng ở trạng thái luôn báo; chương trình suy ra tư thế sai và ra
lệnh cho cơ cấu khác chạy.
**Cách sửa:** bốn tổ hợp ở mục 24.8, và **một biến riêng cho "không biết"**.

### 🔍 BẪY 7 — Rút gọn logic liên quan an toàn

**Hiện tượng:** logic ngắn hơn nhưng không còn đối chiếu được với đặc tả an toàn; và không ai kiểm
chứng được nó đúng.
**Cách sửa:** ⚠⚠ **không rút gọn** ở đó. Rõ ràng và kiểm chứng được quan trọng hơn (Chương 47).

### 🔍 BẪY 8 — Nhầm phép logic trên `BOOL` với phép theo bit trên `WORD`

**Hiện tượng:** kết quả là một con số thay vì đúng/sai, hoặc ngược lại; và điều kiện luôn đúng hoặc
luôn sai.
**Cách sửa:** `BOOL` cho logic, `WORD` cho thao tác bit (Chương 11, mục 11.2).

---

## 24.11 Bảng chốt

| Việc | Cách làm |
|---|---|
| Logic có từ 3 điều kiện trở lên | **Lập bảng chân lý** — `2ⁿ` dòng |
| Từ bảng chân lý ra nấc thang | Lấy dòng kết quả 1 → mỗi dòng một tích AND → OR các tích |
| Đầu vào bằng 0 trong tích | Viết `NOT` |
| Đảo cả một cụm | ⭐ **De Morgan** — đảo từng cái **và đổi phép nối** |
| Kiểm De Morgan có đúng không | Bảng chân lý cả hai vế, so **mọi** dòng |
| Ladder không cho đảo cả cụm | Dùng dạng De Morgan — nhánh song song với tiếp điểm đảo |
| Yêu cầu viết ở dạng phủ định | De Morgan để chuyển sang dạng khẳng định |
| Bìa Karnaugh | Biết ý tưởng là đủ; chỉ tiện với 2–4 biến |
| Logic nhiều biến, nhiều trạng thái | **Máy trạng thái** (Chương 25), không phải một biểu thức lớn |
| ⭐ Rút gọn logic liên động | **Đừng** — ưu tiên đọc được hơn ngắn |
| Phép thử sau khi rút gọn | Đọc biểu thức thành lời; còn khớp đặc tả thì tốt |
| Logic an toàn | ⚠⚠ **Không rút gọn** |
| Hai cảm biến đối nhau | Bốn tổ hợp, và **một biến riêng cho "không biết"** |

---

## 24.12 Tự kiểm

1. Ladder thể hiện AND và OR bằng cách nào?
2. Logic có 4 điều kiện thì bảng chân lý có bao nhiêu dòng? Công thức là gì?
3. ⭐ Viết hai đẳng thức De Morgan. Lỗi phổ biến nhất khi áp dụng chúng là gì, và vì sao lỗi đó
   **nguy hiểm hơn** một lỗi biên dịch?
4. Vì sao khi ladder không cho đảo cả một cụm, bạn **buộc** phải dùng De Morgan?
5. Chuyển câu *"không cho chạy nếu thiếu khí hoặc có lỗi"* thành dạng khẳng định viết được bằng ladder.
6. ⭐ Vì sao động cơ gốc của việc rút gọn logic — tiết kiệm cổng — **không còn đúng** với PLC? Cái gì
   khan hiếm thay vào đó?
7. So sánh `M_Running AND DI_AirOK AND DI_Door1Closed AND NOT M_AnyFault` với `M_MachineOK AND
   M_Stn1Ready`. Bản nào tốt hơn cho việc chẩn đoán, và vì sao?
8. Nêu phép thử một câu để biết mình đã rút gọn quá tay chưa.
9. Hai cảm biến `DI_Clamp1Up` và `DI_Clamp1Dn` cho **bốn** tổ hợp. Nêu ý nghĩa từng tổ hợp và cho
   biết tổ hợp nào là vô lý về vật lý.
10. ⭐ Trong bảng ở mục 24.8, dòng 6 là dòng hay bị bỏ sót. Nó mô tả tình huống gì, và hậu quả trên
    máy nếu quên nó là gì?

> Câu 3, 6 và 10 là ba câu phân loại. Câu 6 là tinh thần của cả chương: **thứ đáng tối ưu trong lập
> trình PLC không phải số cổng logic — mà là thời gian của người sẽ đọc nó.**

---

### Chương tiếp theo

Chương 25 — **Thiết kế theo máy trạng thái**. Chương này cho bạn công cụ xử lý logic tổ hợp. Nhưng
máy thật không chỉ có logic tổ hợp — nó có **trạng thái**, và cùng một tổ hợp đầu vào phải cho kết
quả khác nhau tuỳ máy đang ở đâu. Đó là lúc bảng chân lý hết tác dụng và cần một công cụ khác.

### Nguồn tham khảo chương 24

- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: các phép toán Boolean và
  cách biểu diễn trong LD, FBD, ST. *(tiêu chuẩn có bản quyền)*
- **Kuphaldt, Tony R.** — *Lessons In Electric Circuits, Volume IV: Digital*, ch. 7 *Boolean Algebra*
  (§7.8 *DeMorgan's Theorems*, §7.9 *Converting truth tables into Boolean expressions*) và ch. 8
  *Karnaugh Mapping*: nền toán cho các mục bảng chân lý, De Morgan và bìa Karnaugh. ⭐ Sách mở, đọc
  được toàn văn — đây là chỗ nên tới khi cần **phần chứng minh** mà chương này cố ý lược bớt.
- Giáo trình đại số Boolean và kỹ thuật số cơ bản nói chung — đây là toán học phổ thông, không gắn
  với hãng nào; mọi giáo trình kỹ thuật số nhập môn đều dùng được.
- Đặc tả trình tự và bảng I/O của DP-01 — Phụ lục J; các bảng chân lý ở mục 24.3 và 24.8 lấy điều
  kiện từ đó.

> ⚡ Nhận định ở mục 24.6 và 24.7 — rằng rút gọn logic ít giá trị trong PLC và có thể phản tác dụng —
> là **quan sát thực tế của nghề**, không phải phát biểu của tiêu chuẩn. Nó đúng với logic điều khiển
> máy trên PLC hiện đại, nơi bộ nhớ và thời gian quét dư dả. Trong các ngữ cảnh khác — thiết kế mạch
> logic rời rạc, FPGA, hệ nhúng rất nhỏ — đánh đổi hoàn toàn khác và việc rút gọn vẫn rất đáng giá.
