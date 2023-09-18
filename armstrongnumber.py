def armstrong(n):
    temp = n
    count = 0
    while temp>0:
        count = count + 1
        temp =  temp//10


    sum = 0
    temp = n
    while temp>0:
        rem = temp % 10
        sum = sum + pow(rem , count)
        temp = temp // 10

    if sum == n:
        print ("True")
    else:
        print ("False")
            
def main():
    n = int(input("enter number to check armstrong number"))
    armstrong(n)
main()    