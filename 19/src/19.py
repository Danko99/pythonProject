# 19. Медвежья память

import itertools
def check(arr):
    i=0
    while i<len(arr)-1:

        if arr[i]==arr[i+1]:
            return True
        else:
            return False
    i+=1

combinations = []
quantity = int(input())
word = input()
stuff = list(word)

if len(word) != quantity:
    combinations = itertools.product(word,repeat=quantity)
else:
    for L in range(len(stuff), len(stuff) + 1):
        for subset in itertools.permutations(stuff, L):
            combinations.append(subset)

i=0
combinations=list(combinations)
while i<len(combinations):
    if check(combinations[i]):
        combinations.remove(combinations[i])
    i += 1


for i in combinations:
    print(*i, end=' ', sep='')
