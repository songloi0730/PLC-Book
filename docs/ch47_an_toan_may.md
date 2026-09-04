# Chương 47 — An toàn máy: không logic thường nào thay được

> **Lát cắt máy mẫu:** 5 — máy đầy đủ, gồm cả mạch an toàn, analog, chuyển động và mạng.

---

> ⚠⚠ **ĐỌC TRƯỚC — phạm vi và giới hạn của chương này**
>
> Chương này giúp bạn **hiểu** an toàn máy và **đặt đúng câu hỏi**. Nó **không**:
> - không thay thế **đánh giá rủi ro** cho cỗ máy cụ thể của bạn;
> - không thay thế việc **tính toán và xác định mức hiệu năng** theo tiêu chuẩn gốc;
> - không cho phép bạn tự kết luận một cỗ máy là an toàn.
>
> Ba việc trên phải do **người có thẩm quyền** thực hiện, dựa trên **bản gốc tiêu chuẩn** và trên đúng
> cỗ máy đó. Nội dung ở đây là diễn giải khái niệm ở mức đủ để bạn làm việc được với người đó — không
> phải để thay họ.
>
> Chương này **đang chờ chuyên gia an toàn rà soát** trước khi phát hành.

---

## 47.1 Vì sao logic PLC thường không đủ

Chương 25 xây một máy trạng thái đẹp, có trạng thái `Alarm`, mọi trạng thái đều có đường vào đó. Chương
26 đặt timeout cho mọi bước. Chương 48 sẽ chọn trạng thái an toàn cho mọi ngõ ra. Nghe như đã đủ.

Chưa đủ. Vì tất cả những thứ đó **chỉ hoạt động khi CPU còn chạy chương trình**.

Nhắc lại từ Chương 10: nếu vòng quét vượt quá giới hạn, watchdog kích và **CPU ngừng thực thi**. Lúc đó:

- Máy trạng thái của bạn **không chạy** — không ai chuyển sang `Alarm`.
- Timeout của bạn **không đếm** — không ai phát hiện cơ cấu kẹt.
- Logic dừng khẩn cấp của bạn **không được thực thi**.

Nhưng khí nén vẫn còn trong ống. Động cơ vẫn còn quán tính. Tụ trong biến tần vẫn còn tích điện. **Mối
nguy không dừng theo CPU.**

Đó là lý do có một nguyên tắc không có ngoại lệ trong toàn ngành:

> ⚠⚠ **NGUY HIỂM — nguyên tắc nền tảng của chương này**
>
> **Chức năng an toàn không được phụ thuộc vào chương trình PLC thông thường.**
>
> Nó phải được thực hiện bằng thiết bị được thiết kế riêng cho mục đích đó — mạch cứng, rơ-le an toàn,
> hoặc PLC an toàn — hoạt động **độc lập** với CPU chạy chương trình sản xuất.
>
> PLC thường được phép **biết** rằng E-Stop đã bị nhấn, và **phản ứng** (chuyển sang `Alarm`, hiển thị
> thông báo). Nhưng việc **cắt năng lượng** phải do lớp an toàn làm, không do nó.

---

## 47.2 Đánh giá rủi ro đi trước — không phải thủ tục giấy tờ

Trình tự đúng của một dự án:

```text
1. Xác định giới hạn của máy      (làm gì, ai dùng, dùng thế nào, kể cả dùng sai dự đoán được)
        ↓
2. Nhận diện mối nguy              (liệt kê MỌI cách máy có thể gây hại)
        ↓
3. Ước lượng và đánh giá rủi ro    (mỗi mối nguy: nặng nhẹ ra sao, hay gặp không, tránh được không)
        ↓
4. Giảm thiểu rủi ro theo THỨ TỰ ƯU TIÊN   ← mục 47.3
        ↓
5. Xác định yêu cầu cho từng chức năng an toàn còn lại
        ↓
6. Thiết kế, hiện thực, kiểm định
```

Người mới thường bắt đầu từ bước 6: *"máy này chắc cần E-Stop và một công tắc cửa"*. Làm vậy có hai
hậu quả:

- **Bỏ sót mối nguy** mà không ai nghĩ tới — vì chưa từng liệt kê có hệ thống.
- **Không biết cần mức nào**, nên hoặc chọn thiếu (nguy hiểm) hoặc chọn thừa (đắt vô ích).

> ⚠ **NGUY HIỂM**
> Bước 3 quyết định **mức hiệu năng cần đạt** của mỗi chức năng an toàn, và mức đó quyết định **phải
> dùng kiến trúc nào và thiết bị nào**. Thiết kế trước rồi đánh giá sau thì thường phải làm lại từ đầu
> — và tệ hơn, có thể bạn sẽ vô thức biện minh cho thiết kế đã làm thay vì đánh giá trung thực.

### Ba yếu tố quyết định mức rủi ro

Các tiêu chuẩn dùng ba yếu tố để ước lượng rủi ro của một mối nguy:

| Yếu tố | Câu hỏi | Ví dụ ở DP-01 |
|---|---|---|
| **Mức độ thương tổn** | Nếu xảy ra, hậu quả nhẹ hay nặng? | Kẹp tay: thương tổn hồi phục được. Chiếu UV vào mắt: có thể tổn thương lâu dài |
| **Tần suất/thời gian phơi nhiễm** | Người ở trong vùng nguy hiểm bao lâu, bao nhiêu lần? | Cửa buồng UV mở mỗi lần thay lô — vài lần mỗi ca |
| **Khả năng tránh** | Người có nhận ra và tránh kịp không? | ⚠ Bức xạ UV: **không nhìn thấy, không cảm thấy** → gần như **không tránh được** |

Dòng cuối cùng là điểm mấu chốt của DP-01, và là loại mối nguy nguy hiểm nhất: **không có tín hiệu cảnh
báo tự nhiên**. Với một trục chuyển động, người ta nghe thấy, nhìn thấy, và giật mình rút tay. Với bức
xạ UV, không có gì cả — người bị chiếu thường **không biết mình vừa bị chiếu**, và hậu quả xuất hiện
muộn hơn nhiều giờ.

---

## 47.3 Thứ tự ưu tiên giảm thiểu rủi ro

Đây là thứ tự bắt buộc. **Không được nhảy xuống bậc dưới khi bậc trên còn làm được.**

| Bậc | Biện pháp | Ví dụ ở DP-01 | Vì sao ưu tiên cao hơn |
|---|---|---|---|
| **1** | **Thiết kế lại để loại bỏ mối nguy** | Chọn keo cứng bằng nhiệt thay vì UV → không còn nguồn UV | Mối nguy **không tồn tại** thì không thể gây hại |
| **2** | **Che chắn và thiết bị bảo vệ** | Buồng UV kín, cửa có khoá; rèm quang tại cửa chuyền | Không phụ thuộc vào con người làm đúng |
| **3** | **Thông tin cho người dùng** | Nhãn cảnh báo, hướng dẫn, đào tạo | ⚠ **Yếu nhất** — phụ thuộc hoàn toàn vào con người |

