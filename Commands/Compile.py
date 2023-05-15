from dataclasses import dataclass
import os

from Classes.TodoList import TodoList
from Classes.UserCommand import UserCommand
from Commands.CommandController import *
from Commands.RUCommandController import *

from Commands.AllCommands.MenuNavigations import *
from Commands.AllCommands.TodoItemManipulations import *
from Commands.AllCommands.Show import *
from Commands.AllCommands.UserCommandManipulations import *
from Commands.AllCommands.Database import *

@dataclass
class Compile:
  user_command: UserCommand
  todo_list: TodoList
  controller: CommandController
  ru_controller: RUCommandController

  def execute(self) -> None:
    os.system('cls')
    if self.user_command.menu_status == 1:
      self.controller.execute(ShowTodoList(self.todo_list))
      self.controller.execute(RequestUserCommand(self.user_command))
      if not self.user_command.user_input in ["1", "2", "3", "4", "5"]:
        print("Invalid Input")
        self.controller.execute(Compile(self.user_command, self.todo_list, self.controller, self.ru_controller))
      else:
        match self.user_command.user_input:
          case "1":
            self.ru_controller.execute(CreateTodoItem(self.todo_list))
            self.controller.execute(Compile(self.user_command, self.todo_list, self.controller, self.ru_controller))
          case "2":
            self.controller.execute(ToItemMenuMiddle(self.user_command))
            self.controller.execute(Compile(self.user_command, self.todo_list, self.controller, self.ru_controller))
          case "3":
            self.ru_controller.undo()
            self.controller.execute(Compile(self.user_command, self.todo_list, self.controller, self.ru_controller))
          case "4":
            self.ru_controller.redo()
            self.controller.execute(Compile(self.user_command, self.todo_list, self.controller, self.ru_controller))
          case "5":
            self.controller.execute(SaveData(self.todo_list))
            quit()
    
    elif self.user_command.menu_status == 2:
      self.controller.execute(ShowTodoList(self.todo_list))
      self.controller.execute(RequestUserCommand(self.user_command))
      self.controller.execute(SetUserChoice(self.user_command, self.user_command.user_input))
      if not self.user_command.user_input in self.todo_list.todo_list.keys():
        print("Invalid Input")
        self.controller.execute(ResetUserChoice(self.user_command))
        self.controller.execute(Compile(self.user_command, self.todo_list, self.controller, self.ru_controller))
      else:
        self.controller.execute(ToItemMenu(self.user_command))
        self.controller.execute(Compile(self.user_command, self.todo_list, self.controller, self.ru_controller))
    
    elif self.user_command.menu_status == 3:
      self.controller.execute(ShowTodoItem(self.todo_list.todo_list[self.user_command.user_choice]))
      self.controller.execute(RequestUserCommand(self.user_command))
      if not self.user_command.user_input in ["1", "2", "3", "4"]:
        print("Invalid Input")
        self.controller.execute(Compile(self.user_command, self.todo_list, self.controller, self.ru_controller))
      else:
        match self.user_command.user_input:
          case "1":
            self.ru_controller.execute(Toggle(self.todo_list.todo_list[self.user_command.user_choice]))
          case "2":
            self.ru_controller.execute(EditTodoItem(self.todo_list.todo_list[self.user_command.user_choice]))
          case "3":
            self.ru_controller.execute(DeleteTodoItem(self.todo_list, self.todo_list.todo_list[self.user_command.user_choice]))
          case "4":
            pass
        self.controller.execute(ToMainMenu(self.user_command))
        self.controller.execute(Compile(self.user_command, self.todo_list, self.controller, self.ru_controller))