"""Bọc <table> trong <div class="table-wrap"> để cuộn ngang được trên mobile.

Usage: python wrap_tables.py <body_ids.html> <body_final.html>
"""
import re
import sys

in_path, out_path = sys.argv[1:3]

with open(in_path, encoding='utf-8') as f:
    body = f.read()
body = re.sub(r'<table>', '<div class="table-wrap"><table>', body)
body = re.sub(r'</table>', '</table></div>', body)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(body)
