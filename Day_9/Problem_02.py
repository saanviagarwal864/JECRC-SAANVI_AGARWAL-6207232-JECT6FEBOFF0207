'''
Unique Pair Distance Sum
'''
class Solution:

    def pair_distance_sum(self, positions, k):
        n = len(positions)
        total = 0

        for i in range(n):
            for j in range(i+1,n):
                dist=positions[i]-positions[j]

                if dist<0:
                    dist=-dist

                if dist%k==0:
                    total+=dist

        return total