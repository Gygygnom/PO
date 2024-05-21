from unittest import mock

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

def test_snake_move():
    snake = Snake([Point(10, 10)], "UP")
    snake.move(10, 100, 100)
    assert snake.segments[0].x == 10
    assert snake.segments[0].y == 0  # Verify head moved up

@pytest.mark.skip(reason="UI element test")
def test_snake_draw(surface):
    snake = Snake([Point(10, 10)], "UP")
    block_size = 10
    pygame.draw.rect = mock.MagicMock()
    snake.draw(surface, block_size)
    pygame.draw.rect.assert_called_once_with(surface, (0, 255, 0), [10, 10, block_size, block_size])

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

@pytest.mark.skip(reason="UI element test")
def test_snake_game_draw_score(game, surface):
    pygame.font.Font.render = mock.MagicMock()
    game.drawScore(surface)
    pygame.font.Font.render.assert_called_once()

@pytest.mark.skip(reason="UI element test")
def test_snake_game_draw_objects(game, surface):
    block_size = 10
    game.snake.draw = mock.MagicMock()
    game.apple.draw = mock.MagicMock()
    game.obstacles.append(Obstacle(Point(10, 10)))
    game.bombs.append(Bomb(Point(20, 20), 3))
    game.drawObjects(surface, block_size)
    game.snake.draw.assert_called_once()
    game.apple.draw.assert_called_once()
    for obstacle in game.obstacles:
        obstacle.draw.assert_called_once()
    for bomb in game.bombs:
        bomb.draw.assert_called_once()

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
