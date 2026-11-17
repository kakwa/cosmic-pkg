# Name of the package
NAME = rust-build-helpers

# Version
VERSION = 0.14.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/iced

# URL of the upstream source archive
URL_SRC = https://github.com/pop-os/iced/archive/e03ca50ed8838d3ec8392e32a68ce59634517945.tar.gz

# short summary of what the package provides
SUMMARY = iced build helpers - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "build_helpers"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-build-helpers:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# build_helpers is not published on crates.io. It lives in the pop-os/iced
# repository (the iced git submodule of the libcosmic tree) and uses
# workspace inheritance for its manifest fields, so its Cargo.toml is
# rewritten to a standalone manifest below.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O build-helpers-0.14.0.tar.gz
	@rm -rf $(SOURCE_DIR)/.crate_extract && mkdir -p $(SOURCE_DIR)/.crate_extract
	@tar -xzf $(CACHE_DIR)/build-helpers-0.14.0.tar.gz -C $(SOURCE_DIR)/.crate_extract
	@cp -a $(SOURCE_DIR)/.crate_extract/*/build_helpers/. $(SOURCE_DIR)/
	@rm -rf $(SOURCE_DIR)/.crate_extract
	@cat > $(SOURCE_DIR)/Cargo.toml <<'EOF'
[package]
name = "build_helpers"
version = "0.14.0"
edition = "2024"
license = "MIT"
description = "Helper macros and functions for iced's build system"
homepage = "https://github.com/pop-os/iced"
repository = "https://github.com/pop-os/iced"
rust-version = "1.92"

[dependencies]
cfg_aliases = { version = "0.2.1" }
EOF
	@$(SOURCE_TAR_CMD)
