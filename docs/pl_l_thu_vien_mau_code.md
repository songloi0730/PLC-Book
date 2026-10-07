# Phụ lục L — Thư viện mẫu code dùng ngay

> **Tài liệu tra cứu.** Mười chín đoạn logic lặp lại ở gần như mọi cỗ máy, gom về một chỗ — cộng một
> **danh mục ở L.17** trả lời câu hỏi đứng trước tất cả: *khối nào nên tự viết, khối nào đã có sẵn*. Mỗi mẫu kèm
> ⭐ **điều kiện dùng** và ⚠ **thứ nó KHÔNG làm** — vì chép một mẫu mà không biết giới hạn của nó là
> cách tạo ra lỗi trông rất giống code đúng.

---

> ⚠⚠ **Đọc trước khi chép bất cứ đoạn nào.**
>
> | | |
> |---|---|
> | 1 | ⭐ Mẫu viết bằng **Structured Text**; ⭐⭐ **bảy mẫu có thêm bản LADDER** ngay bên dưới. ⚠ Các mẫu còn lại cố ý **chỉ có ST** — lý do và cách chọn ở **mục L.18** |
> | 2 | ⭐ Tên biến theo máy mẫu DP-01 (Phụ lục J). Đổi sang tên máy của bạn — ⚠ **đừng giữ tên mẫu** |
> | 3 | ⚠⚠ **Không mẫu nào ở đây là chức năng an toàn.** Xem L.3 |
> | 4 | ⭐ Mọi mẫu đều **chạy trong một tác vụ chu kỳ**, được gọi mỗi vòng quét (Chương 10) |
> | 5 | ⚠ Mã báo động viết dạng hằng `ALM_*`, không viết số trực tiếp (Chương 44) |

---

## L.1 Tự giữ Start/Stop — nền của mọi thứ

⭐ **Dùng khi:** nhấn Start rồi nhả, máy vẫn chạy; nhấn Stop thì dừng.

```iecst
// ── Tự giữ: điều kiện DỪNG nằm NỐI TIẾP, NGOÀI dấu ngoặc tự giữ ──
M_Running := (DI_StartPB OR M_Running)      // nhánh tự giữ
             AND DI_StopPB                  // ⚠ nút NC → kiểm BẰNG 1
             AND M_AllPermissive;           // chuỗi cho phép (L.2)
```

⭐ **Cùng mẫu này viết bằng ladder** — đây là nấc thang phổ biến nhất trong cả ngành:

```text
   DI_StartPB      DI_StopPB    M_AllPermissive                      M_Running
 ┌───┤ ├──────┬──────┤ ├────────────┤ ├────────────────────────────────( )───┐
 │            │
 │  M_Running │
 └───┤ ├──────┘
```

> ⭐ **Ở ladder, mạch tự giữ NHÌN THẤY ĐƯỢC** — nó là nhánh song song vòng ngược về. ⚡ Đó là ưu thế
> thật của ladder ở mẫu này: ⚠ trong bản ST, dấu ngoặc đặt sai chỗ **trông vẫn bình thường**; trong
> ladder, nhánh tự giữ ôm nhầm cả `DI_StopPB` thì **nhìn là thấy ngay**.
>
> ⚡ Nấc này giống hệt nấc ở Chương 15 mục 15.4 — cố ý, vì đó là mẫu chuẩn.

> ⚠⚠ **Vị trí của điều kiện dừng quyết định tất cả.** Đưa `DI_StopPB` **vào trong** dấu ngoặc của
> nhánh tự giữ thì ⭐ **nhấn Stop trong lúc vẫn đang giữ Start sẽ KHÔNG dừng được máy** — và người thử
> thường không phát hiện, vì khi thử người ta nhả Start rồi mới nhấn Stop.
>
> ⭐ Nút Stop vật lý là **NC**, nên trong code kiểm **bằng 1**, không phải `NOT`. Đứt dây = dừng
> (Chương 15, mục 15.3).

> ⚠⚠ **Mẫu này giả định nút Start được NHẢ.** Tiếp điểm dính, nút bị đè, hay bit Start từ màn hình
> kẹt ở 1 khi mất kết nối thì lỗi vừa hết là `M_Running` lên lại — máy **tự chạy**. Máy nhận lệnh
> Start từ nhiều nơi thì thay `DI_StartPB` bằng **sườn** của nó (`StartEdge.Q`, L.7); ở ladder là
> tiếp điểm `┤P├`. Lý do đầy đủ: Chương 16 mục 16.6.

---

## L.2 Chuỗi cho phép chạy — và **lý do** khi không cho phép

⭐ **Dùng khi:** cần một cờ duy nhất trả lời *"máy có được phép chạy không"*.

```iecst
// ── Chuỗi cho phép ──
M_AllPermissive := DI_EStopOK                // mạch an toàn đang đóng
                   AND DI_Door1Closed
                   AND DI_Door2Closed
                   AND DI_CurtainOK
                   AND DI_AirOK              // đủ áp khí (Chương 6)
                   AND NOT M_AnyFault
                   AND M_Homed;              // đã về gốc (Chương 37, mục 37.3)

// ── VÌ SAO không cho phép — để báo lên màn hình, đừng bắt người vận hành đoán ──
IF    NOT DI_EStopOK     THEN M_BlockReason := BLK_ESTOP;
ELSIF NOT DI_Door1Closed THEN M_BlockReason := BLK_DOOR1;
ELSIF NOT DI_Door2Closed THEN M_BlockReason := BLK_DOOR2;
ELSIF NOT DI_CurtainOK   THEN M_BlockReason := BLK_CURTAIN;
ELSIF NOT DI_AirOK       THEN M_BlockReason := BLK_AIR;
ELSIF M_AnyFault         THEN M_BlockReason := BLK_FAULT;
ELSIF NOT M_Homed        THEN M_BlockReason := BLK_NOT_HOMED;
ELSE                          M_BlockReason := BLK_NONE;
END_IF;
```

⭐ **Bằng ladder** — chuỗi cho phép là nơi ladder **thắng rõ nhất**:

```text
 DI_EStopOK DI_Door1Closed DI_Door2Closed DI_CurtainOK DI_AirOK M_AnyFault M_Homed  M_AllPermissive
 ───┤ ├────────┤ ├────────────┤ ├───────────┤ ├────────┤ ├───────┤/├───────┤ ├────────( )───
```

> ⭐⭐ **Một nấc thang, đọc từ trái sang phải, và người vận hành hiểu ngay.** ⚡ Khi máy không chạy,
> mở màn hình theo dõi nấc này là **thấy ngay tiếp điểm nào đang hở** — không cần đọc code, không cần
> biết lập trình.
>
> ⭐ Đây là lý do thật khiến chuỗi cho phép **nên** viết bằng ladder kể cả khi cả chương trình viết
> bằng ST: ⚠ nó là nấc mà **người không lập trình cũng phải đọc được**.
>
> ⚠ Nhưng phần `M_BlockReason` thì **để nguyên ST** — ladder diễn đạt chuỗi `ELSIF` rất tệ. ⭐ Đây là
> ví dụ điển hình của việc **trộn hai ngôn ngữ đúng chỗ** (mục L.18).

> ⭐⭐ **`M_BlockReason` là phần đáng giá nhất của mẫu này.** Không có nó, người vận hành chỉ thấy
> *"máy không chạy"* rồi bắt đầu bấm thử mọi thứ — đó là lúc người ta học được thói quen nhấn bừa.
>
> ⚡ Thứ tự `ELSIF` chính là **thứ tự ưu tiên khi báo**: đặt nguyên nhân gốc lên trước (Chương 44).

---

## L.3 ⚠⚠ Dừng khẩn cấp — và điều PLC KHÔNG được làm

> ⚠⚠ **Dừng khẩn cấp KHÔNG phải là một đoạn code.**
>
> Chức năng dừng khẩn cấp phải do **phần cứng an toàn** thực hiện — rơ-le an toàn hoặc PLC an toàn đã
> chứng nhận — **hoạt động độc lập với CPU chạy chương trình sản xuất** (Chương 47). ⭐ Lý do đơn
> giản: CPU treo thì chương trình chết theo, còn mối nguy thì không.
>
> ⚠ Đoạn dưới **chỉ là phần GIÁM SÁT** — để PLC *biết* mạch an toàn đã cắt mà phản ứng cho gọn. Nó
> **không phải** thứ làm máy an toàn, và **không thay thế** thiết kế an toàn do người có thẩm quyền
> duyệt.

```iecst
// ── PHẦN GIÁM SÁT — không phải chức năng an toàn ──
// DI_EStopOK đến từ TIẾP ĐIỂM PHẢN HỒI CỦA RƠ-LE AN TOÀN, không phải từ nút nhấn.

M_EStopActive := NOT DI_EStopOK;

IF M_EStopActive THEN
    // 1. Bỏ mọi yêu cầu đang treo — để khi phục hồi máy không tự chạy tiếp
    M_CycleEnable   := FALSE;
    M_Running       := FALSE;
    M_Stn1_ClampReq := FALSE;
    M_Stn1_StopReq  := FALSE;

    // 2. Chốt cờ lỗi và ghi nhận MỘT LẦN để truy vết (Chương 44) — gom vào M_AnyFault (Chương 25)
    IF NOT M_Alm_EStop THEN
        M_Alm_EStop := TRUE;
        RaiseAlarm(ALM_ESTOP);
    END_IF;

    // 3. ⚠⚠ Toạ độ trục không còn tin được nếu trục đang chạy (Chương 37, mục 37.3)
    M_Homed := FALSE;
END_IF;

// ── Phục hồi: KHÔNG tự động. Thao tác CÓ CHỦ Ý — nhấn Reset → tầng máy vào Resetting → lệnh xoá ──
IF NOT M_EStopActive AND M_ClearFaults THEN
    M_Alm_EStop := FALSE;            // M_Homed vẫn FALSE → buộc về gốc lại
END_IF;
```

> ⚠⚠ **Ba điều tuyệt đối không làm:**
>
> | | |
> |---|---|
> | 1 | ⭐ **Không** cho máy tự chạy lại khi mạch an toàn đóng lại — khởi động lại phải **có chủ ý** (Chương 47) |
> | 2 | ⭐ **Không** lấy `DI_EStopOK` thẳng từ **nút nhấn** — phải là **phản hồi của rơ-le an toàn** |
> | 3 | ⚠⚠ **Không** coi đoạn code này là đã "làm xong phần an toàn" |

---

## L.4 Ba lệnh dừng — và chúng khác nhau thật sự

⚠ *"Dừng"* là ba thứ khác nhau. Trộn chúng lại là nguồn gốc của rất nhiều tranh cãi lúc nghiệm thu.

| Lệnh | Nghĩa | Sản phẩm đang làm dở |
|---|---|---|
| ⭐ **Dừng cuối chu trình** | Làm nốt cái đang làm rồi mới dừng | ⭐ **Hoàn thành** |
| **Tạm dừng** | Đứng yên tại chỗ, giữ nguyên trạng thái | ⭐ **Giữ nguyên**, chờ tiếp tục |
| ⚠ **Dừng ngay** | Cắt ngay lập tức | ⚠⚠ **Dở dang** — phải có cách xử lý (Chương 28) |

