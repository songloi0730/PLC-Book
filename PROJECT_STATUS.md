# PROJECT_STATUS — PLC Programming Book

**Cập nhật:** 2026-08-31 (session 8)
**Giai đoạn:** 🟨 **đang viết — đợt 1–3 xong, đợt 4 đang làm (18/58 chương, 10 hình).**

---

## Đã làm

### Session 1 (2026-08-28) — thu thập & dựng khung

| Việc | Kết quả |
|---|---|
| Thu thập nguồn gốc yêu cầu | Toàn văn bài sticky r/PLC "READ FIRST…" + **96 bình luận** + luồng riêng về giao thức truyền thông + wiki của sub — lấy qua bản lưu Wayback (reddit chặn truy cập tự động). Lưu ở `../PLC/reference/05_Web_Snapshots/` |
| Tải tài liệu mở | 18 file (~180 MB) vào `../PLC/reference/` — chỉ nguồn hợp pháp. Chỉ mục: `../PLC/reference/00_INDEX.md` |
| Dựng khung sách | 43 chương / 8 phần + 9 phụ lục |
| ADR 0001 | 3 phương án cấu trúc, chọn A+C, ghi rõ lý do loại B; nêu 5 điểm còn treo |
| Quy ước viết | `CLAUDE.md` — bất biến B1–B10, 3 khung chương cố định |

### Session 2 (2026-08-29) — chốt hướng & mở rộng

| Việc | Kết quả |
|---|---|
| ✅ Chốt 5 quyết định | `docs/design-notes/0002-*.md` — thay thế phần "Điểm còn treo" của ADR 0001 |
| Đổi máy mẫu | PS-01 (cơ khí) → **DP-01 · Trạm tra keo & sấy UV trên chuyền board mạch** (điện tử). 4 phương án máy điện tử đã cân nhắc, ghi trong ADR 0002 §2 |
| Viết lại hồ sơ máy mẫu | `docs/case_study_may_mau.md` — I/O list đầy đủ (5 nhóm), đặc tả trình tự 2 trạm, mô hình trạng thái, bảng công thức sản phẩm, 7 chức năng an toàn, quy tắc **bóc lớp 5 lát cắt** |
| Mở rộng khung | **43 → 58 chương**, **9 → 11 phụ lục**. 15 chương mới, mỗi chương có lý do "vì sao bắt buộc phải có" trong ADR 0002 §4 |
| Phụ lục A: 3 → 5 hệ | Siemens · Mitsubishi · Inovance · CODESYS (cột neo) · Rockwell; tách thành A1 (khái niệm) và A2 (lệnh + 1 đoạn logic viết 5 lần) |
| Bất biến mới | **B11** song ngữ thuật ngữ · **B12** chống phình mà loãng; **B6** siết lại (ranh giới tự đủ dịch ra xa hơn); **B8** thêm quy tắc bóc lớp |

### Session 3 (2026-08-30) — bổ sung nguồn & đối chiếu khung

| Việc | Kết quả |
|---|---|
| Tải nốt nguồn **miễn phí** còn lại | +13 file. Đáng chú ý: **IFA Report 2/2017e** (324 tr — tài liệu tự do quan trọng nhất về áp dụng ISO 13849), **Siemens Programming Guideline + Style Guide** (nguồn chính cho Ch.30), **đặc tả Modbus / IO-Link / PLCopen Motion** (nguồn *cấp một* cho Ch.39, 12, 37), PPSA, Schneider, SICK FAQ, EtherCAT-TSN, PLC Handbook |
| Cứu 3 nguồn web đã chết | `plcdev` (92 KB, có phần PIDE & tag/UDT), `kronotech`, `plchowto` — lấy qua Wayback |
| Sửa lỗi phát hiện khi kiểm | File IFA tải thiếu (9,5/18,8 MB → 0 trang) đã **tải lại đủ 324 trang**; xoá 1 file hoá ra chỉ là tờ rơi khoá học 2 trang; **sửa lại toàn bộ số trang sai trong chỉ mục**; đánh số lại tham chiếu chương trong chỉ mục từ khung 43 → 58 |
| Đối chiếu khung với 3 nguồn độc lập | `docs/design-notes/0003-*.md` — 4 sách thương mại chủ dự án mua + 1 trang chuyên đề 43 bài + đặc tả chuẩn mở |
| Bổ sung khung theo kết quả đối chiếu | **8 bổ sung** vào Ch.40, Ch.45, Ch.51, Phụ lục I — không phải sửa cấu trúc, khung 58 chương giữ nguyên |

