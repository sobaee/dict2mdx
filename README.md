# dict2mdx
This is a python script to automatically convert Lingvo DSL, Babylon BGL, Stardict, ZIM, Slob, Tabfile txt, etc dictionaries to MDict MDX (see input formats supported by [Pyglossary](https://github.com/ilius/pyglossary)).  

N.B: this script can also pack the resources folder which is located beside the dictionary file to MDD automatically.

This script has developed because Pyglossary developer decided not to support conversion to .mtxt or .mdx; if the developer decided to support conversion to .mdx, this tool would not be developed, and I hope he does that.

<br />
<br />

### REQUIRMENTS: 

1- Python 3.9 and up.

2- [Pyglossary](https://github.com/ilius/pyglossary) which originally come without octopus_mdict_source.py plugin if you install it using `pip install pyglossary`, because of the developer decided to stop developing this plugin.  
SO: DOWNLOAD my modified ready version of pyglossary 5.0.0 with octopus_mdict_source.py plugin added to /pyglossary/plugins folder, and ui_cmd_interactive.py file modified a bit; from my fork [LINK](https://codeload.github.com/sobaee/pyglossaryfork/zip/refs/tags/5.0.0). Decompress the downloaded zip file, and run: `python setup.py install` from inside the decompressed folder to install this modified version of pyglossay and it will work perfectly.

N.B: As a reference; you can download "octopus_mdict_source.py" plugin from this [link](https://gist.github.com/ilius/88d11fa37a4a40cd0d7f6535120b0693).

3- The most important dependencies:  
`pip3 install prompt_toolkit mdict-utils beautifulsoup4 python-lzo python-idzip`

4- Other important dependencies:  
`pip3 install lxml polib PyYAML beautifulsoup4 marisa-trie html5lib PyICU libzim` 

<br />
<br />


### USAGE:

Navigate to the directory that contains this python script and copy the dictionary file to the same directory, and run this command:
`python dict2mdx.py`
<br />
<br />

### Finally:
If requirements are met and all dependencies are ready, your conversion will run smoothly and your .mdx dictionary will be ready, to be used by Multi-dictionaries viewers which support .mdx files (ex. DictTango, Bluedict, Mdict, GoldenDict PC, etc).  

Thanks to "4pda.to" guy "cсpizz" who made the primary version of this automatic script who inspired me to update the script, make a similar python script and make it more useful. [LINK to the original script](https://gist.github.com/glowinthedark/e393730e8477bb64f86fc99ec21d6303).

Thanks to the owners of Pyglossary and mdict-utils.
