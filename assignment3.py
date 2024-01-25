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

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

input_list = [12, 11, 13, 5, 6]
print("Original Array:", input_list)

insertion_sort(input_list)

print("Sorted Array:", input_list)
