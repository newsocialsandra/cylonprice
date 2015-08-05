# coding: utf-8

class Product(object):
	price = 0
	count = 0
	vat = 0

cylon = Product()
cylon.price = 900
cylon.count = 2
cylon.vat = 1.25

manual = Product()
manual.price = 100
manual.count = 1
manual.vat = 1.06

print cylon.price * cylon.count * cylon.vat + manual.price * manual.count * manual.vat

# ["price"] * cylon["count"] * cylon["vat"] + manual["price"] * manual["count"] * manual["vat"] 