
# Phụ lục D — Checklist đấu dây & bật nguồn lần đầu

> ⚠⚠ **ĐỌC TOÀN BỘ MỤC NÀY TRƯỚC KHI DÙNG DANH MỤC BÊN DƯỚI**
>
> Bật nguồn một tủ điện lần đầu là thời điểm **nhiều thứ có thể sai cùng lúc**, và một số thứ sai gây
> hậu quả cho **người**, không chỉ cho thiết bị.
>
> Phụ lục này **không thay thế**:
>
> - **kiến thức và giấy phép an toàn điện** — đọc Chương 3;
> - **quy trình của cơ sở bạn** — nếu nó khác phụ lục này, ⭐ **theo quy trình của cơ sở**;
> - **người có thẩm quyền** — mọi thao tác chạm mạch điện lực và mạch an toàn phải do người có thẩm
>   quyền thực hiện hoặc kiểm tra;
> - hướng dẫn của **nhà sản xuất thiết bị**.
>
> ⚠ Nó là **danh mục nhắc việc** cho người đã biết mình đang làm gì — không phải hướng dẫn cho người
> chưa biết.

---

## D.1 ⭐ Nguyên tắc của cả phụ lục

| # | Nguyên tắc | Vì sao |
|---|---|---|
| 1 | ⭐⭐ **Cấp điện theo từng lớp, không cấp hết một lần** | Một lỗi tại một thời điểm dễ tìm; năm lỗi cùng lúc thì không |
| 2 | ⭐ **Đo trước, bật sau** | Đo mất vài phút; sửa một module cháy mất vài ngày |
| 3 | ⭐ **Rút cầu chì / tháo cầu đấu để cô lập** | Cô lập phần chưa cần |
| 4 | ⚠ **Không bao giờ làm một mình lần bật đầu tiên** | Cần người thứ hai ở nút ngắt |
| 5 | ⭐ **Ghi lại mọi giá trị đo** | ⭐⭐ Chúng trở thành **mốc** cho cả vòng đời máy |
| 6 | ⚠ **Dừng khi gặp điều bất ngờ** | Đừng "thử bật lại xem sao" |

> ⭐⭐ **Nguyên tắc 1 là nguyên tắc quan trọng nhất.** Cấp điện toàn bộ tủ cùng lúc rồi thấy "có gì đó
> sai" là tình huống tệ nhất — bạn không biết bắt đầu từ đâu, và một số thiết bị có thể đã hỏng.
>
> Trình tự ở D.4 chia việc cấp điện thành **sáu lớp**, mỗi lớp kiểm xong mới sang lớp sau.

---

## D.2 Trước khi có điện — kiểm nguội

⚠ **Toàn bộ mục này làm khi tủ CHƯA có điện, đã cô lập và khoá nguồn** (Chương 3).

### Cơ khí và lắp đặt

- [ ] Thiết bị lắp chắc, đúng chiều, đủ khoảng thoát nhiệt theo hướng dẫn nhà sản xuất
- [ ] ⭐ Nhãn thiết bị **khớp danh mục vật tư** — đúng mã, đúng phiên bản
- [ ] ⚠⚠ **Bộ nguồn 24 V có nhãn SELV / PELV / Class 2 / Limited Power** — ⭐ **không có nhãn thì
      tra datasheet, đừng giả định** (Chương 3, mục 3.3)
- [ ] Không có mạt kim loại, đầu dây thừa, dụng cụ bỏ quên trong tủ
- [ ] ⭐ **Tách máng đúng ba nhóm**: động lực · tín hiệu · an toàn (Chương 49 mục 49.3)
- [ ] Cáp giao nhau **cắt vuông góc**, không đi song song đường dài
- [ ] ⭐ Cáp trong xích động là **loại chịu uốn**, đúng bán kính uốn (Chương 49 mục 49.7)
- [ ] Quạt và lọc gió tủ lắp đúng chiều

### Dây và đầu nối

