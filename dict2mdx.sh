#!/bin/bash

# Convert Lingvo DSL, Babylon BGL, Stardict, ZIM, etc dictionaries to MDict MDX (see input formats supported by https://github.com/ilius/pyglossary)
# 
# Dependencies:
# python3, sqlite3, pyglossary, mdict-utils
# optional dependency: dictzip (for unpacking .dz files)
# 
# Install all dependencies with:
# pip3 install mdict-utils lxml polib PyYAML beautifulsoup4 marisa-trie html5lib PyICU libzim>=1.0 python-lzo prompt_toolkit

if command -v python3; then
    echo 'ok!'
else
    echo "ERROR: python not installed! Download and install from https://www.python.org/downloads"
    exit 1
fi

if command -v pyglossary; then
    echo 'ok!'
else
    echo "ERROR: pyglossary not installed! Run 'pip3 install pyglossary'"
    exit 1
fi

if command -v mdict; then
    echo 'ok!'
else
    echo "ERROR: mdict not found! Run 'pip3 install mdict-utils'!"
    exit 1
fi

if command -v sqlite3; then
    echo 'ok!'
else
    echo "ERROR: sqlite3 not found! Use the OS package manager to install!"
    exit 1
fi

if [[ "x" == "x$1" ]]; then
    printf "\n\nUSAGE: `basename $0` dictionary.dsl\n"
    exit 1
fi

src="$1"

printf ${src%.*} > description.html
printf ${src%.*} > title.html

if [[ "$src" =~ .*\.dz ]]; then
    echo 'Unpacking .dz file...'
    idzip -d "$1"
    src="${1%.*}"
fi

if [ -f "${src%.*}.mtxt" ]; then
    mdict --title title.html --description description.html -a "${src%.*}.mtxt" "${src%.*}.mdx"
else

db_file="${src%.*}.cache"

if [ -e "$db_file" ]; then
    read -p "$db_file already exists! OVERWRITE? (y/n) " answer
    if [[ $answer =~ ^[Yy]$ ]]; then
        rm -v "$db_file"
    else
        exit 1
    fi
fi

pyglossary "$src" "$db_file" --write-format=OctopusMdictSource

mdict --title title.html --description description.html -a "$db_file" "${src%.*}.mdx"

if [ -d "${src%.*}.cache_res" ]; then
    mdict -a "${src%.*}.cache_res" "${src%.*}.mdd"
fi

if [ -d "${src%.*}.mtxt_res" ]; then
    mdict -a "${src%.*}.mtxt_res" "${src%.*}.mdd"
fi

if [ -d "${src%.*}.txt_res" ]; then
    mdict -a "${src%.*}.txt_res" "${src%.*}.mdd"
fi

echo 'All done!'

fi