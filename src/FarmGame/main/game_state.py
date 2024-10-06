import abc
import enum

from src.PyEng.components.state_manager import State


class EnumABCMeta(enum.EnumMeta, abc.ABCMeta):
  '''Combine EnumMeta and ABCMeta into a new metaclass
  so GameState can inhert from Enum and State'''
  pass


class GameState(State, enum.Enum, metaclass=EnumABCMeta):
  NORMAL = 'normal'
  UI = 'ui'
  CAMERA = 'camera'
  UI_FOCUS = 'ui_focus'
  MAIN_MENU = 'main_menu'
  INITIAL = 'initial'
