
def maxsumsub(arr,lenght):
    maxsum = arr[0]
    cursum = 0
    for i in arr:
        if cursum<0:
            cursum = 0
        cursum = cursum + i
        maxsum = max(cursum,maxsum)
    return maxsum         

def main():
    n = int(input("enter the size of array"))
    arr = []
    for i in range(n):
        arr.append(int(input("enter element")))
    total = maxsumsub(arr,n)
    print(total)        
main()    




