from src.FarmGame.scene.world_grid import Scene


class GameSession:

  def __init__(self) -> None:
    self.scene = Scene()

  def update(self):
    self.scene.update()
    self.scene.render()
    # self.renderer.render_scene(self.scene)
