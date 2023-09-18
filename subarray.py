def print_subarray(arr, length):
    """Function to print all the subarrays given in an array
    Input arr--> array, length -->length of an array """
    
    
   
    for i in range(0,len(arr)):
        for j in range(i,len(arr)):
            str1=""
            for k in range(i,j+1):
                str1=str1+str(arr[k])
            print(str1)
    
    
    
    
    
    
    
    
    """Dont change anything below. If changed click on reset."""
def main():
    n = int(input("enter size"))
    arr=[]
    for i in range(n):
        arr.append(int(input("enter element")))
    print_subarray(arr, n)
    
main()