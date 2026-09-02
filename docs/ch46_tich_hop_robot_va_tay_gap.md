# Chương 46 — Tích hợp robot & tay gắp

> **Lát cắt máy mẫu:** 4 — thêm mạng: mã 2D, MES, SMEMA, màn hình vận hành, và bộ điều khiển nhiệt độ
> keo nối RS-485.
>
> ⚠ **DP-01 không có robot.** Chương này dùng ví dụ riêng; mục 46.9 nói nếu cần thì ghép thế nào.

---

## 46.1 Bài toán: hai chương trình, không ai đọc được toàn bộ

Một trạm gắp board từ khay sang chuyền. Người tích hợp chọn robot, và viết logic **chia đôi**: PLC lo
chuyền và khay, robot lo việc gắp — và một phần logic quyết định "gắp ô nào tiếp theo" nằm **trong
chương trình robot**.

Máy chạy tốt hai năm. Rồi khay đổi kích thước, cần sửa cách đếm ô.

Người bảo trì mở chương trình PLC. Không thấy logic đếm ô ở đâu. Tìm mãi mới hiểu nó nằm trong robot —
và để sửa cần **phần mềm khác, tay cầm dạy khác, và kiến thức khác**. Người biết dùng nó đã nghỉ việc.

Máy dừng ba ngày chờ nhà cung cấp.

> ⭐ **Vấn đề không phải robot. Vấn đề là logic của một cỗ máy nằm ở hai chỗ, và không ai đọc được
> toàn bộ ở một nơi.**

Đây là cùng bài học với Chương 43 mục 43.3 (đừng để vision điều khiển cơ cấu) và Chương 44 mục 44.6
(đừng để logic trong HMI). Chương này áp nó cho robot — nơi cám dỗ mạnh nhất, vì robot **thật sự có**
khả năng lập trình đầy đủ.

---

## 46.2 Khi nào cần robot

| Dùng **cơ cấu chuyên dụng** khi | Dùng **robot** khi |
|---|---|
| Một hoặc hai vị trí cố định | ⭐ **Nhiều vị trí**, hoặc vị trí thay đổi theo mã hàng |
| Chuyển động thẳng đơn giản | Chuyển động phức tạp, cần tránh vật cản |
| ⭐ Chu kỳ rất ngắn | Chu kỳ vừa phải |
| ⭐ Giá thành quan trọng, sản lượng lớn | Cần linh hoạt, đổi sản phẩm thường xuyên |
| Đội bảo trì quen cơ cấu khí nén | ⭐ Có người biết lập trình robot |
| Không gian chật | Cần vươn xa, xoay nhiều hướng |

> ⭐ **Xy-lanh khí nén thường nhanh hơn và rẻ hơn robot cho một chuyển động cố định.**
> Robot thắng khi bạn cần **nhiều điểm khác nhau**, hoặc khi điểm **đổi theo mã hàng** — vì đổi điểm
> là đổi dữ liệu, không phải đổi cơ khí.
>
> Đây là cùng câu hỏi với Chương 43 mục 43.2: **có cách rẻ hơn làm được việc này không?**

### Ba loại robot hay gặp

| Loại | Đặc điểm | Hợp với |
|---|---|---|
| **SCARA** | Nhanh, cứng theo phương đứng, làm việc trên mặt phẳng | ⭐ Gắp đặt board, lắp ráp điện tử |
| **Sáu trục** | Linh hoạt nhất, vươn mọi hướng | Thao tác phức tạp, xoay nhiều chiều |
| ⭐ **Cộng tác** *(collaborative)* | Chạy chậm, có giới hạn lực | ⚠ Xem cảnh báo ở mục 46.7 |

---

## 46.3 ⭐⭐ Ai chỉ huy ai

Đây là quyết định quan trọng nhất của chương, và nó ảnh hưởng tới toàn bộ cách viết chương trình.

### Hai mô hình

