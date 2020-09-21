


from jk_version import Version
import jk_typing

from .VCardItem import VCardItem






class VCard(object):

	def __init__(self, version:Version = None, data:list = None, orgLines:list = None):
		if version is None:
			version = Version(2, 1)
		else:
			assert isinstance(version, Version)

		if data is None:
			data = []
		else:
			assert isinstance(data, list)
			for d in data:
				assert isinstance(d, VCardItem)

		if orgLines is not None:
			assert isinstance(orgLines, list)
			for line in orgLines:
				assert isinstance(line, str)

		self.version = version
		self.data = data
		self.orgLines = orgLines
	#

	@jk_typing.checkFunctionSignature()
	def getItem(self, key:str):
		for item in self.data:
			if item.key == key:
				return item
		return None
	#

	@jk_typing.checkFunctionSignature()
	def getItems(self, key:str):
		ret = []
		for item in self.data:
			if item.key == key:
				ret.append(item)
		return ret
	#

	def dump(self, prefix:str = None, printFunc = None):
		if prefix is None:
			prefix = ""
		else:
			assert isinstance(prefix, str)

		if printFunc:
			assert callable(printFunc)
		else:
			printFunc = print

		prefix2 = prefix + "\t"
		printFunc(prefix + "VCard[")
		for item in self.data:
			printFunc(prefix2 + str(item))
		printFunc(prefix + "]")
	#

	def __str__(self):
		chunks = [ "VCard< " ]
		b = False
		for x in self.data:
			if b:
				chunks.append(", ")
			else:
				b = True
			chunks.append(str(x))
		chunks.append(" >")
		return "".join(chunks)
	#

	def __repr__(self):
		return self.__str__()
	#

#






