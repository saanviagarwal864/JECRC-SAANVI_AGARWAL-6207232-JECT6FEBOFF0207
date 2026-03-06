'''
Sum of Alternating Square Series
'''
class DefaultSolution:

    def sum_series(self, n):
        total = 0
        for i in range(1, n + 1):
            term = i * i
            if i <= 2:
                total += term
            else:
                if i % 2 == 1:
                    total -= term
                else:
                    total += term

        return total