# Phụ lục O — Sổ tay việc của người lập trình: từng việc · đạt khi · con số

> **Một người lập trình PLC đọc bản thảo sách này đã nói: *"việc của tôi chủ yếu là ánh xạ, I/O và
> viết chương trình."*** Phụ lục này gom **đúng phần việc đó** thành mười sáu thẻ, xếp theo thứ tự
> chúng xảy ra trong một dự án.
>
> ⭐ Mỗi thẻ trả lời bốn câu, không hơn: **làm theo thứ tự nào** · ⭐⭐ **thế nào thì coi là xong** — mỗi
> dòng trả lời được bằng *có* hoặc *không* · **con số nào, lấy từ đâu** · **mẹo nghề**. Phần *vì sao*
> nằm ở chương được trỏ tới — thẻ không nhắc lại, để in ra vẫn gọn.

---

## O.0 Cách dùng sổ tay này — và ba loại con số

```text
 Nhận việc → Bảng I/O → Đặt tên → Ánh xạ vào → Ghi ra → Khung chương trình → Cơ cấu → Trình tự
    O.1        O.2        O.3         O.4         O.5            O.6            O.7       O.8

 → Báo động → Analog → Truyền thông → Thử trên bàn → Kiểm I/O → Chạy thử → Sao lưu → Sửa khi máy chạy
     O.9        O.10       O.11           O.12          O.13        O.14       O.15         O.16
```

Mọi con số trong phụ lục mang **một trong ba nhãn**, vì ba loại số này dùng khác nhau:

| Nhãn | Nghĩa | ⭐ Dùng thế nào |
|---|---|---|
| **[Chuẩn]** | Lấy từ tiêu chuẩn, đặc tả giao thức hoặc khuyến nghị của tổ chức ngành | Không tự chỉnh |
| **[Hãng]** | Lấy từ tài liệu của hãng — **đúng cho dòng sản phẩm đã nêu** | ⚠ Tra lại theo đúng CPU, đúng module của bạn |
| **[Nghề]** | Quy tắc thực dụng của nghề — **điểm xuất phát có lập luận**, không phải giá trị chuẩn hoá | ⭐ Dùng để bắt đầu, **đo trên máy của bạn rồi chỉnh**, và ghi lại con số đã chọn kèm lý do |

> ⚠⚠ **Hai giới hạn của cả phụ lục.**
>
> - Không con số nào ở đây thay được **phép đo trên máy thật**. Con số **[Nghề]** chỉ cho bạn một chỗ
>   bắt đầu hợp lý thay vì đoán.
> - ⚠ **Không thẻ nào áp dụng cho chức năng an toàn.** Dừng khẩn cấp, cửa bảo vệ, rèm quang, STO đi
>   qua phần cứng an toàn hoặc chương trình an toàn, được nghiệm thu bằng thử thật và do người có
>   thẩm quyền ký (Chương 47, 48; Phụ lục C mục C.8). Người lập trình logic thường chỉ **đọc trạng
>   thái** của chúng.

Phụ lục này dùng chung với bốn phụ lục khác — mỗi cái một vai:

| Bạn cần | Ở đâu |
|---|---|
| Biểu mẫu để điền | **Phụ lục C** |
| Mẫu mã chép được | **Phụ lục L** |
| Cấu hình dự án phần mềm (phần cứng, mạng, khởi động, mật khẩu) | **Phụ lục M**, danh mục M.10 |
| Quy ước viết mã | **Phụ lục N** |
| ⭐ **Làm việc nào, theo thứ tự nào, đạt khi nào, con số nào** | **Phụ lục này** |

---

## O.1 Nhận việc — hồ sơ tối thiểu trước dòng mã đầu tiên

**Khi nào:** trước khi mở phần mềm lập trình. **Vì sao:** Chương 23 (đặc biệt mục 23.2b), Chương 22
mục 22.4b.

| # | Việc |
|---|---|
| 1 | Đối chiếu hồ sơ nhận được với bảng dưới. Thiếu mục nào thì ghi thành **câu hỏi có tên người trả lời và hạn** — không tự đoán |
| 2 | Đọc đặc tả, rồi **tự kể lại** một chu trình và hai tình huống lỗi cho người viết đặc tả nghe |
| 3 | Liệt kê **giả định** của bạn ở những chỗ đặc tả còn trống, gửi khách xác nhận (Chương 23, ô *Ngoài hiện trường* ở mục 23.5b) |

| Hồ sơ | Để làm gì trong việc lập trình | Biểu mẫu |
|---|---|---|
| ⭐ **Bảng I/O đã ký** | Nguồn của mọi tên tag và mọi dòng ánh xạ | C.1 |
| Đặc tả trình tự + bảng chuyển trạng thái | Nguồn của mọi bước và mọi trạng thái | C.3 · C.4 |
| ⭐ **Trạng thái an toàn của từng ngõ ra** khi mất điện điều khiển, mất khí, đứt dây | Quyết định cách viết tầng ghi ra và cấu hình ngõ ra khi CPU dừng (thẻ O.5) | Chương 48 mục 48.2 |
| Danh sách chức năng an toàn — tín hiệu nào, do thiết bị nào xử lý | Biết rõ cái gì **không** thuộc chương trình của bạn | Chương 47 mục 47.9 |
| Cấu hình phần cứng | Địa chỉ module, khe cắm | C.10 |
| Quy ước đặt tên **của khách** | Nếu có, quy ước của họ thắng (Chương 30 mục 30.2) | — |
| Tiêu chí nghiệm thu | Biết trước mình sẽ bị thử bằng gì | Chương 23 mục 23.6 |

### ✅ Đạt khi

- [ ] Mọi dòng của bảng hồ sơ đã có — hoặc có **tên người chịu trách nhiệm và hạn**.
- [ ] Bạn kể lại được một chu trình và hai tình huống lỗi, và người viết đặc tả **công nhận là đúng**.
- [ ] ⭐ Mỗi ngõ ra đã có trạng thái an toàn cho cả ba tình huống mất năng lượng.
- [ ] ⚠ Bạn chỉ ra được tín hiệu nào thuộc phần an toàn — và chúng **không** được viết bằng logic thường.

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Phần việc từ nhận yêu cầu tới bảng I/O đã ký, so với cả dự án | **15–25 %**; dưới 10 % gần như luôn trả lại ở khâu chạy thử | [Nghề] — Chương 23 mục 23.2b |

> 💡 **Hai câu hỏi kiểm thứ tự dự án trong mười giây:** *"đã đặt hàng chưa?"* và *"bảng I/O đã ký
> chưa?"*. Câu đầu *rồi* mà câu sau *chưa* thì dự án đang đi ngược (Chương 23 mục 23.2b).
>
> 💡 **Nhận một chương trình cũ thay vì một dự án mới?** Dựng bản đồ chương trình (Chương 22 mục 22.4)
> rồi viết bản tóm tắt hai–ba trang ngay khi dựng xong — đánh dấu rõ chỗ nào là suy đoán.

---

## O.2 Bảng I/O — kiểm và chốt

**Vì sao:** Chương 23 mục 23.3. **Biểu mẫu:** C.1.

