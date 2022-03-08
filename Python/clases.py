class Student():
    nombre_1 = 'augusto'
    nombre_2 = 'josue'
    
    def __init__(self):
        # global nombre_1
        # x=self.nombre_1
        None
    
    def get_second_name(self):
        return self.nombre_2
    
clase = Student()

print(clase.nombre_1)

print(clase.get_second_name())
