"""Write a Python program to check if a given year is a century year (a year divisible 
by 100). 
Input: 1900 
Output: `Century year`
"""
year=int(input("Enter the year:-"))
if(year%100==0):
    print("Century year")
else:
    print("Not Century year")