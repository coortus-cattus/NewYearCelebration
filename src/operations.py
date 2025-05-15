# operations.py
import storage as st
import models as m


class CLI:
    def __init__(self, holiday: 'm.Holiday', storage: 'st.Storage'):
        self._holiday = holiday
        self._storage = storage

    def _display_menu(self):
        """Отображает меню в зависимости от текущего состояния праздника."""
        print(f"\nТекущее состояние: {self._holiday.state}")
        print("Меню:")

        if self._holiday.state in ["Planned", "PlannedError"]:
            print("1. Создать новый праздник")
            print("2. Загрузить существующий праздник")
            print("0. Выход")
        else:  # InProgress, InProgressError, Summarized
            print("3. Добавить гостя")
            print("4. Назначить подарок")
            print("5. Выбрать украшения")
            print("6. Добавить музыку")
            print("7. Приготовить еду")
            print("8. Организовать развлечения")
            print("9. Подвести итоги")
            print("0. Выход")

    def _get_non_empty_input(self, prompt: str) -> str:
        """Запрашивает непустой текстовый ввод от пользователя."""
        while True:
            value = input(prompt).strip()
            if value:
                return value
            print("Ошибка: поле не может быть пустым. Попробуйте снова.")

    def _set_error_state(self):
        """Устанавливает состояние ошибки в зависимости от текущего состояния."""
        if self._holiday.state in ["Planned", "PlannedError"]:
            self._holiday.state = "PlannedError"
        else:
            self._holiday.state = "InProgressError"
        self._storage.save(self._holiday)

    def _reset_to_normal_state(self, choice: int):
        """Сбрасывает состояние ошибки в нормальное перед корректным действием."""
        if self._holiday.state == "PlannedError" and choice in [0, 1, 2]:
            self._holiday.state = "Planned"
        elif self._holiday.state == "InProgressError" and choice in [0, 3, 4, 5, 6, 7, 8, 9]:
            self._holiday.state = "InProgress"

    def _create_new_holiday(self):
        """Создаёт новый праздник с указанным названием."""
        name = self._get_non_empty_input("Введите название нового праздника: ")
        self._holiday = m.Holiday(name, "InProgress")
        self._storage.save(self._holiday)
        print(f"Новый праздник '{name}' создан. Предыдущее состояние перезаписано.")

    def _load_existing_holiday(self):
        """Загружает существующий праздник из хранилища."""
        loaded_data = self._storage.load()
        if loaded_data:
            self._holiday = m.Holiday.from_dict(loaded_data)
            if self._holiday.state in ["PlannedError", "Summarized", "Planned"]:
                if self._holiday.state == "Summarized":
                    print("Праздник вышел из состояния подведения итогов и может продолжить планирование.")
                self._holiday.state = "InProgress"
                self._storage.save(self._holiday)
            print(f"Загружен праздник: {self._holiday.name} (состояние: {self._holiday.state})")
        else:
            print("Сохранённое состояние не найдено.")

    def _add_guest(self):
        """Добавляет нового гостя к празднику."""
        name = self._get_non_empty_input("Введите имя гостя: ")
        age_input = self._get_non_empty_input("Введите возраст гостя: ")
        age = int(age_input)
        self._holiday.add_guest(m.Guest(name, age))
        self._holiday.state = "InProgress"
        self._storage.save(self._holiday)
        print(f"Гость '{name}' добавлен.")

    def _assign_gift(self):
        """Назначает подарок одному из гостей."""
        print(f"Гостей: {len(self._holiday.guests)}")
        if not self._holiday.guests:
            print("Сначала добавьте гостей.")
            return

        gift_name = self._get_non_empty_input("Введите название подарка: ")
        guest_name = self._get_non_empty_input("Введите имя получателя: ")
        recipient = next((g for g in self._holiday.guests if g.name.lower() == guest_name.lower()), None)

        if recipient:
            self._holiday.add_gift(m.Gift(gift_name, recipient))
            self._holiday.state = "InProgress"
            self._storage.save(self._holiday)
            print(f"Подарок '{gift_name}' добавлен для '{recipient.name}'.")
        else:
            print(f"Гость '{guest_name}' не найден. Доступные гости: {', '.join(g.name for g in self._holiday.guests)}")

    def _add_decoration(self):
        """Добавляет украшение к празднику."""
        decoration = self._get_non_empty_input("Введите название украшения: ")
        self._holiday.add_decoration(m.Decoration(decoration))
        self._holiday.state = "InProgress"
        self._storage.save(self._holiday)
        print(f"Украшение '{decoration}' добавлено.")

    def _add_music(self):
        """Добавляет музыкальный трек к празднику."""
        music = self._get_non_empty_input("Введите название музыки: ")
        self._holiday.add_music(m.Music(music))
        self._holiday.state = "InProgress"
        self._storage.save(self._holiday)
        print(f"Музыка '{music}' добавлена.")

    def _prepare_food(self):
        """Добавляет блюдо и количество порций к празднику."""
        if not self._holiday.guests:
            print("Сначала добавьте гостей.")
            return

        dish = self._get_non_empty_input("Введите название блюда: ")
        portions_input = self._get_non_empty_input("Введите количество порций: ")
        portions = int(portions_input)
        self._holiday.serve_food(dish, portions)
        self._holiday.state = "InProgress"
        self._storage.save(self._holiday)
        print(f"Блюдо '{dish}' ({portions} порций) добавлено.")

    def _organize_entertainment(self):
        """Добавляет развлечение к празднику."""
        if not self._holiday.music:
            print("Сначала добавьте музыку.")
            return

        entertainment = self._get_non_empty_input("Введите название развлечения: ")
        self._holiday.add_entertainment(m.Entertainment(entertainment, True))
        self._holiday.state = "InProgress"
        self._storage.save(self._holiday)
        print(f"Развлечение '{entertainment}' добавлено.")

    def _summarize_holiday(self):
        """Подводит итоги праздника и завершает программу."""
        print(self._holiday.summarize())
        self._holiday.state = "Summarized"
        self._storage.save(self._holiday)
        print("Состояние изменено на Summarized.")
        print("Состояние сохранено. Программа завершена.")

    def run(self):
        """Запускает основной цикл программы."""
        while True:
            self._display_menu()

            try:
                choice_input = input("Выберите действие (0-9): ").strip()
                if not choice_input:
                    self._set_error_state()
                    print("Ошибка: выбор не может быть пустым. Введите число от 0 до 9.")
                    continue

                choice = int(choice_input)
                self._reset_to_normal_state(choice)

                if choice == 0:
                    self._holiday.state = "Planned"
                    self._storage.save(self._holiday)
                    print("Состояние сохранено. Программа завершена.")
                    break

                elif choice == 1 and self._holiday.state in ["Planned", "PlannedError"]:
                    self._create_new_holiday()

                elif choice == 2 and self._holiday.state in ["Planned", "PlannedError", "Summarized"]:
                    self._load_existing_holiday()

                elif choice == 3 and self._holiday.state in ["InProgress"]:
                    self._add_guest()

                elif choice == 4 and self._holiday.state in ["InProgress"]:
                    self._assign_gift()

                elif choice == 5 and self._holiday.state in ["InProgress"]:
                    self._add_decoration()

                elif choice == 6 and self._holiday.state in ["InProgress"]:
                    self._add_music()

                elif choice == 7 and self._holiday.state in ["InProgress"]:
                    self._prepare_food()

                elif choice == 8 and self._holiday.state in ["InProgress"]:
                    self._organize_entertainment()

                elif choice == 9 and self._holiday.state in ["InProgress"]:
                    self._summarize_holiday()
                    break

                else:
                    self._set_error_state()
                    print(f"Некорректный выбор или действие недоступно в текущем состоянии (выбор: {choice}).")

            except ValueError:
                self._set_error_state()
                print("Ошибка: введите число от 0 до 9.")