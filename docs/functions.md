### Функциональные модели
## Инициализация игры
# Пользователь делает: 
Запускает игру выполнением команды в командной строке.

# Приложение делает: 
Создает окно игры с начальным положением змейки, яблока и других объектов, а также отображает начальное количество очков.

# Пользователь: 
Ознакамливается с начальным состоянием игры и готов начать игру.


## Обновление состояния игры
# Пользователь делает: 
Управляет змейкой, нажимая клавиши со стрелками или другие клавиши, чтобы изменить направление движения.

# Приложение делает: 
Перемещает змейку в соответствии с выбранным направлением, проверяет столкновения с яблоком, препятствиями, бомбами и самой змейкой, а также увеличивает счёт при съедании яблока.

# Пользователь: 
Наблюдает за изменением положения змейки, съеданием яблок и взрывами бомб, а также следит за текущим счётом.

# Приложение: 
Обновляет экран, отображая текущее состояние игры, включая положение змейки, яблок, препятствий и счёт.

## Проверка столкновений
# Пользователь делает: 
Управляет змейкой, пытаясь избегать столкновений с препятствиями, бомбами и самой собой.

# Приложение делает: 
Проверяет каждый шаг змейки на возможные столкновения с границами игрового поля, яблоками, препятствиями, бомбами и другими сегментами змейки.

# Пользователь: 
Наблюдает за тем, как змейка меняет своё поведение при приближении к препятствиям или бомбам, а также взрывается при столкновении.

# Приложение: 
Регистрирует столкновения и соответственно изменяет состояние игры: либо увеличивает длину змейки при съедании яблока, либо завершает игру при столкновении с препятствием, бомбой или самой собой.

## Генерация новых объектов
# Пользователь делает: 
Наблюдает за происходящим в игре и ожидает появления новых объектов, таких как яблоки и препятствия.

# Приложение делает: 
Периодически создает новые объекты (яблоки и бомбы) на случайных позициях на игровом поле, исключая местоположения, занятые другими объектами.

# Пользователь: 
Реагирует на появление новых объектов, стремясь съесть яблоко и избегать бомб.

# Приложение: 
Обновляет отображение, чтобы отразить появление новых объектов, и продолжает игровой процесс.

## Обработка ввода пользователя
# Пользователь делает: 
Нажимает клавиши на клавиатуре, указывая направление движения змейки или выполняя другие действия в игре.

# Приложение делает: 
Получает данные о вводе пользователя, а затем изменяет состояние игры в соответствии с этим вводом.

# Пользователь: 
Наблюдает за реакцией змейки на свои команды и пытается достичь желаемого результата в игре.

# Приложение: 
Изменяет направление движения змейки, генерирует новые объекты или завершает игру в зависимости от действий пользователя.

