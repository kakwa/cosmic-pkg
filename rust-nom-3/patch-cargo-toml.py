#!/usr/bin/env python3
"""Drop nom 3 optional features that pull unavailable old crates.

mccs-caps only needs nom's default and verbose-errors features.  The
regexp/nightly/regexp_macros features require regex 0.2, compiler-error 0.1
and lazy_static 0.2, which are not packaged in Debian sid.  Removing the
features and their optional dependencies keeps the generated Depends accurate.
"""
import re
import sys
from pathlib import Path

path = Path(sys.argv[1])
text = path.read_text()

text = re.sub(
    r"(?ms)^\[dependencies\.(?:compiler_error|regex|lazy_static)\]\n.*?(?=^\[|\Z)",
    "",
    text,
)
text = re.sub(
    r"(?m)^(?:regexp|nightly|regexp_macros)\s*=.*\n",
    "",
    text,
)
# The published crate does not ship README.md even though Cargo.toml names it.
text = re.sub(r'(?m)^readme\s*=.*\n', "", text)

path.write_text(text)
