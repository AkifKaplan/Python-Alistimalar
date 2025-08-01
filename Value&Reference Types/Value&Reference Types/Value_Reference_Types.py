#value types=>string,number

x=10
y=20

x=y
y=33

print(x,y)

#reference type => list,class
lis1=['apple','banana']
lis2=['apple','banana']

lis1=lis2

lis2[0]="watermelon"
print(lis1,lis2)
