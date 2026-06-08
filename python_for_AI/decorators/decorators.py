# What is a decorator? - A decorator is a type of design function (wrapper for another function), which adds extra functionality to any function in the file
# It takes another function as a parameter "enhances" it and returns the enhanced function
# Syntax: @decorator_name --- write above the function
# Baisc level - take a function wrap it in a decorator function, which has enhancing code, and return it

# Design of Decorator
# def decorator_function(original_func):                  # decorator function - takes original function as a parameter
#     def wrapper(*args, **kwargs):                       # wrapper function which accepts args and kwargs -- why? we are not sure how many args or kwargs will be passed from the function
#         print("some code before callin the function")   # any kind of before operations before calling the original function
#         result = original_function(*args, **kwargs)     # a call to original function - as original function will take args or kwargs , better to write it as parameters
#         print("some code after callin the function")    # any kind of after operations before calling the original function
#         return result                                   # return the "modified" function -- here (result)
#     return wrapper                                      # return the "wrapper" function to the main decorator function

# Higher-order-function(somewhat realted to decorator) - A higher-order function is a function that either accepts one or more functions as arguments or returns a function as its result

# 1. Execution Time Tracker

# Create a decorator that:

# calculates how long a function takes to execute
# prints execution time

from time import time

def performance(time_calculation):
    def wrapper(*args, **kwargs):
        start_time = time()
        result = time_calculation(*args, **kwargs)
        end_time = time()
        print(f"Total time {(end_time - start_time)} sec")
        return result
    return wrapper


@performance
def calculate_time():
    i=0
    while i < 10000000:
        i+=1
calculate_time()