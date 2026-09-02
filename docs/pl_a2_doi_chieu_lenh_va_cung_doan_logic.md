
# Phụ lục A2 — Đối chiếu lệnh & cùng một đoạn logic viết 5 lần

> **Phụ lục A1 đối chiếu khái niệm. A2 đối chiếu lệnh — và viết cùng một đoạn trình tự của DP-01 trên
> cả năm hệ.**

---

> ⚠⚠ **ĐỌC TRƯỚC**
>
> | | |
> |---|---|
> | ⭐ **Mục đích** | Chuyển kiến thức giữa các hệ; đọc được tài liệu của hệ chưa dùng |
> | ⚠ **KHÔNG phải mục đích** | ⭐ **Xếp hạng hãng** — phụ lục **mô tả khác biệt** |
> | ⚠⚠ **Giới hạn** | ⭐ Tên lệnh và chân khối **khác nhau theo dòng sản phẩm và phiên bản phần mềm** |
> | ⭐ **Cách dùng đúng** | Dùng để **biết cần tìm gì**, rồi ⭐ **tra tài liệu dòng cụ thể** |
>
> ⚠ **Mã trong phụ lục này là mã MINH HOẠ để so sánh cấu trúc — không phải mã chạy được nguyên
> văn.** Cú pháp chính xác, tên chân và cách khai báo phải lấy từ tài liệu hệ bạn dùng.

---

## A2.1 ⭐ Ba mức tương đương

Trước khi vào bảng, cần phân biệt ba loại quan hệ:

| Mức | Nghĩa | Ví dụ |
|---|---|---|
| ⭐ **Tương đương 1-1** | Cùng chức năng, chỉ khác tên | `MOVE` ↔ `MOV` |
| ⚡ **Tương đương gần** | Cùng ý tưởng, ⚠ **khác chi tiết** | Bộ định thời — khác cách đặt thời gian |
| ⚠⚠ **KHÔNG tương đương** | ⭐ **Khái niệm khác nhau** | Khối chuyển động; xử lý ngắt |

> ⭐⭐ **Phụ lục này nêu rõ những chỗ KHÔNG tương đương 1-1, không giả vờ chúng giống nhau.**
>
> ⚠ Giả vờ tương đương là cách tạo ra lỗi khi chuyển nền — đúng vấn đề của Chương 56 mục 56.4.

---

## A2.2 Bộ định thời

| | Siemens | Mitsubishi | Inovance | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|---|
| Trễ khi bật | `TON` (IEC) | ⭐ `OUT T0 K20` — thiết bị T | `TON` hoặc thiết bị T | ⭐ `TON` | ⭐ `TON` |
| Trễ khi tắt | `TOF` | ⚠ **Thường phải tự dựng** | `TOF` | `TOF` | `TOF` |
| Xung | `TP` | ⚠ Tự dựng | `TP` | `TP` | ⚡ `TP`/tự dựng |
| **Đặt thời gian** | ⭐ Kiểu `TIME`: `T#2s` | ⭐⭐ **Số nguyên × độ phân giải**: `K20` = 2,0 s nếu T là 100 ms | Tuỳ dòng | ⭐ `T#2s` | ⭐ Mili giây: `2000` |
| **Mức tương đương** | ⚡ Gần | ⚠⚠ **Khác đáng kể** | ⚡ Gần | — (cột neo) | ⚡ Gần |

> ⚠⚠ **Cột Mitsubishi là chỗ khác biệt thật, không phải khác tên.**
>
> ⭐ Ở hệ kiểu thiết bị, mỗi bộ định thời là **một thiết bị `T` có độ phân giải cố định** — `T0–T199`
> có thể là 100 ms, dải khác là 10 ms hoặc 1 ms. Giá trị đặt là **số nguyên đếm theo độ phân giải
> đó**.
>
> ⚠ Nghĩa là `K20` cho **2,0 giây** hay **0,02 giây** tuỳ vào `T` đó thuộc dải nào. ⚠⚠ **Đây là một
> nguồn lỗi kinh điển khi chuyển chương trình hoặc khi đổi số hiệu bộ định thời.**
>
> ⭐ **Luôn kiểm độ phân giải của dải `T` bạn đang dùng.**

