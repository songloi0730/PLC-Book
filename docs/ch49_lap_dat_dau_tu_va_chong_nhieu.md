
# Chương 49 — Lắp đặt, đấu tủ & chống nhiễu

> **Lát cắt máy mẫu:** 5 — máy đầy đủ, gồm cả mạch an toàn, analog, chuyển động và mạng.

---

> ⚠⚠ **ĐỌC TRƯỚC — phạm vi và giới hạn của chương này**
>
> Chương này bàn về **đấu tủ điện và đi dây trên máy** — công việc có điện áp nguy hiểm.
>
> Nó giúp bạn **hiểu vì sao tủ được đấu như vậy** và **đặt đúng câu hỏi** với người làm tủ. Nó
> **không**:
> - không thay thế **kiến thức và giấy phép an toàn điện** — đọc Chương 3 trước;
> - không thay thế **thiết kế điện** do người có chuyên môn thực hiện;
> - không thay thế **quy định của cơ sở** và tiêu chuẩn hiện hành tại thị trường của bạn.
>
> Phần đấu nối điện lưới và phần mạch an toàn phải do **người có thẩm quyền** làm hoặc kiểm tra.

---

## 49.1 Bài toán: lỗi "ngẫu nhiên" mất ba tuần

Một cỗ máy chạy tốt khi nghiệm thu. Sau khi lắp vào chuyền, nó bắt đầu có lỗi **ngẫu nhiên**: thỉnh
thoảng một cảm biến báo sai, thỉnh thoảng mạng rớt, thỉnh thoảng CPU khởi động lại.

Không có quy luật rõ ràng. Không tái hiện được. Người ta đổi cảm biến, đổi module I/O, nạp lại chương
trình, thay cáp mạng. Lỗi vẫn còn.

Ba tuần sau, tìm ra: **cáp tín hiệu analog và cáp động cơ của biến tần đi chung một máng, song song
nhau khoảng bốn mét**. Lỗi xuất hiện đúng lúc biến tần chạy tải nặng — nhưng vì chuyền chạy liên tục
nên không ai nối được hai việc đó với nhau.

Sửa mất hai giờ: tách máng.

> ⭐ **Ba tuần đi tìm cho một sai lầm mất hai giờ để sửa — nhưng chỉ nếu bạn biết chỗ nhìn.**
>
> Đây là mẫu chung của cả chương: **lỗi do lắp đặt không giống lỗi lắp đặt.** Nó giống lỗi phần mềm,
> lỗi cảm biến, lỗi module — bất cứ thứ gì trừ thứ thật sự sai.

---

## 49.2 Vì sao người lập trình phải đọc chương này

Bạn không đấu tủ. Nhưng:

| Lý do | Chương liên quan |
|---|---|
| ⭐ **Bạn là người đi tìm lỗi** khi máy chạy sai | Chương 51 |
| Rất nhiều "lỗi phần mềm" là lỗi lắp đặt | Chương 8 (nguồn), 31 (nhiễu analog), 36 (biến tần) |
| Bạn quyết định những thứ có hậu quả về đi dây | Chương 4, 9, 40 |
| ⭐ Bạn phải **nghiệm thu** phần đấu tủ | Chương 52, mục 52.3 |

> ⭐ **Mục tiêu của chương: khi máy có lỗi chập chờn, bạn biết nghi vào đâu — và biết hỏi câu gì.**

---

## 49.3 ⭐ Tách cáp — quy tắc quan trọng nhất

Ba nhóm cáp, và chúng **không được đi chung**:

| Nhóm | Gồm gì | Đặc tính |
|---|---|---|
| ⚡ **Động lực** | Cáp động cơ từ biến tần, cáp gia nhiệt, cáp hàn, cáp contactor | ⭐ **Nguồn nhiễu mạnh nhất** |
| 📶 **Tín hiệu** | Cảm biến, analog, encoder, mạng, truyền thông | ⭐ **Nạn nhân của nhiễu** |
| 🔴 **An toàn** | Mạch dừng khẩn, khoá cửa, rèm quang | ⚠ Đi riêng — xem bên dưới |

### Quy tắc

