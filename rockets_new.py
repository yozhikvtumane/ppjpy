# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 09:54:08 2019

@author: matvean1
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 10:06:35 2019

@author: hornito1
"""
import json, math, random
### CLASSES ###
"""
If you enjoy working with math, you could implement a safety_check() method. 
This method would take in another rocket object, and call the get_distance() 
method on that rocket. Then it would check if that rocket is too close, and 
print a warning message if the rocket is too close. If there is zero distance 
between the two rockets, your method could print a message such as, 
"The rockets have crashed!" (Be careful; getting a zero distance 
could mean that you accidentally found the distance between a rocket and 
itself, rather than a second rocket.)
"""


class Rocket():
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def move_up(self, x_increment=1, y_increment=1):
        self.x = self.x + x_increment
        self.y = self.y + y_increment

    def land_rocket(self):
            self.y = 0
            print("Safely landed on position %d" % self.x)
            
    def get_distance(self, other_rocket):
        distance = math.sqrt((self.x - other_rocket.x)**2 + (self.y - 
                             other_rocket.y)**2)
        return distance
    
    def safety_check(self, other_rocket):
        distance = self.get_distance(other_rocket)
        if distance < 20:
            print('Warning!!! The rockets are too close to each other!!!')
        else:
            print('The distance is safe!')
        
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=False, indent=4)

#INHERITANCE

class SpaceShuttle(Rocket):
    def __init__(self, x=0, y=0, flights_completed=0):
        super().__init__(x,y)
        self.flights_completed = flights_completed

        
### GENERATION OF OBJECTS ###
        
my_rockets = []

for x in range(0, 3):
    x = random.randint(0, 100)
    y = random.randint(1, 9999)
#    flights = random.randint(0, 11)
    my_rockets.append(Rocket(x, y))
    
for rocket in my_rockets:
    print("Raketa se nachazi na poz x = %d a y = %d" % (rocket.x, rocket.y))

my_shuttles = []

for x in range(0, 3):
    x = random.randint(0, 100)
    y = random.randint(1, 9999)
    flights = random.randint(0, 11)
    my_shuttles.append(SpaceShuttle(x, y, flights))

for shuttle in my_shuttles:
    print("Raketa se nachazi na poz x = %d a y = %d , cislo letu %d" % (shuttle.x, shuttle.y, shuttle.flights_completed))



my_rockets[1].move_up()

for rocket in my_rockets:
    print("Nadmořská výška: " + str(rocket.y))
    
first_shuttle = my_shuttles[0]

for index, shuttle in enumerate(my_shuttles):
    distance = first_shuttle.get_distance(shuttle)
    print(distance)
    

#my_rockets[1].move_up(1)    
#distance = my_rockets[1].get_distance(my_rockets[0])
#print("Vzdal rok c.2 od rokety c.1 je %d bodu" % distance)
#
#my_rockets[0].safety_check(my_rockets[1])
#my_rockets[0].land_rocket()
#
#shuttle = SpaceShuttle(30, 0 , 3)
#shuttle.move_up(50, 1000)
#print(shuttle.toJSON())
#
#my_rockets.append(Rocket(55, 0))
#my_rockets.append(Rocket(70, 0))
#my_rockets.append(Rocket(22, 0))




