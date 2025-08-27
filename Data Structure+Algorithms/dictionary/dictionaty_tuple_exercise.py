# Sum and Product of elements in tuple
print('---1---')
def sum_product(t):
    sum_result = 0
    product_result = 1

    for num in t:
        sum_result += num
        product_result *= num

    return sum_result, product_result

input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)

print('---2---')
#Count Word Frequency, count words in a list
def count_word_frequency(words):
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return word_count

print(count_word_frequency(['Samarth','Magotra','Poulomi','Samarth','Boo','Magotra']))

print('---3---')
#This code snippet defines a function merge_dicts(dict1, dict2)
# that merges two dictionaries and sums the values of common keys.

def merge_dicts(dict1, dict2):
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
print(merge_dicts(dict1, dict2))

print('---4---')
#Key with the Highest Value - Define a function which takes a dictionary as a
#parameter and returns the key with the highest value in a dictionary.

def max_value_key(my_dict):
    return max(my_dict,key=my_dict.get)

my_dict = {'a': 5, 'b': 9, 'c': 2}
print(max_value_key(my_dict))

print('---5---')
#Reverse Key-Value Pairs
#Define a function which takes as a parameter dictionary and returns a dictionary
# in which the key-value pairs are reversed.
def reverse_dict(my_dict):
    return {v: k for k, v in my_dict.items()}

my_dict = {'a': 1, 'b': 2, 'c': 3}
print(reverse_dict(my_dict))

print('---6---')
#Conditional Filter
#Define a function that takes a dictionary as a parameter and returns a
#dictionary with elements based on a condition.
def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0)
print(filtered_dict)

print('---7---')
#Same Frequency - Define a function which takes two lists as parameters and
#check if two given lists have the same frequency of elements.
def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)

list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
print(check_same_frequency(list1, list2))
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 2]
print(check_same_frequency(list1, list2))

print('---8---')
#Elementwise Sum - Create a function that takes two tuples and returns a tuple
# containing the element-wise sum of the input tuples.
def tuple_elementwise_sum(t1, t2):
    if len(t1) != len(t2):
        raise ValueError("Input tuples must have the same length.")

    result = tuple(a + b for a, b in zip(t1, t2))
    return result

tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)

print('---9---')
#Insert at the Beginning -
#Write a function that takes a tuple and a value, and returns a new tuple with
#the value inserted at the beginning of the original tuple.
def insert_value_front(input_tuple, value_to_insert):
    #return tuple([value_to_insert]) + input_tuple
    return (value_to_insert,) + input_tuple  # , is mandatory for single element tuple
input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)

print('---10---')
#Concatenate - Write a function that takes a tuple of strings and concatenates them,
# separating each string with a space.
def concatenate_strings(input_tuple):
    return ' '.join(input_tuple)

input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)

print('---11---')
#Diagonal - Create a function that takes a tuple of tuples and returns a tuple
#containing the diagonal elements of the input.
def get_diagonal(tup):
    diagonal = []
    for i in range(len(tup)):
        diagonal.append(tup[i][i])
    return tuple(diagonal)
    #return tuple(input_tuple[i][i] for i in range(len(input_tuple)))
input_tuple = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)
output_tuple = get_diagonal(input_tuple)
print(output_tuple)

print('---12---')
#Common Elements - Write a function that takes two tuples and returns a tuple containing the
#common elements of the input tuples.
def common_elements(tuple1, tuple2):
    common_element = []
    for i in tuple1:
        for j in tuple2:
            if i == j:
                common_element.append(i)
    return tuple(common_element)
    #return tuple(set(tuple1) & set(tuple2))
    #return tuple(x for x in tuple1 if x in tuple2)
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)
