def addTwo(x):
    return x+2
#parameter
def subtract2(number):
    return number - 2

 #argument
#call statement
newNumber = addTwo(7)
print(newNumber)
newNumber = subtract2(7)
print(newNumber)

def printString(string):
    return print(string)
printString("hello")

#특정 동작을 여러번 반복할때 유용하게 사용 가능
def accel(mass, force):
    a = force/mass
    return a

def doSomething():
    print('hi')
    