> ⭐ **Điểm chung của cả năm hệ — nhắc lại vì nó quan trọng hơn mọi khác biệt cú pháp:**
> ⚠⚠ **Bộ định thời KHÔNG dùng để chuyển bước trình tự** — chỉ để báo lỗi khi phản hồi không tới
> (Chương 21).

---

## A2.3 Bộ đếm

| | Siemens | Mitsubishi | Inovance | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|---|
| Đếm lên | `CTU` | ⭐ `OUT C0 K12` — thiết bị C | `CTU` / thiết bị C | ⭐ `CTU` | ⭐ `CTU` |
| Đếm xuống | `CTD` | ⚡ Tuỳ dòng | | `CTD` | `CTD` |
| Lên–xuống | `CTUD` | ⚡ Thiết bị C hai chiều | | `CTUD` | ⚡ Dùng `CTU`+`CTD` |
| Xoá | Chân `R` | ⭐ Lệnh `RST C0` | | Chân `RESET` | Chân `Reset` |
| **Bộ đếm tốc độ cao** | ⚠⚠ Cấu hình phần cứng | ⚠⚠ Thiết bị đặc biệt | ⚠⚠ Cấu hình | ⚠⚠ Theo phần cứng | ⚠⚠ Module riêng |
| **Mức tương đương** | ⚡ Gần | ⚡ Gần | ⚡ Gần | — | ⚡ Gần |

> ⚠⚠ **Hàng "bộ đếm tốc độ cao" KHÔNG tương đương giữa các hệ.** Nó là chức năng của **phần cứng**,
> nên cách cấu hình, tần số tối đa, và các chế độ đếm khác nhau hoàn toàn.
>
> ⭐ Khi chuyển nền, đây là hạng mục phải **thiết kế lại**, không phải dịch (Chương 18, Phụ lục K.5).

---

## A2.4 Chuyển dữ liệu và so sánh

| Chức năng | Siemens | Mitsubishi | ⭐ CODESYS | Rockwell | Mức |
|---|---|---|---|---|---|
| Gán / chuyển | `MOVE` | `MOV` | `:=` | `MOV` | ⭐ 1-1 |
| Chuyển khối | `MOVE_BLK` | `BMOV` | ⚡ `MEMCPY`/vòng lặp | `COP` · `CPS` | ⚡ Gần |
| Cộng · trừ | `ADD` · `SUB` | `ADD`/`+` · `SUB`/`-` | `+` · `-` | `ADD` · `SUB` | ⭐ 1-1 |
| Nhân · chia | `MUL` · `DIV` | `MUL` · `DIV` | `*` · `/` | `MUL` · `DIV` | ⭐ 1-1 |
| So sánh | `CMP` · toán tử | `LD=` `LD>` … | `=` `>` `<` … | `EQU` `GRT` … | ⭐ 1-1 |
| Giới hạn | `LIMIT` | ⚡ Tự dựng | `LIMIT` | `LIM` | ⚡ Gần |
| Chọn | `SEL` | ⚡ Tự dựng | `SEL` | ⚡ `SEL`/logic | ⚡ Gần |

> ⚠ **Chú ý ở `COP` và `CPS` của Rockwell:** một trong hai đảm bảo dữ liệu không bị thay đổi giữa
> chừng bởi tác vụ khác. ⭐ **Khi sao chép dữ liệu dùng chung giữa nhiều task, sự khác nhau đó quan
> trọng** — đọc tài liệu trước khi chọn.

---

## A2.5 Bắt cạnh

| | Siemens | Mitsubishi | Inovance | ⭐ CODESYS | Rockwell |
|---|---|---|---|---|---|
| Cạnh lên | ⭐ Tiếp điểm `P` · `R_TRIG` | ⭐ `LDP` · `PLS` | `LDP` | ⭐ `R_TRIG` | ⭐ `ONS` · `OSR` |
| Cạnh xuống | Tiếp điểm `N` · `F_TRIG` | `LDF` · `PLF` | `LDF` | `F_TRIG` | `OSF` |
| **Mức tương đương** | ⚡ Gần | ⚡ Gần | ⚡ Gần | — | ⚡ Gần |

