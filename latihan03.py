for x in range(5):
	print(x)

index = 0
while index < 20:
	if index %3 == 0:
		print(index)
	index += 1 #this is the same as count = count + 1

count =0
while True:
	print(count)
	count += 1
	if count >= 5:
		break

for x in range(10):
	if x % 2 == 0:
		continue
	print(x)

for i in range(1, 10):
	if(i%5==0):
		break
	print(i)
else:
	print("this is not printed")

##exercise 3

##genap
for y in range (2, 11, 2):
	print(y)

##ganjil
for i in range (1, 11, 2):
	print(i)

##function

def penjumlahan (x,y):
	print (x + y)

penjumlahan(2,3)

##return

def tambah (i,l):
	c = i+l
	return c
hasil=tambah(5,5)
print(hasil)

def bilangan (x,y):
	while x < y:
		if x % 3 == 0:
			print(x)
		x += 1

bilangan (1, 20)

