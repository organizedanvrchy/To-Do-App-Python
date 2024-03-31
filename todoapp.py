print("Welcome to your ToDo App!\n")
print("Follow the prompt below to begin.\n")

while True:
    user_action = input("\nType add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            print("\nAdd a ToDo to your tasklist!")
            action = input("Enter your task: ") + "\n"
            action = action.title()

            file = open('todo.txt', 'r')
            actions = file.readlines()
            file.close()

            actions.append(action)

            file = open('todo.txt', 'w')
            file.writelines(actions)
            file.close()
        case 'show':
            print("\nHere's your current list of tasks:\n")

            file = open('todo.txt', 'r')
            actions = file.readlines()
            file.close()

            #new_actions = [item.strip('\n') for item in actions]

            for i, value in enumerate(actions, 1):
                print("{}. {}".format(i, value.strip('\n')))
        case 'edit':
            number = int(input("\nEnter the number of the task you would like to edit: "))
            number -= 1
            new_action = input("\nEnter a new value: ")
            new_action = new_action.title()
            actions[number] = new_action
        case 'complete':
            comp = int(input("\nPlease enter the number of the task you would like to mark as complete: "))
            comp -= 1
            actions.pop(comp)
        case 'exit':
            break
        case _:
            print("\nThis command is unknown! Please try again\n")

print("\nGoodbye!")