> ⚠⚠ **Điểm chung phải nhớ trên MỌI hệ: mỗi chỗ bắt cạnh cần một BIT NHỚ RIÊNG.**
>
> Bắt cạnh hoạt động bằng cách so trạng thái hiện tại với trạng thái vòng quét trước — nên nó phải
> nhớ trạng thái đó ở đâu đó.
>
> ⚠ **Dùng chung một bit nhớ cho hai chỗ bắt cạnh là lỗi kinh điển**, và nó tạo ra hành vi rất khó
> hiểu: một chỗ "ăn mất" cạnh của chỗ kia. Trên hệ có thể hiện FB, mỗi `R_TRIG` phải là **một thể
> hiện riêng** (Chương 11, Phụ lục B.9).

---

## A2.6 Quy đổi thang analog

| | Cách làm |
|---|---|
| **Siemens** | ⭐ Có khối chuẩn hoá + đổi thang (`NORM_X` → `SCALE_X`); hoặc tự tính |
| **Mitsubishi** | ⚡ Lệnh đổi thang tuỳ dòng; ⭐ **nhiều người tự tính** |
| **Inovance** | Tuỳ dòng |
| ⭐ **CODESYS** | ⭐ Tự tính hoặc dùng thư viện |
| **Rockwell** | ⭐ `SCL` · `SCP`; hoặc tự tính |
| **Mức tương đương** | ⚡ **Gần** — cùng phép toán, khác cách gói |

> ⭐⭐ **Vì phép toán giống nhau ở mọi hệ, tự viết một khối hàm quy đổi là lựa chọn tốt:**
>
> | Lợi ích | |
> |---|---|
> | ⭐ **Chuyển nền được** | Cùng một khối, dịch sang hệ khác dễ |
> | ⭐ **Kiểm soát được cách xử lý số** | Ép kiểu, thứ tự phép tính, tràn số (Phụ lục K.6) |
> | ⭐⭐ **Gộp luôn phát hiện ngoài dải** | ⚠ Điều mà khối chuẩn thường **không** làm |
>
> ⭐ Hàng cuối là lý do mạnh nhất: khối chuẩn quy đổi 3,0 mA thành một con số âm và **không nói gì**.
> Khối tự viết thì báo *"lỗi cảm biến"* (Chương 31 mục 31.7).

---

## A2.7 ⚠⚠ PID và chuyển động — KHÔNG tương đương

| | PID | Chuyển động |
|---|---|---|
| **Siemens** | Khối PID có bộ tự chỉnh | Thư viện chuyển động riêng |
| **Mitsubishi** | Lệnh PID | Module/đơn vị chuyển động riêng |
| **Inovance** | Tuỳ dòng | Tuỳ dòng |
| ⭐ **CODESYS** | Thư viện | ⭐ Thư viện theo **PLCopen Motion** |
| **Rockwell** | `PID` · `PIDE` | Lệnh chuyển động tích hợp |
| **Mức** | ⚠⚠ **KHÔNG tương đương** | ⚠⚠ **KHÔNG tương đương** |

