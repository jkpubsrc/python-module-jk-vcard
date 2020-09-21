
import jk_typing
from jk_utils.tokenizer2 import TokenizationError
from jk_version import Version

from .QuotedPrintable import QuotedPrintable
from .VCFTokenizer import VCFTokenizer
from .VCFToken import VCFToken
from .VCardItem import VCardItem
from .VCard import VCard







class VCFParser(object):

	@staticmethod
	def parseText(text:str, bDebug:bool = False) -> list:
		tokens = VCFTokenizer.tokenize(text)

		return VCFParser.parseTokens(tokens, bDebug)
	#

	@staticmethod
	def parseTokens(tokens, bDebug:bool = False) -> list:
		ret = []

		# group tokens by begin/end

		buffer = []
		version = None
		orgLines = []
		for token in tokens:
			orgLines.append(token.orgLine)

			if token.key == "VERSION":
				version = Version(token.values[0])

			elif (token.key == "BEGIN") and (token.values[0] == "VCARD"):
				assert not buffer
				assert version is None

			elif (token.key == "END") and (token.values[0] == "VCARD"):
				assert version
				ret.append(
					VCard(version, buffer, orgLines)
				)
				buffer = []
				orgLines = []
				version = None

			else:
				preferredEncoding = None
				if token.hasParam("ENCODING"):
					# this token is encoded; decode it;
					sEncoding = token.getParam("ENCODING")
					sCharset = token.getParam("CHARSET")
					preferredEncoding = sEncoding

					# TODO: support more encoding
					if sEncoding == "QUOTED-PRINTABLE":
						for i in range(0, len(token.values)):
							token.values[i] = QuotedPrintable.decode(token.values[i], sCharset)
						token.removeParam("ENCODING")
						token.removeParam("CHARSET")
					else:
						raise TokenizationError("Unexpected encoding: " + repr(sEncoding), token.lineNo, 1)

				buffer.append(
					VCardItem(token.key, token.params, token.values, preferredEncoding)
				)

		assert not buffer
		assert version is None

		return ret
	#

#




