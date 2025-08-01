a=7
result = a<10 and a>5
print(result)

result = a<10 or a>5
print(result)

result = not(a>0)
print(result)

#identity operator:is

x=y=[1,2,3]#both same memory adress contents
z=[1,2,3]#same contents but different memory adress

print(x is y)#true
print(x is z)#false


#Membership operator
list1 =['banana','apple']
print('banana' in list1)

name ='Akif'

print('A' in name)
print('k' not in name)
