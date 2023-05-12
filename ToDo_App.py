from Classes.TodoItem import *
from Classes.TodoList import *
from Commands.TodoListController import *
from Commands.Compile import *

# def on_ready():
#   pass

# def on_close():
#   pass

def main():
  Todo_List = TodoList()
  controller = TodoListController()
  User_Command = UserCommand()

  todo_item = Todo_List.createTodoItem("Task 1", "The first task")
  Todo_List.addTodoItemToList(todo_item)
  todo_item = Todo_List.createTodoItem("Task 2", "2rd job")
  Todo_List.addTodoItemToList(todo_item)
  todo_item = Todo_List.createTodoItem("Task 3", "Final work")
  Todo_List.addTodoItemToList(todo_item)

  print(todo_item.name)
  
  #=================
  # # VERSION 1: Command (Undo/Redo not implemented).
  controller.execute(Compile(User_Command, Todo_List, controller))
  #=================

  #=================
  # # VERSION 2: Command with Undo/Redo.

  #=================

if __name__ == "__main__":
  main()