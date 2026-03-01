'''
Smart Parking Fee Management System
'''
class Solution:

    def calculate_parking_fee(self, hours):
        # Write your code here
        total_fee=0
        if hours<=0:
            return 'Invalid Parking Duration'
        else:
            if hours<=2:
                total_fee=20*hours
            elif hours<=5:
                total_fee=2*20 + (hours-2)*30
            else:
                total_fee=2*20+3*30+(hours-5)*50
        if total_fee>500:
            total_fee=total_fee*0.1
        return total_fee                        
        