if condition == True: 동작 조건을 작성한다. 조건이 True면 동작한다.
    do this

age = input('Input your age: ')
if int(age) >= 16:
    print('hey youre older than 16')
else :
    print('hey youre younger than 16')


height = input()

if int(height) < 1:
    print('you cannot right, under 1m')
elif int(height) > 2:
    print('you cannot ride, over 2m')
elif int(height) == 5:
    print('wow youre tall)
else:
    print('you can ride')
    0-63 사이 정수를 입력받아서 반복문을 사용하지 않고 2진수로 출력하기 ex 50 입력 -> 110010
<br>0-63 이외의 입력에 대한 고려는 생략해도 좋음
