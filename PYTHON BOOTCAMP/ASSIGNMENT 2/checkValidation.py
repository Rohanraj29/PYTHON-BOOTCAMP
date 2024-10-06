""" Write a program to take a password from the user and check if it matches a preset 
password ("python123"). Print "Access granted" if the password matches, 
otherwise print "Access denied." 
Input: python123 
Output: `Access granted`
"""
current_password="Rahul7488"
new_password=(input("Enter your password:-"))
if(current_password==new_password):
    print("Access Granted")
else:
    print("Access Denied")