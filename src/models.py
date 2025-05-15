# models.py
class Guest:
    def __init__(self, name: str, age: int):
        self._name = name
        self._age = age

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        self._age = value

    def to_dict(self) -> dict:
        return {"name": self._name, "age": self._age}

    @staticmethod
    def from_dict(data: dict) -> 'Guest':
        return Guest(data["name"], data["age"])


class Gift:
    def __init__(self, name: str, recipient: Guest):
        self._name = name
        self._recipient = recipient

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def recipient(self) -> Guest:
        return self._recipient

    @recipient.setter
    def recipient(self, value: Guest):
        self._recipient = value

    def to_dict(self) -> dict:
        return {"name": self._name, "recipient": self._recipient.to_dict()}

    @staticmethod
    def from_dict(data: dict) -> 'Gift':
        return Gift(data["name"], Guest.from_dict(data["recipient"]))


class Decoration:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def to_dict(self) -> dict:
        return {"name": self._name}

    @staticmethod
    def from_dict(data: dict) -> 'Decoration':
        return Decoration(data["name"])


class Music:
    def __init__(self, name: str):
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    def to_dict(self) -> dict:
        return {"name": self._name}

    @staticmethod
    def from_dict(data: dict) -> 'Music':
        return Music(data["name"])


class Entertainment:
    def __init__(self, name: str, requires_music: bool):
        self._name = name
        self._requires_music = requires_music

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def requires_music(self) -> bool:
        return self._requires_music

    @requires_music.setter
    def requires_music(self, value: bool):
        self._requires_music = value

    def to_dict(self) -> dict:
        return {"name": self._name, "requires_music": self._requires_music}

    @staticmethod
    def from_dict(data: dict) -> 'Entertainment':
        return Entertainment(data["name"], data["requires_music"])


class Holiday:
    def __init__(self, name: str, state: str = "Initial"):
        self._name = name
        self._guests = []
        self._gifts = []
        self._decorations = []
        self._music = []
        self._entertainments = []
        self._food = {}
        self._state = state

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, value: str):
        if value in ["Planned", "InProgress", "Summarized", "InProgressError", "PlannedError"]:
            self._state = value
        else:
            raise ValueError("Недопустимое состояние")

    @property
    def guests(self) -> list[Guest]:
        return self._guests

    @property
    def gifts(self) -> list[Gift]:
        return self._gifts

    @property
    def decorations(self) -> list[Decoration]:
        return self._decorations

    @property
    def music(self) -> list[Music]:
        return self._music

    @property
    def entertainments(self) -> list[Entertainment]:
        return self._entertainments

    @property
    def food(self) -> dict:
        return self._food

    def add_guest(self, guest: Guest):
        self._guests.append(guest)

    def add_gift(self, gift: Gift):
        self._gifts.append(gift)

    def add_decoration(self, decoration: Decoration):
        self._decorations.append(decoration)

    def add_music(self, music: Music):
        self._music.append(music)

    def add_entertainment(self, entertainment: Entertainment):
        self._entertainments.append(entertainment)

    def serve_food(self, dish: str, portions: int):
        self._food[dish] = portions

    def summarize(self) -> str:
        summary = f"Праздник: {self._name}\n"
        summary += f"Гости: {', '.join(g.name for g in self._guests) or 'Нет гостей'}\n"
        summary += f"Подарки: {', '.join(g.name for g in self._gifts) or 'Нет подарков'}\n"
        summary += f"Украшения: {', '.join(d.name for d in self._decorations) or 'Нет украшений'}\n"
        summary += f"Музыка: {', '.join(m.name for m in self._music) or 'Нет музыки'}\n"
        summary += f"Развлечения: {', '.join(e.name for e in self._entertainments) or 'Нет развлечений'}\n"
        summary += f"Еда: {', '.join(f'{k} ({v} порций)' for k, v in self._food.items()) or 'Нет еды'}"
        return summary

    def to_dict(self) -> dict:
        return {
            "name": self._name,
            "guests": [g.to_dict() for g in self._guests],
            "gifts": [g.to_dict() for g in self._gifts],
            "decorations": [d.to_dict() for d in self._decorations],
            "music": [m.to_dict() for m in self._music],
            "entertainments": [e.to_dict() for e in self._entertainments],
            "food": self._food,
            "state": self._state
        }

    @staticmethod
    def from_dict(data: dict) -> 'Holiday':
        holiday = Holiday(data["name"], data["state"])
        holiday._guests = [Guest.from_dict(g) for g in data["guests"]]
        holiday._gifts = [Gift.from_dict(g) for g in data["gifts"]]
        holiday._decorations = [Decoration.from_dict(d) for d in data["decorations"]]
        holiday._music = [Music.from_dict(m) for m in data["music"]]
        holiday._entertainments = [Entertainment.from_dict(e) for e in data["entertainments"]]
        holiday._food = data["food"]
        return holiday