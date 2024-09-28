class Version:

  def __init__(self, major: int, minor: int, update: int) -> None:
    self.major = major
    self.minor = minor
    self.update = update

  def __str__(self) -> str:
    return f'{self.major}.{self.minor}.{self.update}'
