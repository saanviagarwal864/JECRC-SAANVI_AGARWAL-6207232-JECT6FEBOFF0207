'''
Longest Continuous Increasing Subsequence
'''
class Solution:
    def solution(self, nums):
        max_len=1
        curr_len=1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                curr_len+=1
            else:
                curr_len=1

            if curr_len>max_len:
                max_len=curr_len

        return max_len                