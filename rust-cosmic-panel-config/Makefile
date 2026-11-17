# Name of the package
NAME = rust-cosmic-panel-config

# Version
VERSION = 1.10.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/cosmic-panel

# URL of the upstream source archive
URL_SRC = https://github.com/pop-os/cosmic-panel/archive/3ce6ce1cec97669f91e809962d9446aaefe8a06e.tar.gz

# short summary of what the package provides
SUMMARY = COSMIC panel configuration - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crates "cosmic-panel-config" and "xdg-shell-wrapper-config"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-cosmic-panel-config:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# These crates are not published on crates.io; their source is a tarball
# built from the upstream cosmic-panel git tree at the revision pinned by
# cosmic-applets' Cargo.lock. The xdg-shell-wrapper-config crate is a path
# dependency of cosmic-panel-config, so it is packaged alongside it.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O cosmic-panel-config-1.10.0.tar.gz
	@rm -rf $(SOURCE_DIR)/.crate_extract && mkdir -p $(SOURCE_DIR)/.crate_extract
	@tar -xzf $(CACHE_DIR)/cosmic-panel-config-1.10.0.tar.gz -C $(SOURCE_DIR)/.crate_extract
	@cp -a $(SOURCE_DIR)/.crate_extract/*/cosmic-panel-config/. $(SOURCE_DIR)/
	@cp -a $(SOURCE_DIR)/.crate_extract/*/xdg-shell-wrapper-config $(SOURCE_DIR)/
	@rm -rf $(SOURCE_DIR)/.crate_extract
	@$(SOURCE_TAR_CMD)
