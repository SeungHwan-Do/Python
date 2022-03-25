#지난 시간에 괄호 사이에 parameter를 작성할 수 있다고 했다.
def func(x):
    print(x)

def func(x, text):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')
func('Tim','1')

#똑같은 매개변수를 반복적으로 사용하기는 번거로울 것이다.
#default value를 설정할 수 있다.
def func(x, text='2'):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')
        print(text)
func('Tim')
#text의 값을 정하지 않아서 기본값이 대입된다.
func('Tim','67')

def func(x=3, text='2'):
    print(x)
    if text == '1':
        print('Text is 1')
    else:
        print('Text is not 1')
        print(text)
func()
 
