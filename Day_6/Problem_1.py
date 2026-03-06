'''
Generate Repeating Digit Series
'''
class Solution:

    def generate_series(self, n):
        series = []
        num=0

        for i in range(n):
            num=num*10+2
            series.append(num)

        return series    
        