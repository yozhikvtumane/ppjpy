#!/usr/bin/python3
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
    "smallStraights": [[1,2,3,4], [2,3,4,5],  [3,4,5,6]],
    "largeStraights": [[1,2,3,4,5], [2,3,4,5,6]]
}

def simulateThrow():
    throw = rnd.randint(1, 6+1, 5)

    print("Your current throw of five dices is %s" %throw)

    for i in range (1,7):
        res[i] = np.count_nonzero(throw == i)

    for i in res.keys():
        if res[i] > 0:
            print("%s : %s %s + %s" % (combs[str(i)], i * res[i] , [z for z in throw if z == i] , [z for z in throw if z != i]))

        if res[i] == 3:
            print(("Three of a kind : %s %s + %s" % (np.sum(throw) , [z for z in throw if z == i] , [z for z in throw if z != i])))
            
            for v,k in res.items():
                if k == 2:
                    arr1 = [z for z in throw if z == i]
                    arr2 = [z for z in throw if z == v]
                    print("Fullhouse! : 25  %s + []" % (arr1 + arr2))

        if res[i] == 4:
            print(("Four of a kind : %s %s + %s" % (np.sum(throw) , [z for z in throw if z == i] , [z for z in throw if z != i])))

        if res[i] == 5:
            print("Yahtzee! : 50 %s + []" % throw)
        
    if len(np.unique(throw)) >= 4:
        throwUnique = list(np.unique(throw))[:]
        large = False
        for i in combs["largeStraights"]:
            if throwUnique == i:
                print("Large straight! 40 %s + []" % i)
                large = True
        if large == False:
            combsManipulations = []
            for b in combs["smallStraights"]:
                if "".join(str(i) for i in b) in  "".join(str(i) for i in throwUnique):
                    throwCopy = list(throw)[:]
                    for z in b:
                        throwCopy.remove(z)
                    print("Small straight: 30 %s + %s" % (b, throwCopy))

    print("Chance : %s %s + []" %(np.sum(throw), [z for z in throw]))

for i in range(100):
    simulateThrow()
