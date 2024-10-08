from src.FarmGame.entities.entity_system import EntitySystem
from src.FarmGame.repository.game_files import GameFiles


class GameRepository:

  def __init__(self) -> None:
    self.entity_system = EntitySystem()
    self.load_resources()

  def load_resources(self) -> None:
    # Load all registries
    self.load_blueprints()

  def load_blueprints(self):
    self.entity_system.load_entities(GameFiles.get_entities_folder())