| Quy tắc | Nội dung |
|---|---|
| ⭐ **Máng riêng cho từng nhóm** | Tốt nhất; khoảng cách càng xa càng tốt |
| **Nếu chung máng thì có vách ngăn kim loại** | Ngăn nối đất |
| ⭐ **Giao nhau thì cắt VUÔNG GÓC** | Ghép nhiễu nhỏ nhất ở góc 90° |
| ⚠ **Không đi song song đường dài** | Đây chính là cỗ máy ở mục 49.1 |
| Cáp động cơ biến tần | ⭐ **Có vỏ chống nhiễu, nối vỏ hai đầu** (Chương 36, mục 36.7) |

```text
   ✓ ĐÚNG — cắt vuông góc
        ═══════════ động lực ═══════════
                    ║
        ────────────╫──────────── tín hiệu
                    ║

   ✗ SAI — song song đường dài
        ═══════════ động lực ═══════════
        ─────────── tín hiệu ───────────
```

> ⚠ **Vì sao mạch an toàn đi riêng?**
> Không phải vì nhiễu — mà vì **rõ ràng khi kiểm tra**. Mạch an toàn phải nhận diện được, truy được
> đường đi, và không lẫn với dây khác. Nhiều nơi quy định **màu dây riêng** cho mạch an toàn.
>
> Đây là yêu cầu thuộc Chương 47, và người kiểm định sẽ tìm nó.

---

## 49.4 ⭐⭐ Nối đất — PE không phải 0 V

Đây là hiểu nhầm gây nhiều lỗi nhất trong chương, và nó rất phổ biến.

### Hai thứ khác nhau

| | **PE** — dây bảo vệ *(protective earth)* | **0 V** — mát của mạch 24 V |
|---|---|---|
| Mục đích | ⭐ **An toàn cho người** — dẫn dòng sự cố về đất | Đường về của dòng mạch điều khiển |
| Dòng chạy qua khi bình thường | ⭐ **Gần như không có** | ⭐ **Toàn bộ dòng tải 24 V** |
| Tiết diện | Theo tiêu chuẩn an toàn | Theo dòng tải |
| Nối vào đâu | Vỏ tủ, vỏ thiết bị, thanh PE | Cực âm bộ nguồn |

> ⚠⚠ **Nối chúng ở nhiều điểm tạo ra vòng lặp đất.**
>
> Nếu 0 V và PE nối với nhau ở **hai chỗ khác nhau**, thì dòng 24 V có **hai đường về** — và một phần
> dòng đó chạy qua PE, qua khung máy, qua máng cáp. Dòng đó sinh ra nhiễu, và nó chạy qua đúng những
> chỗ mà cáp tín hiệu đang đi cạnh.
>
> ⭐ **Nếu cần nối 0 V với PE, nối ở ĐÚNG MỘT ĐIỂM** — thường tại bộ nguồn. Ghi rõ điểm đó vào bản
> vẽ.

### Triệu chứng của vòng lặp đất

| Triệu chứng | Ghi chú |
|---|---|
| Giá trị analog **run** hoặc **trôi** | Chương 31, mục 31.6 |
| Mạng rớt gói ngẫu nhiên | Chương 40 |
| Nhiễu tăng khi thiết bị công suất chạy | ⭐ Dấu hiệu đặc trưng |
| Đo được **điện áp giữa hai điểm đất** ở hai đầu máy | ⭐ Cách xác nhận |

> 💡 **Cách kiểm nhanh:** đo điện áp xoay chiều giữa vỏ tủ và vỏ thiết bị ở xa. Nếu có vài vôn, bạn
> có chênh lệch điện thế đất — và mọi cáp nối hai đầu đó đang chịu nó.

### ⭐ Vỏ chống nhiễu — hai quy tắc khác nhau

Chương 31 mục 31.6 và Chương 36 mục 36.7 đã nêu, gom lại đây vì đây là chỗ dễ nhầm nhất:

| Loại cáp | Nối vỏ | Vì sao |
|---|---|---|
| **Tín hiệu analog, cảm biến** | ⭐ **Một đầu** — thường phía tủ | Tránh dòng vòng qua vỏ ở tần số thấp |
| **Cáp động cơ biến tần** | ⭐ **Hai đầu** | Chắn nhiễu tần số cao — mục tiêu khác |
| **Cáp mạng** | Theo hướng dẫn nhà sản xuất | Thường hai đầu |

