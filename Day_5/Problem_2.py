'''
Shopping Discount System
'''
class Solution:
    def discount(self, total_amount, is_member):
        
        payment=0
        if total_amount>=5000:
            if is_member:
                payment=total_amount*0.80
            else:
                payment=total_amount*0.90
        else:
            if is_member:
                payment=total_amount*0.95

        return payment               