#20. Истина в вине
money = int(input())
count = int(input())

arr = [input().split() for i in range(0, count)]
priceArr = []
canBuy = True
for i in arr:
    i[1] = float(i[1])
    i[2] = float(i[2])
    priceArr.append(i[1] / i[2])

minPriceIndex = arr.index(arr[priceArr.index(min(priceArr))])
print(arr[minPriceIndex][0], end=" ")
temp = 0
bollleCount = 0
while temp <= money - arr[minPriceIndex][1]:
    temp += arr[minPriceIndex][1]
    bollleCount += 1
print(bollleCount)
print(bollleCount * arr[minPriceIndex][2])
print(money - temp)
