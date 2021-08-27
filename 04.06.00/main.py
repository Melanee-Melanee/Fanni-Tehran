from code_course import *
from code_student import *
def main():
    
    c1 = Course('PRINCIPLE OF COMPUTING', 15110, [])
    s1 = Student('hassan', 100, 'Freshman')
    s2 = Student('ABOLFAZL', 100, 'Freshman')
    s3 = Student('ayda', 102, 'junior')
    c1.addStudent(s1)
    c1.addStudent(s2)
    c1.addStudent(s3)
    c1.prinALllStudents()


main()