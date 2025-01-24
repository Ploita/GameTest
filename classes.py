import numpy as np

class deck_class():
    def __init__(self):
        self.cards = ['Duke', 'Assassin', 'Captain', 'Ambassador', 'Contessa'] * 3
    
    def draw(self, n: int):
        drawned_cards = np.random.choice(self.cards, n)
        for a in drawned_cards:
            self.cards.remove(a)

        return drawned_cards


class player_class():
    def __init__(self, deck: deck_class):
        self.coins = 2
        self.n_cards = 2
        self.cards = [deck.draw(2)]