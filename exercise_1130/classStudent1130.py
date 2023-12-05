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
    def setschool(self, new_school):
        self.school = new_school

    def getmajor(self):
        return self.major
    def setmajor(self, new_major):
        self.major = new_major

    def getteacher(self):
        return self.teacher
    def setteacher(self, new_teacher):
        self.teacher = new_teacher

    def getname(self):
        return self.name
    def setname(self, new_name):
        self.name = new_name

    def getstudentID(self):
        return self.studentID
    def setstudentID(self, new_studentID):
        self.studentID = new_studentID

    def getaddress(self):
        return self.address
    def setaddress(self, new_address):
        self.address = new_address

    def getcredit(self):
        return self.credit
    def setcredit(self, new_credit):
        self.credit = new_credit

    def getscore(self):
        return self.score
    def setscore(self, new_score):
        self.score = new_score

    def printAll(self):
        print(self.getschool())
        print(self.getmajor())
        print(self.getteacher())
        print(self.getname())
        print(self.getstudentID())
        print(self.getaddress())
        print(self.getcredit())
        print(self.getscore())

kevinnn = Student('STUST', 'CSIE', 'Micheal', 'Kevinnn', '4B0G0112', 'Tainan', '100', '10')

kevinnn.printAll()


