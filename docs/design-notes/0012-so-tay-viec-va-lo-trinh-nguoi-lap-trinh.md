# 0012 — Đợt 66: "nhắc phải làm mà không có cách làm", và "nhiều phần không liên quan"

**Trạng thái:** ✅ **XONG giai đoạn 1 — 2026-10-01** · giai đoạn 2, 3 xem mục 7
**Ngày:** 2026-10-01
**Thuộc:** đợt 66 — hai nhận xét gửi tới chủ dự án, kèm yêu cầu *"hãy thử phản biện và tiếp tục cải
thiện sách"*:

1. Chủ dự án, khi đọc: *"được nhắc tới khá nhiều kiến thức mới, nhắc tôi phải làm nó nhưng không có
   hướng dẫn chi tiết hay các tiêu chuẩn, tính là đạt, các quy tắc hay các thông số, mẹo dạng sổ tay
   ngành để áp dụng."*
2. Người lập trình PLC khác, khi đọc bản thảo: *"có nhiều phần không liên quan — chỉ cần quan tâm tới
   mapping, IO và viết chương trình."*

---

## 1. Phản biện nhận xét 1 — đo trước khi tin

| Phép đo (trên bản trước đợt 66) | Kết quả | Kết luận |
|---|---|---|
| Câu chỉ thị *phải / cần / nên + động từ việc làm*, có số, bảng, mã hay con trỏ mục trong 8 dòng quanh nó | 303 câu, **6 %** không có gì | ⚠ Nhận xét **không đúng** theo nghĩa hẹp: sách hiếm khi bảo làm mà không trỏ đi đâu |
| Cụm *"đạt khi / xong khi / tiêu chí"* theo nhóm chương | Lõi lập trình (10, 11, 14–30): 40 lần, **vắng hẳn ở Ch.10, 11, 16, 19, 24, 29**. Chạy thử–bảo trì (50–55): **3 lần**, vắng hẳn ở **Ch.52, 54, 55** | ⭐⭐ Nhận xét **đúng** ở đây: có quy trình, có lý do, nhưng **thiếu định nghĩa "xong"** đúng ở những chương người ta làm theo từng bước |
| Chỗ bảo *"cộng biên"*, *"nhiều lần"*, *"khoảng thời gian dài"*, *"vượt ngưỡng"* mà không có số | Ch.6 Bẫy 7 (giới hạn xy-lanh) · Ch.18 mục 18.4 (thời gian lọc) · Ch.26 mục 26.4 (*máy đứng chờ*) · Ch.51 (ngưỡng thời gian hành trình) | ⭐ **Đúng.** Đây là đúng loại câu khiến người đọc thấy *"bị nhắc mà không biết làm tới đâu"* |
| Cùng một con số ở nhiều nơi, không nơi nào nói cách chọn | Giới hạn bước: Phụ lục J mục J.3 ghi 1–2 s, khối mã Ch.26–27 dùng 3 s và 5 s | ⚠ Người đọc so hai chỗ sẽ không biết chỗ nào đúng |
| Sách có sẵn phần "sổ tay" chưa? | Có, nhưng **rải**: biểu mẫu (C), mẫu mã (L), cấu hình (M), quy ước (N), checklist ở Ch.23 mục 23.2b, Ch.27 mục 27.8, Ch.52 mục 52.9 | Thiếu **một chỗ theo thứ tự công việc** nối chúng lại, kèm con số |

⭐ **Kết luận nhận xét 1:** đúng về **tiêu chí đạt** và **con số quyết định**, không đúng về *"không có
hướng dẫn"*. Cách sửa vì vậy không phải viết thêm giải thích, mà là **định nghĩa "xong" và cho con số**
— kèm nhãn nguồn, vì người đọc cần biết con số nào là chuẩn, con số nào là kinh nghiệm.

## 2. Phản biện nhận xét 2 — đúng một nửa

| | |
|---|---|
| ✅ **Đúng** | Với vai trò *chỉ lập trình*, khoảng một phần ba sách là việc của người khác. Ba lộ trình đọc của Ch.1 chia theo **xuất phát điểm** (chuyển ngành · thợ điện · dân phần mềm), **không** chia theo **vai trò** — nên người lập trình không có lối đi tắt |
| ⭐⭐ **Đúng hơn họ nghĩ** | Chính phần họ coi là trọng tâm — **ánh xạ I/O** — là phần sách **dạy mỏng nhất**: `Prg_IoRead` chỉ xuất hiện như một dòng trong cây chương trình (Ch.14 mục 14.7) và danh sách lời gọi (Ch.57); cùng một tín hiệu đã lọc mang **ba tên** ở ba chương (`M_Board1Present` ở Ch.17, `X_BoardStn1` ở Ch.50, đọc thẳng `DI_BoardStn1` ở Ch.26); Phụ lục N mục N.6 thiếu tiền tố `X_` mà Ch.30 đã quy định |
| ⚠ **Sai** | Ba thứ "của người khác" quyết định **dòng mã** của người lập trình: NPN/PNP và NO/NC quyết định `1` nghĩa là gì trong dòng ánh xạ; van một cuộn và trạng thái an toàn từng ngõ ra quyết định cổng cho phép và cấu hình ngõ ra khi CPU dừng; ranh giới phần an toàn quyết định cái gì **không được** viết bằng logic thường. Thiếu ba thứ này thì mã đúng cú pháp mà sai nghĩa — không bộ kiểm nào bắt được |

