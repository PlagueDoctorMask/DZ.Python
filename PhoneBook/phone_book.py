"""Создать телефонный справочник с
возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться
в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в
текстовом файле
3. Пользователь может ввести одну из
характеристик для поиска определенной
записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа
не должна быть линейной"""

def Show_contacts():
    with open ('phon.txt', 'r') as file:
        for line in file:
            print(line)
def Add_contact():
    contact = input("Введите Имя, фамилию, отчество, номер через пробел: ").split()
    with open ('phon.txt', 'a') as file:
        file.write("\n")
        file.write(', '.join(contact))
    print()
    print("Контакт успешно сохранён")
def Delete_contact():
    p = input("Введите контакт, который хотите удалить: ")
    with open("phon.txt", "r") as file:
        lines = file.readlines()
    with open("phon.txt", "w") as file:
        for line in lines:
            if line.strip("\n") != p:
                file.write(line)
    print()
    print("Контакт успешно удалён")
def Find_by_surname():
    p = input("Введите фамилию: ")
    with open ('phon.txt', 'r') as file:
        for line in file:
            check = line.split(", ")
            #print(check[0])
            if check[0] == p:
                print(line)
def Find_by_name():
    p = input("Введите имя: ")
    with open ('phon.txt', 'r') as file:
        for line in file:
            check = line.split(", ")
            #print(check[1])
            if check[1] == p:
                print(line)
def Find_by_number():
    p = int(input("Введите номер: "))
    with open ('phon.txt', 'r') as file:
        for line in file:
            check = line.split(", ")
            #print(check[2])
            if int(check[2]) == p:
                print(line)


flag = True
while flag:
    print("\nВыберите необходимое действие:\n"
          "1. Вывести справочник на экран\n"
          "2. Добавить контакт\n"
          "3. Удалить контакт\n"
          "4. Найти контакт по фамилии\n"
          "5. Найти контакт по имени\n"
          "6. Найти контакт по номеру\n"
          "7. Завершить работу программы\n")
    choice = int(input())
    if choice == 1:
        Show_contacts()
    elif choice == 2:
        Add_contact()
    elif choice == 3:
        Delete_contact()
    elif choice == 4:
        Find_by_surname()
    elif choice == 5:
        Find_by_name()
    elif choice == 6:
        Find_by_number()
    elif choice == 7:
        print("Окончание работы")
        flag = False


