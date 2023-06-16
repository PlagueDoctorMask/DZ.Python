print("Введите номер задания")
task = int(input())
if task == 26:
    def S(a,b):
        if b == 1:
            return a
        else:
            return a * S(a,b-1)
    print("Введите a")
    a = int(input())
    print("Введите b")
    b = int(input())
    print(S(a,b))
if task == 28:
    def sum(a, b):
        if a == 0:
            return b
        return sum(a - 1, b + 1)
    print("Введите a")
    a = int(input())
    print("Введите b")
    b = int(input())
    print(sum(a,b))
        