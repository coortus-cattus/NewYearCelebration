def display_menu():
    print("Добро пожаловать в систему подготовки к Новому Году!")
    print("Выберите действие:")
    print("1. Спланировать праздник")
    print("2. Добавить гостя")
    print("3. Назначить подарок")
    print("4. Украсить помещение")
    print("5. Добавить музыку")
    print("6. Приготовить и подать еду")
    print("7. Организовать развлечения")
    print("8. Подвести итоги")
    print("0. Выход")

def main():
    while True:
        display_menu()
        choice = input("Введите номер команды (0-8): ")
        
        try:
            choice = int(choice)
            if choice == 0:
                print("Состояние сохранено. До встречи!")
                break
            elif choice == 1:
                print("Праздник спланирован! (Пока заглушка)")
            elif choice == 2:
                print("Гость добавлен! (Пока заглушка)")
            elif choice == 3:
                print("Подарок назначен! (Пока заглушка)")
            elif choice == 4:
                print("Помещение украшено! (Пока заглушка)")
            elif choice == 5:
                print("Музыка добавлена! (Пока заглушка)")
            elif choice == 6:
                print("Еда подана! (Пока заглушка)")
            elif choice == 7:
                print("Развлечения начаты! (Пока заглушка)")
            elif choice == 8:
                print("Итоги подведены! (Пока заглушка)")
            else:
                print("Ошибка: выберите число от 0 до 8!")
        except ValueError:
            print("Ошибка: введите число!")
        
        print()

if __name__ == "__main__":
    main()