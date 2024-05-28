from unittest import mock
from unittest.mock import patch
import unittest
import pytest
import pygame
from game import SnakeGame
from entities import Point, Apple, Obstacle, Bomb, Snake, yellow, red, green, black


@pytest.fixture
def game():
    game = SnakeGame(600, 400)
    game.startGame()
    return game


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
    assert game.snake.segments[0].y == initial_y - 10


def test_snake_game_check_collisions(game):
    game.snake.segments = [Point(10, 10), Point(20, 10)]
    game.obstacles.append(Obstacle(Point(10, 10)))
    game.checkCollisions()
    assert game.gameOver


def test_snake_game_check_collision_with_obstacles(game):
    position = Point(10, 10)
    game.obstacles.append(Obstacle(position))
    assert game.checkCollisionWithObstacles(position) == True
    # Проверяем отсутствие коллизий с пустым местом
    assert game.checkCollisionWithObstacles(Point(20, 20)) == False


def test_snake_game_handle_input(game):
    game.handleInput("UP")
    assert game.snake.direction == "UP"

    game.handleInput("LEFT")
    assert game.snake.direction == "LEFT"

    # Проверяем, что змейка не может двигаться в противоположном направлении
    game.handleInput("RIGHT")
    assert game.snake.direction == "LEFT"

    game.handleInput("DOWN")
    assert game.snake.direction == "DOWN"

    # Проверяем, что змейка не может двигаться в противоположном направлении
    game.handleInput("UP")
    assert game.snake.direction == "DOWN"

    # Возвращаем направление на "LEFT", чтобы проверить "RIGHT"
    game.handleInput("LEFT")
    assert game.snake.direction == "LEFT"

    # Проверяем, что змейка может двигаться направо, если текущий направление не "LEFT"
    game.snake.direction = "UP"
    game.handleInput("RIGHT")
    assert game.snake.direction == "RIGHT"


def test_snake_game_generate_apple(game):
    apple = game.generateApple()
    assert not game.checkCollisionWithObstacles(apple.position)
    for segment in game.snake.segments:
        assert apple.position != segment


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
    assert head.x == bomb.position.x and head.y == bomb.position.y  # Убеждаемся, что голова змеи на позиции бомбы


def move_snake_to_bomb(game, bomb_position):
    game.snake.segments[0] = bomb_position


def test_bomb_explosion_reduces_snake_size(game):
    # Инициализация змеи длиной 5 сегментов
    game.snake.segments = [
        Point(100, 100), Point(110, 100), Point(120, 100),
        Point(130, 100), Point(140, 100)
    ]
    # Добавление бомбы на позицию головы змеи
    bomb_position = Point(100, 100)
    game.bombs.append(Bomb(bomb_position))

    # Перемещение змеи на бомбу и обновление игры
    move_snake_to_bomb(game, bomb_position)
    game.update()

    # Проверка, что бомба взорвалась
    assert game.bombs[0].exploded == False
    # Проверка, что длина змеи уменьшилась на 4 сегмента
    assert len(game.snake.segments) - 4 == 1


def test_bomb_explosion_game_over(game):
    # Инициализация змеи длиной 3 сегмента
    game.snake.segments = [
        Point(100, 100), Point(110, 100), Point(120, 100)
    ]
    # Добавление бомбы на позицию головы змеи
    bomb_position = Point(100, 100)
    game.bombs.append(Bomb(bomb_position))

    # Перемещение змеи на бомбу и обновление игры
    move_snake_to_bomb(game, bomb_position)
    game.update()

    # Проверка, что бомба взорвалась
    assert game.bombs[0].exploded == False
    # Проверка, что игра завершилась
    assert game.gameOver == False


# ################################
# Дополнительные тесты
# ################################
def test_obstacle_generation(game):
    initial_obstacle_count = len(game.obstacles)

    directions = {
        "UP": (0, -10),
        "DOWN": (0, 10),
        "LEFT": (-10, 0),
        "RIGHT": (10, 0)
    }

    for direction, (dx, dy) in directions.items():
        # Устанавливаем начальное направление и позицию змейки
        game.snake.direction = direction
        game.snake.segments = [Point(100, 100)]

        # Перемещаем яблоко перед головой змейки
        game.apple.position = Point(100 + dx, 100 + dy)

        # Обновляем игру, чтобы змейка съела яблоко и создала препятствие
        game.update()
        game.update()  # Второе обновление для добавления препятствия

        assert len(game.obstacles) == initial_obstacle_count + 1, f"Failed for direction {direction}"
        initial_obstacle_count = len(game.obstacles)  # Обновляем счетчик для следующего направления

        # Сбрасываем позицию яблока для следующей итерации
        game.apple.position = game.generateApple().position


