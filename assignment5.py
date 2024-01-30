
#MODULE
#QS1

import calendar

def display_month_calendar(year, month):
    cal = calendar.month(year, month)
    print(f"Calendar for {calendar.month_name[month]} {year}:\n")
    print(cal)
display_month_calendar(2022, 1)

#Qs2

from datetime import datetime

def display_current_datetime():
    current_datetime = datetime.now()
    print(f"Current Date and Time: {current_datetime}")
display_current_datetime()


#QS3

import time

def display_current_time():
    current_time = time.localtime()
    formatted_time = time.strftime("%H:%M:%S", current_time)
    print(f"Current Time: {formatted_time}")
display_current_time()

#QS4

import operator
numbers = [1, 2, 3, 4, 5]
add_result = operator.add(3, 4)  
mul_result = operator.mul(3, 4)  
get_second_element = operator.itemgetter(1)
second_element = get_second_element(numbers)
class ExampleClass:
    def __init__(self, value):
        self.value = value
objects = [ExampleClass(10), ExampleClass(20)]
get_value_attr = operator.attrgetter('value')
attr_values = list(map(get_value_attr, objects))
print(f"Add Result: {add_result}")
print(f"Mul Result: {mul_result}")
print(f"Second Element: {second_element}")
print(f"Attribute Values: {attr_values}")

#QS5

import math
radius = 5
area = math.pi * math.pow(radius, 2)
print(f"Area of a circle with radius {radius}: {area:.2f}")
num = 5
factorial_result = math.factorial(num)
print(f"Factorial of {num}: {factorial_result}")
float_num = 3.75
rounded_num = round(float_num)
print(f"Rounded value of {float_num}: {rounded_num}")
log_value = 100
log_base_10 = math.log10(log_value)
print(f"Logarithm base 10 of {log_value}: {log_base_10}")
angle_radians = math.radians(30)
sin_result = math.sin(angle_radians)
print(f"Sine of {math.degrees(angle_radians)} degrees: {sin_result:.2f}")

