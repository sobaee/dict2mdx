#!/bin/bash

# Convert Lingvo DSL, Babylon BGL, Stardict, ZIM, etc dictionaries to MDict MDX (see input formats supported by https://github.com/ilius/pyglossary)
# 
# Dependencies:
# python3, pyglossary, mdict-utils, which
# 
# Install all dependencies with:
# pip3 install mdict-utils lxml polib PyYAML beautifulsoup4 marisa-trie html5lib PyICU libzim>=1.0 python-lzo prompt_toolkit python-idzip
# pyglossary better to be installed from a local folder with: python setup.py install (better to use my ready pyglossary zip file)

if command -v python3 >/dev/null 2>&1; then
    if command -v pyglossary >/dev/null 2>&1; then
        if command -v mdict >/dev/null 2>&1; then
            echo -e "All dependencies are ready!\n"
        else
            echo "ERROR: mdict not found! Run 'pip3 install mdict-utils'!"
            exit 1
        fi
    else
        echo "ERROR: pyglossary not installed! Run 'pip3 install pyglossary'"
        exit 1
    fi
else
    echo "ERROR: python not installed! Download and install from https://www.python.org/downloads"
    exit 1
fi




src=""
read -p "Input file (ex. dictionary.dsl): " src

printf ${src%.*} > description.html
printf ${src%.*} > title.html

if [[ "$src" =~ .*\.dz ]]; then
    echo 'Unpacking .dz file...'
    idzip -d "$1"
    src="${1%.*}"
fi

if [ -f "${src%.*}.mtxt" ]; then
read -p "${src%.*}.mtxt already exists! Do you want to convert it directly to MDX? (y/n) " answer
    case $answer in
    y|Y) # Use Word Title option
        mdict --title title.html --description description.html -a "${src%.*}.mtxt" "${src%.*}.mdx"
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
        exit 1
        ;;
    n|N) # Do not use Word Title option
        
       
        ;;
    *) # Invalid choice
        echo "Invalid option. Please enter y or n."
        ;;
esac
        fi

        
       
db_file="${src%.*}.cache"

if [ -e "$db_file" ]; then
    read -p "$db_file already exists! OVERWRITE? (y/n) " answer
    if [[ $answer =~ ^[Yy]$ ]]; then
        rm -v "$db_file"
    else
        exit 1
    fi
fi

read -p "Do you want to use Word Title option? (y/n): " choice1
    case $choice1 in
    y|Y) # Use Word Title option
        pyglossary "$src" "$db_file" --write-format=OctopusMdictSource --json-write-options '{"word_title": true}'

        echo 'All done!'
        ;;
    n|N) # Do not use Word Title option
        
        pyglossary "$src" "$db_file" --write-format=OctopusMdictSource
        echo 'All done!'
        ;;
    *) # Invalid choice
        echo "Invalid option. Please enter y or n."
        ;;
esac

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
