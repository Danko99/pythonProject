#18. Евротур
import itertools
combinations=[]
word = input()
stuff = list(word)
for L in range(len(stuff), len(stuff)+1):
    for subset in itertools.permutations(stuff, L):
        combinations.append(subset)
print(combinations)



