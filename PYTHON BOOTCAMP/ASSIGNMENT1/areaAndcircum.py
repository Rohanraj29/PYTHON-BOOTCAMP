"""
Take the radius of a circle from the user and calculate the area and 
circumference. 
• Formula: 
Area = π × radius² 
Circumference = 2 × π × radius
"""
radius=int(input("Enter the radius:-"))
pi=3.14
area=pi*radius**2
circumference=2*pi*radius
print("Area of circle is ",area)
print("Circumference of circle is ",circumference)