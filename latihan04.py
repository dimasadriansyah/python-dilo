#function#

def sum_number(x):
	z = 0
	for y in str(x):
		z += int(y)
	if z > 9:
		z = sum_number(z)
	return z
#print(sum_number(1234)) #1 + 2 + 3 + 4

def root_number(num):
	y = 0
	for x in str(num):
		y += int(x)
	if y > 9:
		y = root_number(y)
	return y
#print(root_number(1389))

def repeat_num(num):
	return num if num < 10 else repeat_num(sum(map(int, str(num))))
print(repeat_num(1389))

#class OOP#
class myClass:
	#constructor
	def __init__(self, name, level):
		self.name = name
		self.level = level

	def getName(self):
		return self.name
	def getLevel(self):
		return self.level
def claas():
	pass

claas = myClass('Punchman','1')
className = claas.getName()
classLevel = claas.getLevel()

print(f"class name is {className} and the the level {classLevel}")
print("=====")

def a(kata):
	x = ''
	for i in kata:
		if kata.count(i) > 1:
			x += ')'
		else:
			x += '('
	return x

print(a('hello'))

class calculator:
    def __init__(self, x ,y):
        self.angkapertama = x
        self.angkakedua = y
    
    def getPenjumlahan(x, y):
        return x + y
    
    def getPengurangan(x, y):
        return x - y

    def getPerkalian(x, y):
        return x * y
print(calculator.getPenjumlahan(5,5))
print(calculator.getPengurangan(5,5))
print(calculator.getPerkalian(5,5))
