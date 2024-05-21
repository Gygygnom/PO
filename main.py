import pygame
from game import SnakeGame

def main():
    pygame.init()
    game = SnakeGame(600, 400)
    game.startGame()

    # Инициализация окна
    screen = pygame.display.set_mode((game.gameWidth, game.gameHeight))
    pygame.display.set_caption("Snake Game")

    # Основной игровой цикл
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.handleInput("UP")
                elif event.key == pygame.K_DOWN:
                    game.handleInput("DOWN")
                elif event.key == pygame.K_LEFT:
                    game.handleInput("LEFT")
                elif event.key == pygame.K_RIGHT:
                    game.handleInput("RIGHT")

        game.update()

        # Проверка завершения игры
        if game.gameOver:
            break

        # Отрисовка игровых объектов
        screen.fill((50, 153, 213))  # Синий фон
        game.drawObjects(screen, 10)  # Отрисовка всех игровых объектов
        game.drawScore(screen)  # Отрисовка счета

        pygame.display.flip()

        # Управление частотой обновления экрана (скорость игры)
        clock.tick(15)

    pygame.quit()

if __name__ == "__main__":
    main()
