# Name of the package
NAME = rust-cosmic-settings-config

# Version
VERSION = 1.10.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/cosmic-settings-daemon

# URL of the upstream source archive
URL_SRC = https://github.com/pop-os/cosmic-settings-daemon/archive/8844464b01d38bee68ed7da6083bf6dbaad71941.tar.gz

# short summary of what the package provides
SUMMARY = COSMIC settings configuration - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "cosmic-settings-config"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-cosmic-settings-config:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# This crate is not published on crates.io; its source is a tarball built
# from the upstream cosmic-settings-daemon git tree at the revision pinned
# by cosmic-applets' Cargo.lock.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O cosmic-settings-config-1.10.0.tar.gz
	@rm -rf $(SOURCE_DIR)/.crate_extract && mkdir -p $(SOURCE_DIR)/.crate_extract
	@tar -xzf $(CACHE_DIR)/cosmic-settings-config-1.10.0.tar.gz -C $(SOURCE_DIR)/.crate_extract
	@cp -a $(SOURCE_DIR)/.crate_extract/*/config/. $(SOURCE_DIR)/
	@rm -rf $(SOURCE_DIR)/.crate_extract
	@$(SOURCE_TAR_CMD)