> ⚠⚠ **Đây là hai hạng mục KHÔNG chuyển được giữa các hệ, và phải nói thẳng.**
>
> | Vì sao PID không tương đương | |
> |---|---|
> | ⭐ **Đơn vị tham số khác nhau** | Hệ số tích phân có thể là **thời gian** hoặc **nghịch đảo thời gian** |
> | Cấu trúc thuật toán khác nhau | Vị trí đặt khâu vi phân, cách chống bão hoà tích phân |
> | Cách xử lý chuyển tay/tự động khác nhau | |
>
> ⚠⚠ **Chép tham số PID từ hệ này sang hệ khác gần như chắc chắn cho kết quả sai** — và với vòng
> nhiệt độ trên máy thật, "sai" có thể nghĩa là hỏng sản phẩm hoặc quá nhiệt. ⭐ **Phải chỉnh lại từ
> đầu** (Chương 35).
>
> | Vì sao chuyển động không tương đương | |
> |---|---|
> | ⭐ Mô hình trục, cách về gốc, cách xử lý lỗi đều khác | |
> | ⭐ **PLCopen Motion** là nỗ lực chuẩn hoá — nhưng ⚠ **mức độ tuân thủ khác nhau** | |
> | ⚠ Phần an toàn của truyền động (STO) gắn chặt với phần cứng | Chương 36, 47 |

---

## A2.8 ⭐⭐ Cùng một đoạn trình tự, viết 5 lần

⭐ **Đoạn được chọn:** bước **S1.40** của DP-01 — *nâng kẹp board ở trạm 1*, chờ phản hồi thật, có
timeout báo lỗi (Phụ lục J §J.3.1).

> ⭐ Chọn bước này vì nó chứa **đúng những gì một bước trình tự thật phải có**: ra lệnh, chờ phản hồi,
> giới hạn thời gian, chuyển bước, và báo lỗi khi không đạt.

### Yêu cầu chung — giống nhau ở cả năm hệ

| # | Yêu cầu |
|---|---|
| 1 | Ở bước 40: bật `DO_Clamp1Vlv` |
| 2 | ⭐ **Chuyển sang bước 50 khi `DI_Clamp1Up` = 1** — phản hồi thật |
| 3 | ⚠ Nếu quá **2 giây** chưa có phản hồi → báo lỗi 3041, sang bước lỗi |
| 4 | ⭐ Bộ định thời chỉ để **báo lỗi**, không để chuyển bước |

### ⭐ CODESYS — cột neo (ST)

```text
CASE Stn1_Step OF
  40:
    DO_Clamp1Vlv := TRUE;
    tmrClamp1(IN := TRUE, PT := T#2S);      // thể hiện riêng cho bước này
    IF DI_Clamp1Up THEN
        tmrClamp1(IN := FALSE);
        Stn1_Step := 50;                     // ← phản hồi thật chuyển bước
    ELSIF tmrClamp1.Q THEN
        MaLoi := 3041;                       // ← timeout chỉ báo lỗi
        Stn1_Step := 900;
    END_IF;
END_CASE
```

### Siemens (SCL — rất gần CODESYS)

```text
CASE #Stn1_Step OF
  40:
    #DO_Clamp1Vlv := TRUE;
    #tmrClamp1(IN := TRUE, PT := T#2S);      // FB + Instance DB
    IF #DI_Clamp1Up THEN
        #tmrClamp1(IN := FALSE);
        #Stn1_Step := 50;
    ELSIF #tmrClamp1.Q THEN
        #MaLoi := 3041;
        #Stn1_Step := 900;
    END_IF;
END_CASE;
```

> ⭐ **Khác biệt so với CODESYS gần như chỉ là dấu `#` cho biến cục bộ** và việc bộ định thời cần
> Instance DB. Cấu trúc tư duy giống hệt — vì cả hai bám IEC 61131-3.

### Mitsubishi (Ladder — mô tả cấu trúc)

```text
// So sánh bước, không có CASE ở dòng cũ → dùng so sánh + nhánh

[LD=  D100  K40 ]───┬──[ SET  Y10 ]              // Y10 = DO_Clamp1Vlv
                    │
                    ├──[ OUT  T5  K20 ]           // ⚠ K20 = 2,0 s NẾU T5 là dải 100 ms
                    │
                    ├──[LD  X5]──[MOV K50 D100]   // X5 = DI_Clamp1Up → bước 50
                    │
                    └──[LD  T5]──┬──[MOV K3041 D200]
                                 └──[MOV K900  D100]
```

