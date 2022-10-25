#!/usr/bin/env bash

set -euo pipefail

export NXF_PLUGINS_DEV="${PWD}/plugins"

 ../nextflow/launch.sh "${@}"
