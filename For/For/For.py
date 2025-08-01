#Sum of price of all products
products = [
    {'name' : 'Samsung s5' ,'Price': '3000'},
    {'name' : 'Samsung s6' ,'Price': '4000'},
    {'name' : 'Samsung s7' ,'Price': '8000'},
    {'name' : 'Samsung s8' ,'Price': '9000'},
    {'name' : 'Samsung s9' ,'Price': '30000'},
    {'name' : 'Samsung s10' ,'Price':'44000'}
    ]

sum = 0;
for product in products :
    sum += int(product['Price'])

print(sum)

#Products that is expensive or equal than 5000
for product in products:
    if int(product['Price']) >=5000:
        print(product['name'])

#Which cities are mostly 5 letters?
cities = ['Gaziantep','Eskisehir','Malatya','Van','Izmir','Bolu']

for c in cities:
    if len(c)<=5:
        print(c)

#Which numbers are multiples are three?
numbers = [1,3,4,6,9,11]

for n in numbers:
    if(n%3==0):
        print(n)


