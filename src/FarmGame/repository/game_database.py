from src.FarmGame.entities.entity_system import EntityBlueprint
from src.FarmGame.repository.game_files import GameFiles


# Game Repository
class BlueprintDatabase:

  def __init__(self) -> None:
    self.entities = EntityBlueprint()
    self.items = ItemBlueprint()
    self.load_resources()

  def load_resources(self) -> None:
    # Load all registries
    # load tiles blueprints
    # load items blueprints

    # Load entities blueprints
    self.entities.load_entities(GameFiles.get_entities_folder())