> ⭐ **Và cách nối vỏ quan trọng ngang việc nối ở đâu: phải tiếp xúc TRỌN VÒNG 360°.**
>
> Bện vỏ thành một sợi rồi vặn vào vít — cách làm phổ biến — tạo ra một đoạn dây dài. Ở tần số cao,
> đoạn dây đó có trở kháng đáng kể và vỏ **mất phần lớn tác dụng**.
>
> Dùng **kẹp vỏ chuyên dụng** ôm trọn vòng quanh vỏ cáp. Chi tiết nhỏ, khác biệt lớn.

```text
   ✗ SAI — bện thành sợi, vặn vít        ✓ ĐÚNG — kẹp trọn vòng 360°
   ═══════╗                              ═══════╦═══════
          ╰──────○ vít                          ▓ kẹp ôm quanh vỏ
       đoạn dây dài = trở kháng cao             ▓
                                                ⏚
```

---

## 49.5 Nguồn 24 V và chia nhánh

Chương 8 mục 8.7 đã tính công suất. Ở đây là cách **bố trí**.

### ⭐ Vì sao chia nhánh cầu chì

```text
              ┌─[cc]─── CPU + module
   24 V ──────┼─[cc]─── Cảm biến
              ├─[cc]─── Cơ cấu chấp hành (van, đèn)
              └─[cc]─── Mạng, thiết bị truyền thông
```

| Lợi ích | Giải thích |
|---|---|
| ⭐ **Một chập không kéo sập tất cả** | Cuộn van chập → nhánh đó nhảy, CPU vẫn sống và **báo được lỗi** |
| ⭐ **Cô lập khi chẩn đoán** | Rút một cầu chì để loại trừ cả một nhóm (Chương 51) |
| Bảo vệ đúng mức | Mỗi nhánh cầu chì theo đúng dòng của nó |

> ⭐ **Lợi ích thứ nhất đáng giá hơn nó có vẻ.** Nếu CPU mất điện cùng lúc với sự cố, máy dừng câm —
> không báo động, không ghi log, không ai biết chuyện gì. Với nhánh riêng, CPU sống sót và **nói cho
> bạn biết nhánh nào chết**.

### ⚠ Ba điều hay bị bỏ

| Điều | Ghi chú |
|---|---|
| **Cầu chì phải có đèn báo đứt** | Không thì phải rút ra đo từng cái |
| ⭐ **PLC nên biết trạng thái nguồn từng nhánh** | Một ngõ vào số cho mỗi nhánh quan trọng — rẻ, và biến "máy chạy lạ" thành "nhánh 3 mất điện" |
| **Nguồn dự phòng cho CPU** | Với máy quan trọng, giữ CPU sống qua sụt áp ngắn |

### ⚡ Chống quá áp lan truyền

Sét đánh gần, hoặc một contactor lớn cắt tải cảm, sinh ra **xung quá áp** truyền vào máy qua đường
nguồn hoặc qua cáp tín hiệu đi xa. Xung này ngắn — vài micro giây — nhưng biên độ có thể hàng nghìn
vôn, đủ phá module I/O hoặc cổng mạng.

| Nơi đặt bảo vệ | Vì sao |
|---|---|
| **Đầu vào nguồn của tủ** | Cửa vào phổ biến nhất |
| ⭐ **Cáp tín hiệu chạy ra ngoài nhà, hoặc dài giữa các tủ** | ⭐ **Cáp dài là một cái ăng-ten** |
| **Cáp mạng nối giữa hai toà nhà** | Nơi chênh lệch điện thế đất lớn nhất |

> ⭐ **Thiết bị chống quá áp chỉ có tác dụng khi nối đất tốt** — nó làm việc bằng cách **dẫn xung
> xuống đất**. Đấu nó vào một điểm đất kém thì nó gần như vô dụng. Đây là chỗ mục 49.4 quay lại: nối
> đất kém làm hỏng nhiều thứ hơn ta tưởng.
>
> ⚡ Thiết bị chống quá áp là **vật tư hao mòn** — nó xuống cấp sau mỗi lần chịu xung. Loại có đèn báo
> hoặc tiếp điểm báo trạng thái đáng giá tiền chênh: ⭐ **đưa tiếp điểm đó về một ngõ vào PLC** thì
> máy tự báo khi bảo vệ đã hết tác dụng, thay vì phát hiện sau khi module cháy.

