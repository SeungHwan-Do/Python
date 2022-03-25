#전역 : 말그대로 모든곳
# 지역 : 특정 블록 클래스
var = 9
loop = True

def func(x):
    newVar = 7
    if x == 5:
        return newVar

#print(newVar)
    
#NameError: name 'newVar' is not defined
#newVar은 함수 func안에 선언되었기 때문에 오직 함수 안에서만 접근할 수 있고
#바꿀 수 있고 사용할 수 있다

def otherFunc():
    newVar = 5
    print(newVar)


newVar=23
otherFunc()

def func(x):
    newVar = 7


func(2)
#함수 내에서 전역변수를 변경하는것은 적절하지 않다
#모듈러 프로그래밍을 학습했는데 만약 블록이나 함수 내에서 전역변수를 언급한다면
#다른 파일에서 참조하는데는 문제가 생길것이다.
#사용하고자 하는 프로그램에서 그 변수가 전역변수로 선언되어있지 않다면 동작하지 못할것이다
def func():
    loop = 7
    print(loop )
func()
print(loop)#True출력, 전역변수 변경이 아니라 함수 내의 지역변수가 선언되어
#그 변수의 값이 바뀌는것
#만약 전역변수의 값을 바꾸고 싶다면 루프 내에서 global이라는 키워드를 사용해서
#전역변수를 루프 내에 선언하고 그 값을 다음과 같이 바꿔줘야한다.
def func():
    global loop
    loop = 8
    print(loop )
func()
print(loop)
#8이 출력될것
       