> ⭐ **Kết quả đối chiếu quan trọng nhất:** luận điểm trung tâm của sách — *phương pháp thiết kế
> xứng đáng một phần riêng* — được **hai nguồn độc lập xác nhận**: giáo trình Hanssen đặt "Methodic"
> thành một phần ngang hàng với Hardware và Programming; giáo trình Hugh Jack dành 4 chương liền cho
> chuỗi Boolean → logic có cấu trúc → lưu đồ → trạng thái.

### Session 4 (2026-08-30) — viết đợt 1

| Chương | Từ | Nội dung trọng tâm |
|---|---:|---|
| **Ch.1** — Sách này dành cho ai & cách dùng | ~4 500 | 3 lộ trình đọc kèm **cái bẫy riêng của từng lộ trình**; 3 đường tra cứu (có bảng "đang phải làm gì → đọc chương nào"); DP-01 + quy tắc bóc lớp; vì sao trung lập hãng; quy ước cảnh báo & song ngữ; bảng "thành công = gì" cho cả 8 phần |
| **Ch.10** — Vòng quét | ~4 050 | Mở bằng **bài toán đảo 2 dòng làm chết mạch tạo xung**; 4 giai đoạn; ảnh I/O vs truy cập trực tiếp; thời gian quét & watchdog; **5 bẫy** gồm xung ngắn hơn vòng quét, tưởng lệnh là kết quả, tranh chấp giữa POU |
| **Ch.15** — Ladder Diagram | ~3 880 | Mở bằng **máy vẫn chạy khi đứt dây nút Dừng**; "đây không phải là điện"; ⭐ **bảng 4 tổ hợp NO/NC** (vật lý × lệnh) — chỉ 1/4 tổ hợp vừa đúng vừa an toàn; **5 bẫy** gồm cuộn dây trùng, nhánh tự giữ vòng qua nút Dừng |
| **Ch.4** — Cảm biến số & đấu nối | ~3 880 | Mở bằng **đèn cảm biến sáng mà bit không lên**; trạng thái NORMAL & vì sao đứt dây = tiếp điểm hở; 2/3/4 dây + dòng rò; ⭐ **bảng 4 tổ hợp PNP/NPN × chân chung**; 5 loại cảm biến; **5 bẫy** |

**Tổng đợt 1: ~16 300 từ.** Đã tự kiểm tuân thủ bất biến:

| Bất biến | Kết quả |
|---|---|
| **B1** trung lập hãng | ✅ Không có tên phần mềm hãng nào lọt vào thân 4 chương |
| **B8** bóc lớp lát cắt | ✅ Ch.10 và Ch.15 không nhắc servo / analog / mạng |
| **B11** song ngữ | ✅ Có ở cả 4 chương |
| **B12** đủ mục bắt buộc | ✅ Cả 4 chương đều có *Bẫy thường gặp* và *Tự kiểm* |
| **B2** ghi nguồn cuối chương | ✅ Cả 4 chương |

> ⭐ **Quyết định giọng văn đã chốt qua đợt 1** (áp dụng cho 54 chương còn lại): mỗi chương **mở bằng
> một sự cố thật**, không mở bằng định nghĩa. Ba trong bốn chương mở bằng đúng một câu chuyện hỏng hóc
> — và câu chuyện đó được giải thích trọn vẹn ở mục "Bẫy". Đây là thứ giữ cho sách không rơi thành
> danh mục lệnh.

