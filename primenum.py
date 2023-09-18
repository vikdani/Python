def is_prime(num):
    if num<2:
        return False
    for i in range(2,num):
        if num % i == 0 :
            return False
    return True
def first_n_prine(n):
    prime_num = []
    num  = 2
    while len(prime_num) < n :
        if is_prime(num):
            prime_num.append(num)
        num = num + 1
    return prime_num


n = 15

result = first_n_prine(n)
print(result)


