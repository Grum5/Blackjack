
class Game:
    '''
        Clase principal del juego
    '''

    def __init__(self) -> None:
        ''' Constructor '''

        self.running = True

    def run(self) -> None:
        '''
            Loop principal del juego
        '''

        while self.running:
            pass


if __name__ == '__main__':

    # Instanciar el juego y correrlo
    game = Game()
    game.run()
