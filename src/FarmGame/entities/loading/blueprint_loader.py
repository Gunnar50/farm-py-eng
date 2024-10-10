import pathlib
from src.shared import api
from src.FarmGame.entities.architecture.blueprint import Blueprint
from src.shared import io
from src.shared import exceptions
from src.shared.debug import LOGGER
from src.shared.hash_registry import HashRegistry, UniqueId


class BlueprintLoader:
  def __init__(self, file_prefix: str) -> None:
    self.file_prefix = file_prefix

  def load_folder(self, folder: pathlib.Path,
                  repository: HashRegistry[Blueprint]) -> None:
    for item in folder.iterdir():
      if self.is_folder(item):
        self.load_file(item, repository)
      else:
        self.load_folder(item, repository)

  def load_file(self, file: pathlib.Path,
                repository: HashRegistry[Blueprint]) -> None:
    try:
      blueprint = self.load_blueprint(file)
      repository.register(blueprint)
    except Exception as ex:
      LOGGER.error(f'Failed to load blueprint: {file}')
      # TODO: Push stack trace to a file
      LOGGER.error(f'Stack Trace: {str(ex)[:1000]}')

  def is_folder(self, folder: pathlib.Path) -> bool:
    # Check if any file in the folder ends with .json
    return any(file.is_file() and file.name.endswith(".json")
               for file in folder.iterdir())

  def load_blueprint(self, folder: pathlib.Path) -> Blueprint:
    info_json_file = self.get_info_file(folder)
    # Create pydantic model for the blueprint file info.
    # use that to load the reader and the blueprint settings
    data = io.get_data_model(api.EntityInfo, info_json_file)

    return Blueprint(data.name, data)

  def get_info_file(self, folder: pathlib.Path) -> pathlib.Path:
    for file in folder.iterdir():
      if file.name.startswith(self.file_prefix):
        return file
    raise exceptions.InfoFileNotFound(f'No info file found for {folder.name}')