| # | Việc |
|---|---|
| 1 | Mỗi điểm trên bản vẽ điện **một dòng**: tag · mô tả · loại thiết bị · NO/NC · PNP/NPN · trạng thái nghỉ · địa chỉ · số dây · cầu đấu |
| 2 | Điền **cột phân loại** — tín hiệu nào là an toàn, tín hiệu nào là điều khiển (Chương 23 mục 23.3) |
| 3 | Đếm **theo loại** — DI, DO, AI, AO riêng — rồi tính dự phòng cho **từng module**, không cho tổng |
| 4 | Kiểm dòng tổng qua **chân chung** của từng module ngõ ra (Chương 9 mục 9.4) |
| 5 | Ghi rõ **NC** ở mọi tiếp điểm NC — người sau sẽ mặc định là NO (Chương 15) |
| 6 | Ký — sau mốc này, đổi bảng I/O là một thay đổi có kiểm soát |
| 7 | ⭐ Xếp địa chỉ theo **bảy quy tắc** ở Chương 23 mục 23.3: theo trạm, cặp cảm biến liền nhau, dự phòng trong nhóm, bảng an toàn riêng… |
| 8 | Máy có truyền động: lập thêm bảng **trục và động cơ** — phanh, STO, gốc, cáp (Phụ lục C mục C.10.3) |

### ✅ Đạt khi

- [ ] Mỗi tag có **một** nghĩa, không kiêm nhiệm.
- [ ] Mỗi module còn **≥ 20 % kênh dự phòng**.
- [ ] Tín hiệu an toàn đã tách riêng và đánh dấu.
- [ ] ⭐ Số dây khớp sơ đồ điện **và** khớp nhãn trong tủ.
- [ ] Dòng tổng qua mỗi chân chung đã kiểm và nằm trong giới hạn datasheet.
- [ ] ⭐ Mỗi module có dòng tiêu đề; hai cảm biến của mỗi xy-lanh liền nhau, cùng thứ tự, bắt đầu ở kênh
      chẵn; kênh dự phòng nằm **trong** nhóm của từng trạm.
- [ ] Tín hiệu an toàn có **bảng riêng**; hai kênh của một thiết bị là hai dòng liền nhau.

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Dự phòng I/O và bộ nhớ | **≥ 20 %** | [Nghề] — Chương 8 mục 8.3 |
| Dòng nguồn 24 V | Dòng ở **bước nhiều tải nhất** × **1,3–1,5** | [Nghề] — Chương 8 mục 8.7, Phụ lục K |

> 💡 **Viết bảng I/O theo đúng thứ tự địa chỉ module**, không theo thứ tự trên máy. Lúc kiểm I/O một–một
> (thẻ O.13), người đứng ở tủ đi lần lượt từng kênh — bảng theo thứ tự địa chỉ thì không phải nhảy
> dòng.

---

## O.3 Đặt tên — tag, khối, thể hiện

**Vì sao:** Chương 30 mục 30.2, 30.2b; Phụ lục N mục N.6, N.7.

| Loại | Mẫu | Ví dụ DP-01 |
|---|---|---|
| Dây vào / ra | `DI_` `DO_` `AI_` `AO_` + chỗ + cái gì | `DI_BoardStn1` · `DO_Clamp1Vlv` |
| ⭐ Tín hiệu đã qua tầng ánh xạ vào | `X_` + **đúng phần đuôi của dây** | `X_BoardStn1` — tra chéo một bước sang `DI_BoardStn1` |
| Cờ nội bộ | `M_` | `M_Stn1_ClampReq` |
| Bộ định thời · bộ đếm | `T_` · `C_` | `T_StepTimeout` |
| Giao diện công bố · ruột của trạm | `Stn1.` · `Stn1_` | `Stn1.Ready` · `Stn1_Step` |
| Kiểu khối | `FB_` | `FB_Cylinder2Pos` |
| ⭐ Thể hiện khối | **tên cơ cấu, không tiền tố kiểu** | `Clamp1`, không phải `FB_Clamp1` |

### ✅ Đạt khi

- [ ] ⭐⭐ **Ba nơi, một tên:** tag trong chương trình = số dây trong tủ (Chương 49 mục 49.6) = nhãn trên
      màn hình (Chương 44).
- [ ] Không tên phủ định — `DI_DoorClosed`, không phải `DI_DoorNotOpen` (Chương 30, quy tắc 5).
- [ ] Cùng một khái niệm, cùng một từ — `Board` ở mọi nơi, không lẫn `PCB`, `Part`.
- [ ] Địa chỉ tuyệt đối **chỉ** xuất hiện ở phần khai báo (Chương 27 mục 27.2b).
- [ ] Quy ước đã **viết ra** (Phụ lục N mục N.6). Khách có quy ước riêng thì dùng của khách.
- [ ] ⭐ Hệ kiểu thiết bị: có **trang quy hoạch địa chỉ theo khối** trước dòng mã đầu tiên — mỗi trạm một
      khối cho mỗi loại thiết bị, khối đầu của vùng bước để riêng (Chương 11 mục 11.8b).

> 💡 **Tiền tố theo vai trò là để tham chiếu chéo trả lời nhanh.** Tìm `DI_` cho bạn mọi chỗ chạm dây;
> nếu kết quả nằm ngoài tầng ánh xạ, bạn vừa tìm ra một chỗ đọc vòng (thẻ O.4) — trong ba giây,
> không phải ba giờ (Chương 22 mục 22.3).

---

## O.4 Tầng ánh xạ vào — `Prg_IoRead`

**Vì sao và ví dụ hoàn chỉnh:** Chương 27 mục 27.3c. **Khối dùng:** `FB_Debounce` (Chương 17).

| # | Việc |
|---|---|
| 1 | Một nhóm dòng cho mỗi ngõ vào chương trình dùng, ⭐ **theo đúng thứ tự bảng I/O** |
| 2 | **Chọn nguồn** thật hay mô phỏng — ⚠⚠ không bao giờ cho tín hiệu an toàn (Chương 50 mục 50.3) |
| 3 | **Lọc** theo bảng con số dưới — mỗi thể hiện lọc gọi đúng một lần mỗi vòng, ngoài `IF` |
| 4 | **Đặt tên `X_`** sao cho đứt dây rơi về phía an toàn: nút NC → `X_StopOK`, không đảo thành "đã nhấn" |
| 5 | ⚠ **Chiều an toàn đi thẳng** — tín hiệu dừng, mất khí: chép thẳng, không lọc, không mô phỏng |
| 6 | Gọi `Prg_IoRead` **đầu tiên** trong chương trình chính (Chương 14 mục 14.7) |

### ✅ Đạt khi

- [ ] ⭐ Tham chiếu chéo: mỗi `DI_` **chỉ được đọc trong `Prg_IoRead`** — trừ tín hiệu an toàn đọc trong
      phần an toàn.
- [ ] Mỗi `X_` có chú thích: loại tiếp điểm, thời gian lọc, có mô phỏng hay không.
- [ ] ⭐ Rút dây từng tín hiệu NC → `X_` về `FALSE` và máy về phía an toàn (thử ở thẻ O.13 và Chương 52
      mục 52.7).
- [ ] Tắt mô phỏng thì mọi `X_` bằng đúng dây thật; tín hiệu an toàn **không có** biến `Sim_`.

### 📏 Con số — thời gian lọc

| Tín hiệu | Lọc khởi điểm | Vì sao | Loại |
|---|---|---|---|
| Nút nhấn, công tắc cơ khí | **20 ms** | Tiếp điểm nảy vài mili-giây khi đóng cắt (Chương 4) | [Nghề] |
| Cảm biến quang, tiệm cận — ở mép sản phẩm | **30–50 ms** | Cảm biến điện tử **không nảy tiếp điểm**; thứ cần lọc là nháy ở mép, bề mặt sản phẩm | [Nghề] — DP-01 dùng 50 ms (Chương 17) |
| Reed của xy-lanh | **Không lọc** ở tầng này | Khối cơ cấu đã giám sát thời gian; một lần nháy chỉ làm `Done` trễ một vòng quét (Chương 27 mục 27.3c) | [Nghề] |
| ⚠ Dừng, mất khí, mọi tín hiệu an toàn | **Không lọc** | Lọc chỉ làm chậm phản ứng phía an toàn | — |

