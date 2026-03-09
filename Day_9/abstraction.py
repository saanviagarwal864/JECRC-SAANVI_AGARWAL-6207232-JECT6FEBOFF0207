'''
Abstraction:
--> Hiding the internal implementation and displaying only the functionality to the end user.


Abstract Method:
--> If a method /function consists of only declaration not definition
    then it will be called as "Abstract Method"

Abstract Class:
--> If a class consists of atleast one abstract method then it is called  as "Abstract Class"
--> we cannot create an object from an abstract class

Concret CLass:
--> It consists of zero or no abstract method.

abc: Module
ABC: Abstract Base Class ##used to create a abstract class
abstractmethod:it is imported as a decorator to create abstract class
'''

from abc import ABC, abstractmethod

class ATM(ABC): ##abstract class
    def generate_pin(self):
        pass

    @abstractmethod
    def forget_pin(self):
        pass

    @abstractmethod
    def check_balance(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass

class SBI_ATM(ATM): ##concret vlass
    def generate_pin(self):
        print('It is used to generate ATM pin')

    def forget_pin(self):
        print('Not able to remember the pin!')

    def check_balance(self):
        print('No balance available')

    def withdraw(self):
        print('Do not waste your money')

    def deposit(self):
        print('Save your money and give to me')

obj=SBI_ATM() #until all the methods of the abstract class are defined in sbi class(concret class)
               #it will not run and show error
obj.check_balance()
obj.deposit()
obj.forget_pin()
obj.withdraw()
obj.generate_pin()