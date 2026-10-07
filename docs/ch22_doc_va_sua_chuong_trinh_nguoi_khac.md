# Chương 22 — Đọc & sửa chương trình của người khác

> **Lát cắt máy mẫu:** 1 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp.

---

## 22.1 Kỹ năng chiếm phần lớn thời gian đi làm

Sách dạy lập trình PLC gần như luôn dạy **viết mới**: đây là ladder, đây là timer, hãy viết một
chương trình điều khiển băng tải.

Nhưng công việc thật không như vậy. Với phần lớn người làm nghề này, phần lớn thời gian là:

- máy đã có, chương trình đã có, **bạn phải sửa nó**;
- người viết đã nghỉ việc, hoặc ở công ty khác, hoặc không nhớ nữa;
- không có tài liệu, hoặc có tài liệu nhưng **không khớp với chương trình đang chạy**;
- máy đang sản xuất, và mỗi giờ nó dừng là tiền.

Đây là kỹ năng ít được dạy nhất và được dùng nhiều nhất. Chương này về nó.

> ⚠⚠ **Nguyên tắc bao trùm cả chương**
> Chương trình bạn sắp sửa **đang chạy một cỗ máy thật**, và nó đã chạy được. Điều đó có nghĩa là nó
> **đúng theo một cách nào đó mà bạn chưa hiểu**.
>
> Mỗi lần bạn thấy một đoạn code "thừa" hoặc "sai" và muốn dọn nó đi, hãy giả định rằng nó ở đó vì
> một lý do — thường là một sự cố đã xảy ra và không ai ghi lại. Xoá nó nghĩa là mời sự cố đó quay
> lại, vào lúc bạn không có mặt.

---

## 22.2 Đọc trước, sửa sau — quy trình sáu bước

Đừng mở phần mềm rồi bắt đầu đọc từ dòng đầu tiên. Chương trình PLC không đọc tuyến tính được, và
đọc hết một chương trình lớn có thể mất nhiều ngày.

Đọc **theo mục tiêu**:

| Bước | Việc | Xong khi |
|---|---|---|
| 1 | **Xác định câu hỏi** cụ thể bạn cần trả lời | Viết được nó thành một câu |
| 2 | **Lấy bản sao lưu** của chương trình đang chạy | File đã nằm ở nơi an toàn, có ghi ngày |
| 3 | **Dựng bản đồ**: chương trình có những phần nào | Liệt kê được các POU và việc của từng cái |
| 4 | **Truy ngược từ triệu chứng** tới nguyên nhân | Tìm được đoạn code liên quan |
| 5 | **Hiểu đoạn đó** — cả những chỗ trông thừa | Giải thích được cho người khác |
| 6 | **Sửa nhỏ nhất có thể**, rồi ghi lại | Có thể quay lui trong một phút |

Bước 1 quan trọng hơn nó có vẻ. *"Hiểu chương trình này"* không phải câu hỏi — nó là một cái hố không
đáy. *"Vì sao van kẹp trạm 1 không mở khi có board"* mới là câu hỏi, và nó dẫn thẳng tới một nhánh
nhỏ của chương trình.

---

## 22.3 ⭐ Tham chiếu chéo — công cụ quan trọng nhất

**Tham chiếu chéo** *(cross-reference)* trả lời câu hỏi: **"tag này được dùng ở những đâu?"**

Mọi phần mềm lập trình PLC đều có chức năng này, và nó là **công cụ năng suất nhất** khi đọc chương
trình của người khác. Nếu bạn chỉ học một thứ từ chương này, hãy học thứ này.

### Ba câu hỏi mà nó trả lời

| Câu hỏi | Vì sao quan trọng |
|---|---|
| **Ai GHI vào tag này?** | ⭐ Câu quan trọng nhất — xem bên dưới |
| **Ai ĐỌC tag này?** | Biết sửa nó thì ảnh hưởng tới đâu |
| Tag này có được dùng không? | Tag không ai dùng là dấu hiệu của code chết |

### Vì sao "ai ghi vào" là câu quan trọng nhất

Triệu chứng thường gặp: một giá trị **sai mà không biết từ đâu ra**. Một cờ lên khi lẽ ra phải xuống.
Một ngõ ra tắt trong khi nấc thang điều khiển nó đang đúng.

Nguyên nhân gần như luôn là: **có một chỗ khác cũng ghi vào tag đó**, và bạn chưa biết chỗ đó.

Đây chính là lỗi cuộn dây trùng ở Chương 15 (Bẫy 1) và ghi trùng ngõ ra ở Chương 20 (Bẫy 2) — nhưng
khi đọc chương trình của người khác, bạn không biết trước là nó có tồn tại hay không.

> 💡 **Quy trình ba mươi giây**
> Với **mọi** tag bạn đang nghi ngờ: chạy tham chiếu chéo, lọc lấy các chỗ **ghi**, và đếm.
> - Đúng một chỗ ghi → tốt, đọc chỗ đó.
> - Nhiều hơn một → ⭐ **gần như chắc chắn đây là vấn đề của bạn.** Chỗ chạy sau thắng, và "sau" phụ
>   thuộc thứ tự gọi POU (Chương 14, mục 14.7).
> - Không chỗ nào ghi mà giá trị vẫn đổi → tag được ghi từ ngoài: màn hình vận hành (Chương 44), hệ
>   thống trên (Chương 42), hoặc ai đó đang cưỡng bức (Chương 51).

Trường hợp cuối đáng nhớ. Một giá trị đổi mà không có dòng code nào ghi vào nó là dấu hiệu kinh điển
của **một lệnh cưỡng bức bị quên** — và đó là tai nạn chờ xảy ra.

### Điều tham chiếu chéo **không** làm được

- Không tìm được chỗ ghi **gián tiếp** qua chỉ số mảng tính toán được (`Data[i] := …`).
  ⭐ **Đây là giới hạn lớn nhất, và nó có cách đi vòng — mục 22.3b.**
- Không biết tag đó có được ghi từ **bên ngoài PLC** không.
- Không nói cho bạn **vì sao** người ta ghi vào đó.

---

## 22.3b ⭐⭐ Tham chiếu chéo khi chương trình dùng CHỈ SỐ

Mục 22.3 kết thúc bằng một dòng thừa nhận: ⚠ *tham chiếu chéo không tìm được chỗ ghi gián tiếp qua
chỉ số tính toán được*. ⭐ Mục này trả lời câu đứng ngay sau đó — **vậy làm thế nào?** — vì với máy
lớn thì **gần như toàn bộ chương trình là chỉ số**.

### Vì sao chỉ số làm hỏng tham chiếu chéo

Cả hai kiểu dưới đây đều làm công cụ bó tay, và chúng là hai kiểu khác nhau:

| Kiểu | Trông ra sao | ⚠ Công cụ trả lời được gì |
|---|---|---|
| **Chỉ số vào mảng** | `Cyl[i].Cmd.Req := TRUE;` | Tra `Cyl` → ra **mọi** xy-lanh. Tra `Cyl[12]` → ⚠ **không ra gì**, vì trong mã không có chữ `12` |
| **Thanh ghi chỉ số** *(index register)* | `D100Z1` — địa chỉ cộng thêm nội dung một thanh ghi | ⚠ Càng khó hơn: **địa chỉ thật chỉ tồn tại lúc chạy** |

