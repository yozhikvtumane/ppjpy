import pprint, json

class Rocket:
    
    def __init__(self, x=0, y=0):
        self.id = 
        self.x = x
        self.y = y
        
    def move_up(self, y_increment=1):
        self.y += y_increment
    
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
                          sort_keys=False, indent=4)
    
#zakaznik mel genericke jmeno, penez, metoda pro pridani penez
#myRocket = Rocket()
#print(myRocket)
#
#print('Prvni raketa: ')
#print("nadmprska vyska:" + str(myRocket.y))
#myRocket.move_up()
#print("nadmprska vyska:" + str(myRocket.y))
#
#second_rocket = Rocket()
#print(second_rocket)

my_rockets = []
my_rockets.append(Rocket(50,0))
my_rockets.append(Rocket(110,0))
my_rockets.append(Rocket(280,0))

print(my_rockets[0].toJSON())
#
#for x in range(0, 5):
#    new_rocket = Rocket()
#    my_rockets.append(new_rocket)
#
#for rocket in my_rockets:
#    print(rocket)
#
#my_rockets[1].move_up()
#pprint.pprint(my_rockets[1])
##
#for rocket in my_rockets:
#    print(rocket)
