# Chương 40 — Ethernet công nghiệp: ba họ, chọn thế nào

> **Lát cắt máy mẫu:** 4 — thêm mạng: mã 2D, MES, SMEMA, màn hình vận hành, và bộ điều khiển nhiệt độ
> keo nối RS-485.

---

## 40.1 Bài toán: mạng chạy tốt, servo giật

Gantry của DP-01 nối với ba servo drive qua Ethernet công nghiệp. Cùng cáp mạng đó, người ta nối thêm
màn hình vận hành và một máy tính để tải dữ liệu sản xuất — **tiết kiệm được một bộ chuyển mạch**.

Máy chạy tốt. Cho tới khi ai đó tải một tệp lớn từ máy tính đó.

Trong lúc tải, gantry **giật nhẹ** ở vài điểm trên đường keo. Đường keo có chỗ dày chỗ mỏng. Sau khi
tải xong, mọi thứ trở lại bình thường.

Không có báo lỗi nào. Mạng "chạy tốt" theo mọi nghĩa thông thường: không mất gói, không lỗi.

Nguyên nhân: lưu lượng tải tệp **chen vào giữa** các gói điều khiển servo. Với dữ liệu văn phòng, trễ
vài mili-giây không ai để ý. Với vòng điều khiển vị trí chạy chu kỳ 1 ms, trễ đó là **thiếu một chu
kỳ lệnh**.

Chương này về việc chọn đúng họ mạng cho đúng việc — và về lý do "cũng là Ethernet cả" là một câu
nguy hiểm.

---

## 40.2 Ethernet công nghiệp khác Ethernet văn phòng ở đâu

| | Ethernet văn phòng | Ethernet công nghiệp |
|---|---|---|
| Ưu tiên | **Thông lượng** — truyền nhiều dữ liệu | ⭐ **Tính xác định thời gian** — gói tới đúng lúc |
| Trễ vài chục ms | Không ai để ý | ⚠ Có thể làm hỏng chuyển động |
| Đầu nối | RJ45 thường | M12, hoặc RJ45 có vỏ chống bụi/nước |
| Cáp | Loại thường | Chịu dầu, chịu rung, chịu nhiễu |
| Chuyển mạch | Bất kỳ | ⭐ Loại công nghiệp, thường **quản lý được** |
| Chịu nhiễu | Môi trường sạch | ⚠ Cạnh biến tần và cáp động lực (Chương 36, mục 36.7) |

> ⭐ **Khác biệt cốt lõi không phải tốc độ — mà là "gói tới đúng lúc hay không".**
> Đây là cùng khái niệm **tính tất định** ở Chương 2 mục 2.2, áp cho mạng. Một mạng nhanh mà thỉnh
> thoảng trễ thì tệ hơn một mạng chậm mà đều đặn.

---

## 40.3 ⭐ Ba họ giao thức

Đây là cách phân loại hữu ích nhất khi chọn, vì nó bám theo **cách giao thức xử lý thời gian**.

### Họ 1 — Chạy trên TCP/IP thường

**Ví dụ:** EtherNet/IP, PROFINET RT, Modbus TCP (Chương 39).

| Đặc điểm | Nội dung |
|---|---|
| Chu kỳ | Khoảng **mili-giây** |
| Hạ tầng | ⭐ Chuyển mạch Ethernet thường dùng được; nên dùng loại **quản lý được** |
| Chia sẻ dây | ⭐ **Sống chung được** với lưu lượng khác — nhưng ⚠ xem mục 40.1 |
| Đồng bộ thời gian | Một số dùng giao thức đồng bộ đồng hồ khi cần |
| Hợp với | I/O phân tán, biến tần, màn hình vận hành, trao đổi với hệ thống trên |
| ⚠ Không hợp với | Chuyển động phối hợp nhiều trục |

### Họ 2 — Hỏi–đáp đồng bộ

**Ví dụ:** PROFINET IRT, POWERLINK.

| Đặc điểm | Nội dung |
|---|---|
| Chu kỳ | **100 µs – 1 ms** |
| Cơ chế | ⭐ Chia thời gian thành **khe cố định** — mỗi thiết bị nói trong khe của mình, **không bao giờ va chạm** |
| Hạ tầng | ⚠ **Thiết bị chuyên dụng** — chuyển mạch thường không dùng được |
| Chia sẻ dây | ⚠⚠ **Không** — chia sẻ phá vỡ chính cơ chế đảm bảo thời gian |
| Hợp với | Chuyển động phối hợp, điều khiển đồng bộ nhiều trục |

### Họ 3 — Xử lý gói trên đường đi

**Ví dụ:** EtherCAT.

