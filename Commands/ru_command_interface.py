from typing import Protocol

class RUCommand(Protocol):
  def execute() -> None:
    ...

  def redo() -> None:
    ...

  def undo() -> None:
    ...