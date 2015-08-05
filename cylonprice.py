# coding: utf-8

cylon = {
	"price": 900,
	"count": 2,
	"vat": 1.25
	}
manual = {
	"price": 100,
	"count": 1,
	"vat": 1.06
	}


print cylon["price"] * cylon["count"] * cylon["vat"] + manual["price"] * manual["count"] * manual["vat"] 