---

## 49.6 Đánh số dây và cầu đấu

Việc nhàm chán nhất, và là việc quyết định thời gian sửa máy lúc hai giờ sáng.

| Nguyên tắc | Nội dung |
|---|---|
| ⭐ **Mỗi dây có số ở CẢ HAI đầu** | Một đầu thì vô dụng khi truy từ đầu kia |
| ⭐ **Số dây khớp bản vẽ** | Bản vẽ nói dây 214, trong tủ phải có dây 214 |
| **Nhãn bền** | ⚠ Nhãn viết bút lông phai sau một năm trong dầu |
| **Cầu đấu nhóm theo chức năng** | DI một khối, DO một khối, analog một khối |
| ⭐ **Chừa cầu đấu dự phòng** | 20 % — cùng lý do với chừa khe cắm (Chương 8, mục 8.3) |
| **Dây tín hiệu không đấu chung cầu đấu với động lực** | Cùng lý do tách máng |

> ⭐ **Quy ước đánh số phải khớp với tên tag trong chương trình.**
> Nếu bản vẽ ghi dây 214 đi tới `DI_BoardStn1`, và cầu đấu X2:14, thì người sửa máy đi từ triệu chứng
> ("cảm biến board không báo") tới đúng sợi dây trong ba bước. Không có liên kết đó, mỗi lần truy là
> một cuộc điều tra.
>
> Đây là phần "bảng I/O" ở Chương 23 kéo dài tới tận sợi dây — và là lý do bảng I/O phải làm **trước**
> khi đấu tủ.

---

## 49.7 ⚠ Đi dây trên máng xích động

Cáp đi theo cơ cấu chuyển động là điểm hỏng **được lập trình sẵn** nếu chọn sai.

| Yêu cầu | Vì sao |
|---|---|
| ⭐ **Cáp loại chịu uốn** *(continuous flex)* | ⚠ Cáp thường **gãy lõi** sau vài trăm nghìn lần uốn (Chương 40, mục 40.6) |
| ⭐ **Bán kính uốn tối thiểu** theo datasheet | Uốn gắt hơn quy định thì tuổi thọ giảm rất nhanh |
| **Không xoắn cáp trong xích** | Xích uốn một mặt phẳng; cáp xoắn sẽ mỏi ở chỗ khác |
| **Cố định hai đầu đúng cách** | Cáp phải "trôi" trong xích, không bị kéo căng |
| ⚠ **Không bó chặt nhiều cáp với nhau** | Chúng phải trượt tương đối với nhau |
| **Tách động lực và tín hiệu trong xích** | Cùng quy tắc mục 49.3 — nhiều xích có vách ngăn |

> ⚠⚠ **Cáp gãy lõi là lỗi khó chẩn đoán bậc nhất.**
> Nó **không đứt hẳn** — chỉ chập chờn, và thường chỉ khi cơ cấu ở một tư thế nhất định. Đo thông
> mạch tĩnh vẫn thấy tốt (Chương 3).
>
> ⭐ **Cách xác nhận:** lắc hoặc di chuyển cáp trong lúc theo dõi tín hiệu — với mạng thì theo dõi bộ
> đếm lỗi trên chuyển mạch quản lý được (Chương 40, mục 40.6); với cảm biến thì theo dõi bit trong
> PLC.

### ⭐ Phép tính tuổi thọ

Cùng cách tính với tuổi thọ rơ-le ở Chương 9 mục 9.3:

```text
Số lần uốn/chu trình  ×  chu trình/giờ  ×  giờ/năm  =  số lần uốn/năm
```

Với gantry DP-01: mỗi board gantry đi một vòng, 300 board/giờ (Phụ lục J §J.1), 2 ca × 8 giờ × 300
ngày:

```text
1 × 300 × 4800 = 1 440 000 lần/năm
```

