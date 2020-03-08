import json

class TODO:
	def __init__(self,name):
		self.name = name
		self.list_of_task = {}
		self.finished_task = {}
		
	def add_task(self,id,task):
		self.list_of_task[id] = task
		with open("list.txt", 'a+') as file:
			file.write(json.dumps(self.list_of_task))
			

	def remove_task(self,id):
		del self.list_of_task[id]
		with open("list.txt", 'w') as file:
			file.write(json.dumps(self.list_of_task))
				
	def finish_task(self,id):
		self.finished_task[id] = self.list_of_task[id]
		del self.list_of_task[id]
		with open("done_task.txt", 'a+') as file:
			file.write(json.dumps(self.finished_task))
			
	
	
	
		
		
		
		
		
		
		
new_todo = TODO("new_name")
new_todo.add_task("1","pierwszy task")
new_todo.add_task("2","drugi task")
new_todo.add_task("3","trzeci task")
new_todo.remove_task("1")

new_todo.finish_task("2")


