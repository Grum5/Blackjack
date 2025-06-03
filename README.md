# Blackjack en Python 🃏

Este es un proyecto educativo que simula el juego de **Blackjack** utilizando **Python** y **Pygame**. Incluye un generador pseudoaleatorio basado en el **mapa de Henon**, evitando el uso de bibliotecas como `random`, y siguiendo el patrón **MVC (Modelo-Vista-Controlador)**.

## 🎮 Características

- Juego funcional de Blackjack entre jugador y dealer.
- Renderizado con **Pygame** en una interfaz simple.
- Implementación de un generador caótico de números pseudoaleatorios.
- Estructura clara basada en clases
- Soporte para rondas múltiples.
- Solo control por **teclado**, sin uso de mouse.

## ⚙️ Requisitos

- Python 3.9 o superior
- Pygame

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Controles en el juego:
**H** -> Pedir carta (Hit)  
**S** -> Plantarse (Stand)  
**Q** -> Salir del juego  
**R** -> Reiniciar juego (Esto solo funciona al terminar una ronda)
**Esc** -> Abandonar el juego (Cierra el juego)

## Licencia

Este proyecto se encuentra bajo la licencia MIT. Puedes consultarla en el archivo LICENSE.  
Los resources utilizados tiene su propia licencia descrita a continuación.

## Créditos
Desarrollado como parte de una tarea del curso de **Simulación**, por:
- Grum5
- JoskaSF

## 🎨 Recursos gráficos

Las cartas utilizadas en el juego provienen del paquete **"Playing Cards Pack"** creado por [Kenney.nl](https://kenney.nl/), bajo la licencia [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).

Agradecemos a Kenney por compartir sus recursos de forma libre.  
Enlace al paquete: https://kenney.nl/assets/playing-cards-pack