> ⭐ **Điểm chung của cả hai: cái bạn muốn tra (phần tử số 12) KHÔNG XUẤT HIỆN trong mã nguồn.** Nên
> dù công cụ có tốt tới đâu, nó cũng không thể tìm ra thứ không được viết ra.

### ⭐⭐ Bảy cách làm việc — xếp theo thứ tự nên thử

| # | Cách | Khi nào dùng |
|---|---|---|
| 1 | ⭐⭐ **Tra theo TRƯỜNG, đừng tra theo phần tử** | Luôn luôn — xem bên dưới |
| 2 | ⭐⭐ **Tra biến CHỈ SỐ, không tra mảng** | Khi hỏi *"ai chạm vào số 12"* |
| 3 | ⭐ **Đổi chỉ số thành hằng có tên** | Khi bạn còn quyền sửa chương trình |
| 4 | ⭐ **Đọc chương trình con CẤU HÌNH trước tiên** | Khi mới nhận một chương trình lạ |
| 5 | **Tìm trong bản xuất văn bản** | Khi cần bắt các chỗ viết chỉ số **cứng** |
| 6 | ⭐ **Chuyển sang xem trực tuyến** | Khi tra tĩnh đã bó tay |
| 7 | ⚠ **Sửa thiết kế** để lần sau tra được | Khi bạn là người viết |

### ① Tra theo TRƯỜNG, không theo phần tử

⭐ Đây là cách đảo ngược câu hỏi, và nó giải quyết phần lớn trường hợp.

| ⚠ Câu hỏi bó tay | ⭐ Câu hỏi trả lời được |
|---|---|
| *"Chỗ nào ghi vào `Cyl[12].Cmd.Req`?"* | *"Chỗ nào ghi vào **`.Cmd.Req` của bất kỳ xy-lanh nào**?"* |

⚡ Nghe như trả lời rộng hơn, nhưng thực tế nó **hẹp lại**: trong một chương trình có kỷ luật, số
chỗ ghi vào trường đó thường chỉ là **hai hoặc ba** — khối cơ cấu, chế độ tay, và tầng chống va chạm
(Chương 27 mục 27.3b).

> ⭐⭐ **Và đó chính là câu trả lời bạn cần.** Câu hỏi thật không phải *"ai ghi vào số 12"* mà là
> *"có bao nhiêu nơi có thể ghi vào một cái bất kỳ"*. ⚠ Nếu con số đó là **ba** thì bạn đọc ba chỗ
> là xong. ⚠⚠ Nếu nó là **mười lăm** thì bạn vừa tìm ra vấn đề thật của chương trình, và nó không
> phải vấn đề của xy-lanh số 12.

### ② Tra biến CHỈ SỐ, không tra mảng

⭐ Đổi câu hỏi *"ai ghi vào phần tử 12"* thành **"biến chỉ số nhận giá trị 12 ở đâu"**.

```iecst
// Không tra Cyl[...] — tra chính biến i
FOR i := 1 TO CYL_COUNT DO        // ⭐ chỉ số chạy hết dải: "ai ghi" = vòng lặp này
    FB_Cyl[i](Cmd := Cyl[i].Cmd, ...);
END_FOR;

Cyl[HmiCylNo].Cmd.ManualTrig := …;   // ⚠ chỉ số đến từ NGOÀI — tra HmiCylNo
```

| Chỉ số đến từ đâu | ⭐ Kết luận ngay |
|---|---|
| Một **vòng lặp chạy hết dải** | ⭐ "Ai ghi" = vòng lặp đó. **Xong** — không cần tra thêm |
| Một biến do **nơi khác đặt** | ⭐ Tra biến đó; đây mới là chỗ cần đọc (Chương 44 mục 44.2b) |
| Một **phép tính** | ⚠⚠ Chỗ nguy hiểm nhất — xem cảnh báo cuối mục |

### ③ Đổi chỉ số thành hằng có tên

```iecst
// ⚠ Tra "12" thì ra cả trăm chỗ vô can
Cyl[12].Cmd.Req := TRUE;

// ⭐ Tra CYL_CLAMP_STN1 thì ra ĐÚNG những chỗ liên quan tới nó
Cyl[CYL_CLAMP_STN1].Cmd.Req := TRUE;
```

> ⭐⭐ **Một dòng khai báo hằng lấy lại toàn bộ sức mạnh của tham chiếu chéo cho một phần tử.** Đây là
> cách rẻ nhất trong cả mục, và nó còn làm tên **tự giải thích** — không phải tra bảng nữa
> (Chương 30 mục 30.2b).

### ④ Đọc chương trình con CẤU HÌNH trước tiên

⭐ Chương trình dùng chỉ số **bắt buộc** phải có một chỗ gán *"chỉ số nào là cơ cấu nào"*. Tìm nó
trước khi đọc bất cứ thứ gì khác — thường tên có chữ *config* hoặc *mapping*, và nó là **bản đồ**
của cả chương trình.

⚠ Nếu không tìm thấy chỗ đó, hãy dừng lại và hỏi. ⭐ Đọc một chương trình đánh chỉ số mà không có
bảng tra thì **không phải đọc chậm — mà là không đọc được** (Chương 30 mục 30.2b).

### ⑤ Tìm trong bản xuất văn bản

⭐ Xuất chương trình ra văn bản (Chương 30 mục 30.6) rồi tìm chuỗi `[12]` bằng công cụ tìm kiếm
thường. ⚡ Nó bắt được đúng thứ tham chiếu chéo hay bỏ sót: **những chỗ ai đó viết chỉ số CỨNG** —
và những chỗ đó thường chính là ngoại lệ mà người viết cài vào rồi quên.

### ⑥ Khi tra tĩnh bó tay — chuyển sang xem trực tuyến

⚠ Nếu chỉ số là kết quả một phép tính, không công cụ tĩnh nào lần ra được. ⭐ Khi ấy đổi chiến thuật:

| Làm gì | Vì sao được |
|---|---|
| Mở cửa sổ xem **đúng phần tử 12** và cả **biến chỉ số** | Thấy giá trị đổi **lúc nào** |
| Chạy từng thao tác một, xem giá trị nào đổi theo | ⭐ Thu hẹp còn đúng thao tác gây ra |
| Đặt một điểm dừng hoặc một cờ ghi lại khi phần tử 12 đổi | Chương 51 |

### ⑦ Nếu bạn là người viết — bốn luật để lần sau tra được

| # | Luật | Nó mua cho bạn cái gì |
|---|---|---|
| 1 | ⭐⭐ **Mỗi mảng chỉ có MỘT nơi ghi** — thường là vòng gọi khối | Tra theo trường ra **một** kết quả, không phải mười lăm |
| 2 | ⭐ **Chỉ số cố định luôn là hằng có tên** | Lấy lại tham chiếu chéo cho từng phần tử |
| 3 | ⭐ **Mỗi biến chỉ số dùng cho đúng một mục đích** — đừng dùng lại `i` cho việc khác trong cùng khối | ⚠ Dùng chung là cách nhanh nhất để mất dấu |
| 4 | ⚠ **Ghi lại mọi chỗ ghi chỉ số CỨNG** như một ngoại lệ có chủ ý | Ngoại lệ không ghi lại = quả mìn cho người sau |

