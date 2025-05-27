import pygame


class Screen:

    def __init__(self, width: str, height: str, title: str) -> None:
        ''' Constructor '''

        # Atributos iniciales
        self.width = width
        self.height = height
        self.title = title

        self.surface = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.title)

    def update(self) -> None:
        ''' Metodo para actualizar la pantalla '''

        pygame.display.flip()

    def fill(self,  color: tuple = (47, 113, 105)) -> None:
        ''' Metodo para rellenar la superficie con un color '''

        self.surface.fill(color)

    def get_surface(self) -> pygame.Surface:
        '''
            Metodo que retorna la superficie principal
            para poder dibujar sobre ella
        '''

        return self.surface

    def get_size(self) -> tuple:
        ''' Metodo para retornar el tamaño de la pantalla '''

        return (self.width, self.height)
