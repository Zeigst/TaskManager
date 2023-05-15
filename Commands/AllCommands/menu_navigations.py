from dataclasses import dataclass
from Classes.user_command import UserCommand

@dataclass
class ToMainMenu:
  user_command: UserCommand

  def execute(self) -> None:
    self.user_command.set_menu_status(1)

@dataclass
class ToItemSelectMenu:
  user_command: UserCommand

  def execute(self) -> None:
    self.user_command.set_menu_status(2)

@dataclass
class ToItemMenu:
  user_command: UserCommand

  def execute(self) -> None:
    self.user_command.set_menu_status(3)