'''
control statements:
it is the type of statement which controls the flow of the execution of a program.
'''

##conditional statements: based upon one condition, the flow of the execution of a program will be declared.

'''
1.if statement (simple if),
2. if else statement
3. elif statement
4. nested if statement
'''

'''
entry control:not executed even once
exit control:atleast one time loop will be executed without checking the condition
'''

##wap to check whether the username and password is correct or not. If correct print login successfully completed if not, do nothing.

user={
    'username':'user123',
    'password':'****',
}
un=input('Enter username:')
pswd=input('Enter password:')

##if the condition is true then only if block will get executed
if un==user['username'] and pswd==user['password']:
    print('Login Successfully Completed!')
else:
    print('Incorrect username or password!')
    
print('Program got ended!')


##elif statement
##when you have multiple conditions;multiple statement blocks;
##at least one if condition should be there.

##WAP in python to take a character from the user and check wether it is a vowel or consonent or digit or special character.

'''
1. take a character from the user
2.implement the condition one by one.
'''
chr=input('Enter a character: ') ##5
if chr in 'aeiouAEIOU':
    print('Vowel')
elif chr in '0987654321':
    print('Digit')
elif chr in 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ':
    print('Consonant')
else:
    print('special character')    
