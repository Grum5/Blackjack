import pygame
from pygame.locals import (
    QUIT,
    KEYDOWN,
    K_ESCAPE,
    K_h,
    K_s,
    K_r
)


class EventHandler:
    ''' Clase que encapsula el manejo de eventos del teclado '''

    def __init__(self) -> None:
        ''' Constructor '''

        # Habilitar eventos especificos
        pygame.event.set_allowed([KEYDOWN, QUIT])

        self.quit = False
        self.hit = False
        self.stand = False
        self.restart = False

        # Flag para esperar una acción
        self.wait_for_action = False

    @property
    def is_waiting(self) -> bool:
        ''' Retorna un boleado si se esta esperando una acción '''

        # Se guarda el valor de wait_for_action en una variable temporal
        temp = self.wait_for_action

        # Se cambia el flah de wait_for_action
        self.wait_for_action = True

        return temp

    def process(self) -> None:
        ''' Procesa todos los eventos del ciclo actual y actualiza flags '''

        self.reset_flags()

        for event in pygame.event.get():
            if event.type == QUIT:
                self.quit = True

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.quit = True
                elif event.key == K_h:
                    self.hit = True
                elif event.key == K_s:
                    self.stand = True
                elif event.key == K_r:
                    self.restart = True

    def reset_flags(self) -> None:
        ''' Reinicia los flags para evitar estados persistentes '''

        self.hit = False
        self.stand = False
        self.restart = False
