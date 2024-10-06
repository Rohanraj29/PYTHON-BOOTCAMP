"""Write a program that takes the temperature in Celsius and prints if it is "Hot" 
(>30°C), "Warm" (between 20°C and 30°C), or "Cold" (<20°C). 
Input: 25 
Output: `Warm`
"""
temperature=int(input("Enter the temperature:-"))
if(temperature<20):
    print("Cold")
elif(temperature>30):
    print("Hot")
else:
    print("Warm")