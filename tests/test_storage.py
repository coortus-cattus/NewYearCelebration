# tests/test_storage.py
import unittest
import os
import json
from src.storage import Storage
from src.models import Holiday, Guest


class TestStorage(unittest.TestCase):
    def setUp(self):
        """Создаёт временный файл для тестов."""
        self.test_file = "test_holiday_state.json"
        self.storage = Storage(self.test_file)

    def tearDown(self):
        """Удаляет временный файл после тестов."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_save_and_load_holiday(self):
        """Проверяет сохранение и загрузку праздника."""
        holiday = Holiday("НГ", "Planned")
        holiday.add_guest(Guest("Влад", 18))
        self.storage.save(holiday)

        loaded_data = self.storage.load()
        self.assertIsNotNone(loaded_data)
        restored_holiday = Holiday.from_dict(loaded_data)

        self.assertEqual(restored_holiday.name, "НГ")
        self.assertEqual(restored_holiday.state, "Planned")
        self.assertEqual(len(restored_holiday.guests), 1)
        self.assertEqual(restored_holiday.guests[0].name, "Влад")

    def test_load_nonexistent_file(self):
        """Проверяет загрузку из несуществующего файла."""
        loaded_data = self.storage.load()
        self.assertIsNone(loaded_data)

    def test_load_corrupted_file(self):
        """Проверяет загрузку из повреждённого файла."""
        with open(self.test_file, "w", encoding="utf-8") as file:
            file.write("invalid json")
        
        loaded_data = self.storage.load()
        self.assertIsNone(loaded_data)

    def test_save_overwrites_file(self):
        """Проверяет, что сохранение перезаписывает существующий файл."""
        holiday1 = Holiday("НГ", "Planned")
        holiday1.add_guest(Guest("Влад", 18))
        self.storage.save(holiday1)

        holiday2 = Holiday("ДР", "InProgress")
        holiday2.add_guest(Guest("Ника", 20))
        self.storage.save(holiday2)

        loaded_data = self.storage.load()
        restored_holiday = Holiday.from_dict(loaded_data)
        self.assertEqual(restored_holiday.name, "ДР")
        self.assertEqual(restored_holiday.state, "InProgress")
        self.assertEqual(len(restored_holiday.guests), 1)
        self.assertEqual(restored_holiday.guests[0].name, "Ника")


if __name__ == "__main__":
    unittest.main()