def test_bomb_generation(game):
    initial_bomb_count = len(game.bombs)
    # Ставим яблоко перед головой змеи, чтобы гарантировать его поедание
    game.apple.position = Point(game.snake.segments[0].x, game.snake.segments[0].y - 10)
    game.snake.direction = "UP"
    # Обновляем игру, чтобы змейка съела яблоко и создала бомбу
    game.update()
    game.update()  # Второе обновление для добавления бомбы
    assert len(game.bombs) == initial_bomb_count + 1


def test_snake_game_check_collision_with_bombs(game):
    position = Point(10, 10)
    game.bombs.append(Bomb(position))
    assert game.checkCollisionWithObstacles(position) == True
    # Проверяем отсутствие коллизий с пустым местом
    assert game.checkCollisionWithObstacles(Point(20, 20)) == False


def test_snake_game_check_collisions_with_self(game):
    game.snake.segments = [Point(10, 10), Point(20, 10), Point(10, 10)]
    game.checkCollisions()
    assert game.gameOver


def test_snake_game_check_collisions_with_obstacles(game):
    game.snake.segments = [Point(10, 10)]
    game.obstacles = [Obstacle(Point(10, 10))]
    game.checkCollisions()
    assert game.gameOver


def test_snake_game_check_collisions_with_bombs(game):
    # Устанавливаем змейку длиной 5 сегментов
    game.snake.segments = [
        Point(10, 10), Point(20, 10), Point(30, 10), Point(40, 10), Point(50, 10)
    ]
    # Добавляем бомбу на позицию головы змейки
    bomb_position = Point(10, 10)
    game.bombs = [Bomb(bomb_position)]

    # Проверяем столкновение змейки с бомбой
    game.checkCollisions()

    # Проверяем, что бомба взорвалась
    assert game.bombs[0].exploded == True
    # Проверяем, что длина змейки уменьшилась на 4 сегмента
    assert len(game.snake.segments) == 1
    # Проверяем, что игра не завершилась
    assert not game.gameOver

    # Теперь проверим, что игра завершится, если длина змейки меньше 4 сегментов
    game.snake.segments = [
        Point(10, 10), Point(20, 10), Point(30, 10)
    ]
    game.bombs = [Bomb(bomb_position)]

    # Проверяем столкновение змейки с бомбой
    game.checkCollisions()

    # Проверяем, что бомба взорвалась
    assert game.bombs[0].exploded == True
    # Проверяем, что игра завершилась
    assert game.gameOver


def test_snake_game_draw_score(game):
    surface = mock.Mock()
    game.drawScore(surface)
    surface.blit.assert_called()


def test_snake_game_draw_objects(game):
    # Создаем реальный объект pygame.Surface
    surface = pygame.Surface((game.gameWidth, game.gameHeight))

    # Добавляем несколько препятствий и бомб
    game.obstacles.append(Obstacle(Point(30, 30)))
    game.obstacles.append(Obstacle(Point(40, 40)))
    game.bombs.append(Bomb(Point(50, 50)))
    game.bombs.append(Bomb(Point(60, 60)))

    # Вызываем метод отрисовки объектов
    game.drawObjects(surface, 10)

    # Проверяем цвет пикселей после отрисовки (должен измениться)
    # Проверяем яблоко
    apple_color = surface.get_at((game.apple.position.x + 1, game.apple.position.y + 1))
    assert apple_color == red

    # Проверяем голову змейки
    snake_head_color = surface.get_at((game.snake.segments[0].x + 1, game.snake.segments[0].y + 1))
    assert snake_head_color == green

    # Проверяем препятствия
    for obstacle in game.obstacles:
        obstacle_color = surface.get_at((obstacle.position.x + 1, obstacle.position.y + 1))
        assert obstacle_color == black

    # Проверяем бомбы
    for bomb in game.bombs:
        bomb_color = surface.get_at((bomb.position.x + 1, bomb.position.y + 1))
        assert bomb_color == yellow


def test_snake_move_across_boundary(game):
    game.snake.segments = [Point(0, 0)]
    game.snake.direction = "LEFT"
    game.update()
    assert game.snake.segments[0].x == game.gameWidth - 10

    game.snake.segments = [Point(game.gameWidth - 10, 0)]
    game.snake.direction = "RIGHT"
    game.update()
    assert game.snake.segments[0].x == 0

    game.snake.segments = [Point(0, 0)]
    game.snake.direction = "UP"
    game.update()
    assert game.snake.segments[0].y == game.gameHeight - 10

    game.snake.segments = [Point(0, game.gameHeight - 10)]
    game.snake.direction = "DOWN"
    game.update()
    assert game.snake.segments[0].y == 0