### Session 5 (2026-08-30) — phản hồi giọng văn & dựng bộ hình

Chủ dự án đọc đợt 1 và cho 4 phản hồi + 1 yêu cầu mới. Đã áp hết vào quy ước:

| Phản hồi | Đã làm |
|---|---|
| **Không giới hạn số từ**, ưu tiên chất lượng | **B12 viết lại** — bỏ trần số từ; ràng buộc còn lại là *không loãng*, không phải *ngắn* |
| **Mở bằng sự cố thật là tuỳ chọn**, đừng ép mọi chương | Khung chương sửa: mục N.1 nay có **3 cách mở** (sự cố / câu hỏi / bối cảnh). Ghi rõ *mở bằng sự cố gượng ép còn tệ hơn mở thẳng* |
| **Song ngữ phải đủ**, không thiếu gây khó hiểu | **B11 siết lại** — tiêu chí là **ĐỦ, không phải tiết chế**; thà thừa một cặp ngoặc còn hơn để người đọc đoán |
| **Nội dung quan trọng cần bảng tổng hợp** | **B14 mới** — mỗi khái niệm trọng tâm phải có một bảng chốt lại; bảng đặt *sau* giải thích, không thay giải thích |
| ⭐ **Bổ sung hình ảnh** | **B13 mới** + mục *Quy ước hình* + `tools/sinh_hinh.py`. Đã dựng **5 hình** cho đợt 1 |

**Năm hình đã dựng và nhúng:**

| Hình | Chương | Vì sao hình nói được điều chữ không nói được |
|---|---|---|
| 1.1 — Tổng quan DP-01 | Ch.1 | Quan hệ không gian giữa hai trạm và chuyền |
| 4.2 — Bốn tổ hợp PNP/NPN × chân chung | Ch.4 | ⭐ **Đường đi của dòng điện** — thứ gần như không thể mô tả bằng chữ cho người mới |
| 10.1 — Bốn giai đoạn vòng quét | Ch.10 | Cấu trúc vòng lặp |
| 10.2 — Xung ngắn hơn vòng quét bị bỏ lỡ | Ch.10 | ⭐ **Quan hệ thời gian** — hình cho thấy ngay vì sao xung "không tồn tại" với PLC |
| 15.2 — Mạch tự giữ đúng/sai | Ch.15 | Khác nhau đúng một điểm nối; đặt cạnh nhau mới thấy |

> ⭐ **Quyết định về hình đã chốt:** **tự vẽ SVG bằng script, không tải hình từ đâu.** Lý do: hình
> trong tài liệu hãng và sách thương mại đều có bản quyền — chép vào là vi phạm đúng ranh giới đã đặt
> ở B7 và ADR 0003 §3. Tự vẽ còn cho phép nhãn tiếng Việt và một ngôn ngữ thị giác thống nhất cả 58
> chương. Sinh bằng script để **sửa token là sửa toàn bộ hình**.

> ⚠ **Bài học kỹ thuật khi dựng hình** (ghi vào quy ước để khỏi lặp): ký tự `&` chưa escape làm hỏng
> XML; và **bắt buộc render ra PNG để nhìn bằng mắt** — ba lỗi bố cục (nhãn đè đường ray, nhãn bị cắt
> ở mép, hai nhãn xung ghi giống nhau) chỉ lộ ra khi nhìn, không lộ khi kiểm XML.

### Session 6 (2026-08-31) — viết đợt 2: Phần IV, điểm khác biệt số 1

