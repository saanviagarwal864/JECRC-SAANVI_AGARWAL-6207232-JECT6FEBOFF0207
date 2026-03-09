'''
INHERITANCE:
1. Single level,
2. Multi-level,
3. Multiple,
4. Heirarchical,
5. Hybrid
'''

##Single Level


##PARENT CLASS OR SUPER CLASS
class Parent:
    bank_balance='54L'
    def __init__(self,members): ##parent class constructor
        self.members=members

    def desc(self):
        print('I am the parent class')

##CHILD CLASS OR SUB CLASS
class Child(Parent):
    def __init__(self, child_name,*args): ##child class constructor calling parent clss constructor from child class constructor
        super().__init__(args)
        self.child_name=child_name
    
    def display(self):
        super().desc()

# obj=Child()
# print(obj.bank_balance)
# obj.desc()
obj2=Child('Saanvi','Mom','Dad')
print(obj2.members)
print(obj2.child_name)
obj2.display()