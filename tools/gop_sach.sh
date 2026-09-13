#!/bin/bash
# tools/gop_sach.sh — Ghép bìa + mục lục + 58 chương + 13 phụ lục thành MỘT file .md
# và MỘT file .html hoàn chỉnh (có mục lục bên trái, id neo, bảng cuộn ngang trên
# điện thoại), rồi sao chép sang repo phát hành.
#
# Chạy bằng Bash (Git Bash trên Windows) từ bất kỳ đâu trong repo — script tự về gốc.
#
# Dùng:
#   bash tools/gop_sach.sh                 # phiên bản = ${BASE_VERSION}.<hôm nay YYMMDD>
#   bash tools/gop_sach.sh v1.1.0.260915   # ép phiên bản cụ thể
#   bash tools/gop_sach.sh --khong-chep    # chỉ ghép, không sao chép sang repo phát hành
#
# ⚠ QUY ƯỚC PHIÊN BẢN (xem CLAUDE.md mục "Quy ước gộp sách và phiên bản"):
#   - Mỗi lần ghép lại: phiên bản = ${BASE_VERSION}.<ngày hôm nay YYMMDD>.
#   - Có đợt bổ sung nội dung LỚN → SỬA BASE_VERSION bên dưới (tăng MINOR/MAJOR),
#     đừng chỉ truyền tham số một lần, vì lần ghép sau sẽ tụt lại.
#   - Script tự cập nhật số phiên bản trong cover.md và cover.html.
#
# ⚠ AN TOÀN: khi dọn bản cũ, script CHỈ xoá file mang đúng tên sách này.
#   Thư mục phát hành còn sách khác — không được đụng vào.
#
# Yêu cầu: Node.js (npx marked), Python 3.

set -e
cd "$(dirname "$0")/.."

BASE_VERSION="v1.0.0"          # tăng khi có đợt bổ sung nội dung lớn
TITLE="So tay Lap trinh PLC va Dieu khien May Tu dong hoa"   # không dấu, không ký tự đặc biệt

KHONG_CHEP=0
VERSION=""
for a in "$@"; do
  case "$a" in
    --khong-chep) KHONG_CHEP=1 ;;
    v*) VERSION="$a" ;;
  esac
done
VERSION="${VERSION:-${BASE_VERSION}.$(date +%y%m%d)}"

DICH="/c/Users/dinhn/OneDrive/Study/Chung/CSharp Automation Machine/CSharp-Automation-Machine/book"
OUT_MD="output/${TITLE} ${VERSION}.md"
OUT_HTML="output/${TITLE} ${VERSION}.html"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

echo "== Ghep sach phien ban ${VERSION} =="

# 0. Chan phat hanh khi ban thao con LOI
echo "-- Chay bo kiem truoc khi ghep"
python tools/kiem_tra_chuong.py > "$TMP/k1.txt" 2>&1 || { cat "$TMP/k1.txt"; echo "!! kiem_tra_chuong.py bao LOI — dung ghep"; exit 1; }
python tools/kiem_nhat_quan.py  > "$TMP/k2.txt" 2>&1 || { cat "$TMP/k2.txt"; echo "!! kiem_nhat_quan.py bao LOI — dung ghep"; exit 1; }
tail -2 "$TMP/k1.txt"; tail -2 "$TMP/k2.txt"

# 1. Cap nhat so phien ban trong bia
sed -i -E "s/v[0-9]+\.[0-9]+\.[0-9]+\.[0-9]{6}/${VERSION}/g" output/cover.md output/cover.html

# 2. Ghep .md — moi phan co marker <!-- SECTION: NHAN --> de doi chieu ve sau
: > "$OUT_MD"
{
  echo "<!-- SECTION: COVER -->"; cat output/cover.md; echo ""
  echo "<!-- SECTION: MucLuc -->"; echo "---"; cat docs/00_Muc_luc.md; echo ""
  for n in $(seq -w 1 58); do
    f=$(ls docs/ch${n}_*.md 2>/dev/null | head -1)
    [ -z "$f" ] && { echo "!! THIEU chuong ${n}" >&2; exit 1; }
    echo "<!-- SECTION: $(basename "$f" .md) -->"; echo "---"; cat "$f"; echo ""
  done
  for pl in a1 a2 b c d e f g h i j k l; do
    f=$(ls docs/pl_${pl}_*.md 2>/dev/null | head -1)
    [ -z "$f" ] && { echo "!! THIEU phu luc ${pl}" >&2; exit 1; }
    echo "<!-- SECTION: $(basename "$f" .md) -->"; echo "---"; cat "$f"; echo ""
  done
} >> "$OUT_MD"
echo "-- Da ghep .md: $(wc -l < "$OUT_MD") dong"

# 3. Markdown -> HTML tho (GitHub-flavored)
# Nhung anh ../assets/*.svg thanh data-URI base64 -> ban .md va .html TU DUNG MOT MINH.
# Kho phat hanh KHONG co thu muc assets/; de nguyen ../assets thi anh se VO khi chia se file le.
python tools/nhung_anh.py "$OUT_MD"

npx marked --gfm -i "$OUT_MD" -o "$TMP/body_raw.html"

# 4. Sinh muc luc + gan id vao h1/h2
python tools/build_toc.py "$OUT_MD" "$TMP/body_raw.html" "$TMP/toc.html" "$TMP/body_ids.html"
[ -f "$TMP/toc.html.log" ] && cat "$TMP/toc.html.log"

# 5. Boc <table> de cuon ngang tren dien thoai
python tools/wrap_tables.py "$TMP/body_ids.html" "$TMP/body_final.html"

# 6. Ghep head + muc luc + than + foot
sed "s/{{VERSION}}/${VERSION}/" tools/merge_assets/book_head.html > "$OUT_HTML"
cat "$TMP/toc.html" >> "$OUT_HTML"
echo '<div id="main">' >> "$OUT_HTML"
cat "$TMP/body_final.html" >> "$OUT_HTML"
echo '</div>' >> "$OUT_HTML"
cat tools/merge_assets/book_foot.html >> "$OUT_HTML"
echo "-- Da ghi .html: $(wc -l < "$OUT_HTML") dong"

# 7. Don ban cu TRONG output — chi file mang dung ten sach nay
find output -maxdepth 1 -name "${TITLE} v*.md"   ! -name "${TITLE} ${VERSION}.md"   -delete
find output -maxdepth 1 -name "${TITLE} v*.html" ! -name "${TITLE} ${VERSION}.html" -delete

# 8. Sao chep sang repo phat hanh
if [ "$KHONG_CHEP" = "1" ]; then
  echo "== Xong (khong chep): \"$OUT_MD\""
  exit 0
fi
if [ ! -d "$DICH" ]; then
  echo "!! Khong thay thu muc phat hanh: $DICH"
  exit 1
fi
# ⚠ CHI xoa ban cu CUA SACH NAY. Thu muc con co sach khac — khong duoc dung vao.
find "$DICH" -maxdepth 1 -name "${TITLE} v*.md"   ! -name "${TITLE} ${VERSION}.md"   -delete
find "$DICH" -maxdepth 1 -name "${TITLE} v*.html" ! -name "${TITLE} ${VERSION}.html" -delete
cp "$OUT_MD" "$OUT_HTML" "$DICH/"
echo "-- Da chep sang: $DICH"
echo "-- Sach khac trong thu muc do (giu nguyen):"
ls "$DICH" | grep -v "^${TITLE}" | sed 's/^/     /'

echo "== Xong phien ban ${VERSION} =="
echo "   Buoc tiep: commit + push trong repo phat hanh."
