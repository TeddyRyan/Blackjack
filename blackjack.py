import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def show(self):
        print("{value} of {suit}.".format(value=self.value, suit=self.suit))

class Deck: 
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()
    def build(self):
        for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
            for value in range(1,14):
                self.cards.append(Card(suit, value))
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
    def draw_card(self):
        return self.cards.pop()

class Player: #this is where the inputs will be????
    def __init__(self, name):
       self.name = name
       self.hand = []
       self.draw()
       self.draw()
       print("{name} has:".format(name=self.name))
       self.show_hand()
    #def __repr__(self):
        #print("{name} has a hand of {hand}".format(name=self.name, hand=self.hand))
    def draw(self):
        self.hand.append(deck.draw_card())
        return self.hand
    def show_hand(self):
        for card in self.hand:
            card.show()

#class Dealer: #Rules for how Dealer must play.

deck = Deck()
#card = deck.draw_card()
#card.show()
player = Player(input("What is your name? "))
