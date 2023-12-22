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
import re
import readline

history_file = ".script_history.txt"

# Check if history_file exists
if not os.path.isfile(history_file):
    print(f"{history_file} not found. Ignoring on first run.")

# Load previous command history
try:
    readline.read_history_file(history_file)
except FileNotFoundError:
    pass

def check_command(command):
    try:
        subprocess.check_output([command, '--version'], stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError:
        return False
    else:
        return True

if check_command('python3'):
    if check_command('pyglossary'):
        if check_command('mdict'):
            print("\n If you want to convert any dict to MDX, then convert it to .mtxt first, and the script will ask you the next step!\n\n")
        else:
            print("ERROR: mdict not found! Run 'pip3 install mdict-utils'!")
            exit(1)
    else:
        print("ERROR: pyglossary not installed! Download my modified version on github readme.md and run this command from inside the main folder 'python setup.py install'")
        exit(1)
else:
    print("ERROR: python not installed! install it according to your system")
    exit(1)

subprocess.run('pyglossary --cmd', shell=True)

print()
print()

answer = input("Convert .mtxt to MDX? (y) or press any other key to exit? ")
if answer.lower() == 'y':
    src = input("Enter dict name again: ")

    with open('description.html', 'w') as f:
        f.write(src.rsplit('.', 1)[0])

    with open('title.html', 'w') as f:
        f.write(src.rsplit('.', 1)[0])

    if os.path.isfile(f"{os.path.splitext(src)[0]}.mtxt"):
        subprocess.run(f'mdict --title title.html --description description.html -a {src.rsplit(".",1)[0]}.mtxt {src.rsplit(".",1)[0]}.mdx')
    else:
        print(f"{src.rsplit('.', 1)[0]}.mtxt not found")
        sys.exit(1)
        
    if os.path.isdir(f"{os.path.splitext(src)[0]}.mtxt_res"):
        subprocess.run(['mdict', '-a', f"{os.path.splitext(src)[0]}.mtxt_res", f"{os.path.splitext(src)[0]}.mdd"])
        print('All done!')
        sys.exit(1)
    

else:
    print('Conversion done, Did not converted to MDX')
    sys.exit(1)

# Save command history
readline.write_history_file(history_file)