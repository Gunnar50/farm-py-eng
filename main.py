from src.FarmGame.main.configs.build_config import BuildConfig
from src.FarmGame.main.game_manager import GameManager
from src.PyEng.main.engine import Engine


class EngineTester:

  def __init__(self) -> None:
    self.engine = Engine.create()

  def update(self) -> None:
    self.engine.update()

  def run(self) -> None:
    while True:
      self.update()


class GameApp:

  def __init__(self) -> None:
    self.engine = Engine.create(BuildConfig)
    self.game_manager = GameManager(self.engine)

  def run(self) -> None:
    while True:
      self.game_manager.update()
      # Update engine
      self.engine.update()
    # self.game_manager.clean_up()


if __name__ == '__main__':
  # EngineTester().run()
  GameApp().run()
  # GameApp()
