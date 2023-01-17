from dataclasses import dataclass

@dataclass
class Student:
    #Initializes vars without __init__ method
    name: str
    school_id: str
    gpa: float

def main():
    #Creates and prints student object
    student = Student('Me', 'abcd', 4.0)
    print(student)

main()