#!/bin/bash
#
# Check imports

# Set failure conditions
set -o errexit  # Fail on any error
set -o pipefail # Trace ERR through pipes
set -o errtrace # Trace ERR through sub-shell commands

isort . --skip .pytype $@
