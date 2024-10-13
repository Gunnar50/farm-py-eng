from unittest import mock

import pytest

from src.PyEng.main.engine import Engine
from src.PyEng.main.engine_config import EngineConfigs
from src.shared import exceptions


@pytest.fixture(autouse=True)
def mock_window():
  with mock.patch('src.PyEng.main.engine.Window', autospec=True) as mock_window:
    yield mock_window


@pytest.fixture(autouse=True)
def reset_engine_singleton():
  Engine._Engine__instance = None


class TestEngine:
  configs = EngineConfigs.get_default_configs()

  def test_singleton_behavior(self):
    engine = Engine.create()
    assert isinstance(engine, Engine)

    with pytest.raises(exceptions.IllegalStateException):
      Engine.create()

  def test_get_engine_instance(self):
    engine = Engine.create()
    engine_instance = Engine.get_instance()
    assert engine == engine_instance

  def test_get_instance_no_engine_created(self):
    engine_instance = Engine.get_instance()
    assert isinstance(engine_instance, Engine)

  @mock.patch('os.path.exists')
  def test_missing_assets_folder(self, mock_exists: mock.Mock):
    # Patch os.path.exists to return False
    mock_exists.return_value = False
    with pytest.raises(exceptions.IllegalStateException):
      Engine.create()
