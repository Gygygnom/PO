### Функциональные модели

### Инициализация змейки

Пользователь: Запускает игру.  
Приложение: Инициализирует игровое окно и загружает необходимые ресурсы.  
Пользователь: Управляет змейкой с помощью клавиш на клавиатуре.  
Приложение: Создает змейку, устанавливает начальные координаты и направление движения.  
Пользователь: Начинает движение змейки.  
Приложение: Обновляет положение змейки на экране и отображает ее.

### Обнаружение съедания еды

Пользователь: Направляет змейку к яблоку на экране.  
Приложение: Проверяет, совпадают ли координаты головы змейки с координатами яблока.  
Пользователь: Добирается до яблока и съедает его.  
Приложение: Увеличивает длину змейки на один сегмент и генерирует новое яблоко на случайном месте на игровом поле.  
Пользователь: Продолжает игру, увеличивая свой счет.  
Приложение: Обновляет отображение счета игрока на экране.

### Определение размеров игрового поля

Пользователь: Наблюдает за игровым полем и его границами.  
Приложение: Устанавливает размеры игрового поля в соответствии с заданными параметрами.  
Пользователь: Видит, что игровое поле готово для игры.  
Приложение: Генерирует препятствия на игровом поле, если они предусмотрены в настройках.

### Ускорение змейки

Пользователь: Играет в игру, съедая яблоки и увеличивая счет.  
Приложение: По достижении определенного счета или времени, увеличивает скорость движения змейки.  
Пользователь: Замечает, что игра становится более динамичной и сложной.  
Приложение: Поддерживает динамическую адаптацию сложности игры, ускоряя змейку по мере продвижения.

### Диаграмма активности
![Диаграмма активности](https://www.planttext.com/api/plantuml/png/hLHBIWD14DttAHfNkl02BaHH4K4m43n0ErF6mKbFcEaiH0IDeA925YxS2U85ucSq7sEkK7qZgtjCd4ucwi8i0bLTxzNhUZMzb2WHgterP27iAguY7WULFSNz80PF1P5ambDHp4kXE82OYuINc3aHiX82NnTLu8UCqw-UW2SIuBDuWodsCTN7sD9dsDPDhfluY3tymEwSOLYkrK9O1_ah3WSKfFJVr0rzeXluX6tiM8wj7HBk5T7SOelgY4PV44b3NtC2FLDuQe5hqZUgsL7k6ZFuO5iPOC-gQ6FAyGtVAUXWbvHtPWnu9P8gZiAo5FlWuE_eWdqgS_03IfXRlsOftRGSspLVA2X5IM37EydICbg78EAnDpTCtQyMsK6cQ1KK4Qn4OHWaH9SuVFVwaefVlfb6Fc3BejU4icQCpSAqw97Wyxm62aX7XjkGNWmqxh8NnR-3IG4biA-lyZDjEqoR82jgxmywZ1jarOUTYijHhW7uZ9Nu_FoYQrK-iATZ9hYXhPWOx7Z2Ldrj4r_WDEmYbupauZrEyNrIrz2GZ72wUynsDOZXnsGGFtrvR5IOxyD63KtMiTKG_hmApAtFCsHsJgEOiX1i3Er8CjvEb-HknVTqSiz4yO2AdnYMn_s3pqiWVNfZFm40)

### Управление змейкой:
![Управление змейкой](https://www.planttext.com/api/plantuml/png/RL8xReD04EqvnPRn5Q28Zv03fB6KjOn4N1YYA5q4HH8fYfiKRX9V0HDlJC26AxozKTui-5Em26PdvyrxCplSZkDaiaWUxYFFluacJtgXS41kNr2AXR6fulR7Fjiiy1vdOQJL5LPoW5mHKDcKyKB0roCLnen-8XzvYYkSqbkZGMtViQCjo9p2YEzayCktLgZeD6X9bf4acUdv9Oqi7z_OY2OsQCXHYNh1fy5MjksWoZ8u4RXQlboqWUdKMqTOe2Rum2xCi7QdloBttW5xy227NQeUzySQoxE-dj-5K-VfADQk5jxjPODhCaatR8JtSXBPahmy7WWzMrMkFzwMVQFTssoubezElfFczpY-Nje_pt7dyWod_Efoyy0RCu6_nJy0)

### Обнаружение столкновений:
![Обнаружение столкновений](https://www.planttext.com/api/plantuml/png/RL5BZe905DptANevNW4MurLCn4Y2BWJZLd7ZmiJD9BfHhz2Y88BW5UhTo6gO3uiXQJgfz-fLrUj-60rcqNmIA0TxF97YWG96uuO4EJAa4ijATgvQZFt0qnyuu2fBss5GICoU11NCPq_x8QjVC3sb-JauuS9ApNh9iHKxKuqNWP8dQo7PQTn_PNEteVeZ3kgQeO6uuHMePCtR4DaIHjtMqaReeQbH8cyA52T2Mz7OctQDjURsj9ymt58sT15p6haC9klMWnU4DkpHvk_opinUSpdMJVO_SphqHuh_duLzpt3-DdVlY5lhnbLz4lWARm00)

### Съедение яблока:

![Съедение яблока](https://www.planttext.com/api/plantuml/png/TLBDJeDW4BptARwZVGLwiAzY8ar9i0UfyLffOerjqeDDzA8UV06aG2a8liBi6paBAD_1al3txUxCxEoEW_d5zVpcoXyuUCONKXnH839842D7XbH2kPFjQ70xzNpNdE45UrbeHeH2GkR4g12T3uqNCBf3D1mONWxUyCb8pNX9s8gPgS4t3qhUMNiaMuF37sq-Qagz2O5iCHJmo9zIFxT4LO02DJddKtTcixRC7-JKz5nMFNEY1wXa_G_ZwJ9IhzG3H7rces-7cZ7jVq_GfOIcRLRME1eQbAf2lfCJAazxP1VRjExiqfjOSf-QYbI78VUjbIrKJKcrxLG7ulg13l1L-x7jUYT4JIwTJ4QWK3P6-vA5BBlAXfhFtoNeC9n-6mxSXrZLo4EZYvnZ5d2pVW00)
