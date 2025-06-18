from typing import Any, Optional


class ApplicationException(Exception):
  """Base class for all application exceptions."""

  def __init__(self, message: str, context: Optional[dict[str, Any]] = None):
    super().__init__(message)
    self.context = context


class ComponentDuplicateError(ApplicationException):
  '''Component duplicate error exception'''


class ComponentNotFoundError(ApplicationException):
  '''Component does not exist or was not found exception'''


class InvalidParameters(ApplicationException):
  '''Raise when parameters are invilid'''


class FilePathNotFound(ApplicationException):
  '''Raise if a file path is not found'''


class IllegalStateException(ApplicationException):
  '''Raised when a component has an illegal state eg. not being initialised'''


class IllegalRegistryOverwrite(ApplicationException):
  '''Raised when a registry is being overwritten'''


class RegistryNotFoundException(ApplicationException):
  '''Raised when a registry is not found'''


class InfoFileNotFound(ApplicationException):
  '''Raised if a entity info file does not exist'''


class FailedToLoadBlueprint(ApplicationException):
  '''Raise if a blueprint fails to load'''


class FailedToGetDataModel(ApplicationException):
  '''Raise when data fails to load in specified model'''


class NotDataclass(ApplicationException):
  '''Raise when the specified class is not a dataclass'''
