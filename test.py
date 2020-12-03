# 1
string = "String"
numbers = 1,2,3

print(string)
print(numbers)

# 2
variable01 = "hai"
if variable01 == "hai":
    print("String: %s" % variable01)

# 3
list_ = [1,2,3,4,5,6,7,8,9,10]
print(list_)

# 4
number = 5 + 2 * 4 / 3.0
print(number)

modulo = 19 % 3
print(modulo)

cube = 2 ** 3
print(cube)

ell = "Hai" * 5
print(ell)

list01 = [1,3,5]
list02 = [2,4,6]
allnum = list01 + list02
print(allnum)

print([1,2,3] * 3)

# 5
firstname = "Luke"
lastname = "Skywalker"
print(f"{firstname} {lastname}!")

name = "Quie-Gon Jinn"
role = "Jedi Master"
print(f"{name} is {role}")

# 6
str01 = "John Doe is a anonymous person"
print(len(str01))
print(str01.index("o"))
print(str01.index("y"))
print(str01[3:7])
print(str01[::-1])

# 7
x = 2
print(x == 2)
print(x == 3)
print(x < 3)

# 8
name = "Kenobi"
age = 35
if name == "Kenobi" and age == 35:
	print ("Your name is Kenobi, and you are also 35 year old.")

if name == "Kenobi" or name == "Yoda":
	print("Your name is either Kenobi or Yoda.")

# 9
name = "Anakin"
theList = ['Qui-gon','Luke', 'Anakin']
if name in theList:
    print(name)

# 10
x = [1, 3, 5]
y = x
z = [2, 4, 6]
print(x == y)
print(x is z)
print(y != z)
print(x == z)
print(x is y)
print(not False)
print(not False == False)

# 11
list01 = [1,3,4,5,6,7,7,8,8,9,10,11,12,13,14,15,16,17,18,19,20,21]
for x in list01:
    if x % 3 == 0:
	    print(x)
    else:
        pass

# 12
for x in range(0, 8):
    print(x)
for y in range(33,36):
    print(y)
for h in range(53, 58, 2):
    print(h)

# 13

index = 0
while True:
    print(index)
    index += 1
    if index == 5:
        break

number = 0
while number < 10:
    number += 1
    if number % 2 == 0:
        continue
    print(number)

# 14
def hero(name, level):
    pass