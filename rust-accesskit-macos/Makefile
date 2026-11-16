# Name of the package
NAME = rust-accesskit-macos

# Version
VERSION = 0.23.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/wash2/accesskit

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/accesskit_macos/accesskit_macos-0.23.0.crate

# short summary of what the package provides
SUMMARY = Accessibility API for macOS - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "accesskit_macos"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-accesskit-macos:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(notdir $(URL_SRC))
	@tar -xf $(CACHE_DIR)/$(notdir $(URL_SRC)) -C $(SOURCE_DIR) --strip-components=1
	@$(SOURCE_TAR_CMD)
