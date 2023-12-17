# dict2mdx
This is a bash script to automatically convert Lingvo DSL, Babylon BGL, Stardict, ZIM, Slob, Tabfile txt, etc dictionaries to MDict MDX (see input formats supported by https://github.com/ilius/pyglossary)

REQUIRMENTS: 

1- Pyglossary (which originally come without octopus_mdict_source.py plugin)
https://github.com/ilius/pyglossary.

2- "octopus_mdict_source.py" plugin to be added to /pyglossary/plugins of Pyglossary
https://gist.github.com/ilius/88d11fa37a4a40cd0d7f6535120b0693

3- python 3.9 and up.

4- pip3 install mdict-utils lxml polib PyYAML beautifulsoup4 marisa-trie html5lib PyICU libzim>=1.0 python-lzo prompt_toolkit idzip



USAGE:

Navigate to the directory that contains the dictionary file and this bash file and run this command:
Bash dict2mdx.sh dictname.anyextension (ex. dict.txt)
