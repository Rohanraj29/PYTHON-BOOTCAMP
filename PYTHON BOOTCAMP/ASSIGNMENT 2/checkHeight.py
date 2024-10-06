"""Write a Python program to determine whether a person’s height (in cm) is 
considered short (<150), average (150-180), or tall (>180). 
Input: 165 
Output: `Average height`
"""
height=int(input("Enter your height:-"))
if(height>180):
    print("Tall")
elif(height<150):
    print("Short")
else:
    print("Average")