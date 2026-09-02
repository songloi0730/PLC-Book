
# Phụ lục E — Chỉ mục tra theo triệu chứng

> **Bạn đang đứng trước một cỗ máy không chạy đúng. Bắt đầu từ đây.**
>
> Phụ lục này sắp xếp theo **thứ bạn quan sát được**, không theo thứ bạn cần biết — vì lúc máy hỏng,
> bạn chưa biết mình cần biết gì.

---

> ⚠⚠ **TRƯỚC KHI CHẠM VÀO MÁY**
>
> - ⚠ **Cô lập năng lượng** trước khi chạm phần điện hoặc cơ khí — điện, khí nén, và **năng lượng
>   tích trữ** (Chương 3).
> - ⚠ Nếu phải thử với máy có điện: kiểm tra **không có ai trong vùng nguy hiểm**, và báo người
>   vận hành.
> - ⚠⚠ Công việc chạm mạch điện lực và mạch an toàn phải do **người có thẩm quyền** thực hiện.
> - ⭐ Phụ lục này giúp bạn **thu hẹp phạm vi tìm kiếm**. Nó **không thay thế** quy trình an toàn của
>   cơ sở bạn.

---

## E.1 ⭐⭐ Bốn câu hỏi trước khi tra bảng

Trả lời bốn câu này thường thu hẹp được nửa danh sách nghi phạm:

| # | Câu hỏi | Vì sao quan trọng |
|---|---|---|
| 1 | ⭐⭐ **Cái gì đã thay đổi?** | ⭐ Chương trình mới, thiết bị mới thay, công thức mới, ca mới, thời tiết — **máy không tự nhiên hỏng** |
| 2 | ⭐ **Có tái hiện được không?** | ⚠ Tái hiện được → logic hoặc cấu hình. **Chập chờn → nghi lắp đặt trước** (Ch.49) |
| 3 | ⭐ **Nó luôn hỏng hay chỉ đôi khi?** | Đôi khi → tìm **điều kiện chung** giữa các lần hỏng |
| 4 | **Máy đang ở chế độ nào, bước nào?** | Trạng thái quyết định cái gì được phép chạy |

> ⭐⭐ **Câu 1 là câu có tỉ lệ trúng cao nhất, và là câu hay bị bỏ nhất.** Khi máy chạy tốt ba tháng
> rồi hỏng, ⭐ **thứ hỏng thường không phải thứ chạy tốt ba tháng** — mà là thứ vừa thay đổi.
>
> Hỏi cả những thay đổi "không liên quan": ai đó đấu thêm thiết bị vào tủ, đổi lô vật tư, sửa máy bên
> cạnh, hay chỉ là mùa hè tới và nhiệt độ tủ tăng.

> ⭐ **Nguyên tắc xuyên suốt: đổi MỘT thứ mỗi lần, và ghi lại kết quả.** Đổi ba thứ rồi máy chạy thì
> bạn không biết cái nào đã sửa — và ⚠ **hai cái kia có thể đã tạo ra vấn đề mới** (Chương 51).

---

## E.2 Máy không khởi động được

| Quan sát cụ thể | Nghi trước | Chương |
|---|---|---|
| Nhấn Start không có phản ứng nào | ⭐ **Điều kiện cho phép chạy chưa đủ** — xem danh sách bên dưới | 25, 51 |
| Máy báo "chưa về gốc" | Trình tự về gốc chưa hoàn tất, hoặc cảm biến gốc không tác động | 28 |
| Máy vào Run rồi lập tức về Idle | Một điều kiện cho phép rơi ngay sau khi khởi động | 25, 43 |
| ⚠ Máy tự khởi động sau khi có điện lại | ⚠⚠ **LỖI AN TOÀN — dừng máy và báo ngay** | 47, 48 |
| Không vào được chế độ Auto | Công tắc chế độ, hoặc điều kiện riêng của chế độ | 25 |

### ⭐ Danh sách điều kiện cho phép chạy — kiểm theo thứ tự này