## 3. Quyết định 1 — trả lời nhận xét 2 bằng cách nào

| Phương án | Ưu | Nhược |
|---|---|---|
| A. Cắt hoặc rút gọn các chương "không liên quan" | Sách mỏng hơn | ⚠⚠ Trái mục tiêu bao trùm đã chốt (ADR 0002 §1: *không phải đi tìm tài liệu khác*); mất đúng phần quyết định nghĩa của dòng ánh xạ (mục 2) |
| B. Tách hai tập: *Lập trình* và *Hiện trường* | Mỗi tập gọn cho một vai trò | ⚠ Hơn 2 000 con trỏ chéo trong sách phải rà lại; quyết định cấu trúc lớn — **của chủ dự án** |
| ⭐ C. **Thêm lộ trình theo vai trò + dạy kỹ đúng phần lõi họ cần** | Không mất nội dung; người lập trình có lối đi tắt có căn cứ; phần mỏng nhất (ánh xạ I/O) được viết đủ | Lộ trình phải giữ khớp khi chương đổi |

⭐ **Chọn C**, giữ B làm lựa chọn để chủ dự án quyết sau (mục 7). Cụ thể: **lộ trình D** ở Ch.1 mục 1.2b
— *lõi · giao diện (đúng mục nào) · bỏ qua được (trừ khi)* — kèm ô ⚖ trả lời thẳng nhận xét; và **mục
mới Ch.27 mục 27.3c** dạy tầng ánh xạ vào/ra.

## 4. Quyết định 2 — đặt "sổ tay việc" ở đâu

| Phương án | Ưu | Nhược |
|---|---|---|
| A. Thêm ô *"đạt khi"* và con số vào từng chương | Gặp đúng lúc đọc | ⚠ Rải tiếp — đúng cái bệnh đang chữa; người làm việc theo dự án vẫn phải lật 20 chương |
| ⭐ B. **Phụ lục mới — Phụ lục O, mười sáu thẻ theo thứ tự một dự án**; chương chỉ thêm con số tại chỗ đang thiếu và trỏ sang thẻ | ⭐ Một chỗ, đúng thứ tự công việc, in ra mang theo được — đúng *"dạng sổ tay ngành"*; không phá khung chương | Thêm một phụ lục phải giữ khớp với chương (thẻ chỉ **trỏ**, không chép giải thích) |
| C. Mở rộng Phụ lục C hoặc M | Không thêm phụ lục | C là biểu mẫu, M là cấu hình — nhét quy trình và con số vào làm hỏng vai của cả hai |

⭐ **Chọn B.** Khuôn mỗi thẻ: *các bước · ✅ đạt khi (mỗi dòng trả lời có/không) · con số · mẹo*. ⭐ Mọi con
số mang **một trong ba nhãn**: **[Chuẩn]** (tiêu chuẩn, đặc tả, khuyến nghị tổ chức ngành) · **[Hãng]**
(đúng cho dòng sản phẩm đã nêu) · **[Nghề]** (quy tắc thực dụng, có lập luận, đo rồi chỉnh). Nhãn trả
lời câu hỏi mà người đọc gọi là *"tiêu chuẩn"*: con số này **có được phép đổi không**.

## 5. Quyết định 3 — con số mới lấy từ đâu

Đợt này đưa vào vài con số sách chưa có. ⚠ Không có nguồn chuẩn hoá cho chúng — nên mỗi con số được
**suy ra có lập luận**, gắn nhãn **[Nghề]**, và viết lập luận ngay cạnh:

| Con số | Lập luận |
|---|---|
| Giới hạn xy-lanh = **2 × `T_max`**, tối thiểu `T_max` + 0,5 s; đo ≥ 20 lần ở điều kiện chậm nhất còn hợp lệ | Đủ rộng cho dao động áp khí bình thường; mức +0,5 s giữ biên cho xy-lanh rất nhanh |
| Ngưỡng nhắc chậm dần ≈ **1,5 × mốc** | Nhắc ở **nửa đường** tới giới hạn — lời nhắc luôn tới trước lỗi |
| Giới hạn bước chờ cơ cấu = giới hạn cơ cấu **+ 1–2 s** | Lỗi cụ thể (xy-lanh nào) phải báo trước lỗi chung của bước — đúng điều Ch.26 mục 26.5b đã làm |
| Bước chờ quy trình = giới hạn trên của công thức **× 1,5** | Theo giới hạn, không theo mã hàng đang chạy — đổi mã hàng không sinh báo động giả |
| *Máy đứng chờ*: **5 × chu kỳ đích**, sau một tuần đặt lại = khoảng nghỉ dài nhất **+ 50 %** | Điểm xuất phát rồi thay bằng số đo của chính dây chuyền |
| Thời gian lọc: **≥ 2 lần chu kỳ quét** (nên 3), **≤ 1/5** thời gian có vật hoặc khe hở | Dưới hai lần đọc thì "ổn định" vô nghĩa; chừa biên cho tốc độ dao động. Định lượng đúng ba vế mà Ch.18 mục 18.4 đã nêu bằng lời |
| Tác vụ định kỳ chạy lớn nhất **≤ 50 %** chu kỳ | Vượt 100 % là tác vụ chồng lên chính nó (Ch.27 mục 27.6); một nửa còn lại là chỗ cho phần thêm về sau |

