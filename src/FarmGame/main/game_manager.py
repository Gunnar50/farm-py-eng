from src.FarmGame.main.configs.game_config import GameConfig
# from src.FarmGame.main.game import Game
from src.FarmGame.main.game_state import GameState
from src.FarmGame.repository.game_database import BlueprintDatabase
# from src.FarmGame.scene.render import Render
from src.PyEng.main.engine import Engine


class GameManager:

  def __init__(self, game_configs: GameConfig) -> None:
    self.configs = game_configs
    self.engine = Engine.create(game_configs)

    self.blueprint_db = BlueprintDatabase()
    # init game controls
    # init sounds
    # init session manager
    # self.renderer = Render()
    # self.current_game = Game(self.renderer)

    for i in self.blueprint_db.entities:
      print(i.terrain_type)

  def update(self) -> None:
    # If there is a session (game is running),
    # and the state is not main_menu
    # render the scene
    if self.engine.state_manager.is_not_state(GameState.MAIN_MENU,
                                              GameState.INITIAL):
      # self.engine.render
      # in the renderer
      pass

    # self.current_game.update()
    # Update engine
    self.engine.update()
