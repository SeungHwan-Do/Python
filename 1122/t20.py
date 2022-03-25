x = 'string'
print(type(x))
#사실 우리가 보는 변수 대부분은 object이다. x의 타입을 출력해보면
#class string
y = 23
print(type(y))
# 오브젝트는 특정 속성을 가진다.
# ex String이랑 int형을 더할수는 없듯
#print(y.count('1'))
#AttributeError: 'int' object has no attribute 'count'
print(x.count('1'))
#0
boo = True
#print(boo.count('1'))
#count는 String클래스에 내장된 method이고 우리는 String형 object에 대해 .을
#사용해서 이용할 수 있다
def func():
    print('hello')

func()
#함수와 메소드는 다르다.

#각 자료형은 각자 클래스를 가지고 있다.
class number():
    def __init__(self, num):
        self.var = num
        
    def display(self, x):
        print(x)
#정상 작동하기 위해서는 self 필요!
#y.display(21)
num = number(23)
print(num)
#num을 출력하면 메모리에서 num object의 위치를 표시하게됨
num.display(num.var)
#num.var로 참조가 되는것을 볼 수 있다. number클래스의 var는 클래스의 전역
#변수라는 것을 알 수 있다.
