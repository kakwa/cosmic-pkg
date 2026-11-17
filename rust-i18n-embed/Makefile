# Name of the package
NAME = rust-i18n-embed

# Version
VERSION = 0.16.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://crates.io/crates/i18n-embed

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/i18n-embed/i18n-embed-0.16.0.crate

# short summary of what the package provides
SUMMARY = Compile-time embedding of localization assets - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "i18n-embed"

# License of the upstream project
LICENSE = MIT

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-i18n-embed:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# Recover the upstream sources from crates.io.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(notdir $(URL_SRC))
	@tar -xf $(CACHE_DIR)/$(notdir $(URL_SRC)) -C $(SOURCE_DIR) --strip-components=1
	@$(SOURCE_TAR_CMD)
