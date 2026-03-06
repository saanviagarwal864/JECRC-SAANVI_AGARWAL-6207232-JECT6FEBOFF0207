class Car:
    ## Below variables are known as "Properties/States/Members"
    wheelers = 4
    engine = 'Petrol'
    base_speed = '40kmph'
    max_speed = '120kmph'
    gears = 4

## Below instances are called as objects 
TATA = Car()

## by following below approach, we can aslo add some properties inside an object

TATA.air_bags = True
TATA.security = 'Level 5'


# print(TATA)  ## output --> <__main__.Car object at 0x00000210140086E0> 

## For accessing the properties, we have to follow the below syntax:
print('Properties for TATA:')

print(f'No of wheelers: {TATA.wheelers}')
print(f'Engine Type: {TATA.engine}')
print(f'Base Speed:{TATA.base_speed}')
print(f'Max Speed: {TATA.max_speed}')
print(f'No of manual gears: {TATA.gears}')
print(f'Air Bags: {TATA.air_bags}')
print(f'Security: {TATA.security}')
print()

Mahindra = Car()
print('Properties for Mahindra:')

print(f'No of wheelers: {Mahindra.wheelers}')
print(f'Engine Type: {Mahindra.engine}')
print(f'Base Speed:{Mahindra.base_speed}')
print(f'Max Speed: {Mahindra.max_speed}')
print(f'No of manual gears: {Mahindra.gears}')


suzuki = Car()
toyota = Car()