```iecst
// ── Dừng cuối chu trình: chỉ chặn việc BẮT ĐẦU cái mới ──
IF M_StopEocPB_Rise THEN
    M_NoNewCycle := TRUE;               // trình tự đang chạy vẫn chạy nốt
END_IF;

IF M_NoNewCycle AND (Stn1_Step = 0) AND (Stn2_Step = 0) THEN
    M_CycleEnable := FALSE;             // cả hai trạm đã về bước chờ
    M_NoNewCycle  := FALSE;
END_IF;


// ── Tạm dừng: ĐÓNG BĂNG trình tự, KHÔNG xoá trạng thái ──
IF M_PausePB_Rise THEN
    M_Paused := NOT M_Paused;           // một nút bật/tắt
END_IF;

// Trong mỗi trình tự, chặn NGAY ĐẦU bằng một nhánh IF — KHÔNG dùng RETURN (khung L.6):
//     IF M_Paused OR NOT M_CycleEnable THEN ;  ELSE  …thân trình tự…  END_IF;

// ⚠⚠ Nhưng ngõ ra đang GIỮ thì vẫn phải giữ — tạm dừng không được nhả kẹp:
IF M_Paused THEN
    DO_ConvRun := FALSE;                // dừng cái đang DI CHUYỂN
    // M_Stn1_ClampReq GIỮ NGUYÊN — không đụng tới cái đang GIỮ
END_IF;
```

⭐ **Bằng ladder** — cuộn dây chốt `( S )` / `( R )` làm phần "dừng cuối chu trình" rất gọn:

```text
  M_StopEocPB_Rise                                                 M_NoNewCycle
 ────┤ ├───────────────────────────────────────────────────────────────( S )──

  M_NoNewCycle   Stn1_Step=0    Stn2_Step=0                         M_CycleEnable
 ────┤ ├─────────────┤ ├────────────┤ ├─────────────┬───────────────────( R )──
                                                    │               M_NoNewCycle
                                                    └───────────────────( R )──

  M_PausePB_Rise    M_Paused                                            M_Paused
 ────┤ ├──────────────┤/├───────────────────────────────────────────────( S )──
  M_PausePB_Rise    M_Paused
 ────┤ ├──────────────┤ ├────────────────────────────────────────────────( R )──
```

> ⭐ **Nút bật/tắt bằng ladder cần HAI nấc** — một để bật, một để tắt — trong khi ST chỉ cần
> `M_Paused := NOT M_Paused`. ⚠ Nhưng hai nấc ladder **không có bẫy thứ tự quét** mà phép đảo trong
> ST có thể gặp nếu bị gọi hai lần trong một vòng.
>
> ⚠⚠ **Chú ý cặp `( S )` / `( R )`:** phải kiểm hãng của bạn **cuộn nào thắng** khi cả hai cùng
> tích cực trong một vòng quét — Chương 16 mục 16.2. ⭐ Ở đây hai nấc loại trừ nhau bằng chính
> `M_Paused` nên không gặp, nhưng **đừng dựa vào may mắn ở chỗ khác**.

> ⭐⭐ **Điểm quyết định của "tạm dừng": phân biệt ngõ ra CHUYỂN ĐỘNG với ngõ ra ĐANG GIỮ.**
>
> ⚠ Tắt hết mọi ngõ ra khi tạm dừng là lỗi nguy hiểm — ⭐ **kẹp nhả ra thì sản phẩm rơi**, và với trục
> đứng thì đầu công tác rơi theo. Quy tắc: **dừng cái đang di chuyển, giữ nguyên cái đang giữ**
> (Chương 28).
>
> ⚡ Khi **tiếp tục**: ⚠ đừng chạy tiếp ngay. ⭐ Kiểm lại chuỗi cho phép (L.2) trước — trong lúc tạm
> dừng có thể đã có người mở cửa.

---

## L.5 Chu trình: chạy một lần hay tuần hoàn

```iecst
// M_CycleMode: 0 = một lần (single) · 1 = tuần hoàn (continuous)

IF M_StartPB_Rise AND M_AllPermissive THEN
    M_CycleEnable := TRUE;
END_IF;

// ── Khi một chu trình kết thúc ──
IF M_CycleDone_Rise THEN
    CountTotal := CountTotal + 1;

    IF (M_CycleMode = 0) OR M_NoNewCycle OR NOT M_AllPermissive THEN
        M_CycleEnable := FALSE;         // dừng lại, chờ Start lần sau
    END_IF;
    // Tuần hoàn: giữ M_CycleEnable, trình tự tự quay về bước 0
END_IF;
```

> ⭐ **Chỗ dễ sai: phải kiểm lại `M_AllPermissive` ở CUỐI mỗi chu trình**, không chỉ lúc nhấn Start.
> Máy chạy tuần hoàn hàng giờ — ⚠ điều kiện cho phép có thể đã đổi từ lâu mà không ai để ý.
>
> ⚡ Bộ đếm dùng `DINT` và khai là **biến giữ được**; `M_CycleEnable` thì **không giữ** (Chương 16,
> mục 16.4).

---

## L.6 Khung trình tự bước có timeout — dùng cho mọi trạm

```iecst
VAR
    Stn1_StepPrev  : INT;
    T_StepTimeout  : TON;
    Stn1_StepLimit : TIME;
END_VAR

// ── 0. Xoá cờ lỗi của trạm khi tầng máy ra lệnh — đặt NGOÀI cửa vào, vì lúc máy đang
//       Resetting thì trình tự không chạy (Chương 25 mục 25.5c) ──
IF M_ClearFaults THEN
    Stn1.Fault := FALSE;
END_IF;

// ── 1. Một timer dùng chung — gọi ĐÚNG MỘT lần mỗi vòng, NGOÀI cửa vào (Phụ lục B mục B.9b).
//       Bước vừa đổi, hoặc trình tự đang bị giữ → IN = FALSE → timer về 0; chạy tiếp là bước
//       được TRỌN thời gian cho phép (Chương 26 · Chương 17 Bẫy 3, Bẫy 5 · PLCopen CP20) ──
CASE Stn1_Step OF
    0:   Stn1_StepLimit := T#0S;         // 0 = chờ vô hạn, CÓ CHỦ Ý
   10:   Stn1_StepLimit := T#3S;
   20:   Stn1_StepLimit := T#3S;
   30:   Stn1_StepLimit := T#60S;
END_CASE;

T_StepTimeout(IN := M_CycleEnable AND NOT M_Paused
                    AND (Stn1_StepLimit > T#0S) AND (Stn1_Step = Stn1_StepPrev),
              PT := Stn1_StepLimit);
Stn1_StepPrev := Stn1_Step;

IF T_StepTimeout.Q THEN
    Stn1.FaultStep := Stn1_Step;         // ⭐ GHI LẠI bước bị kẹt — không chỉ "lỗi trạm 1"
    Stn1.Fault     := TRUE;              // cờ của TRẠM — không ghi thẳng M_AnyFault (Chương 25 mục 25.5c)
END_IF;

// ── 2. MỘT cửa vào: tạm dừng, hoặc tầng máy chưa cho phép → GIỮ NGUYÊN bước và ngõ ra ──
//    ⚠ Huỷ chu trình KHÔNG làm ở đây. Nó là một chuyển trạng thái riêng ở tầng máy
//      (Hold → Idle, Chương 25), và bước được xoá ở đó — không phải mỗi lần cờ này tắt.
IF M_Paused OR NOT M_CycleEnable THEN
    ;                                    // ⭐ CỐ Ý không làm gì (L.4, Chương 25)
ELSE

    // ── 3. Thân trình tự — chuyển bước bằng PHẢN HỒI THẬT ──
    CASE Stn1_Step OF
      0:  Stn1.Ready := TRUE;
          Stn1.Busy  := FALSE;
          IF DI_BoardStn1 THEN
              Stn1.Ready := FALSE;
              Stn1.Busy  := TRUE;
              Stn1_Step  := 10;
          END_IF;

     10:  M_Stn1_StopReq := TRUE;
          IF DI_Stop1Up THEN   Stn1_Step := 20;  END_IF;    // ⭐ cảm biến, không phải timer

     20:  M_Stn1_ClampReq := TRUE;
          IF DI_Clamp1Up THEN  Stn1_Step := 30;  END_IF;
      // …
    END_CASE;

END_IF;
```

