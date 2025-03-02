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
            print("All dependings are ready!!\n")
        else:
            print("ERROR: mdict not found! Run 'pip3 install mdict-utils'!")
            exit(1)
    else:
        print("ERROR: pyglossary not installed! Download my modified version on github readme.md and run this command from inside the main folder 'python setup.py install'")
        exit(1)
else:
    print("ERROR: python not installed! install it according to your system")
    exit(1)

answer1 = input("to convert directly from .mtxt to MDX or to pack MDD resources only press (y)!! OR PRESS ANY OTHER KEY TO CONTINUE! ")

if answer1.lower() == 'y':
    src = input("Enter your .mtxt dict full name without spaces: ")

    with open("description.html", "w") as file:
        file.write(src.split('.')[0])

    with open("title.html", "w") as file:
        file.write(src.split('.')[0])

    if os.path.exists(src.split('.')[0] + ".mtxt"):
        cmd = [
            "mdict",
            "--title", "title.html",
            "--description", "description.html",
            "-a", src.split('.')[0] + ".mtxt",
            src.split('.')[0] + ".mdx"
        ]
        subprocess.run(cmd, check=True)

        if os.path.isdir(src.split('.')[0] + ".mtxt_res"):
            cmd = [
                "mdict",
                "-a", src.split('.')[0] + ".mtxt_res",
                src.split('.')[0] + ".mdd"
            ]
            subprocess.run(cmd, check=True)
            print("Sources is also converted to MDD\n")

        print("All done!")
        exit(1)
    else:
        print(f"ERROR: {src.split('.')[0]}.mtxt doesn't found\n")
        if os.path.isdir(src.split('.')[0] + ".mtxt_res"):
            cmd = [
                "mdict",
                "-a", src.split('.')[0] + ".mtxt_res",
                src.split('.')[0] + ".mdd"
            ]
            subprocess.run(cmd, check=True)
            print("Only MDD is packed!!!")
        exit(1)
else:
    print("Your conversion will continue\n")

subprocess.run('pyglossary --cmd', shell=True)

print()
print()
answer = input("Convert .mtxt to MDX? (y) or press any other key to exit? ")

if answer.lower() == "y":
    src = input("Enter your result .mtxt dict full name again, please: ")

    with open("description.html", "w") as file:
        file.write(src.split('.')[0])

    with open("title.html", "w") as file:
        file.write(src.split('.')[0])

    if os.path.exists(src.split('.')[0] + ".mtxt"):
        cmd = [
            "mdict",
            "--title", "title.html",
            "--description", "description.html",
            "-a", src.split('.')[0] + ".mtxt",
            src.split('.')[0] + ".mdx"
        ]
        subprocess.run(cmd, check=True)

        if os.path.isdir(src.split('.')[0] + ".mtxt_res"):
            cmd = [
                "mdict",
                "-a", src.split('.')[0] + ".mtxt_res",
                src.split('.')[0] + ".mdd"
            ]
            subprocess.run(cmd, check=True)
            print("Sources is also converted to MDD\n")

        print("All done!")
        exit(1)
    else:
        print(f"{src.split('.')[0]}.mtxt doesn't found")
        exit(1)
else:
    print("Conversion done, Did not convert to MDX")
    exit(1)

# Save command history
readline.write_history_file(history_file)