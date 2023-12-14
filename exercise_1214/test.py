class Student:
    def __init__(self, name, identify, major):
        self.name = name
        self.identify = identify
        self.major = major
    
    def prinntAll(self):
        print(self.name)
        print(self.identify)
        print(self.major)

class Course(Student):
    def __init__(self, name, identify, major, course):
        super().__init__(name, identify, major)
        self.course = course
    
    def addCourse(self, course, semester):
        self.course = course
        self.semester = semester
        
    def checkCourse(self):
        self.addCourse(self.course, self.semester)
        print(self.course)
        print(self.semester)

obj1 = Student('kevinnn', 'ab1234', 'CSIE')
obj1.prinntAll()

obj2 = Course('kevinnn', 'ab5678', 'CSIE', 'math')
obj2.prinntAll()
print(obj2.course)

obj2.addCourse('physics', 'Spring 2023')
obj2.checkCourse()
