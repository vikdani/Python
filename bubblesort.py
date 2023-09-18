# Bubble sort
n = len(arr)
for i in range(n):
    for j in range(n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]
    


# selection sort
def sort_array(arr, length):

    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if arr[j]>arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]        

    return arr    
def main():
    n=int(input("enter num"))
    arr=[]
    for i in range(0,n):
        arr.append(int(input("enter num")))
    output = sort_array(arr,n)
    for i in range(0,n):
        print(output[i])
    
main()


# Insertion sort
n = len(arr)
for i in range(n):
    key = arr[i]
    j = i - 1
    while j>=0 and arr[j]>key:
        arr[j + 1] =  arr[j]
        j = j - 1
    arr[j+1] = key    


