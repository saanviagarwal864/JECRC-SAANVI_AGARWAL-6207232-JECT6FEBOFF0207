'''
raise--> It is a keyword, which helps us to throw an error in between a program.

Exception Creation,

1. Custom Exception(raise)
2. User-defined Exception(raise)
3. Assertion Exception(assert)
'''

'''
Custom Exception:
1. We use pre-built Exeption classes according to our requirement.

raise ValueError('message')

output:
ValueError:message

'''
# num=17
# if num>=18:
#     print('eligible for voting and driving')
# else:
#     raise ValueError('Age should be greater than or equals to 18!')
#     # raise NameError('Age should be greater than or equals to 18!') #--.we can also give this



'''
User-defined Exception:
1.It is a type of exception in which we can create our own exception classes based upon our own requirement.
we can also provide names to those classes according the user cases.
'''

# class MyException(Exception):
#     pass

# raise MyException('This is my exception class!')


# n1,n2=10,0
# if n2==0:
#     raise MyException('Second number can not be zero!')
# else:
#     print(n1/n2)

'''
Assertion Exception

-- Assertion exception can be created by using one keyword called "assert".

assert <condition>, print(ERROR)
print(output)
'''

s=input('Enter a string:')
assert s==s[::-1],print('It is not a palindromic string!')
print('It is a palindromic string!')

