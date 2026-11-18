# Name of the package
NAME = rust-rustix-0.38

# Version
VERSION = 0.38.44

# Revision number 
RELEASE = 1

# URL of the project 
URL = https://crates.io/crates/rustix

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/rustix/rustix-0.38.44.crate

# short summary of what the package provides
SUMMARY = Safe Rust bindings to Linux and Unix system APIs

# Long version of the summary, but I'm lazy
DESCRIPTION = Source code for Debianized Rust crate "rustix"

# License of the upstream project
LICENSE = Apache-2.0 WITH LLVM-exception or Apache-2.0 or MIT

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
