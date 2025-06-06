import pygame
from src.views.screen import Screen
from src.views.renderer import Renderer
from src.controllers.event_handler import EventHandler
from src.models.player import Player
from src.models.dealer import Dealer
from src.controllers.round_controller import RoundController
from src.controllers.seed_generator import SeedGenerator


class Game:
    '''
        Clase principal del juego
    '''

    def __init__(self) -> None:
        ''' Constructor '''
        
        # Inicializar pygame y sus módulos
        pygame.init()

        # Declarar las instancias necesarias del juego
        self.player = Player()
        self.dealer = Dealer()
        self.seed_generator = SeedGenerator()
        self.round_controller = RoundController(
            seed_generator=self.seed_generator,
            player=self.player,
            dealer=self.dealer
        )
        self.screen = Screen(500, 800, "Blackjack")
        self.renderer = Renderer(self.screen)
        self.event_handler = EventHandler()

        # Hacer invisible el mouse (No se usara)
        pygame.mouse.set_visible(False)

        self.running = True
        self.game_state = "waiting"  # Estados: waiting, player_turn, dealer_turn, game_over

    def run(self) -> None:
        '''
            Loop principal del juego
        '''

        while self.running:

            self.screen.fill()

            # Empieza una ronda, verifica si se esta esperando una acción
            if not self.event_handler.is_waiting:
                winner, is_blackjack = self.round_controller.start_round()
                if is_blackjack:
                    self.game_state = "game_over"
                else:
                    self.game_state = "player_turn"

            # Renderiza el estado actual del juego
            self.renderer.render_all(
                self.player, self.dealer, self.round_controller.deck, 
                self.game_state, self.round_controller.winner
            )

            # Procesa los eventos que suceden
            self.event_handler.process()

            # Manejar eventos de teclado
            if self.event_handler.hit and self.game_state == "player_turn":
                if self.round_controller.player_hit():
                    self.game_state = "game_over"

            if self.event_handler.stand and self.game_state == "player_turn":
                if self.round_controller.player_stand():
                    self.game_state = "game_over"

            if self.event_handler.restart and self.game_state == "game_over":
                self.game_state = "waiting"
                self.event_handler.wait_for_action = False

            if self.event_handler.quit:
                self.running = False

            self.screen.update()