| Đặc điểm | Nội dung |
|---|---|
| Chu kỳ | ⭐ **Rất ngắn** — dưới 100 µs với nhiều trục |
| Cơ chế | ⭐ Một gói **đi xuyên qua** tất cả thiết bị; mỗi thiết bị **đọc và ghi ngay khi gói chạy qua** |
| Hạ tầng | Nối chuỗi *(daisy chain)*; thiết bị có mạch xử lý chuyên dụng |
| Chia sẻ dây | ⚠ Không cho lưu lượng thường |
| Hợp với | Nhiều trục, chu kỳ rất ngắn, hệ có nhiều điểm I/O nhanh |

> 💡 **Cách hình dung họ 3:** thay vì gửi thư riêng cho từng người rồi chờ từng người trả lời, một tờ
> giấy chạy qua bàn tất cả mọi người — ai cần thì đọc phần của mình và điền phần của mình **ngay khi
> nó lướt qua**. Một vòng là xong tất cả.
>
> Đó là lý do nó nhanh hơn hẳn: **không có thời gian chờ trả lời**.

### Bảng so sánh

| | Họ 1 — TCP/IP thường | Họ 2 — đồng bộ khe | Họ 3 — xử lý trên đường đi |
|---|---|---|---|
| Chu kỳ điển hình | ms | 100 µs – 1 ms | ⭐ < 100 µs |
| Chuyển mạch thường | ⭐ Dùng được | ❌ Không | ❌ Không |
| Chia sẻ với lưu lượng khác | ⭐ Được (có điều kiện) | ❌ Không | ❌ Không |
| Cấu trúc | Sao, cây | Sao | Chuỗi |
| Chi phí hạ tầng | ⭐ Thấp | Cao | Trung bình |
| Hợp với chuyển động phối hợp | ❌ | ✅ | ⭐ ✅ |
| Hợp với I/O và thiết bị chung | ⭐ ✅ | ✅ | ✅ |

---

## 40.4 ⚠ "Cũng là Ethernet cả" — câu nguy hiểm

Ba họ trên **đều dùng cáp Ethernet và đầu nối RJ45**. Nhìn bề ngoài giống hệt nhau. Nhưng:

| Hiểu nhầm | Thực tế |
|---|---|
| "Cắm vào chuyển mạch nào cũng được" | ⚠ Họ 2 và 3 cần **thiết bị chuyên dụng** |
| "Nối chung với mạng văn phòng cho tiện" | ⚠⚠ Đúng cỗ máy ở mục 40.1 — và còn là lỗ hổng an ninh (Chương 45) |
| "Thiết bị nào cắm vào cũng chạy" | ⚠ Mỗi họ có giao thức riêng; cắm vật lý được ≠ nói chuyện được |
| "Mạng nhanh thì chuyển động mượt" | ⚠ **Tính xác định** quan trọng hơn tốc độ |

> ⚠⚠ **Nguyên tắc: đừng trộn lưu lượng điều khiển với lưu lượng dữ liệu trên cùng một đường.**
>
> Với họ 2 và 3 thì đây là **yêu cầu kỹ thuật** — trộn vào là phá cơ chế đảm bảo thời gian.
>
> Với họ 1 thì trộn được về mặt kỹ thuật, nhưng ⚠ **vẫn nên tách** vì hai lý do: tránh cỗ máy ở
> mục 40.1, và vì an ninh mạng (Chương 45).

---

## 40.5 Chọn mạng nào

Đừng chọn theo "cái nào tốt nhất". Đi theo bốn câu hỏi, và thường chỉ còn một, hai lựa chọn thật.

> **1. Hệ PLC của bạn hỗ trợ mạng nào?**
> ⭐ Câu này thường quyết định tất cả. Mỗi hãng PLC có mạng "quê nhà" của mình — dùng nó thì mọi thứ
> tích hợp sẵn; dùng mạng khác thì phải thêm module và thêm công cấu hình.
>
> **2. Có chuyển động phối hợp không?**
> Có → họ 2 hoặc 3. Không → họ 1 là đủ và rẻ hơn nhiều.
>
> **3. Thiết bị bạn cần mua có hỗ trợ mạng đó không?**
> ⚠ Kiểm **trước khi chốt**. Không phải biến tần, servo drive, cụm I/O nào cũng có bản cho mọi mạng.
>
> **4. Đội bảo trì và nhà máy đã quen mạng nào?**
> ⭐ Cùng câu hỏi với Chương 13 tiêu chí 7 và Chương 20 mục 20.6 — và nó thường thắng các câu trên.

### Ví dụ áp cho DP-01

| Việc | Mạng | Vì sao |
|---|---|---|
| Servo drive (3 trục, phối hợp XY) | ⭐ **Họ 2 hoặc 3** | Nội suy đường thẳng cần đồng bộ (Chương 37, mục 37.7) |
| Màn hình vận hành | Họ 1 | Dữ liệu đổi chậm, không cần xác định thời gian |
| Đầu đọc mã 2D | Họ 1 | Vài bản tin mỗi board |
| Hệ thống trên (MES) | Họ 1 | Chương 42 |
| Bộ điều khiển nhiệt độ | RS-485 (Chương 38) | Không cần Ethernet |

