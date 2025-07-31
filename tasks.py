import datetime
class Task:

    id_count = 1
    def __init__(self, task, category, *args):
        self.task = task
        self.category = str(category)
        self.date_added = datetime.datetime.now().strftime("%d/%m/%Y::%H:%M")
        self.date_due = None
        self.completed = False

        str_count = 0
        manual_id = None

        for arg in args:
            if isinstance(arg, int):
                manual_id = arg
            elif isinstance(arg , str):
                if str_count == 0:
                    self.date_due = arg
                    str_count+=1

                    

        if manual_id is not None:
            self.id = manual_id
        else:
            self.id = Task.id_count
            Task.id_count+=1

    def mark_done(self):
            self.completed = True
 
    def mark_undone(self):
            self.completed = False

    def is_overdue(self):
        try:
            due = datetime.datetime.strptime(self.date_due, "%d/%m/%Y::%H:%M")
            return datetime.datetime.now() > due if not self.completed else False
        except Exception:
            return False
