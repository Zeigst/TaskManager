from dataclasses import dataclass
from Classes.todo_list import *
from Classes.todo_item import *

@dataclass
class CreateTodoItem:
  todo_list: TodoList
  new_item: TodoItem = None
  success: bool = False

  def execute(self) -> None:
    new_task_name = input("\nEnter task name: ")
    new_task_description = input("Enter task description: ")
    
    if new_task_name in self.todo_list.get_data().keys():
      print("\nERROR: Task name must be unique!")
      input("Press Enter to continue...")
    else:  
      self.new_item = self.todo_list.create_item(new_task_name, new_task_description)
      self.todo_list.add_item(self.new_item)
      self.success = True

  def undo(self) -> None:
    if self.success:
      self.todo_list.remove_item(self.new_item)

  def redo(self) -> None:
    if self.success:
      self.todo_list.add_item(self.new_item)

@dataclass
class DeleteTodoItem:
  todo_list: TodoList
  todo_item: TodoItem

  def execute(self) -> None:
    self.todo_list.remove_item(self.todo_item)

  def undo(self) -> None:
    self.todo_list.add_item(self.todo_item)

  def redo(self) -> None:
    self.todo_list.remove_item(self.todo_item)


@dataclass
class Toggle:
  todo_item: TodoItem

  def execute(self) -> None:
    self.todo_item.toggle_status()
  
  def undo(self) -> None:
    self.todo_item.toggle_status()

  def redo(self) -> None:
    self.todo_item.toggle_status()

@dataclass
class EditTodoItem:
  todo_list: TodoList
  todo_item: TodoItem
  old_name: str = ""
  old_description: str = ""
  new_name: str = ""
  new_description: str = ""
  success: bool = False

  def execute(self) -> None:
    print("\nEDIT TASK:")
    self.new_name = input("\nEnter new task's name: ")
    
    if self.new_name in self.todo_list.get_data().keys():
      print("\nERROR: Task name must be unique!")
      input("Press Enter to continue...")
    else:
      self.new_description = input("Enter new task's description: ")
      self.old_name = self.todo_item.get_name()
      self.old_description = self.todo_item.get_description()
      self.todo_item.set_name(self.new_name)
      self.todo_item.set_description(self.new_description)
      self.success: bool = True

  def undo(self) -> None:
    if self.success:
      self.todo_item.set_name(self.old_name)
      self.todo_item.set_description(self.old_description)

  def redo(self) -> None:
    if self.success:
      self.todo_item.set_name(self.new_name)
      self.todo_item.set_description(self.new_description)