> ⭐ **Hai mạng tách biệt là thiết kế bình thường và nên làm**: một mạng chuyển động cho servo, một
> mạng chung cho phần còn lại. PLC có cổng cho cả hai (hoặc thêm module).
>
> Đây chính là cách tránh cỗ máy ở mục 40.1.

---

## 40.6 Cấu trúc mạng và hạ tầng

### Ba cấu trúc

| Cấu trúc | Hình | ✅ / ⚠ |
|---|---|---|
| **Sao** *(star)* | Mọi thiết bị nối về một chuyển mạch | ⭐ Hỏng một nhánh không ảnh hưởng nhánh khác; ⚠ chuyển mạch là điểm hỏng chung |
| **Chuỗi** *(daisy chain / line)* | Nối tiếp qua từng thiết bị | ⭐ Ít dây; ⚠ **đứt một chỗ là mất phần phía sau** |
| **Vòng** *(ring)* | Chuỗi khép kín | ⭐ Đứt một chỗ vẫn chạy; cần giao thức hỗ trợ |

> ⚠ **Chuỗi rất phổ biến với EtherCAT và với cụm I/O phân tán** vì nó tiết kiệm dây trên máy dài. Cái
> giá: một đầu nối lỏng ở giữa làm **mất mọi thiết bị phía sau** — và triệu chứng chỉ vào đúng vị trí
> đứt, không vào thiết bị hỏng.

### Chuyển mạch — quản lý được hay không

| | Không quản lý | ⭐ Quản lý được |
|---|---|---|
| Cấu hình | Không có | Có giao diện cấu hình |
| ⭐ Ưu tiên lưu lượng *(QoS)* | ❌ | ✅ — gói điều khiển đi trước |
| Phân vùng *(VLAN)* | ❌ | ✅ — tách lưu lượng (Chương 45) |
| ⭐ Chẩn đoán | ❌ Chỉ có đèn | ✅ **Đếm lỗi từng cổng, thấy cổng nào có vấn đề** |
| Giá | Thấp | Cao hơn |

> ⭐ **Hàng "chẩn đoán" thường là lý do đáng giá nhất để mua loại quản lý được.**
> Một cổng có nhiều lỗi khung là dấu hiệu cáp hỏng hoặc đầu nối lỏng — và chuyển mạch quản lý được
> **chỉ thẳng vào cổng đó**. Không có nó, bạn phải rút từng dây để thử (Chương 51).

### ⚠ Đi dây và chống nhiễu

| Việc | Vì sao |
|---|---|
| ⭐ **Tách xa cáp động lực** | Biến tần là nguồn nhiễu mạnh nhất (Chương 36, mục 36.7) |
| Dùng cáp công nghiệp | Chịu dầu, chịu rung, chịu uốn nếu đi trong xích cáp |
| ⚠ **Cáp trong xích cáp phải là loại chịu uốn** | Cáp thường **gãy lõi** sau vài trăm nghìn lần uốn — hỏng chập chờn rất khó tìm |
| Đầu nối chắc chắn | RJ45 thường dễ lỏng do rung; M12 chắc hơn |
| ⚠ Chiều dài đoạn tối đa | Có giới hạn; vượt thì cần chuyển mạch trung gian |

> ⚠ **Cáp mạng gãy lõi do uốn là một trong những lỗi khó chẩn đoán nhất trên máy.**
> Triệu chứng: mất kết nối **ngẫu nhiên**, thường khi cơ cấu ở một tư thế nhất định. Nó không hỏng
> hẳn, nên đo thông mạch tĩnh vẫn thấy tốt.
>
> Cách xác nhận: **lắc nhẹ cáp trong lúc theo dõi bộ đếm lỗi** trên chuyển mạch quản lý được, hoặc
> dùng máy kiểm tra cáp mạng (Chương 51).

---

### ⭐⭐ Hai thứ chuyển mạch phải làm mà "cắm là chạy" không cho bạn

Bảng trên nói chuyển mạch quản lý được hơn ở QoS, VLAN và chẩn đoán. Còn **hai chức năng nữa** mà
thiếu chúng thì mạng công nghiệp **hỏng theo cách rất khó hiểu**.

**Một — lọc gói multicast (IGMP snooping)**

Một số họ giao thức công nghiệp gửi dữ liệu I/O bằng **multicast** — một gói, nhiều người nhận.

| Chuyển mạch | Làm gì với gói multicast |
|---|---|
| ⚠ Không hỗ trợ IGMP snooping | ⭐ **Phát ra MỌI cổng** — như quảng bá |
| ⭐ Có IGMP snooping | Chỉ gửi tới cổng có thiết bị **thật sự đăng ký nhận** |

