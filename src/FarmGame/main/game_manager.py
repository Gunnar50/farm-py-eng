from src.FarmGame.main.configs.game_config import GameConfig
from src.FarmGame.main.game_state import GameState
from src.FarmGame.main.session import GameSession
from src.FarmGame.repository.game_database import BlueprintDatabase
from src.PyEng.components.components import SystemComponent
from src.PyEng.main.engine import Engine


class GameManager(SystemComponent):
  configs: GameConfig
  engine: Engine
  blueprint_db: BlueprintDatabase
  current_session: GameSession

  def __init__(self, engine: Engine, add=True):
    SystemComponent.__init__(self)
    self.engine = engine

    # Load blueprint for assets
    self.blueprint_db = BlueprintDatabase()
    # init game controls
    # init sounds
    # init session manager
    self.current_session = GameSession()

    # for i in cls.blueprint_db.tiles:
    #   print(i.tile_type)

  def get_blueprint_database(self) -> BlueprintDatabase:
    return self.blueprint_db

  def update(self) -> None:
    # If there is a session (game is running),
    # and the state is not main_menu
    # render the scene
    if self.engine.state_manager.is_not_state(GameState.MAIN_MENU,
                                              GameState.INITIAL):
      # self.engine.render
      # in the renderer
      pass

    self.current_session.update()
