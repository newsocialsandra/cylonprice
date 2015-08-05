# coding: utf-8
class Product(object):
	price = 0
	count = 0
	vat = 0

	def price_with_tax(self):
		return self.price * self.count * self. vat

cylon = Product()
cylon.price = 900
cylon.count = 2
cylon.vat = 1.25

manual = Product()
manual.price = 100
manual.count = 1
manual.vat = 1.06

print cylon.price_with_tax() + manual.price_with_tax()