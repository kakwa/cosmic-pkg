import sys, re

d = sys.argv[1]

# Fix cosmic-portal-config/Cargo.toml
p = d + '/cosmic-portal-config/Cargo.toml'
t = open(p).read()
t = t.replace('cosmic-config.workspace = true', 'cosmic-config = "1.0.0"')
t = t.replace('log.workspace = true', 'log = "0.4"')
t = re.sub(
    r'\[dependencies\.serde\]\nfeatures = \["derive"\]\nworkspace = true',
    '[dependencies.serde]\nversion = "1.0"\nfeatures = ["derive"]',
    t
)
open(p, 'w').write(t)

# Remove [workspace] section and [workspace.dependencies] section from main Cargo.toml
# and replace .workspace = true references in [dependencies]
p = d + '/Cargo.toml'
t = open(p).read()
# Remove [workspace]\nmembers = [...]\n
t = re.sub(r'\[workspace\]\nmembers = \[[^\]]*\]\n\n?', '', t)
# Replace workspace references in [dependencies] section
t = t.replace('# Workspace\ncosmic-config.workspace = true\nserde.workspace = true',
              'cosmic-config = "1.0.0"\nserde = "1.0"')
t = t.replace('cosmic-config.workspace = true', 'cosmic-config = "1.0.0"')
t = t.replace('serde.workspace = true', 'serde = "1.0"')
# Remove [workspace.dependencies] section (up to next [section header])
t = re.sub(r'\[workspace\.dependencies\]\n(?:[^\n]*\n)*(?=\[)', '', t)
open(p, 'w').write(t)

print("fixup done")
