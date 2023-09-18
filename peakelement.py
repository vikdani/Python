start = -1
end = -1

l = 0
h = len(arr)-1

while i<=h:
    mid = (l+h)//2
    if target ==nums[mid]:
        start = mid
        h = mid - 1
    elif target<mid:
        h =  mid - 1
    else:
        l = mid + 1


while i<=h:
    mid = (l+h)//2
    if target ==nums[mid]:
        end = mid
        l = mid + 1
    elif target<mid:
        h =  mid - 1
    else:
        l = mid + 1

if start==0  and end==0:
    return [-1,-1]
else:
    return[start,end]
