from dataclasses import dataclass
from Classes.TodoList import TodoList
from Classes.UserCommand import UserCommand
from Commands.TodoListController import *

from Commands.AllCommands.MenuNavigations import *
from Commands.AllCommands.TodoItemManipulations import *
from Commands.AllCommands.Show import *
from Commands.AllCommands.UserCommandManipulations import *


# COMMAND MENU:
# 1. Create new task
# 2. Choose task
# 3. Undo
# 4. End program

@dataclass
class Compile:
  user_command: UserCommand
  todo_list: TodoList
  controller: TodoListController

  def execute(self) -> None:
    
    if self.user_command.menu_status == 1:
      self.controller.execute(ShowTodoList(self.todo_list))
      self.controller.execute(RequestUserCommand(self.user_command))
      if not self.user_command.user_input in ["1", "2", "3", "4"]:
        print("Invalid Input")
      else:
        match self.user_command.user_input:
          case "1":
            self.controller.execute(CreateTodoItem(self.todo_list))
            self.controller.execute(Compile(self.user_command, self.todo_list, self.controller))
          case "2":
            self.controller.execute(ToItemMenuMiddle(self.user_command))
            self.controller.execute(Compile(self.user_command, self.todo_list, self.controller))
          case "3":
            pass
          case "4":
            quit()
    
    elif self.user_command.menu_status == 2:
      self.controller.execute(ShowTodoList(self.todo_list))
      self.controller.execute(RequestUserCommand(self.user_command))
      self.controller.execute(SetUserChoice(self.user_command, self.user_command.user_input))
      if not self.user_command.user_input in self.todo_list.todo_list.keys():
        print("Invalid Input")
        self.controller.execute(ResetUserChoice(self.user_command))
        self.controller.execute(Compile(self.user_command, self.todo_list, self.controller))
      else:
        self.controller.execute(ToItemMenu(self.user_command))
        self.controller.execute(Compile(self.user_command, self.todo_list, self.controller))
    
    elif self.user_command.menu_status == 3:
      self.controller.execute(ShowTodoItem(self.todo_list.todo_list[self.user_command.user_choice]))
      self.controller.execute(RequestUserCommand(self.user_command))
      if not self.user_command.user_input in ["1", "2", "3", "4"]:
        print("Invalid Input")
        self.controller.execute(Compile(self.user_command, self.todo_list, self.controller))
      else:
        match self.user_command.user_input:
          case "1":
            self.controller.execute(Toggle(self.todo_list.todo_list[self.user_command.user_choice]))
          case "2":
            self.controller.execute(EditTodoItem(self.todo_list.todo_list[self.user_command.user_choice]))
          case "3":
            self.controller.execute(DeleteTodoItem(self.todo_list, self.todo_list.todo_list[self.user_command.user_choice]))
          case "4":
            self.controller.execute(ToMainMenu(self.user_command))
            self.controller.execute(Compile(self.user_command, self.todo_list, self.controller))
        self.controller.execute(ToMainMenu(self.user_command))
        self.controller.execute(Compile(self.user_command, self.todo_list, self.controller))