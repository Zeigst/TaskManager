from dataclasses import dataclass
from Classes.TodoList import *
from Classes.TodoItem import *
import os

@dataclass
class ShowTodoList:
  todo_list: TodoList

  def execute(self):
    os.system('cls')
    print("\nWelcome to TaskListManager\n----------")
    print("\nCURRENT TASKS: ")
    for key in self.todo_list.todo_list.keys():
      print(self.todo_list.todo_list[key])

@dataclass
class ShowTodoItem:
  todo_item: TodoItem

  def execute(self):
    os.system('cls')
    print("\nWelcome to TaskListManager\n----------")
    print("\nTask Selected:\n",self.todo_item)