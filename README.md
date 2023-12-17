# dict2mdx
This is a bash script to automatically convert Lingvo DSL, Babylon BGL, Stardict, ZIM, Slob, Tabfile txt, etc dictionaries to MDict MDX (see input formats supported by https://github.com/ilius/pyglossary).
N.B: this script can also pack the resources folder which is located beside the dictionary file into mdd automatically.

REQUIRMENTS: 

1- Pyglossary (which originally come without octopus_mdict_source.py plugin if you install it using `pip`, because of the developer decided to stop developing this plugin)
https://github.com/ilius/pyglossary

N.B: You can download my modified ready version of pyglossary with "octopus_mdict_source.py" plugin added and setup.py fixed; from the google drive link and install it

2- "octopus_mdict_source.py" plugin to be added to /pyglossary/plugins of Pyglossary:
https://gist.github.com/ilius/88d11fa37a4a40cd0d7f6535120b0693

3- python 3.9 and up.

4- `pip3 install mdict-utils lxml polib PyYAML beautifulsoup4 marisa-trie html5lib PyICU libzim>=1.0 python-lzo prompt_toolkit python-idzip`



USAGE:

Navigate to the directory that contains this bash file and copy the dictionary file to the same directory, and run this command:
`bash dict2mdx.sh dictname.anyextension` (ex. dict.txt)

If requirements are met and all dependencies are ready, your conversion will run smoothly and your .mdx dictionary will be ready, to be used by Multi-dictionaries viewers which support .mdx files (ex. Bluedict, Mdict, Golden Dict desktop, etc).

Thanks to 4pda guy who made the primary version of this automatic bash script who inspired me to update this script and make it more useful.

Thanks to the developers of Pyglossary and mdict-utils.

Download this modified ready version of Pyglossary, with octopus_mdict_source.py added and setup.py fixed, so after decompression of this zip file, you can do: `python setup.py install` from imside the decompressed folder to install this modified version of pyglossay and it will work perfectly: https://drive.google.com/open?id=1foGOqZGtbVgG65zlEk2hXMPXKSQyNuIX
