class Student:
    def __init__(self, saxeli, gvari, asaki):
        self.saxeli = saxeli
        self.gvari = gvari
        self.asaki = asaki
    def get_info(self):
        print(f"saxeli: {self.saxeli}")

class School:
    def __init__(self, skolis_saxeli, skolis_misamarti):
        self.skolis_saxeli = skolis_saxeli
        self.skolis_misamarti = skolis_misamarti
        self.students = []
    def add_student(self, student):
        self.students.append(student)
    def remove_student(self, index):
        self.students.pop(index - 1)
    def show_students(self):
        for student in self.students:
            student.get_info()

school = School("126 sajaro skola", "vaja-fshavelas 71")
student_1 = Student("demetre","saxltxucishvili", 14)
student_2 = Student("giorgi", "mesxivili", 16)
student_3 = Student("dachi", "wkadua", 16)
student_4 = Student("jasurbek", "iaxshiboevi", 28)

school.add_student(student_1)
school.add_student(student_2)
school.add_student(student_3)




school.show_students()