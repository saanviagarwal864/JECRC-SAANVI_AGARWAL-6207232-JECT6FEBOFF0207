'''
Hospital Bed Allocation Optimization
'''
class Solution:

    def solution(self, intervals):
        n=len(intervals)

        arrival=[]
        discharge=[]

        for i in range(n):
            arrival.append(intervals[i][0])
            discharge.append(intervals[i][1])

        arrival.sort()
        discharge.sort()

        i=0
        j=0
        beds=0
        max_beds=0

        while i<n and j<n:
            if arrival[i]<discharge[j]:
                beds+=1
                if beds>max_beds:
                    max_beds=beds
                i+=1
            else:
                beds-=1
                j+=1

        return max_beds    
