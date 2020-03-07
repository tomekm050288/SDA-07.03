import uuid

class Vehicle(object):
	def __init(self, idn = str(uuid.uuid4())):
		self.idn = idn
	
	def get_idn(self):
		return self.idn
	
	
class Bicycle(Vehicle):
	def __init__(self,wheels,idn = str(uuid.uuid4())):
		super().__init__(idn)
		self.wheels = wheels
	
	def number_of_wheels(self):
		return self.wheels


class Bike(Bicycle):
	def __init__(self,engine,wheels,idn = str(uuid.uuid4())):
		super().__init__(idn,wheels)
		self.engine = engine
	
	def type_of_engine(self):
		return self.engine
		
	
class Car(Bike):
	def __init__(self,engine,wheels,idn = str(uuid.uuid4())):
		super().__init__(idn,wheels,engine)
		
class Truck(Bike):
	def __init__(self, cargo, engine, wheels, idn = str(uuid.uuid4())):
		super().__init__(idn,wheels,engine)
		self.cargo = cargo
	
	def get_cargo(self):
		return self.cargo
	
	
class Transport_Truck(Truck):
	def __init__(self, cargo, engine, wheels, idn = str(uuid.uuid4())):
		super().__init__(idn,wheels,engine,cargo)

class Plane(Bike):
	def __init__(self,engine,wheels,airport,idn = str(uuid.uuid4())):
		super().__init__(wheels,idn,engine)
		self.airport = airport
		
	def get_home_airport(self):
		return self.airport
		
		
plane1 = Plane("big engine",14,"Balice")