from dataclasses import dataclass, field
from Commands.CommandInterface import *

@dataclass
class TodoListController:
  # undo_stack : list[Command] = field(default_factory=list)
  # redo_stack : list[Command] = field(default_factory=list)

  def execute(self, command: Command) -> None:
    command.execute()
    # self.redo_stack.clear()
    # self.undo_stack.append(command)

  # def undo(self) -> None:
  #   if not self.undo_stack():
  #     return
  #   else:
  #     command: Command = self.undo_stack.pop()
  #     command.undo()
  #     self.redo_stack.append(command)

  # def redo(self) -> None:
  #   if not self.undo_stack():
  #     return
  #   else:
  #     command: Command = self.redo_stack.pop()
  #     command.redo()
  #     self.undo_stack.append(command)


