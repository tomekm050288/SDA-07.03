import uuid
from abc import ABC,abstractmethod

class Vehicle(ABC):
	
	def get_idn(self):
		return self.idn
	
	def number_of_wheels(self):
		return self.wheels


	
class Bicycle(Vehicle):
	def __init__(self,wheels,idn = str(uuid.uuid4())):
		self.wheels = wheels
		self.idn = idn
	

class Bike(Bicycle):
	def __init__(self,engine,wheels,idn = str(uuid.uuid4())):
		super().__init__(wheels)
		self.engine = engine
		self.idn = idn
	
	def type_of_engine(self):
		return self.engine
		
	
class Car(Bike):
	def __init__(self,idn = str(uuid.uuid4()),*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.idn = idn

		
class Truck(Bike):
	def __init__(self, cargo,idn = str(uuid.uuid4()), *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.cargo = cargo
		self.idn = idn
	
	def get_cargo(self):
		return self.cargo
	
	
	
class Transport_Truck(Truck):
	def __init__(self, cargo, idn = str(uuid.uuid4()), *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.idn = idn
		
		

class Plane(Bike):
	def __init__(self,airport,idn = str(uuid.uuid4()),*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.airport = airport
		self.idn = idn
		
	def get_home_airport(self):
		return self.airport
	
		
		
bicycle1 = Bicycle(2)

print(bicycle1.get_idn())
print(bicycle1.number_of_wheels())

plane1 = Plane(airport="Balice",wheels=15,engine="Big")

print(plane1.get_idn())


car1 = Car(engine="1.6",wheels="4")

print(car1.get_idn())


truck1= Truck(engine='2.5',wheels=8,cargo='furniture')

print(truck1.get_idn(), truck1.engine)


