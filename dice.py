import numpy as np
import numpy.random as rnd
import math
# Combination name: point_value [list of dice to keep]+[list of remaining dice]

res = {}
combs = {
    "1" : "Aces",
    "2" : "Twos",
    "3" : "Threes",
    "4" : "Fours",
    "5" : "Fives",
    "6" : "Sixes",
}

throw = rnd.randint(1, 6+1, 5)
print(throw)
for i in range (1,7):
    res[i] = np.count_nonzero(throw == i)

for i in res.keys():
    if res[i] > 0:
        print("%s : %s %s+%s" % (combs[str(i)], i * res[i] , [z for z in throw if z == i] , [z for z in throw if z != i]))
    if res[i] == 3:
        print(("Three of a kind : %s %s+%s" % (np.sum(throw) , [z for z in throw if z == i] , [z for z in throw if z != i])))
    if res[i] == 4:
        print(("Four of a kind : %s %s+%s" % (np.sum(throw) , [z for z in throw if z == i] , [z for z in throw if z != i])))
        
