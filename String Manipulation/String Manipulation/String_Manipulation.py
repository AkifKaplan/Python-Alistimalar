messege='Hello I am Akif. I am studying Computer Engineering'
messege = messege.upper()#Upper
print(messege)

messege = messege.lower()#lower
print(messege)

messege = messege.title()#Uppering every words first letters
print(messege)

messege = messege.capitalize()#Just first letter is uppering
print(messege)

messege = messege.split('.')
print(messege)
print(messege[0])
messege='.'.join(messege)
print(messege)
messege = messege.split()#dividing a sentence into parts
print(messege)


messege='    Hello I am Akif and I am studying Computer Engineering'
messege = messege.strip()#Deleting spaces at the begining and ending.
print(messege)
messege = messege.lstrip()#Deleting spaces at the begining.
messege = messege.rstrip()#Deleting spaces at the ending.
messege = messege.lstrip('Helo ')#delete unwanted characters at the begining.

messege='    Hello I am Akif and I am studying Computer Engineering'
index =messege.find('Computer')#Search.If there is one, tell me which index it starts from
print(index)

messege=messege.replace('Computer Engineering' , 'Ceng')#find and change
print(messege)

isStart=messege.startswith('aaa')#Is it starting with aaa?
print(isStart)