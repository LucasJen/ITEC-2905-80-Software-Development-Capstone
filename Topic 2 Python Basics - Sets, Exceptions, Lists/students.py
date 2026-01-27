from dataclasses import dataclass

@dataclass
class Student:
    name: str
    school_id: str
    gpa: float

#
    # def __str__(self):
    #     return f'Name {self.name}, GPA: {self.gpa}'
    
#The dataclass will generate the __init__ and __str__ automatically. the string method can be overwriten
def main(): # Method definition, must be called to be used.
    alex = Student('Alex', 'mctc', 3.5)
    print(alex.name)
    print(alex.school_id)
    print(alex)

    sam = Student('Sam', 'AMTADGSD', 3.9)

    print(sam)

if __name__ == '__main__':
    main()