def series(n):
    primearray = []
    counter = 0
    x = 2
    while counter <= n:
        prime = True

        for i in range(2,x):
            if x % i == 0:
                prime = False
                break
        if prime:
            primearray.append(x)
            counter += 1
        x = x + 1
        result = " ".join(map(str,primearray))
    print(result)

def main():
    n = int(input("Enter a number: "))
    series(n)

main()


