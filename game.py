import pygame
import random
from entities import Point, Apple, Obstacle, Bomb, Snake, white


class SnakeGame:
    def __init__(self, game_width, game_height):
        self.gameWidth = game_width
        self.gameHeight = game_height
        start_x = game_width // 2
        start_y = game_height // 2
        start_segment = [Point(start_x, start_y)]
        self.snake = Snake(start_segment, "UP")
        self.apple = Apple(Point(random.randrange(0, game_width, 10), random.randrange(0, game_height, 10)))
        self.obstacles = []  # Начально пустой список препятствий
        self.bombs = []  # Начально пустой список бомб
        self.score = 0
        self.highScore = 0
        self.gameOver = False
        self.font = pygame.font.Font(None, 36)  # Шрифт для отображения текста

    def startGame(self):
        self.gameOver = False
        self.score = 0
        self.snake = Snake([Point(self.gameWidth // 2, self.gameHeight // 2)], "UP")
        self.apple = self.generateApple()

    def update(self):
        if not self.gameOver:
            self.snake.move(10, self.gameWidth, self.gameHeight)  # Двигаем змейку
            self.checkCollisions()  # Проверяем столкновения
            if self.snake.segments[0].x == self.apple.position.x and self.snake.segments[0].y == self.apple.position.y:
                self.score += 10
                # Сохраняем координаты хвоста змейки
                tail = self.snake.segments[-1]
                # Добавляем три новых сегмента к змейке начиная с сохраненных координат хвоста
                for _ in range(3):
                    x = tail.x
                    y = tail.y
                    if self.snake.direction == "UP":
                        y += 10
                    elif self.snake.direction == "DOWN":
                        y -= 10
                    elif self.snake.direction == "LEFT":
                        x += 10
                    elif self.snake.direction == "RIGHT":
                        x -= 10
                    new_segment = Point(x, y)
                    self.snake.segments.append(new_segment)
                self.apple = self.generateApple()  # Генерируем новое яблоко
                self.obstacles.append(Obstacle(Point(random.randrange(0, self.gameWidth, 10),
                                                     random.randrange(0, self.gameHeight,
                                                                      10))))  # Добавляем новое препятствие
                self.bombs.append(Bomb(Point(random.randrange(0, self.gameWidth, 10),
                                             random.randrange(0, self.gameHeight, 10))))  # Добавляем новую бомбу

    def checkCollisionWithObstacles(self, position):
        # Проверяем, не совпадает ли позиция с каким-либо препятствием или бомбой
        for obstacle in self.obstacles:
            if position.x == obstacle.position.x and position.y == obstacle.position.y:
                return True
        for bomb in self.bombs:
            if position.x == bomb.position.x and position.y == bomb.position.y:
                return True
        return False

    def handleInput(self, input):
        if input == "UP" and self.snake.direction != "DOWN":
            self.snake.direction = "UP"
        elif input == "DOWN" and self.snake.direction != "UP":
            self.snake.direction = "DOWN"
        elif input == "LEFT" and self.snake.direction != "RIGHT":
            self.snake.direction = "LEFT"
        elif input == "RIGHT" and self.snake.direction != "LEFT":
            self.snake.direction = "RIGHT"

    def generateApple(self):
        while True:
            # Генерируем новую позицию для яблока
            new_position = Point(random.randrange(0, self.gameWidth, 10), random.randrange(0, self.gameHeight, 10))
            # Проверяем, не находится ли новая позиция внутри препятствия или бомбы
            if not self.checkCollisionWithObstacles(new_position):
                return Apple(new_position)

    def checkCollisions(self):
        head = self.snake.segments[0]

        # Проверка столкновения с границами и обработка перехода через границы
        if head.x < 0:
            head.x = self.gameWidth - 10
        elif head.x >= self.gameWidth:
            head.x = 0
        elif head.y < 0:
            head.y = self.gameHeight - 10
        elif head.y >= self.gameHeight:
            head.y = 0

        # Проверка столкновения с самой собой
        if len(self.snake.segments) > 1:
            for segment in self.snake.segments[1:]:
                if head.x == segment.x and head.y == segment.y:
                    self.gameOver = True

        # Проверка столкновения с препятствиями
        for obstacle in self.obstacles:
            if head.x == obstacle.position.x and head.y == obstacle.position.y:
                self.gameOver = True

        # Проверка столкновения с бомбами
        for bomb in self.bombs:
            if not bomb.exploded and head.x == bomb.position.x and head.y == bomb.position.y:
                bomb.explode()
                if len(self.snake.segments) >= 4:
                    self.snake.segments = self.snake.segments[:-4]  # Удаляем последние 4 сегмента
                else:
                    self.gameOver = True  # Игра завершается, если длина змейки меньше 4

    def drawScore(self, surface):
        text = f"Score: {self.score}"
        text_surface = self.font.render(text, True, white)
        surface.blit(text_surface, (10, 10))

    def drawObjects(self, surface, block_size):
        # Отрисовка змейки
        self.snake.draw(surface, block_size)

        # Отрисовка яблока
        self.apple.draw(surface, block_size)

        # Отрисовка препятствий
        for obstacle in self.obstacles:
            obstacle.draw(surface, block_size)

        # Отрисовка бомб
        for bomb in self.bombs:
            bomb.draw(surface, block_size)
