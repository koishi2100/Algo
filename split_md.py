#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re
import sys
from pathlib import Path


def sanitize(name: str) -> str:
    name = re.sub(r'[\\/:*?"<>|]', '_', name).strip().strip('.')
    return name or 'unnamed'


def split_md(source: Path, output_dir: Path) -> None:
    text = source.read_text(encoding='utf-8-sig')
    lines = text.splitlines()

    headings = [
        i for i, line in enumerate(lines)
        if line.startswith('# ') or line == '#'
    ]

    output_dir.mkdir(parents=True, exist_ok=True)
    for k, idx in enumerate(headings):
        end = headings[k + 1] if k + 1 < len(headings) else len(lines)
        body = '\n'.join(lines[idx:end])
        title = lines[idx][2:].strip() if lines[idx] != '#' else 'unnamed'
        out = output_dir / f'{sanitize(title)}.md'
        out.write_text(body.rstrip() + '\n', encoding='utf-8')
        print(f'{out.name}  ({end - idx} 行)')


def main() -> None:
    src = Path(sys.argv[1]) if len(sys.argv) > 1 else Path('Algo.md')
    out = Path(sys.argv[2]) if len(sys.argv) > 2 else Path('released/raw')
    split_md(src, out)


if __name__ == '__main__':
    main()
