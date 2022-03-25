#자바를 공부했다면 try-catch 구문을 보았을 것이다.
#python은 catch대신 try-except인데 알아보도록 하겠다.
#동작을 하거나 어떤것을 시도할텐데 실제로 동작하는지 아닌지 당신은 모른다
#어떤 입력을 주는지 어떤 동작을 하는지 따라서 달렸다
text= input('Username: ')
#텍스트만 받거나 숫자만 받도록 설정할 수 있다.
만약 숫자만 받도록 작성한다면
number = int(text)
print(number)
#글자를 입력했을때 에러가 나는것을 볼 수 있다.
try:
    number = int(text)
    print(number)
#시도한다는 뜻
except:
    print('Invalid Username')
