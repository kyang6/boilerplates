# -*- coding: utf-8 -*-
"""[application description here]"""

import codecs

with codecs.open("SomeFile", "rb", "utf-8") as inFile: 
    text = inFile.read()
    text_lines = inFile.readlines()
# Do something with 'text' here
with codecs.open("DifferentFile", "wb", "utf-8") as outFile:
    outFile.write(text)