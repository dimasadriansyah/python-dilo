class MyClass:
    variable = "blah"
    def function(self):
        print("this is a message")

myobject = MyClass()

class Hero:
    LEVEL = 1
    def __init__ (self, name, power, skill):
        self.name = name
        self.power = power
        self.skill = skill
    def getName(self):
        return self.name
    def getPower(self):
        return self.power
    def getSkill(self):
        return self.skill
hero = Hero("batman", 888, 27)
name = hero.getName() # object dan property (getName)
power = hero.getPower()
skill = hero.getSkill()
print(name)
#exercise
class Bulan:
    level = ["Januari","Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    def __init__ (self, mounth):
        self.mounth = mounth
    def getMounth(self):
        return self.level[self.mounth - 1]
bulan = Bulan(2)
print(bulan.getMounth())
#exercise 2
class Bulan:
    level = ["Januari","Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
    def __init__ (self, first, second):
        self.first = first
        self.second = second
    def getFirst(self):
        antara = ", ".join(self.level[self.first:self.second -1])
        satu = self.level[self.first - 1]
        dua = self.level[self.second - 1]
        if len(antara) > 0:
            return "Diantara bulan "+ satu +" dan " + dua + " adalah bulan "+ antara
        return "tidak ada bulan diantara " + satu + " dan " + dua
bulan = Bulan(1, 2)
print(bulan.getFirst())