| # | Kiểm | Trên DP-01 |
|---|---|---|
| 1 | ⚠ **Mạch an toàn lành** | `DI_EStopOK`, `DI_CurtainOK`, `DI_Door1Closed`, `DI_Door2Closed` |
| 2 | Không có báo động đang treo | Xem danh sách báo động (Ch.43) |
| 3 | Đã về gốc | Các trục ở vị trí gốc |
| 4 | Năng lượng phụ trợ đủ | `DI_AirOK` — khí nén |
| 5 | Thiết bị phụ sẵn sàng | `DI_VfdReady`, `DI_IonizerOK` |
| 6 | Chọn đúng chế độ | `DI_ModeAuto` |
| 7 | Công thức đã tải và hợp lệ | Ch.32 |

> ⭐⭐ **Nếu máy không nói được điều kiện nào đang thiếu, đó là một lỗi thiết kế cần sửa** — không
> phải một tình huống bình thường phải chịu đựng.
>
> Chương 43 gọi đây là "chuỗi cho phép": máy phải hiện được **điều kiện nào chưa đạt**, không chỉ
> "không sẵn sàng". Đây là thứ rẻ để thêm và tiết kiệm hàng giờ mỗi năm.

---

## E.3 Một ngõ vào không lên

⭐ **Đi theo thứ tự này — từ hiện trường về CPU.** Mỗi bước loại được một nhóm nguyên nhân.

| # | Kiểm | Nếu sai thì |
|---|---|---|
| 1 | ⭐ **Đèn trên chính cảm biến** có sáng khi tác động không? | Không → vấn đề ở cảm biến, nguồn cảm biến, hoặc căn chỉnh |
| 2 | Cảm biến có **nguồn 24 V** không? | Không → cầu chì nhánh, đứt dây nguồn (Ch.49 mục 49.5) |
| 3 | ⭐ **Đèn trên module ngõ vào** có sáng không? | Không → đứt dây giữa cảm biến và module, hoặc sai kiểu PNP/NPN |
| 4 | ⭐ **Bit trong PLC** có lên không? | Không dù đèn module sáng → sai địa chỉ, sai cấu hình module, hoặc module hỏng |
| 5 | Bit lên nhưng chương trình không phản ứng | ⭐ Logic — kiểm điều kiện xung quanh, hoặc bit bị **ghi đè ở chỗ khác** |

| Nguyên nhân | Dấu hiệu đặc trưng | Chương |
|---|---|---|
| ⭐ **Sai PNP/NPN** | Cảm biến sáng đèn, module không nhận | 4 mục 4.5 |
| Sai NO/NC | ⭐ **Logic đảo ngược** — bit lên khi đáng lẽ xuống | 4, 15 |
| Cảm biến lệch / bẩn | Đôi khi nhận, đôi khi không | 4 |
| ⚠ **Cáp gãy lõi trong xích động** | ⭐ Chập chờn **theo tư thế**; đo tĩnh vẫn tốt | 49 mục 49.7 |
| Đầu cốt lỏng | ⚠ **Nặng dần theo thời gian** | 3, 49 |
| Bit bị ghi đè trong chương trình | Bit "nhấp nháy" hoặc không bao giờ giữ | 24, 51 |

> ⭐⭐ **Bước 1 loại được nhiều nhất và mất ít thời gian nhất.** Nhìn đèn trên cảm biến trước khi mở
> phần mềm — nó chia đôi bài toán ngay lập tức.

---

## E.4 Một ngõ ra không tác động

| # | Kiểm | Nếu sai thì |
|---|---|---|
| 1 | ⭐ **Bit trong PLC** có lên không? | Không → vấn đề logic, không phải phần cứng |
| 2 | ⭐ **Đèn trên module ngõ ra** có sáng không? | Không dù bit lên → sai địa chỉ, module hỏng |
| 3 | Có **điện áp tại cầu đấu** không? | Không dù đèn sáng → module hỏng, hoặc mất nguồn nhánh ngõ ra |
| 4 | Có điện áp **tại thiết bị** không? | Không → đứt dây |
| 5 | ⚠ Có điện áp tại thiết bị nhưng nó không chạy | Thiết bị hỏng — hoặc ⭐ **thiếu năng lượng phụ trợ** (khí nén cho van) |

