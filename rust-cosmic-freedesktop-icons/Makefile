# Name of the package
NAME = rust-cosmic-freedesktop-icons

# Version
VERSION = 0.4.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/freedesktop-icons

# URL of the upstream source archive
URL_SRC = https://github.com/pop-os/freedesktop-icons/archive/ab4c57b8e416c6af9297cb04d101889896fd9a92.tar.gz

# short summary of what the package provides
SUMMARY = freedesktop icon lookup - Rust source code

# Long version of the summary
DESCRIPTION = Source code for Debianized Rust crate "cosmic-freedesktop-icons"

# License of the upstream project
LICENSE = MIT OR Apache-2.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-cosmic-freedesktop-icons:*:*:*:*:*

###############################################################################
# Rule #
###############################################################################

include buildenv/Makefile.common

# This crate is not published on crates.io; its source is a tarball built
# from the upstream git tree at the revision pinned by cosmic-applets'
# Cargo.lock. Recover it from the local staging area.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O cosmic-freedesktop-icons-0.4.0.tar.gz
	@tar -xzf $(CACHE_DIR)/cosmic-freedesktop-icons-0.4.0.tar.gz -C $(SOURCE_DIR) --strip-components=1
	@$(SOURCE_TAR_CMD)
