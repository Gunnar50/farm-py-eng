from src.shared.hash_registry import Registrable


class Blueprint(Registrable):

  def __init__(self) -> None:
    Registrable.__init__(self)
