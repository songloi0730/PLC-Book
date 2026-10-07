# 0014 — Đợt 68: đọc MÃ THỰC THI của một khung chương trình máy thật

**Trạng thái:** ✅ **XONG 2026-10-07**
**Ngày:** 2026-10-06
**Thuộc:** đợt 68 — chủ dự án đưa thư mục một dự án máy thật (một trạm lắp ráp viết trên nền CODESYS,
kèm chương trình chuyền viết trên một hệ kiểu thiết bị) và hỏi *"có thể bổ sung gì vào sách như cách
tổ chức chương trình, cấu hình hệ thống, cấu hình phần cứng, cài đặt giao tiếp, mã mẫu… nếu cần thì mở
phần mềm ra để đọc mã cho tốt hơn"*.

---

## 1. Ràng buộc trước khi đọc

| Ràng buộc | Áp dụng thế nào |
|---|---|
| **B1b** — ẩn danh dự án thật | Sách không mang tên công ty, khách hàng, dự án, người viết, tên tệp, tên trạm theo ngôn ngữ gốc; mọi ví dụ đặt lại vào DP-01 hoặc một tình huống chung |
| Mã nguồn có chủ | Chỉ rút **quy tắc** và **bài học**; không chép khối, không chép bảng giao tiếp, không chép nhật ký sửa đổi |
| Không giải mã thủ công | Thân mã của dự án kiểu thiết bị lưu dạng mã hoá trong tệp — **không đọc bằng cách giải mã**. Dự án CODESYS mở bằng **chính phần mềm của hãng** (đúng gợi ý của chủ dự án), trên **bản sao**, đóng **không lưu**; không có mật khẩu nào được hỏi |
| B2 / B15 — không khẳng định suông | Mỗi câu về hành vi của hãng phải có nguồn: lần này là sổ tay lập trình chuyển động của chính hãng đó (mục 4) |
| B3 | Mọi thứ chạm tới cửa an toàn, dừng khẩn: chỉ nêu **ranh giới**, không nêu cách làm |

### Cách đọc được mã

Phần mềm mở dự án ở chế độ không giao diện thì báo lỗi bên trong một phần mở rộng của hãng
(`NullReferenceException` lúc nạp dự án). ⭐ Mở **có giao diện** kèm một kịch bản tự động (giao diện
lập trình kịch bản Python của nền CODESYS) thì được: kịch bản duyệt cây dự án, ghi phần khai báo và
phần thân của **332 đối tượng** ra tệp văn bản, đọc cấu hình tác vụ và cây thiết bị, rồi đóng dự án
**không lưu**. Mọi việc làm trên bản sao trong thư mục nháp của phiên.

## 2. Thấy gì — và sách đã có gì

⭐ **Điểm mấu chốt:** sách **đã từng** đọc **kiến trúc** của chính bộ khung này ở **đợt 37–38** (cây
thư mục A–F, kiểu `Cmd · Data · Resp`, cờ bỏ qua, tầng chống va chạm, cửa sổ nhắc thao tác) — khi đó
thân mã **không đọc được**. Lần này đọc được **thân mã**. Vì vậy đợt này **không** viết lại kiến trúc;
nó chỉ lấy thứ chỉ thân mã mới cho thấy.

