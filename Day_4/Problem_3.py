'''
Factory Production Defect Analyzer
'''
class Solution:

    def count_defective_products(self, total_products):
        ## Write your code here
        defective_products=0
        if total_products<=0:
            return 'Invalid Production Count'
        else:
            defective_products=total_products//5
            
        return defective_products        