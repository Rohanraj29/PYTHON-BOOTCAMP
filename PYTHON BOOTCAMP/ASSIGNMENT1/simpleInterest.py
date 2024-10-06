"""
Write a program to take the principal amount, rate of interest, and time from 
the user and calculate the simple interest. 
• Formula: Simple Interest = (Principal × Rate × Time) / 100. 
"""
principal=int(input("Enter the principal amount:-"))
rate=int(input("Enter the rate:-"))
time=int(input("Enter the time:-"))
simple_interest=(principal*rate*time)/100
print("Simple Interest is ",simple_interest)