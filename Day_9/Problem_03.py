'''
Maximum Alternating Subarray Score
'''
class Solution:
    def max_alternating_score(self, arr):
        max_score=0
        for i in range(len(arr)):
            score=0

            for j in range(i,len(arr)):
                if j%2==0:
                    score+=arr[j]
                else:
                    score-=arr[j]
                
                max_score=max(max_score,score)
                
        return max_score