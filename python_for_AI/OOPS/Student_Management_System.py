# attendance in %
import logging
# Set up logging to a file and console
logging.basicConfig(filename='student_marks.log', level=logging.ERROR, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

class Student:
    # class variables - becoz this can be shared overall the class and will be common
    university = "SJSU"
    total_students = 10
    passing_grade = 65      # totalt assume as 100

    # instance variables
    def __init__(self, name, student_id, age, department, attendance):
        self.__name = name
        self.__student_id = student_id
        self.__age = age
        self.department = department
        self.marks = []
        self.attendance = attendance
    
    def get_age(self):
        return self.__age
    
    def get_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    # METHODS

    # __str__ -- to display student information when requrested
    def __str__(self):
        list_grades = ", ".join(str(grade) for grade in self.marks)
        return f"Information of student\nName: {self.get_name()}\nID: {self.get_id()}\nAge: {self.get_age()}\nDepartment: {self.department}\nMarks: [{list_grades}]\nAttendance: {self.attendance}"

    def __repr__(self):
        return f"Student(Name: '{self.get_name()}' ID: {self.get_id()} Age: {self.get_age()} Department: '{self.department}' Attendance: {self.attendance})"
    
    # add/update marks
    def add_marks(self, student_mark):
        try:
            # marks can be float
            mark = float(student_mark)

            if not (0<= mark <= 100):
                raise ValueError(f"Mark {mark} is out of the valid 0-100 range.")
            self.marks.append(mark)
            print(f"Successfully added mark: {mark}")
        
        except ValueError as e:
            logging.error(f"Validation Error for Student {self.get_id()}: {str(e)}")
            print(f"Invalid mark: {str(e)}")

        except Exception as e:
            # log any other error
            logging.critical(f"Unexpected error adding mark for Student {self.get_id()}: {str(e)}")
            print("An unexpected system error occurred.")


    def pass_fail(self):
        try:
            avg_marks = sum(self.marks)/len(self.marks)
            if(avg_marks > Student.passing_grade):
                print(f"Student {self.get_id()} with average marks {avg_marks}: Status is PASS")
            else:
                print(f"Student {self.get_id()} with average marks {avg_marks}: Status is FAIL")
        except ZeroDivisionError as e:
            logging.exception("Fail to add Marks list is empty")
            print("Marks list is empty, cannot calculate average- Check Error logs")


class Scholarship(Student):
    # attributes 
    def __init__(self, name, student_id, age, department, attendance, scholarship_amount, thesis_topic, plagiarism_score):
        super().__init__(name, student_id, age, department, attendance)
        self.scholarship_amount = scholarship_amount
        self.thesis_topic = thesis_topic
        self.plagiarism_score = plagiarism_score

    def pass_fail(self):
        try:
            avg_marks = sum(self.marks)/len(self.marks)
            if(avg_marks > 70 and self.plagiarism_score < 10 ):
                print(f"Student {self.get_id()} with SCHOLARSHIP: Status is PASS")
            else:
                print(f"Student {self.get_id()} with SCHOLARSHIP: Status is FAIL , Reason plagiarism score > 10")

        except ZeroDivisionError as e:
            logging.exception("Fail to add maa as Marks list is empty")
            print("Marks list is empty, cannot calculate average- Check Error logs")

    def __str__(self):
            list_grades = ", ".join(str(grade) for grade in self.marks)
            return f"Information of Scholarship student\nName: {self.get_name()}\nID: {self.get_id()}\nAge: {self.get_age()}\nDepartment: {self.department}\nMarks: [{list_grades}]\nAttendance: {self.attendance}\nScholarship amount: {self.scholarship_amount}\nThesis topic: {self.thesis_topic}"

class Graduate(Student):
    # attributes
    def __init__(self, name, student_id, age, department, attendance, research_credits, internship_status):
        super().__init__(name, student_id, age, department, attendance)
        self.research_credits = research_credits
        self.internship_status = internship_status


    def pass_fail(self):
        try:
            avg_marks = sum(self.marks)/len(self.marks)
            if(avg_marks > 70 and self.research_credits > 10 ):
                print(f"Student {self.get_id()} : Status is PASS")
            else:
                print(f"Student {self.get_id()}: Status is FAIL, Reason - Research credits < 10 or marks less than average")

        except ZeroDivisionError as e:
            logging.exception("Fail to add as Marks list is empty")
            print("Marks list is empty, cannot calculate average- Check Error logs")

    def internshipstatus(self):
        if(self.internship_status == "yes"):
            print(f"Student {self.get_name()} has an Internship")
        else:
            print(f"Student {self.get_name()} dose not have an Internship")

    def __str__(self):
                list_grades = ", ".join(str(grade) for grade in self.marks)
                return f"Information of Scholarship student\nName: {self.get_name()}\nID: {self.get_id()}\nAge: {self.get_age()}\nDepartment: {self.department}\nMarks: [{list_grades}]\nAttendance: {self.attendance}\nResearch credits: {self.research_credits}\nIntersnhip status: {self.internship_status}"

# 4 undergradute students
student1 = Student("Alice Johnson", 101, 20, "Computer Science", 92)
student2 = Student("Brian Smith", 102, 21, "Mechanical Engineering", 88)
student3 = Student("Catherine Lee", 103, 19, "Electrical Engineering", 95)
student4 = Student("David Brown", 104, 22, "Civil Engineering", 81)


# 3 Scholarship students
student5 = Scholarship("Emma Wilson", 105, 20, "Information Technology", 90, 100000, "Fire alarm detection", 5)
student6 = Scholarship("David Chen", 106, 22, "Computer Science", 85, 75000, "AI-based medical diagnosis", 12)
student7 = Scholarship("Aisha Khan", 107, 21, "Data Science", 92, 120000, "Stock market prediction using ML", 3)

# 3 grauate students
student8 = Graduate("Henry Davis", 108, 20, "Artificial Intelligence", 85, 6, "Yes")
student9 = Graduate("Isabella Moore", 109, 19, "Cyber Security", 93, 12, "No")
student10 = Graduate("Jack Anderson", 110, 22, "Software Engineering", 89, 17, "Yes")

 
# add marks of 1 undergradute student

# student1.add_marks(70)
# student1.add_marks(90)
# student1.add_marks(90)
# #print(repr(student1))
# print(student1)
# student1.pass_fail()

# 1 scholarship student
# student6.add_marks(90)
# student6.add_marks(80)
# student6.add_marks(89)
# print(student6)
# student6.pass_fail()

# 1 graduate student
# student9.add_marks(90)
# student9.add_marks(80)
# student9.add_marks(89)

# print(student9)
# student9.pass_fail()