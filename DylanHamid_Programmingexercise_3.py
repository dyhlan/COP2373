# Dylan Hamid
# Programming Exercise 3
# Write a program asking the user for a list of their monthly expenses.
# When asking the user for their expenses, ask for the type of expense and the amount.
# Use the reduce method to analyze the expenses and display the total expense, the highest expense
# and the lowest expense.
# Label what the highest and lowest expense is.

from functools import reduce


def main():
    # Initializing lists to hold user's expenses.
    # One holds the amount, other holds amount and type.
    expense_amount_list = []
    expense_type_and_amount_list = []

    # Getting monthly expenses from user.
    # Loops until user enters "done".
    while True:
        # Catches and repeats if user either enters a non float for the expense amount, or enters a float <=0.
        try:
            # Prompting user for expense type and amount.
            expense_type = input("Please enter the type of expense: ")
            expense_amount = float(input("Please enter the amount of the expense: "))

            # Repeats loop preemptively if user enters an amount <=0
            if expense_amount <= 0:
                raise Exception("ERROR: Please enter a valid number (greater than 0) for expense amount.")
                continue
            else:
                pass

        # Repeats loop if user enters a non-float value for the amount.
        except:
            print("ERROR: Please enter a number greater than zero for the amount of the expense.")
            continue

        # Entering type and amount to a list to be appended to expense_type_and_amount at once.
        expense_type_and_amount = [expense_amount, expense_type]

        # Appending amount and type to expense_type_and_amount at once.
        expense_type_and_amount_list.append(expense_type_and_amount)

        # Appending the expense amount to its dedicated list for analyzing later.
        expense_amount_list.append(expense_amount)

        # Asks user for a codeword to break the loop.
        loop_breaker = input('Please enter "done" if you are done entering your monthly expenses. If not, enter'
                             ' any other key to enter another expense. ')

        # Breaks the loop if user enters the codeword. Continues if not.
        if loop_breaker.lower() == "done":
            break
        else:
            continue

    # Analyzing user's monthly expenses for:
    # 1. The total expenses, with just the amounts
    # 2. The expenses sorted ascending, with both the type and amount, by amount. Used for the lowest expense.
    # 3. The expenses sorted descending, with both the type and amount, by amount. Used for the highest expense.
    expense_total = reduce(lambda value_one, value_two: value_one + value_two, expense_amount_list)
    expenses_sorted_ascending = sorted(expense_type_and_amount_list, key=lambda amount: amount[0])
    expenses_sorted_descending = sorted(expense_type_and_amount_list, key=lambda amount: amount[0], reverse=True)

    # Displaying total amount, highest expense, and lowest expense.
    print(f'Total amount is ${expense_total:.2f}')
    print(f'The highest expense is {expenses_sorted_descending[0][1]}: ${expenses_sorted_descending[0][0]:.2f}')
    print(f'The lowest expense is {expenses_sorted_ascending[0][1]}: ${expenses_sorted_ascending[0][0]:.2f}')


main()