> ⚡ **LƯU Ý**
> Bậc 3 **không được dùng để thay cho** bậc 1 hoặc 2. Dán một cái nhãn "cẩn thận tia UV" rồi coi như
> đã xử lý mối nguy là sai — cả về kỹ thuật lẫn về trách nhiệm. Nhãn chỉ bổ sung cho những rủi ro còn
> lại **sau khi** đã làm hết bậc 1 và 2.

---

## 47.4 Ba cách thực hiện chức năng an toàn

| | **Mạch cứng** | **Rơ-le an toàn** | **PLC an toàn** |
|---|---|---|---|
| Là gì | Tiếp điểm nối trực tiếp, không qua bộ xử lý | Thiết bị chuyên dụng, đã được chứng nhận, có logic cố định | Bộ điều khiển được chứng nhận, lập trình được |
| Phù hợp | Máy rất đơn giản, ít chức năng an toàn | ⭐ **Phần lớn máy cỡ vừa** — kể cả DP-01 | Nhiều chức năng an toàn, cần logic phức tạp, cần chẩn đoán chi tiết |
| Ưu | Đơn giản nhất, dễ hiểu, dễ kiểm | Đã chứng nhận sẵn; đấu theo sơ đồ hãng là đạt kiến trúc mong muốn | Linh hoạt; chẩn đoán tốt; ít dây |
| Nhược | Không mở rộng được; nhiều dây | Mỗi chức năng thường một thiết bị | Đắt; cần đào tạo riêng; lập trình an toàn có quy trình riêng |

> 💡 **MẸO — cách làm thực tế nhất cho người mới**
> **Dùng thiết bị đã được chứng nhận, và đấu đúng theo sơ đồ mẫu của hãng.**
>
> Nhà sản xuất rơ-le an toàn công bố các sơ đồ đấu điển hình kèm mức hiệu năng đạt được. Nếu bạn đấu
> đúng sơ đồ, dùng đúng thiết bị, và không tự ý thêm bớt, thì bạn thừa hưởng kết quả đã được chứng
> nhận đó. Đây là con đường an toàn nhất — cả nghĩa đen lẫn nghĩa nghề nghiệp.
>
> Cái **không** được làm: tự chế một mạch "tương đương" bằng rơ-le thường vì thấy rẻ hơn. Rơ-le an toàn
> khác rơ-le thường ở **tiếp điểm cưỡng bức** *(forcibly guided contacts)* — nếu một tiếp điểm bị hàn
> dính, các tiếp điểm còn lại **không thể** chuyển trạng thái, nên mạch giám sát phát hiện được. Rơ-le
> thường không có tính chất đó.

---

## 47.4b ⭐⭐ Lập trình PLC an toàn — một ngôn ngữ bị cắt bớt có chủ ý

Ô *"Nhược"* của cột **PLC an toàn** ở bảng trên ghi *"lập trình an toàn có quy trình riêng"*. Mục này
nói rõ **riêng ở chỗ nào** — vì hiểu sai điểm này dẫn tới một dự án đội chi phí mà không ai lường trước.

> ⭐⭐ **Viết chương trình an toàn KHÔNG phải là lập trình bình thường cộng thêm cẩn thận.**
> Đó là lập trình trong một ⚠ **tập con bị cắt bớt có chủ ý** của IEC 61131-3 — ít ngôn ngữ hơn, ít
> kiểu dữ liệu hơn, ít khối chức năng hơn. Và ⭐ **công cụ lập trình cưỡng chế điều đó**, không phải
> bạn tự giữ kỷ luật.

### Ba mức người dùng — và chỗ chi phí nhảy vọt

| Mức | Bạn được làm gì | ⭐ Cái giá |
|---|---|---|
| ⭐ **Cơ bản** *(Basic)* | Chỉ **nối các khối chức năng đã được chứng nhận** lại với nhau, dạng đồ hoạ | ⭐⭐ **Thời gian nghiệm thu ngắn hẳn** — các khối đã chứng nhận từ trước |
| ⚠ **Mở rộng** *(Extended)* | Tự viết khối khi khối sẵn có không đủ | ⚠⚠ **Toàn bộ chương trình phải qua quy trình kiểm định đầy đủ** — phức tạp và tốn thời gian hơn nhiều |
| **Hệ thống** *(System)* | Dành cho **nhà cung cấp bộ điều khiển an toàn** | Nằm ngoài phạm vi đặc tả |

> ⭐⭐ **Đây là ranh giới chi phí quan trọng nhất của cả chương.**
>
> Ở mức cơ bản, bạn **thừa hưởng** kết quả chứng nhận của các khối — giống hệt tinh thần *"đấu đúng
> sơ đồ mẫu của hãng"* ở mục trên. ⚠ Nhưng **ngay khi bạn tự viết một khối**, bạn bước sang mức mở
> rộng, và **cả chương trình** — không chỉ khối đó — phải đi qua quy trình kiểm định.
>
> ⭐ Nghĩa là câu hỏi *"tự viết một khối nhỏ thôi mà, có sao đâu?"* ⚠⚠ **không phải câu hỏi kỹ thuật,
> mà là câu hỏi ngân sách và tiến độ**.
>
> ⚡ Lối thoát có sẵn: khối tự viết **sau khi đã được kiểm định/chứng nhận** thì dùng lại được ở mức
> cơ bản — nên nếu công ty làm nhiều máy giống nhau, chi phí đó **trả một lần**.

### ⚠ Ngôn ngữ nào được dùng — và vì sao

Đặc tả giới hạn ngôn ngữ dựa trên khuyến nghị theo mức SIL của IEC 61508:

| Ngôn ngữ | Trạng thái trong lập trình an toàn |
|---|---|
| ⭐ **FBD** và **LD** | ⭐ **Ngôn ngữ ưu tiên** — và chỉ dùng **một tập con đã định** của chúng |
| **ST** | Chỉ ở **mức mở rộng** |
| ⚠ **IL** và **SFC** | ⚠ **Không được đặt vấn đề** trong đặc tả — chi phí vòng đời cao hơn |

> ⭐ **Lý do là kiểm định, không phải khẩu vị:** kiểm thử và thẩm định chương trình viết bằng **ngôn
> ngữ văn bản** thì ⚠ **phức tạp hơn và dễ sai hơn** so với ngôn ngữ đồ hoạ. Ngôn ngữ đồ hoạ cho
> **cái nhìn tổng thể** về chính chương trình an toàn, và công cụ hỗ trợ, dẫn dắt người dùng tốt hơn
> nhiều.
>
> ⚡ Đây là một trong số ít chỗ trong sách mà **ladder thắng ST một cách dứt khoát** — và lý do trùng
> đúng với lý do ở Chương 20 mục 20.6: ⭐ **thứ người khác phải đọc và xác nhận được thì viết bằng cái
> họ đọc được.** Ở đây "người khác" là **người thẩm định**.