| Chương | Từ | Trọng tâm |
|---|---:|---|
| **Ch.25** — Thiết kế theo máy trạng thái | ~4 390 | Mở bằng **máy ở hai trạng thái cùng lúc**; vì sao n cờ độc lập sinh 2ⁿ tổ hợp mà chỉ n có nghĩa; mô hình 7 trạng thái + bảng chuyển trạng thái 4 cột; hiện thực bằng `CASE` và bằng bit trạng thái; **trạng thái máy vs bước trình tự** |
| **Ch.28** — Chế độ vận hành & phục hồi | ~3 990 | Mở bằng **hai board đâm nhau sau khi nhấn Reset**; 5 chế độ và quyền hạn; ⭐ **bảng va chạm → suy ra thứ tự về gốc**; huỷ chu trình vs chạy tiếp; **sản phẩm dở dang phải coi là NG** |
| **Ch.27** — Kiến trúc nhiều trạm | ~3 915 | ⭐ Chương mới quan trọng nhất. **Ba tầng + ba quy tắc gọi Q1/Q2/Q3**; khối cơ cấu tái dùng cho 4 xy-lanh; **giao diện công bố** thay cho đọc ruột nhau; pipeline & nút cổ chai; khi nào KHÔNG tách tác vụ |
| **Ch.26** — Lưu đồ & bit trình tự | ~3 369 | Mở bằng **máy đứng im 40 phút không báo gì**; lưu đồ → bit bước; ⭐ **timeout là cơ chế báo lỗi, không phải cơ chế chuyển bước**; nhánh song song; **bế tắc** và đồ thị chờ |
| **Ch.23** — Từ yêu cầu tới đặc tả | ~3 518 | **Hai loại sai** — code sai rẻ, đặc tả sai đắt hơn 1–2 bậc; bảng I/O 6 cột với **cột phân loại an toàn/quy trình**; mẫu mô tả bước 4 dòng; ⭐ **4 nhóm câu phải hỏi khách hàng**; tiêu chí nghiệm thu viết TRƯỚC |

**Tổng đợt 2: ~19 200 từ + 3 hình.** Toàn sách hiện **~35 500 từ, 9 chương, 8 hình**.

**Ba hình mới:**

| Hình | Vì sao cần hình |
|---|---|
| 25.1 — Máy trạng thái 7 trạng thái | Cấu trúc chuyển tiếp; đường "từ MỌI trạng thái vào Alarm" chỉ thấy được bằng hình |
| 27.1 — Ba tầng kiến trúc | ⭐ Hướng gọi và **hai điều cấm** (đọc ruột nhau, ghi thẳng ngõ ra) — quan hệ cấu trúc |
| 28.1 — Thứ tự về gốc sai/đúng | ⭐ Hai thứ tự đặt cạnh nhau mới thấy vì sao một cái gây va chạm |

> ⭐ **Sợi chỉ xuyên suốt Phần IV đã hình thành:** cả năm chương đều quy về một nguyên tắc —
> **thay giả định bằng bằng chứng**. Ch.23 thay "chắc khách hàng muốn thế" bằng câu hỏi có văn bản.
> Ch.25 thay "suy trạng thái từ mấy cờ" bằng một biến. Ch.26 thay "chờ 2 giây chắc xong" bằng phản hồi
> thật + timeout báo lỗi. Ch.27 thay "nhìn ruột trạm kia" bằng giao diện công bố. Ch.28 thay "chắc tư
> thế vẫn như cũ" bằng trình tự về gốc đúng với mọi tư thế xuất phát.

> ⚡ **Ghi chú kỹ thuật vẽ hình** (đã bổ sung vào *Quy ước hình*): `marker-end` của SVG **không render
> ổn định** ở mọi trình đọc — mọi mũi tên từ nay vẽ bằng **đa giác tường minh** (hàm `arw()`), không
> dùng marker.

### Session 7 (2026-08-31) — viết đợt 3: Phần VII, điểm khác biệt số 2

