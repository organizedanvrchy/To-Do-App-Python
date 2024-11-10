FILEPATH = "task.txt"

def getTasks(filepath=FILEPATH):
    """Reads text file and returns a list of task items"""
    with open(filepath, 'r') as file:
        tasks = file.readlines()
    # Strip any extra newlines or spaces
    return [task.strip() for task in tasks]

def addTasks(tasks, filepath=FILEPATH):
    """Writes the list of tasks to the file, each on a new line"""
    with open(filepath, 'w') as file:
        file.writelines([task + '\n' for task in tasks])
