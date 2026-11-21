from models import Task 
from storage import save_tasks,load_tasks 
class TaskManager:
    def __init__(self,filename="tasks.json"):
        self.filename=filename
        self.tasks=load_tasks(self.filename)
    def add_task(self ,title , category, priority, due_date):
        if not self.tasks:
            task_id=1
        else:
            task_id = len(self.tasks) + 1

        new_task = Task(task_id, title, category, priority, due_date)
        self.tasks.append(new_task)
        save_tasks(self.tasks, self.filename)
        return new_task
    def get_all_tasks(self):
        return self.tasks
    def complete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                task.is_completed = True
                save_tasks(self.tasks, self.filename)
                return True
        return False
    def delete_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                self.tasks.remove(task)
                save_tasks(self.tasks, self.filename)
                return True
        return False
            





