X = 2
y = 3
x == y # False

if x == y and x + y == 5 :
    print('ran')
if y == 3 and x + y == 5 :
    print('ran')

if y == x or x + y == 5 :
    print('ran')
else :
    print( ':(')
if not(x == y and x + y == 5) :
    print('ran')

if x == 2 :
    if y == 3:
        print( 'x = 2, y = 3 ')
               #if 중첩 가능
    else :
        print( ' x =2, y != 3')
else :
    print('x !=2')
