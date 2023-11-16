class Person:
  def __init__(self, age):
    #self.name = name
    self.age = age

  def __str__(self):
    #return f"Name:{self.name}\nAge:{self.age}"
    return f"{self.age}"

#p1 = Person("John", 36)
#p2 = Person('Kevinnn', 21)
p1 = Person(36)
p2 = Person(21)

print(p1)
print(p2)