⭐ Ba ràng buộc cho mọi thời gian lọc — kiểm cả ba, lấy giá trị nằm giữa:

| Ràng buộc | Giá trị | Lập luận |
|---|---|---|
| Cận dưới | **≥ 2 lần chu kỳ quét** — nên từ 3 lần | Bộ định thời chỉ thấy tín hiệu ở mỗi lần đọc; dưới hai lần đọc thì "ổn định" không có nghĩa |
| Cận trên theo sản phẩm | **≤ 1/5** của khoảng ngắn hơn trong hai khoảng: *thời gian có vật* và *khe hở giữa hai vật* | Tín hiệu thật ngắn hơn thời gian lọc sẽ bị nuốt; chừa biên cho tốc độ dao động |
| Cận trên theo vị trí — khi cảm biến quyết định chỗ dừng | **≤ dung sai vị trí ÷ tốc độ** | Mỗi mili-giây lọc là thêm một đoạn trượt |

> ⚡ Thời gian lọc **phần cứng** của module (thường vài trăm micro-giây tới vài mili-giây, Chương 9 mục
> 9.2 và 9.3b) cộng **thêm** vào lọc phần mềm. Xung ngắn hơn lọc phần cứng thì không có cách nào bắt bằng
> ngõ vào thường — dùng bộ đếm tốc độ cao (Chương 18 mục 18.5).
>
> 💡 **Nghi lọc chưa đủ?** Đặt một bộ đếm thứ hai trên tín hiệu **chưa lọc** và hiện cả hai: hiệu số là
> số cạnh giả — bạn đo được thay vì đoán (Chương 18 mục 18.4).

---

## O.5 Tầng ghi ra — `Prg_OutputMap`, và ngõ ra khi CPU dừng

**Vì sao và ví dụ hoàn chỉnh:** Chương 27 mục 27.3c; Chương 14 mục 14.7; Chương 48 mục 48.2.

| # | Việc |
|---|---|
| 1 | **Một dòng cho mỗi ngõ ra đã đấu**, theo thứ tự bảng I/O |
| 2 | Vế phải là **đầu ra của khối cơ cấu** (`Clamp1.Valve`) hoặc lệnh của **chủ duy nhất** của tài nguyên chung ở tầng máy (`M_ConvRunCmd`) |
| 3 | ⚠ **Không `IF`, không liên động, không chặn chung** — kể cả "chặn mọi ngõ ra khi mô phỏng": tắt van một cuộn là **ra lệnh** cho xy-lanh về lò xo (Chương 27 Bẫy 7) |
| 4 | Gọi `Prg_OutputMap` **cuối cùng**, khi mọi quyết định của vòng quét đã xong |
| 5 | ⭐ Cấu hình **trạng thái ngõ ra khi CPU sang STOP hoặc lỗi** cho khớp cột *mất điện điều khiển* của bảng an toàn — ⚠ lúc đó `Prg_OutputMap` **không chạy**, chỉ cấu hình phần cứng quyết định (Chương 10 mục 10.5) |

### ✅ Đạt khi

- [ ] ⭐ Tham chiếu chéo: mỗi `DO_` có **đúng một** chỗ ghi, và chỗ đó nằm trong `Prg_OutputMap`.
- [ ] Không dòng nào ở tầng trạm, tầng máy ghi `DO_` (Chương 27 mục 27.8, dòng 1–2).
- [ ] ⚠⚠ Đã thử: máy đứng ở tư thế làm việc, đưa CPU sang STOP — mọi ngõ ra về đúng trạng thái đã cấu
      hình, **không cơ cấu nào chuyển động ngoài bảng ở Chương 48 mục 48.2**. Làm khi không có người
      trong vùng nguy hiểm.

> 💡 **Viết `Prg_OutputMap` theo thứ tự địa chỉ, mỗi dòng một chú thích tên cơ cấu** — in khối đó ra là
> có ngay phiếu kiểm ngõ ra cho thẻ O.13.

---

## O.6 Khung chương trình, tác vụ và thời gian quét

**Vì sao:** Chương 14 mục 14.4, 14.7; Chương 27 mục 27.6; Chương 10; Phụ lục M mục M.4.

| # | Việc |
|---|---|
| 1 | **Một tác vụ chu kỳ** — thêm tác vụ chỉ khi có một con số biện minh (Chương 27 mục 27.6) |
| 2 | Thứ tự gọi: **ánh xạ vào → chế độ và cho phép → cơ cấu → chống va chạm → gom lỗi → tầng máy → các trạm → … → ghi ra** (khung đầy đủ: Chương 57 mục 57.6) |
| 3 | Cờ vòng quét đầu `M_FirstScan` xoá ở **dòng cuối** của chương trình chính (Chương 16 Bẫy 9) |
| 4 | Chạy đủ tải, **đo thời gian chạy lớn nhất** của từng tác vụ và thời gian quét lớn nhất |
| 5 | Đặt **giám sát thời gian quét** (watchdog) có chủ ý, rồi ghi con số vào hồ sơ |
| 6 | Máy có servo qua mạng trường: mọi khối `MC_*` gom vào **một** chương trình trục, gắn vào **tác vụ của mạng trường**; biến qua lại giữa hai tác vụ — mỗi biến **một** tác vụ ghi (Chương 37 mục 37.8; Chương 22 mục 22.6b) |

### ✅ Đạt khi

- [ ] Chương trình chính gọi mỗi phần **đúng một lần**, đúng thứ tự ở bước 2.
- [ ] ⭐ Thời gian chạy lớn nhất của mỗi tác vụ định kỳ **≤ 50 %** chu kỳ của nó.
- [ ] Thời gian quét lớn nhất đã ghi vào hồ sơ bàn giao (Phụ lục C mục C.9).
- [ ] ⚠ Không có lệnh nạp lại watchdog giữa vòng quét, trừ đoạn khởi tạo chạy một lần (Chương 10 mục 10.2).
- [ ] Có từ hai tác vụ: bảng *biến ↔ tác vụ ghi* không có dòng nào mang hai tác vụ; chu kỳ các tác vụ
      là **bội số nguyên** của nhau.

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Ngân sách thời gian của tác vụ định kỳ | Chạy lớn nhất **≤ 50 %** chu kỳ — còn chỗ cho phần thêm về sau; vượt 100 % là tác vụ chồng lên chính nó | [Nghề] — Chương 27 mục 27.6 |
| Thời gian quét tối đa (Siemens S7-1200) | Đặt được **1–6000 ms**, mặc định **150 ms** | [Hãng] — sổ tay hệ thống S7-1200 |
| Watchdog từng tác vụ (Rockwell Logix) | **1 ms–2000 s**, mặc định **500 ms**, tính cả thời gian bị tác vụ khác ngắt | [Hãng] — 1756-PM005 |
| Chu kỳ tác vụ định kỳ (Rockwell Logix) | **0,1 ms–2000 s**, mặc định **10 ms** | [Hãng] — 1756-PM005 |
| Tác vụ của DP-01 | **10 ms** | Máy mẫu (Chương 14 mục 14.7) |
| Tác vụ EtherCAT (Inovance, dòng cỡ trung) | Ưu tiên **0**, chỉ **một**, chu kỳ thường **1–4 ms**; khối chuyển động của trục **chỉ** gọi ở đây; không đặt 3, 6, 7, 9 ms | [Hãng] — sổ tay lập trình chuyển động 19012378 bản A00 (Chương 37 mục 37.8) |
| Nhịp tự tạo bằng bộ định thời (nháy đèn) | Nửa chu kỳ **≥ 10 lần** chu kỳ tác vụ — sai số làm tròn dưới 10 %; ⚠ không dùng để đo thời gian | [Nghề] — Chương 22 mục 22.6b |

