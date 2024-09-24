class EngineConfigs:
  window_width = 1280
  window_height = 720
  ui_size = 1.0
  fullscreen = 0
  caption = "The Game"
  fps = 100
  vsync = False
  background_colour = (100, 100, 100)

  # ui_resources = UiResources()
  # ui_configs = ui_configs.UiConfigs()
  # resources = Resources()

  # # Using an empty state by default
  # initial_state = EmptyState()
  # default_state = EmptyState()

  debugger = None

  @staticmethod
  def get_default_configs():
    return EngineConfigs