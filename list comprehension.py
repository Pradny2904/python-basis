# Old way
'''
l = ['Tomato', 'Potato', 'Onion', 'Garlic', 'Chilli, Corriandor', 'Pumpkin']
newlist = []
for i in l:
    if 'P' in i:
        newlist.append(i)
print(newlist)

 # List comprehension
l = ['Tomato', 'Potato', 'Onion', 'Garlic', 'Chilli, Corriandor','Pumpkin']
newlist = [x for x in l if 'P' in x ]
print(newlist)


list = ['Tm','Pm', 'Gm', 'Am', 'Sm', 'sn']
newlist = [x for x in list if 'S' in x]
print (newlist)


list = ['Tm','Pm', 'Gm', 'Am', 'Sm', 'sn']
newlst = [x for x in list if x!= 'Am']
print(newlst)


list = ['Tm','Pm', 'Gm', 'Am', 'Sm', 'sn']
newlst = [x for x in list]
print(newlst)


# Get all the values in new list in upper case.

List = ['Ajay', 'Abhedya']
newlist = [x.upper() for x in List]
print (newlist)
'''

# Replace Ajay by Sawant
List = ['Ajay', 'Abhedya']
newlist = [x if x!= 'Ajay' else 'Sawant' for x in List]
print (newlist)