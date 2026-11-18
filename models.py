class Task:
    def __init__(self,task_id,title,category,priority,due_date,is_completed=False):
        self.task_id=task_id
        self.title=title
        self.category=category
        self.priority=priority
        self.due_date=due_date
        self.is_completed=is_completed
    def to_dict(self):
        return{
        "task_id":self.task_id,
        "title":self.title,
        "category":self.category,
        "priority":self.priority,
        "due_date":self.due_date,
        "is_completed":self.is_completed 
        }
    @classmethod
    def from_dict(cls,data):
        return cls(
            task_id=data["task_id"],
            title=data["title"],
            category=data["category"],
            priority=data["priority"],
            due_date=data["due_date"],
            is_completed=data("is_completed",False)

        )
        
        

