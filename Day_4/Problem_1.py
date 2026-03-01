'''
ATM Withdrawal Simulation
'''
class DefaultSolution:

    def atm_withdrawal(self, pins, amount):
        balance = 10000
        correct_pin = 1234
        attempts = 0

        for pin in pins:
            if attempts == 3:
                break

            if pin == correct_pin:
                if amount > balance:
                    return "Insufficient Balance"
                else:
                    balance -= amount
                    return balance
            else:
                attempts += 1

        return "Account Blocked"