> ⭐ **Đọc hai con số mặc định trên cạnh nhau:** với vòng quét khoảng 10 ms, watchdog mặc định dài gấp
> **15–50 lần**. Nó chỉ bắt được chương trình **treo hẳn** — còn vòng quét **dài dần** sau mỗi lần thêm
> chức năng thì chỉ con số bạn ghi lúc máy vừa chạy tốt mới cho thấy (Chương 10, mẹo ghi thời gian quét).

---

## O.7 Cơ cấu — khối dùng lại, và giới hạn thời gian hành trình

**Vì sao:** Chương 27 mục 27.3; Phụ lục L mục L.8; Chương 6 mục 6.4 (mẹo ghi thời gian hành trình).

| # | Việc |
|---|---|
| 1 | Một khối cho mỗi **loại** cơ cấu; mỗi cơ cấu một thể hiện mang tên cơ cấu |
| 2 | Gọi mọi thể hiện ở **một** chương trình (`Prg_Mechanisms`), mỗi thể hiện đúng một lần mỗi vòng |
| 3 | Chỉnh tiết lưu cho tốc độ đúng **trước**, rồi mới đo mốc (Chương 6 mục 6.5) |
| 4 | Đặt giới hạn thời gian hành trình theo cách dưới |
| 5 | Thử năm hành vi trong ô *Đạt khi* |

### ⭐ Đặt giới hạn thời gian hành trình (`Limit`) — làm thế này, không đoán

| Giai đoạn | Làm gì |
|---|---|
| Chưa có máy | Dùng **giá trị thiết kế** của đặc tả (ví dụ cột *Hết giờ* ở Phụ lục J mục J.3), ghi chú *"chưa đo"* |
| ⭐ Máy chạy được | Đo **≥ 20 hành trình mỗi chiều** ở điều kiện **chậm nhất còn hợp lệ** — áp khí thấp nhất cho phép, tải nặng nhất. Lấy giá trị lớn nhất: `T_max`. Ghi làm **mốc** (Phụ lục C mục C.9) |
| Đặt `Limit` | **2 × `T_max`**, làm tròn lên 0,1 s — nhưng **không nhỏ hơn `T_max` + 0,5 s** |
| Đặt ngưỡng **nhắc** chậm dần | Khoảng giữa mốc và `Limit` — xấp xỉ **1,5 × mốc**. ⚡ Chỉ **nhắc**, không dừng máy (Chương 53 Bẫy 8) |

> ⭐ **Vì sao hai con số này, không phải con số khác.** `Limit` quá sát `T_max` thì khí hơi yếu một chút
> là báo động giả; quá xa thì mất tác dụng phát hiện, và mỗi lần kẹt thật máy đứng chờ lâu hơn (Chương 6
> Bẫy 7). Gấp đôi cho biên đủ rộng với dao động áp khí bình thường; mức **+0,5 s** giữ biên có nghĩa cho
> xy-lanh rất nhanh. Ngưỡng nhắc đặt ở nửa đường để ⭐ **lời nhắc luôn tới trước lỗi**, còn kịp lên kế
> hoạch thay thế.

### ✅ Đạt khi — thử trên bàn hoặc trên máy, không người trong vùng

- [ ] Ở gốc, `Req` tắt → `Done`; `Req` bật → van bật, `Done` **chỉ** khi cảm biến đích lên.
- [ ] Giữ cảm biến đích không lên quá `Limit` → `Fault`, mã 1, ⭐ van **giữ nguyên**.
- [ ] Hai cảm biến cùng lên → `Fault`, mã 2.
- [ ] ⚠ Mất `Permit` giữa hành trình → van giữ nguyên, **không** có chuyển động mới (Chương 27 Bẫy 7).
- [ ] Reset khi nguyên nhân còn → lỗi chốt lại ngay trong vòng quét đó.

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Số hành trình đo để lấy mốc | **≥ 20** mỗi chiều | [Nghề] |
| `Limit` | **2 × `T_max`**, tối thiểu `T_max` + 0,5 s | [Nghề] |
| Ngưỡng nhắc chậm dần | ≈ **1,5 × mốc** | [Nghề] — suy ra từ quy tắc *nhắc ở nửa đường* |

> 💡 **Mất khí làm mọi xy-lanh chậm cùng lúc** — nên một báo động gốc *"mất khí"* phải **ức chế** các
> báo động quá giờ của từng xy-lanh (Chương 44 mục 44.3). Không có ức chế thì người vận hành nhận mười
> báo động cho một nguyên nhân.

> ⚡ **Hai đầu chung một ray** (Chương 37 mục 37.7b): khoảng hở tối thiểu = kích thước hai thân theo
> bản vẽ + biên **[Nghề] ≥ 2 lần sai lệch bám lớn nhất** đo được ở tốc độ cao nhất; thời gian phản ứng
> **[Nghề] 3 chu kỳ** của tác vụ chạy phép kiểm — một để vị trí về PLC, một để logic chạy, một để lệnh
> dừng ra tới drive.

---

## O.8 Trình tự — bước, chuyển tiếp, giới hạn thời gian bước

**Vì sao:** Chương 26 (mục 26.4, 26.5b); Chương 25 mục 25.5c; Phụ lục L mục L.6.

| # | Việc |
|---|---|
| 1 | Viết trình tự **bằng lời** (Phụ lục C mục C.3) trước khi viết mã |
| 2 | Đánh số bước **cách nhau 10** — chừa chỗ chèn (Chương 26 Bẫy 3) |
| 3 | Chuyển tiếp bằng **phản hồi thật**; yêu cầu gửi cơ cấu phát ở **chuyển tiếp**, bước sau mới đọc `Done` (Chương 26 Bẫy 7) |
| 4 | Đặt giới hạn thời gian từng bước theo bảng dưới |
| 5 | Mỗi lỗi nói ba điều: **bước nào · đang chờ gì · nên kiểm gì** (Chương 26 mục 26.4) |

### ⭐ Giới hạn thời gian của bước — theo loại bước

| Loại bước | Giới hạn | Loại |
|---|---|---|
| Chờ một cơ cấu | **`Limit` của cơ cấu + 1–2 s** — để lỗi **cụ thể hơn** (xy-lanh nào) báo trước lỗi của bước | [Nghề] — Chương 26 mục 26.5b dùng 3 s và 5 s |
| Chờ quy trình (tra keo, sấy) | **Thời gian dài nhất mà công thức cho phép × 1,5** — lấy theo giới hạn trên của công thức, ⚠ không theo mã hàng đang chạy, để đổi mã hàng không sinh báo động giả | [Nghề] |
| Chờ hệ khác (máy trước, trạm sau) | ⭐ **Không giới hạn ở bước** — `T#0S` kèm ghi chú *có chủ ý*; giám sát ở **tầng máy** bằng cảnh báo *"máy đứng chờ"* | Chương 26 mục 26.4 |
| Chờ trả lời qua mạng (đầu đọc mã, MES) | Theo thẻ O.11 — 3–5 lần thời gian trả lời đo được | [Nghề] — Chương 39 mục 39.7 |

