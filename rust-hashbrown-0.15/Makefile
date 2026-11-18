# Name of the package
NAME = rust-hashbrown-0.15

# Version
VERSION = 0.15.5

# Revision number 
RELEASE = 1

# URL of the project 
URL = https://crates.io/crates/hashbrown

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/hashbrown/hashbrown-0.15.5.crate

# short summary of what the package provides
SUMMARY = Rust port of Google SwissTable hash map

# Long version of the summary, but I'm lazy
DESCRIPTION = Source code for Debianized Rust crate "hashbrown"

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
