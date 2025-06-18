class Version:

  def __init__(self, major: int, minor: int, patch: int) -> None:
    self.major = major
    self.minor = minor
    self.patch = patch

  def __str__(self) -> str:
    return f'{self.major}.{self.minor}.{self.patch}'
