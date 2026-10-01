# Chương 27 — Kiến trúc chương trình cho máy nhiều trạm

> **Lát cắt máy mẫu:** 2 — chuyền, chặn, nâng kẹp, cảm biến board, nút bấm, đèn tháp, hai trạm, trình
> tự song song, công thức sản phẩm.

---

## 27.1 Chỗ chương trình sụp đổ khi máy lớn lên

Chương 25 cho bạn mô hình trạng thái, Chương 26 cho bạn trình tự các bước. Với **một trạm**, hai thứ
đó là đủ — chương trình gọn, đọc được, sửa được.

Rồi máy có **trạm thứ hai**.

Cách tự nhiên nhất là chép trình tự trạm 1 sang, đổi tên tag, thêm điều kiện để hai trạm không giẫm
chân nhau. Chạy được. Rồi thêm chế độ tay cho từng trạm. Rồi thêm xử lý khi trạm 2 lỗi mà trạm 1 vẫn
chạy. Rồi thêm trạm thứ ba.

Đến lúc nào đó, hiện tượng sau xuất hiện — và nó là **triệu chứng đặc trưng** của kiến trúc sai:

> **Sửa một thứ ở trạm 1 làm hỏng một thứ ở trạm 2, mà không ai giải thích được vì sao.**

Nguyên nhân không nằm ở chỗ nào cụ thể trong code. Nó nằm ở chỗ **hai trạm biết quá nhiều về nhau**.
Trạm 1 đọc bước hiện tại của trạm 2 để quyết định; trạm 2 ghi thẳng vào một cờ mà trạm 1 dùng; cả hai
cùng điều khiển chuyền. Mỗi liên kết như vậy là một sợi dây vô hình, và số sợi dây tăng theo bình
phương số trạm.

Chương này là cách tổ chức chương trình để số sợi dây đó **không tăng** khi máy lớn lên.

---

## 27.2 Ba tầng — và quy tắc gọi

Cách tổ chức đã được kiểm chứng là chia chương trình thành **ba tầng**, mỗi tầng một loại trách nhiệm.

![Ba tầng kiến trúc chương trình](../assets/ch27/hinh_27_1_ba_tang.svg)

*Hình 27.1 — Ba tầng và hướng gọi. Mũi tên chỉ đi xuống; tầng dưới không bao giờ gọi ngược lên.*

| Tầng | Trách nhiệm | Trả lời câu hỏi | Ví dụ ở DP-01 |
|---|---|---|---|
| **Máy** *(machine)* | Chế độ vận hành, lỗi toàn máy, cho phép/cấm | *Máy có được phép chạy không?* | Máy trạng thái ở Chương 25 |
| **Trạm** *(station)* | Trình tự xử lý **sản phẩm đang ở trạm đó** | *Board ở trạm này đang ở bước nào?* | Trạm tra keo, trạm sấy |
| **Cơ cấu** *(device)* | Điều khiển **một** thiết bị vật lý | *Xy-lanh này ra hay vào?* | Kẹp trạm 1, chặn trạm 1, chuyền |

### ⭐⭐ Bốn câu hỏi để tự suy ra cách chia — dùng khi máy không giống DP-01

Ba tầng ở trên là **kết quả**, không phải xuất phát điểm. Với một cỗ máy khác — một trạm, hoặc mười
trạm, hoặc một dây chuyền không có "sản phẩm" rõ ràng — bạn phải tự chia. ⭐ Bốn câu hỏi này làm việc đó:

| # | Câu hỏi | Trả lời **CÓ** nghĩa là |
|:-:|---|---|
| 1 | ⭐ *Hai việc này có bao giờ xảy ra **cùng lúc** không?* | ⭐ **Phải tách** — gộp lại thì một việc chặn việc kia |
| 2 | *Việc này có xảy ra **bất kể** các việc khác không?* | ⭐ **Tách** — nó độc lập, đừng buộc nó vào trình tự nào |
| 3 | *Có một **trình tự rõ ràng** không?* | Phần đó là **một** khối trình tự (Chương 26) |
| 4 | ⭐ *Có **ranh giới vật lý** trong quy trình hoặc trong máy không?* | ⭐ **Chia theo đúng ranh giới đó** |

> ⭐⭐ **Câu 4 là câu đáng tin nhất, và cũng là câu hay bị bỏ qua nhất.**
>
> Ranh giới vật lý — hai trạm cách nhau, hai cụm cơ khí độc lập, hai tủ điện — ⭐ **là ranh giới đã
> được thực tế kiểm chứng**. Chia phần mềm theo nó thì cấu trúc chương trình **soi gương** cấu trúc
> máy, và người bảo trì đứng trước máy biết ngay phải mở khối nào.
>
> ⚠ Ngược lại, chia theo thứ tự khác — theo loại thiết bị chẳng hạn, *"tất cả xy-lanh vào một khối"* —
> tạo ra chương trình mà ⚠⚠ **không ai đứng trước máy suy ra được**.

> ⭐ **Thứ tự dùng:** hỏi câu 4 **trước**. Nếu máy có ranh giới vật lý rõ, phần lớn việc chia đã xong.
> Ba câu còn lại dùng để xử lý phần không có ranh giới vật lý.
>
> ⚡ Trên DP-01, câu 4 cho ngay **hai trạm**; câu 1 cho biết hai trạm chạy đồng thời nên **không được**
> gộp; câu 3 cho biết bên trong mỗi trạm là một trình tự; câu 2 tách ra những thứ chạy độc lập —
> ⭐ **và đó chính là ba tầng ở bảng trên.**

> ⚠ **Điều kiện tiên quyết cho cả bốn câu: hiểu quy trình trước đã.** Khi quy trình mới hiểu một
> nửa, việc chia sẽ **phải làm đi làm lại** — và mỗi lần chia lại là viết lại. ⭐ Đây là lý do
> Chương 23 (từ yêu cầu tới đặc tả) đứng **trước** chương này.

---

### Ba quy tắc gọi — vi phạm là kiến trúc hỏng

> **Q1 — Chỉ gọi xuống, không gọi lên.**
> Máy gọi trạm. Trạm gọi cơ cấu. Cơ cấu **không** gọi trạm; trạm **không** gọi máy. Tầng dưới chỉ
> *báo cáo trạng thái* qua các biến ra của nó, và tầng trên đọc.

> **Q2 — Ngang hàng không gọi nhau.**
> Trạm 1 **không** gọi trạm 2, không đọc biến nội bộ của trạm 2. Muốn phối hợp thì đi qua tầng trên,
> hoặc qua một giao diện đã công bố (mục 27.4).

> **Q3 — Chỉ tầng cơ cấu được chạm vào ngõ ra vật lý.**
> Không dòng nào trong tầng trạm hay tầng máy được viết `DO_Clamp1Vlv := …`. Trạm chỉ nói *"kẹp ơi,
> đi ra"*; việc bật van là của khối cơ cấu.

Quy tắc Q3 nghe hình thức, nhưng nó là quy tắc **trả lại nhiều nhất**:

- Cuộn dây trùng (Chương 15, Bẫy 1) **không thể xảy ra** — chỉ có đúng một nơi ghi vào mỗi ngõ ra.
- Muốn biết vì sao một van bật, bạn mở đúng một khối, không phải dò cả chương trình.
- Thêm liên động chống va chạm thì thêm vào một chỗ, áp cho mọi người gọi.

---

## 27.2b ⭐⭐ Bảy bước dựng cấu trúc — làm theo thứ tự nào

Mục 27.2 nói chương trình **nên** có ba tầng. Mục này trả lời câu đứng ngay sau đó: ⭐ **bắt đầu từ
đâu, và theo thứ tự nào** — vì thứ tự sai thì ba tầng kia không tự mọc ra.

PLCopen đề xuất một trình tự bảy bước cho việc cấu trúc hoá phần mềm theo IEC 61131-3. Bảng dưới đặt
nó cạnh chỗ tương ứng trong sách này:

| # | Bước | Trả lời câu hỏi | Chương |
|---|---|---|---|
| 1 | **Xác định giao diện ra bên ngoài** của hệ điều khiển | Máy nói chuyện với **ai** — máy trước, máy sau, cấp trên, người vận hành | 41, 45 |
| 2 | **Chốt các tín hiệu chính trao đổi** với phần còn lại của nhà máy | Qua mỗi giao diện đó, **những bit và số nào** đi qua | 23, 41 |
| 3 | ⭐⭐ **Chốt mọi tương tác của người vận hành, mọi cách BỎ QUA, và dữ liệu giám sát** | Người vận hành làm được gì, và ⭐ **được phép bỏ qua cái gì** | 28, 51 |
| 4 | **Phân rã bài toán từ trên xuống** thành các phần logic | Máy chia thành mấy trạm, mấy cụm, mấy cơ cấu | ⭐ **27** |
| 5 | **Định nghĩa các khối cần có** — chương trình và khối chức năng | Cái gì viết một lần dùng nhiều lần | 27, 30 |
| 6 | **Chốt yêu cầu chu kỳ** cho từng phần | Phần nào phải chạy nhanh, phần nào chậm cũng được | 10, 27 |
| 7 | **Cấu hình hệ thống** — gán chương trình vào tác vụ, gán chân vào/ra | Ai chạy trong tác vụ nào, tag nào ứng chân nào | 27, 30 |

