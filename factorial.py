def iterative(n):
    # check if n is 1, if it is return it
    if n ==1:
        return n
    else:
        temp = iterative(n-1)  #subtract n by one, so we'll eventually get to one
        temp = temp * n 
    return temp


print(iterative(5))
            