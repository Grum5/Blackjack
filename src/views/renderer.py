import pygame
from src.models.deck import Deck
from src.models.player import Player
from src.models.dealer import Dealer
from src.views.screen import Screen
from src.views.card_renderer import CardRenderer

from typing import Tuple


class Renderer:

    def __init__(self, screen: Screen) -> None:
        ''' Constructor '''

        pygame.font.init()

        self.screen = screen
        self.card_render = []
        self.font = pygame.font.SysFont("Arial", 20)
        self.spacing = 100
        self.y_player = 625
        self.y_dealer = -100

    def draw_hand(self, name: str, hand: object) -> None:
        ''' Metodo para dibujar una mano en pantalla '''

        if name == "dealer":
            face_up = False
            y_pos = self.y_dealer

        elif name == "player":
            face_up = True
            y_pos = self.y_player

        for i, card in enumerate(hand.cards):
            x = 10 + i * self.spacing

            self.card_render.append(CardRenderer(card))

            self.card_render[i].draw(
                screen=self.screen.get_surface(),
                pos=(x, y_pos),
                face_up=face_up
            )

    def draw_deck(self, deck: Deck) -> None:
        ''' Metodo para dibujar el deck '''

        if not deck.is_empty:

            # Cargar la primer carta del mazo
            self.card_render.append(CardRenderer(deck.cards[0]))

            self.card_render[0].draw(
                screen=self.screen.get_surface(),
                pos=(150, 275),
                face_up=False
            )

    def draw_instructions(self) -> None:
        ''' Dibuja las instrucciones sobre los controles '''

        instructions = [
            "Teclas:",
            "H - Pedir carta,",
            "S - Plantarse,",
            "Q - Salir",
        ]

        x = 50
        y = 580

        padding = 10

        for i, text in enumerate(instructions):
            text_width = self.font.size(text)[0]
            self.draw_text(text, (x, y))
            x += text_width + padding

    def draw_text(self, text: str, pos: Tuple[int, int]) -> None:
        ''' Metodo para renderizar texto en pantalla '''

        text_surface = self.font.render(text, True, (255, 255, 255))
        surface = self.screen.get_surface()

        surface.blit(text_surface, pos)

    def render_all(self, player: Player, dealer: Dealer, deck: Deck) -> None:
        ''' Metodo para renderizar todos los elementos en pantalla '''

        # Se dibuja el mazo y las manos
        self.draw_deck(deck)
        self.draw_hand(player.name, player.hand)
        self.draw_hand(dealer.name, dealer.hand)

        # Se dibujan los controles
        self.draw_instructions()
