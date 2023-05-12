from dataclasses import dataclass
from Classes.UserCommand import UserCommand

@dataclass
class ToMainMenu:
  user_command: UserCommand

  def execute(self) -> None:
    self.user_command.setMenuStatus(1)

@dataclass
class ToItemMenuMiddle:
  user_command: UserCommand

  def execute(self) -> None:
    self.user_command.setMenuStatus(2)

@dataclass
class ToItemMenu:
  user_command: UserCommand

  def execute(self) -> None:
    self.user_command.setMenuStatus(3)