| ⚠ Điểm khác cần chú ý | |
|---|---|
| ⚠⚠ **`K20` phụ thuộc độ phân giải của `T5`** | ⭐ Phải kiểm dải; xem A2.2 |
| ⚠ **Không có `CASE`** ở dòng cũ | ⭐ Dùng so sánh `LD= D100 K40` cho mỗi bước |
| ⭐ **Số bước nằm trong thanh ghi `D100`** | Cùng ý tưởng, khác cách gọi |
| ⚠ Bộ định thời `T5` phải **xoá khi rời bước** | ⭐ Nếu không, lần sau vào bước nó đã chạy sẵn |

> ⚠⚠ **Hàng cuối là bẫy thật trên hệ kiểu thiết bị:** bộ định thời là **tài nguyên toàn cục**, không
> phải biến cục bộ của bước. ⭐ **Phải chủ động xoá nó khi rời bước** — điều mà thể hiện FB trên hệ
> khác xử lý tự nhiên hơn.

### Inovance (tuỳ dòng)

| Dòng | Cách viết |
|---|---|
| ⭐ Dòng nhỏ (AutoShop) | ⭐ **Gần Mitsubishi** — thiết bị `X`/`Y`/`M`/`D`/`T`, ladder tương tự |
| ⭐ Dòng dùng nền CODESYS (InoProShop) | ⭐⭐ **Gần CODESYS** — ST, thể hiện FB, kiểu `TIME` |

> ⭐ **Đây là ví dụ tốt cho luận điểm của Phụ lục A1: "một hãng" không phải một hệ.** Hai dòng của
> cùng hãng có thể thuộc **hai mô hình tư duy khác nhau** — nên ⚠ **luôn hỏi "dòng nào?" trước khi
> hỏi "hãng nào?"**.

### Rockwell (ST — mô tả cấu trúc)

```text
CASE Stn1_Step OF
  40:
    DO_Clamp1Vlv := 1;
    tmrClamp1.PRE := 2000;                   // ⭐ mili giây, không phải kiểu TIME
    tmrClamp1.TimerEnable := 1;
    TONR(tmrClamp1);
    IF DI_Clamp1Up THEN
        tmrClamp1.TimerEnable := 0;
        Stn1_Step := 50;
    ELSIF tmrClamp1.DN THEN
        MaLoi := 3041;
        Stn1_Step := 900;
    END_IF;
END_CASE;
```

| ⚠ Điểm khác cần chú ý | |
|---|---|
| ⭐ Thời gian là **mili giây dạng số**, không phải kiểu `TIME` | |
| ⭐ Bộ định thời là **tag kiểu `TIMER`** với các trường `.PRE` `.ACC` `.DN` | |
| ⚠⚠ **Ảnh I/O không đồng bộ với quét** | ⭐ Nếu đọc `DI_Clamp1Up` nhiều lần trong đoạn, ⭐ **sao chép nó vào biến ở đầu đoạn** (A1.5) |

### ⭐⭐ Điều rút ra từ năm bản

| Điều | |
|---|---|
| ⭐⭐ **Cấu trúc tư duy giống hệt nhau ở cả năm hệ** | Ra lệnh → chờ phản hồi thật → giới hạn thời gian → báo lỗi |
| ⭐ Khác biệt nằm ở **cú pháp và cách quản lý tài nguyên** | Không nằm ở cách nghĩ |
| ⚠ Ba chỗ khác biệt thật | Độ phân giải bộ định thời · phải tự xoá tài nguyên toàn cục · ảnh I/O |
| ⭐⭐ **Nắm được cách nghĩ thì đổi hệ là việc vài tuần** | ⚠ Chỉ nắm cú pháp một hệ thì đổi hệ là bắt đầu lại |

> ⭐⭐ **Đây là lý do thân sách dạy khái niệm theo IEC thay vì dạy một phần mềm cụ thể.**
>
> Phần mềm đổi phiên bản, hãng đổi dòng sản phẩm, công ty đổi nhà cung cấp. ⭐ **Cách nghĩ "chờ phản
> hồi thật, timeout chỉ để báo lỗi" thì đúng ở mọi hệ và đúng sau mười năm.**

---

