


import binascii




#
# https://en.wikipedia.org/wiki/Quoted-printable
#
class QuotedPrintable(object):

	@staticmethod
	def decode(charSequence:str, encoding:str = None):
		assert isinstance(charSequence, str)
		if encoding:
			assert isinstance(encoding, str)
		else:
			encoding = "utf-8"

		ret = bytearray()

		i = 0
		maxLen = len(charSequence)
		while i < maxLen:
			c = charSequence[i]
			if c == "=":
				ret += binascii.unhexlify(
							charSequence[i+1] + charSequence[i+2]
				)
				i += 3
			else:
				ret.append(c)
				i += 1

		return ret.decode(encoding)
	#

	@staticmethod
	def encode(charSequence:str, bEncodeAll:bool):
		ret = []
		
		byteSequence = charSequence.encode("utf-8")
		for d in byteSequence:
			if not bEncodeAll and (d != 61) and (d >= 33) and (d <= 126):
				ret.append(chr(d))
			else:
				ret.append("=" + hex(d)[2:])

		return "".join(ret).upper()
	#

	@staticmethod
	def needsEncoding(charSequence:str):
		byteSequence = charSequence.encode("utf-8")
		for d in byteSequence:
			if (d != 61) and (d >= 33) and (d <= 126):
				pass
			else:
				return True

		return False
	#

#







