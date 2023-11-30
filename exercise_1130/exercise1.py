class Student:
    def __init__(self, school, major, teacher, name, studentID, address, credit, score):
        self.school = school
        self.major = major
        self.teacher = teacher
        self.name = name
        self.studentID = studentID
        self.address = address
        self.credit = credit
        self.score = score

    def getschool(self):
        return self.school
    def setschool(self):
        return self.school

    def getmajor(self):
        return self.major
    def setmajor(self):
        return self.major

    def getteacher(self):
        return self.teacher
    def setteacher(self):
        return self.teacher

    def getname(self):
        return self.name
    def setname(self):
        return self.name

    def printAll(self):
        print(self.getschool())
        print(self.getmajor())
        print(self.getteacher())
        print(self.getname())

kevinnn = Student('STUST', 'CSIE', 'Micheal', 'Kevinnn', '4B0G0112', 'Tainan', '100', '10')

Student.printAll(kevinnn)
