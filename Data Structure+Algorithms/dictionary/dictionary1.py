import random

#  Update / add an element to the dictionary
dict1 = dict()  #O(1), O(1)
print(dict1)

#Ways of creating dictionary
eng_sp = dict(one='uno', two='dos', three='tres') # O(n), O(n)
eng_sp2 = {'one':'uno', 'two':'dos', 'three':'tres'}
eng_sp_list = [('one','uno'),('two','dos'),('three','tres')]
eng_sp3 = dict(eng_sp_list) # dictionary from list of tuples
print(eng_sp,'\n',eng_sp2,'\n',eng_sp3)

myDict = {'name': 'Edy', 'age': 26}
myDict['address'] = 'London'
print(myDict)

#  Traverse through a dictionary
def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(myDict)

#  Searching a dictionary
def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'
print(searchDict(myDict, 27))

#  Delete or remove a dictionary
del myDict['age']
print(myDict)
removed_elem = myDict.pop('name')
print(myDict, removed_elem)
removed_elem = myDict.pop('sex', None)
removed_elem = myDict.popitem()
print(myDict, removed_elem)
myDict.clear()
print(myDict)

print('***********************DICT METHODS**********************')
# Dictionary methods:
#copy
myDict = {'name': 'Edy', 'age': 26, 'sex':'Male', 'address': '127 Flamsteed Close'}
dict2 = myDict.copy()
print(myDict,dict2, sep='\n')

#fromkeys
dict3 = {}.fromkeys([1,2,3], [3,5,6])
print(dict3)

#get()
print(myDict.get('name'))
print(myDict.get('adc', None))
print(myDict.get('adc', 'Samarth')) # If key dont exist, return Samarth

#items()
print(myDict.items())
for k,v in myDict.items():
    print(f'{k}:{v}')

#keys()
print(myDict.keys())
for k in myDict.keys():
    print(f'{k}')

#values()
print(myDict.values())
for v in myDict.values():
    print(f'{v}')

#pop and popitem
print(myDict.pop('abc', None))
print(myDict.popitem())
print(myDict)

#setdefault()
print(myDict.setdefault('name','added')) # add name key: added if no name key is there
print(myDict)
print(myDict.setdefault('name1','added'))
print(myDict)

#update() - in place update, return none
newDict = {'a':1, 'b':2, 'c':3}
myDict.update(newDict)
print(myDict)
newDict2 = {'a':1, 'b':2, 'd':4, 'e':5}
print(myDict.update(newDict2))
print(myDict)

#MISC
newDict = {'a':1, 'b':2, 'c':3}
print('a' in newDict) # in operator check for key in a dict
print(1 in newDict.values()) # use .value() for values
print(len(newDict)) # number of key, value pairs
print(all(newDict)) # check if all keys are Boolean true, false if any key is false
print(any(newDict)) # check if any keys are Boolean true, false is all keys are false

# sorted method
myDict = {'eooooa': 1, 'aas': 2, 'udd': 3, 'sseo': 4, 'werwi': 5}
print(sorted(myDict)) # sorted by key
print(sorted(myDict, key=len)) # sorted by length of key

#dictionary comprehensions
city = ['Paris', 'London','Rome','Berlin', 'Medrid']
city_temp = {city_key : random.randint(15,25) for city_key in city}
print(city_temp)
city_temp = {city_key : random.randint(15,25) for city_key in city if random.randint(15,25) > 20}
print(city_temp)
above_20 = {city:temp for city,temp in city_temp.items() if temp > 20}
print(above_20)











