'''
lambda(Anonymous Function):
--> lambda is a keyword which is used to create anonymous functions
--> lambda always give one address
--> for calling the lambda function we can store the address of lambda inside
a variable.By invoking the var_name, we can call the function.

SYNTAX:
var_name= lambda args: <exp>
var_name(args) ##Calling the lambda function
'''

##lambda args: <exp>

#syntax 1: use this in begining
# result=lambda a,b: a+b ##returns value
# print(result)
# print(result(1,2))

#syntax 2:
# (lambda a,b: print(a+b))(int(input('First number:')),int(input('Second number:')))


##WAP to find a the square of a number if it is even
# num=int(input('Enter a number:'))
# if  num%2==0:
#     print(num** 2) #num*num
#using lambda
# result=(lambda num: print(num**2) if num%2==0 else None)
# result(2)

# (lambda num: print(num**2) if num%2==0 else None)(int(input()))


'''
lambda args:<exp_1> if <cond> else <exp2>
'''
##wap to find the square of a number if it is even otherwise print cube of it.

# result=(lambda num: print(num**2) if num%2==0 else print(num**3))
# result(11)

# (lambda num: print(num**2) if num%2==0 else print(num**3))(int(input('Enter number:')))

## Check whether a number is positibe or negative or zero.

# num = int(int())
# if num>0:
#     print('positive')
# elif num<0:
#     print('neg')
# else:
#     print('zero')

# if num>0:
#     print('pos')
# else:
#     if num<0:
#         print('neg')
#     else:
#         print('zero')

result=(lambda num: print('POS') if num>0 else print('NEG') if num<0 else print('ZERO'))
result(int(input('Enter number:')))