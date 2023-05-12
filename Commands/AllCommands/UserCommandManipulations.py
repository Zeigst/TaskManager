from dataclasses import dataclass
from Classes.TodoItem import TodoItem
from Classes.TodoList import TodoList
from Classes.UserCommand import UserCommand

@dataclass
class SetUserChoice:
  user_command: UserCommand
  user_choice: str

  def execute(self) -> None:
    self.user_command.setUserChoice(self.user_choice)

@dataclass
class ResetUserChoice:
  user_command: UserCommand

  def execute(self) -> None:
    self.user_command.resetUserChoice()

@dataclass
class RequestUserCommand:
  user_commands: UserCommand
  
  def execute(self) -> None:
    self.user_commands.user_input = self.user_commands.requestUserInputs()