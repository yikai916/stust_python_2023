class person:
    def __init__(self):
        self.name = 'Kevinnn'
        self.gender = 'male'
        self.age =21

    def talk(self):
        print("I'm",self.name)

    def vote(self):
        if self.age > 18:
            print('You can vote')
        else:
            print('You can not vote')


obj = person()
person.talk(obj)
person.vote(obj)
obj.talk()
obj.vote()