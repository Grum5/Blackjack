
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

    def start_round(self) -> Tuple[Optional[str], bool]:
        ''' Metodo que inicializa la ronda '''

        # Se revuelve el mazo y se reinician las manos
        self.deck.shuffle()
        self.player.reset_hand()
        self.dealer.reset_hand()

        # Se reparten 2 cartas a cada mano (un total de 4 cartas menos al deck)
        for _ in range(2):
            self.player.add_card(self.deck.draw())
            self.dealer.add_card(self.deck.draw())

        # Verificar que el jugador y el dealer no tengan blackjack
        player_bj = self.player.hand.is_blackjack()
        dealer_bj = self.dealer.hand.is_blackjack()

        # Empate, ambos tiene blackjack
        if player_bj and dealer_bj:
            return None, True

        # El jugador tiene blackjack
        elif player_bj:
            return "player", True

        # El dealer tiene blackjack
        elif dealer_bj:
            return "dealer", True

        # No hay blackjack, el juego continua
        else:
            return None, False