## Диаграмма активности
[Код диаграммы](piclab3/activity)
![Диаграмма активности](https://www.planttext.com/api/plantuml/png/bPJ1RjD048RlVefHJ-NG0ssQL1nG9GvS8rKym2fTGXJ7gMptK26a9Zc0AAe55xW0Gho0u-BKJLBd5MRVg3Excs0l0ObAgTJiVD_-EpFgSHIBC3uV-9ulNyOG3o7iTL_5SDeBPIVk3GClwlU2Cn6A0Po9JbzqvKbyuKlWOn5qVUbveXCFGsZxuaA6829eUvj3s3a9H5_2Sp6GE_3Q0_evZsH7H19syIkcwYrznke3u3sMcAc9kWOiy4PTgiaZbhruzjYXVk9ANMAA6IvKOjXRN6AETpWdnvt5zXtiXtgFkHffG2KunGKL4s3B3vpoxtH7eQiAqXUC4Pm0pYlq9cF3eR-fCRcvvhxAbceCEdrElpaxnQ5t52gndaF7yuNkdbBrp7P90oM9vwPVTCGN97G0L5XI7wQL7ZGTtIVIbNHzPdILK9PLLvPiEUHdtV2SnlBEFCYTqf6dYJRixJtbeS4JqD2AHZgYk2d1usrJhc7xZDK6RB3QW7KNT1CNMhp40dIt6IdqqoPalj9cTXhtWOcq5gM0l-Zjt51AOlDL5YDryCOMdA-RCMWwcV7xqj_fpNGetJ-qXtzeLvNDcvbSwytRkZlNZh7vNyRrqkJMqhIM5bi-saDoP7ZBFUNLsV3qHS9DnANUlzgGhAvXTKTkA1q_rHCiwjBHrcVItqlhRFtDkJMaiz_U6-zO1gVy7-y1)

## Начать новую игру
[Код диаграммы](piclab3/func1)
![Начать новую игру](https://www.planttext.com/api/plantuml/png/TL91Ji9G4Dtt53-iu0gma2Du1H9AQ5ABiHZ33cYYKTGckc6ZNg4KlYr5FbUOkH5lVgcH80lwE-MzcVVU_7OuxDmCRwzynxuuJVeYGnj-fWndIWbFIKkjQ4i9VLDEFpWrJnKL-6HeHmL7gdRfTqQrbkFrL9q-G7iGQab37uxuLO6xv3575mqrxBk1ge_SiE4erQGvK3dV0v3G1iyCP5GSLvnPo-8-eSRGWiTMYXOMwGF6oZMq9AEWIJp49UdT0hMGggOPJ6XQmq4EjkAO5fXhK2TdEJiK6iyOjYRGaMBiMjZW6lHR2FEkx_ak4fXRHOc2pWBO76Z41-DUY7zNb8Zlyuviw8YL7t6A8vwGiLCDj6vFah6TeCDc3IU_oTWWy3kq5ffCUxBjPN9gzwhu1RLeWEcgONaH8cpokDtftO2weee-jLjObK6wGRTAHDASbjj-uncj9HNnaFqnuleXeC7WVvWi83zs0qhGzNgukuDhfurtkSZE7W00)

## Управлять змейкой
[Код диаграммы](piclab3/func2)
![Управлять змейкой](https://www.planttext.com/api/plantuml/png/fLDDJi9G4Dxt5BE4Ay12hc9Y2KqGZM2CEsmtHaXOuaQ9DoW5z45fkSBCZVnc-XD8chXmqRxslPdlhzFUU7BzC7cy7Nhsu7LunJcdCkSVh0d74l9EtuapZlcR7H-nxYGaUP5GfdhA1tQ4MugJ11LeaaYcCkjwJuDWw5EBttc3sfXGSG2aGntmhjeKZ76wvRZj4GLzF7yOZVB6PvZoQjMJWJ-YrhC_rdAY3d_o6a2vbOILofDIOIk5k0nSEuAR8rxsXT84sj6JWoDHA-h4X3iSL4PLGSxxIms0w9RCAtIgU-1QVybV4qbaI0IGBQ0pKWkyKVPISSx7PhskuB0ubhLmG6sXsRXuew985h2V0kZGb4wPZu6lpMri6W7n1ao4NgPp3jEjMxz0edhKfiDLZaCHSg7_eZKlMltHJT1lrc_QSvkNJ29rW9svPNwoB4-oEFiQoBRPrDBIWYv4MiRkTBua-bC2-Z3O88ENMe1cGneH2jSo-nzfiU9UZRuc6BRnVztTUptiwy_s2m00)

## Съесть яблоко:
[Код диаграммы](piclab3/func3)
![Съесть яблоко](https://www.planttext.com/api/plantuml/png/pP9DJiCm48NtFiKiwGwsoO9U1ObKL6eB8c5VqaKaYjGD4WVe0KZRH0HAV8OtD-9vWWhzEG0BIzOyls-UxUcdsTLzzZ0UETku2A_uGeqFVA8KLF3wg3aQR52YrbnqWHMsy46FtN0WPtZRLRpmz1Fj5LSBVzcJx2QPy4o5ikT48YonfhP5emLNhi_1KXWwTD5fXnRQIxau5mOe0Xdhc7xhznBifkDz5xOHdVr5Ss-1ILySnJWTXAg1TROFxbfvoXGPbyB6v5Rp-9_Jab6QyDvjU8fJDm_VrA3-vS-F-BKmmPIL5L_uvqKDFRaU3jnXWsXl7CnEupnK3eOZTXqXpMxlN9_xC8NV)
