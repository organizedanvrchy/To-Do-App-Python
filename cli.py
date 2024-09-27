import functions
import time

print("Welcome to your ToDo App!")
currTime = time.strftime("%b %d, %Y | %H:%M:%S")
print(currTime)
print("Follow the prompt below to begin.")

while True:
    userAction = input("\nType Add, Show, Edit, Complete, or Exit: ")
    userAction = userAction.strip()

    if userAction.startswith('add'):
        action = userAction[4:].strip()
        
        if not action:
            print("\nYou did not add a task to the list.")
            continue

        action = action.title()  

        actions = functions.getTasks()

        actions.append(action + '\n')

        functions.addTasks(actions, 'task.txt')

    elif userAction.startswith('show'):
        actions = functions.getTasks()

        if len(actions) == 0:
            print("\nYou currently have no tasks in your list!")
        else:
            print("\nHere's a list of your tasks:\n")

        for i, value in enumerate(actions, 1):
            print("{}. {}".format(i, value.strip('\n')))

    elif userAction.startswith('edit'):
        try:
            number = int(userAction[5:])
            number -= 1

            actions = functions.getTasks()
            
            newAction = input("\nEnter a new value: ")
            actions[number] = newAction.title() + '\n'

            functions.addTasks(actions, 'task.txt')
                     
        except ValueError:
            print("\nCommand is not valid. Please type 'edit' followed by the number of the task in your list.")
            continue
        except IndexError:
            print("\nCommand is not valid. You do not have that many tasks on your list.") 
            print("Please type 'edit' followed by the number of the task in your list.")
            continue

    elif userAction.startswith('complete'):
        try:
            number = int(userAction[9:])
            
            actions = functions.getTasks()

            tmp = number - 1
            actionRemove = actions[tmp]
            actions.pop(tmp)

            functions.addTasks(actions, 'task.txt')

        except ValueError:
            print("\nCommand is not valid. Please type 'complete' followed by the number of the task in your list.")
            continue
        except IndexError:
            print("\nCommand is not valid. You do not have that many tasks on your list.") 
            print("Please type 'complete' followed by the number of the task in your list.")
            continue

    elif userAction.startswith('exit'):
        break

    else:
        print("\nThis command is invalid! Please enter a command from the list.\n")

print("\nGoodbye!")
