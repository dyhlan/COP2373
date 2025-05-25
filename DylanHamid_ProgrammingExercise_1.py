# Dylan Hamid
# Programming Exercise 1
# Write an application to pre-sell a limited number of cinema tickets.
# Each buyer can buy up to 4 tickets. No more than 20 tickets can be sold total.
# Prompt the user for the desired number of tickets and then
# display the number of remaining tickets after their purchase.
# Repeat until all tickets have been sold. Then display the total number of buyers.

from itertools import repeat


# Calls ticket_seller, then returns number of buyers.
def main():
    # Calls ticket_seller, assigns return value to number_of_buyers
    number_of_buyers = ticket_seller()

    # Displays number of buyers.
    print(f'There are {number_of_buyers} buyers.')


# Pre-sells the tickets and returns value to main.
def ticket_seller():
    # Initializing accumulators.
    # number_of_buyers is the return value, how many sales are made.
    # tickets_sold is used to control while loop.
    number_of_buyers = 0
    tickets_sold = 0

    # Initialize variable. Displays number of tickets left after a sale.
    number_of_tickets = 20

    # Loops until all 20 tickets are sold.
    while(tickets_sold < 20):
        # Catches if user doesn't input an integer.
        try:
            # Prompts user
            ticket = int(input("How many tickets would you like? "))

            # Adds ticket to total ticket_sold.
            tickets_sold += ticket

            # Ensures sale of 0 tickets doesn't accumulate number_of_buyers.
            if(ticket == 0):
                # Resets tickets_sold to value before this loop.
                tickets_sold -= ticket

            # Desired statement.
            # Accumulates number_of_buyers, and calculates how many tickets are left.
            elif(ticket <= 4 and tickets_sold <= 20):
                number_of_buyers += 1
                number_of_tickets -= ticket

                #Displays how many tickets are left.
                print(f'There are {number_of_tickets} tickets left.')

            # Runs if user tries to buy too many tickets, or tries to buy more tickets than what is left.
            else:
                print("ERROR: Only 20 tickets max can be bought, 4 per buyer. Please try again.")

                # Resets tickets_sold to value before this loop.
                tickets_sold -= ticket

        # Catch for user entering a non-integer when prompted.
        except:
            print('ERROR: Number not entered. Please try again.')

    return number_of_buyers


main()

