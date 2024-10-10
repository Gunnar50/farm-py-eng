class ComponentDuplicateError(Exception):
  '''Component duplicate error exception'''


class ComponentNotFoundError(Exception):
  '''Component does not exist or was not found exception'''


class InvalidParameters(Exception):
  '''Raise when parameters are invilid'''


class FilePathNotFound(Exception):
  '''Raise if a file path is not found'''


class IllegalStateException(Exception):
  '''Raised when a component has an illegal state eg. not being initialised'''


class IllegalRegistryOverwrite(Exception):
  '''Raised when a registry is being overwritten'''


class RegistryNotFoundException(Exception):
  '''Raised when a registry is not found'''


class InfoFileNotFound(Exception):
  '''Raised if a entity info file does not exist'''