> ⚠⚠ **Cạm bẫy cuối, và là cái nguy hiểm nhất của cả cách viết theo chỉ số:**
>
> ⭐ **Chỉ số ngoài dải không sai cú pháp.** `Cyl[30]` khi mảng chỉ có 20 phần tử vẫn biên dịch được.
> Tuỳ hệ, nó sẽ **dừng CPU**, hoặc ⚠⚠ **ghi đè lên vùng nhớ nằm cạnh** — nghĩa là một cơ cấu **hoàn
> toàn khác** bỗng nhận lệnh, và tham chiếu chéo **không bao giờ chỉ ra được** điều đó.
>
> ⭐ Vì vậy **mọi chỉ số đến từ bên ngoài đều phải chặn dải trước khi dùng** — đúng như mẫu ở
> Chương 44 mục 44.2b. ⚡ Đây là lý do thật của việc chặn dải: không phải cho sạch sẽ, mà vì
> **không có công cụ nào cứu bạn nếu bỏ qua nó.**

### ⭐ Còn khi chương trình không dùng tên mà dùng thẳng địa chỉ

Có một kiểu chương trình khác, rất phổ biến ở nền cũ và ở các hệ đánh địa chỉ theo thiết bị: ⚠ **hầu
như không khai báo tên biến nào cả**, mà dùng thẳng `X3`, `Y5`, `M20`, `D13`, và **ý nghĩa nằm trong
CHÚ THÍCH THIẾT BỊ** *(device comment)* gắn với từng địa chỉ.

⚡ Với kiểu này, tham chiếu chéo **lại hoạt động rất tốt** — vì địa chỉ là chuỗi có thật trong mã.
⚠ Nhưng đổi lại hai thứ:

| ⚠ Vấn đề | Hệ quả khi đọc |
|---|---|
| ⚠⚠ **Chú thích gắn với ĐỊA CHỈ, không gắn với ý nghĩa** | Đổi cách đánh địa chỉ thì chú thích **ở lại với địa chỉ cũ** — và nó thành sai |
| ⚠⚠ **Mất tệp chú thích là mất toàn bộ ý nghĩa** | Chương trình còn chạy, nhưng đọc `M20` thì không biết là gì. ⭐ Tệp chú thích phải nằm trong danh mục sao lưu (Chương 54) |
| ⚠ Kiểu này thường đi kèm **thanh ghi chỉ số** | Khi đó lại rơi về đúng bài toán ở đầu mục này |

> ⭐⭐ **Chốt lại cho cả mục — và đây là câu đáng mang đi:**
>
> **Tham chiếu chéo không phải một nút bấm, mà là một CÁCH ĐẶT CÂU HỎI.** ⚠ Hỏi *"ai ghi vào số
> 12"* thì công cụ chịu. ⭐ Hỏi *"có mấy nơi ghi vào trường này"*, *"chỉ số nhận giá trị ở đâu"*,
> *"bảng tra nằm ở đâu"* — thì cùng một công cụ đó trả lời được hết.

---

## 22.4 Dựng bản đồ chương trình

Trước khi lao vào chi tiết, dành hai mươi phút dựng bản đồ. Nó tiết kiệm nhiều giờ sau đó.

| Việc | Cách làm |
|---|---|
| **Liệt kê POU** | Mở danh sách các khối của dự án, ghi tên từng khối và đoán việc của nó từ tên |
| **Tìm điểm vào** | POU nào được tác vụ gọi trực tiếp? Nó gọi những POU nào, theo thứ tự nào? |
| **Tìm nơi ghi ngõ ra** | Tham chiếu chéo vài tag `DO_` — chúng tập trung ở một POU hay rải khắp nơi? |
| **Tìm biến trạng thái** | Có biến kiểu "số bước" hoặc "chế độ" không? Nó là xương sống của trình tự |
| **Đọc bảng tag** | Tên tag cho biết rất nhiều về cách người viết tổ chức tư duy |

> 💡 **Câu hỏi chẩn đoán nhanh: ngõ ra được ghi tập trung hay rải rác?**
> Tập trung ở một POU → người viết có kỷ luật, chương trình có cấu trúc, bạn sẽ đọc được.
> Rải khắp nơi → ⚠ chuẩn bị tinh thần: mỗi thay đổi đều có rủi ro tác dụng phụ, và tham chiếu chéo
> sẽ là công cụ bạn dùng liên tục.

---

## 22.4b ⭐⭐ Thứ lẽ ra bạn phải nhận được — và việc nên làm khi không có

Mục trên dựng bản đồ chương trình **từ con số không**. Đáng hỏi tiếp: ⭐ *vì sao phải dựng lại thứ
lẽ ra đã có sẵn?*

Một bộ hồ sơ đầy đủ luôn mở đầu bằng một **bản tóm tắt hệ thống** — vài trang mô tả toàn cảnh, gồm
ba phần:

| Phần | Trả lời câu hỏi |
|---|---|
| ⭐ **Phát biểu bài toán điều khiển** | *Máy này giải quyết việc gì?* |
| ⭐⭐ **Chiến lược thiết kế** | *Các khối phần cứng và phần mềm chính làm gì — và ⭐ **VÌ SAO chọn chúng**?* |
| **Mục tiêu phải đạt** | *Đo bằng gì thì gọi là đạt?* |

> ⭐⭐ **Phần thứ hai là phần đắt nhất, và cũng là phần luôn mất trước.**
>
> Sơ đồ đấu dây và bảng địa chỉ thì còn — vì thiếu chúng thì **không đấu được máy**. ⚠ Nhưng
> *"vì sao chọn cách này"* thì ⭐ **không ai cần tới để máy chạy**, nên nó không được viết ra, và
> người sau phải **đoán** (Chương 30).
>
> ⚡ Đó chính là lý do mục 22.5 tồn tại: đọc code không chú thích **là hệ quả của việc này**, không
> phải một kỹ năng đáng tự hào.

### ⭐ Khi bạn đã dựng xong bản đồ — hãy viết bản tóm tắt đó ra

Đây là đề nghị thực dụng nhất của cả chương:

> ⭐⭐ **Bạn vừa phải bỏ công dựng lại hiểu biết về cỗ máy. Đừng để công đó chết trong đầu bạn.**
>
> Viết ra **hai tới ba trang** theo đúng ba phần trên, kèm những gì bạn đã **suy ra** và ⚠ **đánh dấu
> rõ chỗ nào là suy đoán chưa xác nhận**.

| Bạn được gì | Người sau được gì |
|---|---|
| ⭐ Viết ra mới phát hiện chỗ mình **tưởng đã hiểu mà chưa** | ⭐ **Không phải làm lại từ đầu** việc bạn vừa làm |
| Có căn cứ khi cần giải trình một thay đổi | Biết chỗ nào là **sự thật** và chỗ nào là **suy đoán của bạn** |
| ⭐ Người bàn giao đọc lại có thể **đính chính** cho bạn | Có cái để đính chính tiếp |

> ⭐ **Và một mục nữa nên có ngay từ đầu: người và thời điểm.** Ai viết chương trình gốc, ai đã sửa,
> sửa khi nào. ⚠ Với chương trình *"chắp vá qua nhiều đời"* ở mục 22.6, ⭐ **biết được đời nào làm gì
> đã là nửa lời giải**.

