def func(x = 1):
    return x ** 2

call = func()
print(call)

def func(word, freq = 1):
    print(word*freq)

call = func('Hi', 5)
call = func('Hi')

def func(word, add = 5, freq = 1):
    print(word*(freq+add))
call = func('Hello')
call = func('Hello', 0)
#add는 남겨놓고 freq를 바꾸고 싶을 때
