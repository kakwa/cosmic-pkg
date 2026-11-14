# Name of the package
NAME = cosmic-initial-setup

# Version
VERSION = 1.11.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/cosmic-initial-setup

# URL of the upstream source archive
URL_SRC = $(URL)/archive/refs/tags/epoch-$(VERSION).tar.gz

# short summary of what the package provides
SUMMARY = COSMIC initial setup

# Long version of the summary
DESCRIPTION = Initial setup application for the COSMIC desktop environment.

# License of the upstream project
LICENSE = GPL-3.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:cosmic-initial-setup:*:*:*:*:*

# Distribution versions to skip
#SKIP=<=:deb:8 <=:el:6 <=:fc:29 <=:ubu:18.4

###############################################################################
# Rule #
########

# Including common rules and targets
include buildenv/Makefile.common

# Recover the upstream sources and remove the upstream Debian packaging.
$(SOURCE_ARCHIVE): $(SOURCE_DIR) $(CACHE) Makefile MANIFEST
	@$(WGS) -u $(URL_SRC) -O $(NAME)-$(VERSION).tar.gz
	@tar -xf $(CACHE_DIR)/$(NAME)-$(VERSION).tar.gz -C $(SOURCE_DIR) --strip-components=1
	@rm -rf -- $(SOURCE_DIR)/debian
	@$(SOURCE_TAR_CMD)
