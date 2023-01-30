def search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        
        
arr = [2,5,8,1,9,10,3]
target = 10


print(search(arr,target))