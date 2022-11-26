import sys
from random import randint
import time


def input_gamers():
    """ввод имен игроков"""
    igrok1 = input('Введите имя 1-го играющего ')
    igrok2 = input('Введите имя 2-го играющего ')
    return igrok1, igrok2


def throw_the_dice(gamer):
    """бросить кости"""
    print('Кубик бросает', gamer)
    time.sleep(2)
    n = randint(1, 6)
    print('Выпало:', n)
    return n


gamer1, gamer2 = input_gamers()


def win_in_one_game(n1, n2):
    """Who wins in one game"""
    score1 = 0
    score2 = 0
    if n1 > n2:
        print('Выиграл', gamer1)
        score1 += 1
    elif n1 < n2:
        print('Выиграл', gamer2)
        score2 += 1
    else:
        print('Ничья')
    return score1, score2


def scores():
    """Total score of all games"""
    scores11 = scores22 = 0
    for i in range(5):
        scores1, scores2 = win_in_one_game(throw_the_dice(gamer1), (throw_the_dice(gamer2)))
        scores11 += scores1
        scores22 += scores2
    return scores11, scores22


def total_winner(scor1, scor2):
    """Absolute winner"""
    if scor1 > scor2:
        print("Победитель - ", gamer1, "со счетом - ",
              scor1, "против ", scor2)
    elif scor1 < scor2:
        print("Победитель - ", gamer2, "со счетом - ",
              scor2, "против ", scor1)
    else:
        print("В итоге победила дружба! Счет: ", scor1,
              " : ", scor2)
    sys.exit()


scored1, scored2 = scores()
total_winner(scored1, scored2)
