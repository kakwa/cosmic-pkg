# Name of the package
NAME = rust-clipboard-macos

# Version
VERSION = 0.1.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/hecrj/window_clipboard

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/clipboard_macos/clipboard_macos-0.1.0.crate

# short summary of what the package provides
SUMMARY = macOS clipboard backend - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "clipboard_macos"

# License of the upstream project
LICENSE = MIT

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-clipboard-macos:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# Recover the upstream sources from crates.io.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(notdir $(URL_SRC))
	@tar -xf $(CACHE_DIR)/$(notdir $(URL_SRC)) -C $(SOURCE_DIR) --strip-components=1
	@$(SOURCE_TAR_CMD)
