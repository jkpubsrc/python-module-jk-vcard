





class VCardItem(object):

	def __init__(self, key:str, params:list, values:list, preferredEncoding:str = None):
		self.key = key
		self.params = params
		self.values = values
		self.preferredEncoding = preferredEncoding
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
		if self.params:
			s = []
			for p in self.params:
				if p[1] is None:
					s.append(p[0])
				else:
					s.append(str(p))
			return self.key + "[" + ", ".join(s) + "]: " + repr(self.values)
		else:
			return self.key + ": " + repr(self.values)
	#

	def __repr__(self):
		return "VCardItem< key=" + self.key + ", params=" + repr(self.params) + ", values=" + repr(self.values) + " >"
	#

#