> ⭐ **Một triệu tư lần uốn mỗi năm.** So con số đó với tuổi thọ uốn ghi trong datasheet cáp. Nếu cáp
> chỉ đảm bảo vài triệu lần, bạn đang nhìn vào một hạng mục **thay thế định kỳ**, không phải một thứ
> lắp một lần cho xong.
>
> Và nếu dùng cáp thường thay vì cáp chịu uốn, con số đó có thể là **vài tháng**.

---

## 49.8 ⭐ Tám sai lầm gây lỗi "ngẫu nhiên"

Gom lại đây vì đây là mục bạn sẽ quay lại khi chẩn đoán (Chương 51).

| # | Sai lầm | Triệu chứng đặc trưng |
|---|---|---|
| 1 | ⭐ **Cáp tín hiệu song song cáp động lực** | Lỗi xuất hiện **đúng lúc thiết bị công suất chạy tải nặng** |
| 2 | ⭐ **Vòng lặp đất** (0 V nối PE ở nhiều điểm) | Analog run; mạng rớt gói; đo được điện áp giữa hai điểm đất |
| 3 | **Vỏ chống nhiễu nối hai đầu** ở cáp analog | Nhiễu **nặng hơn** so với không nối vỏ |
| 4 | **Vỏ bện thành sợi thay vì kẹp 360°** | Vỏ mất phần lớn tác dụng ở tần số cao |
| 5 | ⭐ **Nguồn 24 V thiếu công suất** | Lỗi khi **nhiều cơ cấu cùng tác động**; trông giống lỗi phần mềm (Chương 8, mục 8.7) |
| 6 | ⭐ **Cáp thường trong xích động** | Mất tín hiệu **ngẫu nhiên**, thường ở một tư thế nhất định |
| 7 | **Đầu cốt lỏng** | Nóng dần, sụt áp, và **nặng dần theo thời gian** (Chương 3, mục 3.2) |
| 8 | ⚠⚠ **OSSD đấu vào ngõ vào thường** | Bit nhấp nháy do **xung kiểm tra** của thiết bị an toàn (Chương 47, mục 47.7) |

> ⭐⭐ **Điểm chung của cả tám: chúng không gây lỗi ngay và không gây lỗi đều.**
>
> Máy chạy được lúc nghiệm thu. Lỗi xuất hiện sau vài tuần, vài tháng, hoặc chỉ khi có điều kiện nhất
> định. Và vì không tái hiện được, người ta đi đổi thứ dễ đổi — cảm biến, module, chương trình.
>
> ⭐ **Khi gặp lỗi chập chờn không tái hiện được, hãy nghi lắp đặt trước khi nghi logic.** Đây là quy
> tắc tiết kiệm thời gian nhất trong Chương 51.

---

## 49.9 Trên máy mẫu DP-01

| Hạng mục | Quyết định | Chương |
|---|---|---|
| Máng cáp | ⭐ **Ba máng**: động lực · tín hiệu · an toàn | Mục 49.3 |
| Cáp động cơ chuyền | Có vỏ, ⭐ **nối vỏ hai đầu** | 36, mục 36.7 |
| Cáp analog (áp khí, áp keo, UV) | Đôi xoắn có vỏ, ⭐ **nối vỏ một đầu phía tủ** | 31, mục 31.6 |
| Cáp RS-485 tới bộ điều khiển nhiệt | Đôi xoắn có vỏ, ⚠ **tách xa cáp động cơ** | 38, mục 38.5 |
| ⭐ Cáp trong xích gantry | ⭐ **Loại chịu uốn**, tách động lực/tín hiệu trong xích | Mục 49.7 |
| 0 V và PE | ⭐ Nối **một điểm duy nhất** tại bộ nguồn, ghi vào bản vẽ | Mục 49.4 |
| Nhánh cầu chì 24 V | Bốn nhánh: CPU · cảm biến · cơ cấu · mạng | Mục 49.5 |
| ⭐ Giám sát nguồn nhánh | Ngõ vào số cho từng nhánh quan trọng | Mục 49.5 |
| Mạch an toàn | ⚠ Máng riêng, màu dây riêng | 47 |

### ⭐ Hạng mục cần tính, không chỉ chọn

