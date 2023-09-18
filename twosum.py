# we have to find the sum of two element of array equal to target given and return their index.
dict1 = {}
for i , n in enumerate(nums):
    difference = target - n
    if difference in dict1:
        return [dict1[difference],i]
    dict1[n] = i
return None    