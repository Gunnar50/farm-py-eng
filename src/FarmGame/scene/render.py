from src.FarmGame.scene.world_grid import Scene


class Render:

  def __init__(self) -> None:
    self.terrain_render = TerrainRender.create_default()
    self.entity_render = EntityRender.create_default()

  def render_scene(self, scene: Scene) -> None:
    self.terrain_render.render()
    self.entity_render.render()
