from abc import ABC

class Library:
	def __init__(self, name):
		self.name = name
		
class Item(ABC):
	def __init__(self, id, publish_date,authors = None):
		self.id = id
		self.publish_date = publish_date
		self.authors = authors
		self.history = []
		
		
	def add_history(self,who,when):
		self.history.append((who,when))
		
	def get_id(self):
		return self.id
	
	def get_publish_date(self):
		return self.publish_date
	
		
class Book(Item):
	def __init__(self, isbn, number_of_page, *args,**kwargs):
		super().__init__(*args,**kwargs)
		self.isbn = isbn
		self.number_of_page = number_of_page
		
	def get_isbn(self):
		return self.isbn
	
	def get_number_of_pag(self):
		return self.number_of_page
		

class Magazine(Book):
	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		
		
class Movie(Book):
	def __init__(self,video_lenght,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.video_lenght = video_lenght


class CDs(Book):
	def __init__(self, no_of_songs, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.no_of_songs = no_of_songs


class Author:
	def __init__(self, name = None, surename = None, born_date = None, death_date = None):
		self.name = name
		self.surename = surename
		self.born_date = born_date
		self.death_date = None
		
		
		
author1 = Author(name='Andrzej Sapkowski')
book1 = Book(123,400,99,"12-12-2020",authors = [author1])

print(book1.authors[0].name)


