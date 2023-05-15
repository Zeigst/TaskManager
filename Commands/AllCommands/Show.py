from dataclasses import dataclass
from Classes.todo_list import *
from Classes.todo_item import *

@dataclass
class ShowTodoList:
  todo_list: TodoList

  def execute(self):
    print("\nWelcome to TaskListManager\n----------")
    print("\nCURRENT TASKS: ")
    for key in self.todo_list.get_data().keys():
      print(self.todo_list.get_data()[key])

@dataclass
class ShowTodoItem:
  todo_item: TodoItem

  def execute(self):
    print("\nWelcome to TaskListManager\n----------")
    print("\nTask Selected:\n", self.todo_item)