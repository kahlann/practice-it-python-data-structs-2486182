import collections

# Task class
class Task:
    # Initialiser
    def __init__(self, taskname, priority=False):
        self.taskname = taskname
        self.priority = priority
    
    # String description of the task and whether it has priority
    def __str__(self):
        if self.priority == True:
            return f"{self.taskname} has priority."
        else:
            return f"{self.taskname} does not have priority."

# Function to add the task to a task list (a deque object)
def addTask(task, TaskList):
    # If the task has priority
    if task.priority == True:
        # Add the task to the front of the list
        return TaskList.appendleft(task.taskname)
    # If it does not have priority
    else:
        return TaskList.append(task.taskname)
    
# Function to remove a specific task from the task list (a deque object)
def delTask(task, TaskList):
    return TaskList.remove(task.taskname)

# Function to do the next task from the task list 
def doTask(TaskList):
    return TaskList.popleft()


def main():
    my_tasks = collections.deque()
    # print the current task list
    print(f"Current task list: {my_tasks}")

    # Create some tasks, add them to the task list
    print("Adding tasks...")
    addTask(Task("Start report"), my_tasks)
    addTask(Task("Clean desk"), my_tasks)
    addTask(Task("Make figures"), my_tasks)
    addTask(Task("Reply to emails", True), my_tasks)

    # print the current task list
    print(f"Current task list: {my_tasks}")

    # Do some tasks
    print("Doing a task...")
    doTask(my_tasks)

    # print the current task list
    print(f"Current task list: {my_tasks}")

    # Remove a task
    print("Remove a task...")
    delTask(Task("Clean desk"), my_tasks)

    # print the current task list
    print(f"Current task list: {my_tasks}")

if __name__ == "__main__":
    main()