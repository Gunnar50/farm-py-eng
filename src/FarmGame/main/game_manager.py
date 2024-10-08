from src.FarmGame.main.configs.game_config import GameConfig
# from src.FarmGame.main.game import Game
from src.FarmGame.main.game_state import GameState
from src.FarmGame.repository.game_repository import GameRepository
# from src.FarmGame.scene.render import Render
from src.PyEng.main.engine import Engine


class GameManager:

  def __init__(self, game_configs: GameConfig) -> None:
    self.configs = game_configs
    self.engine = Engine.create(game_configs)

    # self.renderer = Render()
    # self.current_game = Game(self.renderer)
    self.game_repository = GameRepository()

    for i in self.game_repository.entity_system.blueprints:
      print(i.data)

  def update(self):
    # If there is a session, render the scene and the state is not main_menu
    # if self.engine.state_manager.is_not_state(GameState.MAIN_MENU,
    #                                           GameState.INITIAL):
    #   pass

    # self.current_game.update()
    # Update engine
    self.engine.update()
