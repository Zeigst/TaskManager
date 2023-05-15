from dataclasses import dataclass
from Classes.TodoList import *
from Classes.TodoItem import *

@dataclass
class CreateTodoItem:
  todo_list: TodoList
  new_item = None

  def execute(self) -> None:
    new_task_name = input("\nEnter task name: ")
    new_task_description = input("Enter task description: ")
    
    if new_task_name in self.todo_list.todo_list.keys():
      print("\nERROR: Task name must be unique!")
    else:  
      self.new_item = self.todo_list.createTodoItem(new_task_name, new_task_description)
      self.todo_list.addTodoItemToList(self.new_item)

  def undo(self) -> None:
    self.todo_list.removeTodoItem(self.new_item)

  def redo(self) -> None:
    self.todo_list.addTodoItemToList(self.new_item)

@dataclass
class DeleteTodoItem:
  todo_list: TodoList
  todo_item: TodoItem

  def execute(self) -> None:
    self.todo_list.removeTodoItem(self.todo_item)

  def undo(self) -> None:
    self.todo_list.addTodoItemToList(self.todo_item)

  def redo(self) -> None:
    self.todo_list.removeTodoItem(self.todo_item)


@dataclass
class Toggle:
  todo_item: TodoItem

  def execute(self) -> None:
    self.todo_item.toggleStatus()
  
  def undo(self) -> None:
    self.todo_item.toggleStatus()

  def redo(self) -> None:
    self.todo_item.toggleStatus()

@dataclass
class EditTodoItem:
  todo_item: TodoItem
  old_name: str = ""
  old_description: str = ""
  new_name: str = ""
  new_description: str = ""

  def execute(self) -> None:
    print("\nEDIT TASK:")
    self.new_name = input("\nEnter new task's name: ")
    self.new_description = input("Enter new task's description: ")
    self.old_name = self.todo_item.getName()
    self.old_description = self.todo_item.getDescription()
    self.todo_item.setName(self.new_name)
    self.todo_item.setDescription(self.new_description)

  def undo(self) -> None:
    self.todo_item.setName(self.old_name)
    self.todo_item.setDescription(self.old_description)

  def redo(self) -> None:
    self.todo_item.setName(self.new_name)
    self.todo_item.setDescription(self.new_description)
