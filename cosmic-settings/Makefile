# Name of the package
NAME = cosmic-settings

# Version
VERSION = 1.11.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/cosmic-settings

# short summary of what the package provides
SUMMARY = Settings application for the COSMIC desktop environment

# Long version of the summary
DESCRIPTION = Settings application for the COSMIC desktop environment

# License of the upstream project
LICENSE = GPL-3.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:cosmic-settings:*:*:*:*:*

# Distribution versions to skip
#SKIP=<=:deb:8 <=:el:6 <=:fc:29 <=:ubu:18.4

###############################################################################
# Rule #
########

# Including common rules and targets
include buildenv/Makefile.common

# Recover the upstream sources, remove the upstream Debian packaging and
# vendor the Rust dependencies so the build itself can run offline.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(GS) -u $(URL) -t epoch-$(VERSION) -O $(NAME)-$(VERSION).tar.gz
	@tar -xf $(CACHE_DIR)/$(NAME)-$(VERSION).tar.gz -C $(SOURCE_DIR) --strip-components=1
	@rm -rf -- $(SOURCE_DIR)/debian
	@cd $(SOURCE_DIR) && just vendor
	@$(SOURCE_TAR_CMD)
