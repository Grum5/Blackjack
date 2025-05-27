from typing import List
from src.models.card import Card


class Hand:

    def __init__(self) -> None:
        ''' Constructor '''

        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        ''' Metodo para agregar una carta a la mano '''

        self.cards.append(card)

    def clear(self) -> None:
        ''' Metodo para vaciar la mano de cartas '''

        self.cards.clear()

    def get_cards(self) -> List[Card]:
        ''' Metodo que retorna la mano de cartas '''

        return self.cards

    def get_value(self) -> int:
        ''' Metodo para contar el valor total de la mano '''

        # Contadorres
        value = 0
        aces = 0

        for card in self.cards:

            # Se obtiene el valor de la carta
            rank = card.value

            # Si es figura vale 10 puntos
            if rank in ['J', 'Q', 'K']:
                value += 10

            # Si es un AS puede valer 11 o 1, por defecto se considera 11
            elif rank == 'A':
                value += 11
                aces += 1

            # Se da valor dependiendo el numero de la carta
            else:
                value += int(rank)

        # Si se excede el valor de 21, se baja el valor de algunos ases
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1

        return value

    def is_burst(self) -> bool:
        ''' Metodo que verifica si ya se paso de el valor de 21 '''

        return self.get_value() > 21

    def is_blackjack(self) -> bool:
        ''' Metodo que verifica si la mano ya es 21 con 2 cartas '''

        return self.get_value() == 21 and len(self.cards) == 2
