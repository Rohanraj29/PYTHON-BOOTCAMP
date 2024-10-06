"""Write a program that takes three numbers as input and prints the largest number 
among them. 
    Input: 3, 5, 1 
    Output: `The largest number is 5`
    """
a=int(input("Enter the number:-"))
b=int(input("Enter the number:-"))
c=int(input("Enter the number:-"))
if(a>b and a>c):
    print("A is greater")
elif(b>a and b>c):
    print("B is greater")
else:
    print("C is greater")