





class VCFToken(object):

	def __init__(self, key:str, params:list, values:list, lineNo:int, orgLine:str):
		self.key = key
		self.params = params
		self.lineNo = lineNo
		self.values = values
		self.orgLine = orgLine
	#

	def hasParam(self, paramName:str) -> bool:
		for p, v in self.params:
			if p == paramName:
				return True
		return False
	#

	def getParam(self, paramName:str, defaultValue = None):
		for p, v in self.params:
			if p == paramName:
				return v
		return defaultValue
	#

	def removeParam(self, paramName:str) -> bool:
		i = 0
		for p, v in self.params:
			if p == paramName:
				del self.params[i]
				return True
			i += 1
		return False
	#

	def __str__(self):
		return "VCFToken< key=" + repr(self.key) + ", params=" + repr(self.params) + ", values=" + repr(self.values) + " >"
	#

	def __repr__(self):
		return self.__str__()
	#

#