| Cảnh báo *"máy đứng chờ"* | Giá trị | Loại |
|---|---|---|
| Điểm xuất phát | **5 × chu kỳ đích** — DP-01: 5 × 12 s = **60 s** | [Nghề] |
| Sau một tuần chạy | Khoảng nghỉ **dài nhất đã thấy** khi máy trước dừng bình thường (đổi lô, thay vật tư) **+ 50 %** | [Nghề] |

### ✅ Đạt khi

- [ ] Mọi bước chờ có giới hạn — hoặc `T#0S` kèm ghi chú *có chủ ý* **và** có giám sát ở tầng máy.
- [ ] Không chuyển tiếp nào dùng bộ định thời thay cho phản hồi của cơ cấu (ngoại lệ hợp lệ: thời gian
      của quy trình — Chương 26 mục 26.2b).
- [ ] ⭐ Rút từng cảm biến khi đang chạy → dừng đúng bước, thông báo nêu bước và tín hiệu đang chờ.
- [ ] ⭐ **Chu trình thứ hai** chạy giống hệt chu trình đầu — không bước nào bị nhảy qua.
- [ ] Giữ máy (`Hold`) lâu hơn mọi giới hạn rồi chạy tiếp → **không** báo quá giờ giả.

> 💡 **Mã lỗi lấy luôn số bước** — `S1.20` trên màn hình là tra được ngay dòng nào trong đặc tả
> (Phụ lục J mục J.3), không cần bảng mã riêng.

---

## O.9 Báo động và thông báo lỗi

**Vì sao:** Chương 44 mục 44.3; Chương 25 mục 25.5c; Phụ lục L mục L.11.

| # | Việc |
|---|---|
| 1 | Lập danh sách từ bảng lỗi của đặc tả, rồi áp **phép thử**: có hành động cần làm **và** còn đủ thời gian để làm — thiếu một vế thì hạ xuống mức ghi nhận |
| 2 | Xếp **ba mức**: báo động · cảnh báo · ghi nhận |
| 3 | Gom lỗi **một chỗ**: `M_AnyFault` gán đúng một lần (Chương 25 mục 25.5c) |
| 4 | **Ức chế hệ quả** có điều kiện rõ, tự gỡ, và vẫn ghi vào nhật ký |
| 5 | Ghi **báo động đầu tiên** của một chuỗi |
| 6 | Tín hiệu dao động: **trễ trước khi báo** cho xung nhiễu; **vùng chết** cho giá trị sát ngưỡng |
| 7 | ⭐ **Đánh số**: khối theo loại lỗi + số thứ tự thiết bị; lỗi trình tự: khối theo trạm, số theo bước (Chương 44 mục 44.3) |

### ✅ Đạt khi

- [ ] ⭐ Mỗi báo động có dòng **"làm gì tiếp"** — `Kẹp trạm 1 không lên trong 3 giây — kiểm áp khí,
      kiểm cảm biến reed DI_Clamp1Up`, không phải `Lỗi 1042`.
- [ ] Không quá **ba** mức.
- [ ] Reset khi nguyên nhân còn → lỗi chốt lại; máy **không** quay vòng `Alarm ↔ Resetting`.
- [ ] ⭐ Ngắt khí → **một** báo động gốc, không kéo theo quá giờ của từng xy-lanh.
- [ ] Mọi báo động theo ngưỡng có **ngưỡng báo khác ngưỡng gỡ**.
- [ ] Xác nhận **không xoá được** báo động khi nguyên nhân còn.
- [ ] ⭐ Mỗi xy-lanh có **hai số riêng**: *không về gốc* và *không tới đích* — không gộp thành một số
      *"quá giờ"*.

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Lỗi truyền thông — báo khi | **≥ 3 lần lỗi liên tiếp** | [Nghề] — Chương 39 mục 39.7 |
| Nhịp tim giữa hai hệ | Đảo bit mỗi **0,5 s**; báo mất đối tác sau **2 s** không đổi | [Nghề] — Chương 48 mục 48.5 |
| Độ rộng vùng chết | Lớn hơn **biên độ dao động bình thường đã đo** của chính đại lượng đó | [Nghề] — Chương 44 mục 44.3 |
| Ngưỡng nhắc bảo trì theo tuổi thọ | **0,7** (nhắc) và **0,9** (cảnh báo) × tuổi thọ datasheet | [Nghề] — Chương 53 mục 53.5 |

> ⚠ **Ngưỡng nhắc không bao giờ dừng máy** (Chương 53 Bẫy 8). Một lời nhắc làm dừng máy sẽ bị tắt
> trong tuần đầu tiên.

---

## O.10 Analog — từ giá trị thô tới quyết định

**Vì sao:** Chương 31 mục 31.3; Chương 32; Phụ lục L mục L.12 — phép quy đổi tra ở Phụ lục K.

| # | Việc — ⚠ thứ tự không đổi được |
|---|---|
| 1 | ⭐ **Phát hiện ngoài dải trước** — chưa hợp lệ thì chưa quy đổi |
| 2 | Quy đổi: **nhân trước, chia sau**, dùng `DINT` |
| 3 | Lọc — **chỉ** cho hiển thị và ghi |
| 4 | Ngưỡng **có vùng chết**, dùng giá trị **chưa lọc** |

### ✅ Đạt khi

- [ ] ⭐ Giá trị thô ứng với 20 mA đã **tra datasheet module** — `27648` chỉ là một ví dụ thường gặp.
- [ ] Kiểm **quy đổi** bằng nguồn dòng ở tối thiểu **ba điểm 4 · 12 · 20 mA** (0 · 50 · 100 %): giá trị
      hiện lệch không quá tổng sai số khai trong datasheet của module và của nguồn dòng.
- [ ] ⭐ Rút dây cảm biến → báo **lỗi cảm biến**, không báo *"áp thấp"*; logic dùng giá trị thay thế an toàn.
- [ ] Chẩn đoán đứt dây của kênh đã bật trong cấu hình module (Phụ lục M mục M.10).

### 📏 Con số

| Dòng đo được | Nghĩa | Loại |
|---|---|---|
| ≤ 3,6 mA | Cảm biến hỏng — hướng thấp (đứt dây, mất nguồn) | [Chuẩn] — khuyến nghị NAMUR, Chương 31 mục 31.3 |
| 3,8–4,0 mA | ⭐ **Đo dưới dải — không phải lỗi** | [Chuẩn] — như trên |
| 20,5–21,0 mA | Đo trên dải — không phải lỗi | [Chuẩn] — như trên |
| ≥ 21,0 mA | Cảm biến hỏng — hướng cao | [Chuẩn] — như trên |
| Điểm kiểm | Ba điểm 0 · 50 · 100 % cho kiểm quy đổi; **năm điểm** 0 · 25 · 50 · 75 · 100 % khi hiệu chuẩn thiết bị đo | [Nghề] — năm điểm theo thực hành đo lường quá trình |

> ⚠ **Kiểm quy đổi không phải hiệu chuẩn.** Chỉnh hệ số cho PLC hiện khớp đồng hồ chỉ làm hai con số
> **nhất quán**, chưa làm chúng **đúng** — hiệu chuẩn cần một chuẩn chính xác hơn hẳn và có vết truy
> nguyên (Chương 32 mục 32.8).

---

## O.11 Truyền thông — bảng ánh xạ thanh ghi và bắt tay

**Vì sao:** Chương 38 mục 38.9; Chương 39 mục 39.4–39.8; Chương 41 mục 41.3, 41.6; Chương 48 mục 48.5.

