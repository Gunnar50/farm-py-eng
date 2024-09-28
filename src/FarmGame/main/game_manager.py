from src.FarmGame.main.configs.game_config import GameConfig
from src.FarmGame.repository.game_repository import GameRepository
from src.PyEng.main.engine import Engine


class GameManager:

  def __init__(self, game_configs: GameConfig) -> None:
    self.engine = Engine.create(game_configs)
    self.game_repository = GameRepository()

  def update(self):
    # If there is a session, render the scene
    self.engine.update()
