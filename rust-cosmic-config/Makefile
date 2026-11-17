# Name of the package
NAME = rust-cosmic-config

# Version
VERSION = 1.0.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/libcosmic

# URL of the upstream source archive
URL_SRC = https://github.com/pop-os/libcosmic/archive/430f3d48a97d8779f9c1985473912e594ccca1ae.tar.gz

# short summary of what the package provides
SUMMARY = COSMIC configuration system - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crates "cosmic-config" and "cosmic-config-derive"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-cosmic-config:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# These crates are not published on crates.io; their source is a tarball
# built from the upstream libcosmic git tree at the revision pinned by
# cosmic-applets' Cargo.lock. The cosmic-config-derive proc-macro crate is
# a path dependency of cosmic-config, so it is packaged alongside it.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O cosmic-config-1.0.0.tar.gz
	@rm -rf $(SOURCE_DIR)/.crate_extract && mkdir -p $(SOURCE_DIR)/.crate_extract
	@tar -xzf $(CACHE_DIR)/cosmic-config-1.0.0.tar.gz -C $(SOURCE_DIR)/.crate_extract
	@cp -a $(SOURCE_DIR)/.crate_extract/*/cosmic-config/. $(SOURCE_DIR)/
	@cp -a $(SOURCE_DIR)/.crate_extract/*/cosmic-config-derive $(SOURCE_DIR)/
	@rm -rf $(SOURCE_DIR)/.crate_extract
	@$(SOURCE_TAR_CMD)
