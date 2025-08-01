fruits ={'apple' , 'banana' ,'watermelon'}
print(fruits)

#print((fruits[0])) this is false, because cannot indexing

fruits.add('orange')
fruits.add('cherry')
print(fruits)

fruits.update(['mango','grape','apple'])
print(fruits)

fruits.remove('mango')
print(fruits)

fruits.discard('apple')
print(fruits)

fruits.pop()#delete randomly
print(fruits)

fruits.clear()
print(fruits)

mylist=[1,1,2,3,4,4,5]
print(mylist)
print(set(mylist))