# Name of the package
NAME = rust-petgraph-0.8

# Version
VERSION = 0.8.2

# Revision number 
RELEASE = 1

# URL of the project 
URL = https://crates.io/crates/petgraph

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/petgraph/petgraph-0.8.2.crate

# short summary of what the package provides
SUMMARY = Graph data structure library

# Long version of the summary, but I'm lazy
DESCRIPTION = Source code for Debianized Rust crate "petgraph"

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
