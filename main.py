from src.PyEng.main.engine import Engine

# class Game(PyEng.Game):
#   """Main Game Class"""

#   def __init__(self):
#     PyEng.Game.__init__(
#         self,
#         window_size=(960, 630),
#         caption="Farm Game",
#         bg_colour=(100, 100, 100),
#     )

#   def load_data(self):
#     pass

#   def game_loop(self):

#     # updates
#     dt = self.window.get_dt()
#     self.components_manager.update()

#     self.window.clear()
#     # this is where the game should render
#     # render.render
#     self.window.swap_buffers()


class EngineTester:

  def __init__(self) -> None:
    self.engine = Engine.create()

  def update(self) -> None:
    self.engine.update()

  def run(self) -> None:
    while True:
      self.update()


if __name__ == "__main__":
  # Game().run()
  EngineTester().run()
