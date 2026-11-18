#!/usr/bin/env python3
"""Remove web-sys features unavailable in Debian from wgpu-hal's Cargo.toml."""
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()
text = text.replace('    "WebGl2RenderingContext",\n', '')
path.write_text(text)
