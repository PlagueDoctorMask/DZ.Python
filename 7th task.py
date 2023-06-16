print("Введите номер задания")
task = int(input())
if task == 34:
    vowels = ['а', 'у', 'о', 'ы', 'и', 'е', 'ё', 'э', 'ю', 'я']
    str = input("введите строку: ")
    phrases = str.split()
    vowels_in_first_word = 0
    for i in range(len(vowels)):
            if vowels[i] in phrases[0]:
                vowels_in_first_word+=1
    flag = True
    flag1 = True
    count = 0
    vowels_in_word = 0
    while flag:
        if count < len(phrases):
            for i in range(len(phrases)):
                for j in range(len(phrases[i])):
                    for p in range(len(vowels)):
                        if vowels[p] == phrases[i][j]:
                            vowels_in_word+=1
                if vowels_in_first_word != vowels_in_word:
                    flag = False
                    flag1 = False
                vowels_in_word = 0
        else:
            flag = False
        count+=1
    if flag1 == True:
        print("Парам пам-пам")
    else:
        print("Пам парам")
if task == 36:
    def print_operation_table(function, num_rows, num_columns):
        for i in range(1, num_rows+1):
            print()
            for j in range(1, num_columns+1):
                print(function(i,j), end = ' ')

    print("Введите количество строк")
    x = int(input())
    print("Введите количество столбцов")
    y = int(input())  
    print_operation_table(lambda x, y: x * y, x, y)