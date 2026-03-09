'''
Circular Array Rotation Equilibrium
'''
class Solution:
    def count_equilibrium_rotations(self, arr):
        n = len(arr)
        count = 0
        for r in range(n):
            found=False
            for i in range(n):
                left_sum=0
                right_sum=0
                for j in range(i):
                    left_sum+=arr[j]

                for j in range(i+1,n):
                    right_sum+=arr[j]

                if left_sum==right_sum:
                    found=True
                    break

            if found:
                count+=1

            last=arr.pop() ##rotation inserted last element to first
            arr.insert(0,last)
            
        return count