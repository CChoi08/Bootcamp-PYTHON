from card import Card
import random

class Deck:


    def __init__( self ):
        suits = [ "spades" , "hearts" , "clubs" , "diamonds" ]
        self.cards = []

        for s in suits:
            for i in range(1,14):
                str_val = ""
                if i == 1:
                    str_val = "Ace"
                elif i == 11:
                    str_val = "Jack"
                elif i == 12:
                    str_val = "Queen"
                elif i == 13:
                    str_val = "King"
                else:
                    str_val = str(i)
                self.cards.append( Card( s , i , str_val ) )

    def show_cards(self):
        for card in self.cards:
            card.card_info()

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_top(self):
        dealt_cards = random.choice(self.cards)
        self.cards.remove(dealt_cards)
        return dealt_cards
