### Структурные модели


## Описание внутренней структуры приложения

[Код диаграммы](piclab4/stru)
![Внутр структ](https://www.planttext.com/api/plantuml/png/fLJBRkCW5DtxAr1NpZJ-0Qkg-f0wCwjKwg9B2vjRcmQ31RZfO-RV1mm4x7JQHiqY4kS-pdqStmkbiTHZpxAiOLWfT2ier-WjG-PNeESIcQT_lCJ7gVFBdNtjJQliRqZp4_UmgH-XYRa6eQYcWfSkrkU9Zld2OUKzYCIxN8to0JUmHZKJpRPIz1KIjijXOF09qUJp3OvDRKRLV4eJtBx1T2Nw-aEMmiHXfIk92HrLkY9u7fWWG4fK2y5IK9aS5UQqnovRhDZIBQjT7pA41Zn5VaH3TnnluzmKj3rmRR8oglJPn7VkROHAeuIf3gMbPvZ2yqcerRl1Q-ICy-XGO2-U88zrUSMsHdVLZXBTfK07jEtqhDzMYjqo_DZUhSZt_LkY-prn0lwAv65KDhXqEJo4hOnBfsOF2I-vC9GWmJ3KsYmusEoo0wuQ8M5PnEO9v4mz3uARccx4NY_xZl8lpt1QpnGIa74WMCTdqq6plHRCr6ZMTqzr5vfG1nzIKjqfwZ0d37xpOTGvjV-prRV0GHeUz-slqh4jETLCq7TsD66pgS6TAlNVfRlpMHJdwEJ7INBSikGWdlqf2b_94WrT7nZitWv0fukeC4lhiEm2EB5N_Hy0)

## Описание используемых структур/объектов данных

[Код диаграммы](piclab3/vnutr)
![Объект](https://www.planttext.com/api/plantuml/png/bLF1JiCm3BttAwAU0AdJk5OC3Gx0RPCcn06XAMsyDY9DgZg38SI_upHfoxeYGGzjakTd-_cbIxIyiVjAHL6kE29R6waj-umOFGaxfCnj5smU3Zw6Ww-ESbFN2dfARL1QQNGQKYsOXdU_FZiVIAkCAkV_vzsQAliZnyTaHBFRXWkvnx4QEDJA210founH1EouGlW98cNVSYqhxkkSYDze_Zg8G2Wgq9OAAOdsgktacWZFBo50o0PodmfjGqZyk8v7sUvvDMGiQFCaXIt7lJlW0MHHsZ62BaaQElCZQTVzIBWpB0s--O1stGUOO4wdepFhI4f6JdG1pfKZ47FJmBYnahhTJ05Eo-eDcaaVTaQJn3jwkpbvLV5bp9Aa_VGZYxoUIQY_RV5yDhkO26YlrMzWj0Gjt3_o3G00)

## Внутренняя структура приложения:
# Приложение "Змейка" состоит из нескольких основных компонентов:

SnakeGame: Этот класс представляет основное состояние игры, включая размер игрового поля, объекты змейки, яблока, препятствий, бомб, текущий счет, рекордный счет, флаг окончания игры и объект шрифта.

Snake: Этот класс представляет змейку на игровом поле. Он содержит список сегментов, образующих тело змейки, а также текущее направление движения.

Point: Представляет точку на игровом поле с координатами x и y.

Apple: Представляет яблоко на игровом поле. Оно имеет позицию, представленную объектом Point.

Obstacle: Представляет препятствие на игровом поле. Оно также имеет позицию, представленную объектом Point.

Bomb: Представляет бомбу на игровом поле. Она имеет позицию, радиус взрыва, флаг взрыва и анимацию взрыва.

# Используемые структуры/объекты данных:

Point: Точка на игровом поле с координатами x и y.
Apple: Яблоко на игровом поле с позицией, представленной объектом Point.
Obstacle: Препятствие на игровом поле с позицией, также представленной объектом Point.
Bomb: Бомба на игровом поле с позицией, радиусом взрыва, флагом взрыва и анимацией взрыва.
Snake: Змейка на игровом поле с сегментами, образующими ее тело, и текущим направлением движения.
SnakeGame: Состояние игры, включающее размер игрового поля, объекты змейки, яблока, препятствий, бомб, текущий счет, рекордный счет, флаг окончания игры и объект шрифта.