## A2.9 ⭐ Danh mục khi chuyển chương trình sang hệ khác

⚠ **Đây là danh mục kèm với Chương 56 mục 56.4.**

| # | Kiểm | Mục |
|---|---|---|
| 1 | ⚠⚠ **Độ phân giải và cách đặt bộ định thời** | A2.2 |
| 2 | ⭐ Mỗi chỗ bắt cạnh có **bit nhớ / thể hiện riêng** chưa | A2.5 |
| 3 | ⚠⚠ **Vùng nhớ giữ được có sống sót qua nạp chương trình không** — ⭐ **thử thực tế** | A1.6 |
| 4 | ⭐ Ảnh I/O có cố định trong một vòng quét không | A1.5 |
| 5 | ⭐ Khối dùng ở nhiều chỗ có **bộ nhớ riêng** không | A1.4 |
| 6 | ⚠ Mã dựa vào **ô nhớ liền nhau** có còn hợp lệ không | A1.2 |
| 7 | ⚠⚠ **PID: chỉnh lại từ đầu**, không chép tham số | A2.7 |
| 8 | ⚠⚠ **Chuyển động: thiết kế lại**, không dịch | A2.7 |
| 9 | ⚠⚠ **Bộ đếm tốc độ cao: thiết kế lại** | A2.3 |
| 10 | ⚠ Thời gian quét khác → logic phụ thuộc vòng quét chạy khác | Ch.7, 56 |
| 11 | ⚠ Kiểu dữ liệu và điểm tràn số | Ch.14, Phụ lục K.6 |
| 12 | ⚠⚠ **Phần an toàn: KHÔNG chuyển — thiết kế và kiểm định lại** | Ch.47, 48, 56 |

> ⚠⚠ **Mục 12 là ranh giới cứng.** Chức năng an toàn được đánh giá và nghiệm thu như một tổng thể
> gắn với phần cứng cụ thể. ⭐ **Chuyển nền nghĩa là đánh giá lại**, không phải dịch chương trình
> (Chương 48, 56 mục 56.7).

> ⭐⭐ **Mười hai mục này là lý do câu "công cụ chuyển đổi tự động của hãng là điểm khởi đầu, không
> phải kết quả" (Chương 56 mục 56.6).** Công cụ dịch được cú pháp; ⚠ **nó không kiểm được một mục nào
> trong bảng trên**.

---

## A2.10 Dẫn về đâu

| Bạn cần | Đọc |
|---|---|
| ⭐ **Đối chiếu KHÁI NIỆM giữa 5 hệ** | ⭐ **Phụ lục A1** |
| Lệnh theo chuẩn IEC, không theo hãng | **Phụ lục B** |
| ⚠ Quy trình chuyển nền đầy đủ | ⚠ **Chương 56** |
| Trình tự đầy đủ của DP-01 | **Phụ lục J §J.3** |
| Vì sao chuyển bước bằng phản hồi thật | ⭐ **Chương 21** |

---

> ⚠⚠ **Nhắc lại giới hạn — quan trọng với phụ lục này hơn mọi phụ lục khác.**
>
> ⭐ **Mã ở A2.8 là mã minh hoạ cấu trúc, không phải mã chạy được nguyên văn.** Cú pháp chính xác, tên
> chân khối, cách khai báo biến và cách cấu hình bộ định thời phải lấy từ **tài liệu của dòng sản
> phẩm và phiên bản phần mềm bạn đang dùng**.
>
> ⚠ Phụ lục **mô tả khác biệt, không xếp hạng hãng**. Mỗi hệ có lý do riêng cho các lựa chọn thiết kế
> của nó, và ⭐ **hệ tốt nhất cho bạn thường là hệ mà nơi bạn làm việc đang dùng**.
>
> ⚠⚠ Riêng phần **an toàn**: không có bảng đối chiếu nào ở đây áp dụng được. Chức năng an toàn phải
> được thiết kế và kiểm định cho **hệ thống cụ thể**, bởi **người có thẩm quyền** (Chương 47, 48).
