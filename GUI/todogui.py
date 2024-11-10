import functions
import FreeSimpleGUI as fsg
import time

fsg.theme("DarkGrey16")

# Create clock and labels
clock = fsg.Text('', key="clock", size=(20, 1), justification='center', font=('Helvetica', 12))
label = fsg.Text("Task Manager", font=('Helvetica', 24), justification='center')

# Create input field and buttons
inputBox = fsg.InputText(tooltip="Enter your task here", key="inputTask", size=(40, 1))
addButton = fsg.Button("Add", tooltip="Add a new task", size=(10, 1))
editButton = fsg.Button("Edit", tooltip="Edit the selected task", size=(10, 1))
completeButton = fsg.Button("Complete", tooltip="Mark task as complete", size=(15, 1))
exitButton = fsg.Button("Exit", tooltip="Exit the application", size=(10, 1))

# Create task list
listBox = fsg.Listbox(values=functions.getTasks(), key="listTask", 
                      enable_events=True, size=[45, 10], 
                      tooltip="Select a task to edit or complete")

# Organize layout into sections
layout = [
    [label],  # Title
    [clock],  # Clock
    [fsg.Frame(layout=[[inputBox, addButton]], title="", font=('Helvetica', 16))],  # Input box and Add button
    [fsg.Frame(layout=[[listBox]], title="Your Tasks", font=('Helvetica', 16))],  # Task list
    [editButton, completeButton, exitButton],  # Edit, Complete, and Exit buttons
]

# Create window
window = fsg.Window('My To-Do App', layout=layout, font=('Helvetica', 16), element_justification='center')

while True:
    event, values = window.read(timeout=1000)
    window["clock"].update(value=time.strftime("%b %d, %Y | %H:%M:%S"))

    match event:
        case "Add":
            tasks = functions.getTasks()
            newTask = values['inputTask'].strip()
            if newTask:
                tasks.append(newTask)
                functions.addTasks(tasks)
                window['listTask'].update(values=tasks)
                window['inputTask'].update(value='')
            
            else:
                fsg.popup("Please enter a valid task!", font=('Helvetica', 20))

        case "Edit":
            try:
                taskToEdit = values['listTask'][0]
                newTask = values['inputTask']

                if newTask:
                    tasks = functions.getTasks()
                    index = tasks.index(taskToEdit)
                    tasks[index] = newTask
                    functions.addTasks(tasks)
                    window['listTask'].update(values=tasks)
                else:
                    fsg.popup("Please enter a valid task to edit!", font=('Helvetica', 20))

            except IndexError:
                fsg.popup("Please select a task first!", font=('Helvetica', 20))

        case "Complete":
            try:
                taskToComplete = values['listTask'][0]

                tasks = functions.getTasks()
                tasks.remove(taskToComplete)
                functions.addTasks(tasks)

                window['listTask'].update(values=tasks)
                window['inputTask'].update(value='')
            except IndexError:
                fsg.popup("Please select a task first!", font=('Helvetica', 20))

        case "Exit":
            break

        case 'listTask':
            # Only update input if a task is actually selected
            if values['listTask']:  # Check if something is selected
                window['inputTask'].update(value=values['listTask'][0])

        case fsg.WIN_CLOSED:
            break

window.close()