| Nguyên nhân | Dấu hiệu | Chương |
|---|---|---|
| ⭐ **Quá dòng chân chung của module** | Vài ngõ ra cùng nhóm yếu hoặc không tác động khi **cùng bật** | 9 mục 9.4 |
| Nguồn 24 V thiếu công suất | ⭐ Lỗi khi **nhiều cơ cấu cùng tác động**; trông giống lỗi phần mềm | 8 mục 8.7 |
| Van kẹt cơ khí | Có điện, có tiếng, không chuyển động | 5 |
| Thiếu khí nén | ⭐ **Mọi cơ cấu khí nén cùng chậm hoặc không chạy** | 5 |
| Rơ-le hết tuổi thọ | ⚠ Đóng cắt được nhưng **tiếp điểm cháy rỗ** — sụt áp | 9 mục 9.3 |
| Mạch an toàn đang cắt nguồn ngõ ra | ⭐ **Bit lên, đèn module sáng, nhưng không có điện ở cơ cấu** | 47 |

> ⭐⭐ **Hàng cuối gây nhầm lẫn nhiều nhất.** Mạch an toàn cắt nguồn **sau** module ngõ ra — nên PLC
> "tưởng" mình đã bật, đèn module sáng, nhưng cơ cấu không có điện. ⭐ **Kiểm trạng thái rơ-le an toàn
> trước khi nghi module.**

---

## E.5 Giá trị analog sai hoặc nhảy loạn

| Quan sát | Nghi trước | Chương |
|---|---|---|
| ⭐ Giá trị **run liên tục** vài phần trăm | Nhiễu — ⭐ **cáp đi cạnh động lực**, hoặc vòng lặp đất | 31 mục 31.6 · 49 mục 49.4 |
| ⭐ Nhiễu **tăng khi thiết bị công suất chạy** | ⭐⭐ **Ghép nhiễu từ cáp động lực** — dấu hiệu đặc trưng | 49 mục 49.3 |
| Giá trị **luôn bằng 0** | Đứt dây; ⭐ với 4–20 mA thì **phân biệt được**, với 0–10 V thì không | 31 mục 31.7 |
| Giá trị **luôn ở đáy hoặc đỉnh thang** | Sai cấu hình dải, hoặc sai kiểu tín hiệu (áp/dòng) | 31 mục 31.4 |
| ⭐ Giá trị **lệch một hằng số** | Sai hệ số quy đổi, hoặc chưa hiệu chuẩn | 31 |
| Giá trị **nhảy bậc lớn ngẫu nhiên** | Đầu cốt lỏng, hoặc cáp gãy lõi | 49 |
| ⚠ Giá trị **trôi chậm theo tháng** | ⭐⭐ **Cảm biến xuống cấp** — hoặc chính đại lượng đo đang xấu đi (Ch.53) | 53 mục 53.5 |
| Nhiệt độ đọc sai lệch | Sai loại RTD/cặp nhiệt, sai số dây, hoặc thiếu bù đầu lạnh | 33 |

> ⭐⭐ **Hàng "trôi chậm theo tháng" là hàng cần cảnh giác nhất, vì nó KHÔNG trông giống lỗi.** Nó
> trông giống một giá trị bình thường — chỉ là bình thường của tháng này khác bình thường của tháng
> trước.
>
> ⭐ Đây là lý do phải **ghi mốc lúc nghiệm thu** (Chương 8, 36, 40, 49): một phép đo chỉ có nghĩa khi
> có cái để so.

---

## E.6 Mạng rớt hoặc thiết bị mất kết nối

| Quan sát | Nghi trước | Chương |
|---|---|---|
| ⭐ Rớt **ngẫu nhiên**, không theo quy luật | Nhiễu, ⭐ **vòng lặp đất**, hoặc cáp xuống cấp | 40 mục 40.6 · 49 mục 49.4 |
| Rớt **khi cơ cấu chuyển động** | ⭐⭐ **Cáp gãy lõi trong xích động** | 49 mục 49.7 |
| Rớt khi thiết bị công suất chạy | Ghép nhiễu; cáp mạng đi cạnh động lực | 49 mục 49.3 |
| ⭐ **Một thiết bị** mất, các thiết bị khác bình thường | Cáp hoặc cổng của chính thiết bị đó | 40 |
| ⭐ **Tất cả** mất cùng lúc | Chuyển mạch, nguồn nhánh mạng, hoặc cấu hình | 40, 49 mục 49.5 |
| Kết nối được nhưng **dữ liệu sai** | ⭐ Sai địa chỉ thanh ghi, sai thứ tự byte, sai kiểu dữ liệu | 38, 39 |
| Chậm dần rồi mất | Quá tải mạng, hoặc thiết bị đang lỗi | 40 |

