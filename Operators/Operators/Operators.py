x,y,z=5,6,11
print(x,y,z)

x,y=y,x
print(x,y,z)

values =1,2,3
print(type(values))
print(values)


x,y,z=values
print(x,y,z)

#Q1 : (x+y+z)-c, c=a*b, a,b are inputting from user 
x,y,z=2,5,107

a=input("Please first number: ")
b=input("Please second number: ")

c=int(a)*int(b)

k=(x+y+z)-c
print(f"Result:",k)

#Q2:5^2?

print(y**x)

