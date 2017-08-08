tasks=[]
deleted=[]
def ask_input():
        print("\n")
        user_input = input("Type in a command, or type -help for more details.")
        process_input(user_input)
def process_input(user_input):
        if user_input[0]=="'" and user_input[len(user_input)-1] =="'":
                add_task(user_input)
        elif user_input.lower()=="-list":
                list_task()
        elif user_input[0:5].lower()=="-del(" and user_input[len(user_input)-1]==")" and user_input[5:len(user_input)-1].isdigit():
                delete_task(user_input[5:len(user_input)-1])
        elif user_input.lower()=="-listdel":
                listdel_task()
        elif user_input.lower()=="-help":
                gethelp()
        else:
                print("error in input, please try again")
                ask_input()
def gethelp():
        print("\n")
        print("Enter a task in single quotes. Example: 'task 1'\nList all tasks and task indices by typing -list.\nDelete a task by typing -del(index). Example: -del(0)\nView deleted tasks by typing -listdel.\nGet help by typing -help.")
        ask_input()
def add_task(user_input):
        print(str(user_input)+" has been added.")
        tasks.append(user_input)
        ask_input()
def list_task():
        if len(tasks)>0:
                print("\n")
                print("Index \t Task")
                for i in range(0, len(tasks)):
                        print(str(i)+"\t"+str(tasks[i]))
                        print("\n")
        else:
                print("You currently have 0 tasks.")
        ask_input()
def listdel_task():
        if len(deleted)>0:
                print("\n")
                print("Index \t Task")
                for i in range(0, len(deleted)):
                        print(str(i)+"\t"+str(deleted[i]))
                        print("\n")
        else:
                print("You have not deleted any tasks.")
        ask_input()
def delete_task(index):
        index=int(index)
        if index>=len(tasks) or index<0:
                print("index out of bounds. \n")
        else:
                print(str(tasks[index])+" has been deleted. \n")
                deleted.append(tasks[index])
                tasks.remove(tasks[index])
        ask_input()  
gethelp()
ask_input()
    
    
    
