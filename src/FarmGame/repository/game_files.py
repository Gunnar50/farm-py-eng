import pathlib

from src.PyEng.main.engine_files import EngineFiles


class GameFiles:
  ITEMS_FOLDER = 'items'
  ENTITIES_FOLDER = 'entities'
  TILES_FOLDER = 'tiles'

  @staticmethod
  def get_items_folder() -> pathlib.Path:
    return EngineFiles.DATA_FOLDER / GameFiles.ITEMS_FOLDER

  @staticmethod
  def get_entities_folder() -> pathlib.Path:
    return EngineFiles.DATA_FOLDER / GameFiles.ENTITIES_FOLDER

  @staticmethod
  def get_tiles_folder() -> pathlib.Path:
    return EngineFiles.DATA_FOLDER / GameFiles.TILES_FOLDER
