import json
import os
from datetime import datetime

def addTask(task, priority="Medium"):
    task_data = {
        "task": task,
        "priority": priority,
        "status": "incomplete"
    }

    if os.path.exists('tasks.json'):
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    else:
        tasks = []

    tasks.append(task_data)

    with open('tasks.json', 'w') as file:
        json.dump(tasks, file, indent=4)

    print("Task added successfully.")

def showTasks():
    if not os.path.exists('tasks.json'):
        print("No tasks found.")
        return

    with open('tasks.json', 'r') as file:
        tasks = json.load(file)

    incomplete_tasks = [t for t in tasks if t['status'] == 'incomplete']

    if not incomplete_tasks:
        print("No incomplete tasks to show.")
        return

    print("\n--- Incomplete Tasks ---")
    for idx, task in enumerate(incomplete_tasks, 1):
        print(f"{idx}. {task['task']} [Priority: {task['priority']}]")

def showCompletedTasks():
    if not os.path.exists('tasks.json'):
        print("No tasks found.")
        return

    with open('tasks.json', 'r') as file:
        tasks = json.load(file)

    completed_tasks = [t for t in tasks if t['status'] == 'completed']

    if not completed_tasks:
        print("No completed tasks to show.")
        return

    print("\n--- Completed Tasks ---")
    for idx, task in enumerate(completed_tasks, 1):
        completed_at = task.get('completed_at', 'Unknown time')
        print(f"{idx}. {task['task']} [Priority: {task['priority']}] - Completed at: {completed_at}")

def completeTask():
    if not os.path.exists('tasks.json'):
        print("No tasks to complete.")
        return

    with open('tasks.json', 'r') as file:
        tasks = json.load(file)

    incomplete_tasks = [t for t in tasks if t['status'] == 'incomplete']

    if not incomplete_tasks:
        print("No incomplete tasks available to complete.")
        return

    print("\nIncomplete tasks:")
    for idx, task in enumerate(incomplete_tasks, 1):
        print(f"{idx}. {task['task']} [Priority: {task['priority']}]")

    try:
        task_num = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= task_num < len(incomplete_tasks):
            # Find index of this task in the original tasks list
            task_to_complete = incomplete_tasks[task_num]
            for task in tasks:
                if task == task_to_complete:
                    task['status'] = 'completed'
                    task['completed_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    break

            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)

            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input! Please enter a number.")

def undoTask():
    
    if not os.path.exists('tasks.json'):
        print("No tasks to complete.")
        return
    
    with open('tasks.json', 'r') as file:
        tasks = json.load(file)
        
    completed_tasks = [t for t in tasks if t['status'] == 'completed']
    
    if not completed_tasks:
        print("No complete tasks available to undo.")
        return
    
    
    print("\n--- Completed Tasks ---")
    for idx, task in enumerate(completed_tasks, 1):
        completed_at = task.get('completed_at', 'Unknown time')
        print(f"{idx}. {task['task']} [Priority: {task['priority']}] - Completed at: {completed_at}")
        
    try:
        task_num = int(input("Enter task number to mark as incomplete: ")) - 1
        if 0 <= task_num < len(completed_tasks):
            
            task_to_undo = completed_tasks[task_num]
            for task in tasks:
                if task == task_to_undo:
                    task['status'] = 'incomplete'
                    break

            with open('tasks.json', 'w') as file:
                json.dump(tasks, file, indent=4)

            print("Task marked as incomplete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input! Please enter a number.")
    
        

def main():
    while True:
        print("\n--- Your JSON To-Do List ---")
        print("1. Add Task")
        print("2. Show Incomplete Tasks")
        print("3. Complete Task")
        print("4. Show Completed Tasks")
        print("5. Undo Completed Tasks")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                task = input("Enter your task: ")
                priority = input("Priority (High/Medium/Low): ")
                addTask(task, priority)
            elif choice == 2:
                showTasks()
            elif choice == 3:
                completeTask()
            elif choice == 4:
                showCompletedTasks()
            elif choice == 5:
                undoTask()
            elif choice == 6:
                print("Exiting... Bye!")
                break
            else:
                print("Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Enter a number.")

if __name__ == "__main__":
    main()
