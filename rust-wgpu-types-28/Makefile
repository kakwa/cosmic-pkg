# Name of the package
NAME = rust-wgpu-types-28

# Version
VERSION = 28.0.0

# Revision number 
RELEASE = 1

# URL of the project 
URL = https://crates.io/crates/wgpu-types

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/wgpu-types/wgpu-types-28.0.0.crate

# short summary of what the package provides
SUMMARY = Common types and utilities for wgpu, the cross-platform, safe, pure-rust graphics API

# Long version of the summary, but I'm lazy
DESCRIPTION = Source code for Debianized Rust crate "wgpu-types"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

###############################################################################
# Rule #
########

# Including common rules and targets 
include buildenv/Makefile.common

# Recover the upstream sources from crates.io.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(notdir $(URL_SRC))
	@tar -xf $(CACHE_DIR)/$(notdir $(URL_SRC)) -C $(SOURCE_DIR) --strip-components=1
	@python3 patch-cargo-toml.py $(SOURCE_DIR)/Cargo.toml
	@$(SOURCE_TAR_CMD)
