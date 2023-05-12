from Classes.TodoItem import *
from dataclasses import dataclass, field

@dataclass
class TodoList:
  todo_list: dict[str, TodoItem] = field(default_factory=dict)
  temp_item_holder = None

  def createTodoItem(self, name: str, description: str) -> TodoItem:
    todo_item = TodoItem(name, description)
    return todo_item
  
  def addTodoItemToList(self, todo_item: TodoItem) -> None:
    self.todo_list[todo_item.name] = todo_item

  def removeTodoItem(self, todo_item: TodoItem) -> None:
    self.temp_item_holder = todo_item
    self.todo_list.pop(todo_item.name)

  def getTodoItem(self, item_name: str) -> TodoItem:
    return self.todo_list[item_name]