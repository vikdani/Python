def print_subarray(arr):
    n = len(arr)
    for start in range(n):
        for end in range(start + 1 , n + 1):
            subarray = arr[start:end]
            sub_string = " ".join(map(str,subarray))

            print(sub_string)

arr = [1, 2, 3, 4, 5]
print_subarray(arr)