> ⭐⭐ **Bước 3 là bước gây ngạc nhiên nhất, và nó đáng bàn.**
>
> Tương tác người vận hành và ⭐ **các đường "bỏ qua" (override) được chốt ở bước 3 — TRƯỚC khi phân
> rã bài toán ở bước 4.** Nghĩa là chúng được coi là **đầu vào của kiến trúc**, không phải thứ gắn
> thêm khi máy gần xong.
>
> ⚠ Thực tế thì gần như ai cũng làm ngược: viết trình tự tự động trước, rồi mới nghĩ tới chế độ tay,
> rồi cuối cùng mới đối phó với câu *"camera hỏng thì chạy kiểu gì"*. ⭐ Và đó chính là lý do phần đó
> luôn trông như chắp vá — xem Chương 28 và Chương 51 mục 51.7b.

### ⚠ Giới hạn của việc chia nhỏ

Chia để trị là đúng, nhưng nó **không đúng vô hạn**:

> ⚠⚠ **Chia càng nhỏ thì công sức không biến mất — nó chuyển sang việc GHÉP các mảnh lại.**
>
> ⭐ Một khối làm đúng một việc rõ ràng là tốt. Ba mươi khối, mỗi khối ba dòng, nối với nhau bằng
> bốn mươi biến trung gian thì **khó đọc hơn** một khối ba mươi dòng.
>
> ⚡ Dấu hiệu đã chia quá tay: ⚠ **số biến đi lại giữa các khối tăng nhanh hơn số khối**. Khi mỗi
> khối mới thêm vào lại kéo theo năm biến giao tiếp, bạn đang trả nhiều hơn phần được lợi — đúng
> nguyên tắc "giao diện phải nhỏ" ở mục 27.3.

### ⭐ Bốn nguyên tắc đi kèm

| Nguyên tắc | Nghĩa | Ở đâu trong sách |
|---|---|---|
| ⭐⭐ **Chỉ làm việc bằng tên tượng trưng** — địa chỉ tuyệt đối **chỉ xuất hiện ở phần khai báo** | Đổi module, đổi chân thì sửa **một chỗ**; phần còn lại không biết gì | Chương 30 mục 30.2 |
| **Phần nào thuộc về nhau thì để cạnh nhau trong mã nguồn** | Đọc một cơ cấu không phải nhảy bốn chỗ | Chương 30 mục 30.3 |
| ⚠ **Không dùng lệnh nhảy** | Nhảy phá tính đọc được và tính tái dùng, và sinh hiệu ứng phụ | Chương 20 |
| **Đặt tên biến và khối nhất quán** | Cho phép **đoán đúng** thay vì phải tra | Chương 30 mục 30.2 |

---

## 27.3 Tầng cơ cấu — khối tái dùng

Mỗi loại cơ cấu viết **một lần** thành một **khối chức năng** *(function block, FB)*, rồi tạo nhiều
**thể hiện** *(instance)* cho từng cơ cấu cụ thể.

DP-01 ở lát cắt này có bốn xy-lanh hai vị trí (chặn ×2, kẹp ×2). Chúng khác nhau ở tag, giống nhau ở
hành vi. Vậy viết một khối:

```iecst
// ✔ VÍ DỤ HOÀN CHỈNH — khối xy-lanh hai vị trí, dùng lại cho mọi xy-lanh (giống hệt Phụ lục L mục L.8)
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

⭐⭐ **Bốn quyết định trong khối này không hiển nhiên** — và mỗi cái, nếu làm ngược lại, là một lỗi có
thật:

| Quyết định | ⚠ Làm ngược lại thì sao |
|---|---|
| ⭐⭐ **Mất cho phép thì GIỮ lệnh van**, không cắt van | Van 5/2 lò xo về: **cắt điện cũng là một lệnh chuyển động** — về vị trí lò xo. Máy vào `Alarm`, cắt van kẹp → kẹp nhả, board rơi, ⚠⚠ trái ngược chức năng an toàn SF6 của DP-01 (Phụ lục J). Với van một cuộn, *"không cho chuyển động"* nghĩa là **không đổi lệnh**, không phải **tắt lệnh** |
| ⭐ **Lỗi không tự tác động lên van** | Khối tự nhả van khi có lỗi thì ⚠ **một cảm biến hỏng cũng làm cơ cấu chuyển động**. Khối **báo**; tầng máy **quyết định** phản ứng (Chương 28) |
| ⭐ **`Done` so với YÊU CẦU**, không chỉ với van | Lúc đang bị giữ, van và yêu cầu khác nhau. `Done` chỉ so với van sẽ báo *"đã xong"* cho vị trí **cũ** — ⚠ trạm đi bước tiếp trong khi kẹp **chưa** kẹp |
| **Xoá lỗi đứng TRƯỚC các phép kiểm** | Đặt sau thì nguyên nhân còn mà lỗi vẫn biến mất một vòng quét — tầng máy đọc sau sẽ thấy một vòng *"hết lỗi"* giả. Đặt trước thì Reset chỉ có tác dụng khi nguyên nhân **đã hết**, đúng nguyên tắc ở Chương 25 |

> ⚡ **Và `T_Move` được gọi đúng một lần mỗi vòng quét.** Muốn đếm lại từ đầu khi lệnh van đổi, đừng
> gọi `T_Move(IN := FALSE)` rồi gọi lại lần hai — hãy đưa điều kiện *"lệnh vừa đổi"* vào **chính** chân
> `IN`: `(Valve = ValvePrev)` bằng `FALSE` đúng một vòng quét, đủ để bộ định thời xoá về 0. Gọi một
> thể hiện hai lần trong một vòng là lỗi ở Chương 17, Bẫy 5 (PLCopen CP20, Phụ lục N).

Rồi tạo bốn thể hiện:

```iecst
VAR_GLOBAL
    // ⭐ Toàn cục có chủ ý: tầng cơ cấu GỌI, tầng trạm ĐỌC Done (Chương 26) — không ai khác gọi
    Stop1  : FB_Cylinder2Pos;
    Clamp1 : FB_Cylinder2Pos;
    Stop2  : FB_Cylinder2Pos;
    Clamp2 : FB_Cylinder2Pos;
END_VAR