Con số **[Hãng]** mới, đã đối chiếu tài liệu: thời gian quét tối đa S7-1200 (1–6000 ms, mặc định
150 ms); watchdog tác vụ Logix (1 ms–2000 s, mặc định 500 ms); cấu trúc *buffer I/O* của Rockwell
1756-PM004 — nền cho mục 27.3c. Câu *"cảm biến điện tử không nảy tiếp điểm"* lấy từ Bryan, không phải
Petruzella như bản nháp đầu ghi nhầm — đã sửa trước khi ghép.

## 6. Kết quả giai đoạn 1

| Hạng mục | Kết quả |
|---|---|
| ⭐⭐ Phụ lục O | Mười sáu thẻ + bảng con số nhanh (O.17), mọi con số có nhãn |
| ⭐⭐ Ch.27 mục 27.3c | Tầng ánh xạ vào/ra: ba cách đọc ngõ vào (B18), năm việc của tầng đọc, ba điều cấm của tầng ghi, ví dụ hoàn chỉnh **chạy thử 9 phép**; Bẫy 8, 9; bảng chốt dòng 14–15; tự kiểm 13–14 |
| ⭐ Ch.1 mục 1.2b | Lộ trình D: lõi · giao diện (đúng mục) · bỏ qua được (trừ khi); ô ⚖ trả lời nhận xét 2; bảng chốt, tự kiểm, đường tra theo việc |
| Con số tại chỗ | Ch.6 Bẫy 7 · Ch.18 mục 18.4 · Ch.26 mục 26.4 (thêm *"con số lấy ở đâu"*) · Ch.51 · Ch.52 mục 52.4 (*"đạt khi"*) · Phụ lục J mục J.3 (cột hết giờ là giá trị thiết kế) |
| ⚠ Lệch dữ liệu tìm ra và sửa | **15 chỗ** còn ghi *"bảy hạng mục"* sao lưu sau khi Ch.54 đã đổi thành tám — kể cả bảng chốt của chính Ch.54; ⭐ thêm luật `hang_muc_sao_luu` vào bộ kiểm nhất quán (thử bằng lỗi cài: bắt được); C.9 thiếu hạng mục điểm dạy robot và thiếu mốc thời gian quét, thời gian hành trình; Ch.1 ghi *"16 mẫu"* — Phụ lục L có 17; Phụ lục N mục N.6 thiếu tiền tố `X_` |
| Kiểm | Bảy bộ kiểm 0 lỗi; chạy thử **107/107**; markdownlint 0 lỗi |

Chi tiết: nhật ký đối chiếu, đợt 66.

## 7. Còn lại — giai đoạn 2 và 3 (chưa làm)

| Giai đoạn | Việc | Vì sao chưa làm ngay |
|---|---|---|
| 2 | Một dòng *"🎯 Người lập trình cần gì ở chương này"* đầu mỗi chương thuộc nhóm *giao diện* | Bảng lộ trình D đã chứa thông tin đó; làm sau khi chủ dự án xem lộ trình D có đúng ý không |
| 2 | Rà các cụm mơ hồ còn lại theo danh sách của phép đo — *"hợp lý / phù hợp"* (73), *"kiểm tra kỹ / cẩn thận"* (56), *"định kỳ"* không kèm chu kỳ — từng chương, ưu tiên chương lõi | Việc dài; cần đi từng câu, không thay hàng loạt được |
| 2 | Thêm *"✅ đạt khi"* cho Ch.10, 11, 16, 19, 24, 29, 54, 55 — những chương phép đo cho thấy còn vắng | Như trên |
| 3 | ⚠ **Quyết định của chủ dự án:** có tách sách thành hai tập (mục 3, phương án B) không | Quyết định cấu trúc lớn — sách này không tự đổi |
| — | Bất biến mới **B20** trong `CLAUDE.md`: chỗ nào bảo người đọc *phải làm*, chỗ đó phải có — hoặc trỏ tới — **cách làm, tiêu chí đạt và con số có nhãn** | ✅ Đã thêm ở đợt này, để lỗi không quay lại |
