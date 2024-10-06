"""Write a Python program that calculates the grade of a student based on their 
marks. 
     Criteria: 
     Marks >= 90: `A+` 
      Marks >= 80: `A` 
      Marks >= 70: `B+` 
     Marks >= 60: `B` 
     Marks >= 50: `C` 
     Else: `Fail` 
     Input: 85 
    Output: `A`
    """
marks=int(input("Enter your marks:-"))
if(marks>=90 and marks<=100):
    print("A+")
elif(marks>=80 and marks<90):
    print("A")
elif(marks>=70 and marks<80):
    print("B+")
elif(marks>=60 and marks<70):
    print("B")
elif(marks>=50 and marks<60):
    print("C")
else:
    print("Fail")