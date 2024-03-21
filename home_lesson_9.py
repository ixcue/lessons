import random
randomlist = []
for i in range(random.randint(3,10)):
    n = random.randint(0,9)
    randomlist.append(n)
print(randomlist)

lst = [randomlist[0],randomlist[2],randomlist[-2]]
print(lst)