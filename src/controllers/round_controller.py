
from src.controllers.seed_generator import SeedGenerator
from src.models.player import Player
from src.models.dealer import Dealer
from src.models.deck import Deck
from typing import Optional, Tuple


class RoundController:

    def __init__(
            self, seed_generator: SeedGenerator,
            player: Player, dealer: Dealer
    ) -> None:
        ''' Constructor '''

        self.seed_generator = seed_generator
        self.deck = Deck(self.seed_generator)
        self.player = player
        self.dealer = dealer
        self.game_over = False
        self.winner = None

    def start_round(self) -> Tuple[Optional[str], bool]:
        ''' Metodo que inicializa la ronda '''

        # Se reinicia y revuelve el mazo y se reinician las manos
        self.deck.reset()  # Add this line to reset the deck
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.game_over = False
        self.winner = None

        # Se reparten 2 cartas a cada mano (un total de 4 cartas menos al deck)
        for _ in range(2):
            self.player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())

        # Verificar que el jugador y el dealer no tengan blackjack
        player_bj = self.player.hand.is_blackjack()
        dealer_bj = self.dealer.hand.is_blackjack()

        # Empate, ambos tiene blackjack
        if player_bj and dealer_bj:
            self.winner = None
            self.game_over = True
            return None, True

        # El jugador tiene blackjack
        elif player_bj:
            self.winner = "player"
            self.game_over = True
            return "player", True

        # El dealer tiene blackjack
        elif dealer_bj:
            self.winner = "dealer"
            self.game_over = True
            return "dealer", True

        # No hay blackjack, el juego continua
        else:
            return None, False
            
    def player_hit(self) -> bool:
        ''' Método para cuando el jugador pide una carta '''
        if self.game_over:
            return False
            
        # Añadir una carta a la mano del jugador
        self.player.add_card(self.deck.draw())
        
        # Verificar si el jugador se pasó de 21
        if self.player.is_bust():
            self.winner = "dealer"
            self.game_over = True
            return True
            
        return False
        
    def player_stand(self) -> bool:
        ''' Método para cuando el jugador se planta '''
        if self.game_over:
            return False
            
        # Ejecutar el turno del dealer
        return self.dealer_turn()
        
    def dealer_turn(self) -> bool:
        ''' Método para ejecutar el turno del dealer '''
        if self.game_over:
            return False
            
        # El dealer toma cartas hasta tener 17 o más
        while self.dealer.should_hit:
            self.dealer.add_card(self.deck.draw())
            
        # Determinar el ganador
        return self.determine_winner()
        
    def determine_winner(self) -> bool:
        ''' Método para determinar el ganador de la ronda '''
        if self.game_over:
            return False
            
        player_score = self.player.get_score()
        dealer_score = self.dealer.get_score()
        
        # Si el dealer se pasó de 21, gana el jugador
        if self.dealer.is_bust():
            self.winner = "player"
        # Si el jugador tiene mayor puntaje que el dealer, gana el jugador
        elif player_score > dealer_score:
            self.winner = "player"
        # Si el dealer tiene mayor puntaje que el jugador, gana el dealer
        elif dealer_score > player_score:
            self.winner = "dealer"
        # Si hay empate, no hay ganador
        else:
            self.winner = None
            
        self.game_over = True
        return True