- [ ] ⭐ **Mọi dây có số ở CẢ HAI đầu**, khớp sơ đồ (Chương 49 mục 49.6)
- [ ] ⭐ Số dây khớp **bảng I/O** và khớp tên tag trong chương trình
- [ ] Đầu cốt siết đủ lực — ⚠ **kéo nhẹ từng dây để kiểm**
- [ ] Không có lõi đồng thò ra ngoài đầu cốt
- [ ] Tiết diện dây đúng sơ đồ
- [ ] ⭐ Cầu đấu dự phòng còn trống, không bị dùng tạm

### Nối đất và chống nhiễu

- [ ] ⚠⚠ **Vỏ tủ và vỏ mọi thiết bị đã nối đất bảo vệ** — đo thông mạch tới thanh PE
- [ ] ⭐⭐ **0 V nối PE ở ĐÚNG MỘT ĐIỂM** — xác định trên sơ đồ, rồi **đo xác nhận** (Chương 49 mục 49.4)
- [ ] Vỏ chống nhiễu nối đúng số đầu: analog **một đầu**, cáp động cơ **hai đầu**
- [ ] ⭐ Vỏ nối bằng **kẹp trọn vòng 360°**, không bện thành sợi vặn vít
- [ ] Cửa tủ có dây nối đất mềm

### Đo cách điện và ngắn mạch

- [ ] ⚠ **Đo thông mạch từng nhánh 24 V xuống 0 V** — ⭐ **không được thông** (nếu thông là có ngắn mạch)
- [ ] Đo cách điện mạch động lực theo quy định — ⚠ **do người có thẩm quyền thực hiện**
- [ ] ⚠⚠ **Ngắt kết nối thiết bị điện tử trước khi đo cách điện** — điện áp đo cao sẽ phá module

> ⚠⚠ **Hàng cuối là hàng gây thiệt hại đắt nhất trong cả phụ lục nếu bỏ qua.**
>
> Megôm kế tạo **điện áp một chiều cao — thường tới 1000 V** để đo cách điện. ⭐ Đưa 1000 V vào một
> mạch chứa module PLC 24 V thì **mọi module, biến tần và HMI còn đấu vào đó đều hỏng**.
>
> ⭐ **Ngắt ra trước, đo sau.** Không có cách sửa nào rẻ hơn việc nhớ bước này.
>
> *(Đối chiếu: Kuphaldt — Lessons in Electric Circuits (DC), mục megohmmeter.)*

### Mạch an toàn — kiểm nguội

- [ ] ⚠ Mạch an toàn đi **máng riêng**, dùng **màu dây riêng** nếu quy định yêu cầu
- [ ] ⚠⚠ Tín hiệu an toàn dùng tiếp điểm **NC** — đứt dây làm máy dừng (Chương 4, 47)
- [ ] Rơ-le an toàn đấu đúng sơ đồ của nhà sản xuất, ⚠ **kể cả mạch giám sát tiếp điểm**
- [ ] ⚠ **Không có đường tắt tạm thời nào trong mạch an toàn** — kiểm bằng mắt từng đầu cốt

> ⚠⚠ **Đường tắt tạm trong mạch an toàn là thứ phải tìm chủ động, không phải chờ phát hiện.** Nó
> thường được đấu trong lúc chạy thử để "khỏi phải đóng cửa liên tục" — và ⭐ **rất dễ ở lại đó**.
>
> Kiểm bằng mắt, và sau đó kiểm bằng chức năng ở D.5.

---

## D.3 ⭐ Chuẩn bị trước khi bật

- [ ] ⭐ **Có người thứ hai**, biết nút ngắt ở đâu
- [ ] Biết **nút ngắt nguồn chính** ở đâu và mở được nhanh
- [ ] Có sẵn: đồng hồ đo, sơ đồ điện, bảng I/O, ⭐ **danh mục này đã in ra**
- [ ] Có **bình chữa cháy phù hợp cho thiết bị điện** trong tầm với
- [ ] ⚠ Khu vực xung quanh máy **không có người không liên quan**
- [ ] ⚠ **Mọi cơ cấu chuyển động đã được cô lập** — tháo khí nén, hoặc chặn cơ khí
- [ ] ⭐ Chuẩn bị **biểu mẫu ghi giá trị đo** (Phụ lục C.9)

