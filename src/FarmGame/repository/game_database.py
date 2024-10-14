from src.FarmGame.repository.blueprint_loader import (EntityLoader, ItemLoader,
                                                      TilesLoader)


# Game Repository
class BlueprintDatabase:

  def __init__(self) -> None:
    # self.entities = EntityBlueprint()
    # HashRegistry it implements a iterable containing instances of Blueprint
    self.entities = EntityLoader.load()
    self.tiles = TilesLoader.load()
    self.items = ItemLoader.load()
