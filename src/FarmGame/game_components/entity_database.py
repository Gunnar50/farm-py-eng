import os
from typing import Optional

from PyEng.element_manager.components import SystemComponent
from PyEng.shared import db_models
from PyEng.shared.debug import LOGGER
from shared import io


class Database(SystemComponent):
  """Load all the game assests locate in the specified directory."""

  def __init__(self, path: str):
    SystemComponent.__init__(self)
    self._database: dict[str, db_models.BaseModel] = {}
    self.load(path)

  def load(self, path: str):
    for file_name in os.listdir(path):
      if file_name.endswith(".json"):
        file_path = os.path.join(path, file_name)
        for model in io.load_json_data(file_path):
          self._database[model.label] = model

  @property
  def database(self):
    return self._database

  def get_model(self, label: str) -> Optional[db_models.BaseModel]:
    return self._database.get(label, None)

  def get_assets(self):
    return f"{self._database}"

  def print_assets(self):
    for label, model in self._database.items():
      LOGGER.info(f'{label}: {model}')