> ⭐⭐ **Hàng "cô lập cơ cấu chuyển động" đáng làm dù thấy phiền.** Lần bật đầu tiên là lúc dễ có
> **ngõ ra bật ngoài ý muốn** nhất: sai địa chỉ, chương trình còn ở trạng thái thử nghiệm, hoặc ngõ
> ra bị cưỡng bức từ lần kiểm trước và không ai gỡ.
>
> ⚠ Không có khí nén thì một van bật nhầm **không làm gì cả**. Đó là cách rẻ nhất để biến một lỗi
> thành một ghi chú.

---

## D.4 ⭐⭐ Trình tự cấp điện — sáu lớp

⚠ **Mỗi lớp phải kiểm xong mới sang lớp sau.** Gặp bất ngờ ở lớp nào thì **dừng và tìm ra nguyên
nhân** trước khi đi tiếp.

### Lớp 1 — Nguồn vào, chưa có gì phía sau

⭐ Rút hết cầu chì nhánh, hoặc tháo cầu đấu ra tải.

- [ ] Đóng nguồn chính
- [ ] Đo **điện áp vào** — đúng cấp điện áp, đúng số pha
- [ ] ⚠ Đo **thứ tự pha** nếu có thiết bị ba pha nhạy chiều quay
- [ ] Kiểm không có mùi, tiếng động lạ, hay thiết bị nóng bất thường

### Lớp 2 — Bộ nguồn 24 V, chưa có tải

- [ ] Cấp điện cho bộ nguồn 24 V
- [ ] ⭐ **Đo điện áp ra**: khoảng 24 V, ⭐ **ghi giá trị lại**
- [ ] Kiểm đúng cực tính tại cầu đấu phân phối
- [ ] ⚠ Đo lại giữa 0 V và PE — xác nhận **chỉ nối một điểm**

### Lớp 3 — Từng nhánh 24 V, mỗi lần một nhánh

⭐ **Cắm lại từng cầu chì một, không cắm hết cùng lúc.**

- [ ] Nhánh CPU và module — đo điện áp, kiểm đèn nguồn
- [ ] Nhánh cảm biến — đo điện áp, ⭐ **kiểm đèn trên vài cảm biến**
- [ ] Nhánh cơ cấu chấp hành — đo điện áp; ⚠ **cơ cấu chưa có khí nén nên chưa động**
- [ ] Nhánh mạng và truyền thông — đo điện áp, kiểm đèn thiết bị
- [ ] ⭐ Sau mỗi nhánh: kiểm điện áp **có tụt không** — tụt nhiều nghĩa là quá tải hoặc ngắn mạch

> ⚠ **Nếu một cầu chì nhảy ngay khi cắm: KHÔNG cắm lại cái mới.** Tìm nguyên nhân trước — thường là
> ngắn mạch hoặc đấu ngược cực tính. ⭐ Cắm lại lần hai chỉ làm hỏng thêm.

### Lớp 4 — CPU và module

- [ ] CPU lên nguồn, ⭐ **kiểm đèn trạng thái** — so với bảng đèn trong tài liệu CPU
- [ ] ⚠ CPU **ở chế độ STOP**, chưa nạp chương trình chạy máy
- [ ] Kiểm module I/O được nhận đủ, đúng khe cắm
- [ ] ⭐ **Nạp cấu hình phần cứng trước**, chưa nạp chương trình
- [ ] Kiểm không có lỗi chẩn đoán module

### Lớp 5 — ⚠⚠ Mạch an toàn

⚠ **Lớp này do người có thẩm quyền thực hiện hoặc kiểm tra.**

- [ ] Cấp điện mạch an toàn
- [ ] ⭐ Rơ-le an toàn **không tự đóng** khi có điện — phải Reset có chủ ý
- [ ] Kiểm từng kênh của mạch hai kênh
- [ ] ⚠ Kiểm mạch giám sát tiếp điểm hoạt động
- [ ] ⚠⚠ **Kiểm không còn đường tắt nào** — xem D.5

### Lớp 6 — Kiểm I/O, chưa chạy chương trình máy

