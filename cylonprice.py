# # coding: utf-8
class Product(object):
	price = 0
	count = 0
	vat = 0

	def __init__(self, price, count, vat):
		self.price = price
		self.count = count
		self.vat = vat

	def price_with_tax(self):
		return self.price * self.count * self. vat

products = [Product(price = 900, count = 2, vat = 1.25), Product(price = 100, count = 1, vat = 1.06)]
total_price = products[0].price_with_tax() + products[1].price_with_tax()

print total_price

# cylon = Product(price = 900, count = 2, vat = 1.25)
# manual = Product(price = 100, count = 1, vat = 1.06)

# print cylon.price_with_tax() + manual.price_with_tax()