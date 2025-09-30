class Employee:
    
    #initialization_function
    def __init__(self ,name ,age ,department ,is_manager)
        self.name = name
        self.age = age
        self.department = department
        self.is_manager = is_manager
   
    def print_info(self):
        print(self.name ,self.age ,self.department ,self.ismanager)
    