| # | Việc |
|---|---|
| 1 | Lập **bảng ánh xạ** — mỗi dòng: thanh ghi theo tài liệu thiết bị (⭐ ghi rõ đánh số từ 0 hay từ 1) · mã hàm · kiểu dữ liệu · ⭐ thứ tự word nếu 32 bit · đơn vị · hệ số · tag PLC |
| 2 | Thử bằng **phần mềm chủ giả lập trên máy tính** nối thẳng thiết bị trước khi đụng tới PLC (Chương 39 mục 39.8) |
| 3 | Xác nhận từng dòng bằng **một giá trị đã biết** — đổi trên mặt thiết bị, xem có đổi theo không |
| 4 | Định nghĩa **mất truyền thông là một trạng thái**: máy làm gì, báo gì, hồi phục thế nào (Chương 38 mục 38.9) |
| 5 | **Nhịp tim** cho mọi đối tác — bit phải **đảo trạng thái**, không giữ mức (Chương 48 mục 48.5) |
| 6 | ⭐ Phần mềm PC đọc ghi PLC (PLC là **máy chủ**): chia vùng thanh ghi **theo người ghi** — vùng A chỉ PLC ghi, vùng B chỉ phần mềm ghi; bảng giao tiếp là tài liệu **có số phiên bản** (Chương 39 mục 39.9b) |
| 7 | Bắt tay mỗi yêu cầu tới phần mềm bằng **số thứ tự** (`FB_PcRequest`, Phụ lục L mục L.16b); phần mềm ghi kết quả **trước**, số thứ tự **sau** |
| 8 | Bốn ô cố định của bảng giao tiếp: **phiên bản · nhịp tim hai chiều · trạng thái máy · số bước** |

### ✅ Đạt khi

- [ ] ⭐ Mỗi dòng bảng ánh xạ đã xác nhận bằng một giá trị đã biết.
- [ ] Mọi giá trị 32 bit đã kiểm **thứ tự word** bằng giá trị đã biết (Chương 39 mục 39.5).
- [ ] ⭐ Rút cáp → phản ứng đúng đặc tả; cắm lại → hồi phục **không cần nạp lại chương trình**.
- [ ] Bắt tay SMEMA: chỉ chuyển sản phẩm khi **cả hai** tín hiệu cùng đúng; tín hiệu ra khỏi máy qua
      rơ-le hoặc cách ly quang (Chương 41 mục 41.3).
- [ ] ⭐ Bảng giao tiếp với phần mềm PC: tham chiếu chéo trên PLC cho thấy mọi ô vùng B **không** có chỗ
      ghi, mọi ô vùng A **đúng một** chỗ ghi.
- [ ] Tắt phần mềm PC lúc PLC đang chờ → báo quá thời gian, sản phẩm thành *"không biết"*; bật lại →
      chạy tiếp, **không** phải nạp lại gì. Phiên bản hai bên lệch → máy không vào tự động.

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Thời gian chờ trả lời (timeout) | **3–5 lần** thời gian trả lời đo được khi mọi thứ bình thường | [Nghề] — Chương 39 mục 39.7 |
| Báo lỗi truyền thông | Sau **≥ 3 lần lỗi liên tiếp** | [Nghề] — Chương 39 mục 39.7 |
| Đọc thanh ghi một lần (mã hàm 0x03, 0x04) | Tối đa **125** thanh ghi | [Chuẩn] — đặc tả Modbus |
| Ghi nhiều thanh ghi (0x10) | Tối đa **123** thanh ghi | [Chuẩn] — đặc tả Modbus |
| Đọc bit (0x01, 0x02) | Tối đa **2000** bit | [Chuẩn] — đặc tả Modbus |
| Nhịp tim | Đảo **0,5 s** · giám sát **2 s** | [Nghề] — Chương 48 mục 48.5 |
| Phiên bản bảng giao tiếp PLC–PC | Số dạng năm-tháng-ngày, ví dụ `261007` | [Nghề] — đọc bằng mắt, luôn tăng (Chương 39 mục 39.9b) |
| Số thứ tự yêu cầu tới PC | Quay vòng **1…30000**, không dùng số 0 | [Nghề] — vừa kiểu `INT` (Chương 39 mục 39.9b) |
| Bộ đếm sống của nút giữ trên màn hình | Dừng lệnh khi bộ đếm đứng yên quá **3 lần** chu kỳ cập nhật đo được | [Nghề] — Chương 44, Bẫy 14 |

> 💡 **Gặp mã ngoại lệ 02 trong khi chắc chắn địa chỉ đúng?** Giảm số lượng thanh ghi đọc một lần — mã
> 02 nói về **tổ hợp** địa chỉ bắt đầu và số lượng (Chương 39 mục 39.8).

---

## O.12 Kiểm thử trên bàn

**Vì sao:** Chương 50. **Biểu mẫu:** Phụ lục C mục C.7.

| # | Việc |
|---|---|
| 1 | Dựng lớp mô phỏng **trong tầng ánh xạ vào** (Chương 27 mục 27.3c, Chương 50 mục 50.3) |
| 2 | Cho cơ cấu giả **có độ trễ** — không thì không thử được quá giờ (Chương 50 mục 50.3) |
| 3 | Chạy nhóm ca **A–F** (Chương 50 mục 50.4) |
| 4 | Ghi kết quả từng ca (Chương 50 mục 50.5) |
| 5 | ⭐ **Giữ lớp mô phỏng sống** sau bàn giao — mỗi lần sửa về sau thử được trên bàn |

### ✅ Đạt khi

- [ ] Mọi ca A–F **đạt**, mỗi ca có: ngày · người thử · ⭐ **phiên bản chương trình** · cách tạo điều
      kiện · kết quả thật.
- [ ] Mỗi ca có **kỳ vọng viết trước** khi chạy — ca không có kỳ vọng thì không thể trượt.
- [ ] ⚠ Nhóm an toàn **không** thử bằng mô phỏng — đã ghi rõ trong danh sách ca.

### 📏 Con số

| Vòng kiểm thử hồi quy | Chạy | Mất | Loại |
|---|---|---|---|
| Tối thiểu | Nhóm A + ca đúng chỗ sửa | Vài phút | [Nghề] — Chương 50 mục 50.5b |
| ⭐ Tiêu chuẩn — **mặc định** | Trên + nhóm B + nhóm F | ~nửa giờ | [Nghề] — như trên |
| Đầy đủ | A–F | Vài giờ | [Nghề] — bắt buộc khi đổi máy trạng thái, liên động, firmware |

---

## O.13 Kiểm I/O một–một tại máy

**Vì sao:** Chương 52 mục 52.4. **Biểu mẫu:** Phụ lục C mục C.6.

> ⚠⚠ **NGUY HIỂM — kiểm ngõ ra là lúc máy chuyển động lần đầu.** Từng cơ cấu một; không ai trong vùng
> máy; người thao tác đứng ở chỗ nhìn được toàn bộ cơ cấu; tay đặt gần nút dừng khẩn cấp; gỡ mọi cưỡng
> bức ngay sau mỗi phép thử (Chương 52 mục 52.4).

| # | Việc |
|---|---|
| 1 | CPU ở STOP hoặc chạy chương trình rỗng — bạn kiểm **dây**, không kiểm logic |
| 2 | Từng ngõ vào: **tác động thiết bị thật** → đúng bit lên → nhả → bit về |
| 3 | Từng ngõ ra: cưỡng bức theo quy trình (Chương 51 mục 51.7) → đúng cơ cấu chuyển động → gỡ cưỡng bức |
| 4 | Ghi biên bản ngay sau từng kênh |

