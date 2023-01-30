def binary_recur(arr,target):
    start = arr[0]
    end = arr[-1]
    mid = start + end //2 
    if end >= start:
        if arr[mid] < target:
            binary_recur(arr, mid + 1, end, target)
        elif arr[mid] > target:
            binary_recur(arr,start, mid-1, target)
        else:
            return mid
    else: 
        return -1 
    

print(binary_recur([3,456,6,7,1,5],3))    