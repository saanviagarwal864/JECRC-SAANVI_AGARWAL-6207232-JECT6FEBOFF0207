'''
Encapsulation:
1. It is used to provide security to the data(data means variable/prop & methods present
inside a class).

How to provide security to the data?
 To provide security , we have to use access specifiers.
    1.public,
    2.protected(soft barrier '_'),
    3.private('__')

Access Specifier:
 It describes who can access the class members(properties & methods).


'''

##example for public access specifiers
# class Temp:
#     a,b,*c,d='HELLO' ##assigned using packing

#     def greeting(self):
#         print('Good Afternoon user: ')

# class C2(Temp):
#     pass

##example for protected access specifiers
# class Temp:
#     ##soft barrier so it can be easily broken
#     _a=10 ###we used underscore so it will act as protected
#     _b='PYTHON'
#     ##if we put double underscore then it will act as private

# obj=Temp()
# print(obj._b)
# print(obj._a)


##example for private access specifiers
# class Temp:
#     __a=100

#     def __status(self):
#         print('claas name is temp!')

    

# obj=Temp()
# print(obj.__a)
# obj.__status()
##cannot access


'''
How to access private specifiers?
3 methods
1.By using syntax,
2.get & set method,
3. by using @property decorator(setter)
'''

##by using syntax:
'''
obj_name/class_name._ClassName__property_name/__method_name (Accessing)
obj-name/class_name._ClassName__MemberName=NewValue (Modifying)


'''
##accessing
# print(obj._Temp__a)
# print(Temp._Temp__a)

# obj._Temp__status()
# # Temp._Temp__status() not working

# ##modifying

# obj._Temp__a='0123456789'
# print(obj._Temp__a)

# def newmethod(): ##made a new method outside class to modify status method
#     print('new method')

# obj._Temp__status=newmethod
# obj._Temp__status()


## by using  get & set method:

# class Temp:
#     __a=100

#     def __status(self):
#         print('class name is temp!')

#     def get(self):
#         print(self.__a)

#     def set(self,new_val):
#         self.__a=new_val

# obj=Temp()
# obj.get() #100
# print(obj._Temp__a) ##100
# obj.set(10)
# obj.get() #10
# print(obj._Temp__a) #10


#### By using @property decorator
class Temp:
    __a=100

    @property
    def getter(self): ##it acts as a property means variable not method
        print(self.__a)

    @getter.setter
    def set(self,new_val): ##it acts as a property means variable not method
        self.__a=new_val

obj=Temp()
obj.getter #100 can not use getter()
print(obj._Temp__a) #100
obj.set=1000 ##cannot call it but can assign value means not use obj.set()
obj.getter ##1000
print(obj._Temp__a)












