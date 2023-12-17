# dict2mdx
This is a bash script to automatically convert Lingvo DSL, Babylon BGL, Stardict, ZIM, Slob, Tabfile txt, etc dictionaries to MDict MDX (see input formats supported by [Pyglossary](https://github.com/ilius/pyglossary).  
N.B: this script can also pack the resources folder which is located beside the dictionary file to MDD automatically.

<br />
<br />
<br />
##REQUIRMENTS: 

1- [Pyglossary](https://github.com/ilius/pyglossary) which originally come without octopus_mdict_source.py plugin if you install it using `pip install pyglossary`, because of the developer decided to stop developing this plugin.  

SO: You can download my modified ready version of pyglossary 4.6.1 with octopus_mdict_source.py plugin added and setup.py fixed; from this Google Drive [LINK](https://drive.google.com/open?id=1foGOqZGtbVgG65zlEk2hXMPXKSQyNuIX). Decompress the downloaded zip file, and run: `python setup.py install` from inside the decompressed folder to install this modified version of pyglossay and it will work perfectly.

2- JUST IF YOU WILL NOT USE MY MODIFIED VERSION OF PYGLOSSARY FROM THE GOOGLE DRIVE LINK ABOVE; you will need to download "octopus_mdict_source.py" plugin from this [link](https://gist.github.com/ilius/88d11fa37a4a40cd0d7f6535120b0693) and add it to /pyglossary/plugins folder of Pyglossary.

3- python 3.9 and up.

4- `pip3 install mdict-utils lxml polib PyYAML beautifulsoup4 marisa-trie html5lib PyICU libzim>=1.0 python-lzo prompt_toolkit python-idzip`  

<br />
<br />
<br />
##USAGE:

Navigate to the directory that contains this bash file and copy the dictionary file to the same directory, and run this command:
`bash dict2mdx.sh dictname.anyextension` (ex. dict.txt)

### Finally:
If requirements are met and all dependencies are ready, your conversion will run smoothly and your .mdx dictionary will be ready, to be used by Multi-dictionaries viewers which support .mdx files (ex. Bluedict, Mdict, Golden Dict desktop, etc).  

Thanks to 4pda.to guy who made the primary version of this automatic bash script who inspired me to update this script and make it more useful.  

Thanks to the owners of Pyglossary and mdict-utils.