### ✅ Đạt khi

- [ ] **100 % kênh đã đấu dây** có kết quả — kể cả kênh dự phòng đã đấu.
- [ ] Ngõ vào: ⭐ **đúng bit**, không phải bit bên cạnh; trạng thái nghỉ khớp cột *trạng thái nghỉ* của
      bảng I/O — tiếp điểm NC thì nghỉ bằng 1.
- [ ] Ngõ ra: đúng cơ cấu, ⭐ cảm biến phản hồi của chính cơ cấu đó đổi theo; **không** cơ cấu nào khác
      chuyển động.
- [ ] Nhãn trên màn hình và số dây khớp tag (thẻ O.3).
- [ ] ⭐ Danh sách cưỡng bức **rỗng** khi kết thúc.

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Thời gian cho máy cỡ DP-01 | Khoảng **nửa ngày** — nửa ngày rẻ nhất của cả dự án | Máy mẫu (Chương 52 mục 52.4) |

---

## O.14 Chạy thử, đo chu kỳ, ghi mốc

**Vì sao:** Chương 52 mục 52.6–52.9; Chương 55 mục 55.4.

| # | Việc |
|---|---|
| 1 | Chạy khô **từng bước** rồi mới liên tục — kiểm cờ chạy khô, cưỡng bức, ⚠ cờ mô phỏng đã tắt |
| 2 | Có sản phẩm: **một** → hai → liên tục |
| 3 | **Tạo lỗi cố ý** — mười ca của Chương 52 mục 52.7, trên máy thật |
| 4 | Chạy liên tục, **đo chu kỳ trong một giờ** ở điều kiện sản xuất thật |
| 5 | Ghi **mốc** trong lúc chạy liên tục |

### ✅ Đạt khi

- [ ] Đủ mười ca tạo lỗi, mỗi ca có biên bản.
- [ ] ⭐ Sản lượng đếm trong **một giờ liên tục** ≥ cam kết của đặc tả — ⚠ không đo năm phút rồi nhân lên.
- [ ] ⭐ Mốc đã ghi: thời gian quét lớn nhất · điện áp 24 V nhỏ nhất ở bước nặng nhất · nhiệt độ tủ ·
      thời gian hành trình từng xy-lanh · thời gian lớn nhất của từng bước (Phụ lục C mục C.9).
- [ ] Danh mục ở Chương 52 mục 52.9 đạt hết; hạng mục còn mở nằm trong **danh mục tồn**, có người và hạn.

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Đo sản lượng | **Một giờ liên tục**, điều kiện sản xuất thật | Chương 52 mục 52.8 |
| Chạy liên tục — tối thiểu | Đủ để tủ **nóng ổn định**: **vài giờ** | Chương 52 mục 52.8 |
| Ví dụ tiêu chí ổn định đo được | *"Chạy liên tục 8 giờ, không dừng ngoài kế hoạch quá 2 lần"* | Ví dụ đặc tả — Chương 23 mục 23.6 |

---

## O.15 Sao lưu và bàn giao mã

**Vì sao:** Chương 54 mục 54.3, 54.5; Phụ lục C mục C.9; Phụ lục M mục M.8.

### ✅ Đạt khi

- [ ] ⭐ Đủ **tám hạng mục** của Chương 54 mục 54.3 — ⚠ kể cả tham số chức năng an toàn của biến tần,
      servo, và ⭐ chương trình cùng điểm dạy của robot.
- [ ] ⭐⭐ **Đã thử khôi phục ít nhất một lần** — tốt nhất nạp vào CPU dự phòng trên bàn; tối thiểu mở
      tệp trên một máy tính khác.
- [ ] Chương trình đang chạy **khớp bản sao lưu** — kiểm bằng chức năng so sánh dự án, không bằng trí
      nhớ.
- [ ] Quy trình khôi phục một trang cất **cùng chỗ** với bản sao lưu.
- [ ] ⚠ Không còn cưỡng bức, logic tạm, cờ mô phỏng, cờ chạy khô (Chương 52 mục 52.9, dòng 1–3).

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Sao lưu định kỳ | **Hàng quý**, kể cả khi không sửa gì — để phát hiện thay đổi không ai ghi | [Nghề] — Chương 54 |
| Thử khôi phục mức thấp nhất (mở tệp) | **Mười phút mỗi quý** — bắt được ba trong sáu nguyên nhân thất bại | [Nghề] — Chương 54 mục 54.5 |

---

## O.16 Sửa chương trình khi máy đang chạy

**Vì sao:** Chương 53 mục 53.2, 53.3; Chương 22 mục 22.7; Chương 50 mục 50.5b.

| # | Việc |
|---|---|
| 1 | Trả lời **năm câu** trước khi sửa: vì sao · ai duyệt · đã sao lưu chưa · thử thế nào · ai cần biết |
| 2 | Xếp **mức rủi ro**: thấp · vừa · cao · rất cao (Chương 53 mục 53.3) |
| 3 | Sao lưu bản đang chạy |
| 4 | Sửa — trực tuyến **chỉ** trong các trường hợp Chương 53 mục 53.2 cho phép |
| 5 | Chạy **vòng hồi quy** do **người thứ hai** chọn (thẻ O.12) |
| 6 | Ghi lại — **dưới hai phút**, ngay tại máy |

### ✅ Đạt khi

- [ ] Năm câu đã có câu trả lời viết ra.
- [ ] ⚠⚠ Thay đổi chạm mạch an toàn, chương trình an toàn hoặc cấu hình thiết bị an toàn: **không sửa
      trực tuyến**, và đã lên lịch **kiểm định lại**.
- [ ] Vòng hồi quy đã chạy và ghi kết quả.
- [ ] Bản sao lưu mới đã lưu và **khớp** máy.

### 📏 Con số

| Thông số | Giá trị | Loại |
|---|---|---|
| Thời gian ghi một thay đổi | **Dưới hai phút** — biểu mẫu ngắn, ghi tại máy | [Nghề] — Chương 53 mục 53.3 |
| Đường khẩn cấp | Sửa trước, **duyệt và ghi trong 24 giờ** | [Nghề] — Chương 53 mục 53.3 |

---

## O.17 ⭐ Bảng con số nhanh — mọi con số của phụ lục này

In riêng trang này nếu chỉ in một trang.

