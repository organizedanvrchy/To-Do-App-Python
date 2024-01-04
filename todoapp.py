actions = []

print("")
print("Welcome to the infinite list grower!")
print("")
print("Follow the prompt to add or show the list!")
print("")

while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    print("")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            action = input("Enter what you would like to add to the list: ")
            print("")
            action = action.title()
            actions.append(action)
        case 'show':
            for i, value in enumerate(actions, 1):
            print("{}. {}".format(i, value))
            print("")
        case 'edit':
            number = int(input("Enter the number of the item you would like to edit: "))
            print("")
            number -= 1
            new_action = input("Enter a new value: ")
            print("")
            new_action = new_action.title()
            actions[number] = new_action
        case 'complete':
            print("")
            comp = int(input("Please enter the number of the item to complete: "))
            print("")
            comp -= 1
            actions.pop(comp)
        case 'exit':
            break
        case _:
            print("This command is unknown! Please try again")
            print("")

print("")
print("Goodbye!")
