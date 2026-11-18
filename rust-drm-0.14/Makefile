# Name of the package
NAME = rust-drm-0.14

# Version
VERSION = 0.14.1

# Revision number 
RELEASE = 1

# URL of the project 
URL = https://crates.io/crates/drm

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/drm/drm-0.14.1.crate

# short summary of what the package provides
SUMMARY = Safe low-level bindings to the Direct Rendering Manager API

# Long version of the summary, but I'm lazy
DESCRIPTION = Source code for Debianized Rust crate "drm"

# License of the upstream project
LICENSE = MIT

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
