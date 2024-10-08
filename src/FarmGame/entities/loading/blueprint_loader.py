import pathlib
from src.shared import api
from src.FarmGame.entities.architecture.blueprint import Blueprint
from src.shared import io
from src.shared import exceptions
from src.shared.hash_registry import HashRegistry, UniqueId


class BlueprintLoader:
  ENTITY_INFO_FILE = 'entity_info'

  def __init__(self) -> None:
    pass

  def load_blueprint(self, folder: pathlib.Path) -> Blueprint:
    info_json_file = self.get_info_file(folder)
    # Create pydantic model for the blueprint file info.
    # use that to load the reader and the blueprint settings
    data = io.get_data_model(api.EntityInfo, info_json_file)

    return Blueprint(data.name, data)

  def get_info_file(self, folder: pathlib.Path) -> pathlib.Path:
    for file in folder.iterdir():
      if file.name.startswith(self.ENTITY_INFO_FILE):
        return file
    raise exceptions.EntityInfoFileNotFound(
        f'No entity info file found for {folder.name}')
