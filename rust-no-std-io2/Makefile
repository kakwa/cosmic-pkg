# Name of the package
NAME = rust-no-std-io2

# Version
VERSION = 0.9.4

# Revision number 
RELEASE = 1

# URL of the project 
URL = https://crates.io/crates/no_std_io2

# URL of the upstream source archive
URL_SRC = https://static.crates.io/crates/no_std_io2/no_std_io2-0.9.4.crate

# short summary of what the package provides
SUMMARY = Bare essentials of std::io for use in no_std - Rust source code

# Long version of the summary, but I'm lazy
DESCRIPTION = Alloc support is optional. . Source code for Debianized Rust crate "no_std_io2"

# License of the upstream project
LICENSE = Apache-2.0 OR MIT

# NIST Vulnerability Database CPE pattern (default: cpe:2.3:*:*:$(NAME):*)
# CPE values can be discovered at: https://kakwa.github.io/cpe-search/
#NVD_CPE_PATTERN=cpe:2.3:*:*:rust-no-std-io2:*:*:*:*:*

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
	@$(SOURCE_TAR_CMD)

# Example of simple recovery, with good upstream
#$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
#	$(WGS) -u $(URL_SRC) -o $(SOURCE_ARCHIVE)

# more complex case with upstream source rework and rebuilding of the tar
#$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
#	$(WGS) -u $(URL_SRC) -o $(BUILD_DIR)/$(NAME)-$(VERSION).tar.gz
#	mkdir -p $(BUILD_DIR)/tmp
#	tar -vxf $(BUILD_DIR)/$(NAME)-$(VERSION).tar.gz -C $(BUILD_DIR)/tmp
#	rm -rf $(BUILD_DIR)/tmp/$(NAME)-$(VERSION)/debian
#	mv $(BUILD_DIR)/tmp/$(NAME)-$(VERSION)/* $(SOURCE_DIR)
#	rm -rf $(BUILD_DIR)/tmp
#	rm -f $(BUILD_DIR)/$(NAME)-$(VERSION).tar.gz
#	$(SOURCE_TAR_CMD)