| | ⭐ **PLC làm chủ** | **Robot làm chủ** |
|---|---|---|
| Ai giữ trình tự tổng thể | **PLC** | Robot |
| Robot làm gì | Nhận lệnh "chạy chương trình số N", báo xong | Điều phối cả trạm, gọi PLC khi cần |
| Logic nằm ở | ⭐ **Một chỗ** — PLC | ⚠ Hai chỗ |
| Người bảo trì đọc ở đâu | ⭐ Chương trình PLC | ⚠ Cả hai |
| Hợp khi | ⭐ **Robot là một cơ cấu trong máy** | Robot là trung tâm, PLC chỉ phụ trợ |

> ⭐⭐ **Khuyến nghị của sách: PLC làm chủ, robot làm tớ.**
>
> Robot khi đó là **một cơ cấu chấp hành phức tạp** — giống một xy-lanh có nhiều vị trí. PLC ra lệnh
> "đi tới điểm 5", robot đi và báo xong. Trình tự, điều kiện, xử lý lỗi đều nằm ở PLC.
>
> Lý do giống hệt Chương 43 và Chương 44: **người bảo trì phải đọc được toàn bộ logic ở một nơi.**

### ⚠ Khi nào robot làm chủ là hợp lý

Không phải lúc nào cũng sai. Robot làm chủ hợp khi:

- Trạm **chỉ có robot** và vài cảm biến, không có trình tự máy phức tạp.
- Robot cần **phối hợp chuyển động liên tục** với thiết bị khác — điều PLC không làm tốt.
- ⚠ Đội của khách hàng **quen làm việc theo cách đó**, và họ sẽ bảo trì.

> ⚠ Nhưng ngay cả khi đó, ⭐ **ranh giới phải rõ ràng và ghi vào tài liệu**: cái gì ở đâu, ai gọi ai.
> Thứ không chấp nhận được là ranh giới **mơ hồ** — như cỗ máy ở mục 46.1.

---

## 46.4 Ba cách ghép nối

| Cách | Nghĩa | ✅ / ⚠ |
|---|---|---|
| **I/O cứng** | Vài ngõ ra chọn chương trình, vài ngõ vào báo trạng thái | ⭐ Đơn giản, tin cậy, đo được; ⚠ ít thông tin |
| ⭐ **Gọi chương trình theo số** | PLC gửi số hiệu chương trình; robot chạy chương trình đó | ⭐ **Mẫu phổ biến nhất** — kết hợp đơn giản và đủ linh hoạt |
| **Mạng** | Trao đổi dữ liệu đầy đủ: toạ độ, tham số, trạng thái | Linh hoạt nhất; ⚠ phụ thuộc mạng |

### ⭐ Mẫu "gọi chương trình theo số"

```text
   PLC                                    ROBOT
    │                                       │
    ├── Đặt số chương trình = 5 ──────────► │
    ├── Xung "Bắt đầu" ──────────────────► │  chạy chương trình 5
    │                                       │
    │ ◄──────────── "Đang chạy" ───────────┤
    │ ◄──────────── "Xong" ────────────────┤  (hoặc "Lỗi" + mã)
    │                                       │
```

| Tín hiệu | Chiều | Ghi chú |
|---|---|---|
| Số chương trình | PLC → Robot | Vài bit, hoặc một thanh ghi |
| ⭐ **Bắt đầu** | PLC → Robot | Kích bằng **cạnh lên** (Chương 16) |
| Cho phép chạy | PLC → Robot | ⚠ Mất tín hiệu này → robot dừng |
| **Đang chạy** | Robot → PLC | |
| ⭐ **Xong** | Robot → PLC | ⭐ Chuyển bước bằng **cái này**, không bằng timer (Chương 17) |
| **Lỗi** + mã | Robot → PLC | Mã lỗi cụ thể, không chỉ một bit |
| Vị trí an toàn | Robot → PLC | ⭐ Robot đang ở chỗ không cản trở cơ cấu khác |

> ⭐ **Tín hiệu "vị trí an toàn" là tín hiệu hay bị quên và gây va chạm.**
> PLC cần biết robot đã **ra khỏi vùng** trước khi cho chuyền chạy hoặc cho cơ cấu khác vào. "Xong
> chương trình" không đủ — robot có thể xong nhưng vẫn đứng trong vùng.
>
> Đây là cùng nguyên tắc "chờ phản hồi thật" ở Chương 17, và cùng bài toán "ai đang giữ sản phẩm" ở
> Chương 41 mục 41.4.

