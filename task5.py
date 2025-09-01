"""# Task 5: Dynamic To-Do List
def update_todo_list(todo_list, new_tasks, status_updates):
    
    Manage a temporary to-do list by adding new tasks and updating task statuses.
    
    Parameters:
    todo_list: Existing dictionary with tasks as keys and their status as values.
    new_tasks: Any number of new tasks to add (status defaults to 'pending').
    status_updates: Key-value pairs to update the status of existing tasks.
    
    Example:
        todos = {}
        update_todo_list(todos, "Wash dishes", "Read book", Read_book="completed")
    """

def update_todo_list(todo_list, *new_tasks, **status_updates):

    for task in new_tasks:
        todo_list[task] = "Pending"
    
 #  todo_list.update(status_updates)
    todo_list["Read_book"] = status_updates["Read_book"] # This line of code update the todo_list(todos) using key: todo_list["Read_book"] = value: status_updates["Read_book"]
     
    return todo_list

todos = {}
print(update_todo_list(todos, "Wash dishes", "Read book", Read_book="completed"))
