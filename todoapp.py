print("Welcome to your ToDo App!")
print("Follow the prompt below to begin.")

while True:
    user_action = input("\nType Add, Show, Edit, Complete, or Exit: ")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        action = user_action[4:].title()  

        with open('todo.txt', 'r') as file:
            actions = file.readlines()

        actions.append(action + '\n')

        with open('todo.txt', 'w') as file:
            file.writelines(actions)

    elif user_action.startswith('show'):
        with open('todo.txt', 'r') as file:
            actions = file.readlines()

        if len(actions) == 0:
            print("\nYou currently have no tasks in your list!")
        else:
            print("\nHere's a list of your tasks:\n")

        for i, value in enumerate(actions, 1):
            print("{}. {}".format(i, value.strip('\n')))

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number -= 1

            with open('todo.txt', 'r') as file:
                actions = file.readlines()
            
            new_action = input("\nEnter a new value: ")
            actions[number] = new_action.title() + '\n'

            with open('todo.txt', 'w') as file:
                file.writelines(actions)
        except ValueError:
            print("\nCommand is not valid. Please type 'edit' followed by the number of the task in your list.")
            continue
        except IndexError:
            print("\nCommand is not valid. You do not have that many tasks on your list.") 
            print("Please type 'edit' followed by the number of the task in your list.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            
            with open('todo.txt', 'r') as file:
                actions = file.readlines()

            tmp = number - 1
            action_remove = actions[tmp]
            actions.pop(tmp)

            with open('todo.txt', 'w') as file:
                file.writelines(actions)
        except ValueError:
            print("\nCommand is not valid. Please type 'complete' followed by the number of the task in your list.")
            continue
        except IndexError:
            print("\nCommand is not valid. You do not have that many tasks on your list.") 
            print("Please type 'complete' followed by the number of the task in your list.")
            continue

    elif user_action.startswith('exit'):
        break

    else:
        print("\nThis command is invalid! Please enter a command from the list.\n")

print("\nGoodbye!")
