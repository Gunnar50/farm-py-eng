import pathlib

from src.FarmGame.entities.architecture.blueprint import Blueprint
from src.FarmGame.entities.repository.blueprint_repository_loader import BlueprintRepositoryLoader
from src.shared.hash_registry import HashRegistry


class EntityBlueprint:

  def __init__(self) -> None:
    # HashRegistry it implements a iterable containing instances of Blueprint
    self.blueprints: HashRegistry[Blueprint] = HashRegistry()

    self.loader = BlueprintRepositoryLoader(self.blueprints)
    # self.model_atlas = EntityModelAltlas()

  def load_entities(self, entity_path: pathlib.Path) -> None:
    self.loader.load_entity_folder(entity_path)
