""" Write a program that asks the user to enter a year and checks whether the year is a 
leap year or not. 
    Input: 2024 
   Output: `Leap year`
   """
year=int(input("Enter the year:-"))
if(year%4==0):
    print("It is a leap year")
else:
    print("It is not a leap year")