> ⚠⚠ **Mục này mô tả CÔNG CỤ ràng buộc bạn thế nào — nó KHÔNG dạy bạn viết chương trình an toàn.**
> Việc đó cần đào tạo riêng, công cụ được chứng nhận, và người có thẩm quyền thẩm định. ⭐ Mục đích ở
> đây chỉ là để bạn **biết trước mình đang bước vào cái gì** khi chọn cột thứ ba của bảng ở mục 47.4.

---

## 47.5 Mức hiệu năng và kiến trúc — đủ để làm việc

Phần này diễn giải khái niệm ở mức đủ để bạn **đọc hiểu tài liệu và trao đổi với chuyên gia**. Nó
**không đủ** để bạn tự xác định mức cho máy của mình.

### Mức hiệu năng

Tiêu chuẩn về bộ phận liên quan an toàn của hệ điều khiển dùng thang **mức hiệu năng** *(Performance
Level, PL)* từ **a** đến **e**, trong đó **e** là mức cao nhất. Mức cần đạt cho mỗi chức năng an toàn
được suy ra từ ba yếu tố ở mục 47.2.

Một tiêu chuẩn song song dùng thang **mức toàn vẹn an toàn** *(Safety Integrity Level, SIL)*. Hai
thang có thể quy đổi gần đúng cho nhau; chọn dùng thang nào phụ thuộc ngành và thị trường.

### Cây phả hệ — vì sao có hai thang

Người mới rất hay bối rối khi tài liệu chỗ thì nói PL, chỗ lại nói SIL. Lý do nằm ở quan hệ giữa
các tiêu chuẩn:

```text
                    IEC 61508  — an toàn chức năng cho hệ điện/điện tử/
                        │        điện tử lập trình được. Tiêu chuẩn GỐC,
                        │        đặt ra khái niệm SIL 1–4 và vòng đời an toàn.
                        │
          ┌─────────────┴─────────────┐
          │                           │
    ISO 13849-1                  IEC 62061
    thang PL a–e                 thang SIL (CL) cho máy
    xuất phát từ ngành cơ khí    xuất phát từ IEC 61508
          │                           │
          └─────────────┬─────────────┘
                        │
              cùng áp cho MÁY — chọn một, không trộn
```

Ba điều rút ra:

- **IEC 61508 là tiêu chuẩn nền**, viết cho mọi ngành. Bạn hiếm khi áp trực tiếp nó lên một cỗ máy;
  bạn áp một trong hai tiêu chuẩn ngành máy phía dưới. Nhưng khái niệm mà cả hai dùng — vòng đời an
  toàn, xác suất hỏng, mức bao phủ chẩn đoán, hỏng do nguyên nhân chung — đều bắt nguồn từ đây.
- **SIL của ngành quá trình ≠ SIL của ngành máy.** Ngành quá trình (dầu khí, hoá chất) tính SIL theo
  IEC 61511 với chế độ tác động *ít khi* — hệ an toàn nằm im hàng năm rồi mới cần hoạt động một lần.
  Máy tự động hoá thì chức năng an toàn tác động **nhiều lần mỗi ca**. Cùng chữ "SIL 2" nhưng đằng
  sau là hai phép tính khác nhau. Đừng mang con số từ tài liệu ngành này sang ngành kia.
- **Không trộn hai thang trong cùng một chức năng an toàn.** Chọn ISO 13849-1 thì đi hết theo PL; chọn
  IEC 62061 thì đi hết theo SIL. Trộn giữa chừng làm hồ sơ chứng minh mất giá trị.

> 💡 **MẸO**
> Khi đọc catalogue thiết bị an toàn, bạn sẽ thấy nhà sản xuất ghi cả hai: *"phù hợp tới PL e /
> SIL 3"*. Đó là **năng lực tối đa của linh kiện**, không phải mức mà máy của bạn đạt được. Mức của
> máy phụ thuộc cách bạn đấu nối và toàn bộ chuỗi từ cảm biến tới cơ cấu chấp hành.

### Kiến trúc — phân biệt bằng hai câu hỏi

Các tiêu chuẩn định nghĩa một số **hạng mục kiến trúc** *(Category)*: B, 1, 2, 3, 4. Cách nhớ thực dụng
nhất là hai câu hỏi:

> **Câu 1 — Có dự phòng không?** (hai kênh độc lập, hỏng một kênh vẫn còn kênh kia)
> **Câu 2 — Có tự kiểm không?** (hệ thống tự phát hiện được hỏng hóc của chính nó)

| Hạng mục | Dự phòng | Tự kiểm | Hỏng một chỗ thì sao |
|---|:---:|:---:|---|
| **B** | không | không | **Mất chức năng an toàn** |
| **1** | không | không | Mất chức năng, nhưng dùng linh kiện và nguyên tắc đã được kiểm chứng nên **ít hỏng hơn** |
| **2** | không | có, **theo chu kỳ** | Mất chức năng cho tới lần kiểm tiếp theo |
| **3** | **có** | có, một phần | Hỏng **một** chỗ thì **không mất** chức năng; ⚠ nhưng **hỏng tích luỹ có thể làm mất** |
| **4** | **có** | có, đầy đủ | **Không mất** chức năng; hỏng hóc được phát hiện **kịp thời**, và ⭐ **chống được cả hỏng tích luỹ** |

> ⭐⭐ **Hai chi tiết định lượng phân biệt Category 2 và Category 3 — và chúng hay bị bỏ qua:**
>
> | | Chi tiết |
> |---|---|
> | ⚠ **Category 2** | Tự kiểm theo chu kỳ chỉ có giá trị khi ⭐ **kiểm đủ dày so với tần suất dùng**: thông lệ là **tần suất kiểm ít nhất 100 lần tần suất yêu cầu** chức năng an toàn (có ngoại lệ cho phép tối thiểu 25 lần). ⚠ Kiểm quá thưa thì Category 2 **gần như không còn tác dụng** |
> | ⚠⚠ **Category 3** | Chịu được **một** hỏng hóc, nhưng ⭐ **hỏng tích luỹ chưa được phát hiện VẪN có thể làm mất chức năng an toàn**. Chỉ Category 4 mới đảm bảo chống được điều đó |
>
> ⭐ Hàng thứ hai là lý do **giám sát tiếp điểm và kiểm định định kỳ không phải thủ tục giấy tờ** —
> chúng chính là thứ ngăn hỏng hóc tích luỹ trong một hệ Category 3.
>
> *(Đối chiếu: DGUV/IFA Report 2/2017e — Functional safety of machine controls, phần áp dụng
> ISO 13849-1. ⚠ Đây là tài liệu **diễn giải**, không phải bản gốc tiêu chuẩn — con số cụ thể và điều
> kiện áp dụng phải lấy từ ISO 13849-1.)*

