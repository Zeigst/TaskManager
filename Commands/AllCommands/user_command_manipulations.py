from dataclasses import dataclass
from Classes.user_command import UserCommand

@dataclass
class SetUserChoice:
  user_command: UserCommand
  user_choice: str

  def execute(self) -> None:
    self.user_command.set_user_choice(self.user_choice)

@dataclass
class ResetUserChoice:
  user_command: UserCommand

  def execute(self) -> None:
    self.user_command.reset_user_choice()

@dataclass
class RequestUserCommand:
  user_command: UserCommand
  
  def execute(self) -> None:
    self.user_command.user_input = self.user_command.request_user_input()