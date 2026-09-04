# 0004 — Bản đồ nguồn ↔ chương, và chuyện chuyển PDF sang Markdown

- **Ngày:** 2026-09-03
- **Trạng thái:** Đã áp dụng — `tools/lap_chi_muc_nguon.py`, `tools/ban_do_nguon.py`, `docs/00e_Ban_do_nguon.md`
- **Phạm vi:** cách theo dõi **độ phủ** của bộ tài liệu nguồn, để nội dung không bị bỏ sót vì nguồn quá lớn

---

## Bối cảnh

Sau 22 đợt đối chiếu nguồn, một mẫu lỗi lặp lại đủ nhiều để coi là **lỗi hệ thống của quy trình**,
không phải xui rủi:

| Đợt | Chuyện đã xảy ra |
|---|---|
| 2 | Kết luận *"không có tài liệu CODESYS và Inovance"* — ⚠ **sai**, chúng nằm ở thư mục cha mà tôi không quét |
| 15 | Quét từ khoá báo *"Ch.11 thiếu ép kiểu"* — ⚠ **sai**, nội dung nằm ở Ch.19 với từ khác |
| 22 | Tìm ra `VAR_IN_OUT` **do tình cờ** grep một từ khoá khác; nó vắng mặt trong **cả cuốn sách** |

⭐⭐ **Nguyên nhân chung: tôi chỉ tra được những gì tôi NGHĨ RA để tra.** Bộ tài liệu có
**63 tệp PDF · 23.139 trang**. Không có cơ chế nào cho biết *phần nào của bộ tài liệu chưa ai nhìn
tới* — nên một chủ đề có thể được tài liệu phủ đầy đủ mà chương liên quan vẫn thiếu, và **không có
gì báo động**.

⚠ Ba bộ kiểm hiện có **không bắt được loại này**: chúng kiểm bản thảo với chính nó, không kiểm bản
thảo với nguồn.

---

## Các phương án đã cân nhắc

### A — Chuyển toàn bộ 23.139 trang sang Markdown bằng công cụ ML

