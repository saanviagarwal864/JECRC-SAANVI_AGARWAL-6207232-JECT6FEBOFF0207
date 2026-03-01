'''
Password Strength Checker
'''
class DefaultSolution:

    def check_password_strength(self, password):

        if len(password) < 6:
            return "Weak Password"

        has_digit = False

        for ch in password:
            if ch.isdigit():
                has_digit = True
                break

        if has_digit:
            return "Strong Password"
        else:
            return "Moderate Password"