class Pizza:
	skladniki = ["pomidory", "ser"]
	
	def __init__(self, ingredinats):
		self.ingredinats =  ingredinats
		
	def get_ingrediants(self):
		return self.ingredinats
	
	
	@classmethod
	def create_margeritha(cls):
		return cls.skladniki
	
	@classmethod
	def update_margeritha(cls, nowe_skladniki):
		cls.skladniki = nowe_skladniki
		return cls.skladniki
		
	@staticmethod
	def get_possible_pizza():
		return ['margerita']
	
	
	
pizza = Pizza(['mozarella','sos'])

pizza2 = Pizza.create_margeritha()

print(Pizza.get_possible_pizza())