| Thấy trong mã | Sách đang có | Thiếu |
|---|---|---|
| Ba vùng thanh ghi cho phần mềm PC (lệnh · trả lời · số thực), chia **theo kiểu dữ liệu**; vùng số thực có ô PLC ghi lẫn ô PC ghi | Ch.39 dạy PLC **hỏi** thiết bị | ⚠⚠ **PLC làm máy chủ cho phần mềm PC** — chưa có chữ nào |
| Bắt tay "khác 0 là lệnh, bên kia xoá về 0"; chú thích của người viết: *bắt sườn thì có lúc xoá không được*; sửa thành "chép rồi xoá liên tục" | — | ⚠ Cả hai cách đều **hai bên cùng ghi một ô** |
| Hai giàn đối diện chung vùng làm việc: kiểm khoảng hở trên vị trí **hiện tại** và vị trí **đích**; kiểm đích liên tục thì báo động mãi nên chỉ kiểm ở sườn | Ch.27 mục 27.3b — tầng chống va chạm bằng cảm biến rời | ⚠ **Hai trục chung một vùng** — điều kiện là khoảng cách, cần quãng dừng |
| Chạy khô bốn mức; mỗi mức **bật cờ bỏ qua ở sườn lên, tắt ở sườn xuống**; các mức dùng chung cờ | Ch.28 mục 28.3 — một cờ `M_DryRun` | ⚠ **Lỗi thật:** đổi mức 4 → 3 trong một lần ghi để lại cờ sai (mục 3) |
| Toàn bộ cờ bỏ qua nằm trong cấu trúc hệ thống **giữ qua mất điện**; danh sách bỏ qua có cả cửa an toàn và dừng khẩn | Ch.51 mục 51.7b — ba điều kiện, ranh giới an toàn | Xác nhận hai cảnh báo của sách bằng một ca thật |
| Lệnh chạy lấy theo **mức** (`Start AND Ready`) dù đã tính sẵn sườn của nó; Start đến từ nút **hoặc** màn hình | Ch.16 mục 16.6, Phụ lục L.1 — tự giữ theo mức | ⚠ **Câu của sách chưa đủ**: *"không tự lên lại"* chỉ đúng khi Start đã nhả |
| Jog bằng nút giữ trên màn hình | Ch.37 mục 37.4 — *"chỉ chạy khi giữ nút"* | ⚠ Nút giữ trên màn hình **kẹt khi mất kết nối** |
| Mã trạng thái máy cho bên ngoài suy từ một **chuỗi `IF` không có `ELSE`** | Ch.25 — máy trạng thái bằng kiểu liệt kê | Ca lai: cờ rời + một mã suy ra — và lỗ hổng của nó |
| Khối trục gọi trong tác vụ của mạng trường 2 ms ưu tiên 0; logic 4 ms; ⚠ tác vụ chính bị đổi ưu tiên | Ch.27 mục 27.6 — nguyên tắc tác vụ | Khối chuyển động **chỉ được** gọi ở tác vụ mạng trường (tài liệu hãng) |
| Biến điều kiện *"không giao thoa"*, *"rèm không bị che"* gán cứng `TRUE` — chỗ để sẵn cho phép kiểm; một vế giới hạn dương chép hai lần thay cho giới hạn âm; nhịp 100 Hz trong tác vụ 4 ms dùng để đo thời gian; cấu trúc lệnh trục bị hai tác vụ cùng ghi | Ch.22 — đọc chương trình người khác | ⚠ **Danh mục chỗ phải soi** khi nhận chương trình làm sẵn |
| Hai đảo van khác hãng cùng nằm trong cây cấu hình, một cái **bị tắt** | Phụ lục M mục M.2 | Biến thể phần cứng trong một dự án |
| Một chương trình con **chỉ có chú thích**: nhật ký sửa đổi theo ngày (cái gì + vì sao), mục *vấn đề còn mở*; số phiên bản giao diện là ngày sửa | Ch.30 mục 30.6, Bẫy 7 | Ô ⚖ — nhật ký nằm trong chương trình |
| Hai PLC của cùng một máy (chuyền ↔ trạm) bắt tay **hoàn toàn qua mạng**, có nhịp tim, mã trạng thái một byte | Ch.41 mục 41.5 — khuyên tín hiệu cứng cho việc chuyển sản phẩm | Ô ⚖ — khi hai PLC là một máy |

## 3. Bằng chứng cho lỗi chạy khô (mục 2, dòng 4)

Mức 3 bật *(bỏ qua chân không, bỏ qua bộ cấp, bỏ qua bước lấy, bỏ qua bước làm)*; mức 4 bật *(bỏ qua
chân không, bỏ qua bộ cấp, bỏ qua camera dưới, bỏ qua vị trí lấy, bỏ qua vị trí làm)*. Khối mức 3 đứng
**trước** khối mức 4 trong chương trình. Phần mềm PC ghi đè mức 4 bằng mức 3 trong **một** lần ghi:

1. sườn lên của *"mức = 3"* → bật năm cờ của mức 3;
2. **cùng vòng quét**, sườn xuống của *"mức = 4"* → tắt năm cờ của mức 4 — trong đó có **bỏ qua chân
   không** và **bỏ qua bộ cấp**, hai cờ mức 3 cần.

Kết quả: đang ở mức 3 nhưng hai cờ đó **tắt** — máy chờ bộ cấp có hàng, hết giờ thì báo động. Đi
ngược 3 → 4 thì không lỗi, vì thứ tự khối tình cờ đúng. ⭐ Kịch bản thử ở Ch.28 tái hiện đúng lỗi này
trên bản ✗ và chứng minh bản ✔ không mắc.

## 4. Nguồn mới

**Inovance — *Medium-Sized PLC Programming Guide (Motion Control)*, mã tài liệu 19012378, bản A00,
tháng 9/2024** (dòng AM400/AM500/AM600/AC700/AP700/AC800), có sẵn trong `PLC/en/`:

| Mục | Nội dung dùng |
|---|---|
| 3.1 | Phần chương trình chuyển động chạy trong **tác vụ EtherCAT**; logic chung ở tác vụ thường |
| 3.2 (ví dụ) | Tác vụ EtherCAT **2 ms, ưu tiên 0**; logic **20 ms, ưu tiên 16** |
| 4.1 | Chu kỳ EtherCAT thường **1–4 ms**; ⚠ **đừng tự đổi thứ tự ưu tiên** (bảng ưu tiên mặc định); biến toàn cục giữa các tác vụ được đồng bộ ở **điểm canh thời gian**; chu kỳ các tác vụ đặt **bội số nguyên** của nhau — đừng đặt EtherCAT 3, 6, 7, 9 ms |
| 4.5.4 | ⭐ Khối chuyển động của trục **chỉ được gọi** trong tác vụ EtherCAT |

## 5. Quyết định — đặt mỗi thứ ở đâu

