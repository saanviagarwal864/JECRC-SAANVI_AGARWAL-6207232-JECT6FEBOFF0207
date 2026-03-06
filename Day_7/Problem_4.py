'''
Find Missing Transaction ID
'''
class Solution:
    def solution(self, nums):
        actual_sum=0
        exp_sum=(len(nums)+1)*(len(nums)+2)//2
        for i in nums:
            actual_sum+=i
           
        return exp_sum-actual_sum        