# bubble sort
n = len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
return arr            


n = len(arr)
for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if arr[j]>arr[min_index]:
            min_index = j
    arr[i],arr[min_index] = arr[min_index],arr[i]

return arr            