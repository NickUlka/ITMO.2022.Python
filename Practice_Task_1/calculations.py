import math

FOOT_IN_YARD = 3  # константа, определяющая число футов в ярде
FOOT_PER_SECOND = 5280 / 3600  # константа, определяющая, сколько футов/секунду в 1 миле/час


def time_calculation(d_1, d_2, hhh, v_sand, nnn, theta1):
    d_1 *= FOOT_IN_YARD  # перевод в футы
    hhh *= FOOT_IN_YARD  # перевод в футы
    v_sand *= FOOT_PER_SECOND  # перевод в футы в секунду
    xxx = math.tan(math.radians(theta1)) * d_1
    l_1 = math.sqrt(xxx ** 2 + d_1 ** 2)
    l_2 = math.sqrt((hhh - xxx) ** 2 + d_2 ** 2)
    time = (l_1 + nnn * l_2) / v_sand
    return time
