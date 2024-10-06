"""
Write a program that takes the length and width of a rectangle as input and 
calculates its area and perimeter. 
• Formula: 
Area = length × width 
Perimeter = 2 × (length + width) 
"""
length=int(input("Enter the length:-"))
width=int(input("Enter the width:-"))
area=length*width
perimeter=2*(length+width)
print("Area of rectangle is ",area)
print("Perimeter of rectangle is ", perimeter)