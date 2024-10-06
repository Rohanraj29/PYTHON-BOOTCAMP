"""Write a Python program to check whether a number is divisible by both 5 and 11. 
Input: 55 
Output: `Divisible by both 5 and 11`
"""
number=int(input("Enter the number:-"))
if(number%5==0 and number%11==0):
    print("It is divisible by 5 and 11")
else:
    print("It is not divisible by 5 and 11")