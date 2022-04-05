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
        #self.show()
        self.shuffle()
    def build(self):
        for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
            for value in range(2,15):
                self.cards.append(Card(suit, value))
    #def show(self):
        #for card in self.cards:
            #card.show()
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
        for card in self.cards:
            card.show()
    def draw_card(self):
        Card.show(self.cards[-1])
        return self.cards.pop()
 
        

#class Dealer: #Rules for how Dealer must play.
#class Player: #Processes player decisions.

#card = Card("Hearts", 5)
#card.show()
deck = Deck()
print(deck.draw_card())