> ⚠⚠ **Cửa vào chỉ GIỮ, không bao giờ XOÁ bước.** Bản trước của khung này đặt `Stn1_Step := 0` mỗi
> khi `M_CycleEnable` tắt — ⚠ trái với chính định nghĩa của cờ đó ở Chương 25 (*"dừng nhưng GIỮ
> nguyên vị trí"*). Theo máy trạng thái Chương 25, cờ tắt mỗi lần vào `Hold`; nên bản cũ khiến
> **mỗi lần Hold, trình tự quay về "chờ board" trong khi kẹp còn đang hạ** — và `Start` không thể
> *"chạy tiếp từ bước đang nhớ"* được nữa.
>
> ⭐ Huỷ chu trình là **một quyết định của tầng máy**, đi qua một chuyển trạng thái có tên
> (`Hold → Idle`), không phải hệ quả phụ của việc một cờ tắt.

> ⭐ **Không có `RETURN` nào trong khung này — có chủ ý.** Bộ quy tắc viết mã của PLCopen (quy tắc
> CP14, mức ưu tiên **cao**, áp cho mọi ngôn ngữ) yêu cầu **mỗi POU chỉ có một điểm thoát**, với lý
> do rất thực dụng: khi gỡ lỗi, bạn thêm một dòng ngay trước điểm kết thúc và **chắc chắn nó chạy
> trong mọi trường hợp**. Với `RETURN` rải ở đầu, dòng đó bị bỏ qua đúng những lần bạn cần nó nhất.
> ⚡ Nhánh rỗng `;` có chú thích là cách chính tài liệu PLCopen dùng để nói *"ở đây cố ý không làm
> gì"* — Phụ lục N.

> ⚠⚠ **Vì sao bộ định thời nằm NGOÀI cửa vào, với điều kiện giữ đưa vào `IN`.** Bản trước của khung
> này gọi nó **bên trong** nhánh `ELSE`, với ý định *"đang giữ thì đóng băng — một bước đang tạm dừng
> không phải bước bị kẹt"*. Ý định đúng, cách làm sai: bộ định thời **không được gọi thì không tạm
> dừng** — nó tính `ET` từ thời điểm bắt đầu theo đồng hồ nền của CPU (Chương 17 mục 17.3, Phụ lục B
> mục B.9b). Giữ máy mười phút ở bước 20 rồi chạy tiếp → lần gọi đầu tiên thấy `ET` = mười phút →
> **báo lỗi bước ngay khi vừa bấm Start**. ⭐ Đưa điều kiện giữ vào `IN` thì đúng ý: đang giữ → timer
> về 0; chạy tiếp → bước được **trọn** thời gian cho phép.

> ⭐⭐ **Hai quy tắc của khung này quan trọng hơn bản thân đoạn code:**
>
> | | |
> |---|---|
> | 1 | ⭐ **Chuyển bước bằng PHẢN HỒI THẬT**, không bằng timer (Chương 17) |
> | 2 | ⭐ **Timer chỉ để BÁO LỖI**, không để chuyển bước (Chương 26) |
>
> ⚡ Đánh số bước **cách 10** để còn chỗ chèn bước mới mà không phải đánh số lại cả trình tự.
>
> ⚠ `T#0S` ở bước 0 là **quyết định có chủ ý** — chờ board từ máy trước không phải lỗi. Nhưng chờ vô
> hạn phải được **giám sát ở tầng trên** bằng một cảnh báo *"máy đứng chờ"* (Chương 26, Chương 27).

---

## L.7 Bắt cạnh, làm đúng một lần, chống rung

```iecst
VAR
    R_Start    : R_TRIG;                 // ⚠ MỖI tín hiệu một thể hiện RIÊNG
    R_Reset    : R_TRIG;
    R_Board    : R_TRIG;
    T_Debounce : TON;
END_VAR

R_Start(CLK := DI_StartPB);
M_StartPB_Rise := R_Start.Q AND NOT M_FirstScan;   // MỘT vòng quét — trừ vòng đầu (Chương 16 Bẫy 9)

R_Reset(CLK := DI_ResetPB);
M_ResetPB_Rise := R_Reset.Q AND NOT M_FirstScan;

// ── Chống rung TRƯỚC, bắt cạnh SAU — thứ tự này bắt buộc ──
T_Debounce(IN := DI_BoardStn1, PT := T#20MS);
R_Board(CLK := T_Debounce.Q);
M_BoardArrived := R_Board.Q;
```

⭐ **Bằng ladder** — tiếp điểm bắt cạnh `┤P├` và khối `TON` vẽ thành hộp:

```text
  DI_StartPB                                                      M_StartPB_Rise
 ────┤P├────────────────────────────────────────────────────────────────( )───

  DI_BoardStn1        ┌──────────────────┐
 ────┤ ├──────────────┤ IN   T_Debounce Q├──┤P├──────────────────( )───
                      │ T#20MS        PT │                   M_BoardArrived
                      └──────────────────┘
```

| Ký hiệu | Nghĩa |
|---|---|
| `┤P├` | ⭐ **Tiếp điểm bắt cạnh LÊN** — thông đúng một vòng quét khi bit đổi 0→1 |
| `┤N├` | Tiếp điểm bắt cạnh **xuống** |
| Hộp có `IN`/`PT`/`Q` | Khối chức năng đặt **giữa** nấc thang |

> ⭐⭐ **Ở ladder, thứ tự "lọc rung TRƯỚC, bắt cạnh SAU" là thứ nhìn thấy được** — hộp `TON` nằm bên
> trái, `┤P├` nằm bên phải. ⚡ Đảo hai cái là nhìn thấy ngay, khác hẳn bản ST nơi hai dòng đứng cạnh
> nhau và đổi chỗ trông vẫn hợp lý.
>
> ⚠ **Nhưng ladder giấu một thứ mà ST nói rõ:** mỗi hộp là **một thể hiện riêng**. Chép nấc thang
> này rồi dán mà quên đổi tên hộp thì ⚠⚠ **hai tín hiệu dùng chung một timer** — Chương 14 mục 14.3.

> ⚠⚠ **Đảo thứ tự là một lần nhấn ra nhiều xung.** Lọc rung phải đứng **trước** bắt cạnh
> (Chương 16 Bẫy 8).
>
> ⚠ **Mỗi tín hiệu một thể hiện `R_TRIG` riêng.** Dùng chung một thể hiện cho hai tín hiệu thì
> ⭐ **hai tín hiệu ghi đè bộ nhớ trạng thái của nhau** — lỗi cùng loại với Chương 14 mục 14.3.

> ⚠⚠ **Sườn ở vòng quét đầu là sườn giả** khi tín hiệu đã bằng 1 từ trước lúc bật máy — nút kẹt,
> board đang che cảm biến. Hai nút ở trên được che bằng `M_FirstScan` — cờ khai `BOOL := TRUE`, đặt về
> FALSE ở dòng cuối chương trình chính (Chương 57). ⚠ Với `M_BoardArrived` thì cờ này **không đủ**,
> vì bộ lọc rung làm sườn giả tới muộn — Chương 16 Bẫy 9.

---

## L.8 Cơ cấu hai vị trí — khối dùng lại cho mọi xy-lanh

⭐ **Viết một lần, dùng cho mọi xy-lanh trên máy.** Đây là tầng **cơ cấu** ở Chương 27, và là ví dụ
điển hình của việc chuẩn hoá ở Chương 30. ⭐ Đây là **đúng cùng một khối** với Chương 27 mục 27.3 —
lý do của từng quyết định thiết kế nằm ở đó; ở đây là bản để chép.

```iecst
// ✔ VÍ DỤ HOÀN CHỈNH — khối xy-lanh hai vị trí (giống hệt Chương 27 mục 27.3)
FUNCTION_BLOCK FB_Cylinder2Pos
VAR_INPUT
    Req       : BOOL;            // TRUE = yêu cầu tới vị trí LÀM VIỆC — giữ mức, không phải xung
    Permit    : BOOL;            // tầng máy cho phép ĐỔI vị trí — ⚠ không phải Enable kiểu PLCopen
    Reset     : BOOL;            // xoá lỗi đã chốt — nối lệnh xoá M_ClearFaults (Chương 25)
    SensWork  : BOOL;            // cảm biến báo đã tới vị trí làm việc
    SensHome  : BOOL;            // cảm biến báo đã về vị trí gốc
    Limit     : TIME := T#3S;    // thời gian tối đa cho một hành trình
END_VAR
VAR_OUTPUT
    Valve     : BOOL;            // lệnh ra van  ← chỉ khối này quyết định
    Done      : BOOL;            // đã tới ĐÚNG vị trí đang được yêu cầu
    Unknown   : BOOL;            // giữa chừng: cả hai cảm biến cùng tắt
    Fault     : BOOL;            // đã chốt: quá thời gian, hoặc hai cảm biến cùng báo
    FaultCode : INT;             // 0 = không lỗi · 1 = quá thời gian · 2 = hai cảm biến cùng báo
END_VAR
VAR
    T_Move    : TON;
    ValvePrev : BOOL;
    AtTarget  : BOOL;            // xy-lanh đang ở đúng chỗ mà VAN đang đẩy nó tới
END_VAR

// ── 1. Lệnh ra van: CHỈ đổi khi được phép. Mất phép → GIỮ nguyên, không "về lò xo" (Ch.27 Bẫy 7)
IF Permit THEN
    Valve := Req;
END_IF;

// ── 2. Tới đích chưa — kiểm cảm biến ĐÍCH, không suy từ cảm biến kia (Chương 28, Bẫy 1)
AtTarget := (Valve AND SensWork) OR (NOT Valve AND SensHome);
Done     := (Req = Valve) AND AtTarget;     // chưa được phép đổi thì CHƯA xong
Unknown  := NOT SensWork AND NOT SensHome;

// ── 3. Xoá lỗi TRƯỚC khi kiểm lại: nguyên nhân còn thì lỗi chốt lại ngay trong vòng này
IF Reset THEN
    Fault     := FALSE;
    FaultCode := 0;
END_IF;

// ── 4. Quá thời gian: đếm lại từ đầu mỗi khi lệnh van đổi — gọi T_Move đúng MỘT lần
T_Move(IN := NOT AtTarget AND (Valve = ValvePrev), PT := Limit);
ValvePrev := Valve;
IF T_Move.Q THEN
    Fault     := TRUE;
    FaultCode := 1;                         // ⭐ chỉ BÁO — phản ứng là việc của tầng máy
END_IF;

// ── 5. Hai cảm biến cùng báo: vô lý về vật lý → chắc chắn hỏng
IF SensWork AND SensHome THEN
    Fault     := TRUE;
    FaultCode := 2;
END_IF;
END_FUNCTION_BLOCK
```

⭐ **Gọi khối này từ ladder** trông như sau — mỗi xy-lanh một hộp, mỗi hộp một tên:

```text
                                 Clamp1
                      ┌────────────────────────┐
                      │    FB_Cylinder2Pos     │
   M_Stn1_ClampReq    │                        │   DO_Clamp1Vlv
 ────┤ ├──────────────┤ Req              Valve ├────────( )───
   M_MotionEnable     │                        │   M_Clamp1Done
 ────┤ ├──────────────┤ Permit            Done ├────────( )───
   M_ClearFaults      │                        │   M_Clamp1Fault
 ────┤ ├──────────────┤ Reset            Fault ├────────( )───
   DI_Clamp1Up        │                        │
 ────┤ ├──────────────┤ SensWork     FaultCode ├
   DI_Clamp1Dn        │                        │
 ────┤ ├──────────────┤ SensHome       Unknown ├
        T#3S ─────────┤ Limit                  │
                      └────────────────────────┘
```

> ⭐ **Đây là hình dạng quen thuộc nhất với thợ bảo trì:** một hộp có tên, chân trái là lệnh vào,
> chân phải là phản hồi ra. ⚡ Không cần biết bên trong hộp viết bằng gì — và thực tế **bên trong
> nên viết bằng ST**, vì nó có timer, so sánh và mã lỗi (mục L.19). Chân `FaultCode` và `Unknown`
> không cần nối — đọc bằng tên khi cần: `Clamp1.FaultCode`.
>
> ⭐⭐ **Một hộp một tên** — `Stop1`, `Clamp1`, `Stop2`, `Clamp2`: tên **thể hiện** ghi trên hộp, tên
> **kiểu** `FB_Cylinder2Pos` ghi trong hộp. ⚠ Đừng đặt tiền tố `FB_` cho thể hiện — tiền tố đó dành
> cho **kiểu** (Phụ lục N, N10). Hai xy-lanh dùng chung một tên hộp là lỗi cùng loại với dùng chung
> `R_TRIG` ở L.7.

> ⭐⭐ **Phép kiểm "cả hai cảm biến cùng báo" là thứ đáng giá nhất trong khối này.** Về mặt vật lý nó
> **không thể xảy ra** — nên khi nó xảy ra thì chắc chắn có hỏng hóc. ⚡ Đây là cách rẻ nhất để
> **làm cho hỏng hóc trở nên phát hiện được** (Chương 48).
>
> ⚠ Đừng quên tư thế **giữa chừng**: cả hai cảm biến cùng **bằng 0** là bình thường khi đang di
> chuyển — và cũng là trạng thái sau khi **mất khí**. ⭐ Vì vậy **không được suy tư thế từ cảm biến
> đối diện** (Chương 28).

---

## L.8b ⭐ Khối kích bằng sườn — khung `Execute` / `Done` tự viết

⭐ Khung cho **mọi việc có điểm kết thúc** mà bạn muốn đóng gói thành khối: chuyển một board, chạy một
chu trình con, đọc một thanh ghi. Viết theo đúng năm quy tắc chung của PLCopen để người gọi dùng nó
**y như khối của hãng** — lý do và bảng quy tắc ở Chương 30 mục 30.5b; ở đây là bản để chép.

```iecst
// ✔ VÍ DỤ HOÀN CHỈNH — khối kích bằng sườn theo hợp đồng Execute/Done (giống hệt Chương 30 mục 30.5b)
FUNCTION_BLOCK FB_BoardTransfer
VAR_INPUT
    Execute   : BOOL;            // ⭐ SƯỜN LÊN = bắt đầu · tham số được CHỐT tại sườn này
    Arrived   : BOOL;            // "đã tới nơi" — board tới chặn, hoặc đã rời trạm, tuỳ chỗ gọi
    TimeOut   : TIME := T#10S;   // thời gian tối đa cho một lần chuyển
END_VAR
VAR_OUTPUT
    Busy      : BOOL;            // ⭐ Busy · Done · Error LOẠI TRỪ nhau
    Done      : BOOL;
    Error     : BOOL;
    ErrorID   : INT;             // 0 = không lỗi · 1 = quá thời gian
    ConvReq   : BOOL;            // xin tầng máy chạy chuyền — chuyền là tài nguyên chung (Chương 27)
END_VAR
VAR
    ExecEdge  : R_TRIG;
    T_Out     : TON;
    LimitCopy : TIME;            // bản CHỐT của TimeOut
END_VAR
VAR_TEMP
    Start     : BOOL;            // vòng này vừa NHẬN một lệnh mới
    NewResult : BOOL;            // kết quả vừa có trong vòng này
END_VAR

ExecEdge(CLK := Execute);

// ── 1. Sườn lên khi đang rỗi → nhận lệnh, CHỐT tham số. Sườn lên khi đang bận → bỏ qua ──
Start := ExecEdge.Q AND NOT Busy;
IF Start THEN
    Busy      := TRUE;
    Done      := FALSE;
    Error     := FALSE;
    ErrorID   := 0;
    LimitCopy := TimeOut;
END_IF;

// ── 2. Đang bận: chờ tới nơi, giám sát thời gian. T_Out gọi đúng MỘT lần, về 0 ở vòng nhận lệnh ──
T_Out(IN := Busy AND NOT Start, PT := LimitCopy);
IF Busy AND Arrived THEN
    Busy      := FALSE;
    Done      := TRUE;
    NewResult := TRUE;
ELSIF Busy AND T_Out.Q THEN
    Busy      := FALSE;
    Error     := TRUE;
    ErrorID   := 1;
    NewResult := TRUE;
END_IF;
ConvReq := Busy;                 // ngõ ra suy ra SAU khi trạng thái đã cập nhật

// ── 3. Execute đã tắt và việc đã xong → xoá kết quả. Kết quả VỪA có thì vẫn hiện
//       ít nhất MỘT vòng, kể cả khi Execute đã tắt từ giữa chừng ──
IF NOT Execute AND NOT Busy AND NOT NewResult THEN
    Done    := FALSE;
    Error   := FALSE;
    ErrorID := 0;
END_IF;
END_FUNCTION_BLOCK
```

> ⭐ **Đổi thân, giữ khung.** Muốn làm việc khác thì thay phần 2 — điều kiện tới nơi và ngõ ra xin
> tài nguyên — bằng việc của bạn. ⚠ Giữ nguyên phần 1 và phần 3: chúng là **hợp đồng** với bên gọi.
>
> ⚠ Gọi khối **mỗi vòng quét, ngoài `CASE`**, với `Execute` lấy từ bước (Chương 30 mục 30.5b). Gọi
> bên trong một nhánh `CASE` thì rời bước là khối **đứng yên** — quy tắc 2 bị phá.

---

## L.9 Servo — cấp mô-men, về gốc, di chuyển

⭐ Mẫu theo **PLCopen Motion**; tên khối `MC_*` giống nhau ở phần lớn hệ, nên đây là chỗ kỹ năng
chuyển được giữa các hãng nhiều nhất (Chương 37, mục 37.8).

```iecst
VAR
    PwrZ     : MC_Power;
    HomeZ    : MC_Home;
    MoveZ    : MC_MoveAbsolute;
    StopZ    : MC_Stop;
    ResetZ   : MC_Reset;
    TrigHome : R_TRIG;
    TrigMove : R_TRIG;
    AxZ_Step : INT;
END_VAR

// ── 1. Cấp mô-men: GỌI MỖI VÒNG QUÉT, chỉ đổi chân Enable ──
PwrZ(Axis   := AX_Z,
     Enable := M_AllPermissive AND NOT M_EStopActive,
     Status => M_ZPowered);

// ── 2. Execute kích bằng CẠNH LÊN — sinh từ chính bước đang chạy ──
TrigHome(CLK := (AxZ_Step = 10));
TrigMove(CLK := (AxZ_Step = 30));

HomeZ(Axis := AX_Z, Execute := TrigHome.Q,
      Done  => M_ZHomeDone,
      Error => M_ZHomeError);

MoveZ(Axis     := AX_Z, Execute := TrigMove.Q,
      Position := RecipeDispenseHeightX100,
      Velocity := ZVelocity,
      Done           => M_ZMoveDone,
      CommandAborted => M_ZMoveAborted,   // ⚠⚠ KHÔNG được bỏ qua
      Error          => M_ZMoveError);

StopZ (Axis := AX_Z, Execute := (AxZ_Step = 90));
ResetZ(Axis := AX_Z, Execute := M_ClearFaults);    // sườn lên của lệnh xoá (Chương 25 mục 25.5c)

// ── 3. Máy trạng thái của trục ──
CASE AxZ_Step OF

  0:  M_Homed := FALSE;
      IF M_ZPowered THEN  AxZ_Step := 10;  END_IF;

 10:  // Về gốc — BẮT BUỘC sau mỗi lần mất điện với encoder gia số
      IF M_ZHomeDone THEN
          M_Homed  := TRUE;               // ⚠⚠ biến KHÔNG giữ qua mất điện (mục 37.3)
          AxZ_Step := 20;
      ELSIF M_ZHomeError THEN
          AxZ_Step := 90;
      END_IF;

 20:  IF M_ZMoveReq AND M_Homed THEN  AxZ_Step := 30;  END_IF;

 30:  IF M_ZMoveDone THEN
          M_ZMoveReq := FALSE;
          AxZ_Step   := 20;
      ELSIF M_ZMoveError OR M_ZMoveAborted THEN
          AxZ_Step := 90;
      END_IF;

 90:  M_Homed := FALSE;                   // toạ độ không còn tin được
      IF M_ClearFaults THEN  AxZ_Step := 0;  END_IF;    // tầng máy ra lệnh xoá
END_CASE;

// ⭐ Cờ lỗi của trục CHÍNH LÀ bước 90 — không cần cờ chốt riêng; gom vào M_AnyFault (Chương 25)
M_Alm_AxisZ := (AxZ_Step = 90);
```

> ⭐⭐ **Bốn điều hay sai nhất với servo:**
>
> | | |
> |---|---|
> | 1 | ⚠ **Giữ `Execute` ở mức TRUE.** Lệnh kích bằng **cạnh lên** — giữ mức thì lần sau không phát được (Chương 37, Bẫy 7) |
> | 2 | ⚠⚠ **Bỏ qua `CommandAborted`.** Lệnh bị lệnh khác chen ngang: trục **không tới nơi** mà trình tự vẫn ngồi chờ `Done` → treo |
> | 3 | ⭐ **Không kiểm `M_Homed`** trước lệnh tuyệt đối. Sau mất điện, toạ độ **vô nghĩa** (Chương 37, mục 37.3) |
> | 4 | ⚠ **Gọi `MC_Power` có điều kiện.** Phải gọi **mỗi vòng quét**, chỉ đổi chân `Enable` |
>
> ⚡ **Vẫn cần timeout song song.** `Error` bắt được lỗi mà drive báo; timeout bắt được trường hợp
> **không có gì xảy ra cả** (Chương 17, mục 17.4). Dùng khung ở L.6 cho `AxZ_Step`.
>
> ⚠⚠ **STO không phải `MC_Stop`.** Dừng an toàn của truyền động là **chức năng phần cứng** của drive
> (Chương 47); `MC_Stop` chỉ là lệnh dừng thông thường.

---

## L.9b ⭐ Hai đầu chung một ray — kiểm khoảng hở theo ĐÍCH và theo QUÃNG DỪNG

⭐ **Dùng khi:** hai cụm trục chạy chung một vùng làm việc — hai đầu công tác trên một ray, hai giàn
đối diện nhau. Hai trục đưa về **một hệ toạ độ máy** trước, đầu 1 ở bên trái, đầu 2 ở bên phải
(Chương 37 mục 37.7b).

```iecst
// ✔ VÍ DỤ HOÀN CHỈNH — khoảng hở hai đầu chung một ray (giống hệt Chương 37 mục 37.7b)
FUNCTION_BLOCK FB_TwoHeadsGap
VAR_INPUT
    X1Act   : REAL;          // đầu 1 (bên trái): vị trí thật, mm, theo hệ toạ độ MÁY
    X1Tgt   : REAL;          // đầu 1: đích đang lệnh hoặc sắp lệnh — đứng yên thì bằng X1Act
    X2Act   : REAL;          // đầu 2 (bên phải): vị trí thật, mm
    X2Tgt   : REAL;          // đầu 2: đích
    V1Act   : REAL;          // tốc độ thật đầu 1, mm/s, dương = đi sang phải
    V2Act   : REAL;          // tốc độ thật đầu 2, mm/s, dương = đi sang phải
    GapMin  : REAL;          // khoảng hở tối thiểu, mm — kích thước hai thân + biên (mục 37.7b)
    DecStop : REAL;          // gia tốc hãm của lệnh dừng, mm/s² — giá trị NHỎ hơn của hai trục
    TReact  : REAL;          // thời gian phản ứng, s — [Nghề] 3 chu kỳ của tác vụ chạy khối này
END_VAR
VAR_OUTPUT
    PathClear : BOOL;        // ⭐ hai đoạn đường đi theo ĐÍCH không chồng nhau → được phát lệnh
    StopBoth  : BOOL;        // ⚠ khoảng hở HIỆN TẠI không còn đủ để dừng kịp → dừng cả hai
    GapNow    : REAL;        // khoảng hở hiện tại, mm — để hiển thị và ghi mốc
    GapNeed   : REAL;        // khoảng hở cần có ở tốc độ hiện tại, mm
END_VAR
VAR_TEMP
    Close1  : REAL;          // tốc độ đầu 1 tiến VỀ PHÍA đầu 2, mm/s, không âm
    Close2  : REAL;          // tốc độ đầu 2 tiến về phía đầu 1, mm/s, không âm
END_VAR

// ── 1. Kiểm ĐÍCH — dùng lúc RA LỆNH: mỗi đầu chiếm cả đoạn từ chỗ đang đứng tới đích ──
PathClear := (MAX(X1Act, X1Tgt) + GapMin <= MIN(X2Act, X2Tgt)) AND (DecStop > 0.0);

// ── 2. Kiểm HIỆN TẠI — liên tục: khoảng hở phải đủ cho cả quãng phản ứng lẫn quãng phanh ──
GapNow := X2Act - X1Act;
Close1 := MAX(V1Act, 0.0);       // đầu 1 đi sang phải là đi VỀ PHÍA đầu 2
Close2 := MAX(-V2Act, 0.0);      // đầu 2 đi sang trái là đi về phía đầu 1
IF DecStop > 0.0 THEN
    GapNeed  := GapMin
              + (Close1 + Close2) * TReact                               // quãng phản ứng
              + (Close1 * Close1 + Close2 * Close2) / (2.0 * DecStop);   // quãng phanh của từng đầu
    StopBoth := GapNow < GapNeed;
ELSE
    GapNeed  := GapMin;
    StopBoth := TRUE;            // ⚠ thiếu gia tốc hãm → không biết dừng mất bao xa → coi là không an toàn
END_IF;
END_FUNCTION_BLOCK
```

> ⭐⭐ **Hai phép kiểm, hai thời điểm — và đó là toàn bộ ý của mẫu:**
>
> | | |
> |---|---|
> | 1 | ⭐ `PathClear` — dùng **lúc ra lệnh**: đích mới chỉ được phát khi hai đoạn đường đi không chồng nhau. ⚠ Đừng biến nó thành một báo động kiểm liên tục: đích vi phạm thì báo động **đứng mãi** và trục không đi ra được |
> | 2 | ⭐ `StopBoth` — kiểm **liên tục**: khoảng hở hiện tại phải đủ cho quãng phản ứng **và** quãng phanh ở tốc độ đang chạy. Đứng yên sát nhau thì **không** báo — làm việc gần nhau vẫn được phép |
> | 3 | ⚠ Gia tốc hãm là **giá trị của lệnh dừng bạn đặt**, không phải gia tốc lớn nhất của động cơ; thiếu tham số này thì khối coi là **không an toàn** |
>
> ⚠⚠ **Tầng này bảo vệ máy, không bảo vệ người** — nó chạy trong CPU thường (Chương 27 mục 27.3b).

---

## L.10 Đảo chiều có khoá chéo · sao–tam giác

```iecst
// ── Đảo chiều: khoá chéo BA lớp ──
// Lớp 1 — trong code
M_MotorFwd := M_FwdReq AND NOT M_RevReq AND NOT M_MotorRev AND M_AllPermissive;
M_MotorRev := M_RevReq AND NOT M_FwdReq AND NOT M_MotorFwd AND M_AllPermissive;

// Lớp 2 — khoảng chết khi đổi chiều, để hồ quang tắt hẳn
// Lớp 3 — ⭐⭐ KHOÁ CƠ KHÍ giữa hai contactor, ngoài tủ. BẮT BUỘC CÓ.
```

```iecst
// ── Sao–tam giác ──
VAR
    T_Star  : TON;
    T_Dead  : TON;
    SD_Step : INT;
END_VAR

// ⭐ Timer của từng bước gọi NGOÀI CASE, mỗi cái đúng MỘT lần: IN lấy thẳng từ bước, nên
//    rời bước là timer tự xoá — không cần gọi lần hai với IN := FALSE (Chương 17, Bẫy 5)
T_Star(IN := (SD_Step = 10), PT := T_StarTime);      // chạy kiểu sao
T_Dead(IN := (SD_Step = 20), PT := T#80MS);          // ⚠⚠ KHOẢNG CHẾT

// ⭐ Lệnh dừng có hiệu lực ở MỌI bước — không chỉ khi đã sang tam giác
IF NOT M_MotorStart OR NOT M_AllPermissive THEN
    SD_Step := 0;
END_IF;

CASE SD_Step OF
  0:  IF M_MotorStart AND M_AllPermissive THEN
          SD_Step := 10;
      END_IF;

 10:  IF T_Star.Q THEN
          SD_Step := 20;                             // sang khoảng chết
      END_IF;

 20:  IF T_Dead.Q THEN
          SD_Step := 30;
      END_IF;

 30:  ;                                              // chạy tam giác — dừng xử lý ở trên
END_CASE;

// ⭐ Ngõ ra SUY RA TỪ BƯỚC, và đặt SAU khối CASE — để đổi bước là ngõ ra đổi NGAY
// trong cùng vòng quét, không trễ một vòng.
M_KM_Main  := (SD_Step >= 10);
M_KM_Star  := (SD_Step  = 10);
M_KM_Delta := (SD_Step  = 30);
```

⭐ **Khoá chéo bằng ladder** — đây là mẫu ladder kinh điển nhất, và lý do nó kinh điển là
**tiếp điểm khoá chéo nhìn thấy được**:

```text
   M_FwdReq      M_RevReq     M_MotorRev   M_AllPermissive          M_MotorFwd
 ────┤ ├───────────┤/├───────────┤/├────────────┤ ├────────────────────( )───

   M_RevReq      M_FwdReq     M_MotorFwd   M_AllPermissive          M_MotorRev
 ────┤ ├───────────┤/├───────────┤/├────────────┤ ├────────────────────( )───
```

> ⭐⭐ **Đọc chéo hai nấc là thấy ngay khoá chéo:** nấc trên có `┤/├` của `M_MotorRev`, nấc dưới có
> `┤/├` của `M_MotorFwd`. ⚡ Thiếu một trong hai là **nhìn ra được bằng mắt** — trong bản ST thì
> phải đọc kỹ từng vế.
>
> ⚠⚠ **Nhắc lại lần nữa vì nó quan trọng:** hai nấc này là **lớp 1**. Vẫn phải có **khoảng chết**
> (lớp 2) và ⭐⭐ **khoá CƠ KHÍ giữa hai contactor** (lớp 3). Ladder đẹp không cứu được tiếp điểm
> hàn dính.

> ⚠⚠ **Bỏ khoảng chết ở bước 20 là ngắn mạch pha.** Contactor sao chưa nhả hẳn mà contactor tam giác
> đã đóng → ⭐ **nổ contactor**. Đây là lỗi **không được phép xảy ra lần nào**, nên khoảng chết phải
> lấy theo thời gian nhả **ghi trong datasheet contactor**, không lấy theo cảm tính.
>
> ⭐⭐ **Khoá chéo trong code KHÔNG đủ.** Phải có **khoá cơ khí** giữa hai contactor — vì tiếp điểm có
> thể **hàn dính**, và lúc đó code không biết gì (Chương 3, Chương 48).

---

## L.11 Báo động có xác nhận, và "báo động đầu tiên"

```iecst
// ── Một báo động: XOÁ (khi được lệnh VÀ nguyên nhân đã hết) · rồi mới PHÁT HIỆN · CHỐT ──
IF M_ClearFaults AND DI_AirOK THEN          // lệnh xoá đến từ tầng máy — Chương 25 mục 25.5c
    M_Alm_AirLow := FALSE;
END_IF;
IF NOT DI_AirOK AND NOT M_Alm_AirLow THEN
    M_Alm_AirLow := TRUE;                    // chốt lại, không tự mất
    RaiseAlarm(ALM_AIR_LOW);
END_IF;

// ── Báo động ĐẦU TIÊN trong một chuỗi — gần như luôn là nguyên nhân gốc ──
IF NOT M_AnyAlarmActive AND M_NewAlarm THEN
    FirstAlarmCode := NewAlarmCode;
    FirstAlarmTime := CurrentTime;
END_IF;

// ── GOM — đúng MỘT chỗ gán M_AnyFault (Chương 25 mục 25.5c) ──
M_AnyAlarmActive := M_Alm_EStop OR M_Alm_AirLow OR M_Alm_VisionNoAnswer OR M_Alm_AxisZ;
M_AnyFault       := M_AnyAlarmActive
                    OR Stop1.Fault OR Clamp1.Fault OR Stop2.Fault OR Clamp2.Fault
                    OR Stn1.Fault OR Stn2.Fault;

IF NOT M_AnyAlarmActive THEN
    FirstAlarmCode := ALM_NONE;              // hết sạch mới xoá
END_IF;
```

> ⭐⭐ **`FirstAlarmCode` là thứ giúp người bảo trì nhiều nhất.** Một sự cố thường kéo theo năm báo
> động; ⚠ cái xuất hiện **đầu tiên** mới là nguyên nhân, bốn cái sau là hậu quả (Chương 44).
>
> ⚠ **Không cho xoá khi nguyên nhân còn đó.** Nếu không, người vận hành sẽ bấm Reset cho im rồi
> quên mất — và hệ báo động biến thành tiếng ồn.
>
> ⭐ **Mỗi nguồn một cờ, gom ở một chỗ.** Không nguồn nào ghi thẳng `M_AnyFault` — nó chỉ được **gán**
> ở dòng gom trên. Hai nơi cùng ghi một cờ thì phép gán chạy sau **xoá mất** lỗi của phép chạy trước
> (Chương 25 mục 25.5c).
>
> ⚡ Một dòng báo động đủ dùng phải nói **bước nào · đang chờ gì · nên kiểm tra gì**, không phải
> *"Lỗi trạm 1"* (Chương 26, Chương 44).

---

## L.12 Analog: bốn bước, đúng thứ tự

⭐ Mẫu rút gọn của Chương 32 mục 32.9, áp cho `AI_AirPress`.

```iecst
VAR CONSTANT
    RAW_MAX          : DINT := 27648;   // ứng 20 mA — ⚠⚠ TRA DATASHEET MODULE
    PRESS_MAX_X100   : DINT := 1000;    // 10,00 bar — hết dải cảm biến
    RAW_WIRE_BREAK   : DINT := -2000;   // dưới ~3,6 mA — ⚠ TRA DATASHEET
    RAW_OVER_RANGE   : DINT := 29000;   // trên ~21 mA
    AIR_LOW_ON_X100  : DINT := 450;     // báo khi TỤT dưới 4,50 bar
    AIR_LOW_OFF_X100 : DINT := 500;     // chỉ hết khi LÊN quá 5,00 bar
    FILT_K           : DINT := 20;      // lọc nhẹ — CHỈ cho hiển thị
END_VAR

// ── 1. PHÁT HIỆN NGOÀI DẢI TRƯỚC — chưa hợp lệ thì chưa quy đổi ──
IF RawAirPress < RAW_WIRE_BREAK THEN
    M_AirPressFault := TRUE;  M_AirPressFaultCode := 1;    // đứt dây / mất nguồn cảm biến
ELSIF RawAirPress > RAW_OVER_RANGE THEN
    M_AirPressFault := TRUE;  M_AirPressFaultCode := 2;    // chập / quá dải
ELSE
    M_AirPressFault := FALSE; M_AirPressFaultCode := 0;

    // ── 2. Quy đổi: NHÂN TRƯỚC, CHIA SAU, dùng DINT ──
    AirPressX100 := (RawAirPress * PRESS_MAX_X100) / RAW_MAX;

    // ── 3. Lọc — CHỈ cho hiển thị và ghi log ──
    AirPressFiltX100 := AirPressFiltX100
                      + (FILT_K * (AirPressX100 - AirPressFiltX100)) / 100;
END_IF;

// ── 4. Ngưỡng CÓ VÙNG CHẾT, dùng giá trị CHƯA LỌC ──
IF M_AirPressFault THEN
    M_AirLow := FALSE;                                     // mất phép đo ≠ áp thấp
ELSIF AirPressX100 < AIR_LOW_ON_X100 THEN
    M_AirLow := TRUE;
ELSIF AirPressX100 > AIR_LOW_OFF_X100 THEN
    M_AirLow := FALSE;
END_IF;
```

> ⭐⭐ **Thứ tự bốn bước này không đổi được.** Quy đổi trước khi kiểm hợp lệ nghĩa là ⚠ **bạn đang quy
> đổi một giá trị vô nghĩa thành một con số trông rất hợp lý** (Chương 31, Chương 32).
>
> ⚠ **Ngưỡng báo động dùng giá trị CHƯA lọc.** Bộ lọc thêm trễ, và trễ đó cộng vào chuỗi trễ của cả
> máy (Chương 32, mục 32.6). Lọc là để mắt người đọc dễ chịu, không phải để ra quyết định.
>
> ⚠ **Hai ngưỡng khác nhau**, không phải một. Một ngưỡng thì báo động sẽ **nhấp nháy** khi giá trị dao
> động quanh nó.
>
> ⚠⚠ **`RAW_MAX` là con số đầu tiên phải tra.** `27648` chỉ là một ví dụ thường gặp; nhiều hệ dùng
> `32767`, `4095` hoặc số khác (Chương 32, Bẫy 4).

---

## L.13 Đèn tháp và nháy — mỗi lúc nói đúng một thứ

```iecst
VAR
    T_Blink : TON;
END_VAR

// ── Nhịp nháy 1 Hz dùng chung cho cả máy ──
T_Blink(IN := NOT T_Blink.Q, PT := T#500MS);
IF T_Blink.Q THEN
    M_Blink := NOT M_Blink;
END_IF;

// ── Đèn tháp: ưu tiên từ trên xuống, MỖI LÚC CHỈ MỘT màu ──
DO_LampRed    := M_AnyFault;
DO_LampYellow := NOT M_AnyFault AND (M_Paused OR M_NoNewCycle OR (M_ForceActive AND M_Blink));
DO_LampGreen  := NOT M_AnyFault AND NOT M_Paused AND M_Running;
DO_Buzzer     := M_AnyFault AND NOT M_AlarmAcked;
```

⭐ **Bằng ladder** — bốn nấc, mỗi đèn một nấc, và đọc được từ xa:

```text
   M_AnyFault                                                        DO_LampRed
 ────┤ ├────────────────────────────────────────────────────────────────( )───

   M_AnyFault    M_Paused                                       DO_LampYellow
 ────┤/├───┬───────┤ ├───────────────────────────────────────┬───────( )───
           │   M_NoNewCycle                                  │
           ├───────┤ ├───────────────────────────────────────┤
           │  M_ForceActive   M_Blink                        │
           └───────┤ ├──────────┤ ├──────────────────────────┘

   M_AnyFault    M_Paused     M_Running                          DO_LampGreen
 ────┤/├───────────┤/├───────────┤ ├────────────────────────────────────( )───

   M_AnyFault   M_AlarmAcked                                         DO_Buzzer
 ────┤ ├────────────┤/├─────────────────────────────────────────────────( )───
```

> ⭐ **Ngõ ra cuối cùng là chỗ ladder đáng dùng nhất trong cả phụ lục này.** ⚡ Khi máy có sự cố,
> người đầu tiên mở chương trình thường là thợ bảo trì — và họ sẽ tìm **nấc thang điều khiển cái
> đèn đang sáng sai**. ⭐ Bốn nấc ở trên tìm ra trong mười giây; bốn dòng ST thì phải biết tìm ở đâu.

> ⭐ **Đèn vàng nháy khi còn cưỡng bức I/O** là mẹo rẻ nhất chống quên gỡ force: nó biến một trạng
> thái **ẩn trong phần mềm** thành thứ **nhìn thấy được từ đầu kia xưởng** (Chương 51).
>
> ⚠ **Mỗi lúc chỉ một màu.** Ba đèn cùng sáng thì người vận hành không đọc được gì, và đèn tháp mất
> hết tác dụng.

---

## L.14 Đếm sản lượng — con số phải đúng nghĩa

```iecst
// ── Đếm ở nơi sản phẩm RỜI MÁY ĐÃ XONG, không đếm ở đầu vào ──
IF M_BoardOutfeed_Rise THEN
    IF M_LastResultOk THEN
        CountOk := CountOk + 1;
    ELSE
        CountNg := CountNg + 1;
    END_IF;
END_IF;

// ── Tỉ lệ đạt — ⚠⚠ LUÔN kiểm mẫu số ──
CountTotal := CountOk + CountNg;
IF CountTotal > 0 THEN
    YieldPctX10 := (CountOk * 1000) / CountTotal;   // đơn vị 0,1 %
ELSE
    YieldPctX10 := 0;                               // đầu ca, chưa có sản phẩm nào
END_IF;
```

> ⚠⚠ **Đầu ca `CountTotal` bằng 0.** Không có nhánh `ELSE` thì đây là **chia cho 0** — có hệ dừng CPU,
> có hệ **tự thay mẫu số bằng 1** rồi chạy tiếp với con số sai mà không báo gì (Chương 19, mục 19.5).
>
> ⭐ **Nhân trước, chia sau** và **đơn vị nằm trong tên biến** — hai quy tắc của Chương 32 mục 32.4,
> áp ở đây y hệt.
>
> ⚠ Ba bộ đếm nên là `DINT` và **giữ được qua mất điện**; nhưng vẫn phải **ghi ra nơi khác** — pin hết
> thì số liệu biến mất âm thầm (Chương 18, Chương 54).

---

## L.15 Hút chân không có thổi ngược — hai ngõ ra, hai xác nhận

⭐ **Dùng khi:** gắp sản phẩm bằng giác hút. ⚠ Mẫu này khác hẳn xy-lanh hai vị trí ở L.8: **nhả không
phải là ngừng hút**.

```iecst
FUNCTION_BLOCK FB_Vacuum
VAR_INPUT
    SuckReq     : BOOL;      // TRUE = hút · FALSE = nhả
    SensOK      : BOOL;      // công tắc áp chân không báo đã đủ độ chân không
    SensShield  : BOOL;      // bỏ qua cảm biến — có điều kiện, xem Chương 51
    InterLock   : BOOL;      // chặn từ tầng chống va chạm (Chương 27)
    SuckLimit   : TIME := T#1S;    // bao lâu thì phải đạt độ chân không
    BlowTime    : TIME := T#300MS; // thổi ngược bao lâu rồi tắt
END_VAR
VAR_OUTPUT
    OutSuck     : BOOL;      // van hút
    OutBlow     : BOOL;      // ⭐ van THỔI NGƯỢC — ngõ ra riêng
    Holding     : BOOL;      // đang giữ được sản phẩm
    Released    : BOOL;      // đã nhả xong
    Fault       : BOOL;
    FaultCode   : INT;       // 1 = hút không đạt · 2 = rơi giữa chừng
END_VAR
VAR
    T_Suck : TON;
    T_Blow : TON;
END_VAR

// ── Hút ──
OutSuck := SuckReq AND NOT InterLock;
Holding := OutSuck AND (SensOK OR SensShield);

T_Suck(IN := OutSuck AND NOT Holding, PT := SuckLimit);
IF T_Suck.Q THEN
    Fault := TRUE;  FaultCode := 1;        // hút mãi không đạt: hở, tắc, hoặc không có hàng
END_IF;

// ⚠⚠ MẤT CHÂN KHÔNG GIỮA CHỪNG — sản phẩm đã rơi, và đây là báo động RIÊNG
IF OutSuck AND NOT SensOK AND NOT SensShield AND T_Suck.ET > SuckLimit THEN
    Fault := TRUE;  FaultCode := 2;
END_IF;

// ── Nhả: thổi ngược một nhịp NGẮN rồi TẮT ──
T_Blow(IN := NOT SuckReq, PT := BlowTime);
OutBlow  := NOT SuckReq AND NOT T_Blow.Q;  // thổi trong BlowTime, sau đó thôi
Released := NOT SuckReq AND T_Blow.Q;
END_FUNCTION_BLOCK
```

> ⭐⭐ **Ba điều làm mẫu này khác xy-lanh hai vị trí, và cả ba đều là chỗ hay sai:**
>
> | | |
> |---|---|
> | 1 | ⭐ **Ngừng hút KHÔNG phải là nhả.** Sản phẩm nhẹ sẽ dính lại vì độ chân không còn dư — phải **thổi ngược** mới rời ra đúng chỗ |
> | 2 | ⚠⚠ **Thổi ngược phải TẮT sau một nhịp ngắn.** Thổi liên tục thì tốn khí, làm bẩn sản phẩm, và ⭐ **thổi bay sản phẩm kế tiếp** |
> | 3 | ⚠⚠ **"Mất chân không giữa chừng" là báo động riêng, khác "hút không đạt".** Loại một nghĩa là chưa gắp được; loại hai nghĩa là ⭐ **sản phẩm đã rơi đâu đó trong máy** — và phải tìm nó trước khi chạy tiếp |
>
> ⚡ **Cảm biến ở đây là công tắc áp chân không, không phải cảm biến vị trí.** Nó nói *"đủ độ chân
> không"*, ⚠ **không** nói *"đang giữ đúng một sản phẩm"* — giác hút bịt vào mặt bàn cũng cho tín hiệu
> y hệt (Chương 33, Chương 48).

---

## L.16 Đếm tuổi thọ vật tư — cảnh báo trước, báo động sau

⭐ **Dùng khi:** một thứ sẽ mòn và sẽ hỏng — van, giác hút, mũi tra keo, bộ lọc, đèn UV, dây đai. Mẫu
này biến **một sự cố bất ngờ** thành **một việc có kế hoạch** (Chương 53 mục 53.5).

```iecst
FUNCTION_BLOCK FB_PartLife
VAR_INPUT
    CountTrig  : BOOL;       // một xung mỗi lần dùng — ⚠ đã bắt cạnh (L.7)
    ResetTrig  : BOOL;       // thay đồ mới → xoá về 0
    WarnLimit  : DINT;       // ⭐ ngưỡng NHẮC   ≈ tuổi thọ × 0,7
    AlarmLimit : DINT;       // ⭐ ngưỡng CẢNH BÁO ≈ tuổi thọ × 0,9
END_VAR
VAR_OUTPUT
    Count      : DINT;       // ⚠⚠ phải là biến GIỮ ĐƯỢC qua mất điện
    Warning    : BOOL;       // còn thời gian đặt hàng
    Alarm      : BOOL;       // nên thay ở lần dừng máy tới
    PctUsed    : INT;        // % đã dùng, đơn vị 1 %
END_VAR

IF ResetTrig THEN
    Count := 0;
ELSIF CountTrig THEN
    Count := Count + 1;
END_IF;

Warning := (Count >= WarnLimit);
Alarm   := (Count >= AlarmLimit);

IF AlarmLimit > 0 THEN
    PctUsed := DINT_TO_INT((Count * 100) / AlarmLimit);
ELSE
    PctUsed := 0;                        // chưa đặt ngưỡng — đừng chia cho 0 (L.14)
END_IF;
END_FUNCTION_BLOCK
```

> ⭐⭐ **Hai ngưỡng, không phải một — và khoảng cách giữa chúng chính là thời gian đặt hàng phụ tùng.**
> Một ngưỡng thì bạn biết *đúng lúc đã muộn*.
>
> ⚠⚠ **Cả hai ngưỡng đều là NHẮC, không được dừng máy.** Một cỗ máy tự dừng vì *"đã tới hạn thay
> van"* sẽ bị vô hiệu hoá trong vòng một tuần — và khi đó bạn mất luôn cả bộ đếm (Chương 53).
>
> ⚠⚠ **`Count` phải sống sót qua mất điện VÀ qua việc nạp lại chương trình.** ⭐ Đây là chỗ phải
> **thử thật**, không được tin: nhiều người phát hiện bộ đếm bảo trì của mình bị xoá mỗi lần nạp
> chương trình — sau khi đã đếm được ba năm (Chương 11, Chương 54).
>
> ⚡ **Một khối, nhiều thể hiện, ngưỡng là tham số.** Đây đúng là mức 1 của việc tái sử dụng ở
> Chương 30: mỗi vật tư một thể hiện, ngưỡng nạp từ bảng tham số — ⭐ **thêm một thứ cần theo dõi chỉ
> tốn một dòng khai báo**, nên người ta sẽ thật sự thêm.

---

## L.16b ⭐ Yêu cầu tới phần mềm PC theo số thứ tự — không bên nào xoá ô của bên kia

⭐ **Dùng khi:** một phần mềm trên máy tính — xử lý ảnh, đo, truy xuất — đọc ghi vùng thanh ghi của PLC,
và PLC cần nhờ nó làm một việc rồi chờ kết quả. Bảng giao tiếp chia hai vùng **theo người ghi**: vùng A
chỉ PLC ghi, vùng B chỉ phần mềm ghi (Chương 39 mục 39.9b).

```iecst
// ✔ VÍ DỤ HOÀN CHỈNH — một yêu cầu tới phần mềm PC theo số thứ tự (giống hệt Chương 39 mục 39.9b)
FUNCTION_BLOCK FB_PcRequest
VAR_INPUT
    Execute   : BOOL;            // ⭐ SƯỜN LÊN = gửi một yêu cầu mới · lệnh và tham số CHỐT tại sườn này
    Cmd       : INT;             // mã lệnh theo bảng giao tiếp
    Param     : INT;             // tham số của lệnh
    AckId     : INT;             // ← vùng B: số thứ tự phần mềm đã xử lý xong
    AckResult : INT;             // ← vùng B: 1 = OK · 2 = NG · số khác = phần mềm không hiểu lệnh
    TimeOut   : TIME := T#2S;    // [Nghề] 3–5 lần thời gian trả lời đo được (Phụ lục O mục O.11)
END_VAR
VAR_OUTPUT
    ReqId     : INT;             // → vùng A: số thứ tự của yêu cầu — chạy vòng 1…30000, không dùng số 0
    ReqCmd    : INT;             // → vùng A
    ReqParam  : INT;             // → vùng A
    Busy      : BOOL;            // ⭐ Busy · Done · Error LOẠI TRỪ nhau (Chương 30 mục 30.5b)
    Done      : BOOL;            // phần mềm đã trả lời — Ok cho biết OK hay NG
    Ok        : BOOL;            // chỉ có nghĩa khi Done
    Error     : BOOL;
    ErrorID   : INT;             // 0 = không lỗi · 1 = quá thời gian · 2 = phần mềm trả mã lạ
END_VAR
VAR
    ExecEdge  : R_TRIG;
    T_Out     : TON;
    LimitCopy : TIME;            // bản CHỐT của TimeOut
    Started   : BOOL;            // đã qua lần gọi đầu tiên sau khi bật máy
END_VAR
VAR_TEMP
    Start     : BOOL;            // vòng này vừa NHẬN một yêu cầu mới
    NewResult : BOOL;            // kết quả vừa có trong vòng này
END_VAR

// ── 0. Lần gọi đầu sau khi bật máy: lấy số phần mềm đã trả làm gốc → yêu cầu đầu mang số KHÁC ──
IF NOT Started THEN
    ReqId   := AckId;
    Started := TRUE;
END_IF;

ExecEdge(CLK := Execute);

// ── 1. Sườn lên khi rỗi → số thứ tự mới, chốt lệnh và tham số. Sườn lên khi bận → bỏ qua ──
Start := ExecEdge.Q AND NOT Busy;
IF Start THEN
    IF (ReqId < 1) OR (ReqId >= 30000) THEN
        ReqId := 1;              // quay vòng — và số 0 không bao giờ được dùng
    ELSE
        ReqId := ReqId + 1;
    END_IF;
    ReqCmd    := Cmd;
    ReqParam  := Param;
    Busy      := TRUE;
    Done      := FALSE;
    Ok        := FALSE;
    Error     := FALSE;
    ErrorID   := 0;
    LimitCopy := TimeOut;
END_IF;

// ── 2. Xong khi phần mềm báo ĐÚNG số này — trả lời mang số cũ, đến muộn, tự bị bỏ qua ──
T_Out(IN := Busy AND NOT Start, PT := LimitCopy);
IF Busy AND (AckId = ReqId) THEN
    Busy      := FALSE;
    NewResult := TRUE;
    IF (AckResult = 1) OR (AckResult = 2) THEN
        Done := TRUE;
        Ok   := (AckResult = 1);
    ELSE
        Error   := TRUE;
        ErrorID := 2;
    END_IF;
ELSIF Busy AND T_Out.Q THEN
    Busy      := FALSE;
    Error     := TRUE;           // ⚠ không trả lời ≠ NG (Chương 43 mục 43.7)
    ErrorID   := 1;
    NewResult := TRUE;
END_IF;

// ── 3. Execute đã tắt và việc đã xong → xoá kết quả; kết quả VỪA có vẫn hiện ít nhất MỘT vòng ──
IF NOT Execute AND NOT Busy AND NOT NewResult THEN
    Done    := FALSE;
    Ok      := FALSE;
    Error   := FALSE;
    ErrorID := 0;
END_IF;
END_FUNCTION_BLOCK
```

> ⭐⭐ **Ba điều làm mẫu này khác cách *"khác 0 là lệnh, bên kia xoá về 0"* hay gặp:**
>
> | | |
> |---|---|
> | 1 | ⭐ **Không ai xoá ô của người kia** — PLC chỉ ghi `ReqId`, `ReqCmd`, `ReqParam`; phần mềm chỉ ghi `AckId`, `AckResult` |
> | 2 | ⭐ Trả lời **đến muộn** mang số cũ → tự bị bỏ qua; hai kết quả giống nhau liên tiếp vẫn là **hai** kết quả |
> | 3 | ⚠⚠ **Không trả lời không phải NG** — `ErrorID = 1`, trạm xử lý như *"không biết"* (Chương 43 mục 43.7) |
>
> ⚡ Phía phần mềm phải theo **ba luật** ở Chương 39 mục 39.9b — ⚠ nhất là luật 2: ghi kết quả
> **trước**, số thứ tự **sau**, bằng hai lần ghi riêng.

---

## L.17 ⭐⭐ Danh mục khối dùng lại — cái nào tự viết, cái nào đã có sẵn

Trước khi viết một khối chức năng cho máy mới, hỏi đúng **một** câu: ⭐ **thứ này đã có ai làm chuẩn
chưa?** Viết lại một thứ đã được chuẩn hoá thì tốn công là chuyện nhỏ — ⚠ chuyện lớn là **bản của
bạn không được kiểm chứng bằng những gì bản chuẩn đã trải qua**.

⭐ Bảng dưới chia thư viện khối của một cỗ máy thành **ba nhóm**, theo đúng câu hỏi đó.

### Nhóm 1 — ⚠ Chuẩn hoặc hãng ĐÃ CÓ: đừng viết lại

| Bạn định viết | ⭐ Thứ đã có sẵn | Vì sao đừng tự viết |
|---|---|---|
| Khối **trễ** bật/tắt | ⭐ `TON` · `TOF` · `TP` — **khối chuẩn IEC 61131-3** | Hành vi đã định nghĩa trong chuẩn; bản tự viết ⚠ **hay sai ở trường hợp biên** (mất điện giữa chừng, đặt lại khi đang đếm) — Chương 17 |
| Khối **bắt cạnh** | ⭐ `R_TRIG` · `F_TRIG` — **khối chuẩn IEC** | Chương 16, Phụ lục L.7 |
| Khối **đếm** | ⭐ `CTU` · `CTD` · `CTUD` — **khối chuẩn IEC** | Chương 18 |
| Khối **chốt** | ⭐ `SR` · `RS` — **khối chuẩn IEC** | ⚠ Và phải biết cái nào ưu tiên Set, cái nào ưu tiên Reset — Chương 16 |
| Khối **dịch bit / dịch word** | ⭐ `SHL` · `SHR` · `ROL` · `ROR` — **hàm chuẩn IEC**; ngoài ra mọi hãng đều có lệnh dịch riêng | Chương 19 mục 19.6 |
| Khối **gộp 8 bit thành byte** / tách ngược lại | ⭐ Phần lớn hệ cho **truy cập từng bit của một `WORD`/`BYTE`** ngay trong cú pháp | ⚠ Tự viết là thêm một lớp không cần thiết — Chương 11 mục 11.2 |
| Khối **so sánh hai số nguyên bằng nhau** | ⭐ Toán tử `=` | ⚠ Không có gì để bọc |
| Khối **PID** | ⭐ Hầu hết hệ có **khối PID sẵn**, nhiều hệ kèm **tự chỉnh định** *(auto-tune)* | Chương 35. ⭐ Tự viết PID chỉ hợp lý khi bạn cần thứ khối sẵn không làm được — và khi đó hãy nói rõ là **thứ gì** |

> ⚡ **Một ngoại lệ đáng giữ trong nhóm này: so sánh hai SỐ THỰC.**
>
> ⚠ `=` với số thực là bẫy — hai giá trị "bằng nhau về mặt vật lý" vẫn khác nhau ở chữ số cuối.
> ⭐ Một khối `SoSanhReal(a, b, DungSai)` trả về *"lệch nhỏ hơn dung sai"* **là khối đáng viết**, vì
> chuẩn không có sẵn (Chương 19 mục 19.5).

### Nhóm 2 — ⚠⚠ TUYỆT ĐỐI không tự viết

| Bạn định viết | ⭐ Thứ đã có | ⚠⚠ Vì sao |
|---|---|---|
| ⚠⚠ **Khối điều khiển hai tay** | ⭐ **`SF_TwoHandControlTypeII`** và **`SF_TwoHandControlTypeIII`** — khối an toàn đã chuẩn hoá (PLCopen Safety) | Xem khung bên dưới |
| ⚠⚠ Khối **dừng khẩn cấp** | ⭐ `SF_EmergencyStop` | Chương 47, Phụ lục L.3 |
| ⚠⚠ Khối **giám sát cửa / khoá cửa** | ⭐ `SF_Guard` · `SF_GuardLocking` | Chương 47 |
| ⚠⚠ Khối **rèm quang** và **muting** | ⭐ `SF_ESPE` · `SF_MutingSeq` · `SF_MutingPar` | Chương 47 mục 47.7 |
| ⚠⚠ Khối **chọn chế độ** có ràng buộc an toàn | ⭐ `SF_ModeSelector` | Chương 28, Chương 47 |
| ⚠⚠ Khối **bỏ qua** có ràng buộc an toàn | ⭐ `SF_Override` | ⚠ Khác hẳn cờ bỏ qua thường ở Chương 51 mục 51.7b |
| ⚠⚠ Khối **giám sát phản hồi công tắc tơ** | ⭐ `SF_EDM` | Chương 48 |
| ⚠⚠ Khối **nút phục hồi** an toàn | ⭐ `SF_ResetButton` | Chương 47 |

> ⚠⚠ **Nhóm này không phải lời khuyên về năng suất. Đây là ranh giới.**
>
> ⭐ Hai lý do, và lý do thứ hai mới là lý do thật:
>
> | | |
> |---|---|
> | 1 | Các khối này **đã được định nghĩa hành vi rất kỹ** — kể cả những chuyện dễ quên: phải **nhả cả hai nút rồi mới được bắt đầu lần sau**, phải xử lý **nút kẹt dính**, phải báo **lý do từ chối** |
> | 2 | ⚠⚠ **Chúng phải chạy trên phần cứng an toàn đã chứng nhận.** Viết lại chúng bằng logic thường, trong CPU thường, là ⭐ **chuyển một chức năng an toàn vào chỗ mà CPU treo thì nó treo theo** — đúng điều Chương 47 cấm |
>
> ⚡ **Dấu hiệu nhận ra mình đang sai:** nếu khối bạn đang viết có tên chứa *"nút hai tay"*, *"dừng
> khẩn"*, *"cửa an toàn"*, *"rèm quang"* — ⭐ **dừng lại và hỏi người có thẩm quyền về an toàn**,
> trước khi viết dòng tiếp theo.

### Nhóm 3 — ⭐ Nên tự viết: đây mới là thư viện của bạn

⭐ Đây là nhóm đem lại giá trị thật, vì **không ai làm hộ được** — chúng gắn với cách cỗ máy của bạn
hoạt động. Mỗi dòng dưới đây đã có mẫu ở đâu đó trong sách:

| Khối | Làm gì | ⭐ Mẫu ở đâu |
|---|---|---|
| **Cơ cấu hai vị trí** | Xy-lanh có hai cảm biến, timeout, phát hiện hai cảm biến cùng báo | **Phụ lục L.8** |
| **Hút chân không** | Hai ngõ ra, hai xác nhận, thổi ngược có thời hạn | **Phụ lục L.15** |
| ⭐ **Bọc lệnh chuyển động** | Gói `MC_*` thành một giao diện quen thuộc cho trình tự | **Phụ lục L.9**, Chương 37 mục 37.8 |
| **Trục điện qua mạng** | Cùng ý tưởng, nhưng nói chuyện qua thanh ghi | Chương 39 |
| **Kho đệm / trạm đệm** | Theo dõi từng ô, thời gian nằm, thứ tự lấy ra | **Chương 41 mục 41.7b** |
| **Lưới khay** | Dạy ba điểm, suy ra mọi ô | **Phụ lục K.7b** |
| ⭐ **Đếm tuổi thọ vật tư** | Hai ngưỡng: nhắc trước, cảnh báo sau | **Phụ lục L.16**, Chương 53 |
| **Đo chu kỳ** | Đo thật từng trạm, không tính lý thuyết | Chương 55 mục 55.4 |
| ⭐ **Đồng hồ trạng thái máy** | Bật máy · chạy · dừng · chờ, và bất biến giữa chúng | **Chương 55 mục 55.7c** |
| ⭐ **Thống kê năng suất** | Tỉ lệ đạt, khả dụng, hiệu suất — cất số **đếm**, không cất phần trăm | **Chương 55 mục 55.7c** |
| ⭐ **Bắt tay với máy tính / hệ trên** | Số thứ tự yêu cầu · kết quả · quá thời gian — mỗi ô một người ghi | **Phụ lục L.16b**, Chương 39 mục 39.9b |
| ⭐ **Khoảng hở hai đầu chung một ray** | Kiểm đích lúc ra lệnh, kiểm quãng dừng liên tục | **Phụ lục L.9b**, Chương 37 mục 37.7b |
| **Điều khiển lực ép** | Vòng kín trên nền khối PID của hãng, cộng bù hiệu chuẩn | Chương 34, Chương 35 |

> ⭐⭐ **Bằng chứng rằng nhóm 3 đáng đầu tư, đo trên bốn cỗ máy khác nhau của cùng một nhóm kỹ
> thuật:** **25 trên 27 khối giống hệt nhau ở cả bốn máy**. Phần khác nhau gần như chỉ là trình tự
> trạm (Chương 30 mục 30.5).
>
> ⚡ Nói cách khác: **công viết thư viện trả hết ở máy thứ hai**, và từ máy thứ ba trở đi là lãi.

### ⭐ Trước khi thêm một khối vào thư viện — bốn câu hỏi

| # | Hỏi | Nếu câu trả lời là… |
|---|---|---|
| 1 | **Chuẩn IEC đã có chưa?** | Có → dùng khối chuẩn. ⭐ Nó khả chuyển sang mọi hệ (Chương 14) |
| 2 | ⚠⚠ **Nó có phải chức năng an toàn không?** | Có → ⭐ **dừng lại**, dùng khối an toàn đã chứng nhận trên phần cứng an toàn |
| 3 | **Hãng đã có khối tương đương chưa?** | Có → cân nhắc dùng, ⚠ nhưng nhớ **nó khoá bạn vào hãng** (Chương 14 mục 14.6b) |
| 4 | **Nó có xuất hiện ở máy thứ hai không?** | Không → ⚠ **đừng đưa vào thư viện**; viết thẳng trong chương trình máy đó. ⭐ Thư viện đầy khối dùng một lần thì không còn là thư viện |

---

## L.18 ⭐⭐ Ladder hay ST — mẫu nào nên viết bằng gì

Bảy mẫu ở trên có **cả hai bản**. Các mẫu còn lại **chỉ có ST** — và đó là chủ ý, không phải lười.
⭐ Mục này nói rõ vì sao, để bạn quyết định cho máy của mình.

### ⭐ Cùng một bài toán, hai ngôn ngữ, hai kết quả rất khác nhau

| Mẫu | Ladder | ST | ⭐ Nên dùng |
|---|---|---|---|
| **L.1** tự giữ | ⭐⭐ Nhánh tự giữ **nhìn thấy được** | ⚠ Dấu ngoặc sai chỗ trông vẫn bình thường | ⭐ **Ladder** |
| **L.2** chuỗi cho phép | ⭐⭐ Một nấc, thấy ngay tiếp điểm nào hở | Một biểu thức dài | ⭐⭐ **Ladder** |
| **L.4** ba lệnh dừng | ⭐ Rõ, nhưng tốn hai nấc cho một nút bật/tắt | ⭐ Gọn hơn | Hoà |
| **L.7** bắt cạnh + chống rung | ⭐ Thứ tự lọc–bắt cạnh **nhìn thấy được** | ⚠ Hai dòng cạnh nhau, đảo chỗ trông vẫn hợp lý | ⭐ **Ladder** |
| **L.8** gọi khối cơ cấu | ⭐⭐ Hộp có tên — hình dạng quen nhất với thợ bảo trì | Gọn | ⭐ **Ladder gọi, ST viết bên trong** |
| **L.10** khoá chéo | ⭐⭐ Tiếp điểm khoá chéo **nhìn chéo là thấy** | Phải đọc kỹ từng vế | ⭐⭐ **Ladder** |
| **L.13** đèn tháp | ⭐⭐ Mỗi đèn một nấc — tìm ra trong mười giây | Bốn dòng, phải biết tìm ở đâu | ⭐⭐ **Ladder** |
| **L.3** giám sát dừng khẩn | ⚠ Nhiều nấc rời rạc, mất mạch lạc | ⭐ Một khối `IF` đọc liền mạch | ⭐ **ST** |
| **L.5** một lần / tuần hoàn | ⚠ Điều kiện lồng nhau thành nhiều nấc | ⭐ Rõ | ⭐ **ST** |
| **L.6** khung trình tự | ⚠⚠ `CASE` **không có tương đương tự nhiên** | ⭐⭐ Đúng công cụ | ⭐⭐ **ST** |
| **L.9** servo | ⚠ Nhiều hộp, nhiều chân, rối | ⭐ Máy trạng thái đọc được | ⭐⭐ **ST** |
| **L.12** analog bốn bước | ⚠⚠ Phép tính bằng ladder rất khó đọc | ⭐⭐ Tự nhiên | ⭐⭐ **ST** |
| **L.14** đếm sản lượng | ⚠ Phép chia và kiểm mẫu số thành nhiều hộp | ⭐ Bốn dòng | ⭐⭐ **ST** |
| **L.16** tuổi thọ vật tư | ⚠ So sánh và phần trăm rối | ⭐ Rõ | ⭐ **ST** |
| **L.9b** khoảng hở hai đầu | ⚠⚠ Phép tính quãng phanh thành một chuỗi hộp toán | ⭐ Ba dòng | ⭐⭐ **ST** |
| **L.16b** yêu cầu tới phần mềm PC | ⚠ Máy trạng thái nhỏ nhiều nhánh | ⭐ Rõ | ⭐ **ST** |

### ⭐⭐ Rút ra một quy tắc dùng được

| Viết bằng **ladder** khi… | Viết bằng **ST** khi… |
|---|---|
| ⭐⭐ **Thợ bảo trì sẽ phải đọc nó lúc hai giờ sáng** | Chỉ người lập trình đọc |
| Nó là **logic bit**: nối tiếp, song song, khoá chéo, chốt | Có **phép tính**, so sánh nhiều nhánh, xử lý số |
| ⭐ Nó điều khiển **ngõ ra cuối cùng** | Nó là **tính toán trung gian** |
| ⭐ Nó là **liên động** — thứ người ta sẽ soi khi máy không chạy | Nó là **trình tự nhiều bước** (`CASE`) |
| Cần **theo dõi trực tuyến** thấy dòng chạy qua từng tiếp điểm | Cần **vòng lặp**, mảng, chỉ số |

> ⭐⭐ **Câu quyết định, và nó không phải câu kỹ thuật:** ⭐ **ai sẽ mở đoạn này ra xem, và trong
> hoàn cảnh nào?**
>
> ⚡ Cùng một logic, viết bằng ladder thì **người không biết lập trình vẫn dò được** bằng cách nhìn
> tiếp điểm nào đang sáng trên màn hình theo dõi. ⚠ Viết bằng ST thì họ phải **gọi bạn**.

### ⭐ Trộn hai ngôn ngữ — cách trộn đúng

⚠ Trộn **không** có nghĩa là mỗi chỗ một kiểu tuỳ hứng. ⭐ Có một cách chia đã được dùng nhiều và
hợp lý:

| Tầng | Ngôn ngữ | Vì sao |
|---|---|---|
| **Bên trong khối chức năng** | ⭐ **ST** | Có timer, so sánh, mã lỗi — và ⭐ **người dùng khối không cần mở nó ra** |
| **Gọi khối, nối dây giữa các khối** | ⭐ **Ladder** | Hình dạng hộp quen thuộc, thấy được luồng |
| **Trình tự nhiều bước** | ⭐⭐ **ST** với `CASE`, hoặc **SFC** | Chương 21, Chương 26 |
| ⭐⭐ **Chuỗi cho phép và ngõ ra cuối** | ⭐⭐ **Ladder** | ⚠ Đây là chỗ **không nên** dùng ST, kể cả khi cả chương trình viết bằng ST |

> ⭐⭐ **Hàng cuối là lời khuyên đáng giá nhất của cả mục.** Rất nhiều chương trình viết toàn bộ bằng
> ST rồi để ngõ ra cuối cũng bằng ST — ⚡ và đó chính là chỗ thợ bảo trì bị chặn lại. ⭐ **Vài nấc
> thang ladder ở đúng chỗ đó đổi hẳn khả năng tự xử lý của nhà máy**, và nó gần như không tốn gì.

> ⚠ **Một lưu ý về hỗ trợ của hãng.** Không phải hệ nào cũng cho **trộn ngôn ngữ trong cùng một
> chương trình** ở mọi mức. ⭐ Phần lớn hệ hiện đại cho mỗi **khối** một ngôn ngữ (khối này ladder,
> khối kia ST) — như vậy là đủ cho cách chia ở bảng trên. ⚠ **Kiểm trước khi thiết kế theo nó**, và
> xem Phụ lục A1 cho khác biệt giữa các hệ.

---

## L.19 Bảng tra nhanh — mẫu nào cho việc gì

| Việc cần làm | Mẫu | Bẫy lớn nhất | Chương |
|---|---|---|---|
| Nhấn nút rồi nhả, máy vẫn chạy | L.1 | ⚠ Vị trí của điều kiện dừng | 15, 16 |
| Gom điều kiện cho phép | L.2 | ⭐ Phải có **lý do chặn** | 25, 44 |
| Dừng khẩn cấp | L.3 | ⚠⚠ **Không phải việc của PLC** | 47, 48 |
| Dừng ngay / tạm dừng / cuối chu trình | L.4 | ⚠ Nhả kẹp khi tạm dừng | 28 |
| Chạy một lần hay tuần hoàn | L.5 | ⭐ Kiểm cho phép ở **cuối** chu trình | 25 |
| Trình tự nhiều bước | L.6 | ⚠ Timer để **báo lỗi**, không để chuyển bước | 17, 26 |
| Làm đúng một lần mỗi sự kiện | L.7 | ⚠ Lọc rung **trước** bắt cạnh | 16, 18 |
| Điều khiển xy-lanh | L.8 | ⭐ Kiểm **hai cảm biến cùng báo** | 27, 30, 48 |
| Điều khiển servo | L.9 | ⚠ Giữ `Execute`; bỏ qua `CommandAborted` | 37 |
| Hai đầu chung một ray | L.9b | ⚠⚠ Chỉ kiểm vị trí hiện tại — quên quãng phanh | 27, 37 |
| Đảo chiều, sao–tam giác | L.10 | ⚠⚠ **Khoảng chết** và **khoá cơ khí** | 3, 36 |
| Báo động | L.11 | ⭐ Giữ **báo động đầu tiên** | 44 |
| Đọc analog | L.12 | ⚠⚠ Kiểm ngoài dải **trước** khi quy đổi | 31, 32 |
| Đèn tháp | L.13 | ⚠ Mỗi lúc một màu | 44, 51 |
| Đếm sản lượng | L.14 | ⚠⚠ Chia cho 0 ở đầu ca | 19, 55 |
| Gắp bằng giác hút | L.15 | ⚠⚠ Ngừng hút **không phải** là nhả | 6, 33, 46 |
| Theo dõi tuổi thọ vật tư | L.16 | ⚠⚠ Bộ đếm bị xoá khi nạp lại chương trình | 11, 53 |
| Nhờ phần mềm PC làm một việc | L.16b | ⚠⚠ Hai chương trình cùng ghi một ô | 39, 43 |
| ⭐ **Chọn viết bằng ladder hay ST** | **L.18** | ⚠ Viết ngõ ra cuối bằng ST — thợ bảo trì bị chặn | 15, 20 |
| ⭐ Khối nào tự viết, khối nào đã có sẵn | **L.17** | ⚠⚠ Tự viết khối chức năng an toàn | 30, 47 |

---

> ⚠⚠ **Nhắc lại giới hạn.** Mọi đoạn ở đây đều **ngắn hơn thực tế** — chúng bỏ qua phần riêng của máy
> bạn, và bỏ qua mọi thứ thuộc về thiết kế an toàn.
>
> ⭐ Hãy đọc chương được dẫn để hiểu **vì sao** mẫu viết như vậy, rồi viết lại bằng tên biến của bạn.
> ⚠ **Chép nguyên mà không hiểu là cách tạo ra lỗi rất giống code đúng** — và loại lỗi đó khó tìm
> nhất, vì người đọc lại code sẽ thấy nó quen mắt rồi lướt qua.