| Việc | Phép tính | Chương |
|---|---|---|
| Công suất nguồn 24 V | Bước nhiều tải nhất × 1,3–1,5 | 8 mục 8.7, 5 mục 5.7 |
| Tuổi thọ cáp xích gantry | ⭐ **1,44 triệu lần uốn/năm** | Mục 49.7 |
| Tuổi thọ ngõ ra van | 2,88 triệu lần đóng cắt/năm | 9 mục 9.3 |
| Dòng qua chân chung module | Tổng tại thời điểm nhiều tải nhất | 9 mục 9.4 |

> ⭐ **Bốn phép tính này có chung một dạng: đếm số lần, rồi so với con số trong datasheet.**
> Chúng đều đơn giản, đều mất vài phút, và đều là thứ **phải làm trước khi mua** — vì phát hiện sau
> khi máy chạy nghĩa là thay thiết bị và đấu lại dây.

---

## 49.10 Nghiệm thu phần đấu tủ

Việc của người lập trình khi tiếp nhận tủ (Chương 52, mục 52.3):

| Kiểm | Cách |
|---|---|
| Đúng thiết bị, đúng mã | Đối chiếu nhãn với danh mục vật tư |
| ⭐ **Dây có số ở hai đầu, khớp bản vẽ** | Lấy mẫu vài chục dây |
| **Đầu cốt siết đủ chặt** | Kéo nhẹ từng dây; siết lại theo lực quy định |
| ⭐ **Tách máng đúng ba nhóm** | Nhìn — đây là thứ dễ kiểm nhất và hay sai nhất |
| ⭐ **0 V nối PE ở đúng một điểm** | Tra bản vẽ, rồi **đo xác nhận** |
| **Vỏ chống nhiễu nối đúng quy tắc** | Kiểm từng loại cáp theo bảng ở mục 49.4 |
| **Cáp trong xích là loại chịu uốn** | Đọc nhãn cáp |
| ⭐ **Đo điện áp 24 V khi tải nặng** | ⭐ **Ghi lại làm mốc** (Chương 8, mục 8.7; Chương 36, mục 36.8) |
| Nối đất vỏ tủ và vỏ thiết bị | Đo thông mạch tới thanh đất |

> ⭐ **Hàng "ghi lại làm mốc" xuất hiện lần thứ tư trong sách** — điện áp 24 V (Chương 8), dòng động
> cơ (Chương 36), số lỗi mạng (Chương 40), và ở đây.
>
> Chúng là cùng một ý tưởng: **một phép đo chỉ có nghĩa khi có cái để so.** Mười phút lúc nghiệm thu
> đổi lấy khả năng trả lời "cái này có bình thường không" trong suốt vòng đời máy.

---

## 49.11 Bẫy thường gặp

### 🔍 BẪY 1 — Cáp tín hiệu song song cáp động lực

**Hiện tượng:** ⭐ đúng cỗ máy ở mục 49.1 — lỗi ngẫu nhiên, không tái hiện được, và người ta đi đổi
cảm biến với module trong ba tuần.
**Cách sửa:** tách máng; giao nhau thì **cắt vuông góc** (mục 49.3).

### 🔍 BẪY 2 — Nhầm PE với 0 V

**Hiện tượng:** vòng lặp đất — analog run, mạng rớt gói, nhiễu tăng khi thiết bị công suất chạy.
**Cách sửa:** ⭐ nối 0 V với PE ở **đúng một điểm**, ghi vào bản vẽ (mục 49.4).

### 🔍 BẪY 3 — Vỏ chống nhiễu nối sai số đầu

**Hiện tượng:** nhiễu **nặng hơn** khi nối vỏ — vì vỏ thành đường dẫn dòng vòng.
**Cách sửa:** analog **một đầu**, cáp động cơ **hai đầu** (mục 49.4). Hai quy tắc, hai bài toán khác
nhau.

### 🔍 BẪY 4 — Bện vỏ thành sợi rồi vặn vít

**Hiện tượng:** đã nối vỏ đúng số đầu mà vẫn nhiễu.
**Cách sửa:** ⭐ kẹp **trọn vòng 360°** (mục 49.4).

### 🔍 BẪY 5 — Một cầu chì cho tất cả

**Hiện tượng:** một cuộn van chập → **CPU mất điện cùng lúc** → máy dừng câm, không báo động, không
log.
**Cách sửa:** chia nhánh theo nhóm; và ⭐ đưa trạng thái nhánh về PLC (mục 49.5).

