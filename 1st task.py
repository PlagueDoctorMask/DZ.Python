print("Введите номер задания")
task = int(input())
if task == 2:
    print("Введите число")
    a = int(input())
    b = a # просто для красивого вывода
    sum = 0
    while a > 0:
        sum += a%10
        a = a//10
    print(f"сумма цифр числа {b} равна {sum}")
if task == 4:#правильный ответ выдаётся в случае, если он математически возможен, так что не все числа подходят
    print("Введите суммарное число корабликов")
    S = int(input())
    k = S//3 + S//3 #количество катиных корабликов
    p = S//6 #количство корабликов Пети и Серёжи
    print(f" Всего {S} корабликов: у Кати {k} корабликов, у Пети с Серёжей по {p}")
if task == 6:
    print("введите шестизначный номер билета")
    N = input()
    if len(N) != 6:
        print("Написано же шестизначный, это - когда 6 цифр в числе, давай поновой")
    else:
        N = int(N)
        sum1 = sum2 = 0
        for i in range(3):
            sum2 += N%10
            N = N//10
        for i in range(3):
            sum1 += N%10
            N = N//10
        if sum1 == sum2:
            print("Билет счастливый")
        else:
            print("Билет не счастливый")
if task == 8:
    print("Введите число n")
    n = int(input())
    print("Введите число m")
    m = int(input())
    print("Введите число k")
    k = int(input())
    if k>=n or k>=m:
        print("yes")
    else:
        print("no")