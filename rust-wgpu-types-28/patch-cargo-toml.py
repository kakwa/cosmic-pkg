#!/usr/bin/env python3
"""Remove web-sys features unavailable in Debian from wgpu-types' Cargo.toml."""
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()
for feature in ('ImageBitmap', 'ImageData', 'HtmlImageElement', 'HtmlVideoElement', 'VideoFrame'):
    text = text.replace(f'    "{feature}",\n', '')
path.write_text(text)
