from pathlib import Path


class EngineFiles:
  # Get the root folder dynamically based on the location of this file
  # Go up 2 levels to 'src' folder
  # All other folder will be relative to 'src'
  ROOT_FOLDER = Path(__file__).resolve().parents[2]

  ASSETS_FOLDER = ROOT_FOLDER / "assets"
  ERROR_FOLDER = ROOT_FOLDER / "ErrorLogs"

  GUI_FOLDER = ASSETS_FOLDER / "GUI"
  SOUNDS_FOLDER = ASSETS_FOLDER / "sounds"
  FONT_FOLDER = ASSETS_FOLDER / "fonts"

  DEFAULT_FONT_ATLAS = FONT_FOLDER / "default.png"
  DEFAULT_FONT_META = FONT_FOLDER / "default.fnt"