> ⭐⭐ **Cách xác nhận cáp gãy lõi:** lắc hoặc di chuyển cáp trong lúc theo dõi **bộ đếm lỗi trên
> chuyển mạch quản lý được**. Số lỗi tăng khi lắc là bằng chứng trực tiếp.
>
> ⚠ Đo thông mạch tĩnh **không phát hiện được** — dây gãy lõi vẫn thông khi nằm yên.

> ⭐ **Ghi số lỗi mạng lúc nghiệm thu.** Con số "12 lỗi từ khi khởi động" vô nghĩa nếu không biết
> tháng trước là bao nhiêu (Chương 40 mục 40.6).

---

## E.7 Chu trình dừng giữa chừng

| Quan sát | Nghi trước | Chương |
|---|---|---|
| ⭐ Dừng ở **cùng một bước** mỗi lần | ⭐ **Điều kiện chuyển tiếp của bước đó không đạt** — kiểm tín hiệu phản hồi | 21, 51 |
| Dừng ở **bước khác nhau** mỗi lần | Điều kiện chung: an toàn, khí nén, nguồn, mạng | E.2 |
| Báo lỗi hết giờ ở một bước | ⭐ Cơ cấu **không tới nơi**, hoặc cảm biến phản hồi hỏng | 21 |
| ⚠ Dừng **không có báo động nào** | ⭐⭐ **Lỗi thiết kế báo động** — hoặc CPU mất điện (Ch.49 mục 49.5) | 43, 49 |
| Dừng khi đổi công thức | Tham số ngoài dải, hoặc thiếu tham số | 32 |
| ⭐ Dừng lúc **hai trạm cùng cần một thứ** | ⭐ **Bế tắc** trong logic điều phối | 26 |
| Dừng khi máy trước/sau bận | Bắt tay chuyền — có thể là **bình thường**, không phải lỗi | 41, 55 mục 55.6 |

> ⭐⭐ **Hàng "dừng không có báo động" xứng đáng được coi là một lỗi phải sửa, không phải một hiện
> tượng phải chịu.**
>
> Máy dừng câm nghĩa là: hoặc trình tự có đường đi mà không ai lường trước, hoặc CPU mất điện cùng
> lúc với sự cố. Cả hai đều cần sửa — và cả hai đều có cách phát hiện rẻ (bit chẩn đoán mỗi bước; ngõ
> vào giám sát nguồn nhánh).

---

## E.8 Sản phẩm hỏng mà máy báo OK

⚠ **Đây là loại lỗi tệ nhất, vì máy không biết mình đang sai.**

| Quan sát | Nghi trước | Chương |
|---|---|---|
| ⭐ Hỏng **tăng dần theo thời gian** | ⭐⭐ **Một thứ đang mòn hoặc suy giảm** — đèn UV yếu dần, cảm biến trôi | 53 mục 53.5 |
| Hỏng theo **lô vật tư** | Vật tư, không phải máy — nhưng máy nên phát hiện được | 32 |
| ⭐ Hỏng khi **chạy nhanh hơn** | ⭐ Thời gian quá trình không đủ; hoặc chuyển tiếp bằng **bộ định thời thay vì phản hồi** | 55 mục 55.5 |
| Hỏng ở **một vị trí cố định** trên sản phẩm | Cơ khí, gá, hoặc dữ liệu công thức | 32, 37 |
| Hỏng sau khi đổi công thức | Tham số sai nhưng **vẫn trong dải hợp lệ** | 32 |
| ⚠ Hỏng **không có triệu chứng tại chỗ** | ⭐ ESD, keo chưa cứng, mối hàn nguội — ⚠ **lộ ra ở công đoạn sau** | 7, 53 |

