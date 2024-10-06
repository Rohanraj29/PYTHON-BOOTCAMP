"""
 Write a Python program to check if a given number is positive, negative, or zero. 
    Input: 5 
    Output: `Positive number`
"""
number=int(input("Enter the number:-"))
if(number>0):
    print("Positive Number")
elif(number==0):
    print("Zero")
else:
    print("Negative Number")