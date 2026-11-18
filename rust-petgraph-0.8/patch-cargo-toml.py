#!/usr/bin/env python3
"""Remove optional dependencies unavailable in Debian."""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()
text = text.replace('    "dot_parser",\n', '')
text = text.replace('dot_parser = [\n    "std",\n    "dep:dot-parser",\n    "dep:dot-parser-macros",\n]\n', '')
text = re.sub(r'\[dependencies\.dot-parser(-macros)?\]\nversion = "0\.5\.1"\noptional = true\n\n', '', text)
text = text.replace('    "quickcheck",\n', '')
text = re.sub(r'\[dependencies\.quickcheck\]\n(?:.*\n)*?optional = true\n(?:.*\n)*?\n', '', text)
text = re.sub(r'\[\[test\]\]\nname = "quickcheck"\npath = "tests/quickcheck\.rs"\n\n', '', text)
path.write_text(text)
