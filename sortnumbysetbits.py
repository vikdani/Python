# we have to sort number by count of 1 s in according their binary representation

def sortByBits(arr):
    def count_ones(num):
        count = 0
        while num>0:
            count = count + (num & 1)
            num>>=1
        return count
    arr.sort(key=lambda x:(count_ones(x),x))
    return arr