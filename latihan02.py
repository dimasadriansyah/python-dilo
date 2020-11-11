listname = ["Skywalker","Palme Amadia","Qui-gon", "obi wan"]

#for variable in listname:
	#print(variable)

print(listname[::-1])

number= 1 + 2 + 3 /4.0
print (number)

squared = 11 ** 2
print(squared)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(all_numbers)

#string formating

myString = "Luke Skywalker"
myInt = 12
myFloat = 4.8

#python 2 and > 2
print("My string is %s" % myString)
print("This is integer number %d" % myInt)
print("The string %s and the integer %d" % (myString, myInt))

#reference use index
print("The string is {0} nad the integer is {1}".format(myString, myInt))

#lst = {'name': 'obi-wan', 'role':'jedi master'}

#print(f"Hello {myString}")

String = "John wick"
print(len(String))
print(String.index("o")) #huruf o ke 1
print(String.index("w"))

astring = "Hello World!"
print(astring[::-1])
# huruf kapital dan kecil
print(astring.upper())
print(astring.lower())
# check true and false
print(astring.startswith("Hello"))
print(astring.endswith("asadfddsd"))
afewwords = astring.split(" ")
print(afewwords)

#conditions
x=2
print( x == 2)

name = 'John'
age = "23"

if name == "John" and age == 23:
	print ("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
	print("Your name is either John or Risk.")

# The "in" operator:

y = 3

if y == 6:
	print("benar")
elif y == 3:
	print("benar")
else:
	print("salah")

x = 3
y = 3

print(x == y)
print(x is y)
