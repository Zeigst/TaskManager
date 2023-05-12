from typing import Protocol

class Command(Protocol):
  def execute() -> None:
    ...
  
  def undo() -> None:
    ...
  
  def redo() -> None:
    ...