---

## 46.5 ⭐ Dạy điểm — dữ liệu cần sao lưu như code

**Dạy điểm** *(teaching)* là việc đưa robot tới từng vị trí bằng tay cầm dạy và ghi lại toạ độ.

> ⭐⭐ **Toạ độ đã dạy là DỮ LIỆU, và nó quý ngang chương trình.**
>
> Một chương trình robot không có toạ độ thì vô dụng. Và toạ độ **không dựng lại được từ bản vẽ** —
> chúng phản ánh vị trí thật của đồ gá trên cỗ máy đó, sau khi đã căn chỉnh.
>
> Dạy lại toàn bộ điểm cho một trạm có thể mất **cả ngày**.

| Việc bắt buộc | Vì sao |
|---|---|
| ⭐ **Sao lưu toạ độ cùng chương trình** | Chương 54 — và nó thường là **tệp riêng**, dễ bị quên |
| ⭐ **Sao lưu sau mỗi lần dạy lại** | Không phải chỉ lúc bàn giao |
| **Ghi lại lý do dạy lại** | "Đổi đồ gá ngày 12/3" — người sau cần biết |
| ⚠ **Kiểm bản sao lưu khôi phục được** | Bản sao lưu chưa thử khôi phục không phải bản sao lưu |

> ⚠ **Điểm dạy mất hiệu lực khi cơ khí thay đổi** — thay đồ gá, va chạm làm lệch, tháo lắp lại robot.
> Đây là cùng bài toán với hiệu chỉnh camera ở Chương 43 mục 43.6: ⭐ **cần cách kiểm điểm còn đúng
> không**, và kiểm sau mọi lần chạm vào cơ khí.

### 💡 Điểm tương đối thay vì điểm tuyệt đối

Nếu robot gắp từ một khay có nhiều ô đều nhau, **đừng dạy từng ô**.

Dạy **một điểm gốc** và **khoảng cách giữa các ô**, rồi tính. Khi đồ gá lệch, chỉ cần dạy lại một
điểm.

> ⭐ Đây là cùng ý tưởng với "tách tham số khỏi logic" ở Chương 29: **dữ liệu có cấu trúc dễ bảo trì
> hơn nhiều so với một danh sách phẳng.**

---

## 46.6 Tay gắp

| Loại | Nguyên lý | Hợp với |
|---|---|---|
| ⭐ **Chân không** *(giác hút)* | Hút bề mặt phẳng | ⭐ Board mạch, tấm phẳng, hộp |
| **Kẹp cơ khí** | Hai hoặc ba ngón kẹp | Vật có hình dạng nắm được |
| **Từ tính** | Nam châm điện | Vật sắt từ |
| Chuyên dụng | Thiết kế riêng | Vật có hình dạng đặc thù |

### Tay gắp chân không cho board mạch

Đây là loại phổ biến nhất trong lắp ráp điện tử, và nguyên lý đã có ở Chương 6 mục 6.6.

| Điểm | ⚠ Chú ý |
|---|---|
| ⭐ **Cảm biến chân không** | ⭐ **Bắt buộc** — chờ phản hồi thật, không chờ timer (Chương 17) |
| Vị trí giác hút | Tránh linh kiện; ⚠ chọn vùng phẳng trên board |
| Số giác hút | Đủ để giữ chắc; nhiều quá thì khó hút đủ chân không nếu một cái hở |
| ⚠ **Mất khí thì sao** | ⭐ Xem cảnh báo bên dưới |
| Van hút ngược | Nhả nhanh và dứt khoát (Chương 6) |

