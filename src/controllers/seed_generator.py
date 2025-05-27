import time
from src.models.prng.henon import Henon


class SeedGenerator:

    def __init__(self, a=1.4, b=0.3):
        self.a = a
        self.b = b
        self.x0 = 0.1
        self.y0 = 0.3
        self.iterations = 100  # Número inicial de iteraciones
        self._last_values = []

        # Inicializamos el PRNG Henon
        self.prng = Henon(
            self.a, self.b,
            self.x0, self.y0,
            iterations=self.iterations)

    def _is_stuck(self, value, threshold=1e-6):
        # Verifica si value está estancado comparándolo con valores previos
        return any(abs(value - v) < threshold for v in self._last_values)

    def get_seed(self):
        # Obtenemos dos números pseudoaleatorios (x_new, y_new)
        x_new, _ = self.prng.get_pseudonumber()
        y_new, _ = self.prng.get_pseudonumber()

        # Normalizamos x_new y y_new al rango [-1.5, 1.5]
        x_new = (x_new + 1.5) % 3.0 - 1.5
        y_new = (y_new + 1.5) % 3.0 - 1.5

        # Detectamos estancamiento en x_new o y_new
        if self._is_stuck(x_new) or self._is_stuck(y_new):
            print("[SeedGenerator] Estancamiento detectado. Regenerando semilla...")

            # Obtenemos tiempo actual en segundos para variar iteraciones
            t = int(time.time())

            # Calculamos un offset para modificar iteraciones y romper ciclo
            offset = (len(self._last_values) + t) % 1000 + 50

            # Creamos un nuevo PRNG Henon con iteraciones modificadas
            temp_prng = Henon(self.a, self.b, 0.1, 0.3, iterations=offset)

            # Generamos nuevas semillas desde este nuevo PRNG
            x_new, _ = temp_prng.get_pseudonumber()
            y_new, _ = temp_prng.get_pseudonumber()

            # Normalizamos otra vez
            x_new = (x_new + 1.5) % 3.0 - 1.5
            y_new = (y_new + 1.5) % 3.0 - 1.5

            # Limpiamos historial para evitar falsas detecciones rápidas
            self._last_values = []

            # Actualizamos el PRNG principal para usar esta nueva semilla
            self.prng = Henon(
                self.a, self.b,
                x_new, y_new,
                iterations=self.iterations)

        # Guardamos el valor actual para futuras comparaciones
        self._last_values.append(x_new)

        # Limitamos el historial para no crecer indefinidamente
        if len(self._last_values) > 10:
            self._last_values.pop(0)

        return x_new, y_new
