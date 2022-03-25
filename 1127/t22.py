class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(a):
        return a.population

    @staticmethod
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, 'years old')


newPerson = person('tim', 18)
#class method : 어떤 객체에서든 호출할 수 있다.
print(person.getPopulation())
#50이 출력되는것을 볼 수 있는데 클래스를 직접 참조해서 메소드를 사용할 수 있

#class methods는 최소 하나의 parameter가 필요하다 바로 self
print(person.display(newPerson))
print(newPerson.display())
print(newPerson.getPopulation())
print(person.display())
