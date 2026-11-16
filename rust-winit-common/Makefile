# Name of the package
NAME = rust-winit-common

# Version
VERSION = 0.31.0~beta.2

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/winit

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/winit-common/winit-common-0.31.0-beta.2.crate

# short summary of what the package provides
SUMMARY = Winit common internals - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "winit-common"

# License of the upstream project
LICENSE = Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-winit-common:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# Recover the upstream sources from crates.io.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(notdir $(URL_SRC))
	@tar -xf $(CACHE_DIR)/$(notdir $(URL_SRC)) -C $(SOURCE_DIR) --strip-components=1
	@$(SOURCE_TAR_CMD)
