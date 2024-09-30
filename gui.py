import functions
import FreeSimpleGUI as fsg                 

label = fsg.Text("Type in a task:")
inputBox = fsg.InputText(tooltip="Enter task", key="addTask")
listBox = fsg.Listbox(values=functions.getTasks(), key="editTask",
                      enable_events=True, size=[45, 10])
addButton = fsg.Button("Add")
editButton = fsg.Button("Edit")
completeButton = fsg.Button("Complete")
exitButton = fsg.Button("Exit")

window = fsg.Window('My To-Do App', 
                    layout=[[label], 
                            [inputBox, addButton], 
                            [listBox, editButton, completeButton],
                            [exitButton]], 
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Add":
            tasks = functions.getTasks()
            newTask = values['addTask']
            tasks.append(newTask)
            functions.addTasks(tasks)
            
            window['editTask'].update(values=tasks)

        case "Edit":
            taskToEdit = values['editTask'][0]
            newTask = values['addTask']

            tasks = functions.getTasks()
            index = tasks.index(taskToEdit)
            tasks[index] = newTask
            functions.addTasks(tasks)

            window['editTask'].update(values=tasks)

        case "Complete":
            taskToComplete = values['editTask'][0]

            tasks = functions.getTasks()
            tasks.remove(taskToComplete)
            functions.addTasks(tasks)

            window['editTask'].update(values=tasks)
            window['addTask'].update(value='')

        case "Exit":
            break

        case 'editTask':
            window['addTask'].update(value=values['editTask'][0])

        case fsg.WIN_CLOSED:
            break


window.close()
