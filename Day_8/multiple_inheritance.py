'''
Multiple inheritance:
-->parallel order or concurrent way to derieve the properties
--> type of inheritance in which the properties will be derived from multiple parent class to a single
child class.
'''
class Parent_1:
    a=10
class Parent_2:
    b=100
class Parent_3:
    c=300
class Parent_4:
    d=1000

class Child(Parent_1,Parent_2,Parent_3,Parent_4):
    pass

###here we did not make object as we only want to access the properties and there is no method that uses self so no need of object
print(Child.a,Child.b,Child.c,Child.d)


