from dataclasses import dataclass, field
from Commands.CommandInterface import *

@dataclass
class CommandController:

  def execute(self, command: Command) -> None:
    command.execute()
