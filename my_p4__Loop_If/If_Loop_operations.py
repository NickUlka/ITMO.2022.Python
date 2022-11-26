from random import randint
import time

# Ввод имен играющих
igrok1 = input('Введите имя 1-го играющего ')
igrok2 = input('Введите имя 2-го играющего ')
score1 = 0
score2 = 0
# Моделирование бросания кубика первым играющим
for i in range(5):
    print('Кубик бросает', igrok1)
    time.sleep(2)
    n1 = randint(1, 6)
    print('Выпало:', n1)
# Моделирование бросания кубика вторым играющим
    print('Кубик бросает', igrok2)
    time.sleep(2)
    n2 = randint(1, 6)
    print('Выпало:', n2)
    if n1 > n2:
        print('Выиграл', igrok1)
        score1 += 1
    elif n1 < n2:
        print('Выиграл', igrok2)
        score2 += 1
    else:
        print('Ничья')
if score1 > score2:
    print("Победитель - ", igrok1, "со счетом - ",
          score1, "против ", score2)
elif score1 < score2:
    print("Победитель - ", igrok2, "со счетом - ",
          score2, "против ", score1)
else:
    print("В итоге победила дружба! Счет: ", score1,
          " : ", score2)
