#qs1

# def check_even_odd(number):
#     if number % 2 == 0:
#         print(f"{number} is an even number.")
#     else:
#         print(f"{number} is an odd number.")

# user_input = int(input("Enter an integer: "))
# check_even_odd(user_input)

#qs2

# def create_square_dictionary():
#     square_dict = {num: num**2 for num in range(1, 21)}
#     return square_dict

# result_dict = create_square_dictionary()

# for key, value in result_dict.items():
#     print(f"{key}: {value}")


#qs3


# def remove_vowels(input_string):
#     vowels = "aeiouAEIOU"
#     result_string = ''.join([char for char in input_string if char not in vowels])
#     return result_string
# user_input = input("Enter a string: ")
# result = remove_vowels(user_input)
# print("String with vowels removed:", result)

#qs4

# n = 10 
# powers_of_2 = map(lambda x: 2**x, range(n))
# print("Powers of 2:")
# for power in powers_of_2:
#     print(power)

#qs5


# def bubble_sort(arr):
#     n = len(arr)

#     for i in range(n - 1):
#         for j in range(0, n - i - 1):
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
# my_list = [64, 34, 25, 12, 22, 11, 90]

# print("Original list:", my_list)

# bubble_sort(my_list)

# print("Sorted list:", my_list)


#qs6

def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        mid_val = arr[mid]
        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
sorted_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_value = 7

result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Element {target_value} is present at index {result}")
else:
    print(f"Element {target_value} is not present in the list")


#qs7
    
   
# def create_dictionary(keys, values):
#     if len(keys) != len(values):
#         print("Error: The input lists must be of the same length.")
#         return None
    
#     result_dict = dict(zip(keys, values))
#     return result_dict
# keys_list = input("Enter keys separated by space: ").split()
# values_list = input("Enter values separated by space: ").split()
# result_dict = create_dictionary(keys_list, values_list)
# if result_dict:
#     print("Resulting Dictionary:", result_dict)


#qs8

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
# result = fibonacci(6)
# print("Fibonacci number at position 6 is:", result)



#qs9

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)
# result = factorial(5)
# print("Factorial of 5 is:", result)


#qs10


# import time
# def timing_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"{func.__name__} took {execution_time:.6f} seconds to execute.")
#         return result

#     return wrapper

# @timing_decorator
# def example_function():
#     print("Executing the example function...")
#     time.sleep(2)
#     print("Function execution complete.")
# example_function()


#qs11

# def divisible_by_5_and_7_generator(n):
#     for num in range(n + 1):
#         if num % 5 == 0 and num % 7 == 0:
#             yield num
# n = int(input("Enter the value of n: "))
# result_generator = divisible_by_5_and_7_generator(n)
# print(f"Numbers divisible by 5 and 7 between 0 and {n}: {', '.join(map(str, result_generator))}")

#QS12
# def even_numbers_generator(n):
#     for num in range(n + 1):
#         if num % 2 == 0:
#             yield num

# n = int(input("Enter the value of n: "))
# result_generator = even_numbers_generator(n)
# print(f"Even numbers between 0 and {n}: {', '.join(map(str, result_generator))}")


#QS13

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key

# input_list = [12, 11, 13, 5, 6]
# print("Original Array:", input_list)

# insertion_sort(input_list)

# print("Sorted Array:", input_list)




#QS14
# def linear_search(arr, target):
#     for i in range(len(arr)):
#         if arr[i] == target:
#             return i
#     return -1

# numbers = [2, 8, 5, 3, 9, 1, 7]
# target_number = 5

# result = linear_search(numbers, target_number)

# if result != -1:
#     print(f"Element {target_number} found at index {result}.")
# else:
#     print(f"Element {target_number} not found in the list.")



#QS15
    
# def selection_sort(arr):
#     n = len(arr)

#     for i in range(n - 1):
#         min_index = i
#         for j in range(i + 1, n):
#             if arr[j] < arr[min_index]:
#                 min_index = j

#         arr[i], arr[min_index] = arr[min_index], arr[i]
# input_list = [64, 25, 12, 22, 11]
# print("Original Array:", input_list)

# selection_sort(input_list)

# print("Sorted Array:", input_list)



#QS16

# def second_smallest(nums):
#     if len(nums) < 2:
#         return "List should have at least two elements."

#     smallest = float('inf')
#     second_smallest = float('inf')

#     for num in nums:
#         if num < smallest:
#             second_smallest = smallest
#             smallest = num
#         elif num < second_smallest and num != smallest:
#             second_smallest = num

#     return second_smallest

# numbers = [5, 8, 3, 1, 7, 9, 2, 6]
# result = second_smallest(numbers)

# print("Original List:", numbers)
# print("Second Smallest Number:", result)
    