> ⚠⚠ **Hệ quả khi thiếu: mọi thiết bị trên mạng nhận lưu lượng của mọi thiết bị khác.**
>
> Một HMI nhỏ hay một cảm biến sẽ phải xử lý — rồi vứt bỏ — hàng nghìn gói mỗi giây không liên quan
> tới nó. ⭐ Triệu chứng: thiết bị yếu **phản hồi chậm hoặc rớt mạng**, trong khi thiết bị mạnh vẫn
> bình thường. ⚠ Càng thêm thiết bị vào mạng thì càng nặng — nên nó **xuất hiện muộn**, sau khi máy
> đã chạy một thời gian.
>
> ⭐ **Kiểm khi chọn thiết bị:** hỏi thẳng *"chuyển mạch này có IGMP snooping không?"* — và bật nó lên.

**Hai — xử lý vòng lặp mạng**

Cấu trúc **vòng** ở bảng trên cho khả năng chịu đứt một chỗ. ⭐ Nhưng một vòng Ethernet **không có
giao thức quản lý** thì không phải dự phòng — nó là **một sự cố**.

| Tình huống | Kết quả |
|---|---|
| ⚠⚠ Vòng **không có giao thức** | Gói quảng bá chạy vòng **vô tận**, nhân lên → ⭐ **mạng chết hoàn toàn** |
| ⭐ Vòng **có giao thức dự phòng** | Một đoạn được **chặn có chủ ý**; đứt chỗ khác thì nó mở ra |

> ⚠⚠ **Đây cũng là điều xảy ra khi ai đó vô tình cắm hai cổng của cùng một chuyển mạch vào nhau** —
> một sai sót mất hai giây, và **cả mạng ngừng hoạt động**, kể cả phần không liên quan.
>
> ⭐ Triệu chứng đặc trưng: **mọi đèn cổng nháy điên loạn cùng lúc**, mất toàn bộ liên lạc, và ⚠
> **rút một sợi cáp ra thì mọi thứ trở lại bình thường ngay**.
>
> ⭐ Có nhiều họ giao thức xử lý việc này — loại chuẩn hoá rộng dựa trên **cây khung** *(spanning
> tree)*, và các giao thức vòng chuyên dụng cho mạng công nghiệp có thời gian phục hồi nhanh hơn
> nhiều. ⚠ **Chúng không tự có** — phải chọn chuyển mạch hỗ trợ và **cấu hình**.

> ⭐⭐ **Điểm chung của cả hai: chúng biến "cắm dây là chạy" thành "cắm dây rồi cấu hình".**
>
> ⚠ Và cả hai đều hỏng theo kiểu **không lộ ra ngay** — mạng chạy tốt lúc nghiệm thu với ít thiết bị,
> rồi xấu dần khi máy được mở rộng. Đây đúng loại lỗi mà Chương 49 gọi là *"lỗi do lắp đặt không
> giống lỗi lắp đặt"*.

*(Đối chiếu: tài liệu EtherNet/IP của Inovance H5U và InoProShop — nêu yêu cầu chuyển mạch hỗ trợ
IGMP Snooping để lọc gói multicast không liên quan; Rockwell — A Resilient Converged Plantwide
Ethernet Architecture, phần các giao thức dự phòng cho cấu trúc vòng và sao.)*

---

## 40.7 Địa chỉ và cấu hình

### Địa chỉ IP

| Cách | Nghĩa | Dùng khi |
|---|---|---|
| ⭐ **Tĩnh** *(static)* | Đặt cố định cho từng thiết bị | ⭐ **Mặc định cho máy công nghiệp** |
| Động *(DHCP)* | Máy chủ cấp khi thiết bị khởi động | ⚠ Hiếm dùng cho thiết bị điều khiển |

> ⚠⚠ **Dùng địa chỉ tĩnh cho thiết bị điều khiển.**
> Với địa chỉ động, thiết bị có thể nhận **địa chỉ khác** sau khi mất điện — và PLC đang tìm địa chỉ
> cũ sẽ không thấy nó. Máy dừng vì một lý do không liên quan gì tới máy.
>
> Ngoại lệ hợp lý: máy tính của kỹ sư nối tạm vào để lập trình.

> 💡 **Lập sơ đồ địa chỉ và dán trong tủ.** Sáu tháng sau, khi cần thêm một thiết bị, bạn phải biết
> địa chỉ nào đã dùng. Đây là tài liệu bàn giao (Chương 52).

### Tệp mô tả thiết bị

Mỗi họ mạng có định dạng tệp riêng mô tả thiết bị cho công cụ cấu hình — tương tự tệp IODD của
IO-Link (Chương 12, mục 12.6).