> ⭐⭐ **Câu hỏi cốt lõi cho cả nhóm này: máy có phép đo nào để biết việc nó vừa làm là ĐÚNG không —
> hay nó chỉ biết mình đã LÀM?**
>
> Trên DP-01, `AI_UvIntensity` tồn tại đúng vì lý do đó: đèn vẫn sáng, chu trình vẫn xong, máy vẫn
> báo OK — nhưng cường độ đã tụt và keo cứng chưa đủ.
>
> ⭐ Khi thiết kế máy, hãy hỏi câu này cho **mọi bước gia công**. Chỗ nào không trả lời được là chỗ
> lỗi có thể trốn thoát (Chương 43, 53, 57).

---

## E.9 Chuyền tắc hoặc sản lượng thấp

| Quan sát | Nghi trước | Chương |
|---|---|---|
| ⭐ **Trạm nào cũng chờ** | Máy trước không cấp đủ hàng — ⚠ **nút cổ chai nằm ngoài máy bạn** | 55 mục 55.4 |
| ⭐ **Một trạm gần như không bao giờ chờ** | ⭐⭐ **Đó là nút cổ chai** | 55 mục 55.3 |
| Sản lượng thấp hơn tính toán mà không thấy dừng | ⭐ Chu kỳ thực **dài hơn** chu kỳ thiết kế — đo lại từng bước | 55 mục 55.4 |
| ⭐ Trung bình đẹp, sản lượng vẫn thiếu | ⭐ Thỉnh thoảng có chu trình **rất dài** — xem giá trị **lớn nhất** | 55 mục 55.4 |
| Mất nhiều thời gian ở đổi lô | Thời gian xả máy + nạp công thức | 55 mục 55.6 |
| ⭐ **Dừng ngắn nhiều lần** | ⭐⭐ Thường ăn sản lượng **nhiều hơn** cả việc tối ưu chu kỳ | 55 mục 55.6 |
| Board kẹt lặp lại ở một chỗ | Cơ khí, gá, hoặc căn chỉnh — không phải chương trình | 51 |

> ⭐⭐ **Trước khi tối ưu bất cứ thứ gì, tìm nút cổ chai bằng dữ liệu: đo phần trăm thời gian chờ của
> từng trạm.** Tối ưu chỗ khác **không tăng sản lượng**, dù công sức bỏ ra rất thật (Chương 55).

---

## E.10 ⭐ Lỗi chập chờn không tái hiện được

⚠ **Nhóm này có quy tắc riêng, và nó tiết kiệm nhiều thời gian nhất trong cả phụ lục.**

> ⭐⭐ **Lỗi chập chờn không tái hiện được → NGHI LẮP ĐẶT TRƯỚC KHI NGHI LOGIC.**

| Nghi phạm | Dấu hiệu đặc trưng | Chương |
|---|---|---|
| 1 | ⭐ **Cáp tín hiệu song song cáp động lực** — lỗi đúng lúc thiết bị công suất chạy tải nặng | 49 mục 49.3 |
| 2 | ⭐ **Vòng lặp đất** — analog run, mạng rớt gói, đo được điện áp giữa hai điểm đất | 49 mục 49.4 |
| 3 | Vỏ chống nhiễu nối sai số đầu, hoặc bện thành sợi thay vì kẹp 360° | 49 mục 49.4 |
| 4 | ⭐ **Nguồn 24 V thiếu công suất** — lỗi khi nhiều cơ cấu cùng tác động | 8 mục 8.7 |
| 5 | ⭐ **Cáp thường trong xích động** — mất tín hiệu theo tư thế, đo tĩnh vẫn tốt | 49 mục 49.7 |
| 6 | Đầu cốt lỏng — ⚠ **nặng dần theo thời gian** | 3, 49 mục 49.6 |
| 7 | Nhiệt độ tủ — lỗi xuất hiện vào buổi chiều hoặc mùa nóng | 8 |
| 8 | ⭐ Logic phụ thuộc **thời gian quét** — đặc biệt sau khi đổi PLC | 7, 56 mục 56.4 |

> ⭐ **Cách tìm điều kiện chung:** ghi lại **thời điểm** mỗi lần lỗi, rồi đối chiếu với: ca làm việc,
> mã hàng đang chạy, thiết bị công suất nào đang chạy, nhiệt độ, và ai đang vận hành.
>
> ⭐⭐ Ba lần lỗi có ghi thời điểm giá trị hơn ba mươi giờ đoán.

---

## E.11 Sau khi thay đổi thứ gì đó

