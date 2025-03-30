# Диаграмма классов

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

## Черновик диаграммы
- [Holiday] --> 1..* [Guest]
- [Holiday] --> 1..* [Gift]
- [Holiday] --> 1..* [Decoration]
- [Holiday] --> 1..* [Music]
- [Holiday] --> 1..* [Entertainment]
- [Gift] --> *..1 [Guest]
- [Storage] --> 1..1 [Holiday]
- [CLI] --> 1..1 [Holiday]
- [CLI] --> 1..1 [Storage]