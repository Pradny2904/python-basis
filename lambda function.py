'''
#WAP to get even nos using for loop

list = [1,2,3,4,5,6,7]
for i in list:
    if i%2==0:
        print(i, end=' ')


list = [1,2,3,4,5,6,7]
newlist = [x for x in list if x%2==0]
print(newlist)

#WAP to get even nos using Lambda function
list_ = [1,2,3,4,5,6,7]
even =list(filter(lambda x: (x%2==0), list_))
print(even)


# WAP to get larger no using Lambda function

list_ = [10,20,30,40]
larger_no = list(filter(lambda x: if>list==True, list_))
print(larger_no)


list1 = [10,20,30,5]
even = list(filter(lambda p: (p%2==0), list1))
print(even)

number = int(input('Enter the number of rows:'))
for i in range(number):
    print('*'*number)


number = int(input('Enter the number of rows:'))
for i in range(1,number+1):
    print(' '*(number-i)+'*'*i)


l = [1,2,3,4]
l1= l[::-1]
print(l1)



work = input('Enter the name: ')
w1= work[::-1]
print(w1)

work = input('Enter the name: ')
w1 = " ". join(reversed(work))
print(w1)
'''

string = 'Pradnya'
s1 = string.find('r')
print(s1)