> ⚡ **Vì sao đây không phải việc thừa:** hồ sơ tồn tại để trả lời câu hỏi, chẩn đoán sự cố, và ⭐ **sửa
> chương trình khi yêu cầu thay đổi** — ba việc mà **chính bạn** sẽ phải làm lần sau, trên cùng cỗ
> máy này. ⚠ Người bạn đang giúp trước hết là **bạn của sáu tháng tới**.

---

## 22.5 Đọc code không có chú thích

Đây là tình huống phổ biến nhất. Không có chú thích, hoặc chú thích bằng ngôn ngữ bạn không đọc được,
hoặc chú thích chỉ lặp lại code.

### Nguồn thông tin thay thế, theo thứ tự giá trị

| Nguồn | Giá trị | Ghi chú |
|---|---|---|
| **Tên tag** | ⭐ Cao nhất | Ngay cả tên xấu cũng nói được nhóm và chức năng |
| **Bảng I/O và sơ đồ điện** | ⭐ Cao | Cho biết tín hiệu **thật** là gì, tag chỉ là cái tên |
| **Quan sát máy chạy** | ⭐ Rất cao | Xem trực tuyến trong lúc máy chạy chu trình — thấy thứ tự thật |
| Cấu trúc chương trình | Trung bình | Thứ tự gọi POU cho biết ý đồ tổ chức |
| Tên POU và nhóm nấc thang | Trung bình | |
| Tài liệu bàn giao | ⚠ Thay đổi | Có thể đã lỗi thời — **luôn đối chiếu với chương trình thật** |

> ⭐ **Kỹ thuật hiệu quả nhất: xem trực tuyến trong lúc máy chạy một chu trình.**
> Mở chế độ giám sát, cho máy chạy một chu trình chậm hoặc từng bước, và **nhìn giá trị đổi**. Trong
> mười phút bạn hiểu trình tự nhiều hơn hai giờ đọc code tĩnh.
>
> Đây cũng là lý do ladder vẫn thống trị ở tầng máy (Chương 20, mục 20.6): nó **cho xem được** trạng
> thái ngay trên hình.

### Nhận diện "phương ngữ nhà"

Mỗi công ty tích luỹ một bộ quy ước riêng qua nhiều năm — cách đặt tên, cách chia khối, những khối
tiện ích dùng lại, cách đánh số bước.

Nhận ra phương ngữ này **rất đáng làm**, vì một khi hiểu quy tắc thì cả chương trình sáng ra cùng lúc.

| Dấu hiệu phương ngữ | Cách giải mã |
|---|---|
| Tiền tố tag lạ (`P_`, `S_`, `Z_`…) | Tìm vài tag cùng tiền tố, xem chúng có gì chung |
| Số bước nhảy cách đều (10, 20, 30) | Chừa chỗ chèn bước — quy ước rất phổ biến |
| Số bước theo trạm (S1.20, S2.20) | Trạm và bước ghép trong một con số |
| Khối tiện ích xuất hiện khắp nơi | Đọc **một** lần cho kỹ, rồi bạn hiểu mọi chỗ dùng nó |
| Nấc thang trống có chú thích | Dùng làm **tiêu đề nhóm** — đọc chúng trước để có dàn ý |

> 💡 Nếu tiếp quản nhiều máy của cùng một nhà chế tạo, **ghi lại phương ngữ của họ** thành một trang.
> Máy thứ hai bạn sẽ đọc nhanh gấp nhiều lần.

---

## 22.6 ⚠ Chương trình bị sửa chắp vá qua nhiều đời

Một máy mười năm tuổi thường đã qua tay năm, sáu người. Dấu hiệu và cách xử lý:

| Dấu hiệu | Nghĩa là | Xử lý |
|---|---|---|
| **Nhiều phong cách đặt tên** trong cùng chương trình | Nhiều người, không ai áp quy ước | Chấp nhận; đừng dọn (xem cảnh báo bên dưới) |
| Đoạn code **bị vô hiệu hoá** (nhánh không bao giờ đúng) | Ai đó tắt một chức năng nhưng không xoá | ⚠ **Tìm hiểu vì sao trước khi động vào** |
| Cùng một logic viết **hai lần** ở hai chỗ | Người sau không tìm thấy chỗ cũ nên viết lại | Nguy hiểm — hai chỗ có thể xung đột |
| Tag tên `Temp1`, `Test`, `New_Motor2` | Sửa gấp, chưa bao giờ dọn | Rất có thể vẫn đang được dùng — kiểm tham chiếu chéo |
| Timer với thời gian đặt "lạ" (2,7 s) | ⭐ Con số này **đến từ thực nghiệm** | **Đừng làm tròn** — xem bên dưới |
| Chú thích kiểu "đừng sửa dòng này" | Có sự cố đã xảy ra | ⭐ Tin nó. Tìm hiểu, đừng bỏ qua |

> ⚠⚠ **NGUY HIỂM — cám dỗ lớn nhất khi tiếp quản: dọn dẹp**
> Bạn mở một chương trình lộn xộn, thấy ngay mười chỗ có thể làm gọn hơn. Đừng.
>
> - Mỗi thay đổi là một rủi ro, và bạn **chưa hiểu hết** chương trình.
> - Đoạn code "thừa" thường ở đó vì một sự cố đã xảy ra mà không ai ghi lại.
> - Con số "lạ" như `T#2700MS` gần như luôn là **kết quả chỉnh thực nghiệm trên máy thật**. Làm tròn
>   nó thành 3 giây có thể phá một thứ đã chạy đúng nhiều năm.
> - Nếu bạn dọn dẹp và máy hỏng, **bạn** là người phải giải thích — dù đoạn code đó vốn đã tệ.
>
> **Sửa cái bạn được yêu cầu sửa. Ghi lại những chỗ bạn muốn dọn, và đề xuất riêng như một công việc
> có kế hoạch, có thời gian dừng máy, có kiểm thử.**

---

## 22.6b ⭐⭐ Năm chỗ phải soi khi nhận một chương trình làm sẵn

Mục 22.6 là dấu hiệu của chương trình bị sửa qua nhiều đời. Mục này nói một loại khác: lỗi **nằm im**
trong một chương trình **đang chạy tốt**. Đọc mã của một máy đang sản xuất — khung chương trình chuẩn
của một nhóm kỹ thuật, dùng lại qua nhiều máy — cho thấy năm loại. ⭐ Cả năm có chung hai đặc điểm:
biên dịch **không báo gì**, và máy vẫn chạy **gần như mọi lúc**. Và mỗi loại tìm được bằng **một phép
tìm** trong bản xuất văn bản (mục 22.3b, cách ⑤) hoặc bằng tham chiếu chéo.

### ① Biến điều kiện bị gán cứng

```iecst
// ✗ hai dòng thật sự gặp — tên đã đổi
M_NoInterference := TRUE;                    // phép kiểm chưa ai viết — gán cứng cho chạy được
// M_GuardsClosed := X_Guard1 AND X_Guard2;  // dòng tính thật đã bị biến thành chú thích
M_GuardsClosed := TRUE;
```

