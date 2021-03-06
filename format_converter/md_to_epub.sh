#!/bin/bash

set -eu

if [ -z "$1" ]
then
    echo "Usage: bash $0 md_file_path"
    exit 1
fi

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)

~/pandoc/pandoc-2.16.1/bin/pandoc $1 -o $1.epub --metadata-file=${script_dir}/epub_metadata.yaml