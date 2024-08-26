import json
import os

from PyEng.shared.types import StrPath


def load_json(file_path: StrPath):
  if os.path.exists(file_path):
    with open(file_path, 'r') as file:
      return json.load(file)
  else:
    return {}