> ⚠⚠ **NGUY HIỂM — mất khí khi đang giữ vật.**
> Giác hút mất chân không thì **vật rơi**. Với board mạch thì hỏng sản phẩm; với vật nặng thì có thể
> gây thương tích.
>
> Ba biện pháp:
> - ⭐ **Giám sát chân không liên tục** trong lúc di chuyển, không chỉ lúc bắt đầu — mất chân không
>   giữa chừng phải **dừng ngay**.
> - **Bình tích chân không** giữ được vài giây khi mất nguồn khí — đủ để hạ vật xuống.
> - ⚠ Với vật nặng, **không dùng chân không một mình** — cần khoá cơ khí.
>
> Đây là phân tích thuộc Chương 48 mục 48.2 (trạng thái an toàn khi mất năng lượng), và phần bảo vệ
> người thuộc Chương 47.

---

## 46.7 ⚠⚠ Vùng an toàn và robot

Đây là mục có rủi ro cao nhất chương.

### Robot là mối nguy nghiêm trọng

Robot công nghiệp chuyển động **nhanh, mạnh, và không đoán trước được** với người đứng gần. Một robot
đang chạy chương trình có thể vươn tới bất kỳ điểm nào trong vùng làm việc của nó, bất kỳ lúc nào.

| Biện pháp | Nội dung |
|---|---|
| ⭐ **Che chắn vật lý** | Rào, cửa có khoá liên động (Chương 47) |
| **Giới hạn vùng làm việc** | Bằng cơ khí, hoặc bằng chức năng an toàn của bộ điều khiển robot |
| ⭐ **Chức năng an toàn của robot** | Nhiều robot có chức năng giám sát vùng và giới hạn tốc độ **được chứng nhận** |
| **Dừng an toàn** | Qua mạch an toàn hoặc chức năng chuyên dụng (Chương 36, mục 36.6) |

> ⚠⚠ **Giới hạn vùng bằng phần mềm trong chương trình robot KHÔNG phải chức năng an toàn** — trừ khi
> nó là **chức năng an toàn được chứng nhận** của bộ điều khiển robot.
>
> Đây là cùng phân biệt với giới hạn phần mềm ở Chương 37 mục 37.6: một giới hạn nằm trong logic
> thường bảo vệ chống lỗi lập trình, **không** bảo vệ chống lỗi của chính hệ đó.

### ⚠ Robot cộng tác không tự động an toàn

Robot cộng tác được thiết kế để làm việc gần người — chạy chậm, có giới hạn lực, dừng khi chạm.

> ⚠⚠ **Nhưng "robot cộng tác" không có nghĩa là "ứng dụng cộng tác an toàn".**
>
> An toàn phụ thuộc vào **toàn bộ ứng dụng**, không chỉ vào robot:
> - Tay gắp có cạnh sắc không?
> - Vật đang mang có nặng, nóng, sắc không?
> - Robot có thể kẹp người vào một vật cố định không?
> - Tốc độ và lực cho phép là bao nhiêu **với ứng dụng này**?
>
> Một robot cộng tác cầm một con dao vẫn nguy hiểm. ⭐ **Đánh giá rủi ro phải làm cho ứng dụng, không
> phải cho robot** — Chương 47.

> ⚠ Việc xác định robot cộng tác có được vận hành không rào chắn hay không, và với tốc độ/lực nào,
> **phải do người có thẩm quyền** đánh giá theo tiêu chuẩn hiện hành. Đây không phải quyết định của
> người lập trình.

---

## 46.8 Xử lý lỗi và phục hồi

| Tình huống | Xử lý |
|---|---|
| **Robot báo lỗi** | ⭐ Đọc **mã lỗi cụ thể**; hiển thị kèm hướng dẫn (Chương 44, mục 44.3) |
| ⚠ **Robot không phản hồi** | Mất kết nối ≠ robot dừng — ⭐ xem bên dưới |
| **Gắp trượt** | ⭐ Cảm biến chân không phát hiện; dừng và báo, **không tiếp tục** |
| ⚠ **Dừng giữa chừng** | Robot ở tư thế bất kỳ — ⚠ phục hồi cần thận trọng |

