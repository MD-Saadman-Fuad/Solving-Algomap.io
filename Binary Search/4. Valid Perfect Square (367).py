
def isPerfectSquare(num):
    low = 1
    high = num

    while low <= high:
        mid = (low+high)//2
        if mid*mid==num:
            return True
        elif mid*mid > num:
            high = mid-1
        else: 
            low = mid+1
    return False
    


# --- TEST CASES ---

num_1 = 16
num_2 = 14
num_3 = 1
num_4 = 25
num_5 = 36
num_6 = 100

# --- OUTPUT ---

print(isPerfectSquare(num_1))  # Expected: True
print(isPerfectSquare(num_2))  # Expected: False
print(isPerfectSquare(num_3))  # Expected: True
print(isPerfectSquare(num_4))  # Expected: True
print(isPerfectSquare(num_5))  # Expected: True
print(isPerfectSquare(num_6))  # Expected: True
