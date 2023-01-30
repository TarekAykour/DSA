def binary(arr,start,end,target):
    while start <= end:
        mid = (start + end ) // 2
        if arr[mid] < target:
            start = mid + 1
        elif arr[mid] > target:
            end = mid -1
        else:
            return mid
    return start



arr = [21,5,7,8,4,9,10,6,56,6]
target = 5

print(binary(arr, 0, len(arr) - 1, target))