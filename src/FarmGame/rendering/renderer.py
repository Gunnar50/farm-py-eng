from src.FarmGame.scene.world_grid import Scene
from src.PyEng.rendering.entity_render import EntityRender
from src.PyEng.rendering.tile_render import TileRender


class Renderer:

  def __init__(self) -> None:
    pass
    # self.tile_render = TileRender.create_default()
    # self.entity_render = EntityRender.create_default()

  def render_scene(self, scene: Scene) -> None:
    self.tile_renderer.render()
    self.entity_renderer.render()
