"""Write a program that asks the user to input two numbers and prints whether the 
first number is greater than, less than, or equal to the second number. 
Input: 10, 20 
Output: `10 is less than 20`
"""
a=int(input("Enter the number:-"))
b=int(input("Enter the second number:-"))
if(a>b):
    print("A is greater then B")
elif(a<b):
    print("A is less then B")
else:
    print("A is equal to B")
