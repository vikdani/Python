def find_lucky_integer(arr):
    # Step 1: Create a dictionary to store the frequency of each integer
    frequency_dict = {}
    for num in arr:
        frequency_dict[num] = frequency_dict.get(num, 0) + 1

    # Step 2: Find the largest lucky integer
    lucky_integer = -1
    for num, freq in frequency_dict.items():
        if num == freq and num > lucky_integer:
            lucky_integer = num

    return lucky_integer

# Example usage:
arr = [1 , 2 , 2 , 3 , 3 , 3 , 4 , 4 , 4 , 6 , 6 ,6 , 6 , 6 ]
print(find_lucky_integer(arr))       