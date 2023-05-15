from Classes.todo_item import *
from dataclasses import dataclass, field

@dataclass
class TodoList:
  data: dict[str, TodoItem] = field(default_factory=dict)

  def create_item(self, name: str, description: str) -> TodoItem:
    item = TodoItem(name, description)
    return item
  
  def add_item(self, item: TodoItem) -> None:
    self.data[item.name] = item

  def remove_item(self, item: TodoItem) -> None:
    self.data.pop(item.name)

  def get_item(self, item_name: str) -> TodoItem:
    return self.data[item_name]
  
  def set_data(self, data: dict[str, TodoItem]) -> None:
    self.data = data

  def get_data(self) -> dict[str, TodoItem]:
    return self.data