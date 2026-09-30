# 0011 — Đợt 65: PLC an toàn thật, và ô "ngoài hiện trường" cho các chương còn lại

**Trạng thái:** ✅ **XONG 2026-09-30**
**Ngày:** 2026-09-29 – 2026-09-30
**Thuộc:** đợt 65 — hai yêu cầu của chủ dự án: *"tiếp tục phản biện các chương còn lại theo hướng đó"*
(hướng của đợt 64: đúng trên giấy nhưng thực tế làm khác), và *"có thể tải thêm các tài liệu về PLC an
toàn như của SICK để hoàn thiện sách"*.

---

## 1. Bối cảnh — sách đang có gì

| Chỗ | Có | Thiếu |
|---|---|---|
| Ch.47 mục 47.4b | Công cụ PLC an toàn ràng buộc người lập trình thế nào | ⚠⚠ Chưa có gì về **ngày đầu tiên** trên một PLC an toàn thật: chương trình và nhịp riêng, thời gian phản hồi, dừng hẳn khi hỏng dữ liệu, thụ động hoá, chữ ký, cửa hẹp giữa hai phần |
| Ch.47 mục 47.7c (đợt 64) | Lập luận và nguồn định tính về động cơ vô hiệu hoá | ⚠ Không có **số liệu** — người đọc dễ nghĩ đây là chuyện hiếm |
| Các chương còn lại | Phần lớn đã có một câu hoặc một bẫy về cách làm tắt | ⚠ Không có **một dạng thống nhất** để nói *người ta làm gì, vì sao, ranh giới ở đâu* |
| Bộ tài liệu nguồn | SICK ×3, Schneider, DGUV/IFA, PPSA — đều là tài liệu **nguyên lý** | ⚠ Không có tài liệu **lập trình** PLC an toàn của hãng nào |

Tài liệu tải thêm (chủ dự án duyệt từng tệp): Siemens *Programming Guideline Safety for SIMATIC
S7-1200/1500* (mã 109750255, V1.2), Rockwell *GuardLogix 5580 Safety Reference Manual* (1756-RM012J),
SICK *Flexi Soft in Flexi Soft Designer* (IM0031659), Pilz *The Safety Compendium* (2017). ⭐ Sổ tay
*SIMATIC Safety — Configuring and Programming* (11/2023) — lúc đầu tưởng phải tải mà máy chủ trả 403 — hoá
ra **đã có sẵn** trong thư mục `PLC/` (ngoài `reference/`), chỉ là chưa chương nào dẫn. Bài học cũ của
đợt 2 lặp lại: *kết luận "không có nguồn" phải được kiểm kỹ như kết luận "có nguồn"* — tra bản đồ nguồn
trước khi xin tải.

## 2. Phản biện — phát hiện đã kiểm

| # | Chỗ | Phát hiện | Căn cứ |
|---|---|---|---|
| 1 | Phụ lục A2 mục A2.2, Phụ lục B | ⚠ *"Bộ định thời không dùng để chờ"* nói tuyệt đối — lệch Ch.26 mục 26.2b (thời gian **của quy trình** là ngoại lệ hợp lệ) | Chính Ch.26 mục 26.2b |
| 2 | Ch.47 | ⚠⚠ Thiếu hẳn phần lập trình trên PLC an toàn thật | Ba tài liệu hãng ở trên |
| 3 | Ch.47 mục 47.7c | ⚠ Thiếu số liệu | Pilz mục 4.4 (HVBG, gần 37 % máy gia công kim loại); trang IFA (cứ bốn máy một) |
| 4 | Ch.35 mục 35.6b | ⚠ *"Không được chép tham số PID"* — tuyệt đối, trong khi ai cũng chép; thứ nguy hiểm là chép **rồi coi như xong** | Phụ lục A2 mục A2.7 của chính sách |
| 5 | Ch.3, 23, 43, 52 | ⚠ Dạy đúng, nhưng không nói hiện trường làm tắt ở đâu và ranh giới nằm đâu | Ch.3: SICK *Six Steps* tr. 2-7 (LOTO); còn lại là phương pháp nghề |

## 3. Quyết định 1 — đặt phần "PLC an toàn thật" ở đâu

| Phương án | Ưu | Nhược |
|---|---|---|
| ⭐ **A. Mục mới 47.4c, ngay sau 47.4b** | Người đọc vừa học *công cụ ràng buộc gì* thì gặp ngay *ngày đầu tiên trên hệ thật*; nối thẳng tới 47.7 (thời gian dừng, khoảng cách rèm quang) | Ch.47 dài thêm; Ch.47 vốn đang chờ chuyên gia |
| B. Phụ lục riêng về PLC an toàn ba hãng | Đủ chỗ cho bảng đối chiếu dài | ⚠ Phụ lục ít người mở; tách chuyện lập trình an toàn khỏi chương an toàn |
| C. Rải vào Ch.10 (vòng quét), Ch.29 (ghi từ màn hình), Ch.54 (chữ ký) | Mỗi ý nằm cạnh chủ đề gốc | ⚠ Kéo nội dung an toàn ra ngoài vùng có cờ chờ chuyên gia — trái B3b |

