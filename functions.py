def getTasks(filepath='task.txt'):
    """ Reads text file and return list of task items"""
    with open(filepath, 'r') as file:
        a = file.readlines()
    return a

def addTasks(a, filepath='task.txt'):
    """ Writes user provided task to list of task items"""
    with open('task.txt', 'w') as file:
        file.writelines(a)