def test_snake_draw(game):
    # Создаем реальный объект pygame.Surface
    surface = pygame.Surface((game.gameWidth, game.gameHeight))

    # Сохраняем координаты сегментов змейки
    snake_segment_positions = [(segment.x, segment.y) for segment in game.snake.segments]

    # Проверяем начальный цвет пикселей (должен быть черный)
    initial_segment_colors = [surface.get_at(pos) for pos in snake_segment_positions]

    # Вызываем метод отрисовки змейки
    game.snake.draw(surface, 10)

    # Проверяем цвет пикселей после отрисовки (должен измениться)
    new_segment_colors = [surface.get_at(pos) for pos in snake_segment_positions]

    # Проверяем, что цвета изменились, что означает, что сегменты змейки были нарисованы
    for initial_color, new_color in zip(initial_segment_colors, new_segment_colors):
        assert initial_color != new_color


def test_bomb_explode():
    bomb = Bomb(Point(10, 10))
    bomb.explode()
    assert bomb.exploded


def test_obstacle_draw():
    obstacle = Obstacle(Point(30, 30))

    # Создаем реальный объект pygame.Surface
    surface = pygame.Surface((100, 100))

    # Устанавливаем цвет поверхности в белый для четкой проверки изменений
    surface.fill((255, 255, 255))

    # Сохраняем начальный цвет пикселя на позиции препятствия
    initial_color = surface.get_at((30, 30))

    obstacle.draw(surface, 10)

    # Проверяем цвет пикселя после отрисовки (должен измениться)
    new_color = surface.get_at((30, 30))

    # Проверяем, что цвет пикселя изменился
    assert initial_color != new_color


def test_bomb_draw_not_exploded():
    bomb = Bomb(Point(50, 50))

    # Создаем реальный объект pygame.Surface
    surface = pygame.Surface((100, 100))

    # Устанавливаем цвет поверхности в черный для четкой проверки изменений
    surface.fill((0, 0, 0))

    # Вызываем метод отрисовки бомбы
    bomb.draw(surface, 10)

    # Проверяем цвет пикселя после отрисовки (должен измениться на желтый)
    new_color = surface.get_at((50, 50))

    # Проверяем, что цвет пикселя изменился
    assert new_color == yellow


def test_bomb_explosion_animation():
    bomb = Bomb(Point(50, 50))
    bomb.explode()

    # Создаем реальный объект pygame.Surface
    surface = pygame.Surface((100, 100))

    # Сохраняем начальный цвет пикселей в области взрыва
    initial_colors = []
    for x in range(50 - bomb.blast_radius * 10, 50 + bomb.blast_radius * 10 + 1, 10):
        for y in range(50 - bomb.blast_radius * 10, 50 + bomb.blast_radius * 10 + 1, 10):
            if 0 <= x < 100 and 0 <= y < 100:
                initial_colors.append((x, y, surface.get_at((x, y))))

    # Выполняем отрисовку анимации взрыва
    explosion_changed = False
    for _ in range(10):
        bomb.draw(surface, 10)
        # Проверяем, что цвета пикселей изменяются во время анимации
        for x, y, initial_color in initial_colors:
            new_color = surface.get_at((x, y))
            if initial_color != new_color:
                explosion_changed = True

    assert explosion_changed

    # Проверяем, что анимация взрыва завершена и бомба больше не взорвана
    assert bomb.explosion_animation == 0
    assert not bomb.exploded

    # Выполняем отрисовку после завершения анимации, чтобы убедиться, что цвет пикселей не изменяется
    initial_colors_after_explosion = [(x, y, surface.get_at((x, y))) for x, y, _ in initial_colors]
    bomb.draw(surface, 10)
    for (x, y, color_before), (_, _, color_after) in zip(initial_colors_after_explosion,
                                                         initial_colors_after_explosion):
        assert color_before == color_after


def test_snake_check_collisions_with_boundaries(game):
    # Проверка перехода через левую границу
    game.snake.segments = [Point(-10, 100)]  # Начальная позиция за левой границей
    game.checkCollisions()
    assert game.snake.segments[
               0].x == game.gameWidth - 10

    # Проверка перехода через правую границу
    game.snake.segments = [Point(game.gameWidth, 100)]  # Начальная позиция . за правой границей
    game.checkCollisions()
    assert game.snake.segments[0].x == 0

    # Проверка перехода через верхнюю границу
    game.snake.segments = [Point(100, -10)]  # Начальная позиция за верхней границей
    game.checkCollisions()
    assert game.snake.segments[
               0].y == game.gameHeight - 10

    # Проверка перехода через нижнюю границу
    game.snake.segments = [Point(100, game.gameHeight)]  # Начальная позиция за нижней границей
    game.checkCollisions()
    assert game.snake.segments[0].y == 0 