> ⚠ **Tệp mô tả thiết bị phải được lưu cùng dự án** (Chương 54). Không có nó, mở lại dự án sau ba năm
> có thể không cấu hình được thiết bị — và tệp cho đời sản phẩm cũ có thể không còn tải được.

---

## 40.8 ⭐ Chẩn đoán mạng từ trong chương trình

Mạng hỏng là một trạng thái phải xử lý, giống mất truyền thông nối tiếp (Chương 38, mục 38.9).

### Ba mức thông tin

| Mức | Đọc được gì | Dùng để |
|---|---|---|
| **Trạng thái liên kết** | Cổng có tín hiệu vật lý không | Phát hiện đứt cáp, rút dây |
| ⭐ **Trạng thái thiết bị** | Từng thiết bị còn trao đổi dữ liệu không | ⭐ Điều kiện cho phép chạy |
| **Chất lượng** | Số gói lỗi, số lần mất gói | Cảnh báo sớm cáp xuống cấp |

```iecst
// ⭐ Mất một cụm I/O phân tán → mọi ngõ vào của cụm đó VÔ NGHĨA
IF NOT M_RemoteIo1Ok THEN
    M_Alm_RemoteIo1 := TRUE;        // cờ chốt — gom vào M_AnyFault (Ch.25 mục 25.5c)
    M_FaultCode := 501;             // mã riêng — nói rõ SAI Ở ĐÂU
    // ⚠ KHÔNG dùng giá trị ngõ vào của cụm này cho bất kỳ quyết định nào
END_IF;

// Mất một servo drive
IF NOT M_DriveXOk OR NOT M_DriveYOk OR NOT M_DriveZOk THEN
    M_AxisFault := TRUE;
    M_CanStart  := FALSE;
END_IF;

// ⭐ Chất lượng xuống cấp — mức "cảnh báo, vẫn chạy" (Chương 48, mục 48.6)
IF NetErrorCount > BaselineErrCount + 100 THEN
    M_NetQualityWarn := TRUE;       // cáp có thể đang xuống cấp
END_IF;
```

> ⚠⚠ **Mất một cụm I/O phân tán KHÔNG có nghĩa là mọi ngõ vào của nó bằng 0.**
> Nó có nghĩa là bạn **không biết** chúng bằng bao nhiêu. Nếu chương trình đọc chúng như bình thường,
> nó sẽ hiểu "không có board", "cửa mở", "chưa tới vị trí" — tuỳ tín hiệu, và tuỳ hệ.
>
> Đây là cùng nguyên tắc với Chương 31 mục 31.3 và Chương 38 mục 38.9: **mất phép đo phải được xử lý
> tường minh, không được im lặng dùng giá trị mặc định.**

> 💡 **Ghi số lỗi mạng lúc nghiệm thu làm mốc** (Chương 52), giống dòng động cơ ở Chương 36 mục 36.8.
> Số lỗi hôm nay chỉ có nghĩa khi có cái để so.

---

## 40.9 Trên máy mẫu DP-01

### Hai mạng tách biệt

```text
   ┌─────────────────────────────────────────────────────────┐
   │                        PLC                              │
   │   cổng mạng chuyển động        cổng mạng chung          │
   └──────────┬──────────────────────────┬───────────────────┘
              │                          │
      ┌───────┴────────┐         ┌───────┴────────┐
      │  MẠNG CHUYỂN   │         │  MẠNG CHUNG    │
      │     ĐỘNG       │         │   (họ 1)       │
      │   (họ 2 / 3)   │         │                │
      ├─ Drive X       │         ├─ Màn hình vận hành
      ├─ Drive Y       │         ├─ Đầu đọc mã 2D
      └─ Drive Z       │         ├─ Cụm I/O phân tán (nếu có)
                                 └─ Tới hệ thống trên ──► (qua tường lửa, Ch.45)
```

| Quyết định | Lý do |
|---|---|
| ⭐ **Tách hai mạng** | Lưu lượng tải dữ liệu không chen vào điều khiển servo — đúng bài học mục 40.1 |
| Địa chỉ **tĩnh** cho mọi thiết bị | Mục 40.7 |
| Chuyển mạch **quản lý được** cho mạng chung | ⭐ Chẩn đoán từng cổng (mục 40.6) |
| Cáp trong xích cáp gantry là **loại chịu uốn** | ⚠ Gantry chuyển động liên tục — mục 40.6 |
| Tới hệ thống trên **qua tường lửa** | Chương 45 |

> ⭐ **Cáp mạng đi theo gantry là điểm yếu cơ khí đáng chú ý của DP-01.**
> Gantry chạy mỗi board, 300 board/giờ — cáp uốn hàng trăm nghìn lần mỗi tháng. Dùng cáp thường ở đây
> là bảo đảm một sự cố chập chờn trong vòng một năm, và nó sẽ rất khó chẩn đoán.
>
> Đây là cùng loại phép tính với tuổi thọ rơ-le ở Chương 9 mục 9.3: **đếm số lần, rồi so với tuổi thọ
> ghi trong datasheet.**

