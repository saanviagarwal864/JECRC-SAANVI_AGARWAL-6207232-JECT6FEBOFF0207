'''
Exception:
--> unauthorized event
--> flow of the execution of the program will be stopped.
--> after that it will never execute the further code.
--> apart from syntax error we can handle errors by using exception handling
--> 3 different ways to handle exceptions
--> if colour of issue is purple or pink it is exception(classname), if it is red it is called error(objectname),
and if purple it is called warning(approach is old).

Keywords:
1.Try: We will put the problem statement(block of code due to which we might get error)

2.Except:
--> We put actual solution(resolution for error prone code) for the error.
--> in case of java and javascript we use catch but no concept like this in python
--> if we get error in both else and try then this will execute.
--> due to except block we can prevent the unauthorized events(errors).


3.Finally:
--> after getting error or after resolution, forcefully if we want to execute any particular block 
of code then we use finally.(have to execute in both cases).

4.Else:
--> It is an alternative of try block.
--> If we find out any error inside try block interpreted will move forward towards else block
--> if code in else block correct then output will be generated and if incorrect it will show error.
--> if we get eror in try block then it will move to else block and if no error in else block then it
will ignore the error of the try block and else block will be executed if correct.

'''

'''
EXCEPTION HANDLING APPROACHES

--> Specific exception handling
--> Generic exception handling
--> Default exception handling
'''

'''
Specific expection handling:
-->you know the type of error
--> If we are aware of the error or the exception then we can go with 'specific'

try:
  problem
  satatement
except ErrorName:
  resolution/
  solution code

-->

'''

# n1,n2=21,0
# # print(n1/n2) ##error  not execute further

# try:
#     ##problem statement
#     result=n1/n2
#     print(result)
# except ZeroDivisionError:
#     ##solution code
#     print('Please do not choose 0 as the second number!')

# print('Code after try except-01')
# print('Code after try except-02')
# print('Code after try except-03')


##valueError
# a,b,c=1,2 ##throws error here only
# print(a,b,c) 

##here this code also throws nameerror as the value of a b  and c is not assigned
# try:
#     a,b,c=1,2 
# except ValueError:
#     print('For performing mvc number of variables should be equal to number of values')

# print(a,b,c) //error

##correct code

# try:
#     a,b,c=1,2 
# except ValueError:
#     print('For performing mvc number of variables should be equal to number of values')

# try:
#     print(a,b,c)
# except NameError:
#     print('Identifiers are not there in the memory!')

'''
##Exception: parent class name for all the errors
Generic Exception Hnadling:
--It is a type of exception handling approach in which there is no need to pass any particular excetion
class name instead we can use parent exception class called 'Exception'.

--> Using generic exception handling we can not handle keyboard interruption.
'''

# try:
#     a,b,c=1,2 
# except Exception:
#     print('For performing mvc number of variables should be equal to number of values')

# try:
#     print(a,b,c)
# except Exception:
#     print('Identifiers are not there in the memory!')

##generic
import time
# try:
#     while True:
#         print(time.time())
# except Exception:
#     print('loop got stopped!')


##same handling using specific
# try:
#     while True:
#         print(time.time())
# except KeyboardInterrupt:
#     print('loop got stopped!')

# using generic  exception was getting handled but showing keyborad interupt so
#  we use default so no keyboarddefault error shown:
'''
--DEFAULT EXCEPTION HANDLING
--> It is a type of exception handling in which we can handle all types of errors or exceptions 
except "SyntaxError" and "HardwareError".
'''
try:
    while True:
        print(time.time())
except:
    print('loop got stopped!')






    





