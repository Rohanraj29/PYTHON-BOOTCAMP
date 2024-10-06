a=4
b=6
c=8
d=8 # value same then no extra memory allocated same address
print(a)
print(b)
print(c)
print(d)
#Address of a variable by using id keyword
print(id(a))
print(id(b))
print(id(c))
print(id(d))
#Assign value to multiple variable in single line
r,s,p=8,16,24
print(r)
print(s)
print(p)
#Assign same value to multiple variable in single line
m=h=r=2
print(m)
print(h)
print(r)