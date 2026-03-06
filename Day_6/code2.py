## packing
## single packing / tuple packing
'''
... def func_name(*args):
...     statement
...     block
... func_name(val1, val2, val3,.....,valn)
'''

## create a function whichcan take n no of int or float numbers and returns only their addition

# def add_nums(*args):
#     print(args, type(args))
#     sum = 0
#     for i in args:
#         sum += i 
#     print(f'Addition:{sum}')

# add_nums()

# add_nums(1,2, 3, 4, 5, 6, 7, 8)

'''
output:
() <class 'tuple'>
Addition:0
(1, 2, 3, 4, 5, 6, 7, 8) <class 'tuple'>
Addition:36
'''


# def add_nums(*args):
#     args = list(args)
#     print(args, type(args))
#     sum = 0
#     for i in args:
#         sum += i 
#     print(f'Addition:{sum}')

# add_nums()

# add_nums(1,2, 3, 4, 5, 6, 7, 8)

'''
output:
[] <class 'list'>
Addition:0
[1, 2, 3, 4, 5, 6, 7, 8] <class 'list'>
Addition:36
'''


## Create a function which will take n no of inputs from the user and return the sum of only int and floating point numbers. Please make sure that, user is capable of passing all types of values

# def add_nums(*args):
#     sum = 0
#     for i in args:
#         if type(i) == int or type(i) == float:
#          sum += i 
#     print(f'Addition:{sum}')


# add_nums([1,2,3], [2,3,4]) 
# add_nums(1, 2, 3)
# add_nums(2.3, 4.5, 23.6)
# add_nums({1, 2, 3}, {2, 4, 5})

'''
output:
Addition:0
Addition:6
Addition:30.400000000000002
Addition:0
'''

## double packing / dictionary packing -- values which have key value pair

'''
def func_name(**kwargs):
    statement 
    block
func_name(k1=v1, k2=v2, k3=v3....kn=vn)
--> here all the key names should be a string but can't use quotes
'''

# def print_details(**kwargs):
#     print(kwargs)

# print_details(username='user123', password='****', logged_in= True)

'''
output:
{'username': 'user123', 'password': '****', 'logged_in': True}

'''


## unpacking

# def add_nums(*args):
#     sum = 0
#     for i in args:
#         if type(i) == int or type(i) == float:
#          sum += i 
#     print(f'Addition:{sum}')

# add_nums(*eval(input('enter a list of values:')))
# add_nums(*[1, 2, 3, 4, 'Hello', 'Jecrc', (1, 2, 3)])  



## problem --> Create a function which will return a list of prime numbers. Please make sure that user can pass n inputs.
# For checking a number is prime or not, you can create one function.

def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i == 0:
            return False
        
    return True


def find_prime_nums(*args):
    prime = []
    for i in args:
        if isPrime(i) == True:
            prime.append(i)
    print(prime)


find_prime_nums(*eval(input('Enter a list of nums:')))
