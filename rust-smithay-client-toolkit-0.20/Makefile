# Name of the package
NAME = rust-smithay-client-toolkit-0.20

# Version
VERSION = 0.20.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://crates.io/crates/smithay-client-toolkit

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/smithay-client-toolkit/smithay-client-toolkit-0.20.0.crate

# short summary of what the package provides
SUMMARY = Toolkit for making client wayland applications

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "smithay-client-toolkit"

# License of the upstream project
LICENSE = MIT

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# Recover the upstream sources from crates.io.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(notdir $(URL_SRC))
	@tar -xf $(CACHE_DIR)/$(notdir $(URL_SRC)) -C $(SOURCE_DIR) --strip-components=1
	@$(SOURCE_TAR_CMD)