Ba điểm cần hiểu cho đúng:

- **Hạng mục không phải là mức hiệu năng.** Mức hiệu năng đạt được phụ thuộc *cả* kiến trúc, *cả* độ
  tin cậy linh kiện, *cả* mức bao phủ chẩn đoán, *cả* biện pháp chống hỏng do nguyên nhân chung. Chọn
  Category 3 không tự động cho ra PL d.
- **"Hai kênh" phải thật sự độc lập.** Hai kênh đi chung một sợi cáp, qua chung một đầu nối, hoặc dùng
  chung một nguồn thì **một sự cố duy nhất có thể làm hỏng cả hai** — đó là hỏng do nguyên nhân chung.
- **Câu 2 mới là câu tạo ra khác biệt lớn.** Dự phòng mà không tự kiểm thì kênh thứ hai có thể đã hỏng
  từ ba tháng trước mà không ai biết — và bạn đang chạy với một kênh trong khi tưởng có hai.

> ⚠⚠ **NGUY HIỂM**
> Bảng trên là **cách nhớ**, không phải căn cứ thiết kế. Việc xác định mức cần đạt, chọn kiến trúc, và
> tính toán để chứng minh đạt mức đó **phải dựa trên bản gốc tiêu chuẩn** và do người có thẩm quyền
> thực hiện. Không có cỗ máy nào được kết luận là an toàn dựa trên một bảng tóm tắt trong sách.

---

## 47.6 Dừng khẩn cấp

### Ba loại lệnh dừng

Tiêu chuẩn về trang bị điện của máy phân biệt ba loại dừng:

| Loại | Cách dừng | Dùng khi |
|---|---|---|
| **Dừng loại 0** | **Cắt năng lượng ngay lập tức** tới cơ cấu chấp hành | Khi dừng ngay là an toàn nhất |
| **Dừng loại 1** | Dừng **có kiểm soát** (còn năng lượng để hãm), **rồi mới cắt** năng lượng | Khi cắt ngay gây nguy hiểm hơn — ví dụ trục quán tính lớn cần hãm |
| **Dừng loại 2** | Dừng có kiểm soát, **vẫn giữ năng lượng** | ⚠ **Không dùng cho dừng khẩn cấp** |

**Dừng khẩn cấp phải là loại 0 hoặc loại 1.** Loại 2 không đủ vì cơ cấu vẫn còn năng lượng.

### Yêu cầu với nút dừng khẩn cấp

- **Màu đỏ trên nền vàng**, dạng nấm, **tự giữ khi nhấn** — nhả tay ra nó vẫn giữ trạng thái đã nhấn.
- **Gỡ trạng thái phải là hành động có chủ ý** (xoay, kéo), và **gỡ nút không được làm máy khởi động
  lại** — chỉ cho phép khởi động lại bằng một thao tác riêng.
- Phải **luôn tác dụng**, ở mọi chế độ vận hành, không có ngoại lệ.
- Tiếp điểm phải là **NC** — đứt dây thì mạch mở, tức là dừng (Chương 4).

> ⚠⚠ **NGUY HIỂM**
> Dừng khẩn cấp là **biện pháp bổ sung**, không phải biện pháp bảo vệ chính. Nó tồn tại để xử lý tình
> huống ngoài dự kiến, **không** để thay cho che chắn và khoá liên động ở bậc 2 của mục 47.3. Một cỗ
> máy mà cách bảo vệ duy nhất là "người vận hành sẽ nhấn E-Stop kịp" là một cỗ máy chưa được thiết kế
> an toàn.

---

## 47.7 Thiết bị bảo vệ — chọn loại nào

| Thiết bị | Bảo vệ kiểu gì | Phù hợp khi | Điểm phải chú ý |
|---|---|---|---|
| **Che chắn cố định** | Rào vật lý, tháo phải dùng dụng cụ | Vùng không cần vào khi vận hành | Đơn giản và hiệu quả nhất — ưu tiên trước mọi thứ khác |
| **Cửa có khoá liên động** | Mở cửa → dừng máy | Cần vào định kỳ (thay lô, vệ sinh) | Loại **giữ khoá tới khi an toàn** cần cho máy có quán tính hoặc năng lượng còn lại |
| **Rèm quang** *(light curtain)* | Cắt tia → dừng máy | Cửa vào/ra sản phẩm, thao tác thường xuyên | ⚠ **Khoảng cách lắp** phải tính theo thời gian dừng của máy |
| **Thảm an toàn** | Đứng lên → dừng máy | Vùng sàn quanh máy | Diện tích phải phủ hết đường tiếp cận |
| **Điều khiển hai tay** | Phải giữ **cả hai** nút mới chạy | Máy ép, thao tác lặp có nguy cơ kẹp tay | Bảo vệ **người vận hành đó**, không bảo vệ người khác đứng gần |
| **Giám sát tốc độ không** *(zero-speed)* | Chỉ cho mở cửa khi đã dừng hẳn | Trục quán tính lớn | Đi cùng khoá giữ tới khi an toàn |

### ⭐⭐ Hình học quyết định TRƯỚC phần mềm — ba điều người lập trình hay bỏ qua

Bảng trên là **thiết bị**. Nhưng ⭐ **phần lớn việc bảo vệ được quyết định bằng hình học**, và nó nằm
trước mọi thiết bị lẫn mọi dòng code — đúng tinh thần thứ tự ưu tiên ở mục 47.3.

**Một — khoảng cách an toàn phụ thuộc KÍCH THƯỚC LỖ trên che chắn**

Một tấm che có lỗ để nạp liệu hoặc để nhìn vào. ⚠ *"Có che chắn rồi"* **không đủ** — hai đại lượng đi
cùng nhau:

| Ký hiệu | Nghĩa |
|---|---|
| ⭐ **Kích thước lỗ** | ⭐ **Cạnh NHỎ NHẤT** của lỗ — cạnh ngắn của khe, một cạnh của lỗ vuông, **đường kính** của lỗ tròn |
| ⭐ **Khoảng cách an toàn** | Từ tấm che tới **vùng nguy hiểm** |

> ⭐⭐ **Lỗ càng lớn thì tấm che phải đặt càng XA** — vì lỗ lớn cho phép luồn sâu hơn. Quan hệ giữa hai
> con số nằm trong **bảng của tiêu chuẩn về khoảng cách an toàn**, không suy đoán được.
>
> ⚠ Hệ quả hay gặp: **đổi lưới che sang loại mắt to hơn** cho dễ nhìn — ⚠⚠ **việc đó có thể làm mất
> hiệu lực của khoảng cách đang có**, dù tấm che vẫn ở nguyên chỗ cũ.

