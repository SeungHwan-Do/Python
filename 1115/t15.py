#python에만 한정되는 find()메소드
string = 'hello'
print(string.find('l'))

print(string.count('l'))

if string.count('_') > 0:
    print('Not good!')