### 🔍 BẪY 6 — Cáp thường trong xích động

**Hiện tượng:** ⚠ mất tín hiệu ngẫu nhiên sau vài tháng, thường ở một tư thế nhất định; đo thông mạch
tĩnh vẫn tốt.
**Cách sửa:** cáp chịu uốn, đúng bán kính uốn; ⭐ và **tính số lần uốn mỗi năm** (mục 49.7).

### 🔍 BẪY 7 — Số dây chỉ có ở một đầu

**Hiện tượng:** truy một sợi dây từ hiện trường về tủ mất hàng giờ.
**Cách sửa:** số ở **cả hai đầu**, khớp bản vẽ và khớp tên tag (mục 49.6).

### 🔍 BẪY 8 — Không ghi mốc lúc nghiệm thu

**Hiện tượng:** sáu tháng sau đo được 23,1 V ở tải nặng — **không biết** đó là bình thường hay đã xấu
đi.
**Cách sửa:** đo và ghi khi máy còn mới (mục 49.10).

### 🔍 BẪY 9 — Đấu tủ trước khi có bảng I/O

**Hiện tượng:** số dây không khớp tên tag; mỗi lần truy là một cuộc điều tra.
**Cách sửa:** bảng I/O làm **trước** (Chương 23), và quy ước đánh số bám theo nó (mục 49.6).

### 🔍 BẪY 10 — Nghi logic trước khi nghi lắp đặt

**Hiện tượng:** hàng giờ đọc chương trình cho một lỗi nằm ở sợi dây.
**Cách sửa:** ⭐⭐ **lỗi chập chờn không tái hiện được → nghi lắp đặt trước** (mục 49.8, Chương 51).

---

## 49.12 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| Ba nhóm cáp | ⚡ Động lực · 📶 tín hiệu · 🔴 an toàn — **không đi chung** |
| Buộc phải giao nhau | ⭐ **Cắt vuông góc** |
| Vì sao mạch an toàn đi riêng | Không phải vì nhiễu — vì **rõ ràng khi kiểm tra** |
| ⭐⭐ PE và 0 V | **Hai thứ khác nhau** — PE cho an toàn người, 0 V là đường về của dòng |
| Nối 0 V với PE ở đâu | ⭐ **Đúng một điểm**, ghi vào bản vẽ |
| Vỏ cáp analog | **Một đầu** — phía tủ |
| Vỏ cáp động cơ biến tần | **Hai đầu** |
| Cách nối vỏ | ⭐ **Kẹp trọn vòng 360°**, không bện thành sợi |
| Vì sao chia nhánh cầu chì | ⭐ Một chập không kéo sập CPU — **máy còn báo được lỗi** |
| Nên thêm gì cho nhánh nguồn | Ngõ vào số báo trạng thái từng nhánh |
| Chống quá áp lan truyền | Đầu vào nguồn + ⭐ **cáp tín hiệu đi xa**; là **vật tư hao mòn**, nên đưa tiếp điểm báo về PLC |
| Số dây | ⭐ **Cả hai đầu**, khớp bản vẽ **và khớp tên tag** |
| Cáp trong xích động | ⭐ **Loại chịu uốn**, đúng bán kính uốn, không bó chặt |
| Cáp gãy lõi — triệu chứng | Chập chờn theo tư thế; ⚠ **đo tĩnh vẫn tốt** |
| Xác nhận cáp gãy lõi | **Lắc cáp** trong lúc theo dõi tín hiệu |
| ⭐⭐ Lỗi chập chờn không tái hiện | **Nghi lắp đặt trước khi nghi logic** |
| Lúc nghiệm thu phải ghi gì | ⭐ **Mốc**: điện áp 24 V tải nặng, dòng động cơ, số lỗi mạng |

---

## 49.13 Tự kiểm

1. ⭐ Mô tả sự cố ở mục 49.1. Vì sao nó mất ba tuần để tìm, và điều gì làm nó khó nối với nguyên nhân?
2. Kể ba nhóm cáp và quy tắc đi dây cho chúng. Vì sao mạch an toàn đi riêng?
3. ⭐⭐ Phân biệt **PE** với **0 V** trên bốn tiêu chí. Nối chúng ở nhiều điểm gây ra chuyện gì?
4. Nêu bốn triệu chứng của vòng lặp đất và cách kiểm nhanh.
5. ⭐ Vỏ chống nhiễu của cáp analog nối mấy đầu? Của cáp động cơ biến tần nối mấy đầu? Vì sao khác
   nhau?
