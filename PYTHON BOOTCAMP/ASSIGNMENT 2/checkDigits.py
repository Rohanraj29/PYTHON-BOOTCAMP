"""Write a program that takes a number from the user and checks if it is a single-digit, 
double-digit, or more. 
Input: 45 
Output: `Double-digit number`
"""
x = int(input())

if len(str(x)) == 1:

  print("Single digit")

elif len(str(x)) == 2:

  print("Double digit")

else:

  print("Multi-digit")