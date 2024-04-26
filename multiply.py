# Author: Kenneth Hileman
# GitHub username: PHTIWringer
# NOTE: Will not have a ReadMe - Using another IDE
# Date: 04/25/2024
# Description: Program that takes two positive integers and returns the product of those two integers.

def multiply(num1, num2):
    '''Function that takes in two positve integers and returns the product'''
    if num1 >= 1 and num2 >= 1:
        if num2 == 1:
            return num1
        else:
            return num1 + multiply(num1, num2 - 1)
    else:
        print("Error: postive number expected.")

product = multiply(2, 300)
print(product)
