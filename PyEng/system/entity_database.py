import json
import os

import pygame

from PyEng.shared.types import StrPath
from PyEng.utils import io

from PyEng.element_manager.components import SystemComponent


class EntityDatabase(SystemComponent):
  """Load all the game assests locate in the specified directory."""

  def __init__(self, path: StrPath):
    SystemComponent.__init__(self)
    self.database: dict = {}
    if path:
      self.load(path)

  def load(self, path: StrPath):
    for file_name in os.listdir(path):
      if file_name.endswith(".json"):
        file_path = os.path.join(path, file_name)
        for instance in io.load_json_data(file_path):
          self.database[instance.label] = instance

  def get_assets(self):
    return f"{self.database}"

  def print_assets(self):
    for label, asset in self.database.items():
      print(f'{label}: {asset}')
