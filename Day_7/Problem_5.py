'''
Warehouse Load Balancing
'''
class Solution:
    def solution(self, machines):
        total=0
        for i in machines:
            total+=i
        n=len(machines)
        target=total//n

        moves=0
        for i in machines:
           moves=max(moves,i-target)

        return moves     