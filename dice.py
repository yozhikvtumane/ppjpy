# import numpy as np
# import numpy.random as rnd
# import math

# res = {}

# # throw = rnd.randint(1, 6+1, 5)
# throw = np.array([2,2,3,3,2])
# print(throw)
# for i in range (1,7):
#     print(np.count_nonzero(throw == i))
#     res[i] = np.count_nonzero(throw == i)
#     # if res[i]==3:
#     #     if

# for v,k in res.items():
#     if k == 2:
#         res1 = "yes"
#         print('v=',v)

# if res1:
#     print(res1)


# print(res.values())
# throw.sort()
# print(throw)
# print(res)


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

# throw = rnd.randint(1, 6+1, 5)
throw = np.array([2,2,2,3,3])
print("Your current throw of five dices is %s" %throw)
for i in range (1,7):
    print(np.count_nonzero(throw == i))
    res[i] = np.count_nonzero(throw == i)
print(res)
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

print("Chance : %s %s + []" %(np.sum(throw), [z for z in throw]))
        
