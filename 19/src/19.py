# 19. Медвежья память
import itertools
from itertools import chain
combinations = []
quantity = int(input())
word = input()
stuff = list(word)
if len(word) != quantity:
    i = 0
    while i < quantity - len(word):
        stuff.append(word[i])
        i += 1

for L in range(len(stuff), len(stuff) + 1):
    for subset in itertools.permutations(stuff, L):
        combinations.append(subset)

#print(*(i for j in combinations for i in j))
#print (''.join([str(i) if isinstance(i,int) else i for tup in combinations for i in tup]))
