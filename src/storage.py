# storage.py
import json
import os

class Storage:
    def __init__(self, file_path: str):
        self._file_path = file_path

    def save(self, holiday):
        with open(self._file_path, "w", encoding="utf-8") as file:
            json.dump(holiday.to_dict(), file, ensure_ascii=False, indent=4)

    def load(self):
        try:
            with open(self._file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError):
            return None