"""
Sinh mục lục (nav#toc) + gắn id vào mọi h1/h2 của body HTML đã render từ
merged .md — dùng trong pipeline merge_book.sh.

Usage: python build_toc.py <merged.md> <body_raw.html> <toc_out.html> <body_ids_out.html>
"""
import re
import sys

md_path, body_raw_path, toc_out_path, body_ids_out_path = sys.argv[1:5]

with open(md_path, encoding='utf-8') as f:
    lines = f.read().split('\n')

toc_items = []  # (level, text, anchor)
seen = {}
in_code = False
for line in lines:
    stripped = line.strip()
    if stripped.startswith('```') or stripped.startswith('~~~'):
        in_code = not in_code
        continue
    if in_code:
        continue
    m = re.match(r'^(#{1,6})\s+(.*)', line)
    if not m:
        continue
    level = len(m.group(1))
    if level not in (1, 2):
        continue
    text = m.group(2).strip()
    anchor = re.sub(r'[^a-zA-Z0-9À-ɏ\s-]', '', text)
    anchor = re.sub(r'\s+', '-', anchor.strip()).lower()
    if not anchor:
        anchor = 'section'
    base = anchor
    n = seen.get(base, 0)
    if n:
        anchor = f'{base}-{n+1}'
    seen[base] = n + 1
    toc_items.append(('h1' if level == 1 else 'h2', text, anchor))

# Inject id vào body HTML
with open(body_raw_path, encoding='utf-8') as f:
    body = f.read()

idx = [0]
rendered = []  # nội dung tiêu đề ĐÃ render, cùng thứ tự với toc_items
def inject(m):
    tag = m.group(1)
    inner = m.group(2)
    level, text, anchor = toc_items[idx[0]]
    idx[0] += 1
    rendered.append(inner)
    return f'<{tag} id="{anchor}">{inner}</{tag}>'

body2 = re.sub(r'<(h1|h2)>(.*?)</\1>', inject, body, flags=re.DOTALL)

# Sinh HTML mục lục — dùng tiêu đề ĐÃ render từ body, không dùng chữ markdown thô.
# Chữ thô làm lộ nguyên ký hiệu ra mục lục: "khi nào **không** nên dùng", "*(POU)*", "&".
khop = len(rendered) == len(toc_items)
toc_html = '<nav id="toc"><h2>Mục lục</h2><ul>\n'
for i, (level, text, anchor) in enumerate(toc_items):
    if khop:
        text = re.sub(r'</?a\b[^>]*>', '', rendered[i]).strip()
    indent = '' if level == 'h1' else ' style="padding-left:16px;font-size:13px"'
    toc_html += f'  <li{indent}><a href="#{anchor}">{text}</a></li>\n'
toc_html += '</ul></nav>\n'

with open(toc_out_path, 'w', encoding='utf-8') as f:
    f.write(toc_html)

with open(body_ids_out_path, 'w', encoding='utf-8') as f:
    f.write(body2)

with open(toc_out_path + '.log', 'w', encoding='utf-8') as f:
    f.write(f"Muc luc: {len(toc_items)} muc\n")
    f.write(f"Da gan id cho {idx[0]} heading trong body (khop = {idx[0]==len(toc_items)})\n")
