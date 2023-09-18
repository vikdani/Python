def subarray(arr,lenght):
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            str1 = ""
            for k in range(i,j+1):
                str1 = str1 + str(arr[k])
            print( str1  )      

def main():
    arr = []
    n = int(input("enter size of array"))
    for i in range (n):
        arr.append(int(input("enter element")))
    subarray(arr,n)
       
main()