def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = (left+right) // 2
        guess = arr[middle]

        if guess == target:
            return middle
        elif guess < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1 # Target not in the array

