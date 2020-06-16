def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i

    return -1  # not found



# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    #set index 0 and last index
    left = 0
    right = len(arr) - 1  #dynamic setting of last index, array could be million elements, still will be the last one
    # Your code here
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid  + 1 
        else:
            right = mid - 1



    return -1  # not found
