#Qs1

def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix
original_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
for row in original_matrix:
    print(row)

transposed_result = transpose_matrix(original_matrix)

print("\nTransposed Matrix:")
for row in transposed_result:
    print(row)

#Qs2

def capitalize_lines():
    lines = []
    while True:
        line = input("Enter a line (or press Enter to finish): ")
        if not line:
            break
        lines.append(line)
    capitalized_lines = [line.upper() for line in lines]

    print("\nCapitalized Lines:")
    for capitalized_line in capitalized_lines:
        print(capitalized_line)
capitalize_lines()


#Qs3


my_list = [1, 2, 3, 4, 5]
my_list.append(6)
print("After append:", my_list)
my_list.extend([7, 8, 9])
print("After extend:", my_list)
my_list.insert(2, 10)
print("After insert:", my_list)
my_list.remove(3)
print("After remove:", my_list)
popped_element = my_list.pop(4)
print("Popped element:", popped_element)
print("After pop:", my_list)
index_of_4 = my_list.index(4)
print("Index of 4:", index_of_4)
count_of_5 = my_list.count(5)
print("Count of 5:", count_of_5)
my_list.sort()
print("After sort:", my_list)
my_list.reverse()
print("After reverse:", my_list)
copied_list = my_list.copy()
print("Copied list:", copied_list)
my_list.clear()
print("After clear:", my_list)


#Qs4

def read_dictionary_from_keyboard():
    dictionary = {}
    
    while True:
        key = input("Enter a key (or press Enter to finish): ")
        if not key:
            break

        value = input(f"Enter the value for '{key}': ")
        dictionary[key] = value

    return dictionary

def merge_dictionaries(dict1, dict2):
    merged_dict = {**dict1, **dict2}
    return merged_dict
print("Enter values for the first dictionary:")
dictionary1 = read_dictionary_from_keyboard()
print("\nEnter values for the second dictionary:")
dictionary2 = read_dictionary_from_keyboard()
merged_dictionary = merge_dictionaries(dictionary1, dictionary2)
print("\nOriginal Dictionary 1:", dictionary1)
print("Original Dictionary 2:", dictionary2)
print("Merged Dictionary:", merged_dictionary)


#Qs5


sample_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Original Dictionary:", sample_dict)
name_value = sample_dict['name']
print("Value for 'name':", name_value)
keys_list = list(sample_dict.keys())
print("Keys List:", keys_list)
values_list = list(sample_dict.values())
print("Values List:", values_list)
items_list = list(sample_dict.items())
print("Items List:", items_list)
contains_age = 'age' in sample_dict
print("Contains 'age' key:", contains_age)
sample_dict['gender'] = 'Male'
print("After adding 'gender':", sample_dict)
removed_value = sample_dict.pop('age')
print("After removing 'age':", sample_dict)
print("Removed value:", removed_value)
sample_dict.clear()
print("After clearing the dictionary:", sample_dict)


#Qs6

def sum_of_elements(input_list):
    total_sum = sum(input_list)
    return total_sum
numbers = [1, 2, 3, 4, 5]

result = sum_of_elements(numbers)

print("List:", numbers)
print("Sum of elements:", result)


#Qs7
def generate_squared_dictionary(n):
    squared_dict = {i: i*i for i in range(1, n+1)}
    return squared_dict
n = int(input("Enter an integral number (n): "))

result_dict = generate_squared_dictionary(n)

print("Generated Dictionary:", result_dict)


#Qs8

def count_letters_digits(sentence):
    letter_count = 0
    digit_count = 0

    for char in sentence:
        if char.isalpha():
            letter_count += 1
        elif char.isdigit():
            digit_count += 1

    return letter_count, digit_count
user_sentence = input("Enter a sentence: ")

letters, digits = count_letters_digits(user_sentence)

print("Number of letters:", letters)
print("Number of digits:", digits)

#Qs9

from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even Numbers:", even_numbers)
squared_numbers = list(map(lambda x: x**2, numbers))
print("Squared Numbers:", squared_numbers)
product = reduce(lambda x, y: x * y, numbers)
print("Product of Numbers:", product)


#Qs10


squared_numbers = [x**2 for x in range(1, 6)]
print("Squared Numbers:", squared_numbers)
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers:", even_numbers)
letters = [char.upper() for char in 'hello']
print("Uppercase Letters:", letters)