6. Vì sao **bện vỏ thành sợi rồi vặn vít** làm vỏ mất tác dụng? Cách đúng là gì?
7. ⭐ Nêu ba lợi ích của việc chia nhánh cầu chì 24 V. Lợi ích nào đáng giá nhất khi có sự cố?
8. Cáp gãy lõi trong xích động cho triệu chứng gì? Vì sao **đo thông mạch tĩnh không phát hiện được**?
9. ⭐ Tính số lần uốn mỗi năm của cáp trong xích gantry DP-01 với 300 board/giờ, 2 ca × 8 giờ, 300
   ngày. Con số đó nói lên điều gì về cách bạn coi sợi cáp?
10. Vì sao số dây phải có ở **cả hai đầu** và khớp với **tên tag** trong chương trình?
11. Nêu tám sai lầm lắp đặt gây lỗi "ngẫu nhiên". Điểm chung của chúng là gì?
12. ⭐⭐ Khi gặp lỗi chập chờn không tái hiện được, nên nghi vào đâu trước? Vì sao quy tắc này tiết
    kiệm nhiều thời gian nhất?

> Câu 3, 5, 9 và 12 là bốn câu phân loại. Câu 12 là tinh thần của cả chương: **lỗi do lắp đặt không
> giống lỗi lắp đặt — nó giống lỗi phần mềm, và đó là lý do người ta đi tìm nhầm chỗ.**

---

### Chương tiếp theo

Chương 50 — **Mô phỏng & kiểm thử**. Tủ đã đấu xong. Trước khi cấp điện cho cả cỗ máy, chương sau về
việc tìm lỗi ở nơi rẻ nhất: trên bàn, trước khi có phần cứng.

### Nguồn tham khảo chương 49

- IEC 60204-1 — *Safety of machinery — Electrical equipment of machines*: yêu cầu với đi dây, nối
  đất bảo vệ, đánh dấu dây dẫn, và bố trí tủ điện. *(tiêu chuẩn có bản quyền)*
- IEC 61439 (bộ) — *Low-voltage switchgear and controlgear assemblies*: yêu cầu với tủ điện hạ áp.
- IEC 61800-3 — *EMC requirements for adjustable speed drives*: nền cho yêu cầu tách cáp và nối vỏ ở
  mục 49.3–49.4.
- IEC 61918 — *Installation of communication networks in industrial premises*: lắp đặt cáp mạng công
  nghiệp.
- IEC 61643 (bộ) — *Low-voltage surge protective devices*: thiết bị chống quá áp lan truyền cho
  đường nguồn và đường tín hiệu — nền cho mục 49.5.
- **Datasheet cáp** — dùng cho ⚠ **số lần uốn cho phép**, **bán kính uốn tối thiểu**, và loại vỏ.
- **Hướng dẫn lắp đặt của nhà sản xuất biến tần và PLC** — dùng cho nối đất và chống nhiễu; ⭐ **họ đã
  tính cho sản phẩm của họ**.
- Bảng I/O và số liệu đã chốt của DP-01 — Phụ lục J.

> ⚠⚠ **Nhắc lại giới hạn.** Chương này giúp bạn **hiểu và kiểm tra**, không phải để tự thiết kế tủ
> điện. Thiết kế điện — chọn tiết diện dây, tính toán bảo vệ, bố trí nối đất, và toàn bộ phần mạch an
> toàn — phải do **người có chuyên môn điện** thực hiện theo tiêu chuẩn hiện hành tại thị trường của
> bạn, và phải được kiểm định.
>
> ⚡ Các quy tắc đi dây ở mục 49.3–49.4 là **thực hành tốt được thừa nhận rộng rãi**; khoảng cách tách
> cáp cụ thể, tiết diện dây nối đất, và yêu cầu chi tiết khác phải lấy từ **bản gốc tiêu chuẩn** và
> từ hướng dẫn của nhà sản xuất thiết bị.
