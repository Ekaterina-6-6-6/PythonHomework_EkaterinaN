class Product:

	def __init__(self, name, price):
		self.name = name
		self.price = price

	def sayName(self):
		print(self.name)

	def sayPrice(self):
		print("цена продукта", self.price)

	def pay(self):
		print(self.name, self.price)
