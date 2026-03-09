#add tasks, set deadlines, assign priority, and filter by project or tag
class ToDo:
    def __init__(self, task, deadline, priority, project=None, tag=None):
        self.task = task
        self.deadline = deadline
        self.priority = priority
        self.project = project
        self.tag = tag
        
    def display(self):
        print("task:", self.task)
        print("Deadline:", self.deadline)
        print("Priority:", self.priority)
        print("Project:", self.project)
        print("Tag:", self.tag)
        
tasks = []

task = input("Enter your task:")
deadline = input("Enter your deadline:")
priority = input("Enter your priority (High/Medium/Low):")
project = input("Enter your project:")
tag = input("Enter your tag:")

obj = ToDo(task, deadline, priority, project, tag)
tasks.append(obj)
print("\nTask Added Successfully")

filter_project = input("Enter project name to filter: ")
print("\nFiltered by Project:")
for t in tasks:
    if t.project == filter_project:
        t.display()

filter_tag = input("Enter tag to filter: ")
print("\nFiltered by Tag:")
for t in tasks:
    if t.tag == filter_tag:
        t.display()