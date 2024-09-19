import cmd
from datetime import datetime
import json
import os

class Task():
    def __init__(self, line, datetime):
        self.line = line
        self.datetime = datetime

    def to_dict(self):
        return {
            "line": self.line,
            "datetime": self.datetime.isoformat()  # Store datetime in ISO format
        }
    
    @staticmethod
    def load_tasks(filename):
        if not os.path.exists(filename):
            return []
        with open(filename, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []  # Return an empty list if the JSON is invalid

class MyCLI(cmd.Cmd):
    prompt = '-->>> '
    intro = '''
 - Welcome to my task tracker project!! 
 - You can type "add SomeTask" or "list" to see tasks.
 - If you just wanna know more, type "help" to see all commands.
'''

    def __init__(self):
        super().__init__()
        self.filename = 'tasks.json'
        self.tasks = Task.load_tasks(self.filename)

    def do_hello(self, line):
        """Print a greeting."""
        print("Hello, World!")

    def do_quit(self, line):
        """Exit the CLI."""
        return True

    def do_add(self, line):
        """Add a task."""
        if line:
            date_now = datetime.now()
            task = Task(line, date_now)
            self.tasks.append(task.to_dict())
            self.save_tasks()
            print(f"Added task: {line}")
        else:
            print("No task provided. Usage: add SomeTask")

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def do_list(self, line):
        """List all tasks."""
        if not self.tasks:
            print("No tasks available.")
            return
        
        for idx, task in enumerate(self.tasks):
            print(f"{idx + 1}: {task['line']} (Added on: {task['datetime']})")

    def do_remove(self, line):
        """Remove a task by number."""
        if line.isdigit() and 0 < int(line) <= len(self.tasks):
            removed_task = self.tasks.pop(int(line) - 1)
            self.save_tasks()
            print(f"Removed task: {removed_task['line']}")
        else:
            print("Invalid task number.")

if __name__ == '__main__':
    MyCLI().cmdloop()
