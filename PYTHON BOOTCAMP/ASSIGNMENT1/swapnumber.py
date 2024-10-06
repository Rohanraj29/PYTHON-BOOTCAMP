"""
Take two numbers as input from the user and swap their values without using 
a third variable. 
"""
a=int(input("Enter the value of a:-"))
b=int(input("Enter the value of b:-"))
a=a+b
b=a-b
a=a-b
print("value of a and b after swapping is ",a,b)