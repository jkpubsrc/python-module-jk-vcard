
import jk_typing

from .QuotedPrintable import QuotedPrintable

from .VCardItem import VCardItem
from .VCard import VCard







class VCFEncoder(object):

	@staticmethod
	@jk_typing.checkFunctionSignature()
	def toLines(vCard:VCard):
		yield "BEGIN:VCARD"
		yield "VERSION:" + str(vCard.version)
		for item in vCard.data:
			yield VCFEncoder.__itemToLine(item)
		yield "END:VCARD"
	#

	@staticmethod
	def __needsEncoding(charSequence:str):
		for c in charSequence:
			d = ord(c)
			if (d < 32) or (d > 127):
				# print(d, repr(c))
				return True

		return False
	#

	@staticmethod
	def __itemToLine(item:VCardItem) -> str:
		key = item.key
		params = list(item.params)

		# decide: do we need encoding?

		sEncoding = None
		for v in item.values:
			if VCFEncoder.__needsEncoding(v):
				sEncoding = "QUOTED-PRINTABLE"

		# encode

		if sEncoding:
			if sEncoding == "QUOTED-PRINTABLE":
				values = [
					QuotedPrintable.encode(v, True) for v in item.values
				]
				params.append(("CHARSET", "UTF-8"))
				params.append(("ENCODING", sEncoding))

			else:
				raise Exception("Unexpected encoding: " + repr(sEncoding))

		else:
			values = item.values

		# to string

		ret = [ key ]

		for p in params:
			ret.append(";")
			pKey, pValue = p
			ret.append(pKey)
			if pValue is not None:
				ret.append("=" + pValue)

		ret.append(":")

		b = False
		for v in values:
			if b:
				ret.append(";")
			else:
				b = True
			ret.append(v)

		return "".join(ret)
	#

#












