### Структурные модели
Для описания внутренней структуры приложения с помощью диаграммы классов, я предлагаю следующую детализацию на основе функциональных возможностей:

[Код диаграммы](piclab4/structur)
![Диаграмма структурных моделей](https://www.planttext.com/api/plantuml/png/jLJBQiCm4BpdAtIqQV83feI45jf28OKSUZIAjDXBPCb8Sj9I-k-Lv4Si9UsjFjXeTcSqkojvOopLjcl4Oi44DORi9Jt24ss0V2s8UrQaSejtvBOk24ex0vy1gzhEKUF9HQynGBHjXOEs_ZD0wk0sPG9CGLxHsFlTi5wFAanfcClMRfzz2de7knFeWXoK4W6y8sM94crPPh7fPUet7_93zRxQB2_8II4VyAxbrAPWJIKNy2BRpcRetuNZwpYd0WdQKKEzsUtOMA_9PDViBitmlY82gu4T7vGGQ519ayYXP1geWT2Ph5MEVajaIci1-2Jn7SrxchM1ge6W4oRpvaN7iN3KmAmp4ifE6nuwkRz5N_PTVepeum0QTRfgarRd1EAQdg-jXnvFrbjbi9SFswR-ad3-f_8ub7yH3ocJyiVyJ7_s2vTwkOQhLJ-ZWZ0bBKLfo3eER_ihzbjuB2RAw5DcRA1sOgOiTm0v6796Mtlg1YJtVumV)

### Диаграмма объектов (Object Diagram)
[Код диаграммы](piclab4/obj)
![Диаграмма структурных моделей](https://www.planttext.com/api/plantuml/png/TL9DIyGm5BpdLuGzjT05swEWh23eRHUAU10FsVRPHjEaDD7THVpllkQZROhsbCwRcSmyijE63UQp4uIeupjKXfQIVS03wu1-4ufVWyTdNfkMtj3YQe8UWJUjcJ4zol1NmibP9DQvXAO3QNH6xUyz7_0EhcHgHQplHH3TZUUaLvhFStL4LIL08-Tb9EqzCF7oDAD_3ehqrUMgr31UuLAs6BgCaB7B_Wi61DwOq41-uatuBMZV8mGvA2vDSiupUWaHF5GW52wlGrsKRPuEcuMvhUlDGsQ_2M-4Fkb241gkD7aiSe4YHX4pNBw5iSMzwtdQoyMUa3M_X-tsrk_acbPA6iQbNerTgt_7KuSr8n83Cqiu4Wd1QtmE9svQGdOWw_7f_W80)


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