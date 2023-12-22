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
            echo -e "\n If you want to convert any dict to MDX, then convert it to .mtxt first, and the script will ask you the next step!\n\n"
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

python main.py --cmd

echo
echo
read -p "Convert .mtxt to MDX? (y) or press any other key to exit? " answer
    case $answer in
    y|Y) 
    src=""
    read -p "Enter dict name again: " src

    printf ${src%.*} > description.html
    printf ${src%.*} > title.html
    if [ -e "${src%.*}.mtxt" ]; then
       mdict --title title.html --description description.html -a "${src%.*}.mtxt" "${src%.*}.mdx"

        if [ -d "${src%.*}.mtxt_res" ]; then
        mdict -a "${src%.*}.mtxt_res" "${src%.*}.mdd"
        fi

        
        echo 'All done!'
        exit 1
    else
        echo "${src%.*}.mtxt doesn't found"
        exit 1
    fi

        ;;
    n|N) 
        echo 'Conversion done, Did not converted to MDX'
        exit 1
       
        ;;
    *) # Invalid choice
        echo 'Conversion done, Did not converted to MDX'
        ;;
esac