> ⚠⚠ **"PLC mất kết nối với robot" không có nghĩa là robot đã dừng.**
> Robot có thể vẫn đang chạy chương trình của nó. PLC phải giả định **robot vẫn có thể chuyển động**
> và không cho cơ cấu khác vào vùng.
>
> Đây là cùng nguyên tắc với mất truyền thông ở Chương 38 mục 38.9: **mất kết nối nghĩa là không
> biết, không phải là đã dừng.**

### ⚠ Phục hồi sau khi dừng giữa chừng

Robot dừng giữa chương trình đang ở một tư thế bất kỳ, có thể đang giữ vật, có thể đang ở trong vùng
của cơ cấu khác.

> ⚠⚠ **Không được cho robot "chạy tiếp từ chỗ đang dở" một cách tự động.**
>
> Cùng lý do với biến bước của trình tự ở Chương 16 mục 16.4 và Chương 28: tư thế thật có thể đã thay
> đổi, và chương trình tin rằng nó biết mình đang ở đâu.
>
> Quy trình phục hồi phải: xác định robot đang ở đâu, xử lý vật đang giữ (nếu có), đưa robot về **vị
> trí an toàn đã biết**, rồi mới bắt đầu lại. Đây là nội dung Chương 28 áp cho robot.

---

## 46.9 Nếu DP-01 cần robot

DP-01 dùng chuyền và cơ cấu chặn/kẹp — không cần robot cho việc hiện tại. Nhưng nếu mở rộng để **nạp
board từ khay** thay vì nhận từ máy trước:

| Hạng mục | Quyết định |
|---|---|
| Loại robot | **SCARA** — gắp đặt board trên mặt phẳng |
| ⭐ **Ai chỉ huy** | **PLC làm chủ** — robot là một cơ cấu (mục 46.3) |
| Ghép nối | ⭐ **Gọi chương trình theo số** + vài I/O cứng |
| Tay gắp | **Chân không**, ⭐ **có cảm biến** (Chương 6, mục 6.6) |
| Điểm gắp trong khay | ⭐ **Điểm gốc + khoảng cách ô**, không dạy từng ô (mục 46.5) |
| Số ô, khoảng cách | ⭐ **Trong công thức sản phẩm** — mỗi mã hàng một khay khác (Chương 29) |
| Tín hiệu "vị trí an toàn" | ⭐ **Bắt buộc** — trước khi chuyền chạy (mục 46.4) |
| Mất kết nối robot | ⚠ Giả định robot **vẫn có thể chuyển động** (mục 46.8) |
| An toàn | ⚠⚠ Rào che, cửa liên động — Chương 47 |

```iecst
// PLC làm chủ: robot là một bước trong trình tự
CASE LoadStep OF
    10: // Yêu cầu robot gắp board từ ô tiếp theo
        RobotProgNo := PROG_PICK_FROM_TRAY;
        RobotSlotIndex := NextSlot;              // ⭐ tham số, không phải chương trình riêng
        Step := 20;

    20: // ⭐ Kích bằng cạnh lên (Chương 16)
        TrigRobotStart(CLK := TRUE);
        DO_RobotStart := TrigRobotStart.Q;
        Step := 30;

    30: // ⭐ Chờ PHẢN HỒI THẬT, không chờ timer (Chương 17)
        IF DI_RobotDone THEN
            Step := 40;
        ELSIF DI_RobotError THEN
            M_AnyFault := TRUE;
            M_FaultCode := 460 + RobotErrorCode;  // ⭐ mã cụ thể
        END_IF;

    40: // ⭐ Chờ robot RA KHỎI VÙNG trước khi cho chuyền chạy
        IF DI_RobotAtSafePos THEN
            M_ConvInRun := TRUE;
            NextSlot := NextSlot + 1;
            Step := 0;
        END_IF;

ELSE
    LoadStep := 0;                                // Chương 20
END_CASE;

// ⚠ Timeout cho mọi bước chờ (Chương 26)
T_Robot(IN := (LoadStep > 0), PT := T#20S);
IF T_Robot.Q THEN
    M_AnyFault := TRUE;  M_FaultCode := 469;
END_IF;
```