**Hai — chống kẹp có HAI cách, và chỉ một cách là loại bỏ mối nguy**

| Cách | Bản chất |
|---|---|
| ⭐⭐ **Chừa khe hở tối thiểu** giữa các bộ phận chuyển động | ⭐ **Loại bỏ mối nguy** — cơ thể không thể bị chạm tới. An toàn tự thân |
| **Giảm lực và năng lượng** của bộ phận chuyển động | ⚠ **Giảm rủi ro xuống mức chấp nhận được** — mối nguy vẫn còn |

> ⭐ Cách thứ nhất mạnh hơn hẳn, và nó thuần **cơ khí** — không cần cảm biến, không cần logic, ⭐ **không
> hỏng được**.

**Ba — ⚠⚠ điểm cuốn: mối nguy mà LOGIC KHÔNG BẢO VỆ ĐƯỢC**

**Điểm cuốn** *(in-running nip)* là chỗ hai bề mặt hội tụ và **cuốn cơ thể vào**. Nó sinh ra từ bốn
cấu hình:

| | Cấu hình |
|---|---|
| 1 | Hai con lăn **chạm nhau**, quay ngược chiều |
| 2 | Hai con lăn **không chạm nhau** |
| 3 | Một con lăn **gần một vật đứng yên** |
| 4 | ⭐ Một con lăn **tiếp xúc với băng tải, xích, hoặc chính vật liệu** |

> ⚠⚠ **Cấu hình 4 là cấu hình của mọi băng tải — kể cả băng tải của DP-01** (mục 47.9).
>
> ⭐ Điều làm nó nguy hiểm với người làm phần mềm: ⚠⚠ **không có cảm biến nào và không có logic nào
> bảo vệ được**. Khi tóc, găng tay hoặc tay áo đã bị cuốn, ⭐ **dừng máy cũng đã muộn** — và bám càng
> chắc, lực ép càng lớn thì thương tích càng nặng.
>
> ⭐ Thứ duy nhất có tác dụng là **hình học**: che kín chỗ hội tụ, hoặc chừa khe đủ để không cuốn được.

> ⭐⭐ **Vì sao mục này nằm trong một cuốn sách về PLC:** ⚠ để bạn **nhận ra khi bài toán KHÔNG phải
> bài toán của mình.** Người ta hay hỏi *"lập trình thế nào cho an toàn chỗ này?"* — và với ba tình
> huống trên, ⭐ **câu trả lời đúng là "không lập trình, mà sửa cơ khí"**.
>
> ⚠ Con số cụ thể — khoảng cách bao nhiêu, khe hở bao nhiêu — nằm trong **bảng của các tiêu chuẩn**
> tương ứng và ⭐ **do người có thẩm quyền tra và ký**, không phải do người lập trình ước lượng.

### ⭐⭐ OSSD — ngõ ra của thiết bị an toàn, và cái bẫy nó tạo ra

Ngõ ra của rèm quang, máy quét an toàn và rơ-le an toàn có tên riêng: **OSSD** *(Output Signal
Switching Device)* — phần của thiết bị bảo vệ **nối tới hệ điều khiển của máy**.

Nó **không phải một ngõ ra số bình thường**, và khác biệt đó gây ra một trong những lỗi chập chờn
khó hiểu nhất.

| Đặc điểm OSSD | Vì sao có |
|---|---|
| ⭐ **Hai kênh** | Dự phòng (mục 47.5) |
| ⭐⭐ **Tự phát xung kiểm tra rất ngắn** trên ngõ ra khi đang ở trạng thái BẬT | ⭐ Để tự phát hiện **chập sang nguồn 24 V** và **chập chéo giữa hai kênh** |
| Tự tắt khi phát hiện lỗi | Hỏng theo hướng an toàn |

> ⭐⭐ **Vì sao xung kiểm tra quan trọng:** không có nó, một sợi dây OSSD bị chập vào 24 V sẽ làm ngõ
> ra **luôn báo an toàn** — kể cả khi rèm quang đã bị cắt. Xung kiểm tra là thứ biến "một sợi dây
> chập" từ lỗi vô hình thành lỗi phát hiện được.
>
> ⭐ Khả năng phát hiện chập chéo và chập xuống đất chính là một trong những điều kiện để đạt được
> hạng mục và mức hiệu năng cao (mục 47.5).

> ⚠⚠ **BẪY: đấu OSSD vào ngõ vào số THƯỜNG của PLC.**
>
> Ngõ vào thường có thể **nhìn thấy xung kiểm tra** và hiểu nhầm là tín hiệu tắt. Triệu chứng:
>
> | Bạn thấy | Thực tế |
> |---|---|
> | ⭐ Bit nhấp nháy rất nhanh, không theo quy luật | Đó là **xung kiểm tra**, không phải rèm quang bị cắt |
> | Lỗi không tái hiện được, biến mất khi đo bằng đồng hồ | Đồng hồ quá chậm để thấy xung |
> | Báo động "rèm quang" xuất hiện ngẫu nhiên | Logic thường đọc trúng lúc có xung |
>
> ⭐ **Cách xử lý đúng:** đấu OSSD vào **ngõ vào của thiết bị an toàn** (rơ-le an toàn hoặc PLC an
> toàn) — nơi được thiết kế để **bỏ qua xung kiểm tra**. Nếu chỉ cần cho PLC thường **biết** trạng
> thái để hiển thị, hãy lấy tín hiệu đó từ **tiếp điểm phụ của rơ-le an toàn**, không lấy thẳng từ
> OSSD.
>
> ⚠ Một số module ngõ vào có chế độ lọc dài hơn giúp che triệu chứng — ⭐ **nhưng che triệu chứng
> không phải cách đấu đúng**, và nó vẫn không cho bạn mức an toàn nào.
>
> ⭐ Độ rộng và chu kỳ xung kiểm tra **khác nhau theo thiết bị** — tra datasheet của chính thiết bị
> bạn dùng.

*(Đối chiếu: SICK — Guidelines for Safe Machinery, mục thuật ngữ ESPE/OSSD; SICK Safety Guide,
định nghĩa OSSD. Yêu cầu phát hiện chập chéo: DGUV/IFA Report 2/2017e.)*

### Muting — và vì sao nó nguy hiểm

**Muting** là tạm thời vô hiệu hoá một thiết bị bảo vệ để sản phẩm đi qua mà máy không dừng. DP-01 cần
nó ở cửa chuyền: board phải qua được, người thì không.

> ⚠⚠ **NGUY HIỂM**
> Muting là **cố ý tắt một chức năng an toàn**. Nó chỉ chấp nhận được khi hệ thống **phân biệt được
> sản phẩm với người** bằng bằng chứng độc lập — thường là nhiều cảm biến bố trí sao cho một người
> không thể tạo ra cùng một tổ hợp tín hiệu mà sản phẩm tạo ra.
>
> Muting sai thiết kế là **một trong những nguyên nhân tai nạn nghiêm trọng** ở máy có rèm quang. Đây
> là hạng mục bắt buộc phải do người có thẩm quyền thiết kế và kiểm định — không tự làm.

