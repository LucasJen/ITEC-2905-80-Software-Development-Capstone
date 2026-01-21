from dataclasses import dataclass

@dataclass
class Student:
    name: str
    id: str
    gpa: float

    def __str__(self):
        return f'Student name: {self.name}, Student id: {self.id}, Student gpa: {self.gpa}'
    
def main():

    lucas = Student('Lucas', 'wr7695789', 3.9)
    print(lucas)
    print(lucas.name)
    print(lucas.id)
    print(lucas.gpa)
    
main()