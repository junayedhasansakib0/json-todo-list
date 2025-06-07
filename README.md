# JSON To-Do List

## Overview

The JSON To-Do List is a simple command-line application built with Python that allows users to manage their tasks. Tasks are stored in a JSON file (`tasks.json`), with features to add tasks, mark them as completed, and view both incomplete and completed tasks. Each task includes a description, priority level (High, Medium, or Low), status, and a completion timestamp (for completed tasks).

## Features

- **Add Task**: Create a new task with a description and priority (default: Medium).
- **Show Incomplete Tasks**: Display all tasks that are not yet completed.
- **Complete Task**: Mark an incomplete task as completed, recording the completion timestamp.
- **Show Completed Tasks**: View all completed tasks with their completion timestamps.
- **Persistent Storage**: Tasks are saved to and loaded from a `tasks.json` file for persistence between sessions.

## Prerequisites

- Python 3.x installed on your system.
- No external libraries are required as the project uses standard Python modules (`json`, `os`, and `datetime`).

## Installation

1. Clone the repository from GitHub:
   ```bash
   git clone https://github.com/junayedhasansakib0/json-todo-list.git
   ```
2. Navigate to the project directory:
   ```bash
   cd json-todo-list
   ```

## Usage

1. Run the program using Python:
   ```bash
   python todo.py
   ```
2. Follow the on-screen menu to:
   - Add a new task (option 1)
   - View incomplete tasks (option 2)
   - Mark a task as completed (option 3)
   - View completed tasks (option 4)
   - Exit the program (option 5)

### Example Interaction

```
--- Your JSON To-Do List ---
1. Add Task
2. Show Incomplete Tasks
3. Complete Task
4. Show Completed Tasks
5. Exit
Enter your choice: 1
Enter your task: Buy groceries
Priority (High/Medium/Low): High
Task added successfully.
```

### File Structure

- `to_do_list.py`: The main Python script containing the to-do list application logic.
- `tasks.json`: The file where tasks are stored (created automatically when tasks are added).

## How It Works

- Tasks are stored in a JSON file (`tasks.json`) as a list of dictionaries.
- Each task dictionary contains:
  - `task`: The task description (string).
  - `priority`: The task priority (High, Medium, or Low).
  - `status`: The task status (`incomplete` or `completed`).
  - `completed_at`: The timestamp when the task was marked as completed (only for completed tasks).
- The program uses a simple command-line interface with a menu-driven system to interact with the user.

## Contributing

Contributions are welcome! If you'd like to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or suggestions, feel free to open an issue on GitHub or contact the repository owner.
