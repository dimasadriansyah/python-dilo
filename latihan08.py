#soal 1#
def persegi(p, l):
    return p * l
print(persegi(4, 2))

#soal 2
def pangkat(p):
    return p**2
print(pangkat(2))

#soal 3
def segitiga(x, y):
    return 0.5 * x * y
print(segitiga(8, 3))
print('==========')
num = [1,5,6,2,8]
def of(x):
    p = []
    for i in (x):
        y = i**2
        p.append(y)
    return sum(p) 
print(of(num))
def bebas(number):
    return sum(i**2 for i in number)
print(bebas(num))
#dictionaries#
dic = {}
dic["john"] = 1234
dic["jack"] = 4321
dic["bill"] = 54321

user = [

        {"name" : "john",
        "absen" : "1"},

        {"name" : "luke",
        "absen" : "2"},

        {"name" : "bill",
        "absen" : "3"},
]
for u in user:
    print(u["absen"])
print(dic)