| | |
|---|---|
| **Vì sao nguy** | Khung chương trình để sẵn **chỗ** cho một phép kiểm, rồi người làm máy gán cứng cho chạy được. ⚠ **Cái tên vẫn còn** — người đọc, kể cả người nghiệm thu, tưởng phép kiểm còn |
| **Tìm thế nào** | Tìm mọi dòng **gán hằng** đứng ngoài `IF`: `:= TRUE;`, `:= FALSE;`. Với mỗi kết quả hỏi: *tên này có phải tên của một ĐIỀU KIỆN không* — kiểu *…OK*, *…Closed*, *…Ready*, *No…* |
| **Sửa** | Viết phép kiểm thật; hoặc xoá biến và ghi rõ *"máy này không có …"*. ⚠ Không để một cái tên nói dối. Biến thuộc **thiết bị bảo vệ người** thì không phải việc sửa trong chương trình thường — báo người phụ trách an toàn (Chương 47) |
| **✅ Đạt khi** | Mọi biến mang tên điều kiện có **ít nhất một** chỗ gán từ tín hiệu thật — kiểm bằng tham chiếu chéo |

### ② Sườn đã tính mà không ai dùng — lệnh chạy theo MỨC

```iecst
// ✗ thể hiện bắt sườn được gọi đều đặn… nhưng không ai đọc .Q của nó
StartEdge(CLK := M_StartCmd);                // M_StartCmd = nút Start OR bit Start từ màn hình
IF M_StartCmd AND M_Ready AND M_AutoMode THEN
    M_Running := TRUE;                       // ⚠ chạy theo MỨC của lệnh, không theo sườn
END_IF;
```

| | |
|---|---|
| **Vì sao nguy** | ⚠⚠ Lệnh Start **kẹt ở 1** — tiếp điểm dính, hay bit từ màn hình kẹt vì mất kết nối đúng lúc đang nhấn (Chương 44, Bẫy 14) — thì máy **tự chạy lại** ngay khi lỗi vừa được xoá: đúng thứ *"khởi động lại phải có chủ ý"* cấm (Chương 16 mục 16.6) |
| **Tìm thế nào** | Liệt kê mọi thể hiện `R_TRIG`/`F_TRIG`, tham chiếu chéo `.Q` của từng cái. ⭐ Thể hiện được **gọi** mà `.Q` **không ai đọc** là dấu hiệu gần như chắc chắn: người viết định dùng sườn rồi quên |
| **Sửa** | Lấy sườn: `IF StartEdge.Q AND M_Ready AND M_AutoMode THEN` |
| **✅ Đạt khi** | Giữ nút Start, gây một lỗi rồi xoá lỗi → máy **không** chạy lại cho tới khi nhả nút và nhấn lần nữa |

### ③ Nhịp tự tạo nhanh hơn tác vụ — rồi đo thời gian bằng cách đếm nhịp

Chương trình tự tạo một nhịp *"100 Hz"* — 5 ms bật, 5 ms tắt, dựng bằng hai `TON` nối vòng — trong một
tác vụ *(task)* chu kỳ **4 ms**; một bộ đếm cộng 1 mỗi vòng quét mà nhịp đang bật, rồi đọc kết quả như
*"số lần 10 ms"* để đo thời gian một thao tác.

| | |
|---|---|
| **Vì sao sai** | `TON` chỉ được xét **lúc được gọi** (Phụ lục B mục B.9b), nên nửa chu kỳ không thể ngắn hơn một chu kỳ tác vụ và bị **làm tròn lên**. Chạy thử đúng đoạn mã đó: trong tác vụ 4 ms, mỗi nửa chu kỳ dài **12 ms** chứ không phải 5 ms; phép đo bằng đếm nhịp **dư 25 %**. Cùng đoạn mã ấy chuyển sang tác vụ 2 ms thì dư **150 %** — ⚠ con số sai đổi theo chu kỳ tác vụ, nên không *"chỉnh hệ số"* mà chữa được |
| **Tìm thế nào** | Mọi khối tạo nhịp tự viết có thời gian đặt **≤ 2 lần** chu kỳ tác vụ; mọi dòng dạng `IF Clock… THEN X := X + 1` |
| **Sửa** | Đo thời gian bằng `ET` của một `TON`, hoặc bằng hiệu hai lần đọc đồng hồ hệ thống. Nhịp tự tạo chỉ dùng để **nháy đèn**, với nửa chu kỳ **[Nghề] ≥ 10 lần** chu kỳ tác vụ — sai số làm tròn khi đó dưới 10 % |
| **✅ Đạt khi** | Phép đo thời gian của chương trình khớp đồng hồ bấm hoặc bản ghi theo thời gian, sai không quá **một chu kỳ tác vụ** |

### ④ Một vế bị chép trùng

```iecst
// ✗ dòng thật: được chạy tay khi KHÔNG lỗi, hoặc khi lỗi chỉ là đang chạm giới hạn
M_ManualAdmit := (NOT M_AxisFault OR M_PosLimitHit OR M_PosLimitHit) AND M_ManualMode;
//                                                      ⚠ lẽ ra là M_NegLimitHit
```

| | |
|---|---|
| **Vì sao nguy** | Chép một dòng rồi sửa thiếu. Biên dịch không báo, máy chạy được; sai chỉ lộ ở **trường hợp đối xứng hiếm gặp** — ở đây: chạm giới hạn **âm** mà trục báo lỗi thì không chạy tay ra được, đúng lúc người ta cần nhất |
| **Tìm thế nào** | Tìm biểu thức có **cùng một tên hai lần** trong một chuỗi `OR`/`AND` — một biểu thức chính quy như `(\b[\w.]+\b) (OR\|AND) \1\b` trên bản xuất văn bản. ⭐ Soi kỹ các cặp đối xứng: trái/phải, dương/âm, trên/dưới, trạm 1/trạm 2 |
| **Sửa** | Sửa vế; thêm phép thử phía đối xứng vào danh mục kiểm |
| **✅ Đạt khi** | Với **mỗi** cặp đối xứng, đã thử **cả hai phía** trên bàn hoặc trên máy |

### ⑤ Hai tác vụ cùng ghi một biến

Trình tự chạy ở tác vụ chính **đặt** cờ lệnh của một trục; khối điều khiển trục chạy ở tác vụ nhanh hơn,
ưu tiên cao hơn, **xoá** cờ đó khi làm xong.

| | |
|---|---|
| **Vì sao nguy** | Tác vụ ưu tiên cao chen vào **giữa** vòng quét của tác vụ thấp (Chương 27 mục 27.6). Tác vụ thấp đọc cờ đầu vòng, tác vụ cao xoá nó giữa chừng, tác vụ thấp ghi lại giá trị cũ cuối vòng — lệnh **chạy hai lần** hoặc **mất**. ⚠ Lỗi hiếm, và **không tái hiện** được khi ngồi xem trực tuyến |
| **Tìm thế nào** | Tham chiếu chéo, lọc các chỗ **ghi** (mục 22.3), rồi ghi cạnh mỗi chỗ: chương trình đó **chạy ở tác vụ nào**. Một biến có chỗ ghi ở hai tác vụ là dấu hiệu |
| **Sửa** | Mỗi biến **một** tác vụ ghi. Lệnh và xác nhận tách làm hai biến — bên ra lệnh ghi lệnh, bên làm ghi xác nhận — cùng ý với cách *số thứ tự* ở Chương 39 mục 39.9b |
| **✅ Đạt khi** | Bảng *"biến ↔ tác vụ ghi"* không có dòng nào mang hai tác vụ |

