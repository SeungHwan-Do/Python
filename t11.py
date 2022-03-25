fruits = ['apples', 'pear', 'strawberrys']
text = "Hello I like Python"

print(fruits[1])
print(text[11])

#print(text[start:stop:step])
print(text[:])
#range와 동일한 형태
print(text[0:4])
print(text[2:])
print(text[::2])

print(fruits[1:])

#append만들기
a = "added"
fruits[3:3] = a
print(fruits)
