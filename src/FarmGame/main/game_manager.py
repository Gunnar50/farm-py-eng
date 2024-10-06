from src.FarmGame.main.configs.game_config import GameConfig
from src.FarmGame.main.game_state import GameState
from src.FarmGame.repository.game_repository import GameRepository
from src.PyEng.main.engine import Engine


class GameManager:

  def __init__(self, game_configs: GameConfig) -> None:
    self.engine = Engine.create(game_configs)
    self.game_repository = GameRepository()

  def update(self):
    # If there is a session, render the scene and the state is not main_menu
    if self.engine.state_manager.is_not_state(GameState.MAIN_MENU,
                                              GameState.INITIAL):
      pass

    # Update engine
    self.engine.update()
