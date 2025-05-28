import pygame
from src.models.card import Card
from typing import Tuple


class CardRenderer:

    CARD_SIZE = (200, 250)

    def __init__(
            self,
            card: Card,
            size: Tuple[int, int] = (100, 145)
    ) -> None:
        ''' Constructor '''

        self.card = card
        self.size = size
        self.image = self._load_image(card.sprite_path)
        self.back_image = self._load_image("resources/cards/card_back.png")

    def _load_image(self, path: str) -> pygame.Surface:
        ''' Metodo para cargar la imagen de la carta '''

        image = pygame.image.load(path).convert_alpha()
        return pygame.transform.smoothscale(image, CardRenderer.CARD_SIZE)

    def draw(
        self,
        screen: pygame.Surface,
        pos: Tuple[int, int], face_up: bool = True
    ) -> None:
        ''' Metodo para dibujar la carta '''

        img = self.image if face_up else self.back_image
        screen.blit(img, pos)
