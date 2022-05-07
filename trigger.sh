#!/usr/bin/env sh

set -x

cd "$(dirname "$0")"

make pull
make run
