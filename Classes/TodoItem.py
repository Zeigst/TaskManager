from dataclasses import dataclass
from typing import Any

@dataclass
class TodoItem:
  name: str
  description: str
  status: bool = False
  
  def __str__(self) -> str:
    return f"Task: {self.name} | Description: {self.description} | Finished: {self.status}"
  
  def setName(self, name: str) -> None:
    self.name = str(name)
  
  def setDescription(self, description: str) -> None:
    self.description = str(description)

  def toggleStatus(self) -> None:
    self.status = not self.status

  def setStatusFinished(self) -> None:
    self.status = True

  def setStatusUnfinished(self) -> None:
    self.status = False

  def getName(self) -> str:
    return self.name
  
  def getDescription(self) -> str:
    return self.description