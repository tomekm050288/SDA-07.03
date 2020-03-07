class Figure:
	def __init__(self,name,h,a):
		self.name = name
		self.wysokosc = h
		self.szerokosc = a
		
	def get_name(self):
		return "Jestem {}".format(self.name)
		
	def pole(self):
		return self.wysokosc*self.szerokosc
	

class Prostokat(Figure):
	def __init__(self):
		self.name = "Prostokat"
	
	
class Kwadrat(Figure):
	pass
	

ff = Prostokat()

print(ff.get_name())



