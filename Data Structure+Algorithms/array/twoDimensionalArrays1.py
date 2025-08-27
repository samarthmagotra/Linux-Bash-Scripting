import numpy as np

twoDArray = np.array([[11, 15, 10, 6], [10, 14, 11, 5], [12, 17, 12, 8], [15, 18, 14, 9] ])
print(twoDArray)

# at index 1 for row(axis 0). For column, its axis 1
newTwoDArray = np.insert(twoDArray, 1, [[1,2,3,4]], axis=0)
print(newTwoDArray)

print(len(twoDArray))

newTwoDArray = np.append(twoDArray, [[1,2,3,4]], axis=0)
print(newTwoDArray)
print(len(newTwoDArray))
print(len(newTwoDArray[0]))

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) and colIndex >= len(array[0]):
        print('Incorrect Index')
    else:
        print(array[rowIndex][colIndex])
        print(f'Number of elements in array: {len(array)*len(array[0])}')

accessElements(newTwoDArray, 1, 2)

def traverseTDArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(f'Elements at row:{i} and column:{j} is: {array[i][j]}')

traverseTDArray(twoDArray)

def searchTDArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return 'The value is located index '+str(i)+" "+str(j)
    return 'The element not found'

print(searchTDArray(twoDArray, 14))

#deletion in array, delete a column at index 1
print(twoDArray)
newTDArray = np.delete(twoDArray, 1, axis=1)
print(newTDArray)
#deletion in array, delete a row at index 0
newTDArray = np.delete(twoDArray, 0, axis=0)
print(newTDArray)