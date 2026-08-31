#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将 pdf/*.pdf 复制到 print/，并为其在开头插入 other/封面.pdf、结尾插入 other/封底.pdf。
封面上的 "Algo" 会被替换为对应文件名（不含后缀）。
"""
import shutil
from pathlib import Path

import pymupdf

ROOT = Path(__file__).resolve().parent
PDF_DIR = ROOT / 'pdf'
PRINT_DIR = ROOT / 'print'
COVER = ROOT / 'other' / '封面.pdf'
BACK = ROOT / 'other' / '封底.pdf'

FONT = 'C:/Windows/Fonts/simsun.ttc'
SIZE = 48.0

CM = 72 / 25.4
MARGIN = 5.0 * CM
PAGENO_SIZE = 9.5
PAGENO_COLOR = (0.35, 0.35, 0.35)


def stamp_page_numbers(doc: pymupdf.Document, margin: float) -> None:
    for i in range(doc.page_count):
        page = doc[i]
        num = i + 1
        W, H = page.rect.width, page.rect.height
        y = H - margin
        x = W - margin - pymupdf.get_text_length(str(num), fontname='helv', fontsize=PAGENO_SIZE)
        if num % 2 == 0:
            x = margin
        page.insert_text((x, y), str(num), fontname='helv',
                         fontsize=PAGENO_SIZE, color=PAGENO_COLOR)


def cover_with_title(title: str) -> pymupdf.Document:
    doc = pymupdf.open(str(COVER))
    page = doc[0]
    rects = page.search_for('Algo')
    if not rects:
        raise RuntimeError(f'封面中未找到 "Algo"')
    rect = rects[0]
    page.add_redact_annot(rect, fill=(1, 1, 1))
    page.apply_redactions()

    font = pymupdf.Font(fontfile=FONT)
    size = SIZE
    while font.text_length(title, size) > page.rect.width - 60 and size > 18:
        size -= 1
    w = font.text_length(title, size)
    cx = page.rect.width / 2
    cy = rect.y1 - size * 0.13
    page.insert_text((cx - w / 2, cy), title, fontsize=size,
                     fontname='F0', fontfile=FONT)
    return doc


def build_one(src: Path) -> None:
    title = src.stem
    out = PRINT_DIR / src.name
    shutil.copy2(src, out)

    cover = cover_with_title(title)
    body = pymupdf.open(str(out))
    stamp_page_numbers(body, MARGIN)
    back = pymupdf.open(str(BACK))

    result = pymupdf.open()
    result.insert_pdf(cover)
    result.insert_pdf(body)
    result.insert_pdf(back)

    cover.close()
    body.close()
    back.close()
    result.save(str(out), garbage=4, deflate=True)
    result.close()
    print(f'{src.name} -> print/{out.name}')


def main() -> None:
    PRINT_DIR.mkdir(parents=True, exist_ok=True)
    for src in sorted(PDF_DIR.glob('*.pdf')):
        build_one(src)


if __name__ == '__main__':
    main()
