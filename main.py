import cmd
from datetime import datetime




class MyCLI(cmd.Cmd):
    prompt = '-->>> '
    intro = '''
 - Welcome to my task tracker project!! 
 - you can type "add SomeTask" or "list" to see tasks
 - if you just wanna know more just type "help" to see all commands
'''

    def __init__(self):
        super().__init__()
        
        self.tasks = []

        
        

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
            object_json = {line : date_now}
            self.tasks.append(object_json)
            print(f"Task added: {line} and was added in the time : {object_json[line]}")
        else:
            print("No task provided. Usage: add SomeTask")

    def do_list(self, line):
        """List all tasks."""
        if self.tasks:
            print("Tasks:")
            for task in self.tasks:
                print(f" - {task}")
        else:
            print("No tasks found.")
    def do_upadate(self, line):
        "update the task"



if __name__ == '__main__':
    MyCLI().cmdloop()
