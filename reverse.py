# we have to return reverse of a number

reverse = 0
while n > 0:
    reverse = (reverse * 10) + n % 10
    n = n // 10

return reverse    