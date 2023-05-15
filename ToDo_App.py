from Classes.TodoItem import *
from Classes.TodoList import *
from Commands.CommandController import *
from Commands.RUCommandController import *
from Commands.Compile import *

def main():
  todo_list = TodoList()
  controller = CommandController()
  ru_controller = RUCommandController()
  User_Command = UserCommand()

  controller.execute(LoadData(todo_list))
  controller.execute(Compile(User_Command, todo_list, controller, ru_controller))

if __name__ == "__main__":
  main()