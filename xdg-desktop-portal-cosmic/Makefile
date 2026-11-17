# Name of the package
NAME = xdg-desktop-portal-cosmic

# Version
VERSION = 1.11.0

# Revision number
RELEASE = 1

# URL of the project
URL = https://github.com/pop-os/xdg-desktop-portal-cosmic

# URL of the upstream source archive
URL_SRC = $(URL)/archive/refs/tags/epoch-$(VERSION).tar.gz

# short summary of what the package provides
SUMMARY = COSMIC backend for xdg-desktop-portal

# Long version of the summary
DESCRIPTION = XDG desktop portal backend for the COSMIC desktop environment.

# License of the upstream project
LICENSE = GPL-3.0

# NIST Vulnerability Database CPE pattern
#NVD_CPE_PATTERN=cpe:2.3:*:*:xdg-desktop-portal-cosmic:*:*:*:*:*

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
	@sed -i \
	-e 's|default = \["systemd"\]|default = ["systemd", "wgpu"]|' \
	-e 's|cosmic-files = { git = .*|cosmic-files = { version = "1.11.0", default-features = false, features = ["gvfs", "wayland"] }|' \
	-e 's|cosmic-protocols = { git = .*|cosmic-protocols = "0.2.0"|' \
	-e 's|cosmic-client-toolkit = { git = .*|cosmic-client-toolkit = "0.2.0"|' \
	-e 's|cosmic-bg-config = { git = .*|cosmic-bg-config = "1.10.0"|' \
	-e 's|pipewire = { git = .*|pipewire = { version = "0.10.1", features = ["v0_3_33"] }|' \
	-e 's|spa_sys = { package = "libspa-sys", git = .*|spa_sys = { package = "libspa-sys", version = "0.10.1" }|' \
	-e 's|pipewire-sys = { git = .*|pipewire-sys = "0.10.1"|' \
	-e 's|git = "https://github.com/pop-os/libcosmic"|version = "1.0.0"|' \
	-e 's|cosmic-config = { git = .*|cosmic-config = "1.0.0"|' \
    $(SOURCE_DIR)/Cargo.toml
	@sed -i 's|cargo build {{ profile-args }} {{ vendor-args }} --bin {{ name }}|cargo build {{ profile-args }} --offline --bin {{ name }}|' $(SOURCE_DIR)/justfile
	@python3 fixup.py $(SOURCE_DIR)
	@$(SOURCE_TAR_CMD)