| Thông số | Giá trị | Loại | Thẻ |
|---|---|---|---|
| Dự phòng I/O, bộ nhớ | ≥ 20 % | [Nghề] | O.2 |
| Dòng nguồn 24 V | Bước nhiều tải nhất × 1,3–1,5 | [Nghề] | O.2 |
| Lọc nút nhấn, công tắc cơ khí | 20 ms | [Nghề] | O.4 |
| Lọc cảm biến ở mép sản phẩm | 30–50 ms | [Nghề] | O.4 |
| Lọc — cận dưới | ≥ 2 lần chu kỳ quét, nên từ 3 lần | [Nghề] | O.4 |
| Lọc — cận trên | ≤ 1/5 thời gian có vật hoặc khe hở, lấy cái ngắn hơn | [Nghề] | O.4 |
| Lọc tín hiệu dừng, mất khí, an toàn | Không lọc | — | O.4 |
| Ngân sách thời gian tác vụ định kỳ | Chạy lớn nhất ≤ 50 % chu kỳ | [Nghề] | O.6 |
| Thời gian quét tối đa S7-1200 | 1–6000 ms, mặc định 150 ms | [Hãng] | O.6 |
| Tác vụ EtherCAT (Inovance cỡ trung) | Ưu tiên 0 · chỉ một · thường 1–4 ms · không đặt 3, 6, 7, 9 ms | [Hãng] | O.6 |
| Nhịp tự tạo (nháy đèn) | Nửa chu kỳ ≥ 10 × chu kỳ tác vụ; không dùng để đo thời gian | [Nghề] | O.6 |
| Watchdog tác vụ Rockwell Logix | 1 ms–2000 s, mặc định 500 ms | [Hãng] | O.6 |
| Chu kỳ tác vụ định kỳ Rockwell Logix | 0,1 ms–2000 s, mặc định 10 ms | [Hãng] | O.6 |
| Số hành trình đo để lấy mốc | ≥ 20 mỗi chiều | [Nghề] | O.7 |
| Giới hạn hành trình `Limit` | 2 × `T_max`, tối thiểu `T_max` + 0,5 s | [Nghề] | O.7 |
| Ngưỡng nhắc xy-lanh chậm dần | ≈ 1,5 × mốc | [Nghề] | O.7 |
| Biên khoảng hở hai đầu chung một ray | ≥ 2 × sai lệch bám lớn nhất | [Nghề] | O.7 |
| Thời gian phản ứng khi kiểm khoảng hở | 3 chu kỳ tác vụ | [Nghề] | O.7 |
| Giới hạn bước chờ cơ cấu | `Limit` + 1–2 s | [Nghề] | O.8 |
| Giới hạn bước chờ quy trình | Giới hạn trên của công thức × 1,5 | [Nghề] | O.8 |
| Cảnh báo *máy đứng chờ* | 5 × chu kỳ đích; sau một tuần: khoảng nghỉ dài nhất + 50 % | [Nghề] | O.8 |
| Lỗi truyền thông — báo sau | ≥ 3 lần lỗi liên tiếp | [Nghề] | O.9, O.11 |
| Nhịp tim | Đảo 0,5 s · giám sát 2 s | [Nghề] | O.9, O.11 |
| Ngưỡng nhắc / cảnh báo bảo trì | 0,7 / 0,9 × tuổi thọ datasheet | [Nghề] | O.9 |
| Dòng analog — hỏng hướng thấp | ≤ 3,6 mA | [Chuẩn] | O.10 |
| Dòng analog — đo dưới dải, không phải lỗi | 3,8–4,0 mA | [Chuẩn] | O.10 |
| Dòng analog — đo trên dải, không phải lỗi | 20,5–21,0 mA | [Chuẩn] | O.10 |
| Dòng analog — hỏng hướng cao | ≥ 21,0 mA | [Chuẩn] | O.10 |
| Điểm kiểm quy đổi analog | 4 · 12 · 20 mA | [Nghề] | O.10 |
| Timeout truyền thông | 3–5 × thời gian trả lời đo được | [Nghề] | O.11 |
| Modbus — đọc thanh ghi một lần | ≤ 125 | [Chuẩn] | O.11 |
| Modbus — ghi nhiều thanh ghi | ≤ 123 | [Chuẩn] | O.11 |
| Modbus — đọc bit | ≤ 2000 | [Chuẩn] | O.11 |
| Phiên bản bảng giao tiếp PLC–PC | Năm-tháng-ngày, ví dụ 261007 | [Nghề] | O.11 |
| Số thứ tự yêu cầu tới PC | Quay vòng 1…30000, bỏ 0 | [Nghề] | O.11 |
| Bộ đếm sống nút giữ trên màn hình | Dừng khi đứng yên > 3 × chu kỳ cập nhật | [Nghề] | O.11 |
| Đo sản lượng | Một giờ liên tục | Chương 52 | O.14 |
| Sao lưu định kỳ | Hàng quý | [Nghề] | O.15 |
| Ghi một thay đổi | Dưới hai phút; khẩn cấp: ghi trong 24 giờ | [Nghề] | O.16 |
| Cỡ khối quy hoạch địa chỉ (hệ kiểu thiết bị) | 100 mỗi trạm, mọi trạm cùng cỡ | [Nghề] | O.3 |
| FX5, khi dùng lệnh `IST` | `S0`–`S19` bị chiếm sẵn — trình tự bắt đầu từ `S100` | [Hãng] | O.3 |
| Cỡ khối số báo động | Lớn hơn số thiết bị dự kiến cộng chỗ thêm — ví dụ 50 | [Nghề] | O.9 |

> ⭐⭐ **Mỗi con số [Nghề] trong bảng là một quyết định bạn được phép đổi — nhưng phải ghi lại.**
> Đổi `Limit` từ 2 × xuống 1,5 × vì máy của bạn rất ổn định là hợp lý; đổi mà không ghi thì người sau
> sẽ coi đó là lỗi và "sửa" lại.

---

### Nguồn tham khảo phụ lục O

- Các chương và phụ lục được trỏ tới trong từng thẻ — mỗi con số **[Nghề]** ở đây đã có lập luận ở
  chương gốc, hoặc có lập luận ngay trong thẻ (thẻ O.4, O.7, O.8).
- **Siemens** — *S7-1200 Programmable controller System Manual* (A5E02486680), mục chu kỳ quét: thời
  gian quét tối đa đặt được 1–6000 ms, mặc định 150 ms; thời gian quét tối thiểu cố định là tuỳ chọn,
  mặc định tắt — nền cho thẻ O.6. Kiểm 2026-10-01.
- **Rockwell Automation** — *Logix 5000 Controllers Tasks, Programs, and Routines* (1756-PM005, bản
  9/2025): watchdog từng tác vụ 1–2 000 000 ms, mặc định 500 ms, tính cả thời gian bị tác vụ khác ngắt;
  tác vụ định kỳ 0,1 ms–2000 s, mặc định 10 ms — nền cho thẻ O.6. Kiểm 2026-10-01.
- **Rockwell Automation** — *Logix 5000 Controllers I/O and Tag Data* (1756-PM004, bản 11/2023), mục
  *Buffer I/O*: logic không tham chiếu trực tiếp tag của thiết bị thật mà dùng bản sao; chương trình
  chính gọi lần lượt `map_inputs` · logic của máy · `map_outputs` — nền cho thẻ O.4, O.5 và Chương 27
  mục 27.3c.
- **MODBUS Application Protocol Specification V1.1b3** — giới hạn số lượng của mã hàm 0x01–0x04 và
  0x10 — nền cho thẻ O.11.
- **Kuphaldt** — *Lessons in Industrial Instrumentation*, phần hiệu chuẩn: kiểm năm điểm 0 · 25 · 50 ·
  75 · 100 % của dải — nền cho dòng *điểm kiểm* ở thẻ O.10.
- **Bryan, L.A. & Bryan, E.A.** — *Programmable Controllers: Theory and Implementation*, ch. 8, mục
  module vào nhanh: thiết bị vào nhanh — cảm biến tiệm cận, tế bào quang điện — **không có nảy tiếp
  điểm**, nên bộ lọc chỉ gây trễ rất ngắn — nền cho bảng thời gian lọc ở thẻ O.4.

> ⚠ **Giới hạn của phụ lục.** Đây là sổ tay việc của **người lập trình logic thường**. Thiết kế điện,
> đánh giá rủi ro, chức năng an toàn và kiểm định thuộc người có thẩm quyền khác — các thẻ chỉ trỏ
> sang, không thay thế (Chương 47, 48). Tên gọi và cách đặt cụ thể theo từng hệ: Phụ lục A1, A2, M.
