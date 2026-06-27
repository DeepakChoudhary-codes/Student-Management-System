class Student:
    def __init__(self,roll_no,name,marks):
        
        self.roll_no = roll_no
        self.name = name
        self.marks = marks
        
    def calc_grade(self):
        if (self.marks >= 90):
            self.grade = "A"
        elif (self.marks >= 80 and self.marks < 90):
            self.grade = "B"
        elif (self.marks >= 70 and self.marks < 80):
            self.grade = "C"
        elif (self.marks >= 60 and self.marks < 70):
            self.grade = "D"
        else:
            self.grade = "Fail!!!"

    def display(self):
        self.calc_grade()
        print("---Student Record---")
        print("Name :",self.name)
        print("Roll number :",self.roll_no)
        print("Marks :",self.marks)
        print("Grade :",self.grade)

    def __str__(self):
        return f"{self.roll_no} | {self.name} | {self.marks}"

class StudentManager():
    
    def __init__(self,students = None):
        if students == None:
            self.students = []
        else:
            self.students = students

    def add_student(self):
        name = input("enter new student name :")
        roll_no = int(input("enter new student roll number :"))
        marks = float(input("enter new student marks :"))
        new_student = Student(roll_no,name,marks)
        self.students.append(new_student)  
        self.save_to_file()

    def view_students(self):
        for s in self.students:
            s.display() 

    def find_student(self):
        
        find = int(input("enter roll number to find student : "))
        for stu in self.students:
            if (stu.roll_no == find):
                print("---Student found!!!---")
                stu.display()
                break
        else:
            print("---Student not found!!!---")

    def update_student(self):
        search = int(input("enter roll number : "))
        updated = False
        for stu in self.students:
            if(stu.roll_no == search):
                print("---Student Found---")
                update = input("enter which value to update (name/marks) : ")
                if update == "name":
                    stu.name = input("enter new name : ")
                    print("--Updated Successfully--")
                    stu.display()
                    updated = True
                    break        
                elif update == "marks":
                    stu.marks = float(input("enter new marks : "))
                    print("--Updated Successfully--")
                    stu.display()
                    updated = True
                    break
        if(updated == True):
            self.save_to_file()
        else:
            print("---Student not found!!!---")

    def delete_student(self):
        search = int(input("enter roll number : "))
        for stu in self.students:
            if(stu.roll_no == search):
                print("---Student Found---")
                self.students.remove(stu)
                print("---Student Deleted---")
                self.save_to_file()
                break
        else:
            print("---Student not found!!!---")

    def save_to_file(self):
        with open("students.txt","w") as f:
            for stu in self.students:
                f.write(str(stu) + "\n")

    def load_from_file(self):
        try:
            with open("students.txt","r") as f:
                for line in f :
                    line = line.strip()
                    parts = line.split("|")
                    roll_no = int(parts[0].strip())
                    name = parts[1].strip()
                    marks = float(parts[2].strip())
                    st = Student(roll_no,name,marks)
                    self.students.append(st)
        except FileNotFoundError:
            pass

sm = StudentManager()
sm.load_from_file()
try:
    while True:
        op = input("Enter operation to perform on data (add,view,find,update,delete,save) : ")
        if op == "add":
            sm.add_student()
        elif op == "view" :
            sm.view_students()     
        elif op == "find" :
            sm.find_student()     
        elif op == "update" :
            sm.update_student()  
        elif op == "delete" :
            sm.delete_student()  
        elif op == "save" :
            sm.save_to_file()  
        else:
            raise ValueError   
        if input("continue (y/n) ?") != "y" : break
except ValueError:
    print("Enter valid value!!!")