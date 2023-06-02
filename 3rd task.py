print("Введите номер задания")
task = int(input())
if task == 16:
    print("введите количество чисел")
    N = int(input())
    list = []
    for i in range (N):
        print(f"введите {i+1} число")
        list.append(int(input()))
    print("введите искомое число")
    X = int(input())
    count=0
    for i in range(N):
        if list[i] == X:
            count +=1
    print(list)
    print(f"число {X} встречается {count} раз")
if task == 18:
    print("введите количество чисел")
    N = int(input())
    list = []
    for i in range (N):
        print(f"введите {i+1} число")
        list.append(int(input()))
    print("введите искомое число")
    X = int(input())
    count = 0
    flag = True
    while flag:
        for i in range (N):
            if X+count == list[i] or X-count == list[i]:
                answer = list[i]
                flag = False
        count+=1
    print(list)
    print(f"ближайшее число к {X} это - {answer}")
if task == 20:# Программа будет работать по такому принципу, единственное - словарь заполнить до конца надо и написать ещё один для английских букв"
    dict = {'A': '1', 'B':'2', 'C': '2', 'D':'3'}
    print("введите слово")
    word = str(input())
    s = word.upper()
    score = 0
    for i in range(len(word)):
        score += int(dict.get(s[i]))
    print(s)
    print(score)


    