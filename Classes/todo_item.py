from dataclasses import dataclass
from typing import Any

@dataclass
class TodoItem:
  name: str
  description: str
  status: bool = False
  
  def __str__(self) -> str:
    return f"Task: {self.name} | Description: {self.description} | Finished: {self.status}"
  
  def set_name(self, name: str) -> None:
    self.name = str(name)
  
  def set_description(self, description: str) -> None:
    self.description = str(description)

  def toggle_status(self) -> None:
    self.status = not self.status

  def set_status_finished(self) -> None:
    self.status = True

  def set_status_unfinished(self) -> None:
    self.status = False

  def get_name(self) -> str:
    return self.name
  
  def get_description(self) -> str:
    return self.description