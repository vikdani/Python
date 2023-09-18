# store prime num in array
def primenum(n):
    arr = []
    #counter = 0
    i = 2
    while i < n:
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            arr.append(i)
                #counter += 1
        i += 1
    return arr
    
    
    
    
    
def main():
    n = int(input("enter upto which u want prime num"))
    output = primenum(n)
    print  (output)
main() 