# -*- coding: utf-8 -*-
"""Lập chỉ mục cấu trúc của bộ tài liệu nguồn.

Đọc mục lục nhúng (bookmark/outline) của mọi PDF trong cây tài liệu nguồn và
ghi ra một chỉ mục JSON: tệp -> danh sách (mức, tiêu đề, trang).

Vì sao cần: bộ nguồn có hàng chục nghìn trang. Tìm bằng từ khoá chỉ trả về
trang, không cho biết trang đó nằm ở MỤC nào — nên không biết mục nào đã đọc
và mục nào chưa bao giờ được nhìn tới. Chỉ mục này là nền cho `ban_do_nguon.py`.

Dùng:
    python tools/lap_chi_muc_nguon.py              # lập lại chỉ mục
    python tools/lap_chi_muc_nguon.py --tom-tat    # chỉ in thống kê
"""
import os
import sys
import json

GOC = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NGUON = os.path.normpath(os.path.join(GOC, "..", "PLC"))
DICH = os.path.join(GOC, "tools", "chi_muc_nguon.json")


def xp(s):
    """In an toàn trên console mã hoá hẹp (gbk)."""
    try:
        print(s)
    except UnicodeEncodeError:
        print(s.encode("ascii", "replace").decode("ascii"))


def liet_ke_pdf():
    ds = []
    for thu_muc, _, tep in os.walk(NGUON):
        for t in tep:
            if t.lower().endswith(".pdf"):
                ds.append(os.path.join(thu_muc, t))
    return sorted(ds)


def lap_chi_muc():
    import pymupdf

    ket_qua = {}
    for duong in liet_ke_pdf():
        khoa = os.path.relpath(duong, NGUON).replace("\\", "/")
        muc = {"so_trang": 0, "co_bookmark": False, "trich_duoc": False, "muc_luc": []}
        try:
            d = pymupdf.open(duong)
            muc["so_trang"] = d.page_count
            toc = d.get_toc()
            muc["co_bookmark"] = bool(toc)
            muc["muc_luc"] = [[m, (t or "").strip()[:160], p] for m, t, p in toc]
            # trích được text hay không: thử 3 trang giữa
            mau = ""
            for i in {0, d.page_count // 2, max(0, d.page_count - 1)}:
                try:
                    mau += d[i].get_text()
                except Exception:  # noqa: BLE001 - trang hỏng thì bỏ qua
                    pass
            muc["trich_duoc"] = len(mau.strip()) > 200
            d.close()
        except Exception as e:  # noqa: BLE001 - tệp hỏng vẫn phải vào chỉ mục
            muc["loi"] = str(e)[:200]
        ket_qua[khoa] = muc
    return ket_qua


def main():
    if not os.path.isdir(NGUON):
        xp("KHONG THAY thu muc nguon: %s" % NGUON)
        return 1
    ck = lap_chi_muc()
    with open(DICH, "w", encoding="utf-8") as f:
        json.dump(ck, f, ensure_ascii=False, indent=1)

    tong_tr = sum(v["so_trang"] for v in ck.values())
    co_bm = sum(1 for v in ck.values() if v["co_bookmark"])
    khong_trich = [k for k, v in ck.items() if not v["trich_duoc"]]
    tong_muc = sum(len(v["muc_luc"]) for v in ck.values())

    xp("Da lap chi muc: %s" % os.path.relpath(DICH, GOC))
    xp("  Tai lieu PDF     : %d" % len(ck))
    xp("  Tong so trang    : %d" % tong_tr)
    xp("  Co muc luc nhung : %d  (%d muc)" % (co_bm, tong_muc))
    xp("  KHONG trich duoc : %d" % len(khong_trich))
    for k in khong_trich:
        xp("     ! %s" % k)
    return 0


if __name__ == "__main__":
    sys.exit(main())
