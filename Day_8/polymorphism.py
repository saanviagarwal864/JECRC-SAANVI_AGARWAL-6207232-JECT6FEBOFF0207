'''
Polymorphism:
--> using the same method name or operator to perform two or more different operations
'''
# class Temp:
#     def sum(self,a,b):
#         print(a+b)    

#     def sum(self,a,b,c):
#         print(a+b+c)
    
# obj=Temp()
# obj.sum(10,20)  ##it will not excute as it will take the new one sum and wants 3 parameters second one will override the first one

'''
in python if we want to perform method overloading then it will act as a method overriding.
in other programming languages, based upon no.of arguments the respective method block
will get executed but in python it never happens.
'''

##Method overriding--> phenomenon of overriding the prev method's address with the latest one.

class Temp:
    def sum(self,a,b):
        print(a+b)    

    add_two_nums=sum    ##monkey patching

    def sum(self,a,b,c):
        print(a+b+c)
    
obj=Temp()
obj.sum(10,20,30)
obj.add_two_nums(20,10)

''''
Monkey Patching
--> it is a process of storing the previous method's address inside a variable before overring the method
area's address.Using that var, we can access the prev method's method area

--> using monkey patching we can do method overloading in python normally it is not possible
''' 

