import abc

from src.PyEng.components.components import SystemComponent


class State(abc.ABC):
  pass


class QueuedState:

  def __init__(self, state: State, wait_for_request: bool) -> None:
    self.state = state
    self.wait_for_req = wait_for_request


class StateManager(SystemComponent):
  """Handles all states of the game"""

  def __init__(self, default_state: State, initial_state: State) -> None:
    SystemComponent.__init__(self)
    self.default_state = default_state
    self.current_state = initial_state
    self.state_queue: list[QueuedState] = []

  def get_state(self) -> State:
    return self.current_state

  def is_state(self, *states: State) -> bool:
    return any(self.current_state == state for state in states)

  def is_not_state(self, *states: State) -> bool:
    return any(self.current_state != state for state in states)

  def get_next_state(self) -> State:
    if not self.state_queue:
      return self.default_state
    else:
      return self.state_queue[0].state

  def clean_queue(self):
    self.state_queue = [
        state for state in self.state_queue if state.wait_for_req
    ]

  def switch_state(self, new_state: State):
    # registered_users.end_state(self.current_state)
    self.current_state = new_state
    # self.current_state.init()

  def update(self):
    next_state = self.get_next_state()
    self.clean_queue()
    if self.current_state != next_state:
      self.switch_state(next_state)
