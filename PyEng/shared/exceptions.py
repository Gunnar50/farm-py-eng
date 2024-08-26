class ComponentDuplicateError(Exception):
  """Component duplicate error exception"""

  # def __init__(self, component):
  #     super().__init__(f'Component "{component}" cannot be added again.')


class ComponentNotFoundError(Exception):
  """Component does not exist or was not found exception"""


class InvalidParameters(Exception):
  """Raise when parameters are invilid"""


class FilePathNotFound(Exception):
  """Raise if a file path is not found"""
