#key - value


from traceback import print_last


users = {
    'akifkaplan':{
        'age' : 21,
        'depertman' : 'Ceng',
        'adress':'Gaziantep',
        'number':1541,
        'mail':'akif@gmail.com',
        'accessibility':{'student'}
    },
    'faikkaplan':{
        'age' : 66,
        'depertman' : 'Ceng',
        'adress':'Gaziantep',
        'number':1555,
        'mail':'faik@gmail.com',
        'accessibility':['student','teacher']
    }
}
print(users['akifkaplan'])
print(users['faikkaplan']['accessibility'][1])



plakalar = {'Ankara' : 6 , 'Istanbul' : 34}
print(plakalar['Ankara'])
plakalar['Gaziantep']=27
print(plakalar)
plakalar['Ankara'] =33
print(plakalar)



