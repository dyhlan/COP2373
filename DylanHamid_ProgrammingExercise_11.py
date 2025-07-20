# Dylan Hamid
# Programming Exercise 11
# Using the Deck object presented in Section 11.5, write a game program that deals a Poker hand of five cards.
# Then prompt the user to enter a series of numbers (for example: 1, 3, 5)
# that selects cards to be replaced during a draw phrase.
# Then print the result of drawing the new cards.

import random

# Class for a deck of cards.
class Deck():

    # Initializes all attributes for deck.
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        self.cards_in_play_list = []
        self.discards_list = []
        random.shuffle(self.card_list)

    # Reshuffles deck if needed, then deals a card to the user.
    def deal(self):
        if len(self.card_list) < 1:
            random.shuffle(self.discards_list)
            self.card_list = self.discards_list
            self.discards_list = []
            print('Reshuffling...!!!')
        new_card = self.card_list.pop()
        self.cards_in_play_list.append(new_card)
        return new_card

    # Puts all cards in play into the discard list.
    def new_hand(self):
        self.discards_list += self.cards_in_play_list
        self.cards_in_play_list.clear()


def main():
    # Initializes variables.
    # ranks and suits for the rank and suit of the to be drawn card
    # user_deck for the object of deck to be used by user, and user_hand for the user's hand
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    user_deck = Deck(52)
    user_hand = []

    # Dealing user 5 cards, and displaying to user.
    for card in range(5):
        # Determining the card's rank and suit
        deck = user_deck.deal()
        card_rank = deck % 13
        card_suit = deck // 13

        # Displaying to user
        print(f"{card + 1}. {ranks[card_rank]} of {suits[card_suit]}")

        # Adding to user's hand, to be potentially replaced later.
        user_hand.append(f"{ranks[card_rank]} of {suits[card_suit]}")

    # Calling replace_cards to allow user to replace cards, assigning to new_hand
    new_hand = replace_cards(user_hand, user_deck, ranks, suits)

    # Printing user's new hand
    for card in new_hand:
        card_index = new_hand.index(card) + 1

        print(f"{card_index}. {card}")


# Replaces cards
def replace_cards(hand, deck, ranks, suits):
    # Initializing variables brought over from main()
    ranks = ranks
    suits = suits
    hand = hand

    # Prompting user to replace cards.
    cards_to_replace = (input('Please enter the index for which card(s) you would like to replace, separated'
                              ' by comma.\n'
                              'If you would like to replace no cards, please type "0": ')).split(',')

    # Replacing each card user wanted to replace.
    for card in cards_to_replace:

        # Will skip loop if user entered a non-integer value.
        try:
            replaced_card = int(card) - 1

            # Will skip loop if user entered a value out of bounds of the cards_to_replace list.
            if replaced_card < 0 or replaced_card > 4:
                continue

            # Replaces the card
            else:
                # Determining new card's rank and suit
                card_value = deck.deal()
                card_rank = card_value % 13
                card_suit = card_value // 13

                # Replacing the card.
                new_card = f'{ranks[card_rank]} of {suits[card_suit]}'
                hand[replaced_card] = new_card

        # If user enter's non-integer value
        except:
            print("ERROR: Non-integer found. Ignoring non-integer.")
            continue

    # Returning user's hand with the replaced cards to main()
    return hand


main()