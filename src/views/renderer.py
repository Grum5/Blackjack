import pygame
from src.models.deck import Deck
from src.models.player import Player
from src.models.dealer import Dealer
from src.views.screen import Screen
from src.views.card_renderer import CardRenderer


class Renderer:

    def __init__(self, screen: Screen) -> None:
        ''' Constructor '''

        self.screen = screen
        self.card_render = []
        self.spacing = 100
        self.y_player = 600
        self.y_dealer = 100

    def draw_hand(self, name: str, hand: object) -> None:
        ''' Metodo para dibujar una mano en pantalla '''

        if name == "Dealer":
            face_up = False
            y_pos = self.y_dealer

        else:
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

    def render_all(self, player: Player, dealer: Dealer, deck: Deck) -> None:
        ''' Metodo para renderizar todos los elementos en pantalla '''

        # Se dibuja el mazo y las manos
        self.draw_deck(deck)
        self.draw_hand(player.name, player.hand)
        self.draw_hand(dealer.name, dealer.hand)
