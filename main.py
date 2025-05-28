from src.controllers.game import Game
import pygame

if __name__ == '__main__':
    # Inicializar pygame y sus módulos
    pygame.init()
    
    # Instanciar el juego y correrlo
    game = Game()
    game.run()

