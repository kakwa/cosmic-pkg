# Name of the package
NAME = rust-libcosmic

# Version
VERSION = 1.0.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/libcosmic

# URL of the upstream source archive
URL_SRC = file:///tmp/gitc/libcosmic-1.0.0.tar.gz

# short summary of what the package provides
SUMMARY = The COSMIC desktop environment toolkit - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "libcosmic"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-libcosmic:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# This crate is not published on crates.io; its source is a tarball built
# from the upstream git tree at the revision pinned by cosmic-applets'
# Cargo.lock. Recover it from the local staging area.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(notdir $(URL_SRC))
	@tar -xzf $(CACHE_DIR)/$(notdir $(URL_SRC)) -C $(SOURCE_DIR) --strip-components=0
	@$(SOURCE_TAR_CMD)
