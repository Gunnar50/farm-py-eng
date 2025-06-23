#!/bin/bash
#
# Generate key mappings from config files

# Set failure conditions
set -o errexit  # Fail on any error
set -o pipefail # Trace ERR through pipes
set -o errtrace # Trace ERR through sub-shell commands

echo "Generating key mappings..."
rm -rf src/shared/key_mappings.py

python scripts/generate_mappings.py