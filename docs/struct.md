### Структурные модели
Для описания внутренней структуры приложения с помощью диаграммы классов, я предлагаю следующую детализацию на основе функциональных возможностей:
@startuml

class SnakeGame {
    - WIDTH: int
    - HEIGHT: int
    - snake: Snake
    - apple: Apple
    - obstacles: List<Obstacle>
    - score: int
    - high_score: int
    - game_over: bool
    + init()
    + start_game(): void
    + update(): void
    + handle_input(): void
    + generate_apple(): void
    + generate_obstacles(): void
    + check_collisions(): void
    + increase_score(): void
    + increase_speed(): void
}

class Snake {
    - segments: List<Point>
    - direction: str
    + init()
    + move(): void
    + grow(): void
    + draw(): void
}

class Apple {
    - position: Point
    + init()
    + draw(): void
}

class Obstacle {
    - position: Point
    + init()
    + draw(): void
}

SnakeGame -- Snake: contains >
SnakeGame -- Apple: contains >
SnakeGame -- Obstacle: contains >

Snake -- Apple: eats >
Snake -- Obstacle: collides with >

@enduml

### Диаграмма объектов (Object Diagram)

@startuml

object SnakeGame {
    WIDTH: int = 20
    HEIGHT: int = 20
    snake: Snake
    apple: Apple
    obstacles: List<Obstacle>
    score: int = 0
    high_score: int = 0
    game_over: bool = false
}

object Snake {
    segments: List<Point>
    direction: str
}

object Apple {
    position: Point
}

object Obstacle {
    position: Point
}

class Point {
    x: int
    y: int
}

@enduml

### Диаграмма классов (Class Diagram)
Диаграмма классов представляет внутреннюю структуру приложения "Змейка" и описывает классы, их атрибуты и методы, а также взаимосвязи между ними.

## Описание содержания:
SnakeGame: Класс, представляющий игру "Змейка". Содержит атрибуты для хранения размеров игрового поля, змейки, яблока, препятствий, счета, рекордного счета и флага завершения игры. Также включает методы для инициализации игры, запуска, обновления, обработки ввода, генерации объектов, проверки столкновений и управления игровым процессом.
Snake: Класс, представляющий змейку в игре. Содержит атрибуты для хранения сегментов змейки и текущего направления движения, а также методы для движения, увеличения длины и отрисовки.
Apple: Класс, представляющий яблоко на игровом поле. Содержит атрибут для хранения позиции яблока и метод для отрисовки.
Obstacle: Класс, представляющий препятствие на игровом поле. Содержит атрибут для хранения позиции препятствия и метод для отрисовки.
## Связи:

Связь "contains" отражает, что класс SnakeGame содержит объекты Snake, Apple и Obstacle.
Связь "eats" отображает, что змейка взаимодействует с яблоком.
Связь "collides with" показывает, что змейка может столкнуться с препятствием.
### Диаграмма объектов (Object Diagram)
Диаграмма объектов отображает конкретные экземпляры объектов данных в приложении "Змейка".

## Описание содержания:
SnakeGame: Объект, представляющий текущую игровую сессию. Содержит атрибуты для хранения размеров игрового поля, объектов змейки, яблока, препятствий, счета, рекордного счета и флага завершения игры.
Snake: Объект, представляющий змейку в игре. Содержит список сегментов змейки и текущее направление движения.
Apple: Объект, представляющий яблоко на игровом поле. Содержит позицию на поле.
Obstacle: Объект, представляющий препятствие на игровом поле. Содержит позицию на поле.
Point: Класс, представляющий точку на игровом поле с координатами x и y.