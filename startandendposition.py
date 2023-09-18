# given sorted array , we have to find the strating and ending position of an target value

start = -1
end = -1

l = 0
h = len(nums) - 1

while (i<=h):
    mid = (l + h)//2
    if nums[mid]==target:
        start = mid
        h = mid - 1
    elif target<nums[mid]:
        h = mid - 1
    else:
        l = mid + 1

while (i<=h):
    mid = (l + h)//2
    if nums[mid]==target:
        end = mid
        l = mid + 1
    elif target<nums[mid]:
        h = mid - 1
    else:
        l = mid + 1

if start==0 and end ==0:
    return [-1,-1]
else:
    return [start,end]
    