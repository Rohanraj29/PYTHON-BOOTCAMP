"""
 Write a program that asks the user for their age and checks if they are eligible to 
vote (age >= 18). 
    Input: 16 
    Output: `Not eligible to vote`
"""
age=int(input("Enter your age:-"))
if(age>=18):
    print("You are eliglible to vote")
else:
    print("You are not eliglible to vote")