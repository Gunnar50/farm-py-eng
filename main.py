import PyEng


class Game(PyEng.Game):
  """Main Game Class"""

  def load_data(self):
    PyEng.init(
        window_size=(960, 630),
        caption="My Specific Game",
        bg_colour=(100, 0, 0),
        assets_folder="assets/data",
    )
    # print(f'{self.components_manager.components()=}')
    for component in self.components_manager.components():
      setattr(self, component.name, component)
      self.__dict__[component.name] = component

    # print(self.assets)

  def game_loop(self):

    # updates
    dt = self.window.get_dt()
    self.components_manager.update()

    self.window.clear()
    # this is where the game should render
    # render.render
    self.window.swap_buffers()


if __name__ == "__main__":
  Game().run()