### Điều kiện cho phép chạy — bổ sung từ mạng

```iecst
M_CanStart := M_Homed                    // Chương 37
          AND M_DriveXOk AND M_DriveYOk AND M_DriveZOk    // ⭐ mạng chuyển động
          AND M_ScannerCommOk            // Chương 42
          AND NOT M_GlueTempFault        // Chương 39
          AND M_RecipeLoaded             // Chương 29
          AND DI_AirOK
          AND DI_EStopOK
          AND NOT M_AnyFault;
```

> ⭐ Danh sách này đã dài dần qua các chương, và đó là điều đúng: **mỗi hệ thống con thêm một điều
> kiện, và mỗi điều kiện viết rõ ràng để người vận hành thấy được cái nào đang thiếu** (Chương 24,
> mục 24.7).

---

## 40.10 Khác biệt giữa các hãng

| Hệ | Mạng "quê nhà" | Ghi chú |
|---|---|---|
| **Siemens** | **PROFINET** (RT và IRT) | Tích hợp sâu; IRT cho chuyển động |
| **Rockwell** | **EtherNet/IP** | Tích hợp sâu với dòng Logix |
| **Beckhoff** | **EtherCAT** | Chu kỳ rất ngắn; nhiều hãng khác cũng hỗ trợ |
| **Mitsubishi** | **CC-Link IE** | Phổ biến ở máy châu Á |
| **Omron** | EtherCAT, EtherNet/IP | Tuỳ dòng |
| Trung lập | **Modbus TCP** | ⭐ Gần như mọi hệ đều có — mẫu số chung (Chương 39) |

| Khía cạnh | Điều cần biết |
|---|---|
| ⭐ **Dùng mạng quê nhà thì dễ hơn nhiều** | Cấu hình tích hợp trong phần mềm lập trình; thiết bị nhận diện tự động |
| ⚠ Dùng mạng khác | Thường được, nhưng cần module thêm và nhiều công cấu hình hơn |
| Thiết bị đa giao thức | ⭐ Nhiều biến tần và cụm I/O có bản cho nhiều mạng — **kiểm mã sản phẩm** |
| ⚠ Cùng tên chưa chắc tương thích | Ví dụ PROFINET RT và IRT **khác nhau về hạ tầng** — kiểm kỹ |
| Công cụ chẩn đoán | Mỗi hãng có công cụ riêng; ⭐ học dùng nó **trước khi** cần nó lúc 2 giờ sáng |

Chi tiết đối chiếu năm hệ: **Phụ lục A1**.

---

## 40.11 Bẫy thường gặp

### 🔍 BẪY 1 — Trộn lưu lượng điều khiển với dữ liệu

**Hiện tượng:** ⭐ đúng cỗ máy ở mục 40.1 — chuyển động giật khi có ai tải dữ liệu; **không có báo lỗi
nào**, và triệu chứng biến mất khi thử lại.
**Cách sửa:** tách mạng chuyển động khỏi mạng dữ liệu (mục 40.4, 40.9).

### 🔍 BẪY 2 — Dùng chuyển mạch thường cho họ 2 hoặc 3

**Hiện tượng:** hoặc không hoạt động, hoặc hoạt động **không ổn định theo cách khó hiểu**.
**Cách sửa:** họ 2 và 3 cần hạ tầng chuyên dụng (mục 40.3).

### 🔍 BẪY 3 — Dùng địa chỉ động cho thiết bị điều khiển

**Hiện tượng:** sau mất điện, một thiết bị nhận địa chỉ khác và PLC **không thấy nó**. Máy dừng vì lý
do không liên quan gì tới máy.
**Cách sửa:** địa chỉ tĩnh; lập sơ đồ và dán trong tủ (mục 40.7).

### 🔍 BẪY 4 — Cáp thường trong xích cáp

**Hiện tượng:** ⚠ mất kết nối **ngẫu nhiên** sau vài tháng, thường khi cơ cấu ở một tư thế nhất định.
Đo thông mạch tĩnh vẫn tốt.
**Cách sửa:** cáp **chịu uốn** cho mọi chỗ chuyển động; xác nhận bằng cách lắc cáp trong lúc theo dõi
bộ đếm lỗi (mục 40.6).

### 🔍 BẪY 5 — Dùng giá trị ngõ vào của cụm I/O đã mất kết nối

**Hiện tượng:** ⚠⚠ chương trình hiểu "không có board", "cửa mở" — tuỳ tín hiệu — và hành xử theo đó.
**Cách sửa:** mất cụm nghĩa là **không biết**, không phải bằng 0. Xử lý tường minh (mục 40.8).