> ⭐⭐ **Vì sao năm chỗ này đáng soát TRƯỚC mọi việc khác:** chúng không gây triệu chứng hôm bạn nhận
> máy. Chúng gây triệu chứng vào một đêm nào đó — Start kẹt, chạm giới hạn âm, hai tác vụ đụng nhau đúng
> một micro-giây — và khi ấy **người sửa cuối cùng** là người bị hỏi. ⚡ Năm phép tìm mất chưa tới một
> giờ; ghi kết quả vào bản tóm tắt hệ thống (mục 22.4b) như một danh sách *"đã biết"*.

---

## 22.7 ⭐ Quy tắc sửa an toàn

Bốn bước, theo đúng thứ tự. Không bỏ bước nào, kể cả khi "chỉ sửa một dòng".

### 1. Hiểu trước

Trước khi sửa, phải trả lời được **ba câu**:

- Đoạn này đang làm gì?
- Vì sao nó được viết như vậy? (Nếu không biết, ít nhất phải biết là mình không biết.)
- Sửa nó thì **còn gì khác bị ảnh hưởng**? — dùng tham chiếu chéo để trả lời.

Câu thứ ba là câu người ta hay bỏ, và là câu gây ra phần lớn tai nạn khi sửa.

### 2. Sao lưu

> ⚠⚠ **Lấy bản sao lưu của chương trình ĐANG CHẠY, trước khi sửa bất cứ thứ gì.**
>
> - Sao lưu **từ CPU đang chạy**, không phải từ file trên máy tính bạn — hai thứ đó có thể **khác
>   nhau**, và bản trong CPU mới là bản đang điều khiển máy.
> - Sao lưu **cả cấu hình phần cứng và tham số**, không chỉ chương trình.
> - Đặt tên có **ngày và ghi chú**: `DP01_2026-09-01_truoc-khi-sua-timeout-tram1`.
> - ⚠ Bản sao lưu **chưa thử khôi phục không phải bản sao lưu** (Chương 54).

Đây là bước duy nhất bảo đảm bạn quay lui được. Nó tốn năm phút.

### 3. Sửa nhỏ nhất có thể

| Nên | Không nên |
|---|---|
| Đổi một giá trị đặt | Viết lại cả khối |
| Thêm một nhánh mới | Cấu trúc lại logic có sẵn |
| Thêm một nấc thang | Gộp nhiều nấc "cho gọn" |
| Giữ nguyên phong cách của chương trình | Áp phong cách của bạn vào |

> 💡 **Hoà vào, đừng nổi bật.** Nếu chương trình dùng quy ước bạn không thích, **vẫn theo quy ước đó**.
> Một chương trình nhất quán theo cách dở vẫn dễ đọc hơn một chương trình nửa nọ nửa kia. Đây là ứng
> dụng trực tiếp của nguyên tắc ở Chương 30: **nhất quán quan trọng hơn đẹp.**

### 4. Ghi lại

Ghi ngay, không để "lát nữa":

- **Trong chương trình**: chú thích nói **vì sao** sửa, ngày, và tên bạn.
  `// 2026-09-01 [NHAN] tăng timeout bước 20 từ 3s lên 4s — xy-lanh chậm khi khí xuống thấp buổi trưa`
- **Trong nhật ký thay đổi** của máy — file hoặc sổ đặt cùng máy (Chương 30, Chương 54).
- **Trên màn hình hoặc trong tủ**: nếu có ô ghi phiên bản chương trình, cập nhật nó.

> ⭐ Chú thích tốt nhất là chú thích trả lời câu hỏi mà **người tiếp theo sẽ hỏi**. Người đó rất có
> thể là chính bạn, sáu tháng sau, lúc hai giờ sáng, và bạn sẽ không nhớ gì cả.

---

## 22.8 ⚠ Sửa chương trình trên máy đang sản xuất

Tình huống rủi ro cao, cần nói riêng.

Nhiều hệ cho phép **sửa trực tuyến** *(online edit)* — thay đổi chương trình khi CPU đang chạy, không
cần dừng máy. Rất tiện, và rất nguy hiểm.

> ⚠⚠ **NGUY HIỂM — sửa trực tuyến trên máy đang chạy**
>
> - Thay đổi có hiệu lực **ngay lập tức**, giữa chu trình, ở một bước bất kỳ.
> - Không có bước "kiểm tra trước khi áp dụng" — cơ cấu phản ứng ngay.
> - Một số hệ **dừng CPU** khi bạn thay đổi một số thứ (khai báo biến, cấu hình phần cứng). CPU dừng
>   nghĩa là **mọi ngõ ra về trạng thái đã cấu hình cùng lúc**, giữa chu trình (Chương 8, mục 8.8).
> - Sửa nhầm trên máy đang chạy có thể làm hỏng sản phẩm, hỏng thiết bị, hoặc gây thương tích.
>
> **Quy tắc tối thiểu:**
> 1. Không ai ở trong vùng máy.
> 2. Đã sao lưu, và **biết cách quay lui trong một phút**.
> 3. Có người thứ hai đứng cạnh nút dừng khẩn.
> 4. Nếu thay đổi chạm tới cơ cấu chuyển động hoặc tới an toàn → **không sửa trực tuyến**. Dừng máy,
>    sửa, chạy thử theo quy trình (Chương 52).
> 5. Cơ sở của bạn có thể có quy định riêng — **quy định đó thắng**.

> 💡 **Sửa trực tuyến hợp lý nhất cho: đổi một giá trị đặt, thêm một cờ chẩn đoán, thêm một chú
> thích.** Không hợp cho: đổi trình tự, đổi điều kiện liên động, đổi logic ngõ ra.

---

## 22.9 Trên máy mẫu DP-01 — một tình huống thật

> **Yêu cầu:** *"Trạm 1 thỉnh thoảng báo lỗi quá thời gian ở bước nâng kẹp vào buổi trưa. Xử lý đi."*

Áp quy trình:

**Bước 1 — câu hỏi.** Không phải "sửa lỗi timeout", mà: *"vì sao xy-lanh kẹp trạm 1 mất nhiều thời
gian hơn bình thường vào buổi trưa?"* Câu hỏi này chỉ ra rằng đây có thể **không phải vấn đề phần
mềm**.

**Bước 2 — sao lưu.** Trước khi mở bất cứ thứ gì.

**Bước 3 — bản đồ.** Tìm chỗ báo lỗi: tham chiếu chéo tag `Stn1.FaultStep`, thấy nó được ghi ở một
chỗ — khối giám sát thời gian bước. Tốt, chương trình có kỷ luật.

**Bước 4 — truy ngược.** Đoạn code liên quan:

```iecst
T_Step20(IN := (Stn1_Step = 20), PT := T#3S);
IF T_Step20.Q THEN
    Stn1.FaultStep := 20;
    Stn1.Fault     := TRUE;
END_IF;
```

**Bước 5 — hiểu.** Timer đặt 3 giây. Xy-lanh bình thường mất khoảng 0,6 giây (Chương 17, mục 17.1).
Buổi trưa mất hơn 3 giây. Câu hỏi đúng: **vì sao nó chậm đi?**

Ba giả thuyết, và cách phân biệt:

| Giả thuyết | Cách kiểm |
|---|---|
| Áp khí tụt vào giờ cao điểm | ⭐ Ghi lại `DI_AirOK` và thời gian bước theo giờ trong một ngày |
| Bộ lọc khí đầy nước | Kiểm cốc lọc; hiện tượng nặng dần theo thời gian, không theo giờ |
| Xy-lanh mòn | Chậm dần đều, không phụ thuộc giờ |