> ⭐ **Bước 40 là bước chống va chạm.** "Robot báo xong" không đủ — phải chờ nó **ra khỏi vùng**. Đây
> là tín hiệu hay bị quên nhất khi ghép robot (mục 46.4).

---

## 46.10 Khác biệt giữa các hãng

| Khía cạnh | Điều cần biết |
|---|---|
| ⚠ **Ngôn ngữ lập trình robot** | **Mỗi hãng một ngôn ngữ riêng** — không có chuẩn chung như IEC 61131-3. ⚠ Kiến thức chuyển giữa các hãng robot khó hơn nhiều so với giữa các hãng PLC |
| Tay cầm dạy | Giao diện và thao tác khác nhau hoàn toàn |
| ⭐ Ghép với PLC | Gần như mọi robot đều có I/O số và hỗ trợ vài mạng công nghiệp (Chương 40) |
| Gọi chương trình theo số | ⭐ Mẫu này có ở gần như mọi hãng — **tên gọi khác nhau** |
| ⚠ Lưu toạ độ | Tệp riêng, định dạng riêng. ⚠ **Phải nằm trong bản sao lưu** (mục 46.5) |
| Chức năng an toàn | Nhiều robot có chức năng giám sát vùng và tốc độ **được chứng nhận** — ⭐ kiểm mã sản phẩm |
| Mô phỏng ngoại tuyến | Một số hãng có công cụ mô phỏng tốt — hữu ích để giảm thời gian dạy tại máy |

> ⚠⚠ **Ngôn ngữ robot không có chuẩn chung là khác biệt lớn so với PLC.**
> Với PLC, kiến thức IEC 61131-3 chuyển được giữa các hãng (Chương 14, mục 14.6). Với robot thì không
> — mỗi hãng một thế giới.
>
> ⭐ Đây là lập luận **rất mạnh** cho việc chọn "PLC làm chủ" ở mục 46.3: nếu logic nằm ở PLC, việc
> đổi hãng robot chỉ ảnh hưởng phần nhỏ. Nếu logic nằm ở robot, đổi hãng là viết lại.

---

## 46.11 Bẫy thường gặp

### 🔍 BẪY 1 — Chia logic giữa PLC và robot một cách mơ hồ

**Hiện tượng:** ⭐ đúng cỗ máy ở mục 46.1 — người bảo trì không tìm được logic, và cần phần mềm khác
cùng kiến thức khác để sửa.
**Cách sửa:** ⭐⭐ **PLC làm chủ**; nếu buộc phải chia thì ranh giới **rõ ràng và ghi vào tài liệu**
(mục 46.3).

### 🔍 BẪY 2 — Quên tín hiệu "vị trí an toàn"

**Hiện tượng:** chuyền chạy hoặc cơ cấu khác vào vùng trong khi robot **vẫn còn ở đó** — va chạm.
**Cách sửa:** "xong" ≠ "đã ra khỏi vùng". Chờ tín hiệu riêng (mục 46.4, 46.9).

### 🔍 BẪY 3 — Không sao lưu toạ độ đã dạy

**Hiện tượng:** ⚠ mất toạ độ → phải dạy lại toàn bộ, có thể mất cả ngày; và không dựng lại được từ
bản vẽ.
**Cách sửa:** toạ độ nằm trong bản sao lưu, sao lưu **sau mỗi lần dạy lại** (mục 46.5, Chương 54).

### 🔍 BẪY 4 — Dạy từng ô của khay

**Hiện tượng:** đồ gá lệch nhẹ → phải dạy lại **tất cả** các ô.
**Cách sửa:** ⭐ điểm gốc + khoảng cách, tính ra các ô (mục 46.5).

### 🔍 BẪY 5 — Không giám sát chân không liên tục

**Hiện tượng:** ⚠⚠ vật rơi giữa đường di chuyển; hỏng sản phẩm, hoặc gây thương tích với vật nặng.
**Cách sửa:** giám sát **suốt quá trình di chuyển**, mất chân không thì **dừng ngay** (mục 46.6).

### 🔍 BẪY 6 — Chuyển bước bằng timer thay vì tín hiệu "xong"

