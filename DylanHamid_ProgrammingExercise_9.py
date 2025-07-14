# Dylan Hamid
# Programming Exercise 9
# Create a BankAcct Class that contains at least the following state information:
# name, account number, amount and interest rate.
# In addition to an __init__ method, the class should support methods for adjusting the interest rate,
# for withdrawing and depositing, and for giving a balance.
# You should also include a method to calculate the interest based on the number of days.
# Use the __str__ method to display balances and interest amounts.
# Create a test function to test the different methods in the BankAcct Class.


class BankAcct:

    # Initializing Bank Account attributes
    def __init__(self, account_name, account_number, account_amount, interest_rate):
        self.account_name = account_name
        self.account_number = account_number
        self.account_amount = account_amount
        self.interest_rate = interest_rate

    # Method to adjust interest rate
    def adjust_interest_rate(self):
        # Will loop if user enters a non float value.
        while True:
            try:
                # Prompting user for new interest rate to replace current interest rate.
                self.interest_rate = float(input('Please enter the new interest rate here: '))
                break

            # Triggers when non-float value is entered.
            except ValueError:
                print("ERROR: Number not entered. Please try again.")


    # Method to withdraw money from the account
    def withdraw_money(self):
        # Will loop if user enters a non int value.
        while True:
            try:
                # Prompting user for what they would like to withdraw, and subtracting from what is in the
                # account.
                self.account_amount = self.account_amount - int(input('How much money would you like to withdraw? '))
                break

            # Triggers when non-int value is entered.
            except ValueError:
                print("ERROR: Number not entered. Please try again.")

    # Method to deposit money from account
    def deposit_money(self):
        # Will loop if user enters a non int value.
        while True:
            try:
                # Prompting user for what they would like to deposit, and adding to what is in the account.
                self.account_amount = self.account_amount + int(input('How much money would you like to deposit? '))
                break

            # Triggers when non-int value is entered.
            except ValueError:
                print("ERROR: Number not entered. Please try again.")

    # Method to display account balance
    def give_balance(self):
        # Prints the account amount.
        print(f'ACCOUNT BALANCE: {self.account_amount}')

    # Method to calculate interest based on days
    def calculate_interest(self):
        # Will loop if user enters a non int value.
        while True:
            try:
                # Prompting user for the time in days their bank account has been opened, then dividing by 365.
                # Dividing by 365 is needed for calculating interest.
                time = int(input('How many days has the account been opened? ')) / 365
                break

            # Triggers when non-int value is entered.
            except ValueError:
                print("ERROR: Number not entered. Please try again.")

        # Calculates the amount of interest accrued on the amount.
        # Does compound interest calculation, then subtracts the amount in bank account.
        interest_accrued = (self.account_amount * (1 + (self.interest_rate / 4)) ** (4 * time)) - self.account_amount

        # Displays to the user their accrued interest.
        print(f"In {time * 365:.0f} days, your bank account will have accrued ${interest_accrued:.2f} in interest.")

    # Method to display balances and interest amount
    def __str__(self):
        print(f'ACCOUNT AMOUNT: {self.account_amount}\n'
              f'INTEREST RATE: {self.interest_rate}')


def main():
    # Creating hard-coded instance of BankAcct for testing.
    test_account = BankAcct('TEST', 1, 100, .57)

    # Printing initial account balance and interest rate to user.
    test_account.__str__()

    # Prompting user to adjust their interest rate.
    test_account.adjust_interest_rate()

    # Prompting user to withdraw and deposit money from account, displaying the new balance for each transaction.
    test_account.withdraw_money()
    test_account.give_balance()
    test_account.deposit_money()
    test_account.give_balance()

    # Calculating the interest for a user inputted amount of time.
    test_account.calculate_interest()

    # Printing new account balance and interest rate to user.
    test_account.__str__()

main()