**Bước 6 — sửa nhỏ nhất.**

> ⚠ **Cám dỗ:** tăng timeout lên 6 giây. Lỗi hết, việc xong.
>
> **Vì sao đó là sai:** timeout không phải nguyên nhân, nó là **thứ phát hiện ra vấn đề**. Tăng nó
> lên nghĩa là **làm mù bộ phát hiện** — máy vẫn kẹp chậm, board vẫn có thể xê dịch, nhưng bây giờ
> không ai biết nữa (Chương 17, Chương 48).

Việc đúng, theo thứ tự:

1. **Thêm chẩn đoán trước, đừng sửa gì cả**: ghi lại thời gian thực tế của bước 20 và trạng thái
   `DI_AirOK` theo giờ. Đây là thay đổi **chỉ thêm quan sát**, không đổi hành vi — rủi ro thấp nhất.
2. **Đọc số liệu sau một ngày.** Nếu áp khí tụt vào giờ cao điểm thì đó là vấn đề **hệ khí nén của
   nhà máy**, không phải vấn đề chương trình (Chương 6).
3. **Báo cáo phát hiện** kèm số liệu. Việc sửa có thể thuộc về người khác — và nếu bạn tăng timeout
   rồi im lặng, không ai biết nhà máy đang thiếu khí.
4. Nếu sau khi khắc phục nguyên nhân mà thời gian thật vẫn gần 3 giây, **khi đó** mới xét lại giá trị
   timeout — với số liệu làm căn cứ, và ghi rõ lý do trong chú thích.

> ⭐ **Đây là mẫu chung của nghề: yêu cầu nói "sửa lỗi", nhưng việc đúng thường là "tìm ra nguyên nhân
> rồi báo cho đúng người".** Làm cho lỗi biến mất mà không hiểu vì sao là cách chắc chắn để nó quay
> lại — thường vào lúc tệ hơn.

---

## 22.10 Khác biệt giữa các hãng

| Việc | Siemens | Mitsubishi | Rockwell | CODESYS / TwinCAT |
|---|---|---|---|---|
| Tham chiếu chéo | Có, kèm bộ lọc đọc/ghi | Danh sách tham chiếu thiết bị | ⭐ Rất mạnh — mô hình tag làm việc tra cứu dễ hơn hẳn | Có |
| Tìm mọi chỗ ghi vào một tag | Lọc trong bảng tham chiếu chéo | Lọc theo thiết bị | Lọc theo tag | Lọc theo biến |
| So sánh hai phiên bản chương trình | Có công cụ so sánh | Có | Có | Có |
| ⚠ Sửa trực tuyến | Có, phạm vi hạn chế tuỳ loại thay đổi | Có | Có, khá linh hoạt | Tuỳ cấu hình runtime |
| ⚠ Thay đổi làm CPU dừng | Đổi cấu hình phần cứng, một số thay đổi khối dữ liệu | Đổi tham số PLC | Một số thay đổi cấu trúc tag | Tuỳ hệ |
| Tải chương trình **từ CPU** về | Có | Có | Có | Có |
| ⚠ Chương trình trong CPU có đủ chú thích không | ⚠ **Tuỳ cấu hình** — có thể **không** tải về được chú thích và tên | ⚠ Tương tự | Tag và chú thích thường nằm trong bộ điều khiển | ⚠ Tuỳ |

> ⚠⚠ **Hàng cuối là hàng gây đau đớn nhất, và ít người biết trước.**
> Ở một số hệ, chương trình tải về từ CPU có thể **thiếu chú thích, thiếu tên biến gợi nghĩa, thiếu
> cấu trúc**. Bạn nhận được logic đúng nhưng gần như không đọc được.
>
> Hệ quả thực tế: **file dự án gốc là tài sản không thể thay thế**. Nếu nó mất, cái bạn tải về từ CPU
> có thể không đủ để bảo trì tiếp. Đây chính là lý do Chương 54 tồn tại, và là lý do việc bàn giao mã
> nguồn phải là **điều khoản hợp đồng** (Chương 13, tiêu chí 5).
>
> **Trước khi tiếp quản một máy: hỏi xem có file dự án gốc không.** Câu trả lời quyết định công việc
> của bạn dễ hay khó gấp nhiều lần.

---

## 22.11 Bẫy thường gặp

### 🔍 BẪY 1 — Sửa mà không sao lưu

**Hiện tượng:** sửa xong máy hỏng nặng hơn, và **không quay lui được** vì không còn bản gốc.
**Cách sửa:** sao lưu **từ CPU đang chạy** trước khi động vào bất cứ thứ gì. Năm phút.

### 🔍 BẪY 2 — Dọn dẹp code trong lúc sửa việc khác

**Hiện tượng:** máy hỏng theo cách không liên quan gì tới yêu cầu ban đầu, và bạn phải giải thích.
**Cách sửa:** sửa đúng việc được yêu cầu. Ghi riêng đề xuất dọn dẹp thành công việc có kế hoạch
(mục 22.6).

### 🔍 BẪY 3 — Làm tròn một con số "lạ"

`T#2700MS` thành `T#3S` cho "gọn".

**Hiện tượng:** một chức năng đã chạy đúng nhiều năm bỗng sai, và mối liên hệ với thay đổi của bạn
không hiển nhiên.
**Cách sửa:** con số lạ gần như luôn đến từ **thực nghiệm trên máy thật**. Đừng động vào khi chưa
biết nó từ đâu ra.

### 🔍 BẪY 4 — Không kiểm "ai còn ghi vào tag này"

**Hiện tượng:** sửa một nấc thang, ngõ ra vẫn không đổi hành vi — vì có chỗ khác ghi đè, chạy sau.
**Cách sửa:** tham chiếu chéo, lọc lấy các chỗ **ghi**, đếm (mục 22.3).

### 🔍 BẪY 5 — Tăng timeout để lỗi biến mất

**Hiện tượng:** lỗi hết, nhưng vấn đề vật lý vẫn còn và bây giờ **không ai phát hiện được nữa**.
**Cách sửa:** timeout là bộ phát hiện, không phải nguyên nhân. Tìm vì sao chậm (mục 22.9).

### 🔍 BẪY 6 — Sửa trực tuyến trên máy đang chạy khi không cần thiết

**Hiện tượng:** cơ cấu phản ứng ngay giữa chu trình; hoặc CPU dừng đột ngột vì thay đổi thuộc loại
không sửa trực tuyến được.
**Cách sửa:** quy tắc tối thiểu ở mục 22.8. Chạm tới chuyển động hoặc an toàn thì **dừng máy**.

### 🔍 BẪY 7 — Tin tài liệu hơn tin chương trình

**Hiện tượng:** làm theo tài liệu bàn giao, kết quả không khớp — vì máy đã được sửa nhiều lần mà tài
liệu không cập nhật.
**Cách sửa:** **chương trình đang chạy là sự thật duy nhất.** Tài liệu là gợi ý. Khi hai thứ mâu
thuẫn, tin chương trình và **cập nhật tài liệu**.

### 🔍 BẪY 8 — Áp phong cách của mình vào chương trình của người khác

**Hiện tượng:** chương trình thành nửa nọ nửa kia; người sau phải học **hai** quy ước thay vì một.
**Cách sửa:** hoà vào phong cách sẵn có (mục 22.7, bước 3).