### 🔍 BẪY 6 — Không dùng chuyển mạch quản lý được rồi phải rút từng dây

**Hiện tượng:** có lỗi mạng ngẫu nhiên, không biết cổng nào; phải thử loại trừ bằng tay.
**Cách sửa:** chuyển mạch quản lý được cho phép **xem bộ đếm lỗi từng cổng** (mục 40.6).

### 🔍 BẪY 7 — Không ghi mốc số lỗi mạng lúc nghiệm thu

**Hiện tượng:** sáu tháng sau thấy 200 lỗi trên một cổng — nhưng không biết đó là bình thường hay đã
xấu đi.
**Cách sửa:** ghi mốc lúc chạy thử (mục 40.8, Chương 52).

### 🔍 BẪY 8 — Không lưu tệp mô tả thiết bị cùng dự án

**Hiện tượng:** mở lại dự án sau ba năm, không cấu hình được thiết bị; tệp cho đời cũ không còn tải
được.
**Cách sửa:** tệp mô tả nằm trong bản sao lưu dự án (mục 40.7, Chương 54).

### 🔍 BẪY 9 — Nối mạng máy thẳng vào mạng văn phòng

**Hiện tượng:** ⚠⚠ vừa gây vấn đề thời gian (mục 40.1), vừa là lỗ hổng an ninh — bất kỳ ai trong mạng
đều ghi được vào PLC (Chương 39, mục 39.6).
**Cách sửa:** phân vùng và tường lửa (Chương 45).

### 🔍 BẪY 10 — Chọn mạng trước khi kiểm thiết bị có hỗ trợ không

**Hiện tượng:** chốt mạng, rồi phát hiện biến tần hoặc cụm I/O cần dùng **không có bản** cho mạng đó.
**Cách sửa:** câu hỏi 3 ở mục 40.5 — kiểm **trước khi chốt**.

---

## 40.12 Bảng chốt

| Câu hỏi | Trả lời |
|---|---|
| ⭐⭐ Chuyển mạch cần bật gì cho multicast | **IGMP snooping** — thiếu thì mọi thiết bị nhận lưu lượng của mọi thiết bị |
| ⚠⚠ Vòng mạng không có giao thức | **Không phải dự phòng — là sự cố**: gói quảng bá chạy vô tận, mạng chết |
| ⭐ Triệu chứng vòng lặp | Mọi đèn cổng nháy điên loạn; **rút một sợi là hết ngay** |
| Khác biệt cốt lõi của Ethernet công nghiệp | ⭐ **Tính xác định thời gian**, không phải tốc độ |
| Họ 1 — TCP/IP thường | Chu kỳ ms · ⭐ chuyển mạch thường dùng được · I/O, biến tần, HMI, MES |
| Họ 2 — đồng bộ khe | 100 µs–1 ms · ⚠ hạ tầng chuyên dụng · chuyển động |
| Họ 3 — xử lý trên đường đi | ⭐ < 100 µs · nối chuỗi · nhiều trục |
| ⚠ "Cũng là Ethernet cả" | **Sai** — cắm vật lý được ≠ nói chuyện được |
| ⚠⚠ Trộn điều khiển với dữ liệu | **Đừng** — họ 2/3 là cấm, họ 1 là không nên |
| Bốn câu hỏi chọn mạng | Hệ PLC hỗ trợ gì · có chuyển động phối hợp không · thiết bị có bản không · ⭐ **đội quen mạng nào** |
| Cấu trúc chuỗi có rủi ro gì | ⚠ **Đứt một chỗ mất phần phía sau** |
| Vì sao nên chuyển mạch quản lý được | ⭐ **Chẩn đoán lỗi từng cổng** |
| Địa chỉ IP cho thiết bị điều khiển | ⭐ **Tĩnh** — không dùng động |
| Cáp ở chỗ chuyển động | ⚠ **Loại chịu uốn** |
| Cáp gãy lõi — triệu chứng | Mất kết nối **ngẫu nhiên**; đo tĩnh vẫn tốt |
| ⚠⚠ Mất cụm I/O nghĩa là | **Không biết** giá trị, **không phải** bằng 0 |
| Chất lượng mạng xuống cấp | Mức **"cảnh báo, vẫn chạy"**; cần **mốc từ lúc nghiệm thu** |
| Tệp mô tả thiết bị | ⚠ Lưu **cùng dự án** |

---

## 40.13 Tự kiểm

1. ⭐ Ethernet công nghiệp khác Ethernet văn phòng ở điểm cốt lõi nào? Vì sao đó không phải chuyện tốc
   độ?
