x = 279
for i in str(x):
    print(i)

class siswa:
    def __init__ (self, nama, umur):
        self.nama = nama
        self.umur = umur

    def getUmur(self):
        return self.umur
obj = ("john", 24)
print(obj)

def number(num):
    x = ''
    for i in str(num):
        x += str(int(i)**2)
    return int(x)

print(number(248))

