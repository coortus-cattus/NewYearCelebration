# NewYearCelebration

## Описание

CLI-приложение для планирования и управления подготовкой к Новому Году. Пользователь взаимодействует через меню, выбирая действия по номеру:
- 1. Создать праздник с названием.
- 2. Загрузить существующий праздник.
- 3. Добавить гостей (имя, возраст).
- 4. Назначить подарки гостям (название подарка, для кого).
- 5. Выбрать украшения (название).
- 6. Добавить музыку (название).
- 7. Приготовить и подать еду (блюдо, порции, проверка гостей).
- 8. Организовать развлечения (тип, проверка музыки).
- 9. Подвести итоги (гости, подарки, украшения, еда, развлечения).
- 0. Выход с сохранением состояния.
Состояние сохраняется в JSON и восстанавливается при запуске.

## Классы и их члены

1. **Holiday**
   - Атрибуты:
     - `-name: str`
     - `-guests: list[Guest]`
     - `-gifts: list[Gift]`
     - `-decorations: list[Decoration]`
     - `-music: list[Music]`
     - `-entertainments: list[Entertainment]`
     - `-food: dict`
   - Методы:
     - `+__init__(name: str)`
     - `+name(): str` (геттер через @property)
     - `+name(value: str)` (сеттер через @name.setter)
     - `+guests(): list[Guest]` (геттер)
     - `+add_guest(guest: Guest)`
     - `+gifts(): list[Gift]` (геттер)
     - `+add_gift(gift: Gift)`
     - `+decorations(): list[Decoration]` (геттер)
     - `+add_decoration(decoration: Decoration)`
     - `+music(): list[Music]` (геттер)
     - `+add_music(music: Music)`
     - `+entertainments(): list[Entertainment]` (геттер)
     - `+add_entertainment(entertainment: Entertainment)`
     - `+food(): dict` (геттер)
     - `+serve_food(dish: str, portions: int)`
     - `+summarize(): str`

2. **Guest**
   - Атрибуты:
     - `-name: str`
     - `-age: int`
   - Методы:
     - `+__init__(name: str, age: int)`
     - `+name(): str` (геттер)
     - `+name(value: str)` (сеттер)
     - `+age(): int` (геттер)
     - `+age(value: int)` (сеттер)

3. **Gift**
   - Атрибуты:
     - `-name: str`
     - `-recipient: Guest`
   - Методы:
     - `+__init__(name: str, recipient: Guest)`
     - `+name(): str` (геттер)
     - `+name(value: str)` (сеттер)
     - `+recipient(): Guest` (геттер)
     - `+recipient(value: Guest)` (сеттер)

4. **Decoration**
   - Атрибуты:
     - `-name: str`
   - Методы:
     - `+__init__(name: str)`
     - `+name(): str` (геттер)
     - `+name(value: str)` (сеттер)

5. **Music**
   - Атрибуты:
     - `-name: str`
   - Методы:
     - `+__init__(name: str)`
     - `+name(): str` (геттер)
     - `+name(value: str)` (сеттер)

6. **Entertainment**
   - Атрибуты:
     - `-name: str`
     - `-requires_music: bool`
   - Методы:
     - `+__init__(name: str, requires_music: bool)`
     - `+name(): str` (геттер)
     - `+name(value: str)` (сеттер)
     - `+requires_music(): bool` (геттер)
     - `+requires_music(value: bool)` (сеттер)

7. **Storage**
   - Атрибуты:
     - `-file_path: str`
   - Методы:
     - `+__init__(file_path: str)`
     - `+save(holiday: Holiday)`
     - `+load(): Holiday`

8. **CLI**
   - Атрибуты:
     - `-holiday: Holiday`
     - `-storage: Storage`
   - Методы:
     - `+__init__(holiday: Holiday, storage: Storage)`
     - `+run()` (запускает интерфейс)
     - `-display_menu()` (приватный метод для вывода меню)

---
 Более подробная информация в папке docs с диаграммами классов и состояний.