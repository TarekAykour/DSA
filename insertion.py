def insert(arr):
    # we dont start at 0, because thats our sorted side
    for i in range(1, len(arr)):
        key = arr[i] #current element
        pointer = i - 1 #pointer (the element to the left of our current element)
        while pointer >= 0 and arr[pointer] > key:  #keep looping as long as the pointer is greater than the index 0 and the value of the pointer greater than the key value
            arr[pointer + 1] = arr[pointer] #reassign pointer to the right position
            pointer -= 1 #mov to the left
        arr[pointer + 1] = key
    return arr

arr = [8,3,2,9,5,1,0]
print(insert(arr))
        