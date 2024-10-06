#WAP to check if a list contains a palindrome of elements. (Hint: use copy( ) method)
a=[1,2,2,1]
b=a.copy()
b.reverse()
if(a==b):
    print("Palindrome")
else:
    print("Not palindrome")