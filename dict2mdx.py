#!/usr/bin/env python3

# Convert Lingvo DSL, Babylon BGL, Stardict, ZIM, etc dictionaries to MDict MDX (see input formats supported by https://github.com/ilius/pyglossary)
# 
# Dependencies:
# python3, pyglossary, mdict-utils, which
# 
# Install all dependencies with:
# pip3 install mdict-utils lxml polib PyYAML beautifulsoup4 marisa-trie html5lib PyICU libzim>=1.0 python-lzo prompt_toolkit python-idzip
# pyglossary better to be installed from a local folder with: python setup.py install (better to use my ready pyglossary zip file)

import os
import sys
import subprocess

def command_exists(command):
    # Check if a command exists in the system
    return subprocess.call(['which', command], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

if command_exists('python3'):
    print('Python3 is ready!')
else:
    print("ERROR: python not installed! Download and install from https://www.python.org/downloads")
    sys.exit(1)

if command_exists('pyglossary'):
    print('Pyglossary is ready!')
else:
    print("ERROR: pyglossary not installed! Run 'pip3 install pyglossary'")
    sys.exit(1)

if command_exists('mdict'):
    print('Mdict-utils is ready!')
else:
    print("ERROR: mdict not found! Run 'pip3 install mdict-utils'!")
    sys.exit(1)

src = input("Input file (ex. dictionary.dsl): ")

with open('description.html', 'w') as f:
    f.write(os.path.splitext(src)[0])

with open('title.html', 'w') as f:
    f.write(os.path.splitext(src)[0])

if src.endswith('.dz'):
    print('Unpacking .dz file...')
    subprocess.run(['idzip', '-d', src])
    src = os.path.splitext(src)[0]

if os.path.isfile(f"{os.path.splitext(src)[0]}.mtxt"):
    answer = input(f"{os.path.splitext(src)[0]}.mtxt already exists! Do you want to convert it directly to MDX? (y/n) ")
    if answer.lower() == 'y':
        # Use Word Title option
        subprocess.run(['mdict', '--title', 'title.html', '--description', 'description.html', '-a', f"{os.path.splitext(src)[0]}.mtxt", f"{os.path.splitext(src)[0]}.mdx"])
        if os.path.isdir(f"{os.path.splitext(src)[0]}.cache_res"):
            subprocess.run(['mdict', '-a', f"{os.path.splitext(src)[0]}.cache_res", f"{os.path.splitext(src)[0]}.mdd"])
        
        if os.path.isdir(f"{os.path.splitext(src)[0]}.mtxt_res"):
            subprocess.run(['mdict', '-a', f"{os.path.splitext(src)[0]}.mtxt_res", f"{os.path.splitext(src)[0]}.mdd"])
        
        if os.path.isdir(f"{os.path.splitext(src)[0]}.txt_res"):
            subprocess.run(['mdict', '-a', f"{os.path.splitext(src)[0]}.txt_res", f"{os.path.splitext(src)[0]}.mdd"])
        print('All done!')
        sys.exit(1)
    elif answer.lower() == 'n':
        # Do not use Word Title option
        pass
    else:
        # Invalid choice
        print("Invalid option. Please enter y or n.")
        sys.exit(1)

db_file = f"{os.path.splitext(src)[0]}.cache"

if os.path.exists(db_file):
    answer = input(f"{db_file} already exists! OVERWRITE? (y/n) ")
    if answer.lower() == 'y':
        os.remove(db_file)
    else:
        sys.exit(1)

choice1 = input("Do you want to use Word Title option? (y/n): ")
if choice1.lower() == 'y':
    # Use Word Title option
    subprocess.run(['pyglossary', src, db_file, '--write-format=OctopusMdictSource', '--json-write-options', '{"word_title": true}'])
    print('All done!')
elif choice1.lower() == 'n':
    # Do not use Word Title option
    subprocess.run(['pyglossary', src, db_file, '--write-format=OctopusMdictSource'])
    print('All done!')
else:
    # Invalid choice
    print("Invalid option. Please enter y or n.")
    sys.exit(1)

subprocess.run(['mdict', '--title', 'title.html', '--description', 'description.html', '-a', db_file, f"{os.path.splitext(src)[0]}.mdx"])

if os.path.isdir(f"{os.path.splitext(src)[0]}.cache_res"):
    subprocess.run(['mdict', '-a', f"{os.path.splitext(src)[0]}.cache_res", f"{os.path.splitext(src)[0]}.mdd"])

if os.path.isdir(f"{os.path.splitext(src)[0]}.mtxt_res"):
    subprocess.run(['mdict', '-a', f"{os.path.splitext(src)[0]}.mtxt_res", f"{os.path.splitext(src)[0]}.mdd"])

if os.path.isdir(f"{os.path.splitext(src)[0]}.txt_res"):
    subprocess.run(['mdict', '-a', f"{os.path.splitext(src)[0]}.txt_res", f"{os.path.splitext(src)[0]}.mdd"])

print('All done!')