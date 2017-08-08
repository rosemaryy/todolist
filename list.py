tasks=[]
def ask_input():
 	user_input = input("Enter a task in single quotes, list all tasks and task indices by typing -list, and delete a task by typing -del(index).")
 	process_input(user_input)
def process_input(user_input):
 	if user_input[0]=="'" and user_input[len(user_input)-1] =="'":
		add_task(user_input)
  	elif user_input.lower()=="-list":
  		list_task()
  	elif user_input[0:5].lower()=="-del(" and user_input[len(user_input)-1]==")" and user_input[5:len(user_input)-1].isdigit():
    		delete_task(user_input[5:len(user_input)-1])
	else:
    	print("error in input, please try again")
	ask_input()
def add_task(user_input):
	tasks.append(user_input)
	ask_input()
def list_task():
	print("Index \t Task")
	for i in range(0, len(tasks):
		print(i+"\t"+tasks[i])
	ask_input()
def delete_task(index):
	if index>=len(tasks) or index<0:
		print("index out of bounds")
    	else:
		print(tasks[index]+" has been deleted")
		tasks.remove(tasks[index])
	ask_input()  
ask_input()
    
    
    
