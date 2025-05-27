from src.models.card import Card
from src.models.prng.henon import Henon


class Deck:
    '''
        Modelo para el Deck de las cartas
        ¡¡¡ Falta implementar metodo shuffle !!!
    '''

    def __init__(self, prng: Henon):
        ''' Constructor '''

        self.prng = prng
        self.cards = self._create_deck()
        # self.shuffle()

    def _create_deck(self):
        '''
            Metodo privado
            - Crea el deck de cartas
        '''
        suits = ['hearts', 'spades', 'clubs', 'diamonds']
        values = [
            'A', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '10', 'J', 'Q', 'K'
        ]
        return [Card(value, suit) for suit in suits for value in values]