---

## 47.8 STO — dừng an toàn cho truyền động

Với trục có servo hoặc biến tần, cách "cắt năng lượng" ngây thơ là **ngắt contactor phía trước bộ điều
khiển truyền động**. Cách đó dừng được, nhưng có ba nhược điểm thật:

- Bộ điều khiển **mất nguồn hoàn toàn** → mỗi lần dừng khẩn cấp là một lần khởi động lại, mất thời gian.
- Mất **vị trí hiện tại** nếu không dùng loại encoder giữ được vị trí → phải về gốc lại.
- Contactor **mòn** vì đóng cắt dòng lớn.

**STO** *(Safe Torque Off — cắt mô-men an toàn)* giải quyết cả ba: nó cắt **tín hiệu kích** tới tầng
công suất, khiến động cơ **không thể sinh mô-men**, trong khi phần điều khiển vẫn còn nguồn.

Lợi ích của "còn điện nhưng không sinh mô-men":

| | Ngắt contactor phía trước | STO |
|---|---|---|
| Động cơ sinh mô-men được không | Không | Không |
| Bộ điều khiển còn nguồn | Không | **Có** |
| Giữ được vị trí | Tuỳ loại encoder | **Có** |
| Thời gian khôi phục sau khi hết E-Stop | Lâu — khởi động lại | **Nhanh** |
| Tuổi thọ thiết bị đóng cắt | Mòn dần | Không có tiếp điểm công suất |

> ⚠ **NGUY HIỂM — hai điều STO KHÔNG làm**
> - **STO không hãm.** Động cơ ngừng sinh mô-men, nhưng tải có quán tính sẽ **trôi theo đà**. Với trục
>   đứng hoặc tải treo, mất mô-men nghĩa là **rơi**. Trường hợp đó cần thêm phanh cơ khí, và phanh đó
>   cũng phải là phần của chức năng an toàn.
> - **STO không cách ly điện.** Bộ điều khiển vẫn có điện áp nguy hiểm bên trong. **Không được coi STO
>   là biện pháp bảo vệ khi sửa chữa** — việc đó cần cắt điện và khoá theo quy trình LOTO (mục 47.10).

---

## 47.9 Chức năng an toàn của DP-01

Áp toàn bộ chương vào máy mẫu. Bảng dưới là **kết quả của việc phân tích**, không phải danh sách chép sẵn.

| SF | Mối nguy | Biện pháp | Ghi chú thiết kế |
|---|---|---|---|
| **SF1** | Chuyển động gây kẹp/va đập ở mọi cơ cấu | E-Stop hai kênh → rơ-le an toàn → cắt nguồn van + STO cho servo + ngắt contactor trục chính | Dừng loại 0 cho van; loại 1 cho servo nếu cần hãm |
| **SF2** | ⭐ **Bức xạ UV chiếu vào người** | Buồng kín + cửa **khoá giữ tới khi an toàn**; đèn UV chỉ bật được khi cửa đóng và khoá; mở cửa → cắt nguồn đèn **qua mạch an toàn**, không qua lệnh PLC | Mối nguy **không có triệu chứng tức thời** → khả năng tránh rất thấp → mức yêu cầu cao |
| **SF3** | Kẹp tay khi bàn nâng kẹp hoạt động | Cửa bảo vệ có khoá liên động tại cả hai trạm | |
| **SF4** | Với tay vào qua cửa chuyền vào/ra | Rèm quang tại hai cửa chuyền, **có muting** để board đi qua | ⚠ Muting phải do người có thẩm quyền thiết kế — mục 47.7 |
| **SF5** | Máy khởi động bất ngờ sau khi khôi phục nguồn | Yêu cầu Reset **có chủ ý**; không tự vào `Running` | Chương 25, 28 |
| **SF6** | Mất khí nén khi board đang bị kẹp | Trạng thái an toàn của van kẹp: **giữ kẹp**, không nhả | Chương 48 |
| **SF7** | Bỏng do đầu tra keo được gia nhiệt | Che chắn cơ khí + cảnh báo; ngắt gia nhiệt khi mở cửa | |

Chú ý **SF2** là chức năng có yêu cầu cao nhất, và lý do nằm ở cột "khả năng tránh" của mục 47.2 chứ
không ở mức độ thương tổn. Đây là điều dễ bị đánh giá thấp: một mối nguy "chỉ" gây tổn thương mắt
nhưng **không thể nhận biết và không thể tránh** có thể đòi hỏi mức cao hơn một mối nguy nặng hơn mà
người ta nhìn thấy và tránh được.

---

## 47.10 LOTO trong thiết kế

**LOTO** *(lockout–tagout — khoá và treo thẻ)* là quy trình cô lập năng lượng trước khi sửa chữa. Nó
thường được coi là chuyện vận hành, nhưng phần lớn nó **được quyết định lúc thiết kế**.

Với mỗi dạng năng lượng trong máy, phải có cách **cô lập, khoá được, và xả hết năng lượng còn lại**:

| Dạng năng lượng ở DP-01 | Cô lập bằng | Xả năng lượng còn lại |
|---|---|---|
| Điện lưới | Aptomat tổng **có lỗ khoá** | Chờ tụ trong biến tần xả — theo thời gian ghi trên thiết bị |
| Khí nén | Van cô lập **có lỗ khoá**, đặt ở chỗ với tới được | Van phải có **cửa xả** — cô lập mà không xả thì khí vẫn còn trong ống |
| Thế năng | — | Hạ mọi cơ cấu treo xuống, hoặc chèn cơ khí |
| Nhiệt | Ngắt gia nhiệt | Chờ nguội — ghi thời gian chờ trên nhãn |
| Bức xạ UV | Ngắt nguồn đèn, khoá được | Đèn tắt là hết — nhưng đèn còn nóng |

> ⚠ **NGUY HIỂM**
> Ba lỗi thiết kế thường gặp làm LOTO không thực hiện được:
> - **Van khí không có cửa xả** — khoá van rồi mà xy-lanh vẫn có khí, vẫn chuyển động được.
> - **Cơ cấu cô lập không có lỗ khoá** — không gắn khoá vào được thì quy trình vô nghĩa.
> - **Cơ cấu cô lập đặt ở chỗ không với tới** — người sửa sẽ bỏ qua nó.
>
> Cả ba đều phát hiện được lúc thiết kế và rất tốn để sửa sau khi máy đã lắp.

---

## 47.11 Bẫy thường gặp

### 🔍 BẪY 1 — Đưa E-Stop vào logic PLC thường