| # | Nội dung | Phương án đã xét | Chọn | Lý do |
|---|---|---|---|---|
| 1 | PLC làm máy chủ cho phần mềm PC | Ch.39 · Ch.43 · Ch.45 · phụ lục mới | ⭐ **Ch.39 mục 39.9b** + khối ở Phụ lục L + thẻ O.11 | Cơ chế là thanh ghi Modbus TCP — Ch.39 là chủ nhà của *Modbus*; Ch.43/45 dùng nó, trỏ về |
| 2 | Cách bắt tay một yêu cầu | A *khác 0 + xoá* · B *chép + xoá liên tục* · C *số thứ tự* | ⭐ **C**, A và B đặt cạnh nhau theo B18 | C là cách duy nhất giữ **mỗi ô một người ghi**; trả lời đến muộn tự bị loại; khởi động lại không cần xoá gì |
| 3 | Hai trục chung một vùng | Ch.27 mục 27.3b · Ch.37 | ⭐ **Ch.37 mục 37.7b** | Ch.27 thuộc lát cắt 2 — không được nói *servo*, *gantry* (B8); 27.3b giữ phần nguyên tắc tầng, 37.7b phần khoảng cách |
| 4 | Chạy khô nhiều mức | Mục mới · mở rộng 28.3 + Bẫy | ⭐ **28.3** (mục con) + **Bẫy 7** + ví dụ hoàn chỉnh | Lỗi là lỗi **của chế độ**; bẫy cần một mục có tên (B5) |
| 5 | Start theo mức | Sửa Ch.16.6 · Phụ lục L.1 · Ch.44 | ⭐ **Cả ba**: một câu ⚠ ở 16.6 và L.1, chi tiết ở **Ch.44 Bẫy 14** | Câu sai nằm ở 16.6/L.1 (B16 — sửa tại chỗ); cơ chế *màn hình mất kết nối* thuộc lát cắt 4 |
| 6 | Năm chỗ phải soi | Ch.22 · Phụ lục E · Phụ lục O | ⭐ **Ch.22 mục 22.6b** | Đúng việc của chương: nhận chương trình người khác; mỗi chỗ có *cách tìm · vì sao · sửa · đạt khi* (B20) |
| 7 | Tác vụ của khối trục | Ch.27.6 · Ch.37.8 | ⭐ **Ô ⚖ ở 37.8** | Có nguồn hãng; Ch.37 được nói *servo*, *EtherCAT* |
| 8 | Mã trạng thái máy | Ch.25 · Ch.41 · Ch.45 | ⭐ **Ô ⚖ ở Ch.25** | Câu hỏi là *thiết kế trạng thái*, không phải giao thức |
| 9 | Cờ bỏ qua giữ qua mất điện | Ô ⚖ · Bẫy | ⭐ **Ô ⚖ ở 51.7b** | Có lý do thật (một cấu trúc, một vùng địa chỉ cho màn hình) → cần ranh giới, không chỉ cấm |
| 10 | Biến thể phần cứng | Phụ lục M · Ch.40 | ⭐ **M.2** | Việc cấu hình dự án |
| 11 | Nhật ký trong chương trình | Ch.30.6 · Ch.54.7 | ⭐ **Ô ⚖ ở 30.6** | 30.6 là chỗ dạy quản lý phiên bản phía người viết mã |
| 12 | Hai PLC một máy qua mạng | Ô ⚖ ở 41.5 | ⭐ **41.5** | Đúng chỗ sách khuyên tín hiệu cứng — phải nói khi nào người ta làm khác và ranh giới |

## 6. Không lấy

- Tên công ty, khách hàng, dự án, người viết, mã thiết bị, tên trạm, bảng giao tiếp, nhật ký sửa đổi.
- ⚠ **Chế độ "chỉnh máy" tắt tạm một ràng buộc chống va chạm trong 30 s** — B3: sách không đưa cách
  bỏ qua liên động để thử, kể cả có giới hạn thời gian.
- ⚠ Cách nhả phanh tay khi trục không có điện, cách che cửa an toàn và dừng khẩn từ màn hình — chỉ nói
  ranh giới (Ch.51 mục 51.7b), không nói cách làm.
- Tích hợp tô vít điện, chụp bay bằng ngõ ra so sánh của bộ đếm, hiệu chuẩn camera trên/dưới — đáng
  viết nhưng đặc thù một loại máy; **để ngỏ** cho đợt sau (chụp bay hợp với Ch.43 mục 43.4).
- Xoá vùng nhớ bằng con trỏ: trong mã đã đọc, nó chỉ dùng **bên trong một mảng** — không có ca lỗi
  thật để dẫn. Địa chỉ tuyệt đối khai tay: đã tính lại cả dải — **không** chồng nhau.

## 7. Hệ quả

- Ch.16, Ch.22, Ch.25, Ch.28, Ch.30, Ch.37, Ch.39, Ch.41, Ch.44, Ch.51; Phụ lục L, M, O.
- Ba ví dụ hoàn chỉnh mới, mỗi cái có kịch bản trong `tools/chay_thu/kich_ban.py`.
- Chi tiết: nhật ký đối chiếu, đợt 68.
