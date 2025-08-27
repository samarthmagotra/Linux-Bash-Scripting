
#  How to create a Tuple?

newTuple = ('a', 'b', 'c', 'd', 'e') # Time Complexity O(1), Space complexity O(n)
newTuple1 = tuple('abcde')

print(newTuple, newTuple1)

# Access Tuple elements
print(newTuple[0])
print(newTuple[1:3])

#  Traverse through tuple T:O(n),S:O(1)
for i in newTuple:
    print(i)

for index in range(len(newTuple)):
    print(newTuple[index])

#  How to search for an element in Tuple?
print('a' in newTuple)
#using index() method
print(newTuple.index('e')) #O(n)

def searchInTuple(pTuple, element): #O(n), O(1)
    for i in pTuple:
        if i == element:
            return pTuple.index(i)
    return 'The element does not exist'

print(searchInTuple(newTuple, 'f'))

# Tuple Operations / Functions
myTuple = (1,4,3,2,5,1)
myTuple1 = (4,2,6,9,8,7)

print(myTuple + myTuple1) 
print(myTuple * 4)      
print(2 in myTuple1)

#tuple methods
print(myTuple.count(1))
print(myTuple1.index(2))
print(len(myTuple))
print(max(myTuple))
print(min(myTuple))
print(tuple([4,5,6,7,7,9]))
print(sorted(myTuple))
print(all(myTuple))
print(any(myTuple))

# == vs is
init_tuple_a = '3', '4'
init_tuple_b = ('3', '4')
print(init_tuple_a == init_tuple_b)
print(init_tuple_a is init_tuple_b)

init_list_a = ['3', '4']
init_list_b = ['3', '4']
print(init_list_a == init_list_b)
print(init_list_a is init_list_b)

print(id(init_tuple_a), id(init_tuple_b))  # Might be same
print(id(init_list_a), id(init_list_b))    # Definitely different





