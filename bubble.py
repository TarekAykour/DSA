def bubble(arr):
    curr = 0
    # loop through arr from left to right
    for i in range(len(arr)):
        # reverse loop
        for j in range(len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],  arr[j]
    return arr
            
            
arr = [8,6,7,0,1,5,3,4,2,9]
print(bubble(arr))
            
        