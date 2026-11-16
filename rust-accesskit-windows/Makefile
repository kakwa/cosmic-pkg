# Name of the package
NAME = rust-accesskit-windows

# Version
VERSION = 0.30.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/wash2/accesskit

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/accesskit_windows/accesskit_windows-0.30.0.crate

# short summary of what the package provides
SUMMARY = Accessibility API for Windows - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "accesskit_windows"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-accesskit-windows:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(notdir $(URL_SRC))
	@tar -xf $(CACHE_DIR)/$(notdir $(URL_SRC)) -C $(SOURCE_DIR) --strip-components=1
	@$(SOURCE_TAR_CMD)
