#!/usr/bin/env python3
"""Remove the unavailable resvg 0.45 dependency and its SVG feature."""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()
text = re.sub(r'svg = \[\n(?:    .*\n)*?\]\n', '', text)
text = re.sub(r'\[dependencies\.resvg\]\n(?:.*\n)*?optional = true\n(?:.*\n)*?\n', '', text)
path.write_text(text)