#Qs11

numbers = {x: x**2 for x in range(1, 6)}
print("Squared Numbers Dictionary:", numbers)
original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
even_numbers_dict = {key: value for key, value in original_dict.items() if value % 2 == 0}
print("Even Numbers Dictionary:", even_numbers_dict)
letters_dict = {char: char.upper() for char in 'hello'}
print("Uppercase Letters Dictionary:", letters_dict)


#Qs12

def find_largest_smallest(numbers):
    if not numbers:
        return None, None

    largest = smallest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num
        elif num < smallest:
            smallest = num

    return largest, smallest
numbers = [34, 12, 56, 78, 2, 45, 67]

largest, smallest = find_largest_smallest(numbers)

print("List:", numbers)
print("Largest Element:", largest)
print("Smallest Element:", smallest)

#Qs13

def remove_even_numbers(input_list):
    filtered_list = [num for num in input_list if num % 2 != 0]
    return filtered_list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_list = remove_even_numbers(numbers)

print("Original List:", numbers)
print("List after removing even numbers:", result_list)


#Qs14

def generate_square_list():
    square_list = [x**2 for x in range(1, 31)]
    first_5_elements = square_list[:5]
    last_5_elements = square_list[-5:]
    
    return first_5_elements, last_5_elements

first_5, last_5 = generate_square_list()

print("First 5 elements:", first_5)
print("Last 5 elements:", last_5)


#Qs15

def insert_string_at_beginning(input_list, prefix_string):
    modified_list = [prefix_string + str(item) for item in input_list]
    return modified_list
original_list = [1, 2, 3, 4, 5]
prefix = "Item"

result_list = insert_string_at_beginning(original_list, prefix)

print("Original List:", original_list)
print("List after inserting '{}' at the beginning:".format(prefix), result_list)

#Qs16

def iterate_over_two_lists(list1, list2):
    for item1, item2 in zip(list1, list2):
        print(item1, item2)
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']

iterate_over_two_lists(list1, list2)

#Qs17

def add_key_to_dictionary(my_dict, key, value):
    my_dict[key] = value
    return my_dict
original_dict = {'name': 'John', 'age': 25}

new_key = 'city'
new_value = 'New York'

updated_dict = add_key_to_dictionary(original_dict, new_key, new_value)

print("Original Dictionary:", original_dict)
print("Updated Dictionary:", updated_dict)

#Qs18

dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

concatenated_dict = {}
concatenated_dict.update(dic1)
concatenated_dict.update(dic2)
concatenated_dict.update(dic3)

print("Concatenated Dictionary:", concatenated_dict)

#Qs19


my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print("Iterating over the dictionary:")
for key in my_dict:
    print(f"{key}: {my_dict[key]}")
print("\nIterating over key-value pairs using items():")
for key, value in my_dict.items():
    print(f"{key}: {value}")

#Qs20

my_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
total_sum = sum(my_dict.values())
print("Sum of all items in the dictionary:", total_sum)

#Qs21


pets_dict = {'Dog': 'Willie', 'Cat': 'Whiskers', 'Fish': 'Nemo'}
for animal, name in pets_dict.items():
    print(f"{name} is a {animal}.")

#Qs22
    
def filter_marks(subject_marks):
    filtered_dict = {subject: marks for subject, marks in subject_marks.items() if marks > 50}
    return filtered_dict
marks = {'English': 40, 'Maths': 60, 'Hindi': 30, 'Chemistry': 46, 'Physics': 70}
filtered_marks = filter_marks(marks)
print("Original Dictionary:", marks)
print("Filtered Dictionary with Marks > 50:", filtered_marks)

#QS23

def count_letters_digits(sentence):
    result_dict = {'letters': 0, 'digits': 0}

    for char in sentence:
        if char.isalpha():
            result_dict['letters'] += 1
        elif char.isdigit():
            result_dict['digits'] += 1

    return result_dict
input_sentence = "Hello 123 World!"

result = count_letters_digits(input_sentence)
print(result)

#QS24

def generate_square_dict(n):
    square_dict = {i: i**2 for i in range(1, n+1)}
    return square_dict
n_value = 5
result_dict = generate_square_dict(n_value)
print(result_dict)
