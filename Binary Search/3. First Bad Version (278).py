def firstBadVersion(n):

    low = 0
    high = n

    while low<high:
        mid = (low+high)//2
        if isBadVersion(mid):
            high = mid
        else:
            low = mid +1

    return low    


# Test cases

n_1 = 5
bad_1 = 4

n_2 = 1
bad_2 = 1


print(firstBadVersion(n_1))  # Expected: 4
print(firstBadVersion(n_2))  # Expected: 1