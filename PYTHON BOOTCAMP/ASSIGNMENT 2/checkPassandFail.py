""" Write a program that asks the user to enter their exam score and prints whether 
they have passed or failed. The passing score is 40. 
Input: 35 
Output: `Fail` 
"""
score=int(input("Enter your score:-"))
if(score>40):
    print("Pass")
else:
    print("Fail")