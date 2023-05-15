from Classes.todo_item import *
from Classes.todo_list import *
from Commands.command_controller import *
from Commands.ru_command_controller import *
from Commands.compile import *

def main():
  todo_list = TodoList()
  controller = CommandController()
  ru_controller = RUCommandController()
  User_Command = UserCommand()

  controller.execute(LoadData(todo_list))
  controller.execute(Compile(User_Command, todo_list, controller, ru_controller))

if __name__ == "__main__":
  main()