- [ ] ⭐ **Kiểm từng ngõ vào bằng cách tác động thật** (Phụ lục C.6)
- [ ] ⚠ Kiểm ngõ ra bằng cưỡng bức — ⚠⚠ **chỉ khi cơ cấu vẫn còn cô lập**
- [ ] ⚠⚠ **GỠ** (không phải tắt) mọi cưỡng bức sau mỗi phép thử — danh sách phải **rỗng**
- [ ] Kiểm giá trị analog thô hợp lý
- [ ] Kiểm mạng: mọi thiết bị được nhận, ⭐ **ghi số lỗi ban đầu**

> ⭐⭐ **Chỉ sau khi lớp 6 xong mới nạp chương trình máy và cấp khí nén.** Từ đó trở đi bạn chuyển
> sang Chương 52 — chạy khô, chạy chậm, chạy có phôi.

---

## D.5 ⚠⚠ Kiểm chức năng an toàn

⚠ **Đây là hạng mục nghiêm ngặt nhất, và nó không thuộc về người lập trình một mình.**

- [ ] ⚠ **Từng nút dừng khẩn cấp** thử riêng — ⭐ **cả ba nút phải thử cả ba**
- [ ] Từng cửa bảo vệ thử riêng
- [ ] Rèm quang: thử ⭐ **ở nhiều vị trí dọc chiều cao**, không chỉ ở giữa
- [ ] ⚠⚠ **Ngõ ra OSSD đấu vào thiết bị an toàn**, KHÔNG vào ngõ vào PLC thường — ⭐ nếu bit trạng
      thái nhấp nháy rất nhanh thì đó là **xung kiểm tra**, không phải rèm quang bị cắt (Chương 47,
      mục 47.7)
- [ ] ⚠⚠ Khôi phục sau khi tác động: máy **KHÔNG tự chạy lại**, phải Reset có chủ ý
- [ ] ⚠ Mất điện rồi có lại: máy **KHÔNG tự vào Running**
- [ ] Kiểm chức năng dừng đúng **loại dừng** đã thiết kế
- [ ] ⭐ Ghi kết quả vào **biên bản nghiệm thu an toàn** (Phụ lục C.8)
- [ ] ⭐ Ghi **mã kiểm tra** của chương trình an toàn tại thời điểm nghiệm thu

> ⚠⚠ **"Thử cả ba nút" không phải chi tiết vụn vặt.**
>
> Một nút dừng khẩn cấp đấu sai — hoặc đấu vào kênh sai của mạch hai kênh — **không lộ ra khi thử nút
> khác**. Máy vẫn dừng, mọi thứ trông ổn, và cái nút sai đó nằm im cho tới ngày ai đó cần nó.
>
> ⭐ Cùng lý do: rèm quang phải thử ở **nhiều vị trí**, vì một tia bị lệch chỉ lộ ra ở đúng vị trí đó.

> ⚠⚠ **Kiểm chức năng an toàn không thay thế kiểm định.** Danh mục này giúp bạn phát hiện lỗi sớm;
> ⚠ **việc xác nhận máy đạt mức an toàn yêu cầu là việc của người có thẩm quyền**, theo tiêu chuẩn
> hiện hành tại thị trường của bạn (Chương 48).

---

## D.6 ⭐⭐ Ghi mốc — làm ngay, không để sau

⭐ **Mười phút ở đây đổi lấy khả năng trả lời "cái này có bình thường không" trong suốt vòng đời máy.**

| Đo | Giá trị | Điều kiện đo |
|---|---|---|
| Điện áp 24 V — không tải | ______ V | |
| ⭐ **Điện áp 24 V — tải nặng nhất** | ______ V | ⭐ Ghi rõ **bước nào** |
| Dòng tổng 24 V ở tải nặng nhất | ______ A | |
| Điện áp vào, từng pha | ______ V | |
| Dòng động cơ ở tải bình thường | ______ A | |
| ⭐ Số lỗi mạng sau 8 giờ chạy | ______ | Trên chuyển mạch quản lý được |
| Điện áp giữa hai điểm đất xa nhau | ______ V | ⭐ Nên gần 0 |
| Nhiệt độ trong tủ khi chạy ổn định | ______ °C | Ghi cả nhiệt độ phòng |

