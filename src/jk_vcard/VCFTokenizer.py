
import re

from jk_utils.tokenizer2 import TokenizationError

from .VCFToken import VCFToken






class VCFTokenizer(object):

	def __init__(self):
		pass
	#

	@staticmethod
	def tokenize(rawData:str) -> list:
		ret = []

		# split lines, merging multi-lines in the process

		lineNos = []
		contentLines = []
		rawLines = rawData.split("\n")
		lineNo = 0
		for rawLine in rawLines:
			lineNo += 1
			if rawLine:
				if rawLine[0] == " ":
					contentLines[-1] = contentLines[-1] + rawLine[1:]
				else:
					contentLines.append(rawLine)
					lineNos.append(lineNo)
		assert len(contentLines) == len(lineNos)

		# parse each line

		for lineNo, contentLine in zip(lineNos, contentLines):
			parts = contentLine.split(":", 1)
			if len(parts) != 2:
				TokenizationError("No colon found!", lineNo, 1)

			parts0, parts1 = parts

			params = []
			if ";" in parts0:
				temp = parts0.split(";")
				key = temp[0]
				for t in temp[1:]:
					m = re.match("^([a-zA-Z0-9-_]+)=(.+)$", t)
					if m:
						params.append((m.group(1), m.group(2)))
					else:
						params.append((t, None))
			else:
				key = parts0

			if ";" in parts1:
				values = parts1.split(";")
			else:
				values = [ parts1 ]

			ret.append(VCFToken(key, params, values, lineNo, contentLine))

		return ret
	#

#









