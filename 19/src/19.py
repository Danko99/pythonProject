# 19. Медвежья память

import itertools
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

for i in combinations:
    print(*i, end=' ', sep='')
