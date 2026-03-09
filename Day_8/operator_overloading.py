class Mydata:
    def __init__(self,val):
        self.val=val

    def __add__(self, another_obj):
        return self.val+another_obj.val
    
    ##self.val
    ##obj->self.val
    ##another_obj(obj2)-->obj2.val-->another_obj.val
    
obj1=Mydata(10)
obj2=Mydata(20)
print(obj1+obj2)