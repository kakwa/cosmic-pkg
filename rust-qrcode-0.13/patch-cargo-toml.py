#!/usr/bin/env python3
"""Remove the unavailable image 0.24 dependency and feature."""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()
text = re.sub(r'\[dependencies\.image\]\n(?:.*\n)*?default-features = false\n\n', '', text)
text = re.sub(r'\[dev-dependencies\.image\]\n(?:.*\n)*?\n', '', text)
text = text.replace('default = [\n    "image",\n    "svg",\n]\n', 'default = ["svg"]\n')
path.write_text(text)
