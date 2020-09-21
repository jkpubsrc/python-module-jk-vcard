#!/usr/bin/python3




import os
import re

import jk_typing
from jk_utils.tokenizer2 import TokenizationError
from jk_version import Version
from jk_vcard import *







allKeys = set()

with open("contacts.vcf", "r") as f:
	for vCard in VCFParser.parseText(f.read()):
		for key in vCard.itemKeys:
			allKeys.add(key)

print(allKeys)





