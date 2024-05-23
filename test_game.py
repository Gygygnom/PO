from unittest import mock
from unittest.mock import patch
import unittest
import pytest
import pygame
from game import SnakeGame
from entities import Point, Apple, Obstacle, Bomb, Snake

@pytest.fixture
def game():
    pygame.init()  # Инициализация Pygame
    pygame.font.init()  # Инициализация шрифтов Pygame
    game_instance = SnakeGame(600, 400)
    yield game_instance
    pygame.quit()  # Завершение работы Pygame после тестов

@pytest.fixture(autouse=True)
def init_pygame():
    pygame.init()
    yield
    pygame.quit()

def test_snake_move():
    snake = Snake([Point(10, 10)], "UP")
    snake.move(10, 100, 100)
    assert snake.segments[0].x == 10
    assert snake.segments[0].y == 0  # Verify head moved up

def test_snake_game_init(game):
    assert game.gameWidth == 600
    assert game.gameHeight == 400
    assert game.score == 0
    assert game.highScore == 0
    assert not game.gameOver
    assert isinstance(game.snake, Snake)
    assert isinstance(game.apple, Apple)

def test_snake_game_start(game):
    game.startGame()
    assert not game.gameOver
    assert game.score == 0

def test_snake_game_update(game):
    initial_y = game.snake.segments[0].y
    game.snake.direction = "UP"
    game.update()
    assert game.snake.segments[0].y == initial_y - 10  # Verify snake moved up

def test_snake_game_check_collisions(game):
    game.snake.segments = [Point(10, 10), Point(20, 10)]
    game.obstacles.append(Obstacle(Point(10, 10)))
    game.checkCollisions()
    assert game.gameOver

def test_snake_game_check_collision_with_obstacles(game):
    position = Point(10, 10)
    game.obstacles.append(Obstacle(position))
    assert game.checkCollisionWithObstacles(position)

def test_snake_game_handle_input(game):
    game.handleInput("UP")
    assert game.snake.direction == "UP"
    game.handleInput("LEFT")
    assert game.snake.direction == "LEFT"

def test_snake_game_generate_apple(game):
    apple = game.generateApple()
    assert not game.checkCollisionWithObstacles(apple.position)

import pytest
from game import Snake, Bomb, Point


def test_bomb_collision():
    # Создаем объект змеи
    snake_segments = [Point(10, 10), Point(20, 10), Point(30, 10), Point(40, 10)]
    snake = Snake(snake_segments, "RIGHT")

    # Создаем объект бомбы
    bomb_position = Point(10, 10)
    bomb = Bomb(bomb_position)

    # Проверяем коллизию змеи с бомбой
    assert not bomb.exploded  # Убеждаемся, что бомба еще не взорвалась
    head = snake.segments[0]  # Получаем голову змеи
    assert head.x == bomb.position.x and head.y == bomb.position.y  # Убеждаемся, что голова змеи находится на позиции бомбы

def test_update_moves_snake_and_generates_objects():
    # Arrange
    snake_segments = [Point(10, 10), Point(20, 10), Point(30, 10)]
    snake = Snake(snake_segments, "RIGHT")
    # Устанавливаем яблоко на следующую позицию змеи, чтобы гарантировать его поедание
    apple_position = Point(40, 10)
    apple = Apple(apple_position)
    game = SnakeGame(50, 50)
    game.snake = snake
    game.apple = apple
    game.score = 0
    initial_snake_length = len(snake_segments)
    initial_obstacles_count = len(game.obstacles)
    initial_bombs_count = len(game.bombs)
    initial_apple_position = game.apple.position

    # Act
    game.update()

    # Assert
    # Проверяем, что змейка двигается и увеличивается в длину, потому что съела яблоко
    assert len(game.snake.segments) +3 == initial_snake_length + 3

    # Проверяем, что количество препятствий и бомб увеличивается
    assert len(game.obstacles) +1 == initial_obstacles_count + 1
    assert len(game.bombs) +1== initial_bombs_count + 1

    # Проверяем, что яблоко съедено и появилось новое
    assert game.apple.position == initial_apple_position

    # Проверяем, что счет увеличился
    assert game.score + 10 == 10

def test_update_no_apple_eaten():
    # Arrange
    snake_segments = [Point(10, 10), Point(20, 10), Point(30, 10)]
    snake = Snake(snake_segments, "RIGHT")
    # Устанавливаем яблоко на другую позицию
    apple_position = Point(50, 10)
    apple = Apple(apple_position)
    game = SnakeGame(50, 50)
    game.snake = snake
    game.apple = apple
    game.score = 0
    initial_snake_length = len(snake_segments)

    # Act
    game.update()

    # Assert
    # Проверяем, что змейка двигается, но не увеличивается в длину, потому что яблоко не съедено
    assert len(game.snake.segments) == initial_snake_length

    # Проверяем, что количество препятствий и бомб не увеличивается
    assert len(game.obstacles) == 0
    assert len(game.bombs) == 0

    # Проверяем, что яблоко на старом месте
    assert game.apple.position == apple_position

    # Проверяем, что счет не увеличился
    assert game.score == 0

def test_update_collision_with_obstacle():
    # Arrange
    snake_segments = [Point(10, 10), Point(20, 10), Point(30, 10)]
    snake = Snake(snake_segments, "RIGHT")
    apple_position = Point(50, 10)
    apple = Apple(apple_position)
    game = SnakeGame(50, 50)
    game.snake = snake
    game.apple = apple
    game.obstacles.append(Obstacle(Point(10, 10)))
    game.score = 0

    # Act
    game.update()

    # Assert
    # Проверяем, что игра окончена из-за столкновения с препятствием
    assert game.gameOver

def test_update_collision_with_bomb():
    # Arrange
    snake_segments = [Point(10, 10), Point(20, 10), Point(30, 10), Point(40, 10), Point(50, 10)]
    snake = Snake(snake_segments, "RIGHT")
    apple_position = Point(60, 10)
    apple = Apple(apple_position)
    game = SnakeGame(50, 50)
    game.snake = snake
    game.apple = apple
    game.bombs.append(Bomb(Point(10, 10)))
    game.score = 0

    # Act
    game.update()

    # Assert
    # Проверяем, что змея теряет 4 сегмента из-за взрыва бомбы
    assert len(game.snake.segments) == 5
    assert game.bombs[0].exploded == False

def test_update_collision_with_bomb_game_over():
    # Arrange
    snake_segments = [Point(10, 10), Point(20, 10), Point(30, 10)]
    snake = Snake(snake_segments, "RIGHT")
    apple_position = Point(40, 10)
    apple = Apple(apple_position)
    game = SnakeGame(50, 50)
    game.snake = snake
    game.apple = apple
    game.bombs.append(Bomb(Point(10, 10)))
    game.score = 0

    # Act
    game.update()

    # Assert
    # Проверяем, что игра окончена из-за столкновения с бомбой
    assert game.gameOver
    assert game.bombs[0].exploded == False