Dùng [`marker`](https://github.com/datalab-to/marker) (~18k sao) hoặc **MinerU** — hai công cụ mạnh
nhất hiện nay, dùng thị giác máy tính và OCR học sâu, chất lượng bảng và bố cục nhiều cột tốt nhất.

| Ưu | Nhược |
|---|---|
| Chất lượng cao nhất với bảng, nhiều cột, tài liệu quét | ⚠⚠ **Máy này chỉ có `torch` bản CPU** (đã kiểm: `cuda False`) |
| MinerU mạnh với tài liệu CJK — bộ có nhiều tài liệu tiếng Trung | ⚠ 23.139 trang trên CPU: hàng chục giờ |
| | ⚠ Kết quả ~70 MB Markdown — **quá lớn để đọc**, chỉ để tìm kiếm |
| | ⚠ Phải cài thêm vài GB trọng số mô hình |

### B — Chuyển toàn bộ bằng `pymupdf4llm` (không cần ML)

| Ưu | Nhược |
|---|---|
| ⭐ **Đã cài sẵn** (1.28.2) | ⚠ Chất lượng bảng kém hơn A rõ rệt |
| ⭐ Đo thật: **0,4 s/trang** → toàn bộ ~**151 phút**, không cần GPU | ⚠ Vẫn ra ~70 MB — vấn đề "quá lớn để đọc" **không được giải quyết** |
| | ⚠ Không OCR — 3 tệp quét vẫn không đọc được |

### C — Không chuyển gì cả; lập **chỉ mục cấu trúc** từ mục lục nhúng của PDF

| Ưu | Nhược |
|---|---|
| ⭐⭐ Đo thật: **47/63 tệp có mục lục nhúng, tổng 11.231 mục** | ⚠ 16 tệp không có mục lục → chỉ biết tên và số trang |
| ⭐ Chạy hết trong **vài giây**, kết quả ~2 MB JSON | ⚠ Không cho **nội dung**, chỉ cho **cấu trúc** |
| ⭐⭐ Cấu trúc mới là thứ cần cho việc **đo độ phủ** | |

---

## Phương án chọn: **C**, và **không** làm A hay B

⭐⭐ **Lý do cốt lõi: bài toán bị đặt sai tên.** Yêu cầu ban đầu nghe như *"cần chuyển PDF sang MD"*,
nhưng thứ thật sự thiếu không phải **định dạng** — mà là **cơ chế biết mình đã đọc tới đâu**.

Chuyển 70 MB Markdown không giải quyết được điều đó: ⚠ nó chỉ đổi 23.139 trang không đọc hết được
thành 70 MB không đọc hết được. Việc tìm kiếm thì bộ đệm `pdftotext` hiện có **đã làm được rồi**.

⭐ Cái còn thiếu là câu hỏi ⚠ **"tài liệu nào chưa được chương nào dẫn?"** — và câu hỏi đó chỉ cần
**cấu trúc**, không cần nội dung.

### Hiện thực

| Thành phần | Việc |
|---|---|
| `tools/lap_chi_muc_nguon.py` | Đọc mục lục nhúng mọi PDF → `tools/chi_muc_nguon.json`; đánh dấu tệp **không trích được text** |
| `tools/cau_hinh_ban_do.json` | Ánh xạ **bí danh nguồn** (tên xuất hiện trong sách) ↔ **tệp thật** |
| `tools/ban_do_nguon.py` | Ghép chỉ mục + mục *Nguồn tham khảo* của 58 chương + nhật ký đối chiếu → `docs/00e_Ban_do_nguon.md` |

Bản đồ có **sáu phần**, trong đó phần 2 là lý do tồn tại của cả công cụ: ⚠⚠ **nguồn chưa được chương
nào dẫn**.

---

## Kết quả ngay lần chạy đầu

| Phát hiện | Ý nghĩa |
|---|---|
| ⚠⚠ **15 nguồn · ~6.975 trang chưa được chương nào dẫn** | Trong đó **Hugh Jack** (860 tr.) — ⭐ nguồn mạnh nhất cho nhóm chương **thiết kế (22–30)**, nhóm mà nhật ký đã ghi là *"khó đối chiếu bằng tài liệu"* |
| ⚠ **Rabiee — 1 trong 4 giáo trình đã mua — KHÔNG trích được text** | Nó nằm trong ADR 0003 như nguồn sẵn có; thực tế **coi như không có** cho tới khi OCR |
| ⚠ Ch.47 tổng quát hoá nguồn an toàn | Thân chương nêu đích danh SICK và DGUV/IFA, danh sách nguồn thì viết *"nhà sản xuất thiết bị an toàn"* — **đã sửa** thành tên thật |
| 266 dòng nguồn / 157 tên khác nhau | Phần lớn là **tiêu chuẩn không có bản gốc**; giáo trình đọc được thì bị dẫn rất ít |

⭐⭐ **Phát hiện đắt nhất là dòng đầu:** nhóm chương thiết kế được nhật ký xếp vào diện *"chủ yếu là
phương pháp và kinh nghiệm nghề, ít đối chiếu được"* — trong khi ⚠ **nguồn tốt nhất cho đúng nhóm đó
vẫn nằm nguyên, chưa mở**. Kết luận cũ **sai**, và ⭐ **chỉ có bản đồ mới lộ ra**.

---

## Hệ quả

1. ⭐ Bộ kiểm tự động lên **bốn**: ba bộ cũ kiểm *bản thảo với chính nó*, bản đồ kiểm *bản thảo với
   bộ nguồn*.
2. ⭐ **Chạy lại bản đồ sau mỗi đợt đối chiếu** — số nguồn chưa dẫn phải **giảm dần**; nếu nó đứng
   yên thì đợt đó chỉ đào sâu chỗ đã quen.
3. ⚠ Bản đồ **cố tình báo thừa**: nguồn được dẫn bằng tên tổng quát sẽ hiện ra như *"chưa dẫn"*. Đó
   là **hành vi mong muốn** — nó ép danh sách nguồn phải nêu đích danh thứ đã thật sự đọc.
4. ⚠⚠ **Ba tệp không trích được text** phải OCR hoặc **ghi rõ là không có** — không được tiếp tục
   liệt kê chúng như nguồn sẵn có.
5. ⚡ Nếu sau này cần **chất lượng trích cao** cho một tài liệu cụ thể (bảng phức tạp), phương án A/B
   vẫn dùng được **cho riêng tài liệu đó** — không cần chuyển cả bộ.

---

## Ghi chú về công cụ đã khảo sát

Tham khảo, kèm lý do không chọn cho bộ này:

| Công cụ | Ghi chú |
|---|---|
| [`marker`](https://github.com/datalab-to/marker) | Chất lượng cao nhất cho tài liệu dày đặc; ⚠ cần GPU để thực dụng |
| **MinerU** (OpenDataLab) | Mạnh nhất với bố cục phức tạp và tài liệu CJK; ⚠ cùng ràng buộc GPU |
| [`docling`](https://github.com/docling-project/docling) (IBM) | Điểm cao nhất về bảng và tiêu đề trong benchmark OpenDataLoader; giấy phép MIT |
| [`markitdown`](https://github.com/microsoft/markitdown) (Microsoft) | ⭐ Đã cài sẵn (0.1.6); ⚠ **PDF là điểm yếu nhất** của nó — hợp cho Office, không hợp ở đây |
| `pymupdf4llm` | ⭐ Đã cài; 0,4 s/trang, không cần GPU — **lựa chọn đúng nếu về sau cần chuyển một tài liệu cụ thể** |
