name = 'Akif'
surname='Kaplan'
age = 21 


greetings = 'My name is ' + name + ' '+ surname + ', I am ' + str(age)+ ' years old.'

print(greetings)#call
print(greetings[0])#print first item
lenght=len(greetings)#get length
print(lenght)
print(greetings[lenght-1])#print last item
print(greetings[3:7])#print between 3 to 7. items
print(greetings[:15])
print(greetings[15:])
print(greetings[2:40:3])#print three by three
print(greetings[-15:])#last 15 chars
print(greetings[::1])#normal
print(greetings[::-1])#reverse

#formating
print('My name is {} {}'.format(name,surname))#normally
print('My name is {1} {0}'.format(name,surname))#firstly surname than name
print('My name is {n} {s}'.format(n=name,s=surname))


result =100 / 1111
print('The result is {} '.format(result))#aritmethic 
print('The result is {r:1.5} '.format(r=result))#1 is
#how much space to allocate for the full part,
# 5 is how many digits to go after the comma.




#fString
print(f"My name is {name} {surname} and I'm {age} years old.")

#multiple string
mul= 'abc' *3
print(mul)