| Vừa thay đổi | Nghi trước | Chương |
|---|---|---|
| ⭐ **Nạp chương trình mới** | Thay đổi vừa nạp; ⚠ và **bộ đếm giữ được có bị xoá không** | 12, 53 |
| Đổi CPU / PLC | ⭐⭐ **Thời gian quét khác** · tràn số · hành vi bộ định thời | 56 mục 56.4 |
| Thay cảm biến | Sai loại PNP/NPN, sai NO/NC, sai căn chỉnh | 4 |
| Thay biến tần | ⭐ **Tham số chưa nạp lại** | 36, 54 |
| Đổi công thức | Tham số ngoài dải, hoặc thiếu tham số | 32 |
| Đấu thêm thiết bị vào tủ | ⭐ **Quá tải nguồn 24 V**; hoặc thêm nguồn nhiễu | 8, 49 |
| Sửa máy bên cạnh | Đất chung, nguồn chung, hoặc bắt tay chuyền | 41, 49 |
| ⚠ Chạm mạch an toàn | ⚠⚠ **Phải đánh giá lại** — không chỉ kiểm tra chạy được | 47, 48, 53 |

> ⭐⭐ **Bảng này là lý do câu hỏi "cái gì đã thay đổi?" đứng đầu phụ lục.** Nếu bạn trả lời được nó,
> bạn thường nhảy thẳng tới đúng hàng.

---

## E.12 Khi vẫn không tìm ra

| Bước | Nội dung | Chương |
|---|---|---|
| 1 | ⭐ **Viết ra những gì đã loại trừ**, và bằng chứng nào loại trừ nó | 51 |
| 2 | ⭐⭐ **Kiểm lại giả định đầu tiên** — thứ bạn "chắc chắn" thường là chỗ sai |  |
| 3 | ⭐ **Hỏi người vận hành**: *"anh/chị phải làm gì mà máy đáng lẽ nên tự làm?"* | 56 mục 56.4 |
| 4 | So với **mốc đo lúc nghiệm thu** | 8, 36, 40, 49 |
| 5 | ⭐ **Kể lại vấn đề cho người khác nghe** — thường bạn tự tìm ra khi đang kể |  |
| 6 | Nghỉ, rồi quay lại | ⚠ Quyết định lúc mệt là quyết định tệ (Ch.56 mục 56.5) |
| 7 | ⭐ Ghi lại sự cố theo mẫu năm dòng, kể cả khi chưa giải quyết xong | 58 mục 58.6 |

> ⭐⭐ **Bước 2 là bước có tỉ lệ trúng cao nhất trong bảng.** Khi đã tìm lâu mà không ra, nguyên nhân
> thường không nằm ở chỗ bạn chưa nhìn — mà nằm ở chỗ bạn **đã nhìn và cho là đúng**.
>
> Câu hỏi cụ thể: *"tôi đang tin điều gì mà chưa tự mình kiểm chứng?"* — sơ đồ nói vậy, người khác
> nói vậy, lần trước là vậy. ⭐ Kiểm lại một trong số đó.

---

## E.13 Dẫn về đâu

| Bạn cần | Đọc |
|---|---|
| Phương pháp chẩn đoán có hệ thống | ⭐ **Chương 51** |
| Thiết kế báo động nói được **phải làm gì** | Chương 43 |
| Quy tắc lắp đặt và chống nhiễu | ⭐ **Chương 49** |
| Đo chu kỳ, tìm nút cổ chai | Chương 55 |
| Theo dõi sự trôi trước khi thành lỗi | Chương 53 mục 53.5 |
| Bảng I/O và trình tự của DP-01 | **Phụ lục J** |
| Công thức tính, kèm điều kiện áp dụng | **Phụ lục K** |

> ⚠⚠ **Nhắc lại giới hạn.** Phụ lục này liệt kê **nghi phạm thường gặp**, không phải chẩn đoán. Nó
> giúp bạn thu hẹp phạm vi tìm kiếm nhanh hơn.
>
> ⚠ Nó **không thay thế**: quy trình an toàn của cơ sở bạn, hướng dẫn của nhà sản xuất thiết bị, hay
> ⚠⚠ **người có thẩm quyền** khi công việc chạm mạch điện lực hoặc mạch an toàn.
