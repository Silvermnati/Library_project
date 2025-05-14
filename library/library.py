class Librarian(person)
    def __init__(self, name, employee_id):
        super().__init__(name)
        self.employee_id = employee_id

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author        
