import random
import os

class Card:
    def __init__(self, suit, value, card_value):
        self.suit = suit
        self.value = value
        self.card_value = card_value
def print_cards(cards, reveal):
    for card in cards:
        print(card.value + " of " + card.suit)
def __repr__(self):
    print(deck)
def clear():
    os.system("clear")
def blackjack_game(deck):
    
    #participant hands
    player_hand = []
    dealer_hand = []
    player_score = 0
    dealer_score = 0
    player_blackjack = False
    dealer_blackjack = False

    #dealing dealer card 1
    dealer_card = random.choice(deck)
    dealer_hand.append(dealer_card)
    deck.remove(dealer_card)

    dealer_score += dealer_card.card_value

    print("Dealer has: ")
    print_cards(dealer_hand, True)

    #dealing dealer card 2
    dealer_card = random.choice(deck)
    dealer_hand.append(dealer_card)
    deck.remove(dealer_card)
    
    print("? of ?s")
    print("Dealer's card score is: {score} + ?".format(score=dealer_score))

    dealer_score += dealer_card.card_value

    input("[hit enter to continue.]")

    #dealing player card 1
    player_card = random.choice(deck)
    player_hand.append(player_card)
    deck.remove(player_card)

    player_score += player_card.card_value

    #dealing player card 2
    player_card = random.choice(deck)
    player_hand.append(player_card)
    deck.remove(player_card)

    player_score += player_card.card_value
    #player_score = 21

    print("Player has: ")
    print_cards(player_hand, True)
    print("Player's card score is: {score}".format(score=player_score))

    if (len(player_hand) == 2) and (player_score == 21):
        player_blackjack = True
        print("*************************")
        print("Player has blackjack!!!!!")
        print("*************************")
    if (len(player_hand) == 2) and (player_score > 21):
        player_score -= 10

    choice = ""
    while choice != "s":
        if player_blackjack == True:
            input("[hit enter to continue.]")
            break
        choice = input("Do you want to hit or stand? [h/s]: ").lower()
        #print(choice)
        if choice == "h":
            player_card = random.choice(deck)
            player_hand.append(player_card)
            deck.remove(player_card)

            player_score += player_card.card_value
            
            print("Player now has:")
            print_cards(player_hand, True)
            print("Player's score is now: {score}".format(score=player_score))


            if player_score > 21:
                print("You lose!")
                break

        elif choice == "s":
            break
        
        else:
            print("You must hit or stand. [h/s]")

    if player_score <= 21:
        print("Dealer reveals that he has:")
        print_cards(dealer_hand, True)
        print("Dealer's score is: {score}".format(score=dealer_score))

        while dealer_score <= 21:
            if (len(dealer_hand) == 2) and (dealer_score == 21):
                dealer_blackjack = True
                print("Dealer has blackjack!")
                break
            input("[hit enter to contine.]")
            if dealer_score == 21:
                print("Dealer stands!")
                break
            elif dealer_score > player_score:
                print("Dealer stands!")
                break
            elif dealer_score < player_score:
                print("Dealer hits!")
                dealer_card = random.choice(deck)
                dealer_hand.append(dealer_card)
                deck.remove(dealer_card)
                
                dealer_score += dealer_card.card_value
                
                print("Dealer now has:")
                print_cards(dealer_hand, True)
                print("Dealer's score is: {score}".format(score=dealer_score))
        
        if dealer_score > 21:
            print("Dealer busts!!!")  
        if (dealer_score > 21) and (player_score <= 21):
            print("Player wins!!!")
        if (player_score > 21) and (dealer_score <= 21):
            print("Dealer wins!!!")
        if (player_score <= 21) and (dealer_score <= 21) and (player_score > dealer_score):
            print("Player wins!!!")
        if (player_score <= 21) and (dealer_score <= 21) and (dealer_score > player_score):
            print("Dealer wins!")
        if (player_score <= 21) and (dealer_score <= 21) and (dealer_score == player_score):
            print("It's a tie!!!")
    else:
        print("Game over!!!")
    
    input("[hit enter to clear.]")
    clear()

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