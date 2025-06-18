import datetime
import logging
import pathlib
import platform
import random
import re
import socket
import sys
import traceback
from types import TracebackType
from typing import Optional, Type

from src.PyEng.components.components import SystemComponent
from src.PyEng.main.engine_files import EngineFiles
from src.shared import exceptions


class ErrorManager(SystemComponent):
  _log_directory: pathlib.Path
  _logged_exceptions: set[int]

  def __init__(
      self,
      log_dir: pathlib.Path = EngineFiles.ROOT_FOLDER / 'DefaultErrorLogs',
  ):
    """
    Initialize the error manager with a directory for log files.
    Log files will be named dynamically based on date and error type.
    """
    SystemComponent.__init__(self)

    ErrorManager._log_directory = log_dir
    ErrorManager._logged_exceptions = set()

    # Ensure log directory exists
    ErrorManager._log_directory.mkdir(parents=True, exist_ok=True)

    # Set up global exception handler
    sys.excepthook = ErrorManager.handle_exception

  @staticmethod
  def _create_logger(error_name: str) -> tuple[logging.Logger, pathlib.Path]:
    """Create a logger for a specific error type."""

    # Get current date in dd-mm-yyyy format
    current_date = datetime.datetime.now().strftime('%d-%m-%Y_%H%M%S')

    # Sanitize error name for filename (remove invalid characters)
    safe_error_name = re.sub(r'[^a-zA-Z0-9]', '', error_name)

    # Create log filename with date, error name and a random number at the end
    log_filename = f'{current_date}_{safe_error_name}_{random.randint(1000, 9999)}.log'
    log_path = ErrorManager._log_directory / log_filename

    # Create a new logger
    logger = logging.getLogger(f'error.{error_name}.{current_date}')
    logger.setLevel(logging.ERROR)

    # Remove any existing handlers to avoid duplicate logging
    for handler in logger.handlers[:]:
      logger.removeHandler(handler)

    # Create file handler
    file_handler = logging.FileHandler(str(log_path))
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(file_handler)

    # Don't propagate to root logger
    logger.propagate = False

    return logger, log_path

  @staticmethod
  def handle_exception(
      exc_type: Type[BaseException],
      exc_value: BaseException,
      exc_traceback: Optional[TracebackType],
  ) -> None:
    """
    Handle uncaught exceptions and log them to appropriate files.
    
    Args:
        exc_type: The exception class
        exc_value: The exception instance
        exc_traceback: The traceback object
    """
    # Don't log keyboard interrupts
    if issubclass(exc_type, KeyboardInterrupt):
      sys.__excepthook__(exc_type, exc_value, exc_traceback)
      return

    # Get error name for the log file
    error_name = exc_type.__name__

    # Get the appropriate logger
    logger, log_path = ErrorManager._create_logger(error_name)

    if issubclass(exc_type, exceptions.ApplicationException):
      error_header = f'APPLICATION EXCEPTION: {error_name}\n'
    else:
      error_header = f'UNCAUGHT EXCEPTION: {error_name}\n'

    error_msg = ErrorManager.format_message(
        error_header,
        exc_value,
    )

    # Log the exception
    logger.error(error_msg)

    # Show the normal Python error in the console
    sys.__excepthook__(exc_type, exc_value, exc_traceback)
    print('=' * 80)
    print(f'Critical error occurred. Details logged to {log_path}',
          file=sys.stderr)

  @staticmethod
  def _get_system_info() -> dict:
    return {
        'Timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'Platform': platform.platform(),
        'Python Version': sys.version.split()[0],
        'Hostname': socket.gethostname(),
    }

  @staticmethod
  def log_error(
      exception: Exception,
      error_name: Optional[str] = None,
      context: Optional[dict] = None,
  ) -> None:
    """
    Manually log an error with custom message and optional exception.

    Args:
      exception: The exception object
      error_name: Custom name for the error log file (defaults to exception type)
      context: Dictionary of contextual information to include in the log
    """

    # Determine error name for the log file
    if error_name is None:
      error_name = type(exception).__name__

    # Get the appropriate logger
    logger, _ = ErrorManager._create_logger(error_name)

    error_msg = ErrorManager.format_message(
        f'MANUAL CAUGHT EXCEPTION: {error_name}\n',
        exception,
    )

    # Log the error
    logger.error(error_msg)

    if exception:
      ErrorManager._logged_exceptions.add(id(exception))
      raise exception

  @staticmethod
  def format_message(
      error_msg: str,
      exception: BaseException,
  ) -> str:
    message = str(exception)
    if not message:
      message = exception.__class__.__name__

    # Collect system information
    system_info = ErrorManager._get_system_info()

    # Format the error message
    error_msg += '=' * 80 + '\n'
    error_msg += 'SYSTEM INFORMATION:\n'
    error_msg += '\n'.join(f'{k}: {v}' for k, v in system_info.items())
    error_msg += '\n' + '=' * 80 + '\n'
    error_msg += f'ERROR MESSAGE: {message}\n'

    if hasattr(exception, 'context'):
      context: dict = getattr(exception, 'context')
      if context is not None:
        error_msg += 'CONTEXT:\n'
        error_msg += '\n'.join(f'{k}: {v}' for k, v in context.items())
        error_msg += '\n'

    error_msg += '=' * 80 + '\n'

    if exception.__traceback__:
      traceback_lines = traceback.format_exception(type(exception), exception,
                                                   exception.__traceback__)
      traceback_text = ''.join(traceback_lines)
      error_msg += 'TRACEBACK:\n'
      error_msg += traceback_text

    else:
      # Get the current stack trace (excluding this function call)
      error_msg += 'STACK TRACE:\n'
      error_msg += ''.join(traceback.format_stack()[:-2])

    error_msg += '=' * 80 + '\n'
    return error_msg
