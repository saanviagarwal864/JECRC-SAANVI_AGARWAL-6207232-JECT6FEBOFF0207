class Car:
    ## Below variables are known as "Properties/States/Members"
    wheelers = 4
    engine = 'Petrol'
    base_speed = '40kmph'
    max_speed = '120kmph'
    gears = 4

    def __init__(self, air_bags, security, base_budget, varient, total_sale):
        self.air_bags = air_bags
        self.security = security
        self.base_budget = base_budget
        self.varient = varient
        self.total_sale = total_sale

    ## functionality
    def display_properties(self):
        print({
            'wheelers' : self.wheelers,
            'engine' : self.engine,
            'base_speed' : self.base_speed,
            'max_speed' : self.max_speed,
            'gears' : self.gears,
            'air_bags' : self.air_bags,
            'security' : self.security,
            'base_budget' : self.base_budget,
            'varient' : self.varient,
            'total_sale' : self.total_sale,
        })


    @classmethod    ## to make a class method @classmethod need to used otherwise it will become an object method
    def update_gears(cls, new_gears):
        cls.gears = new_gears
        print(f'No of Gears: {cls.gears}')       


    def update_base_speed(self, new_speed):
        self.base_speed = new_speed
        print(f'New Base Speed: {self.base_speed}') 


    def update_max_speed(self, max_speed):
        self.max_speed = max_speed
        print(f'New Max Speed: {self.max_speed}')  


               


TATA = Car(True, 'Level 5', '2L', 12, 100000)
print('Properties before updation: ')
TATA.display_properties()
print()


print('Properties after updation: ')
TATA.update_base_speed('60kmph')
TATA.update_max_speed('180kmph')
TATA.update_gears(5)
print()
TATA.display_properties()

mahindra = Car(True, 'Level 4', '4L', 20, 250000)
mahindra.display_properties()









# TATA = Car()
# TATA.engine = ['Petrol', 'Diesel', 'EV']  ## if we add properties or change exisitng ones using object then that will be shown in object only
# TATA.air_bags = True
# TATA.no_of_air_bags = 4
# TATA.base_budget = '2L'
# TATA.no_of_varient = 12


# def __init__(self, air_bags):
#     self.air_bags = air_bags


## constructor  (__init__) -- initialise the state of an object i.e to add properties in object , it ia a constructor magic method 

'''
class ClassName:
    properties

    def __init__(self, arg1, arg2, arg3, ..., argn):
        self.arg1 = arg1
        self.arg2 = arg2
        ....
        self argn = argn

'''