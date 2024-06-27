#global variables and dictionaries
import sys
all_tasks = []
task_status = []
menu_select = 0

#function for adding a  task to the list
def add_task():
    while True:
        try:
            add_task = str(input("Please add the name of the task you would like to add: "))
            all_tasks.append(add_task)
            task_status.append("Incomplete")
            more_tasks = input("Task added. Would you like to add any more tasks? (Y/N): ")
            while more_tasks not in ["Y", "N"]:
                more_tasks = input("Please type either Y or N: ")
            if more_tasks == "N":
                print(f"'{add_task}' added as incomplete")
                break  
            
        except TypeError: 
            print("Please type a valid task description")


#function to view all of the tasks and their status  
def view_task_list():
    for index, task in enumerate(all_tasks):
        status = task_status[index]
        task_number = index + 1
        print(f"{task_number}. {task} - {status}")


# Function to mark a task as complete 
def mark_complete():

        for index, task in enumerate(all_tasks):
            status = task_status[index]
        task_number = index + 1
        print(f"{task_number}. {task} - {status}")

        change_task_status =  input("What number task do you want to change to complete?: ")
        while True:
            try: 
                change_task_status = int(change_task_status) -1  
                if 0 <= change_task_status < len(all_tasks):
                    task_status[change_task_status] = "Complete"
                    try_again = input("Would you like to change another task?: ")
                    while try_again not in ['Y', 'N']:
                        try_again = input("Please type either Y or N: ")
                if try_again == 'N':
                    break     
                else: 
                    print("Please put in a valid task number")
            except ValueError:
                print("Please put in a valid task number")
       

#function for deleting a task 
def delete_task():
        for index, task in enumerate(all_tasks):
            status = task_status[index]
        task_number = index + 1
        print(f"{task_number}. {task} - {status}")

        delete_the_task =  input("What number task do you want to delete?: ")
        while True:
            try: 
                delete_the_task = int(delete_the_task) -1  
                if 0 <= delete_the_task < len(all_tasks):
                    del task_status[delete_the_task] 
                    del all_tasks[delete_the_task]
                    try_again = input("Would you like to delete another task?: ")
                    while try_again not in ['Y', 'N']:
                        try_again = input("Please type either Y or N: ")
                if try_again == 'N':
                    break     
                else: 
                    print("Please put in a valid task number")
            except ValueError:
                print("Please put in a valid task number")

# function to quit the program        
def quit():
    print("\n Thank you for using. Goodbye.") 
    sys.exit()
        


#run each of the programs and andle the errors 
while True:
    try:
        menu_select = int(input( "\n----------------------------------------\n\t Welcome to the To-Do List App! \n\n \t Menu: \n\t 1. Add a task \n\t 2. View tasks \n\t 3. Mark a task as complete \n\t 4. Delete a task \n\t 5. Quit:\n ---------------------------------------\n"))
        if menu_select == "1":
            add_task()
        if menu_select == "2":
            view_task_list()
        if menu_select == "3":
            mark_complete()
        if menu_select == "4":
            delete_task() 
        if menu_select == "5":
            quit()
        if  menu_select > 5:
            print("Please type one of the listed numbers.")
    except TypeError: 
        print("Please type one of the listed numbers.")
    except ValueError: 
        print("Please type one of the listed numbers.")
    
