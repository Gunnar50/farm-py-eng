import json
import os

import pygame

from PyEng.shared.debug import LOGGER
from PyEng.utils import io

from PyEng.element_manager.components import SystemComponent


class Assets(SystemComponent):
  """Load all the game assests locate in the specified directory."""

  def __init__(self, assets_folder: str):
    SystemComponent.__init__(self)
    self.assets: dict = {}
    self.load_assets(assets_folder)

  def load_assets(self, assets_folder: str):
    for file_name in os.listdir(assets_folder):
      if file_name.endswith(".json"):
        file_path = os.path.join(assets_folder, file_name)
        for instance in io.load_json_data(file_path):
          self.assets[instance.label] = instance

  def get_assets(self):
    return f"{self.assets}"

  def print_assets(self):
    for label, asset in self.assets.items():
      LOGGER.info(f'{label}: {asset}')
