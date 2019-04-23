# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 10:13:44 2019

@author: matvean1
"""
import math, json

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