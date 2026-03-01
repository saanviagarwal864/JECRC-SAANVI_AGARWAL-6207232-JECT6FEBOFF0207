'''
Bank EMI Payment Tracker
'''
class Solution:

    def calculate_total_paid(self, months):
        ## write your code here
        total_amount=0
        if months<=0:
            return 'Invalid Duration'
        else:
            for i in range(0,months):
                if(total_amount>=50000):
                    return total_amount
                    break
                total_amount+=5000 
        return total_amount           