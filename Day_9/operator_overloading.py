'''
----Operator Overloading:---
It is a phenomenon of making the operators to work on user-defined data
 types by invoking respective magic methods.

-- Magic Method/Dundar:----
It is a special type of method in which double underscore will be there a the starting and ending of
the method's name.

---Example:
1. __add__,
2. __sub__,
3. __mul__,
4. __floordiv__,
5. __truediv__,
6. __mod__

--> If we do not use operator overloading what will happen?
--- For using the operators inside user-defined data types we have to use operator overloading.

-- SYNTAX:--

class ClassName:
    def __init__(self,val):
       self.val=val
    def __add__(self, other_obj):
       return self.val + other_obj
    
    obj1=ClassName(val1)
    obj2=ClassName(val2)
    print(obj1 + obj2)    ##obj1.__add__(obj2)

'''

class MyDT:
    def __init__(self,val):
        self.val=val

    def __add__(self, other_obj): ##not applicable for more than two values
        return self.val + other_obj.val
    
    def __sub__(self, other_obj):
        return self.val - other_obj.val
    
    def __mul__(self, other_obj):
        return self.val * other_obj.val
    
    def __floordiv__(self, other_obj):
        return self.val // other_obj.val
    
    def __truediv__(self, other_obj):
        return self.val / other_obj.val
    
    def __mod__(self, other_obj):
        return self.val % other_obj.val
    
    def add(self, *other_obj): ##added for implementing packing concepts to add more than three values
        result=self.val
        for i in other_obj:
            result+=i.val
        return result
    
    def mul(self,*other):
        result=self.val
        for i in other:
            result*=i.val
        return result
    
    def sub(self,*other):
        result=self.val
        for i in other:
            result-=i.val
        return result
    


print(MyDT(10) + MyDT(30))   
print(MyDT(10) - MyDT(30))
print(MyDT(10) * MyDT(30))  
print(MyDT(10) // MyDT(30))   
print(MyDT(10) / MyDT(30))   
print(MyDT(10) % MyDT(30))   
print(MyDT(10.0) + MyDT(30))
# print(MyDT(10) + MyDT(30) + MyDT(40))  
##cannot do for three values here so we use packing concept and
#  introduce other or new method add to do it
print(MyDT.add(MyDT(10) , MyDT(30) , MyDT(40))) 

##similarly for sub and mul
print(MyDT.sub(MyDT(10) , MyDT(30) , MyDT(40)))  
print(MyDT.mul(MyDT(10) , MyDT(30) , MyDT(40)))  




'''
another method to do what we did i.e. making methods applicable for 
more than 2 or multiple values
'''
class MyDT:
    def __init__(self,val):
        self.val=val

    def __str__(self):
        return str(self.val)

    def __add__(self, *other_obj): 
        result=self.val
        for i in other_obj:
            result+=i.val
        return MyDT(result)
    
    def __sub__(self, *other_obj):
        result=self.val
        for i in other_obj:
            result-=i.val
        return MyDT(result)
    
    def __mul__(self, *other_obj):
        result=self.val
        for i in other_obj:
            result*=i.val
        return MyDT(result)
    
    def __floordiv__(self, other_obj):
        return self.val // other_obj.val
    
    def __truediv__(self, other_obj):
        return self.val / other_obj.val
    
    def __mod__(self, other_obj):
        return self.val % other_obj.val
    
    


print(MyDT(10) + MyDT(30))   
print(MyDT(10) - MyDT(30))
print(MyDT(10) * MyDT(30))  
print(MyDT(10) // MyDT(30))   
print(MyDT(10) / MyDT(30))   
print(MyDT(10) % MyDT(30))   
print(MyDT(10.0) + MyDT(30))
print(MyDT(10) + MyDT(30) + MyDT(40)) 
print(MyDT(10) - MyDT(30) - MyDT(40)) 
print(MyDT(10) * MyDT(30) * MyDT(40)) 













        
