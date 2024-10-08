import pathlib

from src.FarmGame.entities.architecture.blueprint import Blueprint
from src.FarmGame.entities.loading.blueprint_loader import BlueprintLoader
from src.shared.debug import LOGGER
from src.shared.hash_registry import HashRegistry


class BlueprintRepositoryLoader:

  def __init__(self, repository: HashRegistry[Blueprint]) -> None:
    self.repository = repository
    # self.component_types: HashRegistry[ComponentType] = HashRegistry()
    self.loader = BlueprintLoader()

  # def register_component_type(self, type: ComponentType):
  #   self.component_types.register(type)

  def load_entity_folder(self, entity_folder: pathlib.Path) -> None:
    for item in entity_folder.iterdir():
      if self.is_entity_folder(item):
        self.load_entity_file(item)
      else:
        self.load_entity_folder(item)

  def load_entity_file(self, file: pathlib.Path) -> None:
    try:
      blueprint = self.loader.load_blueprint(file)
      self.repository.register(blueprint)
    except Exception as ex:
      LOGGER.error(f'Failed to load blueprint: {file}')
      # TODO: Push stack trace to a file
      LOGGER.error(f'Stack Trace: {str(ex)[:1000]}')

  def is_entity_folder(self, entity_folder: pathlib.Path) -> bool:
    # Check if any file in the folder ends with .json
    return any(file.is_file() and file.name.endswith(".json")
               for file in entity_folder.iterdir())
