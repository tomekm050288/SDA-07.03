class Pizza:
	skladniki = ["pomidory", "ser"]
	
	def __init__(self, *ingredinats):
		self.ingredinats =  ingredinats
		
	def get_ingrediants(self):
		return self.ingredinats
	
	
	@classmethod
	def create_margeritha(cls):
		return cls(cls.skladniki)
	
	@classmethod
	def update_margeritha(cls, nowe_skladniki):
		cls.skladniki = nowe_skladniki
		return cls(cls.skladniki)
		
	@staticmethod
	def get_possible_pizza():
		return ['margerita']
	
	
	@classmethod
	def CreatePizza(cls,text):
		new_pizza = cls(*text.split(","))
		return new_pizza
	
line_of_text = "sos,mozarella,szynka,pieczarki"
pizza_1 = Pizza.CreatePizza(line_of_text)

print(pizza_1.ingredinats)



	
pizza = Pizza('mozarella','sos')
print(pizza.ingredinats)


pizza2 = Pizza.create_margeritha()
print(pizza2.ingredinats)

pizza3 = Pizza.update_margeritha(['sos','ser'])
print(pizza3.ingredinats)



print(Pizza.get_possible_pizza())

