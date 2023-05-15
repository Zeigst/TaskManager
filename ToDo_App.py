from Classes.TodoItem import *
from Classes.TodoList import *
from Commands.CommandController import *
from Commands.RUCommandController import *
from Commands.Compile import *

def main():
  Todo_List = TodoList()
  controller = CommandController()
  ru_controller = RUCommandController()
  User_Command = UserCommand()

  todo_item = Todo_List.createTodoItem("Task 1", "The first task")
  Todo_List.addTodoItemToList(todo_item)
  todo_item = Todo_List.createTodoItem("Task 2", "2nd job")
  Todo_List.addTodoItemToList(todo_item)
  todo_item = Todo_List.createTodoItem("Task 3", "Final work")
  Todo_List.addTodoItemToList(todo_item)
  
  # # VERSION 2: Command (Undo/Redo implemented).
  controller.execute(Compile(User_Command, Todo_List, controller, ru_controller))

if __name__ == "__main__":
  main()