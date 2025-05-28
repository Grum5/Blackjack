from src.models.card import Card
from src.models.hand import Hand


class Player:

    def __init__(self, name: str = "player") -> None:
        ''' Constructor '''

        self.name = name
        self.hand = Hand()

    def add_card(self, card: Card) -> None:
        ''' Metodo para agregar una carta a la mano '''

        self.hand.add_card(card)

    def reset_hand(self) -> None:
        ''' Reinicio de la mano '''

        self.hand.clear()

    def get_score(self) -> int:
        ''' Obtiene el valor de la mano '''

        return self.hand.get_value()

    def is_bust(self) -> bool:
        ''' Verifica si se excede el valor de 21 '''

        return self.hand.is_burst()

    def has_blackjack(self) -> bool:
        '''
            Verifica tiene un As y una figura
            - Su mazo tiene 2 cartas con valor total de 21
        '''

        return self.hand.is_blackjack()
