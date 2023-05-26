print("Введите номер задания")
task = int(input())
if task == 10:         # Честно говоря, я вообще не понял задание: раз надо минимальное количество, то 2 варианта:
    print("введите n") 
    n = int(input())
    if n == 1:         # Либо n = 1 и тогда не нужно ничего переворачивать
        print(0)
    else:              # Либо n = любое число, тогда минимальное количество монеток, которые надо перевернуть - 1,    
        print(1)       # Это - случай, когда n-1 монеток лежат одинаково, а одна - нет. В остальных случаях будет не минимальное количество.

if task == 12:
    print("введите произведение")
    S = int(input())
    print("введите сумму")
    P = int(input())
    flag = False
    for i in range (1001):
        if flag == False:
            for j in range(1001):
                if i*j == S and i+j == P and flag == False:
                    print(f"Числа: {i} и {j}")
                    flag = True
if task == 14:
    print("введите N")
    N = int(input())
    count = 0
    flag = True
    while flag:
        if 2**count <= N:
            print(f"2^{count} = {2**count}")
            count+=1
        else:
            flag = False




