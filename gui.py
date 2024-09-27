import functions
import FreeSimpleGUI as fsg                 

label = fsg.Text("Type in a task:")
inputBox = fsg.InputText(tooltip="Enter task")
addButton = fsg.Button("Add")

window = fsg.Window('My To-Do App', layout=[[label], [inputBox, addButton]])
window.read()
window.close()
