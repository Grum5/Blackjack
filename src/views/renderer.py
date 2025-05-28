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
        self.font = pygame.font.SysFont(None, 36)

    def draw_hand(self, name: str, hand: object, hide_first_card: bool = False) -> None:
        ''' Metodo para dibujar una mano en pantalla '''

        y_pos = self.y_dealer if name == "dealer" else self.y_player
        self.card_render = []

        for i, card in enumerate(hand.cards):
            x = 10 + i * self.spacing

            self.card_render.append(CardRenderer(card))

            # Solo la primera carta del dealer se oculta si hide_first_card es True
            face_up = not (hide_first_card and i == 0 and name == "dealer")

            self.card_render[i].draw(
                screen=self.screen.get_surface(),
                pos=(x, y_pos),
                face_up=face_up
            )

    def draw_deck(self, deck: Deck) -> None:
        ''' Metodo para dibujar el deck '''

        if not deck.is_empty:
            # Cargar la primer carta del mazo
            card_render = CardRenderer(deck.cards[0])

            card_render.draw(
                screen=self.screen.get_surface(),
                pos=(150, 275),
                face_up=False
            )

    def draw_text(self, text: str, position: tuple, color: tuple = (255, 255, 255)) -> None:
        ''' Método para dibujar texto en la pantalla '''
        text_surface = self.font.render(text, True, color)
        self.screen.get_surface().blit(text_surface, position)

    def render_all(self, player: Player, dealer: Dealer, deck: Deck, 
                  game_state: str, winner: str = None) -> None:
        ''' Metodo para renderizar todos los elementos en pantalla '''

        # Se dibuja el mazo
        self.draw_deck(deck)

        # Se dibujan las manos (ocultando la primera carta del dealer si es el turno del jugador)
        hide_dealer_card = game_state == "player_turn"
        self.draw_hand(player.name, player.hand)
        self.draw_hand(dealer.name, dealer.hand, hide_dealer_card)

        # Mostrar puntajes
        player_score = player.get_score()
        self.draw_text(f"Jugador: {player_score}", (10, 550))

        # Mostrar puntaje del dealer solo si no estamos ocultando su primera carta
        if not hide_dealer_card:
            dealer_score = dealer.get_score()
            self.draw_text(f"Dealer: {dealer_score}", (10, 50))

        # Mostrar instrucciones según el estado del juego
        if game_state == "player_turn":
            self.draw_text("Presiona H para pedir carta, S para plantarte", (10, 700))
        elif game_state == "game_over":
            # Mostrar resultado
            if winner == "player":
                self.draw_text("¡Has ganado!", (200, 350), (0, 255, 0))
            elif winner == "dealer":
                self.draw_text("Has perdido", (200, 350), (255, 0, 0))
            else:
                self.draw_text("Empate", (200, 350), (255, 255, 0))
            
            self.draw_text("Presiona R para jugar otra ronda", (10, 700))