```iecst
// ✗✗ SAI NGHIÊM TRỌNG
IF NOT DI_EStopOK THEN
    DO_ConvRun     := FALSE;
    DO_Clamp1Vlv   := FALSE;
    // … tắt mọi ngõ ra
END_IF;
```

Đoạn này **không sai về logic** — nó tắt đúng mọi thứ. Nó sai vì **chỉ chạy khi CPU còn chạy**. CPU
treo, watchdog kích, và toàn bộ đoạn trên biến mất trong khi mối nguy vẫn còn.

**Cách đúng:** mạch an toàn cắt năng lượng độc lập với PLC. PLC **đọc** `DI_EStopOK` để biết và phản
ứng (chuyển `Alarm`, hiển thị), nhưng việc cắt không do nó làm.

### 🔍 BẪY 2 — Dùng rơ-le thường thay rơ-le an toàn

Đã nêu ở mục 47.4. Nhắc lại vì cám dỗ về giá là có thật: rơ-le an toàn đắt hơn nhiều lần. Điểm khác
biệt — **tiếp điểm cưỡng bức** — không nhìn thấy được từ bên ngoài, nên rất dễ nghĩ là "cũng như nhau".

### 🔍 BẪY 3 — Hai kênh đi chung một sợi cáp

Đấu hai kênh độc lập rồi luồn cả hai qua **cùng một sợi cáp nhiều lõi**, hoặc qua **cùng một đầu nối**.
Một con chuột cắn, một lần kẹp cáp, một đầu nối vào nước — **cả hai kênh mất cùng lúc**. Dự phòng chỉ
tồn tại trên sơ đồ.

### 🔍 BẪY 4 — Reset tự động khi hết điều kiện

```iecst
// ✗ SAI — máy tự chạy lại khi gỡ E-Stop
IF DI_EStopOK THEN
    MachineState := Running;
END_IF;
```

Gỡ nút E-Stop ra là máy chạy lại ngay — trong khi người vừa nhấn nút có thể vẫn đang ở trong máy.
Khởi động lại **phải là một hành động riêng, có chủ ý**, sau khi gỡ điều kiện dừng.

### 🔍 BẪY 5 — Bỏ qua chức năng an toàn ở chế độ tay

*"Ở chế độ tay thì kỹ thuật viên biết mình làm gì"* — lập luận này sai ở chỗ: chế độ tay là lúc **người
ở gần máy nhất**, và là lúc máy hay ở tư thế bất thường nhất.

Điều được phép nới ở chế độ tay là **thứ tự thao tác** (Chương 28), không phải chức năng an toàn.
Nếu cần chuyển động khi cửa mở để căn chỉnh, đó là một **chế độ riêng có yêu cầu an toàn riêng** —
thường kèm tốc độ giảm, thiết bị cho phép ba vị trí, và phải được thiết kế như một chức năng an toàn.

### 🔍 BẪY 6 — Nghĩ STO là biện pháp bảo vệ khi sửa chữa

Đã nêu ở mục 47.8. Nhắc lại vì hậu quả nghiêm trọng: STO **không cách ly điện**. Người thò tay vào sửa
một trục "đang ở STO" vẫn có thể bị điện giật từ bộ điều khiển, và trục vẫn có thể rơi nếu là trục đứng.

### 🔍 BẪY 7 — Không thử chức năng an toàn khi nghiệm thu

Máy được thử kỹ ở chế độ bình thường, còn E-Stop thì "nhấn thử một cái, thấy dừng, xong".

Thử đúng phải bao gồm: nhấn E-Stop **ở từng bước của chu trình**, mở từng cửa **trong lúc máy đang
chạy**, cắt từng kênh của mạch hai kênh **riêng lẻ** để xác nhận phát hiện được. Danh mục này thuộc
Chương 52, và nó là phần bắt buộc.

---

## 47.12 Bảng chốt — làm gì với chức năng an toàn

| # | Việc | Ai làm | Xong khi |
|---|---|---|---|
| 1 | **Đánh giá rủi ro** — xác định giới hạn, nhận diện mối nguy, ước lượng | Người có thẩm quyền | Có văn bản, có người ký |
| 2 | Áp **thứ tự ưu tiên** giảm thiểu — thiết kế lại trước, che chắn sau, thông tin cuối | Nhóm thiết kế | Không mối nguy nào chỉ được xử lý bằng nhãn cảnh báo |
| 3 | Lập **danh sách chức năng an toàn** còn lại | Nhóm thiết kế | Mỗi SF ghi rõ mối nguy nào, biện pháp gì |
| 4 | **Xác định mức yêu cầu** cho từng SF | Người có thẩm quyền | Dựa trên bản gốc tiêu chuẩn |
| 5 | Chọn **kiến trúc và thiết bị** đạt mức đó | Nhóm thiết kế + hãng | Ưu tiên thiết bị đã chứng nhận, đấu theo sơ đồ hãng |
| 6 | Kiểm **tính độc lập** của các kênh | Nhóm thiết kế | Không chung cáp, không chung đầu nối, không chung nguồn |
| 7 | Thiết kế **LOTO** cho mọi dạng năng lượng | Nhóm thiết kế | Mọi cơ cấu cô lập **khoá được**, **với tới được**, và **xả được** |
| 8 | **Kiểm định** chức năng an toàn | Người có thẩm quyền | Thử từng SF, thử từng kênh riêng lẻ, có biên bản |
| 8b | ⭐ Nếu dùng **PLC an toàn**: chốt **mức người dùng** trước khi báo giá | Nhóm thiết kế + chủ đầu tư | ⚠⚠ Ở mức cơ bản chỉ **nối khối đã chứng nhận**; tự viết khối là **cả chương trình** phải kiểm định |
| 8c | Chốt **ngôn ngữ** dùng cho phần an toàn | Nhóm thiết kế | ⭐ **FBD/LD**; ST chỉ ở mức mở rộng; IL và SFC không đặt vấn đề |
| 2b | ⚠⚠ Đã rà **hình học**: lỗ trên che chắn · khe hở chống kẹp · ⭐ **điểm cuốn** | Người có thẩm quyền | ⭐ Con số tra từ **bảng tiêu chuẩn** và **có người ký** — không ước lượng |
| 9 | **Không phát hành** khi mục 1, 4, 8 chưa có | — | — |

---

## 47.13 Tự kiểm

1. Vì sao chức năng an toàn **không được** phụ thuộc vào chương trình PLC thường? Trả lời bằng cơ chế
   cụ thể ở Chương 10.
2. Nêu **ba yếu tố** quyết định mức rủi ro. Vì sao bức xạ UV của DP-01 lại đòi hỏi mức cao dù thương
   tổn không phải nặng nhất?
3. Nêu **thứ tự ưu tiên** ba bậc giảm thiểu rủi ro. Vì sao dán nhãn cảnh báo không được dùng thay cho
   che chắn?
