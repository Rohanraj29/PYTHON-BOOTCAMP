"""Write a Python program that takes a number from the user and checks if it is 
divisible by 3, 5, or both. 
Input: 15 
Output: `Divisible by both 3 and 5`
"""
number=int(input("Enter the number:-"))
if(number%5==0 and number%3==0):
    print("It is divisible by 5 and 3")
elif(number%5==0):
    print("It is divisible by 5")
elif(number%3==0):
    print("It is divisible by 3")
else:
    print("It is not divisible by 5 and 3")