| Chương | Từ | Trọng tâm |
|---|---:|---|
| **Ch.51** — Xử lý sự cố | ~6 770 | Chương dài nhất sách. Mở bằng **hai người thợ, cùng một cỗ máy** (3 giờ vs 12 phút); ⭐ **truy ngược từ ngõ ra bị lỗi**; 3 câu hỏi mở đầu; bảng tra 2 phút + 6 nhóm lỗi; bộ 9 công cụ; **4 phép đo Đ1–Đ4**; cưỡng bức I/O; ⭐ **4 nguyên nhân vật lý của lỗi chập chờn**; bảng ~40 triệu chứng; **8 bẫy của chính người chẩn đoán** |
| **Ch.47** — An toàn máy | ~5 370 | ⚠⚠ Mở bằng *vì sao logic PLC thường không đủ* — CPU treo thì logic chết, mối nguy thì không; đánh giá rủi ro đi trước; 3 bậc ưu tiên giảm thiểu; **2 câu hỏi phân biệt hạng mục kiến trúc**; 3 loại lệnh dừng; muting; STO và **2 điều STO không làm**; ⭐ mối nguy UV — loại **không có triệu chứng tức thời**; LOTO trong thiết kế |
| **Ch.48** — Fail-safe | ~4 140 | Mở bằng **ionizer hỏng 3 tuần, board hỏng ở tay khách hàng**; trạng thái an toàn cho **3 tình huống mất năng lượng**; vì sao "mất điện thì nhả" KHÔNG phải quy tắc chung; nhịp tim giữa các hệ; ⭐ **lỗi máy không tự phát hiện được** — câu hỏi phải hỏi cho mọi thiết bị phụ trợ |
| **Ch.52** — Chạy thử & bàn giao | ~3 630 | Mở bằng **module cháy sau 3 tiếng vì bỏ qua kiểm I/O**; **8 bước bắt buộc**; ⭐ kiểm I/O 1-1 trước khi chạy logic; ⭐ **10 ca thử tạo lỗi cố ý**; đo chu kỳ trong 1 giờ; **danh mục 10 mục bắt buộc trước bàn giao** |
| **Ch.50** — Mô phỏng & kiểm thử | ~3 160 | 3 mức mô phỏng; lớp chọn nguồn tín hiệu `X_…`; ⚠⚠ **4 biện pháp chống quên cờ mô phỏng**; **danh sách ca kiểm nhóm A–F**; ⭐ **giới hạn của mô phỏng** — 8 thứ chỉ lộ trên máy thật |

**Tổng đợt 3: ~23 070 từ + 1 hình.** Toàn sách hiện **~57 600 từ, 14 chương, 9 hình**.

> ⭐ **Sợi chỉ Phần VII:** nếu Phần IV là *thay giả định bằng bằng chứng*, thì Phần VII là
> **giả định rằng mọi thứ sẽ hỏng, rồi thiết kế cho tình huống đó**. Ch.47 giả định CPU sẽ treo →
> lớp an toàn độc lập. Ch.48 giả định dây sẽ đứt và thiết bị phụ trợ sẽ hỏng âm thầm → chọn trạng thái
> an toàn và bắt máy phải biết. Ch.50 giả định code có lỗi → tìm ở bàn trước. Ch.52 giả định lắp đặt
> có sai → kiểm I/O 1-1 và thử tạo lỗi cố ý. Ch.51 là cái lưới cuối cùng khi bốn lớp trên đều lọt.

> ⚠⚠ **Ch.47 và Ch.48 mang cờ `✅ ⚠⚠` và `✅ ⚠` trong mục lục — ĐÃ VIẾT nhưng CHƯA ĐƯỢC PHÁT HÀNH.**
> Cả hai phải qua rà soát của chuyên gia an toàn trước khi đưa vào bản in. Đây là ràng buộc B3b, không
> phải thủ tục. Việc tìm người rà soát là **hạng mục còn treo duy nhất có rủi ro pháp lý**.

### Session 8 (2026-08-31) — đợt 4, đợt đầu

