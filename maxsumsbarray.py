
def find_maximum_subarray(arr, length):


    maxsum = arr[0]
    cursum = 0
    for i in arr:
        if cursum < 0:
           cursum = 0
        cursum = cursum + i

        maxsum = max(cursum,maxsum)
    return maxsum        

def main():
    n = int(input("enter num"))
    arr=[]
    for i in range(n):
        arr.append(int(input("num")))
    print(find_maximum_subarray(arr, n))
    
main()
    