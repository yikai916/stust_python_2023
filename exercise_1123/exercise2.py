class person:
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age

    def talk(self):
        print("I'm",self.name)

    def vote(self):
        if self.age >= 18:
            print('You can vote')
        else:
            print('You can not vote')


person1 = person('Kevinnn','male',21)
person2 = person('Pretty','female',16)
person1.talk()
person1.vote()
person2.talk()
person2.vote()