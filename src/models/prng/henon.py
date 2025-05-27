
class Henon:
    '''
        Clase para la generación de numeros pseudoaleatorios,
        mediante el mapa de Henon
    '''

    def __init__(
            self,
            a: float, b: float,
            x0: float, y0: float,
            iterations: int
    ) -> None:
        ''' Constructor '''

        # Parametros de entrada para el modelo
        self._a = a
        self._b = b
        self._x0 = x0
        self._y0 = y0

        # Listas donde se almacenaran los datos del modelo
        self.x_array, self.y_array = [], []

        for _ in range(iterations):
            _, _ = self.get_pseudonumber()

    def get_pseudonumber(self) -> tuple[float, float]:
        '''
            Generación de un numero pseudoaleatorio
            - Retorna una tupla de numeros pseudoaleatorio de tipo flotante
        '''

        # Saturación de valores para evitar overflow
        MAX_VALUE = 1e6
        self._x0 = max(min(self._x0, MAX_VALUE), -MAX_VALUE)
        self._y0 = max(min(self._y0, MAX_VALUE), -MAX_VALUE)

        x1 = round(1 - self._a * pow(self._x0, 2) + self._y0, 9)
        y1 = round(self._b * self._x0, 9)

        self._x0, self._y0 = x1, y1
        return x1, y1