**Hiện tượng:** bước sau chạy khi robot **chưa xong** — đúng bẫy trung tâm của Chương 17.
**Cách sửa:** chờ `DI_RobotDone`; timer chỉ để **báo lỗi**.

### 🔍 BẪY 7 — Coi mất kết nối là robot đã dừng

**Hiện tượng:** ⚠⚠ cho cơ cấu khác vào vùng trong khi robot **vẫn đang chạy chương trình**.
**Cách sửa:** mất kết nối = **không biết**, không phải đã dừng (mục 46.8, Chương 38 mục 38.9).

### 🔍 BẪY 8 — Cho robot chạy tiếp từ chỗ đang dở

**Hiện tượng:** ⚠⚠ va chạm — tư thế thật đã đổi trong lúc dừng.
**Cách sửa:** quy trình phục hồi qua **vị trí an toàn đã biết** (mục 46.8, Chương 28).

### 🔍 BẪY 9 — Tin rằng giới hạn vùng bằng phần mềm là an toàn

**Hiện tượng:** ⚠⚠ giới hạn không tác dụng đúng lúc cần nhất.
**Cách sửa:** chức năng an toàn phải là **chức năng được chứng nhận** hoặc che chắn vật lý
(mục 46.7, Chương 37 mục 37.6, Chương 47).

### 🔍 BẪY 10 — Tin rằng robot cộng tác thì mặc nhiên an toàn

**Hiện tượng:** ⚠⚠ tay gắp có cạnh sắc, hoặc vật mang nặng — robot "cộng tác" vẫn gây thương tích.
**Cách sửa:** ⭐ đánh giá rủi ro cho **ứng dụng**, không cho robot; do **người có thẩm quyền** làm
(mục 46.7, Chương 47).

### 🔍 BẪY 11 — Dùng robot cho việc xy-lanh làm được

**Hiện tượng:** chậm hơn, đắt hơn, và cần người biết lập trình robot để bảo trì.
**Cách sửa:** bảng ở mục 46.2 — robot thắng khi cần **nhiều điểm** hoặc **điểm đổi theo mã hàng**.

---

## 46.12 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Robot thắng khi | ⭐ **Nhiều vị trí**, hoặc vị trí **đổi theo mã hàng** |
| Xy-lanh thắng khi | Một, hai vị trí cố định; ⭐ chu kỳ rất ngắn; giá thành quan trọng |
| ⭐⭐ Ai chỉ huy ai | **PLC làm chủ, robot làm tớ** — logic ở **một chỗ** |
| Lý do chính | ⭐ Người bảo trì phải đọc được **toàn bộ logic ở một nơi** |
| Lý do phụ rất mạnh | ⚠ **Ngôn ngữ robot không có chuẩn chung** — đổi hãng là viết lại |
| Mẫu ghép phổ biến nhất | ⭐ **Gọi chương trình theo số** + I/O cứng |
| Tín hiệu hay bị quên nhất | ⭐ **Vị trí an toàn** — "xong" ≠ "đã ra khỏi vùng" |
| Chuyển bước sau lệnh robot | ⭐ Chờ **"xong"**, không chờ timer |
| ⭐⭐ Toạ độ đã dạy là | **Dữ liệu quý ngang code** — không dựng lại được từ bản vẽ |
| Khay nhiều ô | ⭐ **Điểm gốc + khoảng cách**, không dạy từng ô |
| Tay gắp chân không | ⭐ **Cảm biến bắt buộc**; ⚠ **giám sát liên tục** khi di chuyển |
| ⚠⚠ Mất kết nối robot nghĩa là | **Không biết**, ⚠ **không phải đã dừng** |
| Phục hồi sau dừng giữa chừng | Qua **vị trí an toàn đã biết**, không chạy tiếp tự động |
| ⚠⚠ Giới hạn vùng bằng phần mềm | **Không phải chức năng an toàn** |
| ⚠⚠ Robot cộng tác | **Không tự động an toàn** — đánh giá rủi ro cho **ứng dụng** |

---

## 46.13 Tự kiểm

