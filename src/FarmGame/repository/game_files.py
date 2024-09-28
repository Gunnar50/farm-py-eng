import pathlib
from src.PyEng.main.engine_files import EngineFiles


class GameFiles:
  ASSETS_FOLDER = EngineFiles.ASSETS_FOLDER
  ITEMS_FOLDER = 'items'
  ENTITIES_FOLDER = 'entities'

  @staticmethod
  def get_items_folder() -> pathlib.Path:
    return EngineFiles.ROOT_FOLDER / GameFiles.ITEMS_FOLDER

  @staticmethod
  def get_entities_folder() -> pathlib.Path:
    return EngineFiles.ROOT_FOLDER / GameFiles.ENTITIES_FOLDER