Đợt 4 có **19 chương** — làm theo mức giá trị, không theo số thứ tự. Đợt này viết 4 chương:

| Chương | Từ | Trọng tâm |
|---|---:|---|
| **Ch.7** — ESD & môi trường điện tử | ~4 130 | ⭐ Chương đặc thù ngành, không sách PLC nào có. Mở bằng **cỗ máy hỏng sản phẩm 3 tháng không để lại dấu vết**; hỏng ngay vs **hỏng tiềm ẩn**; ⭐ **ba mô hình phóng điện** và vì sao *máy tự động gặp mô hình khác lắp ráp thủ công* → dây đeo cổ tay không cứu được máy; **ba loại đất PE/0V/ESD** và vì sao dây đeo có điện trở (2 lý do, một là an toàn tính mạng); ionizer phải là **điều kiện cho phép chạy** |
| **Ch.6** — Khí nén | ~4 320 | Mở bằng *vì sao người viết PLC cần hiểu khí nén*; FRL và vì sao nước là kẻ thù số một; ⭐⭐ **ba kiểu vị trí giữa van 5/3 — "kín giữa" và "hở giữa" hành xử NGƯỢC NHAU khi mất điện**; công thức lực kèm điều kiện áp dụng; ⭐ **tiết lưu đường xả, không phải đường cấp** + 3 triệu chứng lắp ngược; chân không & giác hút; van cô lập phải **khoá được · có cửa xả · với tới được** |
| **Ch.30** — Chuẩn hoá & tái sử dụng | ~3 655 | Mở bằng **ai là người đọc thật sự** — người mở chương trình lúc 2 giờ sáng; nhất quán > đẹp; tổ chức **theo cơ cấu không theo bước**; UDT; ⭐ **comment như nhật ký kỹ thuật** — ghi cả cái đã thử mà không được; ⚠ **dùng lại khối cho máy có mối nguy khác**; cái gì so sánh được / không |
| **Ch.17** — Timer | ~3 196 | Mở bằng **máy chạy tốt 8 tháng rồi phá một lô** vì dùng timer thay phản hồi; 3 khối chuẩn + sơ đồ thời gian; sai số ≥ 1 chu kỳ quét; ⭐ **timer báo lỗi, không chuyển bước**; **hai nguyên nhân "timer không bao giờ hết giờ" và cách phân biệt bằng một phép quan sát** |

**Đợt này: ~15 300 từ + 1 hình.** Toàn sách **~72 200 từ, 18 chương, 10 hình**.

**Còn lại của đợt 4 (15 chương):** Ch.2–3, 5, 8–9, 11–13, 16, 18–22, 24, 29.

> ⭐ **Quan sát khi viết Ch.7:** đây là chương **không sách PLC nào có**, và nó là chỗ hướng "trọng tâm
> sản xuất điện tử" trả lại giá trị rõ nhất. Điểm phát hiện được khi viết: các biện pháp ESD quen thuộc
> (dây đeo cổ tay, thảm, áo choàng) đều nhắm vào **mô hình người** — trong khi **máy tự động chủ yếu
> gặp mô hình thiết bị tích điện**, nơi chính sản phẩm tích điện rồi phóng qua một chân. Nghĩa là bộ
> biện pháp quen thuộc **không chạm tới vấn đề chính của máy tự động**. Cái chạm tới là vật liệu tiêu
> tán trong máy và ion hoá đúng chỗ.

---

## Quyết định đã chốt (không mở lại nếu không có lý do mới)

| # | Quyết định | Chi tiết |
|---|---|---|
| 1 | **Hướng A+C** — trung lập hãng + máy mẫu xuyên suốt | ADR 0001 |
| 2 | **Máy mẫu DP-01**, lĩnh vực điện tử | ADR 0002 §2 |
| 3 | **5 hệ**, ưu tiên Siemens → Mitsubishi → Inovance → CODESYS → Rockwell | ADR 0002 §3 |
| 4 | **Toàn diện, không giới hạn độ dài** — 58 chương | ADR 0002 §1, §4 |
| 5 | **Song ngữ thuật ngữ** (B11) | ADR 0002 §5 |

