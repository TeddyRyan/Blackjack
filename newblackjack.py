import random

class Card:
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value
def print_cards(cards, reveal):
    for card in cards:
        print(card.value + " of " + card.suit)
def blackjack_game(deck):
    
    #participant hands
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0

    #dealing player card 1
    player_card = random.choice(deck)
    player_hand.append(player_card)
    deck.remove(player_card)


    #dealing player card 2
    player_card = random.choice(deck)
    player_hand.append(player_card)
    deck.remove(player_card)


    print("Player has: ")
    print_cards(player_hand, True)
    #print("Player's card score is: {score}".format())


    dealer_card = random.choice(deck)
    dealer_hand.append(dealer_card)
    deck.remove(dealer_card)

   

    dealer_card = random.choice(deck)
    dealer_hand.append(dealer_card)
    deck.remove(dealer_card)

    print("Dealer has: ")
    print_cards(dealer_hand, True)

    

    return deck

if __name__ == '__main__':
    suits = ["Spades", "Hearts", "Clubs", "Diamonds"]
    suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    cards_values = {"A": 11, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
    deck = []
    for suit in suits:
        for card in cards:
            deck.append(Card(suit, card, cards_values[card]))
    blackjack_game(deck) 