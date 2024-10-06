"""
Write a Python program to calculate Body Mass Index (BMI). Take the user's 
weight (in kg) and height (in meters) as input. 
Formula: BMI = weight / (height × height)
"""
weight=int(input("Enter the weight in kg:-"))
height=int(input("Enter the height in meter"))
BMI=weight/(height*height)
print("Body mass index is ",BMI)