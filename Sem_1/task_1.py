# Задание №5
# Работа в консоли в режиме интерпретатора Python.
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e.
# Используйте while и if.
# Попробуйте разные значения e и n

n = 10
e = 2
summ = 0
el = 0
while el <= n:
    el += 1
    if el % 2 == 0:
        if el % e == 0:
            continue
    summ += el
print(summ)            