import array
import numpy as np

_array = array.array('i',[1,2,3,4,5]) # data type of same type, O(1)
print(_array)
print(_array[4]) #O(n)

#np_array = np.array([1,2,3,4], dtype=int) #O(1)
#print(np_array) #O(n)

#Insertion
_array.insert(0, 6) # Time Complexity, O(n), Space complexity O(1)
print(_array)

_array.insert(6,100)
print(_array)

#Array traversal
def traverseArray(arr):
    for i in arr:    # O(n) -- O(n)
        print(i)     # O(1)

#traverseArray(_array)

# Access array element
def accessElement(arr, index):
    if index > len(arr)-1:  #O(1)
        print(f'There is no element at index {index}') #O(1)
    else:
        print(arr[index]) #O(1)

#accessElement(_array, 7)

# Search an element in array and return index, i-- using linear search algorithm
def searchArray(arr, element):
    for i in range(len(arr)):  # O(n)
        if arr[i] == element: # O(n)  ----> O(n2)
            return i # O(1)
    return f'element {element} not found  in {arr}'

print(searchArray(_array, 10))

#Another way of searching an array
def searchArray2(arr, element):
    for i in arr:
        if i == element:
            return arr.index(element)
    return f'element {element} not found  in {arr}'

print(searchArray2(_array, 6))

# Deleting an element from an array with element value
_array.remove(6) # O(1) if last element is removed, else O(n) since each element has to shift left
print((_array))

# test
data = [[1, 2], [3, 4], [5, 6], [7, 8]] # 2D
print(data[0])
print(data[0][1])

data = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]] # 3D
print(data[0])
print(data[0][1])
print(data[0][1][1])

#Traversing a 2D array and finding the largest value
data = [[1, 2], [3, 4], [5, 6], [7, 8]]
def fun(m):
    v = m[0][0]

    for row in m:
        for element in row:
            if v < element: v = element

    return v

print(fun(data))