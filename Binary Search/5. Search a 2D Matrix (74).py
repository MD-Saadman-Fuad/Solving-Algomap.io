def searchMatrix(matrix, target):

    if matrix == []:
        return False
    m = len(matrix)
    n = len(matrix[0])
    low = 0
    high = (m * n) - 1

    while low <= high:
        mid = (low+high)//2
        row = mid // n
        col = mid % n

        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            low = mid + 1
        else:
            high = mid - 1
    return False


# Get number of rows and columns

# Initialize low and high

# Start Binary Search

# Calculate mid

# Convert mid into row and column

# Get the matrix value

# If value == target:
# Return True

# If value < target:
# Search right

# If value > target:
# Search left

# If target is not found:
# Return False


# --- TEST CASES ---

matrix_1 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target_1 = 3

matrix_2 = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target_2 = 13

matrix_3 = [[1]]
target_3 = 1

matrix_4 = [[1, 3, 5, 7]]
target_4 = 7


# --- OUTPUT ---

print(searchMatrix(matrix_1, target_1))  # Expected: True
print(searchMatrix(matrix_2, target_2))  # Expected: False
print(searchMatrix(matrix_3, target_3))  # Expected: True
print(searchMatrix(matrix_4, target_4))  # Expected: True
