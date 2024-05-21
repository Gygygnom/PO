import pygame

# Цвета
white = (255, 255, 255)
green = (0, 255, 0)
blue = (50, 153, 213)
black = (0, 0, 0)
red = (213, 50, 80)
yellow = (255, 255, 102)
orange = (255, 165, 0)  # Определение цвета orange для анимации взрыва

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Apple:
    def __init__(self, position):
        self.position = position

    def draw(self, surface, block_size):
        pygame.draw.rect(surface, red, [self.position.x, self.position.y, block_size, block_size])

class Obstacle:
    def __init__(self, position):
        self.position = position

    def draw(self, surface, block_size):
        pygame.draw.rect(surface, black, [self.position.x, self.position.y, block_size, block_size])

class Bomb:
    def __init__(self, position, blast_radius=3):
        self.position = position
        self.blast_radius = blast_radius
        self.exploded = False
        self.explosion_animation = 0

    def explode(self):
        self.exploded = True

    def draw(self, surface, block_size):
        if not self.exploded:
            pygame.draw.rect(surface, yellow, [self.position.x, self.position.y, block_size, block_size])
        else:
            # Анимация взрыва
            radius = self.blast_radius * block_size
            explosion_center = (self.position.x + block_size // 2, self.position.y + block_size // 2)

            # Рисуем взрыв в виде кругов с увеличивающимся радиусом
            for r in range(1, self.blast_radius + 1):
                pygame.draw.circle(surface, red, explosion_center, r * block_size, 1)  # Внешняя граница
                pygame.draw.circle(surface, orange, explosion_center, r * block_size - 2, 1)
                pygame.draw.circle(surface, yellow, explosion_center, r * block_size - 4, 1)
                pygame.draw.circle(surface, white, explosion_center, r * block_size - 6, 1)

            # Увеличиваем счетчик анимации взрыва
            self.explosion_animation += 1

            # Завершаем анимацию взрыва
            if self.explosion_animation >= 10:
                self.explosion_animation = 0
                self.exploded = False

class Snake:
    def __init__(self, start_segments, start_direction):
        self.segments = start_segments
        self.direction = start_direction

    def move(self, block_size, game_width, game_height):
        head = self.segments[0]
        x = head.x
        y = head.y
        if self.direction == "UP":
            y -= block_size
            if y < 0:
                y = game_height - block_size
        elif self.direction == "DOWN":
            y += block_size
            if y >= game_height:
                y = 0
        elif self.direction == "LEFT":
            x -= block_size
            if x < 0:
                x = game_width - block_size
        elif self.direction == "RIGHT":
            x += block_size
            if x >= game_width:
                x = 0
        new_segment = Point(x, y)
        self.segments.insert(0, new_segment)
        # Всегда удаляем последний сегмент, чтобы змейка двигалась вперед
        self.segments.pop()

    def draw(self, surface, block_size):
        for segment in self.segments:
            pygame.draw.rect(surface, green, [segment.x, segment.y, block_size, block_size])
