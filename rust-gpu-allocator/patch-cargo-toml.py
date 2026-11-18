#!/usr/bin/env python3
"""Remove the visualizer feature and unavailable egui dependencies."""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()
text = re.sub(r'visualizer = \[\n(?:    .*\n)*?\]\n', '', text)
text = re.sub(r'\[dependencies\.egui(?:_extras)?\]\n(?:.*\n)*?optional = true\n(?:.*\n)*?\n', '', text)
path.write_text(text)
