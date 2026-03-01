'''
Remove Duplicate Transactions
'''
class Solution:
    def remove_duplicates(self, transactions):
        result=[]
        
        for i in range(len(transactions)):
            flag=False
            for j in range(len(result)):
                if transactions[i]==result[j]:
                    flag=True
                    break
                
            if not flag:
                result.append(transactions[i])   

        return result
                    