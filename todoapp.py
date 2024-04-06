print("Welcome to your ToDo App!")
print("Follow the prompt below to begin.")

while True:
    user_action = input("\nType add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            print("\nAdd a task to your list!")
            action = input("Enter your task: ") + "\n"
            action = action.title()

            with open('todo.txt', 'r') as file:
                actions = file.readlines()

            actions.append(action)

            with open('todo.txt', 'w') as file:
                file.writelines(actions)

        case 'show':
            print("\nHere's your current list of tasks:\n")

            with open('todo.txt', 'r') as file:
                actions = file.readlines()

            #new_actions = [item.strip('\n') for item in actions]

            for i, value in enumerate(actions, 1):
                print("{}. {}".format(i, value.strip('\n')))

        case 'edit':
            number = int(input("\nEnter the number of the task you would like to edit: "))
            number -= 1

            with open('todo.txt', 'r') as file:
                actions = file.readlines()
            
            new_action = input("\nEnter a new value: ")
            actions[number] = new_action.title() + '\n'

            with open('todo.txt', 'w') as file:
                file.writelines(actions)

        case 'complete':
            comp = int(input("\nPlease enter the number of the task you would like to mark as complete: "))
            
            with open('todo.txt', 'r') as file:
                actions = file.readlines()

            tmp = comp - 1
            action_remove = actions[tmp]
            actions.pop(tmp)

            with open('todo.txt', 'w') as file:
                file.writelines(actions)

        case 'exit':
            break

        case _:
            print("\nThis command is unknown! Please try again\n")

print("\nGoodbye!")
