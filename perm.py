# swapping two letters


def perm(string, pocket=""):
    if(len(string)) == 0:
        print(pocket)
    else:
        for i in range(len(string)):
            letter = string[i]
            front = string[0:i] #get the value of index of 0
            back = string[i+1:] # get the value of index of i + 1, (so if i is 0 then we get 1) and get val of last index?
            together = front + back
            perm(together, letter+pocket)
            

print(perm("ABC", ""))
    