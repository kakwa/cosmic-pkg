#!/usr/bin/env python3
"""Remove rustc-std-workspace optional dependencies unavailable in Debian."""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()
text = text.replace('    "rustc-dep-of-std",\n', '')
text = re.sub(r'rustc-dep-of-std = \[\n(?:    .*\n)*?\]\n', '', text)
text = re.sub(r'\[dependencies\.(?:alloc|core)\]\n(?:.*\n)*?optional = true\npackage = "rustc-std-workspace-(?:alloc|core)"\n\n', '', text)
path.write_text(text)
