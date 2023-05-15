from dataclasses import dataclass, field
from Commands.RUCommandInterface import *

@dataclass
class RUCommandController:
  undo_stack : list[RUCommand] = field(default_factory=list)
  redo_stack : list[RUCommand] = field(default_factory=list)

  def execute(self, command: RUCommand) -> None:
    command.execute()
    self.redo_stack.clear()
    self.undo_stack.append(command)

  def undo(self) -> None:
    if not self.undo_stack:
      return
    else:
      command: RUCommand = self.undo_stack.pop()
      command.undo()
      self.redo_stack.append(command)

  def redo(self) -> None:
    if not self.redo_stack:
      return
    else:
      command: RUCommand = self.redo_stack.pop()
      command.redo()
      self.undo_stack.append(command)