---

## Thứ tự viết — 6 đợt

Không viết tuần tự 1→58. Lý do: các chương **khác biệt** của sách đáng viết sớm — nếu để cuối mà hụt
hơi thì sách rơi lại thành một tutorial nữa. Sau đợt 1–3 đã có sản phẩm dùng được kể cả nếu dừng.

| Đợt | Chương | Vì sao đợt này | Điều kiện tiên quyết |
|---|---|---|---|
| **1** | Ch.1 · Ch.10 · Ch.15 · Ch.4 | Xương sống: cách dùng sách + vòng quét + ladder + NPN/PNP. Viết xong 4 chương này là đủ để đánh giá **giọng văn và mật độ có đúng không** trước khi cam kết 54 chương còn lại | DP-01 lát cắt 1 đã chốt ✅ |
| **2** | Ch.25 · Ch.28 · Ch.27 · Ch.26 · Ch.23 | Phần IV — điểm khác biệt số 1. Ch.27 (kiến trúc nhiều trạm) là chương mới quan trọng nhất | Đặc tả trình tự DP-01 ✅ |
| **3** | Ch.51 · Ch.47 · Ch.48 · Ch.50 · Ch.52 | Phần VII — điểm khác biệt số 2. Ch.47–48 cần chuyên gia an toàn duyệt → **khởi động sớm để có thời gian chờ** | Chức năng an toàn DP-01 ✅ |
| **4** | Ch.2–3 · Ch.5–9 · Ch.11–13 · Ch.16–22 · Ch.24 · Ch.29–30 | Phần nền — viết nhanh hơn vì đã có khung và giọng văn. Gồm 2 chương mới đặc thù điện tử: Ch.6 (khí nén), Ch.7 (ESD) | Đợt 1 đã chốt giọng văn |
| **5** | Ch.31–37 · Ch.38–46 | Analog & truyền thông. Ch.41–42 (SMEMA, truy xuất) là đặc thù điện tử, viết kỹ | DP-01 lát cắt 3–4 |
| **6** | Ch.49 · Ch.53–56 · Ch.57 · Ch.58 · toàn bộ phụ lục | Ráp lại. **Phụ lục A1/A2 viết sau cùng** — nếu viết sớm sẽ phải sửa 5 lần mỗi khi thân sách đổi | Toàn bộ thân sách ổn định |

---

## Việc kế tiếp ngay

1. ~~Phản hồi giọng văn đợt 1~~ ✅ xong session 5, đã áp vào B11–B14.
2. ~~Viết đợt 2~~ ✅ xong session 6.
3. ~~Viết đợt 3~~ ✅ xong session 7.
4. ~~Dựng quy trình đánh giá + rà lại 18 chương đã viết~~ ✅ xong session 9 — xem mục
   *Quy trình đánh giá* trong `CLAUDE.md`. Bản thảo hiện **0 LỖI · 0 CẢNH BÁO** ở cả hai bộ kiểm.
5. ⚠⚠ **Tìm chuyên gia an toàn rà soát Ch.47 và Ch.48** — hạng mục treo duy nhất có rủi ro pháp lý.
   Hai chương đã viết xong nhưng **không được phát hành** trước khi có rà soát.
6. **Viết nốt đợt 4** — còn 15 chương: Ch.2–3, 5, 8–9, 11–13, 16, 18–22, 24, 29.
7. **Đợt 5** — analog & truyền thông (Ch.31–46).
8. **Đợt 6** — ráp lại (Ch.49, 53–58) + 11 phụ lục. Phụ lục A1/A2 viết sau cùng.
3. **Chốt 5 câu hỏi còn lại của máy mẫu** (`docs/case_study_may_mau.md` §7) — chưa chặn, nhưng
   Ch.55 và Ch.57 sẽ cần.
