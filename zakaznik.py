import json

class Zakaznik:
    def __init__(self, name, surname, money):
        self.jmeno = name
        self.prijmeni = surname
        self.account = money
    
    def addMoney(self, amount):
        self.account += amount

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)


zak1 = Zakaznik("Vasya" , "Pupkeen" , 15000)
zak2 = Zakaznik("Vasya" , "AppleSeed" , 450)
zak3 = Zakaznik("Vasya" , "Hornik" , 99)

zak1.addMoney(99999)

print(zak1.toJSON())
print(zak2.toJSON())
print(zak3.toJSON())