⭐ **Chọn A.** Sáu điều, mỗi điều đối chiếu ba hệ (Siemens, Rockwell, SICK), kết bằng lời miễn trừ
⚠⚠ *"mục này mô tả những gì bạn GẶP — nó không dạy thiết kế chức năng an toàn"*. Mọi con số ghi rõ là của
tài liệu hãng cho dòng sản phẩm đã nêu.

## 4. Quyết định 2 — nói "người ta làm khác" bằng hình thức nào

| Phương án | Ưu | Nhược |
|---|---|---|
| A. Viết thêm vào bẫy thường gặp | Không thêm hình thức mới | ⚠ Bẫy là **lỗi**; cách làm tắt ở hiện trường nhiều khi **có lý** — gọi là bẫy thì người đọc bỏ qua lý do |
| ⭐ **B. Loại ô thứ năm: ⚖ NGOÀI HIỆN TRƯỜNG** — ba câu cố định: *người ta làm gì · vì sao · ranh giới* | Nhận ra ngay; buộc người viết nói **lý do thật** và **ranh giới** — không bênh cách làm tắt, không giả vờ nó không có | Thêm một loại ô; phải giữ kỷ luật để không thành ô ý kiến |
| C. Chương riêng *"sách nói gì, hiện trường làm gì"* | Gom một chỗ | ⚠ Tách lời phản biện khỏi đúng chỗ nó phản biện — người đọc mục 35.6b sẽ không thấy |

⭐ **Chọn B.** Chú giải ở Ch.1, danh sách ô trong `CLAUDE.md`; gắn nhãn lại hai ô phản biện của đợt 64
(Ch.15 mục 15.6, Ch.28 mục 28.5) cho thống nhất.

## 5. Quyết định 3 — chương nào có ô, chương nào không

Tiêu chí: thêm ô khi sách đang dạy một quy tắc mà hiện trường **thường xuyên** làm khác **vì một áp lực
thật**, và sách **chưa nói** chuyện đó. Chương đã có góc nhìn hiện trường thì **không** thêm — ô trùng làm
loãng cả hai chỗ.

| Có ô mới | Không thêm — vì đã có |
|---|---|
| Ch.3 mục 3.7 — LOTO cho việc "một phút" | Ch.13 mục 13.2b · Ch.27 mục 27.1 |
| Ch.23 mục 23.5b — lập trình khi đặc tả chưa đủ | Ch.44 mục 44.4 — *phân quyền quá chặt sẽ bị đi vòng* |
| Ch.35 mục 35.6b — chép tham số PID | Ch.45 mục 45.7 · Ch.54 mục 54.6 |
| Ch.43 mục 43.5b — nới ngưỡng, bỏ qua camera | Ch.51 mục 51.7b — cờ bỏ qua thiết kế sẵn |
| Ch.47 mục 47.4c — dời logic khỏi phần an toàn | Ch.53 Bẫy 5 — quy trình bị lách |
| Ch.52 mục 52.2 — rút gọn chạy thử ở SAT | Ch.7 — ⚠ chưa có nguồn nói hiện trường làm gì; không viết |

⚠ Ràng buộc giữ nguyên: **B3** — không một ô nào mô tả cách vượt qua một chức năng an toàn (tài liệu Pilz
có liệt kê các cách người ta vượt — sách **không** chép); **B3b** — Ch.3 và Ch.47 giữ cờ chờ chuyên gia.

## 6. Kết quả

| Hạng mục | Kết quả |
|---|---|
| Ch.47 | ⭐⭐ Mục 47.4c *sáu điều*; mục 47.7c thêm số liệu, danh sách thiếu sót thiết kế, chế độ vận hành đặc biệt |
| Ô ⚖ | Sáu ô mới (Ch.3, 23, 35, 43, 47, 52) + hai ô đổi nhãn (Ch.15, 28) |
| Nguồn | Bốn tài liệu vào `reference/00_INDEX.md` và bản đồ nguồn (bốn nhãn, đều quy về Ch.47); nguồn Ch.47 tách mỗi tài liệu một dòng; sổ tay Siemens có sẵn nay được dẫn — nhãn *chưa chương nào dẫn* từ 6 còn 5 |
| Kiểm | Bảy bộ kiểm 0 lỗi, chạy thử 98/98, markdownlint 0 lỗi |

Chi tiết: nhật ký đối chiếu, đợt 65 (#698–#717).

## 7. Hệ quả

- ⭐ Sách có một hình thức cố định để **tự phản biện** — mỗi ô ⚖ buộc nói ra ranh giới, nên nó không
  thành lời bênh cách làm tắt.
- ⭐ Hai quy tắc tuyệt đối được nói lại cho đúng phạm vi (A2.2 bộ định thời, Ch.35 chép PID). Bài học rút
  ra: một quy tắc tuyệt đối thường che một quy tắc hẹp hơn — gặp ngoại lệ hợp lý đầu tiên, người đọc sẽ bỏ
  luôn cả quy tắc.
- ⚠ Ch.47 dài thêm và thêm nội dung phải chờ **người có thẩm quyền về an toàn** duyệt — đã ghi vào TODO 6
  của `PROJECT_STATUS.md`.
- ⚠ Còn treo: công cụ bản đồ nguồn khớp theo từ nên quy thừa chương cho vài nhãn (nhật ký #712) — không che
  lỗ hổng nào, sửa sau.