// Gọi mỗi vòng quét — tầng cơ cấu chạy TRƯỚC tầng trạm
Clamp1(Req      := M_Stn1_ClampReq,
       Permit   := M_MotionEnable,
       Reset    := M_ClearFaults,        // lệnh xoá của tầng máy — Chương 25 mục 25.5c
       SensWork := DI_Clamp1Up,
       SensHome := DI_Clamp1Dn,
       Limit    := T#3S);
DO_Clamp1Vlv := Clamp1.Valve;             // ← đúng MỘT dòng ghi vào ngõ ra này
```

Bốn thứ bạn được ngay khi viết như vậy, mà cách viết rải rác không cho:

1. **Timeout tự động cho mọi cơ cấu.** Viết một lần, bốn cơ cấu đều có. Cách rải rác thì bạn sẽ quên
   ít nhất một cái.
2. **Phát hiện tư thế "giữa chừng"** ở mọi cơ cấu, không sót.
3. **Phát hiện cảm biến hỏng** — cả hai cùng bật là tình huống vật lý bất khả, nên chắc chắn là hỏng.
   Rất ít người viết kiểm tra này khi code rải rác.
4. **Một cửa duy nhất để thêm liên động.** Cần chặn chuyển động khi mất khí? Thêm vào `Permit`, một
   chỗ, áp cho cả bốn. ⚠ Và *"chặn"* ở đây là **không đổi vị trí** — bảng ngay trên.

> 💡 **MẸO — tín hiệu vào của khối cơ cấu nên là mức, không phải xung**
> `Req` giữ mức 1 suốt thời gian muốn xy-lanh ở vị trí làm việc. Nếu dùng xung, khối phải tự nhớ trạng
> thái, và bạn vừa tạo thêm một chỗ để mất đồng bộ. Mức thì tự đồng bộ: mất **lệnh** là về vị trí lò xo.
> ⚠ Đừng nhầm với mất **cho phép** — cái đó **giữ nguyên** (Bẫy 7).

---

## 27.3b ⭐⭐ Tầng chống va chạm — một lớp riêng, không rải trong trình tự

Mục 27.3 đặt cơ cấu thành một tầng. Nhưng có một loại điều kiện **không thuộc về cơ cấu nào cả**:
điều kiện nói rằng ⭐ **hai cơ cấu không được ở cùng một chỗ, cùng một lúc**.

Đầu công tác không được hạ xuống khi kẹp chưa lên. Băng tải không được chạy khi kẹp còn giữ board.
Xy-lanh chặn không được hạ khi board chưa qua hẳn.

### Vì sao nó phải là một tầng riêng

Cách làm tự nhiên là viết điều kiện đó ngay tại chỗ ra lệnh:

```iecst
// ⚠ CÁCH HAY GẶP — và nó sẽ hỏng
IF Stn1_Step = 30 AND DI_Clamp1Up THEN     // "nhớ" kiểm kẹp trước khi hạ Z
    M_Z_DownReq := TRUE;
END_IF;
```

Ba vấn đề, cả ba đều chỉ lộ ra khi máy đã chạy:

| # | Vấn đề | Hậu quả |
|---|---|---|
| 1 | ⚠⚠ **Chế độ tay không đi qua trình tự** | Người vận hành hạ Z bằng nút trên màn hình — điều kiện trên **không chạy**. Đây là lúc va chạm thật sự xảy ra (Chương 28 mục 28.2) |
| 2 | ⚠ **Không rà được** | Muốn trả lời *"có bao nhiêu ràng buộc chống va chạm?"* phải đọc hết chương trình. Không ai làm được việc đó ở buổi nghiệm thu |
| 3 | ⚠ **Sửa một chỗ, sót ba chỗ** | Cùng một ràng buộc được viết lại ở mọi nơi có lệnh hạ Z |

⭐ Cách đúng: **tính mọi điều kiện chống va chạm ở MỘT chỗ, thành một tập cờ riêng, và cơ cấu đọc cờ
đó như đọc một ngõ vào.**

```iecst
// ── TẦNG CHỐNG VA CHẠM — chạy mỗi vòng quét, TRƯỚC mọi trình tự ──
// Mỗi dòng là MỘT ràng buộc vật lý, đọc được như một câu tiếng Việt.

M_Itf_ZDown   := NOT DI_Clamp1Up;                      // chưa kẹp thì cấm hạ đầu công tác
M_Itf_ClampDn := NOT M_Z_AtSafeHeight;                 // đầu chưa lên cao thì cấm nhả kẹp   
M_Itf_Stop1Dn := DI_BoardStn1;                         // board còn tại trạm thì cấm hạ chặn
M_Itf_ConvRun := M_Stn1_ClampReq OR M_Stn2_ClampReq;   // còn kẹp thì cấm chạy băng

M_Itf_Any := M_Itf_ZDown OR M_Itf_ClampDn OR M_Itf_Stop1Dn OR M_Itf_ConvRun;
```

Rồi **mọi** đường ra lệnh — tự động, tay, về gốc, chạy khô — đều đi qua cùng một cửa:

```iecst
// Tầng cơ cấu: ngõ ra và yêu cầu chuyển động chỉ đi tiếp khi tầng này cho phép
DO_Stop1Vlv := (M_Stn1_StopReq  OR M_Stn1_StopManual)  AND NOT M_Itf_Stop1Dn;
DO_ConvRun  := (M_ConvRunReq    OR M_ConvRunManual)    AND NOT M_Itf_ConvRun;
M_Z_DownGo  := (M_Z_DownReq     OR M_Z_DownManual)     AND NOT M_Itf_ZDown;
```

> ⭐⭐ **Điểm mấu chốt: cờ chống va chạm nằm ở TẦNG CƠ CẤU, không ở tầng trình tự.** Nhờ vậy nó
> **không thể bị bỏ qua** bởi bất kỳ đường ra lệnh nào — kể cả chế độ tay, kể cả trình tự về gốc
> (Chương 28 mục 28.5).

### Báo động chống va chạm là một nhóm riêng

⭐ Khi một lệnh bị tầng này chặn, **phải báo** — và báo bằng một **nhóm báo động riêng**, không trộn
vào lỗi cơ cấu:

| Nhóm báo động | Nghĩa | Người xử lý |
|---|---|---|
| Lỗi **cơ cấu** | Van hỏng, cảm biến hỏng, quá thời gian | Thợ bảo trì |
| ⭐ Lỗi **chống va chạm** | Cơ cấu bình thường, nhưng **lệnh sai lúc** | ⭐ **Người viết chương trình** |

> ⭐⭐ **Hai nhóm này gọi hai người khác nhau tới máy.** Trộn chúng làm một là lý do thợ bảo trì thay
> một cái van hoàn toàn tốt.
>
> ⚡ Và một báo động chống va chạm ở máy đã nghiệm thu là **tín hiệu có lỗi thiết kế trình tự**, không
> phải sự cố vận hành. Nó nên được đếm và xem lại, không nên chỉ xác nhận rồi chạy tiếp.

### ⚠⚠ Cái tầng này KHÔNG làm

> ⚠⚠ **Tầng chống va chạm bảo vệ MÁY, không bảo vệ NGƯỜI.**
>
> Nó chạy trong CPU thường, nên nó chết cùng CPU. Mọi mối nguy với người vẫn phải do thiết bị an toàn
> xử lý, độc lập — Chương 47.
>
> ⭐ Cách phân biệt nhanh: *"nếu CPU treo giữa lúc này, ai bị thương?"* Trả lời được **"không ai"** thì
> nó thuộc tầng chống va chạm. Trả lời khác đi thì nó thuộc Chương 47, và không có ngoại lệ.

---

### ⭐ Khi "cơ cấu" lại là một bộ điều khiển khác

Xy-lanh là cơ cấu **không tự nghĩ**: bạn ra lệnh, nó làm. Nhưng có loại cơ cấu **mang theo bộ điều
khiển riêng** — có chương trình riêng, máy trạng thái riêng, và thường là **người lập trình riêng**.

⭐ **Quy tắc ba tầng vẫn giữ nguyên**: với tầng trạm, thứ đó vẫn chỉ là một cơ cấu có `Cmd` · `Data` ·
`Resp` (mục 30.3b). ⚠ Nhưng ba điều đổi, và cả ba đều đắt nếu phát hiện muộn:

| | Đổi ở chỗ nào |
|---|---|
| 1 | ⚠⚠ **Phải chốt AI CHỈ HUY AI trước khi viết dòng đầu tiên** — và chốt bằng văn bản, vì hai bên là hai người |
| 2 | ⚠ **Phục hồi khác hẳn**: cơ cấu đó có thể **đang giữ sản phẩm** và đang ở giữa chương trình của nó — không "về gốc" một phát là xong (Chương 28) |
| 3 | ⚠ **Nó có dữ liệu phải sao lưu** mà không nằm trong dự án PLC của bạn (Chương 54 mục 54.3, hạng mục 8) |

⭐ Loại cơ cấu này được nói kỹ ở **Chương 46** — mục 46.3 cho việc chỉ huy, 46.5 cho dữ liệu
phải sao lưu, 46.8 cho phục hồi.

---

## 27.3c ⭐⭐ Tầng ánh xạ vào/ra — nơi duy nhất chương trình chạm vào dây

Ba tầng ở mục 27.2 nói chương trình **nghĩ** thế nào. Dưới cả ba còn một lớp mỏng — nơi chương trình
**chạm vào dây**: đọc ngõ vào ở đầu vòng quét, ghi ngõ ra ở cuối. Chương 14 mục 14.7 và Chương 57 đặt
`Prg_IoRead` đứng đầu, `Prg_OutputMap` đứng cuối chương trình chính, nhưng chưa nói hai khối đó viết
thế nào. Mục này làm việc đó — vì đây là phần việc người lập trình được giao nhiều nhất trên mọi dự án,
và người trong nghề gọi nó bằng một chữ: **ánh xạ vào/ra** *(I/O mapping)*.

### Ba cách đọc ngõ vào — cùng một bài toán

Bài toán: hai tín hiệu của DP-01. `DI_BoardStn1` — cảm biến quang, có thể nháy ở mép board.
`DI_StopPB` — nút Stop, tiếp điểm NC.

| Cách | Viết thế nào | ⭐ Ưu | ⚠ Nhược |
|---|---|---|---|
| A — Đọc thẳng dây | Trình tự viết `IF DI_BoardStn1 THEN`; tầng máy, bộ đếm sản lượng cũng đọc `DI_BoardStn1` | Ít dòng nhất; người bảo trì thấy ngay sợi dây | ⚠ Lọc rung, mô phỏng (Chương 50), đổi kênh phải sửa ở **mọi** chỗ đọc; ⚠ trên hệ cập nhật I/O không đồng bộ với chương trình, hai chỗ đọc có thể thấy **hai giá trị** trong cùng một vòng quét (Chương 10 mục 10.5) |
| B — Chép đệm nguyên trạng *(I/O buffering)* | Đầu vòng quét `X_BoardStn1 := DI_BoardStn1;` — logic chỉ đọc `X_` | ⭐ Đổi kênh sửa **một** dòng; giá trị cố định suốt vòng quét. Rockwell gọi đây là *buffer I/O* và dựng ví dụ đúng ba phần: chép vào · logic của máy · chép ra | Không xử lý gì: nháy ở mép board vẫn đi thẳng vào logic |
| ⭐ C — Ánh xạ có xử lý | Đầu vòng quét: chọn nguồn thật hay mô phỏng → lọc → `X_BoardStn1`; còn `X_StopOK := DI_StopPB` đi thẳng | ⭐ Mọi thứ đặc thù của **một sợi dây** — lọc, mô phỏng, cực tính, đổi kênh — nằm ở **một chỗ**; logic đọc tín hiệu đã sạch | Thêm một tầng phải giữ khớp bảng I/O; tín hiệu đã lọc trễ đúng bằng thời gian lọc |

> ⭐ **Sách chọn C cho mọi máy có trình tự.** B là **mức tối thiểu** trên hệ cập nhật I/O không đồng bộ
> với chương trình — chính hãng khuyên vậy (Phụ lục A1 mục A1.5). A chỉ hợp lý cho chương trình rất
> nhỏ, không có mô phỏng — và là cách **bắt buộc** cho tín hiệu an toàn đọc trong phần an toàn, vốn
> không bao giờ đi qua lớp mô phỏng (Chương 50 mục 50.3).
>
> ⚡ Chương 26 đọc thẳng `DI_BoardStn1` trong trình tự là để ví dụ ngắn, tập trung vào trình tự.
> Chương 17 dựng khối lọc rung, Chương 50 mục 50.3 dựng lớp chọn nguồn — mục này ⭐ **ghép hai thứ đó
> thành một tầng**, và đặt tên theo quy ước `X_` ở Chương 30 mục 30.2: tín hiệu đã qua tầng ánh xạ giữ
> **đúng phần đuôi** của dây, `DI_BoardStn1` → `X_BoardStn1`, để tra chéo chỉ mất một bước.

### Tầng đọc vào làm năm việc — theo đúng thứ tự này

| # | Việc | Quy tắc | Vì sao |
|---|---|---|---|
| 1 | **Chọn nguồn** — dây thật hay giá trị mô phỏng *(simulation)* | `M_SimMode` chọn `Sim_…` thay cho `DI_…` | Mọi xử lý phía sau chạy **y hệt** khi mô phỏng — thử được cả bộ lọc. ⚠⚠ Tín hiệu an toàn **không có** nhánh mô phỏng (Chương 50 mục 50.3) |
| 2 | **Lọc rung** *(debounce)* | `FB_Debounce` của Chương 17; thời gian theo loại tín hiệu — Phụ lục O mục O.4 | Lọc phải đứng **trước** bắt cạnh (Phụ lục L mục L.7) |
| 3 | ⭐ **Đặt tên giữ nghĩa khi đứt dây** | Tên nói trạng thái mà `TRUE` biểu diễn. Tín hiệu NC giữ nghĩa **lành**: `X_StopOK`, cùng kiểu với `DI_EStopOK`, `DI_AirOK` | ⚠ Đảo thành *"đã nhấn"* thì người đọc nấc thang phải đảo lại lần nữa trong đầu, và cái tên gộp *nhấn nút* với *đứt dây* mà không nói ra (Chương 4 mục 4.2, Chương 15 mục 15.3) |
| 4 | ⚠ **Chiều an toàn đi thẳng** | Dừng, mất khí: chép thẳng — không lọc, không qua lớp mô phỏng (Chương 50 mục 50.3) | Lọc chỉ làm chậm phản ứng phía an toàn. Muốn chống báo giả thì đặt trễ ở **báo động** (Chương 44 mục 44.3), không đặt ở tín hiệu điều khiển |
| 5 | **Không suy luận** | Không ghép hai tín hiệu, không kiểm hai cảm biến của một xy-lanh | Đó là việc của khối cơ cấu (mục 27.3). Tầng ánh xạ chỉ trả lời *"dây đang nói gì"* |

### Tầng ghi ra — khối ngắn nhất, và ba điều cấm

| # | Quy tắc | Vì sao |
|---|---|---|
| 1 | Mỗi `DO_` **đúng một dòng**, và dòng đó nằm ở `Prg_OutputMap` | Cuộn dây trùng không thể xảy ra (Chương 15 Bẫy 1); tham chiếu chéo một `DO_` cho đúng một kết quả |
| 2 | Vế phải là **đầu ra của khối cơ cấu**, hoặc lệnh của **chủ duy nhất** ở tầng máy với tài nguyên chung (Bẫy 4) | Quyết định đã nằm ở tầng trên — tầng ghi ra chỉ **chép quyết định ra dây**. Quy tắc Q3 ở mục 27.2 vẫn đúng: khối cơ cấu **quyết định** van |
| 3 | ⚠ **Không `IF`, không liên động, không chặn chung** | Liên động thuộc `Permit` và tầng chống va chạm (mục 27.3, 27.3b). ⚠⚠ Và đừng thêm *"tắt mọi ngõ ra khi mô phỏng"* cho chắc: với van một cuộn, **tắt là ra lệnh chuyển động** (Bẫy 7) — bật cờ mô phỏng trên máy thật sẽ làm kẹp nhả, chặn hạ |

> ⚡ **Mục 27.3 ghi `DO_Clamp1Vlv := Clamp1.Valve;` ngay sau lời gọi khối — có mâu thuẫn không?**
> Không. Quy tắc là **một nơi ghi cho mỗi ngõ ra**, và cả hai cách đều giữ được. Gom về `Prg_OutputMap`
> có thêm hai cái lợi khi máy có hơn một trạm: mọi ngõ ra đọc được **trên một màn hình**, theo đúng thứ
> tự bảng I/O; và chúng được ghi **sau cùng**, khi mọi quyết định của vòng quét đã xong (Chương 14
> mục 14.7).

> ⚠⚠ **Khi CPU dừng, `Prg_OutputMap` không chạy.** Lúc đó ngõ ra theo **cấu hình phần cứng** — giữ
> giá trị cuối hay về giá trị thay thế (Chương 10 mục 10.5). Cấu hình ấy phải khớp cột *mất điện điều
> khiển* trong bảng trạng thái an toàn của từng ngõ ra (Chương 48 mục 48.2), và phải được **thử thật**
> trước khi bàn giao (Chương 52).

### Ví dụ hoàn chỉnh — tầng ánh xạ của DP-01

Ví dụ ánh xạ đủ **ba loại** tín hiệu — nút nhấn, cảm biến sản phẩm, reed của xy-lanh — và ghi bốn van
cùng lệnh chạy chuyền. Các reed còn lại viết y hệt dòng của `Clamp1`. Ví dụ viết bằng ST để chạy thử
được; trên DP-01, `Prg_OutputMap` vẽ bằng LD như Chương 14 mục 14.7 — mỗi dòng gán ở dưới là đúng
một nấc thang: một tiếp điểm, một cuộn dây.

```iecst
// ✔ VÍ DỤ HOÀN CHỈNH — tầng ánh xạ vào/ra của DP-01: chọn nguồn, lọc, đặt tên, ghi ra
//   Cần thêm: khối FB_Debounce (Chương 17) và FB_Cylinder2Pos (mục 27.3)
VAR_GLOBAL
    // ── dây thật — CHỈ hai chương trình dưới đây được chạm vào ──
    DI_StartPB, DI_StopPB, DI_ResetPB : BOOL;   // nút Stop là NC — bình thường TRUE
    DI_AirOK                          : BOOL;   // công tắc áp — TRUE khi đủ khí
    DI_BoardStn1, DI_BoardStn2        : BOOL;   // quang thu-phát, PNP
    DI_Clamp1Up, DI_Clamp1Dn          : BOOL;   // reed của xy-lanh kẹp trạm 1
    DO_ConvRun, DO_Stop1Vlv, DO_Clamp1Vlv, DO_Stop2Vlv, DO_Clamp2Vlv : BOOL;
    // ── tín hiệu đã qua tầng ánh xạ — phần còn lại của chương trình CHỈ đọc tên X_ ──
    X_StartPB, X_ResetPB      : BOOL;   // đã lọc nảy tiếp điểm, 20 ms
    X_StopOK                  : BOOL;   // TRUE = mạch Stop lành, không bị nhấn · nhấn hoặc đứt dây → FALSE
    X_AirOK                   : BOOL;   // đi thẳng, không lọc
    X_BoardStn1, X_BoardStn2  : BOOL;   // lọc hai chiều 50 ms — nháy ở mép board (Chương 17)
    X_Clamp1Up, X_Clamp1Dn    : BOOL;   // không lọc — khối cơ cấu đã giám sát thời gian
    // ── mô phỏng (Chương 50 mục 50.3) — ⚠ không giữ qua mất điện, không có cho tín hiệu an toàn ──
    M_SimMode                 : BOOL;
    Sim_BoardStn1, Sim_BoardStn2 : BOOL;
    Sim_Clamp1Up, Sim_Clamp1Dn   : BOOL;
    // ── nguồn của ngõ ra: tầng cơ cấu (mục 27.3) và chủ tài nguyên chung ở tầng máy (Bẫy 4) ──
    Stop1        : FB_Cylinder2Pos;
    Clamp1       : FB_Cylinder2Pos;
    Stop2        : FB_Cylinder2Pos;
    Clamp2       : FB_Cylinder2Pos;
    M_ConvRunCmd : BOOL;
END_VAR

PROGRAM Prg_IoRead
VAR_EXTERNAL
    DI_StartPB, DI_StopPB, DI_ResetPB, DI_AirOK            : BOOL;
    DI_BoardStn1, DI_BoardStn2, DI_Clamp1Up, DI_Clamp1Dn   : BOOL;
    X_StartPB, X_ResetPB, X_StopOK, X_AirOK                : BOOL;
    X_BoardStn1, X_BoardStn2, X_Clamp1Up, X_Clamp1Dn       : BOOL;
    M_SimMode                                              : BOOL;
    Sim_BoardStn1, Sim_BoardStn2, Sim_Clamp1Up, Sim_Clamp1Dn : BOOL;
END_VAR
VAR
    FltBoard1 : FB_Debounce;
    FltBoard2 : FB_Debounce;
    FltStart  : FB_Debounce;
    FltReset  : FB_Debounce;
    RawBoard1 : BOOL;                    // sau bước chọn nguồn, trước bộ lọc
    RawBoard2 : BOOL;
END_VAR

// ── 1 · Chọn nguồn. ⚠⚠ Tín hiệu an toàn KHÔNG BAO GIỜ đi qua đây (Chương 50 mục 50.3) ──
IF M_SimMode THEN
    RawBoard1  := Sim_BoardStn1;
    RawBoard2  := Sim_BoardStn2;
    X_Clamp1Up := Sim_Clamp1Up;
    X_Clamp1Dn := Sim_Clamp1Dn;
ELSE
    RawBoard1  := DI_BoardStn1;
    RawBoard2  := DI_BoardStn2;
    X_Clamp1Up := DI_Clamp1Up;
    X_Clamp1Dn := DI_Clamp1Dn;
END_IF;

// ── 2 · Lọc — mỗi thể hiện gọi đúng MỘT lần mỗi vòng, ngoài IF (Phụ lục N) ──
FltBoard1(Raw := RawBoard1, TimeOn := T#50MS, TimeOff := T#50MS);
FltBoard2(Raw := RawBoard2, TimeOn := T#50MS, TimeOff := T#50MS);
FltStart(Raw := DI_StartPB, TimeOn := T#20MS, TimeOff := T#20MS);
FltReset(Raw := DI_ResetPB, TimeOn := T#20MS, TimeOff := T#20MS);
X_BoardStn1 := FltBoard1.Out;
X_BoardStn2 := FltBoard2.Out;
X_StartPB   := FltStart.Out;
X_ResetPB   := FltReset.Out;

// ── 3 · Chiều an toàn đi THẲNG — không lọc, không mô phỏng ──
X_StopOK := DI_StopPB;        // NC: nhấn hoặc đứt dây → FALSE → dừng
X_AirOK  := DI_AirOK;         // trễ chống báo giả đặt ở Prg_Alarm, không đặt ở đây
END_PROGRAM

PROGRAM Prg_OutputMap
VAR_EXTERNAL
    DO_ConvRun, DO_Stop1Vlv, DO_Clamp1Vlv, DO_Stop2Vlv, DO_Clamp2Vlv : BOOL;
    Stop1, Clamp1, Stop2, Clamp2 : FB_Cylinder2Pos;
    M_ConvRunCmd : BOOL;
END_VAR

// Mỗi ngõ ra ĐÚNG MỘT dòng — không IF, không liên động, không chặn chung (mục 27.3c)
DO_ConvRun   := M_ConvRunCmd;     // chủ duy nhất: tầng máy
DO_Stop1Vlv  := Stop1.Valve;
DO_Clamp1Vlv := Clamp1.Valve;
DO_Stop2Vlv  := Stop2.Valve;
DO_Clamp2Vlv := Clamp2.Valve;
END_PROGRAM
```

Chạy thử, theo kịch bản trong bộ chạy thử của sách: board nháy ngắn hơn 50 ms **không** làm đổi
`X_BoardStn1`, ổn định đủ lâu thì được công nhận; bật mô phỏng thì `X_` theo giá trị giả còn dây thật bị
bỏ qua; ⭐ nhưng nhấn Stop **vẫn** làm `X_StopOK` về `FALSE` ngay trong vòng quét đó, kể cả khi đang mô
phỏng; nút Start nảy năm lần chỉ được công nhận một lần; và bật cờ mô phỏng **không** làm tắt van nào ở
tầng ghi ra.

### Bảng ánh xạ đạt khi nào

| # | Câu hỏi kiểm tra | Đạt khi |
|---|---|---|
| 1 | ⭐ Tham chiếu chéo `DI_` — kết quả nằm ở đâu? | **Chỉ** trong `Prg_IoRead` — trừ tín hiệu an toàn đọc trong phần an toàn |
| 2 | Tham chiếu chéo một `DO_` — mấy chỗ ghi? | Đúng một, trong `Prg_OutputMap` |
| 3 | Số dòng ánh xạ so với bảng I/O | Mỗi kênh chương trình dùng có đúng một dòng, theo thứ tự bảng I/O |
| 4 | Mỗi `X_` có chú thích loại tiếp điểm, thời gian lọc, có mô phỏng hay không? | Có |
| 5 | Tín hiệu nào có nhánh `Sim_`? | ⚠ Không tín hiệu an toàn nào |
| 6 | Rút dây một tín hiệu NC | `X_` về `FALSE`, máy về phía an toàn |

⭐ Con số cụ thể — thời gian lọc theo loại tín hiệu, cận dưới theo vòng quét, cận trên theo sản phẩm —
gom ở **Phụ lục O mục O.4 và O.5**, cùng các bước làm theo thứ tự.

---

## 27.4 Đồng bộ giữa hai trạm — không được chờ bận

Hai trạm của DP-01 chạy song song trên hai board khác nhau. Chúng cần phối hợp đúng **một** việc: trạm
1 chỉ được nhả board sang khi **trạm 2 đang trống**.

### Cách sai — trạm 1 nhìn vào ruột trạm 2

```iecst
// ✗ SAI — trạm 1 đọc biến nội bộ của trạm 2
IF Stn2_Step = 0 AND NOT DI_BoardStn2 THEN
    // nhả board sang
END_IF;
```

Vì sao sai, kể cả khi nó chạy:

- Trạm 1 giờ **phụ thuộc vào cách đánh số bước bên trong trạm 2**. Ai đó chèn thêm một bước vào trạm 2
  và đổi `Step 0` thành `Step 1` → trạm 1 hỏng, mà lỗi hiện ra ở trạm 1 chứ không ở nơi vừa sửa.
- Không ai đọc code trạm 2 mà biết được **có người khác đang phụ thuộc vào nó**.
- Đây chính là những "sợi dây vô hình" ở mục 27.1.

### Cách đúng — trạm 2 công bố một giao diện

Mỗi trạm công bố một **tập biến ra nhỏ, ổn định**, và đó là **thứ duy nhất** người khác được đọc:

```iecst
// Giao diện công bố của MỘT trạm — coi như hợp đồng, hạn chế thay đổi (kiểu ở Chương 11 mục 11.5)
TYPE ST_Station :                      // giao diện CÔNG BỐ của một trạm — chỉ trạm đó ghi
STRUCT
    Ready       : BOOL;                // sẵn sàng nhận board mới
    Busy        : BOOL;                // đang xử lý
    Fault       : BOOL;                // trạm có lỗi — cờ đã chốt (Chương 25 mục 25.5c)
    FaultStep   : INT;                 // bước lúc lỗi, 0 nếu không lỗi
    BoardDone   : BOOL;                // board đã xong, chờ chuyển đi
    DoneCount   : DINT;                // ⭐ DINT, không phải INT — sẽ tràn
    LastCycleMs : DINT;                // ⭐ đơn vị trong tên
END_STRUCT
END_TYPE

VAR_GLOBAL
    // ⭐ Toàn cục CÓ CHỦ Ý: nhiều phần cần đọc — và CHỈ trạm N được ghi vào StnN (Chương 11 mục 11.6)
    Stn1 : ST_Station;
    Stn2 : ST_Station;
END_VAR
```

⭐ Bước (`Stn2_Step`) **không** có trong kiểu này: nó là ruột, nằm trong chương trình của trạm 2.
Bên trong trạm 2, cứ đổi bao nhiêu bước tuỳ ý — miễn là các trường trên vẫn đúng nghĩa. Trạm 1 chỉ
đọc:

```iecst
// ✓ ĐÚNG — đọc giao diện đã công bố, không đọc ruột
IF Stn1.BoardDone AND Stn2.Ready THEN
    M_Stn1_ReleaseBoard := TRUE;
END_IF;
```

> ⚡ **LƯU Ý — "chờ bận" trong PLC nghĩa là gì**
> Trong lập trình thông thường, *chờ bận (busy-wait)* là vòng lặp quay tại chỗ đến khi điều kiện đúng.
> Trong PLC, viết vòng lặp như vậy **treo CPU** (Chương 20) — nên bạn sẽ không gặp dạng đó.
>
> Dạng nguy hiểm ở PLC là dạng **ẩn**: một trạm đứng yên ở một bước, mỗi vòng quét lại kiểm tra biến
> nội bộ của trạm khác. Nó không treo CPU, nhưng tạo ra đúng cái ràng buộc mà chờ bận tạo ra — **hai
> khối dính chặt vào nhau**. Cách chữa là như trên: chờ trên một **giao diện**, không chờ trên ruột.

### Ai quyết định khi có tranh chấp

Chuyền là tài nguyên **dùng chung**: cả hai trạm đều có lúc cần nó chạy. Nếu mỗi trạm tự bật
`DO_ConvRun` thì đó là cuộn dây trùng, và tệ hơn — hai trạm có thể yêu cầu ngược nhau.

Quy tắc: **tài nguyên dùng chung do tầng trên quản lý**. Hai trạm chỉ *yêu cầu*:

```iecst
VAR_GLOBAL
    M_Stn1_ConvReq : BOOL;     // trạm 1 nêu yêu cầu — chỉ trạm 1 ghi
    M_Stn2_ConvReq : BOOL;     // trạm 2 nêu yêu cầu — chỉ trạm 2 ghi
END_VAR

// Tầng máy quyết định — đúng MỘT nơi ghi vào ngõ ra chuyền
DO_ConvRun := (M_Stn1_ConvReq OR M_Stn2_ConvReq)
              AND M_MotionEnable
              AND (MachineState = Running OR MachineState = Homing);
```

---

## 27.5 Bài toán pipeline của DP-01

Đây là lý do DP-01 được thiết kế có hai trạm (Chương 1): nó buộc bạn gặp bài toán mà máy một trạm
không có.

### Hai trạm, hai board, một chỗ trống

Ở chế độ chạy ổn định, trong máy luôn có **hai board cùng lúc**: board A đang được xử lý ở trạm 1
trong khi board B đang được xử lý ở trạm 2. Ràng buộc duy nhất giữa hai trạm là: **board A chỉ đi sang
được khi trạm 2 đã nhả board B**.

Hệ quả về năng suất — và đây là điều nhiều người ngạc nhiên:

> **Chu kỳ của máy nhiều trạm bằng chu kỳ của trạm CHẬM NHẤT, không phải tổng các trạm.**

Nếu trạm 1 mất 8 giây và trạm 2 mất 12 giây, thì máy cho ra một board mỗi **12 giây** (cộng thời gian
chuyển), chứ không phải 20 giây. Trạm 2 là **nút cổ chai** *(bottleneck)*. Cải tiến trạm 1 xuống 5
giây **không làm máy nhanh hơn chút nào**. Chương 55 khai triển đầy đủ cách tính và cách tìm nút cổ chai.

### Bốn tình huống phải xử lý

Chạy ổn định thì đơn giản. Bốn tình huống sau mới là chỗ code phải đúng:

| Tình huống | Điều gì xảy ra | Trạm 1 phải làm gì |
|---|---|---|
| **Đổ đầy** *(startup)* — máy vừa chạy, chưa có board nào | Trạm 2 trống, chưa có gì để chờ | Chạy bình thường |
| **Xả cạn** *(shutdown)* — không còn board mới vào | Trạm 1 rỗng, trạm 2 vẫn còn board đang xử lý | Không được báo "hết việc" cho tới khi trạm 2 xong |
| **Trạm 2 chậm hơn** | Trạm 1 xong sớm, phải chờ | Giữ board, **không** nhả; báo `Stn1.BoardDone` và chờ `Stn2.Ready` |
| **Trạm 2 lỗi** | Trạm 2 dừng, board kẹt ở đó | Trạm 1 **không được** nhả board sang. Tuỳ chính sách: dừng cả máy, hoặc cho trạm 1 giữ board và chờ |

> 🔍 **BẪY — quên tình huống xả cạn**
> Người viết hay chỉ nghĩ tới chạy ổn định. Khi người vận hành nhấn dừng và không có board mới vào,
> trạm 1 rỗng và báo "xong việc" — máy tưởng đã hết, chuyển sang `Idle`, **trong khi trạm 2 vẫn còn
> một board đang xử lý dở**. Board đó bị bỏ lại trong máy.
>
> Điều kiện đúng để coi là hết việc: **mọi trạm đều rỗng**, không phải "trạm đầu rỗng".

---

## 27.6 Tác vụ — khi nào tách, khi nào đừng

**Tác vụ** *(task)* là một khối thực thi có chu kỳ riêng. Câu hỏi thường gặp: nên chia chương trình
thành nhiều tác vụ không?

**Câu trả lời mặc định: không.** Một tác vụ chu kỳ duy nhất là đủ cho gần như mọi máy cỡ DP-01.

Vì sao mặc định là không:

- Nhiều tác vụ đưa lại **tranh chấp giữa các khối** (Chương 10, Bẫy 5). Một tác vụ nhanh có thể đọc
  dữ liệu do tác vụ chậm ghi dở, và lỗi loại đó cực khó tái hiện.
- Thứ tự thực thi trở nên **khó suy luận**.
- Lợi ích thường được kỳ vọng — "chạy song song cho nhanh" — **không có thật** ở PLC một lõi: tổng
  thời gian không giảm, chỉ được chia nhỏ ra.

Khi nào tách là chính đáng:

| Lý do | Ví dụ |
|---|---|
| Có phần **thật sự cần chu kỳ nhanh hơn** phần còn lại | Vòng điều khiển cần cập nhật mỗi 1 ms trong khi máy chạy 10 ms |
| Có phần **chậm và không cấp bách**, kéo dài thời gian quét | Ghi log, xử lý chuỗi ký tự, trao đổi dữ liệu với hệ thống trên |
| Có phần chạy theo **sự kiện**, không theo chu kỳ | Xử lý ngắt từ bộ đếm tốc độ cao |

Nếu tách, quy tắc bắt buộc: **dữ liệu đi qua ranh giới tác vụ phải qua một vùng đệm rõ ràng**, không
đọc chéo biến trực tiếp.

> ⭐ **Bản 4 của IEC 61131-3 (2025) đưa công cụ chuẩn cho việc này vào chuẩn:** **mutex** — khối
> `MUTEX` với các phương thức khoá, mở, thử khoá — và **semaphore** (`SEMA`), kèm dạng hàm tương ứng.
> ⚠ Hệ bạn đang dùng có thể chưa theo bản 4 (Chương 14 mục 14.1); vùng đệm rõ ràng ở trên vẫn là
> cách chạy được trên **mọi** hệ.

### ⭐⭐ Chính tài liệu hãng cũng khuyên hạn chế số tác vụ

⭐ Lời khuyên *"mặc định là một tác vụ"* ở trên nghe như quan điểm cá nhân. ⚡ Nó không phải: tài
liệu quản lý tác vụ của hãng có hẳn một mục tên là **"thận trọng với số lượng tác vụ bạn dùng"**, và
nêu đúng hai hậu quả:

| Hậu quả khi quá nhiều tác vụ | Nghĩa là gì |
|---|---|
| Tác vụ nền **không kịp chạy xong** | Mỗi tác vụ lấy thời gian CPU của các tác vụ khác |
| ⚠⚠ Một tác vụ **chồng lên chính nó** *(overlap)* | Bị ngắt quá thường xuyên hoặc quá lâu → chưa chạy xong đã bị kích lần sau |

> ⭐⭐ **Và câu này của tài liệu hãng khép lại tranh luận "chạy song song cho nhanh":** ⚡ *bộ điều
> khiển chỉ chạy **một** tác vụ tại một thời điểm.* ⭐ Nhiều tác vụ **không** làm máy nhanh hơn — nó
> chỉ đổi **thứ tự** và **độ ưu tiên**, và đổi lấy một lớp phức tạp mới.

### ⚠⚠ Hai thứ đi kèm mỗi tác vụ mà người mới hay bỏ qua

**Một — điều kiện chồng tác vụ, và nó là một phép tính bạn phải làm.**

> ⚠ Chu kỳ của tác vụ định kỳ **phải dài hơn tổng thời gian chạy của MỌI chương trình gán vào tác vụ
> đó**. ⭐ Không thoả thì tác vụ bị kích lại khi đang chạy dở → hệ báo **lỗi nhẹ** *(minor fault)*.
>
> ⚡ Và đây là lỗi **không xuất hiện lúc nghiệm thu**: nó xuất hiện tháng sau, khi ai đó thêm vài
> khối vào đúng tác vụ đó. ⭐ Giống hệt cơ chế trôi dạt ở Chương 36 — ⚠ nên **ghi lại thời gian chạy
> thật của từng tác vụ lúc nghiệm thu** (Chương 52).

**Hai — mỗi tác vụ có watchdog riêng của nó.**

⭐ Chương 10 mục 10.4 nói về watchdog của **cả vòng quét**. ⚡ Khi đã tách tác vụ thì ⭐ **mỗi tác vụ
mang một watchdog riêng**, đặt riêng — nghĩa là bạn vừa có thêm một chỗ phải đặt đúng, vừa có thêm
một chỗ có thể đặt sai.

### ⭐ Ba loại tác vụ, và con số đi kèm

| Loại | Chạy khi nào | ⭐ Con số đáng nhớ |
|---|---|---|
| **Liên tục** *(continuous)* | Chạy bằng thời gian CPU còn thừa; quét xong là **khởi động lại ngay** | ⭐ Dự án **không bắt buộc** phải có; và nếu có thì ⭐⭐ **chỉ được MỘT** |
| **Định kỳ** *(periodic)* | Đúng chu kỳ đặt trước; ngắt các tác vụ ưu tiên thấp hơn, chạy một lần, trả quyền | Chu kỳ đặt được từ **0,1 ms tới 2000 s**; mặc định **10 ms** |
| **Theo sự kiện** *(event)* | Khi có kích hoạt: ngõ vào số đổi trạng thái · có mẫu analog mới · lệnh sinh sự kiện… | ⚠ **Không phải bộ điều khiển nào cũng hỗ trợ đủ mọi loại kích hoạt** |

> ⭐ **Mức ưu tiên là một con số, và nó có một giá trị đặc biệt.** Ở dòng bộ điều khiển đó có **15**
> mức ưu tiên, và ⭐⭐ **tác vụ xử lý I/O của hệ chạy ở mức 6**. Nên đặt tác vụ của bạn ở mức 1–5
> nghĩa là **cho nó chen ngang cả việc cập nhật I/O**; đặt ở 7–15 nghĩa là để I/O chen ngang nó.
>
> ⚠ Con số 15 **không phải hằng số của ngành** — cùng hãng đó, dòng chạy trên máy tính chỉ có **3**
> mức. ⭐ Đây là lý do mọi con số trong mục này phải **tra lại theo đúng dòng bộ điều khiển bạn
> dùng**, chứ không chép từ máy trước.

> ⚡ **Tên gọi và mô hình khác nhau giữa các hãng** — có hệ bắt khai báo tác vụ tường minh, có hệ
> dùng khối tổ chức với lớp ưu tiên sẵn, có hệ chỉ có chương trình chính quét tuần tự. ⭐ Đối chiếu
> năm hệ: **Phụ lục A1**.

### Thứ tự gọi trong một tác vụ

Trong tác vụ duy nhất, thứ tự gọi các khối **là một phần của thiết kế** (Chương 10):

```text
1. Đọc và xử lý tín hiệu vào     (lọc, bắt cạnh, tính cờ điều kiện)
2. Tầng cơ cấu                    (các FB xy-lanh — tính Done/Fault)
3. Gom lỗi                        (M_AnyFault — đúng MỘT chỗ gán, Chương 25 mục 25.5c)
4. Tầng máy                       (máy trạng thái — dùng M_AnyFault vừa gom)
5. Tầng trạm                      (trình tự — dùng Done vừa tính, ra yêu cầu)
6. Gom yêu cầu → ghi ngõ ra       (đúng một nơi cho mỗi ngõ ra)
7. Hiển thị, đèn tháp, ghi log
```

Thứ tự này không tuỳ ý. Tầng cơ cấu chạy **trước** để `Done` và `Fault` là của **vòng quét này**; nếu
gọi sau, tầng trạm sẽ dùng giá trị của vòng quét trước và mọi phản ứng chậm thêm một chu kỳ.

⚠⚠ Nhưng *"Done của vòng này"* là Done **của yêu cầu mà khối đã nhận** — tức yêu cầu của vòng trước.
Yêu cầu tầng trạm vừa phát ở vòng này thì **chưa khối nào nhìn thấy**. Hệ quả thực hành: trạm phát yêu
cầu ở **chuyển tiếp**, bước sau mới đọc `Done` — viết ngược lại thì trình tự nhảy qua bước mà không chờ
(Chương 26 Bẫy 7; ví dụ hoàn chỉnh ở Chương 26 mục 26.5b đã chạy thử theo đúng thứ tự gọi này). ⭐ Gom
lỗi đứng ngay trước tầng máy vì cùng lý do: máy vào `Alarm` **trong chính vòng quét** lỗi được chốt.

---

## 27.7 Bẫy thường gặp

### 🔍 BẪY 1 — Chép trình tự trạm 1 sang làm trạm 2

Cách nhanh nhất, và là cách sinh ra máy không bảo trì được. Sáu tháng sau, hai bản chép đã lệch nhau:
một bên được sửa lỗi, bên kia không. Không ai nhớ chúng từng giống nhau.

**Cách đúng:** nếu hai trạm cùng loại, viết **một khối trạm** rồi tạo hai thể hiện, đúng như cách làm
với khối cơ cấu. Nếu hai trạm khác loại (như DP-01: tra keo và sấy), viết hai khối riêng nhưng **cùng
một giao diện công bố** — cùng bốn biến `Ready/Busy/Fault/BoardDone`. Nhờ giao diện giống nhau, tầng
máy đối xử với mọi trạm như nhau.

### 🔍 BẪY 2 — Tầng trạm ghi thẳng ngõ ra

```iecst
// ✗ SAI — trạm chạm thẳng vào van
IF Stn1_Step = 20 THEN
    DO_Clamp1Vlv := TRUE;
END_IF;
```

Vi phạm Q3. Hậu quả: nếu chế độ tay cũng ghi vào van đó thì có cuộn dây trùng; và liên động chống va
chạm phải lặp lại ở mọi chỗ.

```iecst
// ✓ ĐÚNG — trạm nêu yêu cầu, khối cơ cấu thực hiện
IF Stn1_Step = 20 THEN
    M_Stn1_ClampReq := TRUE;
END_IF;
```

### 🔍 BẪY 3 — Giao diện trạm phình to

Bắt đầu bằng bốn biến. Rồi có người cần biết thêm một thứ, thêm biến thứ năm. Rồi thứ sáu. Sau một
năm, giao diện có hai mươi biến và trạm lại **hở ruột** như cũ.

**Cách phòng:** coi giao diện là **hợp đồng**. Thêm biến vào giao diện là một quyết định thiết kế, phải
tự hỏi: *"người ngoài có thật sự cần biết điều này, hay họ chỉ đang muốn nhìn trộm vào ruột?"* Thường
là vế sau, và câu trả lời đúng là sửa lại chỗ gọi chứ không mở rộng giao diện.

### 🔍 BẪY 4 — Tài nguyên dùng chung không có chủ

Hai trạm cùng cần chuyền. Cả hai cùng ghi `DO_ConvRun`. Kết quả: cuộn dây trùng, và trạm chạy sau thắng.

Mọi tài nguyên mà **nhiều hơn một trạm** cần đến — chuyền, nguồn khí, đèn tháp, kết nối lên hệ thống
trên — phải có **đúng một chủ ở tầng máy**. Các trạm chỉ nêu yêu cầu.

### 🔍 BẪY 5 — Tầng máy biết quá nhiều về trạm

Ngược lại với Bẫy 3 nhưng cùng bản chất:

```iecst
// ✗ SAI — tầng máy đọc bước bên trong trạm
IF Stn1_Step = 40 AND Stn2_Step = 10 THEN
    DO_LampYellow := TRUE;
END_IF;
```

Tầng máy chỉ được biết trạm **rỗng / bận / lỗi**, không được biết trạm đang ở bước nào. Nếu bạn thấy
tầng máy cần biết số bước, nghĩa là **trách nhiệm đã đặt sai tầng** — việc đó thuộc về trạm.

### 🔍 BẪY 6 — Tách tác vụ để "cho nhanh"

Đã nêu ở mục 27.6. Nhắc lại ở đây vì đây là quyết định **khó sửa về sau**: một khi chương trình đã chia
tác vụ và dữ liệu đọc chéo lẫn nhau, gộp lại rất tốn công. Mặc định một tác vụ; chỉ tách khi có **yêu
cầu định lượng về thời gian** viết ra được thành con số.

### 🔍 BẪY 7 — Cổng cho phép viết bằng phép AND vào van

```iecst
// ✗ SAI với van 5/2 lò xo về — trông đúng, và chạy đúng cho tới lần Alarm đầu tiên
Valve := Req AND Permit AND NOT Fault;
```

⚠⚠ Dòng này nói *"không được phép thì tắt van"*. Nhưng với van một cuộn, **tắt van là ra lệnh cho
xy-lanh chạy về vị trí lò xo**. Máy vào `Alarm` (Chương 25 cắt `M_MotionEnable`) → mọi van tắt → kẹp
nhả, chặn hạ — đúng lúc máy đang báo có sự cố. ⭐ Và thêm `NOT Fault` thì **một cảm biến hỏng** cũng
đủ làm cơ cấu chuyển động.

Có ba cách đặt cổng cho phép vào khối cơ cấu:

| Cách | Viết thế nào | ⭐ Ưu | ⚠ Nhược |
|---|---|---|---|
| A — AND vào van | `Valve := Req AND Permit` | Ngắn; *"mất phép là tắt"* dễ nói | ⚠⚠ Mất phép **gây ra** chuyển động — về lò xo. Trái SF6 của DP-01 |
| ⭐ B — **Giữ lệnh khi mất phép** | `IF Permit THEN Valve := Req; END_IF;` | ⭐ Mất phép = **không có chuyển động MỚI**; vị trí hiện tại được giữ. Đúng nghĩa *"dừng"* của `Hold` và `Alarm` (Chương 25) | Khối có nhớ; `Done` phải so với **yêu cầu** để không báo xong nhầm (bảng ở mục 27.3) |
| C — Không có cổng trong khối | `Valve := Req;` — liên động đặt ở tầng trạm | Khối đơn giản nhất | ⚠ Liên động rải ở mọi chỗ ra yêu cầu — mất đúng cái lợi thứ 4 của khối |

⭐ **Sách chọn B.** ⚡ Muốn đưa cơ cấu về một vị trí **xác định** khi có sự cố thì đó là **một quyết
định phục hồi** (Chương 28) hoặc **một chức năng an toàn** (Chương 47, 48) — nó phải được **viết ra có
chủ ý**, không phải xảy ra như tác dụng phụ của việc mất một bit cho phép.

> ⚠ **Vì sao chân này tên là `Permit`, không phải `Enable`?** PLCopen dành chữ `Enable` cho khối
> **điều khiển theo mức**: `Enable` tắt thì khối **ngừng và xoá ngõ ra** (Chương 30 mục 30.5b). Người
> quen quy ước đó đọc `Enable` = FALSE là *"tắt van"* — ⚠ đúng cách A. Tên chân phải nói đúng nghĩa
> của nó.

> ⚠ **Với van HAI cuộn thì sao?** Van hai cuộn tự giữ vị trí khi mất điện (Chương 6), nên cách A
> không làm xy-lanh chạy. Nhưng khối vẫn nên theo cách B: ⭐ cùng một khối, cùng một nghĩa của
> `Permit`, cho **mọi** loại van — người đọc chương trình không phải nhớ loại van nào đang lắp.

### 🔍 BẪY 8 — Có tầng ánh xạ rồi mà vẫn đọc `DI_` ở chỗ khác

**Hiện tượng:** bật mô phỏng thì trạm chạy đúng nhưng bộ đếm sản lượng đứng im — vì nó vẫn đọc
`DI_BoardStn1`. Hoặc ngược lại trên máy thật: trình tự đọc `X_BoardStn1` đã lọc, còn tầng máy đọc
`DI_BoardStn1` thô và đếm đôi mỗi khi board nháy. ⚠ Máy chạy **nửa thật nửa giả**, và mỗi nửa cho một
câu trả lời khác nhau về cùng một sợi dây.

**Cách sửa:** tham chiếu chéo `DI_` (mục 27.3c, bảng đạt khi dòng 1). ⭐ Một chỗ đọc vòng qua tầng ánh
xạ là **lỗi**, không phải phong cách.

### 🔍 BẪY 9 — Lọc tín hiệu dừng "cho đỡ nhiễu"

**Hiện tượng:** ai đó thấy nút Stop thỉnh thoảng làm máy dừng giả, nên cho nó qua bộ lọc 50 ms — hoặc
lọc `DI_AirOK` hai giây để khỏi báo mất khí giả. Từ đó, mỗi lần nhấn Stop máy đi thêm một quãng, và khi
khí tụt thật thì cơ cấu đã kịp chạy thêm hai giây trên khí yếu.

**Cách sửa:** chiều an toàn **đi thẳng** ở tầng ánh xạ (mục 27.3c, việc 4). Muốn chống báo giả thì đặt
trễ ở **báo động** (Chương 44 mục 44.3); còn dừng giả thật sự thì tìm nguyên nhân — dây, đầu cốt, nhiễu
(Chương 49) — chứ không làm chậm cái nút.

---

## 27.8 Bảng chốt — kiểm tra kiến trúc

Dùng bảng này khi rà soát chương trình của mình hoặc của người khác.

| # | Câu hỏi kiểm tra | Đạt khi |
|---|---|---|
| 1 | Mỗi ngõ ra vật lý được ghi ở **mấy nơi**? | Đúng một |
| 2 | Có dòng nào ở tầng trạm/máy ghi thẳng `DO_…` không? | Không |
| 3 | Trạm A có đọc biến nội bộ của trạm B không? | Không — chỉ đọc giao diện công bố |
| 4 | Tầng máy có đọc số bước của trạm không? | Không |
| 5 | Mọi cơ cấu cùng loại có dùng **chung một khối** không? | Có |
| 6 | Mọi cơ cấu có **timeout** và phát hiện **tư thế giữa chừng** không? | Có — nằm trong khối, không sót cái nào |
| 7 | Tài nguyên dùng chung có **đúng một chủ** không? | Có, ở tầng máy |
| 8 | Thứ tự gọi có đúng **cơ cấu → máy → trạm → ghi ngõ ra** không? | Có |
| 9 | Có bao nhiêu tác vụ? Mỗi tác vụ thêm có **lý do định lượng** không? | Một, trừ khi có con số biện minh |
| 10 | Điều kiện "hết việc" có kiểm **mọi trạm** không? | Có — không chỉ trạm đầu |
| 11 | ⭐ Cách chia có **soi gương ranh giới vật lý** của máy không? | Có — người đứng trước máy suy ra được |
| 12 | ⚠ Hai việc chạy **cùng lúc** có bị gộp vào một khối không? | Không |
| 13 | ⚠⚠ Mất `Permit` thì van **giữ nguyên** hay **tắt**? | Giữ nguyên — tắt van một cuộn là ra lệnh chuyển động (Bẫy 7) |
| 14 | ⭐ Mỗi `DI_` được đọc ở **mấy nơi**? | Một — trong `Prg_IoRead`; tín hiệu an toàn đọc trong phần an toàn (mục 27.3c) |
| 15 | ⚠ Tín hiệu dừng, mất khí có bị lọc hay mô phỏng không? | Không — chiều an toàn đi thẳng (Bẫy 9) |

---

## 27.9 Tự kiểm

1. Nêu **ba quy tắc gọi** giữa các tầng, và giải thích quy tắc Q3 trả lại lợi ích gì.
2. Vì sao trạm 1 đọc `Stn2_Step = 0` là sai, dù đoạn code đó **chạy đúng** ở thời điểm viết?
3. Khối `FB_Cylinder2Pos` cho bạn **bốn thứ** mà code rải rác không cho. Kể đủ bốn.
4. Vì sao cả hai cảm biến của một xy-lanh cùng bật là tình huống phải báo lỗi ngay, chứ không phải là
   một tư thế bình thường?
5. Trạm 1 mất 8 giây, trạm 2 mất 12 giây. Máy cho ra một board mỗi bao nhiêu giây? Nếu cải tiến trạm 1
   xuống 5 giây thì năng suất đổi thế nào — **vì sao**?
6. Mô tả tình huống **xả cạn** và cho biết điều kiện đúng để máy coi là đã hết việc.
7. Hai trạm cùng cần chuyền chạy. Ai được ghi vào `DO_ConvRun`, và hai trạm làm gì?
8. Khi nào tách tác vụ là chính đáng? Nêu **một lý do đúng** và **một lý do sai** thường gặp.
9. ⭐⭐ Nêu **bốn câu hỏi** để tự chia một bài toán điều khiển. ⭐ Câu nào đáng tin nhất, và vì sao?
10. ⚠ Một chương trình chia theo **loại thiết bị** (*"mọi xy-lanh vào một khối"*). Nêu vì sao cách chia
    đó gây khó cho người bảo trì, dù bản thân code có thể chạy đúng.
11. ⭐ Vì sao Chương 23 (từ yêu cầu tới đặc tả) phải đứng **trước** chương này? Chuyện gì xảy ra khi
    chia kiến trúc lúc mới hiểu một nửa quy trình?
12. ⚠⚠ `Valve := Req AND Permit` trông đúng. Vì sao nó sai với van 5/2 lò xo về, và hậu quả trên
    DP-01 khi máy vào `Alarm` lúc board đang bị kẹp là gì? Khối `FB_Cylinder2Pos` tránh nó bằng cách nào,
    và vì sao khi đó `Done` phải so với **yêu cầu** chứ không chỉ với van?
13. ⭐ Ba cách đọc ngõ vào — đọc thẳng dây, chép đệm, ánh xạ có xử lý — khác nhau ở đâu? Trên hệ cập
    nhật I/O **không đồng bộ** với chương trình, cách nào là tối thiểu, và vì sao?
14. ⚠ Vì sao tầng ghi ra **không** được có dòng *"tắt mọi ngõ ra khi mô phỏng"*, dù nghe rất an toàn?
    Và khi CPU dừng thì cái gì quyết định trạng thái ngõ ra?

Câu 2 và câu 5 là hai câu phân loại. Câu 2 kiểm tra bạn phân biệt được *chạy đúng* với *thiết kế đúng*;
câu 5 kiểm tra bạn hiểu nút cổ chai — thứ quyết định mọi quyết định cải tiến năng suất về sau.

---

### Chương tiếp theo

**Chương 28 — Chế độ vận hành & phục hồi sau lỗi.** Kiến trúc đã có, trình tự đã có. Còn một câu hỏi
chưa trả lời: khi máy dừng giữa chừng ở một tư thế bất kỳ, làm cách nào đưa nó về gốc mà không phá gì?
Đó là bài toán khó nhất của nghề này.

---

### Nguồn tham khảo chương 27

- **Stefan Henneken** — *IEC 61131-3: Comparison of Edition 3 and Edition 4* (6/2025): bản 4 thêm chương
  *đồng bộ thực thi song song* — khối `MUTEX`, `SEMA` và dạng hàm — nền cho ghi chú ở mục 27.6.
- IEC 61131-3 — *Programmable controllers, Part 3: Programming languages*: khối chức năng, thể hiện,
  đơn vị tổ chức chương trình, và mô hình tác vụ. *(tiêu chuẩn có bản quyền; chương này chỉ diễn giải
  ở mức khái niệm)*
- Tài liệu hãng về tổ chức tác vụ, chương trình và khối tái dùng — dùng để đối chiếu khác biệt; số hiệu
  cụ thể ghi trong Phụ lục A1.
- Cấu hình cơ cấu và đặc tả trình tự hai trạm của DP-01 — Phụ lục J.
- **Rockwell Automation** — *Logix 5000 Controllers Tasks, Programs, and Routines* (1756-PM005,
  bản 9/2025), ch. 1 *Manage Tasks*: ⭐ mục **"thận trọng với số lượng tác vụ"** và câu ⭐⭐ *bộ điều
  khiển chỉ chạy **một** tác vụ tại một thời điểm* — nền cho lời khuyên "mặc định một tác vụ" ở mục
  27.6; ba loại tác vụ (liên tục — ⭐ **chỉ được một** và **không bắt buộc có** · định kỳ
  **0,1 ms–2000 s**, mặc định **10 ms** · theo sự kiện); ⚠⚠ **lỗi nhẹ khi tác vụ chồng lên chính
  nó** nếu chu kỳ ngắn hơn tổng thời gian chạy; **watchdog riêng cho từng tác vụ**; và 15 mức ưu
  tiên với ⭐ **tác vụ I/O của hệ ở mức 6** (⚠ dòng chạy trên máy tính chỉ có 3 mức).
- **Hugh Jack** — *Automating Manufacturing Systems with PLCs*, §32.4.1 *Developing a Program
  Structure*: ⭐ **bốn câu hỏi để chia bài toán điều khiển** (chạy cùng lúc? · độc lập? · có trình tự
  rõ? · ⭐ **có ranh giới vật lý?**), và ⚠ điều kiện tiên quyết *hiểu quy trình trước* — nền cho
  mục 27.2.
- **PLCopen** — *Structuring Program Development with IEC 61131-3*: ⭐⭐ **bảy bước dựng cấu trúc**
  (nền cho mục 27.2b), năm nguyên tắc mô-đun hoá (giao diện ít và nhỏ, tương tác khai báo tường minh,
  đóng gói dữ liệu), ⚠ **giới hạn của việc chia nhỏ** — chia quá tay thì công sức chuyển sang việc
  ghép, và bốn nguyên tắc đi kèm (chỉ dùng tên tượng trưng · để phần thuộc về nhau cạnh nhau ·
  không dùng lệnh nhảy · đặt tên nhất quán). *(tài liệu mở của PLCopen)*
- **Rockwell Automation** — *Logix 5000 Controllers I/O and Tag Data* (1756-PM004, bản 11/2023), mục
  *Buffer I/O*: ⭐ logic không tham chiếu thẳng tag của thiết bị thật mà dùng **bản sao**, vì I/O cập
  nhật không đồng bộ với chương trình; ví dụ của hãng gọi lần lượt `map_inputs` · logic của máy ·
  `map_outputs` — nền cho cách B và C ở mục 27.3c. Kiểm 2026-10-01.

> ⚡ Ba tầng ở mục 27.2 là **cách tổ chức thực dụng đã được kiểm chứng cho máy tự động hoá rời rạc**,
> không phải một kiến trúc chuẩn hoá bắt buộc. Máy rất nhỏ có thể gộp tầng trạm vào tầng máy; máy rất
> lớn có thể cần thêm tầng dây chuyền phía trên. Điều bắt buộc là **ba quy tắc gọi**, không phải con
> số ba.
