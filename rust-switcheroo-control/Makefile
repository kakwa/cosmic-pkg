# Name of the package
NAME = rust-switcheroo-control

# Version
VERSION = 0.1.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/dbus-settings-bindings

# URL of the upstream source archive
URL_SRC = https://github.com/pop-os/dbus-settings-bindings/archive/eed01dd3609e90e3c8cd043656734c500956c793.tar.gz

# short summary of what the package provides
SUMMARY = Switcheroo control dbus bindings - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "switcheroo-control"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-switcheroo-control:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# This crate is not published on crates.io; its source is a tarball built
# from the upstream git tree at the revision pinned by cosmic-applets'
# Cargo.lock. Recover it from the local staging area.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O switcheroo-control-0.1.0.tar.gz
	@rm -rf $(SOURCE_DIR)/.crate_extract && mkdir -p $(SOURCE_DIR)/.crate_extract
	@tar -xzf $(CACHE_DIR)/switcheroo-control-0.1.0.tar.gz -C $(SOURCE_DIR)/.crate_extract
	@cp -a $(SOURCE_DIR)/.crate_extract/*/switcheroo-control/. $(SOURCE_DIR)/
	@rm -rf $(SOURCE_DIR)/.crate_extract
	@$(SOURCE_TAR_CMD)
