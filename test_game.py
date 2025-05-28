# test_game.py

from src.models.deck import Deck
from src.models.player import Player
from src.models.dealer import Dealer
from src.controllers.seed_generator import SeedGenerator


def test_game_console():
    seed_gen = SeedGenerator()
    prng = seed_gen.prng
    deck = Deck(prng)

    player = Player("Jugador")
    dealer = Dealer()

    while True:
        # Verificar y reiniciar mazo si está vacío
        if deck.is_empty:
            deck.reset()

        # Limpiar manos
        player.reset_hand()
        dealer.reset_hand()

        # Repartir cartas iniciales
        player.draw(deck, 2)
        dealer.draw(deck, 2)

        print("\n=== Nueva Ronda ===")
        print("Tus cartas:", player.hand)
        print("Carta visible del dealer:", dealer.hand.cards[0])

        # ¿Jugador tiene blackjack?
        if player.hand.is_blackjack():
            print("¡Blackjack! Ganaste automáticamente.")
        else:
            # Turno del jugador
            while player.hand.get_value() < 21:
                action = input("¿Hit o Stand? ").strip().lower()
                if action == "hit":
                    player.draw(deck, 1)
                    print("Tus cartas:", player.hand)
                elif action == "stand":
                    break
                else:
                    print("Opción inválida. Escribe 'hit' o 'stand'.")

            if player.hand.get_value() > 21:
                print("Te pasaste. ¡Pierdes!")
                continue

        # Turno del dealer
        print("\nTurno del dealer...")
        print("Cartas del dealer:", dealer.hand)

        while dealer.hand.get_value() < 17:
            dealer.draw(deck, 1)
            print("Dealer toma carta:", dealer.hand)

        # Evaluación final
        player_score = player.hand.get_value()
        dealer_score = dealer.hand.get_value()

        print("\n--- Resultado Final ---")
        print("Jugador:", player_score, "-", player.hand)
        print("Dealer:", dealer_score, "-", dealer.hand)

        if dealer_score > 21 or player_score > dealer_score:
            print("¡Ganaste!")
        elif player_score < dealer_score:
            print("Perdiste.")
        else:
            print("Empate.")

        # ¿Repetir?
        again = input("\n¿Otra ronda? (s/n): ").strip().lower()
        if again != "s":
            break


if __name__ == "__main__":
    test_game_console()