> ⭐⭐ **Hàng "điện áp 24 V khi tải nặng nhất" là hàng giá trị nhất.**
>
> Sáu tháng sau, ai đó đo được 23,1 V và hỏi *"có bình thường không?"*. Nếu mốc là 23,8 V thì có thứ
> đang xấu đi. Nếu mốc là 23,0 V thì mọi thứ vẫn vậy. ⚠ **Không có mốc thì không có câu trả lời** —
> chỉ có phỏng đoán.

---

## D.7 ⚠ Khi gặp bất ngờ

| Hiện tượng | ⚠ Làm gì |
|---|---|
| Cầu chì nhảy ngay khi cắm | ⚠⚠ **Không cắm lại cái mới.** Cô lập, tìm ngắn mạch hoặc ngược cực |
| Mùi khét | ⚠⚠ **Cắt nguồn ngay.** Tìm ra nguồn mùi trước khi bật lại |
| Thiết bị nóng bất thường | Cắt nguồn; kiểm tải, kiểm cực tính, kiểm thông gió |
| Điện áp 24 V tụt nhiều khi có tải | ⭐ Nguồn thiếu công suất, hoặc dây quá nhỏ (Chương 8 mục 8.7) |
| ⚠ Cơ cấu chuyển động ngoài ý muốn | ⚠⚠ **Cắt nguồn.** Kiểm ngõ ra bị cưỡng bức, sai địa chỉ, hoặc chương trình sai |
| CPU báo lỗi cấu hình | Đối chiếu cấu hình phần cứng với module thật, đúng khe cắm |
| Module I/O không được nhận | Kiểm cắm chắc, nguồn module, phiên bản firmware |
| ⚠ Rơ-le an toàn không Reset được | ⚠ Kiểm **cả hai kênh** và mạch giám sát tiếp điểm — ⭐ **đừng nối tắt để "thử xem"** |
| Giá trị analog vô lý | Kiểm kiểu tín hiệu (áp/dòng), cấu hình module, cực tính |

> ⚠⚠ **Hàng cuối cùng đáng nhấn mạnh: nối tắt một mạch an toàn "để thử xem" là cách những đường tắt
> vĩnh viễn ra đời.**
>
> Nếu buộc phải làm để chẩn đoán: ⭐ **ghi vào nhật ký, dán nhãn tại chỗ, và ghi giờ dự kiến gỡ** — và
> ⚠ **gỡ trước khi rời máy** (Chương 53 mục 53.4).

---

## D.8 Dẫn về đâu

| Bạn cần | Đọc |
|---|---|
| ⚠ An toàn điện, cô lập năng lượng | **Chương 3** |
| Quy tắc lắp đặt, tách cáp, nối đất | ⭐ **Chương 49** |
| Chức năng an toàn và nghiệm thu | ⚠ **Chương 47, 48** |
| Chạy thử sau khi bật nguồn xong | **Chương 52** |
| Biểu mẫu kiểm I/O và nghiệm thu | **Phụ lục C.6, C.8, C.9** |
| Khi máy đã chạy mà có lỗi | **Phụ lục E** · Chương 51 |

---

> ⚠⚠ **Nhắc lại, vì đây là phụ lục mang cờ cảnh báo.**
>
> Danh mục này là **công cụ nhắc việc**, không phải giấy phép. Nó **không thay thế**: đào tạo an toàn
> điện, quy trình của cơ sở bạn, hướng dẫn của nhà sản xuất, hay ⚠⚠ **người có thẩm quyền**.
>
> ⚠ Phần đấu nối điện lực và toàn bộ phần mạch an toàn phải do người có chuyên môn phù hợp thực hiện
> hoặc kiểm tra, theo tiêu chuẩn và quy định hiện hành tại thị trường của bạn.
>
> ⭐ Nếu có bất kỳ điều gì trong danh mục này bạn không chắc chắn về ý nghĩa — ⭐ **hãy hỏi trước khi
> bật nguồn**, không phải sau.
