#27. TOP — 5 минимальных
n = int(input())
n_= map(int, input().split())
array=list(n_)
temp_array=[]
i=0
while i < len(array):
    j=0
    temp_array.append(array[i])
    temp_array.sort(reverse=True)
    while j<len(temp_array):
        if len(temp_array) > 5:
            temp_array.remove(temp_array[j])
        j+=1
    i+=1
    print(*temp_array, sep=" ")











