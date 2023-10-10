#!/bin/bash
set -e

cd "$(dirname "$(readlink -f "$BASH_SOURCE")")/.."

{
	cat <<-'EOH'
	# This file lists all individuals that contributed content to the repo.
	# For how it is generated, see `hack/generate-authors.sh`.
	EOH
	echo
	git log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > AUTHORS
