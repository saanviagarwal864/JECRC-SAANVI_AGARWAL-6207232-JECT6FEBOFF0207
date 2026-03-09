'''
Hierarchical inheritance:
-->It is a type of inheritance in which the properties will be derived from single
class to multiple child class.
'''

class Parent:
    gold='2kg'
    silver='10kg'
    no_of_flats=12

class Youngest(Parent):
    name='Priya'

class Elder(Parent):
    my_name='saanvi'

class Middle(Parent):
    name='paridhi'

print(Youngest.gold)
print(Elder.no_of_flats)
print(Middle.silver)
    
