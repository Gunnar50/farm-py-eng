from src.shared.api import InfoFile
from src.shared.hash_registry import Registrable, UniqueId


class Blueprint(Registrable):

  def __init__(self, name: str, data: InfoFile) -> None:
    Registrable.__init__(self)
    self.name = name
    self.data = data

  def get_name(self) -> str:
    return self.name