### 🔍 BẪY 9 — Không ghi lại thay đổi

**Hiện tượng:** sáu tháng sau không ai — kể cả bạn — biết vì sao giá trị đó là 4 giây, hay ai đã đổi
nó, hay đổi để chữa cái gì.
**Cách sửa:** chú thích có **ngày, tên, và lý do**; cộng một dòng trong nhật ký thay đổi của máy.

---

## 22.12 Bảng chốt

| Tình huống | Việc phải làm |
|---|---|
| Bắt đầu đọc một chương trình lạ | Viết ra **một câu hỏi cụ thể** trước |
| Muốn biết vì sao một giá trị sai | ⭐ **Tham chiếu chéo → lọc các chỗ GHI → đếm** |
| Nhiều hơn một chỗ ghi vào cùng một tag | Gần như chắc chắn đó là vấn đề |
| Giá trị đổi mà không dòng code nào ghi | Nghi **cưỡng bức bị quên**, hoặc ghi từ ngoài |
| Không có chú thích | Xem **trực tuyến khi máy chạy** — hiệu quả hơn đọc tĩnh nhiều |
| Trước khi sửa bất cứ thứ gì | ⚠⚠ **Sao lưu từ CPU đang chạy** |
| Thấy code "thừa" hoặc con số "lạ" | ⚠ Giả định nó có lý do. **Đừng dọn** |
| Phong cách chương trình khác của bạn | **Theo phong cách sẵn có** |
| Sửa xong | Ghi **ngày · tên · lý do**, trong code và trong nhật ký |
| Sửa trực tuyến | Chỉ cho giá trị đặt và chẩn đoán. ⚠ Chạm chuyển động hoặc an toàn → **dừng máy** |
| Tài liệu mâu thuẫn chương trình | **Chương trình thắng**, rồi cập nhật tài liệu |
| ⭐⭐ Hồ sơ lẽ ra phải có | **Bản tóm tắt hệ thống**: bài toán · ⭐ **chiến lược và VÌ SAO chọn** · mục tiêu |
| Phần luôn mất trước | ⭐ **"Vì sao chọn cách này"** — vì không cần tới nó thì máy vẫn chạy |
| ⭐ Dựng xong bản đồ thì làm gì | **Viết ra 2–3 trang**, ⚠ **đánh dấu rõ chỗ nào là suy đoán** |
| Ghi thêm mục nào | ⭐ **Ai viết, ai sửa, sửa khi nào** — nửa lời giải cho code chắp vá |
| Trước khi nhận bảo trì một máy | Hỏi: **có file dự án gốc không?** |
| ⭐⭐ Nhận một chương trình đang chạy tốt | Soát **năm chỗ** của mục 22.6b — gán cứng · sườn bỏ đó · nhịp nhanh hơn tác vụ · vế chép trùng · hai tác vụ cùng ghi |

---

## 22.13 Tự kiểm

1. Vì sao *"hiểu chương trình này"* không phải một câu hỏi dùng được? Cho một ví dụ câu hỏi dùng được.
2. ⭐ Tham chiếu chéo trả lời ba câu hỏi nào? Câu nào quan trọng nhất và vì sao?
3. Một tag có **hai** chỗ ghi vào. Vì sao đó gần như chắc chắn là vấn đề, và chỗ nào "thắng"?
4. Một giá trị thay đổi nhưng tham chiếu chéo cho thấy **không dòng code nào** ghi vào nó. Nêu ba khả
   năng.
5. ⭐ Vì sao **không** nên dọn dẹp code trong lúc sửa một việc khác? Nêu ba lý do.
6. Bạn thấy `T#2700MS` và muốn làm tròn thành `T#3S`. Vì sao đừng làm?
7. Nêu bốn bước của quy tắc sửa an toàn. Bước nào là bước duy nhất bảo đảm bạn quay lui được?
8. Vì sao phải sao lưu **từ CPU đang chạy** chứ không phải từ file trên máy tính của bạn?
9. ⭐ Yêu cầu là "trạm 1 báo lỗi timeout, xử lý đi". Vì sao tăng timeout là **sai**, và việc đúng đầu
   tiên nên làm là gì?
10. ⭐ Vì sao câu hỏi *"có file dự án gốc không?"* lại quan trọng tới mức phải hỏi **trước khi** nhận
    bảo trì một máy?
11. ⭐⭐ Nêu **ba phần** của một bản tóm tắt hệ thống. ⭐ Phần nào đắt nhất, và vì sao nó **luôn mất
    trước** trong khi sơ đồ đấu dây thì còn?
12. ⭐ Sau khi dựng xong bản đồ chương trình của người khác, việc nên làm tiếp là gì? Nêu **hai** cái
    lợi cho chính bạn, không phải cho người sau.
13. ⭐ Bạn nhận một chương trình máy đang chạy tốt. Nêu năm chỗ phải soi ở mục 22.6b; với mỗi chỗ, nói
    cách tìm nó trong vài phút và phép thử để biết đã sửa xong.

> Câu 2, 5 và 9 là ba câu phân loại. Câu 9 là tinh thần của cả chương: **làm cho triệu chứng biến mất
> không phải là sửa — và đôi khi nó còn tệ hơn không làm gì, vì nó tắt luôn bộ phát hiện.**

---

### Chương tiếp theo

Chương 23 — **Từ yêu cầu tới đặc tả điều khiển**. Bạn đã biết đọc và sửa chương trình có sẵn. Phần
III kết thúc ở đây; Phần IV bắt đầu bằng việc **thiết kế từ đầu** — và bằng loại sai lầm đắt hơn mọi
lỗi code: viết đúng cái không ai cần.

### Nguồn tham khảo chương 22

- Tài liệu phần mềm lập trình của từng hệ trong Phụ lục A — dùng cho: chức năng tham chiếu chéo, công
  cụ so sánh phiên bản, phạm vi cho phép của sửa trực tuyến, và ⚠ **những gì tải về được từ CPU**.
  Mục cuối khác nhau nhiều giữa các hệ và ảnh hưởng lớn tới công việc bảo trì.
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu về tài liệu kỹ
  thuật đi kèm máy — nền cho việc đòi hỏi file dự án gốc khi bàn giao. *(tiêu chuẩn có bản quyền)*
- Biểu mẫu **nhật ký thay đổi chương trình** — Phụ lục C.
- **Bryan, L.A. & Bryan, E.A.** — *Programmable Controllers: Theory and Implementation*, ch. 12
  *PLC System Documentation* §12-1 và §12-2: các thành phần của một bộ hồ sơ đầy đủ, và ⭐⭐ **bản tóm
  tắt hệ thống** gồm **phát biểu bài toán · chiến lược thiết kế kèm LÝ DO chọn · mục tiêu phải đạt**;
  hồ sơ tồn tại để **trả lời câu hỏi, chẩn đoán, và sửa khi yêu cầu thay đổi** — nền cho mục 22.4b.

> ⚡ Các quy tắc trong chương này là **thực hành nghề**, không phải yêu cầu tiêu chuẩn — trừ phần tài
> liệu bàn giao. Cơ sở của bạn có thể có quy định chặt hơn về việc sửa chương trình trên máy đang
> sản xuất, đặc biệt trong các ngành có quản lý thay đổi nghiêm ngặt. **Quy định của cơ sở luôn
> thắng nội dung chương này.**