1. ⭐ Mô tả sự cố ở mục 46.1. Vấn đề thật là gì, và nó giống bài học nào ở Chương 43 và Chương 44?
2. Nêu bốn tiêu chí chọn giữa robot và cơ cấu chuyên dụng. Robot thắng ở điểm nào?
3. ⭐⭐ So sánh "PLC làm chủ" với "robot làm chủ". Sách khuyến nghị cái nào và nêu **hai** lý do.
4. ⚠ Vì sao "ngôn ngữ robot không có chuẩn chung" là lập luận mạnh cho khuyến nghị ở câu 3?
5. Mô tả mẫu "gọi chương trình theo số". Kể các tín hiệu hai chiều.
6. ⭐ Tín hiệu nào hay bị quên nhất khi ghép robot, và hậu quả là gì? Vì sao "xong" không đủ?
7. ⭐⭐ Vì sao toạ độ đã dạy **quý ngang chương trình**? Vì sao không dựng lại được từ bản vẽ?
8. Với một khay nhiều ô đều nhau, vì sao **không** nên dạy từng ô? Ý tưởng này giống nguyên tắc nào ở
   Chương 29?
9. ⚠⚠ Vì sao phải giám sát chân không **liên tục** chứ không chỉ lúc bắt đầu gắp? Nêu ba biện pháp
   chống vật rơi.
10. ⚠⚠ PLC mất kết nối với robot. Được phép cho cơ cấu khác vào vùng không? Vì sao?
11. Vì sao **không** được cho robot chạy tiếp từ chỗ đang dở sau khi dừng? Liên hệ với chương nào?
12. ⚠⚠ "Robot cộng tác" có nghĩa là ứng dụng an toàn không? Nêu bốn câu hỏi phải trả lời, và **ai**
    được kết luận.

> Câu 3, 6, 7, 10 và 12 là năm câu phân loại. Câu 3 là tinh thần của cả chương: **một cỗ máy có logic
> ở hai chỗ là một cỗ máy mà không ai đọc được toàn bộ — và điều đó lộ ra đúng lúc bạn cần nhất.**

---

### Chương tiếp theo

Chương 47 — **An toàn máy**. Lát cắt 4 kết thúc ở đây; từ Chương 47, máy mẫu đầy đủ. Chương sau là
chương quan trọng nhất của cuốn sách: vì sao **không logic PLC thường nào thay được mạch an toàn**,
và làm sao làm việc đúng với người có thẩm quyền về an toàn.

### Nguồn tham khảo chương 46

- **ISO 10218** (bộ) — *Robots and robotic devices — Safety requirements for industrial robots*:
  yêu cầu an toàn cho robot công nghiệp và cho việc tích hợp chúng. *(tiêu chuẩn có bản quyền)*
- **ISO/TS 15066** — *Robots and robotic devices — Collaborative robots*: yêu cầu cho ứng dụng cộng
  tác — nền cho cảnh báo ở mục 46.7.
- ISO 12100 và ISO 13849 — đánh giá rủi ro và chức năng an toàn (Chương 47).
- **Tài liệu robot** của hãng đang dùng — dùng cho ngôn ngữ, cách ghép nối, ⚠ **định dạng và cách sao
  lưu toạ độ**, và chức năng an toàn có sẵn.
- Bảng I/O và số liệu đã chốt của DP-01 — Phụ lục J.

> ⚠⚠ **Giới hạn của chương này.** Nội dung ở đây là về **giao diện giữa PLC và robot** — phần thuộc
> trách nhiệm của người lập trình PLC. Nó **không** hướng dẫn lập trình robot, và **không** đủ để
> thiết kế an toàn cho một ứng dụng robot.
>
> Việc đánh giá rủi ro, xác định vùng nguy hiểm, chọn biện pháp bảo vệ, và kết luận một ứng dụng
> cộng tác có được vận hành không rào chắn hay không **phải do người có thẩm quyền** thực hiện theo
> tiêu chuẩn hiện hành tại thị trường của bạn. Robot là một trong những mối nguy nghiêm trọng nhất
> trên sàn nhà máy.
