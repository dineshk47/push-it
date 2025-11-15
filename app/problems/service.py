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

# Move all zeros in the list to the end, maintaining order of non-zero elements.
def move_zeros(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
    return nums

# check if a string reads the same backward and forward.
def check_palindrom(string):
    """
    reverse a string, check if the main string and reversed are equal
    """
    rev_str = string[::-1]
    if string.lower() == rev_str.lower():
        return "Given string is palindrom"
    else:
        return "Given string is not a palindrom"
    
# You’re given an array of numbers from 1 to n, one number is missing. Find it.
def find_missing_num(nums):
    """
    we can use the formual for findfin sum of natural numbers n*9(n+1)/2
    to find the actual sum of natural numbers and then we can calculate
    the sum of given numbers in the list, then we can subtract actual-given,
    we will get the number
    """
    n = len(nums)+1 # +1 because one is missing
    actual_sum = n*(n+1)//2
    given_sum = sum(nums)
    missing_number = actual_sum - given_sum
    return missing_number

# Count API Calls per User Q: You’re tracking API requests by user IDs in a list.
def count_api_logs(logs):
    """
    i will taken an empty dict, loop over logs, append to user log to
    the dict, and increase the value everytime the same user comes
    """
    log_result = {}
    for user in logs:
        log_result[user] = log_result.get(user, 0)+1 # if in log_result, user is a fresh entry then 0 will handle that

    return log_result

# Remove Duplicates from List Q: Remove duplicates while maintaining order.
def remove_dupicates(nums):
    """
    i will taken an empty list, loop over given list, 
    will check if the number is present in the declared empty list
    if not then append and return the result
    """
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    return result


# 2,2,8,9,10,4,3,3,11, 1, 9, 10,78,78,-9,-9,32] how many elements have atleast one element smaller to it?
def count_smaller_elements(nums):
    """
    brutforce approach is loop over the list, check each element and compare with the rest of the elements
    optimized: find the smallest number in the list, count its occurences, 
    find the lenght of the list and minus the smallest no occurences from the lenght of the list
    """
    smallest = min(nums)
    s_count = nums.count(smallest)
    result = len(nums) - s_count
    return result

# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.
def merge_strings(string1, string2):
    """
    take an empty list, calculate the lenghts of both the string and derive the min length
    loop on the range of min length and append chars from both the string in the range
    then check the which string is larger and append the rest of the chars from that string and finally convert that list to str and return
    """
    merged = []
    l1 = len(string1)
    l2 = len(string2)
    min_len = min(l1, l2)

    for i in range(min_len):
        merged.append(string1[i])
        merged.append(string2[i])
    
    if l1 > min_len:
        merged.append(l1[min_len:])
    else:
        merged.append(l2[min_len:])
    

# given a string "abcde" output should be {e{d{c{b{a}}}}}
def in_str(string):
    parts = string.split(".")
    parts.reverse()
    result = ""
    for p in parts:
        result += "{" + p
    result += "}" * len(parts)
    return result