3. ~~Bổ sung tài liệu nguồn Siemens & Mitsubishi~~ ✅ xong session 2–3. Thư viện nguồn coi như **đủ để viết**:
   40 file PDF / ~12.500 trang, phủ cả 5 hệ của Phụ lục A + đặc tả chuẩn mở + an toàn + điện nền tảng.
4. Khi viết Phần I–II: quét mục lục sách Rabiee (file không có bookmark) để đối chiếu — không chặn đợt 1.

---

## Rủi ro đã nhận diện

| Rủi ro | Mức | Giảm thiểu |
|---|---|---|
| **Trượt khỏi trung lập hãng** — viết đến chỗ cụ thể rất dễ sa vào "bấm nút ở phần mềm X" | Cao | B1; mỗi lần review chương soát riêng điểm này |
| **58 chương → nguy cơ bỏ dở** | Cao | Thứ tự 6 đợt ở trên; sau đợt 3 đã có sản phẩm độc lập dùng được |
| **Sách phình mà loãng** — hệ quả trực tiếp của quyết định #4 | Cao | **B12**; khung chương cố định; chương thiếu mục "bẫy" và "tự kiểm" coi như chưa xong |
| **Chương an toàn viết bởi người không có thẩm quyền kiểm định** — rủi ro pháp lý thật | Cao | B3/B3b; giữ cờ ⚠⚠; **không phát hành Ch.47–48 nếu chưa có chuyên gia duyệt**; khởi động đợt 3 sớm để có thời gian chờ |
| **Phụ lục A 5 cột phình to và lệch pha thân sách** | Trung bình | Chỉ viết ở đợt 6; tách A1/A2 |
| **Phụ lục A trượt thành so sánh hãng nào hơn** | Trung bình | Nguyên tắc "mô tả khác biệt, không xếp hạng" ghi trong CLAUDE.md |
| **DP-01 quá tải cho chương đầu** | Đã xử lý | Quy tắc **bóc lớp 5 lát cắt** (B8) — Ch.15 không được nhắc servo |
| **Thông tin bản quyền phần mềm lỗi thời** | Thấp | B10: ghi ngày kiểm tra |

---

## Chưa quyết

- **Giấy phép phát hành** (CC BY-NC-SA hay đóng).
- **Định dạng xuất bản** (.md → .docx/.pdf/HTML) — chưa dựng pipeline, chưa có `tools/`.
- **Repo git** — chưa khởi tạo.
- Nền mô phỏng cụ thể cho bài tập Phụ lục I — nghiêng về CODESYS vì miễn phí và là cột neo trung lập,
  nhưng chưa chốt.
- Ai là chuyên gia an toàn sẽ rà soát Ch.47–48.

---

## Cấu trúc thư mục hiện tại

```
PLC_Programming_Book/
  CLAUDE.md                       — quy ước viết, 12 bất biến, bộ hãng Phụ lục A
  PROJECT_STATUS.md               — file này
  docs/
    00_Muc_luc.md                 — ⭐ khung sách 58 chương + 11 phụ lục
    00c_Tai_lieu_tham_khao.md     — mẫu ghi nguồn + nguyên liệu Phụ lục G/H
    case_study_may_mau.md         — hồ sơ máy mẫu DP-01 + quy tắc bóc lớp
    design-notes/
      0001-cau-truc-sach-va-cac-phuong-an.md   — 3 phương án cấu trúc, chọn A+C
      0002-chot-huong-va-mo-rong-khung.md      — ⭐ 5 quyết định đã chốt
      0003-doi-chieu-nguon-ngoai-va-bo-sung-khung.md — đối chiếu khung với nguồn ngoài + 8 bổ sung
```

Tài liệu nguồn nằm ngoài repo, ở `../PLC/reference/` (xem `00_INDEX.md` ở đó).
