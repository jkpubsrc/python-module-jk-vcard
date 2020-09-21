jk_vcard
==========

Introduction
------------

This python module parses (and produces) vCard data as provided in vcf files.

Information about this module can be found here:

* [github.org](https://github.com/jkpubsrc/....)
* [pypi.python.org](https://pypi.python.org/pypi/jk_vcard)

How to use this module
----------------------

### Import this module

Please include this module into your application using the following code:

```python
import jk_vcard
```

### Parse a .vcf file

If you export your contacts in your Android smart phone, a VCF file is created. This can serve as an example file and can be parsed using the following code:

```python
with open("contacts.vcf", "r") as f:
	data = f.read()

for vCard in VCFParser.parseText(data):
	print("-" * 120)
	print()
	vCard.dump()
	print()

print("-" * 120)
```

### Produce a .vcf file from vCard data

If you want to produce a `.vcf` file you simply can invoke `VCFEncoder.toLines(...)` in order to generate text lines in this format:

```python
vCard = ....

for textLine in VCFEncoder.toLines(vCard):
	print(textLine)
```

If you have a list of `VCard` objects you can simple (re)create a `.vcf` file like this:

```python
with open("contacts.vcf", "w") as f:
	for vCard in myVCardList:
		for textLine in VCFEncoder.toLines(vCard):
			f.write(textLine + "\n")
```

Contact Information
-------------------

This work is Open Source. This enables you to use this work for free.

Please have in mind this also enables you to contribute. We, the subspecies of software developers, can create great things. But the more collaborate, the more fantastic these things can become. Therefore Feel free to contact the author(s) listed below, either for giving feedback, providing comments, hints, indicate possible collaborations, ideas, improvements. Or maybe for "only" reporting some bugs:

* Jürgen Knauth: pubsrc@binary-overflow.de

License
-------

This software is provided under the following license:

* Apache Software License 2.0



