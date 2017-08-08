tasks=[]
def ask_input():
        user_input = input("\n Enter a task in single quotes, list all tasks and task indices by typing -list, and delete a task by typing -del(index). \n")
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
        if len(tasks)>0:
                print("\n Index \t Task")
                for i in range(0, len(tasks)):
                        print(str(i)+"\t"+str(tasks[i]))
                        print("\n")
        else:
                print("You currently have 0 tasks.")
        ask_input()
def delete_task(index):
        index=int(index)
        if index>=len(tasks) or index<0:
                print("index out of bounds. \n")
        else:
                print(str(tasks[index])+" has been deleted. \n")
                tasks.remove(tasks[index])
        ask_input()  
ask_input()
    
    
    