4. **Hai câu hỏi** phân biệt các hạng mục kiến trúc là gì? Vì sao câu thứ hai tạo ra khác biệt lớn?
5. Rơ-le an toàn khác rơ-le thường ở điểm nào, và vì sao điểm đó quan trọng?
6. Phân biệt **dừng loại 0, 1, 2**. Loại nào không được dùng cho dừng khẩn cấp, vì sao?
7. Nêu **ba lợi ích** của STO so với ngắt contactor phía trước — và **hai điều STO không làm**.
8. Hai kênh của mạch an toàn đi chung một sợi cáp nhiều lõi. Vì sao đó là lỗi, dù trên sơ đồ vẫn là
   hai kênh?
9. Nêu **ba lỗi thiết kế** làm quy trình LOTO không thực hiện được.
10. Ở chế độ tay, cái gì được nới lỏng và cái gì tuyệt đối không? Nếu cần chuyển động khi cửa mở thì
    phải xử lý thế nào?
11. ⭐⭐ Vì sao viết chương trình an toàn **không phải** là *"lập trình bình thường cộng thêm cẩn thận"*?
    Nêu ba thứ bị cắt bớt.
12. ⚠⚠ Nêu ba **mức người dùng**. ⭐ Chi phí nhảy vọt ở ranh giới nào, và vì sao câu hỏi *"tự viết một
    khối nhỏ thôi mà"* lại là câu hỏi ngân sách chứ không phải câu hỏi kỹ thuật?
13. ⭐ Vì sao lập trình an toàn ưu tiên **FBD và LD** thay vì ST? Liên hệ lý do đó với nguyên tắc ở
    Chương 20 mục 20.6.
14. ⭐ Một tấm che có lỗ để nhìn vào. ⚠ Vì sao *"đã có che chắn"* chưa đủ? ⭐ **Hai** đại lượng nào đi
    cùng nhau, và *"kích thước lỗ"* được đo thế nào với lỗ khe, lỗ vuông, lỗ tròn?
15. ⭐⭐ Chống kẹp có **hai** cách. Cách nào **loại bỏ** mối nguy, cách nào chỉ **giảm** rủi ro?
16. ⚠⚠ **Điểm cuốn** là gì, và nêu bốn cấu hình sinh ra nó. ⭐ Vì sao **không cảm biến nào và không
    logic nào** bảo vệ được? Băng tải của DP-01 thuộc cấu hình nào?

Câu 1, 4 và 7 là ba câu phân loại. Nhưng lưu ý: **trả lời trôi chảy mười câu này không có nghĩa là bạn
đủ thẩm quyền thiết kế mạch an toàn.** Nó có nghĩa là bạn đủ hiểu để làm việc được với người có thẩm
quyền — và biết khi nào phải gọi họ.

---

### Chương tiếp theo

**Chương 48 — Fail-safe & thiết kế phòng sự cố.** Chương này lo lớp an toàn độc lập. Chương 48 lo phần
còn lại: với mỗi ngõ ra, mất nguồn thì về đâu? Đứt dây thì sao? Và vì sao **giám sát phản hồi thay vì
tin lệnh** là nguyên tắc xuyên suốt cả cuốn sách.

---

### Nguồn tham khảo chương 47

- ISO 12100 — *Safety of machinery — General principles for design — Risk assessment and risk reduction*:
  quy trình đánh giá rủi ro và thứ tự ưu tiên giảm thiểu (mục 47.2, 47.3).
- ISO 13849-1 và -2 — *Safety of machinery — Safety-related parts of control systems*: mức hiệu năng,
  hạng mục kiến trúc, và kiểm định (mục 47.5).
- IEC 62061 — *Safety of machinery — Functional safety of safety-related control systems*: thang SIL
  cho máy (mục 47.5).
- IEC 61508 — *Functional safety of electrical/electronic/programmable electronic safety-related
  systems*: tiêu chuẩn gốc về an toàn chức năng, nơi ISO 13849-1 và IEC 62061 lấy khái niệm SIL, vòng
  đời an toàn, mức bao phủ chẩn đoán và hỏng do nguyên nhân chung (mục 47.5 — cây phả hệ).
- IEC 61511 — *Functional safety — Safety instrumented systems for the process industry sector*: nhắc
  ở mục 47.5 để phân biệt SIL ngành quá trình với SIL ngành máy; **không** áp cho máy tự động hoá.
- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: ba loại lệnh dừng, yêu cầu
  với thiết bị dừng khẩn cấp, khởi động lại có chủ ý (mục 47.6).
- IEC 61800-5-2 — *Adjustable speed electrical power drive systems — Safety requirements*: định nghĩa
  các chức năng an toàn của truyền động, trong đó có STO (mục 47.8).
- **Tài liệu hướng dẫn của SICK và Schneider Electric** về thiết bị an toàn — dùng cho phần diễn giải
  khái niệm và ví dụ kiến trúc; nguồn cho định nghĩa **OSSD** và hành vi ngõ ra an toàn (mục 47.7).
- **DGUV / IFA Report 2/2017e** — báo cáo kỹ thuật của viện nghiên cứu an toàn lao động; nguồn cho
  ⭐ **yêu cầu phát hiện chập chéo** trên ngõ ra an toàn (mục 47.7).
- ⭐ **PLCopen Safety — Part 1: Concepts and Function Blocks, v2.10** *(bản chính thức, tải miễn phí
  từ PLCopen)*: §4 *Reduction in the Development Environment* — ⭐⭐ **ba mức người dùng** (cơ bản ·
  mở rộng · hệ thống) và ⚠ **giới hạn tập ngôn ngữ** (FBD/LD ưu tiên, ST chỉ ở mức mở rộng, IL và SFC
  không đặt vấn đề) — nền cho mục 47.4b.
- ⭐ **IRSST (Québec), *Prevention of Mechanical Hazards* (RG-597)** — hướng dẫn về **che chắn cơ khí**:
  ⭐ quan hệ giữa **kích thước lỗ trên che chắn** và **khoảng cách an toàn**; hai cách chống kẹp
  (⭐ **khe hở tối thiểu** — loại bỏ mối nguy — so với **giảm lực/năng lượng**); và ⚠⚠ **bốn cấu hình
  sinh ra điểm cuốn**, trong đó có **con lăn tiếp xúc băng tải** — nền cho mục 47.7.

> ⚠⚠ **Toàn bộ tiêu chuẩn liệt kê ở trên đều có bản quyền và phải mua từ tổ chức phát hành.** Chương
> này diễn giải khái niệm ở mức đủ để trao đổi chuyên môn; **nó không trích dẫn nội dung tiêu chuẩn và
> không thay thế bản gốc**. Mọi con số, ngưỡng, và bảng phân loại dùng để thiết kế thật phải lấy từ bản
> gốc, áp cho đúng phiên bản đang hiệu lực tại thị trường của bạn.
