# Name of the package
NAME = rust-winapi-x86-64-pc-windows-gnu

# Version
VERSION = 0.4.0+ds

# Revision number 
RELEASE = 1

# URL of the project 
URL = https://crates.io/crates/winapi-x86_64-pc-windows-gnu

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/winapi-x86_64-pc-windows-gnu/winapi-x86_64-pc-windows-gnu-0.4.0.crate

# short summary of what the package provides
SUMMARY = Raw FFI bindings for winapi x86-64-pc-windows-gnu - Rust source code

# Long version of the summary, but I'm lazy
DESCRIPTION = Source code for Debianized Rust crate "winapi-x86_64-pc-windows-gnu"

# License of the upstream project
LICENSE = MIT/Apache-2.0

# NIST Vulnerability Database CPE pattern (default: cpe:2.3:*:*:$(NAME):*)
# CPE values can be discovered at: https://kakwa.github.io/cpe-search/
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-winapi-x86-64-pc-windows-gnu:*:*:*:*:*

# Comma separated list of CVEs to ignore
#NVD_IGNORE_CVES=CVE-2023-1234,CVE-2023-5678

# Minimum Version for CVEs (default: $(VERSION))
# Set to 0 for all CVEs
#NVD_MIN_VERSION=0.0.1

# Distribution versions to skip
#
# format: space separated list of rules.
# each rule have the format "<op>:<dist>:<version>", with:
#   <op>:      the operation (must be  '>', '>=', '<', '<=' or '=')
#   <dist>:    the distribution code name (examples: 'deb', 'el', 'fc')
#   <version>: the version number to ignore
#
#SKIP=<=:deb:8 <=:el:6 <=:fc:29 <=:ubu:18.4

###############################################################################
# Rule #
########

# example of source recovery url
#URL_SRC=$(URL)/archive/$(VERSION).tar.gz

# Including common rules and targets 
include buildenv/Makefile.common

# preparation hook for sources
# source archive must be recovered here, optionaly reworked, and
# moved to $(SOURCE_ARCHIVE) (the expected path of the source archive for the
# rest of the build)
#
# $(WGS) should be the prefered way to recover archives
# (add checksum against a manifest file).
# use 'make manifest' to generate/update this manifest file.

# Recover the upstream sources from crates.io.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(notdir $(URL_SRC))
	@tar -xf $(CACHE_DIR)/$(notdir $(URL_SRC)) -C $(SOURCE_DIR) --strip-components=1
	@rm -rf $(SOURCE_DIR)/lib
	@$(SOURCE_TAR_CMD)
