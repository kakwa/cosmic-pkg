# Name of the package
NAME = rust-wgpu-core-deps-windows-linux-android-28

# Version
VERSION = 28.0.0

# Revision number 
RELEASE = 1

# URL of the project 
URL = https://crates.io/crates/wgpu-core-deps-windows-linux-android

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/wgpu-core-deps-windows-linux-android/wgpu-core-deps-windows-linux-android-28.0.0.crate

# short summary of what the package provides
SUMMARY = Feature unification helper crate for the Windows/Linux/Android platforms

# Long version of the summary, but I'm lazy
DESCRIPTION = Source code for Debianized Rust crate "wgpu-core-deps-windows-linux-android"

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
	@$(SOURCE_TAR_CMD)
