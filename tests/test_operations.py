# tests/test_models.py
import unittest
import sys
import os

# Добавляем путь к папке src в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from models import Guest, Gift, Decoration, Music, Entertainment, Holiday


class TestModels(unittest.TestCase):
    def test_guest_creation_and_properties(self):
        """Проверяет создание объекта Guest и работу геттеров/сеттеров."""
        guest = Guest("Влад", 18)
        self.assertEqual(guest.name, "Влад")
        self.assertEqual(guest.age, 18)

        guest.name = "Ника"
        guest.age = 20
        self.assertEqual(guest.name, "Ника")
        self.assertEqual(guest.age, 20)

    def test_guest_serialization(self):
        """Проверяет сериализацию и десериализацию Guest."""
        guest = Guest("Влад", 18)
        guest_dict = guest.to_dict()
        self.assertEqual(guest_dict, {"name": "Влад", "age": 18})

        restored_guest = Guest.from_dict(guest_dict)
        self.assertEqual(restored_guest.name, "Влад")
        self.assertEqual(restored_guest.age, 18)

    def test_gift_creation_and_properties(self):
        """Проверяет создание объекта Gift и работу геттеров/сеттеров."""
        guest = Guest("Влад", 18)
        gift = Gift("Книга", guest)
        self.assertEqual(gift.name, "Книга")
        self.assertEqual(gift.recipient, guest)

        gift.name = "Игрушка"
        new_guest = Guest("Ника", 20)
        gift.recipient = new_guest
        self.assertEqual(gift.name, "Игрушка")
        self.assertEqual(gift.recipient, new_guest)

    def test_gift_serialization(self):
        """Проверяет сериализацию и десериализацию Gift."""
        guest = Guest("Влад", 18)
        gift = Gift("Книга", guest)
        gift_dict = gift.to_dict()
        self.assertEqual(gift_dict, {"name": "Книга", "recipient": {"name": "Влад", "age": 18}})

        restored_gift = Gift.from_dict(gift_dict)
        self.assertEqual(restored_gift.name, "Книга")
        self.assertEqual(restored_gift.recipient.name, "Влад")
        self.assertEqual(restored_gift.recipient.age, 18)

    def test_decoration_creation_and_serialization(self):
        """Проверяет создание и сериализацию Decoration."""
        decoration = Decoration("Гирлянда")
        self.assertEqual(decoration.name, "Гирлянда")

        decoration_dict = decoration.to_dict()
        self.assertEqual(decoration_dict, {"name": "Гирлянда"})

        restored_decoration = Decoration.from_dict(decoration_dict)
        self.assertEqual(restored_decoration.name, "Гирлянда")

    def test_music_creation_and_serialization(self):
        """Проверяет создание и сериализацию Music."""
        music = Music("Jingle Bells")
        self.assertEqual(music.name, "Jingle Bells")

        music_dict = music.to_dict()
        self.assertEqual(music_dict, {"name": "Jingle Bells"})

        restored_music = Music.from_dict(music_dict)
        self.assertEqual(restored_music.name, "Jingle Bells")

    def test_entertainment_creation_and_serialization(self):
        """Проверяет создание и сериализацию Entertainment."""
        entertainment = Entertainment("Танцы", True)
        self.assertEqual(entertainment.name, "Танцы")
        self.assertTrue(entertainment.requires_music)

        entertainment_dict = entertainment.to_dict()
        self.assertEqual(entertainment_dict, {"name": "Танцы", "requires_music": True})

        restored_entertainment = Entertainment.from_dict(entertainment_dict)
        self.assertEqual(restored_entertainment.name, "Танцы")
        self.assertTrue(restored_entertainment.requires_music)

    def test_holiday_creation_and_properties(self):
        """Проверяет создание объекта Holiday и работу геттеров/сеттеров."""
        holiday = Holiday("НГ", "Planned")
        self.assertEqual(holiday.name, "НГ")
        self.assertEqual(holiday.state, "Planned")
        self.assertEqual(holiday.guests, [])
        self.assertEqual(holiday.gifts, [])
        self.assertEqual(holiday.decorations, [])
        self.assertEqual(holiday.music, [])
        self.assertEqual(holiday.entertainments, [])
        self.assertEqual(holiday.food, {})

        holiday.name = "Новый год"
        holiday.state = "InProgress"
        self.assertEqual(holiday.name, "Новый год")
        self.assertEqual(holiday.state, "InProgress")

    def test_holiday_invalid_state(self):
        """Проверяет, что установка недопустимого состояния вызывает ошибку."""
        holiday = Holiday("НГ", "Planned")
        with self.assertRaises(ValueError):
            holiday.state = "Invalid"

    def test_holiday_add_methods(self):
        """Проверяет методы добавления элементов в Holiday."""
        holiday = Holiday("НГ", "InProgress")
        guest = Guest("Влад", 18)
        gift = Gift("Книга", guest)
        decoration = Decoration("Гирлянда")
        music = Music("Jingle Bells")
        entertainment = Entertainment("Танцы", True)

        holiday.add_guest(guest)
        holiday.add_gift(gift)
        holiday.add_decoration(decoration)
        holiday.add_music(music)
        holiday.add_entertainment(entertainment)
        holiday.serve_food("Салат", 5)

        self.assertEqual(holiday.guests, [guest])
        self.assertEqual(holiday.gifts, [gift])
        self.assertEqual(holiday.decorations, [decoration])
        self.assertEqual(holiday.music, [music])
        self.assertEqual(holiday.entertainments, [entertainment])
        self.assertEqual(holiday.food, {"Салат": 5})

    def test_holiday_summarize(self):
        """Проверяет метод summarize для Holiday."""
        holiday = Holiday("НГ", "InProgress")
        holiday.add_guest(Guest("Влад", 18))
        holiday.add_gift(Gift("Книга", Guest("Влад", 18)))
        holiday.add_decoration(Decoration("Гирлянда"))
        holiday.add_music(Music("Jingle Bells"))
        holiday.add_entertainment(Entertainment("Танцы", True))
        holiday.serve_food("Салат", 5)

        summary = holiday.summarize()
        expected = (
            "Праздник: НГ\n"
            "Гости: Влад\n"
            "Подарки: Книга\n"
            "Украшения: Гирлянда\n"
            "Музыка: Jingle Bells\n"
            "Развлечения: Танцы\n"
            "Еда: Салат (5 порций)"
        )
        self.assertEqual(summary, expected)

    def test_holiday_serialization(self):
        """Проверяет сериализацию и десериализацию Holiday."""
        holiday = Holiday("НГ", "InProgress")
        holiday.add_guest(Guest("Влад", 18))
        holiday.add_gift(Gift("Книга", Guest("Влад", 18)))
        holiday.add_decoration(Decoration("Гирлянда"))
        holiday.add_music(Music("Jingle Bells"))
        holiday.add_entertainment(Entertainment("Танцы", True))
        holiday.serve_food("Салат", 5)

        holiday_dict = holiday.to_dict()
        restored_holiday = Holiday.from_dict(holiday_dict)

        self.assertEqual(restored_holiday.name, "НГ")
        self.assertEqual(restored_holiday.state, "InProgress")
        self.assertEqual(len(restored_holiday.guests), 1)
        self.assertEqual(restored_holiday.guests[0].name, "Влад")
        self.assertEqual(len(restored_holiday.gifts), 1)
        self.assertEqual(restored_holiday.gifts[0].name, "Книга")
        self.assertEqual(len(restored_holiday.decorations), 1)
        self.assertEqual(restored_holiday.decorations[0].name, "Гирлянда")
        self.assertEqual(len(restored_holiday.music), 1)
        self.assertEqual(restored_holiday.music[0].name, "Jingle Bells")
        self.assertEqual(len(restored_holiday.entertainments), 1)
        self.assertEqual(restored_holiday.entertainments[0].name, "Танцы")
        self.assertEqual(restored_holiday.food, {"Салат": 5})


if __name__ == "__main__":
    unittest.main()