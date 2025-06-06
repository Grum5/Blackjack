from src.models.card import Card
from src.controllers.seed_generator import SeedGenerator


class Deck:
    '''
        Modelo para el Deck de las cartas
    '''

    def __init__(self, prng: SeedGenerator) -> None:
        ''' Constructor '''

        self.prng = prng
        self.cards = []
        self._create_deck()

    def reset(self) -> None:
        ''' Metodo para reiniciar el mazo '''

        self._create_deck()
        self.shuffle()

    def _create_deck(self) -> None:
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

        for suit in suits:
            for value in values:
                self.cards.append(Card(value, suit))

    def shuffle(self) -> None:
        ''' Metodo para revolver las cartas del deck '''

        for i in range(len(self.cards)):
            # Se obtiene un numero pseudoaletorio
            pseudonumber, _ = self.prng.get_seed()

            # Se normaliza para trabajar con el
            pseudo_normalized = (pseudonumber + 1.5) / 3.0
            j = int(pseudo_normalized * len(self.cards))
            j = max(0, min(j, len(self.cards) - 1))

            # Se revuelven las cartas
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def draw(self) -> Card:
        ''' Remueve y retorna la carta superior del mazo '''

        if self.cards:
            return self.cards.pop()

        raise IndexError("El mazo esta vacio.")

    @property
    def is_empty(self) -> bool:
        ''' Property para verificar que el mazo no este vacio '''

        return len(self.cards) == 0
