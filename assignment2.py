#Qn1  postive or negative
# number = float(input("Enter a number: "))
# if number > 0:
#     print("The entered number is positive.")
# elif number==0:
#     print("The entered number is negative.")
# else:
#     print("The entered number is zero.")

#Qn2 swap two variables
# a = 5
# b = 10
# temp = a
# a = b
# b = temp
# print("After swapping:")
# print("a =", a)
# print("b =", b)

#Qn3 Determine If Year Is Leap Year

# def is_leap_year(year):
#     if (year % 4 == 0):
#         if (year % 100 == 0):
#             if (year % 400 == 0):
#                 return True
#             else:
#                 return False
#         else:
#             return True
#     else:
#         return False

# year = int(input("Enter a year: "))

# if is_leap_year(year):
#     print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.")


#Qs4 given number is odd or even.

# def check_odd_even(number):
#     if number % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# number = int(input("Enter a number: "))
# result = check_odd_even(number)
# print(f"The number {number} is {result}.")


#Qs5  print the fibonocci series
# def fibonacci(n):
#     fib_series = [0, 1]
#     while len(fib_series) < n:
#         fib_series.append(fib_series[-1] + fib_series[-2])
#     return fib_series


# num_terms = int(input("Enter the number of Fibonacci terms: "))


# if num_terms <= 0:
#     print("Please enter a positive integer.")
# else:

#     result = fibonacci(num_terms)

#     print("Fibonacci Series:")
#     print(result)


# Qs6
    
# for i in range(6, 0, -1):
#     print('*' * i)

# #Qsb
    
# for i in range(1, 6):
#     print('*' * i)

# for i in range(6, 0, -1):
#     print('*' * i)

#Qs7

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True

# def print_primes_in_interval(start, end):
#     print(f"Prime numbers between {start} and {end}:")
#     for num in range(start, end + 1):
#         if is_prime(num):
#             print(num)

# start = int(input("Enter the start of the interval: "))
# end = int(input("Enter the end of the interval: "))

# if start >= end:
#     print("Invalid interval. Please make sure the start is less than the end.")
# else:
#     print_primes_in_interval(start, end)


# Qs8
    

# odd_numbers = []
# sum_of_odd_numbers = 0

# for num in range(1, 51, 2):
#     print(num, end=' ')
#     odd_numbers.append(num)
#     sum_of_odd_numbers += num
# print("\nSum of odd numbers:", sum_of_odd_numbers)

#Qs9


# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# number = int(input("Enter a number to find its factorial: "))

# if number < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     result = factorial(number)

#     print(f"The factorial of {number} is: {result}")


#Qs10

# def is_palindrome(s):
#     s = s.replace(" ", "").lower()
#     return s == s[::-1]

# string = input("Enter a string to check if it's a palindrome: ")

# if is_palindrome(string):
#     print(f"{string} is a palindrome.")
# else:
#     print(f"{string} is not a palindrome.")


#Qs11

# sum_of_integers = 0

# for num in range(101, 200):
#     if num % 7 == 0:
#         sum_of_integers += num

# print("Sum of integers greater than 100 and less than 200 divisible by 7:", sum_of_integers)


#Qs 12


# num = int(input("Enter a number to display its multiplication table: "))
# print(f"Multiplication table for {num}:")

# for i in range(1, 11):
#     product = num * i
#     print(f"{num} * {i} = {product}")


#qn13
    

# length = float(input("Enter the length of the rectangle: "))
# width = float(input("Enter the width of the rectangle: "))
# area = length * width
# perimeter = 2 * (length + width)
# print(f"The area of the rectangle is: {area}")
# print(f"The perimeter of the rectangle is: {perimeter}")

#qs14

# n = int(input("Enter a positive integer (n) to find the sum of the first n natural numbers: "))

# if n <= 0:
#     print("Please enter a positive integer.")
# else:
#     sum_of_natural_numbers = (n * (n + 1)) // 2
#     print(f"The sum of the first {n} natural numbers is: {sum_of_natural_numbers}")


#qs15

# def is_armstrong_number(number):
#     num_str = str(number)
#     num_digits = len(num_str)
#     sum_of_digits = sum(int(digit) ** num_digits for digit in num_str)
#     return number == sum_of_digits
# num = int(input("Enter a number to check if it's an Armstrong number: "))
# if is_armstrong_number(num):
#     print(f"{num} is an Armstrong number.")
# else:
#     print(f"{num} is not an Armstrong number.")

#qs16

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# num3 = float(input("Enter the third number: "))
# largest = max(num1, num2, num3)
# print(f"The largest number among {num1}, {num2}, and {num3} is: {largest}")
 

#qs17

# import string

# def remove_punctuation(input_string):
#     translation_table = str.maketrans("", "", string.punctuation)
#     result_string = input_string.translate(translation_table)
#     return result_string
# input_string = input("Enter a string with punctuation: ")
# result = remove_punctuation(input_string)
# print(f"Original String: {input_string}")
# print(f"String without Punctuation: {result}")

#qs18


# num_rows = int(input("Enter the number of rows for the triangle: "))
# for i in range(1, num_rows + 1):
#     print((str(i) + ' ') * i)

#QS19

def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = {vowel: 0 for vowel in vowels}
    for char in input_string:
        if char in vowels:
            vowel_count[char] += 1

    return vowel_count
user_input = input("Enter a string: ")
result = count_vowels(user_input)
for vowel, count in result.items():
    print(f"Number of {vowel}'s: {count}")

#qs20
# class ComplexNumber:
#     def __init__(self, real, imag):
#         self.real = real
#         self.imag = imag

#     def __str__(self):
#         return f"{self.real} + {self.imag}j"

#     def add(self, other):
#         return ComplexNumber(self.real + other.real, self.imag + other.imag)

#     def subtract(self, other):
#         return ComplexNumber(self.real - other.real, self.imag - other.imag)

#     def multiply(self, other):
#         real_part = (self.real * other.real) - (self.imag * other.imag)
#         imag_part = (self.real * other.imag) + (self.imag * other.real)
#         return ComplexNumber(real_part, imag_part)

#     def divide(self, other):
#         denominator = (other.real ** 2) + (other.imag ** 2)
#         real_part = ((self.real * other.real) + (self.imag * other.imag)) / denominator
#         imag_part = ((self.imag * other.real) - (self.real * other.imag)) / denominator
#         return ComplexNumber(real_part, imag_part)
# num1 = ComplexNumber(3, 4)
# num2 = ComplexNumber(1, 2)
# result_addition = num1.add(num2)
# print(f"Addition: {num1} + {num2} = {result_addition}")

# result_subtraction = num1.subtract(num2)
# print(f"Subtraction: {num1} - {num2} = {result_subtraction}")

# result_multiplication = num1.multiply(num2)
# print(f"Multiplication: {num1} * {num2} = {result_multiplication}")

# result_division = num1.divide(num2)
# print(f"Division: {num1} / {num2} = {result_division}")