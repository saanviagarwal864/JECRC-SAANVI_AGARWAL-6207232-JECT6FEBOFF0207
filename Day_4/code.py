'''
🔹 Problem Statement 1

An electricity board charges consumers based on units consumed:

First 100 units → ₹5 per unit

Next 200 units → ₹7 per unit

Above 300 units → ₹10 per unit
If bill>5000 ->5% discount
'''

units=int(input())

bill=0
if (units<0):
    print('Enter valid units!!')
elif(units<=100):
    bill=(units*5)
elif(units<=300):
    bill=(100*5)+(units-100)*7
else:
    bill=(100*5)+(200*7)+(units-300)*10

if(bill>5000):
    bill=((bill/100)*95) 

print(bill)    

'''
Problem Statement 2

Loan eligibility conditions:

Salary > 25000

Cibil score > 700

if salary>50000 & cibil>750 ->instant approval

otherwise->rejected
'''

salary=int(input())
cibil=int(input())
result=''

if(salary>25000 and cibil>700):
    result='Approved after background verification'
    if(salary>50000 and cibil>750):
        result='Instant Approval'
else:
    result='Rejected'

print(result)   

'''
problem 3) cheack wether a year is leap year or not

'''

year=int(input())
result=''

if(year%100==0):
    if(year%4!=0):
        result='leap year'
    else:
        result='not a leap year'
else:
    if(year%4==0):
        result='leap year'
    else:
        result='not a leap year'     
print(result)   


##ascii values for charachter

'''
problem 4)
Wap to take a character from the user and convert it into lowercase if it is in upppercase or vice-verse
'''
character=input('enter character:')

if(ord(character)>=97 and ord(character)<=122 ):
    print(chr(ord(character)-32))
elif(ord(character)>=65 and ord(character)<=90):
    print(chr(ord(character)+32))
else:
    print(character)  


##while loop


# ex1:
i=1
while i<=5:
    print(i)
    i+=1

# ex2:
col1=[1,2,'HELLO',['a','b']]
i=0
while(i<=len(col1)-1):
    print(col1[i])
    i+=1

##For loop:

# ex1:
#Achieve the desired output for the below given input:
#INPUT: SAanvi@123Gh
#OUTPUT: saAANVI@123gH

##restriction is you can't use any inbuilt functions

s1=input('enter string:')
s2=''
for i in s1:
    if(ord(i)>=97 and ord(i)<=122 ):
        s2+=chr(ord(i)-32)
    elif(ord(i)>=65 and ord(i)<=90):
        s2+=chr(ord(i)+32)
    else:
        s2+=i
print(s2)

#wap to find the maximum number only number if collection or string then skip
'''
input:[10,2.2,5,'Hello',[100,200],99.9]
output:99.9
'''
l1=[10,2.2,5,'Hello',[100,200],99.9]
maxi=l1[0]
for i in l1:
    if(type(i) in [int,float]):
        if maxi<i:
            maxi=i   

print(maxi)     

'''
input:{'a':1,'b':2,'c':3,'d':4}
output:{1:'a',2:'b',3:'c',4:'d'}
Swap key and value pair
'''
d1={'a':1,'b':2,'c':3,'d':4}
newd1={}

for i in d1: 
    newd1[d1[i]]=i ##i is accessing the key of d1 and when we use d1[i] it becomes the value and if we write newd1[d1[i]] it becomes the key of newd1
print(newd1)   

'''
input:('Hello','Hi',20,40.2,9.6j,[1,2],'PYTHON','JECRC',(1,2,3))
output:{Hello':'l','Hi':'Hi','PYTHON':'PN','JECRC':'C',(1,2,3):2}
for immutabe datatypes tuple and string we want for even first and last and for odd middle element
'''

col1=eval(input('Enter a collection: '))
new_col1={}
for i in col1:
    if type(i) in [str,tuple]:
        if len(i)%2 == 0:
            new_col1[i]=i[0]+i[-1]
        else:
            new_col1[i]=i[len(i)//2]    
print(new_col1)   



###break###
#wap to check heterogeneous or homogeneous collection

col1=[1,2,8,4,5,6]
i,flag=col1[0],True

for j in col1:
    if type(i)!=type(j):
        flag=False
        break
    
if flag:
    print('Homogeneous')
else:
    print('heterogeneous')                 

