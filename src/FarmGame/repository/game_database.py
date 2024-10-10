import pathlib
from site import ENABLE_USER_SITE
from src.FarmGame.entities.architecture.blueprint import Blueprint
from src.FarmGame.entities.loading.blueprint_loader import BlueprintLoader
from src.FarmGame.repository.game_files import GameFiles
from src.shared import exceptions, io
from src.shared import api
from src.shared.debug import LOGGER
from src.shared.hash_registry import HashRegistry


# Game Repository
class BlueprintDatabase:
  ENTITY_FILE_PREFIX = 'entity_info'
  ITEM_FILE_PREFIX = 'item_info'

  def __init__(self) -> None:
    # self.entities = EntityBlueprint()
    # HashRegistry it implements a iterable containing instances of Blueprint
    self.entities: HashRegistry[Blueprint] = HashRegistry()
    self.entity_loader = BlueprintLoader(self.entities, self.ENTITY_FILE_PREFIX)
    self.items = ItemBlueprint()
    self.load_resources()

  def load_resources(self) -> None:
    # Load all registries
    # load tiles blueprints
    # load items blueprints

    # Load entities blueprints
    self.entity_loader.load_folder(GameFiles.get_entities_folder())
