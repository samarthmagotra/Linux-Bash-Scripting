import numpy as np

#Missing Number
#Write a function to find the missing number in a given integer array of 1 to 100.
# The function takes to parameter the array and the number of elements that needs to be in array.
# For example if we want to find missing number from 1 to 6 the second parameter will be 6.
#Example -    missing_number([1, 2, 3, 4, 6], 6) # 5

def missing_number(arr, n):
    total = 0
    for num in arr:
        total += num
    return f'missing number is: {(n*(n+1)//2) - total}'

print(missing_number([1,2,3,4,6,9,10,8,5],10))

#Max Product of Two Integers
#Find the maximum product of two integers in an array where all elements are positive.
#Example
# arr = [1, 7, 3, 4, 9, 5]
# max_product(arr) # Output: 63 (9*7)

def max_product_1(arr):
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization

    # Iterate through the array
    for num in arr:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment

    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication

def max_product(arr):
    maximum = arr[0]
    second_maximum = -1
    for i in range(1, len(arr)-1):
        if arr[i] >= maximum:
            maximum = arr[i]
    print(f'maximum is {maximum}')
    for num in arr:
        if second_maximum < num < maximum:
            second_maximum = num
    print(f'second maximum is {second_maximum}')
    return f'Output is {maximum*second_maximum}'

print(max_product([1, 7, 3, 4, 9, 5]))
print(max_product_1([1, 7, 3, 4, 9, 5]))

#Middle Function
#Write a function called middle that takes a list and returns
# a new list that contains all but the first and last elements.
#    myList = [1, 2, 3, 4]
#    middle(myList)  # [2,3]

def middle(lst):
    new_lst=[]
    for i in range(1,len(lst)-1):
        new_lst.append(lst[i])
    return new_lst

def middle_1(lst):
    # Return a new list containing all elements from the original list, excluding the first and last elements
    return lst[1:-1]

print(middle([1, 2, 3, 4]))
print(middle([1, 2, 3, 4, 5]))
print(middle_1([1, 2, 3, 4, 5,6,7,8]))

#reverse an array
def reverse_array(arr):
    for i in range(0, (len(arr)//2)):
        end = len(arr)-1-i
        temp = arr[i]
        arr[i] = arr[end]
        arr[end] = temp
    print(f"reversed array is: {arr}")

reverse_array([2,3,4,5,6,7,8])

# return indices of a numbers in a list such that their sum adds up to a target number.
# e.g Input: nums=[2,7,11,15], target=9, Output =[0,1]
def two_sum(lst, target):
    for i in range(len(lst)-1):
        if (lst[i] + lst[i+1]) == target:
            return f'Output = [{i}, {i+1}]'
    return 'Not found'

def findPairs(lst, target):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j]:
                print(f'Same pairs')
                continue
            elif lst[i] + lst[j] == target:
                print(f'i: {i}, j: {j}')

print(two_sum([2,7,11,15], 9))
print(two_sum([2,11,7,15], 9))
print(two_sum([3,2,4], 6))
print(two_sum([3,3], 6))

findPairs([2,7,11,15], 9)
findPairs([2,11,7,15], 9)
findPairs([3,2,4], 6)
findPairs([3,3], 6)

# Search an element in an array
myArray = np.array([1,2,3,4,5,6,7,8,9,10,11,121,44,56,67,0,12])

def findNumber(arr, num):
    for element in arr:
        if element == num:
            return f'Number {num} found'
    return f'Number {num} not found'

print(findNumber(myArray, 122))

# Given a 2D list, calculate the sum of diagonal elements
#Example - myList2D = [[1, 2, 3,4], [4, 5, 6,9], [7, 8, 9,10], [10,11,12,13]]
#diagonal_sum(myList2D)  # 15

def diagonal_sum(my2dlist):
    arr=[]
    for i in range(len(my2dlist)):
        for j in range(len(my2dlist[0])):
            if i==j:
                arr.append(my2dlist[i][j])
    print(arr)
    return sum(arr)

def diagonal_sum_1(matrix):
    # Initialize the sum to 0
    total = 0
    # Iterate through the rows of the matrix
    for i in range(len(matrix)):
        # Add the diagonal element to the total sum
        total += matrix[i][i]
    return f'another way --> {total}'

print(diagonal_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(diagonal_sum([[1, 2, 3,4], [4, 5, 6,9], [7, 8, 9,10], [10,11,12,13]]))
print(diagonal_sum_1([[1, 2, 3,4], [4, 5, 6,9], [7, 8, 9,10], [10,11,12,13]]))

#Best Score
#Given a list, write a function to get first, second best scores from the list.
#List may contain duplicates.
#Example - myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
#first_second(myList) # 90 87
def first_second(arr):
    max1, max2 = 0, 0  # O(1), constant time initialization
    for num in arr:  # O(n), where n is the length of the array
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment

    return f'First and second best scores are {max1} and {max2} respectively' # O(1), constant time multiplication

print(first_second([84,85,86,87,85,90,85,83,23,45,84,1,2,0]))

#Write a function to remove the duplicate numbers on given integer array/list.
#Example - remove_duplicates([1, 1, 2, 2, 3, 4, 5]), Output : [1, 2, 3, 4, 5]

def remove_duplicates(arr):
    lst=[arr[0]]
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1] and arr[i] not in lst:
            lst.append(arr[i])
            #print(lst)
    return f'List after removing duplicates - {lst}'

print(remove_duplicates([1, 1, 2, 2, 3, 4, 5,1,2,7,8,9,0]))

#Another way
def remove_duplicates_1(lst):
    unique_lst = []
    seen = set()
    for item in lst:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst

print(remove_duplicates_1([1, 1, 2, 2, 3, 4, 5,1,2,7,8,9,0]))

#Write a function to find all pairs of an integer array whose sum is equal to a given number.
# Do not consider commutative pairs.
#Example - pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
# Output : ['2+5', '4+3', '3+4', '-2+9']
def pair_sum(arr, target_sum):
    result = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target_sum:
                result.append(f"{arr[i]}+{arr[j]}")
    return result

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))

#Contains Duplicate
#Given an integer array nums, return true if any value appears at least twice in
# the array, and return false if every element is distinct.
#Example : Input: nums = [1,2,3,1],  Output: true
def contains_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i]==nums[j]:
                return True
    return False

def contains_duplicate_1(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate_1([1,2,3,1]))
print(contains_duplicate([1,2,3,1]))

#Rotate Matrix/ Image - LeetCode 48
#You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
#You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
#DO NOT allocate another 2D matrix and do the rotation.
def rotate(matrix):
    n = len(matrix)
    # Transpose the matrix
    for i in range(n):  # Iterate over the rows
        for j in range(i, n):  # Iterate over the columns starting from the current row 'i'
            # Swap the elements at positions (i, j) and (j, i)
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row
    for row in matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row