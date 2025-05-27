import pygame

from src.views.screen import Screen


class Game:
    '''
        Clase principal del juego
    '''

    def __init__(self) -> None:
        ''' Constructor '''

        self.screen = Screen(500, 500, "test")
        self.running = True

    def run(self) -> None:
        '''
            Loop principal del juego
        '''

        while self.running:
            self.handle_events()
            self.screen.fill((0, 0, 0))  # Color negro test
            self.screen.update()

    def handle_events(self) -> None:
        '''
            Manejo de eventos del juego
            ¡¡ Se debe implementar en controllers !!
        '''

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


if __name__ == '__main__':

    # Instanciar el juego y correrlo
    game = Game()
    game.run()
