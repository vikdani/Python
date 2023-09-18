arr.sort()
n = len(arr) + 1
sum1 = 0
while n>0:
    sum1 = sum1 + n
    n = n-1
sum2 = sum(arr)
return sum1-sum2    