from card import Card
from deck import Deck

class User:
    def __init__(self,name):
        self.name = name
        self.hand = []


    def draw(self, cards):
        self.hand.append(cards)
        return self