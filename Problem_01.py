'''
Question 1:
E-Commerce Order Revenue Analyzer
'''
class Solution:

    def city_revenue(self, orders):
        revenue_dict = {}
        for order in orders:
            city = order['city']
            amount = order['amount']

            if city in revenue_dict:
                revenue_dict[city] += amount
            else:
                revenue_dict[city] = amount
        city_with_highest_rev = None
        highest_revenue = 0

        for city in revenue_dict:
            if revenue_dict[city] > highest_revenue:
                highest_revenue = revenue_dict[city]
                city_with_highest_rev  = city

        return [revenue_dict, city_with_highest_rev]
