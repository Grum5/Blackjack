import pygame
from typing import Optional


class Card:
    '''
        Modelo base para las cartas
    '''

    def __init__(
        self,
        value: str,
        suit: str,
    ) -> None:
        ''' Constructor '''

        self.value = value
        self.suit = suit
        self.sprite_path = self._build_sprite_path()

    def _build_sprite_path(self) -> str:
        val = self.value
        if val in [str(i) for i in range(2, 10+1)]:
            val = f"{int(val):02}"

        return f"resources/cards/card_{self.suit}_{val}.png"

    def name(self):
        ''' Retorna el nombre de la carta '''

        return f"{self.value}{self.suit}"
