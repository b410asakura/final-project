# Final-Project

*It's simple game about D. Trump.*

![](https://github.com/b410asakura/final-project/blob/main/game%20images/game%201.PNG)

press **UP** button for jump

press **RIGHT** butoon for going to the right

press **LEFT** button for going to the left

press **SPACE** for shooting balls


video presentation - https://www.youtube.com/watch?v=DLhEoBklFpI
feedback video - https://youtu.be/rzTSV7m5fVU

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pygame.

```bash
pip install pygame
```


## Usage
```python
import pygame
import random

WIDTH = 360  # weidth of window
HEIGHT = 480 # height of window
FPS = 30 # frame rate per second

# creating game and window
pygame.init()
pygame.mixer.init()  # for sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Process (event) input
    # Update
    # Visualization (assembly)
```

# License

[AIU](http://alatoo.edu.kg/)

### Project has done by:
@b410asakura;     *Baiel Saparaliev*

@xNazim;          *Nazim Mukhtarbekov*
