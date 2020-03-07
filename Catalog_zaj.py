import uuid
from abc import ABC



class Pojazd(ABC):
	
    def get_idn(self):
        return self.idn
    
    def get_number_of_wheels(self):
        return self.wheels


class PojazdMechaniczny(Pojazd):
	
	def get_type_of_engine(self):
		return self.engine


class PojazdTowarowy:
    def __init__(self):
        self.cargo = None

    def get_cargo(self):
        return self.cargo

	
class Rower(Pojazd, PojazdTowarowy):
	
    def __init__(self, idn=str(uuid.uuid4()), *args, **kwargs):
        self.idn = idn
        self.wheels = 2
        if 'cargo' in kwargs:
            self.cargo = kwargs['cargo']
		    
class Motor(Pojazd):
    def __init__(self, idn=str(uuid.uuid4())):
        self.idn = idn
        self.wheels = 2

	    
class SamochodOsobowy(PojazdMechaniczny):
    def __init__(self, idn=str(uuid.uuid4())):
        self.idn = idn
        self.wheels = 4
        self.engine = "Benzyna"
	    
    
class SamochodDostawczy(PojazdMechaniczny, PojazdTowarowy):
    def __init__(self, idn=str(uuid.uuid4())):
        self.idn = idn
        self.wheels = 4
        self.engine = "Benzyna"
	    
class Samolot(PojazdMechaniczny, PojazdTowarowy):
    def __init__(self, idn=str(uuid.uuid4())):
        self.idn = idn
        self.wheels = 4
        self.engine = "Benzyna"
	    
    def get_home_airport(self):
        return self.airport
    
    
x = Rower("123", cargo="ziemniaki")