2. Kể ba họ giao thức, chu kỳ điển hình và hạ tầng cần thiết của mỗi họ.
3. ⭐ Giải thích cơ chế của họ 3 (xử lý gói trên đường đi). Vì sao nó nhanh hơn hẳn?
4. ⭐⭐ Vì sao **không** được trộn lưu lượng dữ liệu với lưu lượng điều khiển? Câu trả lời khác nhau
   thế nào giữa họ 1 và họ 2/3?
5. Mô tả sự cố ở mục 40.1. Vì sao nó **không tạo ra báo lỗi nào**, và vì sao nó khó tái hiện?
6. Nêu bốn câu hỏi để chọn mạng. Câu nào thường quyết định nhất?
7. Với DP-01, vì sao nên có **hai mạng tách biệt**? Cái gì nối vào mạng nào?
8. So sánh ba cấu trúc mạng. Cấu trúc chuỗi có rủi ro gì, và vì sao triệu chứng của nó gây nhầm lẫn?
9. ⭐ Nêu lý do đáng giá nhất để mua chuyển mạch quản lý được.
10. Vì sao dùng địa chỉ **tĩnh** cho thiết bị điều khiển? Ngoại lệ hợp lý là gì?
11. ⚠ Cáp mạng gãy lõi do uốn cho triệu chứng gì, và vì sao đo thông mạch không phát hiện được? Xác
    nhận bằng cách nào?
12. ⭐⭐ Mất kết nối với một cụm I/O phân tán: chương trình được phép hiểu các ngõ vào của cụm đó bằng
    0 không? Vì sao?
13. Vì sao phải ghi **mốc số lỗi mạng** lúc nghiệm thu? Liên hệ với chương nào khác?

> Câu 1, 3, 4 và 12 là bốn câu phân loại. Câu 4 là tinh thần của cả chương: **hai gói tin trên cùng
> một sợi dây không bình đẳng — và mạng không nói cho bạn biết gói nào đã tới muộn.**

⭐⭐ **Bổ sung.** Vì sao chuyển mạch **không có IGMP snooping** làm một HMI nhỏ rớt mạng, trong khi
PLC vẫn chạy bình thường? Vì sao triệu chứng đó **xuất hiện muộn**, sau khi máy đã chạy một thời gian?

⚠⚠ **Bổ sung.** Ai đó cắm hai cổng của cùng một chuyển mạch vào nhau. Mô tả chuyện gì xảy ra, triệu
chứng nhận ra, và vì sao một cấu trúc vòng **có giao thức** lại không gặp vấn đề đó.

---

### Chương tiếp theo

Chương 41 — **Ghép nối máy–máy trong dây chuyền**. Máy của bạn hiếm khi đứng một mình. Chương sau về
bắt tay giữa hai máy: chỉ hai tín hiệu mỗi chiều mà đủ điều phối, và câu hỏi quan trọng nhất khi hai
máy gặp nhau — **ai đang giữ sản phẩm**.

### Nguồn tham khảo chương 40

- IEC 61158 và IEC 61784 (bộ) — *Industrial communication networks*: đặc tả và profile của các hệ
  truyền thông công nghiệp, trong đó có các giao thức nêu ở mục 40.3. *(tiêu chuẩn có bản quyền)*
- IEC 61918 — *Industrial communication networks — Installation of communication networks in
  industrial premises*: yêu cầu lắp đặt cáp và hạ tầng — nền cho mục 40.6.
- IEC 61800-3 — *EMC requirements for adjustable speed drives*: nền cho yêu cầu tách cáp ở mục 40.6.
- **Tài liệu mạng của hệ PLC đang dùng** — dùng cho cấu hình, công cụ chẩn đoán, và ⚠ **mạng nào được
  hỗ trợ trên dòng CPU cụ thể**.
- **Datasheet cáp và đầu nối** — dùng cho ⚠ **số lần uốn cho phép** của cáp trong xích cáp, và chiều
  dài đoạn tối đa.
- Bảng I/O và số liệu đã chốt của DP-01 — Phụ lục J.

> ⚡ Các con số về **chu kỳ** ở mục 40.3 là **bậc độ lớn điển hình**, không phải giá trị đảm bảo. Chu
> kỳ thật đạt được phụ thuộc số thiết bị, cấu hình, phần cứng, và lượng dữ liệu trao đổi. ⚠ Khi thiết
> kế hệ chuyển động phối hợp, con số phải lấy từ **tài liệu của hệ cụ thể** và nên **đo xác nhận** khi
> chạy thử.
>
> ⚠ Việc phân ba họ ở mục 40.3 là **cách phân loại thực dụng để chọn**, không phải phân loại chính
> thức trong tiêu chuẩn. Một số giao thức có nhiều chế độ nằm ở các họ khác nhau — ví dụ PROFINET có
> cả chế độ chạy trên TCP/IP thường và chế độ đồng bộ. ⭐ **Kiểm chế độ cụ thể**, đừng kết luận từ tên
> giao thức.
