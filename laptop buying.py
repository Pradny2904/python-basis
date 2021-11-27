name= input('Enter your name please: ')
print('Hello', name, 'Welcome to our computer center' )
budget=int(input('What is your budget? '))
if budget >= 40000:
    print('1.Asus','2.Vostro', '3.HP', sep='\n')
else:
     print('Sorry then you will have to go for some other brand')
     print('1.Dell','2.Acer','3.Lenovo', sep='\n')
choice= int(input('What is your choice'))
if choice==1:
    print('You have selected Asus')
ram=int(input('How much ram you need in GB? '))    
if ram==2:
              print('Ok, it is available')
else:
    print('Sorry choose ram at least 2 GB')
if hdd==100:
    print('ok, it is available')
else:
    print('Sorry choose hdd at least 100 GB')

