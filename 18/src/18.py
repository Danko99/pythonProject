# 18. Евротур
word = 'halloklempnerdasistfantastischfluggegecheimen'
words = list(word)
words_dict = {}
for i in words:
    words_dict[i] = words.count(i) / len(words)
probability = []
stopWord = input()
sum = 1
for i in stopWord:
    if words_dict.keys().__contains__(i):
        sum *= words_dict[i]
    else:
        sum = 0

print(sum)
